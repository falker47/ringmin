"""Bounded exact support for THREE_LEVEL_COMMON_CHAIN.md.

Run with python -I -S. No third-party, production, prior-checker or saved
result imports. No tour enumeration. Fractions certify the strict gates;
bounded grid couplings check the shared-measure accounting, not geometry.
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
BETA = (F(1, 5), F(23, 100))
WIDTH = (F(3, 1000), F(9, 1000))
H = sum(WIDTH)
CUBES = sum(h**3 for h in WIDTH)
DENOMINATOR = 16 + 432*H


def parameter_gates():
    def trig(x, count, odd):
        return sum(F((-1)**j, factorial(2*j+odd))*x**(2*j+odd)
                   for j in range(count))

    assert 0 < TAU[0] < TAU[1] < 1
    assert trig(TAU[0], 30, 0) > TAU[0]
    assert trig(TAU[1], 31, 0) < TAU[1]
    sine_low = trig(TAU[0], 30, 1)
    sine_high = trig(TAU[1], 31, 1)
    assert Q[0] < (1-sine_high)/(1+sine_high)
    assert (1-sine_low)/(1+sine_low) < Q[1]
    assert F("0.19502009") < Q[0] < Q[1] < F("0.19502010")

    def atan(x, count):
        return sum(F((-1)**j, 2*j+1)*x**(2*j+1)
                   for j in range(count))

    # tan(4 atan(1/5) - atan(1/239))=1, angle in (0,pi/2).
    tangent = F(1, 5)
    for _ in range(2):
        tangent = 2*tangent/(1-tangent*tangent)
    assert (tangent-F(1, 239))/(1+tangent/F(239)) == 1
    pi_low = 16*atan(F(1, 5), 32)-4*atan(F(1, 239), 31)
    pi_high = 16*atan(F(1, 5), 31)-4*atan(F(1, 239), 32)
    assert PI[0] < pi_low < pi_high < PI[1]
    print("PASS rational Taylor gates: tau, q, pi")


def deletion_interval(beta):
    q = Q[0]
    s = 1+q
    left, right = (s-2*beta)/s, (1-q)/s
    assert 0 < left < right < 1
    integral = right-left
    for j in range(1, 81):
        coefficient = F(comb(2*j, j), 4**j*(2*j-1))
        integral -= coefficient*(right**(2*j+1)-left**(2*j+1))/(2*j+1)
    next_coefficient = F(comb(162, 81), 4**81*161)
    tail = (right-left)*next_coefficient*right**162/(1-right**2)
    radical_low, radical_high = s*s/4*(integral-tail), s*s/4*integral
    linear = s*(beta-q)-(beta*beta-q*q)/2
    moving_error = 4*(Q[1]-Q[0])
    return (linear-2*radical_high-moving_error,
            linear-2*radical_low+moving_error)


def coefficient_gates():
    d1, d2 = map(deletion_interval, BETA)
    assert F("0.0005467128705163") < d1[0] < d1[1]
    assert d1[1] < F("0.0005467128705164")
    assert F("0.0024141028962390") < d2[0] < d2[1]
    assert d2[1] < F("0.0024141028962391")
    assert 0 < d1[0] < d1[1] < d2[0]
    assert H == F(3, 250) and CUBES == F(189, 250000000)
    assert DENOMINATOR == F(2648, 125)
    zeta = tuple((WIDTH[0]*d1[j]+WIDTH[1]*d2[j]-8*CUBES)/DENOMINATOR
                 for j in range(2))
    eta = (zeta[0]/PI[1], zeta[1]/PI[0])
    assert F("2.6023553183e-7") < eta[0] < eta[1]
    assert eta[1] < F("2.6023553184e-7")

    old_t = tuple(map(F, ("0.0092836183568361125168565556",
                         "0.0092836183568361125168565557")))
    # Root endpoints are checked by signs, never trusted as data.
    polynomial = lambda t: 432*t**3+24*t**2
    assert 0 < old_t[0] < old_t[1]
    assert polynomial(old_t[0]) < d2[0] < d2[1] < polynomial(old_t[1])
    old_eta = (old_t[0]**3/PI[1], old_t[1]**3/PI[0])
    improvement = (eta[0]-old_eta[1], eta[1]-old_eta[0])
    assert F("5.5513553e-9") < improvement[0] < improvement[1]
    assert improvement[1] < F("5.5513554e-9")
    gap = F(11, 2000000000)
    assert improvement[0] > gap
    a_upper = 1+(5+19*H/(2*DENOMINATOR))/PI[0]
    assert a_upper < F("2.593263")
    assert improvement[0]-F("2.593263")/10**12 > gap

    # The single-cutoff scalar information permits W_1=W_2=W_0 at old e.
    assert d1[1] < polynomial(old_t[0])
    # But the new joint hyperplane excludes the same formal data.
    assert zeta[0] > old_t[1]**3
    print("PASS exact integral gates: both cutoffs, 80 terms and moving-q error")
    print("2.6023553183e-7 < eta_3 < 2.6023553184e-7")
    print("5.5513553e-9 < eta_3-eta_split < 5.5513554e-9")
    print("PASS finite transfer gates: A_3 < 2.593263; n >= 10^12")


def finite_domain_gates():
    assert Q[0]-F(1, 1000) > F(1, 6)
    assert BETA[0]-F(1, 1000) > Q[1]
    assert BETA[1]-F(1, 1000) > BETA[0]
    assert 1+F(1, 6)-2*BETA[1] > F(1, 2)
    assert BETA[1]-BETA[0]-F(1, 1000) == F(29, 1000) > H
    # L/H > 1, needed by the scalar minimax for every sign of F_n.
    assert DENOMINATOR/H > 1
    for f in (F(-1), F(0), F(1, 100000)):
        optimum = max(f, 0)/DENOMINATOR
        value = lambda e: max(e, f/H-(DENOMINATOR/H-1)*e)
        assert value(optimum) == optimum
        for e in (F(0), optimum/2, optimum, optimum+1):
            assert value(e) >= optimum
    print("PASS finite domain, floors, cutoff separation and scalar sign gates")


def measure_checks():
    parities = set()
    double_crossing_seen = False
    count = 0
    for n in (1000, 1001, 1002, 1003):
        # Exact q floors in these bounded cases only. The theorem uses (4).
        k = (Q[0]*n).__floor__()
        assert k == (Q[1]*n).__floor__()
        grid = [F(j, n) for j in range(k, n+1)]
        cuts = [F((beta*n).__floor__(), n)-F(1, 2*n) for beta in BETA]
        parities.add(len(grid) % 2)
        for cut in cuts:
            for h in (F(1, 4*n), F(1, 2*n), F(1, n), *WIDTH, F(1)):
                mass = F(sum(abs(x-cut) <= h for x in grid), n)
                assert mass <= 4*h

        # Three explicit doubly stochastic graph measures, not cyclic tours.
        # Identity, reversal and cyclic shift provide equal grid marginals.
        for permutation in (grid, list(reversed(grid)), grid[17:]+grid[:17]):
            assert sorted(permutation) == grid
            energy = F(0)
            crossings = [F(0), F(0)]
            for x, z in zip(grid, permutation):
                distance = abs(x-z)
                indicators = [(x-b)*(z-b) < 0 for b in cuts]
                double_crossing_seen |= all(indicators)
                long_weight = sum(h*distance for h, crosses in zip(WIDTH, indicators)
                                  if crosses and distance > h)
                assert long_weight <= distance**2
                energy += distance**2/n
                for i, crosses in enumerate(indicators):
                    if crosses:
                        crossings[i] += distance/n
            assert sum(h*v for h, v in zip(WIDTH, crossings)) <= 4*CUBES+energy
            count += 1
    assert parities == {0, 1} and double_crossing_seen and count == 12
    print("PASS 12 prescribed grid couplings: marginals, strips, shared energy, both parities")


def negative_controls():
    # Two separately legal budgets can overspend the common energy.
    energy = F(1, 1000000)
    independent_k = [4*h*h+energy/h for h in WIDTH]
    assert all(k <= 4*h*h+energy/h for h, k in zip(WIDTH, independent_k))
    assert sum(h*k for h, k in zip(WIDTH, independent_k)) > 4*CUBES+energy
    # With a cutoff ON a grid point, a tiny strip has mass 1/n > 4h.
    n = 1000
    h = F(1, 8*n)
    assert F(1, n) > 4*h
    # Without separation, a double crossing can spend energy twice.
    distance, width = F(3, 200), F(1, 100)
    assert distance > width and 2*width*distance > distance**2
    print("PASS negative controls: independent budgets, on-grid cutoff, missing separation")


if __name__ == "__main__":
    parameter_gates()
    finite_domain_gates()
    coefficient_gates()
    measure_checks()
    negative_controls()
    print("PASS all three-level checks; analytic proof supplies all-order quantifiers")
