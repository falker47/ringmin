#!/usr/bin/env python3
"""Exact task-local radius-8 bridge audit, independent of production/diagnostics.

Only stdlib integers and Fraction are used. No root solver, floating point,
numerical artifact, production import, or assert statement enters the proof.
Run with --tables to print the complete rational witnesses in Markdown.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F

K = 8
SEPARATOR = F(176)
DENOMINATOR = 10000
PI_LOWER = F(333, 106)
PI_UPPER = F(22, 7)
ARC_DOMAIN = F(3, 20)
ARC_CUBIC = F(7, 40)

# Each row is ((a,b), m), giving the bound m/10000 on the positive sine.
# The order is the entire cyclic tour, including the last-to-first edge.
UPPER_ROWS = (
    ((8, 36), 860), ((10, 36), 956), ((10, 34), 933),
    ((12, 34), 1017), ((12, 32), 991), ((14, 32), 1065),
    ((14, 30), 1036), ((16, 30), 1102), ((16, 28), 1070),
    ((18, 28), 1129), ((18, 26), 1093), ((20, 26), 1147),
    ((20, 24), 1107), ((22, 24), 1155), ((22, 23), 1134),
    ((21, 23), 1110), ((21, 25), 1152), ((19, 25), 1101),
    ((19, 27), 1139), ((17, 27), 1083), ((17, 29), 1117),
    ((15, 29), 1055), ((15, 31), 1085), ((13, 31), 1015),
    ((13, 33), 1043), ((11, 33), 964), ((11, 35), 988),
    ((9, 35), 899), ((9, 37), 920), ((8, 37), 870),
)
LOWER_ROWS = (
    ((8, 37), 869), ((10, 37), 966), ((10, 35), 944),
    ((12, 35), 1028), ((12, 33), 1003), ((14, 33), 1078),
    ((14, 31), 1050), ((16, 31), 1117), ((16, 29), 1085),
    ((18, 29), 1145), ((18, 27), 1110), ((20, 27), 1164),
    ((20, 25), 1126), ((22, 25), 1175), ((22, 23), 1133),
    ((23, 24), 1177), ((21, 24), 1131), ((21, 26), 1171),
    ((19, 26), 1119), ((19, 28), 1156), ((17, 28), 1099),
    ((17, 30), 1132), ((15, 30), 1069), ((15, 32), 1099),
    ((13, 32), 1028), ((13, 34), 1055), ((11, 34), 975),
    ((11, 36), 999), ((9, 36), 908), ((9, 38), 929),
    ((8, 38), 878),
)


class AuditFailure(RuntimeError):
    """An explicit gate failed; also active under python -O."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditFailure(message)


def endpoint(n: int) -> None:
    require(type(n) is int and n in (37, 38), "endpoint must be 37 or 38")


def rank_tour(n: int) -> tuple[int, ...]:
    """Fixed-k theorem section 1, rank arms; no parity-edge formula here."""
    endpoint(n)
    size = n - K + 1
    mid = (size + 1) // 2
    arms = []
    for start in (1, 2):
        arm = []
        for j in range(size):
            low, high = start + 2*j, size - start - 2*j
            if low <= mid:
                arm.append(low)
            if high > mid:
                arm.append(high)
        arms.append(arm)
    return tuple(v + K - 1 for v in arms[0] + arms[1][::-1] + [size])


