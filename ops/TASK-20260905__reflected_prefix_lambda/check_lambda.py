"""Exact rational gates and independent diagnostics for fixed-alpha lambda variation.

Exact mode: standard-library integer intervals, 50 decimal places, outward
rounding after every operation, 64-term series, 100-step switch isolation.
Diagnostics: canonical mpmath at 70 digits; never used by the exact gates.
No production, verifier or preceding-checker imports; no files are written.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import isqrt


SCALE = 10**50
TERMS = 64
BISECTIONS = 100


def ceildiv(a: int, b: int) -> int:
    return -((-a)//b)


class I:
    """Closed [lo/SCALE, hi/SCALE]; construction accepts exact rationals only."""

    def __init__(self, value=0):
        if not isinstance(value, (int, Q)):
            raise TypeError('integer or Fraction required')
        q = Q(value)
        self.lo = q.numerator*SCALE//q.denominator
        self.hi = ceildiv(q.numerator*SCALE, q.denominator)

    @classmethod
    def raw(cls, lo: int, hi: int):
        if lo > hi:
            raise ValueError('reversed interval')
        result = cls.__new__(cls)
        result.lo, result.hi = lo, hi
        return result

    @classmethod
    def box(cls, lo: Q, hi: Q):
        if lo > hi:
            raise ValueError('reversed rational box')
        return cls.raw(cls(lo).lo, cls(hi).hi)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, I) else I(other)

    def __add__(self, other):
        other = self.coerce(other)
        return I.raw(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I.raw(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I.raw(min(products)//SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError('division by an interval containing zero')
        pairs = [(a*SCALE, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return I.raw(min(a//b for a, b in pairs),
                     max(ceildiv(a, b) for a, b in pairs))

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError('nonnegative integer power required')
        answer, factor = I(1), self
        while n:
            if n % 2:
                answer = answer*factor
            factor = factor*factor
            n //= 2
        return answer

    def sqrt(self):
        if self.lo < 0:
            raise ValueError('sqrt requires a nonnegative interval')
        lo, hi = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        return I.raw(lo, hi+(hi*hi != self.hi*SCALE))

    def widen(self, error):
        if error.lo < 0:
            raise ValueError('nonnegative error bound required')
        return I.raw(self.lo-error.hi, self.hi+error.hi)

    def inside(self, lo: Q, hi: Q):
        assert lo < Q(self.lo, SCALE) <= Q(self.hi, SCALE) < hi

    def short(self, places=12):
        """Outward integer decimal grid, with explicit scale (no float)."""
        scale = 10**places
        return f'[{self.lo*scale//SCALE},{ceildiv(self.hi*scale, SCALE)}]/{scale}'


def sqrt(x):
    return I.coerce(x).sqrt()


def atan(x):
    x = I.coerce(x)
    # Principal real atan(x)=4 atan(q), with two half-angle reductions.
    for _ in range(2):
        x = x/(1+sqrt(1+x*x))
    q = I(Q(max(abs(x.lo), abs(x.hi)), SCALE))
    assert q.hi < SCALE
    total, power, square = I(0), x, x*x
    for k in range(TERMS):
        total += power*(1 if k % 2 == 0 else -1)/(2*k+1)
        power *= square
    error = q**(2*TERMS+1)/(2*TERMS+1)
    return 4*total.widen(error)


def log(x):
    x = I.coerce(x)
    if x.lo <= 0:
        raise ValueError('positive logarithm argument required')
    # log(x)=4 log(x**(1/4)); artanh series with geometric tail.
    fourth = sqrt(sqrt(x))
    y = (fourth-1)/(fourth+1)
    q = I(Q(max(abs(y.lo), abs(y.hi)), SCALE))
    assert q.hi < SCALE
    total, power, square = I(0), y, y*y
    for k in range(TERMS):
        total += power/(2*k+1)
        power *= square
    error = 2*q**(2*TERMS+1)/((2*TERMS+1)*(1-q*q))
    return 4*(2*total).widen(error)


def asinh_sqrt_ratio(t, c):
    return log((sqrt(t)+sqrt(t+c))/sqrt(c))


def primitive_f(t, c):
    """Integral of sqrt(t*(t+c))."""
    return ((2*t+c)*sqrt(t*(t+c))-c*c*asinh_sqrt_ratio(t, c))/4


def primitive_h(c, w):
    """Integral of sqrt(w/(c-w)), 0<w<c."""
    return c*atan(sqrt(w/(c-w)))-sqrt(w*(c-w))


def primitive_circle(v, radius):
    root = sqrt(radius*radius-v*v)
    return (v*root+radius*radius*atan(v/root))/2


def shift_derivative(alpha):
    a, b = (1+alpha)/3, 1-alpha

    def primitive(t, c):
        return sqrt(t*(t+c))-c*asinh_sqrt_ratio(t, c)

    return (a/2+(primitive(b, 1+alpha)-primitive(a, 1+alpha)
                 +primitive(I(1), alpha)-primitive(b, alpha))/2
            -(sqrt(2)-1)*sqrt(b))


def switch_ratio(u, x):
    return sqrt(u/(1+u))+sqrt(u/(1+x-u))-1


def switch_point(x: Q):
    """Enclose z(x), retaining the all-chord case; fixed 100 bisections."""
    endpoint = switch_ratio(I(x), I(x))
    if endpoint.hi < 0:
        return I(x)
    assert endpoint.lo > 0, 'endpoint branch must be separated'
    lo, hi = Q(0), x
    for _ in range(BISECTIONS):
        mid = (lo+hi)/2
        value = switch_ratio(I(mid), I(x))
        if value.hi < 0:
            lo = mid
        elif value.lo > 0:
            hi = mid
        else:
            raise AssertionError('insufficient precision in fixed bisection')
    return I.box(lo, hi)


def switch_box(x):
    """z is increasing in x, also through the chord endpoint transition."""
    low = switch_point(Q(x.lo, SCALE))
    high = switch_point(Q(x.hi, SCALE))
    return I.raw(low.lo, high.hi)


def slope(x):
    """Phi(x)=E'(x) in the switched regime, from exact primitives."""
    assert switch_ratio(I(Q(x.lo, SCALE)), I(Q(x.lo, SCALE))).lo > 0
    z = switch_box(x)
    i1 = primitive_h(2+x, 1+z)-primitive_h(2+x, I(1))
    i2 = primitive_h(1+x, x)-primitive_h(1+x, z)
    if Q(x.hi, SCALE) <= Q(1, 3):
        diag = 1+x
    elif Q(x.lo, SCALE) >= Q(1, 3):
        diag = 2*sqrt(x*(1+x))
    else:
        # The two continuous diagonal branches agree at 1/3; a hull is safe.
        chord, chain = 1+x, 2*sqrt(x*(1+x))
        diag = I.raw(min(chord.lo, chain.lo), max(chord.hi, chain.hi))
    return sqrt(x)*(sqrt(1+x)+1)-diag+(i1+i2)/2


