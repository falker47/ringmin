"""Post-proof bounded corroboration, independent of production and verifier.

Exact shell algebra; exact two-path topology for all permutations m=2..6.
70-digit roots: all permutations m=2..5 plus five explicit m=6 permutations.
180 bisections; angular/normalized Cartesian guard -1e-55. No RNG.
All numerical outputs are observations, not interval/global certificates.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import permutations
import math

import mpmath as mp
import sympy as sp


def exact_gates():
    x = sp.symbols("x")
    assert sp.expand((1+x)**2*(1-x*x)-1-x*(2-2*x*x-x**3)) == 0
    assert F(1, 2) < F(3, 4)**2  # 1/sqrt(2) < 3/4; positive sides
    assert 2-2*F(1, 2)-F(3, 4)*F(1, 2) == F(5, 8) > 0
    print("PASS: exact shell polynomial and positive rational branch gates")


def radii(P):
    return tuple(r for i, high in enumerate(P, 1) for r in (i, high))


def topology():
    counts = Counter()
    seam_paths = 0
    for m in range(2, 7):
        for P in permutations(range(m+1, 2*m+1)):
            order = radii(P)
            n = len(order)

            def high_path(path):
                assert len(path) >= 3 and len(path) % 2 == 1
                assert all(order[p] > m for p in path[::2])
                assert all(order[p] <= m for p in path[1::2])
                for left, low, right in zip(path[::2], path[1::2], path[2::2]):
                    i = order[low]-1
                    assert {order[left], order[right]} == {P[i-1], P[i]}
                    assert max(order[left], order[right]) < 2*(m+1)

            for a in range(n):
                for b in range(a+1, n):
                    # Orient mixed paths from their low endpoint.
                    start, end = (b, a) if order[a] > m >= order[b] else (a, b)
                    for direction in (-1, 1):
                        path = [start]
                        while path[-1] != end:
                            path.append((path[-1]+direction) % n)
                        assert len(path) <= n and len(set(path)) == len(path)
                        seam_paths += any({p, q} == {0, n-1}
                                          for p, q in zip(path, path[1:]))
                        if order[start] > m:
                            high_path(path)
                            counts["HH"] += 1
                        elif order[end] > m:
                            if len(path) == 2:
                                counts["LH adjacent"] += 1
                            else:
                                high_path(path[1:])
                                assert order[path[1]] > order[start]
                                counts["LH via highs"] += 1
                        else:
                            if path[1] == path[-2]:
                                assert len(path) == 3 and order[path[1]] > order[end]
                                counts["LL common high"] += 1
                            else:
                                high_path(path[1:-1])
                                assert order[path[1]] > order[start]
                                assert order[path[-2]] > order[end]
                                counts["LL via highs"] += 1
    expected = sum(math.factorial(m)*(2*m)*(2*m-1) for m in range(2, 7))
    assert sum(counts.values()) == expected and 2*seam_paths == expected
    assert all(counts[k] > 0 for k in ("HH", "LH adjacent", "LH via highs",
                                     "LL common high", "LL via highs"))
    print(f"PASS: exact topology for 872 permutations, {expected} directed paths")
    print(f"topology_counts={dict(sorted(counts.items()))}; seam_paths={seam_paths}")


def cell_data(P, R, split):
    def theta(a, b):
        return 2*mp.asin(mp.sqrt(mp.mpf(a*b)/((R+a)*(R+b))))

    gaps = [mp.mpf(0)]*(2*len(P))
    for j, right in enumerate(P):
        low, left = j+1, P[j-1]
        a, b, c = theta(left, low), theta(low, right), theta(left, right)
        extra = max(mp.mpf(0), c-a-b)
        gaps[(2*j-1) % len(gaps)] = a+split*extra
        gaps[2*j] = b+(1-split)*extra
    return mp.fsum(gaps), gaps


def root(P):
    lo, hi = mp.mpf("1e-9"), mp.mpf(16*len(P)**2)
    assert cell_data(P, lo, 0)[0] > 2*mp.pi > cell_data(P, hi, 0)[0]
    for _ in range(180):
        mid = (lo+hi)/2
        if cell_data(P, mid, 0)[0] > 2*mp.pi:
            lo = mid
        else:
            hi = mid
    assert 0 <= 2*mp.pi-cell_data(P, hi, 0)[0] < mp.mpf("1e-48")
    return hi


def audit(P, R, split=0, close=True, slack_edge=-1, transform=None):
    order = radii(P)
    total, gaps = cell_data(P, R, split)
    if close:
        assert total <= 2*mp.pi
        gaps[slack_edge] += 2*mp.pi-total
    if transform == "rotate":
        order, gaps = order[1:]+order[:1], gaps[1:]+gaps[:1]
    elif transform == "reflect":
        indices = [(-i) % len(order) for i in range(len(order))]
        gaps = [gaps[(i-1) % len(order)] for i in indices]
        order = tuple(order[i] for i in indices)
    total = mp.fsum(gaps)
    assert min(gaps) > 0
    if close:
        assert abs(total-2*mp.pi) < mp.mpf("1e-60")
    positions = [mp.mpf(0)]
    for gap in gaps[:-1]:
        positions.append(positions[-1]+gap)
    cart = ([( (R+a)*mp.cos(t), (R+a)*mp.sin(t))
             for a, t in zip(order, positions)] if close else None)
    min_angle, min_cart = mp.inf, mp.inf
    counts = Counter()
    m = len(P)
    for i, a in enumerate(order):
        for j in range(i+1, len(order)):
            b = order[j]
            # Independent scorer formula, not cell_data's asin kernel.
            required = 2*mp.atan2(mp.sqrt(a*b), mp.sqrt(R*(R+a+b)))
            arc = positions[j]-positions[i]
            min_angle = min(min_angle, arc-required, total-arc-required)
            counts["HH" if min(a, b)>m else "LL" if max(a, b)<=m else "LH"] += 2
            if close:
                dx, dy = cart[i][0]-cart[j][0], cart[i][1]-cart[j][1]
                margin = (dx*dx+dy*dy-(a+b)**2)/((R+a)*(R+b))
                min_cart = min(min_cart, margin)
    assert min_angle >= -mp.mpf("1e-55"), (P, R, split, transform, min_angle)
    assert min_cart >= -mp.mpf("1e-55"), (P, R, split, transform, min_cart)
    return min_angle, min_cart, counts


def main():
    exact_gates()
    topology()
    mp.mp.dps = 70
    cases = [(m, P) for m in range(2, 6)
             for P in permutations(range(m+1, 2*m+1))]
    cases += [(6, P) for P in ((7, 8, 9, 10, 11, 12), (12, 11, 10, 9, 8, 7),
                              (7, 12, 8, 11, 9, 10), (12, 7, 11, 8, 10, 9),
                              (10, 7, 12, 8, 11, 9))]
    worst_angle = worst_cart = mp.mpf(0)
    counts = Counter()
    audits = closed = 0
    for case_index, (m, P) in enumerate(cases, 1):
        R = root(P)
        probes = [(R, dict(split=q)) for q in (mp.mpf(0), mp.mpf(".5"), mp.mpf(1))]
        probes += [(R/10, dict(close=False))]
        edges = range(2*m) if m <= 4 else (0, m, 2*m-1)
        probes += [(2*R, dict(split=mp.mpf(".5"), slack_edge=edge)) for edge in edges]
        if m <= 4:
            probes += [(R, dict(transform=t)) for t in ("rotate", "reflect")]
        for radius, options in probes:
            a, c, count = audit(P, radius, **options)
            worst_angle, worst_cart = min(worst_angle, a), min(worst_cart, c)
            counts.update(count)
            audits += 1
            closed += options.get("close", True)
        if case_index in (2, 8, 32, 152, 157):
            print(f"PASS: high-precision cases={case_index}, latest m={m}", flush=True)
    assert len(cases) == 157
    print(f"PASS: 157 roots, {audits} path audits, {closed} closed Cartesian audits")
    print(f"directed_pair_counts={dict(sorted(counts.items()))}; total={sum(counts.values())}")
    print("min_angular_slack=" + mp.nstr(worst_angle, 9))
    print("min_normalized_cartesian_slack=" + mp.nstr(worst_cart, 9))
    print("PASS: three root splits, unclosed paths, extra closure in every small-cycle gap, symmetries")
    print("70-digit numerical observations only; exact gates are algebra/topology, not global certification.")


if __name__ == "__main__":
    main()
