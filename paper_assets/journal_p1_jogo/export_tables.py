"""Rebuild the eight table bodies used in the JOGO manuscript."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DRAFT = ROOT / "paper_assets/journal_p1_v5"
ARCHIVE = ROOT / "paper_assets/general_radii/certificates"
ORIGINAL = ROOT / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
TABLE = re.compile(r"\\begin\{table\}.*?\\end\{table\}", re.S)
TABULAR = re.compile(r"\\begin\{tabularx?\}.*?\\end\{tabularx?\}", re.S)


def decimal_endpoint(value):
    scaled = Fraction(value) * 10**11
    if scaled.denominator != 1:
        raise ValueError("Published endpoint falls outside the eleven-place decimal grid")
    units, remainder = divmod(scaled.numerator, 10**11)
    return f"{units}.{remainder:011d}"


def certificate_rows():
    rows = {"brackets": [], "coverage": [], "quadratic": []}
    cases = json.loads(ORIGINAL.read_bytes())["certificate"]["cases"]
    for case in cases:
        n = case["n"]
        rows["brackets"].append((n, decimal_endpoint(case["L"]), decimal_endpoint(case["U"]),
                                 len(case["upper_witnesses"])))
        counts = case["lower_bound"]
        rows["coverage"].append((n, f"{counts['canonical_orders_covered']:,}",
                                 f"{counts['explicit_full_orders_checked']:,}",
                                 f"{counts['canonical_skeletons_expanded']:,}" if n >= 10 else "--"))
        quadratic = json.loads((ARCHIVE / f"quadratic_{n:02}.json").read_bytes())
        if len(quadratic["stereographic"]) != n or quadratic["radii"] != [j*j for j in range(1, n+1)]:
            raise ValueError(f"Invalid quadratic witness for n={n}")
        rows["quadratic"].append((n, decimal_endpoint(quadratic["lower"]),
                                  decimal_endpoint(quadratic["upper"]), 1))
    return rows


def export(output):
    output.mkdir(parents=True, exist_ok=True)
    source = (DRAFT / "main.tex").read_text(encoding="utf-8")
    source = re.sub(r"\\input\{([\w.-]+\.tex)\}",
                    lambda m: (DRAFT / m[1]).read_text(encoding="utf-8"), source)
    numeric = certificate_rows()
    for table in TABLE.findall(source):
        name = re.search(r"\\label\{tab:(\w+)\}", table)[1]
        body = TABULAR.search(table)[0]
        if name in numeric:
            heading, data = body.split(r"\midrule", 1)
            _, ending = data.split(r"\bottomrule", 1)
            lines = [" & ".join(map(str, row)) + r" \\" for row in numeric[name]]
            body = "\n".join([heading + r"\midrule", *lines, r"\bottomrule" + ending])
        (output / f"{name}.tex").write_text(body + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    export(parser.parse_args().output_dir)
