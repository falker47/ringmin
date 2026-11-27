"""Appendix A.6 of Paper I: the six rational bridges (A.18)-(A.21), Tables 6-8.

Every printed rational is re-derived exactly from the manuscript source and
then the six inequalities are confirmed a second time with Arb, without the
paper's elementary estimates.
"""

from __future__ import annotations

import re
from fractions import Fraction

from flint import arb

from p1_base import ball, chain_sum, check, frac, need, pair, paper_text, table_body, two_pi
from p1_seam import edges_A5, has_threshold, kappa

BRIDGES = {  # (A.18): (k,n) -> (separator, relation of the root to the separator)
    (1, 7): (Fraction(6), "below"),
    (1, 8): (Fraction(51, 10), "above"),
    (2, 12): (Fraction(17), "below"),
    (2, 13): (Fraction(14), "above"),
    (3, 16): (Fraction(32), "below"),
    (3, 17): (Fraction(32), "above"),
}


def cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.split("&")]


@check("P1-B1", "exact", "(A.18): the six separators are the ones used in Tables 6-8")
def separators():
    text = paper_text()
    block = text[text.index("\\tag{A.18}") - 400:text.index("\\tag{A.18}")]
    found = re.findall(r"R_\{(\d),(\d+)\}<(\d+)<T_\{\1,\2\}|T_\{(\d),(\d+)\}<([\d/]+)<R_\{\4,\5\}", block)
    seen = {}
    for k1, n1, r1, k2, n2, r2 in found:
        if k1:
            seen[int(k1), int(n1)] = (Fraction(r1), "below")
        else:
            seen[int(k2), int(n2)] = (Fraction(r2), "above")
    need(seen == BRIDGES, "printed (A.18) differs: %r" % seen)
    for (k, n) in BRIDGES:
        need(has_threshold(k, n))  # "all six rows lie in the positive-threshold domain"
    return "6 bridges parsed from the manuscript"


@check("P1-B2", "exact", "Table 6: h, v, square margins and the direction of each threshold comparison")
def threshold_sides():
    rows = [cells(row) for row in table_body("tab:seam2")]
    need(len(rows) == 6)
    for row in rows:
        k, n = pair(row[0])
        r, h_printed, v_printed = frac(row[1]), frac(row[2]), frac(row[3])
        need(BRIDGES[k, n][0] == r)
        alpha, beta = Fraction(1, n) + Fraction(1, n - 1), Fraction(1, n * (n - 1))
        h = Fraction(1, k) + alpha - 1 / r
        v = 4 * (alpha / k + beta)
        need(h == h_printed and v == v_printed and h > 0 and v > 0, "(%d,%d)" % (k, n))
        margin = re.fullmatch(r"\$(v-h\^2|h\^2-v)=(\d+/\d+)\$", row[4])
        need(margin is not None)
        value = Fraction(margin.group(2))
        if margin.group(1) == "v-h^2":
            # kappa - 1/r = h - sqrt(v) < 0  =>  T > r
            need(v - h * h == value and value > 0)
            need(BRIDGES[k, n][1] == "below" and "r<T" in row[5])
        else:
            need(h * h - v == value and value > 0)
            need(BRIDGES[k, n][1] == "above" and "<r" in row[5])
        # the identity kappa - 1/r = h - sqrt(v), confirmed with Arb
        need((kappa(k, n) - ball(1 / r) - (ball(h) - ball(v).sqrt())).overlaps(arb(0)))
    return "6 rows reproduce exactly"


def edge_table():
    out = {}
    for row in (cells(r) for r in table_body("tab:seam3")):
        k, n = pair(row[0])
        d = int(row[3])
        numerators = [int(x) for x in row[4].split(",")]
        out[k, n] = (frac(row[1]), row[2], [Fraction(x, d) for x in numerators])
    return out


