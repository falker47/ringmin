"""Section 3 of Paper I: the Supnick tour and Theorem 3.2 (chain optimization).

The paper imports Supnick's extreme-tour theorem.  The checks below do not
rely on the citation.  For a symmetric matrix c with Monge second differences
D[p][q] = c[p][q] + c[p+1][q+1] - c[p][q+1] - c[p+1][q] <= 0 one has, for
every tour t,

    cost(t) = const + sum_{p<q} (-D[p][q]) X_t(p,q) + sum_p (-D[p][p]) X_t(p,p)/2,

where X_t(p,q) counts the tour edges joining {1..p} to {q+1..N}.  Degree and
forest counting give X_t(p,q) <= min(2p, 2(N-q), p+N-q-1) for p<q and
X_t(p,p) <= 2 min(p, N-p).  A tour attaining every bound simultaneously is
therefore a maximum-cost tour for every symmetric Monge matrix, i.e. a
minimum-angle tour for the anti-Monge kernel.
"""

from __future__ import annotations

import itertools
import random
from fractions import Fraction

from p1_base import (chain_sum, check, cycle_edges, need, rank_cycle, theta,
                    tours, undirected)


def zigzag(N: int) -> list[int]:
    """<N,2,N-2,4,N-4,...,5,N-3,3,N-1,1>, built without the threshold H."""
    used = {N, 1}
    left, right = [N], [1]
    t = 1
    while len(used) < N:
        cand_left = t + 1 if t % 2 else N - t          # 2, N-2, 4, N-4, ...
        cand_right = N - t if t % 2 else t + 1         # N-1, 3, N-3, 5, ...
        if cand_left not in used and 1 <= cand_left <= N:
            left.append(cand_left)
            used.add(cand_left)
        if cand_right not in used and 1 <= cand_right <= N:
            right.append(cand_right)
            used.add(cand_right)
        t += 1
        need(t <= 2 * N + 2, "zigzag did not terminate")
    return left + right[::-1]


def cut_counts(cycle, N):
    """X[p][q] = number of edges {i,j} with min <= p and max > q (p <= q)."""
    grid = [[0] * (N + 2) for _ in range(N + 2)]
    for u, v in cycle_edges(cycle):
        grid[min(u, v)][max(u, v)] += 1
    # prefix over low endpoint, suffix over high endpoint
    X = [[0] * (N + 1) for _ in range(N + 1)]
    for p in range(1, N):
        running = [0] * (N + 2)
        for hi in range(N, 0, -1):
            running[hi] = running[hi + 1] + sum(grid[lo][hi] for lo in range(1, p + 1))
        for q in range(p, N):
            X[p][q] = running[q + 1]
    return X


def cut_bound(N, p, q):
    if p == q:
        return 2 * min(p, N - p)
    return min(2 * p, 2 * (N - q), p + N - q - 1)


@check("P1-S1", "exact", "Section 3: rank rule yields a Hamiltonian cycle; printed examples")
def rank_rule():
    need(rank_cycle(4) == [1, 3, 2, 4])
    need(rank_cycle(7) == [1, 6, 3, 4, 5, 2, 7])
    need(rank_cycle(3) == [1, 2, 3])
    for N in range(3, 601):
        cyc = rank_cycle(N)
        need(sorted(cyc) == list(range(1, N + 1)), "N=%d is not a permutation" % N)
        if N >= 4:
            need(cyc[0] == 1 and cyc[1] == N - 1 and cyc[-1] == N)
    return "N=3..600"


@check("P1-S2", "exact", "Section 3: rank cycle = Supnick zigzag <N,2,N-2,...,3,N-1,1>")
def equals_zigzag():
    for N in range(3, 601):
        need(undirected(cycle_edges(rank_cycle(N))) == undirected(cycle_edges(zigzag(N))),
             "N=%d differs from the zigzag tour" % N)
    return "edge sets equal for N=3..600"


@check("P1-S3", "exact", "Theorem 3.2: rank cycle attains every cut bound (optimal for all Monge matrices)")
def attains_cut_bounds():
    for N in range(3, 161):
        X = cut_counts(rank_cycle(N), N)
        for p in range(1, N):
            for q in range(p, N):
                need(X[p][q] == cut_bound(N, p, q), "N=%d p=%d q=%d" % (N, p, q))
    return "all (p,q), N=3..160"


