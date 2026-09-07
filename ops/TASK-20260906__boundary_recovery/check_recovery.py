"""Bounded exact audit of the adjacent-block boundary recovery.

Run with python -S. Integer/Fraction arithmetic only; no file writes,
production, verifier, old checker or numerical-root imports. Strict
imported brackets overcover floors of the SAME exact implicit constants.
This program never chooses substitute parameters or certifies the minima.
The research proof, not a finite scan, establishes the all-m theorem.
"""

from fractions import Fraction as Q


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1+AL)*XL, (1+AH)*XH
EL, EH = Q(43, 1000), Q(11, 250)
MAX_M = 512


def ceil_q(value):
    return -((-value)//1)


def floor_cells(lo, hi, m, step):
    """All floors compatible with lo<parameter<hi, then closed boxes.

    ceil(hi*m/step)-1 handles strict upper endpoints even at exact
    integer ties. Clipping and closing can only add limiting cases.
    """
    for k in range((lo*m/step)//1, ceil_q(hi*m/step)):
        lower = max(lo, Q(step*k, m))
        upper = min(hi, Q(step*(k+1), m))
        if lower < upper:
            yield step*k, (lower, upper)


def list_order(m, s, q, d):
    """Independent constructor: rotate highs and reverse even-slot lists."""
    if any(type(value) is not int for value in (m, s, q, d)) or m < 2:
        raise ValueError('require integer m>=2 and integer s, q, d')
    if not (0 <= s < m and q >= 0 and d >= 0 and q % 2 == d % 2 == 0
            and (not d or q) and m-s >= q+d+2):
        raise ValueError('require adjacent even blocks before the high wrap')
    highs = list(range(m+1, 2*m+1))
    order = highs[s:]+highs[:s]
    order[1:q:2] = order[1:q:2][::-1]
    order[q+1:q+d:2] = order[q+1:q+d:2][::-1]
    return order


def audit_order(m, s, q, d, order, predecessors=None):
    """Compare the note's formulas to every actual cyclic-list pair."""
    e, r = q+d, m-s
    ranks = []
    for i in range(1, m+1):
        if i <= q and i % 2 == 0:
            ranks.append(q+2-i)
        elif q < i <= e and i % 2 == 0:
            ranks.append(2*q+d+2-i)
        else:
            ranks.append(i)
    assert sorted(ranks) == list(range(1, m+1))
    assert [ranks[j-1] for j in ranks] == list(range(1, m+1))
    assert sorted(order) == list(range(m+1, 2*m+1))
    assert order == [m+1+((j+s-1) % m) for j in ranks]
    for a, length in ((0, q), (q, d)):
        assert sorted(ranks[a:a+length]) == list(range(a+1, a+length+1))
        assert all(ranks[i-1] == i for i in range(a+1, a+length, 2))
        fixed_even = sum(ranks[i-1] == i for i in range(a+2, a+length+1, 2))
        assert fixed_even == int(length % 4 == 2)
        if length in (0, 2):
            assert ranks[a:a+length] == list(range(a+1, a+length+1))
    if predecessors is None:
        predecessors = order[-1:]+order[:-1]
    assert len(predecessors) == m and sorted(predecessors) == sorted(order)

    exc = {1, r, r+1}
    if q:
        exc.add(q+1)
    if d:
        exc.add(e+1)
    exc &= set(range(1, m+1))
    first = set(range(2, q+1)) if q else set()
    second = set(range(q+2, e+1)) if d else set()
    assert not (first & second or exc & (first | second))
    ordinary = set(range(1, m+1))-exc-first-second
    expected_exc = 2 if m <= 6 else 3 if m <= 9 else 4 if not d else 5
    assert len(exc) == expected_exc
    assert len(first) == max(0, q-1) and len(second) == max(0, d-1)
    assert len(ordinary) == m-len(first)-len(second)-expected_exc
    for cells, length in ((first, q), (second, d)):
        assert sum(i % 2 == 0 for i in cells) == length//2
        assert sum(i % 2 == 1 for i in cells) == max(0, length//2-1)

    seams = {1: (m+s, m+s+1) if s else (2*m, m+1),
             r: (2*m-1, 2*m)}
    if s:
        seams[r+1] = (2*m, m+1)
    if q:
        seams[q+1] = (m+s+2, m+s+q+1)
    if d:
        assert q > 0 and s > 0
        seams[e+1] = (m+s+q+2, m+s+e+1)
        assert q+1 in exc and q+1 not in second
    assert set(seams) == exc

    # Endpoints suffice for the affine max-norm panel bounds. All
    # coordinates are scaled by m, so these comparisons are integers.
    panels_checked = 0
    for i, (prev, curr) in enumerate(zip(predecessors, order), 1):
        if i in exc:
            assert (prev, curr) == seams[i], (m, s, q, d, i)
            continue
        if i in first or i in second:
            c = q if i in first else 2*q+d
            if i % 2 == 0:
                expected = (m+s+i-1, m+s+c+2-i)
                times, bound = (i-2, i), 2
                triples = [(t, m+s+t, m+s+c-t) for t in times]
            else:
                expected = (m+s+c+3-i, m+s+i)
                times, bound = (i-1, i+1), 4
                triples = [(t, m+s+c-t, m+s+t) for t in times]
        else:
            assert i in ordinary and (i < r or i > r+1)
            offset = m+s if i < r else s
            expected = (offset+i-1, offset+i)
            bound = 1
            triples = [(t, offset+t, offset+t) for t in (i-1, i)]
        assert (prev, curr) == expected, (m, s, q, d, i)
        for triple in triples:
            assert 0 <= triple[0] <= m
            assert all(m <= value <= 2*m for value in triple[1:])
            assert max(abs(a-b) for a, b in zip((i, prev, curr), triple)) <= bound
        panels_checked += 1
    assert panels_checked == m-len(exc)

    # Separate block orientations each allocate one half of length/m;
    # complementary unit panels supply the remaining mass exactly.
    assert 2*(q//2)+2*(d//2)+(m-e) == m
    return panels_checked


def audit_box(m, s, q, d, aa, ll, ee):
    """Check residual and domain bounds for the entire closed floor box."""
    assert 2*(s+q+d) < m and m-s >= q+d+2
    assert (q == 0) == (m <= 6)
    assert (s == 0) == (m <= 9)
    assert d <= q
    if m <= 45:
        assert d == 0
    if m == 46:
        assert d in (0, 2)
    if m >= 47:
        assert d >= 2
    # The upper floor-box boundary is included only as an overcover;
    # residual equality there is harmless for these non-strict bounds.
    for alpha in aa:
        da = m*alpha-s
        assert 0 <= da <= 1
        for lam in ll:
            dl = m*lam-q
            assert 0 <= dl <= 2
            for epsilon in ee:
                de = m*epsilon-d
                assert 0 <= de <= 2
                assert alpha+lam+epsilon < Q(1, 2)
                assert da+dl <= 3
                assert da+2*dl+de <= 7
                # m times the sum of the THREE bad-interval lengths.
                assert dl+(dl+de)+da <= 7


def must_reject(call, exception):
    try:
        call()
    except exception:
        return
    raise AssertionError('mutation or malformed input was not rejected')


def main():
    assert 0 < AL < AH and 0 < EL < EH < LL < LH
    slack = Q(1, 2)-AH-LH-EH
    assert slack > 0
    assert 6*LH < 2 < 7*LL
    assert 9*AH < 1 < 10*AL
    assert 45*EH < 2 < 47*EL
    # Exact tie behavior of the floor-box enumerator, independent of
    # the particular irrationality or rationality of the input minima.
    assert [n for n, _ in floor_cells(Q(1, 4), Q(1, 2), 8, 2)] == [2]
    assert [n for n, _ in floor_cells(Q(1, 8), Q(3, 8), 8, 2)] == [0, 2]

    cases = cells = panels = 0
    m46_widths = set()
    for m in range(2, MAX_M+1):
        per_m = 0
        for s, aa in floor_cells(AL, AH, m, 1):
            for q, ll in floor_cells(LL, LH, m, 2):
                for d, ee in floor_cells(EL, EH, m, 2):
                    audit_box(m, s, q, d, aa, ll, ee)
                    panels += audit_order(m, s, q, d, list_order(m, s, q, d))
                    cases += 1
                    cells += m
                    per_m += 1
                    if m == 46:
                        m46_widths.add(d)
        assert per_m > 0
    assert m46_widths == {0, 2}

    sample_floors = [(s, q, d)
                     for s, _ in floor_cells(AL, AH, 100, 1)
                     for q, _ in floor_cells(LL, LH, 100, 2)
                     for d, _ in floor_cells(EL, EH, 100, 2)]
    assert sample_floors == [(10, 30, 4)]
    m, s, q, d = 100, 10, 30, 4
    order = list_order(m, s, q, d)
    assert order[30:34] == [141, 144, 143, 142]
    assert (order[29], order[30]) == (112, 141)
    assert (order[33], order[34]) == (142, 145)
    assert (order[89], order[90]) == (200, 101)
    assert (order[-1], order[0]) == (110, 111)

    duplicate = order.copy()
    duplicate[0] = duplicate[1]
    must_reject(lambda: audit_order(m, s, q, d, duplicate), AssertionError)
    highs = list(range(m+1, 2*m+1))
    union = highs[s:]+highs[:s]
    union[1:q+d:2] = union[1:q+d:2][::-1]
    must_reject(lambda: audit_order(m, s, q, d, union), AssertionError)
    false_seam = order[-1:]+order[:-1]
    # Swap predecessors, preserving their entire marginal multiset.
    # The shared entry now has the old isolated-entry value m+s+q.
    j = false_seam.index(m+s+q)
    false_seam[q], false_seam[j] = false_seam[j], false_seam[q]
    must_reject(lambda: audit_order(m, s, q, d, order, false_seam), AssertionError)
    # At m=2 retain the predecessor marginal but destroy the cyclic seam.
    tiny = list_order(2, 0, 0, 0)
    must_reject(lambda: audit_order(2, 0, 0, 0, tiny, tiny), AssertionError)

    invalid = [(1, 0, 0, 0), (True, 0, 0, 0), (10, -1, 2, 0),
               (10, 1, 3, 0), (10, 1, 2, 1), (10, 1, 0, 2),
               (10, 1, 6, 2), (10, 1, -2, 0)]
    for args in invalid:
        must_reject(lambda args=args: list_order(*args), ValueError)

    print('EXACT half-wrap slack =', slack, '> 0')
    print('PASS rational domain and small-case gates; strict-upper floor ties')
    print(f'PASS m=2..{MAX_M}: {cases} floor triples; {cells} actual cyclic cells')
    print(f'PASS {panels} nonexception panel bounds; all exception pairs and counts')
    print('PASS all closed floor-box corners: coordinate and boundary-mass constants')
    print('PASS m=46 both d=0,2; m=100 example; 4 rejected mutations; 8 invalid inputs')
    print('NOTE: exact finite audit only; input minima and all-m weak proof are separate; no numerical diagnostics or radius transfer')


if __name__ == '__main__':
    main()