def cyclic_edges(tour: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    require(len(tour) >= 3, "cycle needs at least three vertices")
    return tuple(tuple(sorted((a, tour[(i+1) % len(tour)])))
                 for i, a in enumerate(tour))


def parity_edges(n: int) -> tuple[tuple[int, int], ...]:
    """Independent even/odd edge families, keeping multiplicity visible."""
    endpoint(n)
    size = n - K + 1
    h = size // 2
    edges = [(K, n)]
    if size % 2 == 0:
        edges.append((K+h-1, K+h))
        edges.extend((i, n+K-1-i) for i in range(K, K+h-1))
        edges.extend((i, n+K+1-i) for i in range(K+1, K+h))
    else:
        edges.extend((i, n+K-1-i) for i in range(K, K+h))
        edges.extend((i, n+K+1-i) for i in range(K+1, K+h+1))
    return tuple(tuple(sorted(e)) for e in edges)


def check_edges(n: int, tour: tuple[int, ...], edges: tuple) -> None:
    endpoint(n)
    size = n - K + 1
    require(len(tour) == size and set(tour) == set(range(K, n+1)),
            "tour is not a complete permutation")
    require(len(edges) == size and len(set(edges)) == size,
            "missing or duplicate edge")
    require(all(len(e) == 2 and K <= e[0] < e[1] <= n for e in edges),
            "edge domain/normalization")
    require(Counter(v for e in edges for v in e)
            == Counter({v: 2 for v in range(K, n+1)}), "degree must be two")
    require({(K, n-1), (K, n)} <= set(edges), "both seam edges required")
    require(Counter(edges) == Counter(cyclic_edges(tour)),
            "edge list differs from complete cycle")
    require(Counter(edges) == Counter(parity_edges(n)), "parity edges disagree")


def check_threshold(a: F, b: F, q: F, direction: str) -> tuple[F, F, F]:
    """kappa=a-sqrt(b); compare positive T=1/kappa with q."""
    require(all(isinstance(v, F) for v in (a, b, q)), "rational inputs required")
    require(direction in ("above", "below"), "unknown threshold direction")
    require(q > 0 and a > 0 and b > 0, "positive threshold inputs required")
    positive_margin = a*a-b
    require(positive_margin > 0, "kappa must be positive before reciprocal")
    h = a - 1/q
    require(h > 0, "positive comparison before squaring required")
    margin = b-h*h if direction == "above" else h*h-b
    require(margin > 0, "strict threshold square comparison failed")
    return positive_margin, h, margin


def threshold_data(n: int) -> tuple[F, F]:
    endpoint(n)
    return F(1, K)+F(1, n)+F(1, n-1), F(4*(2*n+K-1), K*n*(n-1))


def multiply(a: tuple, b: tuple) -> tuple:
    result = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return tuple(result)


def check_arcsine_majorant() -> None:
    require(0 < ARC_DOMAIN < 1 and ARC_CUBIC > 0, "arcsine domain/coefficient")
    # In t=u^2: (1+3*c*t)^2(1-t)-1.
    polynomial = list(multiply(multiply((F(1), 3*ARC_CUBIC),
                                       (F(1), 3*ARC_CUBIC)), (F(1), F(-1))))
    polynomial[0] -= 1
    require(tuple(polynomial) == (F(0), F(1, 20), F(-1239, 1600), F(-441, 1600)),
            "arcsine derivative polynomial identity")
    t = ARC_DOMAIN**2
    require(80-1239*t-441*t*t == F(8303879, 160000) > 0,
            "arcsine decreasing polynomial endpoint")


def atan_partial(x: F, terms: int) -> F:
    require(0 < x < 1 and type(terms) is int and terms > 0, "atan domain")
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))


def check_pi() -> tuple[F, F]:
    x, y = F(1, 5), F(1, 239)
    require(0 < y < x < 1, "Machin positive branch inputs")
    t2 = 2*x/(1-x*x)
    require(t2 == F(5, 12) and 0 < t2 < 1, "Machin double-angle branch")
    t4 = 2*t2/(1-t2*t2)
    require(t4 == F(120, 119), "Machin quadruple angle")
    require((t4-y)/(1+t4*y) == 1, "Machin tangent subtraction")
    # Finite geometric identity, both signs: terms 1,2,4,5.
    for terms in (1, 2, 4, 5):
        coefficients = tuple(F((-1)**j) for j in range(terms))
        product = multiply(coefficients, (F(1), F(1)))
        require(product == (F(1),) + (F(0),)*(terms-1)
                + (F((-1)**(terms-1)),), "atan finite remainder identity")
    lo = 16*atan_partial(x, 4)-4*atan_partial(y, 1)
    hi = 16*atan_partial(x, 5)-4*atan_partial(y, 2)
    require(lo == F(1231847548, 392109375) > PI_LOWER,
            "pi lower rational comparison")
    require(hi < PI_UPPER, "pi upper rational comparison")
    return lo, hi


