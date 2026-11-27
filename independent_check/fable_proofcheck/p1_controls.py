"""Negative controls for Paper I: false variants that the checks must reject."""

from __future__ import annotations

from fractions import Fraction

from p1_base import chain_sum, control, cycle_edges, frac, hull, need, root_bracket, sigma, table_body, two_pi
from p1_cosine import S, cos_enclosure
from p1_coverage import ceil_upper, lower_coverage
from p1_seam import delta, edges_A5
from p1_supnick import cut_bound, cut_counts


@control("P1-X1", "the pyramid order 1,3,5,7,8,6,4,2 attains every cut bound")
def pyramid_is_not_supnick():
    N = 8
    X = cut_counts([1, 3, 5, 7, 8, 6, 4, 2], N)
    for p in range(1, N):
        for q in range(p, N):
            need(X[p][q] == cut_bound(N, p, q))


@control("P1-X2", "the seam deficit is still positive at (k,n)=(1,8)")
def onset_one_later():
    lo, hi = root_bracket(cycle_edges(sigma(1, 8)))
    need(delta(hull(lo, hi), 1, 8) > 0)


@control("P1-X3", "the bridge R_{1,8} > 6 (the paper uses 51/10)")
def wrong_separator():
    need(chain_sum(edges_A5(1, 8), 6) > two_pi())


@control("P1-X4", "Table 7 with the first numerator of row (1,7) lowered from 28 to 27")
def tampered_edge_bound():
    q = Fraction(27, 100)
    need(q * q - Fraction(1 * 7) / ((6 + 1) * (6 + 7)) > 0)


@control("P1-X5", "every order of 1..6 is excluded at the upper endpoint U_6")
def exclusion_at_upper_endpoint():
    rows = {int(c[0]): frac(c[2]) for c in (r.split("&") for r in table_body("tab:brackets"))}
    lower_coverage(6, rows[6], ceil_upper(two_pi() * S))


@control("P1-X6", "T_- - 1 and T_- bracket 2 pi 2^128")
def shifted_circumference():
    t_minus = 2138057168129933495719360746323741566601
    _, upper, _, _ = cos_enclosure(t_minus ** 2, (4 * S) ** 2)
    need(upper < 0)
