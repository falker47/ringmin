#!/usr/bin/env python3
"""Exact audit for the effective fixed-k Supnick seam cutoff.

The proof path uses only standard-library ``fractions.Fraction`` and exact
coefficient arithmetic. It scans neither k nor n. The optional mutation audit
changes constants in memory and verifies that the exact gates reject them.
"""

from fractions import Fraction
from pathlib import Path
import sys


class AuditFailure(RuntimeError):
    """Raised when an exact proof gate fails."""


Poly = tuple[Fraction, ...]

K_EFF = 4325
R5 = Fraction(13, 5)
R6 = Fraction(11, 5)
RHO_LOWER_SEPARATOR = Fraction(20, 9)
RHO_UPPER_SEPARATOR = Fraction(41, 16)
ALPHA_LOWER = Fraction(365721, 573440)

WEIGHT_BOUND = Fraction(58)
DENOMINATOR_ARGUMENT_COEFFICIENT = Fraction(25)
ANGLE_DENOMINATOR_COEFFICIENT = Fraction(50)
ANGLE_ARCSINE_COEFFICIENT = Fraction(250, 3)
CLOSURE_WEIGHT_COEFFICIENT = Fraction(116)
CLOSURE_DENOMINATOR_COEFFICIENT = Fraction(200)
CLOSURE_ARCSINE_COEFFICIENT = Fraction(1000, 3)

H_TAIL_BOUND = Fraction(4329)
Q_ERROR_BOUND = Fraction(18000)
Q_BASE = Fraction(768)
H_ZERO_MAX = Fraction(352)
THRESHOLD_ERROR_NUMERATOR = 4193
THRESHOLD_ERROR_DENOMINATOR = 256

EXPECTED_CORE_GATE_COUNT = 156
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


def _poly_scale(poly: Poly, scalar: int | Fraction) -> Poly:
    factor = Fraction(scalar)
    return _trim(tuple(factor * coefficient for coefficient in poly))


