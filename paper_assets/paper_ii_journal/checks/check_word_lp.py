"""Finite exact certificates for the global-limit word LP.

SciPy discovers a sparse primal candidate and approximate dual. Fractions
independently checks every count equality and every word inequality against
directed rational cost endpoints. No production, verifier or prior-checker
imports. These bounded instances corroborate the scheme, not its all-k,r proof.
Run: python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py
"""

from fractions import Fraction as Q
from itertools import product
from math import isqrt

from scipy.optimize import linprog


SCALE = 10**30


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sqrt_interval(value):
    require(value >= 0, "negative radicand")
    low = Q(isqrt(value.numerator * SCALE**2 // value.denominator), SCALE)
    high = low if low * low == value else low + Q(1, SCALE)
    require(low * low <= value <= high * high, "root direction")
    return low, high


def span(word, roots, endpoint):
    positions = [Q(0)]
    for i in range(1, len(word)):
        positions.append(max(positions[j] + roots[word[j], word[i]][endpoint]
                             for j in range(i)))
    return positions[-1]


def solve_columns(matrix, rhs):
    """Unique exact solution on the discovered support; all rows retained."""
    rows = [list(row) + [value] for row, value in zip(matrix, rhs)]
    count = len(matrix[0])
    pivot_row = 0
    pivots = []
    for column in range(count):
        pivot = next((i for i in range(pivot_row, len(rows))
                      if rows[i][column]), None)
        require(pivot is not None, "dependent proposed support")
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [value / divisor for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                factor = rows[i][column]
                rows[i] = [x - factor*y for x, y in zip(rows[i], rows[pivot_row])]
        pivots.append((column, pivot_row))
        pivot_row += 1
    require(all(any(row[:-1]) or row[-1] == 0 for row in rows),
            "inconsistent proposed support")
    solution = [Q(0)] * count
    for column, row in pivots:
        solution[column] = rows[row][-1]
    return solution


def check_primal(weights, counts, k, r):
    require(all(value >= 0 for value in weights), "negative primal mass")
    require(sum(weights) == 1, "primal mass")
    for j in range(k):
        require(sum(p * c[j] for p, c in zip(weights, counts)) == Q(r, k),
                "primal type margin")


def check_dual(dual, counts, lower):
    for c, cost in zip(counts, lower):
        require(dual[0] + sum(y * n for y, n in zip(dual[1:], c)) <= cost,
                "dual word inequality")


def rejects(function, *args):
    try:
        function(*args)
    except ValueError:
        return
    raise ValueError("negative control unexpectedly passed")


def outward(value, lower=True, digits=9):
    scale = 10**digits
    integer = value.numerator * scale // value.denominator
    if not lower and Q(integer, scale) < value:
        integer += 1
    sign = "-" if integer < 0 else ""
    return f"{sign}{abs(integer)//scale}.{abs(integer)%scale:0{digits}d}"


def certify(k, r):
    words = list(product(range(1, k+1), repeat=r))
    roots = {(i, j): sqrt_interval(Q(i*j, k*k))
             for i in range(1, k+1) for j in range(1, k+1)}
    counts = [tuple(word.count(j) for j in range(1, k+1)) for word in words]
    lower = [span(w, roots, 0)/r for w in words]
    upper = [span(w, roots, 1)/r for w in words]
    require(all(Q(0) <= hi-lo <= Q(r-1, r*SCALE)
                for lo, hi in zip(lower, upper)), "directed path cost width")
    matrix = [[Q(1)] * len(words)]
    matrix += [[Q(c[j]) for c in counts] for j in range(k-1)]
    rhs = [Q(1)] + [Q(r, k)] * (k-1)
    found = linprog([float(v) for v in upper],
                    A_eq=[[float(v) for v in row] for row in matrix],
                    b_eq=[float(v) for v in rhs], bounds=(0, None),
                    method="highs")
    require(found.success, "LP discovery failed")
    support = [i for i, value in enumerate(found.x) if value > 1e-8]
    weights = solve_columns([[row[i] for i in support] for row in matrix], rhs)
    selected_counts = [counts[i] for i in support]
    check_primal(weights, selected_counts, k, r)
    primal_upper = sum(p * upper[i] for p, i in zip(weights, support))

    # Rationalize discovery output, then make EVERY inequality valid exactly.
    dual = [Q(float(value)).limit_denominator(10**9)
            for value in found.eqlin.marginals]
    worst = max(dual[0] + sum(y*n for y, n in zip(dual[1:], c)) - lo
                for c, lo in zip(counts, lower))
    dual[0] -= max(Q(0), worst)
    check_dual(dual, counts, lower)
    dual_lower = dual[0] + Q(r, k) * sum(dual[1:])
    require(Q(0) <= primal_upper-dual_lower < Q(1, 10**6),
            "unresolved primal-dual gap")

    # Equality cases do not depend on interval refinement termination.
    if k == 1:
        require(dual_lower == primal_upper == Q(r-1, r), "one-type exact oracle")
    if r == 2:
        pair_low = sum(roots[j, k+1-j][0] for j in range(1, k+1))/(2*k)
        pair_high = sum(roots[j, k+1-j][1] for j in range(1, k+1))/(2*k)
        require(dual_lower <= pair_high and primal_upper >= pair_low,
                "antitone two-letter oracle")

    # Prove the rational mixture creates integer equal type counts.
    denominator = 1
    from math import lcm
    for p in weights:
        denominator = lcm(denominator, p.denominator)
    multiplicities = [int(denominator * p) for p in weights]
    total_by_type = [sum(v*c[j] for v, c in zip(multiplicities, selected_counts))
                     for j in range(k)]
    require(len(set(total_by_type)) == 1, "rational recovery type counts")
    require(sum(total_by_type) == denominator*r, "rational recovery total")

    bad_weights = weights.copy()
    bad_weights[0] = -1
    rejects(check_primal, bad_weights, selected_counts, k, r)
    bad_weights = weights.copy()
    bad_weights[0] += Q(1, 7)
    rejects(check_primal, bad_weights, selected_counts, k, r)
    bad_dual = dual.copy()
    bad_dual[0] += 2
    rejects(check_dual, bad_dual, counts, lower)
    print(f"PASS k={k} r={r}: {len(words)} words; {len(support)} primal blocks; "
          f"lambda in [{outward(dual_lower)},{outward(primal_upper, False)}]; "
          "all rational primal/dual gates")
    return len(words), 3


def main():
    cases = [(1, 2), (1, 5), (2, 2), (2, 3), (3, 4), (4, 5)]
    totals = [certify(k, r) for k, r in cases]
    print(f"PASS {sum(x for x, _ in totals)} complete word inequalities; "
          f"{sum(x for _, x in totals)} corrupt certificates rejected")
    print("Scope: bounded exact LP certificates; no finite Ringmin optimum, "
          "simple closed form, or asymptotic proof by computation.")


if __name__ == "__main__":
    main()
