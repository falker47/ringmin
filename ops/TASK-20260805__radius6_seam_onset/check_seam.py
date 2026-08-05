#!/usr/bin/env python3
"""Independent audit for the exact radius-6 formal Supnick seam onset.

The default path uses only Python's standard library and exact ``Fraction``
arithmetic. It audits every new endpoint inequality, every row of both
adjacent-edge tables, and the exact comparisons with pi. The optional mpmath
path is a separately labeled finite numerical diagnostic; it is not a premise
of the all-n theorem. This script deliberately does not import ``ringmin``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

K = 6
MIN_N = K + 2
LEFT_ENDPOINT = 29
RIGHT_ENDPOINT = 30
SEPARATOR = Fraction(211, 2)
_EXPLICIT_GATE_COUNT = 0


class AuditFailure(RuntimeError):
    """An explicit audit gate failed."""


def _require(condition: bool, message: str) -> None:
    """Raise explicitly so gates remain active under ``python -O``."""
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
    """The proof-note representative on the consecutive radii 6,...,n."""
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
    """Parity-explicit specialization of the fixed-k formulas at k=6."""
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


N29_UPPER_ROWS = (
    ((6, 28), Fraction(224, 19847), Fraction(1063, 10000), Fraction(26494743, 1984700000000)),
    ((8, 28), Fraction(896, 60609), Fraction(76, 625), Fraction(77584, 23675390625)),
    ((8, 26), Fraction(832, 59701), Fraction(1181, 10000), Fraction(68626461, 5970100000000)),
    ((10, 26), Fraction(1040, 60753), Fraction(1309, 10000), Fraction(99111193, 6075300000000)),
    ((10, 24), Fraction(320, 19943), Fraction(1267, 10000), Fraction(14278527, 1994300000000)),
    ((12, 24), Fraction(1152, 60865), Fraction(86, 625), Fraction(31508, 4755078125)),
    ((12, 22), Fraction(352, 19975), Fraction(83, 625), Fraction(4311, 312109375)),
    ((14, 22), Fraction(1232, 60945), Fraction(711, 5000), Fraction(1795469, 304725000000)),
    ((14, 20), Fraction(1120, 59989), Fraction(1367, 10000), Fraction(100784421, 5998900000000)),
    ((16, 20), Fraction(1280, 60993), Fraction(1449, 10000), Fraction(60963793, 6099300000000)),
    ((16, 18), Fraction(128, 6669), Fraction(693, 5000), Fraction(2780581, 166725000000)),
    ((17, 18), Fraction(1224, 60515), Fraction(1423, 10000), Fraction(27715687, 1210300000000)),
    ((17, 19), Fraction(1292, 61005), Fraction(91, 625), Fraction(98981, 4766015625)),
    ((15, 19), Fraction(380, 20003), Fraction(1379, 10000), Fraction(38524923, 2000300000000)),
    ((15, 21), Fraction(1260, 60973), Fraction(719, 5000), Fraction(20663053, 1524325000000)),
    ((13, 21), Fraction(364, 19987), Fraction(27, 200), Fraction(10523, 799480000)),
    ((13, 23), Fraction(1196, 60909), Fraction(701, 5000), Fraction(30743509, 1522725000000)),
    ((11, 23), Fraction(1012, 59881), Fraction(1301, 10000), Fraction(154640481, 5988100000000)),
    ((11, 25), Fraction(1100, 60813), Fraction(269, 2000), Fraction(489493, 243252000000)),
    ((9, 25), Fraction(100, 6641), Fraction(307, 2500), Fraction(907609, 41506250000)),
    ((9, 27), Fraction(972, 60685), Fraction(633, 5000), Fraction(3162393, 303425000000)),
    ((7, 27), Fraction(84, 6625), Fraction(1127, 10000), Fraction(116837, 5300000000)),
    ((7, 29), Fraction(812, 60525), Fraction(1159, 10000), Fraction(4083301, 242100000000)),
    ((6, 29), Fraction(696, 59987), Fraction(539, 5000), Fraction(27483227, 1499675000000)),
)


N30_LOWER_ROWS = (
    ((6, 29), Fraction(696, 59987), Fraction(1, 10), Fraction(9613, 5998700)),
    ((8, 29), Fraction(928, 61063), Fraction(3, 25), Fraction(30433, 38164375)),
    ((8, 27), Fraction(864, 60155), Fraction(11, 100), Fraction(272249, 120310000)),
    ((10, 27), Fraction(72, 4081), Fraction(13, 100), Fraction(30311, 40810000)),
    ((10, 25), Fraction(1000, 60291), Fraction(3, 25), Fraction(82381, 37681875)),
    ((12, 25), Fraction(80, 4089), Fraction(13, 100), Fraction(108959, 40890000)),
    ((12, 23), Fraction(1104, 60395), Fraction(13, 100), Fraction(166649, 120790000)),
    ((14, 23), Fraction(1288, 61423), Fraction(7, 50), Fraction(210273, 153557500)),
    ((14, 21), Fraction(1176, 60467), Fraction(13, 100), Fraction(1541077, 604670000)),
    ((16, 21), Fraction(448, 20493), Fraction(7, 50), Fraction(115843, 51232500)),
    ((16, 19), Fraction(1216, 60507), Fraction(7, 50), Fraction(75157, 151267500)),
    ((18, 19), Fraction(24, 1079), Fraction(7, 50), Fraction(7129, 2697500)),
    ((17, 18), Fraction(1224, 60515), Fraction(7, 50), Fraction(18953, 30257500)),
    ((17, 20), Fraction(272, 12299), Fraction(7, 50), Fraction(77349, 30747500)),
    ((15, 20), Fraction(1200, 60491), Fraction(7, 50), Fraction(35941, 151227500)),
    ((15, 22), Fraction(88, 4097), Fraction(7, 50), Fraction(19247, 10242500)),
    ((13, 22), Fraction(1144, 60435), Fraction(13, 100), Fraction(245297, 120870000)),
    ((13, 24), Fraction(416, 20461), Fraction(7, 50), Fraction(37411, 51152500)),
    ((11, 24), Fraction(1056, 60347), Fraction(13, 100), Fraction(361357, 603470000)),
    ((11, 26), Fraction(1144, 61279), Fraction(13, 100), Fraction(1083849, 612790000)),
    ((9, 26), Fraction(936, 60227), Fraction(3, 25), Fraction(42957, 37641875)),
    ((9, 28), Fraction(336, 20381), Fraction(3, 25), Fraction(26571, 12738125)),
    ((7, 28), Fraction(784, 60075), Fraction(11, 100), Fraction(22837, 24030000)),
    ((7, 30), Fraction(56, 4065), Fraction(11, 100), Fraction(13627, 8130000)),
    ((6, 30), Fraction(720, 60433), Fraction(1, 10), Fraction(11567, 6043300)),
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
    """Audit the exact Machin lower bound and the classical 22/7 upper bound."""
    denominator = (Fraction(1), Fraction(0), Fraction(1))

    # For a=atan(1/5), the integrated polynomial is a strict lower bound:
    # 1/(1+x^2) > 1-x^2+x^4-x^6. The remainder is x^8/(1+x^2).
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

    # Exact tangent identities plus sign gates audit the pi/4 branch of
    # 4*atan(1/5)-atan(1/239).
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
    _require(
        tan_difference == 1,
        "Machin tangent-subtraction identity failed",
    )

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

    # x^4(1-x)^4/(1+x^2) integrates to 22/7-pi and is positive on (0,1).
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
    order_29 = shifted_supnick_tour(LEFT_ENDPOINT)
    order_30 = shifted_supnick_tour(RIGHT_ENDPOINT)
    _require(
        order_29
        == (
            6, 28, 8, 26, 10, 24, 12, 22, 14, 20, 16, 18,
            17, 19, 15, 21, 13, 23, 11, 25, 9, 27, 7, 29,
        ),
        "hard-coded n=29 endpoint order mismatch",
    )
    _require(
        order_30
        == (
            6, 29, 8, 27, 10, 25, 12, 23, 14, 21, 16, 19, 18,
            17, 20, 15, 22, 13, 24, 11, 26, 9, 28, 7, 30,
        ),
        "hard-coded n=30 endpoint order mismatch",
    )
    deleted_30 = tuple(value for value in order_30 if value != RIGHT_ENDPOINT)
    _require(
        not cycle_equivalent(deleted_30, order_29),
        "negative control failed: vertex deletion unexpectedly preserves the tour",
    )

    # Imported fixed-k threshold boundary: n=24 has none; n=25 does.
    boundary_gap_24 = Fraction(1, K) - Fraction(1, 24) - Fraction(1, 23)
    _require(
        boundary_gap_24 == Fraction(15, 184) > 0,
        "n=24 threshold-boundary sign gate failed",
    )
    _require(
        Fraction(4, 24 * 23) - boundary_gap_24**2
        == Fraction(61, 101568)
        > 0,
        "n=24 no-threshold boundary square audit failed",
    )
    boundary_gap_25 = Fraction(1, K) - Fraction(1, 25) - Fraction(1, 24)
    _require(
        boundary_gap_25 == Fraction(17, 200) > 0,
        "n=25 threshold-boundary sign gate failed",
    )
    _require(
        boundary_gap_25**2 - Fraction(4, 25 * 24)
        == Fraction(67, 120000)
        > 0,
        "n=25 positive-threshold boundary square audit failed",
    )

    reciprocal_separator = Fraction(1, 1) / SEPARATOR
    _require(
        reciprocal_separator == Fraction(2, 211) > 0,
        "unexpected reciprocal separator",
    )

    # n=29: 0 < kappa_{6,29} < 2/211, hence 211/2 < T_{6,29}.
    base_29 = Fraction(1, K) + Fraction(1, 29) + Fraction(1, 28)
    radical_29_square = 4 * Fraction(2 * 29 + K - 1, K * 29 * 28)
    _require(base_29 == Fraction(577, 2436) > 0, "unexpected n=29 rational term")
    _require(
        radical_29_square == Fraction(3, 58) > 0,
        "unexpected n=29 radical square",
    )
    _require(
        base_29**2 - radical_29_square == Fraction(25993, 5934096) > 0,
        "n=29 kappa positivity comparison failed",
    )
    gap_29 = base_29 - reciprocal_separator
    _require(
        gap_29 == Fraction(116875, 513996) > 0,
        "unexpected n=29 separator gap",
    )
    _require(
        radical_29_square - gap_29**2
        == Fraction(5332031, 264191888016)
        > 0,
        "n=29 threshold separator comparison failed",
    )

    # n=30: kappa_{6,30} > 2/211 > 0, hence T_{6,30} < 211/2.
    base_30 = Fraction(1, K) + Fraction(1, 30) + Fraction(1, 29)
    radical_30_square = 4 * Fraction(2 * 30 + K - 1, K * 30 * 29)
    _require(base_30 == Fraction(34, 145) > 0, "unexpected n=30 rational term")
    _require(
        radical_30_square == Fraction(13, 261) > 0,
        "unexpected n=30 radical square",
    )
    _require(
        base_30**2 - radical_30_square == Fraction(979, 189225) > 0,
        "n=30 kappa positivity comparison failed",
    )
    gap_30 = base_30 - reciprocal_separator
    _require(
        gap_30 == Fraction(6884, 30595) > 0,
        "unexpected n=30 separator gap",
    )
    _require(
        gap_30**2 - radical_30_square
        == Fraction(6894679, 8424486225)
        > 0,
        "n=30 threshold separator comparison failed",
    )

    # n=29: every upper row is an adjacent edge, in cyclic order.
    _require(len(N29_UPPER_ROWS) == 24, "n=29 proof table edge count failed")
    _require(
        tuple(row[0] for row in N29_UPPER_ROWS) == ordered_adjacent_edges(order_29),
        "n=29 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N29_UPPER_ROWS} == set(formula_edges(29)),
        "n=29 proof table does not equal the parity edge set",
    )
    upper_sum = Fraction(0)
    for edge, expected_square, upper, expected_margin in N29_UPPER_ROWS:
        _require(edge == _edge(*edge), f"n=29 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=29 sine square mismatch at {edge}")
        _require(
            upper**2 - actual_square == expected_margin > 0,
            f"n=29 upper margin failed at {edge}",
        )
        _require(
            0 < actual_square < upper**2
            and 0 < upper <= Fraction(91, 625) < Fraction(3, 20) < 1,
            f"n=29 arcsine domain failed at {edge}",
        )
        upper_sum += upper + Fraction(7, 40) * upper**3

    # For 0<u<=3/20, this exact derivative majorant is strict.
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
        upper_sum == Fraction(12564579832327, 4000000000000),
        "unexpected n=29 arcsine upper sum",
    )
    _require(
        Fraction(333, 106) - upper_sum
        == Fraction(77268886669, 212000000000000)
        > 0,
        "n=29 rational chain upper bridge failed",
    )

    # n=30: every lower row is an adjacent edge, in cyclic order.
    _require(len(N30_LOWER_ROWS) == 25, "n=30 proof table edge count failed")
    _require(
        tuple(row[0] for row in N30_LOWER_ROWS) == ordered_adjacent_edges(order_30),
        "n=30 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N30_LOWER_ROWS} == set(formula_edges(30)),
        "n=30 proof table does not equal the parity edge set",
    )
    lower_sum = Fraction(0)
    for edge, expected_square, lower, expected_margin in N30_LOWER_ROWS:
        _require(edge == _edge(*edge), f"n=30 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=30 sine square mismatch at {edge}")
        _require(
            actual_square - lower**2 == expected_margin > 0,
            f"n=30 lower margin failed at {edge}",
        )
        _require(
            0 < lower and lower**2 < actual_square < 1,
            f"n=30 arcsine domain failed at {edge}",
        )
        lower_sum += lower
    _require(lower_sum == Fraction(159, 50), "unexpected n=30 lower sum")
    _require(
        lower_sum - Fraction(22, 7) == Fraction(13, 350) > 0,
        "n=30 rational chain lower bridge failed",
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
    kappa = (c - p_zero) * (c - alpha + 2 * root_beta) / (c + alpha + 2 * q)
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
                    f"diagnostic R=211/2 closure sign failed at n={n}",
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
    print("exact_threshold_domain_and_R211over2_bridges=PASS n=24,25,29,30")
    print("exact_complete_edge_tables_and_chain_bridges_at_R211over2=PASS n=29,30")
    print("exact_pi_identities=PASS 333/106<pi<22/7")
    print(f"shifted_order_conventions_and_edge_sets=PASS n={MIN_N}..{args.order_stop}")
    print(
        "theorem_sources=research/RADIUS6_SEAM_ONSET.md+"
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
            f"diagnostic n={n:03d} R_6n={mp.nstr(row['R'], 18)} "
            f"T_6n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    print(
        "classification=NUMERICAL_DIAGNOSTIC_ONLY; finite scans are not proof; "
        "theorem sources are the two proof notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
