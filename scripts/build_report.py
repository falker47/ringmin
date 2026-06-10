from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

CERT_STATEMENT = (
    "global optimality certified up to absolute tolerance 1e-10 in R; "
    "bisection rel. tol 1e-12/1e-13; values of the found binding structure "
    "verified to 50 digits via mpmath."
)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    lines = ["| " + " | ".join(columns) + " |"]
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return "\n".join(lines)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#")))


def update_certificates() -> None:
    for n in range(3, 14):
        path = ROOT / "results" / f"n{n:02d}" / "certificate.txt"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        lines = [line for line in text.splitlines() if not line.startswith("certificate_semantics=")]
        lines.append(f"certificate_semantics={CERT_STATEMENT}")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    update_certificates()

    summary_rows: list[dict[str, object]] = []
    for n in range(3, 14):
        payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
        summary_rows.append(
            {
                "n": n,
                "R*": payload.get("R_mpmath_30", f"{payload['R_float64']:.12f}"),
                "cycle": payload["ordering"],
                "floaters": payload["floating_circles"],
                "certified": payload["certified"],
            }
        )

    regimes = read_csv(ROOT / "results" / "regimes.csv")
    patterns = read_csv(ROOT / "results" / "patterns_table.csv")
    highprec = read_csv(ROOT / "results" / "highprec.csv")
    validity = json.loads((ROOT / "results" / "supnick_validity.json").read_text(encoding="utf-8"))
    validity_rows = [
        {
            "kind": row["kind"],
            "n": row["n"],
            "R_chain": row["R_chain"],
            "valid": row["valid_at_chain_R"],
            "violated_pairs": row["violated_pairs"],
        }
        for row in validity
    ]

    report = [
        "# ringmin Report",
        "",
        f"Certificate semantics: {CERT_STATEMENT}",
        "",
        "## Certified Optima",
        markdown_table(summary_rows, ["n", "R*", "cycle", "floaters", "certified"]),
        "",
        "## Regimes",
        markdown_table(
            regimes,
            [
                "n",
                "floaters",
                "delta",
                "chain==subset_opt",
                "chain==interleave",
                "max_pocket_subset_interleave",
                "supnick_subset_valid",
            ],
        ),
        "",
        "## Supnick Validity",
        markdown_table(validity_rows, ["kind", "n", "R_chain", "valid", "violated_pairs"]),
        "",
        "## High Precision",
        markdown_table(highprec, ["n", "R_mpmath_30", "max_abs_essential_slack", "binding_verified"]),
        "",
        "## Patterns",
        markdown_table(
            patterns,
            [
                "n",
                "certified_R",
                "interleave_R_full",
                "sequential_R_full",
                "zigzag_R_full",
                "worst_order_R_chain",
                "worst_order_R_full",
                "worst_order_full_differs",
            ],
        ),
        "",
    ]
    (ROOT / "REPORT.md").write_text("\n".join(report), encoding="utf-8")
    print(f"wrote {ROOT / 'REPORT.md'}")
    print("updated certificates n03..n13")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
