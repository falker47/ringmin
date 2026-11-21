"""Offline arithmetic for the common left endpoint of bounds (22) and (23)."""

import hashlib
import json
import runpy
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_BLOB = "ab21727593fe9acbc0a28fffc50ef2dcf2cc4d84"
SOURCE_SHA256 = "a5b32177e4f3832b2d7b202fcd6e80f598ac0d4f962326a6aa8af60b6feddd2b"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_source():
    data = (HERE / "source" / "ALL_N_LOWER_BOUND.md").read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    require(hashlib.sha1(header + data).hexdigest() == SOURCE_BLOB, "source Git blob")
    require(hashlib.sha256(data).hexdigest() == SOURCE_SHA256, "source SHA-256")


def product(left, right):
    """Polynomial product with coefficients listed constant term first."""
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def evaluate_radical(poly, a, b):
    """Horner evaluation at a + b sqrt(2), returning both rational parts."""
    u = v = Q(0)
    for coefficient in reversed(poly):
        u, v = coefficient + a * u + 2 * b * v, a * v + b * u
    return u, v


def coefficient():
    # 24p(a) from the tail sum, and 24 times its limiting middle-branch gain.
    tail = [4 * v for v in product([1, -1], [1, 4, 1])]
    gain = product(product([-1, 3], [-1, 3]), [-1, 3])
    cubic = [Q(u + v, 24) for u, v in zip(tail, gain, strict=True)]
    # Solve H'(a) = 0. After multiplying by 8, the polynomial is primitive.
    c, b, a = [8 * i * cubic[i] for i in range(1, 4)]
    discriminant = b * b - 4 * a * c
    factor = isqrt(discriminant.numerator // (2 * discriminant.denominator))
    require(discriminant == 2 * factor**2 and a > 0, "derivative discriminant")
    u, v = -b / (2 * a), -factor / (2 * a)
    require((u, v) == (Q(13, 23), Q(-2, 23)), "middle optimizer")
    # 1 < sqrt(2) < 3/2 gives a rational enclosure for this root.
    require(Q(1, 3) < u + Q(3, 2) * v < u + v < Q(1, 2), "middle regime")
    require(evaluate_radical([c, b, a], u, v) == (0, 0), "stationarity")
    p = evaluate_radical([Q(t, 24) for t in tail], u, v)
    residual = evaluate_radical([Q(t, 24) for t in gain], u, v)
    require(p == (Q(9038, 36501), Q(722, 36501)), "tail coefficient")
    require(residual == (Q(944, 36501), Q(-630, 36501)), "prefix gain")
    total = evaluate_radical(cubic, u, v)
    require(total == (p[0] + residual[0], p[1] + residual[1]), "sum of contributions")
    require(total == (Q(434, 1587), Q(4, 1587)), "normalized lower endpoint")
    return total


def check_simplex():
    # T(z)-z = (1-3z)^2(4-3z) / (27(1-z)^2). Check every coefficient.
    numerator = [4, *[-27 * t for t in product([1, -1], [1, -1])]]
    require(numerator == product(product([1, -3], [1, -3]), [4, -3]), "Bellman identity")
    # A separate equal-mesh witness uses sum_{i=1}^k i^2 = P(k).
    # P(0)=0 and P(k)-P(k-1)=k^2 identify this polynomial for all integers k.
    six_p = product([0, 1], product([1, 1], [1, 2]))
    six_previous = product([-1, 1], product([0, 1], [-1, 2]))
    difference = [x - y for x, y in zip(six_p, six_previous, strict=True)]
    require(six_p[0] == 0 and difference == [0, 0, 6, 0], "sum of squares")
    mesh_denominator = [6 * t for t in product(product([1, 1], [1, 1]), [1, 1])]
    require(Q(six_p[-1], mesh_denominator[-1]) == Q(1, 3), "mesh limit")


def arctangent_bracket(d, pairs=16):
    """Consecutive even and odd partial sums bracket atan(1/d) for d>1."""
    lower = sum(Q((-1)**j, (2*j + 1) * d**(2*j + 1)) for j in range(2*pairs))
    upper = lower + Q(1, (4*pairs + 1) * d**(4*pairs + 1))
    return lower, upper


def pi_bracket():
    # For a=atan(1/5), b=atan(1/239), 0<4a-b<4/5<pi/2.
    # Check tan(4a-b)=1 before using the alternating series for pi=16a-4b.
    t = Q(1, 5)
    for _ in range(2):
        t = 2 * t / (1 - t*t)
    h = Q(1, 239)
    require((t - h) / (1 + t*h) == 1, "Machin identity")
    lo5, hi5 = arctangent_bracket(5)
    lo239, hi239 = arctangent_bracket(239)
    return 16*lo5 - 4*hi239, 16*hi5 - 4*lo239


def decimal_bounds(lower, upper, places):
    """Outward decimal formatting using integer floor and ceiling."""
    scale = 10**places
    left = lower.numerator * scale // lower.denominator
    right = -(-upper.numerator * scale // upper.denominator)

    def fixed(value):
        return f"{value // scale}.{value % scale:0{places}d}"

    return f"[{fixed(left)}, {fixed(right)}]"


def radius_bracket(total, pi):
    scale = 10**50
    root = isqrt(2 * scale**2)
    require(root**2 < 2 * scale**2 < (root + 1)**2, "sqrt(2) enclosure")
    lo = (total[0] + total[1] * Q(root, scale)) / pi[1]
    hi = (total[0] + total[1] * Q(root + 1, scale)) / pi[0]
    require(Q("0.088183442492803631749528358531") < lo < hi
            < Q("0.088183442492803631749528358532"), "lower endpoint enclosure")
    return lo, hi


def upper_witness(pi, radius):
    """Replay the finite line placement used for Paper II's comparison."""
    path = HERE.parents[1] / "paper_assets/line_upper/certificates/p2_n03200.json"
    witness = json.loads(path.read_bytes())
    n, denominator = witness["n"], witness["D"]
    require(witness["schema"] == "ringmin-line-v1" and witness["power"] == 2
            and n == 3200 and denominator == n**2, "quadratic witness parameters")
    order, positions = witness["order"], witness["positions"]
    require(sorted(order) == list(range(1, n + 1)) and len(positions) == n
            and all(type(x) is int for x in positions), "integer positions and permutation")
    coords = [positions[i-1] for i in order]
    require(all(a < b for a, b in zip(coords, coords[1:])), "order of witness")
    span = coords[-1] - coords[0]
    require(span == witness["span_numerator"] == 9108638531, "witness span")
    for j, v in enumerate(positions):
        for i in range(j):
            if abs(v - positions[i]) < (i + 1) * (j + 1):
                raise ValueError(f"infeasible line witness at labels {i+1},{j+1}")
    # Each unit closing gap suffices for two marks in [0,1].
    normalized = (Q(span, denominator) + 1) / n
    lo, hi = normalized / pi[1], normalized / pi[0]
    ceiling = Q(*witness["B"])
    require(ceiling == Q("0.088581212993") and ceiling - Q(1, 10**12) < lo < hi < ceiling,
            "strict twelve-place upper ceiling")
    require(radius[1] < lo, "comparison interval is ordered")
    return n * (n - 1) // 2


def main():
    check_source()
    finite = runpy.run_path(str(HERE / "finite.py"))["check_finite"]()
    check_simplex()
    total = coefficient()
    pi = pi_bracket()
    physical = radius_bracket(total, pi)
    pairs = upper_witness(pi, physical)
    print(f"Source Git blob {SOURCE_BLOB}, SHA-256 {SOURCE_SHA256}")
    print(finite)
    print("Simplex limit 1/3, density (13-2*sqrt(2))/23")
    print("Tail (9038+722*sqrt(2))/36501, gain (944-630*sqrt(2))/36501")
    print("Lower endpoint (434+4*sqrt(2))/(1587*pi) in", decimal_bounds(*physical, 30))
    # Numerical values of the source's other endpoints, for comparison only.
    for label, factor in (("(22) right", Q(1, 2)), ("(23) right", Q(857, 3000)),
                          ("full-tail baseline", Q(1, 6))):
        print(f"{label} {factor}/pi in", decimal_bounds(factor / pi[1], factor / pi[0], 30))
    print(f"Upper witness: {pairs} pairs, span 9108638531/10240000, ceiling 0.088581212993")
    print("PASS offline arithmetic and finite checks")


if __name__ == "__main__":
    main()
