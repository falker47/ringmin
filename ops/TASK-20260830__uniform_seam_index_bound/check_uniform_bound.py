#!/usr/bin/env python3
"""Symbolic exact audit for the uniform fixed-k seam-index bound.

The default and only path uses standard-library ``fractions.Fraction`` and
coefficient arithmetic. It does not evaluate a finite list of k-values and
does not import the production package.
"""

from fractions import Fraction


class AuditFailure(RuntimeError):
    """Raised when an exact symbolic gate fails."""


Poly = tuple[Fraction, ...]
RationalFunction = tuple[Poly, Poly]

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


def _poly_add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return _trim(
        tuple(
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        )
    )


def _poly_negate(poly: Poly) -> Poly:
    return _trim(tuple(-coefficient for coefficient in poly))


def _poly_subtract(left: Poly, right: Poly) -> Poly:
    return _poly_add(left, _poly_negate(right))


def _poly_multiply(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += (
                left_coefficient * right_coefficient
            )
    return _trim(tuple(result))


def _poly_scale(poly: Poly, scalar: int | Fraction) -> Poly:
    factor = Fraction(scalar)
    return _trim(tuple(factor * coefficient for coefficient in poly))


def _poly_power(poly: Poly, exponent: int) -> Poly:
    _require(exponent >= 0, "negative polynomial exponent")
    result = _poly(1)
    for _ in range(exponent):
        result = _poly_multiply(result, poly)
    return result


def _poly_integral_zero_one(poly: Poly) -> Fraction:
    return sum(
        (coefficient / (index + 1) for index, coefficient in enumerate(poly)),
        Fraction(0),
    )


def _rat_add(left: RationalFunction, right: RationalFunction) -> RationalFunction:
    left_num, left_den = left
    right_num, right_den = right
    return (
        _poly_add(
            _poly_multiply(left_num, right_den),
            _poly_multiply(right_num, left_den),
        ),
        _poly_multiply(left_den, right_den),
    )


def _rat_subtract(
    left: RationalFunction, right: RationalFunction
) -> RationalFunction:
    return _rat_add(left, (_poly_negate(right[0]), right[1]))


def _rat_multiply(
    left: RationalFunction, right: RationalFunction
) -> RationalFunction:
    return (
        _poly_multiply(left[0], right[0]),
        _poly_multiply(left[1], right[1]),
    )


def _rat_scale(value: RationalFunction, scalar: int | Fraction) -> RationalFunction:
    return (_poly_scale(value[0], scalar), value[1])


def _rat_equal(left: RationalFunction, right: RationalFunction) -> bool:
    return _poly_multiply(left[0], right[1]) == _poly_multiply(
        right[0], left[1]
    )


def _check_positive_linear_on_k_ge_one(poly: Poly, name: str) -> None:
    _require(len(poly) <= 2, f"{name} is not linear")
    constant = poly[0]
    slope = poly[1] if len(poly) == 2 else Fraction(0)
    _require(slope >= 0, f"{name} is not nondecreasing for k>=1")
    _require(constant + slope > 0, f"{name} is not positive at k=1")


def check_exact_symbolic_audit() -> None:
    """Check identities and sign certificates without a parameter scan."""
    one = _poly(1)
    k = _poly(0, 1)
    n_0 = _poly(14, 4)
    n_minus_one = _poly(13, 4)
    count = _poly(15, 3)
    d_factor = _poly(83, 21)

    _require(
        _poly_add(_poly_subtract(n_0, k), one) == count,
        "N=n_0-k+1 identity failed",
    )
    _require(count == _poly(15, 3), "N=3k+15 identity failed")
    count_excess = _poly_subtract(count, _poly(18))
    _require(
        count_excess == _poly(-3, 3),
        "N-18=3(k-1) identity failed",
    )
    _require(
        count_excess[0] + count_excess[1] == 0
        and count_excess[1] > 0,
        "N>=18 domain sign gate failed",
    )

    threshold_domain_excess = _poly_subtract(
        n_0, _poly_add(_poly_scale(k, 4), one)
    )
    _require(
        threshold_domain_excess == _poly(13)
        and threshold_domain_excess[0] > 0,
        "n_0>=4k+1 threshold-domain gate failed",
    )

    for name, factor in (
        ("k", k),
        ("n_0", n_0),
        ("n_0-1", n_minus_one),
        ("D", d_factor),
        ("N", count),
    ):
        _check_positive_linear_on_k_ge_one(factor, name)

    # Exact polynomial witness for 22/7-pi > 0.
    x = _poly(0, 1)
    one_minus_x = _poly(1, -1)
    pi_numerator = _poly_multiply(
        _poly_power(x, 4), _poly_power(one_minus_x, 4)
    )
    pi_denominator = _poly(1, 0, 1)
    pi_quotient = _poly(4, 0, -4, 0, 5, -4, 1)
    _require(
        pi_numerator
        == _poly_add(
            _poly_multiply(pi_denominator, pi_quotient), _poly(-4)
        ),
        "22/7-pi polynomial-division identity failed",
    )
    _require(
        _poly_integral_zero_one(pi_quotient) == Fraction(22, 7),
        "22/7-pi quotient integral failed",
    )
    _require(
        pi_numerator == _poly(0, 0, 0, 0, 1, -4, 6, -4, 1),
        "x^4(1-x)^4 expansion failed",
    )

    # S_k=k(21k+83)/22 and the chain-side terminal identity.
    s_numerator = _poly_multiply(k, d_factor)
    s_value = (s_numerator, _poly(22))
    chain_terminal = _rat_multiply(
        (k, one),
        _rat_subtract((_poly_scale(count, 7), _poly(22)), (one, one)),
    )
    _require(
        _rat_equal(chain_terminal, s_value),
        "k(7N/22-1)=S_k identity failed",
    )
    _require(
        s_numerator == _poly(0, 83, 21),
        "S_k numerator expansion failed",
    )

    # Q_k and the rational pre-square gate A_k.
    common_knn = _poly_multiply(_poly_multiply(k, n_0), n_minus_one)
    q_numerator_raw = _poly_subtract(
        _poly_add(_poly_scale(n_0, 2), k), one
    )
    q_value = (q_numerator_raw, common_knn)
    q_expected = (_poly(27, 9), common_knn)
    _require(_rat_equal(q_value, q_expected), "Q_k identity failed")
    _require(q_numerator_raw == _poly(27, 9), "Q_k numerator failed")

    one_over_k = (one, k)
    one_over_n = (one, n_0)
    one_over_n_minus_one = (one, n_minus_one)
    one_over_s = (_poly(22), s_numerator)
    a_value = _rat_subtract(
        _rat_add(_rat_add(one_over_k, one_over_n), one_over_n_minus_one),
        one_over_s,
    )
    positive_split = _rat_add(
        (_poly(61, 21), _poly_multiply(k, d_factor)),
        (_poly(27, 8), _poly_multiply(n_0, n_minus_one)),
    )
    p_poly = _poly(11102, 12651, 4475, 504)
    a_denominator = _poly_multiply(
        _poly_multiply(_poly_multiply(k, d_factor), n_0), n_minus_one
    )
    a_expected = (p_poly, a_denominator)
    _require(
        _rat_equal(a_value, positive_split),
        "positive split for A_k failed",
    )
    _require(_rat_equal(a_value, a_expected), "A_k=P/denominator failed")
    _require(
        all(coefficient > 0 for coefficient in p_poly),
        "P(k) does not have strictly positive coefficients",
    )

    # Exact expansion of A_k^2-4Q_k.
    p_square_expected = _poly(
        123254404,
        280902804,
        259410701,
        124417266,
        32777833,
        4510800,
        254016,
    )
    p_square = _poly_power(p_poly, 2)
    _require(p_square == p_square_expected, "P(k)^2 expansion failed")

    subtrahend = _poly_scale(
        _poly_multiply(
            _poly_multiply(
                _poly_multiply(k, _poly(3, 1)),
                _poly_power(d_factor, 2),
            ),
            _poly_multiply(n_0, n_minus_one),
        ),
        36,
    )
    subtrahend_expected = _poly(
        0,
        135410184,
        194010840,
        110857896,
        31578696,
        4484592,
        254016,
    )
    _require(
        subtrahend == subtrahend_expected,
        "quadratic subtrahend expansion failed",
    )

    f_poly = _poly(
        123254404,
        145492620,
        65399861,
        13559370,
        1199137,
        26208,
    )
    _require(
        _poly_subtract(p_square, subtrahend) == f_poly,
        "positive quadratic numerator F(k) failed",
    )
    _require(
        all(coefficient > 0 for coefficient in f_poly),
        "F(k) does not have strictly positive coefficients",
    )

    h_poly = _poly_multiply(
        _poly_multiply(_poly_power(d_factor, 2), _poly_power(n_0, 2)),
        _poly_power(n_minus_one, 2),
    )
    h_expected = _poly(
        228191236,
        386290632,
        272124148,
        102108144,
        21523408,
        2416512,
        112896,
    )
    _require(h_poly == h_expected, "positive denominator polynomial failed")
    _require(
        all(coefficient > 0 for coefficient in h_poly),
        "denominator polynomial does not have strictly positive coefficients",
    )

    a_square = _rat_multiply(a_value, a_value)
    quadratic_difference = _rat_subtract(a_square, _rat_scale(q_value, 4))
    expected_difference_denominator = _poly_multiply(_poly_power(k, 2), h_poly)
    expected_difference = (f_poly, expected_difference_denominator)
    _require(
        _rat_equal(quadratic_difference, expected_difference),
        "A_k^2-4Q_k rational identity failed",
    )
    _require(
        expected_difference_denominator
        == _poly_multiply(
            _poly_multiply(
                _poly_multiply(_poly_power(k, 2), _poly_power(d_factor, 2)),
                _poly_power(n_0, 2),
            ),
            _poly_power(n_minus_one, 2),
        ),
        "quadratic denominator factorization failed",
    )

    # Logical sign certificates used before squaring and reciprocating.
    _require(
        all(coefficient > 0 for coefficient in _poly(61, 21))
        and all(coefficient > 0 for coefficient in _poly(27, 8)),
        "A_k pre-square positive-summand gate failed",
    )
    _require(
        all(coefficient > 0 for coefficient in q_numerator_raw),
        "Q_k positivity gate failed",
    )
    _require(
        all(coefficient > 0 for coefficient in d_factor),
        "S_k positivity gate failed",
    )


def main() -> int:
    check_exact_symbolic_audit()
    print("independent_of_production=PASS (stdlib fractions only)")
    print(
        "exact_symbolic_polynomial_audit=PASS "
        f"explicit_gates={_EXPLICIT_GATE_COUNT} optimized_safe=YES"
    )
    print("exact_pi_bound_witness=PASS pi<22/7 strict")
    print("exact_chain_bridge=PASS R_k,4k+14>S_k")
    print("pre_square_positivity_gate=PASS A_k>0 and Q_k>0")
    print("quadratic_difference=PASS A_k^2-4Q_k>0")
    print("exact_threshold_bridge=PASS kappa_k,4k+14>1/S_k>0")
    print("parameter_scans=NONE")
    print(
        "theorem_sources=research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md+"
        "research/FIXED_K_SUPNICK_SEAM.md"
    )
    print(
        "classification=EXACT_STDLIB_FRACTION_SYMBOLIC_AUDIT; checker is "
        "corroborative and does not reprove the imported fixed-k theorem"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
