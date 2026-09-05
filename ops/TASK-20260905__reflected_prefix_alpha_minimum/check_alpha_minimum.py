"""Only the new alpha-minimum gates; no production or older-checker imports.

Exact mode uses stdlib Fraction, integer square roots and concavity bounds.
The accepted x_* bracket and its stationary minimum property are inputs.
Optional diagnostics independently integrate the original full-max cost.
No files are written, no finite global certificate is claimed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import isqrt


SCALE = 10**24
XL, XH = Q(719, 2500), Q(2877, 10000)
X0 = (XL+XH)/2
AL, AH, A107 = Q(1093, 10000), Q(10931, 100000), Q(107, 1000)


def sqrt_box(value):
    value = Q(value)
    if value < 0:
        raise ValueError('square root requires a nonnegative rational')
    k = isqrt(value.numerator*SCALE*SCALE//value.denominator)
    lo = Q(k, SCALE)
    hi = lo if lo*lo == value else Q(k+1, SCALE)
    assert 0 <= lo <= hi and lo*lo <= value <= hi*hi
    return lo, hi


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def concave_integral(fun, left, right, panels):
    """Trapezoid lower / midpoint upper; caller proves concavity."""
    if not (0 <= left <= right and isinstance(panels, int) and panels > 0):
        raise ValueError('invalid integration domain or panel count')
    if left == right:
        return Q(0), Q(0)
    width = (right-left)/panels
    nodes = [fun(left+i*width) for i in range(panels+1)]
    lower = width*(nodes[0][0]/2+sum(v[0] for v in nodes[1:-1])
                   +nodes[-1][0]/2)
    upper = width*sum(fun(left+(Q(i)+Q(1, 2))*width)[1]
                      for i in range(panels))
    assert lower <= upper
    return lower, upper


def switch_box(x):
    """64 sign-separated dyadic steps on the unsquared switch equation."""
    if not (XL <= x <= XH):
        raise ValueError('switch gate is restricted to the accepted x box')

    def v(t):
        return add(sqrt_box(t/(1+t)), sqrt_box(t/(1+x-t)))

    assert v(x)[0] > 1
    lo, hi = Q(0), x
    for _ in range(64):
        mid = (lo+hi)/2
        lower, upper = v(mid)
        if upper < 1:
            lo = mid
        elif lower > 1:
            hi = mid
        else:
            raise ArithmeticError('switch sign not separated')
    assert v(lo)[1] < 1 < v(hi)[0]
    assert 0 < lo < hi < x and hi-lo == x/2**64
    return lo, hi


def e_boxes():
    zl, zh = switch_box(X0)
    chord = concave_integral(
        lambda u: sqrt_box((1+u)*(1+X0-u)), Q(0), zl, 2048)
    chain = concave_integral(
        lambda u: add(sqrt_box(u*(1+u)), sqrt_box(u*(1+X0-u))),
        zh, X0, 2048)
    # On the omitted switch interval 0 <= max(chord,chain) <= 4.
    base = X0+X0*X0/2
    point = (chord[0]+chain[0]-base,
             chord[1]+chain[1]+4*(zh-zl)-base)
    # Taylor about the accepted stationary minimum: E''<3 on (tau,1/3).
    displacement = Q(3, 2)*((XH-XL)/2)**2
    assert displacement == Q(3, 800000000)
    return point, (point[0]-displacement, point[1])


def d_box(alpha):
    if not (0 < alpha < Q(1, 2)):
        raise ValueError('D quadrature gate requires 0<alpha<1/2')
    a, b = (1+alpha)/3, 1-alpha
    first = concave_integral(
        lambda t: sqrt_box(t/(t+1+alpha)), a, b, 256)
    second = concave_integral(
        lambda t: sqrt_box(t/(t+alpha)), b, Q(1), 256)
    r2, rb = sqrt_box(2), sqrt_box(b)
    assert r2[0] > 1
    return (a/2+(first[0]+second[0])/2-(r2[1]-1)*rb[1],
            a/2+(first[1]+second[1])/2-(r2[0]-1)*rb[0])


def outward(box):
    scale = 10**12
    return f'[{box[0]*scale//1},{-((-box[1]*scale)//1)}]/{scale}'


def recovery_audit():
    count, cases = 0, set()
    for alpha in (Q(0), AL, AH, Q(1, 2)):
        for x in (XL, XH):
            lam = (1+alpha)*x
            for m in range(2, 17):
                s, q = (alpha*m)//1, 2*((lam*m/2)//1)
                r, beta, length = m-s, Q(s, m), Q(q, m)
                ranks = [q+2-i if i <= q and i % 2 == 0 else i
                         for i in range(1, m+1)]
                p = [m+1+(j+s-1) % m for j in ranks]
                # Independent list operation: reverse even slots of the shift.
                expected = list(range(m+s+1, 2*m+1))+list(range(m+1, m+s+1))
                expected[1:q:2] = reversed(expected[1:q:2])
                assert p == expected and sorted(p) == list(range(m+1, 2*m+1))
                assert q % 2 == 0 and s+q < m and r >= q+1
                exc = {1, r, r+1}
                if q:
                    exc.add(q+1)
                exc &= set(range(1, m+1))
                assert len(exc) <= 4
                assert p[-1] == (m+s if s else 2*m)
                assert p[0] == m+s+1
                if q:
                    assert (p[q-1], p[q]) == (m+s+2, m+s+q+1)
                if s:
                    assert (p[r-1], p[r]) == (2*m, m+1)
                for i in range(1, m+1):
                    if i in exc:
                        continue
                    t = Q(i, m)
                    actual = (Q(p[i-2], m), Q(p[i-1], m))
                    if i <= q:
                        if i % 2 == 0:
                            exact = (1+beta+t-Q(1, m), 1+beta+length-t+Q(2, m))
                            target = (1+alpha+t, 1+alpha+lam-t)
                        else:
                            exact = (1+beta+length-t+Q(3, m), 1+beta+t)
                            target = (1+alpha+lam-t, 1+alpha+t)
                    else:
                        offset = 1 if i < r else 0
                        exact = (offset+beta+t-Q(1, m), offset+beta+t)
                        target = (offset+alpha+t, offset+alpha+t)
                        assert (t < 1-alpha) == (i < r)
                    assert actual == exact
                    assert max(abs(a-b) for a, b in zip(actual, target)) <= Q(3, m)
                if m >= 15:
                    assert q >= 2 and r >= q+2
                cases.add((q == 0, r == 1, r == q+1, s == 0))
                count += 1
    assert (True, True, True, False) in cases  # m=2, alpha=1/2
    assert any(not no_block and coincident for no_block, _, coincident, _ in cases)
    print(f'PASS recovery: {count} exact cases, m=2..16; endpoint shifts, coincident seams, cyclic predecessors and 3/m errors')


def exact_gates():
    assert Q(1, 4) < XL < XH < Q(1, 3)
    assert sqrt_box(XL/(1+XL))[0]+sqrt_box(XL)[0] > 1  # XL>tau
    assert Q(1, 2)-Q(3, 2)*XH == Q(1369, 20000) > Q(1, 15)
    assert Q(7, 5)**2 < 2 < Q(10, 7)**2
    assert Q(7, 4)**2 > 3
    curvature = Q(7, 60)-Q(1, 324)
    assert curvature == Q(46, 405) > Q(1, 9)
    assert Q(5, 6)-Q(7, 10)-Q(13, 83) == Q(-29, 1245) < 0
    assert Q(5, 4)*Q(7, 10)-Q(3, 4)-Q(3, 2)/324 == Q(13, 108) > 0
    assert Q(8, 3)-1+Q(1, 3)+Q(1, 8) == Q(17, 8) < 3
    print('PASS analytic rational gates: wrap gap>1/15; Fsecond>46/405>1/9; Fprime(0)<-29/1245; Fprime(1/2)>13/108; Esecond<3')
    point, estar = e_boxes()
    print(f'EXACT E({X0}) in {outward(point)}')
    print(f'EXACT E(x_*) in {outward(estar)}')
    assert Q(-84428, 10**8) < estar[0] <= estar[1] < Q(-84426, 10**8)
    ds, fs = [], []
    for alpha in (AL, AH):
        d = d_box(alpha)
        f = (d[0]+(1+alpha)*estar[0], d[1]+(1+alpha)*estar[1])
        ds.append(d)
        fs.append(f)
        print(f'EXACT D({alpha}) in {outward(d)}')
        print(f'EXACT Fprime({alpha}) in {outward(f)}')
    assert Q(-3, 2000000) < fs[0][0] <= fs[0][1] < Q(-1, 1000000)
    assert Q(2, 1000000) < fs[1][0] <= fs[1][1] < Q(5, 2000000)
    assert A107 < AL < AH < Q(1, 2)
    # Strong convexity followed by pi<22/7 (accepted exact integral proof).
    gap = (AL-A107)**2/(36*Q(22, 7))
    assert gap == Q(3703, 79200000000) > Q(1, 22000000)
    assert Q(14191368, 10**8)-Q(1, 22000000) < Q(14191364, 10**8)
    print('PASS isolation/comparison: 1093/10000<alpha_hat<10931/100000; C_107-C_hat>1/22000000; C_hat<14191364/100000000')
    for invalid in (lambda: sqrt_box(-1), lambda: d_box(0),
                    lambda: switch_box(Q(0)),
                    lambda: concave_integral(sqrt_box, Q(1), Q(0), 1)):
        try:
            invalid()
        except ValueError:
            pass
        else:
            raise AssertionError('invalid gate input accepted')
    recovery_audit()
    return point, estar, ds, fs


def diagnostics(boxes):
    import mpmath as mp

    mp.mp.dps = 70

    def val(q):
        return mp.mpf(q.numerator)/q.denominator

    def inside(value, box):
        assert val(box[0]) < value < val(box[1])

    def z(x):
        return mp.findroot(lambda t: mp.sqrt(t/(1+t))+mp.sqrt(t/(1+x-t))-1,
                           (mp.mpf('0.27'), mp.mpf('0.29')))

    def phi(x):
        zz = z(x)
        return (mp.sqrt(x)*(mp.sqrt(1+x)+1)-(1+x)
                +(mp.quad(lambda t: mp.sqrt((1+t)/(1+x-t)), [0, zz])
                  +mp.quad(lambda t: mp.sqrt(t/(1+x-t)), [zz, x]))/2)

    def e(x):
        zz = z(x)
        return (mp.quad(lambda t: mp.sqrt((1+t)*(1+x-t))-(1+t), [0, zz])
                +mp.quad(lambda t: mp.sqrt(t)*(mp.sqrt(1+t)+mp.sqrt(1+x-t))-(1+t), [zz, x]))

    def d(alpha):
        a, b = (1+alpha)/3, 1-alpha
        return (a/2+(mp.quad(lambda t: mp.sqrt(t/(t+1+alpha)), [a, b])
                     +mp.quad(lambda t: mp.sqrt(t/(t+alpha)), [b, 1]))/2
                -(mp.sqrt(2)-1)*mp.sqrt(b))

    x = mp.findroot(phi, (val(XL), val(XH)))
    ev = e(x)
    root = mp.findroot(lambda alpha: d(alpha)+(1+alpha)*ev, (val(AL), val(AH)))
    point, estar, ds, fs = boxes
    inside(e(val(X0)), point)
    inside(ev, estar)
    for alpha, db, fb in zip((AL, AH), ds, fs):
        inside(d(val(alpha)), db)
        inside(d(val(alpha))+(1+val(alpha))*ev, fb)
    assert val(AL) < root < val(AH) and val(XL) < x < val(XH)

    def original_cost(alpha):
        aa, b = 1+alpha, 1-alpha
        lam, zz, a = aa*x, aa*z(x), aa/3
        block = (mp.quad(lambda t: mp.sqrt((aa+t)*(aa+lam-t)), [0, zz])
                 +mp.quad(lambda t: mp.sqrt(t)*(mp.sqrt(aa+t)+mp.sqrt(aa+lam-t)), [zz, lam]))
        tail = (mp.quad(lambda t: aa+t, [lam, a])
                +2*mp.quad(lambda t: mp.sqrt(t*(aa+t)), [a, b])
                +2*mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [b, 1]))
        kval = (mp.quad(lambda t: (aa+t)/2, [0, a])
                +mp.quad(lambda t: mp.sqrt(t*(aa+t)), [a, b])
                +mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [b, 1]))
        assert abs((block+tail)-(2*kval+aa*aa*ev)) < mp.mpf('1e-60')
        return (block+tail)/(4*mp.pi)

    costs = [original_cost(a) for a in (mp.mpf(0), val(A107), root, mp.mpf(1)/2)]
    assert costs[2] < min(costs[0], costs[1], costs[3])
    assert costs[1]-costs[2] > val(Q(1, 22000000))
    print('PASS independent 70-digit diagnostics: E and both D/Fprime enclosures; four original full-max cost identities including alpha=0,1/2')
    for name, value in (('alpha_hat', root), ('E(x_*)', ev), ('C_hat', costs[2]),
                        ('C_107-C_hat', costs[1]-costs[2])):
        print(f'NUMERICAL {name} = {mp.nstr(value, 38)}')
    print('NOTE: numerical observations only; imported full-feasibility/root theorems are not re-certified here.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only', action='store_true')
    args = parser.parse_args()
    gates = exact_gates()
    if not args.exact_only:
        diagnostics(gates)
