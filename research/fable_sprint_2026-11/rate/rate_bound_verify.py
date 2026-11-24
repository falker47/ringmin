#!/usr/bin/env python3
"""Independent exact verifier for the explicit-rate statements.

Standard library only; shares no code with rate_bound_generate.py.

Checks, in exact rational arithmetic:

    R1  rigorous rational bounds PI_LO < pi < PI_UP from Machin's formula
        pi = 16 atan(1/5) - 4 atan(1/239) with alternating-series bounds,
        and  E_UP = 4428345/10^7 > PI_UP * 0.140958576058  (so E_UP exceeds
        E = pi C_* for the uniform law, given the imported bound on C_*);
    R2  every table row: T is the least admissible integer, the recorded B
        equals T r (e + 1/k) + T + (k-1) rho - 1 - n e, the recorded pair
        (kappa, rho) minimises B over the stated box, and the two decimal
        ceilings are valid upper bounds;
    R3  the finite part of Corollary 2:  for every 2 <= n <= N_MAX,
            min_{kappa <= rho} B(n, kappa, rho; 1) <= (5/2) sqrt(n L),
        where L <= log2(n) is a rational lower bound;
    R4  the analytic part of Corollary 2 at its threshold: with L = 11,
            (3/2) sqrt(1 + 2/L) + (5/2)/sqrt(L)
              + 2 sqrt(1 + 2/L) / 2^(L/2)  <  5/2,
        proved through rational upper bounds of the three square roots.

Usage:
    python -I -S rate_bound_verify.py rate_bound_table.json [N_MAX]
"""
from __future__ import annotations

import json
import math
import sys
import time
from fractions import Fraction as Fr

C_STAR_UP = Fr(140958576058, 10**12)  # imported: Paper II, Proposition 6.1


def fail(msg: str) -> None:
    print("FAIL:", msg)
    sys.exit(1)


def atan_inv_bounds(m: int, terms: int) -> tuple[Fr, Fr]:
    """Rational (lower, upper) bounds for atan(1/m) from the alternating series."""
    partial = Fr(0)
    sums = []
    for i in range(terms):
        partial += Fr((-1) ** i, (2 * i + 1) * m ** (2 * i + 1))
        sums.append(partial)
    # consecutive partial sums of a decreasing alternating series bracket the limit
    a, b = sums[-2], sums[-1]
    return min(a, b), max(a, b)


def pi_bounds() -> tuple[Fr, Fr]:
    lo5, up5 = atan_inv_bounds(5, 14)
    lo239, up239 = atan_inv_bounds(239, 6)
    return 16 * lo5 - 4 * up239, 16 * up5 - 4 * lo239


