"""Bounded audits of local stability; no enumeration or production imports.

Symbolic identities and Fraction sign gates audit the analytic proof.
70-digit atan root probes are diagnostics, never uniform certificates.
The two m=4 rational brackets deliberately reuse the prior exact checker.
Run from the repository root with python -B; no artifact is regenerated.
"""

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import runpy
import sys

import mpmath as mp
import sympy as sp


def exact_checks():
    radius, a, b = sp.symbols('R a b', positive=True)
    z = sp.sqrt(a*b/((radius+a)*(radius+b)))
    angle = 2*sp.asin(z)
    high_derivative = sp.sqrt(radius*a)/(
        sp.sqrt(b)*(radius+b)*sp.sqrt(radius+a+b))
    cross = sp.sqrt(radius)/(2*sp.sqrt(a*b)*(radius+a+b)**sp.Rational(3, 2))
    radial = z/sp.sqrt(1-z*z)*(1/(radius+a)+1/(radius+b))
    for expression in (
        sp.diff(angle, b)-high_derivative,
        sp.diff(high_derivative, a)-cross,
        -sp.diff(angle, radius)-radial,
    ):
        assert sp.simplify(expression) == 0
    print('PASS symbolic: high, cross and radial derivative identities')

    t = sp.symbols('t', nonnegative=True)
    m = t+4
    polynomial = sp.Poly(sp.expand(
        sp.Rational(3, 4)*m*m+(1-sp.Rational(22, 7))*m-sp.Rational(22, 7)), t)
    assert all(coefficient > 0 for coefficient in polynomial.all_coeffs())
    assert F(3, 2)**2 > 2
    assert F(16, 32**2)+F(5, 32) == F(11, 64) < F(1, 3)
    assert 3**3 < 6**2  # 3^(3/2)<6, with positive sides.
    assert F(7, 4) < 2
    print('PASS rational: lower-root polynomial coefficients='
          f'{polynomial.all_coeffs()}; m=32 chord gate=11/64<1/3; '
          'rate/sharpness constant gates')

    previous = Path(__file__).resolve().parent.parent / (
        'TASK-20260905__permuted_halves_root_search/check_roots.py')
    prior = runpy.run_path(str(previous), run_name='prior_rational_functions')
    tau = prior['tau_bounds']()
    assert 6 < tau[0] < tau[1] < F(44, 7)
    brackets = (
        ((8, 7, 5, 6), F('5.7677942845'), F('5.7677942846')),
        ((7, 8, 5, 6), F('5.7835600858'), F('5.7835600859')),
    )
    for p, lo, hi in brackets:
        assert prior['exact_score'](lo, p)[0] > tau[1]
        assert prior['exact_score'](hi, p)[1] < tau[0]
    _, al, ah = brackets[0]
    _, bl, bh = brackets[1]
    assert bl-ah == F('0.0157658012')
    assert bh-al == F('0.0157658014')
    print('PASS reused rational scorer: two m=4 root brackets, four signs; '
          '0.0157658012 < rho_B-rho_A < 0.0157658014')


def angle(radius, a, b):
    # Independent angular representation, not the asin derivative formula.
    return 2*mp.atan2(mp.sqrt(a*b), mp.sqrt(radius*(radius+a+b)))


def cell(radius, t, a, b):
    return max(angle(radius, t, a)+angle(radius, t, b), angle(radius, a, b))


def score(radius, p):
    # Read each low's actual neighbors from the full alternating cycle.
    cycle = [v for low, high in enumerate(p, 1) for v in (low, high)]
    return mp.fsum(cell(radius, cycle[i], cycle[i-1], cycle[i+1])
                   for i in range(0, len(cycle), 2))


@lru_cache(None)
def root(p):
    m = len(p)
    assert sorted(p) == list(range(m+1, 2*m+1))
    lo, hi = mp.mpf(1)/128, mp.mpf(2*m*m)
    assert score(lo, p) > 2*mp.pi > score(hi, p)
    for _ in range(240):
        middle = (lo+hi)/2
        if score(middle, p) > 2*mp.pi:
            lo = middle
        else:
            hi = middle
    assert hi-lo < mp.mpf('1e-65')
    value = (lo+hi)/2
    if m >= 3:
        lower = max(1, (m+1)*(1/mp.sin(mp.pi/m)-1))
        assert value >= lower
    if m >= 4:
        assert value > m*m/(4*mp.pi)
    return value


