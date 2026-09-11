"""Bounded exact support for the optimized midpoint split, Sections 11-12.

Only standard-library arithmetic: polynomial coefficients, rational Taylor
gates, 80 terms in the endpoint z-integral with a proved tail, and cubic
signs. No production/prior-checker imports, saved artifacts, tour samples,
floating quadrature, or geometric certification. Run with python -I.
"""

from fractions import Fraction as F
from math import factorial


TAU = tuple(map(F, (
    "0.7390851332151606416553120876738734040134",
    "0.7390851332151606416553120876738734040135")))
Q = tuple(map(F, (
    "0.1950200913506069300798071259134151019366",
    "0.1950200913506069300798071259134151019367")))
PI = tuple(map(F, (
    "3.1415926535897932384626433832795028841971",
    "3.1415926535897932384626433832795028841972")))
T_TEXT = ("0.0092836183568361125168565556",
          "0.0092836183568361125168565557")
ETA_TEXT = ("2.546841764900829732093748e-7",
            "2.546841764900829732093749e-7")
TOTAL_TEXT = ("0.1405693355294332566284894404",
              "0.1405693355294332566284894405")
A_TEXT = ("2.592952349827745447477519",
          "2.592952349827745447477520")


def add(*polynomials):
    """Sparse exact polynomials in two formal variables (r,t)."""
    result = {}
    for polynomial in polynomials:
        for degree, value in polynomial.items():
            result[degree] = result.get(degree, 0) + value
    return {degree: value for degree, value in result.items() if value}


def scale(polynomial, factor):
    return {degree: factor * value for degree, value in polynomial.items()
            if factor * value}


def mul(left, right):
    return add(*({(i + k, j + ell): a * b}
                 for (i, j), a in left.items()
                 for (k, ell), b in right.items()))


def derivative(polynomial, coordinate):
    result = {}
    for degree, value in polynomial.items():
        if degree[coordinate]:
            reduced = list(degree)
            reduced[coordinate] -= 1
            result[tuple(reduced)] = degree[coordinate] * value
    return result


def identities():
    one, r, t = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
    # After u=2h/E^(1/3), multiply the split difference by u>0:
    # u^3-3u+2=(u-1)^2(u+2). u is the second formal variable.
    t_minus_one = add(t, scale(one, -1))
    assert mul(mul(t_minus_one, t_minus_one), add(t, scale(one, 2))) == {
        (0, 3): 1, (0, 1): -3, (0, 0): 2}
    assert 4 * F(1, 2)**2 + 1 / F(1, 2) == 3
    assert 54 * 8 == 432 and 2 * 3 * 4 == 24  # 8^(2/3)=4
    assert 4**3 == 8**2

    difference = add(r, scale(t, -1))
    sum1 = add(r, t)
    sum2 = add(mul(r, r), mul(r, t), mul(t, t))
    # Substitute d=432r^3+24r^2 into g(t)-r^3.
    assert mul(difference, add(scale(sum1, 24), scale(sum2, 431))) == {
        (3, 0): 431, (2, 0): 24, (0, 3): -431, (0, 2): -24}
    assert mul(difference, sum2) == {(3, 0): 1, (0, 3): -1}

    # Derive m'(d)=3t/(48+1296t) by cross multiplication.
    p = {(0, 3): 432, (0, 2): 24}
    denominator = add(scale(one, 48), scale(t, 1296))
    assert mul(derivative({(0, 3): 1}, 1), denominator) == mul(
        scale(t, 3), derivative(p, 1))
    # Derivative numerator for 3t/(48+1296t) is the positive constant 144.
    assert add(scale(denominator, 3), scale(t, -3 * 1296)) == scale(one, 144)
    # Convexity/secant identity, valid as a polynomial, including t=0,r=t.
    secant = add(
        mul(scale(r, 3), add(scale(sum1, 24), scale(sum2, 432))),
        scale(mul(add(scale(one, 48), scale(r, 1296)), sum2), -1))
    assert secant == scale(mul(difference, add(r, scale(t, 2))), 24)
    assert add({(0, 3): 432, (0, 2): 40}, scale(p, -1)) == {(0, 2): 16}
    print("PASS exact identities: split, E-to-e, scalar crossing, inverse derivative, secant, improvement")


def parameters():
    def trig(x, terms, odd):
        return sum((F((-1)**j, factorial(2*j + odd)) * x**(2*j + odd)
                    for j in range(terms)), F(0))

    assert 0 < TAU[0] < TAU[1] < 1
    assert trig(TAU[0], 42, 0) > TAU[0]  # degree 82, lower cosine
    assert trig(TAU[1], 41, 0) < TAU[1]  # degree 80, upper cosine
    sin_lo, sin_hi = trig(TAU[0], 42, 1), trig(TAU[1], 41, 1)
    assert 0 < sin_lo < sin_hi < 1
    assert Q[0] < (1-sin_hi)/(1+sin_hi) < (1-sin_lo)/(1+sin_lo) < Q[1]

    def atan(x, terms):
        return sum((F((-1)**j, 2*j+1) * x**(2*j+1)
                    for j in range(terms)), F(0))

    tangent = F(1, 5)
    for _ in range(2):
        tangent = 2*tangent/(1-tangent*tangent)
    assert tangent == F(120, 119)
    assert (tangent-F(1, 239))/(1+tangent/F(239)) == 1
    pi_lo = 16*atan(F(1, 5), 42) - 4*atan(F(1, 239), 41)
    pi_hi = 16*atan(F(1, 5), 41) - 4*atan(F(1, 239), 42)
    assert PI[0] < pi_lo < pi_hi < PI[1]
    print("PASS rational input gates: tau, q, pi")


