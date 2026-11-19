"""Print certified rational ceilings, reference comparisons and exploratory fits."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import pi
from pathlib import Path
import re


def intercept(xs, ys):
    xbar, ybar = sum(xs)/len(xs), sum(ys)/len(ys)
    slope = sum((x-xbar)*(y-ybar) for x, y in zip(xs,ys))/sum((x-xbar)**2 for x in xs)
    return ybar - slope*xbar


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    base = Path(__file__).resolve().parent
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--certificates", type=Path, default=base/"certificates")
    args = parser.parse_args()
    rows = (args.inputs/"arxiv/p1_v4/bracket_rows.tex").read_text(encoding="utf-8")
    squared = (args.inputs/"ringmin-squared/README.md").read_text(encoding="utf-8")
    refs = {1: {}, 2: {}}
    for n, hi in re.findall(r"(?m)^(\d+) & [0-9.]+ & ([0-9.]+) &", rows):
        refs[1][int(n)] = Q(hi)
    # The published Markdown table uses a TeX escaped space after its comma.
    squared = squared.replace(r"\ ", " ")
    for n, hi in re.findall(r"(?m)^\| (\d+) \| \d+ \| \d+ \| .*?,\s*([0-9.]+)\]", squared):
        refs[2][int(n)] = Q(hi)
    if set(refs[1]) != set(range(3,15)) or set(refs[2]) != set(range(3,7)):
        raise ValueError("reference tables do not have the expected coverage")
    linear = {}
    for file in sorted(args.certificates.glob("p*_n*.json")):
        contents = file.read_bytes()
        d = json.loads(contents)
        n, p = d["n"], d["power"]
        s = Q(d["span_numerator"], d["D"])
        b = Q(*d["B"])
        print(file.name, f"B={float(b):.12f}", f"bytes={len(contents)}",
              f"sha256={hashlib.sha256(contents).hexdigest()}")
        if n in refs[p]:
            # Archimedes' pi < 22/7 makes this comparison rational.
            lower_on_construction = n**p*(s+1)*Q(7,22)
            if lower_on_construction <= refs[p][n]:
                raise ValueError("simple rational comparison inconclusive")
            print("  REFERENCE", refs[p][n], "<", lower_on_construction, "< R_line")
        if p == 1 and n >= 200:
            linear[n] = float(s / n)
    for k in [3, 4, 5]:
        ns = sorted(linear)[-k:]
        for exponent in [0.5, 1]:
            estimate = intercept([n**(-exponent) for n in ns],[linear[n] for n in ns])
            print(f"FIT S/n k={k} power={exponent} E={estimate:.9f} C={estimate/pi:.9f}")


if __name__ == "__main__":
    main()
