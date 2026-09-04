"""Exact sequence-proof gates; stdlib only, no production/diagnostic imports.

Polynomials are tuples of Fraction coefficients in ascending degree.
No roots, floating-point arithmetic, asymptotic bounds or scans over k.
The analytic arguments being audited are in research/SUPNICK_SEAM_SEQUENCES.md.
"""

from collections import Counter
from fractions import Fraction as F
from math import comb


class AuditFailure(ValueError):
    """An exact gate failed, including under python -O."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def poly(*values):
    result = list(map(F, values)) or [F(0)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def add(a, b):
    return poly(*( (a[i] if i < len(a) else 0)
                  + (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b))) ))


def scale(a, factor):
    return poly(*(factor*x for x in a))


def sub(a, b):
    return add(a, scale(b, -1))


def mul(*factors):
    result = poly(1)
    for factor in factors:
        row = [F(0)]*(len(result)+len(factor)-1)
        for i, a in enumerate(result):
            for j, b in enumerate(factor):
                row[i+j] += a*b
        result = poly(*row)
    return result


def derivative(a):
    return poly(*(i*a[i] for i in range(1, len(a))))


def evaluate(a, t):
    value = F(0)
    for coefficient in reversed(a):
        value = value*t+coefficient
    return value


def certify_positive(p, zero_at_origin=False):
    """Certify p(t)>0 for 0<t<=1/6 by t=y/(6(1+y))."""
    degree = len(p)-1
    coefficients = tuple(sum((p[i]*F(comb(degree-i, j-i), 6**i)
                              for i in range(j+1)), F(0))
                         for j in range(degree+1))
    require(coefficients[0] == p[0], "transform constant")
    require(coefficients[-1] == evaluate(p, F(1, 6)), "closed endpoint")
    if zero_at_origin:
        require(degree >= 1, "zero polynomial is not strictly positive")
        require(coefficients[0] == 0, "expected origin zero")
        require(all(v > 0 for v in coefficients[1:]), "positive nonconstant coefficients")
    else:
        require(all(v > 0 for v in coefficients), "positive coefficients")
    return degree, sum(v > 0 for v in coefficients)


def threshold_gates(c):
    require(type(c) is int and c in (5, 6), "offset domain")
    t = poly(0, 1)
    a, b, g = poly(4, c), poly(4, c-1), poly(9, 2*c-1)
    ab = mul(a, b)
    u = add(ab, add(a, b))
    v = mul(ab, g)
    h = poly(32*(2*c-1), 48*c*(c-1)+9,
             6*c*(c-1)*(2*c-1), c*c*(c-1)**2)
    require(sub(mul(u, u), scale(v, 4)) == mul(t, h), "conjugate identity")
    require(all(x > 0 for x in h+v), "positive H and V")
    p, j = mul(ab, u), scale(ab, 2)
    pr = add(sub(scale(mul(h, p), 2), mul(t, h, derivative(p))),
             mul(t, derivative(h), p))
    jr = add(sub(scale(mul(h, j), 2), mul(t, h, derivative(j))),
             mul(t, derivative(h), j))
    den = scale(mul(v, h, h), 2)
    nr = scale(mul(v, pr), 2)
    ns = sub(scale(mul(v, jr), 2), mul(t, h, j, derivative(v)))
    leading = F(24, 2*c-1)
    linear = {5: F(61, 36), 6: F(2447, 1452)}[c]
    gates = [("radical_coefficient", ns, False)]
    for sign, label in ((-1, "lower"), (1, "upper")):
        target = poly(2*leading, linear+sign*F(1, 8))
        m = sub(mul(target, den), nr)
        margin = scale(sub(mul(m, m), mul(ns, ns, v)), sign)
        gates.extend(((label+"_presquare", m, False),
                      (label+"_margin", margin, True)))
    return gates


def atan_partial(x, terms):
    require(F(0) < x < 1 and terms > 0, "atan series domain")
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                for j in range(terms)), F(0))


def check_constants():
    # Even partial sums are lower bounds; odd partial sums are upper bounds.
    a_lo, a_hi = atan_partial(F(3, 4), 24), atan_partial(F(3, 4), 25)
    pi_lo = 16*atan_partial(F(1, 5), 10)-4*atan_partial(F(1, 239), 3)
    pi_hi = 16*atan_partial(F(1, 5), 11)-4*atan_partial(F(1, 239), 2)
    require(F(3) < pi_lo < pi_hi < F(22, 7), "pi interval")
    require(F(447, 100) < (6+F(25, 2)*a_lo)/pi_hi, "alpha lower")
    require((6+F(25, 2)*a_hi)/pi_lo < F(4471, 1000), "alpha upper")
    require(F(287, 250) < (2+F(5, 2)*a_lo)/pi_hi, "beta lower")
    require((2+F(5, 2)*a_hi)/pi_lo < F(1149, 1000), "beta upper")
    require(F(159, 250) < 2/pi_hi < 2/pi_lo < F(637, 1000), "gamma interval")
    # Machin branch: tan(2 atan(1/5))=5/12,
    # tan(4 atan(1/5))=120/119, tan(4 atan(1/5)-atan(1/239))=1.
    double = 2*F(1, 5)/(1-F(1, 5)**2)
    quadruple = 2*double/(1-double**2)
    require(double == F(5, 12) and quadruple == F(120, 119), "Machin doubling")
    require((quadruple-F(1, 239))/(1+quadruple*F(1, 239)) == 1, "Machin tangent")
    require(0 < 4*atan_partial(F(1, 5), 2)-F(1, 239)
            < F(4, 5) < 1, "Machin positive branch")
    require(F(5, 2)+F(109, 720) == F(1909, 720) < F(8, 3), "error width")
    require(F(1, 4)+F(1, 60) == F(4, 15), "quadrature lower error")
    require(F(4, 15)+F(3, 16) == F(109, 240), "quadrature width")
    require((F(216, 480)+F(36, 64))/108 == F(3, 320), "derivative remainder")
    slope5 = F(4471, 1000)-F(16, 3)
    slope6 = F(447, 100)-F(48, 11)
    bound5 = (6*slope5+5*F(1149, 1000)+F(637, 1000)+F(3, 320)
              -F(5, 2)-F(61, 36)+F(1, 8))
    bound6 = (6*slope6+6*F(287, 250)+F(159, 250)
              -F(5, 2)-F(2447, 1452)-F(1, 8))
    require(slope5 < 0 and slope6 > 0, "derivative slope directions")
    require(bound5 < -F(8, 3) and bound6 > F(8, 3), "derivative separators")
    # Coefficients in k^2, ck, c^2, k, c, 1 of
    # 12*(7/22)*P - (5k+c-1)^2 + 9.
    positive = (12*F(7, 22)*F(27, 4)-25,
                12*F(7, 22)*F(33, 10)-10,
                12*F(7, 22)*F(7, 20)-1, F(10), F(2), F(8))
    require(positive == (F(17, 22), F(13, 5), F(37, 110), F(10), F(2), F(8)),
            "root comparison polynomial identity")
    require(all(x > 0 for x in positive), "root comparison polynomial positivity")
    require(F(189, 88)*6 > 3, "positive comparison radius")
    print(f'derivative_upper_c5_at_6={bound5} margin_below_minus_8over3={-F(8, 3)-bound5}')
    print(f'derivative_lower_c6_at_6={bound6} margin_above_8over3={bound6-F(8, 3)}')


def check_parity_representations():
    """Four construction checks, not a scan of radii or an all-k proof."""
    total = 0
    for k in (6, 7):
        for c in (5, 6):
            n, size = 4*k+c, 3*k+c+1
            h = size//2
            edges = [(k, n)]
            if size % 2 == 0:
                edges += [(k+h-1, k+h)]
                edges += [(i, n+k-1-i) for i in range(k, k+h-1)]
                edges += [(i, n+k+1-i) for i in range(k+1, k+h)]
            else:
                edges += [(i, n+k-1-i) for i in range(k, k+h)]
                edges += [(i, n+k+1-i) for i in range(k+1, k+h+1)]
            arms = []
            for first in (1, 2):
                arm = []
                for j in range(size):
                    low, high = first+2*j, size-first-2*j
                    if low <= (size+1)//2:
                        arm.append(low)
                    if high > (size+1)//2:
                        arm.append(high)
                arms.append(arm)
            tour = [k+i-1 for i in arms[0]+arms[1][::-1]+[size]]
            require(sorted(tour) == list(range(k, n+1)), "complete rank tour")
            cyclic = [tuple(sorted((a, tour[(i+1) % size]))) for i, a in enumerate(tour)]
            require(Counter(cyclic) == Counter(edges), "parity/rank edges")
            doubled = Counter({e: 2 for e in edges})
            symmetric = Counter({(k, n): 2})
            for i in range(k, n):
                symmetric[tuple(sorted((i, n+k-1-i)))] += 1
            for i in range(k+1, n+1):
                symmetric[tuple(sorted((i, n+k+1-i)))] += 1
            if size % 2 == 0:
                p = (n+k-1)//2
                symmetric[(p, p)] -= 1
                symmetric[(p+1, p+1)] -= 1
                symmetric[(p, p+1)] += 2
            require(doubled == symmetric, "central-edge correction identity")
            total += size
    require(total == 104, "four construction sizes")
    print('parity_constructions=4 cyclic_edges=104 central_correction=PASS')


def check_rejections():
    bad = (poly(-1), poly(1, -12), poly(0), poly(0, -1))
    rejected = 0
    for p in bad:
        try:
            certify_positive(p, zero_at_origin=p[0] == 0)
        except AuditFailure:
            rejected += 1
    require(rejected == 4, "failed positivity gates must reject")
    # A correct radical sign but reversed squared margin must also fail.
    for c in (5, 6):
        margin = threshold_gates(c)[-1][1]
        try:
            certify_positive(scale(margin, -1), zero_at_origin=True)
        except AuditFailure:
            rejected += 1
    require(rejected == 6, "reversed threshold margins must reject")
    print('targeted_rejections=6 PASS')


def main():
    check_constants()
    check_parity_representations()
    for c in (5, 6):
        for name, p, zero in threshold_gates(c):
            degree, positives = certify_positive(p, zero)
            require((degree, positives) == ((20, 20) if zero else
                    (8, 9) if name == 'radical_coefficient' else (10, 11)),
                    'certificate degree/count')
            print(f'c={c} gate={name} degree={degree} positive_coefficients={positives}'
                  f' origin_zero={zero} endpoint_1over6=PASS')
    check_rejections()
    print('exact_sequence_gates=PASS arithmetic=stdlib/Fraction optimized_safe=YES')
    print('production_imports=0 diagnostic_imports=0 root_evaluations=0 k_scan=NONE')


if __name__ == '__main__':
    main()
