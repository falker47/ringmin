#!/usr/bin/env python3
"""Independent exact verifier for rounding_certificates.json.

Shares no code with rounding_generate.py and uses only the Python standard
library.  For every instance it checks, in exact rational arithmetic, the
finite inequality (3.4) of NOTE_QUANTILE_RATE.md:

    V1  the recorded points are a feasible line placement P of the type list
        U_q (q copies of each type v_j = (j/k)**p): every pair satisfies
        (x_a - x_b)**2 >= v_a v_b;
    V2  every selected piece is a dyadic sub-block of a window of r
        consecutive points of P, with a positive integer multiplicity;
    V3  the selected pieces contain exactly T r / k points of every type;
    V4  at most T pieces have size r, at most 2(k-1) have each smaller
        dyadic size, and there are at most T + (k-1) rho pieces in all;
    V5  the total extent of the pieces is at most (T r / (k q)) span(P);
    V6  the pieces, laid out left to right with gaps M = 1, form a feasible
        placement (all pairs re-checked from scratch) whose span is at most
            (T r / (k q)) span(P) + T + (k - 1) rho - 1.

It also checks the counting step (3.6) for a range of n:

    V7  with T = ceil(ceil(n/k) / (r/k)): T r <= n + r - 1, every type is
        needed at most T r / k times, and i/n <= ceil(i k / n)/k.

Exit status 0 means every check passed.

Usage:
    python -I -S rounding_verify.py rounding_certificates.json
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction


def fail(msg: str) -> None:
    print("FAIL:", msg)
    sys.exit(1)


def all_pairs_ok(xs, marks) -> bool:
    """Exact check of (x_a - x_b)^2 >= mark_a * mark_b for all pairs."""
    n = len(xs)
    for a in range(n):
        xa, ma = xs[a], marks[a]
        for b in range(a + 1, n):
            d = xs[b] - xa
            if d * d < ma * marks[b]:
                return False
    return True


def verify_instance(idx: int, inst: dict) -> dict:
    p, kappa, rho, q, T = (inst[key] for key in ("p", "kappa", "rho", "q", "T"))
    for name, val in (("p", p), ("kappa", kappa), ("rho", rho), ("q", q), ("T", T)):
        if not isinstance(val, int) or isinstance(val, bool):
            fail(f"instance {idx}: {name} is not an integer")
    if not (p >= 1 and 0 <= kappa <= rho and q >= 1 and T >= 1):
        fail(f"instance {idx}: parameters out of range")
    k, r = 1 << kappa, 1 << rho
    if (k * q) % r:
        fail(f"instance {idx}: r does not divide k q")
    seq = inst["sequence"]
    xs = [Fraction(num, den) for num, den in inst["coordinates"]]
    n_pts = k * q
    if len(seq) != n_pts or len(xs) != n_pts:
        fail(f"instance {idx}: wrong number of points")
    if any((not isinstance(t, int)) or t < 1 or t > k for t in seq):
        fail(f"instance {idx}: bad type index")
    for j in range(1, k + 1):
        if seq.count(j) != q:
            fail(f"instance {idx}: type {j} does not occur q times")
    if any(xs[i] > xs[i + 1] for i in range(n_pts - 1)):
        fail(f"instance {idx}: coordinates are not nondecreasing")
    mark = [None] + [Fraction(j, k) ** p for j in range(1, k + 1)]
    if any(m > 1 for m in mark[1:]):
        fail(f"instance {idx}: a mark exceeds M = 1")

    # V1
    if not all_pairs_ok(xs, [mark[t] for t in seq]):
        fail(f"instance {idx}: V1 placement P is infeasible")
    span_p = xs[-1] - xs[0]

    # V2-V5
    totals = [0] * (k + 1)
    per_level = [0] * (rho + 1)
    extent_sum = Fraction(0)
    seen = set()
    for piece in inst["pieces"]:
        if len(piece) != 3 or any((not isinstance(v, int)) or isinstance(v, bool) for v in piece):
            fail(f"instance {idx}: malformed piece")
        start, length, mult = piece
        if mult < 1 or length < 1 or r % length or length & (length - 1):
            fail(f"instance {idx}: V2 bad piece size or multiplicity")
        if start < 0 or start + length > n_pts or start % length:
            fail(f"instance {idx}: V2 piece is not a dyadic sub-block")
        if (start, length) in seen:
            fail(f"instance {idx}: V2 duplicate piece")
        seen.add((start, length))
        level = (r // length).bit_length() - 1
        per_level[level] += mult
        for t in seq[start : start + length]:
            totals[t] += mult
        extent_sum += mult * (xs[start + length - 1] - xs[start])
    need = Fraction(T * r, k)
    if need.denominator != 1:
        fail(f"instance {idx}: T r / k is not an integer")
    if any(totals[j] != need for j in range(1, k + 1)):
        fail(f"instance {idx}: V3 composition mismatch")
    if per_level[0] > T or any(c > 2 * (k - 1) for c in per_level[1:]):
        fail(f"instance {idx}: V4 too many pieces at some level: {per_level}")
    if sum(per_level) > T + (k - 1) * rho:
        fail(f"instance {idx}: V4 too many pieces in total: {per_level}")
    budget = Fraction(T * r, k * q) * span_p
    if extent_sum > budget:
        fail(f"instance {idx}: V5 extent budget exceeded")

    # V6: assemble with unit gaps and re-check every pair
    ys, ms = [], []
    cursor = None
    n_pieces = 0
    for start, length, mult in sorted(inst["pieces"]):
        for _ in range(mult):
            base = Fraction(0) if cursor is None else cursor + 1
            x0 = xs[start]
            for i in range(start, start + length):
                ys.append(base + xs[i] - x0)
                ms.append(mark[seq[i]])
            cursor = ys[-1]
            n_pieces += 1
    if len(ys) != T * r:
        fail(f"instance {idx}: V6 assembled size mismatch")
    if not all_pairs_ok(ys, ms):
        fail(f"instance {idx}: V6 assembled placement is infeasible")
    span_v = max(ys) - min(ys)
    if span_v != extent_sum + (n_pieces - 1):
        fail(f"instance {idx}: V6 span accounting mismatch")
    bound = budget + T + (k - 1) * rho - 1
    if span_v > bound:
        fail(f"instance {idx}: V6 span bound violated")

    return {
        "points": n_pts,
        "assembled": len(ys),
        "pieces": n_pieces,
        "per_level": per_level,
        "span_p": span_p,
        "span_v": span_v,
        "bound": bound,
    }


def verify_counting(kappa_max: int = 6, rho_max: int = 8, n_max: int = 600) -> int:
    """V7: the counting step, checked exhaustively on a parameter box."""
    checked = 0
    for kappa in range(kappa_max + 1):
        k = 1 << kappa
        for rho in range(kappa, rho_max + 1):
            r = 1 << rho
            for n in range(2, n_max + 1):
                per_type = -(-n // k)  # ceil(n / k)
                T = -(-per_type // (r // k))
                if T < 1 or T * r > n + r - 1:
                    fail(f"V7 size bound fails at k={k} r={r} n={n}")
                counts = [0] * (k + 1)
                for i in range(1, n + 1):
                    j = -(-i * k // n)  # ceil(i k / n)
                    if not (1 <= j <= k) or i * k > j * n:
                        fail(f"V7 type assignment fails at k={k} n={n} i={i}")
                    counts[j] += 1
                if max(counts) > T * r // k:
                    fail(f"V7 demand exceeds supply at k={k} r={r} n={n}")
                checked += 1
    return checked


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    t0 = time.perf_counter()
    with open(sys.argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("schema") != "ringmin-rounding-certificates/1":
        fail("unknown schema")
    pairs = 0
    for idx, inst in enumerate(data["instances"]):
        res = verify_instance(idx, inst)
        pairs += res["points"] * (res["points"] - 1) // 2
        pairs += res["assembled"] * (res["assembled"] - 1) // 2
        k, r = 1 << inst["kappa"], 1 << inst["rho"]
        print(
            f"PASS {idx:2d} p={inst['p']} k={k:2d} r={r:2d} q={inst['q']:2d} T={inst['T']:2d} "
            f"pieces/level={res['per_level']} span={float(res['span_v']):.6f} "
            f"<= bound={float(res['bound']):.6f}"
        )
    counted = verify_counting()
    print(f"PASS V7 counting step on {counted} parameter triples")
    print(
        f"ALL PASS: {len(data['instances'])} instances, {pairs} exact pair checks, "
        f"{time.perf_counter() - t0:.1f}s"
    )


if __name__ == "__main__":
    main()
