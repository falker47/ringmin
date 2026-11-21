"""Replay the fixed four-slab comparison using rigorous complex quadrature.

Definition: the block-cost display in the cited asymptotic preprint, integrated
with respect to its two equally weighted (transposed) orientations. Symmetry
gives one copy per slab. All arithmetic decisions about switches are rational.
"""

import re
from fractions import Fraction

from flint import acb, arb, ctx, fmpq


def exact(x):
    return fmpq(x.numerator, x.denominator)


def slab_cost(left, right, x0, y0, slope):
    # X=x0+t, Y=y0+slope*t. The legs dominate the chord exactly when
    # sqrt(t/X)+sqrt(t/Y)>=1. Both ratios increase (positive intercepts).
    def legs_dominate(t):
        p = t / (x0 + t)
        q = t / (y0 + slope * t)
        rest = 1 - p - q
        return rest <= 0 or 4 * p * q >= rest**2

    def integrate(lo, hi, legs):
        if lo == hi:
            return arb(0)

        def integrand(t, analytic):
            x = exact(x0) + t
            y = exact(y0) + slope * t
            if legs:
                return (t * x).sqrt(analytic=analytic) + (t * y).sqrt(analytic=analytic)
            return (x * y).sqrt(analytic=analytic)

        value = acb.integral(integrand, exact(lo), exact(hi))
        if not value.is_finite() or not value.imag.contains(0):
            raise ArithmeticError("quadrature failed")
        return value.real

    if legs_dominate(left):
        return integrate(left, right, True)
    if not legs_dominate(right):
        return integrate(left, right, False)
    lo, hi = left, right
    for _ in range(90):
        mid = (lo + hi) / 2
        if legs_dominate(mid):
            hi = mid
        else:
            lo = mid
    # Both branches are nonnegative and bounded by 3 for t<=1 and X,Y<=2.
    strip = arb(0).union(arb(exact(3 * (hi - lo))))
    return integrate(left, lo, False) + strip + integrate(hi, right, True)


def run(root):
    main = (root / "paper_assets/journal_p2_sidma/main.tex").read_text(encoding="utf-8")
    remark = main.split(r"\begin{remark}", 1)[1].split(r"\end{remark}", 1)[0]
    remark = remark.replace(r"\allowbreak", "").replace(" ", "").replace("\n", "")
    (alpha,) = re.findall(r"\\alpha=(0\.\d+)", remark)
    (lengths,) = re.findall(r"\((0\.\d+,0\.\d+,0\.\d+,0\.\d+)\)", remark)
    (endpoints,) = re.findall(r"\[(0\.\d+,0\.\d+)\]", remark)
    shift = Fraction(alpha)
    slabs = list(map(Fraction, lengths.split(",")))
    if not (0 <= shift < 1 and all(h > 0 for h in slabs) and sum(slabs) < 1 - shift):
        raise ValueError("slab parameters outside the transfer theorem")
    with ctx.workprec(192):
        total = arb(0)
        left = Fraction(0)
        for h in slabs:
            right = left + h
            total += slab_cost(left, right, 1 + shift, 1 + shift + left + right, -1)
            left = right
        for right, intercept in ((1 - shift, 1 + shift), (Fraction(1), shift)):
            total += slab_cost(left, right, intercept, intercept, 1)
            left = right
        value = total / (4 * arb.pi())
        lo, hi = (arb(exact(Fraction(s))) for s in endpoints.split(","))
        yield (
            "Remark 6.2 fixed four-block cost (both decimal endpoints)",
            lo < value < hi,
        )
        numbers = (root / "paper_assets/journal_p2_sidma/numbers.tex").read_text(
            encoding="utf-8"
        )
        (macro,) = re.findall(r"\\newcommand\{\\CstarUpper\}\{(\d+\.\d+)\}", numbers)
        yield (
            "Remark 6.2 strict improvement over the fixed parameter choice",
            arb(exact(Fraction(macro))) < lo,
        )
        (k,) = re.findall(r"For example, \$k=r=(\d+)\$", main)
        denominator, tolerance = re.search(
            r"gives width \$1/\((\d+)\\pi\)<(\d+\.\d+)\$", main
        ).groups()
        width = 2 / (int(k) * arb.pi())
        yield (
            "Theorem 4.1 LP width example",
            int(k) == 2 * int(denominator) and width < arb(exact(Fraction(tolerance))),
        )

        # On the square profile the integrand is t(1-t). Compare its exact
        # primitive at 0 and 1 with both occurrences of the printed bound.
        mass = Fraction(1, 2) - Fraction(1, 3)
        (abstract_denominator,) = re.findall(r"1/\((\d+)\\pi\)\\le C_2", main)
        (corollary_denominator,) = re.findall(r"C_2\\ge 1/\((\d+)\\pi\)", main)
        yield (
            "Corollary 5.6 square-profile adjacent integral",
            all(
                mass == Fraction(1, int(d))
                for d in (abstract_denominator, corollary_denominator)
            ),
        )
