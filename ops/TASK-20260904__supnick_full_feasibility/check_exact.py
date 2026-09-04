"""Independent symbolic and finite combinatorial audit of the proof note.

No production or diagnostic imports. No numerical roots or transcendental
approximations. This checks identities/transcription, not a proof assistant
derivation of the imported all-k seam theorem.
"""

from collections import Counter
from fractions import Fraction

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def same(lhs, rhs, name):
    require(sp.simplify(lhs - rhs) == 0, name)


def edge(a, b):
    return tuple(sorted((a, b)))


def rank_tour(k, n):
    size = n - k + 1
    middle = (size + 1) // 2
    first, second = [], []
    for rank in range(1, middle + 1):
        arm = first if rank % 2 else second
        arm.append(k + rank - 1)
        partner = size - rank
        if partner > middle:
            arm.append(k + partner - 1)
    return first + list(reversed(second)) + [n]


def actual_edges(tour):
    return Counter(edge(a, tour[(i + 1) % len(tour)])
                   for i, a in enumerate(tour))


def parity_edges(k, n):
    size, total = n - k + 1, n + k
    half = size // 2
    result = Counter([edge(k, n)])
    if size % 2:
        result.update(edge(i, total - 1 - i) for i in range(k, k + half))
        result.update(edge(i, total + 1 - i) for i in range(k + 1, k + half + 1))
    else:
        result.update([edge(k + half - 1, k + half)])
        result.update(edge(i, total - 1 - i) for i in range(k, k + half - 1))
        result.update(edge(i, total + 1 - i) for i in range(k + 1, k + half))
    return result


def symmetrized_edges(k, n, correct=True):
    size, total = n - k + 1, n + k
    result = Counter({edge(k, n): Fraction(1)})
    for i in range(k, n):
        result[edge(i, total - 1 - i)] += Fraction(1, 2)
    for i in range(k + 1, n + 1):
        result[edge(i, total + 1 - i)] += Fraction(1, 2)
    if correct and size % 2 == 0:
        p = (total - 1) // 2
        result[edge(p, p)] -= Fraction(1, 2)
        result[edge(p + 1, p + 1)] -= Fraction(1, 2)
        result[edge(p, p + 1)] += 1
    return result


def path_coefficients(path):
    result = Counter(edge(a, b) for a, b in zip(path, path[1:]))
    result[edge(path[0], path[-1])] -= 1
    return result


def fan_coefficients(path):
    result = Counter()
    for j in range(1, len(path) - 1):
        result[edge(path[0], path[j])] += 1
        result[edge(path[j], path[j + 1])] += 1
        result[edge(path[0], path[j + 1])] -= 1
    return result


def audit_tour(tour, k, n):
    require(sorted(tour) == list(range(k, n + 1)), "vertex multiplicity")
    require(actual_edges(tour) == parity_edges(k, n), "cyclic edges")


def expect_rejection(action, name):
    try:
        action()
    except RuntimeError:
        return
    raise RuntimeError(f"rejection gate did not reject: {name}")


def main():
    print(f"EXACT IDENTITY AUDIT; SymPy={sp.__version__}; no numeric roots")
    radius, a, b = sp.symbols("R a b", positive=True)
    theta = 2 * sp.asin(sp.sqrt(a * b / ((radius + a) * (radius + b))))
    first = sp.sqrt(radius * b / a) / ((radius + a) * sp.sqrt(radius + a + b))
    mixed = sp.sqrt(radius) / (2 * sp.sqrt(a * b) * (radius + a + b) ** sp.Rational(3, 2))
    same(sp.diff(theta, a), first, "original kernel first derivative")
    same(sp.diff(theta, a, b), mixed, "original kernel mixed derivative")
    x, y = sp.symbols("x y", positive=True)
    transformed = 2 * sp.asin(x * y)
    same(sp.diff(transformed, x, y), 2 / (1 - x*x*y*y) ** sp.Rational(3, 2),
         "transformed mixed derivative")
    same(sp.diff(sp.sqrt(a / (radius + a)), a),
         radius / (2 * sp.sqrt(a) * (radius + a) ** sp.Rational(3, 2)),
         "increasing radius parametrization")
    # Geometry identity used after BOTH path inequalities, not just one.
    expected_cosine = 1 - 2 * a * b / ((radius + a) * (radius + b))
    distance_sq = (radius + a)**2 + (radius + b)**2 - 2*(radius + a)*(radius + b)*expected_cosine
    same(distance_sq, (a + b)**2, "Cartesian contact identity")
    energy, ab, bc, ac = sp.symbols("E theta_ab theta_bc theta_ac")
    same((energy - ab) + (ab + bc - ac), energy + bc - ac,
         "arbitrary path induction step")
    expect_rejection(lambda: same(sp.diff(theta, a, b), -mixed, "bad derivative"),
                     "mixed derivative sign")
    print("PASS: 6 symbolic identities; 1 wrong-sign rejection")

    cycles, total_edges, pairs, paths, rejections = 0, 0, 0, 0, 1
    for k in (6, 7, 8, 9):
        n = 4 * k + 5
        tour = rank_tour(k, n)
        size = len(tour)
        audit_tour(tour, k, n)
        expected = parity_edges(k, n)
        require(expected == symmetrized_edges(k, n), "central angular correction")
        where = tour.index(k)
        require({tour[(where - 1) % size], tour[(where + 1) % size]} == {n - 1, n},
                "both seam neighbors")
        # Check every rotation and reflection using the independent edge formula.
        for reflected in (tour, list(reversed(tour))):
            for shift in range(size):
                audit_tour(reflected[shift:] + reflected[:shift], k, n)
        for i in range(size):
            for j in range(i + 1, size):
                forward = tour[i:j + 1]
                wrap = tour[j:] + tour[:i + 1]
                require(len(forward) + len(wrap) - 2 == size, "path edge counts")
                both = actual_edges(tour)
                path_union = Counter(edge(a, b) for path in (forward, wrap)
                                     for a, b in zip(path, path[1:]))
                require(path_union == both, "complementary edge coverage")
                for path in (forward, wrap):
                    require(len(set(path)) == len(path), "simple path")
                    require(path_coefficients(path) == fan_coefficients(path),
                            "formal telescoping coefficients")
                    paths += 1
                pairs += 1
        bad_tour = tour[:-1] + [tour[0]]
        expect_rejection(lambda: audit_tour(bad_tour, k, n), "duplicate vertex")
        rejections += 1
        omitted_closure = Counter(edge(a, b) for a, b in zip(tour, tour[1:]))
        expect_rejection(lambda: require(omitted_closure == expected, "missing closure"),
                         "missing closing edge")
        rejections += 1
        if size % 2 == 0:
            expect_rejection(lambda: require(expected == symmetrized_edges(k, n, False),
                                              "missing central correction"),
                             "omitted even correction")
            rejections += 1
        cycles += 1
        total_edges += size
    print(f"PASS: {cycles} rank/parity constructions, {total_edges} edges; "
          "all rotations/reflections; both central-correction cases")
    print(f"PASS: {pairs} unordered pairs, {paths} directed paths; "
          "formal telescoping and complementary coverage")
    print(f"PASS: {rejections} rejection gates total")
    print("LIMIT: finite audits guard transcription; the note supplies the all-k proof")


if __name__ == "__main__":
    main()
