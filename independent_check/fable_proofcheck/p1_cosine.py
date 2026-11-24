"""Section 6.2 and Appendix B of Paper I: outward integer cosine arithmetic."""

from __future__ import annotations

import random
import re
from fractions import Fraction

from p1_base import ball, check, frac, need, not_outside, paper_text, table_body, theta, two_pi

S = 2 ** 128
B = 2 ** 224
TERMS = 112


def cos_enclosure(a: int, d: int, terms: int = TERMS, grid: int = B):
    """Appendix B recurrence for cos x with x^2 = a/d; returns integers (lo, hi)
    such that lo/grid <= cos x <= hi/grid, plus the term bounds for auditing."""
    need(a >= 0 and d > 0 and terms % 2 == 0)
    l, u = grid, grid
    lower = upper = 0
    ls, us = [], []
    for j in range(terms):
        ls.append(l)
        us.append(u)
        if j % 2 == 0:
            lower += l
            upper += u
        else:
            lower -= u
            upper -= l
        den = d * (2 * j + 1) * (2 * j + 2)
        l = (a * l) // den
        u = -((-a * u) // den)
    ls.append(l)
    us.append(u)
    return lower, upper + u, ls, us  # remainder in [0, t_N]: add u_N to the upper sum only


@check("P1-A1", "exact", "Appendix B: induction l_j <= B t_j <= u_j and the alternating remainder")
def recurrence_invariants():
    rng = random.Random(3)
    count = 0
    for _ in range(40):
        num, den = rng.randint(0, 4000), 1000
        x = Fraction(num, den)  # 0 <= x <= 4
        a, d = num * num, den * den
        lower, upper, ls, us = cos_enclosure(a, d)
        t = Fraction(1)
        for j in range(TERMS + 1):
            need(ls[j] <= B * t <= us[j])
            t = t * x * x / ((2 * j + 1) * (2 * j + 2))
        # exact partial sum and tail bound: cos x in [P, P + t_N] for even N
        partial = Fraction(0)
        t = Fraction(1)
        for j in range(TERMS):
            partial += t if j % 2 == 0 else -t
            t = t * x * x / ((2 * j + 1) * (2 * j + 2))
        need(Fraction(lower, B) <= partial and partial + t <= Fraction(upper, B))
        # Arb cannot resolve a tail of size x^224/224!, so this is a consistency
        # test; the proof of containment is the exact comparison above.
        need(not_outside(ball(x).cos(), Fraction(lower, B), Fraction(upper, B)))
        need(upper - lower < 2 * TERMS + 4)  # rounding loss is a few hundred units of 2^-224
        count += 1
    # the tail ratio at the cutoff, for the whole range 0 <= x <= 4
    need(Fraction(16, (2 * TERMS + 1) * (2 * TERMS + 2)) < 1)
    return "%d rational arguments in [0,4]" % count


@check("P1-A2", "exact", "Appendix B: printed T_-, T_+ enclose 2 pi * 2^128 by the paper's own sign test")
def circumference():
    text = paper_text()
    t_minus = int(re.search(r"T_-&=(\d+)", text).group(1))
    t_plus = int(re.search(r"T_\+&=(\d+)", text).group(1))
    need(t_plus == t_minus + 1 and 6 * S < t_minus < t_plus < 7 * S)
    # cos(T_-/(4S)) > 0 > cos(T_+/(4S)), by the Appendix B recurrence only
    lower, _, _, _ = cos_enclosure(t_minus ** 2, (4 * S) ** 2)
    _, upper, _, _ = cos_enclosure(t_plus ** 2, (4 * S) ** 2)
    need(lower > 0 and upper < 0)
    need(Fraction(3, 2) < Fraction(t_minus, 4 * S) and Fraction(t_plus, 4 * S) < Fraction(7, 4))
    # independent confirmation
    scaled = two_pi() * S
    need(ball(t_minus) < scaled and scaled < ball(t_plus))
    return "T_- = floor(2 pi 2^128), T_+ = T_- + 1"


@check("P1-A3", "exact", "(10): the recurrence proves cos(l/S) > 1-2q > cos(u/S) for all 908 pair intervals")
def pair_intervals():
    rows = [row.split("&") for row in table_body("tab:brackets")]
    count = 0
    widest = 0
    for cells in rows:
        n = int(cells[0])
        for endpoint in (frac(cells[1]), frac(cells[2])):
            for a in range(1, n + 1):
                for b in range(a + 1, n + 1):
                    scaled = theta(endpoint, a, b) * S
                    l = int(scaled.floor().unique_fmpz())
                    u = l + 1
                    need(0 < l <= u < 3 * S and u - l <= 2)
                    q = Fraction(a * b) / ((endpoint + a) * (endpoint + b))
                    target = 1 - 2 * q
                    low_l, _, _, _ = cos_enclosure(l * l, S * S)
                    _, up_u, _, _ = cos_enclosure(u * u, S * S)
                    need(Fraction(low_l, B) > target and target > Fraction(up_u, B),
                         "inconclusive at n=%d pair (%d,%d)" % (n, a, b))
                    count += 1
    need(count == 908)
    return "908 intervals of width 1/2^128 certified by the 112-term recurrence on the grid 2^224"


@check("P1-A4", "exact", "Appendix B: failure mode - a too coarse grid is inconclusive, never a wrong sign")
def coarse_grid_is_safe():
    # With a coarse grid the enclosure widens but must still contain cos x.
    for grid_bits in (8, 16, 40):
        grid = 2 ** grid_bits
        for num in range(0, 401, 7):
            x = Fraction(num, 100)
            lower, upper, _, _ = cos_enclosure(num * num, 100 * 100, grid=grid)
            need(not_outside(ball(x).cos(), Fraction(lower, grid), Fraction(upper, grid)))
            need(upper - lower < 2 * TERMS + 4)
    return "enclosures remain valid at grids 2^8, 2^16, 2^40"
