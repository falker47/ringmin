"""Exact, bounded arithmetic corroboration; no production imports or tour search."""

from fractions import Fraction as Q
from math import comb, isqrt


S = (1, 7, 3, 5, 4, 6, 2, 8)
T = (2, 7, 4, 5, 6, 3, 8)
I = tuple(a for a in S if a != 1)
S12 = (2, 12, 4, 10, 6, 8, 7, 9, 5, 11, 3, 13)
T11 = (3, 12, 5, 10, 7, 8, 9, 6, 11, 4, 13)
I11 = tuple(a for a in S12 if a != 2)
PI_LO, PI_HI = Q(3141592653, 10**9), Q(3141592654, 10**9)


def edges(tour):
    assert len(tour) == len(set(tour)) >= 3
    return tuple(sorted(tuple(sorted((a, b)))
                        for a, b in zip(tour, tour[1:] + tour[:1])))


def rank_edges(size, offset):
    h = size // 2
    es = [(j, size-j) for j in range(1, h + size % 2)]
    es += [(j, size+2-j) for j in range(2, h+1 + size % 2)]
    es += [(1, size)]
    if size % 2 == 0:
        es += [(h, h+1)]
    return tuple(sorted((a+offset, b+offset) for a, b in es))


def sqrt_bounds(z, scale=10**6):
    assert z > 0
    p = isqrt((z.numerator * scale**2) // z.denominator)
    lo, hi = Q(p, scale), Q(p + 1, scale)
    assert lo**2 <= z < hi**2
    return lo, hi


def asin_poly(x):
    return sum((Q(comb(2*j, j), 4**j * (2*j+1)) * x**(2*j+1)
                for j in range(12)), Q(0))


def atan_bounds(x, terms):
    assert 0 < x < 1 and terms > 0 and terms % 2 == 0
    lo = sum(((-1)**j * x**(2*j+1) / (2*j+1)
              for j in range(terms)), Q(0))
    return lo, lo + x**(2*terms+1) / (2*terms+1)


def closure_bounds(tour, radius, method):
    lo = hi = Q(0)
    floors = []
    for a, b in edges(tour):
        if method == "asin":
            x, y = sqrt_bounds(Q(a*b) / ((radius+a)*(radius+b)))
            floors.append(int(x * 10**6))
            lo += 2 * asin_poly(x)
            hi += 2 * (asin_poly(y) + y**25 / (1-y*y))
        else:
            assert method == "atan"
            x, y = sqrt_bounds(Q(a*b) / (radius*(radius+a+b)), 10**10)
            lo += 2 * atan_bounds(x, 32)[0]
            hi += 2 * atan_bounds(y, 32)[1]
    return lo, hi, floors


def main():
    a, b = atan_bounds(Q(1, 5), 8), atan_bounds(Q(1, 239), 8)
    assert PI_LO < 16*a[0] - 4*b[1]
    assert 16*a[1] - 4*b[0] < PI_HI
    assert set(S) == set(range(1, 9))
    assert set(T) == set(I) == set(range(2, 9))
    assert set(edges(I)) == (set(edges(S)) - {(1, 7), (1, 8)}) | {(7, 8)}
    assert set(S12) == set(range(2, 14))
    assert set(T11) == set(I11) == set(range(3, 14))
    assert set(edges(I11)) == (set(edges(S12)) - {(2, 12), (2, 13)}) | {(12, 13)}
    for tour, offset in ((S, 0), (T, 1), (S12, 1), (T11, 2)):
        assert edges(tour) == rank_edges(len(tour), offset)
    gates = (
        ("S lower", S, Q(23, 4), 628726, 628728, "above"),
        ("S upper", S, Q(144, 25), 628049, 628051, "below"),
        ("T upper", T, Q(23, 4), 626827, 626829, "below"),
        ("I lower", I, Q(577, 100), 630128, 630131, "above"),
        ("S12 lower", S12, Q(1827, 100), 628508, 628512, "above"),
        ("S12 upper", S12, Q(457, 25), 628255, 628258, "below"),
        ("T11 upper", T11, Q(1827, 100), 626690, 626694, "below"),
        ("I11 lower", I11, Q(183, 10), 630763, 630766, "above"),
    )
    for name, tour, r, left, right, sign in gates:
        lo, hi, floors = closure_bounds(tour, r, "asin")
        print(name, "radius=", r, "sqrt floors=", floors)
        print("closure floor/ceiling at 1e-5:", lo*10**5 // 1,
              -(hi*10**5 // -1))
        assert Q(left, 10**5) < lo < hi < Q(right, 10**5)
        alo, ahi, _ = closure_bounds(tour, r, "atan")
        assert Q(left, 10**5) < alo < ahi < Q(right, 10**5)
        if sign == "above":
            assert Q(left, 10**5) > 2*PI_HI
        else:
            assert Q(right, 10**5) < 2*PI_LO
    # The analytic proof covers all rectangles/tours; these are its constants.
    epsilon = Q(1, 2000)
    assert Q(1, 880) > 2*epsilon
    assert Q(32, 15) < 3
    assert Q(144, 25) + epsilon/3 < Q(577, 100)
    assert Q(2, 4095) > 2*Q(1, 5000)
    assert Q(39, 70) < 1
    assert Q(457, 25) + Q(1, 5000) < Q(183, 10)
    # Smallest-cardinality incompatibility is a rank-edge identity.
    s5, s4 = (1, 4, 3, 2, 5), (2, 4, 3, 5)
    assert edges(s5) == rank_edges(5, 0)
    assert edges(s4) == rank_edges(4, 1)
    assert edges(tuple(a for a in s5 if a != 1)) != edges(s4)
    print("PASS: 8 rational closure gates by two formulas; pi, gap constants,")
    print("cyclic deletion and five/four rank obstruction. No tour enumeration.")


if __name__ == "__main__":
    main()
