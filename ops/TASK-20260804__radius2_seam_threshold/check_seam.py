#!/usr/bin/env python3
"""Finite diagnostics for the exact radius-2 Supnick seam theorem.

This script deliberately does not import ``ringmin``. Exact ``Fraction``
checks audit every rational bridge in the proof note. The mpmath scan is
finite diagnostic evidence only; it is not the all-n proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

import mpmath as mp


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
    """Proof-note representative on radii 2,...,n."""
    if n < 4:
        raise ValueError(f"n must be at least 4, got {n}")
    size = n - 1
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
            f"shifted Supnick construction missed indices for n={n}: {used}"
        )
    indices = first + list(reversed(second)) + [size]
    return tuple(index + 1 for index in indices)


def shifted_interleave_tour(n: int) -> tuple[int, ...]:
    """Independently written production-style interleave construction."""
    if n < 4:
        raise ValueError(f"n must be at least 4, got {n}")
    size = n - 1
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
            f"shifted interleave construction missed indices for n={n}: {used}"
        )
    return tuple(index + 1 for index in arm_a + list(reversed(arm_b)))


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
    if n % 2 == 1:
        half = (n - 1) // 2
        edges = {_edge(2, n), _edge(half + 1, half + 2)}
        edges.update(_edge(i, 2 * half + 2 - i) for i in range(2, half + 1))
        edges.update(_edge(i, 2 * half + 4 - i) for i in range(3, half + 2))
    else:
        half = (n - 2) // 2
        edges = {_edge(2, n)}
        edges.update(_edge(i, 2 * half + 3 - i) for i in range(2, half + 2))
        edges.update(_edge(i, 2 * half + 5 - i) for i in range(3, half + 3))
    return frozenset(edges)


def check_order_convention(stop: int) -> None:
    for n in range(4, stop + 1):
        paper = shifted_supnick_tour(n)
        interleave = shifted_interleave_tour(n)
        if not cycle_equivalent(paper, interleave):
            raise AssertionError(
                f"tour convention mismatch at n={n}: {paper=} {interleave=}"
            )
        if paper[0] != 2 or paper[1] != n - 1 or paper[-1] != n:
            raise AssertionError(f"seam-neighbor mismatch at n={n}: {paper}")
        actual_edges = adjacent_edges(paper)
        expected_edges = formula_edges(n)
        if len(actual_edges) != n - 1 or actual_edges != expected_edges:
            raise AssertionError(
                f"edge formula mismatch at n={n}: {actual_edges=} {expected_edges=}"
            )


def _sine_square(R: Fraction, a: int, b: int) -> Fraction:
    return Fraction(a * b, 1) / ((R + a) * (R + b))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_exact_bridges() -> None:
    # The positive x-threshold domain starts exactly at n=9.
    _require(
        Fraction(1, 14) - Fraction(13, 56) ** 2 == Fraction(55, 3136) > 0,
        "n=8 no-threshold comparison failed",
    )
    _require(
        Fraction(19, 72) ** 2 - Fraction(1, 18) == Fraction(73, 5184) > 0,
        "n=9 threshold-domain comparison failed",
    )

    # kappa_12 < 1/17, hence T_{2,12} > 17.
    gap_12 = Fraction(89, 132) - Fraction(1, 17)
    _require(gap_12 == Fraction(1381, 2244), "unexpected n=12 threshold gap")
    _require(
        Fraction(25, 66) - gap_12 * gap_12
        == Fraction(239, 5035536)
        > 0,
        "n=12 threshold square comparison failed",
    )

    # kappa_13 > 1/14, hence T_{2,13} < 14.
    gap_13 = Fraction(103, 156) - Fraction(1, 14)
    _require(gap_13 == Fraction(643, 1092), "unexpected n=13 threshold gap")
    _require(
        gap_13 * gap_13 - Fraction(9, 26)
        == Fraction(673, 1192464)
        > 0,
        "n=13 threshold square comparison failed",
    )

    # At R=17, exact upper bounds prove C_{2,12}(17) < 2*pi.
    R12_test = Fraction(17, 1)
    n12_rows = (
        ((2, 11), Fraction(11, 266), Fraction(51, 250), Fraction(2183, 8312500)),
        ((11, 4), Fraction(11, 147), Fraction(137, 500), Fraction(9043, 36750000)),
        ((4, 9), Fraction(6, 91), Fraction(257, 1000), Fraction(10459, 91000000)),
        ((9, 6), Fraction(27, 299), Fraction(301, 1000), Fraction(89699, 299000000)),
        ((6, 7), Fraction(7, 92), Fraction(69, 250), Fraction(32, 359375)),
        ((7, 8), Fraction(7, 75), Fraction(153, 500), Fraction(227, 750000)),
        ((8, 5), Fraction(4, 55), Fraction(27, 100), Fraction(19, 110000)),
        ((5, 10), Fraction(25, 297), Fraction(291, 1000), Fraction(150257, 297000000)),
        ((10, 3), Fraction(1, 18), Fraction(59, 250), Fraction(79, 562500)),
        ((3, 12), Fraction(9, 145), Fraction(1, 4), Fraction(1, 2320)),
        ((12, 2), Fraction(24, 551), Fraction(209, 1000), Fraction(68231, 551000000)),
    )
    upper_sum = Fraction(0)
    for (a, b), expected_square, upper, expected_margin in n12_rows:
        actual_square = _sine_square(R12_test, a, b)
        _require(
            actual_square == expected_square,
            f"n=12 sine square mismatch at {(a, b)}",
        )
        _require(
            upper * upper - actual_square == expected_margin > 0,
            f"n=12 upper-bound margin failed at {(a, b)}",
        )
        _require(
            upper < Fraction(1, 3),
            f"n=12 arcsine domain check failed at {(a, b)}",
        )
        upper_sum += upper + upper**3 / 5
    _require(
        Fraction(5) - Fraction(21, 9) - Fraction(9, 81)
        == Fraction(23, 9)
        > 0,
        "arcsine derivative-bound endpoint check failed",
    )
    _require(
        upper_sum == Fraction(1457520693, 500000000) < 3,
        "n=12 chain-cost upper bound failed",
    )

    # At R=14, exact lower bounds prove C_{2,13}(14) > 2*pi.
    R13_test = Fraction(14, 1)
    n13_rows = (
        ((2, 12), Fraction(3, 52), Fraction(6, 25), Fraction(3, 32500)),
        ((12, 4), Fraction(4, 39), Fraction(8, 25), Fraction(4, 24375)),
        ((4, 10), Fraction(5, 54), Fraction(38, 125), Fraction(149, 843750)),
        ((10, 6), Fraction(1, 8), Fraction(353, 1000), Fraction(391, 1000000)),
        ((6, 8), Fraction(6, 55), Fraction(33, 100), Fraction(21, 110000)),
        ((8, 7), Fraction(4, 33), Fraction(87, 250), Fraction(223, 2062500)),
        ((7, 9), Fraction(3, 23), Fraction(361, 1000), Fraction(2617, 23000000)),
        ((9, 5), Fraction(45, 437), Fraction(8, 25), Fraction(157, 273125)),
        ((5, 11), Fraction(11, 95), Fraction(17, 50), Fraction(9, 47500)),
        ((11, 3), Fraction(33, 425), Fraction(139, 500), Fraction(1543, 4250000)),
        ((3, 13), Fraction(13, 153), Fraction(291, 1000), Fraction(43807, 153000000)),
        ((13, 2), Fraction(13, 216), Fraction(49, 200), Fraction(173, 1080000)),
    )
    lower_sum = Fraction(0)
    for (a, b), expected_square, lower, expected_margin in n13_rows:
        actual_square = _sine_square(R13_test, a, b)
        _require(
            actual_square == expected_square,
            f"n=13 sine square mismatch at {(a, b)}",
        )
        _require(
            actual_square - lower * lower == expected_margin > 0,
            f"n=13 lower-bound margin failed at {(a, b)}",
        )
        lower_sum += lower
    _require(
        lower_sum == Fraction(373, 100) > Fraction(22, 7),
        "n=13 chain-cost lower bound failed",
    )


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
        if not hi_value < target:
            raise AssertionError(f"chain root upper bracket failed for n={n}")
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
    alpha = mp.mpf(1) / n + mp.mpf(1) / (n - 1)
    beta = mp.mpf(1) / (n * (n - 1))
    kappa = mp.mpf(1) / 2 + alpha - 2 * mp.sqrt(alpha / 2 + beta)
    return None if kappa <= 0 else 1 / kappa


def scan(start: int, stop: int, digits: int) -> dict[int, dict[str, mp.mpf | None]]:
    rows: dict[int, dict[str, mp.mpf | None]] = {}
    with mp.workdps(digits):
        for n in range(start, stop + 1):
            R = chain_root(n, digits)
            deficit = theta(R, n, 2) + theta(R, 2, n - 1) - theta(R, n, n - 1)
            rows[n] = {
                "R": +R,
                "T": seam_threshold(n),
                "deficit": +deficit,
            }
    return rows


def _sign(value: mp.mpf) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def check_numeric_scan(
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
    base = scan(start, stop, digits)
    higher = scan(start, stop, stability_digits)
    max_relative_R_delta = mp.mpf("0")
    max_absolute_deficit_delta = mp.mpf("0")

    with mp.workdps(stability_digits):
        for n in range(start, stop + 1):
            base_R = mp.mpf(base[n]["R"])
            high_R = mp.mpf(higher[n]["R"])
            base_deficit = mp.mpf(base[n]["deficit"])
            high_deficit = mp.mpf(higher[n]["deficit"])
            max_relative_R_delta = max(
                max_relative_R_delta,
                abs(base_R - high_R) / max(1, abs(high_R)),
            )
            max_absolute_deficit_delta = max(
                max_absolute_deficit_delta,
                abs(base_deficit - high_deficit),
            )
            if _sign(base_deficit) != _sign(high_deficit):
                raise AssertionError(f"precision-dependent deficit sign at n={n}")
            expected_sign = 1 if n <= 12 else -1
            if _sign(high_deficit) != expected_sign:
                raise AssertionError(
                    f"unexpected diagnostic deficit sign at n={n}: {high_deficit}"
                )
            threshold = higher[n]["T"]
            if n <= 8 and threshold is not None:
                raise AssertionError(f"unexpected positive threshold at n={n}")
            if n >= 9:
                if threshold is None:
                    raise AssertionError(f"missing positive threshold at n={n}")
                comparison_sign = _sign(high_R - mp.mpf(threshold))
                if comparison_sign != -expected_sign:
                    raise AssertionError(f"root/threshold sign mismatch at n={n}")

        tolerance = mp.power(10, -min(30, digits // 2))
        if max_relative_R_delta >= tolerance:
            raise AssertionError(
                f"root precision stability failed: {max_relative_R_delta} >= {tolerance}"
            )
        if max_absolute_deficit_delta >= tolerance:
            raise AssertionError(
                "deficit precision stability failed: "
                f"{max_absolute_deficit_delta} >= {tolerance}"
            )

    first_monotonicity_failure: tuple[int, int] | None = None
    for n in range(start + 1, stop + 1):
        previous = mp.mpf(higher[n - 1]["deficit"])
        current = mp.mpf(higher[n]["deficit"])
        if current > previous:
            first_monotonicity_failure = (n - 1, n)
            break
    if start <= 4 and stop >= 30 and first_monotonicity_failure != (29, 30):
        raise AssertionError(
            "expected first raw-deficit monotonicity failure at (29,30), got "
            f"{first_monotonicity_failure}"
        )
    return higher, max_relative_R_delta, max_absolute_deficit_delta, first_monotonicity_failure


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=4)
    parser.add_argument("--stop", type=int, default=200)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--stability-digits", type=int, default=100)
    args = parser.parse_args()
    if args.start < 4 or args.stop < args.start:
        parser.error("require 4 <= start <= stop")
    if args.digits < 40:
        parser.error("--digits must be at least 40")
    if args.stability_digits <= args.digits:
        parser.error("--stability-digits must exceed --digits")

    check_exact_bridges()
    check_order_convention(args.stop)
    rows, max_R_delta, max_D_delta, failure = check_numeric_scan(
        args.start,
        args.stop,
        args.digits,
        args.stability_digits,
    )

    print("independent_of_production=PASS (no ringmin imports)")
    print("exact_rational_domain_and_bridges_n8_n9_n12_n13=PASS")
    print(f"shifted_order_convention_edge_sets=PASS n=4..{args.stop}")
    print(
        "diagnostic_sign_scan=PASS "
        f"n={args.start}..{args.stop} digits={args.stability_digits}"
    )
    print(
        "precision_stability=PASS "
        f"digits={args.digits}/{args.stability_digits} "
        f"max_relative_R_delta={mp.nstr(max_R_delta, 8)} "
        f"max_absolute_deficit_delta={mp.nstr(max_D_delta, 8)}"
    )

    selected = sorted(
        {args.start, args.stop, 4, 8, 9, 12, 13, 29, 30}.intersection(
            range(args.start, args.stop + 1)
        )
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"n={n:03d} R_2n={mp.nstr(row['R'], 18)} "
            f"T_2n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    if failure is None:
        print("raw_deficit_nonincreasing=NOT_OBSERVED_IN_SELECTED_RANGE")
    else:
        print(f"raw_deficit_nonincreasing=REFUTED first_pair={failure}")
    print("classification=FINITE_DIAGNOSTIC_ONLY; all-n proof is the proof note")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
