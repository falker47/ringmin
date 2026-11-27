"""Paper II (supplement S1, lemmas L1-L8): constants and finite objects.

Nothing here is copied from a saved numerical result.  tau, q and pi come
from Arb; the manuscript ``supplement.tex`` is read only for the printed
decimals that are being checked.
"""

from __future__ import annotations

import re
from fractions import Fraction

from flint import acb, arb

from fable_common import ROOT, ball, check, control, hull, need, not_outside, two_pi  # noqa: F401

SUPPLEMENT = ROOT / "paper_assets" / "journal_p2_sidma" / "supplement.tex"
MAIN = ROOT / "paper_assets" / "journal_p2_sidma" / "main.tex"

BETA = (Fraction(2091, 10000), Fraction(10907, 50000), Fraction(23, 100))
WIDTH_A = BETA[1] - BETA[0]
WIDTH_B = BETA[2] - BETA[1]


def exact(x: arb) -> Fraction:
    """Fraction equal to an exact (zero-radius) Arb number."""
    man, exp = x.man_exp()
    return Fraction(int(man)) * Fraction(2) ** int(exp)


def supplement_text() -> str:
    return SUPPLEMENT.read_text(encoding="utf-8")


def printed(name: str) -> Fraction:
    """A decimal printed as ``name=0.123...`` (TeX alignment allowed)."""
    found = re.search(re.escape(name) + r"&?=(\d+\.\d+)", supplement_text())
    need(found is not None, "constant %s not found in the supplement" % name)
    return Fraction(found.group(1))


def _tau_bracket():
    lo, hi = Fraction(0), Fraction(1)
    for _ in range(230):
        mid = (lo + hi) / 2
        value = ball(mid).cos() - ball(mid)
        if value > 0:
            lo = mid
        elif value < 0:
            hi = mid
        else:
            break
    return lo, hi


TAU_LO, TAU_HI = _tau_bracket()      # cos t - t is strictly decreasing on (0,1)
TAU = hull(TAU_LO, TAU_HI)
SIN_TAU = TAU.sin()
Q = (1 - SIN_TAU) / (1 + SIN_TAU)
Q_LO, Q_HI = exact(Q.lower()), exact(Q.upper())
C_TERM = TAU * (1 + Q) / two_pi()


def floor_q(n: int) -> int:
    """k = floor(q n), certified by the rational bracket of q."""
    k = (Q_LO * n).__floor__()
    need(k == (Q_HI * n).__floor__(), "floor(q n) is not decided at n=%d" % n)
    return k


def theta(R, u, v) -> arb:
    R, u, v = ball(R), ball(u), ball(v)
    return 2 * (u * v / ((R + u) * (R + v))).sqrt().asin()


def cycle_edges(cycle):
    m = len(cycle)
    return [(cycle[i], cycle[(i + 1) % m]) for i in range(m)]


def chain_sum(cycle, R) -> arb:
    total = arb(0)
    for u, v in cycle_edges(cycle):
        total += theta(R, u, v)
    return total


