"""Bounded gates for alpha variation with the accepted x_* kept fixed.

Exact mode uses Fraction, integer square roots and concave quadrature
enclosures, with no transcendental library. Diagnostics use canonical
mpmath at 70 digits and the original unnormalized full-max integrals.
No production, verifier or older-checker imports; no files are written.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import isqrt


SCALE = 10**20
PANELS = 128
AL = Q(53, 500)
AB = Q(267, 2500)
AR = Q(107, 1000)
XL = Q(719, 2500)
XH = Q(2877, 10000)


def sqrt_box(value):
    """Exact outward endpoints; verify both squared inequalities each time."""
    value = Q(value)
    if value < 0:
        raise ValueError('square root requires a nonnegative rational')
    root = isqrt(value.numerator*SCALE*SCALE//value.denominator)
    lo = Q(root, SCALE)
    hi = lo if lo*lo == value else Q(root+1, SCALE)
    assert 0 <= lo <= hi and lo*lo <= value <= hi*hi
    assert hi-lo <= Q(1, SCALE)
    return lo, hi


def concave_integral(c, left, right):
    """Trap lower, midpoint upper for f_c(t)=sqrt(t/(t+c))."""
    if not (c > 0 and 0 < left <= right):
        raise ValueError('requires c>0 and 0<left<=right')
    width = (right-left)/PANELS
    nodes = [sqrt_box(t/(t+c))
             for t in (left+i*width for i in range(PANELS+1))]
    lower = width*(nodes[0][0]/2+sum(v[0] for v in nodes[1:-1])
                   +nodes[-1][0]/2)
    mids = [left+(Q(i)+Q(1, 2))*width for i in range(PANELS)]
    upper = width*sum(sqrt_box(t/(t+c))[1] for t in mids)
    assert lower <= upper
    return lower, upper


def d_box(alpha):
    """D=K', including the jump of the moving high wrap."""
    if not (0 < alpha < Q(1, 2)):
        raise ValueError('this gate is restricted to 0<alpha<1/2')
    a, b = (1+alpha)/3, 1-alpha
    first = concave_integral(1+alpha, a, b)
    second = concave_integral(alpha, b, Q(1))
    r2, rb = sqrt_box(2), sqrt_box(b)
    assert r2[0] > 1
    return (a/2+(first[0]+second[0])/2-(r2[1]-1)*rb[1],
            a/2+(first[1]+second[1])/2-(r2[0]-1)*rb[0])


def short(box, places=12):
    """Integer endpoints on an outward decimal grid, without floats."""
    scale = 10**places
    lo, hi = box
    return f'[{lo*scale//1},{-((-hi*scale)//1)}]/{scale}'


def permutation(m, alpha, x):
    if not (isinstance(m, int) and m >= 2 and AL <= alpha <= AR
            and XL <= x <= XH):
        raise ValueError('outside the bounded audit domain')
    lam = (1+alpha)*x
    s, q = (alpha*m)//1, 2*((lam*m/2)//1)
    ranks = [q+2-i if i <= q and i % 2 == 0 else i
             for i in range(1, m+1)]
    p = [m+1+((j+s-1) % m) for j in ranks]
    return p, s, q


