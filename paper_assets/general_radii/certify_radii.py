#!/usr/bin/env python3
"""Propose exact global radius brackets for distinct positive integer radii."""
import argparse
import json
import math
import re
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCHEMA = "ringmin.distinct-integer-radii.v1"


def check_domain(radii, deleted):
    if (len(radii) < 3 or tuple(sorted(set(radii))) != tuple(radii)
            or any(type(r) is not int or r <= 0 for r in radii)):
        raise ValueError("the sorted radii must be at least three distinct positive integers")
    if not 0 <= deleted <= len(radii) - 3:
        raise ValueError("deletion depth must leave at least three core radii")


def angle_proposals(radii, radius, bits, upper=False):
    """Generate one-sided integer proposals; the standalone verifier proves every lower entry."""
    scale = 1 << bits
    with mp.workprec(bits + 100):
        R = mp.mpf(radius.numerator) / radius.denominator
        round_edge = mp.ceil if upper else mp.floor
        adjust = 1 if upper else -1
        T = int((mp.floor if upper else mp.ceil)(2 * mp.pi * scale)) - adjust
        W = [[0] * len(radii) for _ in radii]
        for i, a in enumerate(radii):
            for j in range(i):
                b = radii[j]
                # atan2 avoids loss of relative accuracy at either end of (0, pi).
                ang = 2 * mp.atan2(mp.sqrt(a * b), mp.sqrt(R * (R + a + b)))
                W[i][j] = W[j][i] = max(0, int(round_edge(ang * scale)) + adjust)
    return W, T


def completion_dp(core, W):
    """Suffix cost from last, through mask (low bit = first nonanchor), back to anchor."""
    vertices, anchor = core[:-1], core[-1]

    @lru_cache(None)
    def finish(last, mask):
        if not mask:
            return W[last][anchor]
        best = None
        choices = mask
        while choices:
            bit = choices & -choices
            choices -= bit
            v = vertices[bit.bit_length() - 1]
            value = W[last][v] + finish(v, mask ^ bit)
            if best is None or value < best:
                best = value
        return best

    return finish


def skeletons(core, W, T, counts):
    vertices, anchor = core[:-1], core[-1]
    finish = completion_dp(core, W)

    def traverse(order, mask, cost):
        if cost + finish(order[-1], mask) > T:
            counts["pruned_oriented"] += math.factorial(mask.bit_count())
        elif not mask:
            if order[1] < order[-1]:
                counts["retained_cores"] += 1
                yield order
            else:
                counts["reverse_leaves"] += 1
        else:
            choices = mask
            while choices:
                bit = choices & -choices
                choices -= bit
                v = vertices[bit.bit_length() - 1]
                yield from traverse(order + (v,), mask ^ bit, cost + W[order[-1]][v])

    yield from traverse((anchor,), (1 << len(vertices)) - 1, 0)


def insertions(core, deleted):
    """Insert labels in increasing rank, including the gap ending at the anchor."""
    def extend(order, rank):
        if rank == deleted:
            yield order
            return
        for gap in range(1, len(order) + 1):
            yield from extend(order[:gap] + (rank,) + order[gap:], rank + 1)

    yield from extend(core, 0)


def positive_prefix_cycle(order, W, T):
    for first_rank in range(len(order) - 2):
        cycle = [i for i in order if i >= first_rank]
        if sum(W[cycle[j - 1]][v] for j, v in enumerate(cycle)) > T:
            return True
    return False


def potentials(order, W, T, pad=0):
    """Longest paths in the two-directed-arc difference system, or None for a positive cycle."""
    n = len(order)
    arcs = []
    for j, b in enumerate(order):
        for i in range(j):
            edge = W[order[i]][b] + pad
            arcs.extend(((i, j, edge), (j, i, edge - T)))
    x = [0] * n
    for _ in range(n):
        moved = False
        for i, j, cost in arcs:
            new = x[i] + cost
            if new > x[j]:
                x[j] = new
                moved = True
        if not moved:
            return [v - x[0] for v in x]
    return None


