"""Independent bounded audit of the adjacent-high-swap note.

No production, verify.py, or previous checker imports. Symbolic algebra and
Fraction enclosures are exact. mpmath comparisons are finite observations.
The asin interval tail uses positive coefficients <=1 and 300 terms;
integer square-root endpoints have denominator 10**40. No RNG.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import isqrt

import mpmath as mp
import sympy as sp


def symbolic_checks():
    R, a, b = sp.symbols('R a b', positive=True)
    theta = 2*sp.asin(sp.sqrt(a*b/((R+a)*(R+b))))
    h = sp.sqrt(R*a)/(sp.sqrt(b)*(R+b)*sp.sqrt(R+a+b))
    mixed = sp.sqrt(R)/(2*sp.sqrt(a*b)*(R+a+b)**sp.Rational(3, 2))
    assert sp.simplify(sp.diff(theta, b)-h) == 0
    assert sp.simplify(sp.diff(h, a)-mixed) == 0
    A, c, d, z = sp.symbols('A c d z', positive=True)
    pocket = A+c+d+2*z
    relation = z*z-(A*c+A*d+c*d)
    polys = [((A+c)*pocket+A*c)-(A+c+z)**2,
             ((A+d)*pocket+A*d)-(A+d+z)**2,
             (A+c+z)*(A+d+z)-A*A-z*(2*A+c+d+2*z)]
    for poly in polys:
        assert sp.rem(sp.expand(poly), relation, z) == 0
    k, s, p, w = sp.symbols('k s p w', positive=True)
    assert sp.expand((k-s-w)**2-4*(p+s*w)
                     - (w*w-2*(k+s)*w+(k-s)**2-4*p)) == 0
    assert sp.simplify(((k+s)**2-4*(k*s+p))-((k-s)**2-4*p)) == 0
    print('PASS symbolic: angular derivatives, pocket addition, threshold polynomial')


def branch(radius, low, a, b):
    """Exact sign(C-H), with the sign gate checked BEFORE squaring."""
    A, c, d, k = 1/Q(radius), 1/Q(a), 1/Q(b), 1/Q(low)
    gate = k-A-c-d
    if gate <= 0:
        return 1
    difference = 4*(A*c+A*d+c*d)-gate*gate
    return (difference > 0)-(difference < 0)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def sub(x, y):
    return x[0]-y[1], x[1]-y[0]


@lru_cache(None)
def angle_interval(radius, a, b):
    radius, a, b = Q(radius), Q(a), Q(b)
    q = a*b/((radius+a)*(radius+b))
    assert 0 < q < 1
    scale = 10**40
    root = isqrt(q.numerator*scale*scale//q.denominator)
    lower, upper = Q(root, scale), Q(root+1, scale)
    assert lower*lower <= q <= upper*upper
    total, power, coeff = Q(0), Q(1), Q(1)
    for n in range(300):
        total += coeff*power
        power *= q
        coeff *= Q((2*n+1)**2, 2*(n+1)*(2*n+3))
    # asin(sqrt(q)) = sqrt(q) sum c_n q**n; 0<c_n<=1.
    result = 2*lower*total, 2*upper*(total+power/(1-q))
    assert result[1]-result[0] < Q(1, 10**20)
    return result


def cell_interval(radius, low, a, b):
    chain = add(angle_interval(radius, low, a), angle_interval(radius, low, b))
    chord = angle_interval(radius, a, b)
    return max(chain[0], chord[0]), max(chain[1], chord[1])


def score_interval(radius, p):
    total = Q(0), Q(0)
    for i in range(1, len(p)+1):
        total = add(total, cell_interval(radius, i, p[i-2], p[i-1]))
    return total


def exact_witnesses():
    before, after = (4, 5, 6), (5, 4, 6)
    for radius, lowbound, highbound, expected in [
            (1, Q(-17413, 10**6), Q(-17412, 10**6), (1, 1)),
            (100, Q(2980, 10**6), Q(2981, 10**6), (-1, 1))]:
        for b in (4, 5):
            assert (branch(radius, 1, 6, b), branch(radius, 3, 6, b)) == expected
        interval = sub(score_interval(radius, after), score_interval(radius, before))
        assert lowbound < interval[0] <= interval[1] < highbound
        print(f'PASS exact swap m=3 R={radius}: {lowbound} < Delta < {highbound}')

    for radius, expected in [(1, (1, 1)), (100, (-1, 1))]:
        for b in (5, 6):
            assert (branch(radius, 1, 4, b), branch(radius, 2, 4, b)) == expected
        increment2 = sub(cell_interval(radius, 2, 4, 6), cell_interval(radius, 2, 4, 5))
        increment1 = sub(cell_interval(radius, 1, 4, 6), cell_interval(radius, 1, 4, 5))
        cross = sub(increment2, increment1)
        assert cross[0] > 0 if radius == 1 else cross[1] < 0
    print('PASS exact low/high cross difference: positive at R=1, negative at R=100')

    shifts = [tuple(range(5+s, 9))+tuple(range(5, 5+s)) for s in range(4)]
    for radius, p, margin in [(1, (8, 6, 5, 7), Q(8, 1000)),
                              (10, (6, 8, 7, 5), Q(7, 1000))]:
        candidate = score_interval(radius, p)
        for shift in shifts:
            assert sub(score_interval(radius, shift), candidate)[0] > margin
        print(f'PASS exact m=4 R={radius}: {p} beats all four shifts by > {margin}')
    assert branch(1, Q(2, 15), 1, Q(2, 3)) == 0
    # The no-finite-crossing boundary k=(sqrt(A)+sqrt(c))**2 is rational here.
    assert Q(1) == (Q(1, 2)+Q(1, 2))**2
    assert all(branch(4, 1, 4, b) == 1 for b in (2, 5, 100))
    print('PASS exact branch equality and infinite-threshold boundary probes')


mp.mp.dps = 70
GUARD = mp.mpf('1e-60')


@lru_cache(None)
def asin_angle(radius, a, b):
    radius, a, b = mp.mpf(radius), mp.mpf(a), mp.mpf(b)
    return 2*mp.asin(mp.sqrt(a*b/((radius+a)*(radius+b))))


@lru_cache(None)
def atan_angle(radius, a, b):
    radius, a, b = mp.mpf(radius), mp.mpf(a), mp.mpf(b)
    return 2*mp.atan2(mp.sqrt(a*b), mp.sqrt(radius*(radius+a+b)))


@lru_cache(None)
def threshold(radius, low, a):
    A, c, k = 1/mp.mpf(radius), 1/mp.mpf(a), 1/mp.mpf(low)
    if k <= (mp.sqrt(A)+mp.sqrt(c))**2:
        return mp.inf
    return 1/(k+A+c-2*mp.sqrt(k*(A+c)+A*c))


@lru_cache(None)
def increment(radius, low, a, x, y):
    B = threshold(radius, low, a)
    q = min(mp.mpf(y), max(mp.mpf(x), B))
    value = (asin_angle(radius, low, q)-asin_angle(radius, low, x)
             + asin_angle(radius, a, y)-asin_angle(radius, a, q))
    kind = 'C' if q == y else 'H' if q == x else 'M'
    return value, q, kind


def direct_cells(radius, p):
    return [max(atan_angle(radius, i, p[i-2])+atan_angle(radius, i, p[i-1]),
                atan_angle(radius, p[i-2], p[i-1])) for i in range(1, len(p)+1)]


def numeric_swaps():
    orders = swaps = conditions = 0
    max_error = mp.mpf(0)
    branch_pairs = set()
    for m in range(2, 7):
        candidates = []
        for p in permutations(range(m+1, 2*m+1)):
            orders += 1
            structure = (all(p[j] > p[j+1] for j in range(m-2))
                         and p[-2] < p[-1] < p[0]) if m >= 3 else True
            if structure:
                candidates.append(p)
            for radius in map(mp.mpf, ('0.1', '1', '2', '5', '10', '100')):
                before = direct_cells(radius, p)
                has_improvement = False
                for j in range(m):
                    k = (j+1) % m
                    changed = list(p)
                    changed[j], changed[k] = changed[k], changed[j]
                    after = direct_cells(radius, changed)
                    actual = mp.fsum(a-b for a, b in zip(after, before))
                    has_improvement |= actual < -GUARD
                    swaps += 1
                    if m == 2:
                        assert after == before
                        continue
                    exterior = {j, (j+2) % m}
                    assert all(a == b for i, (a, b) in enumerate(zip(after, before))
                               if i not in exterior)
                    assert all(after[i] != before[i] for i in exterior)
                    x, y = sorted((p[j], p[k]))
                    l, r, u, v = j+1, (j+2) % m+1, p[j-1], p[(j+2) % m]
                    left, ql, kl = increment(radius, l, u, x, y)
                    right, qr, kr = increment(radius, r, v, x, y)
                    branch_pairs.add(kl+kr)
                    predicted = left-right
                    oriented = actual if p[j] < p[k] else -actual
                    error = abs(predicted-oriented)
                    assert error < GUARD, (m, p, radius, j, error)
                    max_error = max(max_error, error)
                    if l <= r and u <= v and ql >= qr:
                        assert oriented <= GUARD
                        conditions += 1
                    if l >= r and u >= v and ql <= qr:
                        assert oriented >= -GUARD
                        conditions += 1
                if radius <= 1 and not structure:
                    assert has_improvement, (m, p, radius)
        assert len(candidates) == (2 if m == 2 else m-2)
        print(f'PASS numeric m={m}: all permutations/seams and small-R exclusion')
    assert orders == 872 and swaps == 30228
    print(f'PASS numeric: orders={orders}, swaps={swaps}, conditional_probes={conditions}')
    print('integer_swap_branch_pairs='+','.join(sorted(branch_pairs)))
    print('max_abs_local_vs_full_atan_error='+mp.nstr(max_error, 8))


def positive_real_branch_probes():
    # Independent inverse construction: choose the crossing b0 and derive
    # the inserted low from the exact pocket formula. Not integer permutations.
    radius, x, y = mp.mpf(10), mp.mpf(4), mp.mpf(5)
    cases = {}
    worst = mp.mpf(0)
    for a in (mp.mpf(6), mp.mpf(7)):
        for b0 in (mp.mpf(2), mp.mpf('4.5'), mp.mpf(10)):
            A, c, d = 1/radius, 1/a, 1/b0
            low = 1/(A+c+d+2*mp.sqrt(A*c+A*d+c*d))
            assert 0 < low < min(a, x)
            value, q, kind = increment(radius, low, a, x, y)
            def direct(b):
                return max(atan_angle(radius, low, a)+atan_angle(radius, low, b),
                           atan_angle(radius, a, b))
            error = abs(value-(direct(y)-direct(x)))
            assert error < GUARD
            worst = max(worst, error)
            assert abs(threshold(radius, low, a)-b0) < GUARD
            cases[int(a), kind] = value, direct(y)-direct(x)
    products = set()
    for left in 'CHM':
        for right in 'CHM':
            li, ld = cases[6, left]
            ri, rd = cases[7, right]
            assert abs((li-ri)-(ld-rd)) < GUARD
            products.add(left+right)
    assert len(products) == 9
    # Exact finite crossing B=2/3; exercise q=x, q=y and interior q.
    low, a, R = mp.mpf(2)/15, mp.mpf(1), mp.mpf(1)
    for x0, y0 in [(mp.mpf(2)/3, mp.mpf(1)), (mp.mpf(1)/2, mp.mpf(2)/3),
                   (mp.mpf(1)/2, mp.mpf(1))]:
        value, _, _ = increment(R, low, a, x0, y0)
        def f(b):
            return max(atan_angle(R, low, a)+atan_angle(R, low, b), atan_angle(R, a, b))
        assert abs(value-(f(y0)-f(x0))) < GUARD
    assert threshold(4, 1, 4) == mp.inf
    print('PASS positive-real cell probes: all nine branch pairs, finite endpoints, infinite equality')
    print('max_abs_positive_real_increment_error='+mp.nstr(worst, 8))


if __name__ == '__main__':
    symbolic_checks()
    exact_witnesses()
    numeric_swaps()
    positive_real_branch_probes()
    print('Exact local inequalities plus finite 70-digit corroboration; no global certificate.')
