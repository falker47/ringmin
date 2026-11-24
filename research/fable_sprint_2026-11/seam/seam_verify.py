#!/usr/bin/env python3
"""Rigorous ball-arithmetic verifier for seam_certificate.json.

Requires python-flint (Arb).  Shares no code with seam_generate.py and does
not trust the recorded signs: it recomputes each of them.

Definitions (Paper I, Sections 3 and 5).  For integers k >= 1, n >= k+2 let
sigma_{k,n} be the canonical Supnick cycle on the radii k,...,n, let
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))), let R_{k,n} be the unique root
of  sum_{edges} theta_R = 2 pi,  and

    Delta_{k,n} = theta(n,k) + theta(k,n-1) - theta(n,n-1)   at R = R_{k,n}.

For each record (k, n, lo, hi, sign) with exact rationals lo < hi:

    S1  sigma_{k,n} is rebuilt from the rank rule; it is a cyclic arrangement
        of k..n in which the two neighbours of k are n-1 and n, and its edge
        set equals the explicit list (A.5) of Paper I, Appendix A;
    S2  C(lo) > 2 pi > C(hi) with certified strict inequalities, so the
        strictly decreasing angle sum has its root inside (lo, hi);
    S3  the ball for Delta evaluated on the whole interval [lo, hi] has the
        recorded strict sign.

Then, for every k <= kmax, the verifier extracts the unique consecutive pair
Delta_{k,m-1} > 0 > Delta_{k,m} and compares m with the closed form

    m = 8 (k = 1),   4k + 5 (2 <= k <= 5),   4k + 6 (k >= 6).

For k <= k_window it also checks the full sign pattern on
k+2 <= n <= 4k + window_extra.

Usage:
    python -I seam_verify.py seam_certificate.json [--jobs J]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from multiprocessing import Pool

from flint import arb, ctx, fmpq

PREC_BITS = 128


def canonical_cycle(k: int, n: int) -> list[int]:
    """sigma_{k,n}: concatenate A, reverse(B), N on ranks; shift ranks by k-1."""
    size = n - k + 1
    half = -(-size // 2)
    list_a: list[int] = []
    j = 0
    while True:
        progressed = False
        if 1 + 2 * j <= half:
            list_a.append(1 + 2 * j)
            progressed = True
        if size - 1 - 2 * j > half:
            list_a.append(size - 1 - 2 * j)
            progressed = True
        if not progressed:
            break
        j += 1
    list_b: list[int] = []
    j = 0
    while True:
        progressed = False
        if 2 + 2 * j <= half:
            list_b.append(2 + 2 * j)
            progressed = True
        if size - 2 - 2 * j > half:
            list_b.append(size - 2 - 2 * j)
            progressed = True
        if not progressed:
            break
        j += 1
    ranks = list_a + list(reversed(list_b)) + [size]
    return [k + rank - 1 for rank in ranks]


def edge_list_a5(k: int, n: int) -> set[tuple[int, int]]:
    """Edge set of sigma_{k,n} as printed in Paper I, Appendix A, eq. (A.5)."""
    size = n - k + 1
    total = k + n
    h = size // 2
    edges = [(k, n)]
    if size % 2 == 0:
        edges.append((k + h - 1, k + h))
        edges += [(i, total - 1 - i) for i in range(k, k + h - 1)]
        edges += [(i, total + 1 - i) for i in range(k + 1, k + h)]
    else:
        edges += [(i, total - 1 - i) for i in range(k, k + h)]
        edges += [(i, total + 1 - i) for i in range(k + 1, k + h + 1)]
    return {(min(a, b), max(a, b)) for a, b in edges}


def decimal_to_fmpq(text: str) -> fmpq:
    """Exact rational value of a decimal string such as '1.234e+03'."""
    mant, _, exp = text.lower().partition("e")
    exponent = int(exp) if exp else 0
    sign = -1 if mant.startswith("-") else 1
    mant = mant.lstrip("+-")
    whole, _, frac = mant.partition(".")
    digits = int((whole + frac) or "0")
    exponent -= len(frac)
    value = fmpq(sign * digits)
    if exponent >= 0:
        return value * fmpq(10**exponent)
    return value / fmpq(10**-exponent)


def angle(big_r: arb, a: int, b: int) -> arb:
    return 2 * (arb(a * b) / ((big_r + a) * (big_r + b))).sqrt().asin()


def check_record(rec):
    ctx.prec = PREC_BITS
    k, n, lo_text, hi_text, sign = rec
    if not (isinstance(k, int) and isinstance(n, int) and k >= 1 and n >= k + 2 and sign in (1, -1)):
        return (k, n, None, "malformed record")
    cyc = canonical_cycle(k, n)
    if sorted(cyc) != list(range(k, n + 1)):
        return (k, n, None, "S1 not a permutation")
    pos = cyc.index(k)
    nbrs = {cyc[pos - 1], cyc[(pos + 1) % len(cyc)]}
    if nbrs != {n - 1, n}:
        return (k, n, None, "S1 seam neighbours are not n-1, n")
    cyc_edges = {(min(a, b), max(a, b)) for a, b in zip(cyc, cyc[1:] + cyc[:1])}
    if len(cyc_edges) != len(cyc) or cyc_edges != edge_list_a5(k, n):
        return (k, n, None, "S1 cycle edges differ from the printed list (A.5)")
    lo_q, hi_q = decimal_to_fmpq(lo_text), decimal_to_fmpq(hi_text)
    if not (0 < lo_q < hi_q):
        return (k, n, None, "bracket not ordered")
    two_pi = 2 * arb.pi()
    sums = []
    for end in (lo_q, hi_q):
        big_r = arb(end)
        total = arb(0)
        prev = cyc[-1]
        for cur in cyc:
            total += angle(big_r, prev, cur)
            prev = cur
        sums.append(total - two_pi)
    if not (sums[0] > 0 and sums[1] < 0):
        return (k, n, None, "S2 root not bracketed")
    ball = arb(lo_q).union(arb(hi_q))
    delta = angle(ball, n, k) + angle(ball, k, n - 1) - angle(ball, n, n - 1)
    if delta > 0:
        got = 1
    elif delta < 0:
        got = -1
    else:
        return (k, n, None, "S3 sign of the deficit is not decided")
    if got != sign:
        return (k, n, None, "S3 recorded sign is wrong")
    return (k, n, got, float(abs(delta).lower()))


def expected_onset(k: int) -> int:
    if k == 1:
        return 8
    return 4 * k + 5 if k <= 5 else 4 * k + 6


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificate")
    ap.add_argument("--jobs", type=int, default=1)
    args = ap.parse_args()
    t0 = time.perf_counter()
    with open(args.certificate, encoding="utf-8") as fh:
        doc = json.load(fh)
    if doc.get("schema") != "ringmin-seam-certificate/1":
        print("FAIL: unknown schema")
        sys.exit(1)
    records = doc["records"]
    if args.jobs > 1:
        with Pool(args.jobs) as pool:
            results = pool.map(check_record, records, chunksize=16)
    else:
        results = [check_record(rec) for rec in records]

    signs: dict[int, dict[int, int]] = {}
    min_margin = None
    for k, n, got, info in results:
        if got is None:
            print(f"FAIL: k={k} n={n}: {info}")
            sys.exit(1)
        if n in signs.setdefault(k, {}):
            print(f"FAIL: duplicate record k={k} n={n}")
            sys.exit(1)
        signs[k][n] = got
        if min_margin is None or info < min_margin[0]:
            min_margin = (info, k, n)

    kmax, k_window, extra = doc["kmax"], doc["k_window"], doc["window_extra"]
    onsets = {}
    for k in range(1, kmax + 1):
        row = signs.get(k, {})
        flips = [n for n in row if row[n] == -1 and row.get(n - 1) == 1]
        if len(flips) != 1:
            print(f"FAIL: k={k}: no unique certified sign change")
            sys.exit(1)
        m = flips[0]
        if m != expected_onset(k):
            print(f"FAIL: k={k}: certified onset {m} differs from the closed form")
            sys.exit(1)
        onsets[k] = m
        if k <= k_window:
            for n in range(k + 2, 4 * k + extra + 1):
                want = 1 if n < m else -1
                if row.get(n) != want:
                    print(f"FAIL: k={k} n={n}: window sign pattern broken")
                    sys.exit(1)
    print(f"PASS S1-S3 on {len(records)} records at {PREC_BITS} bits")
    print(f"PASS onsets for 1 <= k <= {kmax}: s_1=8, s_k=4k+5 (2<=k<=5), s_k=4k+6 (6<=k<={kmax})")
    print(
        f"PASS full sign pattern on k+2 <= n <= 4k+{extra} for 1 <= k <= {k_window}"
    )
    print(f"first rows: {[(k, onsets[k]) for k in range(1, 11)]}")
    print(f"smallest certified |Delta| lower bound: {min_margin[0]:.3e} at (k, n) = {min_margin[1:]}")
    print(f"ALL PASS in {time.perf_counter() - t0:.0f}s")


if __name__ == "__main__":
    main()
