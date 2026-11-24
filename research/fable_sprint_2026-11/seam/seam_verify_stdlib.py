#!/usr/bin/env python3
"""Exact-rational cross-check of the seam certificate (standard library only).

A second, slower verifier that uses no ball-arithmetic library.  It replays
the two onset records (n = m-1 and n = m) of every k <= KSTD with
fractions.Fraction and proves the same three facts as seam_verify.py:

    the chain root lies in (lo, hi);  Delta_{k,m-1} > 0;  Delta_{k,m} < 0.

The cycle is taken from the explicit edge list (A.5) of Paper I, Appendix A,
not from the rank rule used by seam_verify.py, so the two verifiers also
differ in how they read the definition of sigma_{k,n}.

Method.  For rational R and integers a, b put q = ab/((R+a)(R+b)), so that
theta = 2 asin sqrt(q) lies in (0, pi) and cos(theta) = 1 - 2q exactly.
A dyadic interval (l, u) contains theta as soon as

    cos(l) > 1 - 2q > cos(u),        0 < l < u < 3.14,

because cos is strictly decreasing on [0, pi].  Both cosines are bounded by
consecutive Taylor partial sums (alternating series with decreasing terms
for arguments below 3.14).  The interval is proposed from a float value and
then proved; the float is not trusted.  pi is enclosed by Machin's formula.
Since theta_R is strictly decreasing in R, the deficit on [lo, hi] is
bounded by combining the angles at the two endpoints.

Usage:
    python -I -S seam_verify_stdlib.py seam_certificate.json [KSTD]
"""
from __future__ import annotations

import json
import math
import sys
import time
from fractions import Fraction as Fr

SLACK = Fr(1, 2**40)
TAYLOR_TERMS = 22


def fail(msg: str) -> None:
    print("FAIL:", msg)
    sys.exit(1)


def cos_bounds(x: Fr) -> tuple[Fr, Fr]:
    """Rational (lower, upper) bounds for cos(x), 0 < x < 3.14."""
    if not (0 < x < Fr(314, 100)):
        fail("cosine argument out of range")
    x2 = x * x
    term = Fr(1)
    partial = Fr(1)
    sums = [partial]
    for i in range(1, TAYLOR_TERMS + 1):
        term = -term * x2 / ((2 * i - 1) * (2 * i))
        partial += term
        sums.append(partial)
    a, b = sums[-2], sums[-1]
    return min(a, b), max(a, b)


def atan_inv_bounds(m: int, terms: int) -> tuple[Fr, Fr]:
    partial = Fr(0)
    sums = []
    for i in range(terms):
        partial += Fr((-1) ** i, (2 * i + 1) * m ** (2 * i + 1))
        sums.append(partial)
    a, b = sums[-2], sums[-1]
    return min(a, b), max(a, b)


def pi_bounds() -> tuple[Fr, Fr]:
    lo5, up5 = atan_inv_bounds(5, 30)
    lo239, up239 = atan_inv_bounds(239, 10)
    return 16 * lo5 - 4 * up239, 16 * up5 - 4 * lo239


def angle_bounds(big_r: Fr, a: int, b: int) -> tuple[Fr, Fr]:
    """Proved rational (l, u) with l < theta_R(a, b) < u."""
    q = Fr(a * b) / ((big_r + a) * (big_r + b))
    guess = Fr(2.0 * math.asin(math.sqrt(float(q))))
    low, up = guess - SLACK, guess + SLACK
    target = 1 - 2 * q
    if not cos_bounds(low)[0] > target:
        fail("lower angle bound not proved")
    if not cos_bounds(up)[1] < target:
        fail("upper angle bound not proved")
    return low, up


