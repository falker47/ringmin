#!/usr/bin/env python3
"""Independent audit for the exact radius-4 formal Supnick seam onset.

The default path uses only integer and ``Fraction`` arithmetic to audit every
new endpoint inequality and every row of both adjacent-edge tables.  The
optional mpmath path is a separately labeled finite numerical diagnostic; it
is not a premise of the all-n theorem.  This script deliberately does not
import ``ringmin``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

K = 4
MIN_N = K + 2
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
    """The proof-note representative on the consecutive radii 4,...,n."""
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
    """Parity-explicit specialization of the fixed-k formulas at k=4."""
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


N20_UPPER_ROWS = (
    ((4, 19), Fraction(38, 1863), Fraction(18, 125), Fraction(9862, 29109375)),
    ((6, 19), Fraction(19, 644), Fraction(43, 250), Fraction(407, 5031250)),
    ((6, 17), Fraction(51, 1876), Fraction(83, 500), Fraction(43441, 117250000)),
    ((8, 17), Fraction(68, 1943), Fraction(47, 250), Fraction(42087, 121437500)),
    ((8, 15), Fraction(12, 377), Fraction(9, 50), Fraction(537, 942500)),
    ((10, 15), Fraction(1, 26), Fraction(99, 500), Fraction(2413, 3250000)),
    ((10, 13), Fraction(13, 378), Fraction(93, 500), Fraction(9661, 47250000)),
    ((12, 13), Fraction(26, 651), Fraction(1, 5), Fraction(1, 16275)),
    ((11, 12), Fraction(66, 1891), Fraction(47, 250), Fraction(52219, 118187500)),
    ((11, 14), Fraction(77, 1952), Fraction(1, 5), Fraction(27, 48800)),
    ((9, 14), Fraction(63, 1888), Fraction(23, 125), Fraction(14377, 29500000)),
    ((9, 16), Fraction(24, 649), Fraction(97, 500), Fraction(106441, 162250000)),
    ((7, 16), Fraction(56, 1881), Fraction(87, 500), Fraction(237289, 470250000)),
    ((7, 18), Fraction(21, 646), Fraction(91, 500), Fraction(49763, 80750000)),
    ((5, 18), Fraction(9, 374), Fraction(39, 250), Fraction(3177, 11687500)),
    ((5, 20), Fraction(2, 77), Fraction(81, 500), Fraction(5197, 19250000)),
    ((4, 20), Fraction(4, 189), Fraction(73, 500), Fraction(7181, 47250000)),
)


N21_LOWER_ROWS = (
    ((4, 20), Fraction(4, 189), Fraction(7, 50), Fraction(739, 472500)),
    ((6, 20), Fraction(3, 98), Fraction(17, 100), Fraction(839, 490000)),
    ((6, 18), Fraction(27, 952), Fraction(4, 25), Fraction(1643, 595000)),
    ((8, 18), Fraction(18, 493), Fraction(19, 100), Fraction(2027, 4930000)),
    ((8, 16), Fraction(32, 957), Fraction(9, 50), Fraction(2483, 2392500)),
    ((10, 16), Fraction(4, 99), Fraction(1, 5), Fraction(1, 2475)),
    ((10, 14), Fraction(7, 192), Fraction(19, 100), Fraction(43, 120000)),
    ((12, 14), Fraction(21, 496), Fraction(1, 5), Fraction(29, 12400)),
    ((12, 13), Fraction(26, 651), Fraction(19, 100), Fraction(24989, 6510000)),
    ((11, 13), Fraction(143, 3843), Fraction(19, 100), Fraction(42677, 38430000)),
    ((11, 15), Fraction(33, 793), Fraction(1, 5), Fraction(32, 19825)),
    ((9, 15), Fraction(27, 767), Fraction(9, 50), Fraction(5373, 1917500)),
    ((9, 17), Fraction(153, 3953), Fraction(19, 100), Fraction(102967, 39530000)),
    ((7, 17), Fraction(119, 3819), Fraction(17, 100), Fraction(86309, 38190000)),
    ((7, 19), Fraction(7, 207), Fraction(9, 50), Fraction(733, 517500)),
    ((5, 19), Fraction(19, 759), Fraction(3, 20), Fraction(769, 303600)),
    ((5, 21), Fraction(21, 781), Fraction(4, 25), Fraction(629, 488125)),
    ((4, 21), Fraction(14, 639), Fraction(7, 50), Fraction(3689, 1597500)),
)


def check_exact_rational_audit(order_stop: int) -> None:
    """Audit exact transcriptions only; no floating-point call occurs here."""
    check_order_convention(order_stop)
    order_20 = shifted_supnick_tour(20)
    order_21 = shifted_supnick_tour(21)
    _require(
        order_20
        == (4, 19, 6, 17, 8, 15, 10, 13, 12, 11, 14, 9, 16, 7, 18, 5, 20),
        "hard-coded n=20 endpoint order mismatch",
    )
    _require(
        order_21
        == (4, 20, 6, 18, 8, 16, 10, 14, 12, 13, 11, 15, 9, 17, 7, 19, 5, 21),
        "hard-coded n=21 endpoint order mismatch",
    )
    deleted_21 = tuple(value for value in order_21 if value != 21)
    _require(
        not cycle_equivalent(deleted_21, order_20),
        "negative control failed: vertex deletion unexpectedly preserves the tour",
    )

    # Imported fixed-k physical threshold boundary: n=16 has none; n=17 does.
    _require(
        Fraction(4, 16 * 15) - Fraction(29, 240) ** 2
        == Fraction(119, 57600)
        > 0,
        "n=16 no-threshold boundary audit failed",
    )
    _require(
        Fraction(35, 272) ** 2 - Fraction(4, 17 * 16)
        == Fraction(137, 73984)
        > 0,
        "n=17 positive-threshold boundary audit failed",
    )

    # n=20: 0 < kappa_{4,20} < 1/50, hence 50 < T_{4,20}.
    base_20 = Fraction(1, 4) + Fraction(1, 20) + Fraction(1, 19)
    radical_20_square = 4 * Fraction(2 * 20 + K - 1, K * 20 * 19)
    _require(base_20 == Fraction(67, 190) > 0, "unexpected n=20 rational term")
    _require(
        radical_20_square == Fraction(43, 380) > 0,
        "unexpected n=20 radical square",
    )
    _require(
        base_20**2 - radical_20_square == Fraction(101, 9025) > 0,
        "n=20 kappa positivity comparison failed",
    )
    gap_20 = base_20 - Fraction(1, 50)
    _require(gap_20 == Fraction(158, 475) > 0, "unexpected n=20 separator gap")
    _require(
        radical_20_square - gap_20**2 == Fraction(2269, 902500) > 0,
        "n=20 threshold separator comparison failed",
    )

    # n=21: kappa_{4,21} > 1/50 > 0, hence T_{4,21} < 50.
    base_21 = Fraction(1, 4) + Fraction(1, 21) + Fraction(1, 20)
    radical_21_square = 4 * Fraction(2 * 21 + K - 1, K * 21 * 20)
    _require(base_21 == Fraction(73, 210) > 0, "unexpected n=21 rational term")
    _require(
        radical_21_square == Fraction(3, 28) > 0,
        "unexpected n=21 radical square",
    )
    _require(
        base_21**2 - radical_21_square == Fraction(151, 11025) > 0,
        "n=21 kappa positivity comparison failed",
    )
    gap_21 = base_21 - Fraction(1, 50)
    _require(gap_21 == Fraction(172, 525) > 0, "unexpected n=21 separator gap")
    _require(
        gap_21**2 - radical_21_square == Fraction(211, 1102500) > 0,
        "n=21 threshold separator comparison failed",
    )

    radius = Fraction(50)

    # n=20: every upper row is an adjacent edge, in cyclic order.
    _require(len(N20_UPPER_ROWS) == 17, "n=20 proof table edge count failed")
    _require(
        tuple(row[0] for row in N20_UPPER_ROWS) == ordered_adjacent_edges(order_20),
        "n=20 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N20_UPPER_ROWS} == set(formula_edges(20)),
        "n=20 proof table does not equal the parity edge set",
    )
    upper_sum = Fraction(0)
    for edge, expected_square, upper, expected_margin in N20_UPPER_ROWS:
        _require(edge == _edge(*edge), f"n=20 row edge is not normalized: {edge}")
        actual_square = _sine_square(radius, *edge)
        _require(actual_square == expected_square, f"n=20 sine square mismatch at {edge}")
        _require(
            upper**2 - actual_square == expected_margin > 0,
            f"n=20 upper margin failed at {edge}",
        )
        _require(
            0 < actual_square < upper**2 and 0 < upper <= Fraction(1, 5) < Fraction(1, 3),
            f"n=20 arcsine domain failed at {edge}",
        )
        upper_sum += upper + upper**3 / 5

    # For 0<u<=1/3, the derivative estimate used in the proof note is strict.
    _require(
        Fraction(5) - Fraction(21, 9) - Fraction(9, 81)
        == Fraction(23, 9)
        > 0,
        "arcsine derivative-bound endpoint failed",
    )
    _require(
        upper_sum == Fraction(47493609, 15625000),
        "unexpected n=20 arcsine upper sum",
    )
    _require(
        Fraction(76, 25) - upper_sum == Fraction(6391, 15625000) > 0,
        "n=20 rational chain upper bridge failed",
    )

    # Exact radical gates for 76/25 < 4*sqrt(2-sqrt(2)) < pi.
    sqrt_two_upper = Fraction(889, 625)
    _require(
        0 < sqrt_two_upper < 2,
        "regular-octagon pre-square sign gate failed",
    )
    _require(
        sqrt_two_upper**2 - 2 == Fraction(9071, 390625) > 0,
        "regular-octagon sqrt(2) upper comparison failed",
    )
    _require(
        2 - sqrt_two_upper == Fraction(361, 625) == Fraction(19, 25) ** 2,
        "regular-octagon nested-radical comparison failed",
    )
    _require(Fraction(19, 25) > 0, "regular-octagon final sign gate failed")

    # n=21: every lower row is an adjacent edge, in cyclic order.
    _require(len(N21_LOWER_ROWS) == 18, "n=21 proof table edge count failed")
    _require(
        tuple(row[0] for row in N21_LOWER_ROWS) == ordered_adjacent_edges(order_21),
        "n=21 proof table is not in complete cyclic-edge order",
    )
    _require(
        {row[0] for row in N21_LOWER_ROWS} == set(formula_edges(21)),
        "n=21 proof table does not equal the parity edge set",
    )
    lower_sum = Fraction(0)
    for edge, expected_square, lower, expected_margin in N21_LOWER_ROWS:
        _require(edge == _edge(*edge), f"n=21 row edge is not normalized: {edge}")
        actual_square = _sine_square(radius, *edge)
        _require(actual_square == expected_square, f"n=21 sine square mismatch at {edge}")
        _require(
            actual_square - lower**2 == expected_margin > 0,
            f"n=21 lower margin failed at {edge}",
        )
        _require(
            0 < lower and lower**2 < actual_square < 1,
            f"n=21 arcsine domain failed at {edge}",
        )
        lower_sum += lower
    _require(lower_sum == Fraction(159, 50), "unexpected n=21 lower sum")
    _require(
        lower_sum - Fraction(22, 7) == Fraction(13, 350) > 0,
        "n=21 rational chain lower bridge failed",
    )


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
            expected_sign = 1 if n <= 20 else -1
            _require(
                _sign(high_deficit) == expected_sign,
                f"unexpected diagnostic deficit sign at n={n}: {high_deficit}",
            )
            _require(
                abs(high_deficit) > mp.power(10, -(stability_digits // 2)),
                f"diagnostic deficit is too close to zero at n={n}",
            )
            threshold = higher[n]["T"]
            if n <= 16:
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
            if n >= 18:
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

        for n, expected_sign in ((20, -1), (21, 1)):
            if start <= n <= stop:
                closure, _ = chain_value_and_derivative(mp.mpf(50), shifted_supnick_tour(n))
                _require(
                    _sign(closure - 2 * mp.pi) == expected_sign,
                    f"diagnostic R=50 closure sign failed at n={n}",
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
    if args.order_stop < 21:
        parser.error("--order-stop must be at least 21")
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
        "exact_fraction_audit=PASS "
        f"explicit_gates={exact_gate_count} optimized_safe=YES"
    )
    print("exact_threshold_domain_and_R50_bridges=PASS n=16,17,20,21")
    print("exact_complete_edge_tables_and_chain_bridges_at_R50=PASS n=20,21")
    print(f"shifted_order_conventions_and_edge_sets=PASS n={MIN_N}..{args.order_stop}")
    print(
        "theorem_sources=research/RADIUS4_SEAM_ONSET.md+"
        "research/FIXED_K_SUPNICK_SEAM.md"
    )

    if not args.diagnostics:
        print("numerical_diagnostics=SKIPPED (opt in with --diagnostics)")
        print(
            "classification=EXACT_FRACTION_AUDIT; checker is corroborative only; "
            "theorem sources are the two proof notes"
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
        {args.start, args.stop, 6, 16, 17, 20, 21}.intersection(
            range(args.start, args.stop + 1)
        )
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"diagnostic n={n:03d} R_4n={mp.nstr(row['R'], 18)} "
            f"T_4n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    print(
        "classification=NUMERICAL_DIAGNOSTIC_ONLY; finite scans are not proof; "
        "theorem sources are the two proof notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
