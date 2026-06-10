from __future__ import annotations

import math
import random

import pytest

from ringmin.evaluator import chain_radius, full_radius
from ringmin.geometry import cycle_equivalent, theta
from ringmin.patterns import interleave, sequential, supnick_max_tour
from ringmin.search import certified_search


def test_n3_descartes_order_123() -> None:
    result = full_radius((1, 2, 3))
    expected = 6.0 / 23.0
    assert result.R_chain == pytest.approx(expected, abs=1e-10)
    assert result.R_full == pytest.approx(expected, abs=1e-10)
    assert abs(result.R_full - result.R_chain) <= 1e-10


def test_n10_certified_search_matches_mse_prior() -> None:
    result = certified_search(10, k=5000)
    best = result.best
    assert result.certified
    assert best.R_full == pytest.approx(9.979907, abs=5e-6)
    assert 1.0 in best.floating_radii
    chain_part = tuple(int(r) for r in best.order if int(r) != 1)
    assert cycle_equivalent(chain_part, (10, 2, 9, 4, 7, 6, 5, 8, 3))


def test_n10_sequential_full_equals_chain() -> None:
    result = full_radius(sequential(range(1, 11)))
    assert result.R_full == pytest.approx(10.77, abs=0.01)
    assert abs(result.R_full - result.R_chain) <= 1e-9


def test_rotation_reflection_invariance_n8_random() -> None:
    rng = random.Random(4619480)
    for _ in range(20):
        order = list(range(1, 9))
        rng.shuffle(order)
        base = full_radius(tuple(order)).R_full
        shift = rng.randrange(8)
        rotated = tuple(order[shift:] + order[:shift])
        reflected = tuple(reversed(order))
        assert full_radius(rotated).R_full == pytest.approx(base, abs=1e-9)
        assert full_radius(reflected).R_full == pytest.approx(base, abs=1e-9)


def test_theta_properties() -> None:
    for R in (0.1, 1.0, 10.0, 100.0):
        for a in range(1, 8):
            for b in range(1, 8):
                value = theta(R, a, b)
                assert 0.0 < value < math.pi
                assert value == pytest.approx(theta(R, b, a), abs=1e-15)
                assert theta(R * 1.5, a, b) < value


def test_supermodularity_numerical_check() -> None:
    rng = random.Random(295)
    for _ in range(5000):
        R = 10 ** rng.uniform(-2, 3)
        a, b = sorted(rng.sample(range(1, 30), 2))
        c, d = sorted(rng.sample(range(1, 30), 2))
        lhs = theta(R, a, c) + theta(R, b, d)
        rhs = theta(R, a, d) + theta(R, b, c)
        if lhs + 1e-12 < rhs:
            raise AssertionError(
                "supermodularity counterexample: "
                f"R={R}, a={a}, b={b}, c={c}, d={d}, lhs={lhs}, rhs={rhs}"
            )


def test_interleave_example_m9_values_2_to_10() -> None:
    assert cycle_equivalent(interleave(range(2, 11)), (10, 2, 9, 4, 7, 6, 5, 8, 3))


def test_interleave_example_m10_values_2_to_11() -> None:
    assert cycle_equivalent(interleave(range(2, 12)), (11, 2, 10, 4, 8, 6, 7, 5, 9, 3))


def test_supnick_max_tour_matches_interleave_m5_to_m13() -> None:
    for m in range(5, 14):
        values = tuple(range(1, m + 1))
        closed = supnick_max_tour(values)
        generated = interleave(values)
        assert cycle_equivalent(closed, generated), (
            f"m={m}: closed={closed}, interleave={generated}"
        )


def test_full_never_below_chain_on_samples() -> None:
    rng = random.Random(123)
    for _ in range(10):
        order = list(range(1, 8))
        rng.shuffle(order)
        result = full_radius(tuple(order))
        assert result.R_full + 1e-10 >= result.R_chain
        assert chain_radius(tuple(order)) == pytest.approx(result.R_chain, abs=1e-12)
