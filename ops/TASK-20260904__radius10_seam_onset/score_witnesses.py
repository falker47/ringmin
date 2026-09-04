#!/usr/bin/env python3
"""Independent integer scorer: read checker literals; never import/execute it."""

import ast
from collections import Counter
from math import isqrt
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
NOTE = HERE.parents[1] / "research" / "RADIUS10_SEAM_ONSET.md"


class ScoreFailure(ValueError):
    """A witness or proof-note transcription failed independent scoring."""


def need(condition, message):
    if not condition:
        raise ScoreFailure(message)


def read_literals(source):
    names = {"UPPER_ROWS": 45, "LOWER_ROWS": 46}
    result = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in names:
                n = names[target.id]
                need(n not in result, "duplicate witness assignment")
                result[n] = ast.literal_eval(node.value)
    need(set(result) == {45, 46}, "both witness literals required")
    return result


def score(note, recorded):
    """Independent oracle: only integers, text, and literal tables as input."""
    need(set(recorded) == {45, 46}, "only endpoints 45,46")
    all_edges = 0
    aggregate = []
    for n in (45, 46):
        title = f"### Complete table for n={n}\n"
        need(note.count(title) == 1, "one complete table per endpoint")
        block = note.split(title)[1].lstrip("\n").split("\n\n", 1)[0]
        rows = [tuple(map(int, values)) for values in re.findall(
            r"^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
            block, re.MULTILINE)]
        need(len(rows) == n-9, "complete table row count")
        need(tuple(row[:3] for row in rows) == recorded[n], "note/literal agreement")

        # Specialize the mathematical edge families independently of checker code.
        central = [(27, 28)] if n == 45 else []
        expected = [(10, n)] + central
        for radius in range(10, 27 if n == 45 else 28):
            expected.append((radius, n+9-radius))
        for radius in range(11, 28 if n == 45 else 29):
            expected.append((radius, n+11-radius))
        edges = [(a, b) for a, b, _, _, _ in rows]
        need(Counter(edges) == Counter(expected), "complete parity multiset")
        need(len(set(edges)) == len(edges), "edge multiplicity one")

        matches = re.findall(re.escape(f"sigma*_{{10,{n}}} =")+r"\s*\(([^)]+)\)", note)
        need(len(matches) == 1, "one complete tour per endpoint")
        tour = tuple(map(int, matches[0].replace("\n", "").split(",")))
        need(sorted(tour) == list(range(10, n+1)), "tour permutation")
        cycle = [tuple(sorted(pair)) for pair in zip(tour, tour[1:]+tour[:1])]
        need(Counter(cycle) == Counter(expected), "cyclic closure/coverage")
        need(Counter(v for e in edges for v in e) ==
             Counter({v: 2 for v in range(10, n+1)}), "degree two")

        numerator = 0
        for a, b, m, q, margin in rows:
            # Expanded denominator and integer cross-products, no Fraction scorer.
            need(q == 72900+270*(a+b)+a*b, "denominator reconstruction")
            target = 100000000*a*b
            expected_m = (isqrt(target//q)+1 if n == 45
                          else isqrt((target-1)//q))
            need(m == expected_m, "isqrt witness reconstruction")
            need(m > 0 and q > a*b > 0, "positive sine domain")
            raw = m*m*q-target
            need(margin == (raw if n == 45 else -raw), "square margin transcription")
            need(margin > 0, "strict directed square margin")
            if n == 45:
                need(m <= 2000, "upper analytic domain")
                numerator += 500000000*m+m**3
            else:
                numerator += m
        if n == 45:
            need(numerator == 15404369802693, "upper aggregate transcription")
            need(157*5000000000000-50*numerator > 0, "upper sum versus 157/50")
        else:
            need(numerator == 32044, "lower aggregate transcription")
            need(7*numerator-220000 == 4308 > 0, "lower sum versus 22/7")
        aggregate.append(numerator)
        all_edges += len(rows)

        # Threshold numerators over L and 270L; compare with the note table.
        length = 10*n*(n-1)
        an = n*(n-1)+10*(2*n-1)
        bn = 4*(2*n+9)
        hn = 270*an-length
        positive = an*an-bn*length
        raw = bn*270**2*length-hn*hn
        directed = raw if n == 45 else -raw
        need(min(an, bn, hn, positive, directed) > 0, "threshold sign gates")
        line = next((line for line in note.splitlines()
                     if line.startswith(f"| {n} | `")), "")
        fractions = re.findall(r"(\d+)/(\d+)", line)
        need(len(fractions) == 5, "threshold table fields")
        nums = (an, bn, positive, hn, directed)
        dens = (length, length, length**2, 270*length, (270*length)**2)
        for (p, q), num, den in zip(fractions, nums, dens):
            need(int(p)*den == int(q)*num, "threshold fraction transcription")
    return all_edges, tuple(aggregate)


if __name__ == "__main__":
    tables = read_literals((HERE / "check_seam.py").read_text(encoding="utf-8"))
    count, sums = score(NOTE.read_text(encoding="utf-8"), tables)
    print(f"independent_integer_scorer=PASS endpoints=2 witnesses={count}")
    print(f"upper_numerator={sums[0]} denominator=5000000000000")
    print(f"lower_numerator={sums[1]} denominator=10000")
    print("note_tables=PASS note_tours=PASS threshold_cross_products=PASS")
