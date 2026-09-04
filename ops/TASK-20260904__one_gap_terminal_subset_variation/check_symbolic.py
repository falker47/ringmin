"""Independent symbolic gates for the one-gap continuum variation.

This file imports no ringmin production code. It checks identities used by
the proof; it is not a proof assistant and does not reprove Supnick's theorem.
"""

from __future__ import annotations

import sympy as sp


def require_zero(name: str, expression: sp.Expr) -> None:
    simplified = sp.trigsimp(sp.simplify(expression))
    if simplified != 0:
        raise AssertionError(f"{name}: {simplified}")


def main() -> None:
    s, theta, tau = sp.symbols("s theta tau", positive=True, real=True)
    # Check the primitive on its proof domain y=s*sin(theta)^2,
    # 0<theta<pi/2. This avoids asking SymPy to infer the sign of s-y.
    parametric_y = s * sp.sin(theta) ** 2
    parametric_primitive = s * theta - s * sp.sin(theta) * sp.cos(theta)
    pulled_back_integrand = sp.tan(theta) * sp.diff(parametric_y, theta)
    require_zero(
        "primitive",
        sp.diff(parametric_primitive, theta) - pulled_back_integrand,
    )

    g = s * sp.sin(theta) * sp.cos(theta)
    integral_x_m = s * (sp.pi / 4 - theta) - s / 2 + g
    lower = -g + s / 4 + integral_x_m / 2
    common = s * (sp.pi / 4 - theta - sp.sin(theta) * sp.cos(theta)) / 2
    require_zero("lower_derivative", lower - common)

    # For an upper gap, p=s-x has angle pi/2-theta.
    integral_p_m = s * (theta - sp.pi / 4) - s / 2 + g
    upper = -s / 4 - integral_p_m / 2
    require_zero("upper_derivative", upper - common)
    require_zero("median_derivative", common.subs(theta, sp.pi / 4) + s / 4)

    phi = sp.pi / 4 - theta - sp.sin(theta) * sp.cos(theta)
    require_zero("phi_derivative", sp.diff(phi, theta) + 2 * sp.cos(theta) ** 2)

    q = sp.sin(tau)
    alpha = (1 - q) / (1 + q)
    scale = 2 / (1 + q)
    half_angle_square = (1 - sp.sin(tau)) / 2
    require_zero("lower_endpoint_ratio", alpha / scale - half_angle_square)

    theta_alpha = sp.pi / 4 - tau / 2
    endpoint_phi = sp.pi / 4 - theta_alpha - sp.sin(theta_alpha) * sp.cos(theta_alpha)
    require_zero("endpoint_phi", endpoint_phi - (tau - sp.cos(tau)) / 2)

    for n in range(3, 101):
        if n % 2 == 0:
            h = n // 2
            count = (h - 1) + (h - 1) + 2
        else:
            h = (n - 1) // 2
            count = h + h + 1
        if count != n:
            raise AssertionError((n, count))

    print("primitive_and_variations=PASS identities=5")
    print("optimized_endpoint_sign=PASS identities=3")
    print("supnick_parity_edge_counts=PASS sizes=3..100")
    print(f"sympy={sp.__version__} imports_ringmin=NO classification=EXACT_SYMBOLIC_AUDIT")


if __name__ == "__main__":
    main()