def excess(x):
    """E on the auxiliary 0<x<=1 domain, not a wrap-crossing construction."""
    z = switch_box(x)
    radius = 1+x/2
    block = (primitive_circle(z-x/2, radius)
             -primitive_circle(-x/2, radius))
    endpoint = switch_ratio(I(Q(x.hi, SCALE)), I(Q(x.hi, SCALE)))
    if endpoint.hi >= 0:
        assert switch_ratio(I(Q(x.lo, SCALE)), I(Q(x.lo, SCALE))).lo > 0
        c = 1+x
        block += (primitive_f(x, I(1))-primitive_f(z, I(1))
                  +primitive_circle(x-c/2, c/2)
                  -primitive_circle(z-c/2, c/2))
    if Q(x.hi, SCALE) <= Q(1, 3):
        diagonal = x+x*x/2
    elif Q(x.lo, SCALE) >= Q(1, 3):
        diagonal = I(Q(7, 18))+2*(primitive_f(x, I(1))
                                         -primitive_f(I(Q(1, 3)), I(1)))
    else:
        raise ValueError('cost gate must not straddle the tail switch')
    return block-diagonal


def coefficient(alpha, lam, pi):
    aa, b = 1+alpha, 1-alpha
    k = (primitive_f(b, aa)+primitive_f(I(1), alpha)-primitive_f(b, alpha)
         +(log(3)/8-I(Q(1, 12)))*aa*aa)
    return (2*k+aa*aa*excess(lam/aa))/(4*pi)


