"""Failure-sensitivity tests for the independent checker, using temporary inputs."""

from copy import deepcopy
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import unittest

import figure
import lower
import upper


ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "paper_assets"
S1 = Path("paper_assets/asymptotic_sequel/proposition7_supplement/certificate.json")
SIDMA = Path("paper_assets/journal_p2_sidma")


class RefereeControls(unittest.TestCase):
    def test_line_rejects_invalid_witnesses(self):
        witness = json.loads(
            (ASSETS / "line_upper/certificates/p2_n00003.json").read_bytes()
        )
        # In the first mutation both consecutive gaps pass; the outer pair fails.
        for change in (
            {"positions": [3, 5, 0], "span_numerator": 5},
            {"B": [176838825657, 10**12]},
            {"B": [176838825660, 10**12]},
            {"order": [3, 1, 1]},
            {"positions": [3.0, 6, 0]},
            {"span_numerator": 5},
        ):
            with self.subTest(change=change), self.assertRaises(ValueError):
                upper.check_placement({**witness, **change}, 2, 3)

    def test_lower_detects_independent_mutations(self):
        inputs = [
            SIDMA / name
            for name in ("main.tex", "supplement.tex", "numbers.tex", "s1_support.zip")
        ]
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for relative in [*inputs, S1]:
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, root / relative)
            cases = (
                (
                    "numbers.tex",
                    "0.1405694688",
                    "0.15",
                    "numbers.tex CstarLower rounded down",
                ),
                ("supplement.tex", "0.00035,", "0.00036,", "S1 KKT multiplier 1"),
                (
                    "main.tex",
                    ".14056946887766098063392.",
                    ".14056946887766098060000.",
                    "S1 abstract and main proposition strict enclosure",
                ),
            )
            for name, old, new, label in cases:
                with self.subTest(label=label):
                    path = root / SIDMA / name
                    source = path.read_text(encoding="utf-8")
                    self.assertEqual(source.count(old), 1)
                    path.write_text(source.replace(old, new), encoding="utf-8")
                    self.assertIs(dict(lower.run(root))[label], False)
                    path.write_text(source, encoding="utf-8")

            certificate = json.loads((root / S1).read_bytes())
            for key, slot, bad, label in (
                ("G_signs", "zero", ["1", "2"], "S1 certificate G(zero)"),
                ("multipliers", 1, ["0.5", "0.6"], "S1 certificate lambda 2"),
            ):
                with self.subTest(label=label):
                    modified = deepcopy(certificate)
                    modified[key][slot] = bad
                    (root / S1).write_text(json.dumps(modified), encoding="utf-8")
                    self.assertIs(dict(lower.run(root))[label], False)

    def test_pruning_agrees_with_unpruned_orders(self):
        _, period = figure.tau_ticks()
        for n in range(3, 9):
            for radius in (Fraction(1, 3), Fraction(3), Fraction(7), Fraction(12)):
                with self.subTest(n=n, radius=radius):
                    table = figure.angle_table(n, radius, False)
                    exists = any(
                        figure.positions((n, *order), table, period) is not None
                        for order in permutations(range(1, n))
                    )
                    self.assertEqual(
                        figure.no_lower_order(n, table, period), not exists
                    )

    def test_reversed_endpoints_and_coincident_centers(self):
        lo, hi = map(Fraction, ("0.26086956521", "0.26086956522"))
        tlo, thi = figure.tau_ticks()
        self.assertFalse(
            figure.no_lower_order(3, figure.angle_table(3, hi, False), thi)
        )
        self.assertIsNone(
            figure.positions((3, 1, 2), figure.angle_table(3, lo, True), tlo)
        )
        self.assertFalse(figure.cartesian_disjoint((3, 1, 2), (0, 0, 0), hi))


if __name__ == "__main__":
    unittest.main()
