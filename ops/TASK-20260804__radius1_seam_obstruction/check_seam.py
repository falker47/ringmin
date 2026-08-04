#!/usr/bin/env python3
"""Independent diagnostics for the radius-1 Supnick seam theorem.

This script deliberately does not import ``ringmin``.  Exact Fraction checks
audit the two rational bridges used in the proof.  The mpmath scan is finite
diagnostic evidence only; it is not the all-n proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

import mpmath as mp


def _append_once(target: list[int], used: set[int], value: int) -> None:
    if value in used:
        raise AssertionError(f"duplicate Supnick value: {value}")
    used.add(value)
    target.append(value)


def paper_supnick_tour(n: int) -> tuple[int, ...]:
    """Parity-independent representative fixed in the proof note."""
    if n < 3:
        raise ValueError(f"n must be at least 3, got {n}")
    h = (n + 1) // 2
    used: set[int] = set()
    first: list[int] = []
    second: list[int] = []

    j = 0
    while True:
        before = len(used)
        low = 1 + 2 * j
        high = n - 1 - 2 * j
        if low <= h:
            _append_once(first, used, low)
        if high > h:
            _append_once(first, used, high)
        j += 1
        if len(used) == before:
            break

    j = 0
    while True:
        before = len(used)
        low = 2 + 2 * j
        high = n - 2 - 2 * j
        if low <= h:
            _append_once(second, used, low)
        if high > h:
            _append_once(second, used, high)
        j += 1
        if len(used) == before:
            break

    if used != set(range(1, n)):
        raise AssertionError(f"Supnick construction missed values for n={n}: {used}")
    return tuple(first + list(reversed(second)) + [n])


def interleave_tour(n: int) -> tuple[int, ...]:
    """Independent production-style interleave construction."""
    if n < 3:
        raise ValueError(f"n must be at least 3, got {n}")
    h = (n + 1) // 2
    used: set[int] = {n}
    arm_a = [n]
    arm_b: list[int] = []
    offset = 0
    while True:
        before = len(used)
        low_a = 1 + 2 * offset
        high_a = n - 1 - 2 * offset
        low_b = 2 + 2 * offset
        high_b = n - 2 - 2 * offset
        if low_a <= h:
            _append_once(arm_a, used, low_a)
        if high_a > h:
            _append_once(arm_a, used, high_a)
        if low_b <= h:
            _append_once(arm_b, used, low_b)
        if high_b > h:
            _append_once(arm_b, used, high_b)
        offset += 1
        if len(used) == before:
            break
    if used != set(range(1, n + 1)):
        raise AssertionError(f"interleave construction missed values for n={n}: {used}")
    return tuple(arm_a + list(reversed(arm_b)))


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
    if n % 2 == 0:
        m = n // 2
        edges = {_edge(1, n), _edge(m, m + 1)}
        edges.update(_edge(j, n - j) for j in range(1, m))
        edges.update(_edge(j, n + 2 - j) for j in range(2, m + 1))
    else:
        m = (n - 1) // 2
        edges = {_edge(1, n)}
        edges.update(_edge(j, n - j) for j in range(1, m + 1))
        edges.update(_edge(j, n + 2 - j) for j in range(2, m + 2))
    return frozenset(edges)


def check_order_convention(stop: int) -> None:
    for n in range(3, stop + 1):
        paper = paper_supnick_tour(n)
        interleave = interleave_tour(n)
        if not cycle_equivalent(paper, interleave):
            raise AssertionError(
                f"tour convention mismatch at n={n}: {paper=} {interleave=}"
            )
        if paper[0] != 1 or paper[1] != n - 1 or paper[-1] != n:
            raise AssertionError(f"seam-neighbor mismatch at n={n}: {paper}")
        actual_edges = adjacent_edges(paper)
        expected_edges = formula_edges(n)
        if len(actual_edges) != n or actual_edges != expected_edges:
            raise AssertionError(
                f"edge formula mismatch at n={n}: {actual_edges=} {expected_edges=}"
            )


def _sine_square(R: Fraction, a: int, b: int) -> Fraction:
    return Fraction(a * b, 1) / ((R + a) * (R + b))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_exact_bridges() -> None:
    # kappa_8 > 10/51, hence T_8 < 51/10.
    rational_gap = Fraction(71, 56) - Fraction(10, 51)
    _require(
        rational_gap == Fraction(3061, 2856),
        "unexpected rational gap in the n=8 threshold bound",
    )
    _require(
        rational_gap * rational_gap - Fraction(8, 7)
        == Fraction(47737, 8156736),
        "n=8 threshold square comparison failed",
    )

    R8_test = Fraction(51, 10)
    n8_rows = (
        ((1, 8), Fraction(800, 7991), Fraction(79, 250), Fraction(128169, 499437500)),
        ((4, 5), Fraction(2000, 9191), Fraction(233, 500), Fraction(1029801, 2297750000)),
        ((1, 7), Fraction(700, 7381), Fraction(307, 1000), Fraction(4348131, 7381000000)),
        ((2, 6), Fraction(400, 2627), Fraction(39, 100), Fraction(4333, 26270000)),
        ((3, 5), Fraction(500, 2727), Fraction(107, 250), Fraction(28577, 170437500)),
        ((2, 8), Fraction(1600, 9301), Fraction(207, 500), Fraction(1461451, 2325250000)),
        ((3, 7), Fraction(700, 3267), Fraction(231, 500), Fraction(669613, 816750000)),
        ((4, 6), Fraction(800, 3367), Fraction(487, 1000), Fraction(1451977, 3367000000)),
    )
    lower_sum = Fraction(0)
    for (a, b), expected_square, lower, expected_margin in n8_rows:
        actual_square = _sine_square(R8_test, a, b)
        _require(actual_square == expected_square, f"n=8 sine square mismatch at {(a, b)}")
        _require(
            actual_square - lower * lower == expected_margin > 0,
            f"n=8 lower-bound margin failed at {(a, b)}",
        )
        lower_sum += lower
    _require(
        lower_sum == Fraction(327, 100) > Fraction(22, 7),
        "n=8 lower-bound sum failed",
    )

    # 0 < kappa_7 < 1/6, hence T_7 > 6.
    _require(
        Fraction(55, 42) ** 2 - Fraction(4, 3) == Fraction(673, 1764),
        "n=7 threshold positivity check failed",
    )
    _require(
        Fraction(8, 7) ** 2 < Fraction(4, 3),
        "n=7 threshold upper bound failed",
    )

    R7_test = Fraction(6, 1)
    n7_rows = (
        ((1, 7), Fraction(1, 13), Fraction(7, 25), Fraction(12, 8125)),
        ((1, 6), Fraction(1, 14), Fraction(27, 100), Fraction(103, 70000)),
        ((2, 5), Fraction(5, 44), Fraction(17, 50), Fraction(27, 13750)),
        ((3, 4), Fraction(2, 15), Fraction(37, 100), Fraction(107, 30000)),
        ((2, 7), Fraction(7, 52), Fraction(37, 100), Fraction(297, 130000)),
        ((3, 6), Fraction(1, 6), Fraction(41, 100), Fraction(43, 30000)),
        ((4, 5), Fraction(2, 11), Fraction(43, 100), Fraction(339, 110000)),
    )
    upper_sum = Fraction(0)
    for (a, b), expected_square, upper, expected_margin in n7_rows:
        actual_square = _sine_square(R7_test, a, b)
        _require(actual_square == expected_square, f"n=7 sine square mismatch at {(a, b)}")
        _require(
            upper * upper - actual_square == expected_margin > 0,
            f"n=7 upper-bound margin failed at {(a, b)}",
        )
        _require(upper < Fraction(1, 2), f"n=7 arcsin domain check failed at {(a, b)}")
        upper_sum += upper
    _require(upper_sum == Fraction(247, 100), "n=7 upper-bound sum failed")
    _require(
        Fraction(12, 5) * upper_sum == Fraction(741, 125) < 6,
        "n=7 chain-cost upper bound failed",
    )

    # kappa_5 > 0, the starting point for positive lower-side thresholds.
    _require(29 * 29 > 2 * 20 * 20, "n=5 threshold positivity check failed")


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
        order = paper_supnick_tour(n)
        target = 2 * mp.pi
        lo = mp.mpf("0")
        hi = mp.mpf(4 * n * n)
        hi_value, _ = chain_value_and_derivative(hi, order)
        if not hi_value < target:
            raise AssertionError(f"chain root upper bracket failed for n={n}")
        current = mp.mpf(n * n) / 8
        tolerance = mp.power(10, -(digits - 15))

        for _ in range(160):
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
    kappa = 1 + mp.mpf(1) / n + mp.mpf(1) / (n - 1)
    kappa -= 2 * mp.sqrt(mp.mpf(2) / (n - 1))
    return None if kappa <= 0 else 1 / kappa


def scan(start: int, stop: int, digits: int) -> dict[int, dict[str, mp.mpf | None]]:
    rows: dict[int, dict[str, mp.mpf | None]] = {}
    with mp.workdps(digits):
        for n in range(start, stop + 1):
            R = chain_root(n, digits)
            deficit = theta(R, n, 1) + theta(R, 1, n - 1) - theta(R, n, n - 1)
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
            expected_sign = 1 if n <= 7 else -1
            if _sign(high_deficit) != expected_sign:
                raise AssertionError(
                    f"unexpected diagnostic deficit sign at n={n}: {high_deficit}"
                )

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
    for n in range(max(start + 1, 9), stop + 1):
        previous = mp.mpf(higher[n - 1]["deficit"])
        current = mp.mpf(higher[n]["deficit"])
        if current > previous:
            first_monotonicity_failure = (n - 1, n)
            break
    if start <= 8 and stop >= 20 and first_monotonicity_failure != (19, 20):
        raise AssertionError(
            "expected first raw-deficit monotonicity failure at (19,20), got "
            f"{first_monotonicity_failure}"
        )
    return higher, max_relative_R_delta, max_absolute_deficit_delta, first_monotonicity_failure


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--stop", type=int, default=200)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--stability-digits", type=int, default=100)
    args = parser.parse_args()
    if args.start < 3 or args.stop < args.start:
        parser.error("require 3 <= start <= stop")
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
    print("exact_rational_bridges_n7_n8=PASS")
    print(f"order_convention_edge_sets=PASS n=3..{args.stop}")
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
        {args.start, args.stop, 7, 8, 19, 20}.intersection(range(args.start, args.stop + 1))
    )
    for n in selected:
        row = rows[n]
        threshold = "NA" if row["T"] is None else mp.nstr(row["T"], 18)
        print(
            f"n={n:03d} R_n={mp.nstr(row['R'], 18)} "
            f"T_n={threshold} deficit_lhs_minus_rhs={mp.nstr(row['deficit'], 18)}"
        )
    if failure is None:
        print("raw_deficit_nonincreasing=NOT_OBSERVED_IN_SELECTED_RANGE")
    else:
        print(f"raw_deficit_nonincreasing=REFUTED first_pair={failure}")
    print("classification=FINITE_DIAGNOSTIC_ONLY; all-n proof is the proof note")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
