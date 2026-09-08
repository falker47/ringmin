"""Bounded corroboration; the analytic proof supplies all limit quantifiers.

Default: exact integers/Fractions, N=4..96 at k=1,7,23, every proper
terminal restriction with at least three survivors. No tour optimization.
--symbolic: independent derivative/primitive identities with SymPy.
--diagnostic: 28 prescribed floating-point chain roots, never certificates.
No production imports, saved results, random seeds or implicit exact floors.
"""

import argparse
from collections import Counter
from fractions import Fraction as Q
from math import factorial


def supnick(k, n):
    size = n - k + 1
    if k < 1 or size < 3:
        raise ValueError("positive integer radii and at least three vertices required")
    middle = (size + 1) // 2
    arms = []
    for parity in (1, 2):
        arm = []
        for low in range(parity, middle + 1, 2):
            arm.append(low)
            high = size - low
            if high > middle:
                arm.append(high)
        arms.append(arm)
    return tuple(k + j - 1 for j in arms[0] + arms[1][::-1] + [size])


def edges(tour):
    assert len(tour) == len(set(tour)) >= 3
    return Counter(tuple(sorted(pair))
                   for pair in zip(tour, tour[1:] + tour[:1]))


def below_edges(k, n, ell):
    size = n - k + 1
    h, odd = divmod(size, 2)
    d = ell - k
    assert 1 <= d <= h - 1
    pairs = [(i, n + k - 1 - i) for i in range(ell, k + h - 1 + odd)]
    pairs += [(i, n + k + 1 - i) for i in range(ell, k + h + odd)]
    if not odd:
        pairs.append((k + h - 1, k + h))
    assert len(pairs) == size - 2 * d
    pairs.append((n - 1, n))
    pairs += [(n - j, n + 2 - j) for j in range(2, d + 1)]
    assert len(pairs) == size - d
    return Counter(tuple(sorted(pair)) for pair in pairs)


def above_edges(ell, n):
    return Counter([(a, a + 2) for a in range(ell, n - 1)]
                   + [(ell, ell + 1), (n - 1, n)])


def exact_checks():
    cases = early = late = transition = 0
    parities = set()
    for k in (1, 7, 23):
        for size in range(4, 97):
            n = k + size - 1
            tour = supnick(k, n)
            assert set(tour) == set(range(k, n + 1))
            h = size // 2
            ell_0 = k + (size + 1) // 2
            for ell in range(k + 1, n - 1):
                d = ell - k
                restricted = tuple(a for a in tour if a >= ell)
                actual = edges(restricted)
                assert len(actual) == n - ell + 1
                assert all(count == 1 for count in actual.values())
                assert edges(restricted[1:] + restricted[:1]) == actual
                assert edges(restricted[::-1]) == actual
                parities.add((size % 2, len(restricted) % 2))
                if d <= h - 1:
                    expected = below_edges(k, n, ell)
                    early += 1
                    # All deleted low vertices are independent in the old cycle.
                    for a, b in edges(tour):
                        assert not (a < ell and b < ell)
                elif ell >= ell_0:
                    expected = above_edges(ell, n)
                    late += 1
                else:
                    # The omitted middle case is at most one vertex from (10).
                    if n - ell_0 + 1 >= 3:
                        reference = edges(tuple(a for a in tour if a >= ell_0))
                        assert reference == above_edges(ell_0, n)
                        changed = sum((actual - reference).values())
                        changed += sum((reference - actual).values())
                        assert changed <= 3 * abs(ell - ell_0)
                    transition += 1
                    cases += 1
                    continue
                assert actual == expected
                # Omitting the cyclic high seam must be detected in either regime.
                wrong = expected.copy()
                wrong.subtract({(n - 1, n): 1})
                assert actual != +wrong
                cases += 1
    assert parities == {(0, 0), (0, 1), (1, 0), (1, 1)}
    print(f"PASS exact arcs: {cases} restrictions; {early} below, {late} above, "
          f"{transition} middle; all four parity pairs; rotations/reversals.")
    print("PASS exact negative controls: omitted top seam rejected in both regimes.")

    a, b = Q(73, 100), Q(3, 4)
    cos_lower = sum((-1)**j * a**(2*j) / factorial(2*j) for j in range(4))
    cos_upper = sum((-1)**j * b**(2*j) / factorial(2*j) for j in range(3))
    sin_lower = sum((-1)**j * a**(2*j+1) / factorial(2*j+1) for j in range(4))
    sin_upper = sum((-1)**j * b**(2*j+1) / factorial(2*j+1) for j in range(3))
    gates = (cos_lower - a, b - cos_upper,
             sin_lower - Q(2, 3), Q(7, 10) - sin_upper)
    expected = (Q(10924138073711, 720000000000000), Q(37, 2048),
                Q(102214670540903, 504000000000000000), Q(751, 40960))
    assert gates == expected and all(gate > 0 for gate in gates)
    for index, gate in enumerate(gates, 1):
        print(f"PASS rational Taylor gate {index}: {gate} > 0")
    transform = lambda u: (1-u)/(1+u)
    assert transform(Q(7, 10)) == Q(3, 17)
    assert transform(Q(2, 3)) == Q(1, 5)
    assert (1+Q(3, 17))/5 == Q(4, 17)
    assert Q(4, 17)-Q(23, 100) == Q(9, 1700) > 0
    print("PASS rational interval implications: 3/17<q_*<1/5; "
          "(1+q_*)/5>4/17>23/100, margin 9/1700.")


