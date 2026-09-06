"""Irreducible rational gates for the continuous second-block start theorem.

Run with python -S. Imports only stdlib Fraction/isqrt; writes no files.
No floats, quadrature, root search, scan, optimizer or previous code imports.
The exact alpha and width brackets are imported from the width proof,
Sections 4 and 7; their defining minima are not re-proved here.
"""

from fractions import Fraction as Q
from math import isqrt


SCALE = 10**30
AL, AH = Q(10930369, 10**8), Q(10930371, 10**8)
EL, EH = Q(31248, 10**6), Q(1, 32)
XH = Q(2877, 10000)
U, DELTA = Q(1, 3), Q(1, 10**6)


def exact(value):
    if not isinstance(value, (int, Q)):
        raise TypeError('integer or Fraction required')
    return Q(value)


def sqrt_bounds(value):
    value = exact(value)
    if value < 0:
        raise ValueError('negative radicand')
    scaled = value.numerator*SCALE*SCALE
    low = isqrt(scaled//value.denominator)
    high = low + (low*low*value.denominator != scaled)
    lower, upper = Q(low, SCALE), Q(high, SCALE)
    assert 0 <= lower <= upper and lower*lower <= value <= upper*upper
    return lower, upper


def radical_sign(p, q):
    """Exact sign of sqrt(p)+sqrt(q)-1, with positivity before squaring."""
    p, q = exact(p), exact(q)
    if p < 0 or q < 0:
        raise ValueError('negative radicand')
    residual = 1-p-q
    if residual < 0:
        return 1
    difference = 4*p*q-residual*residual
    return (difference > 0)-(difference < 0)


def endpoint_sum_bounds(A, e):
    """Enclose sqrt(B*(B+e))+sqrt(U+e)*(sqrt(B)+sqrt(B+e))."""
    A, e = exact(A), exact(e)
    if A <= 0 or e <= 0:
        raise ValueError('positive parameters required')
    B = A+U
    c = sqrt_bounds(B*(B+e))
    low = sqrt_bounds(U+e)
    left, right = sqrt_bounds(B), sqrt_bounds(B+e)
    return (c[0]+low[0]*(left[0]+right[0]),
            c[1]+low[1]*(left[1]+right[1]))


def outward(value, grid):
    return value.numerator*grid//value.denominator


def main():
    a_low, a_high = 1+AL, 1+AH
    u_low, u_high = U-DELTA, U+DELTA
    assert 0 < AL < AH < Q(1, 2) and 0 < EL < EH
    assert a_high*XH < u_low
    assert u_high+EH < 1-AH
    assert 3*(u_high+EH) < a_low
    assert a_low > EH
    # v(0)<2*sqrt(u/(A+u))<1 on the whole rectangle.
    assert 3*u_high < a_low
    # v(e) increases in u,e and decreases in A (A>e).
    t = u_low+EL
    assert radical_sign(t/(a_high+t), t/(a_high+u_low)) > 0
    print('PASS rectangle: |u-1/3|<=1/10^6, EL<=epsilon<=EH; disjoint, pre-wrap, diagonal chord, block mixed')

    # Positive summands increase separately with A,e; subtraction reverses
    # the endpoint choices. The linear term is enclosed independently.
    lower_sum = endpoint_sum_bounds(a_low, EL)[0]
    upper_sum = endpoint_sum_bounds(a_high, EH)[1]
    lower = 2*(a_low+U)+EL-upper_sum
    upper = 2*(a_high+U)+EH-lower_sum
    assert Q(1, 20000) < lower <= upper < Q(1, 10000)
    grid = 10**12
    left, right = outward(lower, grid), -outward(-upper, grid)
    print(f'EXACT 4*pi*partial_u Delta C(1/3,epsilon_*) in [{left},{right}]/10^12')
    print('PASS strict quantitative gate: 1/20000 < 4*pi*partial_u Delta C < 1/10000')

    assert sqrt_bounds(0) == (0, 0) and sqrt_bounds(4) == (2, 2)
    assert radical_sign(Q(1, 4), Q(1, 4)) == 0
    assert radical_sign(0, 0) == -1 and radical_sign(1, 1) == 1
    for invalid in (lambda: sqrt_bounds(0.1), lambda: sqrt_bounds(-1),
                    lambda: radical_sign(-1, 1),
                    lambda: endpoint_sum_bounds(1, 0)):
        try:
            invalid()
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError('invalid exact-gate input accepted')
    print('PASS exact ties, square-root enclosures and four invalid-input guards')
    print('NOTE: analytic sign and endpoint cancellation are proved in the note; imported minima and extra decimal digits are not certified here')


if __name__ == '__main__':
    main()
