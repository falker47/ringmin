"""Exercise the independent finite profile checker without importing numerical search code."""

import importlib.util
from fractions import Fraction
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "paper_assets" / "paper_ii_profiles" / "checks" / "verify_finite.py"
spec = importlib.util.spec_from_file_location("profile_finite_checker", CHECK)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def test_sorted_matching_with_and_without_surplus():
    assert checker.verify_matching() > 400


def test_copies_all_orders_and_all_paths():
    assert checker.verify_copies() == 70


def test_copied_coordinates_all_pairs():
    assert checker.verify_placements() == 480


def test_certified_squeeze_comparisons():
    assert checker.verify_squeeze() == 16


def test_external_reference_rows_when_available():
    folder = ROOT / ".codex_inputs"
    if not folder.exists():
        pytest.skip("official external setup inputs unavailable")
    assert checker.verify_sources(folder) == 16


@pytest.mark.parametrize("power", checker.POWER)
def test_directed_edge_bounds(power):
    for i, j, n in ((1, 1, 7), (1, 5, 7), (7, 7, 7)):
        scale = 1009
        lower, upper = checker.edge_bounds(i, j, n, power, scale)
        exponent = power / 2
        truth = Fraction(i*j, n*n) ** exponent.numerator
        assert Fraction(lower, scale)**exponent.denominator <= truth
        assert Fraction(upper, scale)**exponent.denominator >= truth
        assert upper - lower in (0, 1)


def test_machin_enclosure_and_constants():
    lo, hi = checker.pi_bounds()
    assert Fraction(333, 106) < lo < hi < Fraction(355, 113)
    for n in range(2, 8):
        assert checker.exhaustive(n, Fraction(0)) == (n - 1, n - 1)


def test_sampling_counterexamples():
    def mark(x):
        return int(x.denominator % 2 == 0)

    for n in (3, 5, 7, 11):
        assert sum(mark(Fraction(i, n)) for i in range(1, n + 1)) == 0
    for n in (2, 4, 8, 16):
        assert sum(mark(Fraction(i, n)) for i in range(1, n + 1)) == n - 1


def test_stability_with_zero_marks_ties_and_jumps():
    assert checker.verify_stability() == 225


def test_rational_word_lp_duals_and_finite_batches():
    assert checker.verify_word_lp() == 12
