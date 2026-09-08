"""Bounded numerical observations, never certificates; no writes/project imports.

All bracket-compatible floors are overcovered at the declared small sizes;
no approximate implicit parameter is substituted. Geometry uses atan angles
and Cartesian distances, while cell roots use asin. The difference-constraint
solver uses every unordered pair and never uses the cell criterion.
"""

from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps = 50
TAU = 2*mp.pi
TOL = mp.mpf('1e-32')
SIZES = tuple(range(2, 13))+(16, 46)


def floor_cases(m):
    al, ah = Q(1093, 10000), Q(10931, 100000)
    ll, lh = (1+al)*Q(719, 2500), (1+ah)*Q(2877, 10000)
    for s in range((m*al)//1, -((-m*ah)//1)):
        for q in range((m*ll/2)//1, -((-m*lh/2)//1)):
            for d in range((m*Q(43, 1000)/2)//1,
                           -((-m*Q(11, 250)/2)//1)):
                yield s, 2*q, 2*d


def order(m, s, q, d):
    # Work on slots using pairwise exchanges, not the displayed J formula.
    p = [m+1+(s+j) % m for j in range(m)]
    for start, length in ((0, q), (q, d), (q+d, 2*(m//2000))):
        slots = list(range(start+1, start+length, 2))
        for j in range(len(slots)//2):
            left, right = slots[j], slots[-1-j]
            p[left], p[right] = p[right], p[left]
    assert sorted(p) == list(range(m+1, 2*m+1))
    return p


def angle(R, a, b):
    return 2*mp.asin(mp.sqrt(a*b/((R+a)*(R+b))))


def alternate(R, a, b):
    return 2*mp.atan(mp.sqrt(a*b/(R*(R+a+b))))


def cells(R, p):
    rows = []
    for i, right in enumerate(p, 1):
        a, b, c = angle(R, p[i-2], i), angle(R, i, right), angle(R, p[i-2], right)
        rows.append((a, b, c, max(a+b, c)))
    return rows


def root(p, omit=()):
    lo, hi = mp.mpf(0), mp.mpf(2*len(p)**2)

    def score(R):
        return mp.fsum(row[3] for i, row in enumerate(cells(R, p), 1) if i not in omit)

    assert score(hi) < TAU
    for _ in range(120):
        mid = (lo+hi)/2
        if score(mid) > TAU:
            lo = mid
        else:
            hi = mid
    assert score(lo) > TAU >= score(hi)
    return (lo+hi)/2


def placement(R, p):
    data = cells(R, p)
    xs = [row[0] for row in data]
    ys = [row[3]-row[0] for row in data]
    slack = TAU-mp.fsum(xs+ys)
    assert slack > 0
    xs[0] += slack
    radii, angles, phi = [], [], mp.mpf(0)
    for i, high in enumerate(p, 1):
        radii.extend((i, high))
        angles.extend((phi, phi+ys[i-1]))
        phi += ys[i-1]+xs[i % len(p)]
    assert abs(phi-TAU) < TOL
    return radii, angles


def geometry(R, radii, angles):
    centers = [(R+r)*mp.exp(mp.j*t) for r, t in zip(radii, angles)]
    count = 0
    for j, b in enumerate(radii):
        assert abs(abs(centers[j])-R-b) < TOL
        for i in range(j):
            a = radii[i]
            bound = alternate(R, a, b)
            path = angles[j]-angles[i]
            assert path >= bound-TOL and TAU-path >= bound-TOL
            assert abs(centers[j]-centers[i]) >= a+b-TOL
            count += 1
    return count


def all_pairs_feasible(R, radii):
    # phi_j-phi_i in [theta,2*pi-theta] for every i<j.
    # A super-source of zero-weight arcs is represented by zero initial labels.
    edges = []
    for j, b in enumerate(radii):
        for i in range(j):
            theta = alternate(R, radii[i], b)
            edges.extend(((i, j, TAU-theta), (j, i, -theta)))
    dist = [mp.mpf(0) for _ in radii]
    for _ in radii:
        changed = False
        for i, j, weight in edges:
            candidate = dist[i]+weight
            if candidate < dist[j]-TOL:
                dist[j] = candidate
                changed = True
        if not changed:
            # Check the actual returned witness against ALL constraints.
            assert all(dist[j] <= dist[i]+weight+TOL for i, j, weight in edges)
            return True
    return False


def main():
    cases = pairs = probes = 0
    for m in SIZES:
        for s, q, d in floor_cases(m):
            p = order(m, s, q, d)
            rho = root(p)
            step = mp.mpf('1e-12')*max(1, rho)
            even, phis = placement(rho+step, p)
            odd = [h for h in even if h != 2*m]
            odd_phis = [t for h, t in zip(even, phis) if h != 2*m]
            pairs += geometry(rho+step, even, phis)
            pairs += geometry(rho+step, odd, odd_phis)
            assert not all_pairs_feasible(rho-step, even)
            assert all_pairs_feasible(rho+step, even)
            assert all_pairs_feasible(rho+step, odd)
            probes += 3
            if m >= 4:
                r = m-s
                tau = root(p, {r, r % m+1})
                assert 0 < tau < rho
                assert not all_pairs_feasible(tau-step, odd)
                probes += 1
            cases += 1
            print('PASS numerical case', (m, s, q, d), 'rho/(2m)^2', mp.nstr(rho/(4*m*m), 14), flush=True)
    print('PASS', cases, 'floor cases;', pairs, 'even/deleted-odd pairs: both directed paths and Cartesian distances')
    print('PASS', probes, 'independent all-pairs difference-constraint probes; even root sides and odd squeeze sides')
    print('NOTE: 50-digit numerical observations, tolerance 1e-32, probe offset 1e-12*max(1,rho); no exact certificate or implicit-floor oracle')


if __name__ == '__main__':
    main()
