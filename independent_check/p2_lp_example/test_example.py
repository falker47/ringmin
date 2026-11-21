"""Replay the printed square-law numbers with rational arithmetic and explicit paths."""
from copy import deepcopy
from fractions import Fraction
from itertools import combinations, pairwise, product
import json
from math import lcm
from pathlib import Path
import re
import unittest

import check_example


HERE = Path(__file__).resolve().parent
SIDMA = HERE.parents[1] / "paper_assets/journal_p2_sidma"
SOLVED = {(4, 4), (6, 4), (6, 6)}
PROJECTED = {(16, 16), (64, 64)}


def path_edges(r):
    """Every increasing path between the endpoints, including the direct edge."""
    interior = range(1, r - 1)
    return [tuple(pairwise((0, *middle, r - 1))) for size in range(r - 1)
            for middle in combinations(interior, size)]


def path_span(word, paths):
    return max(sum(word[i] * word[j] for i, j in edges) for edges in paths)


def over_pi(value):
    return rf"\frac{{{value.numerator}}}{{{value.denominator}\pi}}"


class WorkedExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((HERE / "certificates.json").read_text(encoding="utf-8"))
        cls.records = {(rec["k"], rec["r"]): rec for rec in data["certificates"]}
        cls.section = (SIDMA / "sections/worked_lp_example.tex").read_text(encoding="utf-8")

    def optimum_from_paths(self, record):
        k, r = record["k"], record["r"]
        labels = range(1, k + 1)
        paths = path_edges(r)
        weights = [(a["word"], Fraction(a["weight"])) for a in record["primal"]]
        self.assertTrue(all(p >= 0 for _, p in weights))
        self.assertEqual(sum(p for _, p in weights), 1)
        for j in labels:
            self.assertEqual(sum(w.count(j) * p for w, p in weights), Fraction(r, k))
        primal = sum(p * path_span(w, paths) for w, p in weights) / (r * k**2)
        y0 = Fraction(record["dual"]["y0"])
        y = list(map(Fraction, record["dual"]["y"]))
        self.assertEqual(len(y), k)
        self.assertEqual(primal, y0 + Fraction(r, k) * sum(y))
        # Dual prices only depend on counts. Visit every word and test the
        # tightest inequality in each count class using its minimum span.
        least = {}
        for word in product(labels, repeat=r):
            counts = tuple(word.count(j) for j in labels)
            span = path_span(word, paths)
            if counts not in least or span < least[counts]:
                least[counts] = span
        for counts, span in least.items():
            self.assertLessEqual(y0 + sum(c * price for c, price in zip(counts, y)),
                                 Fraction(span, r * k**2), counts)
        self.assertEqual(primal, check_example.verify_certificate(record))
        return primal

    def test_scaling_table(self):
        self.assertEqual(self.records.keys(), SOLVED)
        results = {case: self.optimum_from_paths(rec) for case, rec in self.records.items()}
        body = self.section.split(r"\midrule")[1].split(r"\bottomrule")[0]
        seen = []
        for row in body.split(r"\\"):
            if not row.strip():
                continue
            cells = [cell.strip().strip("$") for cell in row.split("&")]
            k, r = map(int, cells[:2])
            words, value, interval, width = cells[2:]
            seen.append((k, r))
            self.assertEqual(Fraction(width), Fraction(1, k) + Fraction(1, r))
            if (k, r) in results:
                self.assertEqual(int(words), k**r)
                optimum = results[k, r]
                self.assertEqual(Fraction(value), optimum)
                lo, hi = optimum - Fraction(1, k), optimum + Fraction(1, r)
                self.assertEqual(interval, f"[{lo},{hi}]")
            else:
                self.assertIn((k, r), PROJECTED)
                self.assertEqual(words, f"{k}^{{{r}}}")
                self.assertEqual((value, interval), ("---", "---"))
        self.assertCountEqual(seen, SOLVED | PROJECTED)

    def test_quantiles_and_edge_units(self):
        profile_power = int(re.search(r"f\(x\)=x\^(\d+)", self.section)[1])
        quantile_power = int(re.search(r"Q_\\mu\(t\)=t\^(\d+)", self.section)[1])
        mark_bound = int(re.search(r"\$M=(\d+)\$", self.section)[1])
        edge_power = int(re.search(r"\$ij/k\^(\d+)\$", self.section)[1])
        self.assertGreater(profile_power, 0)
        self.assertEqual(quantile_power, profile_power)  # increasing transform of U
        self.assertEqual(mark_bound, 1**quantile_power)
        for k in {k for k, _ in SOLVED}:
            for i, j in product(range(1, k + 1), repeat=2):
                qi = Fraction(i, k)**quantile_power
                qj = Fraction(j, k)**quantile_power
                edge = Fraction(i * j, k**edge_power)
                self.assertEqual(edge**2, qi * qj)
                self.assertEqual(edge * k**2, i * j)

    def test_displayed_certificate(self):
        k, r = 6, 6
        record = self.records[k, r]
        paths = path_edges(r)
        atoms = [(a["word"], path_span(a["word"], paths), Fraction(a["weight"]))
                 for a in record["primal"]]
        compact = re.sub(r"\s+", "", self.section)
        self.assertIn("$k=r=" + str(k) + "$", compact)
        shown = re.findall(r"\((\d+),(\d+),(\d+/\d+)\)", compact)
        self.assertEqual(shown, [("".join(map(str, word)), str(span), str(p))
                                 for word, span, p in atoms])
        self.assertIn(rf"(w,{k*k}\ell(w),p_w)", compact)
        batch = lcm(*(p.denominator for _, _, p in atoms))
        copies = [int(batch * p) for _, _, p in atoms]
        self.assertEqual(copies, [1, 3, 2])
        self.assertRegex(self.section, r"one,\s+three and two copies")

        y = list(map(Fraction, record["dual"]["y"]))
        scale = lcm(*(price.denominator for price in y))
        prices = ",".join(str(price * scale) for price in y)
        self.assertIn(rf"y_0={record['dual']['y0']},\qquad{scale}(y_1,\ldots,y_{k})=({prices})", compact)
        self.assertIn(rf"\sum_j({scale}y_j)c_j(w)\le{Fraction(scale, r*k*k)}({k*k}\ell(w))", compact)
        self.assertIn("$" + f"{k}^{r}" + "$", compact)
        self.assertIn(rf"\ell(w)/{r}", compact)
        optimum = sum(span * p for _, span, p in atoms) / (r * k**2)
        self.assertIn("$" + str(optimum) + "$", compact)
        lo, hi = optimum - Fraction(1, k), optimum + Fraction(1, r)
        self.assertIn(rf"{over_pi(lo)}\leC_2\le{over_pi(hi)}", compact)
        self.assertLess(lo, Fraction(1, 6))  # Corollary on power radii
        numbers = (SIDMA / "numbers.tex").read_text(encoding="utf-8")
        upper = Fraction(re.search(r"\\CtwoUpper\}\{([\d.]+)\}", numbers)[1])
        self.assertLess(upper * Fraction(22, 7), hi)  # pi < 22/7

    def test_path_and_storage_examples(self):
        word, path, numerator, denominator = re.search(
            r"in\s+\$(\d+)\$.*?indices\s+\$([\d,]+)\$.*?\$(\d+)/(\d+)\$",
            self.section, re.DOTALL).groups()
        vertices = tuple(map(int, path.split(",")))
        self.assertIn(vertices, combinations(map(int, word), len(vertices)))
        self.assertEqual(int(numerator), sum(a * b for a, b in pairwise(vertices)))
        self.assertEqual(int(denominator), 6**2)
        grid, base, exponent = re.search(
            r"At \$k=r=(\d+)\$.*?\$(\d+)\^\{(\d+)\}\$ bytes", self.section,
            re.DOTALL).groups()
        self.assertEqual(int(base)**int(exponent), int(grid)**int(grid))

    def test_checker_rejects_an_off_support_dual_violation(self):
        # Indices 1 and 2 occur once each in both positive-mass words.
        # This perturbation preserves the objective and both tight rows.
        record = deepcopy(self.records[4, 4])
        prices = record["dual"]["y"]
        prices[0] = str(Fraction(prices[0]) + 1)
        prices[1] = str(Fraction(prices[1]) - 1)
        with self.assertRaisesRegex(ValueError, "dual constraint violated"):
            check_example.verify_certificate(record)


if __name__ == "__main__":
    unittest.main()
