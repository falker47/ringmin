"""Only critical inequalities for the continuous second-block width theorem.

Run with python -S. Standard-library integer intervals; no floats, external
packages, quadrature, optimizer, permutations, production or older checkers.
The imported E(x_*) enclosure is from the alpha-minimum proof, Section 4.
All loops have fixed budgets. This program writes no files.
"""

from fractions import Fraction as Q
from math import isqrt


SCALE = 10**40
TERMS = 64
STEPS = 80
U = Q(1, 3)
AL, AH = Q(1093, 10000), Q(10931, 100000)
ARL, ARH = Q(10930369, 10**8), Q(10930371, 10**8)
EL, EH = Q(31248, 10**6), Q(1, 32)


def ceiling(a, b):
    return -((-a)//b)


class Box:
    """Closed rational enclosure, outward rounded to the grid 1/SCALE."""

    def __init__(self, value=0):
        if not isinstance(value, (int, Q)):
            raise TypeError('exact integer or Fraction required')
        value = Q(value)
        self.lo = value.numerator*SCALE//value.denominator
        self.hi = ceiling(value.numerator*SCALE, value.denominator)

    @classmethod
    def raw(cls, lo, hi):
        if lo > hi:
            raise ValueError('reversed interval')
        out = cls.__new__(cls)
        out.lo, out.hi = lo, hi
        return out

    @classmethod
    def interval(cls, lo, hi):
        if lo > hi:
            raise ValueError('reversed rational interval')
        return cls.raw(cls(lo).lo, cls(hi).hi)

    @staticmethod
    def of(value):
        return value if isinstance(value, Box) else Box(value)

    def __add__(self, other):
        other = self.of(other)
        return Box.raw(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Box.raw(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) + (-self)

    def __mul__(self, other):
        other = self.of(other)
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Box.raw(min(products)//SCALE, ceiling(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.of(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError('denominator contains zero')
        pairs = [(a*SCALE, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return Box.raw(min(a//b for a, b in pairs),
                       max(ceiling(a, b) for a, b in pairs))

    def __rtruediv__(self, other):
        return self.of(other)/self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError('nonnegative integer power required')
        out, term = Box(1), self
        while n:
            if n % 2:
                out = out*term
            term = term*term
            n //= 2
        return out

    def sqrt(self):
        if self.lo < 0:
            raise ValueError('negative square-root argument')
        lo, hi = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        return Box.raw(lo, hi+(hi*hi != self.hi*SCALE))

    def widen(self, error):
        if error.lo < 0:
            raise ValueError('negative error bound')
        return Box.raw(self.lo-error.hi, self.hi+error.hi)

    def display(self):
        grid = 10**12
        return f'[{self.lo*grid//SCALE},{ceiling(self.hi*grid, SCALE)}]/10^12'


def sqrt(x):
    return Box.of(x).sqrt()


def atan(x):
    x = Box.of(x)
    for _ in range(2):
        x = x/(1+sqrt(1+x*x))
    q = Box(Q(max(abs(x.lo), abs(x.hi)), SCALE))
    assert q.hi < SCALE
    total, term, square = Box(0), x, x*x
    for k in range(TERMS):
        total += term*(1 if k % 2 == 0 else -1)/(2*k+1)
        term *= square
    return 4*total.widen(q**(2*TERMS+1)/(2*TERMS+1))


def log(x):
    x = Box.of(x)
    if x.lo <= 0:
        raise ValueError('nonpositive logarithm argument')
    fourth = sqrt(sqrt(x))
    y = (fourth-1)/(fourth+1)
    q = Box(Q(max(abs(y.lo), abs(y.hi)), SCALE))
    assert q.hi < SCALE
    total, term, square = Box(0), y, y*y
    for k in range(TERMS):
        total += term/(2*k+1)
        term *= square
    error = 2*q**(2*TERMS+1)/((2*TERMS+1)*(1-q*q))
    return 4*(2*total).widen(error)


def h(c, w):
    """d/dw h(c,w) = sqrt(w/(c-w))."""
    return c*atan(sqrt(w/(c-w)))-sqrt(w*(c-w))


def f(t, c):
    """d/dt f(t,c) = sqrt(t*(t+c))."""
    return ((2*t+c)*sqrt(t*(t+c))
            -c*c*log((sqrt(t)+sqrt(t+c))/sqrt(c)))/4


def circle(v, radius):
    root = sqrt(radius*radius-v*v)
    return (v*root+radius*radius*atan(v/root))/2


def shift_d(alpha):
    A, b = 1+alpha, 1-alpha
    a = A/3

    def primitive(t, c):
        return sqrt(t*(t+c))-c*log((sqrt(t)+sqrt(t+c))/sqrt(c))

    return (a/2+(primitive(b, A)-primitive(a, A)
                 +primitive(Box(1), alpha)-primitive(b, alpha))/2
            -(sqrt(2)-1)*sqrt(b))


def radical_sign(p, q):
    """Sign of sqrt(p)+sqrt(q)-1; only nonnegative sides are squared."""
    if p < 0 or q < 0:
        raise ValueError('negative radicand')
    residual = 1-p-q
    if residual < 0:
        return 1
    difference = 4*p*q-residual*residual
    return (difference > 0)-(difference < 0)


def v_sign(A, e, s):
    B = A+U
    return radical_sign((U+s)/(B+s), (U+s)/(B+e-s))


def z_point(A, e):
    if not (A > 1 and 0 < e < 1):
        raise ValueError('restricted positive width gate')
    assert v_sign(A, e, 0) < 0
    if v_sign(A, e, e) <= 0:
        return Box(e)
    lo, hi = Q(0), e
    for _ in range(STEPS):
        mid = (lo+hi)/2
        sign = v_sign(A, e, mid)
        if sign == 0:
            return Box(mid)
        if sign < 0:
            lo = mid
        else:
            hi = mid
    assert v_sign(A, e, lo) < 0 < v_sign(A, e, hi)
    assert hi-lo == e/2**STEPS
    return Box.interval(lo, hi)


def z_box(A, e):
    # The clipped switch increases separately in A and e (proved in note).
    lower = z_point(Q(A.lo, SCALE), Q(e.lo, SCALE))
    upper = z_point(Q(A.hi, SCALE), Q(e.hi, SCALE))
    return Box.raw(lower.lo, upper.hi)


def slope(A, e):
    """Psi=4*pi*Delta C', restricted to the proved mixed-block gates."""
    A, e = Box.of(A), Box.of(e)
    assert v_sign(Q(A.hi, SCALE), Q(e.lo, SCALE), Q(e.lo, SCALE)) > 0
    B, z = A+U, z_box(A, e)
    i1 = h(2*B+e, B+z)-h(2*B+e, B)
    i2 = h(B+U+e, U+e)-h(B+U+e, U+z)
    if e.hi <= (A/3-U).lo:
        diagonal = B+e
    else:
        assert e.lo >= (A/3-U).hi
        diagonal = 2*sqrt((U+e)*(B+e))
    return sqrt(U+e)*(sqrt(B+e)+sqrt(B))-diagonal+(i1+i2)/2


def critical_delta(A, at_wrap):
    """D(h) or the endpoint extension D(L), with all max branches."""
    B, w = A+U, A/3-U
    e = 2-A-U if at_wrap else w
    assert w.lo > 0
    if at_wrap:
        assert e.lo > w.hi
    assert v_sign(Q(A.hi, SCALE), Q(e.lo, SCALE), Q(e.lo, SCALE)) > 0
    z = z_box(A, e)
    M, T = B+e/2, B+U+e
    chord = circle(z-e/2, M)-circle(-e/2, M)
    chain = (f(U+e, A)-f(U+z, A)
             +circle(U+e-T/2, T/2)-circle(U+z-T/2, T/2))
    diagonal = B*w+w*w/2
    if at_wrap:
        diagonal += 2*(f(U+e, A)-f(U+w, A))
    return chord+chain-diagonal


def report(name, value, positive):
    assert value.lo > 0 if positive else value.hi < 0, name
    print(f'EXACT {name} in {value.display()}')


def main():
    # Imported exact enclosure, not re-optimization or a decimal premise.
    estar = Box.interval(Q(-844272415, 10**12), Q(-844268070, 10**12))
    report('Fprime(10930369/10^8)', shift_d(Box(ARL))+(1+ARL)*estar, False)
    report('Fprime(10930371/10^8)', shift_d(Box(ARH))+(1+ARH)*estar, True)
    assert AL < ARL < ARH < AH
    print('PASS same alpha_hat isolated in (10930369/10^8,10930371/10^8)')

    # Coarse original alpha box suffices for every all-domain curvature gate.
    A = Box.interval(1+AL, 1+AH)
    B, a, b, length = A+U, A/3, 2-A, 2-A-U
    assert (1+AH)*Q(2877, 10000) < U
    assert 0 < AH/4 < Q(3119, 10**5) < Q(312, 10**4) < EL < EH < AL/3
    assert AH/3 < Q(1, 20) and 4*(1+AH)/3 < Q(3, 2)
    assert 2*AH/3 < 1-AH-U
    assert Q(2, 5) < 1-AH-U
    assert v_sign(1+AL, Q(3119, 10**5), Q(3119, 10**5)) < 0
    assert v_sign(1+AH, Q(312, 10**4), Q(312, 10**4)) > 0
    print('PASS domain/switch order: 3119/10^5<tau<312/10^4<EL<EH<h<1/20<L')
    assert Q(1, 2)-Q(3, 160) == Q(77, 160) > 0
    report('Mprime endpoint square at a', (B-a)**2*(A+a)**3-A**4*B, True)
    # A+b=2 is exact, improving dependency control.
    report('Mprime endpoint square at b', 8*(B-b)**2-A**4*B, True)
    report('Jprime square gate', 4*B*B*b-18*length*length, True)
    print('PASS analytic implications: Psiprime>77/160 on (tau,h); Psisecond<0 on (h,L)')

    A = Box.interval(1+ARL, 1+ARH)
    report('Psi(31248/10^6)', slope(A, Box(EL)), False)
    report('Psi(1/32)', slope(A, Box(EH)), True)
    report('Psi(1/3)', slope(A, Box(Q(1, 3))), True)
    report('Psi(2/5)', slope(A, Box(Q(2, 5))), False)
    report('4*pi*Delta C(h)', critical_delta(A, at_wrap=False), True)
    report('4*pi*Delta C(L)', critical_delta(A, at_wrap=True), True)

    # Small domain guards relevant to the critical arithmetic, not a scan.
    assert radical_sign(Q(1, 4), Q(1, 4)) == 0
    assert radical_sign(Q(0), Q(0)) == -1
    assert radical_sign(Q(1), Q(1)) == 1
    for invalid in (lambda: Box(0.1), lambda: sqrt(-1),
                    lambda: Box(1)/Box.interval(-1, 1),
                    lambda: log(0), lambda: z_point(Q(1), Q(1, 10))):
        try:
            invalid()
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError('invalid critical arithmetic input accepted')
    print('PASS ties and five invalid-input guards')
    print('PASS unique continuous global minimum: 31248/10^6<epsilon_*<1/32')
    print('NOTE: no finite permutations, radius transfer, global bound or imported-minimum re-proof')


if __name__ == '__main__':
    main()
