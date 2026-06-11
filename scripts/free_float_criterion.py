from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from heuristic_sweep import pocket_radius
from ringmin.evaluator import chain_radius, full_radius, is_feasible
from ringmin.geometry import TAU, theta
from ringmin.patterns import supnick_max_tour

TOL = 1e-12
VIOLATION_TOL = 1e-10


def read_heuristic_best() -> dict[int, float]:
    path = ROOT / "results" / "heuristic_n14_18.csv"
    best: dict[int, float] = {}
    if not path.exists():
        return best
    with path.open(newline="", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            if line.startswith("n,"):
                import csv

                reader = csv.DictReader([line, *fh])
                for row in reader:
                    best[int(row["n"])] = float(row["R_full"])
                break
    return best


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


def adjacent_chain_positions(R: float, order: tuple[int, ...]) -> tuple[float, ...]:
    positions = [0.0]
    total = 0.0
    for i in range(len(order) - 1):
        total += theta(R, float(order[i]), float(order[i + 1]))
        positions.append(total)
    closing = theta(R, float(order[-1]), float(order[0]))
    if abs((total + closing) - TAU) > 1e-8:
        raise AssertionError(
            f"chain positions do not close: order={order!r}, R={R!r}, sum={total + closing!r}"
        )
    return tuple(positions)


def is_adjacent_pair(i: int, j: int, n: int) -> bool:
    return j == i + 1 or (i == 0 and j == n - 1)


def violated_nonadjacent_pairs(R: float, order: tuple[int, ...]) -> list[dict[str, object]]:
    positions = adjacent_chain_positions(R, order)
    rows: list[dict[str, object]] = []
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if is_adjacent_pair(i, j, len(order)):
                continue
            sep = theta(R, float(order[i]), float(order[j]))
            delta = positions[j] - positions[i]
            forward_slack = delta - sep
            wrap_slack = (TAU - sep) - delta
            if forward_slack < -VIOLATION_TOL:
                rows.append(
                    {
                        "i": i,
                        "j": j,
                        "pair": [int(order[i]), int(order[j])],
                        "kind": "forward",
                        "slack": forward_slack,
                    }
                )
            if wrap_slack < -VIOLATION_TOL:
                rows.append(
                    {
                        "i": i,
                        "j": j,
                        "pair": [int(order[i]), int(order[j])],
                        "kind": "wrap",
                        "slack": wrap_slack,
                    }
                )
    rows.sort(key=lambda row: float(row["slack"]))
    return rows


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


def insert_after_gaps(
    order: tuple[int, ...],
    insertions: dict[int, tuple[int, ...]],
) -> tuple[int, ...]:
    result: list[int] = []
    for i, value in enumerate(order):
        result.append(value)
        result.extend(insertions.get(i, ()))
    return tuple(result)


def best_complete_configuration(
    R_chain_base: float,
    order: tuple[int, ...],
    circle2_gaps: list[dict[str, object]],
    circle1_gaps: list[dict[str, object]],
    joint_2_then_1: list[dict[str, object]],
    joint_1_then_2: list[dict[str, object]],
) -> dict[str, object]:
    candidates: set[tuple[int, ...]] = set()
    for gap2 in circle2_gaps:
        for gap1 in circle1_gaps:
            gap2_index = int(gap2["gap_index"])
            gap1_index = int(gap1["gap_index"])
            if gap2_index == gap1_index:
                continue
            candidates.add(insert_after_gaps(order, {gap2_index: (2,), gap1_index: (1,)}))
    for row in joint_2_then_1:
        candidates.add(insert_after_gaps(order, {int(row["gap_index"]): (2, 1)}))
    for row in joint_1_then_2:
        candidates.add(insert_after_gaps(order, {int(row["gap_index"]): (1, 2)}))
    if not candidates:
        return {
            "best_complete_R_full": "",
            "best_complete_order": "",
            "best_complete_R_chain": "",
        }

    best = None
    for candidate in sorted(candidates):
        result = full_radius(candidate)
        if best is None or result.R_full < best.R_full:
            best = result
    if best is None:
        raise AssertionError("complete-configuration candidate generation failed")
    return {
        "best_complete_R_full": f"{best.R_full:.12f}",
        "best_complete_order": list(int(x) for x in best.order),
        "best_complete_R_chain": f"{best.R_chain:.12f}",
    }


def row_for_n(n: int) -> dict[str, object]:
    order = tuple(int(x) for x in supnick_max_tour(range(3, n + 1)))
    R = chain_radius(order)
    chain_valid = is_feasible(order, R)
    violations = violated_nonadjacent_pairs(R, order)
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
    raw_circle2_hosted = bool(circle2_gaps or joint_2_then_1 or joint_1_then_2)
    raw_circle1_hosted_separately_or_jointly = bool(
        circle1_separate or joint_2_then_1 or joint_1_then_2
    )
    circle2_hosted = chain_valid and raw_circle2_hosted
    circle1_hosted_separately_or_jointly = (
        chain_valid and raw_circle1_hosted_separately_or_jointly
    )
    complete = (
        best_complete_configuration(
            R,
            order,
            circle2_gaps,
            circle1_gaps,
            joint_2_then_1,
            joint_1_then_2,
        )
        if chain_valid and raw_circle2_hosted and raw_circle1_hosted_separately_or_jointly
        else {
            "best_complete_R_full": "",
            "best_complete_order": "",
            "best_complete_R_chain": "",
        }
    )
    return {
        "n": n,
        "tour": list(order),
        "R_chain_supnick_3_to_n": f"{R:.12f}",
        "chain_valid": chain_valid,
        "violated_nonadjacent_pairs": json.dumps(violations, sort_keys=True),
        "top2_pockets": json.dumps(pockets[:2], sort_keys=True),
        "circle2_hosted": circle2_hosted,
        "circle1_hosted_separately_or_jointly": circle1_hosted_separately_or_jointly,
        "raw_circle2_pocket_hosted": raw_circle2_hosted,
        "raw_circle1_hosted_separately_or_jointly": raw_circle1_hosted_separately_or_jointly,
        "circle1_hosted_separately": circle1_separate,
        "joint_2_then_1_pairs": json.dumps(joint_2_then_1, sort_keys=True),
        "joint_1_then_2_pairs": json.dumps(joint_1_then_2, sort_keys=True),
        **complete,
    }


def main() -> int:
    rows = [row_for_n(n) for n in range(14, 21)]
    heuristic_best = read_heuristic_best()
    improved: list[tuple[int, str, float]] = []
    for row in rows:
        n = int(row["n"])
        best_complete = row.get("best_complete_R_full")
        if n in (17, 18) and best_complete:
            full_value = float(best_complete)
            if full_value < heuristic_best.get(n, float("inf")) - 1e-9:
                improved.append((n, str(row["best_complete_order"]), full_value))
    out = ROOT / "results" / "free_float_criterion_n14_20.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")
    for row in rows:
        print(
            "n={n} R={R_chain_supnick_3_to_n} chain_valid={chain_valid} "
            "violations={violated_nonadjacent_pairs} top2={top2_pockets} "
            "circle2_hosted={circle2_hosted} "
            "circle1_hosted_separately_or_jointly={circle1_hosted_separately_or_jointly} "
            "best_complete_R={best_complete_R_full}".format(
                **row
            )
        )
    if improved:
        print(f"BLOCKED: complete Supnick{{3..n}} insertions beat heuristic: {improved}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
