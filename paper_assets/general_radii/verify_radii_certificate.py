#!/usr/bin/env python3
"""Verify a distinct-positive-integer-radii certificate using the standard library alone."""
import argparse
import itertools
import json
import math
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


SCHEMA = "ringmin.distinct-integer-radii.v1"
FIELDS = {"schema", "radii", "deleted", "bits", "lower", "upper", "strict_buffer",
          "tau_upper", "angle_lower", "coverage", "order", "stereographic"}


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def unique_keys(pairs):
    result = dict(pairs)
    require(len(result) == len(pairs), "duplicate JSON field")
    return result


def ratio(text):
    require(type(text) is str, "expected an exact rational string")
    value = Fraction(text)
    require(str(value) == text, "noncanonical rational")
    return value


@lru_cache(None)
def tau_bounds(bits):
    """Machin 2*pi = 32 atan(1/5) - 8 atan(1/239), exact alternating rationals."""
    def atan(d):
        s = Fraction()
        k = 0
        power = d
        while True:
            term = Fraction(1, (2*k+1)*power)
            other = s + (-term if k % 2 else term)
            if term < Fraction(1, 1 << (bits + 12)):
                return min(s, other), max(s, other)
            s, power, k = other, power*d*d, k+1
    a, b = atan(5), atan(239)
    return 32*a[0] - 8*b[1], 32*a[1] - 8*b[0]


