from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.artifacts import result_payload
from ringmin.geometry import cycle_equivalent
from ringmin.search import certified_search_values


def pocket_radius(R: float, a: float, b: float) -> float:
    curvature = (
        1.0 / R
        + 1.0 / a
        + 1.0 / b
        + 2.0 * math.sqrt(1.0 / (R * a) + 1.0 / (a * b) + 1.0 / (R * b))
    )
    return 1.0 / curvature


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=7)
    parser.add_argument("--stop", type=int, default=13)
    parser.add_argument("--k", type=int, default=20000)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    out_root = ROOT / "results" / "subsets"
    out_root.mkdir(parents=True, exist_ok=True)
    csv_path = ROOT / "results" / "subset_comparison.csv"
    rows: list[dict[str, object]] = []

    for n in range(args.start, args.stop + 1):
        subset = certified_search_values(
            tuple(range(2, n + 1)),
            k=args.k,
            workers=args.workers,
            checkpoint_dir=ROOT / "results" / "checkpoints",
            resume=args.resume,
            label=f"subset_2_{n}",
            result_n=n,
        )
        subset_dir = out_root / f"n{n:02d}"
        subset_dir.mkdir(parents=True, exist_ok=True)
        subset_payload = result_payload(
            subset.best,
            subset.certified,
            {
                "n": n,
                "values": list(subset.values),
                "runtime_seconds": subset.runtime_seconds,
                "stage_a_seconds": subset.stage_a_seconds,
                "stage_b_seconds": subset.stage_b_seconds,
                "stage_b_candidates": subset.stage_b_candidates,
                "evaluated_full": subset.evaluated_full,
                "enumerated_chain": subset.enumerated_chain,
                "fallback_used": subset.fallback_used,
            },
        )
        (subset_dir / "optimum.json").write_text(
            json.dumps(subset_payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        full_payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
        full_order = tuple(full_payload["ordering"])
        floaters = set(full_payload["floating_circles"])
        realized_chain = tuple(value for value in full_order if value not in floaters)
        subset_order = tuple(subset_payload["ordering"])
        pockets = [
            pocket_radius(subset.best.R_full, a, subset.best.order[(i + 1) % len(subset.best.order)])
            for i, a in enumerate(subset.best.order)
        ]
        row = {
            "n": n,
            "R_subset": f"{subset.best.R_full:.12f}",
            "subset_cycle": list(subset_order),
            "R_full": f"{float(full_payload['R_float64']):.12f}",
            "full_cycle": list(full_order),
            "realized_chain_cycle": list(realized_chain),
            "delta": f"{float(full_payload['R_float64']) - subset.best.R_full:.12f}",
            "cycle_match": cycle_equivalent(realized_chain, subset_order),
            "max_subset_pocket": f"{max(pockets):.12f}",
            "subset_certified": subset.certified,
            "subset_runtime_seconds": f"{subset.runtime_seconds:.3f}",
            "subset_stage_b_candidates": subset.stage_b_candidates,
        }
        rows.append(row)
        print(
            f"n={n} R_subset={row['R_subset']} subset={row['subset_cycle']} "
            f"R_full={row['R_full']} delta={row['delta']} "
            f"match={row['cycle_match']} max_pocket={row['max_subset_pocket']} "
            f"runtime={row['subset_runtime_seconds']}s stage_b={subset.stage_b_candidates}"
        )

    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
