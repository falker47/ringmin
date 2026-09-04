"""Exact rational enclosures and symbolic audits; no Ringmin imports.

The analytic minimization proof is in the research note. This audit checks
its algebra and gives a directed rational enclosure at alpha=107/1000.
All enclosure endpoints use Fraction, including the sqrt/log/pi remainders.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt

import sympy as sp


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def scale(q, x):
    return (q * x[0], q * x[1]) if q >= 0 else (q * x[1], q * x[0])


def sqrt_bound(q):
    if q < 0:
        raise ValueError("negative square root")
    unit = 10**35
    k = isqrt(q.numerator * unit**2 // q.denominator)
    bounds = Q(k, unit), Q(k + 1, unit)
    assert bounds[0] ** 2 <= q < bounds[1] ** 2
    return bounds


def log_near_one(q):
    assert 1 <= q <= 2
    z = (q - 1) / (q + 1)
    count = 80
    total = 2 * sum((z ** (2 * j + 1) / (2 * j + 1) for j in range(count)), Q(0))
    tail = 2 * z ** (2 * count + 1) / ((2 * count + 1) * (1 - z * z))
    return total, total + tail


LOG2 = log_near_one(Q(2))


def log_bound(q):
    if q <= 0:
        raise ValueError("nonpositive logarithm")
    if q < 1:
        return neg(log_bound(1 / q))
    k = 0
    while q > 2:
        q /= 2
        k += 1
    return add(scale(k, LOG2), log_near_one(q))


def log_interval(x):
    return log_bound(x[0])[0], log_bound(x[1])[1]


def atan_bound(q):
    assert 0 < q < 1
    count = 80  # even: partial sum below the true alternating sum
    lower = sum(((-1) ** j * q ** (2 * j + 1) / (2 * j + 1)
                 for j in range(count)), Q(0))
    return lower, lower + q ** (2 * count + 1) / (2 * count + 1)


def primitive(c, t):
    if c == 0:
        return t * t / 2, t * t / 2
    root = sqrt_bound(t * (t + c))
    argument = scale(1 / c, add((2 * t + c, 2 * t + c), scale(2, root)))
    return add(scale((2 * t + c) / 4, root),
               scale(-c * c / 8, log_interval(argument)))


def coefficient_at(alpha, pi):
    assert 0 <= alpha <= Q(1, 2)
    b = 1 - alpha
    d = add(scale(Q(1, 8), log_bound(Q(3))), (-Q(1, 12), -Q(1, 12)))
    result = add(primitive(1 + alpha, b), primitive(alpha, Q(1)))
    result = add(result, neg(primitive(alpha, b)))
    result = add(result, scale((1 + alpha) ** 2, d))
    assert result[0] > 0 and pi[0] > 0
    return result[0] / (2 * pi[1]), result[1] / (2 * pi[0])


def symbolic_audit():
    t, c = sp.symbols("t c", positive=True)
    q = sp.sqrt(t * (t + c))
    primitive_expr = (2 * t + c) * q / 4 - c**2 * sp.log((2 * t + c + 2 * q) / c) / 8
    g = q - c * sp.log((sp.sqrt(t) + sp.sqrt(t + c)) / sp.sqrt(c))
    assert sp.simplify(sp.diff(primitive_expr, t) - q) == 0
    assert sp.simplify(sp.diff(g, t) - sp.sqrt(t / (t + c))) == 0
    f = sp.sqrt(t / (t + c))
    assert sp.simplify(sp.diff(f, c) + sp.sqrt(t) / (2 * (t + c) ** sp.Rational(3, 2))) == 0
    concavity = -c * (4 * t + c) / (4 * t ** sp.Rational(3, 2) * (t + c) ** sp.Rational(5, 2))
    assert sp.simplify(sp.diff(f, t, 2) - concavity) == 0
    switch_value = c**2 * (sp.Rational(5, 18) - sp.log(3) / 8)
    assert sp.simplify(primitive_expr.subs(t, c / 3) - switch_value) == 0
    assert sp.expand((t + c)**2 - 4 * t * (t + c)) == sp.expand((t + c) * (c - 3 * t))
    x = sp.symbols("x")
    assert sp.expand((1 + x)**2 * (1 - x*x) - 1) == sp.expand(x * (2 - 2*x*x - x**3))

    # Boundary terms in the two Leibniz differentiations, independent of F.
    b = sp.symbols("b", positive=True)
    first_boundary = sp.Rational(1, 6) - sp.Rational(1, 12)
    first_boundary += (sp.sqrt(b) - sp.sqrt(b / 2)) / 2
    first_boundary += (sp.sqrt(2) - 1) / (2 * sp.sqrt(b))
    target = sp.Rational(1, 12) + (1 - 1/sp.sqrt(2))*sp.sqrt(b)/2
    target += (sp.sqrt(2)-1)/(2*sp.sqrt(b))
    assert sp.simplify(first_boundary - target) == 0
    d0 = sp.Rational(1, 6) + (g.subs({t: 1, c: 1}) - g.subs({t: sp.Rational(1, 3), c: 1}))/2 - (sp.sqrt(2)-1)
    d0_expected = sp.Rational(5, 6)-sp.sqrt(2)/2-sp.log(1+sp.sqrt(2))/2+sp.log(3)/4
    assert sp.simplify(sp.expand_log(d0 - d0_expected, force=True)) == 0
    print(f"PASS: symbolic primitive, switch, shell, derivatives and boundary gates (sympy {sp.__version__})")


def main():
    symbolic_audit()
    # Exact sign gates used in the analytic proof, without decimal constants.
    assert Q(7, 5)**2 < 2 and Q(7, 4)**2 > 3
    assert Q(7, 6)**2 < 2 and 25 > 18 and 10 > 9
    assert Q(5, 6)-Q(7, 10)-Q(13, 83) == -Q(29, 1245)
    assert Q(2, 3) < log_bound(Q(3))[0] < log_bound(Q(3))[1] < Q(4, 3)
    # Machin identity: tangent(4 atan(1/5)-atan(1/239))=1;
    # the angle is in (0,pi/2), so it is pi/4.
    tangent2 = 2*Q(1, 5)/(1-Q(1, 5)**2)
    tangent4 = 2*tangent2/(1-tangent2**2)
    assert (tangent4-Q(1, 239))/(1+tangent4*Q(1, 239)) == 1
    pi = add(scale(16, atan_bound(Q(1, 5))), scale(-4, atan_bound(Q(1, 239))))
    witness = coefficient_at(Q(107, 1000), pi)
    baseline = coefficient_at(Q(0), pi)
    assert Q("0.14199597949") < witness[0] < witness[1] < Q("0.14199597951")
    assert Q("0.14233385361") < baseline[0] < baseline[1] < Q("0.14233385363")
    assert witness[1] < baseline[0]
    print("PASS: exact rational sign and Machin identity gates")
    print("PROVED ENCLOSURE: 0.14199597949 < K(107/1000)/(2*pi) < 0.14199597951")
    print("PROVED ENCLOSURE: 0.14233385361 < K(0)/(2*pi) < 0.14233385363")
    print("PASS: rational witness strictly improves the unshifted coefficient")


if __name__ == "__main__":
    main()
