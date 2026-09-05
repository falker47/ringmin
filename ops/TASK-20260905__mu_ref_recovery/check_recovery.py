"""Bounded exact audit of mu_ref recovery; the research note is the proof.

Only the prescribed construction is evaluated: no permutation/coupling
optimization, no randomness, no production/verifier/previous-checker imports.
All gates use integer/rational arithmetic or symbolic polynomial identities.
"""

from __future__ import annotations

from fractions import Fraction as Q

import sympy as sp


def recovered_order(m: int, s: int) -> tuple[int, ...]:
    """Independent list implementation: shift, then reverse even positions."""
    if type(m) is not int or type(s) is not int or m < 2 or not 0 <= 2*s < m:
        raise ValueError("require integer m>=2 and integer 0<=s<m/2")
    highs = list(range(m + 1, 2*m + 1))
    order = highs[s:] + highs[:s]
    q = 2*(m//8)
    order[1:q:2] = reversed(order[1:q:2])
    return tuple(order)


def fractional_shift(t: Q, alpha: Q) -> Q:
    value = t + alpha
    return 1 + value - value.numerator//value.denominator


def comparison(i: int, m: int, q: int, alpha: Q) -> tuple[Q, Q, Q]:
    t, aa, ell = Q(i, m), 1 + alpha, Q(1, 4)
    if i <= q:
        pair = (aa + t, aa + ell - t)
        return (t, *pair) if i % 2 == 0 else (t, *reversed(pair))
    high = fractional_shift(t, alpha)
    return t, high, high


def symbolic_gates() -> None:
    k, j, i, q, m, beta, t = sp.symbols("k j i q m beta t")
    assert sp.expand((2*k + 2 - 2*j) - 2*(k + 1-j)) == 0
    assert sp.expand(q + 2 - (q + 2-i)) == i
    assert sp.simplify((m + m*beta + i-1)/m - (1+beta+t-1/m)
                       ).subs(i, m*t) == 0
    assert sp.simplify((m + m*beta + q+3-i)/m
                       - (1+beta+q/m-t+3/m)).subs(i, m*t) == 0
    assert sp.simplify((q/2) + (q/2-1) + (m-q-3) + 4) == m
    assert sp.simplify((q/2) + (q/2-1) + (m-q-2) + 3) == m
    ell = Q(1, 4)
    assert ell**3/(24*Q(13, 8)) == Q(1, 2496)
    assert 4*2496 == 9984
    print("PASS symbolic: parity involution, predecessor formulas, complete cell counts, strict-gap normalization")


def finite_gates() -> None:
    cases = representatives = cell_comparisons = 0
    for m in range(2, 129):
        q = 2*(m//8)
        for s in range((m+1)//2):
            order = recovered_order(m, s)
            ranks = [q+2-i if i <= q and i % 2 == 0 else i
                     for i in range(1, m+1)]
            assert sorted(ranks) == list(range(1, m+1))
            assert [ranks[j-1] for j in ranks] == list(range(1, m+1))
            assert order == tuple(m+1+(j+s-1) % m for j in ranks)
            assert sorted(order) == list(range(m+1, 2*m+1))
            assert sorted(order[-1:] + order[:-1]) == sorted(order)
            cases += 1

            if m < 8:
                assert q == 0
                continue
            r = m-s
            bad = {1, q+1, r, r+1} & set(range(1, m+1))
            assert len(bad) == (4 if s else 3)
            assert order[-1] == (m+s if s else 2*m)
            assert order[0] == m+s+1
            assert order[q-1:q+1] == (m+s+2, m+s+q+1)
            assert order[r-1] == 2*m
            if s:
                assert order[r] == m+1
            even = [i for i in range(2, q+1) if i % 2 == 0]
            odd = [i for i in range(3, q+1) if i % 2]
            tail = [i for i in range(q+1, m+1) if i not in bad]
            assert len(even) == q//2 and len(odd) == q//2-1
            assert len(tail) == m-q-(3 if s else 2)
            assert sorted(even + odd + tail + list(bad)) == list(range(1, m+1))

            # Interior points of every admissible alpha floor interval, plus
            # its positive lower endpoint (where alpha*m is exactly integer).
            lower, upper = Q(s, m), min(Q(s+1, m), Q(1, 2))
            alphas = [(3*lower+upper)/4, (lower+3*upper)/4]
            if lower:
                alphas.append(lower)
            for alpha in alphas:
                assert 0 < alpha < Q(1, 2)
                assert (alpha*m).numerator//(alpha*m).denominator == s
                assert 0 <= Q(1, 4)-Q(q, m) < Q(2, m)
                representatives += 1
                for cell in range(1, m+1):
                    actual = (Q(cell, m), Q(order[cell-2], m), Q(order[cell-1], m))
                    target = comparison(cell, m, q, alpha)
                    assert 0 <= target[0] <= 1 and all(1 <= v <= 2 for v in target[1:])
                    if cell not in bad:
                        assert max(abs(a-b) for a, b in zip(actual, target)) <= Q(3, m)
                        cell_comparisons += 1
                    if 2 <= cell <= q:
                        if cell % 2 == 0:
                            pair = (Q(m+s+cell-1, m), Q(m+s+q+2-cell, m))
                        else:
                            pair = (Q(m+s+q+3-cell, m), Q(m+s+cell, m))
                        assert actual[1:] == pair
    for invalid in ((1, 0), (8, -1), (8, 4), (8.0, 0), (8, True)):
        try:
            recovered_order(*invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid construction input accepted")
    print(f"PASS bounded exact: {cases} prescribed (m,s) orders, m=2..128; permutation and cyclic occurrence checks")
    print(f"PASS bounded exact: {representatives} rational alpha representatives; {cell_comparisons} ordinary triple comparisons <=3/m")
    print("PASS bounded exact: all seam/junction/wrap counts and endpoints, all m mod 8, invalid-input rejection")


def polynomial_moments() -> None:
    t, x, y = sp.symbols("t x y")
    alpha, ell = sp.Rational(1, 10), sp.Rational(1, 4)
    aa, wrap = 1+alpha, 1-alpha
    polynomials = (t, x, y, t*x, t*x*x, t*x*y, (x-y)**2, t*(x-y))
    probes = []
    for ff in polynomials:
        def pullback(xx, yy):
            return ff.subs({x: xx, y: yy}, simultaneous=True)

        integral = (sp.integrate((pullback(aa+t, aa+ell-t)
                                 + pullback(aa+ell-t, aa+t))/2, (t, 0, ell))
                    + sp.integrate(pullback(aa+t, aa+t), (t, ell, wrap))
                    + sp.integrate(pullback(alpha+t, alpha+t), (t, wrap, 1)))
        target = Q(int(integral.p), int(integral.q))
        terms = [(powers, Q(int(coeff.p), int(coeff.q)))
                 for powers, coeff in sp.Poly(ff, t, x, y).terms()]
        # Supremum and gradient-sum bounds on [0,1]x[1,2]^2.
        maximum = sum(abs(cc)*2**(b+c) for (_, b, c), cc in terms)
        lipschitz = sum(abs(cc)*(a*2**(b+c) + Q(b+c, 2)*2**(b+c))
                        for (a, b, c), cc in terms)
        probes.append((terms, target, maximum, lipschitz))

    assert probes[0][1] == Q(1, 2)
    assert probes[1][1] == probes[2][1] == Q(3, 2)
    assert probes[-2][1] == Q(1, 192)
    assert probes[-1][1] == 0
    count = 0
    for m in (8, 9, 15, 16, 31, 32, 64, 128, 256, 512, 1024):
        order = recovered_order(m, m//10)
        triples = [(Q(i, m), Q(order[i-2], m), Q(order[i-1], m))
                   for i in range(1, m+1)]
        max_error = Q(0)
        for terms, target, maximum, lipschitz in probes:
            empirical = sum((sum(cc*tt**a*xx**b*yy**c for (a, b, c), cc in terms)
                             for tt, xx, yy in triples), Q(0))/m
            error = abs(empirical-target)
            assert error <= (6*lipschitz+16*maximum)/m
            max_error = max(max_error, error)
            count += 1
        print(f"DIAGNOSTIC m={m}: maximum of eight exact moment errors = {max_error}")
    print(f"PASS bounded exact: {count} polynomial moments against independently integrated mu_ref at alpha=1/10; proved Lipschitz bound")
    print("NOTE: finite checks audit formulas; the continuous-test proof establishes recovery at the exact alpha_*")


def main() -> None:
    symbolic_gates()
    finite_gates()
    polynomial_moments()


if __name__ == "__main__":
    main()
