"""Exact bounded audit of the fixed second-block full-root transfer.

Run with python -S. No production, verifier or previous-checker imports;
no decimal minimizers, root optimization, permutation search or files written.
All integer floors compatible with the imported strict brackets are covered.
The analytic note supplies the all-m theorem; these are local proof audits.
"""

from fractions import Fraction as Q
from math import isqrt


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1+AL)*XL, (1+AH)*XH
u, eps = Q(1, 3), Q(1, 100)
v = u+eps
SIZES = tuple(range(2, 17))+(199, 200, 201, 399, 400, 401, 599, 600, 601, 1200, 1201)
SCALE = 10**24


def sign(x):
    return (x > 0)-(x < 0)


def sqrt_bounds(x):
    assert x >= 0
    k = isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo = Q(k, SCALE)
    hi = lo if lo*lo == x else Q(k+1, SCALE)
    assert lo*lo <= x <= hi*hi
    return lo, hi


def atan_bounds(x, terms=48):
    """Alternating-series enclosure; even partial sum is the lower bound."""
    assert 0 <= x <= Q(1, 2) and terms > 0 and terms % 2 == 0
    power, total = x, Q(0)
    for j in range(terms):
        total += (-1)**j*power/(2*j+1)
        power *= x*x
    return total, total+power/(2*terms+1)


def theta_bounds(R, a, b):
    """Independent half-angle tangent, not the branch oracle's sine formula."""
    lo, hi = sqrt_bounds(Q(a*b)/(R*(R+a+b)))
    assert hi <= Q(1, 2)
    return 2*atan_bounds(lo)[0], 2*atan_bounds(hi)[1]


def radical_sum_sign(a, b, c):
    """Exact sign of sqrt(a)+sqrt(b)-sqrt(c), with positive-side gates."""
    assert min(a, b, c) >= 0
    k = c-a-b
    if k < 0:
        return 1
    if k == 0:
        return 1 if a*b > 0 else 0
    return sign(4*a*b-k*k)


def sine_branch(U, V, W):
    assert 0 < U < 1 and 0 < V < 1 and 0 < W < 1
    if U+V >= 1:
        return 1
    return radical_sum_sign(U*(1-V), V*(1-U), W)


def angular_branch(R, low, left, right):
    """+1 chain, -1 chord, 0 exact tie; valid at every rational R>0."""
    assert R > 0 and min(low, left, right) > 0
    U = Q(low*left)/((R+low)*(R+left))
    V = Q(low*right)/((R+low)*(R+right))
    W = Q(left*right)/((R+left)*(R+right))
    return sine_branch(U, V, W), U+V >= 1


