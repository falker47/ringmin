from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import chain_radius, full_radius
from ringmin.geometry import cycle_equivalent
from ringmin.patterns import interleave, sequential, supnick_min_tour, zigzag


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--stop", type=int, default=18)
    parser.add_argument("--chain-only", action="store_true")
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    heuristic_rows: dict[int, dict[str, str]] = {}
    heuristic_path = ROOT / "results" / "heuristic_n14_18.csv"
    if heuristic_path.exists():
        with heuristic_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(line for line in fh if not line.startswith("#")):
                heuristic_rows[int(row["n"])] = row
    for n in range(args.start, args.stop + 1):
        values = tuple(range(1, n + 1))
        optimum_path = ROOT / "results" / f"n{n:02d}" / "optimum.json"
        if optimum_path.exists():
            optimum = json.loads(optimum_path.read_text(encoding="utf-8"))
            reference_R = float(optimum["R_float64"])
            reference_cycle = optimum["ordering"]
            reference_label = "CERTIFIED"
        else:
            optimum = heuristic_rows[n]
            reference_R = float(optimum["R_full"])
            reference_cycle = json.loads(optimum["ordering"])
            reference_label = "NON-EXHAUSTIVE"
        interleave_order = interleave(values)
        sequential_order = sequential(values)
        zigzag_order = zigzag(values)
        worst_order = supnick_min_tour(values)
        worst_chain = chain_radius(worst_order)
        worst_full = full_radius(worst_order).R_full
        row: dict[str, object] = {
            "n": n,
            "reference_label": reference_label,
            "certified_R": f"{reference_R:.12f}",
            "certified_cycle": reference_cycle,
            "interleave_order": list(interleave_order),
            "certified_cycle_equals_interleave": cycle_equivalent(
                tuple(reference_cycle), interleave_order
            ),
            "worst_order": list(worst_order),
            "worst_order_R_chain": f"{worst_chain:.12f}",
            "worst_order_R_full": f"{worst_full:.12f}",
            "worst_order_full_differs": abs(worst_full - worst_chain) > 1e-9,
        }
        if not args.chain_only:
            row.update(
                {
                    "interleave_R_full": f"{full_radius(interleave_order).R_full:.12f}",
                    "sequential_R_full": f"{full_radius(sequential_order).R_full:.12f}",
                    "zigzag_R_full": f"{full_radius(zigzag_order).R_full:.12f}",
                }
            )
        rows.append(row)

    out = ROOT / "results" / "patterns_table.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")
    for row in rows:
        print(
            f"n={row['n']} full_eq_interleave={row['certified_cycle_equals_interleave']} "
            f"worst_chain={row['worst_order_R_chain']} "
            f"worst_full={row['worst_order_R_full']} "
            f"differs={row['worst_order_full_differs']} worst_order={row['worst_order']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