def arithmetic_audit():
    count = 0
    grid = [Q(n, d) for n in range(-4, 5) for d in (1, 3, 7)]
    for a in grid:
        for b in grid:
            for result, exact in [(I(a)+I(b), a+b), (I(a)-I(b), a-b),
                                  (I(a)*I(b), a*b)]:
                assert Q(result.lo, SCALE) <= exact <= Q(result.hi, SCALE)
                count += 1
            if b:
                result = I(a)/I(b)
                assert Q(result.lo, SCALE) <= a/b <= Q(result.hi, SCALE)
                count += 1
    for a in grid:
        if a >= 0:
            root = sqrt(a)
            assert Q(root.lo, SCALE)**2 <= a <= Q(root.hi, SCALE)**2
    boxes = [(Q(-2), Q(-1, 3)), (Q(-1, 7), Q(2, 3)), (Q(1, 3), Q(7, 3))]
    box_count = 0
    for a0, a1 in boxes:
        for b0, b1 in boxes:
            left, right = I.box(a0, a1), I.box(b0, b1)
            operations = [(left+right, lambda a, b: a+b),
                          (left-right, lambda a, b: a-b),
                          (left*right, lambda a, b: a*b)]
            if b0*b1 > 0:
                operations.append((left/right, lambda a, b: a/b))
            for enclosure, oracle in operations:
                for a in (a0, (a0+a1)/2, a1):
                    for b in (b0, (b0+b1)/2, b1):
                        assert Q(enclosure.lo, SCALE) <= oracle(a, b) <= Q(enclosure.hi, SCALE)
                        box_count += 1
    for operation in [lambda: I(0.1), lambda: I.box(Q(1), Q(0)),
                      lambda: I(1)/I.box(Q(-1), Q(1)),
                      lambda: sqrt(-1), lambda: log(0), lambda: I(2)**-1]:
        try:
            operation()
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError('malformed interval operation accepted')
    print(f'PASS interval arithmetic: {count} point and {box_count} box Fraction oracle checks; square and domain gates')


def exact_gates():
    arithmetic_audit()
    # Algebra used by the all-domain curvature proof.
    assert 1-Q(2, 9)-Q(3, 11) == Q(50, 99)
    assert Q(50, 99)**2-4*Q(2, 9)*Q(3, 11) == Q(124, 9801) > 0
    assert Q(2, 9)-Q(8, 17)**2 == Q(2, 2601) > 0
    assert 5-13*Q(8, 17)+5*Q(8, 17)**2 == -Q(3, 289) < 0
    assert Q(4, 3) > Q(17, 15)**2
    assert Q(1, 7) > Q(3, 8)**2 and Q(10, 7)**2 > 2
    assert Q(5, 96) > Q(1, 20) and Q(3, 56) > Q(1, 20)
    assert Q(1, 20)-Q(1, 21) == Q(1, 420)
    assert Q(5, 3)-1-Q(7, 72) == Q(41, 72) > 0
    assert 17**2*3 > 28**2
    print('PASS analytic square gates: z(1/3)>2/7; Phi\'>41/72 in the middle; Phi\'<-1/420 in the tail')

    gates = [
        ('D(53/500)', shift_derivative(I(Q(53, 500))), Q(-3, 10000), Q(-2, 10000)),
        ('D(107/1000)', shift_derivative(I(Q(107, 1000))), Q(7, 100000), Q(9, 100000)),
        ('Phi(719/2500)', slope(I(Q(719, 2500))), Q(-5, 100000), Q(-4, 100000)),
        ('Phi(2877/10000)', slope(I(Q(2877, 10000))), Q(10, 100000), Q(11, 100000)),
        ('Phi(4/5)', slope(I(Q(4, 5))), Q(-2, 1000), Q(-1, 1000)),
        ('E(1)', excess(I(1)), Q(12, 1000), Q(13, 1000)),
    ]
    for name, value, lo, hi in gates:
        value.inside(lo, hi)
        print(f'EXACT {name} in ({lo},{hi}); enclosure={value.short()}')

    # These are rational isolations of the one previously defined alpha_*.
    al, ah = Q(10678476019, 10**11), Q(10678476021, 10**11)
    assert shift_derivative(I(al)).hi < 0 < shift_derivative(I(ah)).lo
    alpha = I.box(al, ah)
    assert Q(159, 500) < (1+Q(53, 500))*Q(719, 2500)
    assert (1+Q(107, 1000))*Q(2877, 10000) < Q(319, 1000)
    assert Q(4, 5)*(1+Q(107, 1000)) < Q(89, 100) < Q(891, 1000) < 1-Q(107, 1000)
    print(f'EXACT alpha_* in ({al},{ah}); lambda_* in (159/500,319/1000)')
    print('EXACT descending counterexample interval: [89/100,891/1000] lies after x=4/5 and before the wrap')

    # Machin identity: tan(4 atan(1/5))=120/119; subtracting atan(1/239)
    # gives tangent 1. The angle is in (0,pi/2), hence equals pi/4.
    assert (Q(120, 119)-Q(1, 239))/(1+Q(120, 119)*Q(1, 239)) == 1
    pi = 16*atan(I(Q(1, 5)))-4*atan(I(Q(1, 239)))
    pi.inside(Q(314159265358979323846, 10**20), Q(314159265358979323847, 10**20))
    c318 = coefficient(alpha, I(Q(159, 500)), pi)
    c30 = coefficient(alpha, I(Q(3, 10)), pi)
    c318.inside(Q(14191368, 10**8), Q(14191369, 10**8))
    c30.inside(Q(14192459, 10**8), Q(14192460, 10**8))
    assert Q(14192459-14191369, 10**8) > Q(1, 100000)
    print(f'EXACT C_ref(159/500) in (14191368/100000000,14191369/100000000); enclosure={c318.short()}')
    print(f'EXACT C_30 in (14192459/100000000,14192460/100000000); enclosure={c30.short()}')
    print('PASS exact gates: C_rp<C_ref(159/500)<C_30-1/100000; C_rp<14191369/100000000')


