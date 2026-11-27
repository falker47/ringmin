"""Section 5 and Appendix A of Paper I: the seam criterion and persistence."""

from __future__ import annotations

import itertools
import random
from fractions import Fraction

from flint import arb

from p1_base import (ball, chain_sum, check, cycle_edges, hull, need,
                    root_bracket, sigma, theta, two_pi, undirected)

ONSETS = {1: 8, 2: 13, 3: 17}  # Table 1 of the paper


def edges_A5(k: int, n: int):
    """Edge list (A.5), in the printed list order."""
    N, L = n - k + 1, k + n
    if N % 2 == 0:
        h = N // 2
        need(h >= 2)
        edges = [(k, n), (k + h - 1, k + h)]
        edges += [(i, L - 1 - i) for i in range(k, k + h - 1)]
        edges += [(i, L + 1 - i) for i in range(k + 1, k + h)]
    else:
        h = (N - 1) // 2
        need(h >= 1)
        edges = [(k, n)]
        edges += [(i, L - 1 - i) for i in range(k, k + h)]
        edges += [(i, L + 1 - i) for i in range(k + 1, k + h + 1)]
    return edges


def delta(R, k, n) -> arb:
    return theta(R, n, k) + theta(R, k, n - 1) - theta(R, n, n - 1)


def kappa(k, n) -> arb:
    """(A.16)."""
    return (ball(Fraction(1, k) + Fraction(1, n) + Fraction(1, n - 1))
            - 2 * ball(Fraction(2 * n + k - 1, k * n * (n - 1))).sqrt())


def has_threshold(k, n) -> bool:
    """Exact test of P_n(0) < 1/k, i.e. alpha + 2 sqrt(beta) < 1/k."""
    alpha = Fraction(1, n) + Fraction(1, n - 1)
    beta = Fraction(1, n * (n - 1))
    gap = Fraction(1, k) - alpha
    return gap > 0 and 4 * beta < gap * gap


@check("P1-E1", "exact", "(A.5): explicit edge lists equal the rank-rule cycle, both parities")
def edge_lists():
    count = 0
    for k in range(1, 7):
        for n in range(k + 2, k + 260):
            cyc = sigma(k, n)
            listed = edges_A5(k, n)
            need(len(listed) == n - k + 1 == len(undirected(listed)))
            need(undirected(listed) == undirected(cycle_edges(cyc)), "k=%d n=%d" % (k, n))
            pos = cyc.index(k)
            need({cyc[pos - 1], cyc[(pos + 1) % len(cyc)]} == {n - 1, n})
            sums = {a + b for a, b in listed}
            need(sums <= {k + n - 1, k + n, k + n + 1})
            count += 1
    need(sigma(5, 7) == [5, 6, 7] and sigma(5, 8) == [5, 7, 6, 8])
    return "%d pairs (k,n); neighbours of k are n-1 and n" % count


@check("P1-E2", "exact", "Lemma A.1: the stated edge matching n -> n+1 is a bijection onto the new list minus one edge")
def growth_matching():
    count = 0
    for k in range(1, 7):
        for n in range(k + 2, k + 200):
            old, new = edges_A5(k, n), edges_A5(k, n + 1)
            N = n - k + 1
            if N % 2:  # N = 2h+1
                h = (N - 1) // 2
                image = [(a, b + 1) for a, b in old]
                extra = (k + h, k + h + 1)
            else:  # N = 2h: the central edge is retained unchanged
                h = N // 2
                image = [(k, n + 1), (k + h - 1, k + h)] + [(a, b + 1) for a, b in old[2:]]
                extra = (k + h, k + h + 1)
            need(len(undirected(image)) == len(old))
            need(undirected(image) | {frozenset(extra)} == undirected(new), "k=%d n=%d" % (k, n))
            need(frozenset(extra) not in undirected(image))
            count += 1
    return "%d steps: every old edge maps to an edge with endpoints >= the old ones, plus one new edge" % count