def cycle_edges(k: int, n: int) -> list[tuple[int, int]]:
    """Edges of sigma_{k,n}, taken from Paper I, Appendix A, eq. (A.5).

    This verifier never builds the cycle from the rank rule; it only checks
    that the printed edge list is a single Hamiltonian cycle on k..n whose
    seam vertex k is joined to n-1 and n.
    """
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
    nbrs: dict[int, list[int]] = {v: [] for v in range(k, n + 1)}
    for a, b in edges:
        if a == b or a not in nbrs or b not in nbrs:
            fail(f"bad edge in (A.5) for k={k}, n={n}")
        nbrs[a].append(b)
        nbrs[b].append(a)
    if len(edges) != size or any(len(v) != 2 for v in nbrs.values()):
        fail(f"(A.5) is not 2-regular for k={k}, n={n}")
    if sorted(nbrs[k]) != [n - 1, n]:
        fail(f"seam neighbours of k are not n-1, n for k={k}, n={n}")
    prev, cur, steps = k, nbrs[k][0], 1
    while cur != k:
        nxt = nbrs[cur][0] if nbrs[cur][0] != prev else nbrs[cur][1]
        prev, cur = cur, nxt
        steps += 1
    if steps != size:
        fail(f"(A.5) is not a single cycle for k={k}, n={n}")
    return edges


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    kstd = int(sys.argv[2]) if len(sys.argv) == 3 else 100
    t0 = time.perf_counter()
    with open(sys.argv[1], encoding="utf-8") as fh:
        doc = json.load(fh)
    pi_lo, pi_up = pi_bounds()
    if not (Fr(31415926535897932, 10**16) < pi_lo < pi_up < Fr(31415926535897933, 10**16)):
        fail("Machin enclosure too wide")
    by_k: dict[int, dict[int, tuple[Fr, Fr]]] = {}
    for k, n, lo_text, hi_text, _sign in doc["records"]:
        if k <= kstd:
            by_k.setdefault(k, {})[n] = (Fr(lo_text), Fr(hi_text))
    angles = 0
    for k in range(1, kstd + 1):
        m = 8 if k == 1 else (4 * k + 5 if k <= 5 else 4 * k + 6)
        for n, want in ((m - 1, 1), (m, -1)):
            if n not in by_k.get(k, {}):
                fail(f"missing record k={k} n={n}")
            lo, hi = by_k[k][n]
            if not 0 < lo < hi:
                fail(f"bad bracket k={k} n={n}")
            sum_low_at_lo = Fr(0)
            sum_up_at_hi = Fr(0)
            for a, b in cycle_edges(k, n):
                sum_low_at_lo += angle_bounds(lo, a, b)[0]
                sum_up_at_hi += angle_bounds(hi, a, b)[1]
                angles += 2
            if not sum_low_at_lo > 2 * pi_up:
                fail(f"k={k} n={n}: C(lo) > 2 pi not proved")
            if not sum_up_at_hi < 2 * pi_lo:
                fail(f"k={k} n={n}: C(hi) < 2 pi not proved")
            seam_lo = [angle_bounds(lo, *pair) for pair in ((n, k), (k, n - 1), (n, n - 1))]
            seam_hi = [angle_bounds(hi, *pair) for pair in ((n, k), (k, n - 1), (n, n - 1))]
            angles += 6
            # theta decreases in R: on [lo, hi] each angle lies in (low at hi, up at lo)
            delta_min = seam_hi[0][0] + seam_hi[1][0] - seam_lo[2][1]
            delta_max = seam_lo[0][1] + seam_lo[1][1] - seam_hi[2][0]
            if want == 1 and not delta_min > 0:
                fail(f"k={k} n={n}: Delta > 0 not proved")
            if want == -1 and not delta_max < 0:
                fail(f"k={k} n={n}: Delta < 0 not proved")
    print(
        f"ALL PASS: onsets s_1=8, s_k=4k+5 (2<=k<=5), s_k=4k+6 (6<=k<={kstd}) "
        f"re-proved in exact rationals; {angles} angle enclosures, "
        f"{time.perf_counter() - t0:.0f}s"
    )


if __name__ == "__main__":
    main()
