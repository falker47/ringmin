#!/usr/bin/env python3
"""Exact symbolic audit for the eventual fixed-k Supnick seam onset.

The default and only path uses standard-library ``fractions.Fraction`` and
coefficient arithmetic. It performs no scan over k or n and imports no
production package. Analytic convergence and the imported fixed-k theorem
remain proof dependencies rather than claims of this checker.
"""

from fractions import Fraction


class AuditFailure(RuntimeError):
    """Raised when an exact symbolic gate fails."""


Poly = tuple[Fraction, ...]

_EXPLICIT_GATE_COUNT = 0


def _require(condition: bool, message: str) -> None:
    global _EXPLICIT_GATE_COUNT
    _EXPLICIT_GATE_COUNT += 1
    if not condition:
        raise AuditFailure(message)


def _trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) or (Fraction(0),)


def _poly(*coefficients: int | Fraction) -> Poly:
    return _trim(tuple(Fraction(value) for value in coefficients))


def _add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return _trim(
        tuple(
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        )
    )


def _scale(poly: Poly, scalar: int | Fraction) -> Poly:
    factor = Fraction(scalar)
    return _trim(tuple(factor * coefficient for coefficient in poly))


def _multiply(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += (
                left_coefficient * right_coefficient
            )
    return _trim(tuple(result))


def _power(poly: Poly, exponent: int) -> Poly:
    _require(exponent >= 0, "negative polynomial exponent")
    result = _poly(1)
    for _ in range(exponent):
        result = _multiply(result, poly)
    return result


def _integral_zero_one(poly: Poly) -> Fraction:
    return sum(
        (coefficient / (index + 1) for index, coefficient in enumerate(poly)),
        Fraction(0),
    )


def _check_parity_and_endpoints() -> None:
    parity_cases = (
        (5, 0, 0, "even"),
        (5, 1, 1, "odd"),
        (6, 1, 0, "even"),
        (6, 0, 1, "odd"),
    )
    for c_value, k_parity, expected_n_parity, expected_formula in parity_cases:
        actual_n_parity = (3 * k_parity + c_value + 1) % 2
        _require(
            actual_n_parity == expected_n_parity,
            f"parity class failed for c={c_value}, k parity={k_parity}",
        )
        _require(
            expected_formula == ("even" if actual_n_parity == 0 else "odd"),
            f"parity formula label failed for c={c_value}",
        )

    k = _poly(0, 1)
    for c_value in (5, 6):
        h_even = _poly(Fraction(c_value + 1, 2), Fraction(3, 2))
        h_odd = _poly(Fraction(c_value, 2), Fraction(3, 2))
        five_k = _scale(k, 5)

        even_first_twice = _scale(_add(_add(k, h_even), _poly(-2)), 2)
        even_second_twice = _scale(_add(_add(k, h_even), _poly(-1)), 2)
        odd_first_twice = _scale(_add(_add(k, h_odd), _poly(-1)), 2)
        odd_second_twice = _scale(_add(k, h_odd), 2)

        _require(
            _add(even_first_twice, _scale(five_k, -1))
            == _poly(c_value - 3),
            f"even first endpoint failed for c={c_value}",
        )
        _require(
            _add(even_second_twice, _scale(five_k, -1))
            == _poly(c_value - 1),
            f"even second endpoint failed for c={c_value}",
        )
        _require(
            _add(odd_first_twice, _scale(five_k, -1))
            == _poly(c_value - 2),
            f"odd first endpoint failed for c={c_value}",
        )
        _require(
            _add(odd_second_twice, _scale(five_k, -1)) == _poly(c_value),
            f"odd second endpoint failed for c={c_value}",
        )
        _require(
            8 >= c_value + 1 and 8 >= c_value,
            f"k>=8 edge-count/radius domain failed for c={c_value}",
        )

    per_long_sum = Fraction(21, 2) + Fraction(3, 4) + Fraction(25, 2)
    _require(per_long_sum == Fraction(95, 4), "Riemann error total failed")
    _require(
        2 * per_long_sum + 10 == Fraction(115, 2) < 58,
        "uniform weight-sum constant failed",
    )


def _check_threshold_factorization() -> None:
    t = _poly(0, 1)
    explicit_h = {
        5: _poly(288, 969, 1080, 400),
        6: _poly(352, 1449, 1980, 900),
    }

    for c_value in (5, 6):
        a_poly = _poly(4, c_value)
        b_poly = _poly(4, c_value - 1)
        g_poly = _poly(9, 2 * c_value - 1)
        ab_poly = _multiply(a_poly, b_poly)
        u_poly = _add(_add(ab_poly, a_poly), b_poly)

        left = _add(
            _power(u_poly, 2),
            _scale(_multiply(_multiply(a_poly, b_poly), g_poly), -4),
        )
        h_formula = _poly(
            32 * (2 * c_value - 1),
            48 * c_value * (c_value - 1) + 9,
            6 * c_value * (c_value - 1) * (2 * c_value - 1),
            c_value * c_value * (c_value - 1) * (c_value - 1),
        )
        _require(
            left == _multiply(t, h_formula),
            f"threshold conjugate factorization failed for c={c_value}",
        )
        _require(
            h_formula == explicit_h[c_value],
            f"threshold H transcription failed for c={c_value}",
        )
        _require(
            all(coefficient > 0 for coefficient in h_formula),
            f"threshold H positivity failed for c={c_value}",
        )
        _require(
            h_formula[0] / 768 == Fraction(2 * c_value - 1, 24),
            f"threshold limit failed for c={c_value}",
        )

        ab_excess = _add(ab_poly, _poly(-16))
        abg_excess = _add(_multiply(ab_poly, g_poly), _poly(-144))
        u_excess = _add(u_poly, _poly(-24))
        _require(
            all(value >= 0 for value in ab_excess),
            f"AB coefficient signs failed for c={c_value}",
        )
        _require(
            all(value >= 0 for value in abg_excess),
            f"ABG coefficient signs failed for c={c_value}",
        )
        _require(
            all(value >= 0 for value in u_excess),
            f"U coefficient signs failed for c={c_value}",
        )
        _require(
            sum(ab_excess, Fraction(0)) <= 74,
            f"AB uniform bound failed for c={c_value}",
        )
        _require(
            sum(abg_excess, Fraction(0)) <= 1656,
            f"ABG uniform bound failed for c={c_value}",
        )
        _require(
            sum(u_excess, Fraction(0)) <= 85,
            f"U uniform bound failed for c={c_value}",
        )
        _require(
            sum(h_formula[1:], Fraction(0)) <= 4329,
            f"H uniform bound failed for c={c_value}",
        )

    _require(1800 < 43**2, "uniform square-root upper gate failed")
    _require(Fraction(2 * 1656, 24) == 138, "square-root error failed")
    _require(74 * 195 + 16 * (85 + 138) == 17998 < 18000,
             "Q uniform error failed")
    ratio_error = Fraction(4329, 768) + Fraction(352 * 18000, 768**2)
    _require(ratio_error == Fraction(4193, 256), "ratio error identity failed")
    _require(ratio_error < 17, "ratio error strict bound failed")
    _require(Fraction(17, 91) < Fraction(3, 16),
             "reciprocal lower gate failed")
    _require(
        Fraction(17, 1) / (Fraction(3, 16) * Fraction(3, 8))
        == Fraction(2176, 9),
        "reciprocal error constant failed",
    )
    _require(Fraction(24, 9) == Fraction(8, 3), "c=5 limit failed")
    _require(Fraction(24, 11) < Fraction(8, 3), "endpoint order failed")


def _check_rho_certificate() -> None:
    x = _poly(0, 1)
    one_plus_x_squared = _poly(1, 0, 1)

    # Exact polynomial division behind 22/7-pi > 0.
    one_minus_x = _poly(1, -1)
    pi_positive_numerator = _multiply(_power(x, 4), _power(one_minus_x, 4))
    pi_quotient = _poly(4, 0, -4, 0, 5, -4, 1)
    _require(
        pi_positive_numerator
        == _add(_multiply(one_plus_x_squared, pi_quotient), _poly(-4)),
        "pi upper-bound polynomial division failed",
    )
    _require(
        _integral_zero_one(pi_quotient) == Fraction(22, 7),
        "pi upper-bound quotient integral failed",
    )

    # Signed geometric remainder behind pi>3.
    pi_lower_poly = _poly(1, 0, -1, 0, 1, 0, -1, 0,
                          1, 0, -1, 0, 1, 0, -1)
    x_sixteen = _power(x, 16)
    _require(
        _add(_multiply(one_plus_x_squared, pi_lower_poly), x_sixteen)
        == _poly(1),
        "pi lower-bound geometric identity failed",
    )
    pi_lower_sum = sum(
        ((-1) ** index * Fraction(1, 2 * index + 1) for index in range(8)),
        Fraction(0),
    )
    _require(
        pi_lower_sum == Fraction(33976, 45045),
        "pi lower-bound integral failed",
    )
    _require(
        pi_lower_sum - Fraction(3, 4) == Fraction(769, 180180) > 0,
        "pi>3 strict margin failed",
    )

    # Signed geometric remainder behind the lower bound for atan(3/4).
    alpha_lower_poly = _poly(1, 0, -1, 0, 1, 0, -1)
    x_eight = _power(x, 8)
    _require(
        _add(_multiply(one_plus_x_squared, alpha_lower_poly), x_eight)
        == _poly(1),
        "alpha geometric identity failed",
    )
    endpoint = Fraction(3, 4)
    alpha_lower = (
        endpoint
        - endpoint**3 / 3
        + endpoint**5 / 5
        - endpoint**7 / 7
    )
    _require(
        alpha_lower == Fraction(365721, 573440),
        "alpha lower rational failed",
    )
    _require(alpha_lower < endpoint, "alpha interval order failed")

    lower_margin = 132 + 275 * alpha_lower - 96 * Fraction(22, 7)
    upper_margin = 32 * 3 - 36 - 75 * endpoint
    _require(
        lower_margin == Fraction(650463, 114688) > 0,
        "rho>24/11 exact margin failed",
    )
    _require(
        upper_margin == Fraction(15, 4) > 0,
        "rho<8/3 exact margin failed",
    )
    _require(
        Fraction(25, 4) - Fraction(3, 2) ** 2 == 4,
        "circular-segment endpoint failed",
    )


def check_exact_symbolic_audit() -> None:
    """Run every exact gate without a parameter scan."""
    _check_parity_and_endpoints()
    _check_threshold_factorization()
    _check_rho_certificate()


def main() -> int:
    check_exact_symbolic_audit()
    print("independent_of_production=PASS (stdlib fractions only)")
    print(
        "parity_endpoint_audit=PASS "
        "c_cases=2 parity_subsequences=4 parameter_scans=NONE"
    )
    print("threshold_conjugate_factorization=PASS c=5,6")
    print("uniform_threshold_denominator_bounds=PASS error_lt_17/k")
    print("exact_rho_interval=PASS 24/11<rho<8/3")
    print(
        "exact_symbolic_audit=PASS "
        f"explicit_gates={_EXPLICIT_GATE_COUNT} optimized_safe=YES"
    )
    print(
        "classification=EXACT_STDLIB_FRACTION_SYMBOLIC_AUDIT; checker is "
        "corroborative and does not mechanize analytic convergence or the "
        "imported fixed-k theorem"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
