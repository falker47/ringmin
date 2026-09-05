"""Bounded independent audit of ONE fixed second-block recovery.

Run with python -S. Integers/Fraction only; no files written, no imports
of production, verify.py, old checkers or numerical minimizers. Bracket
boxes overcover the SAME exact implicit parameters, not new parameters
chosen for optimization. The research note, not this scan, proves all m.
"""

from fractions import Fraction as Q


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1+AL)*XL, (1+AH)*XH
U0, WIDTH = Q(1, 3), Q(1, 100)
V0 = U0+WIDTH
MAX_M = 1201
MOMENT_M = (200, 201, 399, 400, 401, 599, 600, 601, 1199, 1200, 1201)


def ceil_q(value):
    return -((-value)//1)


def floor_boxes(m):
    """Closed rational enclosures of every possible exact floor cell.

    Strict upper brackets use ceil-1, including exact rational ties.
    The alpha/lambda correlation can only remove cases from this list.
    """
    for s in range((AL*m)//1, ceil_q(AH*m)):
        aa = max(AL, Q(s, m)), min(AH, Q(s+1, m))
        for k in range((LL*m/2)//1, ceil_q(LH*m/2)):
            ll = max(LL, Q(2*k, m)), min(LH, Q(2*k+2, m))
            if aa[0] < aa[1] and ll[0] < ll[1]:
                yield s, 2*k, aa, ll


def list_order(m, s, q):
    """Independent constructor: rotate a list, reverse two even-slot lists."""
    if any(type(x) is not int for x in (m, s, q)) or m < 2:
        raise ValueError("m>=2, s and q must be integers")
    p, d = 2*(m//6), 2*(m//200)
    if not (0 <= s < m and 0 <= q <= p and q % 2 == 0
            and s+max(q, p+d) < m):
        raise ValueError("require disjoint even blocks before the high wrap")
    highs = list(range(m+1, 2*m+1))
    order = highs[s:]+highs[:s]
    order[1:q:2] = order[1:q:2][::-1]
    order[p+1:p+d:2] = order[p+1:p+d:2][::-1]
    return order


def audit_order(m, s, q, order, predecessors=None):
    """Check occurrences and ALL actual cyclic-list cells against the note."""
    p, d, r = 2*(m//6), 2*(m//200), m-s
    e = p+d
    ranks = []
    for i in range(1, m+1):
        if i <= q and i % 2 == 0:
            ranks.append(q+2-i)
        elif p < i <= e and i % 2 == 0:
            ranks.append(2*p+d+2-i)
        else:
            ranks.append(i)
    assert sorted(ranks) == list(range(1, m+1))
    assert [ranks[j-1] for j in ranks] == list(range(1, m+1))
    assert sorted(order) == list(range(m+1, 2*m+1))
    assert order == [m+1+((j+s-1) % m) for j in ranks]
    if predecessors is None:
        predecessors = order[-1:]+order[:-1]
    assert sorted(predecessors) == sorted(order)

    exc = {1, r, r+1}
    if q:
        exc.add(q+1)
    if d:
        exc.update((p+1, e+1))
    exc &= set(range(1, m+1))
    interior_1 = set(range(2, q+1)) if q else set()
    interior_2 = set(range(p+2, e+1)) if d else set()
    assert not (interior_1 & interior_2 or exc & (interior_1 | interior_2))
    ordinary = set(range(1, m+1))-exc-interior_1-interior_2
    assert len(exc) == (2 if m <= 6 else 3 if m <= 9 else 4 if m < 200 else 6)
    assert len(interior_1) == max(0, q-1)
    assert len(interior_2) == max(0, d-1)
    for cells, length in ((interior_1, q), (interior_2, d)):
        assert sum(i % 2 == 0 for i in cells) == length//2
        assert sum(i % 2 == 1 for i in cells) == max(0, length//2-1)
    ordinary_count = (m-2 if m <= 6 else m-q-2 if m <= 9
                      else m-q-3 if m < 200 else m-q-d-4)
    assert len(ordinary) == ordinary_count
    assert len(ordinary)+len(exc)+len(interior_1)+len(interior_2) == m

    seams = {1: (m+s, m+s+1) if s else (2*m, m+1),
             r: (2*m-1, 2*m)}
    if s:
        seams[r+1] = (2*m, m+1)
    if q:
        seams[q+1] = (m+s+2, m+s+q+1)
    if d:
        assert p >= q+2 and r >= e+2
        seams[p+1] = (m+s+p, m+s+p+1)
        seams[e+1] = (m+s+p+2, m+s+e+1)
    assert set(seams) == exc

    # Direct cyclic-list scorer: no predecessor obtained from J's formula.
    for i, (prev, curr) in enumerate(zip(predecessors, order), 1):
        if i in exc:
            expected = seams[i]
        elif i in interior_1 or i in interior_2:
            c = q if i in interior_1 else 2*p+d
            expected = ((m+s+i-1, m+s+c+2-i) if i % 2 == 0
                        else (m+s+c+3-i, m+s+i))
        else:
            expected = ((m+s+i-1, m+s+i) if i < r
                        else (s+i-1, s+i))
            assert i < r or i > r+1
        assert (prev, curr) == expected, (m, s, q, i, expected, prev, curr)

    # Baseline preservation, checked from a separately rotated list.
    highs = list(range(m+1, 2*m+1))
    baseline = highs[s:]+highs[:s]
    baseline[1:q:2] = baseline[1:q:2][::-1]
    baseline_prev = baseline[-1:]+baseline[:-1]
    for i, pair in enumerate(zip(predecessors, order), 1):
        if not (d and p+2 <= i <= e+1):
            assert pair == (baseline_prev[i-1], baseline[i-1])
    if d in (0, 2):
        assert baseline == order
    else:
        assert baseline != order
    return len(ordinary)+len(interior_1)+len(interior_2)


def audit_box(m, s, q, aa, ll):
    """Interval-coordinate gates apply to every parameter in the floor box."""
    p, d, r = 2*(m//6), 2*(m//200), m-s
    assert 0 <= s < m and 0 <= q <= p and s+p+d < m
    assert Q(s, m) <= aa[0] <= aa[1] <= Q(s+1, m)
    assert Q(q, m) <= ll[0] <= ll[1] <= Q(q+2, m)
    assert (q == 0) == (m <= 6)
    assert (q == 2) == (7 <= m <= 12)
    assert (s == 0) == (m <= 9)
    assert (d == 0) == (m < 200)
    assert (d == 2) == (200 <= m <= 399)
    if q:
        assert r >= q+2
    if m < 200:
        return
    assert ll[1] < Q(p, m) <= U0 < Q(p+d, m) <= V0
    assert 1+aa[1]+V0+(U0-Q(p, m)) < 2
    # Scaled errors are affine in alpha/lambda. Checking the corners is
    # an exact box bound, including hypothetical exact floor ties.
    for alpha in aa:
        da = s-m*alpha
        assert -1 <= da <= 0 and abs(da-1) <= 2
        for lam in ll:
            for offset in (2, 3):
                assert abs(da+q-m*lam+offset) <= 3
                assert abs(da+2*p+d-m*(U0+V0)+offset) <= 5


# A separate outward interval polynomial integrator for continuous tests.
# An interval is a pair of exact Fractions; dependencies only widen it.
def point(x):
    return Q(x), Q(x)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def power(x, n):
    answer = point(1)
    for _ in range(n):
        answer = mul(answer, x)
    return answer


def poly_mul(a, b):
    result = [point(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] = add(result[i+j], mul(x, y))
    return result


def pullback(terms, high_x, high_y):
    result = []
    for (a, b, c), coefficient in terms.items():
        term = [point(coefficient)]
        for poly, degree in (([point(0), point(1)], a),
                             (high_x, b), (high_y, c)):
            for _ in range(degree):
                term = poly_mul(term, poly)
        while len(result) < len(term):
            result.append(point(0))
        for i, value in enumerate(term):
            result[i] = add(result[i], value)
    return result


def integral(poly, lo, hi):
    result = point(0)
    for k, coefficient in enumerate(poly, 1):
        width = add(power(hi, k), neg(power(lo, k)))
        result = add(result, mul(coefficient, mul(width, point(Q(1, k)))))
    return result


def continuum_moment(terms, aa, ll):
    A, wrap = add(point(1), aa), add(point(1), neg(aa))
    diag = [A, point(1)]
    wrapped = [aa, point(1)]
    prefix = [add(A, ll), point(-1)]
    second = [add(A, point(U0+V0)), point(-1)]
    intervals = (
        (point(0), ll, diag, prefix, Q(1, 2)),
        (point(0), ll, prefix, diag, Q(1, 2)),
        (ll, point(U0), diag, diag, Q(1)),
        (point(U0), point(V0), diag, second, Q(1, 2)),
        (point(U0), point(V0), second, diag, Q(1, 2)),
        (point(V0), wrap, diag, diag, Q(1)),
        (wrap, point(1), wrapped, wrapped, Q(1)),
    )
    result = point(0)
    for lo, hi, xx, yy, weight in intervals:
        value = integral(pullback(terms, xx, yy), lo, hi)
        result = add(result, mul(point(weight), value))
    return result


def moment_checks(m, order, aa, ll):
    monomials = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
                 (1, 1, 0), (1, 0, 1), (1, 1, 1), (1, 2, 0), (1, 0, 2))
    tests = [{term: Q(1)} for term in monomials]
    tests += [{(0, 2, 0): Q(1), (0, 1, 1): Q(-2), (0, 0, 2): Q(1)},
              {(1, 1, 0): Q(1), (1, 0, 1): Q(-1)}]
    triples = tuple(zip(range(1, m+1), order[-1:]+order[:-1], order))
    for index, terms in enumerate(tests):
        enclosure = continuum_moment(terms, aa, ll)
        empirical = sum((coefficient*Q(
            sum(i**a*x**b*y**c for i, x, y in triples), m**(a+b+c+1))
            for (a, b, c), coefficient in terms.items()), Q(0))
        maximum = sum(abs(cc)*2**(b+c) for (a, b, c), cc in terms.items())
        lipschitz = sum(abs(cc)*(a+Q(b+c, 2))*2**(b+c)
                        for (a, b, c), cc in terms.items())
        upper_error = max(abs(empirical-enclosure[0]), abs(empirical-enclosure[1]))
        assert upper_error <= (7*lipschitz+32*maximum)/m
        known = {0: Q(1), 1: Q(1, 2), 2: Q(3, 2), 3: Q(3, 2), 10: Q(0)}
        if index in known:
            assert enclosure[0] <= known[index] <= enclosure[1]
        if index == 9:
            # Separate reflection substitution: integral (x-y)^2 equals
            # lambda^3/3 + epsilon^3/3; the second summand must be present.
            exact_span = (ll[0]**3/3+WIDTH**3/3, ll[1]**3/3+WIDTH**3/3)
            assert enclosure[0] <= exact_span[0] <= exact_span[1] <= enclosure[1]
    return len(tests)


def failure_checks():
    invalid = ((1, 0, 0), (600, -1, 190), (600, 65, 191),
               (600, 65, 202), (600, 599, 190), (True, 0, 0))
    for args in invalid:
        try:
            list_order(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid construction input accepted")
    m, s, q = 600, 65, 190
    order = list_order(m, s, q)
    duplicate = order.copy()
    duplicate[201] = duplicate[200]
    omitted = order.copy()
    omitted[201:206:2] = omitted[201:206:2][::-1]
    all_reversed = omitted.copy()
    all_reversed[200:206] = all_reversed[200:206][::-1]
    wrong_predecessor = order.copy()  # same high marginal, wrong incidence
    variants = ((duplicate, None), (omitted, None), (all_reversed, None),
                (order, wrong_predecessor))
    for bad_order, bad_prev in variants:
        try:
            audit_order(m, s, q, bad_order, bad_prev)
        except AssertionError:
            pass
        else:
            raise AssertionError("faulty occurrence/parity/predecessor variant accepted")
    print("PASS negative gates: 6 invalid inputs and 4 faulty occurrence/parity/predecessor variants rejected")


def main():
    assert U0-LH > Q(1, 100)
    assert 1-AH-V0 > Q(1, 2) and 1-AH-LH > Q(1, 2)
    assert 6*LH < 2 < 7*LL and 12*LH < 4 < 13*LL
    assert 9*AH < 1 < 10*AL
    assert Q(2, 1) == ceil_q(Q(2)) and ceil_q(Q(5, 2)) == 3
    for degree in range(9):
        poly = [point(0)]*degree+[point(1)]
        assert integral(poly, point(0), point(1)) == point(Q(1, degree+1))
    print("PASS exact fixed gates: block separation, wrap separation, all small-m thresholds; 9 exact polynomial integration oracles")
    cases = cells = compared = moments = alpha_ties = lambda_ties = 0
    ambiguous_sizes = 0
    residues = [0]*600
    for m in range(2, MAX_M+1):
        residues[m % 600] += 1
        boxes = list(floor_boxes(m))
        assert boxes
        ambiguous_sizes += len(boxes) > 1
        for s, q, aa, ll in boxes:
            order = list_order(m, s, q)
            good_cells = audit_order(m, s, q, order)
            audit_box(m, s, q, aa, ll)
            cells += m
            compared += good_cells if m >= 200 else 0
            alpha_ties += aa[0] == Q(s, m)
            lambda_ties += ll[0] == Q(q, m)
            if m in MOMENT_M:
                moments += moment_checks(m, order, aa, ll)
            cases += 1
    assert all(count == 2 for count in residues)
    assert alpha_ties and lambda_ties and ambiguous_sizes
    boxes_600 = list(floor_boxes(600))
    assert len(boxes_600) == 1 and boxes_600[0][:2] == (65, 190)
    order_600 = list_order(600, 65, 190)
    assert order_600[200:206] == [866, 871, 868, 869, 870, 867]
    print(f"PASS bounded floor cover: {cases} prescribed orders, m=2..{MAX_M}; {ambiguous_sizes} sizes with multiple bracket-compatible floor pairs")
    print(f"PASS independent lists: {cells} cyclic cells; exact occurrences, involution, both orientations, all junction/wrap pairs and complete counts")
    print(f"PASS coordinate enclosures: {compared} nonexceptional cells at m>=200 covered by <=5/m at the exact implicit parameters")
    print(f"PASS floor boundaries: all 600 residues twice; {alpha_ties} alpha and {lambda_ties} lambda lower-floor ties; empty/length-2 blocks; exact m=600 witness")
    print(f"PASS independent interval moments: {moments} tests at {len(MOMENT_M)} fixed sizes; nonsymmetric tests, second-block moment and (7L+32M)/m bound")
    failure_checks()
    print("NOTE: exact bounded bookkeeping checks; analytic proof supplies all-m continuous-test recovery. No parameter optimization, root transfer or geometric bound.")


if __name__ == "__main__":
    main()
