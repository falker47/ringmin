"""Bounded support for the analytic two-level minimax extension.

Default: exact Fraction Taylor gates, an 80-term integrated binomial
enclosure with a proved tail, scalar identities and finite error gates.
--diagnostics: independent mpmath quadrature/primitive at 80 and 120 dps,
plus two SymPy identities. No tours, n-grid, production imports or results.
The scalar relaxation's sharpness is not sharpness for common tours.
"""

import argparse
from fractions import Fraction as Q
from math import factorial


BETA = Q(23, 100)
TAU_LO = Q("0.7390851332151606416553120876738734040134")
TAU_HI = Q("0.7390851332151606416553120876738734040135")
Q_LO = Q("0.1950200913506069300798071259134151019366")
Q_HI = Q("0.1950200913506069300798071259134151019367")
PI_LO = Q("3.1415926535897932384626433832795028841971")
PI_HI = Q("3.1415926535897932384626433832795028841972")
D_LO = Q("0.00241410289623904895465331017")
D_HI = Q("0.00241410289623904895465331018")
ETA_LO = Q("0.00000000051529885884211781970537738")
ETA_HI = Q("0.00000000051529885884211781970537739")
ETA_FINITE = Q("0.0000000005152")
TERMS = 80


def cosine(x, degree):
    return sum(((-1)**j * x**(2*j) / factorial(2*j)
                for j in range(degree // 2 + 1)), Q(0))


def sine(x, degree):
    return sum(((-1)**j * x**(2*j+1) / factorial(2*j+1)
                for j in range((degree + 1) // 2)), Q(0))


def arctangent(x, last_index):
    return sum(((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(last_index + 1)), Q(0))


def parameter_gates():
    assert 0 < TAU_LO < TAU_HI < 1
    assert cosine(TAU_LO, 82) > TAU_LO
    assert cosine(TAU_HI, 80) < TAU_HI
    sin_lo, sin_hi = sine(TAU_LO, 83), sine(TAU_HI, 81)
    assert 0 < sin_lo < sin_hi < 1
    assert Q_LO < (1-sin_hi)/(1+sin_hi)
    assert (1-sin_lo)/(1+sin_lo) < Q_HI
    assert Q(3, 17) < Q_LO < Q_HI < Q(1, 5) < BETA

    # Machin identity: tan(4 atan(1/5)-atan(1/239))=1,
    # and the angle lies in (0,pi/2); hence it equals pi/4.
    assert (Q(120, 119)-Q(1, 239))/(1+Q(120, 119*239)) == 1
    machin_lo = 16*arctangent(Q(1, 5), 41)-4*arctangent(Q(1, 239), 40)
    machin_hi = 16*arctangent(Q(1, 5), 40)-4*arctangent(Q(1, 239), 41)
    assert PI_LO < machin_lo < machin_hi < PI_HI
    print("exact parameter gates: tau, q_*, pi PASS (40 decimal places)")


def integral_enclosure(terms):
    # Evaluate at rational q0=Q_LO, then allow the analytic Lipschitz
    # error |D(q_*)-D(q0)| <= 4*(Q_HI-Q_LO).
    q0 = Q_LO
    s = 1+q0
    zq = (1-q0)/s
    zb = (s-2*BETA)/s
    assert 0 < zb < zq < 1
    coeff = Q(1, 2)
    primitive_difference = zq-zb
    for j in range(1, terms+1):
        primitive_difference -= coeff*(zq**(2*j+1)-zb**(2*j+1))/(2*j+1)
        coeff *= Q(2*j-1, 2*(j+1))
    # coeff is c_(terms+1). All subsequent c_j are positive and smaller.
    integral_upper = s*s*primitive_difference/4
    tail = s*s*(zq-zb)*coeff*zq**(2*terms+2)/(4*(1-zq*zq))
    linear = s*(BETA-q0)-(BETA*BETA-q0*q0)/2
    q_error = 4*(Q_HI-Q_LO)
    lower = linear-2*integral_upper-q_error
    upper = linear-2*integral_upper+2*tail+q_error
    assert lower < upper and tail > 0
    return lower, upper


def exact_checks():
    parameter_gates()
    d_lo, d_hi = integral_enclosure(TERMS)
    assert D_LO < d_lo < d_hi < D_HI
    eta_lo, eta_hi = d_lo*d_lo/(3600*PI_HI), d_hi*d_hi/(3600*PI_LO)
    assert ETA_LO < eta_lo < eta_hi < ETA_HI
    assert 0 < d_lo < d_hi < Q(1, 100) < 1800
    assert Q("0.00000000051529885884") < eta_lo
    assert eta_hi < Q("0.00000000051529885885")
    print("exact integral enclosure: 80 integrated binomial terms + positive tail PASS")
    print("0.00241410289623904895465331017 < D < 0.00241410289623904895465331018")
    print("5.1529885884211781970537738e-10 < eta_60 < 5.1529885884211781970537739e-10")

    # Analytic minimax proof uses t=sqrt(e), crossing t=D/60.
    # For 0<=t<=D/60 the difference from the crossing value factors as
    # (D/60-t)*(60-D/60-t)>=0 whenever 0<=D<=1800.
    assert d_hi/60 < 30
    assert eta_lo > 515*Q(1, 10**12)
    assert eta_hi < 516*Q(1, 10**12)
    assert eta_hi < Q("0.0000000005153")
    # Finite D_n positivity from a>1/6, x<b<=beta.
    assert Q(7, 6)-5*BETA == Q(1, 60) > 0
    assert (Q(3, 17)-Q(1, 102)) == Q(1, 6)
    assert BETA-Q(1, 102) > Q(1, 5)
    # With n>=102, D_n<2; |D_n-D|<=10/n bounds square loss by 21/n.
    assert d_hi+2 < Q(21, 10)
    assert 1+(6+Q(21, 3600))/PI_LO < 3
    assert eta_lo-Q(3, 10**14) > ETA_FINITE > Q(1, 10**12)
    print("exact minimax/domain/error gates: PASS; 515 < eta_60/10^-12 < 516")
    print("finite corollary: n>=10^14 gives B_n/n^2 >= C+eta_60-3/n > C+5.152e-10")
    return d_lo, d_hi, eta_lo, eta_hi


def diagnostics(bounds):
    import mpmath as mp
    import sympy as sp

    t, d = sp.symbols("t d", real=True)
    factor = t*t+d-60*t-d*d/3600-(d/60-t)*(60-d/60-t)
    assert sp.expand(factor) == 0
    x, s = sp.symbols("x s", positive=True)
    primitive = ((2*x-s)*sp.sqrt(x*(s-x))/4
                 + s*s*sp.asin((2*x-s)/s)/8)
    derivative = sp.diff(primitive, x).subs(s, x+sp.Symbol("y", positive=True))
    assert sp.simplify(derivative-sp.sqrt(x*(s-x)).subs(s, x+sp.Symbol("y", positive=True))) == 0
    print("independent symbolic identities: minimax factorization, integral primitive PASS")

    def mpq(value):
        return mp.mpf(value.numerator)/value.denominator

    for precision in (80, 120):
        with mp.workdps(precision):
            tau = mp.findroot(lambda value: mp.cos(value)-value, (mp.mpf(".73"), mp.mpf(".75")))
            q = (1-mp.sin(tau))/(1+mp.sin(tau))
            beta, total = mpq(BETA), 1+q
            value = mp.quad(lambda u: total-u-2*mp.sqrt(u*(total-u)), [q, beta])

            def primitive_at(u):
                return ((2*u-total)*mp.sqrt(u*(total-u))/4
                        + total*total*mp.asin((2*u-total)/total)/8)

            alternate = total*(beta-q)-(beta*beta-q*q)/2-2*(primitive_at(beta)-primitive_at(q))
            eta = value*value/(3600*mp.pi)
            assert mpq(bounds[0]) < value < mpq(bounds[1])
            assert mpq(bounds[2]) < eta < mpq(bounds[3])
            assert abs(value-alternate) < mp.mpf(10)**(-precision+10)
            print(f"independent numerical diagnostic ({precision} dps): D={mp.nstr(value, 35)}, eta_60={mp.nstr(eta, 35)} PASS")
    print("Numerical diagnostics only; exact enclosures above do not depend on mpmath.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics", action="store_true")
    args = parser.parse_args()
    bounds = exact_checks()
    if args.diagnostics:
        diagnostics(bounds)
    print("PASS: bounded analytic support; no tour enumeration or finite optimum certification")
