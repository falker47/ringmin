"""Bounded exact audit of the second reflected-block continuum variation.

Run with python -S. Integers/Fraction only, no imports from production or
earlier checkers, no floating arithmetic, optimization or permutations.
An independent eight-panel rational enclosure checks one raw chord cost;
the proof, not a finite sample, supplies the all-domain statements.
"""

from fractions import Fraction as Q
from math import isqrt


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
U0, E0 = Q(1, 3), Q(1, 100)


# Ascending coefficients for polynomials in r; no symbolic library.
def poly(values):
    out = [Q(v) for v in values]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


ZERO, ONE, R, RBAR = poly([0]), poly([1]), poly([0, 1]), poly([1, -1])


def add(p, q):
    return poly([(p[i] if i < len(p) else 0)
                 + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return poly([c*v for v in p])


def mul(p, q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return poly(out)


def power(p, n):
    out = ONE
    for _ in range(n):
        out = mul(out, p)
    return out


def integral(p, left=Q(0), right=Q(1)):
    return sum((v*(right**(i+1)-left**(i+1))/Q(i+1)
                for i, v in enumerate(p)), Q(0))


# Formal jets through order two of sqrt(1+e*p(r)).
def root_jet(p):
    return [ONE, scale(p, Q(1, 2)), scale(mul(p, p), Q(-1, 8))]


def jet_add(p, q):
    return [add(a, b) for a, b in zip(p, q)]


def jet_scale(p, c):
    return [scale(a, c) for a in p]


def jet_mul(p, q):
    out = [ZERO, ZERO, ZERO]
    for i in range(3):
        for j in range(3-i):
            out[i+j] = add(out[i+j], mul(p[i], q[j]))
    return out


def radical_sum_sign(p, q):
    """Exact sign of sqrt(p)+sqrt(q)-1, retaining the pre-square gate."""
    if p < 0 or q < 0:
        raise ValueError("nonnegative radicands required")
    residual = 1-p-q
    if residual < 0:
        return 1
    difference = 4*p*q-residual**2
    return (difference > 0)-(difference < 0)


def endpoint_signs(A, u, width):
    B = A+u
    return (radical_sum_sign(u/B, u/(B+width)),
            radical_sum_sign((u+width)/(B+width), (u+width)/B))


def sqrt_upper(value):
    """Rational square-root upper bound, proved by an integer square."""
    if value < 0:
        raise ValueError("nonnegative radicand required")
    if value == 0:
        return Q(0)
    unit = 2**80
    numerator = value.numerator*unit**2
    denominator = value.denominator
    integer = isqrt(numerator//denominator)
    if integer**2*denominator < numerator:
        integer += 1
    bound = Q(integer, unit)
    assert bound**2 >= value and (bound-Q(1, unit))**2 < value
    return bound


def main():
    assert 0 < AL < AH < Q(1, 2)
    assert Q(1, 4) < XL < XH < Q(1, 3)
    gates = {
        "prefix separation": U0-(1+AH)*XH,
        "pre-wrap separation": 1-AH-U0-E0,
        "chord gate": AL-4*E0,
        "M<3/2": Q(3, 2)-(1+AH+U0+E0/2),
    }
    assert all(value > 0 for value in gates.values())
    print("PASS exact witness gates: "
          + "; ".join(f"{key}={value}>0" for key, value in gates.items()))

    roots = [Q(0), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(3, 2)]
    for left in roots:
        for right in roots:
            expected = (left+right > 1)-(left+right < 1)
            assert radical_sum_sign(left**2, right**2) == expected
    for p, q in [(Q(-1), Q(0)), (Q(0), Q(-1))]:
        try:
            radical_sum_sign(p, q)
        except ValueError:
            pass
        else:
            raise AssertionError("negative radicand accepted")
    for alpha in (AL, (AL+AH)/2, AH):
        A = 1+alpha
        assert endpoint_signs(A, U0, E0) == (-1, -1)
        assert endpoint_signs(A, A/3, E0) == (-1, 1)
        assert endpoint_signs(A, Q(1, 2), E0) == (1, 1)
    print("PASS sign-safe radical oracle: 49 square-root cases including ties; "
          "2 invalid inputs; 9 chord/mixed/chain endpoint probes")

    # Independent affine pullbacks for both high marginals; reflection twice.
    B = 1+(AL+AH)/2+U0
    direct = add(poly([B]), scale(R, E0))
    reflected = add(poly([B]), scale(RBAR, E0))
    assert add(ONE, scale(RBAR, -1)) == R
    for degree in range(9):
        assert integral(power(direct, degree)) == integral(power(reflected, degree))
    assert integral(ONE) == 1
    print("PASS reflection pullbacks: moments 0..8, mass and involution; "
          "conditional balance is the exact coordinate swap in the proof")

    chord = jet_mul(root_jet(R), root_jet(RBAR))
    difference = jet_add(chord, jet_scale([ONE, R, ZERO], -1))
    assert [integral(term) for term in difference] == [0, 0, Q(-1, 24)]
    # The generic chain coefficient is checked at three exact positive pairs.
    for u, B in [(Q(1, 3), Q(7, 5)), (Q(1, 2), Q(8, 5)), (Q(2, 5), Q(8, 5))]:
        high_difference = jet_add(root_jet(scale(RBAR, 1/B)),
                                  jet_scale(root_jet(scale(R, 1/B)), -1))
        chain = jet_mul(root_jet(scale(R, 1/u)), high_difference)
        assert [integral(term) for term in chain] == [0, 0, -Q(1)/(24*u*B)]
    assert integral(power(add(scale(R, 2), poly([-1])), 2)) == Q(1, 3)
    assert integral(power(add(R, poly([Q(-1, 2)])), 2)) == Q(1, 12)
    print("PASS formal Taylor algebra: chord moment -1/24; "
          "3 chain coefficients -1/(24*u*B); both rationalization moments")

    high_r = root_jet(scale(R, Q(1, 4)))
    high_ref = root_jet(scale(RBAR, Q(1, 4)))
    switch_chord = jet_scale(jet_mul(high_r, high_ref), 4)
    switch_chain = jet_scale(jet_mul(root_jet(R), jet_add(high_r, high_ref)), 2)
    switch = jet_add(switch_chord, jet_scale(switch_chain, -1))
    assert switch[0] == ZERO and switch[1] == poly([Q(1, 4), -2])
    crossing = Q(1, 8)
    assert switch[1][0]+switch[1][1]*crossing == 0
    assert integral(switch[1], right=crossing) == Q(1, 64)
    assert Q(1, 8)+Q(29, 16) == Q(31, 16) < 2
    assert 1+Q(1, 48) == Q(49, 48)
    assert Q(1, 64)-Q(49, 48*128) == Q(47, 6144) > 0
    print("PASS switch: scaled root 1/8; positive-part moment 1/64; "
          "remainder 49/48; explicit positive margin 47/6144")

    # Independent raw-cost upper enclosure. Branches were checked above.
    # c(s) is concave: midpoint quadrature is an upper bound, not a decimal
    # approximation. A-monotonicity of the cost difference transfers the
    # AH endpoint bound to the imported alpha interval (proof Section 4).
    B = 1+AH+U0
    panels = 8
    step = E0/panels
    chord_upper = Q(0)
    assert sqrt_upper(Q(0)) == 0
    assert sqrt_upper(Q(1, 4)) == Q(1, 2)
    for index in range(panels):
        s = Q(2*index+1, 2)*step
        chord_upper += step*sqrt_upper((B+s)*(B+E0-s))
    raw_upper = chord_upper-(B*E0+E0**2/2)
    assert raw_upper < -E0**3/36
    assert 144/E0**3 == 144000000
    print("PASS independent exact cost enclosure: 8 midpoint panels with "
          "rational root upper bounds prove raw Delta<-epsilon^3/36 at A=1+AH")
    print("NOTE: exact continuum checks only; no finite recovery, "
          "new global bound, re-certification of minima or numerical optimization.")


if __name__ == "__main__":
    main()
