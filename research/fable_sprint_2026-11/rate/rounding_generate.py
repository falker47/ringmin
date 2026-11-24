#!/usr/bin/env python3
"""Generator for the dyadic rounding construction of NOTE_QUANTILE_RATE.md.

For a power profile Q(t) = t**p, types v_j = Q(j/k) with k = 2**kappa, and
blocks of r = 2**rho points, this script

1. builds a feasible rational line placement P of the type list U_q
   (q copies of every type), in a pseudo-random left-to-right order;
2. cuts P into windows of r consecutive points and runs the dyadic rounding
   of Lemma 3 (support reduction to linearly independent count vectors,
   integer parts, halving of the fractional remainder);
3. writes the placement and the selected integer pieces as a JSON certificate.

Everything is exact rational arithmetic (fractions.Fraction).  The script is
an untrusted generator: rounding_verify.py re-derives every claim from the
certificate alone and shares no code with this file.

Usage:
    python -I rounding_generate.py --out rounding_certificates.json
"""
from __future__ import annotations

import argparse
import json
import math
import random
import time
from fractions import Fraction as F

SQRT_DIGITS = 12  # outward rounding grid for irrational gaps (odd p only)

# (p, kappa, rho, q, T, seed, order)
INSTANCES = [
    (1, 1, 1, 8, 5, 11, "shuffle"),
    (1, 2, 2, 8, 3, 12, "shuffle"),
    (1, 2, 3, 64, 7, 13, "shuffle"),
    (1, 2, 4, 32, 5, 14, "sorted"),
    (1, 3, 3, 24, 7, 15, "shuffle"),
    (1, 3, 5, 48, 5, 16, "shuffle"),
    (1, 4, 4, 48, 9, 17, "shuffle"),
    (1, 4, 6, 64, 3, 18, "zigzag"),
    (2, 1, 2, 16, 3, 21, "shuffle"),
    (2, 2, 2, 16, 5, 22, "shuffle"),
    (2, 2, 3, 64, 7, 23, "zigzag"),
    (2, 3, 3, 40, 9, 24, "shuffle"),
    (2, 3, 4, 64, 11, 25, "shuffle"),
    (2, 4, 4, 64, 13, 26, "shuffle"),
    (2, 4, 5, 64, 7, 27, "sorted"),
    (2, 5, 5, 32, 9, 28, "shuffle"),
    (3, 3, 4, 32, 5, 31, "shuffle"),
    (1, 5, 5, 32, 17, 32, "shuffle"),
]


def gap_upper(p: int, k: int, i: int, j: int) -> F:
    """Rational upper bound for sqrt(v_i v_j), v_j = (j/k)**p; exact if p is even."""
    if p % 2 == 0:
        return F((i * j) ** (p // 2), k**p)
    scale = 10**SQRT_DIGITS
    target = (i * j) ** p * scale * scale
    s = math.isqrt(target)
    if s * s < target:
        s += 1
    return F(s, scale * k**p)


def make_order(k: int, q: int, seed: int, order: str) -> list[int]:
    seq = [j for j in range(1, k + 1) for _ in range(q)]
    if order == "sorted":
        return seq
    if order == "zigzag":
        # alternate large and small types
        lo, hi, out = 0, len(seq) - 1, []
        while lo <= hi:
            out.append(seq[hi])
            hi -= 1
            if lo <= hi:
                out.append(seq[lo])
                lo += 1
        return out
    random.Random(seed).shuffle(seq)
    return seq


def place(p: int, k: int, seq: list[int]) -> list[F]:
    """Leftmost placement in the given order, using the outward-rounded gaps."""
    cache: dict[tuple[int, int], F] = {}
    xs: list[F] = []
    for i, a in enumerate(seq):
        best = F(0)
        for j in range(i):
            b = seq[j]
            key = (a, b) if a <= b else (b, a)
            g = cache.get(key)
            if g is None:
                g = cache[key] = gap_upper(p, k, key[0], key[1])
            cand = xs[j] + g
            if cand > best:
                best = cand
        xs.append(best)
    return xs


def null_vector(cols: list[tuple[int, ...]]):
    """Nontrivial rational z with sum z_i cols[i] = 0, or None if independent."""
    m = len(cols)
    if m == 0:
        return None
    k = len(cols[0])
    rows = [[F(cols[c][r]) for c in range(m)] for r in range(k)]
    pivots: list[int] = []
    row = 0
    for c in range(m):
        piv = next((r for r in range(row, k) if rows[r][c] != 0), None)
        if piv is None:
            # column c is free: express it through the pivot columns
            z = [F(0)] * m
            z[c] = F(1)
            for r, pc in enumerate(pivots):
                z[pc] = -rows[r][c]
            return z
        rows[row], rows[piv] = rows[piv], rows[row]
        inv = 1 / rows[row][c]
        rows[row] = [v * inv for v in rows[row]]
        for r in range(k):
            if r != row and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[row])]
        pivots.append(c)
        row += 1
    return None


