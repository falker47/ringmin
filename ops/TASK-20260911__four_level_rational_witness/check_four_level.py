"""Bounded rational support for THREE_LEVEL_COMMON_CHAIN.md, Section 11.

Run with python -I -S. Only standard-library integer/Fraction arithmetic;
no production, prior-checker, result or third-party imports. Fixed witness,
fixed series lengths, no search or optimization. The accepted analytic
corollary supplies all-order/all-n quantifiers, not the boundary examples.
"""

from fractions import Fraction as F
from math import comb, factorial

if not __debug__:
    raise RuntimeError("This checker requires enabled assertions; omit -O.")

TAU = tuple(map(F, (
    "0.7390851332151606416553120876738734040134",
    "0.7390851332151606416553120876738734040135")))
Q = tuple(map(F, (
    "0.1950200913506069300798071259134151019366",
    "0.1950200913506069300798071259134151019367")))
PI = tuple(map(F, (
    "3.1415926535897932384626433832795028841971",
    "3.1415926535897932384626433832795028841972")))
BETA = (F(2091, 10000), F(10907, 50000), F(23, 100))
WIDTH = (F(451, 100000), F(451, 100000), F(367, 50000))
H = sum(WIDTH)
CUBES = sum(h**3 for h in WIDTH)
L = 16+432*H
N = 100000


def parameter_gates():
    def trig(x, count, odd):
        return sum(F((-1)**j, factorial(2*j+odd))*x**(2*j+odd)
                   for j in range(count))

    assert 0 < TAU[0] < TAU[1] < 1
    assert trig(TAU[0], 30, 0) > TAU[0]
    assert trig(TAU[1], 31, 0) < TAU[1]
    sine_low, sine_high = trig(TAU[0], 30, 1), trig(TAU[1], 31, 1)
    assert 0 < sine_low < sine_high < 1
    assert Q[0] < (1-sine_high)/(1+sine_high)
    assert (1-sine_low)/(1+sine_low) < Q[1]
    assert F("0.19502009") < Q[0] < Q[1] < F("0.19502010")

    def atan(x, count):
        return sum(F((-1)**j, 2*j+1)*x**(2*j+1) for j in range(count))

    tangent = F(1, 5)
    for _ in range(2):
        tangent = 2*tangent/(1-tangent*tangent)
    assert (tangent-F(1, 239))/(1+tangent/F(239)) == 1
    pi_low = 16*atan(F(1, 5), 32)-4*atan(F(1, 239), 31)
    pi_high = 16*atan(F(1, 5), 31)-4*atan(F(1, 239), 32)
    assert PI[0] < pi_low < pi_high < PI[1]
    print("PASS rational Taylor gates: tau, q, pi")


def finite_gates():
    assert N >= 102 and Q[0]-F(1, N) > F(1, 6)
    assert 0 < Q[1] < F(1, 5) < BETA[0] < BETA[1] < BETA[2] <= F(23, 100)
    assert all(h > 0 for h in WIDTH)
    margins = tuple(BETA[i+1]-BETA[i]-WIDTH[i]-WIDTH[i+1] for i in range(2))
    assert margins == (F(1, 50000), F(1, 100000))
    assert all(N*d >= 1 for d in margins)
    assert N*(BETA[0]-Q[1]) > 1
    assert N*(1-BETA[-1]) >= 2
    assert 1+F(1, 6)-2*BETA[-1] == F(53, 75) > F(1, 2)
    # a in (1/6,1/5) gives the existing derivative/Hessian/run gates.
    assert 6 < 9 and 54 < 64  # sqrt(6)<3; 3*sqrt(6)/2<4
    assert F(1, 4)/F(1, 6) < 2  # Hessian off-diagonal
    assert F(6, 5)/(4*F(1, 6)**2) == F(54, 5) < 11
    assert 43+11 == 54 and 8*(54*H+2) == L > H > 0
    print("PASS all-n domain: N=100000; adjacent margins 1/50000, 1/100000")

    # Boundary corroboration only: the inequalities above prove every n>=N.
    for n in (N, N+1):
        ell = [(b*n).__floor__() for b in BETA]
        assert F(ell[0], n) > Q[1]
        assert ell[0] < ell[1] < ell[2] <= n-2
        for i in range(2):
            assert F(ell[i+1]-ell[i], n) >= WIDTH[i]+WIDTH[i+1]
            # Midpoint differences cancel the two half-grid offsets.
            assert F(2*ell[i+1]-1, 2*n)-F(2*ell[i]-1, 2*n) == F(ell[i+1]-ell[i], n)
    # The unchanged witness does fail a finite floor gate at n=1000.
    n = 1000
    ell = [(b*n).__floor__() for b in BETA]
    assert F(ell[1]-ell[0], n) == F(9, 1000) < WIDTH[0]+WIDTH[1]
    print("PASS finite boundary checks; negative control rejects n=1000")


