#!/usr/bin/env python3
"""Finite diagnostics for the exact fixed-k Supnick seam theorem.

This task-local script deliberately does not import ``ringmin``. Exact
``Fraction`` checks audit the order and threshold algebra. The mpmath scan is
finite diagnostic evidence only; it does not prove the all-k theorem or an
exact onset for any k >= 3.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

import mpmath as mp


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _append_rank(
    target: list[int], used: set[int], rank: int, size: int
) -> None:
    _require(1 <= rank <= size, f"Supnick rank outside 1..{size}: {rank}")
    _require(rank not in used, f"duplicate Supnick rank: {rank}")
    used.add(rank)
    target.append(rank)


def rank_supnick_tour(size: int) -> tuple[int, ...]:
    """Parity-independent proof-note representative on ranks 1,...,size."""
    if size < 3:
        raise ValueError(f"size must be at least 3, got {size}")
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
            _append_rank(first, used, low, size)
        if high > midpoint:
            _append_rank(first, used, high, size)
        offset += 1
        if len(used) == before:
            break

    offset = 0
    while True:
        before = len(used)
        low = 2 + 2 * offset
        high = size - 2 - 2 * offset
        if low <= midpoint:
            _append_rank(second, used, low, size)
        if high > midpoint:
            _append_rank(second, used, high, size)
        offset += 1
        if len(used) == before:
            break

    _require(
        used == set(range(1, size)),
        f"proof-note Supnick construction missed ranks for size={size}: {used}",
    )
    result = tuple(first + list(reversed(second)) + [size])
    _require(set(result) == set(range(1, size + 1)), "invalid rank permutation")
    return result


def rank_interleave_tour(size: int) -> tuple[int, ...]:
    """Independently written production-style interleave construction."""
    if size < 3:
        raise ValueError(f"size must be at least 3, got {size}")
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
            _append_rank(arm_a, used, low_a, size)
        if high_a > midpoint:
            _append_rank(arm_a, used, high_a, size)
        if low_b <= midpoint:
            _append_rank(arm_b, used, low_b, size)
        if high_b > midpoint:
            _append_rank(arm_b, used, high_b, size)
        offset += 1
        if len(used) == before:
            break
    _require(
        used == set(range(1, size + 1)),
        f"interleave construction missed ranks for size={size}: {used}",
    )
    return tuple(arm_a + list(reversed(arm_b)))


def shifted_supnick_tour(k: int, n: int) -> tuple[int, ...]:
    if k < 1 or n < k + 2:
        raise ValueError(f"require k>=1 and n>=k+2, got k={k}, n={n}")
    return tuple(k + rank - 1 for rank in rank_supnick_tour(n - k + 1))


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


def formula_edges(k: int, n: int) -> frozenset[tuple[int, int]]:
    size = n - k + 1
    if size % 2 == 0:
        half = size // 2
        edges = {_edge(k, n), _edge(k + half - 1, k + half)}
        edges.update(
            _edge(i, n + k - 1 - i) for i in range(k, k + half - 1)
        )
        edges.update(
            _edge(i, n + k + 1 - i) for i in range(k + 1, k + half)
        )
    else:
        half = (size - 1) // 2
        edges = {_edge(k, n)}
        edges.update(
            _edge(i, n + k - 1 - i) for i in range(k, k + half)
        )
        edges.update(
            _edge(i, n + k + 1 - i)
            for i in range(k + 1, k + half + 1)
        )
    return frozenset(edges)


def check_order_conventions(max_k: int, extra: int) -> None:
    for k in range(1, max_k + 1):
        stop = 4 * k + 1 + extra
        for n in range(k + 2, stop + 1):
            proof_order = shifted_supnick_tour(k, n)
            interleave_ranks = rank_interleave_tour(n - k + 1)
            interleave = tuple(k + rank - 1 for rank in interleave_ranks)
            _require(
                cycle_equivalent(proof_order, interleave),
                f"tour convention mismatch at k={k}, n={n}",
            )
            _require(
                proof_order[0] == k
                and proof_order[1] == n - 1
                and proof_order[-1] == n,
                f"seam-neighbor mismatch at k={k}, n={n}: {proof_order}",
            )
            actual = adjacent_edges(proof_order)
            expected = formula_edges(k, n)
            _require(
                len(actual) == n - k + 1 and actual == expected,
                f"edge formula mismatch at k={k}, n={n}",
            )


def exact_terms(
    k: int, n: int
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    c = Fraction(1, k)
    alpha = Fraction(1, n) + Fraction(1, n - 1)
    beta = Fraction(1, n * (n - 1))
    q_squared = alpha / k + beta
    return c, alpha, beta, q_squared


def check_exact_algebra(max_k: int, extra: int) -> None:
    for k in range(1, max_k + 1):
        boundary_before = 4 * k
        boundary_start = 4 * k + 1
        c_before, alpha_before, beta_before, _ = exact_terms(k, boundary_before)
        c_start, alpha_start, beta_start, _ = exact_terms(k, boundary_start)
        _require(c_before - alpha_before > 0, f"unexpected 4k sign for k={k}")
        _require(c_start - alpha_start > 0, f"unexpected 4k+1 sign for k={k}")
        _require(
            4 * beta_before > (c_before - alpha_before) ** 2,
            f"P_4k(0)>1/k boundary failed for k={k}",
        )
        _require(
            4 * beta_start < (c_start - alpha_start) ** 2,
            f"P_(4k+1)(0)<1/k boundary failed for k={k}",
        )

        stop = boundary_start + extra
        for n in range(k + 2, stop + 1):
            c, alpha, beta, q_squared = exact_terms(k, n)
            expected_q_squared = Fraction(2 * n + k - 1, k * n * (n - 1))
            _require(
                q_squared == expected_q_squared,
                f"q^2 identity failed at k={k}, n={n}",
            )
            _require(
                (c + alpha) ** 2 - 4 * q_squared
                == (c - alpha) ** 2 - 4 * beta,
                f"rationalization identity failed at k={k}, n={n}",
            )

            gap = c - alpha
            physical_from_pocket = gap > 0 and gap**2 > 4 * beta
            physical_from_integer_domain = n >= boundary_start
            _require(
                physical_from_pocket == physical_from_integer_domain,
                f"physical-domain mismatch at k={k}, n={n}",
            )

            kappa_numerator = (c + alpha) ** 2 - 4 * q_squared
            if physical_from_integer_domain:
                _require(
                    q_squared > alpha**2,
                    f"physical square-root branch failed at k={k}, n={n}",
                )
                _require(
                    kappa_numerator > 0,
                    f"positive kappa numerator failed at k={k}, n={n}",
                )
                _require(
                    alpha**2 < 4 * q_squared,
                    f"kappa<1/k comparison failed at k={k}, n={n}",
                )
            else:
                _require(
                    kappa_numerator < 0,
                    f"pre-domain kappa sign failed at k={k}, n={n}",
                )
            _require(
                Fraction(1, n - 1) < c,
                f"positive rationalization factor failed at k={k}, n={n}",
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


def chain_root(k: int, n: int, digits: int) -> mp.mpf:
    with mp.workdps(digits):
        order = shifted_supnick_tour(k, n)
        target = 2 * mp.pi
        lo = mp.mpf("0")
        hi = mp.mpf(max(1, n * n))
        for _ in range(20):
            hi_value, _ = chain_value_and_derivative(hi, order)
            if hi_value < target:
                break
            hi *= 2
        else:
            raise AssertionError(f"root upper bracket failed at k={k}, n={n}")

        current = hi / 2
        tolerance = mp.power(10, -(digits - 14))
        for _ in range(220):
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
        raise AssertionError(
            f"chain root did not converge at k={k}, n={n}, digits={digits}"
        )


def threshold_values(k: int, n: int) -> tuple[mp.mpf, mp.mpf] | None:
    if n < 4 * k + 1:
        return None
    c = mp.mpf(1) / k
    alpha = mp.mpf(1) / n + mp.mpf(1) / (n - 1)
    beta = mp.mpf(1) / (n * (n - 1))
    q = mp.sqrt(alpha / k + beta)
    direct_kappa = c + alpha - 2 * q
    numerator = (c - alpha) ** 2 - 4 * beta
    stable_kappa = numerator / (c + alpha + 2 * q)
    _require(stable_kappa > 0, f"nonpositive numeric kappa at k={k}, n={n}")
    return 1 / stable_kappa, abs(direct_kappa - stable_kappa)


def scan(
    max_k: int, extra: int, digits: int
) -> dict[tuple[int, int], dict[str, mp.mpf | None]]:
    rows: dict[tuple[int, int], dict[str, mp.mpf | None]] = {}
    with mp.workdps(digits):
        for k in range(1, max_k + 1):
            stop = 4 * k + 1 + extra
            for n in range(k + 2, stop + 1):
                root = chain_root(k, n, digits)
                deficit = (
                    theta(root, n, k)
                    + theta(root, k, n - 1)
                    - theta(root, n, n - 1)
                )
                alpha = mp.mpf(1) / n + mp.mpf(1) / (n - 1)
                beta = mp.mpf(1) / (n * (n - 1))
                pocket_gap = (
                    1 / root
                    + alpha
                    + 2 * mp.sqrt(alpha / root + beta)
                    - mp.mpf(1) / k
                )
                threshold_data = threshold_values(k, n)
                threshold = None if threshold_data is None else +threshold_data[0]
                kappa_delta = (
                    None if threshold_data is None else +threshold_data[1]
                )
                rows[(k, n)] = {
                    "R": +root,
                    "T": threshold,
                    "deficit": +deficit,
                    "pocket_gap": +pocket_gap,
                    "kappa_delta": kappa_delta,
                }
    return rows


def _sign_with_tolerance(value: mp.mpf, tolerance: mp.mpf) -> int:
    if abs(value) <= tolerance:
        return 0
    return 1 if value > 0 else -1


def check_numeric_scan(
    max_k: int,
    extra: int,
    digits: int,
    stability_digits: int,
) -> tuple[
    dict[tuple[int, int], dict[str, mp.mpf | None]],
    mp.mpf,
    mp.mpf,
    mp.mpf,
    dict[int, int | None],
    list[tuple[int, int]],
]:
    base = scan(max_k, extra, digits)
    higher = scan(max_k, extra, stability_digits)
    comparison_tolerance = mp.power(10, -min(25, digits // 2))
    sign_tolerance = mp.power(10, -min(25, stability_digits // 2))
    max_relative_root_delta = mp.mpf("0")
    max_absolute_deficit_delta = mp.mpf("0")
    max_kappa_formula_delta = mp.mpf("0")
    first_negative: dict[int, int | None] = {}
    inconclusive: list[tuple[int, int]] = []

    with mp.workdps(stability_digits):
        for key, high_row in higher.items():
            base_row = base[key]
            base_root = mp.mpf(base_row["R"])
            high_root = mp.mpf(high_row["R"])
            base_deficit = mp.mpf(base_row["deficit"])
            high_deficit = mp.mpf(high_row["deficit"])
            max_relative_root_delta = max(
                max_relative_root_delta,
                abs(base_root - high_root) / max(1, abs(high_root)),
            )
            max_absolute_deficit_delta = max(
                max_absolute_deficit_delta,
                abs(base_deficit - high_deficit),
            )
            base_sign = _sign_with_tolerance(base_deficit, sign_tolerance)
            high_sign = _sign_with_tolerance(high_deficit, sign_tolerance)
            if base_sign and high_sign:
                _require(base_sign == high_sign, f"precision-dependent sign at {key}")

            kappa_delta = high_row["kappa_delta"]
            if kappa_delta is not None:
                max_kappa_formula_delta = max(
                    max_kappa_formula_delta, mp.mpf(kappa_delta)
                )

        _require(
            max_relative_root_delta < comparison_tolerance,
            "root precision stability failed: "
            f"{max_relative_root_delta} >= {comparison_tolerance}",
        )
        _require(
            max_absolute_deficit_delta < comparison_tolerance,
            "deficit precision stability failed: "
            f"{max_absolute_deficit_delta} >= {comparison_tolerance}",
        )
        _require(
            max_kappa_formula_delta < comparison_tolerance,
            "direct/stable kappa comparison failed: "
            f"{max_kappa_formula_delta} >= {comparison_tolerance}",
        )

        for k in range(1, max_k + 1):
            stop = 4 * k + 1 + extra
            previous_root: mp.mpf | None = None
            previous_threshold: mp.mpf | None = None
            previous_difference: mp.mpf | None = None
            seen_negative = False
            first_negative[k] = None
            for n in range(k + 2, stop + 1):
                row = higher[(k, n)]
                root = mp.mpf(row["R"])
                deficit = mp.mpf(row["deficit"])
                pocket_gap = mp.mpf(row["pocket_gap"])
                deficit_sign = _sign_with_tolerance(deficit, sign_tolerance)
                pocket_sign = _sign_with_tolerance(pocket_gap, sign_tolerance)

                if previous_root is not None:
                    _require(root > previous_root, f"root growth failed at k={k}, n={n}")
                previous_root = root

                if deficit_sign == 0 or pocket_sign == 0:
                    inconclusive.append((k, n))
                else:
                    _require(
                        deficit_sign == pocket_sign,
                        f"Descartes sign mismatch at k={k}, n={n}",
                    )

                threshold = row["T"]
                if n <= 4 * k:
                    _require(threshold is None, f"unexpected threshold at k={k}, n={n}")
                    _require(
                        deficit_sign > 0 and pocket_sign > 0,
                        f"pre-domain positive sign failed at k={k}, n={n}",
                    )
                    continue

                _require(threshold is not None, f"missing threshold at k={k}, n={n}")
                threshold_value = mp.mpf(threshold)
                difference = root - threshold_value
                difference_sign = _sign_with_tolerance(difference, sign_tolerance)
                if previous_threshold is not None:
                    _require(
                        threshold_value < previous_threshold,
                        f"threshold decrease failed at k={k}, n={n}",
                    )
                    _require(
                        difference > mp.mpf(previous_difference),
                        f"R-T growth failed at k={k}, n={n}",
                    )
                previous_threshold = threshold_value
                previous_difference = difference

                if deficit_sign and difference_sign:
                    _require(
                        deficit_sign == -difference_sign,
                        f"root/threshold sign mismatch at k={k}, n={n}",
                    )
                if deficit_sign < 0:
                    if first_negative[k] is None:
                        first_negative[k] = n
                    seen_negative = True
                elif seen_negative and deficit_sign > 0:
                    raise AssertionError(
                        f"finite persistence failure at k={k}, n={n}"
                    )

    return (
        higher,
        max_relative_root_delta,
        max_absolute_deficit_delta,
        max_kappa_formula_delta,
        first_negative,
        inconclusive,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-k", type=int, default=8)
    parser.add_argument("--extra", type=int, default=24)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--stability-digits", type=int, default=90)
    args = parser.parse_args()
    if args.max_k < 1:
        parser.error("--max-k must be at least 1")
    if args.extra < 1:
        parser.error("--extra must be at least 1")
    if args.digits < 40:
        parser.error("--digits must be at least 40")
    if args.stability_digits <= args.digits:
        parser.error("--stability-digits must exceed --digits")

    check_exact_algebra(args.max_k, args.extra)
    check_order_conventions(args.max_k, args.extra)
    (
        _,
        max_root_delta,
        max_deficit_delta,
        max_kappa_delta,
        first_negative,
        inconclusive,
    ) = check_numeric_scan(
        args.max_k,
        args.extra,
        args.digits,
        args.stability_digits,
    )

    print("independent_of_production=PASS (no ringmin imports)")
    print(f"exact_algebra_and_domain=PASS k=1..{args.max_k}")
    print(
        "shifted_order_conventions_and_edges=PASS "
        f"k=1..{args.max_k} through n=4k+1+{args.extra}"
    )
    print(
        "diagnostic_root_threshold_deficit_scan=PASS "
        f"digits={args.digits}/{args.stability_digits}"
    )
    print(
        "precision_stability=PASS "
        f"max_relative_R_delta={mp.nstr(max_root_delta, 8)} "
        f"max_absolute_deficit_delta={mp.nstr(max_deficit_delta, 8)} "
        f"max_direct_stable_kappa_delta={mp.nstr(max_kappa_delta, 8)}"
    )
    for k in range(1, args.max_k + 1):
        observed = first_negative[k]
        observed_text = "NONE" if observed is None else str(observed)
        print(
            f"k={k:03d} physical_domain_start={4*k+1} "
            f"first_negative_observed_in_finite_scan={observed_text}"
        )
    if inconclusive:
        formatted = ",".join(f"({k},{n})" for k, n in inconclusive)
        print(f"near_zero_equality_or_inconclusive={formatted}")
    else:
        print("near_zero_equality_or_inconclusive=NONE")
    print(
        "classification=FINITE_DIAGNOSTIC_ONLY; "
        "no exact onset for k>=3 is inferred"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
