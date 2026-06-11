from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

CERTIFIED_STOP = 14


def main() -> int:
    heuristic_rows: dict[int, dict[str, str]] = {}
    heuristic_path = ROOT / "results" / "heuristic_n14_18.csv"
    if heuristic_path.exists():
        with heuristic_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(line for line in fh if not line.startswith("#")):
                heuristic_rows[int(row["n"])] = row

    rows: list[dict[str, object]] = []
    for n in range(3, 19):
        if n <= CERTIFIED_STOP:
            payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
            R = float(payload["R_float64"])
            label = "CERTIFIED"
        else:
            row = heuristic_rows[n]
            R = float(row["R_full"])
            label = "NON-EXHAUSTIVE"
        rows.append(
            {
                "n": n,
                "R": f"{R:.12f}",
                "n2_over_8_minus_R": f"{(n * n / 8.0) - R:.12f}",
                "label": label,
            }
        )

    out = ROOT / "results" / "asymptotic_fit.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")
    print(out.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