def diagnostics():
    import mpmath as mp

    mp.mp.dps = 70
    mpq = lambda q: mp.mpf(q.numerator)/q.denominator

    def derivative_alpha(a):
        lo, hi = (1+a)/3, 1-a
        return (lo/2+mp.quad(lambda t: mp.sqrt(t/(1+a+t)), [lo, hi])/2
                +mp.quad(lambda t: mp.sqrt(t/(a+t)), [hi, 1])/2
                -(mp.sqrt(2)-1)*mp.sqrt(hi))

    alpha = mp.findroot(derivative_alpha, (mp.mpf('.106'), mp.mpf('.107')))
    aa, wrap = 1+alpha, 1-alpha
    tau = mp.findroot(lambda x: mp.sqrt(x/(1+x))+mp.sqrt(x)-1,
                      (mp.mpf('.27'), mp.mpf('.30')))

    def switch(x):
        if x <= tau:
            return x
        return mp.findroot(lambda u: mp.sqrt(u/(1+u))+mp.sqrt(u/(1+x-u))-1,
                           (mp.mpf('.25'), mp.mpf('.4')))

    def phi(x):
        z = switch(x)
        endpoint = max(mp.sqrt(1+x), mp.sqrt(x)*(mp.sqrt(1+x)+1))
        diagonal = max(1+x, 2*mp.sqrt(x*(1+x)))
        return (endpoint-diagonal
                +mp.quad(lambda u: mp.sqrt((1+u)/(1+x-u)), [0, z])/2
                +mp.quad(lambda u: mp.sqrt(u/(1+x-u)), [z, x])/2)

    def cost(lam):
        # Independent original (unnormalized) max, split only at its actual ties.
        z = aa*switch(lam/aa)
        chord = lambda t: mp.sqrt((aa+t)*(aa+lam-t))
        chain = lambda t: mp.sqrt(t)*(mp.sqrt(aa+t)+mp.sqrt(aa+lam-t))
        block = mp.quad(lambda t: max(chord(t), chain(t)), [0, z, lam])
        splits = sorted(set([lam, max(lam, aa/3), wrap]))
        tail = mp.quad(lambda t: max(aa+t, 2*mp.sqrt(t*(aa+t))), splits)
        tail += 2*mp.quad(lambda t: mp.sqrt(t*(alpha+t)), [wrap, 1])
        return (block+tail)/(4*mp.pi)

    x_min = mp.findroot(phi, (mp.mpf('.2876'), mp.mpf('.2877')))
    x_max = mp.findroot(phi, (mp.mpf('.77'), mp.mpf('.80')))
    print('DIAGNOSTIC alpha_*='+mp.nstr(alpha, 35))
    print('DIAGNOSTIC tau='+mp.nstr(tau, 35))
    print('DIAGNOSTIC lambda_min='+mp.nstr(aa*x_min, 35))
    print('DIAGNOSTIC lambda_max='+mp.nstr(aa*x_max, 35))
    print('DIAGNOSTIC C_rp='+mp.nstr(cost(aa*x_min), 35))

    # Fixed probes cover all branches, the two transitions, and the upper end.
    points = [mp.mpf(1)/(4*aa), mp.mpf('.27'), tau-mp.mpf('1e-8'),
              tau+mp.mpf('1e-8'), mp.mpf('.2876'), mp.mpf('.2877'),
              mp.mpf(1)/3-mp.mpf('1e-8'), mp.mpf(1)/3+mp.mpf('1e-8'),
              mp.mpf('.6'), mp.mpf('.8'), mp.mpf('.891')/aa]
    for x in points:
        assert abs(mp.diff(cost, aa*x)-aa*phi(x)/(4*mp.pi)) < mp.mpf('1e-55')
        if x < tau:
            curvature = 1/mp.sqrt(1+x)+mp.asin(x/(2+x))/2-1
            assert curvature < 0
        else:
            z = switch(x)
            rr = mp.sqrt(z/(1+z))
            zp = (1-rr)**2/(2-rr+2*rr*rr)
            assert abs(zp-mp.diff(switch, x)) < mp.mpf('1e-55')
            jj = (mp.quad(lambda u: mp.sqrt(1+u)/(1+x-u)**mp.mpf('1.5'), [0, z])
                  +mp.quad(lambda u: mp.sqrt(u)/(1+x-u)**mp.mpf('1.5'), [z, x]))
            qq = zp*(mp.sqrt(1+z)-mp.sqrt(z))/(2*mp.sqrt(1+x-z))
            dp = 1 if x < mp.mpf(1)/3 else (1+2*x)/mp.sqrt(x*(1+x))
            curvature = ((1+2*x)/(2*mp.sqrt(x*(1+x)))+1/(2*mp.sqrt(x))
                         -dp+mp.sqrt(x)/2-jj/4+qq)
            if x < mp.mpf(1)/3:
                assert curvature > mp.mpf(41)/72
            else:
                assert curvature < -mp.mpf(1)/420
        assert abs(curvature-mp.diff(phi, x)) < mp.mpf('1e-55')
    for center in [tau, mp.mpf(1)/3]:
        eps = mp.mpf('1e-18')
        assert abs(phi(center-eps)-phi(center+eps)) < 4*eps
        assert abs(cost(aa*(center-eps))-cost(aa*(center+eps))) < eps
    print(f'PASS independent full-max diagnostics: {len(points)} derivatives and curvatures; both switch continuity checks')

    # Independent quadrature comparison to exact interval outputs (diagnostic).
    for q in [Q(719, 2500), Q(2877, 10000), Q(4, 5)]:
        enclosure = slope(I(q))
        value = phi(mpq(q))
        assert mpq(Q(enclosure.lo, SCALE)) < value < mpq(Q(enclosure.hi, SCALE))
    al, ah = Q(10678476019, 10**11), Q(10678476021, 10**11)
    alpha_box = I.box(al, ah)
    pi = 16*atan(I(Q(1, 5)))-4*atan(I(Q(1, 239)))
    for lam in [Q(3, 10), Q(159, 500)]:
        enclosure = coefficient(alpha_box, I(lam), pi)
        value = cost(mpq(lam))
        assert mpq(Q(enclosure.lo, SCALE)) < value < mpq(Q(enclosure.hi, SCALE))
    assert cost(mp.mpf('.891')) < cost(mp.mpf('.89'))
    print('PASS diagnostic quadrature agrees with exact slope/coefficient enclosures and descending counterexample')
    print('NOTE: decimals and derivative diagnostics are numerical observations; exact gates use integers only.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only', action='store_true',
                        help='run only the standard-library rational proof gates')
    args = parser.parse_args()
    exact_gates()
    if not args.exact_only:
        diagnostics()
