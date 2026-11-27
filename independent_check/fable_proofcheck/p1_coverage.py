"""Sections 6.1, 6.3, 6.4 and Appendix C of Paper I: coverage and strictness.

``lower_coverage`` is a fresh implementation of the lower exclusion for the
linear family.  It does not read any certificate: integer weights come from
Arb enclosures of the kernel at the printed endpoint L_n.
"""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter
from fractions import Fraction

from p1_base import ball, check, frac, need, table_body, theta, tours, two_pi

S = 2 ** 128


def floor_lower(x) -> int:
    """An integer <= every point of the ball x."""
    return int(x.lower().floor().unique_fmpz())


def ceil_upper(x) -> int:
    """An integer >= every point of the ball x."""
    return int(x.upper().ceil().unique_fmpz())


def canonical(cycle):
    """Rotation/reflection normal form: largest label first, then the smaller neighbour."""
    n = len(cycle)
    i = cycle.index(max(cycle))
    rot = tuple(cycle[i:]) + tuple(cycle[:i])
    if rot[1] > rot[-1]:
        rot = (rot[0],) + tuple(reversed(rot[1:]))
    return rot


def cycle_cost(cycle, w):
    return sum(w[cycle[i], cycle[(i + 1) % len(cycle)]] for i in range(len(cycle)))


def held_karp(anchor, V, w):
    """D[mask][j]: least weight of a path anchor -> (labels of mask) ending at V[j]."""
    m = len(V)
    D = [[None] * m for _ in range(1 << m)]
    for j in range(m):
        D[1 << j][j] = w[anchor, V[j]]
    for mask in range(1, 1 << m):
        for j in range(m):
            if not mask >> j & 1 or mask == 1 << j:
                continue
            rest = mask ^ (1 << j)
            D[mask][j] = min(D[rest][i] + w[V[i], V[j]] for i in range(m) if rest >> i & 1)
    return D


def branch(anchor, V, w, T):
    """Depth-first traversal with the exact completion bound (12).

    Returns (P, retained oriented leaves, least pruning margin, root cost).
    """
    m = len(V)
    D = held_karp(anchor, V, w)
    full = (1 << m) - 1
    root = min(D[full][j] + w[V[j], anchor] for j in range(m))
    state = {"P": 0, "margin": None}
    leaves = []

    def prune(margin, completions):
        state["P"] += completions
        if state["margin"] is None or margin < state["margin"]:
            state["margin"] = margin

    if root > T:
        prune(root - T, math.factorial(m))
        return state["P"], leaves, state["margin"], root

    def visit(j, unvisited, cost, prefix):
        bound = cost + D[unvisited | (1 << j)][j]
        if bound > T:
            prune(bound - T, math.factorial(bin(unvisited).count("1")))
            return
        if not unvisited:
            leaves.append(tuple(prefix))
            return
        for nxt in range(m):
            if unvisited >> nxt & 1:
                prefix.append(V[nxt])
                visit(nxt, unvisited ^ (1 << nxt), cost + w[V[j], V[nxt]], prefix)
                prefix.pop()

    for first in range(m):
        visit(first, full ^ (1 << first), w[anchor, V[first]], [V[first]])
    return state["P"], leaves, state["margin"], root


