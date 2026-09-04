#!/usr/bin/env python3
"""Task-local independent integer/table cross-check and coupled rejection tests."""

import ast
import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("radius10_exact", HERE / "check_seam.py")
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)
NOTE = HERE.parents[1] / "research" / "RADIUS10_SEAM_ONSET.md"
SCORE_SPEC = importlib.util.spec_from_file_location("radius10_score", HERE / "score_witnesses.py")
scorer = importlib.util.module_from_spec(SCORE_SPEC)
SCORE_SPEC.loader.exec_module(scorer)


class ExactChecks(unittest.TestCase):
    def rejects(self, pattern, function, *args):
        with self.assertRaisesRegex(c.AuditFailure, pattern):
            function(*args)

    def test_complete_audit(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            c.audit()
        self.assertIn("exact_bridge=PASS inequalities=4", output.getvalue())

    def test_only_two_endpoints(self):
        for n in (44, 47, 10, True, c.F(45)):
            with self.subTest(n=n):
                self.rejects("only endpoints", c.rank_tour, n)
                self.rejects("only endpoints", c.parity_edges, n)
                self.rejects("only endpoints", c.threshold_data, n)

    def test_missing_closure(self):
        self.rejects("edge multiplicity", c.check_rows, 45, c.UPPER_ROWS[1:], True)

    def test_duplicate_edge(self):
        rows = c.UPPER_ROWS[:-1]+(c.UPPER_ROWS[0],)
        self.rejects("edge multiplicity", c.check_rows, 45, rows, True)

    def test_invalid_tour(self):
        tour = c.rank_tour(45)
        self.rejects("complete permutation", c.check_edges, 45,
                     tour[:-1]+(10,), c.parity_edges(45))

    def test_different_hamiltonian_cycle(self):
        tour = list(c.rank_tour(45))
        tour[4], tour[5] = tour[5], tour[4]
        self.rejects("parity edges disagree", c.check_edges, 45,
                     tuple(tour), c.cyclic_edges(tour))

    def test_edge_normalization_and_domain(self):
        for first in ((45, 10, 786), (8, 45, 786), (10, 10, 786)):
            with self.subTest(first=first):
                self.rejects("edge domain", c.check_rows, 45,
                             (first,)+c.UPPER_ROWS[1:], True)

    def test_every_upper_witness_one_unit_too_small(self):
        for i, (a, b, m) in enumerate(c.UPPER_ROWS):
            with self.subTest(edge=(a, b)):
                rows = c.UPPER_ROWS[:i]+((a, b, m-1),)+c.UPPER_ROWS[i+1:]
                self.rejects("strict upper sine square margin", c.check_rows, 45, rows, True)

    def test_every_lower_witness_one_unit_too_large(self):
        for i, (a, b, m) in enumerate(c.LOWER_ROWS):
            with self.subTest(edge=(a, b)):
                rows = c.LOWER_ROWS[:i]+((a, b, m+1),)+c.LOWER_ROWS[i+1:]
                self.rejects("strict lower sine square margin", c.check_rows, 46, rows, False)

    def test_nonpositive_and_noninteger_bounds(self):
        for m, message in ((0, "positive sine"), (-786, "positive sine"),
                           (c.F(786), "integer triples"), (True, "integer triples")):
            with self.subTest(m=m):
                self.rejects(message, c.check_rows, 45, ((10, 45, m),)+c.UPPER_ROWS[1:], True)

    def test_arcsine_domain_and_wrong_coefficient(self):
        self.rejects("outside domain", c.check_rows, 45,
                     ((10, 45, 2001),)+c.UPPER_ROWS[1:], True)
        for name, value in (("ARC_CUBIC", c.F(1, 10)), ("ARC_DOMAIN", c.F(1, 2))):
            with self.subTest(name=name), patch.object(c, name, value):
                self.rejects("fixed arcsine", c.check_arcsine)

    def test_chain_sum_failure_despite_valid_term_bounds(self):
        upper = tuple((a, b, 2000) for a, b, _ in c.UPPER_ROWS)
        lower = tuple((a, b, 1) for a, b, _ in c.LOWER_ROWS)
        self.rejects("strict chain sum margin", c.check_rows, 45, upper, True)
        self.rejects("strict chain sum margin", c.check_rows, 46, lower, False)

    def test_wrong_direction_or_separator(self):
        self.rejects("wrong chain direction", c.check_rows, 45, c.UPPER_ROWS, False)
        with patch.object(c, "Q", 271):
            self.rejects("fixed witness parameters", c.check_rows, 45, c.UPPER_ROWS, True)

    def test_threshold_positive_inputs(self):
        for args in ((-1, 1, 270), (1, 0, 270), (1, 1, 0)):
            with self.subTest(args=args):
                self.rejects("positive threshold inputs", c.check_threshold,
                             *(c.F(v) for v in args), "above")

    def test_curvature_zero_or_negative(self):
        for b in (1, 2):
            self.rejects("positive curvature", c.check_threshold,
                         c.F(1), c.F(b), c.F(270), "above")

    def test_pre_square_sign_zero_or_negative(self):
        for q in (c.F(1), c.F(1, 2)):
            self.rejects("positive pre-square sign", c.check_threshold,
                         c.F(1), c.F(1, 4), q, "below")

    def test_threshold_equality_and_reversed_directions(self):
        for direction in ("above", "below"):
            self.rejects("strict directed square margin", c.check_threshold,
                         c.F(1), c.F(1, 4), c.F(2), direction)
        for n in (45, 46):
            self.rejects("strict directed square margin", c.check_threshold,
                         *c.threshold_data(n), c.F(270), "below" if n == 45 else "above")

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

    def test_exact_sine_equality_rejected_both_directions(self):
        # Synthetic boundary, not evaluation of another n or another root.
        for upper in (True, False):
            self.rejects("strict .* sine square margin", c.check_sine,
                         c.F(1, 100), c.F(1, 10), upper)

    def test_sine_domain_and_types(self):
        for s2, u in ((c.F(0), c.F(1, 10)), (c.F(1), c.F(1, 10)),
                      (c.F(1, 100), c.F(-1, 10)), (c.F(1, 100), c.F(1))):
            self.rejects("positive sine", c.check_sine, s2, u, True)
        self.rejects("Fraction sine inputs", c.check_sine, 1, c.F(1, 10), True)
        self.rejects("boolean direction", c.check_sine, c.F(1, 100), c.F(1, 10), 1)

    def test_independent_scorer_and_literals(self):
        source = (HERE / "check_seam.py").read_text(encoding="utf-8")
        data = scorer.read_literals(source)
        self.assertEqual(data, {45: c.UPPER_ROWS, 46: c.LOWER_ROWS})
        self.assertEqual(scorer.score(NOTE.read_text(encoding="utf-8"), data),
                         (73, (15404369802693, 32044)))

    def test_scorer_rejects_missing_closure(self):
        note = NOTE.read_text(encoding="utf-8")
        line = next(line for line in note.splitlines() if line.startswith("| 10 | 45 | 715 |"))
        with self.assertRaisesRegex(scorer.ScoreFailure, "row count"):
            scorer.score(note.replace(line+"\n", ""), {45: c.UPPER_ROWS, 46: c.LOWER_ROWS})

    def test_scorer_rejects_mutated_margins_thresholds_and_tour(self):
        note = NOTE.read_text(encoding="utf-8")
        line = next(line for line in note.splitlines() if line.startswith("| 10 | 45 | 715 |"))
        pieces = line.split(" | ")
        changed = " | ".join(pieces[:-1]+["1 |"])
        for mutated, message in (
            (note.replace(line, changed), "square margin transcription"),
            (note.replace("1751/35283600", "1752/35283600"), "threshold fraction"),
            (note.replace("(10,44,12,42,", "(10,44,14,42,"), "tour permutation"),
        ):
            with self.subTest(message=message):
                with self.assertRaisesRegex(scorer.ScoreFailure, message):
                    scorer.score(mutated, {45: c.UPPER_ROWS, 46: c.LOWER_ROWS})

    def test_scorer_rejects_shared_witness_transcription_error(self):
        # Alter both note and checker literal: agreement alone must not suffice.
        note = NOTE.read_text(encoding="utf-8").replace("| 10 | 45 | 715 |", "| 10 | 45 | 714 |")
        rows = ((10, 45, 714),)+c.UPPER_ROWS[1:]
        with self.assertRaisesRegex(scorer.ScoreFailure, "isqrt witness reconstruction"):
            scorer.score(note, {45: rows, 46: c.LOWER_ROWS})

    def test_scorer_requires_both_unique_literal_assignments(self):
        for source in ("UPPER_ROWS=()", "UPPER_ROWS=()\nUPPER_ROWS=()\nLOWER_ROWS=()"):
            with self.assertRaises(scorer.ScoreFailure):
                scorer.read_literals(source)

    def test_scorer_uses_no_checker_or_fraction_arithmetic(self):
        tree = ast.parse((HERE / "score_witnesses.py").read_text(encoding="utf-8"))
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)
            self.assertNotIsInstance(node, ast.Assert)
            if isinstance(node, ast.Constant):
                self.assertNotIsInstance(node.value, float)
        self.assertEqual(imports, {"ast", "collections", "math", "pathlib", "re"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
