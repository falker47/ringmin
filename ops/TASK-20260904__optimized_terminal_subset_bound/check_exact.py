"""Independent exact/finite audit for the optimized terminal-subset bound.

Uses only the standard library and does not import production or proof-note
code. Analytic convergence and optimization uniqueness remain arguments in
the proof note; this script corroborates the parity convention and supplies
exact rational brackets for the reported optimizer diagnostics.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F
from math import factorial


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def canonical_rank_tour(size: int) -> list[int]:
    h = (size + 1) // 2
    left: list[int] = []
    right: list[int] = []
    j = 0
    while True:
        changed = False
        low = 1 + 2 * j
        high = size - 1 - 2 * j
        if low <= h:
            left.append(low)
            changed = True
        if high > h:
            left.append(high)
            changed = True
        if not changed:
            break
        j += 1
    j = 0
    while True:
        changed = False
        low = 2 + 2 * j
        high = size - 2 - 2 * j
        if low <= h:
            right.append(low)
            changed = True
        if high > h:
            right.append(high)
            changed = True
        if not changed:
            break
        j += 1
    tour = left + list(reversed(right)) + [size]
    require(sorted(tour) == list(range(1, size + 1)), "rank partition")
    return tour


def cycle_edges(values: list[int]) -> set[tuple[int, int]]:
    return {
        tuple(sorted((values[i], values[(i + 1) % len(values)])))
        for i in range(len(values))
    }


def formula_edges(k: int, n: int) -> set[tuple[int, int]]:
    size = n - k + 1
    h = size // 2
    if size % 2 == 0:
        edges = {(k, n), (k + h - 1, k + h)}
        edges.update((i, n + k - 1 - i) for i in range(k, k + h - 1))
        edges.update((i, n + k + 1 - i) for i in range(k + 1, k + h))
    else:
        edges = {(k, n)}
        edges.update((i, n + k - 1 - i) for i in range(k, k + h))
        edges.update((i, n + k + 1 - i) for i in range(k + 1, k + h + 1))
    return {tuple(sorted(edge)) for edge in edges}


def alternating_bounds(x: F, kind: str, pairs: int = 18) -> tuple[F, F]:
    """Return exact lower/upper Taylor bounds for sin, cos, or atan on (0,1)."""
    if kind == "sin":
        term = lambda j: (-1) ** j * x ** (2 * j + 1) / factorial(2 * j + 1)
    elif kind == "cos":
        term = lambda j: (-1) ** j * x ** (2 * j) / factorial(2 * j)
    elif kind == "atan":
        term = lambda j: (-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
    else:
        raise ValueError(kind)
    lower = sum((term(j) for j in range(2 * pairs)), F(0))
    upper = lower + term(2 * pairs)
    require(lower < upper, f"{kind} alternating orientation")
    return lower, upper


def decimal_string(value: F, digits: int = 28) -> str:
    getcontext().prec = digits
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def main() -> None:
    comparisons = 0
    for size in range(3, 301):
        for k in (1, 7, 53):
            n = k + size - 1
            tour = [k + rank - 1 for rank in canonical_rank_tour(size)]
            actual = cycle_edges(tour)
            expected = formula_edges(k, n)
            require(actual == expected, f"edge formula size={size} k={k}")
            require(len(expected) == size, f"edge count size={size} k={k}")
            comparisons += 1

    # The decreasing function cos(t)-t has its zero in this exact interval.
    scale = 10**14
    tau_lo = F(73908513321516, scale)
    tau_hi = F(73908513321517, scale)
    cos_lo, _ = alternating_bounds(tau_lo, "cos")
    _, cos_hi = alternating_bounds(tau_hi, "cos")
    require(cos_lo - tau_lo > 0, "tau lower sign")
    require(cos_hi - tau_hi < 0, "tau upper sign")

    sin_lo, _ = alternating_bounds(tau_lo, "sin")
    _, sin_hi = alternating_bounds(tau_hi, "sin")
    lambda_lo = (1 + sin_lo) / (1 - sin_lo)
    lambda_hi = (1 + sin_hi) / (1 - sin_hi)
    require(F(512767681049, 10**11) < lambda_lo < lambda_hi
            < F(512767681051, 10**11), "lambda diagnostic bracket")

    # Machin's identity, with directed alternating-series bounds for pi.
    atan5_lo, atan5_hi = alternating_bounds(F(1, 5), "atan")
    atan239_lo, atan239_hi = alternating_bounds(F(1, 239), "atan")
    pi_lo = 16 * atan5_lo - 4 * atan239_hi
    pi_hi = 16 * atan5_hi - 4 * atan239_lo
    require(F(31415926535897, 10**13) < pi_lo < pi_hi
            < F(31415926535899, 10**13), "pi bracket")

    coefficient_lo = tau_lo / (pi_hi * (1 + sin_hi))
    coefficient_hi = tau_hi / (pi_lo * (1 + sin_lo))
    require(F(1405690808452, 10**13) < coefficient_lo < coefficient_hi
            < F(1405690808454, 10**13), "coefficient diagnostic bracket")

    print(f"supnick_parity_edge_sets=PASS comparisons={comparisons} sizes=3..300")
    print("tau_root_exact_signs=PASS interval=[0.73908513321516,0.73908513321517]")
    print("lambda_interval=[" + decimal_string(lambda_lo) + ","
          + decimal_string(lambda_hi) + "]")
    print("coefficient_interval=[" + decimal_string(coefficient_lo) + ","
          + decimal_string(coefficient_hi) + "]")
    print("classification=EXACT_RATIONAL_AND_FINITE_AUDIT; analytic limits and imported Supnick theorem are not mechanized")


if __name__ == "__main__":
    main()