@check("P1-E3", "interval", "Lemma A.1 and (A.6): roots increase in n and exceed k(csc(pi/N)-1)")
def growth_roots():
    count = 0
    for k in (1, 2, 3, 4):
        previous_hi = None
        for n in range(k + 2, 46):
            edges = cycle_edges(sigma(k, n))
            lo, hi = root_bracket(edges, steps=70)
            if previous_hi is not None:
                need(chain_sum(edges, previous_hi) > two_pi())  # R_{k,n} > hi_{n-1} > R_{k,n-1}
            previous_hi = hi
            N = n - k + 1
            bound = k * (1 / (arb.pi() / N).sin() - 1)
            need(chain_sum(edges, bound) > two_pi())   # (A.6): R_{k,n} > k(csc(pi/N)-1)
            need(k * (N / arb.pi() - 1) < bound)
            count += 1
    return "%d roots" % count


@check("P1-E4", "interval", "Lemma A.2: least triangle defect and its equality case, brute force")
def triangle_defect():
    count = 0
    for k, n in [(1, 3), (1, 4), (1, 9), (2, 4), (2, 11), (3, 5), (3, 12), (5, 14)]:
        labels = list(range(k, n + 1))
        for R in (Fraction(1, 20), Fraction(1), Fraction(6), Fraction(51, 10), Fraction(32), Fraction(900)):
            th = {(x, y): theta(R, x, y) for x in labels for y in labels}
            d = th[n, k] + th[k, n - 1] - th[n, n - 1]
            for a, b, c in itertools.permutations(labels, 3):
                defect = th[a, b] + th[b, c] - th[a, c]
                if b == k and {a, c} == {n - 1, n}:
                    need(defect.overlaps(d))
                else:
                    need(defect > d, "k=%d n=%d R=%s (a,b,c)=%s" % (k, n, R, (a, b, c)))
                count += 1
    return "%d ordered triples; strict except b=k, {a,c}={n-1,n}" % count


@check("P1-E5", "interval", "(A.10): fan identity and the bound (m-1) delta_R on random simple paths")
def fan_identity():
    rng = random.Random(5)
    count = 0
    for _ in range(300):
        k = rng.randint(1, 4)
        n = k + rng.randint(3, 12)
        R = Fraction(rng.randint(1, 4000), 100)
        m = rng.randint(2, n - k)
        path = rng.sample(range(k, n + 1), m + 1)
        slack = sum((theta(R, path[i], path[i + 1]) for i in range(m)), arb(0)) - theta(R, path[0], path[m])
        fan = arb(0)
        for j in range(1, m):
            fan += theta(R, path[0], path[j]) + theta(R, path[j], path[j + 1]) - theta(R, path[0], path[j + 1])
        need((slack - fan).overlaps(arb(0)) and (slack - fan).rad() < arb(10) ** (-60))
        d = delta(R, k, n)
        if m >= 3 or not (path[1] == k and {path[0], path[2]} == {n - 1, n}):
            need(slack > (m - 1) * d)
        count += 1
    return "%d paths" % count


def classify(k, n):
    """Sign of Delta_{k,n} and full feasibility of the cumulative placement.

    All quantities are evaluated on a ball containing the root bracket, so
    every reported sign holds at the exact chain root.
    """
    cyc = sigma(k, n)
    N = len(cyc)
    lo, hi = root_bracket(cycle_edges(cyc))
    R = hull(lo, hi)
    gaps = [theta(R, cyc[i], cyc[(i + 1) % N]) for i in range(N)]
    prefix = [arb(0)]
    for g in gaps:
        prefix.append(prefix[-1] + g)
    d = delta(R, k, n)
    least_other = None
    feasible = True
    seam_pair = frozenset((n - 1, n))
    for i in range(N):
        for j in range(i + 1, N):
            need_angle = theta(R, cyc[i], cyc[j])
            plus = prefix[j] - prefix[i]
            minus = two_pi() - plus  # exact complement at the root
            adjacent_plus = j == i + 1
            adjacent_minus = i == 0 and j == N - 1
            for length, adjacent, steps in ((plus, adjacent_plus, j - i), (minus, adjacent_minus, N - (j - i))):
                if adjacent:
                    continue  # one-edge path: slack is zero by construction
                slack = length - need_angle
                is_seam = steps == 2 and frozenset((cyc[i], cyc[j])) == seam_pair and (
                    cyc[(i + 1) % N] == k if length is plus else cyc[(j + 1) % N] == k)
                if is_seam:
                    need(slack.overlaps(d))
                    continue
                need(slack > 0 or slack < 0, "undecided slack k=%d n=%d" % (k, n))
                if slack < 0:
                    feasible = False
                if least_other is None or slack < least_other:
                    least_other = slack
    need(d > 0 or d < 0, "seam deficit sign undecided at k=%d n=%d" % (k, n))
    if d < 0:
        feasible = False
    return d, feasible, least_other, (lo, hi)


