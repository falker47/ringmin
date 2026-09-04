"""Symbolic audit of the displayed alternating-halves constants and gates.

This is corroborating task-local evidence, not a computer-assisted proof.
It deliberately does not import the Ringmin production package.
"""

from __future__ import annotations

import sympy as sp


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> None:
    t, x = sp.symbols("t x", nonnegative=True)
    sqrt2 = sp.sqrt(2)
    J = 3 * sqrt2 / 4 - sp.log(1 + sqrt2) / 4
    J_display = 3 * sqrt2 / 4 - sp.log(3 + 2 * sqrt2) / 8
    small = sp.Rational(5, 18) - sp.log(3) / 8
    K = J - sp.Rational(1, 12) + sp.log(3) / 8

    integral_J = sp.integrate(sp.sqrt(t * (t + 1)), (t, 0, 1))
    integral_small = sp.integrate(sp.sqrt(t * (t + 1)), (t, 0, sp.Rational(1, 3)))
    require(sp.simplify(integral_J.rewrite(sp.log) - J) == 0, "J integral identity")
    require(sp.simplify(integral_small.rewrite(sp.log) - small) == 0, "small integral identity")
    require(sp.expand((1 + sqrt2) ** 2) == 3 + 2 * sqrt2, "J logarithm square identity")
    rewritten_display = J_display.xreplace({3 + 2 * sqrt2: (1 + sqrt2) ** 2})
    require(sp.simplify(sp.expand_log(rewritten_display, force=True) - J) == 0, "J displayed logarithm identity")

    direct_part = sp.integrate(2 * (x + sp.Rational(1, 2)), (x, 0, sp.Rational(1, 6)))
    require(direct_part == sp.Rational(7, 36), "direct valley integral")
    require(sp.simplify(direct_part + J - small - K) == 0, "K assembly")
    require(sp.simplify(K - J - (3 * sp.log(3) - 2) / 24) == 0, "valley correction")

    squared_switch = sp.expand(4 * (x + sp.Rational(1, 2)) ** 2 - 16 * x * (x + sp.Rational(1, 2)))
    expected_switch = sp.expand(4 * (x + sp.Rational(1, 2)) * (sp.Rational(1, 2) - 3 * x))
    require(sp.simplify(squared_switch - expected_switch) == 0, "switch factorization")

    shell_gate = sp.expand((1 + x) ** 2 * (1 - x**2) - 1)
    require(sp.simplify(shell_gate - x * (2 - 2 * x**2 - x**3)) == 0, "shell gate factorization")
    shell_endpoint = sp.simplify(2 - 2 * sp.Rational(1, 2) - 1 / (2 * sqrt2))
    require(shell_endpoint.is_positive is True, "shell gate endpoint sign")
    require(sp.Rational(169, 81) > 2, "sqrt(2)<13/9 square gate")

    print(f"sympy={sp.__version__}")
    print(f"J={sp.N(J, 30)}")
    print(f"K={sp.N(K, 30)}")
    print(f"c_chain={sp.N(J/(2*sp.pi), 30)}")
    print(f"c_full={sp.N(K/(2*sp.pi), 30)}")
    print("PASS: 11 symbolic integral, assembly, switch, and inequality gates")


if __name__ == "__main__":
    main()
