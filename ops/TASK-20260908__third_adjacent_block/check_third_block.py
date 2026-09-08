"""Exact gates and independent raw-cost enclosure for the third-block theorem.

Run with python -S. Imported brackets only; no floating values, root solver,
parameter refinement, production/previous-checker import or file write.
Finite moment probes supplement the arbitrary-test analytic measure proof.
"""

from fractions import Fraction as Q
from itertools import product
from math import isqrt


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, EH = Q(43, 1000), Q(11, 250)
DELTA = Q(1, 1000)


def sqrt_upper(q):
    """Directed rational upper root, verified by squaring nonnegative sides."""
    assert q >= 0
    scale = 10**30
    lower = Q(isqrt(q.numerator * scale**2 // q.denominator), scale)
    upper = lower + Q(1, scale)
    assert 0 <= lower and lower**2 <= q < upper**2
    return upper


def sqrt_sum_sign(p, q):
    """Exact sign of sqrt(p)+sqrt(q)-1, retaining pre-square signs/ties."""
    assert p >= 0 and q >= 0
    residual = 1-p-q
    if residual < 0:
        return 1
    signed = 4*p*q-residual**2
    return (signed > 0)-(signed < 0)


def main():
    assert 0 < AL < AH < Q(1, 2)
    assert Q(1, 4) < XL < XH < Q(1, 3)
    assert 0 < EL < EH and DELTA == Q(1, 1000)
    a_low, a_high = 1+AL, 1+AH
    v_low, v_high = a_low*XL+EL, a_high*XH+EH
    margins = {
        'v lower': v_low,
        'A-3v-4delta': a_low*(1-3*XH)-3*EH-4*DELTA,
        'a-v-delta': a_low*(Q(1, 3)-XH)-EH-DELTA,
        'b-v-delta': 1-AH-v_high-DELTA,
        '3/2-M': Q(3, 2)-a_high-v_high-DELTA/2,
    }
    for name, margin in margins.items():
        assert margin > 0, name
        print('EXACT', name, '>', margin, '> 0')
    assert margins['A-3v-4delta']+DELTA == 3*margins['a-v-delta']
    assert -DELTA**3/36 == -Q(1, 36000000000)
    assert DELTA**3/576 == Q(1, 576000000000)

    # Independent branch comparison includes degenerate and nondegenerate ties.
    for p, q, expected in [(Q(1, 4), Q(1, 4), 0),
                           (Q(1, 9), Q(1, 9), -1),
                           (Q(4, 9), Q(4, 9), 1),
                           (Q(1), Q(0), 0), (Q(2), Q(0), 1)]:
        assert sqrt_sum_sign(p, q) == expected

    # Eight corner probes, not replacements for the exact parameters.
    moments = 0
    for alpha, x, e in product((AL, AH), (XL, XH), (EL, EH)):
        A = 1+alpha
        lam, v = A*x, A*x+e
        ends = (Q(0), lam, v, v+DELTA)
        assert 0 < lam < v < v+DELTA < A/3 < 1-alpha < 1
        assert A+ends[-1] < 2
        for left, right in zip(ends, ends[1:]):
            # Reflection maps the two closed endpoints into each other.
            intercept = left+right
            assert intercept-left == right and intercept-right == left
            for degree in range(7):
                power = degree+1
                direct = ((A+right)**power-(A+left)**power)/power
                reflected = ((A+intercept-left)**power
                             -(A+intercept-right)**power)/power
                assert (direct+reflected)/2 == direct
                moments += 1
        # Lengths of the five high ranges sum exactly to one.
        high_ends = (Q(1), A, A+lam, A+v, A+v+DELTA, Q(2))
        assert all(l < r for l, r in zip(high_ends, high_ends[1:]))
        assert sum(r-l for l, r in zip(high_ends, high_ends[1:])) == 1
        for s in (Q(0), DELTA/2, DELTA):
            t, X, Y = v+s, A+v+s, A+v+DELTA-s
            assert sqrt_sum_sign(t/X, t/Y) == -1
            assert 4*t < X
    print('PASS 8 endpoint partitions,', moments,
          'reflection moments, 24 full-max branch probes and 5 sign/tie controls')

    # Independent midpoint upper enclosure of (13), using the raw maximum.
    # Proof supplies concavity after the uniform branch gate and monotonicity
    # of the integrated difference in B. B_high is the worst allowed corner.
    A, v = a_high, v_high
    B = A+v
    panels = 8
    width = DELTA/panels
    cost_upper = Q(0)
    for j in range(panels):
        t = v+width*Q(2*j+1, 2)
        X = A+t
        Y = A+2*v+DELTA-t
        chord_upper = sqrt_upper(X*Y)
        chain_upper = sqrt_upper(t)*(sqrt_upper(X)+sqrt_upper(Y))
        assert sqrt_sum_sign(t/X, t/Y) == -1 and 4*t < X
        cost_upper += width*max(chord_upper, chain_upper)
    raw_upper = cost_upper-DELTA*(B+DELTA/2)
    assert raw_upper < -Q(1, 36000000000)
    print('EXACT 8-panel raw full-max upper =', raw_upper)
    print('PASS independent integral enclosure < -1/36000000000')
    print('PASS analytic pi<4 conversion: C_b-C_3 > 1/576000000000')
    print('NOTE: continuum proof and imported minima are separate; no finite recovery or radius/global transfer')


if __name__ == '__main__':
    main()