def _poly_multiply(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += (
                left_coefficient * right_coefficient
            )
    return _trim(tuple(result))


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


def _require_strict_positive(value: Fraction, message: str) -> None:
    _require(value > 0, message)


def _check_strict_fraction_order(
    left: Fraction,
    right: Fraction,
    expected_difference: Fraction,
    name: str,
) -> None:
    _require(
        left.denominator > 0 and right.denominator > 0,
        f"{name}: nonpositive normalized denominator",
    )
    cross_gap = (
        right.numerator * left.denominator
        - left.numerator * right.denominator
    )
    _require_strict_positive(
        Fraction(cross_gap), f"{name}: strict cross-product gap failed"
    )
    _require(
        Fraction(cross_gap, left.denominator * right.denominator)
        == expected_difference,
        f"{name}: cross-product difference transcription failed",
    )
    _require(right - left == expected_difference, f"{name}: exact difference failed")
    _require_strict_positive(
        expected_difference, f"{name}: expected difference is not strict"
    )


def _closure_error(radius_scale: Fraction, k_value: int) -> Fraction:
    k = Fraction(k_value)
    return (
        CLOSURE_WEIGHT_COEFFICIENT / radius_scale
        + CLOSURE_DENOMINATOR_COEFFICIENT / radius_scale**2
    ) / k + CLOSURE_ARCSINE_COEFFICIENT / (radius_scale**3 * k**2)


def _check_constants_and_domains() -> None:
    _require(K_EFF > 0, "K_eff positivity failed")
    _require(5 * R5 == 13, "r_5 transcription failed")
    _require(5 * R6 == 11, "r_6 transcription failed")
    _require(
        9 * RHO_LOWER_SEPARATOR == 20,
        "lower rho separator transcription failed",
    )
    _require(
        16 * RHO_UPPER_SEPARATOR == 41,
        "upper rho separator transcription failed",
    )
    _require(K_EFF >= 8, "closure k>=8 domain failed")
    _require(K_EFF >= 6 + 1, "N<=4k domain failed")
    _require(R5 * K_EFF == 11245 > 10, "r_5 k>=10 gate failed")
    _require(R6 * K_EFF == 9515 > 10, "r_6 k>=10 gate failed")
    _require(
        THRESHOLD_ERROR_DENOMINATOR * K_EFF
        - 104 * THRESHOLD_ERROR_NUMERATOR
        == 671128 > 0,
        "c=5 cutoff cross-product fingerprint failed",
    )
    _require(
        THRESHOLD_ERROR_DENOMINATOR * K_EFF
        - 264 * THRESHOLD_ERROR_NUMERATOR
        == 248 > 0,
        "c=6 critical cutoff cross-product fingerprint failed",
    )

    positive_fractions = (
        R5,
        R6,
        RHO_LOWER_SEPARATOR,
        RHO_UPPER_SEPARATOR,
        ALPHA_LOWER,
        WEIGHT_BOUND,
        DENOMINATOR_ARGUMENT_COEFFICIENT,
        ANGLE_DENOMINATOR_COEFFICIENT,
        ANGLE_ARCSINE_COEFFICIENT,
        CLOSURE_WEIGHT_COEFFICIENT,
        CLOSURE_DENOMINATOR_COEFFICIENT,
        CLOSURE_ARCSINE_COEFFICIENT,
        H_TAIL_BOUND,
        Q_ERROR_BOUND,
        Q_BASE,
        H_ZERO_MAX,
    )
    _require(
        all(value > 0 and value.denominator > 0 for value in positive_fractions),
        "positive constant/denominator manifest failed",
    )


def _check_denominator_arcsine_and_closure() -> None:
    # Exact rational fingerprints for the denominator and arcsine gates.
    z = _poly(0, 1)
    _require(
        _poly_multiply(_poly(1, 2), _poly(-1, 1))
        == _poly(-1, -1, 2),
        "denominator inequality factorization failed",
    )
    _require(
        Fraction(1) - Fraction(1, 2) ** 2 == Fraction(3, 4),
        "u<=1/2 square gate failed",
    )
    _require(
        Fraction(1, 2) ** 2 == Fraction(1, 4) < Fraction(3, 4),
        "nonnegative square-root lower gate failed",
    )
    _require(
        Fraction(1, 2) + Fraction(3, 4) == Fraction(5, 4) > 1,
        "arcsine integrand denominator gate failed",
    )
    _require(
        Fraction(1) * (Fraction(1) + 1) == 2,
        "radius-denominator minimum product failed",
    )
    _require(
        _poly(1, 2)[0] > 0
        and sum(_poly(1, 2), Fraction(0)) > 0
        and _poly(-1, 1)[0] <= 0
        and sum(_poly(-1, 1), Fraction(0)) <= 0,
        "denominator factor interval signs failed",
    )
    _require(
        _poly_subtract(_poly(1), z) == _poly(1, -1),
        "one-minus-factor identity failed",
    )

    per_long_error = Fraction(21, 2) + Fraction(3, 4) + Fraction(25, 2)
    _require(per_long_error == Fraction(95, 4), "Riemann error total failed")
    _require(
        2 * per_long_error + 10 == Fraction(115, 2) < WEIGHT_BOUND,
        "uniform weight bound failed",
    )
    _require(
        Fraction(5) * 10 / 2 == DENOMINATOR_ARGUMENT_COEFFICIENT,
        "denominator argument coefficient failed",
    )
    _require(
        2 * DENOMINATOR_ARGUMENT_COEFFICIENT
        == ANGLE_DENOMINATOR_COEFFICIENT,
        "angle denominator coefficient failed",
    )
    _require(
        2 * Fraction(5) ** 3 / 3 == ANGLE_ARCSINE_COEFFICIENT,
        "angle arcsine coefficient failed",
    )
    _require(
        2 * WEIGHT_BOUND == CLOSURE_WEIGHT_COEFFICIENT,
        "closure weight coefficient failed",
    )
    _require(
        4 * ANGLE_DENOMINATOR_COEFFICIENT
        == CLOSURE_DENOMINATOR_COEFFICIENT,
        "closure denominator coefficient failed",
    )
    _require(
        4 * ANGLE_ARCSINE_COEFFICIENT == CLOSURE_ARCSINE_COEFFICIENT,
        "closure arcsine coefficient failed",
    )

    cases = (
        (
            "c=5",
            R5,
            Fraction(12540, 169),
            Fraction(125000, 6591),
            Fraction(16922476, 986310195),
        ),
        (
            "c=6",
            R6,
            Fraction(11380, 121),
            Fraction(125000, 3993),
            Fraction(12994684, 597532485),
        ),
    )
    m = _poly(0, 1)
    k_plus_m = _poly(K_EFF, 1)
    for name, radius_scale, expected_a, expected_b, expected_at_k in cases:
        a_value = (
            CLOSURE_WEIGHT_COEFFICIENT / radius_scale
            + CLOSURE_DENOMINATOR_COEFFICIENT / radius_scale**2
        )
        b_value = CLOSURE_ARCSINE_COEFFICIENT / radius_scale**3
        _require(a_value == expected_a, f"{name}: A_r transcription failed")
        _require(b_value == expected_b, f"{name}: B_r transcription failed")
        _require(
            a_value > 0 and b_value > 0,
            f"{name}: closure error coefficient positivity failed",
        )

        # Cross-multiplied identity for E(K)-E(K+m), m>=0.
        left = _poly_add(
            _poly_add(
                _poly_scale(_poly_power(k_plus_m, 2), a_value * K_EFF),
                _poly_scale(_poly_power(k_plus_m, 2), b_value),
            ),
            _poly_add(
                _poly_scale(k_plus_m, -a_value * K_EFF**2),
                _poly(-b_value * K_EFF**2),
            ),
        )
        bracket = _poly_add(
            _poly_scale(k_plus_m, a_value * K_EFF),
            _poly(2 * b_value * K_EFF, b_value),
        )
        right = _poly_multiply(m, bracket)
        denominator = _poly_scale(_poly_power(k_plus_m, 2), K_EFF**2)
        _require(left == right, f"{name}: error monotonicity identity failed")
        _require(
            right[0] == 0 and all(value >= 0 for value in right),
            f"{name}: error monotonicity numerator sign failed",
        )
        _require(
            all(value > 0 for value in denominator),
            f"{name}: error monotonicity denominator sign failed",
        )
        _require(
            _closure_error(radius_scale, K_EFF) == expected_at_k,
            f"{name}: E_r(K) evaluation failed",
        )

    e5 = _closure_error(R5, K_EFF)
    e6 = _closure_error(R6, K_EFF)
    gap5 = 6 * (1 - RHO_UPPER_SEPARATOR / R5)
    gap6 = 6 * (RHO_LOWER_SEPARATOR / R6 - 1)
    _require(gap5 == Fraction(9, 104), "c=5 angular gap failed")
    _require(gap6 == Fraction(2, 33), "c=6 angular gap failed")
    _check_strict_fraction_order(
        e5,
        gap5,
        Fraction(547450327, 7890481560),
        "c=5 closure error margin",
    )
    _check_strict_fraction_order(
        e6,
        gap6,
        Fraction(7739802, 199177495),
        "c=6 closure error margin",
    )


def _check_rho_separators() -> None:
    x = _poly(0, 1)
    one_plus_x_squared = _poly(1, 0, 1)

    # Exact polynomial division behind pi<22/7.
    one_minus_x = _poly(1, -1)
    pi_numerator = _poly_multiply(
        _poly_power(x, 4), _poly_power(one_minus_x, 4)
    )
    pi_quotient = _poly(4, 0, -4, 0, 5, -4, 1)
    _require(
        pi_numerator
        == _poly_add(
            _poly_multiply(one_plus_x_squared, pi_quotient), _poly(-4)
        ),
        "pi upper polynomial division failed",
    )
    _require(
        _poly_integral_zero_one(pi_quotient) == Fraction(22, 7),
        "pi upper quotient integral failed",
    )

    # Exact signed remainder behind pi>3.
    pi_lower_poly = _poly(
        1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1
    )
    _require(
        _poly_add(
            _poly_multiply(one_plus_x_squared, pi_lower_poly),
            _poly_power(x, 16),
        )
        == _poly(1),
        "pi lower geometric identity failed",
    )
    pi_lower_sum = sum(
        ((-1) ** index * Fraction(1, 2 * index + 1) for index in range(8)),
        Fraction(0),
    )
    _require(
        pi_lower_sum == Fraction(33976, 45045),
        "pi lower integral failed",
    )
    _require(
        pi_lower_sum - Fraction(3, 4) == Fraction(769, 180180) > 0,
        "pi>3 strict margin failed",
    )

    # Exact signed remainder behind alpha>L, alpha=atan(3/4).
    alpha_lower_poly = _poly(1, 0, -1, 0, 1, 0, -1)
    _require(
        _poly_add(
            _poly_multiply(one_plus_x_squared, alpha_lower_poly),
            _poly_power(x, 8),
        )
        == _poly(1),
        "alpha lower geometric identity failed",
    )
    endpoint = Fraction(3, 4)
    alpha_lower = (
        endpoint
        - endpoint**3 / 3
        + endpoint**5 / 5
        - endpoint**7 / 7
    )
    _require(alpha_lower == ALPHA_LOWER, "alpha lower rational failed")
    _require(
        Fraction(25, 4) - Fraction(3, 2) ** 2 == 4,
        "3-4-5 circular endpoint failed",
    )
    _require(endpoint > 0, "alpha upper endpoint positivity failed")

    raw_lower = (12 + 25 * ALPHA_LOWER) / (4 * Fraction(22, 7))
    raw_upper = (12 + 25 * endpoint) / (4 * 3)
    _require(
        raw_lower == Fraction(291351, 131072),
        "raw lower rho separator failed",
    )
    _require(raw_upper == RHO_UPPER_SEPARATOR, "upper rho separator failed")
    _check_strict_fraction_order(
        RHO_LOWER_SEPARATOR,
        raw_lower,
        Fraction(719, 1179648),
        "coarsened lower rho separator",
    )
    _check_strict_fraction_order(
        R6,
        RHO_LOWER_SEPARATOR,
        Fraction(1, 45),
        "r_6 below rho separator",
    )
    _check_strict_fraction_order(
        RHO_LOWER_SEPARATOR,
        RHO_UPPER_SEPARATOR,
        Fraction(49, 144),
        "rho separator order",
    )
    _check_strict_fraction_order(
        RHO_UPPER_SEPARATOR,
        R5,
        Fraction(3, 80),
        "rho separator below r_5",
    )


def _check_threshold_and_inversion() -> None:
    t = _poly(0, 1)
    explicit_h = {
        5: _poly(288, 969, 1080, 400),
        6: _poly(352, 1449, 1980, 900),
    }

    for c_value in (5, 6):
        a_poly = _poly(4, c_value)
        b_poly = _poly(4, c_value - 1)
        g_poly = _poly(9, 2 * c_value - 1)
        ab_poly = _poly_multiply(a_poly, b_poly)
        u_poly = _poly_add(_poly_add(ab_poly, a_poly), b_poly)
        h_formula = _poly(
            32 * (2 * c_value - 1),
            48 * c_value * (c_value - 1) + 9,
            6 * c_value * (c_value - 1) * (2 * c_value - 1),
            c_value**2 * (c_value - 1) ** 2,
        )
        conjugate_left = _poly_subtract(
            _poly_power(u_poly, 2),
            _poly_scale(_poly_multiply(ab_poly, g_poly), 4),
        )
        _require(
            conjugate_left == _poly_multiply(t, h_formula),
            f"c={c_value}: threshold conjugate factorization failed",
        )
        _require(
            h_formula == explicit_h[c_value],
            f"c={c_value}: H polynomial transcription failed",
        )
        _require(
            all(coefficient > 0 for coefficient in h_formula),
            f"c={c_value}: H positivity failed",
        )
        _require(
            h_formula[0] / Q_BASE == Fraction(2 * c_value - 1, 24),
            f"c={c_value}: threshold limit failed",
        )

        ab_excess = _poly_subtract(ab_poly, _poly(16))
        abg_excess = _poly_subtract(
            _poly_multiply(ab_poly, g_poly), _poly(144)
        )
        u_excess = _poly_subtract(u_poly, _poly(24))
        _require(
            all(value >= 0 for value in ab_excess),
            f"c={c_value}: AB coefficient signs failed",
        )
        _require(
            all(value >= 0 for value in abg_excess),
            f"c={c_value}: ABG coefficient signs failed",
        )
        _require(
            all(value >= 0 for value in u_excess),
            f"c={c_value}: U coefficient signs failed",
        )
        _require(
            sum(ab_excess, Fraction(0)) <= 74,
            f"c={c_value}: AB uniform bound failed",
        )
        _require(
            sum(abg_excess, Fraction(0)) <= 1656,
            f"c={c_value}: ABG uniform bound failed",
        )
        _require(
            sum(u_excess, Fraction(0)) <= 85,
            f"c={c_value}: U uniform bound failed",
        )
        _require(
            sum(h_formula[1:], Fraction(0)) <= H_TAIL_BOUND,
            f"c={c_value}: H tail bound failed",
        )

    _require(Fraction(1800) < 43**2, "square-root upper gate failed")
    _require(
        Fraction(2 * 1656, 24) == 138,
        "square-root rationalization coefficient failed",
    )
    _require(
        74 * 195 + 16 * (85 + 138) == 17998 < Q_ERROR_BOUND,
        "Q error coefficient failed",
    )
    _require(Q_BASE == 16 * 48 > 0, "Q positive lower bound failed")
    _require(H_ZERO_MAX == 352 > 0, "H(0) positive upper bound failed")

    # Symbolic coefficient audit of
    # 768H-H0Q = 768(H-H0)-H0(Q-768),
    # in the independent basis (H, H0Q, H0).
    common_denominator_left = (Q_BASE, Fraction(-1), Fraction(0))
    common_denominator_right = (
        Q_BASE,
        Fraction(-1),
        -Q_BASE + Q_BASE,
    )
    _require(
        common_denominator_left
        == common_denominator_right
        == (Fraction(768), Fraction(-1), Fraction(0)),
        "threshold common-denominator identity failed",
    )

    ratio_error = (
        H_TAIL_BOUND / Q_BASE
        + H_ZERO_MAX * Q_ERROR_BOUND / Q_BASE**2
    )
    threshold_error_coefficient = Fraction(
        THRESHOLD_ERROR_NUMERATOR, THRESHOLD_ERROR_DENOMINATOR
    )
    _require(
        ratio_error == threshold_error_coefficient,
        "threshold ratio error identity failed",
    )
    _require(
        Q_BASE > 0 and H_ZERO_MAX > 0,
        "threshold denominator/positivity gate failed",
    )

    error_at_k = threshold_error_coefficient / K_EFF
    _require(
        error_at_k == Fraction(4193, 1107200),
        "threshold error at K failed",
    )
    m = _poly(0, 1)
    k_plus_m = _poly(K_EFF, 1)
    reciprocal_tail_cross = _poly_subtract(k_plus_m, _poly(K_EFF))
    reciprocal_tail_denominator = _poly_scale(k_plus_m, K_EFF)
    _require(
        reciprocal_tail_cross == m,
        "threshold tail 1/K-1/(K+m) numerator failed",
    )
    _require(
        all(value > 0 for value in reciprocal_tail_denominator),
        "threshold tail reciprocal denominator failed",
    )
    _require(
        m[0] == 0 and m[1] > 0,
        "threshold tail reciprocal numerator sign failed",
    )
    upper5 = Fraction(3, 8) + error_at_k
    lower6 = Fraction(11, 24) - error_at_k
    _require(
        upper5 == Fraction(419393, 1107200) > 0,
        "c=5 positive upper bound failed",
    )
    _require(
        lower6 == Fraction(1509821, 3321600) > 0,
        "c=6 positive lower bound failed",
    )
    _check_strict_fraction_order(
        upper5,
        Fraction(5, 13),
        Fraction(83891, 14393600),
        "c=5 kappa upper margin",
    )
    _check_strict_fraction_order(
        Fraction(5, 11),
        lower6,
        Fraction(31, 36537600),
        "c=6 kappa lower margin",
    )

    reciprocal_upper5 = 1 / upper5
    reciprocal_lower6 = 1 / lower6
    _require(
        Fraction(5, 13) * R5 == 1,
        "c=5 reciprocal comparator identity failed",
    )
    _require(
        Fraction(5, 11) * R6 == 1,
        "c=6 reciprocal comparator identity failed",
    )
    _require(
        reciprocal_upper5
        == Fraction(1107200, 419393)
        == R5 + Fraction(83891, 2096965),
        "c=5 positive inversion margin failed",
    )
    _require(
        reciprocal_lower6
        == Fraction(3321600, 1509821)
        == R6 - Fraction(31, 7549105),
        "c=6 positive inversion margin failed",
    )
    _check_strict_fraction_order(
        R5,
        reciprocal_upper5,
        Fraction(83891, 2096965),
        "c=5 threshold reciprocal order",
    )
    _check_strict_fraction_order(
        reciprocal_lower6,
        R6,
        Fraction(31, 7549105),
        "c=6 threshold reciprocal order",
    )


def check_exact_audit() -> None:
    """Run every exact proof gate once, without a parameter scan."""
    if _EXPLICIT_GATE_COUNT != 0:
        raise AuditFailure("audit must start from a zero gate count")
    _check_constants_and_domains()
    _check_denominator_arcsine_and_closure()
    _check_rho_separators()
    _check_threshold_and_inversion()
    if _EXPLICIT_GATE_COUNT != EXPECTED_CORE_GATE_COUNT:
        raise AuditFailure(
            "explicit gate-count fingerprint failed: "
            f"expected {EXPECTED_CORE_GATE_COUNT}, got {_EXPLICIT_GATE_COUNT}"
        )


_MUTATIONS = (
    ("K_EFF = 4325", "K_EFF = 4324", "cutoff-4324"),
    (
        "THRESHOLD_ERROR_NUMERATOR = 4193",
        "THRESHOLD_ERROR_NUMERATOR = 4194",
        "threshold-error-up",
    ),
    (
        "THRESHOLD_ERROR_NUMERATOR = 4193",
        "THRESHOLD_ERROR_NUMERATOR = 4192",
        "threshold-error-down",
    ),
    ("R5 = Fraction(13, 5)", "R5 = Fraction(14, 5)", "r5"),
    ("R6 = Fraction(11, 5)", "R6 = Fraction(12, 5)", "r6"),
    (
        "RHO_LOWER_SEPARATOR = Fraction(20, 9)",
        "RHO_LOWER_SEPARATOR = Fraction(19, 9)",
        "rho-lower",
    ),
    (
        "RHO_UPPER_SEPARATOR = Fraction(41, 16)",
        "RHO_UPPER_SEPARATOR = Fraction(42, 16)",
        "rho-upper",
    ),
    (
        "WEIGHT_BOUND = Fraction(58)",
        "WEIGHT_BOUND = Fraction(59)",
        "weight-bound",
    ),
    (
        "CLOSURE_DENOMINATOR_COEFFICIENT = Fraction(200)",
        "CLOSURE_DENOMINATOR_COEFFICIENT = Fraction(201)",
        "closure-denominator",
    ),
    (
        "CLOSURE_ARCSINE_COEFFICIENT = Fraction(1000, 3)",
        "CLOSURE_ARCSINE_COEFFICIENT = Fraction(1001, 3)",
        "closure-arcsine",
    ),
    (
        "H_TAIL_BOUND = Fraction(4329)",
        "H_TAIL_BOUND = Fraction(4330)",
        "h-tail",
    ),
    (
        "Q_ERROR_BOUND = Fraction(18000)",
        "Q_ERROR_BOUND = Fraction(18001)",
        "q-error",
    ),
    ("Q_BASE = Fraction(768)", "Q_BASE = Fraction(769)", "q-base"),
    (
        "6: _poly(352, 1449, 1980, 900)",
        "6: _poly(352, 1450, 1980, 900)",
        "h-coefficient",
    ),
    (
        "Fraction(31, 36537600)",
        "Fraction(0)",
        "strict-critical-margin",
    ),
)


def _run_mutation_audit() -> int:
    source = Path(__file__).read_text(encoding="utf-8")
    rejected = 0
    for old, new, label in _MUTATIONS:
        expected_occurrences = 1 + sum(
            1 for candidate, _, _ in _MUTATIONS if candidate == old
        )
        if source.count(old) != expected_occurrences:
            raise AuditFailure(
                f"mutation anchor occurrence fingerprint failed: {label}"
            )
        namespace = {"__name__": f"mutation_{label}"}
        mutated = source.replace(old, new, 1)
        try:
            exec(compile(mutated, f"<mutation:{label}>", "exec"), namespace)
            namespace["check_exact_audit"]()
        except namespace.get("AuditFailure", AuditFailure):
            rejected += 1
        except Exception as error:
            raise AuditFailure(
                f"mutation crashed outside an exact gate: {label}: "
                f"{type(error).__name__}"
            ) from error
        else:
            raise AuditFailure(f"altered constant was accepted: {label}")
    try:
        _require_strict_positive(Fraction(0), "strict zero rejection probe")
    except AuditFailure:
        strict_zero_rejected = True
    else:
        strict_zero_rejected = False
    if not strict_zero_rejected:
        raise AuditFailure("strict-positive helper accepted zero")
    _require(rejected == len(_MUTATIONS), "mutation rejection count failed")
    return rejected


def main() -> int:
    arguments = sys.argv[1:]
    if arguments not in ([], ["--self-test-mutations"]):
        print("usage: check_effective_cutoff.py [--self-test-mutations]")
        return 2

    check_exact_audit()
    print("independent_of_production=PASS (stdlib fractions only)")
    print("parameter_scans=NONE symbolic_tail_variable=m>=0")
    print("exact_rho_separators=PASS 11/5<20/9<rho<41/16<13/5")
    print("closure_tail=PASS K_eff=4325 c=5,6 denominator+arcsine gates")
    print("kappa_inversion=PASS positive H/Q exact error=4193/(256k)")
    print("effective_onset=PASS s_k=4k+6 for every integer k>=4325")
    print(f"exact_core_gates=PASS count={_EXPLICIT_GATE_COUNT}")

    if arguments:
        rejected = _run_mutation_audit()
        print(f"constant_mutations_rejected=PASS count={rejected}")
    print(
        "classification=EXACT_STDLIB_FRACTION_AUDIT; checker is "
        "corroborative and imports the fixed-k sign/persistence theorem"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