def symbolic_checks():
    import sympy as sp

    s, x = sp.symbols("s x", positive=True)
    # Independent antiderivative of sqrt(x*(s-x)); s/2 centered coordinates.
    primitive = ((x-s/2)*sp.sqrt(x*(s-x))/2
                 + s**2*sp.asin(2*x/s-1)/8)
    derivative = sp.diff(primitive, x)
    # The only radical rewrite is valid on the stated domain 0<x<s.
    derivative = derivative.subs(sp.sqrt(1-(2*x/s-1)**2),
                                 2*sp.sqrt(x*(s-x))/s)
    assert sp.simplify(derivative-sp.sqrt(x*(s-x))) == 0
    chord_derivative = sp.diff((1-(s-x)**2)/2, x)
    assert sp.simplify(chord_derivative-(s-x)) == 0
    # Squaring comparison uses strictly positive sides in the analytic proof.
    assert sp.expand((s-x)-4*x) == s-5*x
    assert sp.simplify(((1-(s-x)**2)/2).subs(x, s/2)
                       - ((1-x*x)/2).subs(x, s/2)) == 0
    q, beta = sp.symbols("q beta", positive=True)
    assert sp.simplify(sp.integrate(1-x, (x, 0, beta-q))
                       - (1-(1+q-beta)**2)/2) == 0
    print("PASS symbolic: primitive, chord derivative, sign identity, "
          "midpoint continuity, replacement-chord integral (5 identities).")


def diagnostic():
    import math
    import mpmath as mp

    mp.mp.dps = 50
    tau = mp.findroot(lambda t: mp.cos(t)-t, (mp.mpf('.73'), mp.mpf('.75')))
    qstar = (1-mp.sin(tau))/(1+mp.sin(tau))
    cterm = tau/(mp.pi*(1+mp.sin(tau)))

    def coefficient(q, beta):
        s = 1+q
        if 2*beta >= s:
            return (1-beta**2)/(2*mp.pi)
        return (2*mp.quad(lambda x: mp.sqrt(x*(s-x)), [beta, s/2])
                + (1-(s-beta)**2)/2)/mp.pi

    parameters = ((mp.mpf('.1'), mp.mpf('.3')),
                  (mp.mpf('.2'), mp.mpf('.6')),
                  (mp.mpf('.2'), mp.mpf('.8')),
                  (mp.mpf(2)/3, mp.mpf(3)/4),
                  (qstar, mp.mpf(1)/5), (qstar, mp.mpf(23)/100),
                  (qstar, (1+qstar)/5))
    largest_error = 0.0
    parities = set()
    cases = 0
    print("DIAGNOSTIC only: implicit q_* floors are high-precision observations.")
    for q, beta in parameters:
        psi = coefficient(q, beta)
        errors = []
        for n in (256, 257, 1024, 1025):
            k, ell = int(mp.floor(q*n)), int(mp.floor(beta*n))
            tour = tuple(a for a in supnick(k, n) if a >= ell)
            pairs = tuple(edges(tour).elements())
            products = [(math.sqrt(a*b), a+b) for a, b in pairs]
            weight = math.fsum(p for p, _ in products)
            lo, hi = max(1e-12, weight/math.pi-n), weight/math.pi
            # Alternate atan kernel; no production root or formula import.
            for _ in range(64):
                radius = (lo+hi)/2
                closure = 2*math.fsum(math.atan(p/math.sqrt(radius*(radius+t)))
                                      for p, t in products)
                if closure > 2*math.pi:
                    lo = radius
                else:
                    hi = radius
            radius = (lo+hi)/2
            asin_closure = 2*math.fsum(math.asin(math.sqrt(a*b/((radius+a)*(radius+b))))
                                      for a, b in pairs)
            assert abs(asin_closure-2*math.pi) < 2e-12
            error = radius/(n*n)-float(psi)
            # A diagnostic sanity guard, not the analytic error constant.
            assert abs(error) < 4/n
            errors.append(error)
            largest_error = max(largest_error, abs(error))
            parities.add(((n-k+1) % 2, len(tour) % 2))
            cases += 1
        print(f"DIAGNOSTIC q={float(q):.9f} beta={float(beta):.9f} "
              f"Psi={float(psi):.12f} errors="
              + ",".join(f"{error:.3e}" for error in errors))
    assert len(parities) == 4
    print(f"PASS diagnostic: {cases} prescribed roots; alternate-angle agreement "
          f"<2e-12; all parity pairs; max normalized error {largest_error:.3e}.")
    print(f"DIAGNOSTIC C_term={float(cterm):.12f}; "
          f"Psi(q_*,1/5)-C_term={float(coefficient(qstar,mp.mpf(1)/5)-cterm):.12g}; "
          f"Psi(q_*,23/100)-C_term={float(coefficient(qstar,mp.mpf(23)/100)-cterm):.12g}.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O: exact audit assertions must be enabled")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbolic", action="store_true")
    parser.add_argument("--diagnostic", action="store_true")
    args = parser.parse_args()
    exact_checks()
    if args.symbolic:
        symbolic_checks()
    if args.diagnostic:
        diagnostic()
