"""Supplement S1, L1 (angular geometry, deletion) and L2 (terminal parameters)."""

from __future__ import annotations

import itertools
import random
from fractions import Fraction

from flint import arb

from p2_base import (C_TERM, Q, Q_HI, Q_LO, SIN_TAU, TAU, TAU_HI, TAU_LO, ball, chain_sum,
                     check, integral, need, printed, supnick, theta, two_pi)


@check("P2-L1a", "exact", "(SM2.1): arcsin and arctan forms of the kernel; bounds 2 sqrt(uv)/(R+n) <= theta <= 2 sqrt(uv)/R")
def kernel_forms():
    count = 0
    grid = [Fraction(1, 3), Fraction(2), Fraction(9), Fraction(40)]
    for R, u, v in itertools.product(grid, repeat=3):
        s2 = u * v / ((R + u) * (R + v))
        need(1 - s2 == R * (R + u + v) / ((R + u) * (R + v)))        # identity quoted in the text
        need(s2 / (1 - s2) == u * v / (R * (R + u + v)))             # tan^2 of the half angle
        root = (ball(u) * ball(v)).sqrt()
        arctan_form = 2 * (root / (ball(R) * ball(R + u + v)).sqrt()).atan()
        need((theta(R, u, v) - arctan_form).overlaps(arb(0)))
        n = 40
        need(2 * root / ball(R + n) < theta(R, u, v) and theta(R, u, v) < 2 * root / ball(R))
        count += 1
    return "%d exact grid points" % count


def sqrt_sum(cycle) -> arb:
    m = len(cycle)
    return sum(((ball(cycle[i]) * ball(cycle[(i + 1) % m])).sqrt() for i in range(m)), arb(0))


@check("P2-L1b", "interval", "Lemma SM2.1: S/pi - n <= Rc(omega) <= S/pi for arbitrary cycles of radii in {1..n}")
def root_sandwich():
    rng = random.Random(1)
    count = 0
    cases = [([1, 2, 3], 3), ([1, 2, 3], 50), ([48, 49, 50], 50), (list(range(1, 13)), 12)]
    for _ in range(120):
        n = rng.randint(3, 60)
        m = rng.randint(3, min(n, 25))
        cases.append((rng.sample(range(1, n + 1), m), n))
    for labels in (range(1, 80), range(19, 103)):
        cases.append((supnick(labels), max(labels)))
    for cycle, n in cases:
        S = sqrt_sum(cycle)
        upper = S / arb.pi()
        need(chain_sum(cycle, upper) < two_pi())            # Rc < S/pi
        lower = upper - n
        if lower > 0:
            need(chain_sum(cycle, lower) > two_pi())        # Rc > S/pi - n
        else:
            need(lower < 0)                                 # the lower bound is vacuous here
        count += 1
    return "%d cycles, both sides strict" % count


@check("P2-L1c", "interval", "Lemma SM2.2: deleting circles from a fully feasible configuration keeps Rc(omega') <= R")
def deletion():
    rng = random.Random(2)
    done = 0
    attempts = 0
    while done < 60:
        attempts += 1
        need(attempts < 5000)
        m = rng.randint(4, 9)
        radii = rng.sample(range(1, 30), m)
        R = Fraction(rng.randint(5, 400), 3)
        # random rational gaps summing to one turn; keep only fully feasible draws
        weights = [rng.randint(1, 20) for _ in range(m)]
        total = sum(weights)
        angles = [two_pi() * ball(Fraction(sum(weights[:i]), total)) for i in range(m)]
        feasible = True
        for i in range(m):
            for j in range(i + 1, m):
                sep = angles[j] - angles[i]
                need_angle = theta(R, radii[i], radii[j])
                ok = sep > need_angle and two_pi() - sep > need_angle
                bad = sep < need_angle or two_pi() - sep < need_angle
                if not ok:
                    feasible = False
                need(ok or bad, "undecided pair")
        if not feasible:
            continue
        for size in range(3, m + 1):
            keep = sorted(rng.sample(range(m), size))
            survivors = [radii[i] for i in keep]       # induced cyclic order
            need(chain_sum(survivors, R) < two_pi())   # hence Rc(omega') < R
        done += 1
    return "%d feasible configurations (of %d draws), every subset size >= 3" % (done, attempts)


def cos_partial(x: Fraction, m: int) -> Fraction:
    total, term = Fraction(0), Fraction(1)
    for j in range(m):
        total += term if j % 2 == 0 else -term
        term = term * x * x / ((2 * j + 1) * (2 * j + 2))
    return total


def sin_partial(x: Fraction, m: int) -> Fraction:
    total, term = Fraction(0), x
    for j in range(m):
        total += term if j % 2 == 0 else -term
        term = term * x * x / ((2 * j + 2) * (2 * j + 3))
    return total


def atan_partial(x: Fraction, m: int) -> Fraction:
    return sum((Fraction((-1) ** j) * x ** (2 * j + 1) / (2 * j + 1) for j in range(m)), Fraction(0))


