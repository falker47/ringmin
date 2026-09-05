"""Bounded audit of the three-marginal proof; no production imports/search.

The universal result is the analytic proof in the research note. Exact
symbolic/rational gates audit its algebra and affine marginal maps.
70-digit alternate-angle/root/integral diagnostics are observations only.
Run with --exact-only to omit every floating calculation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q

import mpmath as mp
import sympy as sp


def exact_gates():
    ell = Q(1, 4)
    assert ell < Q(1, 2)
    assert Q(3, 4)**2 <= 1 - Q(1, 2)**2
    assert Q(3, 4) * Q(7, 4) > 1
    assert 2 * Q(1, 2) == 1  # 2 sqrt(t)<=1 on t<=1/4
    assert ell**3 / (24 * Q(13, 8)) == Q(1, 2496)
    assert 4 * 2496 == 9984

    t, alpha, u, length, midpoint = sp.symbols(
        "t alpha u length midpoint", positive=True
    )
    aa = 1 + alpha
    mm = aa + length / 2
    assert sp.expand((aa + t) * (aa + length - t)
                     - (mm**2 - (t - length / 2)**2)) == 0
    assert sp.integrate(u**2 / (2 * midpoint),
                        (u, -length / 2, length / 2)) == length**3 / (24 * midpoint)
    assert sp.integrate(aa + t, (t, 0, length)) == length * aa + length**2 / 2
    v = sp.symbols("v", positive=True)
    assert sp.expand((midpoint-v)*(midpoint+v)
                     - (midpoint**2-v**2)) == 0

    # Exact affine pushforward maps: endpoints and |Jacobian|, not moments.
    forward, reflected = aa + t, aa + length - t
    assert forward.subs(t, 0) == reflected.subs(t, length) == aa
    assert forward.subs(t, length) == reflected.subs(t, 0) == aa + length
    assert sp.diff(forward, t) == 1 and sp.diff(reflected, t) == -1
    before, after, wrap = aa + t, alpha + t, 1 - alpha
    assert sp.simplify(before.subs(t, wrap)) == 2
    assert sp.simplify(after.subs(t, wrap)) == 1
    assert after.subs(t, 1) == before.subs(t, 0) == aa
    assert sp.diff(before, t) == sp.diff(after, t) == 1
    assert Q(1, 2) + Q(1, 2) == 1

    # Independent differentiation of the segment used in the denominator bound.
    q, a, b = sp.symbols("q a b", positive=True)
    ff = ((1+q*a)*(1+q*b))**(-sp.Rational(1, 2))
    target = -ff/2 * (a/(1+q*a) + b/(1+q*b))
    assert sp.simplify(sp.diff(ff, q) - target) == 0
    z = sp.symbols("z", real=True)
    radical = sp.sqrt(1-z*z)
    assert sp.simplify((1/radical-1)*radical*(1+radical)-z*z) == 0

    # Check the two branches' exact leading normalization R=4*c*m^2.
    c, m, low, x, y = sp.symbols("c m low x y", positive=True)
    adjacent = 2*(sp.sqrt((m*low)*(m*x))+sp.sqrt((m*low)*(m*y)))/(4*c*m*m)
    chord = 2*sp.sqrt((m*x)*(m*y))/(4*c*m*m)
    assert sp.simplify(adjacent - sp.sqrt(low)*(sp.sqrt(x)+sp.sqrt(y))/(2*c*m)) == 0
    assert sp.simplify(chord-sp.sqrt(x*y)/(2*c*m)) == 0
    error = 1/(2*c*c*m*m)+1/(12*c**3*m**3)
    assert sp.simplify(2*m*error - (1/(c*c*m)+1/(6*c**3*m*m))) == 0
    print("PASS exact: scalar guards, reflection saving >1/2496, coefficient denominator 9984*pi")
    print("PASS exact: affine marginal endpoints/Jacobians and split shift image")
    print("PASS exact: denominator/asin identities and cell/score normalization")


def prescribed_orders(m):
    highs = tuple(range(m+1, 2*m+1))
    shift = (107*m)//1000
    shifted = highs[shift:] + highs[:shift]
    zigzag = tuple(value for pair in zip(highs, reversed(highs)) for value in pair)
    # Take each high once in the deterministic alternating-extremes list.
    zigzag = tuple(dict.fromkeys(zigzag))
    return tuple(dict.fromkeys((highs, tuple(reversed(highs)), shifted, zigzag)))


def angular_atan(a, b, radius):
    """Half-angle atan formula, independent of the expansion's asin form."""
    return 2*mp.atan(mp.sqrt(mp.mpf(a)*b/(radius*(radius+a+b))))


