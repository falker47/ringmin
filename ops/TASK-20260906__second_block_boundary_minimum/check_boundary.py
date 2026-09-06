"""Only rational endpoint gates for the continuous boundary-width theorem.

Run with python -S. Exact imported brackets enclose alpha_hat and x_*;
their defining minima are not recomputed here. No floats, radicals,
transcendental enclosures, root solver, quadrature, mesh or production import.
The analytic proof supplies branch classification, mixed curvature and attainment.
This fixed-budget program writes no files.
"""
from fractions import Fraction as Q

AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, ET, EH = Q(43, 1000), Q(87, 2000), Q(11, 250)


def endpoint_gate(A, x, epsilon):
    """Return positive pre-square residual and signed squared comparison.

    F=sqrt(p)+sqrt(q). With p,q>=0 and r=1-p-q>0,
    sign(F-1)=sign(4*p*q-r*r). No extraneous squared root is selected.
    """
    assert A > 0 and Q(1, 4) < x < Q(1, 3)
    w = epsilon/A
    assert 0 < w < Q(1, 3)-x
    p = (x+w)/(1+x+w)
    q = (x+w)/(1+x)
    residual = 1-p-q
    assert p > 0 and q > 0 and residual > 0
    return residual, 4*p*q-residual*residual


def main():
    assert 0 < AL < AH < Q(1, 2)
    assert Q(1, 4) < XL < XH < Q(1, 3)
    assert 0 < EL < ET < EH < (1+AL)*(Q(1, 3)-XH)
    assert (1+AL)*(1+XL) > 1
    # F increases in x and w=epsilon/A. These are its upper/lower
    # rectangle corners, not replacements for the exact parameters.
    left_residual, left_delta = endpoint_gate(1+AL, XH, EL)
    right_residual, right_delta = endpoint_gate(1+AH, XL, ET)
    assert left_delta < 0 < right_delta
    slack = EH-ET-ET*ET/8
    assert slack > 0
    print('EXACT lower residual =', left_residual)
    print('EXACT lower signed square =', left_delta, '< 0')
    print('EXACT upper residual =', right_residual)
    print('EXACT upper signed square =', right_delta, '> 0')
    print('EXACT location slack =', slack, '> 0')
    print('PASS imported bracket order and two directed endpoint sign gates')
    print('PASS analytic distance-bound implication: 43/1000 < epsilon_b < 11/250')
    print('NOTE: continuum proof and imported minima are separate; no numerical root or integral is certified here')


if __name__ == '__main__':
    main()
