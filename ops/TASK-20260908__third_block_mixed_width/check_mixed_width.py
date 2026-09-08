"""Two rational sign gates for the continuous mixed third-width theorem.

Run with python -S. No width scan, root solver, quadrature, radicals,
parameter reoptimization, production import or output files. Analytic
curvature and endpoint arguments, not finite probes, prove uniqueness.
"""

from fractions import Fraction as Q


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, ET, EU = Q(43, 1000), Q(87, 2000), Q(7, 160)
ALOW, AHIGH = 1+AL, 1+AH
VL, VU = ALOW*XL+EL, AHIGH*XH+EU
TL, TU, DU = Q(29, 5000), Q(67, 10000), Q(27, 4000)
D0, D1, DG = Q(1, 1000), Q(1, 250), Q(1986317, 400000000)


def endpoint_gate(A, v, d):
    """With positive p,q,r, sign(W-1) equals sign(4*p*q-r*r)."""
    if not (A > 0 and A/4 < v < A/3 and 0 < d < A/3-v):
        raise ValueError('gate must lie in the strict chord-diagonal domain')
    p, q = (v+d)/(A+v+d), (v+d)/(A+v)
    r = 1-p-q
    if not (p > 0 and q > 0 and r > 0):
        raise ValueError('squared comparison requires positive p, q and residual')
    return r, 4*p*q-r*r


def main():
    assert 0 < AL < AH < Q(1, 2)
    assert Q(1, 4) < XL < XH < Q(1, 3)
    inherited_slack = EU-ET-ET*ET/8
    assert 0 < EL < ET < ET+ET*ET/8 < EU < Q(11, 250)
    assert ALOW/4 < VL < VU < ALOW/3
    assert 0 < D0 < D1 < DG < TL < TU < DU < ALOW/3-VU
    assert ALOW+VL > 1

    # W decreases in A and increases in v on d<A; the proof supplies
    # these directions. Exactly two fixed endpoint gates, not a scan.
    left_residual, left_square = endpoint_gate(ALOW, VU, TL)
    right_residual, right_square = endpoint_gate(AHIGH, VL, TU)
    assert left_square < 0 < right_square

    root_slack = DU-TU-TU*TU/8
    h_slack = ALOW/3-VU-DU
    cost_slack = Q(3, 2)-AHIGH-VU-DU/2
    assert root_slack > 0 and h_slack > 0 and cost_slack > 0
    saving = (TL**3/36-D1**3/24)/16
    cost_lower, cost_upper = -DU**3/288, -TL**3/576
    assert cost_lower < cost_upper < 0 < saving

    print('EXACT inherited epsilon slack =', inherited_slack)
    print('EXACT lower residual =', left_residual)
    print('EXACT lower signed square =', left_square, '< 0')
    print('EXACT upper residual =', right_residual)
    print('EXACT upper signed square =', right_square, '> 0')
    print('EXACT stationary upper slack =', root_slack)
    print('EXACT diagonal cutoff slack =', h_slack)
    print('EXACT cost denominator slack =', cost_slack)
    print('EXACT cost difference bracket =', cost_lower, ',', cost_upper)
    print('EXACT saving over 1/250 >', saving)
    print('PASS two directed rational sign gates and positive pre-square residuals')
    print('PASS inherited bounds and analytic location/cost implications')
    print('NOTE: continuous proof supplies uniqueness; no finite recovery or geometric transfer')


if __name__ == '__main__':
    main()
