#!/usr/bin/env python3
"""Generator for the explicit-rate table of NOTE_QUANTILE_RATE.md.

For k = 2**kappa <= r = 2**rho put

    T(n, kappa, rho) = ceil( ceil(n/k) / (r/k) ),
    B(n, kappa, rho; e) = T r (e + 1/k) + T + (k-1) rho - 1 - n e,

so that Theorem 1 reads  b_n^Q - n E <= M * B(n, kappa, rho; E/M).  This
script minimises B over 0 <= kappa <= rho for selected n, both for the
law-free value e = 1 and for the uniform law, where e <= E_UP with

    E_UP = 0.4428345 > pi * 0.140958576058 > pi * C_*      (imported bound).

Integer arithmetic only.  The output is an untrusted table;
rate_bound_verify.py recomputes every number with separate code.

Usage:
    python -I rate_bound_generate.py --out rate_bound_table.json
"""
from __future__ import annotations

import argparse
import json
import math
import time

# Rational upper bound for E = pi * C_* in the uniform case (see the note, 5.2).
E_UP_NUM, E_UP_DEN = 4428345, 10**7
# Rational lower bound for pi used for the ring-coefficient column.
PI_LO_NUM, PI_LO_DEN = 314159265358, 10**11

TABLE_N = [10**j for j in range(2, 13)] + [3200, 2**14, 2**20, 2**30]
LOG_POWER = 64  # log2(n) >= (bit_length(n**LOG_POWER) - 1) / LOG_POWER


def t_value(n: int, kappa: int, rho: int) -> int:
    k = 1 << kappa
    step = 1 << (rho - kappa)
    per_type = (n + k - 1) // k
    return (per_type + step - 1) // step


def bound_num(n: int, kappa: int, rho: int, e_num: int, e_den: int) -> tuple[int, int]:
    """B(n, kappa, rho; e_num/e_den) as (numerator, denominator = k * e_den)."""
    k, r = 1 << kappa, 1 << rho
    t = t_value(n, kappa, rho)
    num = t * r * (e_num * k + e_den) + k * e_den * (t + (k - 1) * rho - 1) - n * e_num * k
    return num, k * e_den


def minimise(n: int, e_num: int, e_den: int):
    best = None
    for rho in range(n.bit_length() + 3):
        for kappa in range(rho + 1):
            num, den = bound_num(n, kappa, rho, e_num, e_den)
            if best is None or num * best[1] < best[0] * den:
                best = (num, den, kappa, rho)
    return best


def log2_lower(n: int) -> tuple[int, int]:
    return (n**LOG_POWER).bit_length() - 1, LOG_POWER


def ratio_ceiling(num: int, den: int, n: int, places: int = 4) -> str:
    """Smallest decimal c (given places) with (num/den)**2 <= c**2 n L_lo."""
    l_num, l_den = log2_lower(n)
    scale = 10**places
    # c = m / scale ;  need num^2 * scale^2 * l_den <= m^2 * den^2 * n * l_num
    lhs = num * num * scale * scale * l_den
    rhs_unit = den * den * n * l_num
    m = math.isqrt(lhs // rhs_unit)
    while m * m * rhs_unit < lhs:
        m += 1
    return f"{m // scale}.{m % scale:0{places}d}"


def decimal_ceiling(num: int, den: int, places: int) -> str:
    scale = 10**places
    m = -((-num * scale) // den)
    return f"{m // scale}.{m % scale:0{places}d}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="rate_bound_table.json")
    args = ap.parse_args()
    t0 = time.perf_counter()
    rows = []
    for n in sorted(TABLE_N):
        row = {"n": n}
        for tag, (e_num, e_den) in (("law_free", (1, 1)), ("uniform", (E_UP_NUM, E_UP_DEN))):
            num, den, kappa, rho = minimise(n, e_num, e_den)
            g = math.gcd(num, den)
            entry = {
                "kappa": kappa,
                "rho": rho,
                "T": t_value(n, kappa, rho),
                "B": f"{num // g}/{den // g}",
                "ratio_ceiling": ratio_ceiling(num, den, n),
            }
            if tag == "uniform":
                # (B + 1) / (pi n) <= (B + 1) / (PI_LO n)
                entry["ring_error_ceiling"] = decimal_ceiling(
                    (num + den) * PI_LO_DEN, den * PI_LO_NUM * n, 9
                )
            row[tag] = entry
        rows.append(row)
        print(n, row["law_free"]["B"], row["law_free"]["ratio_ceiling"], row["uniform"]["ring_error_ceiling"])
    doc = {
        "schema": "ringmin-rate-bound-table/1",
        "e_up": f"{E_UP_NUM}/{E_UP_DEN}",
        "pi_lo": f"{PI_LO_NUM}/{PI_LO_DEN}",
        "log_power": LOG_POWER,
        "rows": rows,
    }
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=1)
        fh.write("\n")
    print(f"wrote {args.out} in {time.perf_counter() - t0:.2f}s")


if __name__ == "__main__":
    main()
