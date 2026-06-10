from __future__ import annotations

import argparse
import csv
import json
import math
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import FullResult, chain_radius, full_radius, full_radius_value
from ringmin.patterns import supnick_max_tour


CSV_METADATA = (
    "# pocket_supnick_subset_definition="
    "Supnick maximum tour on the subset {2,...,n}, evaluated at that subset tour's "
    "own adjacent-chain radius R_chain(Supnick({2,...,n})); value is the maximum "
    "Descartes pocket radius over adjacent pairs of that subset tour at that R. "
    "Legacy max_pocket was different: it was the maximum adjacent-pair pocket of "
    "the reported heuristic full {1,...,n} order, evaluated at that order's "
    "heuristic R_full; at n=14 this was 1.643769515813, while "
    "pocket_supnick_subset is 1.672994284651."
)

HEURISTIC_SCHEMA: dict[str, object] = {
    "artifact": "heuristic_n14_18",
    "label": "NON-EXHAUSTIVE",
    "fields": {
        "pocket_supnick_subset": {
            "definition": (
                "Maximum Descartes pocket radius over adjacent pairs of the Supnick "
                "maximum tour on the subset {2,...,n}, evaluated at that subset "
                "tour's own adjacent-chain radius R_chain(Supnick({2,...,n}))."
            ),
            "note": (
                "This is a free-float criterion for adding circle 1 to the "
                "Supnick {2,...,n} tour. It is not evaluated on the heuristic "
                "full n-circle order and not evaluated at the heuristic R_full."
            ),
        },
        "realized_hosting_pockets": {
            "definition": (
                "For each floating circle in the heuristic full order, skip adjacent "
                "floating circles to find the essential bridged nonfloating pair "
                "(a,b), then report the Descartes pocket radius of (a,b) at the "
                "heuristic full radius R_full."
            ),
        },
    },
    "legacy_max_pocket_note": (
        "The retired max_pocket field used a different subset/tour and radius: it "
        "was the maximum adjacent-pair Descartes pocket of the reported heuristic "
        "full {1,...,n} order, evaluated at that order's heuristic R_full. The new "
        "pocket_supnick_subset field uses the Supnick {2,...,n} tour and evaluates "
        "at R_chain(Supnick({2,...,n})); for n=14 this changed 1.643769515813 to "
        "1.672994284651. The discrepancy is therefore not merely a different R; "
        "the evaluated tour/subset also changed."
    ),
}

CSV_FIELDNAMES = [
    "n",
    "label",
    "R_full",
    "R_chain",
    "ordering",
    "floating_circles",
    "essential_pairs",
    "pocket_supnick_subset",
    "realized_hosting_pockets",
    "best_restart_count",
    "runtime_seconds",
    "cache_size",
]


@dataclass(frozen=True)
class Objective:
    R_chain: float
    R_full: float


def canonical_tuple(order: tuple[int, ...]) -> tuple[int, ...]:
    n = len(order)
    max_value = max(order)
    idx = order.index(max_value)
    rotated = order[idx:] + order[:idx]
    reflected_rest = tuple(reversed(rotated[1:]))
    reflected = (max_value, *reflected_rest)
    return min(rotated, reflected)


def evaluate(order: tuple[int, ...], cache: dict[tuple[int, ...], Objective]) -> Objective:
    key = canonical_tuple(order)
    cached = cache.get(key)
    if cached is not None:
        return cached
    rc = chain_radius(key)
    _, rf = full_radius_value(key, R_chain=rc)
    objective = Objective(rc, rf)
    cache[key] = objective
    return objective


def greedy_insert(base: tuple[int, ...], inserts: tuple[int, ...], cache: dict[tuple[int, ...], Objective]) -> tuple[int, ...]:
    order = base
    for value in inserts:
        best_order: tuple[int, ...] | None = None
        best_value = math.inf
        for gap in range(len(order) + 1):
            candidate = order[:gap] + (value,) + order[gap:]
            value_full = evaluate(candidate, cache).R_full
            if value_full < best_value:
                best_value = value_full
                best_order = candidate
        if best_order is None:
            raise AssertionError("greedy insertion produced no candidate")
        order = best_order
    return order


