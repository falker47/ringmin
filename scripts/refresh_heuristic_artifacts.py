from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from heuristic_sweep import (
    CSV_FIELDNAMES,
    CSV_METADATA,
    HEURISTIC_SCHEMA,
    pocket_supnick_subset,
    realized_hosting_pockets,
)
from ringmin.evaluator import full_radius


def payload_from_existing(payload: dict[str, object]) -> dict[str, object]:
    n = int(payload["n"])
    certified_path = ROOT / "results" / f"n{n:02d}" / "optimum.json"
    certified_payload: dict[str, object] | None = None
    if certified_path.exists():
        candidate = json.loads(certified_path.read_text(encoding="utf-8"))
        if candidate.get("certified") is True:
            certified_payload = candidate

    source = certified_payload if certified_payload is not None else payload
    order = tuple(int(x) for x in source["ordering"])
    R_chain = float(source["R_chain_float64"] if certified_payload is not None else source["R_chain"])
    result = full_radius(order, R_chain=R_chain)
    refreshed = {
        "schema": HEURISTIC_SCHEMA,
        "n": n,
        "label": "CERTIFIED" if certified_payload is not None else "NON-EXHAUSTIVE",
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
        "best_restart_count": "" if certified_payload is not None else int(payload["best_restart_count"]),
        "runtime_seconds": (
            float(certified_payload["runtime_seconds"])
            if certified_payload is not None
            else float(payload["runtime_seconds"])
        ),
        "cache_size": "" if certified_payload is not None else int(payload["cache_size"]),
    }
    return refreshed


def main() -> int:
    out_dir = ROOT / "results" / "heuristic"
    rows: list[dict[str, object]] = []
    for path in sorted(out_dir.glob("n*.json")):
        old = json.loads(path.read_text(encoding="utf-8"))
        refreshed = payload_from_existing(old)
        path.write_text(json.dumps(refreshed, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        rows.append(refreshed)
        print(
            f"n={refreshed['n']} R={refreshed['R_full']:.12f} "
            f"floaters={refreshed['floating_circles']} "
            f"hosting={refreshed['realized_hosting_pockets']}"
        )

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
