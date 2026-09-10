"""Bounded independent support for common-chain Section 12.

Default: standard-library rational arithmetic, fixed Taylor degrees, a
degree-40 midpoint polynomial integral and an explicit tail, integer square
root brackets, cubic sign gates, polynomial identities and finite errors.
--diagnostics adds independent SymPy algebra and 80/120-dps mpmath checks.
No production, result, or previous checker imports; no tours or n-grid.
Run without Python -O: assertions are the exact verification gates.
"""

import argparse
from fractions import Fraction as Q
from math import factorial, isqrt


BETA = Q(23, 100)
TAU_LO = Q("0.7390851332151606416553120876738734040134")
TAU_HI = Q("0.7390851332151606416553120876738734040135")
Q_LO = Q("0.1950200913506069300798071259134151019366")
Q_HI = Q("0.1950200913506069300798071259134151019367")
PI_LO = Q("3.1415926535897932384626433832795028841971")
PI_HI = Q("3.1415926535897932384626433832795028841972")
D_LO = Q("0.00241410289623904895465331017")
D_HI = Q("0.00241410289623904895465331018")
T_LO = Q("0.00747297755774039228453004644791959838")
T_HI = Q("0.00747297755774039228453004644791959839")
ETA_LO = Q("1.3284070181357731944366841527895847e-7")
ETA_HI = Q("1.3284070181357731944366841527895848e-7")
TOTAL_LO = Q("0.14056921368595858012283567471592395015")
TOTAL_HI = Q("0.14056921368595858012283567471592395016")
LOSS_UPPER = Q("2.592306")
FINITE_ETA = Q("1.3284e-7")
TERMS = 40


