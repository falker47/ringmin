#!/usr/bin/env python3
"""Independent audit for the exact radius-5 formal Supnick seam onset.

The default path uses only Python's standard library and exact ``Fraction``
arithmetic.  It audits every new endpoint inequality, every row of both
adjacent-edge tables, and polynomial identities supporting the exact
comparisons with pi.  The optional mpmath path is a separately labeled finite
numerical diagnostic; it is not a premise of the all-n theorem.  This script
deliberately does not import ``ringmin``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

K = 5
MIN_N = K + 2
LEFT_ENDPOINT = 24
RIGHT_ENDPOINT = 25
SEPARATOR = Fraction(75)
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
    """The proof-note representative on the consecutive radii 5,...,n."""
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
    """Parity-explicit specialization of the fixed-k formulas at k=5."""
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


N24_UPPER_ROWS = (
    ((5, 23), Fraction(23, 1568), Fraction(61, 500), Fraction(5283, 24500000)),
    ((7, 23), Fraction(23, 1148), Fraction(71, 500), Fraction(9267, 71750000)),
    ((7, 21), Fraction(49, 2624), Fraction(137, 1000), Fraction(61, 640625)),
    ((9, 21), Fraction(3, 128), Fraction(77, 500), Fraction(557, 2000000)),
    ((9, 19), Fraction(57, 2632), Fraction(37, 250), Fraction(10177, 41125000)),
    (
        (11, 19),
        Fraction(209, 8084),
        Fraction(161, 1000),
        Fraction(136341, 2021000000),
    ),
    ((11, 17), Fraction(187, 7912), Fraction(77, 500), Fraction(20031, 247250000)),
    ((13, 17), Fraction(221, 8096), Fraction(83, 500), Fraction(32709, 126500000)),
    ((13, 15), Fraction(13, 528), Fraction(157, 1000), Fraction(917, 33000000)),
    ((14, 15), Fraction(7, 267), Fraction(81, 500), Fraction(1787, 66750000)),
    (
        (14, 16),
        Fraction(32, 1157),
        Fraction(167, 1000),
        Fraction(267573, 1157000000),
    ),
    ((12, 16), Fraction(64, 2639), Fraction(39, 250), Fraction(13919, 164937500)),
    ((12, 18), Fraction(24, 899), Fraction(41, 250), Fraction(11219, 56187500)),
    ((10, 18), Fraction(12, 527), Fraction(151, 1000), Fraction(16127, 527000000)),
    ((10, 20), Fraction(8, 323), Fraction(79, 500), Fraction(15843, 80750000)),
    (
        (8, 20),
        Fraction(32, 1577),
        Fraction(143, 1000),
        Fraction(248073, 1577000000),
    ),
    ((8, 22), Fraction(176, 8051), Fraction(37, 250), Fraction(21819, 503187500)),
    ((6, 22), Fraction(44, 2619), Fraction(13, 100), Fraction(2611, 26190000)),
    ((6, 24), Fraction(16, 891), Fraction(27, 200), Fraction(9539, 35640000)),
    ((5, 24), Fraction(1, 66), Fraction(31, 250), Fraction(463, 2062500)),
)


N25_LOWER_ROWS = (
    ((5, 24), Fraction(1, 66), Fraction(3, 25), Fraction(31, 41250)),
    ((7, 24), Fraction(28, 1353), Fraction(7, 50), Fraction(3703, 3382500)),
    ((7, 22), Fraction(77, 3977), Fraction(27, 200), Fraction(180767, 159080000)),
    ((9, 22), Fraction(33, 1358), Fraction(31, 200), Fraction(7481, 27160000)),
    ((9, 20), Fraction(3, 133), Fraction(3, 20), Fraction(3, 53200)),
    ((11, 20), Fraction(22, 817), Fraction(4, 25), Fraction(678, 510625)),
    ((11, 18), Fraction(33, 1333), Fraction(31, 200), Fraction(38987, 53320000)),
    ((13, 18), Fraction(39, 1364), Fraction(33, 200), Fraction(18651, 13640000)),
    ((13, 16), Fraction(2, 77), Fraction(4, 25), Fraction(18, 48125)),
    ((15, 16), Fraction(8, 273), Fraction(17, 100), Fraction(1103, 2730000)),
    ((14, 15), Fraction(7, 267), Fraction(4, 25), Fraction(103, 166875)),
    ((14, 17), Fraction(119, 4094), Fraction(17, 100), Fraction(3417, 20470000)),
    ((12, 17), Fraction(17, 667), Fraction(31, 200), Fraction(39013, 26680000)),
    ((12, 19), Fraction(38, 1363), Fraction(33, 200), Fraction(35693, 54520000)),
    ((10, 19), Fraction(19, 799), Fraction(3, 20), Fraction(409, 319600)),
    ((10, 21), Fraction(7, 272), Fraction(4, 25), Fraction(23, 170000)),
    ((8, 21), Fraction(7, 332), Fraction(29, 200), Fraction(197, 3320000)),
    ((8, 23), Fraction(92, 4067), Fraction(3, 20), Fraction(197, 1626800)),
    ((6, 23), Fraction(23, 1323), Fraction(13, 100), Fraction(6413, 13230000)),
    ((6, 25), Fraction(1, 54), Fraction(27, 200), Fraction(317, 1080000)),
    ((5, 25), Fraction(1, 64), Fraction(3, 25), Fraction(49, 40000)),
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
    """Audit the rational polynomial identities behind 3<pi<22/7."""
    denominator = (Fraction(1), Fraction(0), Fraction(1))

    alternating = tuple(
        Fraction((-1) ** (index // 2)) if index % 2 == 0 else Fraction(0)
        for index in range(15)
    )
    product = _poly_multiply(denominator, alternating)
    remainder = _poly_add((Fraction(1),), tuple(-value for value in product))
    expected_remainder = tuple(
        Fraction(1) if index == 16 else Fraction(0) for index in range(17)
    )
    _require(
        remainder == expected_remainder,
        "finite geometric identity for the pi lower bound failed",
    )
    alternating_integral = _poly_integral_zero_one(alternating)
    _require(
        alternating_integral == Fraction(33976, 45045),
        "unexpected integrated polynomial for the pi lower bound",
    )
    _require(
        alternating_integral - Fraction(3, 4)
        == Fraction(769, 180180)
        > 0,
        "exact 3<pi rational bridge failed",
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
    order_24 = shifted_supnick_tour(LEFT_ENDPOINT)
    order_25 = shifted_supnick_tour(RIGHT_ENDPOINT)
    _require(
        order_24
        == (5, 23, 7, 21, 9, 19, 11, 17, 13, 15, 14, 16, 12, 18, 10, 20, 8, 22, 6, 24),
        "hard-coded n=24 endpoint order mismatch",
    )
    _require(
        order_25
        == (5, 24, 7, 22, 9, 20, 11, 18, 13, 16, 15, 14, 17, 12, 19, 10, 21, 8, 23, 6, 25),
        "hard-coded n=25 endpoint order mismatch",
    )
    deleted_25 = tuple(value for value in order_25 if value != RIGHT_ENDPOINT)
    _require(
        not cycle_equivalent(deleted_25, order_24),
        "negative control failed: vertex deletion unexpectedly preserves the tour",
    )

    # Imported fixed-k threshold boundary: n=20 has none; n=21 does.
    boundary_gap_20 = Fraction(1, K) - Fraction(1, 20) - Fraction(1, 19)
    _require(
        boundary_gap_20 == Fraction(37, 380) > 0,
        "n=20 threshold-boundary sign gate failed",
    )
    _require(
        Fraction(4, 20 * 19) - boundary_gap_20**2
        == Fraction(151, 144400)
        > 0,
        "n=20 no-threshold boundary square audit failed",
    )
    boundary_gap_21 = Fraction(1, K) - Fraction(1, 21) - Fraction(1, 20)
    _require(
        boundary_gap_21 == Fraction(43, 420) > 0,
        "n=21 threshold-boundary sign gate failed",
    )
    _require(
        boundary_gap_21**2 - Fraction(4, 21 * 20)
        == Fraction(169, 176400)
        > 0,
        "n=21 positive-threshold boundary square audit failed",
    )

    # n=24: 0 < kappa_{5,24} < 1/75, hence 75 < T_{5,24}.
    base_24 = Fraction(1, K) + Fraction(1, 24) + Fraction(1, 23)
    radical_24_square = 4 * Fraction(2 * 24 + K - 1, K * 24 * 23)
    _require(base_24 == Fraction(787, 2760) > 0, "unexpected n=24 rational term")
    _require(
        radical_24_square == Fraction(26, 345) > 0,
        "unexpected n=24 radical square",
    )
    _require(
        base_24**2 - radical_24_square == Fraction(45289, 7617600) > 0,
        "n=24 kappa positivity comparison failed",
    )
    gap_24 = base_24 - Fraction(1, 75)
    _require(gap_24 == Fraction(3751, 13800) > 0, "unexpected n=24 separator gap")
    _require(
        radical_24_square - gap_24**2
        == Fraction(281999, 190440000)
        > 0,
        "n=24 threshold separator comparison failed",
    )

    # n=25: kappa_{5,25} > 1/75 > 0, hence T_{5,25} < 75.
    base_25 = Fraction(1, K) + Fraction(1, 25) + Fraction(1, 24)
    radical_25_square = 4 * Fraction(2 * 25 + K - 1, K * 25 * 24)
    _require(base_25 == Fraction(169, 600) > 0, "unexpected n=25 rational term")
    _require(
        radical_25_square == Fraction(9, 125) > 0,
        "unexpected n=25 radical square",
    )
    _require(
        base_25**2 - radical_25_square == Fraction(2641, 360000) > 0,
        "n=25 kappa positivity comparison failed",
    )
    gap_25 = base_25 - Fraction(1, 75)
    _require(gap_25 == Fraction(161, 600) > 0, "unexpected n=25 separator gap")
    _require(
        gap_25**2 - radical_25_square == Fraction(1, 360000) > 0,
        "n=25 threshold separator comparison failed",
    )

    # n=24: every upper row is an adjacent edge, in cyclic order.
    _require(len(N24_UPPER_ROWS) == 20, "n=24 proof table edge count failed")
    _require(
        tuple(row[0] for row in N24_UPPER_ROWS) == ordered_adjacent_edges(order_24),
        "n=24 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N24_UPPER_ROWS} == set(formula_edges(24)),
        "n=24 proof table does not equal the parity edge set",
    )
    upper_sum = Fraction(0)
    for edge, expected_square, upper, expected_margin in N24_UPPER_ROWS:
        _require(edge == _edge(*edge), f"n=24 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=24 sine square mismatch at {edge}")
        _require(
            upper**2 - actual_square == expected_margin > 0,
            f"n=24 upper margin failed at {edge}",
        )
        _require(
            0 < actual_square < upper**2
            and 0 < upper <= Fraction(167, 1000) < Fraction(1, 3),
            f"n=24 arcsine domain failed at {edge}",
        )
        upper_sum += upper + upper**3 / 5

    _require(
        Fraction(5) - Fraction(21, 9) - Fraction(9, 81)
        == Fraction(23, 9)
        > 0,
        "arcsine derivative-bound endpoint failed",
    )
    _require(
        upper_sum == Fraction(14962647891, 5000000000),
        "unexpected n=24 arcsine upper sum",
    )
    _require(
        Fraction(3) - upper_sum == Fraction(37352109, 5000000000) > 0,
        "n=24 rational chain upper bridge failed",
    )

    # n=25: every lower row is an adjacent edge, in cyclic order.
    _require(len(N25_LOWER_ROWS) == 21, "n=25 proof table edge count failed")
    _require(
        tuple(row[0] for row in N25_LOWER_ROWS) == ordered_adjacent_edges(order_25),
        "n=25 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N25_LOWER_ROWS} == set(formula_edges(25)),
        "n=25 proof table does not equal the parity edge set",
    )
    lower_sum = Fraction(0)
    for edge, expected_square, lower, expected_margin in N25_LOWER_ROWS:
        _require(edge == _edge(*edge), f"n=25 row edge is not normalized: {edge}")
        actual_square = _sine_square(SEPARATOR, *edge)
        _require(actual_square == expected_square, f"n=25 sine square mismatch at {edge}")
        _require(
            actual_square - lower**2 == expected_margin > 0,
            f"n=25 lower margin failed at {edge}",
        )
        _require(
            0 < lower and lower**2 < actual_square < 1,
            f"n=25 arcsine domain failed at {edge}",
        )
        lower_sum += lower
    _require(lower_sum == Fraction(63, 20), "unexpected n=25 lower sum")
    _require(
        lower_sum - Fraction(22, 7) == Fraction(1, 140) > 0,
        "n=25 rational chain lower bridge failed",
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

        for n, expected_sign in ((LEFT_ENDPOINT, -1), (RIGHT_ENDPOINT, 1)):
            if start <= n <= stop:
                closure, _ = chain_value_and_derivative(
                    mp.mpf(SEPARATOR.numerator) / SEPARATOR.denominator,
                    shifted_supnick_tour(n),
                )
                _require(
                    _sign(closure - 2 * mp.pi) == expected_sign,
                    f"diagnostic R=75 closure sign failed at n={n}",
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
    print("exact_threshold_domain_and_R75_bridges=PASS n=20,21,24,25")
    print("exact_complete_edge_tables_and_chain_bridges_at_R75=PASS n=24,25")
    print("exact_pi_polynomial_identities=PASS 3<pi<22/7")
    print(f"shifted_order_conventions_and_edge_sets=PASS n={MIN_N}..{args.order_stop}")
    print(
        "theorem_sources=research/RADIUS5_SEAM_ONSET.md+"
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
        {args.start, args.stop, MIN_N, 4 * K, 4 * K + 1, LEFT_ENDPOINT, RIGHT_ENDPOINT}.intersection(
            range(args.start, args.stop + 1)
        )
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"diagnostic n={n:03d} R_5n={mp.nstr(row['R'], 18)} "
            f"T_5n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    print(
        "classification=NUMERICAL_DIAGNOSTIC_ONLY; finite scans are not proof; "
        "theorem sources are the two proof notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
