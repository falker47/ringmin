"""Derive publication tables without changing any certificate or result."""
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
source = ROOT / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
cases = json.loads(source.read_text(encoding="utf-8"))["certificate"]["cases"]
rows = [r"% Exact rational endpoints from the protected certificate; do not edit.",
        r"\begin{tabular}{rrrr}\toprule", r"$n$ & $L_n$ & $U_n$ & Witnesses\\\midrule"]
coverage = [r"% Exact combinatorial counts from the protected certificate; do not edit.",
            r"\begin{tabular}{rrrr}\toprule",
            r"$n$ & Full classes covered & Explicit full classes & Retained skeletons\\\midrule"]
for row in cases:
    n = row["n"]
    if Fraction(row["U"]) - Fraction(row["L"]) != Fraction(1, 10**11):
        raise ValueError("incorrect width")
    fmt = lambda s: s + "0" * (11 - len(s.split(".")[1]))
    rows.append(f"{n} & {fmt(row['L'])} & {fmt(row['U'])} & {len(row['upper_witnesses'])}" + r" \\")
    lower = row["lower_bound"]
    coverage.append(f"{n} & {lower['canonical_orders_covered']:,} & {lower['explicit_full_orders_checked']:,} & "
                    + (f"{lower['canonical_skeletons_expanded']:,}" if n >= 10 else "--") + r" \\")
rows.append(r"\bottomrule\end{tabular}")
coverage.append(r"\bottomrule\end{tabular}")
(OUT / "bracket_rows.tex").write_text("\n".join(rows)+"\n", encoding="utf-8", newline="\n")
(OUT / "coverage_rows.tex").write_text("\n".join(coverage)+"\n", encoding="utf-8", newline="\n")
print("Exported 12 exact endpoint rows and 12 coverage rows; all widths = 1/100000000000.")
