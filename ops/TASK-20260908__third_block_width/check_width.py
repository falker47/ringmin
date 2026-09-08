"""Bounded exact checks for the variable third-width continuous theorem.

Run with python -S. Only accepted brackets; no float, root solver, scan,
production/previous-checker import, finite recovery or output artifact.
Analytic arguments in the proof, not probes, supply universal quantifiers.
"""

from fractions import Fraction as Q
from itertools import product
from math import isqrt


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, EH = Q(43, 1000), Q(11, 250)
D0, D1 = Q(1, 1000), Q(1, 250)
L = (1+AL)*(1-3*XH)-3*EH
DG = L/4
PANELS = 16


def sqrt_bounds(value):
    if value < 0:
        raise ValueError('square root requires a nonnegative rational')
    scale = 10**40
    lo = Q(isqrt(value.numerator*scale**2//value.denominator), scale)
    hi = lo+Q(1, scale)
    assert 0 <= lo and lo**2 <= value < hi**2
    return lo, hi


def asin_bounds(value):
    """Eight positive terms; successive term ratio is strictly below value^2."""
    if not 0 <= value < 1:
        raise ValueError('inverse sine enclosure requires 0<=value<1')
    term, partial = value, Q(0)
    for j in range(8):
        partial += term
        ratio = Q((2*j+1)**2, 2*(j+1)*(2*j+3))
        assert 0 < ratio < 1
        term *= value**2*ratio
    return partial, partial+term/(1-value**2)


def sum_root_sign(p, q):
    """Sign of sqrt(p)+sqrt(q)-1, including pre-square signs and ties."""
    if min(p, q) < 0:
        raise ValueError('root-sign inputs must be nonnegative')
    residual = 1-p-q
    if residual < 0:
        return 1
    signed = 4*p*q-residual**2
    return (signed > 0)-(signed < 0)


def closed_bounds(B, width):
    """Independent rational enclosures of the closed cost and derivative."""
    M = B+width/2
    c_lo, c_hi = sqrt_bounds(B*(B+width))
    a_lo, a_hi = asin_bounds(width/(2*M))
    return ((width*c_lo/2+M**2*a_lo-width*M,
             width*c_hi/2+M**2*a_hi-width*M),
            (c_lo+M*a_lo-(B+width), c_hi+M*a_hi-(B+width)))


def raw_bounds(A, v, width):
    """Raw max integral: concave trapezoid lower / midpoint upper bounds.

    Analytic branch gates in the proof ensure concavity on this slab.
    Pointwise exact signs additionally guard each actual evaluation.
    Leibniz integral bounds use its increasing integrand, not the asin form.
    """
    if not (A > 0 and v > 0 and 0 < width <= DG):
        raise ValueError('raw check requires A,v>0 and 0<width<=DG')
    B, step = A+v, width/PANELS

    def cost(s):
        t, X, Y = v+s, B+s, B+width-s
        assert sum_root_sign(t/X, t/Y) == -1 and 4*t < X
        c_lo, c_hi = sqrt_bounds(X*Y)
        t_lo, t_hi = sqrt_bounds(t)
        x_lo, x_hi = sqrt_bounds(X)
        y_lo, y_hi = sqrt_bounds(Y)
        return max(c_lo, t_lo*(x_lo+y_lo)), max(c_hi, t_hi*(x_hi+y_hi))

    endpoints = [cost(j*step) for j in range(PANELS+1)]
    trap = step*((endpoints[0][0]+endpoints[-1][0])/2
                 +sum(p[0] for p in endpoints[1:-1]))
    mid = step*sum(cost(step*Q(2*j+1, 2))[1] for j in range(PANELS))
    diagonal = width*(B+width/2)
    c_lo, c_hi = sqrt_bounds(B*(B+width))
    left = right = Q(0)
    for j in range(PANELS):
        sl, sr = j*step, (j+1)*step
        left += step*sqrt_bounds((B+sl)/(B+width-sl))[0]
        right += step*sqrt_bounds((B+sr)/(B+width-sr))[1]
    return ((trap-diagonal, mid-diagonal),
            (c_lo-(B+width)+left/2, c_hi-(B+width)+right/2))


def main():
    assert 0 < AL < AH < Q(1, 2) and Q(1, 4) < XL < XH < Q(1, 3)
    assert 0 < EL < EH and 0 < D0 < D1 < DG
    assert L == Q(1986317, 100000000)
    assert DG == Q(1986317, 400000000)
    vl, vh = (1+AL)*XL+EL, (1+AH)*XH+EH
    margins = {
        'a-v-D_g': L/3-DG,
        'b-v-D_g': 1-AH-vh-DG,
        '3/2-M(D_g)': Q(3, 2)-(1+AH)-vh-DG/2,
        'A-3v-4d_1': L-4*D1,
        'a-v-d_1': L/3-D1,
    }
    for name, margin in margins.items():
        assert margin > 0, name
        print('EXACT', name, '>', margin, '> 0')
    assert L-4*DG == 0  # Strict accepted input brackets give actual >0.
    assert D1**3/36-D0**3/24 == Q(1, 576000000)
    assert Q(1, 576000000)/16 == Q(1, 9216000000)
    print('PASS 0<1/1000<1/250<D_g; uniform gate has strict actual sign at D_g')

    cases = moments = 0
    for alpha, x, e in product((AL, AH), (XL, XH), (EL, EH)):
        A = 1+alpha
        lam, v = A*x, A*x+e
        B, h = A+v, A/3-v
        assert 0 < DG < h < 1-alpha-v
        for width in (D0, D1, DG):
            ends = (Q(1), A, A+lam, A+v, A+v+width, Q(2))
            assert all(l < r for l, r in zip(ends, ends[1:]))
            assert sum(r-l for l, r in zip(ends, ends[1:])) == 1
            for degree in range(5):
                power = degree+1
                direct = ((A+v+width)**power-(A+v)**power)/power
                reflection = ((A+2*v+width-v)**power
                              -(A+2*v+width-(v+width))**power)/power
                assert direct == reflection
                moments += 1
            cost, deriv = raw_bounds(A, v, width)
            formula, slope = closed_bounds(B, width)
            assert cost[0] <= formula[0] <= formula[1] <= cost[1] < 0
            assert deriv[0] <= slope[0] <= slope[1] <= deriv[1] < 0
            cases += 1
        # First-obstruction controls: endpoint chain at h, midpoint chord,
        # removed diagonal ties exactly there. No unproved chord extension.
        assert sum_root_sign((v+h)/(B+h), (v+h)/B) == 1
        assert sum_root_sign((v+h/2)/(B+h/2), (v+h/2)/(B+h/2)) == -1
        assert 4*(v+h) == B+h
    print('PASS', cases, 'raw full-max/closed-cost and Leibniz/closed-derivative enclosures')
    print('PASS', moments, 'new-slab reflection moments; 24 high partitions; 8 chain/tie endpoint controls')

    # F_ch increases in B: derivative integrand is
    # (2B+width)/(2sqrt((B+s)(B+width-s)))-1 >=0, since its
    # positive square difference is (width-2s)^2. Thus the following
    # lower saving holds throughout the accepted B bracket. Two raw max
    # quadratures supply it independently of the centered saving bound.
    old, _ = raw_bounds(1+AL, vl, D0)
    new, _ = raw_bounds(1+AH, vh, D1)
    saving_lower = old[0]-new[1]
    assert saving_lower > Q(1, 576000000)
    print('EXACT raw old-minus-new lower =', saving_lower)
    print('PASS independent saving >1/576000000; cost saving >1/9216000000 via pi<4')

    controls = [(Q(1, 4), Q(1, 4), 0), (Q(1, 9), Q(1, 9), -1),
                (Q(4, 9), Q(4, 9), 1), (Q(1), Q(0), 0), (Q(2), Q(0), 1)]
    for p, q, expected in controls:
        assert sum_root_sign(p, q) == expected
    assert asin_bounds(Q(0)) == (0, 0)
    invalid = [lambda: sqrt_bounds(Q(-1)), lambda: asin_bounds(Q(-1)),
               lambda: asin_bounds(Q(1)), lambda: sum_root_sign(Q(-1), Q(0)),
               lambda: raw_bounds(Q(1), Q(1, 3), Q(0)),
               lambda: raw_bounds(Q(1), Q(1, 3), 2*DG)]
    for probe in invalid:
        try:
            probe()
        except ValueError:
            pass
        else:
            raise AssertionError('invalid input was not rejected')
    print('PASS 5 radical sign/tie controls; zero inverse sine; 6 invalid inputs')
    print('NOTE: analytic proof supplies all-width signs; no refinement, recovery, radius/global transfer or hosted CI')


if __name__ == '__main__':
    main()
