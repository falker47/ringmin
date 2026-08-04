#!/usr/bin/env python3
"""Independent audit for the exact radius-3 Supnick seam onset.

The exact layer uses only integer and ``Fraction`` arithmetic to check every
new bridge in the proof note. The optional mpmath layer is a separately
labeled finite diagnostic; it is not a premise of the all-n theorem. This
script deliberately does not import ``ringmin``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

_EXPLICIT_GATE_COUNT = 0


def _require(condition: bool, message: str) -> None:
    """Raise explicitly so audit gates remain active under ``python -O``."""
    global _EXPLICIT_GATE_COUNT
    _EXPLICIT_GATE_COUNT += 1
    if not condition:
        raise AssertionError(message)


def _append_index(
    target: list[int], used: set[int], index: int, size: int
) -> None:
    if not 1 <= index <= size:
        raise AssertionError(f"Supnick index outside 1..{size}: {index}")
    if index in used:
        raise AssertionError(f"duplicate Supnick index: {index}")
    used.add(index)
    target.append(index)


def shifted_supnick_tour(n: int) -> tuple[int, ...]:
    """Proof-note representative on the consecutive radii 3,...,n."""
    if n < 5:
        raise ValueError(f"n must be at least 5, got {n}")
    size = n - 2
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

    if used != set(range(1, size)):
        raise AssertionError(
            f"shifted Supnick construction missed ranks for n={n}: {used}"
        )
    ranks = first + list(reversed(second)) + [size]
    return tuple(rank + 2 for rank in ranks)


def shifted_interleave_tour(n: int) -> tuple[int, ...]:
    """Independent production-style interleave construction."""
    if n < 5:
        raise ValueError(f"n must be at least 5, got {n}")
    size = n - 2
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
    if used != set(range(1, size + 1)):
        raise AssertionError(
            f"shifted interleave construction missed ranks for n={n}: {used}"
        )
    return tuple(rank + 2 for rank in arm_a + list(reversed(arm_b)))


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


def adjacent_edges(order: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        _edge(value, order[(index + 1) % len(order)])
        for index, value in enumerate(order)
    )


def formula_edges(n: int) -> frozenset[tuple[int, int]]:
    """Parity-explicit specialization of the fixed-k edge formulas at k=3."""
    if n < 5:
        raise ValueError(f"n must be at least 5, got {n}")
    size = n - 2
    if size % 2 == 0:
        half = size // 2
        edges = {_edge(3, n), _edge(3 + half - 1, 3 + half)}
        edges.update(_edge(i, n + 2 - i) for i in range(3, 3 + half - 1))
        edges.update(_edge(i, n + 4 - i) for i in range(4, 3 + half))
    else:
        half = (size - 1) // 2
        edges = {_edge(3, n)}
        edges.update(_edge(i, n + 2 - i) for i in range(3, 3 + half))
        edges.update(_edge(i, n + 4 - i) for i in range(4, 4 + half))
    return frozenset(edges)


def cycle_from_formula_edges(n: int) -> tuple[int, ...]:
    """Reconstruct the oriented cycle from the independent degree-2 graph."""
    edges = formula_edges(n)
    neighbors: dict[int, set[int]] = {value: set() for value in range(3, n + 1)}
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    _require(
        all(len(adjacent) == 2 for adjacent in neighbors.values()),
        f"formula graph is not 2-regular at n={n}: {neighbors}",
    )

    cycle = [3, n - 1]
    previous = 3
    current = n - 1
    while True:
        candidates = neighbors[current] - {previous}
        _require(
            len(candidates) == 1,
            f"formula cycle continuation is ambiguous at n={n}, vertex={current}",
        )
        next_value = next(iter(candidates))
        if next_value == 3:
            break
        _require(
            next_value not in cycle,
            f"formula cycle closes a proper subcycle at n={n}: {cycle}",
        )
        cycle.append(next_value)
        previous, current = current, next_value
    _require(
        len(cycle) == n - 2 and set(cycle) == set(range(3, n + 1)),
        f"formula cycle missed vertices at n={n}: {cycle}",
    )
    return tuple(cycle)


def check_order_convention(stop: int) -> None:
    for n in range(5, stop + 1):
        paper = shifted_supnick_tour(n)
        interleave = shifted_interleave_tour(n)
        _require(
            cycle_equivalent(paper, interleave),
            f"tour convention mismatch at n={n}: {paper=} {interleave=}",
        )
        _require(
            paper[0] == 3 and paper[1] == n - 1 and paper[-1] == n,
            f"seam-neighbor mismatch at n={n}: {paper}",
        )
        actual_edges = adjacent_edges(paper)
        expected_edges = formula_edges(n)
        _require(
            len(actual_edges) == n - 2 and actual_edges == expected_edges,
            f"edge formula mismatch at n={n}: {actual_edges=} {expected_edges=}",
        )
        _require(
            cycle_from_formula_edges(n) == paper,
            f"formula-graph reconstruction mismatch at n={n}",
        )


def _sine_square(R: Fraction, a: int, b: int) -> Fraction:
    return Fraction(a * b, 1) / ((R + a) * (R + b))


N16_UPPER_ROWS = (
    ((3, 16), Fraction(1, 35), Fraction(17, 100), Fraction(23, 70000)),
    ((9, 10), Fraction(15, 287), Fraction(23, 100), Fraction(1823, 2870000)),
    ((3, 15), Fraction(9, 329), Fraction(17, 100), Fraction(5081, 3290000)),
    ((4, 14), Fraction(7, 207), Fraction(19, 100), Fraction(4727, 2070000)),
    ((5, 13), Fraction(13, 333), Fraction(1, 5), Fraction(8, 8325)),
    ((6, 12), Fraction(9, 209), Fraction(21, 100), Fraction(2169, 2090000)),
    ((7, 11), Fraction(77, 1677), Fraction(11, 50), Fraction(10417, 4192500)),
    ((8, 10), Fraction(1, 21), Fraction(11, 50), Fraction(41, 52500)),
    ((4, 16), Fraction(1, 27), Fraction(1, 5), Fraction(2, 675)),
    ((5, 15), Fraction(75, 1739), Fraction(21, 100), Fraction(16899, 17390000)),
    ((6, 14), Fraction(21, 437), Fraction(11, 50), Fraction(377, 1092500)),
    ((7, 13), Fraction(7, 135), Fraction(23, 100), Fraction(283, 270000)),
    ((8, 12), Fraction(3, 55), Fraction(6, 25), Fraction(21, 6875)),
    ((9, 11), Fraction(99, 1763), Fraction(6, 25), Fraction(1593, 1101875)),
)


N17_LOWER_ROWS = (
    ((3, 17), Fraction(51, 1715), Fraction(17, 100), Fraction(2873, 3430000)),
    ((3, 16), Fraction(1, 35), Fraction(4, 25), Fraction(13, 4375)),
    ((4, 15), Fraction(5, 141), Fraction(9, 50), Fraction(1079, 352500)),
    ((5, 14), Fraction(35, 851), Fraction(1, 5), Fraction(24, 21275)),
    ((6, 13), Fraction(13, 285), Fraction(21, 100), Fraction(863, 570000)),
    ((7, 12), Fraction(7, 143), Fraction(11, 50), Fraction(197, 357500)),
    ((8, 11), Fraction(11, 215), Fraction(11, 50), Fraction(297, 107500)),
    ((9, 10), Fraction(15, 287), Fraction(11, 50), Fraction(2773, 717500)),
    ((4, 17), Fraction(17, 441), Fraction(19, 100), Fraction(10799, 4410000)),
    ((5, 16), Fraction(5, 111), Fraction(21, 100), Fraction(1049, 1110000)),
    ((6, 15), Fraction(45, 893), Fraction(11, 50), Fraction(4447, 2232500)),
    ((7, 14), Fraction(49, 897), Fraction(23, 100), Fraction(15487, 8970000)),
    ((8, 13), Fraction(13, 225), Fraction(6, 25), Fraction(1, 5625)),
    ((9, 12), Fraction(27, 451), Fraction(6, 25), Fraction(639, 281875)),
    ((10, 11), Fraction(55, 903), Fraction(6, 25), Fraction(1867, 564375)),
)


def check_exact_rational_audit(order_stop: int) -> None:
    """Audit exact transcriptions only; no floating-point call occurs here."""
    check_order_convention(order_stop)
    _require(
        shifted_supnick_tour(16)
        == (3, 15, 5, 13, 7, 11, 9, 10, 8, 12, 6, 14, 4, 16),
        "hard-coded n=16 endpoint order mismatch",
    )
    _require(
        shifted_supnick_tour(17)
        == (3, 16, 5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 15, 4, 17),
        "hard-coded n=17 endpoint order mismatch",
    )
    deleted_17 = tuple(value for value in shifted_supnick_tour(17) if value != 17)
    _require(
        not cycle_equivalent(deleted_17, shifted_supnick_tour(16)),
        "negative control failed: vertex deletion unexpectedly preserves the tour",
    )

    # The imported fixed-k threshold domain changes exactly between n=12,13.
    _require(
        Fraction(4, 132) - Fraction(7, 44) ** 2
        == Fraction(29, 5808)
        > 0,
        "n=12 no-threshold boundary audit failed",
    )
    _require(
        Fraction(9, 52) ** 2 - Fraction(4, 156)
        == Fraction(35, 8112)
        > 0,
        "n=13 positive-threshold boundary audit failed",
    )

    # n=16: 0 < kappa_{3,16} < 1/32, hence 32 < T_{3,16}.
    base_16 = Fraction(1, 3) + Fraction(1, 16) + Fraction(1, 15)
    radical_16_square = 4 * Fraction(34, 3 * 16 * 15)
    _require(base_16 == Fraction(37, 80), "unexpected n=16 rational term")
    _require(
        radical_16_square == Fraction(17, 90),
        "unexpected n=16 radical square",
    )
    _require(
        base_16**2 - radical_16_square
        == Fraction(1441, 57600)
        > 0,
        "n=16 kappa positivity comparison failed",
    )
    gap_16 = base_16 - Fraction(1, 32)
    _require(gap_16 == Fraction(69, 160), "unexpected n=16 separator gap")
    _require(
        radical_16_square - gap_16**2
        == Fraction(671, 230400)
        > 0,
        "n=16 threshold separator comparison failed",
    )

    # n=17: kappa_{3,17} > 1/32 > 0, hence T_{3,17} < 32.
    base_17 = Fraction(1, 3) + Fraction(1, 17) + Fraction(1, 16)
    radical_17_square = 4 * Fraction(36, 3 * 17 * 16)
    _require(base_17 == Fraction(371, 816), "unexpected n=17 rational term")
    _require(
        radical_17_square == Fraction(3, 17),
        "unexpected n=17 radical square",
    )
    gap_17 = base_17 - Fraction(1, 32)
    _require(gap_17 == Fraction(691, 1632), "unexpected n=17 separator gap")
    _require(
        gap_17**2 - radical_17_square
        == Fraction(7465, 2663424)
        > 0,
        "n=17 threshold separator comparison failed",
    )

    # n=16: exact termwise upper bounds imply sum asin(s_e) < 3 < pi.
    R_test = Fraction(32)
    upper_sum = Fraction(0)
    _require(len(N16_UPPER_ROWS) == 14, "n=16 proof table edge count failed")
    _require(
        {_edge(*edge) for edge, _, _, _ in N16_UPPER_ROWS}
        == set(formula_edges(16)),
        "n=16 proof table does not equal the full edge set",
    )
    for edge, expected_square, upper, expected_margin in N16_UPPER_ROWS:
        actual_square = _sine_square(R_test, *edge)
        _require(
            actual_square == expected_square,
            f"n=16 sine square mismatch at {edge}",
        )
        _require(
            upper**2 - actual_square == expected_margin > 0,
            f"n=16 upper margin failed at {edge}",
        )
        _require(
            0 < upper <= Fraction(6, 25) < Fraction(1, 3),
            f"n=16 arcsine domain failed at {edge}",
        )
        upper_sum += upper + upper**3 / 5
    _require(
        Fraction(5) - Fraction(21, 9) - Fraction(9, 81)
        == Fraction(23, 9)
        > 0,
        "arcsine derivative-bound endpoint failed",
    )
    _require(
        upper_sum == Fraction(14885133, 5000000),
        "unexpected n=16 arcsine upper sum",
    )
    _require(
        Fraction(3) - upper_sum == Fraction(114867, 5000000) > 0,
        "n=16 chain upper bridge failed",
    )

    # n=17: exact termwise lower bounds imply sum asin(s_e) > 22/7 > pi.
    lower_sum = Fraction(0)
    _require(len(N17_LOWER_ROWS) == 15, "n=17 proof table edge count failed")
    _require(
        {_edge(*edge) for edge, _, _, _ in N17_LOWER_ROWS}
        == set(formula_edges(17)),
        "n=17 proof table does not equal the full edge set",
    )
    for edge, expected_square, lower, expected_margin in N17_LOWER_ROWS:
        actual_square = _sine_square(R_test, *edge)
        _require(
            actual_square == expected_square,
            f"n=17 sine square mismatch at {edge}",
        )
        _require(
            actual_square - lower**2 == expected_margin > 0,
            f"n=17 lower margin failed at {edge}",
        )
        _require(
            0 < lower < 1 and 0 < actual_square < 1,
            f"n=17 arcsine domain failed at {edge}",
        )
        lower_sum += lower
    _require(lower_sum == Fraction(63, 20), "unexpected n=17 lower sum")
    _require(
        lower_sum - Fraction(22, 7) == Fraction(1, 140) > 0,
        "n=17 chain lower bridge failed",
    )


def _load_mpmath() -> None:
    """Load the numerical dependency only for opt-in diagnostics."""
    global mp
    import mpmath as mp


def theta(R: mp.mpf, a: int, b: int) -> mp.mpf:
    z = mp.sqrt(mp.mpf(a * b) / ((R + a) * (R + b)))
    return 2 * mp.asin(z)


def chain_value_and_derivative(
    R: mp.mpf, order: tuple[int, ...]
) -> tuple[mp.mpf, mp.mpf]:
    value = mp.mpf("0")
    derivative = mp.mpf("0")
    for index, a in enumerate(order):
        b = order[(index + 1) % len(order)]
        z = mp.sqrt(mp.mpf(a * b) / ((R + a) * (R + b)))
        value += 2 * mp.asin(z)
        derivative -= z * (1 / (R + a) + 1 / (R + b)) / mp.sqrt(1 - z * z)
    return value, derivative


def chain_root(n: int, digits: int) -> mp.mpf:
    with mp.workdps(digits):
        order = shifted_supnick_tour(n)
        target = 2 * mp.pi
        lo = mp.mpf("0")
        hi = mp.mpf(4 * n * n)
        hi_value, _ = chain_value_and_derivative(hi, order)
        _require(hi_value < target, f"chain root upper bracket failed for n={n}")
        current = mp.mpf(n * n) / 8
        tolerance = mp.power(10, -(digits - 15))

        for _ in range(180):
            value, derivative = chain_value_and_derivative(current, order)
            if value > target:
                lo = current
            else:
                hi = current
            if hi - lo <= tolerance * max(1, abs(current)):
                return +(lo + hi) / 2
            newton = current - (value - target) / derivative
            if not lo < newton < hi:
                newton = (lo + hi) / 2
            current = newton
        raise AssertionError(f"chain root did not converge for n={n}, digits={digits}")


def seam_threshold(n: int) -> mp.mpf | None:
    """Use the rationalized kappa form to avoid diagnostic cancellation."""
    c = mp.mpf(1) / 3
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
                theta(root, n, 3)
                + theta(root, 3, n - 1)
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
) -> tuple[
    dict[int, dict[str, mp.mpf | None]],
    mp.mpf,
    mp.mpf,
    tuple[int, int] | None,
]:
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
                f"precision-dependent deficit sign at n={n}",
            )
            expected_sign = 1 if n <= 16 else -1
            _require(
                _sign(high_deficit) == expected_sign,
                f"unexpected diagnostic deficit sign at n={n}: {high_deficit}",
            )
            _require(
                abs(high_deficit) > mp.power(10, -(stability_digits // 2)),
                f"diagnostic deficit is too close to zero at n={n}",
            )
            threshold = higher[n]["T"]
            if n <= 12:
                _require(threshold is None, f"unexpected positive threshold at n={n}")
            else:
                _require(threshold is not None, f"missing positive threshold at n={n}")
                comparison_sign = _sign(high_root - mp.mpf(threshold))
                _require(
                    comparison_sign == -expected_sign,
                    f"root/threshold sign mismatch at n={n}",
                )

        for n in range(start + 1, stop + 1):
            _require(
                mp.mpf(higher[n]["R"]) > mp.mpf(higher[n - 1]["R"]),
                f"diagnostic root monotonicity failed at n={n}",
            )
            if n >= 14:
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
            "root precision stability failed: "
            f"{max_relative_root_delta} >= {tolerance}",
        )
        _require(
            max_absolute_deficit_delta < tolerance,
            "deficit precision stability failed: "
            f"{max_absolute_deficit_delta} >= {tolerance}",
        )

    first_raw_monotonicity_failure: tuple[int, int] | None = None
    with mp.workdps(stability_digits):
        for n in range(start + 1, stop + 1):
            previous = mp.mpf(higher[n - 1]["deficit"])
            current = mp.mpf(higher[n]["deficit"])
            if current > previous:
                first_raw_monotonicity_failure = (n - 1, n)
                break
    if start <= 5 and stop >= 41:
        _require(
            first_raw_monotonicity_failure == (40, 41),
            "unexpected first raw-deficit monotonicity failure: "
            f"{first_raw_monotonicity_failure}",
        )
    return (
        higher,
        max_relative_root_delta,
        max_absolute_deficit_delta,
        first_raw_monotonicity_failure,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order-stop", type=int, default=200)
    parser.add_argument("--start", type=int, default=5)
    parser.add_argument("--stop", type=int, default=100)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--stability-digits", type=int, default=100)
    parser.add_argument(
        "--diagnostics",
        action="store_true",
        help="add finite two-precision mpmath diagnostics after exact gates",
    )
    args = parser.parse_args()
    if args.order_stop < 17:
        parser.error("--order-stop must be at least 17")
    if args.start < 5 or args.stop < args.start:
        parser.error("require 5 <= start <= stop")
    if args.diagnostics:
        if args.digits < 40:
            parser.error("--digits must be at least 40")
        if args.stability_digits <= args.digits:
            parser.error("--stability-digits must exceed --digits")

    check_exact_rational_audit(args.order_stop)
    exact_gate_count = _EXPLICIT_GATE_COUNT
    print("independent_of_production=PASS (no ringmin imports)")
    print(
        "exact_rational_transcription_audit=PASS "
        f"explicit_gates={exact_gate_count} optimized_safe=YES"
    )
    print("exact_threshold_domain_and_R32_bridges=PASS n=12,13,16,17")
    print("exact_termwise_chain_bridges_at_R32=PASS n=16,17")
    print(f"shifted_order_conventions_and_edge_sets=PASS n=5..{args.order_stop}")
    print(
        "theorem_sources=research/RADIUS3_SEAM_ONSET.md+"
        "research/FIXED_K_SUPNICK_SEAM.md"
    )

    if not args.diagnostics:
        print("numerical_diagnostics=SKIPPED (opt in with --diagnostics)")
        print(
            "classification=EXACT_RATIONAL_AUDIT; checker is corroborative only; "
            "theorem sources are the two proof notes"
        )
        return 0

    _load_mpmath()
    rows, max_root_delta, max_deficit_delta, raw_failure = check_numeric_diagnostics(
        args.start,
        args.stop,
        args.digits,
        args.stability_digits,
    )
    print(
        "numerical_diagnostics=PASS "
        f"n={args.start}..{args.stop} digits={args.digits}/{args.stability_digits}"
    )
    print(
        "precision_stability=PASS "
        f"max_relative_R_delta={mp.nstr(max_root_delta, 8)} "
        f"max_absolute_deficit_delta={mp.nstr(max_deficit_delta, 8)}"
    )
    selected = sorted(
        {args.start, args.stop, 5, 12, 13, 16, 17}.intersection(
            range(args.start, args.stop + 1)
        )
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"n={n:03d} R_3n={mp.nstr(row['R'], 18)} "
            f"T_3n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    if raw_failure is None:
        print("raw_deficit_nonincreasing=NOT_REFUTED_IN_SELECTED_RANGE")
    else:
        print(f"raw_deficit_nonincreasing=REFUTED first_pair={raw_failure}")
    print(
        "classification=NUMERICAL_DIAGNOSTIC_ONLY; checker is corroborative only; "
        "theorem sources are the two proof notes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
