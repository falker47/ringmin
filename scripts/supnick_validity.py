from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import chain_radius, is_feasible
from ringmin.geometry import TAU, cycle_equivalent, theta
from ringmin.patterns import interleave


def pocket_radius(R: float, a: float, b: float) -> float:
    import math

    curvature = (
        1.0 / R
        + 1.0 / a
        + 1.0 / b
        + 2.0 * math.sqrt(1.0 / (R * a) + 1.0 / (a * b) + 1.0 / (R * b))
    )
    return 1.0 / curvature


def max_pocket_for_chain(order: tuple[int, ...]) -> float:
    R = chain_radius(order)
    return max(pocket_radius(R, a, order[(i + 1) % len(order)]) for i, a in enumerate(order))


def violated_pairs_at_chain(order: tuple[int, ...], tol: float = 1e-10) -> list[dict[str, object]]:
    R = chain_radius(order)
    if is_feasible(order, R, tol=tol):
        return []
    rows: list[dict[str, object]] = []
    positions = [0.0]
    for i, radius in enumerate(order):
        if i == len(order) - 1:
            break
        positions.append(positions[-1] + theta(R, radius, order[i + 1]))
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            sep = theta(R, order[i], order[j])
            delta = positions[j] - positions[i]
            forward_slack = delta - sep
            wrap_slack = (TAU - sep) - delta
            adjacent = (j == i + 1) or (i == 0 and j == len(order) - 1)
            if not adjacent and (forward_slack < -tol or wrap_slack < -tol):
                rows.append(
                    {
                        "i": i,
                        "j": j,
                        "radius_i": order[i],
                        "radius_j": order[j],
                        "forward_slack": forward_slack,
                        "wrap_slack": wrap_slack,
                    }
                )
    return rows


def main() -> int:
    validity_rows: list[dict[str, object]] = []
    for kind, start, stop in (("subset", 8, 14), ("full", 3, 14)):
        for n in range(start, stop + 1):
            values = tuple(range(2, n + 1)) if kind == "subset" else tuple(range(1, n + 1))
            order = tuple(int(x) for x in interleave(values))
            R = chain_radius(order)
            violations = violated_pairs_at_chain(order)
            row = {
                "kind": kind,
                "n": n,
                "order": list(order),
                "R_chain": f"{R:.12f}",
                "valid_at_chain_R": len(violations) == 0,
                "violated_pairs": [
                    [item["radius_i"], item["radius_j"]] for item in violations
                ],
                "violation_details": violations,
            }
            validity_rows.append(row)
            print(
                f"{kind} n={n} R_chain={R:.12f} valid={row['valid_at_chain_R']} "
                f"violated={row['violated_pairs']}"
            )

    validity_path = ROOT / "results" / "supnick_validity.json"
    validity_path.write_text(json.dumps(validity_rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    subset_valid = {
        row["n"]: row["valid_at_chain_R"]
        for row in validity_rows
        if row["kind"] == "subset"
    }
    subset_rows = {}
    with (ROOT / "results" / "subset_comparison.csv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            subset_rows[int(row["n"])] = row

    regimes: list[dict[str, object]] = []
    for n in range(3, 15):
        optimum = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
        order = tuple(optimum["ordering"])
        floaters = tuple(optimum["floating_circles"])
        chain = tuple(value for value in order if value not in set(floaters))
        subset_row = subset_rows.get(n)
        if subset_row is None:
            delta = ""
            chain_subset = ""
            if n >= 4:
                max_pocket = f"{max_pocket_for_chain(tuple(int(x) for x in interleave(range(2, n + 1)))):.12f}"
            else:
                max_pocket = ""
            subset_valid_value = ""
        else:
            delta = subset_row["delta"]
            chain_subset = subset_row["cycle_match"]
            max_pocket = f"{max_pocket_for_chain(tuple(int(x) for x in interleave(range(2, n + 1)))):.12f}"
            subset_valid_value = subset_valid.get(n, "")
        regimes.append(
            {
                "n": n,
                "floaters": list(floaters),
                "delta": delta,
                "chain==subset_opt": chain_subset,
                "chain==interleave": cycle_equivalent(chain, interleave(sorted(chain))),
                "max_pocket_subset_interleave": max_pocket,
                "supnick_subset_valid": subset_valid_value,
            }
        )

    regimes_path = ROOT / "results" / "regimes.csv"
    with regimes_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(regimes[0]))
        writer.writeheader()
        writer.writerows(regimes)
    print(f"wrote {validity_path}")
    print(f"wrote {regimes_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
