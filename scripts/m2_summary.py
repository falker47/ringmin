from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import chain_radius
from ringmin.geometry import cycle_equivalent
from ringmin.patterns import interleave, supnick_min_tour


def main() -> int:
    print("FULL_RESULTS")
    necklace_rows = []
    for n in range(3, 14):
        payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
        order = tuple(payload["ordering"])
        floaters = tuple(payload["floating_circles"])
        realized_chain = tuple(value for value in order if value not in set(floaters))
        nonadj = [
            (pair["radius_i"], pair["radius_j"])
            for pair in payload["essential_tight_pairs"]
            if not pair["adjacent"]
        ]
        interleave_full = cycle_equivalent(order, interleave(range(1, n + 1)))
        chain_interleave = cycle_equivalent(realized_chain, interleave(sorted(realized_chain)))
        worst_order = supnick_min_tour(range(1, n + 1))
        worst_chain = chain_radius(worst_order)
        if n <= 7:
            necklace_rows.append((n, interleave_full))
        print(
            f"n={n} R={float(payload['R_float64']):.12f} "
            f"cycle={list(order)} floaters={list(floaters)} "
            f"essential_nonadj={nonadj} "
            f"interleave_full={interleave_full} chain_interleave={chain_interleave} "
            f"worst_order_chain={worst_chain:.12f} "
            f"certified={payload['certified']} runtime={payload['runtime_seconds']:.3f}s "
            f"stage_b={payload.get('stage_b_candidates')}"
        )
    print("N3_TO_N7_FULL_CYCLE_EQUALS_INTERLEAVE")
    for n, value in necklace_rows:
        print(f"n={n} full_cycle_equals_interleave={value}")

    print("SUBSET_COMPARISON")
    subset_csv = (ROOT / "results" / "subset_comparison.csv").read_text(encoding="utf-8")
    print(subset_csv)

    for n in (11, 12, 13):
        print(f"OPTIMUM_JSON_N{n}")
        print((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
