#!/usr/bin/env python3
"""Task-local independent integer/table cross-check and coupled rejection tests."""

import ast
import contextlib
import importlib.util
import io
from math import isqrt
from pathlib import Path
import re
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("radius9_exact", HERE / "check_seam.py")
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)
NOTE = HERE.parents[1] / "research" / "RADIUS9_SEAM_ONSET.md"


class ExactChecks(unittest.TestCase):
    def rejects(self, pattern, function, *args):
        with self.assertRaisesRegex(c.AuditFailure, pattern):
            function(*args)

    def test_complete_audit(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            c.audit()
        self.assertIn("exact_bridge=PASS inequalities=4", output.getvalue())

    def test_note_tables_and_independent_integer_scorer(self):
        note = NOTE.read_text(encoding="utf-8")
        for n, recorded in ((41, c.UPPER_ROWS), (42, c.LOWER_ROWS)):
            block = note.split(f"### Complete table for n={n}\n", 1)[1]
            block = block.lstrip("\n").split("\n\n", 1)[0]
            rows = [tuple(map(int, values)) for values in re.findall(
                r"^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
                block, re.MULTILINE)]
            self.assertEqual(len(rows), n-8)
            self.assertEqual(tuple(row[:3] for row in rows), recorded)
            self.assertEqual(c.table_text(n, recorded),
                             f"### Complete table for n={n}\n\n"+block)
            # Separate integer reconstruction: no Fraction or checker scorer.
            for a, b, m, q, margin in rows:
                self.assertEqual(q, 48400+220*(a+b)+a*b)
                square_target = 100000000*a*b
                expected = (isqrt(square_target//q)+1 if n == 41
                            else isqrt((square_target-1)//q))
                self.assertEqual(m, expected)
                raw = m*m*q-square_target
                self.assertEqual(margin, raw if n == 41 else -raw)
                self.assertGreater(margin, 0)
                self.assertGreater(m, 0)
                self.assertGreater(q-a*b, 0)
            if n == 41:
                self.assertLessEqual(max(r[2] for r in rows), 2000)
                numerator = sum(500000000*r[2]+r[2]**3 for r in rows)
                self.assertEqual(numerator*62500000000,
                                 194613679989*5000000000000)
                self.assertGreater(157*5000000000000-50*numerator, 0)
            else:
                numerator = sum(r[2] for r in rows)
                self.assertEqual(numerator, 32503)
                self.assertEqual(7*numerator-220000, 7521)

    def test_note_tours_and_cyclic_edges(self):
        note = NOTE.read_text(encoding="utf-8")
        for n in (41, 42):
            match = re.search(re.escape(f"sigma*_{{9,{n}}} =")+r"\s*\(([^)]+)\)", note)
            self.assertIsNotNone(match)
            tour = tuple(map(int, match[1].replace("\n", "").split(",")))
            self.assertEqual(tour, c.rank_tour(n))
            self.assertEqual(sorted(tour), list(range(9, n+1)))
            edges = [tuple(sorted(pair)) for pair in zip(tour, tour[1:]+tour[:1])]
            rows = c.UPPER_ROWS if n == 41 else c.LOWER_ROWS
            self.assertEqual(sorted(edges), sorted((a, b) for a, b, _ in rows))

    def test_integer_threshold_cross_products(self):
        # Common denominator L: A=an/L, B=bn/L, H=hn/(220 L).
        for n in (41, 42):
            length = 9*n*(n-1)
            an, bn = n*(n-1)+9*(2*n-1), 4*(2*n+8)
            hn = 220*an-length
            positive = an*an-bn*length
            raw = bn*220**2*length-hn*hn
            directed = raw if n == 41 else -raw
            self.assertTrue(min(an, bn, hn, positive, directed) > 0)
            a, b = c.threshold_data(n)
            self.assertEqual(a.numerator*length, an*a.denominator)
            self.assertEqual(b.numerator*length, bn*b.denominator)
            checked = c.check_threshold(a, b, c.F(220), "above" if n == 41 else "below")
            for value, num, den in zip(checked, (positive, hn, directed),
                                       (length**2, 220*length, (220*length)**2)):
                self.assertEqual(value.numerator*den, num*value.denominator)

    def test_only_two_endpoints(self):
        for n in (40, 43, 9, True, c.F(41)):
            with self.subTest(n=n):
                self.rejects("only endpoints", c.rank_tour, n)
                self.rejects("only endpoints", c.parity_edges, n)
                self.rejects("only endpoints", c.threshold_data, n)

    def test_missing_closure(self):
        self.rejects("edge multiplicity", c.check_rows, 41, c.UPPER_ROWS[1:], True)

    def test_duplicate_edge(self):
        rows = c.UPPER_ROWS[:-1]+(c.UPPER_ROWS[0],)
        self.rejects("edge multiplicity", c.check_rows, 41, rows, True)

    def test_invalid_tour(self):
        tour = c.rank_tour(41)
        self.rejects("complete permutation", c.check_edges, 41,
                     tour[:-1]+(9,), c.parity_edges(41))

    def test_different_hamiltonian_cycle(self):
        tour = list(c.rank_tour(41))
        tour[4], tour[5] = tour[5], tour[4]
        self.rejects("parity edges disagree", c.check_edges, 41,
                     tuple(tour), c.cyclic_edges(tour))

    def test_edge_normalization_and_domain(self):
        for first in ((41, 9, 786), (8, 41, 786), (9, 9, 786)):
            with self.subTest(first=first):
                self.rejects("edge domain", c.check_rows, 41,
                             (first,)+c.UPPER_ROWS[1:], True)

    def test_every_upper_witness_one_unit_too_small(self):
        for i, (a, b, m) in enumerate(c.UPPER_ROWS):
            with self.subTest(edge=(a, b)):
                rows = c.UPPER_ROWS[:i]+((a, b, m-1),)+c.UPPER_ROWS[i+1:]
                self.rejects("strict upper sine square margin", c.check_rows, 41, rows, True)

    def test_every_lower_witness_one_unit_too_large(self):
        for i, (a, b, m) in enumerate(c.LOWER_ROWS):
            with self.subTest(edge=(a, b)):
                rows = c.LOWER_ROWS[:i]+((a, b, m+1),)+c.LOWER_ROWS[i+1:]
                self.rejects("strict lower sine square margin", c.check_rows, 42, rows, False)

    def test_zero_square_margin_original_candidate(self):
        rows = tuple((a, b, 1000 if (a, b) == (20, 30) else m)
                     for a, b, m in c.LOWER_ROWS)
        self.rejects("strict lower sine square margin", c.check_rows, 42, rows, False)

    def test_nonpositive_and_noninteger_bounds(self):
        for m, message in ((0, "positive sine"), (-786, "positive sine"),
                           (c.F(786), "integer triples"), (True, "integer triples")):
            with self.subTest(m=m):
                self.rejects(message, c.check_rows, 41, ((9, 41, m),)+c.UPPER_ROWS[1:], True)

    def test_arcsine_domain_and_wrong_coefficient(self):
        self.rejects("outside domain", c.check_rows, 41,
                     ((9, 41, 2001),)+c.UPPER_ROWS[1:], True)
        for name, value in (("ARC_CUBIC", c.F(1, 10)), ("ARC_DOMAIN", c.F(1, 2))):
            with self.subTest(name=name), patch.object(c, name, value):
                self.rejects("fixed arcsine", c.check_arcsine)

    def test_chain_sum_failure_despite_valid_term_bounds(self):
        upper = tuple((a, b, 2000) for a, b, _ in c.UPPER_ROWS)
        lower = tuple((a, b, 1) for a, b, _ in c.LOWER_ROWS)
        self.rejects("strict chain sum margin", c.check_rows, 41, upper, True)
        self.rejects("strict chain sum margin", c.check_rows, 42, lower, False)

    def test_wrong_direction_or_separator(self):
        self.rejects("wrong chain direction", c.check_rows, 41, c.UPPER_ROWS, False)
        with patch.object(c, "Q", 221):
            self.rejects("fixed witness parameters", c.check_rows, 41, c.UPPER_ROWS, True)

    def test_threshold_positive_inputs(self):
        for args in ((-1, 1, 220), (1, 0, 220), (1, 1, 0)):
            with self.subTest(args=args):
                self.rejects("positive threshold inputs", c.check_threshold,
                             *(c.F(v) for v in args), "above")

    def test_curvature_zero_or_negative(self):
        for b in (1, 2):
            self.rejects("positive curvature", c.check_threshold,
                         c.F(1), c.F(b), c.F(220), "above")

    def test_pre_square_sign_zero_or_negative(self):
        for q in (c.F(1), c.F(1, 2)):
            self.rejects("positive pre-square sign", c.check_threshold,
                         c.F(1), c.F(1, 4), q, "below")

    def test_threshold_equality_and_reversed_directions(self):
        for direction in ("above", "below"):
            self.rejects("strict directed square margin", c.check_threshold,
                         c.F(1), c.F(1, 4), c.F(2), direction)
        for n in (41, 42):
            self.rejects("strict directed square margin", c.check_threshold,
                         *c.threshold_data(n), c.F(220), "below" if n == 41 else "above")

    def test_invalid_threshold_format(self):
        self.rejects("Fraction inputs", c.check_threshold, 1, c.F(1, 4), c.F(2), "above")
        self.rejects("threshold direction", c.check_threshold,
                     c.F(1), c.F(1, 4), c.F(2), "unknown")

    def test_invalid_pi_bounds_and_atan_domain(self):
        for name, value in (("PI_LOWER", c.F(22, 7)), ("PI_UPPER", c.F(157, 50))):
            with self.subTest(name=name), patch.object(c, name, value):
                self.rejects("strict rational pi bounds", c.check_pi)
        for x, m in ((c.F(0), 2), (c.F(1), 2), (c.F(1, 5), 0)):
            self.rejects("atan domain", c.atan_sum, x, m)

    def test_checker_independence_and_optimization_safe_gates(self):
        tree = ast.parse((HERE / "check_seam.py").read_text(encoding="utf-8"))
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)
            self.assertNotIsInstance(node, ast.Assert)
            if isinstance(node, ast.Constant):
                self.assertNotIsInstance(node.value, float)
        self.assertEqual(imports, {"argparse", "collections", "fractions"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
