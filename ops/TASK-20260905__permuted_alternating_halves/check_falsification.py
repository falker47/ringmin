"""Pre-proof bounded falsification; no production/verifier/old-checker imports.

All m! permutations for m=2..6, no RNG or symmetry quotient. Seven probes
per order: five absolute scales and two near the conjectured cell root.
LP constraints use positions and both directions for every pair, never cells.
Numerical observations only. Stop and print the first discrepant input.
"""

from itertools import permutations
import math

import numpy as np
from scipy.optimize import linprog


def cell_sum(P, R):
    def theta(a, b):
        return 2 * math.asin(math.sqrt(a*b/((R+a)*(R+b))))

    return math.fsum(max(theta(i, right) + theta(left, i), theta(left, right))
                     for i, (left, right) in enumerate(zip(P[-1:]+P[:-1], P), 1))


def cell_root(P):
    lo, hi = 1e-9, 16.0 * len(P)**2
    assert cell_sum(P, lo) > math.tau > cell_sum(P, hi)
    for _ in range(64):
        mid = (lo+hi)/2
        if cell_sum(P, mid) > math.tau:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def full_lp(order, R):
    n = len(order)
    rows, upper = [], []
    for i in range(n):
        for j in range(i+1, n):
            a, b = order[i], order[j]
            # Half-angle atan2 from the law of cosines; independent of asin.
            theta = 2 * math.atan2(math.sqrt(a*b), math.sqrt(R*(R+a+b)))
            row = np.zeros(n)
            row[j], row[i] = 1, -1
            rows.extend((row, -row))
            upper.extend((math.tau-theta, -theta))
    matrix, rhs = np.array(rows), np.array(upper)
    result = linprog(np.zeros(n), A_ub=matrix, b_ub=rhs,
                     bounds=[(0, 0)] + [(None, None)]*(n-1), method="highs",
                     options={"primal_feasibility_tolerance": 1e-9,
                              "dual_feasibility_tolerance": 1e-9})
    assert result.status in (0, 2), (order, R, result.message)
    if result.status == 0:
        assert np.min(rhs-matrix@result.x) >= -1e-7, (order, R, result.x)
    return result.status == 0


def main():
    orders = probes = 0
    min_margin = math.inf
    for m in range(2, 7):
        count = 0
        for P in permutations(range(m+1, 2*m+1)):
            order = tuple(r for i, high in enumerate(P, 1) for r in (i, high))
            root = cell_root(P)
            radii = [m*m*s for s in (1e-6, .01, .1, 1, 100)]
            radii += [root*(1-1e-5), root*(1+1e-5)]
            for R in radii:
                margin = math.tau-cell_sum(P, R)
                assert abs(margin) > 1e-7, ("undecided boundary", m, P, R, margin)
                actual = full_lp(order, R)
                if actual != (margin > 0):
                    print(f"DISCREPANCY m={m} P={P} R={R!r} "
                          f"cell_margin={margin!r} lp_feasible={actual}", flush=True)
                    raise AssertionError("retain and analyze this numerical candidate")
                min_margin = min(min_margin, abs(margin))
                probes += 1
            count += 1
        assert count == math.factorial(m)
        orders += count
        print(f"PASS m={m}: {count} permutations, {7*count} independent LP probes", flush=True)
    assert orders == 872 and probes == 6104
    print(f"PASS: {orders} permutations, {probes} probes, no discrepancy")
    print(f"min_abs_cell_margin={min_margin:.9g}")
    print("Numerical falsification only; no all-m proof or global certificate.")


if __name__ == "__main__":
    main()