def direct_cells(order, radius):
    return [max(angular_atan(i, order[i-2], radius)
                + angular_atan(i, order[i-1], radius),
                angular_atan(order[i-2], order[i-1], radius))
            for i in range(1, len(order)+1)]


def g(t, x, y):
    return max(mp.sqrt(t)*(mp.sqrt(x)+mp.sqrt(y)), mp.sqrt(x*y))


def leading_cells(order):
    mm = mp.mpf(len(order))
    return [g(i/mm, order[i-2]/mm, order[i-1]/mm)
            for i in range(1, len(order)+1)]


def root_atan(order):
    lower, upper = mp.mpf(0), 2*mp.mpf(len(order))**2
    assert mp.fsum(direct_cells(order, upper)) < 2*mp.pi
    for _ in range(240):
        mid = (lower+upper)/2
        if mp.fsum(direct_cells(order, mid)) > 2*mp.pi:
            lower = mid
        else:
            upper = mid
    result = (lower+upper)/2
    assert abs(mp.fsum(direct_cells(order, result))-2*mp.pi) < mp.mpf("1e-55")
    return result


def finite_diagnostics():
    guard = mp.mpf("1e-55")
    orders = probes = checked_cells = root_checks = 0
    largest_ratio = mp.mpf(0)
    for m in (2, 3, 4, 8, 16, 32, 64, 128):
        for order in prescribed_orders(m):
            orders += 1
            assert sorted(order) == list(range(m+1, 2*m+1))
            gg = leading_cells(order)
            average = mp.fsum(gg)/m
            assert 1 <= average <= 2*mp.sqrt(2)

            # Exact empirical high marginals and cyclic seam telescoping.
            xx = [Q(order[i-2], m) for i in range(1, m+1)]
            yy = [Q(order[i-1], m) for i in range(1, m+1)]
            assert sorted(xx) == sorted(yy) == [Q(j, m) for j in range(m+1, 2*m+1)]
            lhs = sum((Q(i, m)*(xx[i-1]**2-yy[i-1]**2)
                       for i in range(1, m+1)), Q(0))/m
            rhs = (sum((yy[j]**2/m for j in range(m-1)), Q(0))
                   + (Q(1, m)-1)*yy[-1]**2)/m
            assert lhs == rhs and abs(lhs) <= Q(12, m)

            for c in (mp.mpf(1)/10, mp.mpf(1)/7, mp.mpf(1)/5):
                if m*c < 1:
                    continue  # Explicit domain of the small-angle bound.
                cells = direct_cells(order, 4*c*m*m)
                ee = 1/(2*c*c*m*m)+1/(12*c**3*m**3)
                for actual, leading in zip(cells, gg):
                    difference = abs(actual-leading/(2*c*m))
                    assert difference <= 2*ee + guard
                    largest_ratio = max(largest_ratio, difference/(2*ee))
                    checked_cells += 1
                assert abs(mp.fsum(cells)-average/(2*c)) <= 2*m*ee+guard
                probes += 1

            rho = root_atan(order)
            coefficient = rho/(4*m*m)
            cmin, cmax = 1/(8*mp.pi), 1/mp.pi
            if m >= 32:
                assert cmin < coefficient < cmax
                ee = 1/(cmin*cmin*m)+1/(6*cmin**3*m*m)
                assert abs(coefficient-average/(4*mp.pi)) <= ee/(2*mp.pi**2)+guard
            root_checks += 1
    print(f"PASS bounded: {orders} prescribed orders; exact empirical marginal/seam identities")
    print(f"PASS bounded: {probes} score probes, {checked_cells} cells; max error/bound={mp.nstr(largest_ratio, 16)}")
    print(f"PASS bounded: {root_checks} alternate-atan full roots; residual <1e-55")
    print("NOTE: finite root/score probes corroborate, but do not prove, the uniform limit")


