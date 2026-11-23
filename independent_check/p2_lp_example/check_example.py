"""Check the square-quantile finite-word LP examples for Paper II.

Run `python independent_check/p2_lp_example/check_example.py` from the repo root.
The witnesses in certificates.json were found by solving the finite LPs
numerically. This replay needs only the Python standard library. It proves
optimality from the rational witnesses, integer longest-path costs and every
indexed word inequality. Large-grid rows report only the theorem's width and
the size of the LP; no costs or optima are evaluated for those grids.
"""
import argparse
import json
from fractions import Fraction
from itertools import product
from math import lcm
from pathlib import Path


def scaled_span(word):
    """Return k² times the span for marks (j/k)²; every edge has weight i*j."""
    positions = [0]
    for i in range(1, len(word)):
        positions.append(max(positions[j] + word[j] * word[i] for j in range(i)))
    return positions[-1]


def verify_certificate(certificate):
    """Return the exact optimum after verifying the primal and dual witnesses."""
    k, r = certificate["k"], certificate["r"]
    if k < 1 or r < 2:
        raise ValueError("the finite-word LP requires k >= 1 and r >= 2")
    total_weight = Fraction(0)
    counts = [Fraction(0) for _ in range(k)]
    weighted_span = Fraction(0)
    for atom in certificate["primal"]:
        word, weight = atom["word"], Fraction(atom["weight"])
        if len(word) != r or any(type(j) is not int or not 1 <= j <= k for j in word):
            raise ValueError(f"invalid indexed word: {word}")
        if weight < 0:
            raise ValueError(f"negative primal weight for {word}")
        total_weight += weight
        for j in word:
            counts[j - 1] += weight
        weighted_span += weight * scaled_span(word)
    if total_weight != 1 or any(total != Fraction(r, k) for total in counts):
        raise ValueError("primal mass or type balance is incorrect")

    y0 = Fraction(certificate["dual"]["y0"])
    y = [Fraction(value) for value in certificate["dual"]["y"]]
    if len(y) != k:
        raise ValueError("expected one dual price for each indexed type")
    # Multiply the paper's inequalities by a common positive denominator.
    # The cost coefficient is 1/(k²r), since scaled_span returns k² times ℓ.
    cost_denominator = k * k * r
    scale = lcm(cost_denominator, y0.denominator, *(price.denominator for price in y))
    offset = int(scale * y0)
    prices = [int(scale * price) for price in y]
    cost_factor = scale // cost_denominator
    for word in product(range(1, k + 1), repeat=r):
        if offset + sum(prices[j - 1] for j in word) > cost_factor * scaled_span(word):
            raise ValueError(f"dual constraint violated at {word}")

    primal = weighted_span / cost_denominator
    dual = y0 + Fraction(r, k) * sum(y)
    if primal != dual:
        raise ValueError(f"primal {primal} and dual {dual} differ")
    return primal


def table_rows():
    data = json.loads(Path(__file__).with_name("certificates.json").read_text(encoding="utf-8"))
    for certificate in data["certificates"]:
        k, r = certificate["k"], certificate["r"]
        optimum = verify_certificate(certificate)
        lower = optimum - Fraction(1, k)
        upper = optimum + Fraction(1, r)
        yield k, r, k**r, optimum, lower, upper, upper - lower
    for k, r in ((16, 16), (64, 64)):
        width = Fraction(1, k) + Fraction(1, r)
        yield k, r, f"{k}^{{{r}}}", None, None, None, width


def latex_row(k, r, words, optimum, lower, upper, width):
    value = "---" if optimum is None else f"${optimum}$"
    interval = "---" if optimum is None else f"$[{lower},{upper}]$"
    return rf"{k} & {r} & ${words}$ & {value} & {interval} & ${width}$ \\"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--latex", action="store_true", help="print the article's tabular rows")
    options = parser.parse_args()
    if not options.latex:
        print("k | r | words | lambda | pi*lower | pi*upper | pi*width")
    for row in table_rows():
        if options.latex:
            print(latex_row(*row))
        else:
            print(*("--" if item is None else item for item in row), sep=" | ")


if __name__ == "__main__":
    main()
