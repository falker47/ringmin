"""Exact arithmetic corroboration; no search, production imports or numerics.

The geometric deletion and analytic convergence arguments remain in the
proof note. These gates check rational remainders, constant comparisons,
and the four symbolic residue cases used to pass to all integers.
"""

from fractions import Fraction as F


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def multiply(a: list[F], b: list[F]) -> list[F]:
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def main() -> None:
    # Coefficient identities establish the signed integrands, not just
    # sampled function values. Coefficients are in ascending degree.
    denominator = [F(1), F(0), F(1)]
    alternating = [F((-1) ** (i // 2)) if i % 2 == 0 else F(0)
                   for i in range(7)]
    remainder_identity = multiply(denominator, alternating)
    remainder_identity[8] += 1
    require(remainder_identity == [F(1)] + [F(0)] * 8,
            "atan signed-remainder polynomial")

    quotient = [F(v) for v in (4, 0, -4, 0, 5, -4, 1)]
    pi_numerator = multiply(denominator, quotient)
    pi_numerator[0] -= 4
    require(pi_numerator == [F(v) for v in (0, 0, 0, 0, 1, -4, 6, -4, 1)],
            "positive pi-integrand polynomial")
    require(sum((v / (i + 1) for i, v in enumerate(quotient)), F(0))
            == F(22, 7), "integrated pi quotient")

    x = F(3, 4)
    lower = sum(((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                 for j in range(4)), F(0))
    require(lower == F(365721, 573440), "atan lower value")
    margin = 132 + 275 * lower - 96 * F(22, 7)
    require(margin == F(650463, 114688) and margin > 0,
            "rho strict separator")
    require(F(24, 11) / 16 == F(3, 22), "normalization by 16")
    require(F(3, 22) - F(1, 8) == F(1, 88), "deficit gap")

    # n=4k+5+j, j=0,1,2,3: polynomials valid for every k, not a k scan.
    # (4k+8)^2-(4k+5+j)^2=(3-j)(8k+13+j)>=0 for k>=1.
    for j in range(4):
        n_poly = [F(5 + j), F(4)]
        upper_poly = [F(8), F(4)]
        n_squared = multiply(n_poly, n_poly)
        upper_squared = multiply(upper_poly, upper_poly)
        diff = [a - b for a, b in zip(upper_squared, n_squared)]
        require(diff == [F((3 - j) * (13 + j)), F(8 * (3 - j)), F(0)]
                and all(c >= 0 for c in diff), "all-integer denominator gate")
        require(n_squared[2] == 16, "leading normalization coefficient")

    print("signed_remainder_identities=PASS identities=2 pi_quotient=22/7")
    print(f"atan_lower={lower} rho_cross_margin={margin}")
    print("constant_separation=PASS (24/11)/16=3/22 gap_to_1/8=1/88")
    print("all_integer_interpolation=PASS symbolic_residues=4 parameter_scans=NONE")
    print("classification=EXACT_RATIONAL_AUDIT; geometry and limits require analytic proof")


if __name__ == "__main__":
    main()
