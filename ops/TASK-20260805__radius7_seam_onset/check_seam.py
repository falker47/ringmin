#!/usr/bin/env python3
"""Independent audit for the exact radius-7 formal Supnick seam onset.

The default path uses only Python's standard library and exact Fraction
arithmetic. It audits every new endpoint inequality, every row of both
adjacent-edge tables, and the exact comparisons with pi. The optional mpmath
path is a separately labeled finite numerical diagnostic; it is not a premise
of the all-n theorem. This script deliberately does not import ringmin.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

K = 7
MIN_N = K + 2
LEFT_ENDPOINT = 33
RIGHT_ENDPOINT = 34
SEPARATOR = Fraction(140)
_EXPLICIT_GATE_COUNT = 0


class AuditFailure(RuntimeError):
    """An explicit audit gate failed."""


def _require(condition: bool, message: str) -> None:
    """Raise explicitly so gates remain active under python -O."""
    global _EXPLICIT_GATE_COUNT
    _EXPLICIT_GATE_COUNT += 1
    if not condition:
        raise AuditFailure(message)


def _append_index(
    target: list[int], used: set[int], index: int, size: int
) -> None:
    _require(1 <= index <= size, f"Supnick index outside 1..{size}: {index}")
    _require(index not in used, f"duplicate Supnick index: {index}")
    used.add(index)
    target.append(index)


def shifted_supnick_tour(n: int) -> tuple[int, ...]:
    """The proof-note representative on the consecutive radii 7,...,n."""
    if n < MIN_N:
        raise ValueError(f"n must be at least {MIN_N}, got {n}")
    size = n - K + 1
    midpoint = (size + 1) // 2
    used: set[int] = set()
    first: list[int] = []
    second: list[int] = []

    offset = 0
    while True:
        before = len(used)
        low = 1 + 2 * offset
        high = size - 1 - 2 * offset
        if low <= midpoint:
            _append_index(first, used, low, size)
        if high > midpoint:
            _append_index(first, used, high, size)
        offset += 1
        if len(used) == before:
            break

    offset = 0
    while True:
        before = len(used)
        low = 2 + 2 * offset
        high = size - 2 - 2 * offset
        if low <= midpoint:
            _append_index(second, used, low, size)
        if high > midpoint:
            _append_index(second, used, high, size)
        offset += 1
        if len(used) == before:
            break

    _require(
        used == set(range(1, size)),
        f"shifted Supnick construction missed ranks for n={n}: {used}",
    )
    ranks = first + list(reversed(second)) + [size]
    return tuple(rank + K - 1 for rank in ranks)


def shifted_interleave_tour(n: int) -> tuple[int, ...]:
    """Independent production-style interleave construction."""
    if n < MIN_N:
        raise ValueError(f"n must be at least {MIN_N}, got {n}")
    size = n - K + 1
    midpoint = (size + 1) // 2
    used: set[int] = {size}
    arm_a = [size]
    arm_b: list[int] = []
    offset = 0
    while True:
        before = len(used)
        low_a = 1 + 2 * offset
        high_a = size - 1 - 2 * offset
        low_b = 2 + 2 * offset
        high_b = size - 2 - 2 * offset
        if low_a <= midpoint:
            _append_index(arm_a, used, low_a, size)
        if high_a > midpoint:
            _append_index(arm_a, used, high_a, size)
        if low_b <= midpoint:
            _append_index(arm_b, used, low_b, size)
        if high_b > midpoint:
            _append_index(arm_b, used, high_b, size)
        offset += 1
        if len(used) == before:
            break
    _require(
        used == set(range(1, size + 1)),
        f"shifted interleave construction missed ranks for n={n}: {used}",
    )
    return tuple(rank + K - 1 for rank in arm_a + list(reversed(arm_b)))


def cycle_equivalent(left: Iterable[int], right: Iterable[int]) -> bool:
    a = tuple(left)
    b = tuple(right)
    if len(a) != len(b):
        return False
    doubled = a + a
    reversed_a = tuple(reversed(a))
    doubled_reversed = reversed_a + reversed_a
    return any(doubled[i : i + len(b)] == b for i in range(len(b))) or any(
        doubled_reversed[i : i + len(b)] == b for i in range(len(b))
    )


def _edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def ordered_adjacent_edges(order: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        _edge(value, order[(index + 1) % len(order)])
        for index, value in enumerate(order)
    )


def adjacent_edges(order: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(ordered_adjacent_edges(order))


def formula_edges(n: int) -> frozenset[tuple[int, int]]:
    """Parity-explicit specialization of the fixed-k formulas at k=7."""
    if n < MIN_N:
        raise ValueError(f"n must be at least {MIN_N}, got {n}")
    size = n - K + 1
    if size % 2 == 0:
        half = size // 2
        edges = {_edge(K, n), _edge(K + half - 1, K + half)}
        edges.update(_edge(i, n + K - 1 - i) for i in range(K, K + half - 1))
        edges.update(_edge(i, n + K + 1 - i) for i in range(K + 1, K + half))
    else:
        half = (size - 1) // 2
        edges = {_edge(K, n)}
        edges.update(_edge(i, n + K - 1 - i) for i in range(K, K + half))
        edges.update(
            _edge(i, n + K + 1 - i) for i in range(K + 1, K + half + 1)
        )
    return frozenset(edges)


def cycle_from_formula_edges(n: int) -> tuple[int, ...]:
    """Reconstruct an oriented cycle from the independent degree-2 graph."""
    edges = formula_edges(n)
    neighbors: dict[int, set[int]] = {value: set() for value in range(K, n + 1)}
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    _require(
        all(len(values) == 2 for values in neighbors.values()),
        f"formula graph is not 2-regular at n={n}: {neighbors}",
    )

    cycle = [K, n - 1]
    previous = K
    current = n - 1
    while True:
        candidates = neighbors[current] - {previous}
        _require(
            len(candidates) == 1,
            f"formula cycle continuation is ambiguous at n={n}, vertex={current}",
        )
        next_value = next(iter(candidates))
        if next_value == K:
            break
        _require(
            next_value not in cycle,
            f"formula cycle closes a proper subcycle at n={n}: {cycle}",
        )
        cycle.append(next_value)
        previous, current = current, next_value
    _require(
        len(cycle) == n - K + 1 and set(cycle) == set(range(K, n + 1)),
        f"formula cycle missed vertices at n={n}: {cycle}",
    )
    return tuple(cycle)


def check_order_convention(stop: int) -> None:
    for n in range(MIN_N, stop + 1):
        proof_order = shifted_supnick_tour(n)
        interleave_order = shifted_interleave_tour(n)
        _require(
            cycle_equivalent(proof_order, interleave_order),
            f"tour convention mismatch at n={n}",
        )
        _require(
            proof_order[0] == K
            and proof_order[1] == n - 1
            and proof_order[-1] == n,
            f"seam-neighbor mismatch at n={n}: {proof_order}",
        )
        actual_edges = adjacent_edges(proof_order)
        expected_edges = formula_edges(n)
        _require(
            len(actual_edges) == n - K + 1 and actual_edges == expected_edges,
            f"edge formula mismatch at n={n}",
        )
        _require(
            {_edge(K, n - 1), _edge(K, n)} <= actual_edges,
            f"formal seam edges missing at n={n}",
        )
        _require(
            cycle_from_formula_edges(n) == proof_order,
            f"formula-graph reconstruction mismatch at n={n}",
        )


def _sine_square(radius: Fraction, a: int, b: int) -> Fraction:
    return Fraction(a * b, 1) / ((radius + a) * (radius + b))


N33_UPPER_ROWS = (
    ((7, 32), Fraction(8, 903), Fraction(12, 125), Fraction(5032, 14109375)),
    ((9, 32), Fraction(72, 6407), Fraction(27, 250), Fraction(170703, 400437500)),
    ((9, 30), Fraction(27, 2533), Fraction(13, 125), Fraction(6202, 39578125)),
    ((11, 30), Fraction(33, 2567), Fraction(57, 500), Fraction(90183, 641750000)),
    ((11, 28), Fraction(11, 906), Fraction(14, 125), Fraction(5701, 14156250)),
    ((13, 28), Fraction(13, 918), Fraction(3, 25), Fraction(137, 573750)),
    ((13, 26), Fraction(169, 12699), Fraction(29, 250), Fraction(117359, 793687500)),
    ((15, 26), Fraction(39, 2573), Fraction(31, 250), Fraction(35153, 160812500)),
    ((15, 24), Fraction(18, 1271), Fraction(3, 25), Fraction(189, 794375)),
    ((17, 24), Fraction(102, 6437), Fraction(63, 500), Fraction(48453, 1609250000)),
    ((17, 22), Fraction(187, 12717), Fraction(61, 500), Fraction(569957, 3179250000)),
    ((19, 22), Fraction(209, 12879), Fraction(16, 125), Fraction(31399, 201234375)),
    ((19, 20), Fraction(19, 1272), Fraction(31, 250), Fraction(8723, 19875000)),
    ((20, 21), Fraction(3, 184), Fraction(16, 125), Fraction(229, 2875000)),
    ((18, 21), Fraction(27, 1817), Fraction(61, 500), Fraction(11057, 454250000)),
    ((18, 23), Fraction(207, 12877), Fraction(16, 125), Fraction(62137, 201203125)),
    ((16, 23), Fraction(92, 6357), Fraction(61, 500), Fraction(654397, 1589250000)),
    ((16, 25), Fraction(20, 1287), Fraction(63, 500), Fraction(108103, 321750000)),
    ((14, 25), Fraction(5, 363), Fraction(59, 500), Fraction(13603, 90750000)),
    ((14, 27), Fraction(27, 1837), Fraction(61, 500), Fraction(85477, 459250000)),
    ((12, 27), Fraction(81, 6346), Fraction(57, 500), Fraction(184077, 793250000)),
    ((12, 29), Fraction(87, 6422), Fraction(59, 500), Fraction(302491, 802750000)),
    ((10, 29), Fraction(29, 2535), Fraction(27, 250), Fraction(7103, 31687500)),
    ((10, 31), Fraction(31, 2565), Fraction(11, 100), Fraction(73, 5130000)),
    ((8, 31), Fraction(62, 6327), Fraction(1, 10), Fraction(127, 632700)),
    ((8, 33), Fraction(66, 6401), Fraction(51, 500), Fraction(149001, 1600250000)),
    ((7, 33), Fraction(11, 1211), Fraction(12, 125), Fraction(2509, 18921875)),
)


N34_LOWER_ROWS = (
    ((7, 33), Fraction(11, 1211), Fraction(19, 200), Fraction(2829, 48440000)),
    ((9, 33), Fraction(297, 25777), Fraction(21, 200), Fraction(512343, 1031080000)),
    ((9, 31), Fraction(31, 2831), Fraction(1, 10), Fraction(269, 283100)),
    ((11, 31), Fraction(341, 25821), Fraction(11, 100), Fraction(285659, 258210000)),
    ((11, 29), Fraction(319, 25519), Fraction(11, 100), Fraction(102201, 255190000)),
    ((13, 29), Fraction(29, 1989), Fraction(3, 25), Fraction(224, 1243125)),
    ((13, 27), Fraction(39, 2839), Fraction(23, 200), Fraction(58169, 113560000)),
    ((15, 27), Fraction(81, 5177), Fraction(1, 8), Fraction(7, 331328)),
    ((15, 25), Fraction(5, 341), Fraction(3, 25), Fraction(56, 213125)),
    ((17, 25), Fraction(85, 5181), Fraction(1, 8), Fraction(259, 331584)),
    ((17, 23), Fraction(391, 25591), Fraction(3, 25), Fraction(14056, 15994375)),
    ((19, 23), Fraction(437, 25917), Fraction(1, 8), Fraction(2051, 1658688)),
    ((19, 21), Fraction(19, 1219), Fraction(3, 25), Fraction(904, 761875)),
    ((20, 21), Fraction(3, 184), Fraction(1, 8), Fraction(1, 1472)),
    ((20, 22), Fraction(11, 648), Fraction(13, 100), Fraction(61, 810000)),
    ((18, 22), Fraction(11, 711), Fraction(3, 25), Fraction(476, 444375)),
    ((18, 24), Fraction(54, 3239), Fraction(1, 8), Fraction(217, 207296)),
    ((16, 24), Fraction(8, 533), Fraction(3, 25), Fraction(203, 333125)),
    ((16, 26), Fraction(4, 249), Fraction(1, 8), Fraction(7, 15936)),
    ((14, 26), Fraction(13, 913), Fraction(23, 200), Fraction(37023, 36520000)),
    ((14, 28), Fraction(1, 66), Fraction(3, 25), Fraction(31, 41250)),
    ((12, 28), Fraction(1, 76), Fraction(11, 100), Fraction(201, 190000)),
    ((12, 30), Fraction(9, 646), Fraction(23, 200), Fraction(9133, 12920000)),
    ((10, 30), Fraction(1, 85), Fraction(21, 200), Fraction(503, 680000)),
    ((10, 32), Fraction(8, 645), Fraction(11, 100), Fraction(391, 1290000)),
    ((8, 32), Fraction(16, 1591), Fraction(1, 10), Fraction(9, 159100)),
    ((8, 34), Fraction(34, 3219), Fraction(1, 10), Fraction(181, 321900)),
    ((7, 34), Fraction(17, 1827), Fraction(19, 200), Fraction(20453, 73080000)),
)


def _poly_trim(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _poly_add(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    size = max(len(left), len(right))
    values = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        values[index] += value
    for index, value in enumerate(right):
        values[index] += value
    return _poly_trim(tuple(values))


def _poly_multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    values = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            values[left_index + right_index] += left_value * right_value
    return _poly_trim(tuple(values))


def _poly_integral_zero_one(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (value / (index + 1) for index, value in enumerate(coefficients)),
        Fraction(0),
    )


def _check_exact_pi_comparisons() -> None:
    """Audit the exact Machin lower bound and classical 22/7 upper bound."""
    denominator = (Fraction(1), Fraction(0), Fraction(1))
    alternating = (
        Fraction(1),
        Fraction(0),
        Fraction(-1),
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(-1),
    )
    product = _poly_multiply(denominator, alternating)
    remainder = _poly_add((Fraction(1),), tuple(-value for value in product))
    expected_remainder = tuple(
        Fraction(1) if index == 8 else Fraction(0) for index in range(9)
    )
    _require(
        remainder == expected_remainder,
        "finite geometric identity for the Machin atan lower bound failed",
    )

    x = Fraction(1, 5)
    y = Fraction(1, 239)
    _require(0 < y < x < 1, "Machin arctangent argument signs failed")
    a_lower = x - x**3 / 3 + x**5 / 5 - x**7 / 7
    _require(
        a_lower == Fraction(323852, 1640625) > 0,
        "unexpected integrated Machin lower polynomial",
    )
    tan_two_a = 2 * x / (1 - x**2)
    _require(
        tan_two_a == Fraction(5, 12) and 0 < tan_two_a < 1,
        "Machin first tangent-doubling or branch gate failed",
    )
    _require(1 - tan_two_a**2 > 0, "Machin second doubling denominator failed")
    tan_four_a = 2 * tan_two_a / (1 - tan_two_a**2)
    _require(
        tan_four_a == Fraction(120, 119) > 0,
        "Machin second tangent-doubling failed",
    )
    _require(
        1 + tan_four_a * y > 0,
        "Machin tangent-subtraction denominator failed",
    )
    tan_difference = (tan_four_a - y) / (1 + tan_four_a * y)
    _require(tan_difference == 1, "Machin tangent-subtraction identity failed")
    machin_lower = 16 * a_lower - 4 * y
    _require(
        machin_lower == Fraction(1231847548, 392109375),
        "unexpected Machin rational lower bound for pi",
    )
    _require(
        machin_lower - Fraction(333, 106)
        == Fraction(3418213, 41563593750)
        > 0,
        "Machin bridge 333/106 < pi failed",
    )

    numerator = [Fraction(0) for _ in range(9)]
    for first_power, first_coefficient in enumerate(
        (Fraction(1), Fraction(-4), Fraction(6), Fraction(-4), Fraction(1))
    ):
        numerator[first_power + 4] = first_coefficient
    quotient = (
        Fraction(4),
        Fraction(0),
        Fraction(-4),
        Fraction(0),
        Fraction(5),
        Fraction(-4),
        Fraction(1),
    )
    reconstructed = _poly_add(
        _poly_multiply(denominator, quotient), (Fraction(-4),)
    )
    _require(
        reconstructed == tuple(numerator),
        "polynomial division identity for the 22/7 pi bound failed",
    )
    _require(
        _poly_integral_zero_one(quotient) == Fraction(22, 7),
        "unexpected quotient integral for the 22/7 pi bound",
    )


def check_exact_rational_audit(order_stop: int) -> None:
    """Audit exact transcriptions only; no floating-point call occurs here."""
    check_order_convention(order_stop)
    order_33 = shifted_supnick_tour(LEFT_ENDPOINT)
    order_34 = shifted_supnick_tour(RIGHT_ENDPOINT)
    _require(
        order_33
        == (
            7, 32, 9, 30, 11, 28, 13, 26, 15, 24, 17, 22, 19, 20,
            21, 18, 23, 16, 25, 14, 27, 12, 29, 10, 31, 8, 33,
        ),
        "hard-coded n=33 endpoint order mismatch",
    )
    _require(
        order_34
        == (
            7, 33, 9, 31, 11, 29, 13, 27, 15, 25, 17, 23, 19, 21,
            20, 22, 18, 24, 16, 26, 14, 28, 12, 30, 10, 32, 8, 34,
        ),
        "hard-coded n=34 endpoint order mismatch",
    )
    deleted_34 = tuple(value for value in order_34 if value != RIGHT_ENDPOINT)
    _require(
        not cycle_equivalent(deleted_34, order_33),
        "negative control failed: vertex deletion unexpectedly preserves the tour",
    )

    boundary_gap_28 = Fraction(1, K) - Fraction(1, 28) - Fraction(1, 27)
    _require(
        boundary_gap_28 == Fraction(53, 756) > 0,
        "n=28 threshold-boundary sign gate failed",
    )
    _require(
        Fraction(4, 28 * 27) - boundary_gap_28**2
        == Fraction(215, 571536)
        > 0,
        "n=28 no-threshold boundary square audit failed",
    )
    boundary_gap_29 = Fraction(1, K) - Fraction(1, 29) - Fraction(1, 28)
    _require(
        boundary_gap_29 == Fraction(59, 812) > 0,
        "n=29 threshold-boundary sign gate failed",
    )
    _require(
        boundary_gap_29**2 - Fraction(4, 29 * 28)
        == Fraction(233, 659344)
        > 0,
        "n=29 positive-threshold boundary square audit failed",
    )

    reciprocal_separator = Fraction(1, 1) / SEPARATOR
    _require(
        reciprocal_separator == Fraction(1, 140) > 0,
        "unexpected reciprocal separator",
    )

    alpha_33 = Fraction(1, 33) + Fraction(1, 32)
    q_33_square = alpha_33 / K + Fraction(1, 33 * 32)
    _require(
        q_33_square - alpha_33**2
        == Fraction(46457, 7805952)
        > 0,
        "n=33 physical-minus-root sign gate failed",
    )
    base_33 = Fraction(1, K) + alpha_33
    radical_33_square = 4 * q_33_square
    _require(base_33 == Fraction(1511, 7392) > 0, "unexpected n=33 rational term")
    _require(
        radical_33_square == Fraction(3, 77) > 0,
        "unexpected n=33 radical square",
    )
    _require(
        base_33**2 - radical_33_square
        == Fraction(154225, 54641664)
        > 0,
        "n=33 kappa positivity comparison failed",
    )
    gap_33 = base_33 - reciprocal_separator
    _require(
        gap_33 == Fraction(7291, 36960) > 0,
        "unexpected n=33 separator gap",
    )
    _require(
        radical_33_square - gap_33**2
        == Fraction(63719, 1366041600)
        > 0,
        "n=33 threshold separator comparison failed",
    )
    p_gap_33 = Fraction(1, K) - reciprocal_separator - alpha_33
    p_radical_33_square = 4 * (
        alpha_33 * reciprocal_separator + Fraction(1, 33 * 32)
    )
    _require(
        p_gap_33 == Fraction(2741, 36960) > 0,
        "n=33 direct Descartes sign gate failed",
    )
    _require(
        p_radical_33_square - p_gap_33**2
        == Fraction(63719, 1366041600)
        > 0,
        "n=33 direct Descartes square comparison failed",
    )

    alpha_34 = Fraction(1, 34) + Fraction(1, 33)
    q_34_square = alpha_34 / K + Fraction(1, 34 * 33)
    _require(
        q_34_square - alpha_34**2
        == Fraction(51605, 8812188)
        > 0,
        "n=34 physical-minus-root sign gate failed",
    )
    base_34 = Fraction(1, K) + alpha_34
    radical_34_square = 4 * q_34_square
    _require(base_34 == Fraction(1591, 7854) > 0, "unexpected n=34 rational term")
    _require(
        radical_34_square == Fraction(148, 3927) > 0,
        "unexpected n=34 radical square",
    )
    _require(
        base_34**2 - radical_34_square
        == Fraction(206497, 61685316)
        > 0,
        "n=34 kappa positivity comparison failed",
    )
    gap_34 = base_34 - reciprocal_separator
    _require(
        gap_34 == Fraction(15349, 78540) > 0,
        "unexpected n=34 separator gap",
    )
    _require(
        gap_34**2 - radical_34_square
        == Fraction(3113401, 6168531600)
        > 0,
        "n=34 threshold separator comparison failed",
    )
    p_gap_34 = Fraction(1, K) - reciprocal_separator - alpha_34
    p_radical_34_square = 4 * (
        alpha_34 * reciprocal_separator + Fraction(1, 34 * 33)
    )
    _require(
        p_gap_34 == Fraction(5969, 78540) > 0,
        "n=34 direct Descartes sign gate failed",
    )
    _require(
        p_gap_34**2 - p_radical_34_square
        == Fraction(3113401, 6168531600)
        > 0,
        "n=34 direct Descartes square comparison failed",
    )

    _require(len(N33_UPPER_ROWS) == 27, "n=33 proof table edge count failed")
    _require(
        tuple(row[0] for row in N33_UPPER_ROWS) == ordered_adjacent_edges(order_33),
        "n=33 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N33_UPPER_ROWS} == set(formula_edges(33)),
        "n=33 proof table does not equal the parity edge set",
    )
    upper_sum = Fraction(0)
    for edge, expected_square, upper, expected_margin in N33_UPPER_ROWS:
        _require(edge == _edge(*edge), f"n=33 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=33 sine square mismatch at {edge}")
        _require(
            upper**2 - actual_square == expected_margin > 0,
            f"n=33 upper margin failed at {edge}",
        )
        _require(
            0 < actual_square < upper**2
            and 0 < upper <= Fraction(16, 125) < Fraction(3, 20) < 1,
            f"n=33 arcsine domain failed at {edge}",
        )
        upper_sum += upper + Fraction(7, 40) * upper**3

    derivative_factor = (Fraction(1), Fraction(21, 40))
    derivative_identity = _poly_add(
        _poly_multiply(
            _poly_multiply(derivative_factor, derivative_factor),
            (Fraction(1), Fraction(-1)),
        ),
        (Fraction(-1),),
    )
    _require(
        derivative_identity
        == (
            Fraction(0),
            Fraction(1, 20),
            Fraction(-1239, 1600),
            Fraction(-441, 1600),
        ),
        "arcsine derivative-majorant polynomial identity failed",
    )
    endpoint_square = Fraction(3, 20) ** 2
    _require(
        Fraction(80) - 1239 * endpoint_square - 441 * endpoint_square**2
        == Fraction(8303879, 160000)
        > 0,
        "arcsine derivative-majorant endpoint failed",
    )
    _require(
        upper_sum == Fraction(3919372517, 1250000000),
        "unexpected n=33 arcsine upper sum",
    )
    _require(
        Fraction(333, 106) - upper_sum
        == Fraction(398256599, 66250000000)
        > 0,
        "n=33 rational chain upper bridge failed",
    )

    _require(len(N34_LOWER_ROWS) == 28, "n=34 proof table edge count failed")
    _require(
        tuple(row[0] for row in N34_LOWER_ROWS) == ordered_adjacent_edges(order_34),
        "n=34 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N34_LOWER_ROWS} == set(formula_edges(34)),
        "n=34 proof table does not equal the parity edge set",
    )
    lower_sum = Fraction(0)
    for edge, expected_square, lower, expected_margin in N34_LOWER_ROWS:
        _require(edge == _edge(*edge), f"n=34 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=34 sine square mismatch at {edge}")
        _require(
            actual_square - lower**2 == expected_margin > 0,
            f"n=34 lower margin failed at {edge}",
        )
        _require(
            0 < lower and lower**2 < actual_square < 1,
            f"n=34 arcsine domain failed at {edge}",
        )
        lower_sum += lower
    _require(lower_sum == Fraction(641, 200), "unexpected n=34 lower sum")
    _require(
        lower_sum - Fraction(22, 7) == Fraction(87, 1400) > 0,
        "n=34 rational chain lower bridge failed",
    )

    _check_exact_pi_comparisons()


def _load_mpmath() -> None:
    """Load the numerical dependency only for opt-in diagnostics."""
    global mp
    import mpmath as mp


def theta(radius: mp.mpf, a: int, b: int) -> mp.mpf:
    argument = mp.sqrt(mp.mpf(a * b) / ((radius + a) * (radius + b)))
    return 2 * mp.asin(argument)


def chain_value_and_derivative(
    radius: mp.mpf, order: tuple[int, ...]
) -> tuple[mp.mpf, mp.mpf]:
    value = mp.mpf("0")
    derivative = mp.mpf("0")
    for index, a in enumerate(order):
        b = order[(index + 1) % len(order)]
        argument = mp.sqrt(mp.mpf(a * b) / ((radius + a) * (radius + b)))
        value += 2 * mp.asin(argument)
        derivative -= argument * (
            1 / (radius + a) + 1 / (radius + b)
        ) / mp.sqrt(1 - argument * argument)
    return value, derivative


def chain_root(n: int, digits: int) -> mp.mpf:
    with mp.workdps(digits):
        order = shifted_supnick_tour(n)
        target = 2 * mp.pi
        low = mp.mpf("0")
        high = mp.mpf(4 * n * n)
        high_value, _ = chain_value_and_derivative(high, order)
        _require(high_value < target, f"chain root upper bracket failed for n={n}")
        current = mp.mpf(n * n) / 8
        tolerance = mp.power(10, -(digits - 15))

        for _ in range(180):
            value, derivative = chain_value_and_derivative(current, order)
            if value > target:
                low = current
            else:
                high = current
            if high - low <= tolerance * max(1, abs(current)):
                return +(low + high) / 2
            newton = current - (value - target) / derivative
            if not low < newton < high:
                newton = (low + high) / 2
            current = newton
        raise AuditFailure(f"chain root did not converge for n={n}, digits={digits}")


def seam_threshold(n: int) -> mp.mpf | None:
    """Use a rationalized kappa form to reduce diagnostic cancellation."""
    c = mp.mpf(1) / K
    alpha = mp.mpf(1) / n + mp.mpf(1) / (n - 1)
    beta = mp.mpf(1) / (n * (n - 1))
    q = mp.sqrt(alpha * c + beta)
    direct = c + alpha - 2 * q
    root_beta = mp.sqrt(beta)
    p_zero = alpha + 2 * root_beta
    kappa = (c - p_zero) * (c - alpha + 2 * root_beta) / (
        c + alpha + 2 * q
    )
    _require(
        abs(kappa - direct) <= 32 * mp.eps * max(1, abs(kappa), abs(direct)),
        f"direct/rationalized kappa mismatch at n={n}",
    )
    return None if kappa <= 0 else 1 / kappa


def scan(start: int, stop: int, digits: int) -> dict[int, dict[str, mp.mpf | None]]:
    rows: dict[int, dict[str, mp.mpf | None]] = {}
    with mp.workdps(digits):
        for n in range(start, stop + 1):
            root = chain_root(n, digits)
            deficit = (
                theta(root, n, K)
                + theta(root, K, n - 1)
                - theta(root, n, n - 1)
            )
            rows[n] = {"R": +root, "T": seam_threshold(n), "deficit": +deficit}
    return rows


def _sign(value: mp.mpf) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def check_numeric_diagnostics(
    start: int,
    stop: int,
    digits: int,
    stability_digits: int,
) -> tuple[dict[int, dict[str, mp.mpf | None]], mp.mpf, mp.mpf]:
    """Finite numerics, deliberately separate from the exact rational audit."""
    base = scan(start, stop, digits)
    higher = scan(start, stop, stability_digits)
    max_relative_root_delta = mp.mpf("0")
    max_absolute_deficit_delta = mp.mpf("0")

    with mp.workdps(stability_digits):
        for n in range(start, stop + 1):
            base_root = mp.mpf(base[n]["R"])
            high_root = mp.mpf(higher[n]["R"])
            base_deficit = mp.mpf(base[n]["deficit"])
            high_deficit = mp.mpf(higher[n]["deficit"])
            max_relative_root_delta = max(
                max_relative_root_delta,
                abs(base_root - high_root) / max(1, abs(high_root)),
            )
            max_absolute_deficit_delta = max(
                max_absolute_deficit_delta,
                abs(base_deficit - high_deficit),
            )
            _require(
                _sign(base_deficit) == _sign(high_deficit),
                f"precision-dependent diagnostic deficit sign at n={n}",
            )
            expected_sign = 1 if n <= LEFT_ENDPOINT else -1
            _require(
                _sign(high_deficit) == expected_sign,
                f"unexpected diagnostic deficit sign at n={n}: {high_deficit}",
            )
            _require(
                abs(high_deficit) > mp.power(10, -(stability_digits // 2)),
                f"diagnostic deficit is too close to zero at n={n}",
            )
            threshold = higher[n]["T"]
            if n <= 4 * K:
                _require(threshold is None, f"unexpected positive threshold at n={n}")
            else:
                _require(threshold is not None, f"missing positive threshold at n={n}")
                comparison_sign = _sign(high_root - mp.mpf(threshold))
                _require(
                    comparison_sign == -expected_sign,
                    f"diagnostic root/threshold sign mismatch at n={n}",
                )

        for n in range(start + 1, stop + 1):
            _require(
                mp.mpf(higher[n]["R"]) > mp.mpf(higher[n - 1]["R"]),
                f"diagnostic root monotonicity failed at n={n}",
            )
            if n >= 4 * K + 2:
                previous_threshold = higher[n - 1]["T"]
                current_threshold = higher[n]["T"]
                if previous_threshold is not None and current_threshold is not None:
                    _require(
                        mp.mpf(current_threshold) < mp.mpf(previous_threshold),
                        f"diagnostic threshold monotonicity failed at n={n}",
                    )

        tolerance = mp.power(10, -min(30, digits // 2))
        _require(
            max_relative_root_delta < tolerance,
            f"diagnostic root precision stability failed: {max_relative_root_delta}",
        )
        _require(
            max_absolute_deficit_delta < tolerance,
            f"diagnostic deficit precision stability failed: {max_absolute_deficit_delta}",
        )

        separator = mp.mpf(SEPARATOR.numerator) / SEPARATOR.denominator
        for n, expected_sign in ((LEFT_ENDPOINT, -1), (RIGHT_ENDPOINT, 1)):
            if start <= n <= stop:
                closure, _ = chain_value_and_derivative(
                    separator, shifted_supnick_tour(n)
                )
                _require(
                    _sign(closure - 2 * mp.pi) == expected_sign,
                    f"diagnostic R=140 closure sign failed at n={n}",
                )

    return higher, max_relative_root_delta, max_absolute_deficit_delta


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order-stop", type=int, default=250)
    parser.add_argument("--start", type=int, default=MIN_N)
    parser.add_argument("--stop", type=int, default=120)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--stability-digits", type=int, default=100)
    parser.add_argument(
        "--diagnostics",
        action="store_true",
        help="add finite two-precision mpmath diagnostics after exact gates",
    )
    args = parser.parse_args()
    if args.order_stop < RIGHT_ENDPOINT:
        parser.error(f"--order-stop must be at least {RIGHT_ENDPOINT}")
    if args.start < MIN_N or args.stop < args.start:
        parser.error(f"require {MIN_N} <= start <= stop")
    if args.diagnostics:
        if args.digits < 40:
            parser.error("--digits must be at least 40")
        if args.stability_digits <= args.digits:
            parser.error("--stability-digits must exceed --digits")

    check_exact_rational_audit(args.order_stop)
    exact_gate_count = _EXPLICIT_GATE_COUNT
    print("independent_of_production=PASS (no ringmin imports)")
    print(
        "exact_stdlib_fraction_audit=PASS "
        f"explicit_gates={exact_gate_count} optimized_safe=YES"
    )
    print("exact_threshold_domain_and_R140_bridges=PASS n=28,29,33,34")
    print("exact_complete_edge_tables_and_chain_bridges_at_R140=PASS n=33,34")
    print("exact_pi_identities=PASS 333/106<pi<22/7")
    print(f"shifted_order_conventions_and_edge_sets=PASS n={MIN_N}..{args.order_stop}")
    print(
        "theorem_sources=research/RADIUS7_SEAM_ONSET.md+"
        "research/FIXED_K_SUPNICK_SEAM.md"
    )

    if not args.diagnostics:
        print("numerical_diagnostics=SKIPPED (opt in with --diagnostics)")
        print(
            "classification=EXACT_STDLIB_FRACTION_AUDIT; checker is "
            "corroborative only; theorem sources are the two proof notes"
        )
        return 0

    _load_mpmath()
    rows, max_root_delta, max_deficit_delta = check_numeric_diagnostics(
        args.start,
        args.stop,
        args.digits,
        args.stability_digits,
    )
    print(
        "numerical_diagnostics=PASS NUMERICAL_DIAGNOSTIC_ONLY "
        f"n={args.start}..{args.stop} digits={args.digits}/{args.stability_digits}"
    )
    print(
        "diagnostic_precision_stability=PASS "
        f"max_relative_R_delta={mp.nstr(max_root_delta, 8)} "
        f"max_absolute_deficit_delta={mp.nstr(max_deficit_delta, 8)}"
    )
    selected = sorted(
        {
            args.start,
            args.stop,
            MIN_N,
            4 * K,
            4 * K + 1,
            LEFT_ENDPOINT,
            RIGHT_ENDPOINT,
        }.intersection(range(args.start, args.stop + 1))
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"diagnostic n={n:03d} R_7n={mp.nstr(row['R'], 18)} "
            f"T_7n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    print(
        "classification=NUMERICAL_DIAGNOSTIC_ONLY; finite scans are not proof; "
        "theorem sources are the two proof notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