@check("P1-E6", "interval", "Theorem 5.1(1): feasible at the chain root <=> Delta >= 0 (all pairs, both arcs)")
def seam_criterion():
    count = 0
    for k in (1, 2, 3, 4):
        for n in range(k + 2, 34):
            d, feasible, least_other, _ = classify(k, n)
            need(feasible == (d > 0), "k=%d n=%d" % (k, n))
            if n - k + 1 >= 4 and d > 0:
                # the seam is the unique least nonadjacent slack (Appendix A.4)
                need(least_other > d)
            count += 1
    return "%d cycles: every nonadjacent directed path checked" % count


@check("P1-E7", "interval", "Table 1 / Theorem 5.1(3): signs of Delta_{k,n} and onsets 8, 13, 17")
def onset_table():
    out = []
    for k, s in ONSETS.items():
        for n in range(k + 2, 71):
            lo, hi = root_bracket(cycle_edges(sigma(k, n)), steps=70)
            d = delta(hull(lo, hi), k, n)
            need((d > 0) if n < s else (d < 0), "k=%d n=%d" % (k, n))
        out.append("k=%d: + on %d..%d, - on %d..70" % (k, k + 2, s - 1, s))
    return "; ".join(out)


@check("P1-E8", "exact", "(A.12)-(A.16): Descartes-pocket identities as polynomial identities")
def pocket_identities():
    # q is treated as an independent symbol; each identity holds modulo
    # q^2 = x(u+v)+uv, which is what "follow by squaring" asserts.
    grid = [Fraction(1, 5), Fraction(2, 3), Fraction(3), Fraction(7, 2)]
    count = 0
    for x, u, v, q in itertools.product(grid, repeat=4):
        rel = q * q - (x * (u + v) + u * v)
        w = x + u + v + 2 * q
        need((x + u + q) ** 2 - (x * u + (x + u) * w) == rel)
        need((x + v + q) ** 2 - (x * v + (x + v) * w) == rel)
        need((x + u + q) * (x + v + q) - x * x - q * (2 * x + u + v + 2 * q) == -rel)
        # tangent addition: [t1+t2]/(1-t1 t2) with t1=x/(x+u+q), t2=x/(x+v+q)
        num = x * (x + v + q) + x * (x + u + q)
        den = (x + u + q) * (x + v + q) - x * x
        need(num * q - x * den == x * rel)
        count += 1
    # (A.12): ab/(R(R+a+b)) = x^2/(x(u+v)+uv) with x=1/R, u=1/a, v=1/b
    for R, a, b in itertools.product(grid, repeat=3):
        x, u, v = 1 / R, 1 / a, 1 / b
        need(a * b / (R * (R + a + b)) == x * x / (x * (u + v) + u * v))
    # (A.16): with c=1/k, q_n^2 = alpha c + beta, kappa = c + alpha - 2 q_n
    for alpha, beta, c, qn in itertools.product(grid, repeat=4):
        rel = qn * qn - (alpha * c + beta)
        kap = c + alpha - 2 * qn
        need(alpha * kap + beta - (qn - alpha) ** 2 == -rel)
        need(qn * qn - alpha * alpha - (alpha * (c - alpha) + beta) == rel)
        # squared crossing equation: x^2 - 2(c+alpha)x + (c-alpha)^2 - 4 beta = 0 at kappa
        need(kap * kap - 2 * (c + alpha) * kap + (c - alpha) ** 2 - 4 * beta == 4 * rel)
    return "%d grid points per identity" % count


