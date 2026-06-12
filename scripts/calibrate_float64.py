from __future__ import annotations

import argparse
import csv
import math
import multiprocessing as mp_pool
import random
import sys
import time
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]

TAU_FLOAT = 2.0 * math.pi


def canonical_random_order(n: int, rng: random.Random) -> tuple[int, ...]:
    rest = list(range(1, n))
    rng.shuffle(rest)
    order = (n, *rest)
    if order[1] > order[-1]:
        order = (order[0], *reversed(order[1:]))
    return tuple(order)


def theta_float(R: float, a: float, b: float) -> float:
    return 2.0 * math.asin(math.sqrt((a * b) / ((R + a) * (R + b))))


def chain_radius_float(order: tuple[int, ...]) -> float:
    lo = 1e-9
    hi = 4.0 * len(order) * len(order)
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        total = 0.0
        for i, a in enumerate(order):
            total += theta_float(mid, float(a), float(order[(i + 1) % len(order)]))
        if total > TAU_FLOAT:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def induced(order: tuple[int, ...], removed: set[int]) -> tuple[int, ...]:
    return tuple(value for value in order if value not in removed)


def lower_bound_float(order: tuple[int, ...]) -> float:
    return max(radius for _, radius in component_float_radii(order))


def component_orders(order: tuple[int, ...]) -> list[tuple[int, ...]]:
    components = [order]
    without_1 = induced(order, {1})
    if len(without_1) >= 3:
        components.append(without_1)
    without_1_2 = induced(order, {1, 2})
    if len(without_1_2) >= 3:
        components.append(without_1_2)
    return components


def component_float_radii(order: tuple[int, ...]) -> list[tuple[tuple[int, ...], float]]:
    return [(component, chain_radius_float(component)) for component in component_orders(order)]


def theta_mp(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return 2 * mp.asin(mp.sqrt((a * b) / ((R + a) * (R + b))))


def theta_derivative_mp(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    x = mp.sqrt((a * b) / ((R + a) * (R + b)))
    return -x * (1 / (R + a) + 1 / (R + b)) / mp.sqrt(1 - x * x)


def chain_sum_mp(R: mp.mpf, order: tuple[int, ...]) -> mp.mpf:
    radii = tuple(mp.mpf(value) for value in order)
    return mp.fsum(theta_mp(R, radii[i], radii[(i + 1) % len(radii)]) for i in range(len(radii)))


def chain_sum_derivative_mp(R: mp.mpf, order: tuple[int, ...]) -> mp.mpf:
    radii = tuple(mp.mpf(value) for value in order)
    return mp.fsum(
        theta_derivative_mp(R, radii[i], radii[(i + 1) % len(radii)])
        for i in range(len(radii))
    )


def chain_radius_mp(order: tuple[int, ...], start: float) -> mp.mpf:
    target = 2 * mp.pi
    R = mp.mpf(str(start))
    for _ in range(3):
        residual = chain_sum_mp(R, order) - target
        if abs(residual) < mp.mpf("1e-45"):
            return R
        R -= residual / chain_sum_derivative_mp(R, order)
        if R <= 0:
            break

    lo = mp.mpf("1e-9")
    hi = mp.mpf(4 * len(order) * len(order))
    for _ in range(170):
        mid = (lo + hi) / 2
        if chain_sum_mp(mid, order) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def lower_bound_mp(order: tuple[int, ...]) -> mp.mpf:
    return max(chain_radius_mp(component, start) for component, start in component_float_radii(order))


def lower_bounds_float_and_mp(order: tuple[int, ...]) -> tuple[mp.mpf, mp.mpf]:
    components = component_float_radii(order)
    lb_float = max(mp.mpf(str(radius)) for _, radius in components)
    lb_mp = max(chain_radius_mp(component, radius) for component, radius in components)
    return lb_float, lb_mp


def calibrate_batch(batch: list[tuple[int, ...]]) -> tuple[str, str, str, tuple[int, ...]]:
    mp.mp.dps = 50
    max_abs = mp.mpf("0")
    max_over = mp.mpf("0")
    worst_order: tuple[int, ...] = ()
    for order in batch:
        lb_float, lb_mp = lower_bounds_float_and_mp(order)
        diff = lb_mp - lb_float
        if abs(diff) > max_abs:
            max_abs = abs(diff)
            worst_order = order
        if diff < 0:
            max_over = max(max_over, -diff)
    return mp.nstr(max_abs, 25), mp.nstr(max_over, 25), str(len(batch)), worst_order


def chunks(values: list[tuple[int, ...]], size: int) -> list[list[tuple[int, ...]]]:
    return [values[i : i + size] for i in range(0, len(values), size)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=8)
    parser.add_argument("--stop", type=int, default=14)
    parser.add_argument("--samples", type=int, default=100000)
    parser.add_argument("--seed", type=int, default=4619480)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=250)
    args = parser.parse_args()

    started = time.perf_counter()
    rows: list[dict[str, object]] = []
    global_max = mp.mpf("0")
    global_over = mp.mpf("0")
    global_worst: tuple[int, ...] = ()

    for n in range(args.start, args.stop + 1):
        rng = random.Random(args.seed + 1009 * n)
        orders = [canonical_random_order(n, rng) for _ in range(args.samples)]
        batches = chunks(orders, args.batch_size)
        n_max = mp.mpf("0")
        n_over = mp.mpf("0")
        n_worst: tuple[int, ...] = ()
        if args.workers <= 1:
            results = [calibrate_batch(batch) for batch in batches]
        else:
            with mp_pool.Pool(processes=args.workers) as pool:
                results = list(pool.imap_unordered(calibrate_batch, batches))
        for max_abs_text, max_over_text, _, worst_order in results:
            max_abs = mp.mpf(max_abs_text)
            max_over = mp.mpf(max_over_text)
            if max_abs > n_max:
                n_max = max_abs
                n_worst = worst_order
            n_over = max(n_over, max_over)
        if n_max > global_max:
            global_max = n_max
            global_worst = n_worst
        global_over = max(global_over, n_over)
        row = {
            "n": n,
            "samples": args.samples,
            "max_abs_deviation": mp.nstr(n_max, 18),
            "max_float64_overestimate": mp.nstr(n_over, 18),
            "worst_order": list(n_worst),
        }
        rows.append(row)
        print(
            f"n={n} samples={args.samples} max_abs={row['max_abs_deviation']} "
            f"max_over={row['max_float64_overestimate']} worst={row['worst_order']}",
            flush=True,
        )

    out = ROOT / "results" / "float64_calibration.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    elapsed = time.perf_counter() - started
    print(f"wrote {out}")
    print(f"GLOBAL_MAX_ABS_DEVIATION={mp.nstr(global_max, 18)}")
    print(f"GLOBAL_MAX_FLOAT64_OVERESTIMATE={mp.nstr(global_over, 18)}")
    print(f"GLOBAL_WORST_ORDER={list(global_worst)}")
    print(f"RUNTIME_SECONDS={elapsed:.3f}")
    return 0 if global_max <= mp.mpf("1e-11") else 2


if __name__ == "__main__":
    raise SystemExit(main())