def deletion_interval(beta):
    """80 integrated binomial terms, geometric tail, moving-q error."""
    assert Q[1] < beta <= F(23, 100)
    q, s = Q[0], 1+Q[0]
    left, right = (s-2*beta)/s, (1-q)/s
    assert 0 < left < right < 1
    integral = right-left
    for j in range(1, 81):
        coefficient = F(comb(2*j, j), 4**j*(2*j-1))
        integral -= coefficient*(right**(2*j+1)-left**(2*j+1))/(2*j+1)
    next_coefficient = F(comb(162, 81), 4**81*161)
    tail = (right-left)*next_coefficient*right**162/(1-right**2)
    assert tail > 0 and integral > tail
    radical_low, radical_high = s*s/4*(integral-tail), s*s/4*integral
    linear = s*(beta-q)-(beta*beta-q*q)/2
    moving_error = 4*(Q[1]-Q[0])
    return (linear-2*radical_high-moving_error,
            linear-2*radical_low+moving_error)


def show_interval(name, bounds, digits=20):
    """Print strict outward decimal rationals using integer division only."""
    low, high = bounds
    assert 0 < low < high
    scale = 10**digits
    lower = (low*scale).__floor__()-1
    upper = (high*scale).__ceil__()+1
    assert F(lower, scale) < low < high < F(upper, scale)

    def decimal(integer):
        whole, fraction = divmod(integer, scale)
        return f"{whole}.{fraction:0{digits}d}"

    print(f"{decimal(lower)} < {name} < {decimal(upper)}")


def coefficient_gates():
    ds = tuple(deletion_interval(b) for b in BETA)
    assert all(0 < lo < hi for lo, hi in ds)
    assert ds[0][1] < ds[1][0] and ds[1][1] < ds[2][0]
    numerator = tuple(sum(h*d[j] for h, d in zip(WIDTH, ds))-8*CUBES
                      for j in range(2))
    assert numerator[0] > 0  # Discharges the positive part in eta(h).
    eta = (numerator[0]/(PI[1]*L), numerator[1]/(PI[0]*L))

    # Recompute eta_3 from its integral definition, not a copied decimal.
    old_d1 = deletion_interval(F(1, 5))
    old_h = (F(3, 1000), F(9, 1000))
    old_l = 16+432*sum(old_h)
    old_cubes = sum(h**3 for h in old_h)
    old_num = tuple(old_h[0]*old_d1[j]+old_h[1]*ds[2][j]-8*old_cubes
                    for j in range(2))
    assert old_num[0] > 0
    old_eta = (old_num[0]/(PI[1]*old_l), old_num[1]/(PI[0]*old_l))
    gain = (eta[0]-old_eta[1], eta[1]-old_eta[0])
    margin = (gain[0]-F(1, 10000000), gain[1]-F(1, 10000000))
    assert margin[0] > 0, "Fixed witness does not certify the requested strict margin."

    # Existing terminal theorem: C=tau*(1+q)/(2*pi).
    c = (TAU[0]*(1+Q[0])/(2*PI[1]), TAU[1]*(1+Q[1])/(2*PI[0]))
    total = (c[0]+eta[0], c[1]+eta[1])
    a = (1+(5+19*H/(2*L))/PI[1], 1+(5+19*H/(2*L))/PI[0])
    assert a[1] < F("2.594")
    assert margin[0] > a[1]/10**8

    print(f"H={H}; sum(h_i^3)={CUBES}; L={L}")
    for i, d in enumerate(ds, 1):
        show_interval(f"D_{i}", d)
    for name, bounds in (("F", numerator), ("eta_4", eta), ("eta_3", old_eta),
                         ("eta_4-eta_3", gain), ("eta_4-eta_3-1e-7", margin),
                         ("C_term+eta_4", total), ("A_4", a)):
        show_interval(name, bounds)
    print("PASS strict improvement eta_4 > eta_3 + 1e-7")
    print("PASS finite strict transfer for n>=10^8")


if __name__ == "__main__":
    parameter_gates()
    finite_gates()
    coefficient_gates()
    print("PASS fixed four-level witness; universal quantifiers use the proved corollary")
