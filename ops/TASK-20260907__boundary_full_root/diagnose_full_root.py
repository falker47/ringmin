"""Bounded noncertified diagnostics; writes no files, imports no project code.

Exact-family parameters are numerically recomputed from defining equations.
All printed roots, costs and geometric checks are numerical observations.
The independent all-pairs solver uses difference constraints, not cell maxima.
"""
import mpmath as mp

mp.mp.dps = 60
Q = lambda p, q=1: mp.mpf(p)/q
STEPS = 140
TAU = 2*mp.pi
TOL = Q(1, 10**35)


def bisect_increasing(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(STEPS):
        mid = (lo+hi)/2
        if f(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def g(t, x, y):
    return max(mp.sqrt(t*x)+mp.sqrt(t*y), mp.sqrt(x*y))


def switch(A, u, e):
    gap = lambda s: (mp.sqrt((u+s)*(A+u+s))
                     +mp.sqrt((u+s)*(A+u+e-s))
                     -mp.sqrt((A+u+s)*(A+u+e-s)))
    if gap(e) <= 0:
        return e
    return bisect_increasing(gap, Q(0), e)


def raw_delta(A, u, e):
    z = switch(A, u, e)
    return mp.quad(lambda s: g(u+s, A+u+s, A+u+e-s)
                   -g(u+s, A+u+s, A+u+s), sorted(set([Q(0), z, e])))


def H(T, t):
    return T*mp.atan(mp.sqrt(t/(T-t)))-mp.sqrt(t*(T-t))


def width_slope(A, u, e):
    # Leibniz derivative from the defining integral; no optimized parameter scan.
    B, z = A+u, switch(A, u, e)
    integral = H(2*B+e, B+z)-H(2*B+e, B)
    integral += H(B+u+e, u+e)-H(B+u+e, u+z)
    return g(u+e, B+e, B)-(B+e)+integral/2


def parameters():
    x = bisect_increasing(lambda e: width_slope(Q(1), Q(0), e),
                          Q(719, 2500), Q(2877, 10000))
    E = raw_delta(Q(1), Q(0), x)

    def alpha_slope(alpha):
        A, b = 1+alpha, 1-alpha
        a = A/3
        Kp = (a/2+mp.quad(lambda t: mp.sqrt(t/(A+t)), [a, b])/2
              +mp.quad(lambda t: mp.sqrt(t/(alpha+t)), [b, 1])/2
              -(mp.sqrt(2)-1)*mp.sqrt(b))
        return Kp+A*E

    alpha = bisect_increasing(alpha_slope, Q(1093, 10000), Q(10931, 100000))
    A, lam = 1+alpha, (1+alpha)*x
    h = A/3-lam
    eps = bisect_increasing(lambda e: width_slope(A, lam, e), Q(43, 1000), Q(11, 250))
    assert Q(43, 1000) < eps < Q(11, 250) < h
    return x, E, alpha, A, lam, eps


def continuum(E, alpha, A, lam, eps):
    a, b, v = A/3, 1-alpha, lam+eps
    z1, zb = switch(A, Q(0), lam), switch(A, lam, eps)
    prefix = mp.quad(lambda t: g(t, A+t, A+lam-t), [0, z1, lam])
    block = mp.quad(lambda t: g(t, A+t, A+2*lam+eps-t), [lam, lam+zb, v])
    tail = mp.quad(lambda t: g(t, A+t, A+t), [v, a, b])
    tail += mp.quad(lambda t: g(t, alpha+t, alpha+t), [b, 1])
    Ib = prefix+block+tail
    K = (mp.quad(lambda t: (A+t)/2, [0, a])
         +mp.quad(lambda t: mp.sqrt(t*(A+t)), [a, b])
         +mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [b, 1]))
    Chat = K/(2*mp.pi)+A*A*E/(4*mp.pi)
    Db = raw_delta(A, lam, eps)
    Cb, C2 = Ib/(4*mp.pi), Chat+raw_delta(A, Q(1, 3), Q(1, 100))/(4*mp.pi)
    assert abs(Cb-Chat-Db/(4*mp.pi)) < Q(1, 10**38)
    assert Cb < C2 < Chat
    assert eps/2 < zb < eps and 0 < z1 < lam
    # Direct full max versus branch-split quadrature; both intervals nonempty.
    split = mp.quad(lambda s: mp.sqrt((A+lam+s)*(A+lam+eps-s)), [0, zb])
    split += mp.quad(lambda s: mp.sqrt(lam+s)*(mp.sqrt(A+lam+s)+mp.sqrt(A+lam+eps-s)), [zb, eps])
    assert abs(split-block) < Q(1, 10**38)
    chord_only = mp.quad(lambda s: mp.sqrt((A+lam+s)*(A+lam+eps-s)), [0, eps])
    assert block-chord_only > Q(1, 10**12)  # rejects importing the old branch
    step = Q(1, 10**12)
    derivative = (raw_delta(A, lam, eps+step)-raw_delta(A, lam, eps-step))/(2*step)
    assert abs(derivative) < Q(1, 10**22)
    print('PASS recomputed exact-family equations; full-max identity/split <1e-38; mixed branch and chord-only mutation; stationary residual <1e-22', flush=True)
    for name, value in [('x_star', lam/A), ('alpha_hat', alpha), ('lambda', lam),
                        ('epsilon_b', eps), ('chain_interval_length', eps-zb),
                        ('D_b_min', Db), ('C_b', Cb), ('C_2-C_b', C2-Cb)]:
        print('DIAGNOSTIC', name, mp.nstr(value, 24), flush=True)
    return Ib, Cb


def construct(m, alpha, lam, eps):
    s, q, d = int(mp.floor(alpha*m)), 2*int(mp.floor(lam*m/2)), 2*int(mp.floor(eps*m/2))
    # List operations, independently of the displayed J formula.
    P = list(range(m+s+1, 2*m+1))+list(range(m+1, m+s+1))
    P[1:q:2] = P[1:q:2][::-1]
    P[q+1:q+d:2] = P[q+1:q+d:2][::-1]
    assert sorted(P) == list(range(m+1, 2*m+1))
    return s, q, d, P


def theta(R, h, k):
    return 2*mp.asin(mp.sqrt(Q(h*k)/((R+h)*(R+k))))


def alternate_angle(R, h, k):
    return 2*mp.atan(mp.sqrt(Q(h*k)/(R*(R+h+k))))


def cells(R, P):
    out = []
    for i, right in enumerate(P, 1):
        left = P[i-2]
        a, b, c = theta(R, left, i), theta(R, i, right), theta(R, left, right)
        out.append((a, b, c, max(a+b, c)))
    return out


def score(R, P, omitted=()):
    return mp.fsum(d for i, (_, _, _, d) in enumerate(cells(R, P), 1) if i not in omitted)


def cell_root(P, omitted=()):
    lo, hi = Q(0), Q(2*len(P)**2)
    while score(hi, P, omitted) > TAU:
        hi *= 2
    for _ in range(STEPS):
        mid = (lo+hi)/2
        if score(mid, P, omitted) > TAU:
            lo = mid
        else:
            hi = mid
    assert score(lo, P, omitted) > TAU >= score(hi, P, omitted)
    return lo, hi


def placement(R, P, split=Q(0)):
    data = cells(R, P)
    excess = [max(Q(0), c-a-b) for a, b, c, _ in data]
    x = [a+split*ex for (a, _, _, _), ex in zip(data, excess)]
    y = [b+(1-split)*ex for (_, b, _, _), ex in zip(data, excess)]
    slack = TAU-mp.fsum(x+y)
    assert slack >= -TOL
    x[0] += slack
    order, angles = [], []
    pos = Q(0)
    for i, p in enumerate(P, 1):
        order.extend((i, p))
        angles.extend((pos, pos+y[i-1]))
        pos += y[i-1]+x[i % len(P)]
    assert abs(pos-TAU) < TOL
    return order, angles


def check_geometry(R, order, angles):
    centers = [(R+r)*mp.exp(mp.j*phi) for r, phi in zip(order, angles)]
    pairs, worst = 0, Q(0)
    for i, a in enumerate(order):
        assert abs(abs(centers[i])-(R+a)) < TOL
        for j in range(i+1, len(order)):
            b = order[j]
            angle = alternate_angle(R, a, b)
            forward = angles[j]-angles[i]
            reverse = TAU-forward
            assert forward >= angle-TOL and reverse >= angle-TOL
            cartesian = abs(centers[j]-centers[i])-(a+b)
            assert cartesian >= -TOL
            worst = min(worst, forward-angle, reverse-angle, cartesian)
            pairs += 1
    return pairs, worst


def stn_feasible(R, order):
    """All pair difference constraints via Bellman-Ford, independent of cells."""
    n = len(order)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            angle = alternate_angle(R, order[i], order[j])
            edges.extend(((i, j, TAU-angle), (j, i, -angle)))
    potentials = [Q(0)]*n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            candidate = potentials[u]+w
            if candidate < potentials[v]-Q(1, 10**48):
                potentials[v] = candidate
                changed = True
        if not changed:
            return True
    return False


def odd_stn_root(order, upper):
    assert stn_feasible(upper, order)
    lo, hi = upper/2, upper
    while stn_feasible(lo, order):
        lo /= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if stn_feasible(mid, order):
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def finite_diagnostics(alpha, lam, eps, Ib, Cb):
    sizes = tuple(range(2, 13))+(32, 45, 46, 47, 92, 100, 256)
    pair_count, stn_count, worst = 0, 0, Q(0)
    mixed_cells = set()
    for m in sizes:
        s, q, d, P = construct(m, alpha, lam, eps)
        lo, hi = cell_root(P)
        G = mp.fsum(g(Q(i, m), Q(P[i-2], m), Q(p, m)) for i, p in enumerate(P, 1))/m
        assert abs(G-Ib) <= Q(116, m)
        if m >= 32:
            for c0 in (Q(1, 32), Q(1, 2)):
                Em = 1/(c0*c0*m)+1/(6*c0**3*m*m)
                assert abs(score(4*c0*m*m, P)-G/(2*c0)) <= Em
        for a, b, c, _ in cells(hi, P):
            mixed_cells.add(mp.sign(a+b-c))
        if m <= 100:
            for split in ((Q(0), Q(1, 2), Q(1)) if m <= 6 else (Q(0),)):
                order, angles = placement(hi, P, split)
                pairs, slack = check_geometry(hi, order, angles)
                pair_count += pairs
                worst = min(worst, slack)
                odd = [(r, angle) for r, angle in zip(order, angles) if r != 2*m]
                pairs, slack = check_geometry(hi, [x[0] for x in odd], [x[1] for x in odd])
                pair_count += pairs
                worst = min(worst, slack)
        if m <= 8:
            order = [r for i, p in enumerate(P, 1) for r in (i, p)]
            assert not stn_feasible(lo*(1-Q(1, 10**12)), order)
            assert stn_feasible(hi*(1+Q(1, 10**12)), order)
            odd_order = [r for r in order if r != 2*m]
            odd_root = odd_stn_root(odd_order, hi)
            assert odd_root <= hi+TOL
            if m >= 4:
                r, j = m-s, (m-s) % m+1
                tlo, _ = cell_root(P, (r, j))
                assert tlo <= odd_root+Q(1, 10**25)
            stn_count += 1
        if m in (2, 46, 100, 256):
            print('DIAGNOSTIC finite m=', m, 'floors=', (s, q, d),
                  'rho/(2m)^2=', mp.nstr(hi/(4*m*m), 19), flush=True)
    assert mixed_cells == {-1, 1}
    print('PASS', len(sizes), 'finite roots/cost recovery;', pair_count,
          'even/deleted-odd pair checks in both directions and Cartesian coordinates; min slack=',
          mp.nstr(worst, 5), flush=True)
    print('PASS', stn_count, 'independent all-pairs even root +/- probes and odd STN roots with separate lower squeeze', flush=True)

    # One prescribed large order: root solving only, no parameter/permutation search.
    m = 2048
    s, _, _, P = construct(m, alpha, lam, eps)
    r, j = m-s, (m-s) % m+1
    center = Cb*4*m*m
    rho = mp.findroot(lambda R: score(R, P)-TAU, (center*Q(99, 100), center*Q(101, 100)))
    tau = mp.findroot(lambda R: score(R, P, (r, j))-TAU, (center*Q(99, 100), center*Q(101, 100)))
    for value, omitted in ((rho, ()), (tau, (r, j))):
        assert score(value*(1-Q(1, 10**30)), P, omitted) > TAU
        assert score(value*(1+Q(1, 10**30)), P, omitted) < TAU
        assert Q(1, 32) < value/(4*m*m) < Q(1, 2)
    E = Q(1024, m)+Q(16384, 3*m*m)
    B = Q(96, m)+Q(2048, m*m)+Q(32768, 3*m**3)
    assert abs(rho/(4*m*m)-Cb) <= (Q(116, m)+E)/(4*mp.pi)
    assert abs(tau/(4*m*m)-Cb) <= (Q(116, m)+E+B)/(4*mp.pi)
    assert tau <= rho
    G = mp.fsum(g(Q(i, m), Q(P[i-2], m), Q(p, m)) for i, p in enumerate(P, 1))/m
    assert abs(G-Ib) <= Q(116, m)
    for c in (Q(1, 32), Cb, Q(1, 2)):
        R = 4*c*m*m
        S, T = score(R, P), score(R, P, (r, j))
        assert abs(S-G/(2*c)) <= E
        assert abs(S-Ib/(2*c)) <= Q(2880, m)+Q(16384, 3*m*m)
        assert 0 <= S-T <= B
    print('PASS m=2048 compact brackets, complete uniform score/root bounds and two-cell omission bounds', flush=True)
    print('DIAGNOSTIC m=2048 rho/(2m)^2=', mp.nstr(rho/(4*m*m), 22),
          'tau/(2m)^2=', mp.nstr(tau/(4*m*m), 22), flush=True)


if __name__ == '__main__':
    x, E, alpha, A, lam, eps = parameters()
    Ib, Cb = continuum(E, alpha, A, lam, eps)
    finite_diagnostics(alpha, lam, eps, Ib, Cb)
    print('NOTE: 60-digit mpmath', mp.__version__, '; numerical observations, not certificates or exact parameter definitions')
