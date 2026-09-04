#!/usr/bin/env python3
"""Exact radius-9 endpoint audit; stdlib only, no production/diagnostic import.

Only n=41,42 and R=220 are evaluated. All proof arithmetic uses integers
and Fraction; explicit exceptions retain the gates under python -O.
"""

import argparse
from collections import Counter
from fractions import Fraction as F

K, Q, D = 9, 220, 10000
PI_LOWER, PI_UPPER = F(157, 50), F(22, 7)
ARC_DOMAIN, ARC_CUBIC = F(1, 5), F(1, 5)

# (a, b, m): bound m/D for sqrt(ab/((Q+a)(Q+b))).
# Complete parity-family order, including closure (9,n) as the first row.
UPPER_ROWS = (
    (9, 41, 786), (9, 40, 778), (10, 39, 810), (11, 38, 838),
    (12, 37, 863), (13, 36, 886), (14, 35, 907), (15, 34, 925),
    (16, 33, 941), (17, 32, 955), (18, 31, 967), (19, 30, 977),
    (20, 29, 986), (21, 28, 992), (22, 27, 997), (23, 26, 1001),
    (24, 25, 1002), (10, 41, 827), (11, 40, 856), (12, 39, 883),
    (13, 38, 907), (14, 37, 929), (15, 36, 948), (16, 35, 965),
    (17, 34, 980), (18, 33, 994), (19, 32, 1005), (20, 31, 1015),
    (21, 30, 1023), (22, 29, 1029), (23, 28, 1034),
    (24, 27, 1037), (25, 26, 1039),
)
LOWER_ROWS = (
    (9, 42, 793), (25, 26, 1038), (9, 41, 785), (10, 40, 817),
    (11, 39, 846), (12, 38, 872), (13, 37, 896), (14, 36, 917),
    (15, 35, 935), (16, 34, 952), (17, 33, 967), (18, 32, 979),
    (19, 31, 990), (20, 30, 999), (21, 29, 1007), (22, 28, 1013),
    (23, 27, 1017), (24, 26, 1019), (10, 42, 834), (11, 41, 864),
    (12, 40, 892), (13, 39, 916), (14, 38, 938), (15, 37, 958),
    (16, 36, 976), (17, 35, 992), (18, 34, 1006), (19, 33, 1018),
    (20, 32, 1028), (21, 31, 1037), (22, 30, 1044),
    (23, 29, 1049), (24, 28, 1053), (25, 27, 1056),
)


