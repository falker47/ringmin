#!/usr/bin/env python3
"""Ringmin: fresh global-bracket candidate, standard library only (Python >=3.9).

Recomputes exact outward angular enclosures and a NEW complete combinatorial
lower-bound argument. Constructs and checks rational all-pairs feasible
placements at U. No historical float64 lower bound, Top-K, pickle, solver,
network or repository content is read or trusted for the proof computation.

The decimal test radii and trial orders below are explicit inputs taken from
pinned historical evidence. Their source is provenance, NOT an assumption
that the reported radii are correct. Every necessary inequality is recomputed.

Writes ONE new report in --output-dir (outside Git worktrees/checkpoints).
PASS_GLOBAL_BRACKET_CANDIDATE is a computer-assisted certificate candidate;
it is not external review, formal verification, journal readiness or acceptance
of a new repository/Registry baseline. See ringmin_global_interval_proof.md.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import platform
import random
import sys
import time
import uuid
from datetime import datetime, timezone

VERSION = "0.1.0"
REFERENCE_COMMIT = "c0d9d6e66afc8ec94918adbe23345bdc7a7fa43b"
SOURCE_EVIDENCE_ZIP_SHA256 = "ab93503aa6d06b8661c48a54469b88e1b6395cab043d9c1ba39fafb3e9adf9b7"
SCALE = 1 << 128
SQRT_SCALE = 1 << 192
SERIES_TARGET = Fraction(1, 1 << 176)
# A constructive positive angular slack, NOT an error tolerance.
PLACEMENT_PAD = (SCALE + 10**16 - 1) // 10**16

CASES = json.loads(r'''[{"n":3,"L":"0.26086956521","U":"0.26086956522","orders":[[3,1,2]],"frontier_blob":"12370624c97aae77177090fb3ec4aeb91adf0554"},{"n":4,"L":"0.84445358956","U":"0.84445358957","orders":[[4,1,3,2]],"frontier_blob":"f4443fbc2d78bbdbee720dab54bedd582f3485cf"},{"n":5,"L":"1.6954940812","U":"1.69549408121","orders":[[5,1,4,3,2]],"frontier_blob":"b0da48c7fb11f3867e0e562c958a40fdf5bca4ab"},{"n":6,"L":"2.79491951889","U":"2.7949195189","orders":[[6,1,5,3,4,2]],"frontier_blob":"37915150b0992a6fe017aaa3045be3c61360cb82"},{"n":7,"L":"4.15318955374","U":"4.15318955375","orders":[[7,1,6,3,4,5,2]],"frontier_blob":"02b09a343fe3cab4ddc45657bd798c50c78ebe0a"},{"n":8,"L":"5.76779428458","U":"5.76779428459","orders":[[8,1,6,4,5,3,7,2]],"frontier_blob":"4888f41f4de76bb3c40c9f757f1c5a1eea54de8a"},{"n":9,"L":"7.72672655261","U":"7.72672655262","orders":[[9,2,8,1,5,6,4,7,3]],"frontier_blob":"de0ed201769d4f2fd39c3b0c7abdc955c154d681"},{"n":10,"L":"9.97990738586","U":"9.97990738587","orders":[[10,2,9,4,7,1,6,5,8,3],[10,2,9,4,7,6,5,1,8,3],[10,2,9,1,4,7,6,5,8,3],[10,2,9,4,7,6,1,5,8,3]],"frontier_blob":"03168df1c34b6f1f5ce8961af381993ee078880a"},{"n":11,"L":"12.48872048718","U":"12.48872048719","orders":[[11,2,10,4,8,1,6,7,5,9,3],[11,2,10,4,8,6,7,5,1,9,3],[11,2,10,4,8,6,1,7,5,9,3],[11,2,10,1,4,8,6,7,5,9,3],[11,2,10,4,8,6,7,1,5,9,3],[11,2,10,4,1,8,6,7,5,9,3]],"frontier_blob":"d53c982703bf2629b212eef11724962f0da63144"},{"n":12,"L":"15.25887043044","U":"15.25887043045","orders":[[12,2,11,4,9,6,7,1,8,5,10,3],[12,2,11,4,9,1,6,7,8,5,10,3],[12,2,11,4,9,6,7,8,5,1,10,3],[12,2,11,4,9,6,1,7,8,5,10,3],[12,2,11,4,9,6,7,8,1,5,10,3],[12,2,11,1,4,9,6,7,8,5,10,3],[12,2,11,4,1,9,6,7,8,5,10,3],[12,1,3,10,5,8,7,6,9,4,11,2],[12,2,11,4,9,6,7,8,5,10,1,3]],"frontier_blob":"dda8986e4cdf168a3c702136c6f1a85c8ecf660e"},{"n":13,"L":"18.31756304721","U":"18.31756304722","orders":[[13,1,4,11,5,9,7,8,6,10,2,12,3],[13,3,12,2,10,6,8,7,1,9,5,11,4],[13,3,12,2,10,1,6,8,7,9,5,11,4],[13,3,12,2,10,6,8,1,7,9,5,11,4],[13,3,12,2,10,6,8,7,9,5,1,11,4],[13,3,12,2,10,6,1,8,7,9,5,11,4],[13,3,12,2,10,6,8,7,9,1,5,11,4],[13,3,12,2,10,6,8,7,9,5,11,1,4],[13,1,3,12,2,10,6,8,7,9,5,11,4],[13,3,1,12,2,10,6,8,7,9,5,11,4]],"frontier_blob":"106d3f91aa61d687f43ab279865ce81fa22fc19b"},{"n":14,"L":"21.66539518221","U":"21.66539518222","orders":[[14,3,13,2,9,1,8,7,10,6,11,5,12,4],[14,3,13,2,9,8,7,1,10,6,11,5,12,4],[14,3,13,2,9,8,7,10,6,1,11,5,12,4],[14,3,13,2,9,8,7,10,1,6,11,5,12,4],[14,3,13,2,9,8,1,7,10,6,11,5,12,4],[14,3,13,2,9,8,7,10,6,11,5,1,12,4],[14,3,13,2,9,8,7,10,6,11,1,5,12,4],[14,1,4,12,5,11,6,10,7,8,9,2,13,3],[14,3,13,2,9,8,7,10,6,11,5,12,1,4],[14,1,3,13,2,9,8,7,10,6,11,5,12,4],[14,3,1,13,2,9,8,7,10,6,11,5,12,4]],"frontier_blob":"414bbb0aa2d286c905540a91bd59386066ca405d"}]''' )

class CheckFailure(Exception):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise CheckFailure(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                      allow_nan=False).encode("ascii")


def down(q: Fraction) -> int:
    return (q.numerator * SCALE) // q.denominator


def up(q: Fraction) -> int:
    return -((-q.numerator * SCALE) // q.denominator)


@lru_cache(None)
def tau_enclosure() -> tuple[int, int]:
    """Machin identity and exact alternating rational partial sums."""
    def atan_bounds(d: int, terms: int) -> tuple[Fraction, Fraction]:
        x = Fraction(1, d)
        partial = sum(((-1 if k % 2 else 1) * x**(2*k+1) / (2*k+1)
                       for k in range(terms)), Fraction(0))
        tail = x**(2*terms+1) / (2*terms+1)
        return ((partial, partial+tail) if terms % 2 == 0
                else (partial-tail, partial))
    a, b = atan_bounds(5, 80), atan_bounds(239, 25)
    lower, upper = 32*a[0]-8*b[1], 32*a[1]-8*b[0]
    require(6 < lower < upper < 7, "2*pi interval domain")
    lo, hi = down(lower), up(upper)
    require(0 < hi-lo <= 2, "2*pi interval width")
    return lo, hi


def angle_enclosure(q: Fraction) -> tuple[int, int]:
    """2*asin(sqrt(q)): exact rational polynomial, then outward conversion.

    This implementation differs from the retained pilot's per-term fixed-point
    rounding. sqrt(q) is enclosed at 192 bits. The remaining power-series
    coefficients and partial sums are exact Fractions; only the final result
    is converted to the common 128-bit grid.
    """
    require(type(q) is Fraction and 0 < q < Fraction(9, 10), "Angle domain")
    root = math.isqrt((q.numerator * SQRT_SCALE**2) // q.denominator)
    xlo, xhi = Fraction(root, SQRT_SCALE), Fraction(root+1, SQRT_SCALE)
    require(xlo*xlo <= q <= xhi*xhi, "Integer square-root enclosure")
    term, partial = Fraction(1), Fraction(0)
    for k in range(2000):
        partial += term
        nxt = term * q * Fraction((2*k+1)**2, (2*k+2)*(2*k+3))
        tail = nxt / (1-q)
        if tail < SERIES_TARGET:
            lower, upper = 2*xlo*partial, 2*xhi*(partial+tail)
            lo, hi = down(lower), up(upper)
            require(0 < lo <= hi and hi-lo <= 2, "Angular enclosure width")
            return lo, hi
        term = nxt
    raise CheckFailure("Arcsin series exceeded iteration cap")


def angular_tables(n: int, radius: Fraction) -> tuple[list, list]:
    lo = [[0]*(n+1) for _ in range(n+1)]
    hi = [[0]*(n+1) for _ in range(n+1)]
    require(radius > 0, "Nonpositive central radius")
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            q = Fraction(a*b) / ((radius+a)*(radius+b))
            low, high = angle_enclosure(q)
            lo[a][b] = lo[b][a] = low
            hi[a][b] = hi[b][a] = high
    return lo, hi


def cyclic_sum(order: tuple[int, ...], weights: list) -> int:
    require(len(order) >= 3, "Cycle requires at least three radii")
    return sum(weights[order[i]][order[(i+1) % len(order)]]
               for i in range(len(order)))


def lower_witness(order: tuple[int, ...], weights: list, tau_hi: int):
    for which, removed in enumerate(((), (1,), (1, 2))):
        cycle = tuple(x for x in order if x not in removed)
        if len(cycle) >= 3:
            margin = cyclic_sum(cycle, weights) - tau_hi
            if margin > 0:
                return which, margin
    return None


def completion_table(values: tuple[int, ...], anchor: int, weights: list):
    """Bottom-up exact Held-Karp table H[mask][last-index].

    H[mask][j] is minimum path cost from values[j], visiting every vertex
    represented in mask once, then returning to anchor. j must be outside mask.
    Every recurrence uses a proper smaller mask; no floating-point arithmetic.
    """
    m = len(values)
    table = [[None]*m for _ in range(1 << m)]
    table[0] = [weights[v][anchor] for v in values]
    full = (1 << m)-1
    for mask in range(1, 1 << m):
        candidates = [k for k in range(m) if mask & (1 << k)]
        for j in range(m):
            if mask & (1 << j):
                continue
            table[mask][j] = min(weights[values[j]][values[k]]
                                 + table[mask ^ (1 << k)][k]
                                 for k in candidates)
    root = min(weights[anchor][values[k]] + table[full ^ (1 << k)][k]
               for k in range(m))
    # Explicit Bellman-equation validation over every used state.
    for mask in range(1 << m):
        for j in range(m):
            if mask & (1 << j):
                require(table[mask][j] is None, "Invalid DP state filled")
                continue
            require(type(table[mask][j]) is int, "Missing DP state")
            if mask:
                terms = [weights[values[j]][values[k]] + table[mask ^ (1 << k)][k]
                         for k in range(m) if mask & (1 << k)]
                require(table[mask][j] == min(terms), "Bellman equation failed")
            else:
                require(table[mask][j] == weights[values[j]][anchor], "DP terminal failed")
    return table, root


def fresh_lower_bound(n: int, weights: list, tau_hi: int) -> dict:
    """Complete coverage without any historical heaps or pruning comparisons."""
    expected = math.factorial(n-1)//2
    witness_counts = [0, 0, 0]
    minimum_leaf_margin = None
    witness_hash = hashlib.sha256()
    def reject_order(order):
        nonlocal minimum_leaf_margin
        witness = lower_witness(order, weights, tau_hi)
        if witness is None:
            raise CheckFailure("Lower bound inconclusive at order " + repr(order))
        which, margin = witness
        witness_counts[which] += 1
        minimum_leaf_margin = (margin if minimum_leaf_margin is None
                               else min(minimum_leaf_margin, margin))
        witness_hash.update(bytes(order) + bytes((which,)))

    if n <= 9:
        visited = 0
        for perm in itertools.permutations(range(1, n)):
            if perm[0] < perm[-1]:
                reject_order((n,)+perm)
                visited += 1
        require(visited == expected == sum(witness_counts), "Direct canonical count")
        return {"status": "PASS_COMPLETE_LOWER_BOUND", "method": "fresh_direct_canonical_enumeration",
                "canonical_orders_covered": expected, "explicit_full_orders_checked": visited,
                "witness_counts_full_remove1_remove12": witness_counts,
                "minimum_explicit_angular_margin_scaled": str(minimum_leaf_margin),
                "explicit_order_witness_sha256": witness_hash.hexdigest()}

    # Every full cycle yields a unique cycle on {2,...,n} after deleting 1,
    # up to rotation/reflection. Conversely insert 1 into each skeleton gap.
    anchor, values = n, tuple(range(2, n))
    m, full = len(values), (1 << len(values))-1
    table, root_bound = completion_table(values, anchor, weights)
    stats = {"nodes": 0, "pruned_subtrees": 0, "pruned_oriented_completions": 0,
             "canonical_skeletons_expanded": 0, "reversed_leaves_omitted": 0,
             "explicit_full_orders_checked": 0}
    minimum_prune_margin = None
    frontier_hash = hashlib.sha256()
    def walk(path: tuple[int, ...], mask: int, cost: int, last_index: int | None):
        nonlocal minimum_prune_margin
        stats["nodes"] += 1
        bound = root_bound if last_index is None else cost + table[mask][last_index]
        if bound > tau_hi:
            margin = bound-tau_hi
            stats["pruned_subtrees"] += 1
            stats["pruned_oriented_completions"] += math.factorial(bin(mask).count("1"))
            minimum_prune_margin = (margin if minimum_prune_margin is None
                                    else min(minimum_prune_margin, margin))
            frontier_hash.update(b"P"+bytes(path)+b":"+str(mask).encode()+b";")
            return
        if mask == 0:
            require(cost+weights[path[-1]][anchor] == bound, "Leaf completion mismatch")
            if path[1] > path[-1]:
                stats["reversed_leaves_omitted"] += 1
                return
            require(path[1] < path[-1], "Degenerate reflection")
            stats["canonical_skeletons_expanded"] += 1
            frontier_hash.update(b"E"+bytes(path)+b";")
            for position in range(1, len(path)+1):
                order = path[:position]+(1,)+path[position:]
                reject_order(order)
                stats["explicit_full_orders_checked"] += 1
            return
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            j = bit.bit_length()-1
            remaining -= bit
            v = values[j]
            walk(path+(v,), mask ^ bit, cost+weights[path[-1]][v], j)
    walk((anchor,), full, 0, None)
    k = stats["canonical_skeletons_expanded"]
    omitted = stats["pruned_oriented_completions"]
    require(stats["reversed_leaves_omitted"] == k, "Reflection coverage mismatch")
    require(omitted+2*k == math.factorial(n-2), "Skeleton factorial coverage mismatch")
    require(omitted % 2 == 0, "Asymmetric total omitted skeleton count")
    explicit = stats["explicit_full_orders_checked"]
    pruned_full = omitted*(n-1)//2
    require(explicit == k*(n-1) == sum(witness_counts), "Insertion coverage mismatch")
    require(pruned_full+explicit == expected, "Full canonical factorial coverage mismatch")
    dp_stream = [[mask, j, str(v)] for mask, row in enumerate(table)
                 for j, v in enumerate(row) if v is not None]
    return {"status": "PASS_COMPLETE_LOWER_BOUND", "method": "fresh_integer_completion_pruning_and_insertion",
            "canonical_orders_covered": expected, "skeleton_vertices": list(range(2, n+1)),
            "dp_states": len(dp_stream)+1, "dp_root_cost_minus_tau_hi_scaled": str(root_bound-tau_hi),
            "dp_table_sha256": digest(canonical_bytes(dp_stream)),
            **stats, "full_canonical_orders_covered_by_pruning": pruned_full,
            "minimum_prune_angular_margin_scaled": str(minimum_prune_margin) if minimum_prune_margin is not None else None,
            "witness_counts_full_remove1_remove12": witness_counts,
            "minimum_explicit_angular_margin_scaled": str(minimum_leaf_margin) if minimum_leaf_margin is not None else None,
            "explicit_order_witness_sha256": witness_hash.hexdigest(),
            "pruning_and_skeleton_stream_sha256": frontier_hash.hexdigest()}


def check_placement(order: tuple[int, ...], x: list[int], upper: list, tau_lo: int) -> int:
    """Independent of the constructing shortest-path algorithm: check all pairs."""
    n = len(order)
    require(len(x) == n and all(type(v) is int for v in x), "Position type/size")
    require(x[0] == 0 and all(x[i] < x[i+1] for i in range(n-1)) and x[-1] < tau_lo,
            "Positions are not strictly cyclically ordered")
    margins = []
    for i in range(n):
        for j in range(i+1, n):
            separation = upper[order[i]][order[j]]
            difference = x[j]-x[i]
            margins.extend((difference-separation, tau_lo-separation-difference))
    require(all(v >= PLACEMENT_PAD for v in margins), "All-pairs placement inequality failed")
    return min(margins)


def construct_placement(order: tuple[int, ...], upper: list, tau_lo: int) -> dict:
    n = len(order)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            separation = upper[order[i]][order[j]]+PLACEMENT_PAD
            edges.extend(((i, j, tau_lo-separation), (j, i, -separation)))
    distances = [0]*n
    converged = False
    for _ in range(n):
        changed = False
        for i, j, cost in edges:
            if distances[j] > distances[i]+cost:
                distances[j] = distances[i]+cost
                changed = True
        if not changed:
            converged = True
            break
    require(converged, "Upper witness construction inconclusive for " + repr(order))
    x = [v-distances[0] for v in distances]
    slack = check_placement(order, x, upper, tau_lo)
    return {"order": list(order), "positions_scaled_integers": [str(v) for v in x],
            "minimum_verified_all_pairs_slack_scaled": str(slack),
            "pair_constraints_checked": n*(n-1), "status": "PASS_ANGULAR_PLACEMENT"}


def stereographic_proposal(position: int) -> Fraction:
    """Propose rational t ~ tan(angle/2), without a libm dependency.

    The fixed-point Taylor approximation is a GENERATOR ONLY. No error bound
    for this approximation is assumed: check_cartesian_placement below proves
    the resulting exact rational geometry directly, or rejects the candidate.
    """
    H = 1 << 192
    z = position * H // (2*SCALE)
    z2 = z*z
    sine_term, cosine_term = z, H
    sine, cosine = z, H
    for k in range(1, 60):
        sine_term = sine_term*z2 // (H*H*(2*k)*(2*k+1))
        cosine_term = cosine_term*z2 // (H*H*(2*k-1)*(2*k))
        sign = -1 if k % 2 else 1
        sine += sign*sine_term
        cosine += sign*cosine_term
    require(cosine != 0, "Stereographic proposal at numerical pole")
    proposal = Fraction(sine, cosine)
    D = 10**40
    return Fraction((proposal.numerator*D)//proposal.denominator, D)


def check_cartesian_placement(order: tuple[int, ...], ts: list[Fraction], radius: Fraction) -> dict:
    """Exact rational independent geometry check; NO trigonometry or intervals.

    Center = (radius+r) * ((1-t^2)/(1+t^2), 2*t/(1+t^2)).
    Check central tangency and pairwise squared Euclidean distances exactly.
    """
    require(len(ts) == len(order) and all(type(t) is Fraction for t in ts), "Rational direction inputs")
    require(ts[0] == 0 and all(t != 0 for t in ts[1:]), "Direction origin or collision")
    keys = [(0 if t >= 0 else 1, t) for t in ts]
    require(all(keys[i] < keys[i+1] for i in range(len(keys)-1)), "Cartesian cyclic order")
    centers = []
    for r, t in zip(order, ts):
        den = 1+t*t
        x, y = (radius+r)*(1-t*t)/den, (radius+r)*2*t/den
        require(x*x+y*y == (radius+r)**2, "Exact central tangency failed")
        centers.append((x,y))
    minimum = None
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            x1,y1 = centers[i]
            x2,y2 = centers[j]
            gap = (x2-x1)**2+(y2-y1)**2-(order[i]+order[j])**2
            require(gap > 0, "Exact rational outer-circle non-overlap failed")
            minimum = gap if minimum is None else min(minimum,gap)
    require(minimum is not None, "No outer pair checked")
    return {"status": "PASS_EXACT_RATIONAL_CARTESIAN_PLACEMENT",
            "stereographic_parameters": [{"numerator":str(t.numerator),"denominator":str(t.denominator)} for t in ts],
            "central_tangencies_checked":len(order),
            "outer_pairs_checked":len(order)*(len(order)-1)//2,
            "minimum_squared_distance_gap": {"numerator":str(minimum.numerator),"denominator":str(minimum.denominator)}}


def regression_controls() -> dict:
    tl, th = tau_enclosure()
    al, ah = angle_enclosure(Fraction(1, 4))
    require(6*al <= th and 6*ah >= tl, "pi/3 identity")
    # Machin identity: tan(4 atan(1/5)-atan(1/239)) = 1 exactly.
    a = Fraction(1, 5)
    twice = 2*a/(1-a*a)
    four = 2*twice/(1-twice*twice)
    b = Fraction(1, 239)
    require((four-b)/(1+four*b) == 1, "Machin rational tangent identity")
    rng = random.Random(47913)
    dp_tests = 0
    for size in range(3, 9):
        for _ in range(3):
            weights = [[0]*size for _ in range(size)]
            for i in range(size):
                for j in range(i+1, size):
                    weights[i][j] = weights[j][i] = rng.randrange(1, 1000)
            values = tuple(range(1, size))
            table, cost = completion_table(values, 0, weights)
            brute = min(cyclic_sum((0,)+perm, weights)
                        for perm in itertools.permutations(values))
            require(cost == brute, "DP versus exhaustive test")
            dp_tests += 1
    # Malformed all-pairs witness must be rejected, not silently tolerated.
    _, upper = angular_tables(3, Fraction(CASES[0]["U"]))
    rejected = False
    try:
        check_placement((3, 1, 2), [0, 0, 0], upper, tl)
    except CheckFailure:
        rejected = True
    require(rejected, "Bad placement negative control")
    return {"status": "PASS", "DP_random_symmetric_exhaustive_comparisons": dp_tests,
            "bad_placement_rejected": rejected,
            "scope": "Regression controls, not an external/formal review"}


def run() -> dict:
    require([c["n"] for c in CASES] == list(range(3, 15)), "Case coverage")
    controls = regression_controls()
    tau_lo, tau_hi = tau_enclosure()
    rows, elapsed = [], []
    print("Riferimento degli input: " + REFERENCE_COMMIT, flush=True)
    print("NUOVO replay globale: nessun checkpoint, Top-K o lower bound float64.", flush=True)
    print(" n  ordini canonici coperti   ordini completi espliciti   testimoni U   stato", flush=True)
    for case in CASES:
        tick = time.perf_counter()
        n, L, U = case["n"], Fraction(case["L"]), Fraction(case["U"])
        require(0 < L < U and U-L == Fraction(1, 10**11), "Test bracket")
        orders = [tuple(o) for o in case["orders"]]
        require(len(set(orders)) == len(orders) and len(orders) > 0, "Duplicate/empty trial orders")
        for o in orders:
            require(len(o) == n and all(type(v) is int for v in o)
                    and set(o) == set(range(1, n+1)) and o[0] == n and o[1] < o[-1], "Trial order schema")
        low_L, high_L = angular_tables(n, L)
        low_U, high_U = angular_tables(n, U)
        lower = fresh_lower_bound(n, low_L, tau_hi)
        placements = [construct_placement(order, high_U, tau_lo) for order in orders]
        for order, placement in zip(orders, placements):
            ts = [stereographic_proposal(int(v)) for v in placement["positions_scaled_integers"]]
            placement["exact_cartesian_check"] = check_cartesian_placement(order, ts, U)
        # A sufficient infeasibility test must not reject the proven placements.
        require(all(lower_witness(o, low_U, tau_hi) is None for o in orders),
                "Lower-test contradiction at proven feasible U")
        intervals = []
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                intervals.append({"a": a, "b": b, "L_lower": str(low_L[a][b]),
                                  "L_upper": str(high_L[a][b]), "U_lower": str(low_U[a][b]),
                                  "U_upper": str(high_U[a][b])})
        row = {"n": n, "L": case["L"], "U": case["U"],
               "bracket_width": "1/100000000000", "lower_bound": lower,
               "upper_witnesses": placements, "angle_intervals_scaled": intervals,
               "candidate_claim": "L < global_infimum_radius <= U",
               "status": "PASS_GLOBAL_BRACKET_CANDIDATE"}
        rows.append(row)
        elapsed.append({"n": n, "seconds": time.perf_counter()-tick})
        print("%2d  %24d  %26d  %7d/%-4d  %s" %
              (n, lower["canonical_orders_covered"], lower["explicit_full_orders_checked"],
               len(placements), len(orders), row["status"]), flush=True)
    certificate = {"model": "outer circles of radii 1..n externally tangent to central circle, pairwise interior-disjoint",
                   "version": VERSION, "scale_denominator": str(SCALE),
                   "tau_lower_scaled": str(tau_lo), "tau_upper_scaled": str(tau_hi),
                   "placement_padding_scaled": str(PLACEMENT_PAD),
                   "input_cases_sha256": digest(canonical_bytes(CASES)), "cases": rows}
    return {"status": "PASS_GLOBAL_BRACKET_CANDIDATE", "certificate": certificate,
            "certificate_sha256": digest(canonical_bytes(certificate)),
            "regression_controls": controls, "timings": elapsed,
            "limitations": [
                "New proof computation; NOT a reconstruction or validation of every historical pruning.",
                "This program and mathematical derivation require external independent review before journal use.",
                "No claim of exact decimal equality, classification of all optima, floating-circle rigidity or uniqueness.",
                "No review baseline promotion, manuscript/solver edit or journal submission.",
                "No proof assistant verification of Python, integer arithmetic, OS or hardware."]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    output = args.output_dir.resolve(strict=True)
    require(output.is_dir(), "Output directory must already exist")
    for ancestor in (output, *output.parents):
        require(ancestor.name.casefold() != "checkpoints" and not (ancestor/".git").exists(),
                "Refusing output within checkpoints or a Git worktree")
    script = Path(__file__).resolve(strict=True)
    raw = script.read_bytes()
    started = time.perf_counter()
    result = run()
    now = datetime.now(timezone.utc)
    report = {"report_type": "fresh_global_interval_certificate_candidate", "created_utc": now.isoformat(),
              "reference_commit_for_input_provenance_only": REFERENCE_COMMIT,
              "source_evidence_zip_sha256": SOURCE_EVIDENCE_ZIP_SHA256,
              "script_sha256": digest(raw), "python": sys.version, "platform": platform.platform(),
              **result, "total_seconds": time.perf_counter()-started}
    require(script.read_bytes() == raw, "Script changed during execution")
    name = "global_interval_replay_%s_%s.json" % (now.strftime("%Y%m%dT%H%M%SZ"), uuid.uuid4().hex[:8])
    path = output/name
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, ensure_ascii=True, allow_nan=False)
        stream.write("\n")
    readback = json.loads(path.read_text(encoding="utf-8"))
    require(digest(canonical_bytes(readback["certificate"])) == result["certificate_sha256"], "Report readback")
    print("\nESITO: " + result["status"], flush=True)
    print("Intervalli globali candidati: 12/12 | testimoni geometrici: 47/47", flush=True)
    print("SHA256 certificato deterministico: " + result["certificate_sha256"], flush=True)
    print("Tempo osservato: %.2f secondi" % report["total_seconds"], flush=True)
    print("Report JSON: " + str(path), flush=True)
    print("Richiede revisione indipendente; nessuna promozione Registry o journal-readiness.", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("INTERROTTO: nessun checkpoint/repository modificato.", file=sys.stderr)
        raise SystemExit(130)
    except Exception as exc:
        print("FAIL/INCONCLUSIVE: %s: %s" % (type(exc).__name__, exc), file=sys.stderr)
        raise SystemExit(2)