def recovery_audit():
    count = 0
    branches = set()
    for alpha in (AL, (AL+AR)/2, AR):
        for x in (XL, (XL+XH)/2, XH):
            lam, aa, b = (1+alpha)*x, 1+alpha, 1-alpha
            for m in range(2, 129):
                p, s, q = permutation(m, alpha, x)
                r, beta, length = m-s, Q(s, m), Q(q, m)
                assert s+q < m and r >= q+2 and q % 2 == 0
                assert sorted(p) == list(range(m+1, 2*m+1))
                # Independent construction: reverse only the even slots
                # of a shifted list, instead of using the rank involution.
                original = list(range(m+s+1, 2*m+1))+list(range(m+1, m+s+1))
                expected = original[:]
                expected[1:q:2] = reversed(original[1:q:2])
                assert p == expected
                exceptional = {1, r, r+1}
                if q:
                    exceptional.add(q+1)
                exceptional &= set(range(1, m+1))
                expected_size = (4 if s else 3) if q else (3 if s else 2)
                assert len(exceptional) == expected_size
                branches.add((min(q, 4), bool(s)))
                assert p[-1] == (m+s if s else 2*m)
                assert p[0] == m+s+1
                if q:
                    assert (p[q-1], p[q]) == (m+s+2, m+s+q+1)
                if s:
                    assert (p[r-1], p[r]) == (2*m, m+1)
                for i in range(1, m+1):
                    t = Q(i, m)
                    actual = (Q(p[i-2], m), Q(p[i-1], m))
                    if i in exceptional:
                        continue
                    if i <= q:
                        if i % 2 == 0:
                            exact = (1+beta+t-Q(1, m),
                                     1+beta+length-t+Q(2, m))
                            target = (aa+t, aa+lam-t)
                        else:
                            exact = (1+beta+length-t+Q(3, m), 1+beta+t)
                            target = (aa+lam-t, aa+t)
                    else:
                        offset = 1 if i < r else 0
                        exact = (offset+beta+t-Q(1, m), offset+beta+t)
                        target = (offset+alpha+t, offset+alpha+t)
                        assert (t < b) == (i < r)
                    assert actual == exact
                    assert max(abs(a-e) for a, e in zip(actual, target)) <= Q(3, m)
                if m >= 8:
                    assert q >= 2
                    # Nonlinear continuous test: F(t,u,v)=u*v.
                    moment = sum(Q(p[i-1]*p[i], m*m) for i in range(m))/m
                    limit = (aa*aa*lam+aa*lam*lam+lam**3/6
                             +((aa+b)**3-(aa+lam)**3)/3
                             +((alpha+1)**3-(alpha+b)**3)/3)
                    assert abs(moment-limit) <= Q(88, m)
                count += 1
    assert {(0, False), (2, False), (2, True), (4, True)} <= branches
    print(f'PASS recovery audit: {count} rational cases, m=2..128; occurrence, cyclic predecessors, all seams, 3/m errors and nonlinear moment bound')


def exact_gates():
    # The accepted theorem supplies XL<x_*<XH and tau<x_*<1/3.
    # Domain inequalities below also hold on this enclosing x box.
    assert 0 < AL < AB < AR < Q(1, 2)
    assert Q(1, 4) < XL < XH < Q(1, 3)
    assert Q(1, 4) < (1+AL)*XL
    assert (1+AR)/3 < 1-AR
    assert (1-AR)-(1+AR)/3 == Q(131, 250) > Q(1, 2)
    print('PASS domain: I=[53/500,107/1000]; 1/4<lambda<A/3<b; b-lambda>131/250; r>=q+2 for every m>=2')

    boxes = [d_box(alpha) for alpha in (AL, AB, AR)]
    for alpha, box in zip((AL, AB, AR), boxes):
        print(f'EXACT D({alpha}) in {short(box)}')
    assert Q(-3, 10000) < boxes[0][0] <= boxes[0][1] < Q(-1, 5000)
    assert 0 < boxes[1][0] <= boxes[1][1] < Q(1, 100000)
    assert Q(7, 100000) < boxes[2][0] <= boxes[2][1] < Q(9, 100000)
    print('PASS alpha isolation: 53/500<alpha_*<267/2500<107/1000; D(107/1000)<9/100000')

    # Chord saving at x=1/4; strictness is the positive-measure argument
    # in the note, and E(x_*)<E(1/4) is imported from the accepted theorem.
    assert Q(1, 4)**3/(24*(1+Q(1, 8))) == Q(1, 1728)
    # Positive integral proving pi<22/7, with exact polynomial division.
    quotient = [Q(4), Q(0), Q(-4), Q(0), Q(5), Q(-4), Q(1)]
    product = [Q(0)]*9
    for i, value in enumerate(quotient):
        product[i] += value
        product[i+2] += value
    product[0] -= 4
    assert product == [0, 0, 0, 0, 1, -4, 6, -4, 1]
    assert sum(v/Q(i+1) for i, v in enumerate(quotient)) == Q(22, 7)
    numerator = Q(9, 100000)-(1+AL)/1728
    assert numerator < -2*Q(22, 7)/12000
    assert AR-AB == Q(1, 5000)
    assert (AR-AB)/12000 == Q(1, 60000000)
    assert Q(14191369, 10**8)-Q(1, 60000000) < Q(14191368, 10**8)
    print('PASS exact comparisons: E(x_*)<-1/1728; C_alpha derivative<-1/12000 on I; C_rp-C_107>1/60000000; C_107<14191368/100000000')
    # Domain checks are part of this proof gate's contract.
    for operation in (lambda: sqrt_box(-1), lambda: d_box(0),
                      lambda: concave_integral(Q(0), Q(1), Q(2)),
                      lambda: permutation(1, AR, XL)):
        try:
            operation()
        except ValueError:
            pass
        else:
            raise AssertionError('invalid gate input was accepted')
    recovery_audit()
    return boxes