def t_least(n: int, k: int, r: int) -> int:
    """Least T >= 1 with T * (r/k) >= ceil(n/k), found by direct search."""
    per_type = n // k + (1 if n % k else 0)
    step = r // k
    t = max(1, per_type // step)
    while t * step < per_type:
        t += 1
    while t > 1 and (t - 1) * step >= per_type:
        t -= 1
    return t


def bound(n: int, kappa: int, rho: int, e: Fr) -> Fr:
    k, r = 2**kappa, 2**rho
    t = t_least(n, k, r)
    return t * r * (e + Fr(1, k)) + t + (k - 1) * rho - 1 - n * e


def log2_lower(n: int, power: int) -> Fr:
    # 2^(bits-1) <= n^power  =>  log2 n >= (bits - 1)/power
    return Fr((n**power).bit_length() - 1, power)


def parse_frac(text: str) -> Fr:
    num, den = text.split("/")
    return Fr(int(num), int(den))


def sqrt_upper(x: Fr, digits: int = 12) -> Fr:
    """Rational y >= sqrt(x), verified by y*y >= x."""
    scale = 10**digits
    target = (x.numerator * scale * scale) // x.denominator + 1
    y = Fr(math.isqrt(target) + 1, scale)
    if y * y < x:
        fail("sqrt_upper self-check")
    return y


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    n_max = int(sys.argv[2]) if len(sys.argv) == 3 else 2**15
    t0 = time.perf_counter()
    with open(sys.argv[1], encoding="utf-8") as fh:
        doc = json.load(fh)
    if doc.get("schema") != "ringmin-rate-bound-table/1":
        fail("unknown schema")

    # R1
    pi_lo, pi_up = pi_bounds()
    if not (Fr(314159265358, 10**11) < pi_lo < pi_up < Fr(314159265359, 10**11)):
        fail("R1 Machin enclosure too wide")
    table_pi_lo = parse_frac(doc["pi_lo"])
    e_up = parse_frac(doc["e_up"])
    if not table_pi_lo <= pi_lo:
        fail("R1 table pi_lo is not a lower bound")
    if not e_up > pi_up * C_STAR_UP:
        fail("R1 E_UP does not exceed pi_up * C_star_up")
    if not e_up <= 1:
        fail("R1 E_UP exceeds M = 1")
    print(f"PASS R1 pi in ({float(pi_lo):.12f}, {float(pi_up):.12f}), E_UP = {float(e_up)}")

    # R2
    power = doc["log_power"]
    for row in doc["rows"]:
        n = row["n"]
        for tag, e in (("law_free", Fr(1)), ("uniform", e_up)):
            ent = row[tag]
            kappa, rho = ent["kappa"], ent["rho"]
            if not (0 <= kappa <= rho):
                fail(f"R2 n={n} {tag}: kappa > rho")
            k, r = 2**kappa, 2**rho
            if ent["T"] != t_least(n, k, r):
                fail(f"R2 n={n} {tag}: T mismatch")
            val = bound(n, kappa, rho, e)
            if val != parse_frac(ent["B"]):
                fail(f"R2 n={n} {tag}: B mismatch")
            box = n.bit_length() + 3
            for rr in range(box):
                for kk in range(rr + 1):
                    if bound(n, kk, rr, e) < val:
                        fail(f"R2 n={n} {tag}: ({kk},{rr}) beats the recorded pair")
            c = Fr(ent["ratio_ceiling"])
            if val * val > c * c * n * log2_lower(n, power):
                fail(f"R2 n={n} {tag}: ratio ceiling invalid")
            if tag == "uniform":
                ring = (val + 1) / (pi_lo * n)
                if Fr(ent["ring_error_ceiling"]) < ring:
                    fail(f"R2 n={n}: ring error ceiling invalid")
    print(f"PASS R2 {len(doc['rows'])} table rows (values, minimality on the box, ceilings)")

    # R3
    worst = (Fr(0), 0)
    for n in range(2, n_max + 1):
        best = None
        for rho in range(n.bit_length() + 1):
            r = 2**rho
            for kappa in range(rho + 1):
                k = 2**kappa
                t = t_least(n, k, r)
                # k * B(n, kappa, rho; 1), an integer
                kb = t * r * (k + 1) + k * (t + (k - 1) * rho - 1 - n)
                if best is None or kb * best[1] < best[0] * k:
                    best = (kb, k)
        val = Fr(best[0], best[1])
        lo = log2_lower(n, 16)
        if 4 * val * val > 25 * n * lo:
            fail(f"R3 n={n}: min B = {val} exceeds (5/2) sqrt(n log2 n)")
        q = val * val / (n * lo)
        if q > worst[0]:
            worst = (q, n)
    print(
        f"PASS R3 2 <= n <= {n_max}: min B <= (5/2) sqrt(n log2 n); "
        f"largest (min B)^2/(n L) = {float(worst[0]):.4f} at n = {worst[1]} (must be <= 6.25)"
    )

    # R4
    L = 11
    s1 = sqrt_upper(Fr(1) + Fr(2, L))  # sqrt(1 + 2/L)
    inv_sqrt_l = sqrt_upper(Fr(1, L))  # 1/sqrt(L)
    inv_sqrt_2 = sqrt_upper(Fr(1, 2))  # 1/sqrt(2)
    # 2^(-L/2) = 2^(-5) / sqrt(2) for L = 11
    total = Fr(3, 2) * s1 + Fr(5, 2) * inv_sqrt_l + 2 * s1 * inv_sqrt_2 / 2 ** (L // 2)
    if not total < Fr(5, 2):
        fail("R4 analytic threshold inequality")
    print(f"PASS R4 threshold constant at L = 11: {float(total):.6f} < 5/2")
    print(f"ALL PASS in {time.perf_counter() - t0:.1f}s")


if __name__ == "__main__":
    main()