class AuditFailure(ValueError):
    """An exact proof gate failed."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def endpoint(n):
    require(type(n) is int and n in (41, 42), "only endpoints 41,42 allowed")


def rank_tour(n):
    """Rank arms from fixed-k section 1, without using parity edge families."""
    endpoint(n)
    size = n-K+1
    mid = (size+1)//2
    arms = []
    for start in (1, 2):
        arm = []
        j = 0
        while True:
            low, high = start+2*j, size-start-2*j
            if low > mid and high <= mid:
                break
            if low <= mid:
                arm.append(low)
            if high > mid:
                arm.append(high)
            j += 1
        arms.append(arm)
    return tuple(K+r-1 for r in arms[0]+arms[1][::-1]+[size])


def cyclic_edges(tour):
    require(len(tour) >= 3, "cycle length")
    return tuple(tuple(sorted((a, tour[(i+1) % len(tour)])))
                 for i, a in enumerate(tour))


def parity_edges(n):
    """Independent specialization of the odd/even formulas, no tour input."""
    endpoint(n)
    if n == 41:  # N=33=2*16+1
        return ((9, 41),) + tuple((i, 49-i) for i in range(9, 25)) + tuple(
            (i, 51-i) for i in range(10, 26))
    # N=34=2*17
    return ((9, 42), (25, 26)) + tuple((i, 50-i) for i in range(9, 25)) + tuple(
        (i, 52-i) for i in range(10, 26))


def check_edges(n, tour, edges):
    endpoint(n)
    size = n-K+1
    require(all(type(v) is int for v in tour), "integer vertices required")
    require(len(tour) == size and set(tour) == set(range(K, n+1)),
            "tour must be a complete permutation")
    require(all(len(e) == 2 and all(type(v) is int for v in e)
                and K <= e[0] < e[1] <= n for e in edges), "edge domain")
    require(len(edges) == size and len(set(edges)) == size, "edge multiplicity")
    require(Counter(v for e in edges for v in e) ==
            Counter({v: 2 for v in range(K, n+1)}), "degree two required")
    require({(K, n), (K, n-1)} <= set(edges), "both seam edges required")
    require(Counter(edges) == Counter(cyclic_edges(tour)), "cyclic edges disagree")
    require(Counter(edges) == Counter(parity_edges(n)), "parity edges disagree")


def threshold_data(n):
    endpoint(n)
    return F(1, K)+F(1, n)+F(1, n-1), F(4*(2*n+K-1), K*n*(n-1))


def check_threshold(a, b, separator, direction):
    """T=1/(a-sqrt(b)); return positivity, pre-square and directed margins."""
    require(all(type(v) is F for v in (a, b, separator)), "Fraction inputs required")
    require(direction in ("above", "below"), "threshold direction")
    require(a > 0 and b > 0 and separator > 0, "positive threshold inputs")
    positive = a*a-b
    require(positive > 0, "positive curvature before reciprocal")
    h = a-1/separator
    require(h > 0, "positive pre-square sign")
    directed = b-h*h if direction == "above" else h*h-b
    require(directed > 0, "strict directed square margin")
    return positive, h, directed


def multiply(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return tuple(result)


def check_arcsine():
    require(ARC_DOMAIN == F(1, 5) and ARC_CUBIC == F(1, 5),
            "fixed arcsine domain and majorant")
    # t=u^2: (1+3t/5)^2(1-t)-1 = t(5-21t-9t^2)/25.
    p = list(multiply(multiply((1, 3*ARC_CUBIC), (1, 3*ARC_CUBIC)), (1, -1)))
    p[0] -= 1
    require(tuple(p) == (0, F(1, 5), F(-21, 25), F(-9, 25)),
            "arcsine polynomial identity")
    t = ARC_DOMAIN**2
    require(5-21*t-9*t*t == F(2591, 625) > 0, "arcsine positive endpoint")


def atan_sum(x, terms):
    require(type(x) is F and 0 < x < 1 and type(terms) is int and terms > 0,
            "atan domain")
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))


def check_pi():
    x, y = F(1, 5), F(1, 239)
    require(0 < y < x < 1, "Machin positive branch inputs")
    t2 = 2*x/(1-x*x)
    require(t2 == F(5, 12) and 0 < t2 < 1, "Machin double-angle branch")
    t4 = 2*t2/(1-t2*t2)
    require(t4 == F(120, 119) and (t4-y)/(1+t4*y) == 1,
            "Machin tangent identity")
    for terms in (1, 2, 3):
        p = multiply(tuple((-1)**j for j in range(terms)), (1, 1))
        require(p == (1,)+(0,)*(terms-1)+((-1)**(terms-1),),
                "finite geometric remainder identity")
    # Even partial sums below atan, odd above: signed integral remainders.
    lower = 16*atan_sum(x, 2)-4*atan_sum(y, 1)
    upper = 16*atan_sum(x, 3)-4*atan_sum(y, 2)
    require(PI_LOWER < lower < upper < PI_UPPER, "strict rational pi bounds")
    return lower, upper


def check_rows(n, rows, upper):
    endpoint(n)
    require(upper is (n == 41), "wrong chain direction")
    require((K, Q, D) == (9, 220, 10000), "fixed witness parameters")
    require(all(len(row) == 3 and all(type(v) is int for v in row) for row in rows),
            "integer triples required")
    edges = tuple((a, b) for a, b, m in rows)
    check_edges(n, rank_tour(n), edges)
    check_arcsine()
    check_pi()
    total = F(0)
    for a, b, m in rows:
        s2, u = F(a*b, (Q+a)*(Q+b)), F(m, D)
        require(0 < s2 < 1 and 0 < u < 1, "positive sine/bound domain")
        if upper:
            require(u <= ARC_DOMAIN, "arcsine bound outside domain")
            require(u*u > s2, "strict upper sine square margin")
            total += u+ARC_CUBIC*u**3
        else:
            require(s2 > u*u, "strict lower sine square margin")
            total += u
    require(total < PI_LOWER if upper else total > PI_UPPER, "strict chain sum margin")
    return total


def table_text(n, rows):
    check_rows(n, rows, n == 41)
    lines = [f"### Complete table for n={n}", "",
             "| a | b | m_e | Q_e | M_e |", "|---:|---:|---:|---:|---:|"]
    for a, b, m in rows:
        denominator = (Q+a)*(Q+b)
        margin = m*m*denominator-D*D*a*b
        if n == 42:
            margin = -margin
        lines.append(f"| {a} | {b} | {m} | {denominator} | {margin} |")
    return "\n".join(lines)


def audit():
    for n in (41, 42):
        tour = rank_tour(n)
        check_edges(n, tour, parity_edges(n))
        for orientation in (tour, tour[::-1]):
            for shift in range(len(tour)):
                moved = orientation[shift:]+orientation[:shift]
                check_edges(n, moved, cyclic_edges(moved))
        a, b = threshold_data(n)
        positive, h, margin = check_threshold(a, b, F(Q), "above" if n == 41 else "below")
        print(f"threshold n={n} A={a} B={b} A2-B={positive} H={h} directed_margin={margin}")
    check_arcsine()
    lo, hi = check_pi()
    print(f"pi lower={lo} margin={lo-PI_LOWER} upper={hi} margin={PI_UPPER-hi}")
    upper = check_rows(41, UPPER_ROWS, True)
    lower = check_rows(42, LOWER_ROWS, False)
    require(upper == F(194613679989, 62500000000), "recorded upper sum")
    require(lower == F(32503, 10000), "recorded lower sum")
    print(f"chain n=41 edges=33 upper_half_sum={upper} margin={PI_LOWER-upper}")
    print(f"chain n=42 edges=34 lower_half_sum={lower} margin={lower-PI_UPPER}")
    print("exact_bridge=PASS inequalities=4 cyclic_edges=67 symmetry_variants=134")
    print("corollary=s_9=42 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tables", action="store_true", help="print all exact witness rows")
    args = parser.parse_args()
    audit()
    if args.tables:
        for n, rows in ((41, UPPER_ROWS), (42, LOWER_ROWS)):
            print(table_text(n, rows))