@check("P1-E9", "interval", "(A.13),(A.15): pocket radius 1/w fills the gap; sign of delta_R = sign(P_n(1/R)-1/k)")
def pocket_sign():
    count = 0
    for a, b in [(7, 6), (13, 12), (40, 39), (5, 2)]:
        for R in (Fraction(1, 3), Fraction(4), Fraction(57)):
            x, u, v = ball(1 / Fraction(R)), ball(Fraction(1, a)), ball(Fraction(1, b))
            w = x + u + v + 2 * (x * (u + v) + u * v).sqrt()
            rho = 1 / w
            diff = theta(R, a, rho) + theta(R, rho, b) - theta(R, a, b)
            need(diff.overlaps(arb(0)) and diff.rad() < arb(10) ** (-60))
            count += 1
    for k in range(1, 6):
        for n in range(k + 2, 40):
            alpha, beta = Fraction(1, n) + Fraction(1, n - 1), Fraction(1, n * (n - 1))
            for R in (Fraction(1, 7), Fraction(2), Fraction(11), Fraction(32), Fraction(500)):
                P = ball(1 / R) + ball(alpha) + 2 * (ball(alpha / R + beta)).sqrt()
                d = delta(R, k, n)
                side = P - ball(Fraction(1, k))
                need((d > 0 and side > 0) or (d < 0 and side < 0), "k=%d n=%d R=%s" % (k, n, R))
                count += 1
    return "%d samples" % count


@check("P1-E10", "exact", "Appendix A.5: P_4k(0) > 1/k > P_4k+1(0); threshold exists exactly for n >= 4k+1")
def threshold_domain():
    for k in range(1, 400):
        need(not has_threshold(k, 4 * k))
        need(has_threshold(k, 4 * k + 1))
        for n in range(k + 2, 4 * k + 1):
            need(not has_threshold(k, n))
        for n in range(4 * k + 1, 4 * k + 60):
            need(has_threshold(k, n))
            # kappa > 0 exactly: (1/k+alpha)^2 > 4(alpha/k+beta)
            alpha, beta = Fraction(1, n) + Fraction(1, n - 1), Fraction(1, n * (n - 1))
            need((Fraction(1, k) + alpha) ** 2 > 4 * (alpha / k + beta))
    return "k=1..399"


@check("P1-E11", "interval", "Appendix A.5: T_{k,n} decreases, R_{k,n}-T_{k,n} increases; sign Delta = -sign(R-T)")
def persistence():
    count = 0
    for k in (1, 2, 3, 4, 5):
        previous_T = None
        previous_gap = None
        first_negative = None
        for n in range(4 * k + 1, 4 * k + 40):
            need(has_threshold(k, n))
            kap = kappa(k, n)
            need(kap > 0)
            T = 1 / kap
            need(T > k)
            if previous_T is not None:
                need(T < previous_T)
            previous_T = T
            lo, hi = root_bracket(cycle_edges(sigma(k, n)), steps=70)
            R = hull(lo, hi)
            gap = R - T
            if previous_gap is not None:
                need(gap > previous_gap)
            previous_gap = gap
            d = delta(R, k, n)
            need((d < 0 and gap > 0) or (d > 0 and gap < 0))
            if first_negative is None and d < 0:
                first_negative = n
            count += 1
        if k in ONSETS:
            need(first_negative == ONSETS[k])
        need(first_negative is not None and first_negative >= 4 * k + 1)
    return "%d (k,n) with a finite threshold; s_k >= 4k+1 observed for k<=5" % count


@check("P1-E12", "interval", "Corollary 5.2 vs Table 2: L_n < R_{1,n} <= U_n for n=3..7, R_{1,n} < L_n for n=8..14")
def corollary_against_brackets():
    from p1_base import frac, table_body

    rows = [row.split("&") for row in table_body("tab:brackets")]
    need(len(rows) == 12)
    out = []
    for cells in rows:
        n, L, U = int(cells[0]), frac(cells[1]), frac(cells[2])
        need(U - L == Fraction(1, 10**11))
        edges = cycle_edges(sigma(1, n))
        if n <= 7:
            need(chain_sum(edges, L) > two_pi())   # R_{1,n} > L_n
            need(chain_sum(edges, U) < two_pi())   # R_{1,n} < U_n
            d, feasible, _, _ = classify(1, n)
            need(feasible and d > 0)
        else:
            need(chain_sum(edges, L) < two_pi())   # chain bound strictly below L_n
            out.append(n)
    return "n=3..7 inside the certified bracket; chain root below L_n for n in %s" % out
