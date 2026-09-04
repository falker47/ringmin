"""Independent symbolic audit; imports SymPy but no Ringmin code."""

import sympy as s


def require(condition, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def main() -> None:
    k, n = s.symbols("k n", positive=True)
    ell = n / k

    h_even = (n - k + 1) / 2
    require(s.simplify((k + h_even - 2) / k
                       - ((ell + 1) / 2 - s.Rational(3, 2) / k)) == 0,
            "even minus endpoint")
    require(s.simplify((k + h_even - 1) / k
                       - ((ell + 1) / 2 - s.Rational(1, 2) / k)) == 0,
            "even plus endpoint")
    require(s.simplify(2 + 2 * (h_even - 1) - (n - k + 1)) == 0,
            "even edge count")

    h_odd = (n - k) / 2
    require(s.simplify((k + h_odd - 1) / k
                       - ((ell + 1) / 2 - 1 / k)) == 0,
            "odd minus endpoint")
    require(s.simplify((k + h_odd) / k - (ell + 1) / 2) == 0,
            "odd plus endpoint")
    require(s.simplify(1 + 2 * h_odd - (n - k + 1)) == 0,
            "odd edge count")

    i = s.symbols("i")
    require(s.simplify((n + k - 1 - i) / k
                       - (ell + 1 - 1 / k - i / k)) == 0,
            "minus paired endpoint")
    require(s.simplify((n + k + 1 - i) / k
                       - (ell + 1 + 1 / k - i / k)) == 0,
            "plus paired endpoint")

    q = s.symbols("q", positive=True)
    root = s.sqrt(1 - q**2)
    h = s.asin(q) + q * root
    antiderivative = (q * root + s.asin(q)) / 2
    require(s.simplify(s.diff(antiderivative, q) - root) == 0,
            "semicircle antiderivative")
    require(s.simplify(s.diff(h, q) - 2 * root) == 0,
            "H derivative")

    f = h / (s.pi * (1 + q) ** 2)
    expected_derivative = 2 * (root - s.asin(q)) / (s.pi * (1 + q) ** 3)
    require(s.simplify(s.diff(f, q) - expected_derivative) == 0,
            "coefficient derivative")

    lam = (1 + q) / (1 - q)
    coefficient_from_lambda = (lam + 1) ** 2 * h / (4 * s.pi * lam**2)
    require(s.simplify(coefficient_from_lambda - f) == 0,
            "lambda-q coefficient transformation")
    require(s.simplify(s.diff(lam, q) - 2 / (1 - q) ** 2) == 0,
            "lambda-q monotonicity")
    require(s.limit(f, q, 0, dir="+") == 0, "lambda down-to-one boundary")
    require(s.limit(f, q, 1, dir="-") == s.Rational(1, 8),
            "lambda infinity boundary")

    lambda_symbol = s.symbols("lambda", positive=True)
    q_lambda = (lambda_symbol - 1) / (lambda_symbol + 1)
    i_closed = ((lambda_symbol + 1) ** 2 / 8
                * (s.asin(q_lambda)
                   + q_lambda * s.sqrt(1 - q_lambda**2)))
    x = s.symbols("x", positive=True)
    primitive = ((2 * x - lambda_symbol - 1)
                 * s.sqrt(x * (lambda_symbol + 1 - x)) / 4
                 + (lambda_symbol + 1) ** 2
                 * s.asin((2 * x - lambda_symbol - 1)
                          / (lambda_symbol + 1)) / 8)
    require(s.simplify(s.diff(primitive, x)
                       - s.sqrt(x * (lambda_symbol + 1 - x))) == 0,
            "integral primitive")
    require(s.simplify(primitive.subs(x, (lambda_symbol + 1) / 2)
                       - primitive.subs(x, 1) - i_closed) == 0,
            "integral endpoints")

    print("parity_endpoint_and_count_identities=PASS identities=8")
    print("integral_and_coefficient_identities=PASS identities=3")
    print("optimization_derivative_and_boundaries=PASS identities=5")
    print(f"sympy={s.__version__} imports_ringmin=NO classification=EXACT_SYMBOLIC_AUDIT")


if __name__ == "__main__":
    main()