def floor_cover(m):
    # Strict upper endpoints: ceil(x)-1 is the greatest possible floor.
    for s in range((AL*m)//1, -((-AH*m)//1)):
        for k in range((LL*m/2)//1, -((-LH*m/2)//1)):
            yield s, 2*k


def construct(m, s, q):
    assert type(m) is int and m >= 2
    p, d = 2*(m//6), 2*(m//200)
    assert 0 <= s < m and q % 2 == 0 and 0 <= q <= p
    assert s+max(q, p+d) < m
    highs = list(range(m+1, 2*m+1))
    P = highs[s:]+highs[:s]
    # Independent list operations, with one occurrence in each even slot.
    P[1:q:2] = P[1:q:2][::-1]
    P[p+1:p+d:2] = P[p+1:p+d:2][::-1]
    assert sorted(P) == highs
    return P


def seam_pairs(m, s, q):
    p, d, r = 2*(m//6), 2*(m//200), m-s
    e = p+d
    pairs = {1: (m+s, m+s+1) if s else (2*m, m+1), r: (2*m-1, 2*m)}
    if s:
        pairs[r+1] = (2*m, m+1)
    if q:
        pairs[q+1] = (m+s+2, m+s+q+1)
    if d:
        pairs[p+1] = (m+s+p, m+s+p+1)
        pairs[e+1] = (m+s+p+2, m+s+e+1)
    return pairs


def deleted_cells(m, s, P):
    """Audit the odd cycle directly, without applying the alternating criterion."""
    assert m >= 10 and s > 0
    r = m-s
    assert P[r-1] == 2*m
    cycle = [item for i, high in enumerate(P, 1) for item in (i, high) if item != 2*m]
    assert sorted(cycle) == list(range(1, 2*m))
    successors = dict(zip(cycle, cycle[1:]+cycle[:1]))
    used = set()
    for i in range(1, m+1):
        if i in (r, r+1):
            continue
        left, right = P[i-2], P[i-1]
        assert successors[left] == i and successors[i] == right
        for edge in ((left, i), (i, right)):
            assert edge not in used
            used.add(edge)
    assert len(used) == 2*m-4
    assert len(cycle)-len(used) == 3
    return len(used)


def analytic_gates():
    assert u-LH > Q(1, 100) and 1-AH-v > Q(1, 2)
    assert AL-4*eps == Q(693, 10000) > 0
    assert v < (1+AL)/3 and (1+AH)/3 < 1-AH
    assert (1+AH)+u+eps/2 < Q(3, 2)
    # Prefix has a genuine chain part at x_*, certified without a squared root choice.
    assert radical_sum_sign(XL/(1+XL), XL, Q(1)) > 0
    assert 2 < Q(3, 2)**2  # 2 sqrt(2)+1 < 4, and ||g|| < 3.
    assert 2-1-Q(3, 8) == Q(5, 8)  # high-shell small-angle polynomial margin

    m, c0 = 2048, Q(1, 32)
    E = 1/(c0*c0*m)+1/(6*c0**3*m*m)
    B = 3/(c0*m)+2/(c0*c0*m*m)+1/(3*c0**3*m**3)
    assert E < 1 and B < 1
    assert 16-E-B > Q(44, 7) and 3+E < 6
    assert 7*4+32*3 == 124

    # Actual second block, including its entry and exit: all m>=200.
    m = 200
    assert 4*(v+Q(1, m))/((1+AL)+u-Q(3, m)) < Q(99, 100)**2
    assert 4*Q(1, m) < Q(1, 2)**2  # low seam: chain/chord < 1/2
    assert 2*(1-AH) > Q(5, 4)**2  # pre-wrap endpoint: ratio > 5/4
    assert radical_sum_sign((1-AH)/2, (1-AH)/(1+Q(1, m)), Q(3, 2)**2) > 0
    # Prefix exit has the opposite branch; retain this true jump.
    m = 100000
    t = LL-Q(1, m)
    assert radical_sum_sign(t/(1+AH+Q(2, m)), t/(1+AH+LH+Q(1, m)), Q(201, 200)**2) > 0
    assert Q(96, m)+Q(512, m*m) < Q(1, 200)

    # Oracle guard cases: exact tie, either side, and sum of half-angles >= pi/2.
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)) == 0
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)-Q(1, 100)) == 1
    assert sine_branch(Q(1, 4), Q(1, 4), Q(3, 4)+Q(1, 100)) == -1
    assert sine_branch(Q(1, 2), Q(1, 2), Q(99, 100)) == 1
    assert radical_sum_sign(Q(0), Q(1), Q(1)) == 0
    print("PASS exact analytic gates: fixed domains, both continuum branches, Lipschitz 4, root/deletion cutoff 2048, all seam signs at m>=100000")


