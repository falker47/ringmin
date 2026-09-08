"""Bounded exact three-block audit; python -S; no writes or project imports.

Adapted from the boundary full-root checker at base dbb41f3. The list
constructor and arctangent enclosures are independent of production;
analytic sign/error algebra is shared with the proof. No implicit root
or optimized parameter is computed; all bracket-compatible floors covered.
"""
from fractions import Fraction as Q
from math import isqrt

AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1+AL)*XL, (1+AH)*XH
EL, EH = Q(43, 1000), Q(11, 250)
C0 = Q(1, 32)
SCALE = 10**24
DELTA = Q(1, 1000)
SIZES = tuple(range(2, 17))+(32, 45, 46, 47, 1999, 2000, 2001,
                            2047, 2048, 2049, 3999, 4000, 4001,
                            5999, 6000, 6001)


def sign(x):
    return (x > 0)-(x < 0)


def floor_cover(m):
    # For L<parameter<H, floor ranges from floor(L*m) to ceil(H*m)-1.
    for s in range((AL*m)//1, -((-AH*m)//1)):
        for q2 in range((LL*m/2)//1, -((-LH*m/2)//1)):
            for d2 in range((EL*m/2)//1, -((-EH*m/2)//1)):
                yield s, 2*q2, 2*d2


def construct(m, s, q, d, f=None):
    if f is None:
        f = 2*(m//2000)
    assert all(type(x) is int for x in (m, s, q, d, f))
    assert m >= 2 and 0 <= s < m and 0 <= f <= d <= q
    assert q % 2 == d % 2 == f % 2 == 0 and s+q+d+f < Q(m, 2)
    highs = list(range(m+1, 2*m+1))
    P = highs[s:]+highs[:s]
    P[1:q:2] = P[1:q:2][::-1]
    P[q+1:q+d:2] = P[q+1:q+d:2][::-1]
    P[q+d+1:q+d+f:2] = P[q+d+1:q+d+f:2][::-1]
    assert sorted(P) == highs
    return P


def formula(m, s, q, d, i):
    f, e = 2*(m//2000), q+d
    j = (q+2-i if i <= q and i % 2 == 0 else
         2*q+d+2-i if q < i <= e and i % 2 == 0 else
         2*e+f+2-i if e < i <= e+f and i % 2 == 0 else i)
    return m+1+(j+s-1) % m


def seams(m, s, q, d):
    r, e = m-s, q+d
    out = {1: (m+s, m+s+1) if s else (2*m, m+1),
           r: (2*m-1, 2*m)}
    if s:
        out[r+1] = 2*m, m+1
    if q:
        out[q+1] = m+s+2, m+s+q+1
    if d:
        out[e+1] = m+s+q+2, m+s+e+1
    f = 2*(m//2000)
    if f:
        out[e+f+1] = m+s+e+2, m+s+e+f+1
    return out


def deletion(m, s, P):
    r = m-s
    j = r % m+1
    assert P[r-1] == 2*m
    cycle = [x for i, p in enumerate(P, 1) for x in (i, p) if x != 2*m]
    assert sorted(cycle) == list(range(1, 2*m))
    nxt = dict(zip(cycle, cycle[1:]+cycle[:1]))
    used = set()
    for i in range(1, m+1):
        contains = 2*m in (P[i-2], P[i-1])
        assert contains == (i in (r, j))
        if contains:
            continue
        left, right = P[i-2], P[i-1]
        assert nxt[left] == i and nxt[i] == right
        for edge in ((left, i), (i, right)):
            assert edge not in used
            used.add(edge)
    assert len(used) == 2*m-4 and len(cycle)-len(used) == 3
    assert nxt[r] == j  # merged low-low gap, including cyclic j=1
    return len(used)


def radical_sign(a, b, c):
    """Sign(sqrt(a)+sqrt(b)-sqrt(c)); every squaring gate retained."""
    assert min(a, b, c) >= 0
    h = c-a-b
    if h < 0:
        return 1
    if h == 0:
        return 1 if a*b > 0 else 0
    return sign(4*a*b-h*h)


def sine_branch(U, V, W):
    assert 0 < U < 1 and 0 < V < 1 and 0 < W < 1
    if U+V >= 1:  # sum of the two half-angles >= pi/2
        return 1
    return radical_sign(U*(1-V), V*(1-U), W)


def angular_branch(R, low, left, right):
    assert R > 0 and min(low, left, right) > 0
    return sine_branch(Q(low*left)/((R+low)*(R+left)),
                       Q(low*right)/((R+low)*(R+right)),
                       Q(left*right)/((R+left)*(R+right)))


def down(x):
    return Q((x*SCALE)//1, SCALE)


def up(x):
    return -down(-x)


def add(a, b):
    return down(a[0]+b[0]), up(a[1]+b[1])


def mul_positive(a, b):
    assert min(*a, *b) >= 0
    return down(a[0]*b[0]), up(a[1]*b[1])


def scale(a, c):
    assert c >= 0
    return down(a[0]*c), up(a[1]*c)


def sqrt_bounds(x):
    x = Q(x)
    assert x >= 0
    k = isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo = Q(k, SCALE)
    hi = lo if lo*lo == x else Q(k+1, SCALE)
    assert lo*lo <= x <= hi*hi
    return lo, hi


def atan_small(x):
    """Outward-rounded alternating series; 32 terms and signed remainder."""
    assert 0 <= x <= Q(1, 2)
    power = (x, x)
    square = (x*x, x*x)
    total = (Q(0), Q(0))
    for k in range(32):
        term = scale(power, Q(1, 2*k+1))
        total = add(total, term if k % 2 == 0 else (-term[1], -term[0]))
        power = mul_positive(power, square)
    return total[0], up(total[1]+power[1]/65)


def theta_bounds(R, h, k):
    # tan(theta/2)^2=hk/[R(R+h+k)], independent of the sine sign oracle.
    lo, hi = sqrt_bounds(Q(h*k)/(R*(R+h+k)))
    assert hi <= Q(1, 2)
    return 2*atan_small(lo)[0], 2*atan_small(hi)[1]


def imax(a, b):
    return max(a[0], b[0]), max(a[1], b[1])


def full_intervals(R, i, left, right):
    angles = [theta_bounds(R, h, k)
              for h, k in ((i, left), (i, right), (left, right))]
    leads = [scale(sqrt_bounds(Q(h*k)), 2/R)
             for h, k in ((i, left), (i, right), (left, right))]
    full = imax(add(angles[0], angles[1]), angles[2])
    linear = imax(add(leads[0], leads[1]), leads[2])
    return angles, leads, full, linear


def within(a, b, error):
    assert -error <= a[0]-b[1] and a[1]-b[0] <= error


def analytic_gates():
    margin = Q(1, 2)-AH-LH-EH-DELTA
    assert margin == Q(26541513, 10**9) > 0
    assert 0 < DELTA < EL < EH < LL < LH
    assert 6*LH < 2 < 7*LL and 9*AH < 1 < 10*AL
    assert 45*EH < 2 < 47*EL
    assert (1+AL)*(1-3*XH)-3*EH-4*DELTA == Q(1586317, 10**8) > 0
    upper_M = 1+AH+LH+EH+DELTA/2
    assert upper_M == Q(1472958487, 10**9) < Q(3, 2)
    assert DELTA**3/36 == Q(1, 36000000000)
    assert DELTA**3/(36*16) == Q(1, 576000000000)
    assert 2 < Q(3, 2)**2
    assert 2-1-Q(3, 8) == Q(5, 8)
    assert Q(3, 4)*Q(7, 4) > 1
    assert 4*4+11*4+38*3 == 174
    assert 1024+16*174 == 3808 and 1024+174 == 1198
    m = 2048
    E = Q(1024, m)+Q(16384, 3*m*m)
    B = Q(96, m)+Q(2048, m*m)+Q(32768, 3*m**3)
    assert E < 1 and B < 1 and 16-E-B > Q(44, 7) and 3+E < 6
    assert Q(4*m*m, (2*m-1)**2) > 1
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)) == 0
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)-Q(1, 100)) == 1
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)+Q(1, 100)) == -1
    assert sine_branch(Q(1, 2), Q(1, 2), Q(99, 100)) == 1
    assert radical_sign(Q(0), Q(1), Q(1)) == 0
    print('EXACT half-wrap margin =', margin)
    print('PASS domain, shell, full-max/tie, saving and constants 174,3808,1198; root/deletion cutoff 2048', flush=True)


def bounded_checks():
    cases = cells = signs_checked = interval_cells = edges = 0
    seen_signs, at46 = set(), set()
    for m in SIZES:
        for s, q, d in floor_cover(m):
            cases += 1
            P = construct(m, s, q, d)
            assert P == [formula(m, s, q, d, i) for i in range(1, m+1)]
            r, e, f = m-s, q+d, 2*(m//2000)
            z = e+f
            assert r >= z+2
            exc = seams(m, s, q, d)
            assert len(exc) == (2 if m <= 6 else 3 if m <= 9 else 6 if f else 5 if d else 4)
            interior = max(q-1, 0)+max(d-1, 0)+max(f-1, 0)
            assert interior+len(exc) <= m
            if m == 46:
                at46.add(d)
            for i, right in enumerate(P, 1):
                left = P[i-2]
                assert m < min(left, right) <= max(left, right) <= 2*m and left != right
                if i in exc:
                    assert (left, right) == exc[i]
                cells += 1
                for R in (Q(1), Q(m*m, 8), Q(m*m, 2), Q(2*m*m)):
                    branch = angular_branch(R, i, left, right)
                    seen_signs.add(branch)
                    signs_checked += 1
                probes = set(exc) | {q+2, e, q+d//2, e+2, z, e+f//2}
                if m <= 6 or i in probes:
                    R = Q(2*m*m)
                    angles, leads, full, linear = full_intervals(R, i, left, right)
                    gap = angles[0][0]+angles[1][0]-angles[2][1], angles[0][1]+angles[1][1]-angles[2][0]
                    branch = angular_branch(R, i, left, right)
                    assert (gap[0] > 0 if branch > 0 else gap[1] < 0 if branch < 0 else gap[0] <= 0 <= gap[1])
                    em = Q(2, m*m)+Q(2, 3*m**3)  # c0=1/2
                    for angle, leading in zip(angles, leads):
                        within(angle, leading, em)
                    within(full, linear, 2*em)
                    interval_cells += 1
            edges += deletion(m, s, P)
    assert at46 == {0, 2} and seen_signs == {-1, 1}
    print('PASS', cases, 'floor cases;', cells, 'actual cells;', signs_checked,
          'rational branch signs;', interval_cells, 'independent angle/full-max enclosures', flush=True)
    print('PASS', edges, 'disjoint retained odd gaps; all small cycles and both m=46 floors')


def complete_score_enclosures():
    count = 0
    for m in (32, 46, 47):
        for s, q, d in floor_cover(m):
            P = construct(m, s, q, d)
            removed = {m-s, (m-s) % m+1}
            for c in (C0, Q(1, 2)):
                R = 4*c*m*m
                full_total = linear_total = omitted = (Q(0), Q(0))
                for i, right in enumerate(P, 1):
                    _, _, full, linear = full_intervals(R, i, P[i-2], right)
                    full_total = add(full_total, full)
                    linear_total = add(linear_total, linear)
                    if i in removed:
                        omitted = add(omitted, full)
                E = 1/(c*c*m)+1/(6*c**3*m*m)
                within(full_total, linear_total, E)
                B = Q(96, m)+Q(2048, m*m)+Q(32768, 3*m**3)
                assert 0 <= omitted[0] <= omitted[1] <= B
                count += 1
    print('PASS', count, 'complete-score and two-cell deletion interval bounds at c=1/32,1/2')


def mutation_checks():
    m = 4000
    s, q, d = next(floor_cover(m))
    f, e = 2*(m//2000), q+d
    P = construct(m, s, q, d)
    # Rejected wrong actual seam, merged blocks, lost cell and lone branches.
    assert (P[e-1], P[e]) == (m+s+q+2, m+s+e+1)
    assert P[e-1] not in (m+s+e, m+s+e+2)
    assert P[-1] != P[0]
    assert construct(m, s, q, d+f, 0) != P
    R = Q(2*m*m)
    signs = {angular_branch(R, i, P[i-2], p) for i, p in enumerate(P, 1)}
    assert signs == {-1, 1}
    seam = full_intervals(R, e+1, P[e-1], P[e])[2]
    assert seam[0] > 0  # omission or duplication changes the full score
    rejected = 0
    for args in ((1, 0, 0, 0, 0), (10, 0, 3, 0, 0), (10, 0, 2, 3, 0),
                 (10, 0, 0, 2, 0), (10, 0, 2, 0, 2)):
        try:
            construct(*args)
        except AssertionError:
            rejected += 1
    assert rejected == 5
    print('PASS incorrect shared/cyclic predecessors, merged second/third, lost/duplicated seam and single-branch controls; 5 invalid inputs')


if __name__ == '__main__':
    analytic_gates()
    bounded_checks()
    complete_score_enclosures()
    mutation_checks()
    print('NOTE: exact finite arithmetic audits; analytic all-m proofs and imported minima remain separate')