def scan(W, T, deleted):
    """A surviving word or a complete lower-endpoint coverage record."""
    n = len(W)
    counts = dict(pruned_oriented=0, retained_cores=0, reverse_leaves=0,
                  explicit=0, prefix_exclusions=0, graph_exclusions=0)
    core = tuple(range(deleted, n))
    for skeleton in skeletons(core, W, T, counts):
        for order in insertions(skeleton, deleted):
            counts["explicit"] += 1
            if positive_prefix_cycle(order, W, T):
                counts["prefix_exclusions"] += 1
            elif potentials(order, W, T) is None:
                counts["graph_exclusions"] += 1
            else:
                return order, None
    multiplier = math.factorial(n - 1) // math.factorial(len(core) - 1)
    p, k = counts["pruned_oriented"], counts["retained_cores"]
    if (p + 2*k != math.factorial(len(core) - 1) or k != counts["reverse_leaves"]
            or p % 2 or counts["explicit"] != k * multiplier):
        raise ArithmeticError("skeleton/insertion partition failed")
    counts["full_classes"] = p // 2 * multiplier + counts["explicit"]
    return None, counts



def seek_order(W, T, deleted, warm):
    """Find one feasible relaxed word, stopping on incompatible partial insertions."""
    if potentials(warm, W, T) is not None:
        return warm
    counters = dict(pruned_oriented=0, retained_cores=0, reverse_leaves=0)
    ranks = (tuple(reversed(range(deleted))) if len(W) >= 12 else tuple(range(deleted)))

    def insert_feasible(order, step):
        if potentials(order, W, T) is None:
            return None
        if step == deleted:
            return order
        label = ranks[step]
        for gap in range(1, len(order) + 1):
            child = insert_feasible(order[:gap] + (label,) + order[gap:], step + 1)
            if child is not None:
                return child
        return None

    for core in skeletons(tuple(range(deleted, len(W))), W, T, counters):
        order = insert_feasible(core, 0)
        if order is not None:
            return order
    return None


def auto_bracket(radii, deleted, bits, digits):
    """Discrete bisection over grid radii. Relaxed integer feasibility guides proposals."""
    grid = 10**digits
    left, right = 0, len(radii) * max(radii) * grid
    warm = tuple(range(len(radii)))
    while right - left > 1:
        mid = (right + left) // 2
        W, T = angle_proposals(radii, Fraction(mid, grid), bits)
        order = seek_order(W, T, deleted, warm)
        if order is None:
            left = mid
        else:
            warm, right = order, mid
    if left == 0:
        raise ValueError("grid too coarse for a positive lower endpoint; increase --digits")
    return Fraction(left, grid), Fraction(right, grid), warm


def stereographic(order, radii, radius, bits):
    W, T = angle_proposals(radii, radius, bits, upper=True)
    x = potentials(order, W, T, pad=4)
    if x is None:
        raise ArithmeticError("upper witness infeasible at working precision; widen U or increase --bits")
    # The isolated verifier checks each resulting rational direction directly.
    with mp.workprec(bits + 100):
        denominator = 1 << (bits + 40)
        directions = []
        for angle in x:
            t = mp.tan(mp.mpf(angle) / (2 << bits))
            directions.append(Fraction(int(mp.nint(t * denominator)), denominator))
    centers = []
    for v, t in zip(order, directions):
        a = radii[v]
        centers.append(((radius + a) * (1-t*t) / (1+t*t),
                        (radius + a) * 2*t / (1+t*t)))
    for j, (xj, yj) in enumerate(centers):
        if xj*xj + yj*yj != (radius+radii[order[j]])**2:
            raise ArithmeticError("central tangency failed")
        for i in range(j):
            xi, yi = centers[i]
            if (xi-xj)**2 + (yi-yj)**2 <= (radii[order[i]]+radii[order[j]])**2:
                raise ArithmeticError("upper proposal lacks strict Cartesian separation")
    return [str(t) for t in directions]