def bounded_cells():
    cases = cells = branch_checks = intervals = odd_edges = 0
    signs, large_half_sum = set(), 0
    for m in SIZES:
        for s, q in floor_cover(m):
            cases += 1
            P = construct(m, s, q)
            p, d, r = 2*(m//6), 2*(m//200), m-s
            seams = seam_pairs(m, s, q)
            assert len(seams) == (2 if m <= 6 else 3 if m <= 9 else 4 if m < 200 else 6)
            for i, right in enumerate(P, 1):
                left = P[i-2]  # actual cyclic list: i=1 uses P_m
                assert m+1 <= left <= 2*m and m+1 <= right <= 2*m and left != right
                if i in seams:
                    assert (left, right) == seams[i]
                cells += 1
                for R in (Q(1), Q(m*m, 8), Q(m*m, 2), Q(2*m*m)):
                    branch, large = angular_branch(R, i, left, right)
                    signs.add(branch)
                    large_half_sum += large
                    branch_checks += 1
                # Independent transcendental interval comparison at a bounded set.
                if m <= 12 or i in seams:
                    R = Q(2*m*m)
                    a, b, c = theta_bounds(R, i, left), theta_bounds(R, i, right), theta_bounds(R, left, right)
                    lo, hi = a[0]+b[0]-c[1], a[1]+b[1]-c[0]
                    branch = angular_branch(R, i, left, right)[0]
                    assert (lo > 0 if branch > 0 else hi < 0 if branch < 0 else lo <= 0 <= hi)
                    leading = [tuple(2*x/R for x in sqrt_bounds(Q(h*k)))
                               for h, k in ((i, left), (i, right), (left, right))]
                    em = Q(2, m*m)+Q(2, 3*m**3)  # c=1/2 in (10)
                    for angle, approx in zip((a, b, c), leading):
                        assert -em <= angle[0]-approx[1]
                        assert angle[1]-approx[0] <= em
                    full = max(a[0]+b[0], c[0]), max(a[1]+b[1], c[1])
                    linear = (max(leading[0][0]+leading[1][0], leading[2][0]),
                              max(leading[0][1]+leading[1][1], leading[2][1]))
                    assert -2*em <= full[0]-linear[1]
                    assert full[1]-linear[0] <= 2*em
                    intervals += 1
                if d and p+1 <= i <= p+d+1:
                    t, x, y = Q(i, m), Q(left, m), Q(right, m)
                    assert min(x, y) > (1+AL)+u-Q(3, m)
                    assert t <= v+Q(1, m)
                    assert radical_sum_sign(t/x, t/y, Q(99, 100)**2) < 0
            if m >= 10:
                odd_edges += deleted_cells(m, s, P)
            if m == 600:
                assert (s, q, p, d, r) == (65, 190, 200, 6, 535)
                actual = {i: angular_branch(Q(2*m*m), i, P[i-2], P[i-1])[0] for i in seams}
                assert actual == {1: -1, r: 1, r+1: 1, q+1: 1, p+1: -1, p+d+1: -1}
    assert signs == {-1, 1} and large_half_sum > 0
    print(f"PASS finite cover: {cases} prescribed orders at {len(SIZES)} fixed sizes m=2..1201; {cells} actual cyclic cells; {branch_checks} exact angular branch comparisons")
    print(f"PASS independent half-angle atan intervals: {intervals} separated signs and uniform angular/full-max error bounds; rational sqrt endpoints squared; 48-term proven remainders; exact synthetic tie gates")
    print(f"PASS deletion incidence: {odd_edges} disjoint surviving directed edges; exactly two cells omitted and three odd-cycle gaps uncounted per case")
    # Each of these simplifications contradicts a strict checked branch/incidence.
    assert actual[1] == -1 and actual[535] == 1
    assert seam_pairs(600, 65, 190)[536] != (600, 601)
    P = construct(600, 65, 190)
    assert 1200 in (P[535-1], P[535])
    print("PASS obstruction controls: chain-only seam, chord-only wrap, diagonalized wrap and keeping the deleted-high cell each violate an exact gate")


def saving_enclosure():
    a5, a239 = atan_bounds(Q(1, 5)), atan_bounds(Q(1, 239))
    pi_lo, pi_hi = 16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0]
    assert 3 < pi_lo < pi_hi < Q(22, 7)
    ML, MH, h = 1+AL+u+eps/2, 1+AH+u+eps/2, eps/2
    # Rationalized integral: bound its positive denominator over the whole interval.
    lower = eps**3/(96*pi_hi*MH)
    upper = eps**3/(48*pi_lo*(ML+sqrt_bounds(ML*ML-h*h)[0]))
    assert lower > Q(1, 144000000)/pi_lo
    assert lower > Q(2, 10**9)
    assert Q(14191364, 10**8)-lower < Q(141913638, 10**9)
    display = 10**18
    lo, hi = (lower*display)//1, -((-upper*display)//1)
    print(f"PASS exact coefficient saving: {lo}/10^18 < C_hat-C_2 < {hi}/10^18; in particular C_2 < C_hat-1/(144000000*pi) and C_2 < 141913638/10^9")


def main():
    analytic_gates()
    bounded_cells()
    saving_enclosure()
    print("NOTE: exact local proof audits, not finite global certification or a numerical root/parameter optimizer; all-m feasibility and limits use the written proof.")


if __name__ == "__main__":
    main()
