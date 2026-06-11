from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.highprec import full_radius_mp, pair_slack_mp, recover_positions_mp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--stop", type=int, default=14)
    parser.add_argument("--digits", type=int, default=50)
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for n in range(args.start, args.stop + 1):
        path = ROOT / "results" / f"n{n:02d}" / "optimum.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        order = tuple(payload["ordering"])
        R_mp = full_radius_mp(order, digits=args.digits)
        positions = recover_positions_mp(order, R_mp, digits=args.digits)

        max_abs_essential_slack = mp.mpf("0")
        for pair in payload["essential_tight_pairs"]:
            forward, wrap = pair_slack_mp(order, R_mp, positions, pair["i"], pair["j"])
            slack = forward if pair["kind"] == "forward" else wrap
            max_abs_essential_slack = max(max_abs_essential_slack, abs(slack))

        R_30 = mp.nstr(R_mp, 30)
        payload["R_mpmath_30"] = R_30
        payload["R_mpmath_full"] = mp.nstr(R_mp, args.digits)
        payload["mpmath_digits"] = args.digits
        payload["mpmath_max_abs_essential_slack"] = mp.nstr(max_abs_essential_slack, 20)
        payload["mpmath_binding_structure_verified"] = bool(max_abs_essential_slack < mp.mpf("1e-25"))
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        rows.append(
            {
                "n": n,
                "R_mpmath_30": R_30,
                "R_float64": payload["R_float64"],
                "max_abs_essential_slack": mp.nstr(max_abs_essential_slack, 20),
                "binding_verified": payload["mpmath_binding_structure_verified"],
            }
        )
        print(
            f"n={n} R_mpmath_30={R_30} "
            f"max_abs_essential_slack={mp.nstr(max_abs_essential_slack, 8)} "
            f"verified={payload['mpmath_binding_structure_verified']}"
        )

    out = ROOT / "results" / "highprec.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