def make_certificate(radii, deleted, bits=128, digits=11, endpoints=None, proposal=None):
    check_domain(radii, deleted)
    if bits < 32 or digits < 0:
        raise ValueError("use at least 32 angle bits and a nonnegative number of decimal places")
    if endpoints is None:
        L, U, order = auto_bracket(radii, deleted, bits, digits)
    else:
        L, U = endpoints
        if not 0 < L < U:
            raise ValueError("endpoints must satisfy 0 < lower < upper")
        order = proposal
    W, T = angle_proposals(radii, L, bits)
    survivor, coverage = scan(W, T, deleted)
    if survivor is not None:
        raise ValueError("lower endpoint unresolved for order " + repr([radii[i] for i in survivor]))
    if order is None:
        upper, period = angle_proposals(radii, U, bits, upper=True)
        order, _ = scan(upper, period, deleted)
    if order is None or tuple(sorted(order)) != tuple(range(len(radii))):
        raise ValueError("no admissible upper order at supplied endpoint")
    try:
        directions = stereographic(order, radii, U, bits)
    except ArithmeticError:
        if endpoints is not None:
            raise
        # An exact grid optimum can permit tangencies but no strict witness at U.
        U += Fraction(1, 10**digits)
        directions = stereographic(order, radii, U, bits)
    # Every rigorous integer violation is at least one unit of the angular grid.
    epsilon = min((U-L)/2, L**2 / (4 * len(radii) * max(radii) * (1 << bits)))
    return dict(schema=SCHEMA, radii=list(radii), deleted=deleted, bits=bits,
                lower=str(L), upper=str(U), strict_buffer=str(epsilon), tau_upper=T,
                angle_lower=[W[i][j] for i in range(len(W)) for j in range(i)],
                coverage=coverage, order=[radii[i] for i in order],
                stereographic=directions)


def linear_reference(n):
    path = ROOT / ".codex_inputs/arxiv/p1_v4/bracket_rows.tex"
    text = path.read_text(encoding="utf-8")
    row = re.search(rf"^{n}\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)", text, re.M)
    if not row:
        raise ValueError("no published bracket for that n")
    data = ROOT / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
    cases = json.loads(data.read_text(encoding="utf-8"))["certificate"]["cases"]
    case = next(case for case in cases if case["n"] == n)
    order = tuple(i - 1 for i in case["upper_witnesses"][0]["order"])
    return tuple(map(Fraction, row.groups())), order


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    family = parser.add_mutually_exclusive_group(required=True)
    family.add_argument("--linear", type=int, metavar="N", help="reproduce Paper I v4 endpoints")
    family.add_argument("--quadratic", type=int, metavar="N")
    family.add_argument("--radii", type=int, nargs="+", metavar="R")
    parser.add_argument("--delete", type=int, help="number of smallest radii deleted to form the core")
    parser.add_argument("--bits", type=int, help="angle-grid precision (default at least 128 bits)")
    parser.add_argument("--digits", type=int, default=11, help="decimal places in automatic bracket")
    parser.add_argument("--lower", type=Fraction)
    parser.add_argument("--upper", type=Fraction)
    parser.add_argument("--order", type=int, nargs="+", help="optional actual radii in circular order")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        endpoints = order = None
        if args.linear is not None:
            radii = tuple(range(1, args.linear + 1))
            endpoints, order = linear_reference(args.linear)
        elif args.quadratic is not None:
            radii = tuple(i*i for i in range(1, args.quadratic + 1))
        else:
            radii = tuple(sorted(args.radii))
        default_depth = (0 if len(radii) <= 4 else
                         (min((len(radii)-1)//3, 4) if args.quadratic and len(radii) >= 7 else 1))
        deleted = default_depth if args.delete is None else args.delete
        if (args.lower is None) != (args.upper is None):
            raise ValueError("supply both rational endpoints")
        if args.lower is not None:
            endpoints = (args.lower, args.upper)
        if args.order:
            if endpoints is None:
                raise ValueError("--order needs supplied or published endpoints")
            order = tuple(radii.index(r) for r in args.order)
        check_domain(radii, deleted)
        bits = args.bits
        if bits is None:
            bits = max(128, max(radii).bit_length() + 4*max(args.digits, 0) + 32)
        cert = make_certificate(radii, deleted, bits, args.digits, endpoints, order)
        args.output.write_bytes((json.dumps(cert, indent=2) + "\n").encode("utf-8"))
        print(f"CANDIDATE n={len(radii)} ({cert['lower']}, {cert['upper']}] {args.output.name}")
    except (OSError, ValueError, ArithmeticError) as exc:
        print("FAIL", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
