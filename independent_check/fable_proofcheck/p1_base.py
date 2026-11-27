"""Paper I objects: kernel, chain sums, chain roots, the rank cycle, TeX data."""

from __future__ import annotations

import itertools
import re
from fractions import Fraction

from flint import arb

from fable_common import ROOT, ball, check, control, hull, need, not_outside, two_pi  # noqa: F401

PAPER = ROOT / "paper_assets" / "journal_p1_jogo" / "main.tex"


def theta(R, a, b) -> arb:
    """theta_R(a,b) = 2 arcsin sqrt(ab/((R+a)(R+b))) as an Arb ball."""
    R, a, b = ball(R), ball(a), ball(b)
    return 2 * (a * b / ((R + a) * (R + b))).sqrt().asin()


def chain_sum(edges, R) -> arb:
    total = arb(0)
    for a, b in edges:
        total += theta(R, a, b)
    return total


def cycle_edges(cycle):
    n = len(cycle)
    return [(cycle[i], cycle[(i + 1) % n]) for i in range(n)]


def root_bracket(edges, steps: int = 110):
    """Rational lo < hi with C(lo) > 2*pi > C(hi), by sign bisection.

    The chain sum is strictly decreasing in R, so the unique root lies in
    (lo, hi).  Every sign used is a certain Arb comparison.
    """
    tau = two_pi()
    lo = Fraction(1, 10**6)
    need(chain_sum(edges, lo) > tau, "lower start does not exceed 2*pi")
    hi = Fraction(1)
    while not chain_sum(edges, hi) < tau:
        hi *= 2
        need(hi < 10**9, "no upper start found")
    for _ in range(steps):
        mid = (lo + hi) / 2
        value = chain_sum(edges, mid)
        if value > tau:
            lo = mid
        elif value < tau:
            hi = mid
        else:
            break
    return lo, hi


def rank_cycle(N: int) -> list[int]:
    """The rank rule of Section 3 / Appendix A.1, transcribed literally."""
    H = -(-N // 2)
    A: list[int] = []
    j = 0
    while True:
        appended = False
        if 1 + 2 * j <= H:
            A.append(1 + 2 * j)
            appended = True
        if N - 1 - 2 * j > H:
            A.append(N - 1 - 2 * j)
            appended = True
        if not appended:
            break
        j += 1
    Bl: list[int] = []
    j = 0
    while True:
        appended = False
        if 2 + 2 * j <= H:
            Bl.append(2 + 2 * j)
            appended = True
        if N - 2 - 2 * j > H:
            Bl.append(N - 2 - 2 * j)
            appended = True
        if not appended:
            break
        j += 1
    return A + Bl[::-1] + [N]


def sigma(k: int, n: int) -> list[int]:
    """sigma_{k,n}: rank i replaced by k+i-1."""
    return [k + i - 1 for i in rank_cycle(n - k + 1)]


def undirected(edges) -> set[frozenset]:
    return {frozenset(e) for e in edges}


def tours(N: int):
    """One representative of every undirected Hamiltonian cycle on 1..N."""
    for perm in itertools.permutations(range(2, N + 1)):
        if perm[0] < perm[-1]:
            yield (1,) + perm


def paper_text() -> str:
    return PAPER.read_text(encoding="utf-8")


def table_body(label: str) -> list[str]:
    """Rows between \\midrule and \\bottomrule of the table carrying a label."""
    text = paper_text()
    start = text.index("\\label{%s}" % label)
    mid = text.index("\\midrule", start)
    end = text.index("\\bottomrule", mid)
    rows = [row.strip() for row in text[mid + len("\\midrule"):end].split("\\\\")]
    return [row for row in rows if row and not row.startswith("%")]


def frac(text: str) -> Fraction:
    return Fraction(text.replace(",", "").replace("$", "").strip())


def pair(text: str) -> tuple[int, int]:
    found = re.fullmatch(r"\$\((\d+),(\d+)\)\$", text.strip())
    need(found is not None, "cannot parse pair %r" % text)
    return int(found.group(1)), int(found.group(2))
