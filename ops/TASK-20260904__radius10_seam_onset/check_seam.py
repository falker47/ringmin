#!/usr/bin/env python3
"""Exact radius-10 endpoint audit; stdlib only, no production/diagnostic import.

Only n=45,46 and R=270 are evaluated. All proof arithmetic uses integers
and Fraction; explicit exceptions retain the gates under python -O.
"""

import argparse
from collections import Counter
from fractions import Fraction as F

K, Q, D = 10, 270, 10000
PI_LOWER, PI_UPPER = F(157, 50), F(22, 7)
ARC_DOMAIN, ARC_CUBIC = F(1, 5), F(1, 5)

# (a, b, m): bound m/D for sqrt(ab/((Q+a)(Q+b))).
# Complete parity-family order, including closure (10,n) as the first row.
UPPER_ROWS = (
    (10, 45, 715), (27, 28, 925), (10, 44, 708), (11, 43, 734),
    (12, 42, 757), (13, 41, 779), (14, 40, 798), (15, 39, 816),
    (16, 38, 831), (17, 37, 845), (18, 36, 858), (19, 35, 869),
    (20, 34, 879), (21, 33, 887), (22, 32, 894), (23, 31, 900),
    (24, 30, 904), (25, 29, 907), (26, 28, 909), (11, 45, 748),
    (12, 44, 773), (13, 43, 795), (14, 42, 815), (15, 41, 833),
    (16, 40, 850), (17, 39, 865), (18, 38, 879), (19, 37, 891),
    (20, 36, 901), (21, 35, 911), (22, 34, 918), (23, 33, 925),
    (24, 32, 931), (25, 31, 935), (26, 30, 938), (27, 29, 940),
)
LOWER_ROWS = (
    (10, 46, 721), (10, 45, 714), (11, 44, 740), (12, 43, 764),
    (13, 42, 786), (14, 41, 806), (15, 40, 824), (16, 39, 840),
    (17, 38, 854), (18, 37, 867), (19, 36, 879), (20, 35, 889),
    (21, 34, 898), (22, 33, 905), (23, 32, 912), (24, 31, 916),
    (25, 30, 920), (26, 29, 923), (27, 28, 924), (11, 46, 754),
    (12, 45, 779), (13, 44, 802), (14, 43, 822), (15, 42, 841),
    (16, 41, 858), (17, 40, 874), (18, 39, 888), (19, 38, 900),
    (20, 37, 911), (21, 36, 921), (22, 35, 929), (23, 34, 936),
    (24, 33, 942), (25, 32, 947), (26, 31, 951), (27, 30, 953),
    (28, 29, 954),
)


class AuditFailure(ValueError):
    """An exact proof gate failed."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def endpoint(n):
    require(type(n) is int and n in (45, 46), "only endpoints 45,46 allowed")


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
    if n == 45:  # N=36=2*18
        return ((10, 45), (27, 28)) + tuple((i, 54-i) for i in range(10, 27)) + tuple(
            (i, 56-i) for i in range(11, 28))
    # N=37=2*18+1
    return ((10, 46),) + tuple((i, 55-i) for i in range(10, 28)) + tuple(
        (i, 57-i) for i in range(11, 29))


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


def check_sine(s2, u, upper):
    """One directed strict square witness; equality is never accepted."""
    require(type(s2) is F and type(u) is F and type(upper) is bool,
            "Fraction sine inputs and boolean direction required")
    require(0 < s2 < 1 and 0 < u < 1, "positive sine/bound domain")
    if upper:
        require(u <= ARC_DOMAIN, "arcsine bound outside domain")
        require(u*u > s2, "strict upper sine square margin")
        return u+ARC_CUBIC*u**3
    require(s2 > u*u, "strict lower sine square margin")
    return u


def check_rows(n, rows, upper):
    endpoint(n)
    require(upper is (n == 45), "wrong chain direction")
    require((K, Q, D) == (10, 270, 10000), "fixed witness parameters")
    require(all(len(row) == 3 and all(type(v) is int for v in row) for row in rows),
            "integer triples required")
    edges = tuple((a, b) for a, b, m in rows)
    check_edges(n, rank_tour(n), edges)
    check_arcsine()
    check_pi()
    total = F(0)
    for a, b, m in rows:
        s2, u = F(a*b, (Q+a)*(Q+b)), F(m, D)
        total += check_sine(s2, u, upper)
    require(total < PI_LOWER if upper else total > PI_UPPER, "strict chain sum margin")
    return total


def table_text(n, rows):
    check_rows(n, rows, n == 45)
    lines = [f"### Complete table for n={n}", "",
             "| a | b | m_e | Q_e | M_e |", "|---:|---:|---:|---:|---:|"]
    for a, b, m in rows:
        denominator = (Q+a)*(Q+b)
        margin = m*m*denominator-D*D*a*b
        if n == 46:
            margin = -margin
        lines.append(f"| {a} | {b} | {m} | {denominator} | {margin} |")
    return "\n".join(lines)


def audit():
    for n in (45, 46):
        tour = rank_tour(n)
        check_edges(n, tour, parity_edges(n))
        for orientation in (tour, tour[::-1]):
            for shift in range(len(tour)):
                moved = orientation[shift:]+orientation[:shift]
                check_edges(n, moved, cyclic_edges(moved))
        a, b = threshold_data(n)
        positive, h, margin = check_threshold(a, b, F(Q), "above" if n == 45 else "below")
        print(f"threshold n={n} A={a} B={b} A2-B={positive} H={h} directed_margin={margin}")
    check_arcsine()
    lo, hi = check_pi()
    print(f"pi lower={lo} margin={lo-PI_LOWER} upper={hi} margin={PI_UPPER-hi}")
    upper = check_rows(45, UPPER_ROWS, True)
    lower = check_rows(46, LOWER_ROWS, False)
    require(upper == F(15404369802693, 5000000000000), "recorded upper sum")
    require(lower == F(8011, 2500), "recorded lower sum")
    print(f"chain n=45 edges=36 upper_half_sum={upper} margin={PI_LOWER-upper}")
    print(f"chain n=46 edges=37 lower_half_sum={lower} margin={lower-PI_UPPER}")
    print("exact_bridge=PASS inequalities=4 cyclic_edges=73 symmetry_variants=146")
    print("corollary=s_10=46 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tables", action="store_true", help="print all exact witness rows")
    args = parser.parse_args()
    audit()
    if args.tables:
        for n, rows in ((45, UPPER_ROWS), (46, LOWER_ROWS)):
            print(table_text(n, rows))
