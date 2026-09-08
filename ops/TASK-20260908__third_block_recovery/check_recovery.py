"""Bounded exact audit of mu_3 finite recovery; run with python -S.

Integer/Fraction arithmetic only. No file writes or production, verifier,
prior-checker or root imports. Bracket-compatible floors are an overcover,
never replacement parameters. The proof supplies the all-m theorem.
"""

from fractions import Fraction as Q
from itertools import product


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1+AL)*XL, (1+AH)*XH
EL, EH, DELTA = Q(43, 1000), Q(11, 250), Q(1, 1000)
SPECIAL = (1998, 1999, 2000, 2001, 2002, 3998, 3999, 4000, 4001,
           5999, 6000, 6001, 8000)


def ceil_q(value):
    return -((-value)//1)


def floor_cells(lo, hi, m, step):
    """All floors for lo<parameter<hi, with closed clipped residual boxes."""
    for k in range((lo*m/step)//1, ceil_q(hi*m/step)):
        lower = max(lo, Q(step*k, m))
        upper = min(hi, Q(step*(k+1), m))
        if lower < upper:
            yield step*k, (lower, upper)


def list_order(m, s, q, d, f):
    """Construct from integer gates by rotation and separate slice reversals."""
    if any(type(x) is not int for x in (m, s, q, d, f)) or m < 1:
        raise ValueError('require integer m>=1 and integer floor ranks')
    if not (0 <= s < m and 0 <= f <= d <= q
            and all(x % 2 == 0 for x in (q, d, f))):
        raise ValueError('require nested nonnegative even lengths and valid shift')
    if m == 1:
        if (s, q, d, f) != (0, 0, 0, 0):
            raise ValueError('m=1 has no blocks')
        return [2]
    if m-s < q+d+f+2:
        raise ValueError('require exits strictly before the high wrap')
    highs = list(range(m+1, 2*m+1))
    order = highs[s:]+highs[:s]
    for a, length in ((0, q), (q, d), (q+d, f)):
        order[a+1:a+length:2] = order[a+1:a+length:2][::-1]
    return order


def audit_order(m, s, q, d, f, order, predecessors=None, exceptions=None):
    """Audit formula, all pairs and panels against the independently built list."""
    e, z, r = q+d, q+d+f, m-s
    blocks = ((0, q), (q, d), (e, f))
    ranks = []
    for i in range(1, m+1):
        if i <= q and i % 2 == 0:
            ranks.append(q+2-i)
        elif q < i <= e and i % 2 == 0:
            ranks.append(2*q+d+2-i)
        elif e < i <= z and i % 2 == 0:
            ranks.append(2*e+f+2-i)
        else:
            ranks.append(i)
    assert sorted(ranks) == list(range(1, m+1))
    assert [ranks[j-1] for j in ranks] == list(range(1, m+1))
    assert sorted(order) == list(range(m+1, 2*m+1))
    assert order == [m+1+((j+s-1) % m) for j in ranks]
    if predecessors is None:
        predecessors = order[-1:]+order[:-1]
    assert len(predecessors) == m and sorted(predecessors) == sorted(order)
    if m == 1:
        assert (s, q, d, f, order, predecessors) == (0, 0, 0, 0, [2], [2])
        return 0

    for a, length in blocks:
        assert sorted(ranks[a:a+length]) == list(range(a+1, a+length+1))
        assert all(ranks[i-1] == i for i in range(a+1, a+length, 2))
        fixed_even = sum(ranks[i-1] == i for i in range(a+2, a+length+1, 2))
        assert fixed_even == int(length % 4 == 2)
        if length in (0, 2):
            assert ranks[a:a+length] == list(range(a+1, a+length+1))

    designated = {1, r, r+1}
    designated.update(a+length+1 for a, length in blocks if length)
    designated &= set(range(1, m+1))
    if exceptions is None:
        exceptions = sorted(designated)
    assert len(exceptions) == len(set(exceptions)), 'duplicated seam mass'
    exc = set(exceptions)
    assert exc == designated, 'lost or extra exception'

    interiors = {}
    for a, length in blocks:
        cells = set(range(a+2, a+length+1)) if length else set()
        assert not (cells & exc or cells & set(interiors))
        assert len(cells) == max(0, length-1)
        assert sum(i % 2 == 0 for i in cells) == length//2
        assert sum(i % 2 == 1 for i in cells) == max(0, length//2-1)
        interiors.update((i, 2*a+length) for i in cells)
    active = sum(length > 0 for _, length in blocks)
    ordinary = set(range(1, m+1))-exc-set(interiors)
    assert len(exc) == 2+int(s > 0)+active <= 6
    assert len(interiors) == z-active
    assert len(ordinary) == m-z-2-int(s > 0)
    assert len(exc)+len(interiors)+len(ordinary) == m

    seams = {1: (m+s, m+s+1) if s else (2*m, m+1),
             r: (2*m-1, 2*m)}
    if s:
        seams[r+1] = (2*m, m+1)
    if q:
        seams[q+1] = (m+s+2, m+s+q+1)
    if d:
        seams[e+1] = (m+s+q+2, m+s+e+1)
    if f:
        seams[z+1] = (m+s+e+2, m+s+z+1)
        assert e+1 in exc and e+1 not in interiors
        assert order[e-1] == m+s+q+2
    assert set(seams) == exc

    panels = 0
    for i, (prev, curr) in enumerate(zip(predecessors, order), 1):
        if i in exc:
            assert (prev, curr) == seams[i], (m, s, q, d, f, i)
            continue
        if i in interiors:
            c = interiors[i]
            if i % 2 == 0:
                expected = (m+s+i-1, m+s+c+2-i)
                bound = 2
                triples = [(t, m+s+t, m+s+c-t) for t in (i-2, i)]
            else:
                expected = (m+s+c+3-i, m+s+i)
                bound = 4
                triples = [(t, m+s+c-t, m+s+t) for t in (i-1, i+1)]
        else:
            assert i in ordinary and (i < r or i > r+1)
            offset = m+s if i < r else s
            expected = (offset+i-1, offset+i)
            bound = 1
            triples = [(t, offset+t, offset+t) for t in (i-1, i)]
        assert (prev, curr) == expected, (m, s, q, d, f, i)
        for triple in triples:
            assert 0 <= triple[0] <= m
            assert all(m <= value <= 2*m for value in triple[1:])
            assert max(abs(a-b) for a, b in zip((i, prev, curr), triple)) <= bound
        panels += 1
    assert panels == m-len(exc)
    assert sum(2*(length//2) for _, length in blocks)+(m-z) == m
    return panels


def audit_box(m, s, q, d, f, aa, ll, ee):
    """Affine residual bounds on every exact closed floor-box corner."""
    assert 2*(s+q+d+f) < m and m-s >= q+d+f+2
    assert f == 2*(m//2000) and 0 <= f <= d <= q
    assert (q == 0) == (m <= 6)
    assert (s == 0) == (m <= 9)
    if m <= 45:
        assert d == 0
    if m == 46:
        assert d in (0, 2)
    if m >= 47:
        assert d >= 2
    dd = m*DELTA-f
    assert 0 <= dd < 2
    for alpha, lam, epsilon in product(aa, ll, ee):
        da, dl, de = m*alpha-s, m*lam-q, m*epsilon-d
        # Closure adds only harmless upper residual ties.
        assert 0 <= da <= 1 and 0 <= dl <= 2 and 0 <= de <= 2
        assert alpha+lam+epsilon+DELTA < Q(1, 2)
        assert da+dl <= 3 and da+2*dl+de <= 7
        assert da+2*dl+2*de+dd <= 11
        assert da+dl+(dl+de)+(dl+de+dd) <= 13


def must_reject(call, exception):
    try:
        call()
    except exception:
        return
    raise AssertionError('mutation or malformed input was not rejected')


def main():
    assert 0 < DELTA < EL < EH < LL < LH and 0 < AL < AH
    slack = Q(1, 2)-AH-LH-EH-DELTA
    assert slack > 0
    assert 6*LH < 2 < 7*LL and 9*AH < 1 < 10*AL
    assert 45*EH < 2 < 47*EL
    assert [x for x, _ in floor_cells(Q(1, 4), Q(1, 2), 8, 2)] == [2]
    assert [x for x, _ in floor_cells(Q(1, 8), Q(3, 8), 8, 2)] == [0, 2]
    audit_order(1, 0, 0, 0, 0, list_order(1, 0, 0, 0, 0))

    cases = cells = panels = 0
    m46_widths, lengths, fixed_parities = set(), set(), set()
    for m in (*range(2, 513), *SPECIAL):
        per_m = 0
        f = 2*(m//2000)
        lengths.add(f)
        if f:
            fixed_parities.add(f % 4)
        for s, aa in floor_cells(AL, AH, m, 1):
            for q, ll in floor_cells(LL, LH, m, 2):
                for d, ee in floor_cells(EL, EH, m, 2):
                    audit_box(m, s, q, d, f, aa, ll, ee)
                    panels += audit_order(m, s, q, d, f, list_order(m, s, q, d, f))
                    cases += 1
                    cells += m
                    per_m += 1
                    if m == 46:
                        m46_widths.add(d)
        assert per_m > 0
    assert m46_widths == {0, 2} and {0, 2, 4, 6, 8} <= lengths
    assert fixed_parities == {0, 2}
    assert [(m, 2*(m//2000)) for m in (1999, 2000, 3999, 4000)] == [
        (1999, 0), (2000, 2), (3999, 2), (4000, 4)]

    exact_onset = [(s, q, d) for s, _ in floor_cells(AL, AH, 2000, 1)
                   for q, _ in floor_cells(LL, LH, 2000, 2)
                   for d, _ in floor_cells(EL, EH, 2000, 2)]
    assert exact_onset == [(218, 638, 86)]
    onset = list_order(2000, 218, 638, 86, 2)
    assert (onset[723], onset[724]) == (2858, 2943)
    assert (onset[725], onset[726]) == (2944, 2945)
    assert (onset[1781], onset[1782]) == (4000, 2001)
    assert (onset[-1], onset[0]) == (2218, 2219)

    # This is ONE bracket-compatible floor case, not a choice of the
    # implicitly defined parameters. The loop above checks every case.
    m = 4000
    s = next(floor_cells(AL, AH, m, 1))[0]
    q = next(floor_cells(LL, LH, m, 2))[0]
    d = next(floor_cells(EL, EH, m, 2))[0]
    f, e = 4, q+d
    order = list_order(m, s, q, d, f)
    audit = lambda values: audit_order(m, s, q, d, f, values)
    duplicate = order.copy()
    duplicate[0] = duplicate[1]
    must_reject(lambda: audit(duplicate), AssertionError)
    for start, end in ((0, e), (q, e+f)):
        highs = list(range(m+1, 2*m+1))
        union = highs[s:]+highs[:s]
        # Preserve the third/first separate block outside the merged pair.
        a, length = (e, f) if start == 0 else (0, q)
        union[a+1:a+length:2] = union[a+1:a+length:2][::-1]
        union[start+1:end:2] = union[start+1:end:2][::-1]
        must_reject(lambda: audit(union), AssertionError)

    predecessors = order[-1:]+order[:-1]
    j = predecessors.index(m+s+e)
    predecessors[e], predecessors[j] = predecessors[j], predecessors[e]
    must_reject(lambda: audit_order(m, s, q, d, f, order, predecessors), AssertionError)
    exc = sorted({1, m-s, m-s+1, q+1, e+1, e+f+1})
    must_reject(lambda: audit_order(m, s, q, d, f, order,
                                   exceptions=[i for i in exc if i != e+1]), AssertionError)
    must_reject(lambda: audit_order(m, s, q, d, f, order,
                                   exceptions=exc+[e+1]), AssertionError)
    tiny = list_order(2, 0, 0, 0, 0)
    must_reject(lambda: audit_order(2, 0, 0, 0, 0, tiny, tiny), AssertionError)

    invalid = [(0, 0, 0, 0, 0), (True, 0, 0, 0, 0), (10, -1, 2, 0, 0),
               (10, 1, 3, 0, 0), (10, 1, 2, 1, 0), (10, 1, 2, 2, 1),
               (10, 1, 0, 2, 0), (10, 1, 2, 0, 2), (10, 1, 6, 2, 0),
               (10, 1, -2, 0, 0), (1, 0, 2, 0, 0), (10, 10, 0, 0, 0)]
    for args in invalid:
        must_reject(lambda args=args: list_order(*args), ValueError)

    print('EXACT half-wrap slack =', slack, '> 0')
    print('PASS rational domain/onset gates; strict bracket floor ties; exact delta floors')
    print(f'PASS m=2..512 plus {len(SPECIAL)} declared sizes: {cases} floor cases; {cells} cyclic cells')
    print(f'PASS {panels} nonexception panel bounds; all pairs, counts, parity and bijections')
    print('PASS all closed floor-box corners: coordinate constant 11; boundary-mass constant 13')
    print('PASS m=1; m=46 both widths; third lengths 0,2,4,6,8; both midpoint parities')
    print('PASS exact m=2000 floors (218,638,86,2); actual shared seam (2858,2943)')
    print('PASS 7 rejected mutations (including lost/duplicated second-third seam); 12 invalid inputs')
    print('NOTE: exact finite audit; implicit floors overcovered, minima imported, all-m proof separate; no radius transfer')


if __name__ == '__main__':
    main()