def integral_diagnostics():
    # Locate only the one-dimensional shift critical point for diagnostics.
    # This is not a search over measures or permutations.
    def derivative(alpha):
        aa, bb = (1+alpha)/3, 1-alpha
        return (aa/2 + mp.quad(lambda t: mp.sqrt(t/(t+1+alpha)), [aa, bb])/2
                + mp.quad(lambda t: mp.sqrt(t/(t+alpha)), [bb, 1])/2
                - (mp.sqrt(2)-1)*mp.sqrt(bb))

    alpha = mp.findroot(derivative, (mp.mpf("0.10"), mp.mpf("0.12")))
    assert 0 < alpha < mp.mpf(1)/2
    assert abs(derivative(alpha)) < mp.mpf("1e-60")
    ell, aa = mp.mpf(1)/4, 1+alpha
    midpoint = aa+ell/2
    switch, wrap = aa/3, 1-alpha

    # Split every active-branch switch and the high wrap explicitly.
    baseline = (mp.quad(lambda t: aa+t, [0, switch])
                + mp.quad(lambda t: 2*mp.sqrt(t*(aa+t)), [switch, wrap])
                + mp.quad(lambda t: 2*mp.sqrt(t*(alpha+t)), [wrap, 1]))
    reflected_block = mp.quad(lambda t: g(t, aa+t, aa+ell-t), [0, ell])
    unchanged = (mp.quad(lambda t: aa+t, [ell, switch])
                 + mp.quad(lambda t: 2*mp.sqrt(t*(aa+t)), [switch, wrap])
                 + mp.quad(lambda t: 2*mp.sqrt(t*(alpha+t)), [wrap, 1]))
    reflected = reflected_block+unchanged
    saved = mp.quad(lambda u: u*u/(midpoint+mp.sqrt(midpoint*midpoint-u*u)),
                    [-ell/2, 0, ell/2])
    assert abs((baseline-reflected)-saved) < mp.mpf("1e-60")
    assert saved > ell**3/(24*midpoint) > mp.mpf(1)/2496
    # Independent closed antiderivative for the reflected semicircle integral.
    closed_block = ell*mp.sqrt(aa*(aa+ell))/2 + midpoint**2*mp.asin(ell/(2*midpoint))
    assert abs(reflected_block-closed_block) < mp.mpf("1e-60")
    print("DIAGNOSTIC alpha_*=" + mp.nstr(alpha, 30))
    print("DIAGNOSTIC 4*pi*C_shift=" + mp.nstr(baseline, 30))
    print("DIAGNOSTIC reflected cost=" + mp.nstr(reflected, 30))
    print("DIAGNOSTIC saved cost=" + mp.nstr(saved, 30))
    print("DIAGNOSTIC reflected cost/(4*pi)=" + mp.nstr(reflected/(4*mp.pi), 30))
    print("PASS bounded: split direct integral, rationalized saving and closed block agree <1e-60")
    print("NOTE: reflected cost is a feasible relaxation cost, not the relaxation minimum or a geometric bound")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-only", action="store_true")
    args = parser.parse_args()
    exact_gates()
    if not args.exact_only:
        mp.mp.dps = 70
        finite_diagnostics()
        integral_diagnostics()


if __name__ == "__main__":
    main()
