from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from heuristic_sweep import pocket_radius
from ringmin.evaluator import chain_radius, full_radius
from ringmin.patterns import supnick_max_tour


def max_adjacent_pocket(R: float, order: tuple[int, ...]) -> float:
    return max(pocket_radius(R, a, order[(i + 1) % len(order)]) for i, a in enumerate(order))


def main() -> int:
    n = 14
    heuristic = json.loads((ROOT / "results" / "heuristic" / "n14.json").read_text(encoding="utf-8"))
    heuristic_result = full_radius(tuple(heuristic["ordering"]), R_chain=float(heuristic["R_chain"]))

    supnick_2 = tuple(int(x) for x in supnick_max_tour(range(2, n + 1)))
    R_supnick_2 = chain_radius(supnick_2)
    pocket_supnick_2 = max_adjacent_pocket(R_supnick_2, supnick_2)

    supnick_3 = tuple(int(x) for x in supnick_max_tour(range(3, n + 1)))
    R_supnick_3 = chain_radius(supnick_3)
    pocket_supnick_3 = max_adjacent_pocket(R_supnick_3, supnick_3)

    heuristic_full_order_pocket = max_adjacent_pocket(heuristic_result.R_full, tuple(heuristic_result.order))
    heuristic_chain_pocket = max_adjacent_pocket(heuristic_result.R_chain, tuple(heuristic_result.order))

    rows = [
        {
            "name": "current_pocket_supnick_subset",
            "subset": "{2,...,14}",
            "tour": list(supnick_2),
            "R": R_supnick_2,
            "R_definition": "R_chain of Supnick({2,...,14})",
            "max_pocket": pocket_supnick_2,
        },
        {
            "name": "supnick_3_to_14_circle2_free_float",
            "subset": "{3,...,14}",
            "tour": list(supnick_3),
            "R": R_supnick_3,
            "R_definition": "R_chain of Supnick({3,...,14})",
            "max_pocket": pocket_supnick_3,
        },
        {
            "name": "legacy_max_pocket",
            "subset": "{1,...,14}",
            "tour": list(heuristic_result.order),
            "R": heuristic_result.R_full,
            "R_definition": "heuristic R_full",
            "max_pocket": heuristic_full_order_pocket,
        },
        {
            "name": "heuristic_full_order_at_R_chain",
            "subset": "{1,...,14}",
            "tour": list(heuristic_result.order),
            "R": heuristic_result.R_chain,
            "R_definition": "heuristic R_chain",
            "max_pocket": heuristic_chain_pocket,
        },
    ]
    out = ROOT / "results" / "pocket_definition_audit_n14.json"
    out.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    for row in rows:
        print(
            f"{row['name']}: subset={row['subset']} R={row['R']:.12f} "
            f"max_pocket={row['max_pocket']:.12f} R_definition={row['R_definition']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