def diagnostics(boxes):
    import mpmath as mp

    mp.mp.dps = 70

    def mpq(q):
        return mp.mpf(q.numerator)/q.denominator

    def switch(x):
        return mp.findroot(lambda z: mp.sqrt(z/(1+z))
                           +mp.sqrt(z/(1+x-z))-1, (x*mp.mpf('.9'), x))

    def excess(x):
        z = switch(x)
        chord = mp.quad(lambda u: mp.sqrt((1+u)*(1+x-u)), [0, z])
        chain = mp.quad(lambda u: mp.sqrt(u)*(mp.sqrt(1+u)
                                               +mp.sqrt(1+x-u)), [z, x])
        return chord+chain-x-x*x/2

    def phi(x):
        z = switch(x)
        return (mp.sqrt(x)*(mp.sqrt(1+x)+1)-(1+x)
                +(mp.quad(lambda u: mp.sqrt((1+u)/(1+x-u)), [0, z])
                  +mp.quad(lambda u: mp.sqrt(u/(1+x-u)), [z, x]))/2)

    def derivative(alpha):
        a, b = (1+alpha)/3, 1-alpha
        return (a/2+mp.quad(lambda t: mp.sqrt(t/(t+1+alpha)), [a, b])/2
                +mp.quad(lambda t: mp.sqrt(t/(t+alpha)), [b, 1])/2
                -(mp.sqrt(2)-1)*mp.sqrt(b))

    def shift_cost(alpha):
        a, b, aa = (1+alpha)/3, 1-alpha, 1+alpha
        return (mp.quad(lambda t: (aa+t)/2, [0, a])
                +mp.quad(lambda t: mp.sqrt(t*(aa+t)), [a, b])
                +mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [b, 1]))

    xs = mp.findroot(phi, (mpq(XL), mpq(XH)))
    astar = mp.findroot(derivative, (mpq(AL), mpq(AB)))
    e = excess(xs)
    assert mpq(XL) < xs < mpq(XH) and mpq(AL) < astar < mpq(AB)
    assert e < -mp.mpf(1)/1728

    def original_cost(alpha):
        aa, b = 1+alpha, 1-alpha
        lam, a = aa*xs, aa/3
        z = mp.findroot(lambda t: mp.sqrt(t/(aa+t))
                       +mp.sqrt(t/(aa+lam-t))-1, (lam*mp.mpf('.9'), lam))
        block = (mp.quad(lambda t: mp.sqrt((aa+t)*(aa+lam-t)), [0, z])
                 +mp.quad(lambda t: mp.sqrt(t)*(mp.sqrt(aa+t)
                                                +mp.sqrt(aa+lam-t)), [z, lam]))
        tail = (mp.quad(lambda t: aa+t, [lam, a])
                +2*mp.quad(lambda t: mp.sqrt(t*(aa+t)), [a, b])
                +2*mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [b, 1]))
        return (block+tail)/(4*mp.pi)

    for alpha, box in zip((AL, AB, AR), boxes):
        value = derivative(mpq(alpha))
        assert mpq(box[0]) < value < mpq(box[1])
    step = mp.mpf('1e-18')
    errors = []
    for alpha in (mpq(AL), astar, mpq(AR)):
        value = original_cost(alpha)
        formula = shift_cost(alpha)/(2*mp.pi)+(1+alpha)**2*e/(4*mp.pi)
        assert abs(value-formula) < mp.mpf('1e-60')
        slope = (original_cost(alpha+step)-original_cost(alpha-step))/(2*step)
        target = (derivative(alpha)+(1+alpha)*e)/(2*mp.pi)
        errors.append(abs(slope-target))
        assert errors[-1] < mp.mpf('1e-32') and slope < -mp.mpf(1)/12000
    assert abs((excess(xs+step)-excess(xs-step))/(2*step)) < mp.mpf('1e-32')
    crp, c107 = original_cost(astar), original_cost(mpq(AR))
    assert crp-c107 > mp.mpf(1)/60000000
    print('PASS independent 70-digit quadrature: three D enclosures, three original full-max cost identities and alpha derivatives; fixed x_* stationarity')
    print('NUMERICAL x_* =', mp.nstr(xs, 38))
    print('NUMERICAL alpha_* =', mp.nstr(astar, 38))
    print('NUMERICAL derivative at alpha_* =', mp.nstr((1+astar)*e/(2*mp.pi), 38))
    print('NUMERICAL lambda(107/1000) =', mp.nstr((1+mpq(AR))*xs, 38))
    print('NUMERICAL C_107 =', mp.nstr(c107, 38))
    print('NUMERICAL C_rp-C_107 =', mp.nstr(crp-c107, 38))

    def theta(radius, a, b):
        return 2*mp.asin(mp.sqrt(a*b/((radius+a)*(radius+b))))

    pairs = 0
    for m in (2, 3, 7, 8, 10, 16, 32, 64):
        # Accepted rational x bracket fixes these exact floors. No decimal
        # is used to select the finite theorem's order.
        low_order = permutation(m, AR, XL)
        high_order = permutation(m, AR, XH)
        assert low_order == high_order
        p, _, _ = low_order

        def score(radius):
            return sum(max(theta(radius, i+1, p[i-1])+theta(radius, i+1, p[i]),
                           theta(radius, p[i-1], p[i])) for i in range(m))

        lo, hi = mp.mpf(0), mp.mpf(4*m*m)
        assert score(hi) < 2*mp.pi
        for _ in range(190):
            mid = (lo+hi)/2
            if score(mid) > 2*mp.pi:
                lo = mid
            else:
                hi = mid
        root = (lo+hi)/2
        eta = root*mp.mpf('1e-35')
        assert score(root-eta) > 2*mp.pi > score(root+eta)
        radius = root+eta
        left, right = [], []
        for i in range(m):
            a, b = theta(radius, i+1, p[i-1]), theta(radius, i+1, p[i])
            c = theta(radius, p[i-1], p[i])
            left.append(a)
            right.append(b+max(0, c-a-b))
        left[0] += 2*mp.pi-sum(left)-sum(right)
        radii, angles, angle = [], [], mp.mpf(0)
        for i in range(m):
            radii += [i+1, p[i]]
            angles.append(angle)
            angle += right[i]
            angles.append(angle)
            angle += left[(i+1) % m]
        assert abs(angle-2*mp.pi) < mp.mpf('1e-60')
        xy = [((radius+r)*mp.cos(t), (radius+r)*mp.sin(t))
              for r, t in zip(radii, angles)]
        for i in range(2*m):
            for j in range(i+1, 2*m):
                separation = angles[j]-angles[i]
                need = theta(radius, radii[i], radii[j])
                assert min(separation, 2*mp.pi-separation)-need > -mp.mpf('1e-45')
                distance2 = sum((xy[i][k]-xy[j][k])**2 for k in (0, 1))
                assert distance2-(radii[i]+radii[j])**2 > -mp.mpf('1e-40')
                pairs += 1
        if m in (16, 64):
            print(f'NUMERICAL m={m} full radius/(2m)^2 = {mp.nstr(root/(4*m*m), 24)}')
    print(f'PASS finite witness diagnostics: 8 sizes, exact bracket-determined floors, +/-relative 1e-35 root signs, {pairs} all-pairs angular and Cartesian checks')
    print('NOTE: diagnostics are numerical observations, not finite global certificates or proof of an asymptotic limit.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only', action='store_true',
                        help='run only the standard-library exact rational checks')
    args = parser.parse_args()
    exact_boxes = exact_gates()
    if not args.exact_only:
        diagnostics(exact_boxes)