def swapped(p, j):
    q = list(p)
    k = (j+1) % len(p)
    q[j], q[k] = q[k], q[j]
    return tuple(q)


def numerical_checks():
    mp.mp.dps = 70
    guard = mp.mpf('1e-55')
    swaps = probes = 0
    biggest_ratio = mp.mpf(0)
    for m in (2, 3, 4, 8, 16, 32, 48, 64):
        highs = tuple(range(m+1, 2*m+1))
        prescribed = (highs, highs[::-1], highs[m//2:]+highs[:m//2])
        for p in dict.fromkeys(prescribed):
            rp = root(p)
            for j in sorted({0, m-2, m-1}):
                q = swapped(p, j)
                rq = root(q)
                x, y = p[j], p[(j+1) % m]
                u, v = p[j-1], p[(j+2) % m]
                for radius in (mp.mpf(1), rp, mp.mpf(2*m*m)):
                    delta = score(radius, q)-score(radius, p)
                    if m == 2:
                        assert abs(delta) < guard
                    else:
                        local = (cell(radius, j+1, u, y)-cell(radius, j+1, u, x)
                                 + cell(radius, (j+2) % m+1, x, v)
                                 - cell(radius, (j+2) % m+1, y, v))
                        assert abs(delta-local) < guard
                    bound = mp.sqrt(2)*abs(x-y)/radius
                    assert abs(delta) <= bound+guard
                    later = radius*mp.mpf('1.125')
                    assert score(later, p) <= (radius+2*m)/(later+2*m)*score(radius, p)+guard
                    probes += 1
                if m == 2:
                    assert abs(rp-rq) < guard
                else:
                    r = min(rp, rq)
                    bound = mp.sqrt(2)/(2*mp.pi)*(1+2*m/r)*abs(x-y)
                    assert abs(rp-rq) <= bound+guard
                    assert abs(rp-rq) <= 2*abs(x-y)+guard
                    biggest_ratio = max(biggest_ratio, abs(rp-rq)/bound)
                swaps += 1
        print(f'PASS numerical size m={m}: prescribed orders and cyclic boundary swaps', flush=True)

    print(f'PASS numerical: swaps={swaps}, score/contraction probes={probes}, '
          f'max root-change / bound={mp.nstr(biggest_ratio, 12)}')
    for m in (32, 48, 64):
        # A fixed interior shift, no optimization or scan over shifts.
        shift = max(1, m//10)
        highs = tuple(range(m+1, 2*m+1))
        p = highs[shift:]+highs[:shift]
        q = swapped(p, 0)
        drop = root(p)-root(q)
        bound = 3/(4*mp.pi*(m+1))*(1+8*mp.pi/m)
        assert 0 < drop < bound
        for order in (p, q):
            radius = root(order)
            for low in (1, 3):
                a, b = order[low-2], order[low-1]
                assert angle(radius, a, b) > angle(radius, low, a)+angle(radius, low, b)

        sharp = (m+2, 2*m, 2*m-1, *range(m+3, 2*m-1), m+1)
        changed = swapped(sharp, 0)
        linear_drop = root(sharp)-root(changed)
        lower = mp.mpf(m)/(12288*mp.pi)
        assert linear_drop > lower
        print(f'PASS numerical m={m}: shift drop={mp.nstr(drop, 14)}, '
              f'O(1/m) bound={mp.nstr(bound, 14)}; '
              f'sharp-family drop/m={mp.nstr(linear_drop/m, 14)}')
    print(f'PASS bounded audit: distinct roots={root.cache_info().currsize}; '
          '70 digits, 240 bisections, guard=1e-55; no enumeration')


if __name__ == '__main__':
    print(f'Python {sys.version.split()[0]}; mpmath {mp.__version__}; sympy {sp.__version__}')
    exact_checks()
    numerical_checks()
