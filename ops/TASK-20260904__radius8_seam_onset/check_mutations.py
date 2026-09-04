#!/usr/bin/env python3
"""Targeted rejection tests and a separate integer/table audit of the bridge."""

from __future__ import annotations

import ast
from contextlib import redirect_stdout
from fractions import Fraction as F
import importlib.util
import io
from pathlib import Path
import re
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("radius8_exact", HERE / "check_seam.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load task-local checker")
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class ExactBridgeTests(unittest.TestCase):
    def test_valid_complete_audit(self):
        with redirect_stdout(io.StringIO()) as output:
            C.audit()
        self.assertIn("exact_bridge=PASS", output.getvalue())

    def test_independent_integer_scorer_and_note_tables(self):
        # Direct integer cross-products; no call to the Fraction row scorer.
        note = (HERE.parents[1] / "research" / "RADIUS8_SEAM_ONSET.md").read_text(
            encoding="utf-8")
        expected_moments = {}
        for n, rows in ((37, C.UPPER_ROWS), (38, C.LOWER_ROWS)):
            block = note.split(f"### Complete table for n={n}\n", 1)[1]
            block = block.lstrip("\n").split("\n\n", 1)[0]
            table = [tuple(map(int, match)) for match in re.findall(
                r"^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
                block, re.MULTILINE)]
            self.assertEqual(len(table), n-7)
            self.assertEqual(tuple(((a,b),m) for a,b,m,_,_ in table), rows)
            for a,b,m,q,margin in table:
                self.assertEqual(q, (176+a)*(176+b))
                self.assertGreater(m, 0)
                self.assertGreater(q-a*b, 0)
                directed = m*m*q-10000**2*a*b
                self.assertEqual(margin, directed if n == 37 else -directed)
                self.assertGreater(margin, 0)
                if n == 37:
                    self.assertLessEqual(20*m, 3*10000)
            expected_moments[n] = (sum(m for _,_,m,_,_ in table),
                                   sum(m**3 for _,_,m,_,_ in table))
        # Integer proof of upper half-sum <333/106 and lower half-sum >22/7.
        first, third = expected_moments[37]
        upper_num = 40*10000**2*first+7*third
        self.assertGreater(333*40*10000**3-106*upper_num, 0)
        self.assertGreater(7*expected_moments[38][0]-22*10000, 0)
        # Separate integer Descartes algebra, from common denominator 8n(n-1).
        for n in (37, 38):
            a_num = n*(n-1)+8*(2*n-1)
            den = 8*n*(n-1)
            b_num = 4*(2*n+7)
            self.assertGreater(a_num*a_num-b_num*den, 0)
            h_num = 176*a_num-den
            self.assertGreater(h_num, 0)
            difference = 176**2*b_num*den-h_num*h_num
            self.assertGreater(difference if n == 37 else -difference, 0)

    def test_source_is_exact_and_independent(self):
        tree = ast.parse((HERE / "check_seam.py").read_text(encoding="utf-8"))
        imports = set()
        for node in ast.walk(tree):
            self.assertNotIsInstance(node, ast.Assert)
            if isinstance(node, ast.Constant):
                self.assertNotIsInstance(node.value, float)
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            if isinstance(node, ast.ImportFrom):
                imports.add(node.module)
        self.assertEqual(imports, {"__future__", "argparse", "collections", "fractions"})

    def test_missing_cyclic_closure_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "missing or duplicate"):
            C.check_rows(37, C.UPPER_ROWS[:-1], True)

    def test_duplicate_edge_rejected(self):
        rows = C.LOWER_ROWS[:-1]+(C.LOWER_ROWS[0],)
        with self.assertRaisesRegex(C.AuditFailure, "missing or duplicate"):
            C.check_rows(38, rows, False)

    def test_missing_interior_edge_rejected(self):
        rows = C.UPPER_ROWS[:10]+C.UPPER_ROWS[11:]
        with self.assertRaisesRegex(C.AuditFailure, "missing or duplicate"):
            C.check_rows(37, rows, True)

    def test_duplicate_tour_vertex_rejected(self):
        tour = C.rank_tour(38)
        bad = tour[:-1]+(tour[0],)
        with self.assertRaisesRegex(C.AuditFailure, "permutation"):
            C.check_edges(38, bad, C.cyclic_edges(bad))

    def test_rewired_complete_cycle_rejected(self):
        tour = list(C.rank_tour(37))
        tour[4], tour[6] = tour[6], tour[4]
        with self.assertRaisesRegex(C.AuditFailure, "parity edges"):
            C.check_edges(37, tuple(tour), C.cyclic_edges(tuple(tour)))

    def test_parity_formula_omission_rejected(self):
        edges = C.parity_edges(38)
        with patch.object(C, "parity_edges", return_value=edges[:-1]):
            with self.assertRaisesRegex(C.AuditFailure, "parity edges"):
                C.check_rows(38, C.LOWER_ROWS, False)

    def test_upper_bound_below_sine_rejected(self):
        rows = ((C.UPPER_ROWS[0][0], 859),)+C.UPPER_ROWS[1:]
        with self.assertRaisesRegex(C.AuditFailure, "upper sine square"):
            C.check_rows(37, rows, True)

    def test_lower_bound_above_sine_rejected(self):
        rows = ((C.LOWER_ROWS[0][0], 870),)+C.LOWER_ROWS[1:]
        with self.assertRaisesRegex(C.AuditFailure, "lower sine square"):
            C.check_rows(38, rows, False)

    def test_negative_bound_same_square_rejected(self):
        rows = ((C.UPPER_ROWS[0][0], -860),)+C.UPPER_ROWS[1:]
        with self.assertRaisesRegex(C.AuditFailure, "positive integer"):
            C.check_rows(37, rows, True)

    def test_upper_majorant_domain_rejected(self):
        rows = ((C.UPPER_ROWS[0][0], 1600),)+C.UPPER_ROWS[1:]
        with self.assertRaisesRegex(C.AuditFailure, "outside arcsine"):
            C.check_rows(37, rows, True)

    def test_weakened_arcsine_polynomial_rejected(self):
        with patch.object(C, "ARC_CUBIC", F(1, 6)):
            with self.assertRaisesRegex(C.AuditFailure, "polynomial identity"):
                C.check_arcsine_majorant()

    def test_enlarged_arcsine_domain_rejected(self):
        with patch.object(C, "ARC_DOMAIN", F(1, 2)):
            with self.assertRaisesRegex(C.AuditFailure, "polynomial endpoint"):
                C.check_arcsine_majorant()

    def test_invalid_pi_lower_rejected(self):
        with patch.object(C, "PI_LOWER", F(22, 7)):
            with self.assertRaisesRegex(C.AuditFailure, "pi lower"):
                C.check_pi()

    def test_invalid_pi_upper_rejected(self):
        with patch.object(C, "PI_UPPER", F(3)):
            with self.assertRaisesRegex(C.AuditFailure, "pi upper"):
                C.check_pi()

    def test_threshold_direction_reversed_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "threshold square"):
            C.check_threshold(*C.threshold_data(37), F(176), "below")

    def test_negative_pre_square_comparison_rejected(self):
        # A^2>B and B-H^2>0 both hold, but H<0: sign gate must run.
        with self.assertRaisesRegex(C.AuditFailure, "before squaring"):
            C.check_threshold(F(2), F(1), F(2, 5), "above")

    def test_nonpositive_curvature_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "before reciprocal"):
            C.check_threshold(F(1), F(2), F(2), "above")

    def test_negative_A_same_square_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "positive threshold inputs"):
            C.check_threshold(F(-2), F(1), F(1), "below")

    def test_threshold_equality_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "strict threshold square"):
            C.check_threshold(F(2), F(1), F(1), "above")

    def test_wrong_separator_rejected(self):
        with patch.object(C, "SEPARATOR", F(175)):
            with self.assertRaisesRegex(C.AuditFailure, "fixed witness parameters"):
                C.check_rows(37, C.UPPER_ROWS, True)

    def test_wrong_endpoint_direction_rejected(self):
        with self.assertRaisesRegex(C.AuditFailure, "bound direction"):
            C.check_rows(38, C.LOWER_ROWS, True)

    def test_invalid_endpoints_rejected(self):
        for n in (36, 39, True, 37.0):
            with self.subTest(n=n), self.assertRaisesRegex(C.AuditFailure, "endpoint"):
                C.rank_tour(n)


if __name__ == "__main__":
    unittest.main(verbosity=2)
