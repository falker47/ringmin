"""Bounded independent corroboration of common-chain Section 11.6.

Six fixed prescribed cycles, not general-tour enumeration. Standard library
only; no production, previous-checker, certificate or network imports.
Construct/filter the rank traversal and compare full signed costs against
the local formula as formal integer linear combinations of radicals.
Exact rational Taylor gates certify each actual floor. Integer square-root
enclosures corroborate signs and asymptotics, not the infinite theorem.
"""

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import factorial, isqrt


WIDTHS = (40, 50, 80, 120, 200, 400)
TAU_LO = Q("0.7390851332151606416553120876738734040134")
TAU_HI = Q("0.7390851332151606416553120876738734040135")
Q_LO = Q("0.1950200913506069300798071259134151019366")
Q_HI = Q("0.1950200913506069300798071259134151019367")
BETA = Q(23, 100)
SCALE = 10**60


def parameter_gates():
    def trig_sum(x, terms, sine=False):
        return sum((-1)**j * x**(2*j+int(sine))
                   / factorial(2*j+int(sine)) for j in range(terms))

    assert 0 < TAU_LO < TAU_HI < 1
    # Even term count ends negative (lower bound); odd ends positive.
    assert trig_sum(TAU_LO, 42) > TAU_LO
    assert trig_sum(TAU_HI, 41) < TAU_HI
    sin_lo = trig_sum(TAU_LO, 42, sine=True)
    sin_hi = trig_sum(TAU_HI, 41, sine=True)
    assert Q_LO < (1-sin_hi)/(1+sin_hi)
    assert (1-sin_lo)/(1+sin_lo) < Q_HI
    assert Q(3, 17) < Q_LO < Q_HI < Q(1, 5)
    print("exact rational optimizer gates: PASS")


def rank_cycle(k, n):
    """Direct two-arm traversal specification, independent of edge formulas."""
    size = n-k+1
    half = (size+1)//2
    arms = []
    for start in (1, 2):
        arm = []
        j = 0
        while True:
            low, high = start+2*j, size-start-2*j
            additions = ([low] if low <= half else [])
            additions += [high] if high > half else []
            if not additions:
                break
            arm.extend(additions)
            j += 1
        arms.append(arm)
    return tuple(k+rank-1 for rank in arms[0]+arms[1][::-1]+[size])


def edges(walk):
    return tuple(zip(walk, walk[1:]+walk[:1]))


def edge_set(edge_list):
    return {tuple(sorted(edge)) for edge in edge_list}


def formal(constant, radicals):
    """Canonical syntax; no approximate radical simplification is used."""
    return constant, tuple(sorted((r, c) for r, c in radicals.items() if c))


def direct_score(walk, k, n, ell):
    """Filter an actual cyclic traversal and subtract full W and D_n sums."""
    assert len(walk) == len(set(walk)) == n-k+1
    assert set(walk) == set(range(k, n+1))
    outer = edges(walk)
    survivors = tuple(i for i in walk if i >= ell)
    inner = edges(survivors)
    assert len(survivors) == n-ell+1 >= 3
    assert len(edge_set(outer)) == len(outer)
    assert len(edge_set(inner)) == len(inner)
    assert Counter(v for pair in outer for v in pair) == Counter(
        {i: 2 for i in range(k, n+1)})

    total = n+k
    radical_cost = Counter(u*v for u, v in inner)
    radical_cost.subtract(u*v for u, v in outer)
    constant = 0
    for j in range(k, ell):
        constant -= total-j
        radical_cost[j*(total-j)] += 2

    # Recover actual deletion neighbors from the traversal, including wrap.
    replacement, removed = [], []
    defect_sums = {}
    for position, j in enumerate(walk):
        if j >= ell:
            continue
        left = walk[position-1]
        right = walk[(position+1) % len(walk)]
        assert left >= ell and right >= ell  # Every deletion is isolated.
        replacement.append((left, right))
        removed.extend(((left, j), (j, right)))
        defect_sums[j] = left+right+2*j-2*total
    assert len(removed) == 2*(ell-k)
    assert len(edge_set(replacement)) == ell-k
    assert edge_set(outer)-edge_set(inner) == edge_set(removed)
    assert edge_set(inner)-edge_set(outer) == edge_set(replacement)
    energy_numerator = sum((u+v-total)**2 for u, v in outer)
    return formal(constant, radical_cost), defect_sums, energy_numerator


def local_formula(k, n, ell, m):
    """Equation (39f), using only j,d and S, not traversal neighbors."""
    total = n+k
    constant = -n
    radicals = Counter({n*(n-1): 1, k*n: 1, k*(n-1): -1})
    for j in range(k+1, ell):
        displacement = m if j >= ell-m else 0
        reflected = total-j
        center = reflected-displacement
        constant -= reflected
        radicals[center*center-1] += 1
        radicals[j*(center-1)] -= 1
        radicals[j*(center+1)] -= 1
        radicals[j*reflected] += 2
    return formal(constant, radicals)