def cos_lower(angle, scale, grid):
    """A lower bound on grid*cos(angle/scale), with an alternating-series remainder."""
    aa, ss = angle**2, scale**2
    term_lo = term_hi = grid
    total = grid
    k = 1
    while True:
        denom = ss*(2*k-1)*(2*k)
        term_lo = term_lo*aa // denom
        term_hi = -((-term_hi*aa) // denom)
        # At x <= 4 and k >= 2 the following terms decrease in absolute value.
        if k >= 2 and term_hi <= 2:
            return total - term_hi
        total += -term_hi if k % 2 else term_lo
        k += 1


def weights(radii, L, bits, lower, T):
    S = 1 << bits
    circumference_lo, circumference_hi = tau_bounds(bits)
    require(type(T) is int and 6*S < T < 7*S and T > S*circumference_hi,
            "unproved circumference upper endpoint")
    n = len(radii)
    require(type(lower) is list and len(lower) == n*(n-1)//2, "angular table length")
    W = [[0]*n for _ in radii]
    grid = 1 << (2*bits + 80)
    for (i, j), a in zip(((i, j) for i in range(n) for j in range(i)), lower):
        require(type(a) is int and 0 <= a < S*circumference_lo/2, "angle outside [0,pi)")
        ra, rb = radii[i], radii[j]
        q = Fraction(ra*rb) / ((L+ra)*(L+rb))
        if a:
            target = 1 - 2*q
            require(cos_lower(a, S, grid)*target.denominator > grid*target.numerator,
                    f"false angle lower bound for radii {ra}, {rb}")
        W[i][j] = W[j][i] = a
    return W


def forward_table(vertices, anchor, W):
    """Minimum cost from anchor through mask, ending at j (a local bit index)."""
    D = {}
    for mask in range(1, 1 << len(vertices)):
        members = [j for j in range(len(vertices)) if mask >> j & 1]
        for j in members:
            prev = mask ^ (1 << j)
            D[mask, j] = (min(D[prev, k]+W[vertices[k]][vertices[j]]
                              for k in members if k != j)
                          if prev else W[anchor][vertices[j]])
    return D


def full_orders(skeleton, d):
    """Choose weakly increasing gap slots then assign a permutation of the d labels."""
    for slots in itertools.combinations_with_replacement(range(len(skeleton)), d):
        for labels in itertools.permutations(range(d)):
            buckets = [[v] for v in skeleton]
            for slot, label in zip(slots, labels):
                buckets[slot].append(label)
            yield tuple(itertools.chain.from_iterable(buckets))


def classify_order(order, W, T):
    n = len(order)
    for threshold in range(n-2):
        walk = tuple(v for v in order if v >= threshold)
        cost = sum(W[a][b] for a, b in zip(walk, walk[1:] + walk[:1]))
        if cost > T:
            return "prefix_exclusions"
    # Max-plus Floyd-Warshall. A positive diagonal implies a positive simple cycle.
    C = [[0]*n for _ in order]
    for i, a in enumerate(order):
        for j, b in enumerate(order):
            if i != j:
                C[i][j] = W[a][b] - (T if j < i else 0)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                C[i][j] = max(C[i][j], C[i][k] + C[k][j])
        if any(C[i][i] > 0 for i in range(n)):
            return "graph_exclusions"
    raise ValueError(f"lower endpoint has an unresolved order {order}")


def lower_audit(W, T, d):
    n = len(W)
    anchor = n-1
    vertices = tuple(range(d, anchor))
    D = forward_table(vertices, anchor, W)
    all_bits = (1 << len(vertices)) - 1
    root = min(D[all_bits, j]+W[vertices[j]][anchor] for j in range(len(vertices)))
    counts = dict(pruned_oriented=0, retained_cores=0, reverse_leaves=0,
                  explicit=0, prefix_exclusions=0, graph_exclusions=0)
    pending = [((anchor,), all_bits, 0, None)]
    while pending:
        prefix, left, cost, j = pending.pop()
        minimum = root if j is None else cost + D[left | (1 << j), j]
        if minimum > T:
            counts["pruned_oriented"] += math.factorial(left.bit_count())
        elif left:
            for k, v in enumerate(vertices):
                if left & (1 << k):
                    pending.append((prefix + (v,), left ^ (1 << k),
                                    cost + W[prefix[-1]][v], k))
        elif prefix[1:] > prefix[:0:-1]:
            counts["reverse_leaves"] += 1
        else:
            counts["retained_cores"] += 1
            for order in full_orders(prefix, d):
                counts["explicit"] += 1
                counts[classify_order(order, W, T)] += 1
    k = len(vertices) + 1
    multiplier = math.prod(range(k, n))
    p, kept = counts["pruned_oriented"], counts["retained_cores"]
    require(p % 2 == 0 and counts["reverse_leaves"] == kept
            and p + 2*kept == math.factorial(k-1), "oriented core partition")
    require(counts["explicit"] == kept*multiplier
            and counts["explicit"] == counts["prefix_exclusions"] + counts["graph_exclusions"],
            "insertion and leaf partition")
    counts["full_classes"] = p//2*multiplier + counts["explicit"]
    require(counts["full_classes"] == math.factorial(n-1)//2, "full factorial partition")
    return counts


def geometry(radii, U, order, parameters):
    require(type(order) is list and all(type(r) is int for r in order)
            and sorted(order) == radii, "witness radii must be a permutation")
    require(type(parameters) is list and len(parameters) == len(radii), "witness length")
    ts = list(map(ratio, parameters))
    keys = [(t < 0, t) for t in ts]
    require(ts[0] == 0 and all(a < b for a, b in zip(keys, keys[1:])),
            "witness polar order")
    centers = []
    for r, t in zip(order, ts):
        unit_x = (1-t*t)/(1+t*t)
        unit_y = 2*t/(1+t*t)
        x, y = (U+r)*unit_x, (U+r)*unit_y
        require(x*x+y*y == (U+r)**2, "central tangency")
        centers.append((x, y))
    for i, j in itertools.combinations(range(len(radii)), 2):
        x, y = centers[i]
        xx, yy = centers[j]
        require((x-xx)**2+(y-yy)**2 > (order[i]+order[j])**2,
                f"strict Cartesian gap failed for {order[i]}, {order[j]}")


def verify(data):
    require(type(data) is dict and set(data) == FIELDS and data["schema"] == SCHEMA,
            "unknown certificate schema/fields")
    radii = data["radii"]
    require(type(radii) is list and len(radii) >= 3 and all(type(r) is int and r > 0 for r in radii)
            and radii == sorted(set(radii)), "radii must be sorted, distinct positive integers")
    d, bits = data["deleted"], data["bits"]
    require(type(d) is int and 0 <= d <= len(radii)-3, "invalid deletion depth")
    require(type(bits) is int and bits >= 32, "invalid angular precision")
    L, U, epsilon = (ratio(data[k]) for k in ("lower", "upper", "strict_buffer"))
    require(0 < L < U, "invalid radius endpoints")
    # n*(2*max(r)/L**2) bounds the absolute derivative of each simple cycle's sum.
    D = 2*len(radii)*max(radii) / L**2
    require(0 < epsilon < U-L and epsilon == min((U-L)/2, Fraction(1, 2*(1 << bits)*D)),
            "invalid strictness buffer")
    geometry(radii, U, data["order"], data["stereographic"])
    W = weights(radii, L, bits, data["angle_lower"], data["tau_upper"])
    audited = lower_audit(W, data["tau_upper"], d)
    recorded = data["coverage"]
    require(type(recorded) is dict and all(type(v) is int for v in recorded.values())
            and audited == recorded, "recomputed coverage differs")
    return audited


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, nargs="*")
    parser.add_argument("--all", action="store_true", help="verify all sibling certificates")
    args = parser.parse_args()
    paths = sorted((Path(__file__).parent / "certificates").glob("*.json")) if args.all else args.files
    if not paths or (args.all and args.files):
        parser.error("choose certificate files or --all")
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)
            stats = verify(data)
            print(f"PASS {path.name} n={len(data['radii'])} classes={stats['full_classes']}")
        except (OSError, ValueError, ArithmeticError, TypeError) as exc:
            print(f"FAIL {path.name}: {exc}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