def parameter_checks():
    def trig(x, degree, odd):
        return sum(((-1)**j*x**(2*j+odd)/factorial(2*j+odd)
                    for j in range((degree-odd)//2+1)), Q(0))

    assert 0 < TAU_LO < TAU_HI < 1
    assert trig(TAU_LO, 82, 0) > TAU_LO
    assert trig(TAU_HI, 80, 0) < TAU_HI
    sine_low, sine_high = trig(TAU_LO, 83, 1), trig(TAU_HI, 81, 1)
    assert 0 < sine_low < sine_high < 1
    assert Q_LO < (1-sine_high)/(1+sine_high)
    assert (1-sine_low)/(1+sine_low) < Q_HI

    def atan(x, last):
        return sum(((-1)**j*x**(2*j+1)/(2*j+1)
                    for j in range(last+1)), Q(0))

    assert (Q(120, 119)-Q(1, 239))/(1+Q(120, 119*239)) == 1
    low = 16*atan(Q(1, 5), 41)-4*atan(Q(1, 239), 40)
    high = 16*atan(Q(1, 5), 40)-4*atan(Q(1, 239), 41)
    assert PI_LO < low < high < PI_HI
    assert Q(3, 17) < Q_LO < Q_HI < Q(1, 5) < BETA
    assert Q(3, 17)-Q(1, 102) == Q(1, 6)
    assert BETA-Q(1, 102) > Q(1, 5)
    assert Q(7, 6)-5*BETA == Q(1, 60) > 0
    print("exact parameter/domain gates: PASS (tau, q, pi; n>=102)")


def sqrt_bracket(value):
    assert value > 0
    scale = 10**50
    base = isqrt(value.numerator*scale**2//value.denominator)
    low, high = Q(base, scale), Q(base+1, scale)
    assert low**2 <= value < high**2
    return low, high


def midpoint_integral():
    # Independent of Section 9's z-integral binomial implementation.
    # x=m+h*u, -1<=u<=1; x*(s-x)=A*(1+v1*u+v2*u^2).
    q = Q_LO
    s, m, h = 1+q, (q+BETA)/2, (BETA-q)/2
    a = m*(s-m)
    v1, v2 = (s-2*m)*h/a, -h*h/a
    radius = abs(v1)+abs(v2)
    assert 0 < radius < Q(1, 10)
    power, coefficient, integral = [Q(1)], Q(1), Q(0)
    for j in range(TERMS+1):
        # Exact polynomial integration on [-1,1].
        integral += coefficient*sum((2*value/(degree+1)
                                    for degree, value in enumerate(power)
                                    if degree % 2 == 0), Q(0))
        if j < TERMS:
            next_power = [Q(0)]*(len(power)+2)
            for degree, value in enumerate(power):
                next_power[degree+1] += v1*value
                next_power[degree+2] += v2*value
            power = next_power
            coefficient *= (Q(1, 2)-j)/(j+1)
            assert abs(coefficient) <= 1
    # All omitted |binomial(1/2,j)|<=1; integrate uniform geometric tail.
    tail = 2*radius**(TERMS+1)/(1-radius)
    sqrt_low, sqrt_high = sqrt_bracket(a)
    assert integral > tail > 0
    i_low = h*sqrt_low*(integral-tail)
    i_high = h*sqrt_high*(integral+tail)
    linear = s*(BETA-q)-(BETA**2-q**2)/2
    q_error = 4*(Q_HI-Q_LO)  # Section 9's analytic moving-endpoint bound.
    low, high = linear-2*i_high-q_error, linear-2*i_low+q_error
    assert D_LO < low < high < D_HI
    print("independent exact D enclosure: PASS (degree 40, tail, isqrt)")
    return low, high


def poly_add(left, right):
    result = left.copy()
    for degree, value in right.items():
        result[degree] = result.get(degree, 0)+value
    return {degree: value for degree, value in result.items() if value}


def poly_multiply(left, right):
    result = {}
    for (i, j), value in left.items():
        for (k, ell), other in right.items():
            key = (i+k, j+ell)
            result[key] = result.get(key, 0)+value*other
    return {degree: value for degree, value in result.items() if value}


def scalar_algebra():
    # Variables (r,t), with d=432*r^3+40*r^2. Compare coefficients,
    # not a sample grid: the second branch minus r^3 factors globally.
    factor = {(1, 0): 1, (0, 1): -1}
    other = {(1, 0): 40, (0, 1): 40,
             (2, 0): 431, (1, 1): 431, (0, 2): 431}
    difference = {(3, 0): 431, (2, 0): 40,
                  (0, 2): -40, (0, 3): -431}
    assert poly_multiply(factor, other) == difference
    cube_factor = {(2, 0): 1, (1, 1): 1, (0, 2): 1}
    assert poly_multiply(factor, cube_factor) == {(3, 0): 1, (0, 3): -1}
    # Secant loss <= m'(d) on the left of the crossing:
    # 3r(40(r+t)+432(r^2+rt+t^2))
    # -(80+1296r)(r^2+rt+t^2)=40(r-t)(r+2t).
    sum2 = cube_factor
    denominator = poly_add({(1, 0): 40, (0, 1): 40},
                           {degree: 432*value for degree, value in sum2.items()})
    left = poly_multiply({(1, 0): 3}, denominator)
    subtract = poly_multiply({(0, 0): -80, (1, 0): -1296}, sum2)
    assert poly_add(left, subtract) == poly_multiply(
        factor, {(1, 0): 40, (0, 1): 80})
    # Exact inverse derivative formula and monotonicity reduce to 240>0.
    assert 3*80 == 240 > 0
    print("exact coefficient identities: PASS (crossing, cubes, secant error)")


def cubic(t):
    return 432*t**3+40*t**2


def coefficient_checks(d_low, d_high):
    assert 0 < T_LO < T_HI
    assert cubic(T_LO) < d_low < d_high < cubic(T_HI)
    eta_low, eta_high = T_LO**3/PI_HI, T_HI**3/PI_LO
    assert ETA_LO < eta_low < eta_high < ETA_HI
    c_low = TAU_LO*(1+Q_LO)/(2*PI_HI)
    c_high = TAU_HI*(1+Q_HI)/(2*PI_LO)
    assert TOTAL_LO < c_low+eta_low < c_high+eta_high < TOTAL_HI
    print("exact monotone cubic gates: PASS")
    print("1.3284070181357731944366841527895847e-7 < eta_new"
          " < 1.3284070181357731944366841527895848e-7")
    print("0.14056921368595858012283567471592395015 < C+eta_new"
          " < 0.14056921368595858012283567471592395016")

    derivative_low = 3*T_LO/(80+1296*T_LO)
    derivative_high = 3*T_HI/(80+1296*T_HI)
    assert 0 < derivative_low < derivative_high < Q(1, 432)
    a_low = 1+(5+Q(19, 2)*derivative_low)/PI_HI
    a_high = 1+(5+Q(19, 2)*derivative_high)/PI_LO
    assert Q("2.5923053389421502294191108763168") < a_low
    assert a_high < Q("2.5923053389421502294191108763170") < LOSS_UPPER
    assert eta_low-LOSS_UPPER/10**13 > FINITE_ETA
    old_low, old_high = d_low**2/(3600*PI_HI), d_high**2/(3600*PI_LO)
    assert 257*old_high < eta_low < eta_high < 258*old_low
    # At every finite crossing 0<d<2, t<1/6, and the old sqrt bound
    # is strictly looser: d^2/t^3=t*(40+432t)^2<3600.
    assert cubic(Q(1, 6)) > 2 > D_HI > 0
    assert Q(1, 6)*(40+432*Q(1, 6))**2 < 3600
    print("exact finite-error gates: PASS; A<2.592306; 257<eta_new/eta_60<258")
    print("finite corollary: n>=10^13 gives R*(n)>=B_n>(C+1.3284e-7)*n^2")
    return d_low, d_high, eta_low, eta_high


def diagnostics(bounds):
    import mpmath as mp
    import sympy as sp

    r, t = sp.symbols("r t", positive=True)
    assert sp.expand(cubic(r)-40*t**2-431*t**3-r**3
                     -(r-t)*(40*(r+t)+431*(r*r+r*t+t*t))) == 0
    assert sp.simplify(sp.diff(t**3, t)/sp.diff(cubic(t), t)
                       -3*t/(80+1296*t)) == 0
    assert sp.simplify(sp.diff(3*t/(80+1296*t), t)
                       -240/(80+1296*t)**2) == 0
    print("independent SymPy crossing/inverse-derivative identities: PASS")

    for precision in (80, 120):
        with mp.workdps(precision):
            def as_mp(value):
                return mp.mpf(value.numerator)/value.denominator

            tau = mp.findroot(lambda x: mp.cos(x)-x, (mp.mpf(".73"),
                              mp.mpf(".75")), maxsteps=50)
            q = (1-mp.sin(tau))/(1+mp.sin(tau))
            d = mp.quad(lambda x: 1+q-x-2*mp.sqrt(x*(1+q-x)),
                        [q, as_mp(BETA)])
            low, high = mp.mpf(0), mp.mpf(1)/6
            for _ in range(420):
                middle = (low+high)/2
                if cubic(middle) < d:
                    low = middle
                else:
                    high = middle
            root = (low+high)/2
            eta = root**3/mp.pi
            assert as_mp(bounds[0]) < d < as_mp(bounds[1])
            assert as_mp(T_LO) < root < as_mp(T_HI)
            assert as_mp(bounds[2]) < eta < as_mp(bounds[3])
            print(f"numerical diagnostic ({precision} dps): "
                  f"eta_new={mp.nstr(eta, 40)} PASS")
    print("Diagnostics are observations, not premises of the rational enclosures.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O; exact gates use assertions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics", action="store_true")
    args = parser.parse_args()
    parameter_checks()
    scalar_algebra()
    bounds = coefficient_checks(*midpoint_integral())
    if args.diagnostics:
        diagnostics(bounds)
    print("PASS: bounded independent scalar support; no geometric optimality certificate")