def check_rows(n: int, rows: tuple, upper: bool) -> F:
    endpoint(n)
    require(upper is (n == 37), "wrong endpoint bound direction")
    require(SEPARATOR == F(176) and DENOMINATOR == 10000, "fixed witness parameters")
    tour = rank_tour(n)
    edges = tuple(e for e, _ in rows)
    check_edges(n, tour, edges)
    require(edges == cyclic_edges(tour), "proof rows must follow cyclic order")
    total = F(0)
    for (a, b), m in rows:
        require(type(m) is int and m > 0, "positive integer bound required")
        s2 = F(a*b) / ((SEPARATOR+a)*(SEPARATOR+b))
        u = F(m, DENOMINATOR)
        require(0 < s2 < 1 and 0 < u < 1, "sine/bound domain")
        if upper:
            require(u <= ARC_DOMAIN, "upper bound outside arcsine majorant domain")
            require(u*u-s2 > 0, "upper sine square margin")
            total += u+ARC_CUBIC*u**3
        else:
            require(s2-u*u > 0, "lower sine square margin")
            total += u
    if upper:
        require(total < PI_LOWER, "chain upper bridge")
    else:
        require(total > PI_UPPER, "chain lower bridge")
    return total


def table_text(n: int, rows: tuple) -> str:
    """M/(D^2 Q_e) is the strict sine-square margin; all entries exact."""
    check_rows(n, rows, n == 37)
    lines = [f"### Complete table for n={n}", "",
             "| a | b | m_e | Q_e | M_e |", "|---:|---:|---:|---:|---:|"]
    for (a, b), m in rows:
        denominator = (176+a)*(176+b)
        margin = m*m*denominator-DENOMINATOR**2*a*b
        if n == 38:
            margin = -margin
        lines.append(f"| {a} | {b} | {m} | {denominator} | {margin} |")
    return "\n".join(lines)


def audit() -> None:
    require(K == 8 and SEPARATOR == F(176), "fixed endpoint problem")
    for n in (37, 38):
        tour = rank_tour(n)
        edges = cyclic_edges(tour)
        check_edges(n, tour, edges)
        for oriented in (tour, tour[::-1]):
            for shift in range(len(tour)):
                moved = oriented[shift:]+oriented[:shift]
                check_edges(n, moved, cyclic_edges(moved))
        a, b = threshold_data(n)
        pm, h, margin = check_threshold(a, b, SEPARATOR,
                                       "above" if n == 37 else "below")
        print(f"threshold n={n} A={a} B={b} A2-B={pm} H={h} square_margin={margin}")
    check_arcsine_majorant()
    lo, hi = check_pi()
    print(f"pi lower_witness={lo} lower_margin={lo-PI_LOWER}")
    print(f"pi upper_witness={hi} upper_margin={PI_UPPER-hi}")
    upper = check_rows(37, UPPER_ROWS, True)
    lower = check_rows(38, LOWER_ROWS, False)
    require(upper == F(62794038854497, 20000000000000), "n=37 recorded total")
    require(lower == F(16459, 5000), "n=38 recorded total")
    print(f"chain n=37 edges=30 upper_half_sum={upper} margin={PI_LOWER-upper}")
    print(f"chain n=38 edges=31 lower_half_sum={lower} margin={lower-PI_UPPER}")
    print("exact_bridge=PASS inequalities=4 cyclic_edges=61 symmetry_variants=122")
    print("corollary=s_8=38 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tables", action="store_true", help="print exact proof tables")
    options = parser.parse_args()
    audit()
    if options.tables:
        print(table_text(37, UPPER_ROWS))
        print()
        print(table_text(38, LOWER_ROWS))
