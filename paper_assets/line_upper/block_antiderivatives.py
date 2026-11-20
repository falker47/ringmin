"""Arb antiderivatives with exact branch isolation for the rational block example."""
from fractions import Fraction as Q
from math import ceil, floor

from flint import arb, ctx

ALPHA = Q("0.10930")
LENGTHS = tuple(map(Q, ("0.31903", "0.04370", "0.00580", "0.00005")))


def ball(q):
    return arb(q.numerator) / q.denominator


def switch_sign(t, x, y):
    # Compare sqrt(t/x)+sqrt(t/y) with 1 without ambiguous squaring.
    p, q = t/x, t/y
    residual = 1-p-q
    if residual < 0:
        return 1
    test = 4*p*q - residual**2
    return (test > 0) - (test < 0)


def circle_primitive(z, radius):
    return (z*(radius**2-z**2).sqrt() + radius**2*(z/radius).asin()) / 2


def rising_primitive(t, c):
    h = c/2
    u = t+h
    radical = (t*(t+c)).sqrt()
    return (u*radical - h*h*(u+radical).log())/2


def piece(u, v, c, reflected):
    # X=c+t. Y=c+u+v-t on a reflection and X otherwise.
    e = c+u+v
    def which(t):
        return switch_sign(t, c+t, e-t if reflected else c+t)

    def primitive(t, legs):
        s, a = ball(t), ball(c)
        if not reflected:
            return 2*rising_primitive(s, a) if legs else s*(a+s/2)
        b = ball(e)
        if legs:
            return rising_primitive(s, a) + circle_primitive(s-b/2, b/2)
        return circle_primitive(s-(b-a)/2, (a+b)/2)

    if which(u) >= 0:
        return primitive(v, True) - primitive(u, True)
    if which(v) <= 0:
        return primitive(v, False) - primitive(u, False)
    lo, hi = u, v
    for _ in range(88):
        middle = (lo+hi)/2
        if which(middle) < 0:
            lo = middle
        else:
            hi = middle
    # Both ratios in which() increase. The uncertain switch strip has
    # width hi-lo and the original integrand is in [0,3].
    strip = arb(0).union(3*ball(hi-lo))
    return (primitive(lo, False) - primitive(u, False) + strip
            + primitive(v, True) - primitive(hi, True))


def cost(alpha=ALPHA, lengths=LENGTHS):
    ctx.prec = 192
    total = arb(0)
    left = Q(0)
    for length in lengths:
        total += piece(left, left+length, 1+alpha, True)
        left += length
    assert left < 1-alpha
    total += piece(left, 1-alpha, 1+alpha, False)
    total += piece(1-alpha, Q(1), alpha, False)
    return total/(4*arb.pi())


def literal_error():
    # Paper II v3 and S2 isolations, endpoints interpreted as rationals.
    a_lo, a_hi = Q("0.1093"), Q("0.10931")
    ranges = [((1+a_lo)*Q("0.2876"), (1+a_hi)*Q("0.2877")),
              (Q("0.043"), Q(7,160)), (Q(29,5000), Q(27,4000)),
              (Q(1,20000), Q(1,20000))]
    da = max(abs(ALPHA-a_lo), abs(ALPHA-a_hi))
    error = 4*da
    u0 = u_lo = u_hi = du = Q(0)
    for nominal, (lo, hi) in zip(LENGTHS, ranges):
        v0, v_lo, v_hi = u0+nominal, u_lo+lo, u_hi+hi
        dv = max(abs(v0-v_lo), abs(v0-v_hi))
        error += max(nominal, hi)*(2*(du+dv)+4*da)
        u0, u_lo, u_hi, du = v0, v_lo, v_hi, dv
    return ball(error)/(4*arb.pi())


def endpoints(value, digits=14):
    scale = 10**digits
    return (floor(Q(str(value.lower().fmpq()))*scale),
            ceil(Q(str(value.upper().fmpq()))*scale))


def format_endpoint(n, digits):
    return f"{n//10**digits}.{n%10**digits:0{digits}d}"


def report(label, value, digits):
    lo, hi = endpoints(value, digits)
    print(label, format_endpoint(lo, digits), format_endpoint(hi, digits))


if __name__ == "__main__":
    example = cost()
    report("RATIONAL_BLOCK_ARB", example, 14)
    radius = literal_error()
    report("LITERAL_U4_LIPSCHITZ", (example-radius).union(example+radius), 12)
    report("DIAGONAL_ARB", cost(Q(107,1000), ()), 14)