def seed_orders(n: int, rng: random.Random, total: int, cache: dict[tuple[int, ...], Objective]) -> list[tuple[str, tuple[int, ...]]]:
    seeds: list[tuple[str, tuple[int, ...]]] = []
    values = tuple(range(1, n + 1))
    seeds.append(("supnick_full", tuple(int(x) for x in supnick_max_tour(values))))

    subset = tuple(int(x) for x in supnick_max_tour(range(2, n + 1)))
    for gap in range(len(subset) + 1):
        seeds.append((f"subset2_gap_{gap}", subset[:gap] + (1,) + subset[gap:]))

    subset3 = tuple(int(x) for x in supnick_max_tour(range(3, n + 1)))
    seeds.append(("subset3_greedy_1_2", greedy_insert(subset3, (1, 2), cache)))
    seeds.append(("subset3_greedy_2_1", greedy_insert(subset3, (2, 1), cache)))

    seen = {canonical_tuple(order) for _, order in seeds}
    while len(seeds) < total:
        order_list = list(values)
        rng.shuffle(order_list)
        order = tuple(order_list)
        key = canonical_tuple(order)
        if key in seen:
            continue
        seen.add(key)
        seeds.append((f"random_{len(seeds)}", order))
    return seeds[:total]


def random_move(order: tuple[int, ...], rng: random.Random) -> tuple[int, ...]:
    n = len(order)
    data = list(order)
    move = rng.randrange(3)
    if move == 0:
        i, j = rng.sample(range(n), 2)
        data[i], data[j] = data[j], data[i]
    elif move == 1:
        i, j = rng.sample(range(n), 2)
        value = data.pop(i)
        data.insert(j, value)
    else:
        i, j = sorted(rng.sample(range(n), 2))
        if i != j:
            data[i : j + 1] = reversed(data[i : j + 1])
    return tuple(data)


def local_search(
    start: tuple[int, ...],
    rng: random.Random,
    cache: dict[tuple[int, ...], Objective],
    max_rounds: int,
    samples_per_round: int,
) -> tuple[tuple[int, ...], Objective, int]:
    current = canonical_tuple(start)
    current_obj = evaluate(current, cache)
    evaluations = 1
    no_improve_rounds = 0

    for _ in range(max_rounds):
        best_neighbor = current
        best_obj = current_obj
        for _ in range(samples_per_round):
            neighbor = canonical_tuple(random_move(current, rng))
            obj = evaluate(neighbor, cache)
            evaluations += 1
            if obj.R_full < best_obj.R_full - 1e-10:
                best_neighbor = neighbor
                best_obj = obj
        if best_obj.R_full < current_obj.R_full - 1e-10:
            current = best_neighbor
            current_obj = best_obj
            no_improve_rounds = 0
        else:
            no_improve_rounds += 1
            if no_improve_rounds >= 6:
                break
    return current, current_obj, evaluations


def pocket_radius(R: float, a: float, b: float) -> float:
    curvature = (
        1.0 / R
        + 1.0 / a
        + 1.0 / b
        + 2.0 * math.sqrt(1.0 / (R * a) + 1.0 / (a * b) + 1.0 / (R * b))
    )
    return 1.0 / curvature


def max_pocket(result: FullResult) -> float:
    return max(
        pocket_radius(result.R_full, radius, result.order[(i + 1) % len(result.order)])
        for i, radius in enumerate(result.order)
    )


def pocket_supnick_subset(n: int) -> float:
    order = tuple(int(x) for x in supnick_max_tour(range(2, n + 1)))
    R = chain_radius(order)
    return max(pocket_radius(R, radius, order[(i + 1) % len(order)]) for i, radius in enumerate(order))


def realized_hosting_pockets(result: FullResult) -> list[dict[str, object]]:
    floating = set(int(x) for x in result.floating_radii)
    order = tuple(int(x) for x in result.order)
    essential_pairs = {
        tuple(sorted((binding.i, binding.j))): binding for binding in result.essential_tight_pairs
    }
    rows: list[dict[str, object]] = []
    for idx, radius in enumerate(order):
        if radius not in floating:
            continue
        prev_idx = (idx - 1) % len(order)
        while order[prev_idx] in floating:
            prev_idx = (prev_idx - 1) % len(order)
        next_idx = (idx + 1) % len(order)
        while order[next_idx] in floating:
            next_idx = (next_idx + 1) % len(order)
        pair_key = tuple(sorted((prev_idx, next_idx)))
        if pair_key not in essential_pairs:
            raise AssertionError(
                f"no essential bridged pair found for floater {radius}: "
                f"order={order}, prev={prev_idx}, next={next_idx}"
            )
        a = order[prev_idx]
        b = order[next_idx]
        rows.append(
            {
                "floater": radius,
                "host_pair": [a, b],
                "host_indices": [prev_idx, next_idx],
                "pocket_radius": pocket_radius(result.R_full, a, b),
            }
        )
    return rows