@check("P2-L2a", "exact", "Section SM9.1: the rational gates for tau, sin tau, q and pi, exactly as printed")
def trigonometric_gates():
    T_lo, T_hi = printed("T_-"), printed("T_+")
    q_lo, q_hi = printed("q_-"), printed("q_+")
    pi_lo, pi_hi = printed("\\pi_-"), printed("\\pi_+")
    need(0 < T_lo < T_hi < 1)
    need(cos_partial(T_lo, 30) > T_lo and cos_partial(T_hi, 31) < T_hi)
    s_lo, s_hi = sin_partial(T_lo, 30), sin_partial(T_hi, 31)
    need(0 < s_lo < s_hi < 1)
    need(q_lo < (1 - s_hi) / (1 + s_hi) < (1 - s_lo) / (1 + s_lo) < q_hi)
    need(q_lo > Fraction(3, 17) and q_hi < Fraction(1, 5))
    machin_lo = 16 * atan_partial(Fraction(1, 5), 32) - 4 * atan_partial(Fraction(1, 239), 31)
    machin_hi = 16 * atan_partial(Fraction(1, 5), 31) - 4 * atan_partial(Fraction(1, 239), 32)
    need(pi_lo < machin_lo < machin_hi < pi_hi)
    # branch justification of Machin's identity
    t5 = Fraction(1, 5)
    double = 2 * t5 / (1 - t5 * t5)
    quad = 2 * double / (1 - double * double)
    need(quad == Fraction(120, 119))
    need((quad - Fraction(1, 239)) / (1 + quad * Fraction(1, 239)) == 1)
    need(4 * (t5 - t5 ** 3 / 3) > Fraction(1, 239))      # the angle is positive
    # independent Arb confirmation that the printed intervals contain the constants
    need(ball(T_lo) < TAU and TAU < ball(T_hi))
    need(ball(q_lo) < Q and Q < ball(q_hi))
    need(ball(pi_lo) < arb.pi() and arb.pi() < ball(pi_hi))
    need(T_lo < TAU_LO and TAU_HI < T_hi and q_lo < Q_LO and Q_HI < q_hi)
    # the grid gate (SM4.1) of L3
    need(Fraction(3, 17) - Fraction(1, 102) == Fraction(1, 6))
    return "all printed 40-digit gates hold; tau, q, pi confirmed by Arb"


@check("P2-L2b", "interval", "Lemma SM3.1: J = pi C_term, by rigorous quadrature and by the closed form")
def terminal_identity():
    s = 1 + Q
    # quadrature needs exact endpoints: integrate on [Q_LO, 1] with parameter ball Q
    # and bound the sliver [Q_LO, q] by its length times max |integrand| <= 1.
    quad = integral(lambda z, analytic: (z * (s - z)).sqrt(analytic=analytic), Q_LO, 1)
    sliver = ball(Q_HI - Q_LO)
    target = TAU * (1 + Q) / 2
    need(quad - sliver < target + sliver and target - sliver < quad + sliver)
    need((quad - target).rad() < arb(10) ** (-45) and abs(quad - target) < arb(10) ** (-45))
    # closed form: with v = (1-q)/(1+q) = sin tau, J = (1+q)^2/4 * (arcsin v + v sqrt(1-v^2))
    v = (1 - Q) / (1 + Q)
    need((v - SIN_TAU).overlaps(arb(0)))
    closed = (1 + Q) ** 2 / 4 * (v.asin() + v * (1 - v * v).sqrt())
    need((closed - target).overlaps(arb(0)) and (closed - target).rad() < arb(10) ** (-60))
    need((C_TERM * arb.pi() - target).overlaps(arb(0)))
    return "quadrature and closed form agree with tau(1+q)/2 to 1e-45"


@check("P2-L2c", "interval", "Lemma SM3.1: r -> (1/pi) int_r^1 sqrt(x(1+r-x)) dx has its unique maximum at r = q")
def terminal_maximum():
    import sympy as sp

    v = sp.symbols("v", positive=True)
    A = sp.asin(v) + v * sp.sqrt(1 - v ** 2)
    need(sp.simplify(sp.diff(A, v) - 2 * sp.sqrt(1 - v ** 2)) == 0)
    Phi = A / (sp.pi * (1 + v) ** 3) * (1 + v)
    claimed = 2 * (sp.sqrt(1 - v ** 2) - sp.asin(v)) / (sp.pi * (1 + v) ** 3)
    need(sp.simplify(sp.diff(Phi, v) - claimed) == 0)

    def value(r):
        r = ball(r)
        w = (1 - r) / (1 + r)
        return (w.asin() + w * (1 - w * w).sqrt()) / (arb.pi() * (1 + w) ** 2)

    best = TAU / (arb.pi() * (1 + SIN_TAU))
    need((best - C_TERM).overlaps(arb(0)))
    count = 0
    previous = None
    for num in range(1, 1000):
        r = Fraction(num, 1000)
        here = value(r)
        need(here < best)                       # no grid point beats r = q
        # the integral itself, by quadrature, at a few points
        if num % 111 == 0:
            quad = integral(lambda z, analytic, r=r: (z * (1 + ball(r) - z)).sqrt(analytic=analytic), r, 1) / arb.pi()
            need((quad - here).overlaps(arb(0)))
        if previous is not None:                # increasing below q, decreasing above q
            need(here > previous if r < Q_LO else here < previous or r - Fraction(1, 1000) < Q_HI)
        previous = here
        count += 1
    need(value(Fraction(1, 10**9)) < ball(Fraction(1, 8)) + arb(10) ** (-8))   # endpoint limit 1/8 as r -> 0
    need(value(1 - Fraction(1, 10**9)) < arb(10) ** (-8))                      # endpoint limit 0 as r -> 1
    return "%d grid values of r strictly below the value at q; derivative formula by sympy" % count