def sqrt_interval(value):
    value = Q(value)
    assert value >= 0
    root = isqrt(value.numerator*SCALE*SCALE//value.denominator)
    lo, hi = Q(root, SCALE), Q(root+1, SCALE)
    assert lo*lo <= value < hi*hi
    return lo, hi


def expression_interval(expression, denominator):
    constant, radicals = expression
    lo = hi = Q(constant)
    for radicand, coefficient in radicals:
        root_lo, root_hi = sqrt_interval(radicand)
        lo += coefficient*(root_lo if coefficient > 0 else root_hi)
        hi += coefficient*(root_hi if coefficient > 0 else root_lo)
    return lo/denominator, hi/denominator


def coefficient_intervals():
    t_lo, t_hi = 1+Q_LO-BETA, 1+Q_HI-BETA
    ratio_lo = sqrt_interval(BETA/t_hi)[0]
    ratio_hi = sqrt_interval(BETA/t_lo)[1]
    a_lo, a_hi = 1-ratio_hi, 1-ratio_lo
    product_lo = sqrt_interval(BETA*t_lo)[0]
    product_hi = sqrt_interval(BETA*t_hi)[1]
    c_lo, c_hi = 1/(4*product_hi), 1/(4*product_lo)
    # The limit is A_q / 4^(2/3); cube to avoid a numerical cube root.
    assert 16*Q(203, 1000)**3 < a_lo**3
    assert a_hi**3 < 16*Q(204, 1000)**3
    print("exact limit enclosure: 0.203 < A_q/4^(2/3) < 0.204 PASS")
    return (a_lo, a_hi), (c_lo, c_hi)


def decimal_value(value):
    return Decimal(value.numerator)/Decimal(value.denominator)


def main():
    if not __debug__:
        raise SystemExit("Do not run this assert-based checker with -O")
    parameter_gates()
    a_bounds, c_bounds = coefficient_intervals()
    parities = set()
    variants_checked = 0
    for m in WIDTHS:
        n = m*m
        k = (Q_LO*n).__floor__()
        assert k == (Q_HI*n).__floor__()
        assert 23*n % 100 == 0
        ell = 23*n//100
        size = n-k+1
        parities.add(size % 2)
        base = rank_cycle(k, n)

        def exchange(j):
            if ell-m <= j < ell:
                return j+m
            if ell <= j < ell+m:
                return j-m
            return j

        walk = tuple(map(exchange, base))
        assert all(exchange(exchange(j)) == j for j in base)
        # Put a swapped deleted label at the written wrap, then reverse it.
        cut = walk.index(ell-m)
        rotated = walk[cut:]+walk[:cut]
        variants = (walk, rotated, rotated[::-1])
        expected = local_formula(k, n, ell, m)
        c_n = 1 if size % 2 else 2
        expected_energy = 4*m**3+size-c_n
        expected_defects = {j: (-1 if j == k else
                               -2*m if j >= ell-m else 0)
                            for j in range(k, ell)}
        for variant in variants:
            observed, defects, energy_numerator = direct_score(
                variant, k, n, ell)
            assert observed == expected, (m, "formal radical mismatch")
            assert defects == expected_defects, (m, "first variation mismatch")
            assert energy_numerator == expected_energy
            variants_checked += 1

        delta_lo, delta_hi = expression_interval(observed, n*n)
        assert delta_hi < 0
        assert delta_hi-delta_lo < Q(1, 10**40)
        remainder_lo = m**4*(delta_lo+a_bounds[0]/m**2+c_bounds[0]/m**3)
        remainder_hi = m**4*(delta_hi+a_bounds[1]/m**2+c_bounds[1]/m**3)
        assert remainder_hi-remainder_lo < Q(1, 10**30)
        with localcontext() as ctx:
            ctx.prec = 40
            delta = decimal_value((delta_lo+delta_hi)/2)
            energy = decimal_value(Q(expected_energy, n**3))
            ratio = -delta / energy**(Decimal(2)/3)
            remainder = decimal_value((remainder_lo+remainder_hi)/2)
            print(f"m={m}, n={n}, k={k}, N={size}: exact identities/sign PASS; "
                  f"m^2*Delta~{m*m*delta:.12f}, "
                  f"|Delta|/E^(2/3)~{ratio:.12f}, "
                  f"m^4 remainder~{remainder:.12f}")
    assert parities == {0, 1}
    print(f"{len(WIDTHS)} actual floors; both N parities; "
          f"{variants_checked} rotations/reversals: PASS")
    print("Full cyclic signed radical identity, induced replacement edges, "
          "wrap, defect sums, E and negative Delta: PASS")
    print("Remainder values are finite corroboration; no inference of a "
          "uniform bound or infinite theorem from these six sizes.")


if __name__ == "__main__":
    main()
