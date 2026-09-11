"""Bounded exact diagnostics for common-chain Section 11.5.

Six prescribed relabeled cycles, no tour enumeration or optimization.
The rank-list constructor and the direct cyclic/oriented-edge scorer are
separate from the formulas under test. Standard library only; no production,
certificate, previous-checker or network imports. Run normally, not with -O.
The infinite-family proof is analytic, not inferred from these diagnostics.
"""

from collections import Counter
from fractions import Fraction as Q
from math import factorial


WIDTHS = (40, 50, 60, 80, 100, 120)
TAU_LO = Q("0.7390851332151606416553120876738734040134")
TAU_HI = Q("0.7390851332151606416553120876738734040135")
Q_LO = Q("0.1950200913506069300798071259134151019366")
Q_HI = Q("0.1950200913506069300798071259134151019367")


def parameter_gates():
    # Alternating Taylor bounds on (0,1), independently recomputed here.
    def cosine(x, terms):
        return sum((-1)**j * x**(2*j) / factorial(2*j)
                   for j in range(terms))

    def sine(x, terms):
        return sum((-1)**j * x**(2*j+1) / factorial(2*j+1)
                   for j in range(terms))

    assert 0 < TAU_LO < TAU_HI < 1
    assert cosine(TAU_LO, 42) > TAU_LO  # Last term negative: lower bound.
    assert cosine(TAU_HI, 41) < TAU_HI  # Last term positive: upper bound.
    sin_lo, sin_hi = sine(TAU_LO, 42), sine(TAU_HI, 41)
    assert Q_LO < (1-sin_hi)/(1+sin_hi)
    assert (1-sin_lo)/(1+sin_lo) < Q_HI
    assert Q(3, 17) < Q_LO < Q_HI < Q(1, 5)
    print("exact rational optimizer bracket: PASS")


def canonical_cycle(k, n):
    """Rank lists of FIXED_K_SUPNICK_SEAM.md, Section 1."""
    size = n-k+1
    half = (size+1)//2
    arms = []
    for start in (1, 2):
        arm = []
        for low in range(start, half+1, 2):
            arm.append(low)
            if size-low > half:
                arm.append(size-low)
        arms.append(arm)
    return tuple(k+rank-1 for rank in arms[0]+arms[1][::-1]+[size])


def cyclic_edges(walk):
    return tuple(zip(walk, walk[1:]+walk[:1]))


def score(walk, k, n, ell):
    """Score actual cyclic edges, using twice-integer midpoint signs."""
    size = n-k+1
    assert len(walk) == len(set(walk)) == size
    assert set(walk) == set(range(k, n+1))
    edges = cyclic_edges(walk)
    assert len({tuple(sorted(edge)) for edge in edges}) == size
    degree = Counter(v for edge in edges for v in edge)
    assert degree == Counter({i: 2 for i in range(k, n+1)})
    total = n+k
    pairs = [(x, total-y) for u, v in edges
             for x, y in ((u, v), (v, u))]
    assert Counter(x for x, _ in pairs) == degree
    assert Counter(z for _, z in pairs) == degree
    assert Counter((total-z, total-x) for x, z in pairs) == Counter(pairs)
    energy_numerator = sum((u+v-total)**2 for u, v in edges)
    assert sum((x-z)**2 for x, z in pairs) == 2*energy_numerator
    assert sum(x**3-z**3 for x, z in pairs) == 0
    crossing = [(x, z) for x, z in pairs
                if (2*x-2*ell+1)*(2*z-2*ell+1) < 0]
    crossing_numerator = sum(abs(x-z) for x, z in crossing)
    # The returned normalizations are n^3*E and 2*n^2*K.
    return energy_numerator, crossing_numerator, len(crossing)


def main():
    if not __debug__:
        raise SystemExit("Do not run this assert-based diagnostic with -O")
    parameter_gates()
    parities = set()
    count = 0
    for m in WIDTHS:
        n = m*m
        k = (Q_LO*n).__floor__()
        assert k == (Q_HI*n).__floor__()
        assert 23*n % 100 == 0
        ell = 23*n//100
        assert k+1 <= ell-m and 2*(ell+m) < n
        size = n-k+1
        zero_count = 1 if size % 2 else 2
        parities.add(size % 2)
        base = canonical_cycle(k, n)
        base_edges = cyclic_edges(base)
        defects = Counter(u+v-n-k for u, v in base_edges)
        assert set(defects) == {-1, 0, 1}
        assert defects[0] == zero_count
        assert score(base, k, n, ell) == (size-zero_count, 2, 2)

        def exchange(i):
            if ell-m <= i < ell:
                return i+m
            if ell <= i < ell+m:
                return i-m
            return i

        touched = set(range(ell-m, ell+m))
        affected = [(u, v) for u, v in base_edges
                    if u in touched or v in touched]
        assert len(affected) == 4*m
        assert all((u in touched) != (v in touched) for u, v in affected)
        for i in touched:
            assert exchange(exchange(i)) == i
        walk = tuple(map(exchange, base))
        cut = walk.index(ell-m)  # A changed vertex at the written wrap.
        variants = (walk, walk[cut:]+walk[:cut], walk[::-1])
        expected = (4*m**3+size-zero_count, 4*m*m-2*m+2, 4*m-2)
        for variant in variants:
            observed = score(variant, k, n, ell)
            assert observed == expected, (m, observed, expected)
            energy = Q(observed[0], n**3)
            crossing = Q(observed[1], 2*n*n)
            assert Q(4, m**3) <= energy <= Q(5, m**3)
            assert Q(1, m*m) <= crossing <= Q(2, m*m)
            assert 25*crossing**3 >= energy**2  # K >= 5^(-2/3) E^(2/3).
            assert crossing**3 <= 125*energy**2  # Existing all-tour bound.
            count += 1
        print(f"m={m}, n={n}, k={k}, N={size}: "
              f"n^3*E={expected[0]}, 2*n^2*K={expected[1]}, "
              f"crossings={expected[2]} PASS")
    assert parities == {0, 1}
    print(f"exact floors and base cycles: {len(WIDTHS)}; both N parities PASS")
    print(f"relabeled cycles: {count} orientations; degree, both marginals, "
          "reflection symmetry, wrap, E/K formulas and bounds PASS")
    print("No tour enumeration; finite diagnostics only, not the all-n proof.")


if __name__ == "__main__":
    main()
