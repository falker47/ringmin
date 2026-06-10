from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from heuristic_sweep import pocket_radius
from ringmin.evaluator import chain_radius
from ringmin.geometry import theta
from ringmin.patterns import supnick_max_tour

TOL = 1e-12


def pockets_for_order(R: float, order: tuple[int, ...]) -> list[dict[str, object]]:
    pockets: list[dict[str, object]] = []
    for i, a in enumerate(order):
        b = order[(i + 1) % len(order)]
        pockets.append(
            {
                "gap_index": i,
                "pair": [int(a), int(b)],
                "pocket_radius": pocket_radius(R, float(a), float(b)),
            }
        )
    pockets.sort(key=lambda row: float(row["pocket_radius"]), reverse=True)
    return pockets


def joint_fit_pairs(R: float, order: tuple[int, ...], first: int, second: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for i, a in enumerate(order):
        b = order[(i + 1) % len(order)]
        required = theta(R, float(a), float(first))
        required += theta(R, float(first), float(second))
        required += theta(R, float(second), float(b))
        available = theta(R, float(a), float(b))
        slack = available - required
        if slack >= -TOL:
            rows.append(
                {
                    "gap_index": i,
                    "pair": [int(a), int(b)],
                    "insert_order": [first, second],
                    "slack": slack,
                }
            )
    return rows


def row_for_n(n: int) -> dict[str, object]:
    order = tuple(int(x) for x in supnick_max_tour(range(3, n + 1)))
    R = chain_radius(order)
    pockets = pockets_for_order(R, order)
    circle2_gaps = [row for row in pockets if float(row["pocket_radius"]) >= 2.0 - TOL]
    circle1_gaps = [row for row in pockets if float(row["pocket_radius"]) >= 1.0 - TOL]
    circle1_separate = any(
        int(gap2["gap_index"]) != int(gap1["gap_index"])
        for gap2 in circle2_gaps
        for gap1 in circle1_gaps
    )
    joint_2_then_1 = joint_fit_pairs(R, order, 2, 1)
    joint_1_then_2 = joint_fit_pairs(R, order, 1, 2)
    circle2_hosted = bool(circle2_gaps or joint_2_then_1 or joint_1_then_2)
    circle1_hosted_separately_or_jointly = bool(
        circle1_separate or joint_2_then_1 or joint_1_then_2
    )
    return {
        "n": n,
        "tour": list(order),
        "R_chain_supnick_3_to_n": f"{R:.12f}",
        "top2_pockets": json.dumps(pockets[:2], sort_keys=True),
        "circle2_hosted": circle2_hosted,
        "circle1_hosted_separately_or_jointly": circle1_hosted_separately_or_jointly,
        "circle1_hosted_separately": circle1_separate,
        "joint_2_then_1_pairs": json.dumps(joint_2_then_1, sort_keys=True),
        "joint_1_then_2_pairs": json.dumps(joint_1_then_2, sort_keys=True),
    }


def main() -> int:
    rows = [row_for_n(n) for n in range(14, 21)]
    out = ROOT / "results" / "free_float_criterion_n14_20.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")
    for row in rows:
        print(
            "n={n} R={R_chain_supnick_3_to_n} top2={top2_pockets} "
            "circle2_hosted={circle2_hosted} "
            "circle1_hosted_separately_or_jointly={circle1_hosted_separately_or_jointly}".format(
                **row
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