@check("P1-B3", "exact", "Table 7 and (A.19): rational edge bounds in the list order of (A.5); minimum margins")
def edge_bounds():
    table = edge_table()
    need(set(table) == set(BRIDGES))
    text = paper_text()
    block = text[text.index("respectively,", text.index("\\label{tab:seam3}")):text.index("\\tag{A.19}")]
    printed_minima = [Fraction(int(a), int(b)) for a, b in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", block)]
    need(len(printed_minima) == 6)
    minima = []
    for (k, n) in BRIDGES:  # same row order as the table
        r, direction, qs = table[k, n]
        edges = edges_A5(k, n)
        need(len(qs) == len(edges) and r == BRIDGES[k, n][0])
        need(direction == ("upper" if BRIDGES[k, n][1] == "below" else "lower"))
        margins = []
        for (a, b), q in zip(edges, qs):
            z2 = Fraction(a * b) / ((r + a) * (r + b))
            margins.append(q * q - z2 if direction == "upper" else z2 - q * q)
            need(q > 0 and margins[-1] > 0, "(%d,%d) edge %s" % (k, n, (a, b)))
        minima.append(min(margins))
    need(minima == printed_minima, "minimum margins: %s" % minima)
    # the worked example below Table 7
    need(Fraction(28, 100) ** 2 - Fraction(1, 13) == Fraction(12, 8125))
    # "an even row includes its central edge as the second entry"
    for (k, n) in BRIDGES:
        if (n - k + 1) % 2 == 0:
            h = (n - k + 1) // 2
            need(edges_A5(k, n)[1] == (k + h - 1, k + h))
    return "all %d edge comparisons positive; minima equal (A.19)" % sum(len(v[2]) for v in table.values())


@check("P1-B4", "exact", "(A.20),(A.21) and 3 < pi < 22/7: elementary estimates used for the chain sides")
def elementary_estimates():
    # (1+3u^2/5)^2 (1-u^2) - 1 = u^2 (5-21u^2-9u^4)/25 : degree 6 identity, 9 points
    for num in range(-4, 5):
        u = Fraction(num, 3)
        need((1 + 3 * u * u / 5) ** 2 * (1 - u * u) - 1 == u * u * (5 - 21 * u * u - 9 * u ** 4) / 25)
    need(5 - Fraction(21, 9) - Fraction(9, 81) == Fraction(23, 9))
    # 2/sqrt(3) < 6/5 by squaring; 1/sqrt(1-z^2) < 2/sqrt(3) for z < 1/2
    need(Fraction(4, 3) < Fraction(36, 25) and 1 / (1 - Fraction(1, 4)) == Fraction(4, 3))
    # x^4(1-x)^4 = (1+x^2)(x^6-4x^5+5x^4-4x^2+4) - 4  (degree 8, 11 points)
    for num in range(-5, 6):
        x = Fraction(num, 4)
        need(x ** 4 * (1 - x) ** 4 == (1 + x * x) * (x ** 6 - 4 * x ** 5 + 5 * x ** 4 - 4 * x * x + 4) - 4)
    # integral of the quotient polynomial on [0,1] is 22/7, hence 22/7 - pi = integral > 0
    need(Fraction(1, 7) - Fraction(4, 6) + 1 - Fraction(4, 3) + 4 == Fraction(22, 7))
    need(arb.pi() > 3 and arb.pi() < ball(Fraction(22, 7)))
    # Arb confirmation of the two arcsin estimates on a grid of their domains
    for num in range(1, 50):
        z = Fraction(num, 100)
        need(ball(z).asin() < ball(Fraction(6, 5) * z))
        if 3 * z <= 1:
            need(ball(z).asin() < ball(z + z ** 3 / 5))
        need(ball(z).asin() > ball(z))
    return "polynomial identities exact; estimates confirmed on a grid"


@check("P1-B5", "exact", "Table 8: the six closure comparisons, as exact rational sums")
def chain_sides():
    table = edge_table()
    rows = {pair(cells(row)[0]): cells(row) for row in table_body("tab:seam4")}
    need(set(rows) == set(BRIDGES))
    for (k, n), (r, direction, qs) in table.items():
        printed = Fraction(re.search(r"=(\d+/\d+)\$", rows[k, n][1]).group(1))
        if direction == "lower":
            total = sum(qs)
            need(total == printed and total > Fraction(22, 7), "(%d,%d)" % (k, n))
            need("\\sum q_e=" in rows[k, n][1] and ">22/7" in rows[k, n][2])
        elif "(6/5)" in rows[k, n][1]:
            need(all(q < Fraction(1, 2) for q in qs))
            total = Fraction(6, 5) * sum(qs)
            need(total == printed and total < 3, "(%d,%d)" % (k, n))
        else:
            need(all(3 * q <= 1 for q in qs))
            total = sum(q + q ** 3 / 5 for q in qs)
            need(total == printed and total < 3, "(%d,%d)" % (k, n))
    return "6 sums reproduce exactly; each side of pi is strict"


@check("P1-B6", "interval", "(A.18): all six bridges confirmed directly with Arb (no elementary estimate)")
def bridges_direct():
    out = []
    for (k, n), (r, side) in BRIDGES.items():
        T = 1 / kappa(k, n)
        C = chain_sum(edges_A5(k, n), r)
        if side == "below":   # R_{k,n} < r < T_{k,n}
            need(C < two_pi() and ball(r) < T)
        else:                 # T_{k,n} < r < R_{k,n}
            need(C > two_pi() and T < ball(r))
        out.append("(%d,%d)" % (k, n))
    return "verified " + " ".join(out)
