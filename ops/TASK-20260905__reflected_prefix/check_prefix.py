"""Bounded audit; analytic authority: PERMUTED_HALVES_REFLECTED_PREFIX.md.

No search over permutations, randomness, production or old-checker imports.
Exact checks use stdlib Fraction. Diagnostics use canonical mpmath==1.3.0.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import comb

import mpmath as mp


def order(m: int, s: int, q: int) -> tuple[int, ...]:
    """Independent list rotation and even-slot reversal, no rank formula."""
    if any(type(v) is not int for v in (m, s, q)):
        raise ValueError("m, s, q must be integers")
    if not (m >= 2 and 0 <= 2*s < m and 0 <= q < m-s and q % 2 == 0):
        raise ValueError("require m>=2, 0<=s<m/2, even 0<=q<m-s")
    highs = list(range(m+1, 2*m+1))
    highs = highs[s:] + highs[:s]
    highs[1:q:2] = highs[1:q:2][::-1]
    return tuple(highs)


def exceptions(m: int, s: int, q: int) -> set[int]:
    return ({1, m-s, m-s+1} | ({q+1} if q else set())) & set(range(1, m+1))


def floor(value: Q) -> int:
    return value.numerator // value.denominator


def target(i: int, m: int, q: int, alpha: Q, lam: Q) -> tuple[Q, Q]:
    t, aa = Q(i, m), 1+alpha
    if i <= q:
        pair = (aa+t, aa+lam-t)
        return pair if i % 2 == 0 else pair[::-1]
    h = 1+t+alpha-floor(t+alpha)
    return h, h


def rational_gates() -> None:
    margins = [Q(281, 500)**2-Q(6, 19), Q(647, 1000)**2-Q(28, 67),
               Q(24, 25)**2-Q(23, 25), 2-Q(707, 500)**2,
               Q(11, 12)-Q(957, 1000)**2]
    assert margins == [Q(259, 4750000), Q(46803, 67000000), Q(1, 625),
                       Q(151, 250000), Q(2453, 3000000)]
    assert min(margins) > 0
    upper = (Q(13, 72)+Q(5, 36)*(Q(281, 500)+Q(647, 1000))
             +Q(1, 24)*Q(24, 25)-Q(207, 500)*Q(957, 1000))
    assert upper == -Q(17383, 2250000)
    lam, x, y = Q(3, 10), Q(13, 12), Q(83, 60)
    hh = x*y-lam*(x+y)
    assert hh == Q(2731, 3600) > 0
    assert hh**2-4*lam**2*x*y == Q(466441, 12960000) > 0
    assert Q(3, 10) < Q(13, 36)
    assert Q(3, 10)**3/(24*Q(33, 20)) == Q(3, 4400)
    assert Q(1, 4)**3/(24*Q(13, 12)) == Q(1, 1664)
    assert Q(3, 4400)-Q(1, 1664) == Q(37, 457600) > 0
    assert 4*457600 == 1830400
    print(f"PASS rational: D(1/12)<{upper}; branch margin=466441/12960000; cost gap>37/457600")


def occurrences() -> None:
    cases = cells = coincident = empty = two = 0
    for m in range(2, 65):
        for s in range((m+1)//2):
            r = m-s
            for q in range(0, r, 2):
                pp = order(m, s, q)
                jj = [q+2-i if i <= q and i % 2 == 0 else i
                      for i in range(1, m+1)]
                assert sorted(jj) == list(range(1, m+1))
                assert [jj[j-1] for j in jj] == list(range(1, m+1))
                assert pp == tuple(m+1+(j+s-1) % m for j in jj)
                assert sorted(pp) == list(range(m+1, 2*m+1))
                assert sorted(pp[-1:]+pp[:-1]) == sorted(pp)
                bad = exceptions(m, s, q)
                assert pp[-1] == (m+s if s else 2*m)
                assert pp[0] == m+s+1 and pp[r-1] == 2*m
                if s:
                    assert pp[r-1:r+1] == (2*m, m+1)
                if q:
                    assert pp[q-1:q+1] == (m+s+2, m+s+q+1)
                    assert len(bad) == 4-(s == 0)-(r == q+1)
                    coincident += r == q+1
                else:
                    assert len(bad) == 3-(s == 0)
                    empty += 1
                two += q == 2
                interior = set(range(2, q+1))
                tail = set(range(q+1, m+1))-bad
                assert not interior & bad and not interior & tail
                assert interior | tail | bad == set(range(1, m+1))
                for i in range(1, m+1):
                    actual = pp[i-2], pp[i-1]
                    if i in interior:
                        expected = ((m+s+i-1, m+s+q+2-i) if i % 2 == 0
                                    else (m+s+q+3-i, m+s+i))
                        assert actual == expected
                    elif i not in bad:
                        offset = m+s if i < r else s
                        assert actual == (offset+i-1, offset+i)
                    cells += 1
                cases += 1
    for invalid in [(1, 0, 0), (8, -1, 2), (8, 4, 2), (8, 1, 7),
                    (8, 1, 8), (8, 1, -2), (8, True, 2), (8.0, 1, 2)]:
        try:
            order(*invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid input accepted: {invalid}")
    print(f"PASS occurrences: {cases} legal (m,s,q), m=2..64; {cells} predecessor cells")
    print(f"PASS seams: {coincident} coincident r=q+1, {empty} q=0, {two} q=2; invalid inputs rejected")


def coordinates() -> None:
    reps = cells = 0
    for m in range(2, 49):
        for lam in [Q(1, 4), Q(3, 10), Q(1, 2), Q(3, 4), Q(7, 8)]:
            q = 2*floor(lam*m/2)
            for s in range((m+1)//2):
                lo, hi = Q(s, m), min(Q(s+1, m), Q(1, 2), 1-lam)
                if lo >= hi:
                    continue
                alphas = [(lo+hi)/2] + ([lo] if lo else [])
                pp, bad = order(m, s, q), exceptions(m, s, q)
                for alpha in alphas:
                    assert floor(alpha*m) == s and alpha+lam < 1
                    for i in range(1, m+1):
                        pair = target(i, m, q, alpha, lam)
                        assert all(1 <= v <= 2 for v in pair)
                        if i not in bad:
                            assert max(abs(Q(pp[i-2], m)-pair[0]),
                                       abs(Q(pp[i-1], m)-pair[1])) <= Q(3, m)
                            cells += 1
                    reps += 1
    print(f"PASS coordinates: {reps} rational (alpha,lambda,m) tests; {cells} ordinary pairs within 3/m")


def multiply(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def polynomial_integral(powers: tuple[int, int, int], x: tuple[Q, Q],
                        y: tuple[Q, Q], lo: Q, hi: Q) -> Q:
    """Expand affine powers by binomial theorem; integrate rationally."""
    a, b, c = powers
    coeff = [Q(0)]*a+[Q(1)]
    for (offset, slope), exponent in [(x, b), (y, c)]:
        coeff = multiply(coeff, [Q(comb(exponent, j))*offset**(exponent-j)*slope**j
                                for j in range(exponent+1)])
    return sum(v*(hi**(j+1)-lo**(j+1))/(j+1) for j, v in enumerate(coeff))


def moments() -> None:
    alpha = Q(1, 10)
    count = 0
    tests = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
             (1, 1, 0), (0, 1, 1), (2, 1, 2), (1, 3, 1)]
    for lam in [Q(3, 10), Q(1, 2), Q(3, 4)]:
        for powers in tests:
            aa, bb = 1+alpha, 1-alpha
            exact = (polynomial_integral(powers, (aa, Q(1)), (aa+lam, Q(-1)), Q(0), lam)
                     +polynomial_integral(powers, (aa+lam, Q(-1)), (aa, Q(1)), Q(0), lam))/2
            exact += polynomial_integral(powers, (aa, Q(1)), (aa, Q(1)), lam, bb)
            exact += polynomial_integral(powers, (alpha, Q(1)), (alpha, Q(1)), bb, Q(1))
            a, b, c = powers
            norm = 2**(b+c)
            lipschitz = a*norm+(b+c)*Q(norm, 2)
            for m in [8, 9, 13, 20, 31, 64, 127, 256, 513]:
                q, s = 2*floor(lam*m/2), floor(alpha*m)
                if q < 2 or m-s < q+2:
                    continue
                pp = order(m, s, q)
                empirical = Q(sum(i**a*pp[i-2]**b*pp[i-1]**c for i in range(1, m+1)),
                              m**(1+a+b+c))
                assert abs(empirical-exact) <= (6*lipschitz+16*norm)/m
                count += 1
    print(f"PASS moments: {count} exact nonsymmetric polynomial tests, alpha=1/10, lambda=3/10,1/2,3/4")


def primitive_f(t, c):
    return ((2*t+c)*mp.sqrt(t*(t+c))/4
            -c*c*mp.asinh(mp.sqrt(t/c))/4)


def primitive_circle(u, radius):
    return (u*mp.sqrt(radius*radius-u*u)+radius*radius*mp.asin(u/radius))/2


def alpha_star():
    def primitive(t, c):
        return mp.sqrt(t*(t+c))-c*mp.asinh(mp.sqrt(t/c))

    def derivative(alpha):
        a, b = (1+alpha)/3, 1-alpha
        return (a/2+(primitive(b, 1+alpha)-primitive(a, 1+alpha))/2
                +(primitive(1, alpha)-primitive(b, alpha))/2
                -(mp.sqrt(2)-1)*mp.sqrt(b))

    return mp.findroot(derivative, (mp.mpf(1)/12, mp.mpf(1)/8))


def branch(alpha, lam):
    aa = 1+alpha
    ratio = lambda t: mp.sqrt(t/(aa+t))+mp.sqrt(t/(aa+lam-t))
    if ratio(lam) <= 1:
        return lam
    lo, hi = mp.mpf(0), lam
    for _ in range(210):
        mid = (lo+hi)/2
        if ratio(mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def continuum(alpha, lam):
    aa, b, a = 1+alpha, 1-alpha, (1+alpha)/3
    z = branch(alpha, lam)
    chord = lambda t: mp.sqrt((aa+t)*(aa+lam-t))
    chain = lambda t: mp.sqrt(t)*(mp.sqrt(aa+t)+mp.sqrt(aa+lam-t))
    full = lambda t: max(chord(t), chain(t))
    block_quad = mp.quad(full, sorted(set([mp.mpf(0), z, lam])))
    diag = lambda t, h: max(2*mp.sqrt(t*h), h)
    tail_quad = mp.quad(lambda t: diag(t, aa+t), sorted(set([lam, max(lam, a), b])))
    tail_quad += mp.quad(lambda t: diag(t, alpha+t), [b, 1])
    mm, cc = aa+lam/2, aa+lam
    block_formula = primitive_circle(z-lam/2, mm)-primitive_circle(-lam/2, mm)
    block_formula += primitive_f(lam, aa)-primitive_f(z, aa)
    block_formula += primitive_circle(lam-cc/2, cc/2)-primitive_circle(z-cc/2, cc/2)
    start = max(lam, a)
    tail_formula = 2*(primitive_f(b, aa)-primitive_f(start, aa)
                      +primitive_f(1, alpha)-primitive_f(b, alpha))
    if lam < a:
        tail_formula += aa*(a-lam)+(a*a-lam*lam)/2
    assert abs(block_quad-block_formula) < mp.mpf('1e-48')
    assert abs(tail_quad-tail_formula) < mp.mpf('1e-48')
    return (block_quad+tail_quad)/(4*mp.pi), z


def theta_asin(r, a, b):
    return 2*mp.asin(mp.sqrt(mp.mpf(a)*b/((r+a)*(r+b))))


def theta_atan(r, a, b):
    return 2*mp.atan(mp.sqrt(mp.mpf(a)*b/(r*(r+a+b))))


def score(r, pp, theta):
    return mp.fsum(max(theta(r, i, pp[i-2])+theta(r, i, pp[i-1]),
                       theta(r, pp[i-2], pp[i-1])) for i in range(1, len(pp)+1))


def geometry(pp, radius):
    radii, gaps = [], []
    for i in range(1, len(pp)+1):
        left = theta_atan(radius, i, pp[i-2])
        right = theta_atan(radius, i, pp[i-1])
        chord = theta_atan(radius, pp[i-2], pp[i-1])
        radii.extend([pp[i-2], i])
        gaps.extend([left, right+max(0, chord-left-right)])
    slack = 2*mp.pi-mp.fsum(gaps)
    assert slack > 0
    gaps[0] += slack
    angles = [mp.mpf(0)]
    for gap in gaps[:-1]:
        angles.append(angles[-1]+gap)
    points = [(radius+r)*mp.exp(1j*t) for r, t in zip(radii, angles)]
    count = 0
    for j in range(len(radii)):
        for k in range(j+1, len(radii)):
            delta = angles[k]-angles[j]
            required = theta_asin(radius, radii[j], radii[k])
            assert min(delta, 2*mp.pi-delta)-required >= -mp.mpf('1e-45')
            assert abs(points[k]-points[j])-radii[k]-radii[j] >= -mp.mpf('1e-40')
            count += 1
    return count


def diagnostics() -> None:
    mp.mp.dps = 60
    alpha = alpha_star()
    # Independently check the defining derivative using direct integration.
    a, b = (1+alpha)/3, 1-alpha
    residual = (a/2+mp.quad(lambda t: mp.sqrt(t/(t+1+alpha)), [a, b])/2
                +mp.quad(lambda t: mp.sqrt(t/(t+alpha)), [b, 1])/2
                -(mp.sqrt(2)-1)*mp.sqrt(b))
    assert abs(residual) < mp.mpf('1e-55')
    assert mp.mpf(1)/12 < alpha < mp.mpf(1)/2
    print('DIAGNOSTIC alpha_*='+mp.nstr(alpha, 32))
    values = []
    for lam in [mp.mpf(1)/4, mp.mpf(3)/10, mp.mpf(1)/2, mp.mpf(3)/4]:
        coefficient, z = continuum(alpha, lam)
        values.append(coefficient)
        print(f'DIAGNOSTIC lambda={mp.nstr(lam, 5)} z={mp.nstr(z, 20)} C={mp.nstr(coefficient, 32)}')
    assert values[1] < values[0]-mp.mpf(37)/(1830400*mp.pi)
    # At the boundary v_lambda(lambda)=1, the interval of chain cost vanishes.
    aa = 1+alpha
    boundary = mp.findroot(lambda l: mp.sqrt(l/(aa+l))+mp.sqrt(l/aa)-1, (.30, .35))
    left, _ = continuum(alpha, boundary-mp.mpf('1e-12'))
    right, _ = continuum(alpha, boundary+mp.mpf('1e-12'))
    assert abs(left-right) < mp.mpf('1e-10')
    print('PASS full cost: quadrature vs elementary primitives; both block/tail branches and switch boundary')
    total_pairs = 0
    for m in [2, 3, 7, 8, 9, 20, 64, 128, 256]:
        s, q = int(mp.floor(alpha*m)), 2*((3*m)//20)
        pp = order(m, s, q)
        # Recompute this bounded floor choice at twice the working precision.
        with mp.workdps(120):
            high_alpha = alpha_star()
            assert s == int(mp.floor(high_alpha*m))
            assert min(high_alpha*m-s, s+1-high_alpha*m) > mp.mpf('1e-20')
        lo, hi = mp.mpf(0), mp.mpf(m*m)
        assert score(hi, pp, theta_asin) < 2*mp.pi
        for _ in range(165):
            mid = (lo+hi)/2
            if score(mid, pp, theta_asin) > 2*mp.pi:
                lo = mid
            else:
                hi = mid
        root = (lo+hi)/2
        eps = mp.mpf('1e-35')*max(1, root)
        assert score(root-eps, pp, theta_atan) > 2*mp.pi
        assert score(root+eps, pp, theta_atan) < 2*mp.pi
        g = lambda t, x, y: max(mp.sqrt(t)*(mp.sqrt(x)+mp.sqrt(y)), mp.sqrt(x*y))
        empirical = mp.fsum(g(mp.mpf(i)/m, mp.mpf(pp[i-2])/m,
                             mp.mpf(pp[i-1])/m) for i in range(1, m+1))/m
        normalized = root/(4*m*m)
        cmin, cmax = 1/(8*mp.pi), 1/mp.pi
        if m >= 64:
            error = 1/(cmin*cmin*m)+1/(6*cmin**3*m*m)
            assert cmin < normalized < cmax
            assert abs(normalized-empirical/(4*mp.pi)) <= error/(2*mp.pi**2)
            assert abs(score(root, pp, theta_atan)-empirical/(2*normalized)) <= error
        if m <= 20:
            total_pairs += geometry(pp, root+eps)
        print(f'DIAGNOSTIC m={m} q={q} root/n^2={mp.nstr(normalized, 22)} empirical/(4pi)={mp.nstr(empirical/(4*mp.pi), 22)}')
    print(f'PASS roots: 9 full roots bracketed by independent atan scoring; {total_pairs} angular/Cartesian pairs')
    print('NOTE: 60/120-digit diagnostics are not interval certificates; all-m recovery and strict improvement are analytic.')


if __name__ == '__main__':
    rational_gates()
    occurrences()
    coordinates()
    moments()
    diagnostics()
