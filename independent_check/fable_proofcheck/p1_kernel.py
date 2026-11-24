"""Section 2-3 of Paper I: angular kernel, both arcs, anti-Monge structure."""

from __future__ import annotations

import itertools
from fractions import Fraction

from p1_base import ball, check, need, theta, two_pi

GRID = [Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(7)]


@check("P1-K1", "exact", "Lemma 2.1: squared-distance identities behind (3)")
def distance_identities():
    # Polynomial identities of degree <= 2 in each of R,a,b and 1 in c=cos A,
    # verified on a 4x4x4x3 grid (more than degree+1 points per variable).
    count = 0
    for R, a, b in itertools.product(GRID, repeat=3):
        for c in (Fraction(-1), Fraction(1, 7), Fraction(1)):
            dist2 = (R + a) ** 2 + (R + b) ** 2 - 2 * (R + a) * (R + b) * c
            half = (1 - c) / 2  # sin^2(A/2)
            need(dist2 == (a - b) ** 2 + 4 * (R + a) * (R + b) * half)
            q = a * b / ((R + a) * (R + b))
            # dist2 >= (a+b)^2  <=>  c <= 1-2q : the difference is the same
            # quantity up to the positive factor 2(R+a)(R+b).
            need(dist2 - (a + b) ** 2 == 2 * (R + a) * (R + b) * ((1 - 2 * q) - c))
            need(0 < q < 1)
            count += 1
    return "%d exact grid points" % count


@check("P1-K2", "interval", "Lemma 2.1: disjoint interiors <=> theta <= A <= 2pi-theta")
def both_arcs():
    # A is sampled through rational points (cos A, sin A) of the unit circle;
    # the geometric predicate is exact, the angular predicate uses Arb.
    count = 0
    for R, a, b in itertools.product([Fraction(1, 2), Fraction(3), Fraction(11)], [1, 2, 5], [1, 3, 8]):
        q = Fraction(a * b) / ((R + a) * (R + b))
        th = theta(R, a, b)
        for num in range(-40, 41):
            t = Fraction(num, 7)
            c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
            disjoint = c <= 1 - 2 * q  # exact
            if c == 1 - 2 * q:
                continue  # tangent sample: boundary of both predicates
            angle = (ball(s) / ball(1 + c)).atan() * 2 if c != -1 else None
            if angle is None:
                continue
            A = angle if s >= 0 else angle + two_pi()  # A in [0, 2pi)
            inside = (th < A) and (A < two_pi() - th)
            outside = (A < th) or (A > two_pi() - th)
            need(inside or outside, "undecided angular sample")
            need(inside == disjoint)
            count += 1
    return "%d rational directions agree" % count


@check("P1-K3", "interval", "Lemma 2.1: kernel symmetric, decreasing in R, increasing in each radius")
def monotone():
    count = 0
    values = [Fraction(1, 4), Fraction(1), Fraction(3), Fraction(10), Fraction(40)]
    for R, a, b in itertools.product(values, repeat=3):
        need(theta(R, a, b).overlaps(theta(R, b, a)))
        need(theta(R, a, b) > theta(R + Fraction(1, 5), a, b))
        need(theta(R, a + Fraction(1, 5), b) > theta(R, a, b))
        need(theta(R, a, b) > 0 and theta(R, a, b) < two_pi() / 2)
        count += 1
    return "%d triples" % count


@check("P1-K4", "symbolic", "(6)/(A.8): first and mixed partial derivatives of the kernel")
def derivatives():
    import sympy as sp

    R, a, b = sp.symbols("R a b", positive=True)
    th = 2 * sp.asin(sp.sqrt(a * b / ((R + a) * (R + b))))
    first = sp.sqrt(R * b / a) / ((R + a) * sp.sqrt(R + a + b))
    mixed = sp.sqrt(R) / (2 * sp.sqrt(a * b) * (R + a + b) ** sp.Rational(3, 2))
    need(sp.simplify(sp.diff(th, a) / first) == 1)
    need(sp.simplify(sp.diff(first, b) / mixed) == 1)
    # arcsin and arctan forms of the kernel agree: tan^2 = sin^2/(1-sin^2).
    s2 = a * b / ((R + a) * (R + b))
    need(sp.simplify(s2 / (1 - s2) - a * b / (R * (R + a + b))) == 0)
    # derivative in R used in Section 6.4 and Appendix C
    q = a * b / ((R + a) * (R + b))
    claimed = -sp.sqrt(q / (1 - q)) * (1 / (R + a) + 1 / (R + b))
    need(sp.simplify(sp.diff(th, R) / claimed) == 1)
    return "sympy: theta_1, theta_12, d theta/dR match the printed formulas"


@check("P1-K5", "interval", "Lemma 3.1: strict anti-Monge inequality (5), brute force")
def anti_monge():
    count = 0
    radii = [Fraction(1, 2), 1, 2, 3, 5, 8, 13, Fraction(41, 2)]
    for R in (Fraction(1, 50), Fraction(1), Fraction(9), Fraction(300)):
        table = {(x, y): theta(R, x, y) for x in radii for y in radii}
        for a, a2 in itertools.combinations(radii, 2):
            for b, b2 in itertools.combinations(radii, 2):
                # includes rectangles that meet or cross the diagonal
                need(table[a, b] + table[a2, b2] > table[a, b2] + table[a2, b])
                count += 1
    return "%d strict quadruples, diagonal included" % count