def rank_cycle(N: int) -> list[int]:
    """Supnick rank cycle 1, N-1, 3, N-3, ..., N-2, 2, N (all edge sums N, N+1 or N+2)."""
    H = -(-N // 2)
    A, Bl = [], []
    for out, low0, high0 in ((A, 1, N - 1), (Bl, 2, N - 2)):
        j = 0
        while True:
            appended = False
            if low0 + 2 * j <= H:
                out.append(low0 + 2 * j)
                appended = True
            if high0 - 2 * j > H:
                out.append(high0 - 2 * j)
                appended = True
            if not appended:
                break
            j += 1
    return A + Bl[::-1] + [N]


def supnick(labels):
    """Supnick order on a list of distinct labels (the small-energy regime of L3)."""
    labels = sorted(labels)
    return [labels[i - 1] for i in rank_cycle(len(labels))]


def integral(function, a, b) -> arb:
    """Rigorous quadrature (Arb's acb_calc_integrate) of a real integrand."""
    value = acb.integral(function, acb(ball(a)), acb(ball(b)))
    need(value.imag.contains(0))
    return value.real


def defect_integrand(r):
    """x -> 1+r-x - 2 sqrt(x(1+r-x)), holomorphic near (0, 1+r)."""
    r = ball(r)
    return lambda z, analytic: 1 + r - z - 2 * (z * (1 + r - z)).sqrt(analytic=analytic)


class Order:
    """The finite objects of Sections SM4-SM5 for one cyclic order of k..n."""

    def __init__(self, n: int, cycle):
        self.n = n
        self.k = floor_q(n)
        need(sorted(cycle) == list(range(self.k, n + 1)), "not a cyclic order of k..n")
        self.cycle = list(cycle)
        self.alpha = Fraction(self.k, n)
        self.s = 1 + self.alpha
        self.edges = cycle_edges(self.cycle)
        n_ = Fraction(n)
        self.E = sum(((Fraction(u + v, n) - self.s) ** 2 for u, v in self.edges), Fraction(0)) / n_
        self.W0 = self.cost(self.cycle)
        self.Jn = sum((self.f(Fraction(j, n), self.s - Fraction(j, n)) for j in range(self.k, n + 1)), arb(0)) / n
        self.e = self.W0 - self.Jn

    @staticmethod
    def f(x, y) -> arb:
        return (ball(x) * ball(y)).sqrt()

    def cost(self, cycle) -> arb:
        return sum((self.f(Fraction(u, self.n), Fraction(v, self.n)) for u, v in cycle_edges(cycle)), arb(0)) / self.n

    def D_alpha(self, x) -> arb:
        return ball(self.s - x) - 2 * self.f(x, self.s - x)

    def p(self, x) -> arb:
        return (1 - (ball(x) / ball(self.s - x)).sqrt()) / 2

    def cut(self, beta):
        """All quantities of Section SM5 at the cutoff l = floor(beta n)."""
        n, s = self.n, self.s
        ell = (Fraction(beta) * n).__floor__()
        B = Fraction(2 * ell - 1, 2 * n)
        survivors = [v for v in self.cycle if v >= ell]
        W = self.cost(survivors)
        Dn = sum((self.D_alpha(Fraction(j, n)) for j in range(self.k, ell)), arb(0)) / n
        neighbours = {}
        m = len(self.cycle)
        for i, v in enumerate(self.cycle):
            neighbours[v] = (self.cycle[i - 1], self.cycle[(i + 1) % m])
        Lam = arb(0)
        for v in range(self.k, ell):
            x = Fraction(v, n)
            Lam += self.p(x) * ball(sum(x + Fraction(y, n) - s for y in neighbours[v]))
        Lam /= n
        K = Fraction(0)
        for u, v in self.edges:
            for x, y in ((u, v), (v, u)):
                xx, z = Fraction(x, n), s - Fraction(y, n)
                if (xx - B) * (z - B) < 0:
                    K += abs(xx - z)
        K /= 2 * n
        return {"ell": ell, "B": B, "W": W, "Dn": Dn, "Delta": W - self.W0 - Dn, "Lambda": Lam,
                "K": K, "survivors": survivors, "gamma": Fraction(ell, n)}


def D_closed(beta) -> arb:
    """D(beta) = int_q^beta [1+q-x - 2 sqrt(x(1+q-x))] dx by the arcsine primitive.

    With sin(phi) = (2x-s)/s, s = 1+q, the lower limit x = q is phi = -tau.
    """
    s = 1 + Q
    beta_ = ball(beta)
    y = (2 * beta_ - s) / s
    radical = s * s / 8 * (y.asin() + y * (1 - y * y).sqrt() + TAU + SIN_TAU * TAU)
    return s * (beta_ - Q) - (beta_ * beta_ - Q * Q) / 2 - 2 * radical


def D_quadrature(beta) -> arb:
    """The same integral by rigorous quadrature on [Q_LO, beta].

    The sliver between Q_LO and q is bounded by its length times max|integrand| <= 2.
    """
    value = integral(defect_integrand(Q), Q_LO, beta)
    sliver = 2 * ball(Q_HI - Q_LO)
    return value + sliver * arb(0).union(arb(-1))