@check("P1-V1", "exact", "Section 6.3: (n-1)!/2 classes; deleting label 1 is a bijection onto (skeleton class, gap)")
def class_counts():
    for n in range(3, 9):
        reps = {canonical(t) for t in tours(n)}
        need(len(reps) == math.factorial(n - 1) // 2)
        if n >= 4:
            pairs = Counter()
            for rep in reps:
                skeleton = canonical(tuple(x for x in rep if x != 1))
                pairs[skeleton] += 1
            need(len(pairs) == math.factorial(n - 2) // 2)
            need(set(pairs.values()) == {n - 1})
            # reflection fixes no oriented skeleton with >= 3 distinct labels
            for skeleton in pairs:
                need(skeleton[1] != skeleton[-1])
    return "n=3..8"


@check("P1-V2", "exact", "(11)-(13): DP is the exact least path; pruned set = {cost > T}; P+2K=(n-2)!")
def dp_and_pruning():
    rng = random.Random(42)
    trials = 0
    for size in (5, 6, 7, 8):  # skeleton size
        labels = list(range(2, size + 2))
        anchor, V = labels[-1], labels[:-1]
        for _ in range(6):
            w = {}
            for a, b in itertools.combinations(labels, 2):
                w[a, b] = w[b, a] = rng.randint(100, 999)
            costs = {perm: cycle_cost((anchor,) + perm, w) for perm in itertools.permutations(V)}
            T = sorted(costs.values())[rng.randint(0, len(costs) // 3)]
            D = held_karp(anchor, V, w)
            m = len(V)
            for j in range(m):  # exactness of the DP against brute force
                best = min(sum(w[x, y] for x, y in zip((anchor,) + p, p)) for p in itertools.permutations(V) if p[-1] == V[j])
                need(D[(1 << m) - 1][j] == best)
            P, leaves, margin, root = branch(anchor, V, w, T)
            need(root == min(costs.values()))
            need(set(leaves) == {p for p, c in costs.items() if c <= T} and len(leaves) == len(set(leaves)))
            need(P == sum(1 for c in costs.values() if c > T) and P % 2 == 0)
            K = len(leaves) // 2
            need(len({canonical((anchor,) + p) for p in leaves}) == K)
            need(P + 2 * K == math.factorial(size - 1))
            n = size + 1  # full problem obtained by restoring one deleted label
            need(Fraction(P * (n - 1), 2) + K * (n - 1) == Fraction(math.factorial(n - 1), 2))
            trials += 1
    return "%d random weighted skeletons against brute force" % trials


@check("P1-V3", "exact", "Appendix C: I_{n,k}=(n-1)!/(k-1)! full classes above each core; partition identity")
def lifting_counts():
    for n in range(4, 8):
        reps = {canonical(t) for t in tours(n)}
        for k in range(3, n + 1):
            d = n - k
            above = Counter(canonical(tuple(x for x in rep if x > d)) for rep in reps)
            need(len(above) == math.factorial(k - 1) // 2)
            need(set(above.values()) == {math.factorial(n - 1) // math.factorial(k - 1)})
            need(math.prod(range(k, n)) == math.factorial(n - 1) // math.factorial(k - 1))
    # the worked example of Section 9: n=14, d=4
    need(10 * 11 * 12 * 13 == math.factorial(13) // math.factorial(9))
    return "n=4..7, all admissible k"


def derivative_bound(L, a, b):
    qL = Fraction(a * b) / ((L + a) * (L + b))
    return max(Fraction(1), qL / (1 - qL)) * (1 / (L + a) + 1 / (L + b))


@check("P1-V4", "exact", "Section 6.4 and Appendix C: rational bounds on |d theta/dR| for R >= L")
def derivative_bounds():
    count = 0
    for L in (Fraction(1, 4), Fraction(26, 100), Fraction(3), Fraction(21)):
        for a, b in itertools.combinations(range(1, 15), 2):
            for R in (L, L + Fraction(1, 10**11), L + Fraction(1, 3), 4 * L, L + 1000):
                q = Fraction(a * b) / ((R + a) * (R + b))
                z = q / (1 - q)
                need(z == Fraction(a * b) / (R * (R + a + b)))
                total = 1 / (R + a) + 1 / (R + b)
                square = z * total * total  # (d theta/dR)^2, by P1-K4
                need(square <= derivative_bound(L, a, b) ** 2)
                need(square <= (Fraction(2 * 14) / (L * L)) ** 2)  # Appendix C with a_n = 14
                count += 1
    return "%d exact comparisons of squares" % count


def lower_coverage(n, R, T):
    """Exclude every cyclic order of 1..n at radius R; returns a summary dict."""
    w = {}
    for a, b in itertools.combinations(range(1, n + 1), 2):
        w[a, b] = w[b, a] = floor_lower(theta(R, a, b) * S)
        need(w[a, b] > 0)
    margin = None

    def violated(cycle):
        return cycle_cost(cycle, w) - T if len(cycle) >= 3 else 0

    def best_violation(full):
        # the three tests of Section 6.1: full order, delete 1, delete {1,2}
        return max(violated(full), violated(tuple(x for x in full if x > 1)),
                   violated(tuple(x for x in full if x > 2)))

    if n <= 9:
        classes = 0
        for tour in tours(n):
            excess = best_violation(tour)
            need(excess > 0, "n=%d order %s is not excluded" % (n, tour))
            margin = excess if margin is None else min(margin, excess)
            classes += 1
        return {"classes": classes, "explicit": classes, "K": None, "margin": margin}
    anchor, V = n, list(range(2, n))
    P, leaves, margin, root = branch(anchor, V, w, T)
    K = len(leaves) // 2
    canon = [leaf for leaf in leaves if leaf[0] < leaf[-1]]
    need(len(canon) == K and P % 2 == 0)
    need({tuple(reversed(leaf)) for leaf in canon} == set(leaves) - set(canon))  # K reversed leaves
    need(P + 2 * K == math.factorial(n - 2))
    seen = set()
    for leaf in canon:
        skeleton = (anchor,) + leaf
        for gap in range(n - 1):
            full = skeleton[:gap + 1] + (1,) + skeleton[gap + 1:]
            seen.add(canonical(full))
            excess = best_violation(full)
            need(excess > 0, "n=%d insertion %s is not excluded" % (n, full))
            margin = excess if margin is None else min(margin, excess)
    need(len(seen) == K * (n - 1))
    classes = P // 2 * (n - 1) + K * (n - 1)
    return {"classes": classes, "explicit": K * (n - 1), "K": K, "margin": margin}


@check("P1-V5", "interval", "Theorem 7.1 (lower side) and Table 3: fresh exclusion of every order at L_n and at L_n+eps_n")
def independent_lower_bound():
    brackets = {int(c[0]): (frac(c[1]), frac(c[2])) for c in (r.split("&") for r in table_body("tab:brackets"))}
    printed = {}
    for cells in (r.split("&") for r in table_body("tab:coverage")):
        skeletons = cells[3].strip()
        printed[int(cells[0])] = (int(cells[1].replace(",", "")), int(cells[2].replace(",", "")),
                                  None if skeletons == "--" else int(skeletons.replace(",", "")))
    T = ceil_upper(two_pi() * S)
    need(ball(T) > two_pi() * S)
    explicit_total = classes_total = 0
    for n in range(3, 15):
        L, U = brackets[n]
        result = lower_coverage(n, L, T)
        need(result["classes"] == math.factorial(n - 1) // 2)
        need((result["classes"], result["explicit"], result["K"]) == printed[n],
             "Table 3 row n=%d: recomputed %s" % (n, result))
        explicit_total += result["explicit"]
        classes_total += result["classes"]
        # Section 6.4: the rational buffer
        D = n * max(derivative_bound(L, a, b) for a, b in itertools.combinations(range(1, n + 1), 2))
        eps = Fraction(result["margin"], 2 * S * D)
        need(0 < eps < U - L)
        # direct confirmation of the buffer: every order is still excluded at L+eps,
        # and angles only grow below it, so Rstar(n) >= L+eps > L.
        again = lower_coverage(n, L + eps, T)
        need(again["classes"] == math.factorial(n - 1) // 2)
    need(explicit_total == 268648 and classes_total == 3374988556)
    return "n=3..14 excluded at L_n and at L_n+eps_n; counts equal Table 3 (268,648 explicit; 3,374,988,556 total)"


@check("P1-V6", "exact", "Sections 6.2, 6.5, 10: the reported totals 908, 47, 540, 3,004 and 6,008 follow from Table 2")
def reported_totals():
    from p1_base import paper_text

    witnesses = {int(c[0]): int(c[3]) for c in (r.split("&") for r in table_body("tab:brackets"))}
    need(sorted(witnesses) == list(range(3, 15)))
    intervals = 2 * sum(n * (n - 1) // 2 for n in witnesses)           # both endpoints
    total = sum(witnesses.values())
    tangencies = sum(count * n for n, count in witnesses.items())
    pairs = sum(count * n * (n - 1) // 2 for n, count in witnesses.items())
    need((intervals, total, tangencies, pairs, 2 * pairs) == (908, 47, 540, 3004, 6008))
    text = paper_text()
    for phrase in ("908 angle intervals", "47 witnesses", "540 central tangencies", "3,004 outer pairs",
                   "6,008 directed angular", "All 908 pair intervals", "47 Cartesian witnesses"):
        need(phrase in " ".join(text.split()), "phrase not found: %s" % phrase)
    return "908 intervals, 47 witnesses, 540 tangencies, 3,004 pairs, 6,008 directed inequalities"