def basic_solution(items, count, cost):
    """Reduce a nonnegative combination to linearly independent support.

    The combination sum_B w_B count(B) is preserved and sum_B w_B cost(B)
    does not increase.
    """
    supp: dict[tuple[int, int], F] = {}
    for key, w in items:
        if w == 0:
            continue
        supp[key] = supp.get(key, F(0)) + w
        keys = list(supp)
        z = null_vector([count(b) for b in keys])
        if z is None:
            continue
        dz = sum(zi * cost(b) for zi, b in zip(z, keys))
        if dz > 0:
            z = [-zi for zi in z]
        step = min(supp[b] / -zi for zi, b in zip(z, keys) if zi < 0)
        for zi, b in zip(z, keys):
            supp[b] += step * zi
        supp = {b: w for b, w in supp.items() if w != 0}
        assert all(w > 0 for w in supp.values())
        assert null_vector([count(b) for b in supp]) is None
    return supp


def run_instance(p, kappa, rho, q, T, seed, order):
    k, r = 2**kappa, 2**rho
    assert kappa <= rho and q % (r // k) == 0
    n_pts = k * q
    seq = make_order(k, q, seed, order)
    xs = place(p, k, seq)

    def count(block):
        start, length = block
        vec = [0] * k
        for t in seq[start : start + length]:
            vec[t - 1] += 1
        return tuple(vec)

    def cost(block):
        start, length = block
        return xs[start + length - 1] - xs[start]

    weight = F(T * r, k * q)
    current = [((start, r), weight) for start in range(0, n_pts, r)]
    pieces = []
    for level in range(rho + 1):
        supp = basic_solution(current, count, cost)
        current = []
        for (start, length), h in sorted(supp.items()):
            mult = h.numerator // h.denominator
            if mult:
                pieces.append([start, length, mult])
            frac = h - mult
            if frac:
                assert length > 1, "fractional weight on a single point"
                half = length // 2
                current.append(((start, half), frac))
                current.append(((start + half, half), frac))
    assert not current
    return {
        "p": p,
        "kappa": kappa,
        "rho": rho,
        "q": q,
        "T": T,
        "seed": seed,
        "order": order,
        "sequence": seq,
        "coordinates": [[x.numerator, x.denominator] for x in xs],
        "pieces": pieces,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="rounding_certificates.json")
    args = ap.parse_args()
    t0 = time.perf_counter()
    out = []
    for inst in INSTANCES:
        t1 = time.perf_counter()
        cert = run_instance(*inst)
        out.append(cert)
        print(
            f"p={inst[0]} k={2**inst[1]} r={2**inst[2]} q={inst[3]} T={inst[4]} "
            f"order={inst[6]}: {len(cert['pieces'])} piece kinds, "
            f"{time.perf_counter() - t1:.1f}s"
        )
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(
            {"schema": "ringmin-rounding-certificates/1", "sqrt_digits": SQRT_DIGITS, "instances": out},
            fh,
            separators=(",", ":"),
        )
        fh.write("\n")
    print(f"wrote {args.out} ({len(out)} instances) in {time.perf_counter() - t0:.1f}s")


if __name__ == "__main__":
    main()
