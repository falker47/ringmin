#!/usr/bin/env python3
"""Untrusted float64 generator for the seam-onset certificate.

For k = 1..K it locates, in double precision, the first n at which the seam
deficit of the canonical Supnick cycle on {k,...,n} is negative at its chain
root, and writes a rational bracket for the chain root R_{k,n} at n = m-1 and
n = m.  For k <= K_WINDOW it writes a bracket for every n in
[k+2, 4k+WINDOW_EXTRA].

Nothing here is rigorous.  seam_verify.py (ball arithmetic) and
seam_verify_stdlib.py (exact rationals) re-derive every sign from the
brackets alone.

Usage:
    python -I seam_generate.py --kmax 4400 --out seam_certificate.json
"""
from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np
from scipy.optimize import brentq

REL_HALF_WIDTH = 1e-9
K_WINDOW = 60
WINDOW_EXTRA = 60


def supnick_radii(k: int, n: int) -> np.ndarray:
    """Radii of the canonical cycle sigma_{k,n} in cyclic order (float array)."""
    size = n - k + 1
    half = (size + 1) // 2
    a_list, b_list = [], []
    low, high = 1, size - 1
    while low <= half or high > half:
        if low <= half:
            a_list.append(low)
        if high > half:
            a_list.append(high)
        low += 2
        high -= 2
    low, high = 2, size - 2
    while low <= half or high > half:
        if low <= half:
            b_list.append(low)
        if high > half:
            b_list.append(high)
        low += 2
        high -= 2
    ranks = a_list + b_list[::-1] + [size]
    return np.asarray(ranks, dtype=np.float64) + (k - 1)


def theta(big_r: float, a, b):
    return 2.0 * np.arcsin(np.sqrt(a * b / ((big_r + a) * (big_r + b))))


def chain_root(k: int, n: int) -> float:
    cyc = supnick_radii(k, n)
    nxt = np.roll(cyc, -1)

    def excess(big_r: float) -> float:
        return float(theta(big_r, cyc, nxt).sum()) - 2.0 * math.pi

    return brentq(excess, 1e-6, 4.0 * n * n + 10.0, xtol=1e-14, rtol=4e-15, maxiter=500)


def deficit(k: int, n: int) -> tuple[float, float]:
    big_r = chain_root(k, n)
    d = theta(big_r, n, k) + theta(big_r, k, n - 1) - theta(big_r, n, n - 1)
    return big_r, float(d)


def record(k: int, n: int):
    big_r, d = deficit(k, n)
    lo = f"{big_r * (1.0 - REL_HALF_WIDTH):.15e}"
    hi = f"{big_r * (1.0 + REL_HALF_WIDTH):.15e}"
    return [k, n, lo, hi, 1 if d > 0 else -1]


def onset(k: int) -> int:
    n = max(k + 2, 4 * k + 3)
    while deficit(k, n)[1] < 0 and n > k + 2:
        n -= 1
    while deficit(k, n)[1] > 0:
        n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kmax", type=int, default=4400)
    ap.add_argument("--out", default="seam_certificate.json")
    args = ap.parse_args()
    t0 = time.perf_counter()
    records = []
    for k in range(1, args.kmax + 1):
        m = onset(k)
        if k <= K_WINDOW:
            ns = range(k + 2, 4 * k + WINDOW_EXTRA + 1)
        else:
            ns = (m - 1, m)
        for n in ns:
            records.append(record(k, n))
        if k % 400 == 0:
            print(f"k={k} onset={m} ({time.perf_counter() - t0:.0f}s)", flush=True)
    doc = {
        "schema": "ringmin-seam-certificate/1",
        "kmax": args.kmax,
        "k_window": K_WINDOW,
        "window_extra": WINDOW_EXTRA,
        "records": records,
    }
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, separators=(",", ":"))
        fh.write("\n")
    print(f"wrote {args.out}: {len(records)} records in {time.perf_counter() - t0:.0f}s")


if __name__ == "__main__":
    main()
