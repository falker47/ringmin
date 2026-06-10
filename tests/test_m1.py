from __future__ import annotations

import random

import pytest

from ringmin.crosscheck import slsqp_fixed_order, slsqp_unconstrained_global
from ringmin.evaluator import full_radius
from ringmin.search import certified_search


def test_slsqp_fixed_order_cross_validation_n7() -> None:
    rng = random.Random(4619480)
    for case in range(10):
        order = list(range(1, 8))
        rng.shuffle(order)
        exact = full_radius(tuple(order))
        check = slsqp_fixed_order(tuple(order), starts=20, seed=case)
        assert check.R == pytest.approx(exact.R_full, abs=1e-6)


def test_slsqp_unconstrained_global_n6_matches_certified() -> None:
    certified = certified_search(6, k=5000).best
    check = slsqp_unconstrained_global(6, starts=80, seed=6)
    assert check.R == pytest.approx(certified.R_full, abs=1e-6)