def integral_bounds():
    """Endpoint expansion of Section 9, unlike the previous midpoint checker.

    With z=(s-2x)/s, integrate 1-sum c_j*z^(2j) exactly.
    The omitted positive tail is bounded by its largest value at z_q,
    interval length, and the geometric sum. All term counts are fixed.
    """
    q, beta = Q[0], F(23, 100)
    s = 1+q
    zq, zb = (1-q)/s, (s-2*beta)/s
    assert 0 < zb < zq < 1
    primitive, coefficient = zq-zb, F(1, 2)
    for j in range(1, 81):
        primitive -= coefficient * (zq**(2*j+1)-zb**(2*j+1))/(2*j+1)
        next_coefficient = coefficient * F(2*j-1, 2*(j+1))
        assert 0 < next_coefficient < coefficient
        coefficient = next_coefficient
    factor = s*s/4
    tail = factor*(zq-zb)*coefficient*zq**162/(1-zq*zq)
    integral_hi = factor*primitive
    integral_lo = integral_hi-tail
    assert 0 < integral_lo < integral_hi
    linear = s*(beta-q)-(beta*beta-q*q)/2
    # Analytic moving-endpoint Lipschitz bound from Section 9.2.
    error = 4*(Q[1]-Q[0])
    d_lo, d_hi = linear-2*integral_hi-error, linear-2*integral_lo+error
    assert F("0.00241410289623904895465331017") < d_lo < d_hi
    assert d_hi < F("0.00241410289623904895465331018")
    print("PASS rational D enclosure: 80 endpoint terms, positive tail, moving-q error")
    return d_lo, d_hi


def cubic(t, coefficient=24):
    return 432*t**3 + coefficient*t**2


def enclosures(d_lo, d_hi):
    lo, hi = map(F, T_TEXT)
    assert 0 < lo < hi
    assert cubic(lo) < d_lo < d_hi < cubic(hi)
    eta_lo, eta_hi = lo**3/PI[1], hi**3/PI[0]
    assert F(ETA_TEXT[0]) < eta_lo < eta_hi < F(ETA_TEXT[1])
    total_lo = TAU[0]*(1+Q[0])/(2*PI[1])+eta_lo
    total_hi = TAU[1]*(1+Q[1])/(2*PI[0])+eta_hi
    assert F(TOTAL_TEXT[0]) < total_lo < total_hi < F(TOTAL_TEXT[1])
    mu_lo, mu_hi = (3*x/(48+1296*x) for x in (lo, hi))
    assert 0 < mu_lo < mu_hi < F(1, 432)
    a_lo = 1+(5+F(19, 2)*mu_lo)/PI[1]
    a_hi = 1+(5+F(19, 2)*mu_hi)/PI[0]
    assert F(A_TEXT[0]) < a_lo < a_hi < F(A_TEXT[1]) < F("2.592953")
    for name, bracket in (("t_*", T_TEXT), ("eta_split", ETA_TEXT),
                          ("C+eta_split", TOTAL_TEXT), ("A", A_TEXT)):
        print(f"{bracket[0]} < {name} < {bracket[1]}")

    # Recheck the earlier coefficient's root locally solely for comparison.
    old_lo = F("0.00747297755774039228453004")
    old_hi = F("0.00747297755774039228453005")
    assert cubic(old_lo, 40) < d_lo < d_hi < cubic(old_hi, 40)
    old_eta_lo, old_eta_hi = old_lo**3/PI[1], old_hi**3/PI[0]
    assert F("1.917")*old_eta_hi < eta_lo < eta_hi < F("1.918")*old_eta_lo

    # Old sqrt envelope is nonbinding throughout 0<d<2.
    assert cubic(F(1, 6)) == F(8, 3) > 2
    assert F(1, 6)*(24+432*F(1, 6))**2 == 1536 < 3600
    assert F(ETA_TEXT[0])-F("2.592953")/10**12 > F("2.5468e-7")
    print("PASS comparison: 1.917 < eta_split/eta_new < 1.918; old sqrt bound nonbinding")
    print("PASS finite gate: n>=10^12 gives R*(n)>=B_n>(C+2.5468e-7)*n^2")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O; exact verification uses assertions.")
    identities()
    parameters()
    enclosures(*integral_bounds())
    print("PASS bounded independent identities/enclosures; no tour or geometry certificate")