def result_payload(n: int, result: FullResult, best_restarts: int, runtime: float, cache_size: int) -> dict[str, object]:
    return {
        "schema": HEURISTIC_SCHEMA,
        "n": n,
        "label": "NON-EXHAUSTIVE",
        "R_full": result.R_full,
        "R_chain": result.R_chain,
        "ordering": [int(x) for x in result.order],
        "floating_circles": [int(x) for x in result.floating_radii],
        "essential_pairs": [
            {
                "i": pair.i,
                "j": pair.j,
                "radius_i": int(pair.radius_i),
                "radius_j": int(pair.radius_j),
                "kind": pair.kind,
                "slack": pair.slack,
                "adjacent": (pair.j == pair.i + 1)
                or (pair.i == 0 and pair.j == len(result.order) - 1),
            }
            for pair in result.essential_tight_pairs
        ],
        "pocket_supnick_subset": pocket_supnick_subset(n),
        "realized_hosting_pockets": realized_hosting_pockets(result),
        "best_restart_count": best_restarts,
        "runtime_seconds": runtime,
        "cache_size": cache_size,
    }


def run_one(n: int, restarts: int, seed: int, max_rounds: int, samples_per_round: int) -> dict[str, object]:
    rng = random.Random(seed + n * 1009)
    cache: dict[tuple[int, ...], Objective] = {}
    seeds = seed_orders(n, rng, restarts, cache)
    best_order: tuple[int, ...] | None = None
    best_obj: Objective | None = None
    best_restart_count = 0
    start_time = time.perf_counter()

    for idx, (kind, order) in enumerate(seeds, start=1):
        local_rng = random.Random(seed + n * 100000 + idx)
        candidate_order, candidate_obj, _ = local_search(
            order,
            local_rng,
            cache,
            max_rounds=max_rounds,
            samples_per_round=samples_per_round,
        )
        if best_obj is None or candidate_obj.R_full < best_obj.R_full - 1e-9:
            best_order = candidate_order
            best_obj = candidate_obj
            best_restart_count = 1
        elif abs(candidate_obj.R_full - best_obj.R_full) <= 1e-9:
            best_restart_count += 1
        if idx % 20 == 0:
            print(
                f"n={n} restart={idx}/{restarts} best={best_obj.R_full if best_obj else math.inf:.12f} "
                f"cache={len(cache)}",
                flush=True,
            )

    if best_order is None or best_obj is None:
        raise AssertionError(f"no heuristic result for n={n}")
    detailed = full_radius(best_order, R_chain=best_obj.R_chain)
    runtime = time.perf_counter() - start_time
    return result_payload(n, detailed, best_restart_count, runtime, len(cache))


def certified_guard(results: list[dict[str, object]]) -> None:
    certified = {}
    for n in range(3, 14):
        payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
        certified[n] = float(payload["R_float64"])
    for row in results:
        n = int(row["n"])
        if n in certified and float(row["R_full"]) < certified[n] - 1e-8:
            raise AssertionError(
                f"heuristic found R below certified value for n={n}: "
                f"{row['R_full']} < {certified[n]}"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=14)
    parser.add_argument("--stop", type=int, default=18)
    parser.add_argument("--restarts", type=int, default=200)
    parser.add_argument("--seed", type=int, default=4619480)
    parser.add_argument("--max-rounds", type=int, default=28)
    parser.add_argument("--samples-per-round", type=int, default=64)
    args = parser.parse_args()

    out_dir = ROOT / "results" / "heuristic"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for n in range(args.start, args.stop + 1):
        row = run_one(n, args.restarts, args.seed, args.max_rounds, args.samples_per_round)
        rows.append(row)
        (out_dir / f"n{n:02d}.json").write_text(
            json.dumps(row, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(
            f"NON-EXHAUSTIVE n={n} R={row['R_full']:.12f} "
            f"cycle={row['ordering']} floaters={row['floating_circles']} "
            f"best_restarts={row['best_restart_count']} runtime={row['runtime_seconds']:.3f}s",
            flush=True,
        )
    certified_guard(rows)

    csv_path = ROOT / "results" / "heuristic_n14_18.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        fh.write(CSV_METADATA + "\n")
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "schema.json").write_text(
        json.dumps(HEURISTIC_SCHEMA, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