@check("P1-S4", "exact", "Theorem 3.2: cut bounds are valid and tight; uniqueness (all tours, N<=9)")
def brute_force_cuts():
    total = 0
    for N in range(3, 10):
        best = cut_counts(rank_cycle(N), N)
        star = undirected(cycle_edges(rank_cycle(N)))
        attained_by = 0
        for tour in tours(N):
            X = cut_counts(tour, N)
            equal = True
            for p in range(1, N):
                for q in range(p, N):
                    need(X[p][q] <= best[p][q], "N=%d: a tour beats the rank cycle" % N)
                    equal = equal and X[p][q] == best[p][q]
            attained_by += equal
            need(equal == (undirected(cycle_edges(tour)) == star))
            total += 1
        need(attained_by == 1)
    return "%d tours; the rank cycle is the unique simultaneous maximizer" % total


@check("P1-S5", "exact", "Theorem 3.2: cut-count cost formula and max tour on random integer Monge matrices")
def monge_matrices():
    rng = random.Random(20261124)
    trials = 0
    for N in range(4, 9):
        star = rank_cycle(N)
        for _ in range(12):
            first = [rng.randint(-50, 50) for _ in range(N + 1)]
            D = [[0] * (N + 1) for _ in range(N + 1)]
            for p in range(1, N):
                for q in range(p, N):
                    D[p][q] = D[q][p] = -rng.randint(0, 9)
            c = [[0] * (N + 1) for _ in range(N + 1)]
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    c[i][j] = first[i] + first[j] - first[1] + sum(
                        D[p][q] for p in range(1, i) for q in range(1, j))
            for i, r in itertools.combinations(range(1, N + 1), 2):
                need(all(c[i][j] == c[j][i] for j in range(1, N + 1)))
                for j, s in itertools.combinations(range(1, N + 1), 2):
                    need(c[i][j] + c[r][s] <= c[i][s] + c[r][j])  # Monge, diagonal included
            const = 2 * sum(first[1:]) - N * first[1]

            def formula(tour):
                X = cut_counts(tour, N)
                value = Fraction(const)
                for p in range(1, N):
                    for q in range(p, N):
                        if p == q:
                            value += D[p][p] * (N - p - Fraction(X[p][p], 2))
                        else:
                            value += D[p][q] * (2 * (N - q) - X[p][q])
                return value

            def cost(tour):
                return sum(c[u][v] for u, v in cycle_edges(tour))

            top = cost(star)
            for tour in tours(N):
                need(cost(tour) == formula(tour))
                need(cost(tour) <= top)
            trials += 1
    return "%d random symmetric Monge matrices, all tours" % trials


@check("P1-S6", "interval", "Theorem 3.2: minimum angle sum at fixed R for the actual kernel (all tours)")
def kernel_optimality():
    rng = random.Random(7)
    cases = 0
    for N in range(4, 9):
        for _ in range(3):
            pool = rng.sample(range(1, 400), N)
            radii = sorted(Fraction(v, rng.choice([1, 2, 3, 7])) for v in pool)
            need(len(set(radii)) == N)
            star = [radii[i - 1] for i in rank_cycle(N)]
            star_set = undirected(cycle_edges(star))
            for R in (Fraction(1, 9), Fraction(4), Fraction(250)):
                best = chain_sum(cycle_edges(star), R)
                for tour in tours(N):
                    other = [radii[i - 1] for i in tour]
                    if undirected(cycle_edges(other)) == star_set:
                        continue
                    need(chain_sum(cycle_edges(other), R) > best)
                cases += 1
    return "%d (radii, R) cases with arbitrary distinct rational radii" % cases


@check("P1-S7", "interval", "Theorem 3.2: chain root of the Supnick order is minimal (all tours, N<=7)")
def root_optimality():
    from p1_base import root_bracket, two_pi

    rng = random.Random(11)
    cases = 0
    for N in range(4, 8):
        radii = sorted(rng.sample(range(1, 60), N))
        star = [radii[i - 1] for i in rank_cycle(N)]
        lo, hi = root_bracket(cycle_edges(star))
        for tour in tours(N):
            other = [radii[i - 1] for i in tour]
            if undirected(cycle_edges(other)) == undirected(cycle_edges(star)):
                continue
            # C_other(hi) > 2 pi  =>  Rchain(other) > hi > Rchain(star)
            need(chain_sum(cycle_edges(other), hi) > two_pi())
            cases += 1
        need(theta(lo, 1, 1) > 0)
    return "%d competing orders have a strictly larger chain root" % cases
