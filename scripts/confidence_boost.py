from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from heuristic_sweep import CSV_FIELDNAMES, CSV_METADATA, run_one


def read_main_rows() -> dict[int, dict[str, object]]:
    rows: dict[int, dict[str, object]] = {}
    csv_path = ROOT / "results" / "heuristic_n14_18.csv"
    with csv_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(line for line in fh if not line.startswith("#")):
            rows[int(row["n"])] = row
    return rows


def write_main_rows(rows: dict[int, dict[str, object]]) -> None:
    csv_path = ROOT / "results" / "heuristic_n14_18.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        fh.write(CSV_METADATA + "\n")
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        for n in sorted(rows):
            writer.writerow(rows[n])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=16)
    parser.add_argument("--stop", type=int, default=18)
    parser.add_argument("--restarts", type=int, default=600)
    parser.add_argument("--seed", type=int, default=4619480)
    parser.add_argument("--max-rounds", type=int, default=16)
    parser.add_argument("--samples-per-round", type=int, default=48)
    args = parser.parse_args()

    current = read_main_rows()
    boost_rows: list[dict[str, object]] = []
    improved: list[tuple[int, float, float]] = []
    out_dir = ROOT / "results" / "heuristic"

    for n in range(args.start, args.stop + 1):
        row = run_one(n, args.restarts, args.seed, args.max_rounds, args.samples_per_round)
        boost_rows.append(row)
        old_R = float(current[n]["R_full"])
        new_R = float(row["R_full"])
        if new_R < old_R - 1e-9:
            improved.append((n, old_R, new_R))
            current[n] = row
            (out_dir / f"n{n:02d}.json").write_text(
                json.dumps(row, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            print(f"IMPROVED n={n} old={old_R:.12f} new={new_R:.12f}", flush=True)
        else:
            print(f"no improvement n={n} old={old_R:.12f} new={new_R:.12f}", flush=True)

    if improved:
        write_main_rows(current)

    out = ROOT / "results" / "heuristic_confidence_n16_18.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(boost_rows)
    print(f"wrote {out}")
    if improved:
        print(f"IMPROVEMENTS={improved}")
    else:
        print("IMPROVEMENTS=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
