"""Independent finite checks for the profile proof, using standard-library integers and Fractions."""

import argparse
import json
import re
from fractions import Fraction
from functools import cache
from itertools import combinations_with_replacement, permutations
from math import isqrt
from pathlib import Path

POWER = tuple(map(Fraction, ("0", "1/2", "1", "2", "3")))
LINEAR = (
    ("0.26086956521", "0.26086956522"), ("0.84445358956", "0.84445358957"),
    ("1.69549408120", "1.69549408121"), ("2.79491951889", "2.79491951890"),
    ("4.15318955374", "4.15318955375"), ("5.76779428458", "5.76779428459"),
    ("7.72672655261", "7.72672655262"), ("9.97990738586", "9.97990738587"),
    ("12.48872048718", "12.48872048719"), ("15.25887043044", "15.25887043045"),
    ("18.31756304721", "18.31756304722"), ("21.66539518221", "21.66539518222"),
)
QUADRATIC = (
    ("0.3832870361393696523322205393924377858638763427734375",
     "0.383487036139369685816546962087159045040607452392578125"),
    ("1.4955284118749971877804227915476076304912567138671875",
     "1.4957284118749971657535979829845018684864044189453125"),
    ("3.934227717145796443531935437931679189205169677734375",
     "3.9344277171457964215051106293685734272003173828125"),
    ("8.4678350760883720482752323732711374759674072265625",
     "8.4680350760883715821591977146454155445098876953125"),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pi_bounds():
    """Consecutive alternating-series partial sums of Machin's arctangents."""
    def atan_bounds(den):
        partial = sum(Fraction((-1)**j, (2*j + 1) * den**(2*j + 1)) for j in range(16))
        return partial, partial + Fraction(1, 33 * den**33)

    a, b = atan_bounds(5)
    c, d = atan_bounds(239)
    return 16*a - 4*d, 16*b - 4*c


def edge_bounds(i, j, n, power, scale):
    """Enclose scale*(ij/n²)^(p/2) between consecutive integers, or one exact integer."""
    exponent = power / 2
    m, d = exponent.numerator, exponent.denominator
    require(d in (1, 2, 4), "unsupported root degree")
    numerator = (i*j)**m * scale**d
    denominator = n**(2*m)
    lower = numerator // denominator
    if d >= 2:
        lower = isqrt(lower)
    if d == 4:
        lower = isqrt(lower)
    exact = lower**d * denominator == numerator
    return lower, lower if exact else lower + 1


def matrices(n, power):
    scale = n*n * (1 << 72)
    bounds = [[edge_bounds(i, j, n, power, scale) for j in range(1, n + 1)]
              for i in range(1, n + 1)]
    low = [[edge[0] for edge in row] for row in bounds]
    high = [[edge[1] for edge in row] for row in bounds]
    return scale, low, high


def path_span(word, paths, weights):
    return max(sum(weights[word[i]][word[j]] for i, j in edges) for edges in paths)


@cache
def exhaustive(n, power):
    """Enumerate every order and every increasing path, independently of the search recurrence."""
    scale, low, high = matrices(n, power)
    paths = []
    for mask in range(1 << (n - 2)):
        vertices = [0] + [j for j in range(1, n - 1) if mask & (1 << (j - 1))] + [n - 1]
        paths.append(list(zip(vertices, vertices[1:])))
    minimal_low = minimal_high = None
    for word in permutations(range(n)):
        lower = path_span(word, paths, low)
        upper = lower if power in (0, 2) else path_span(word, paths, high)
        if minimal_low is None or lower < minimal_low:
            minimal_low = lower
        if minimal_high is None or upper < minimal_high:
            minimal_high = upper
    if power in (0, 2):
        require(low == high, "failed to represent rational weights exactly")
    return Fraction(minimal_low, scale), Fraction(minimal_high, scale)


def full_recurrence(word, weights):
    coordinates = [0]
    for k in range(1, len(word)):
        coordinates.append(max(x + weights[previous][word[k]]
                               for x, previous in zip(coordinates, word[:k])))
    return coordinates


def verify_matching():
    cases = 0
    for n in (2, 3, 4):
        for m in range(1, n + 1):
            for donors in combinations_with_replacement(range(3), n):
                for targets in combinations_with_replacement(range(3), m):
                    sorted_ok = all(a <= b for a, b in zip(targets, donors[-m:]))
                    possible = any(all(a <= b for a, b in zip(targets, ordering))
                                   for ordering in permutations(donors, m))
                    require(sorted_ok == possible, f"matching case {donors}, {targets}")
                    cases += 1
    return cases


def verify_copies():
    cases = 0
    for power in POWER:
        for n in range(2, 6):
            lower, _ = exhaustive(n, power)
            for m in range(n + 1, 8):
                q = (m + n - 1) // n
                d = n*q - m
                _, upper = exhaustive(m, power)
                require(upper <= q*(lower + 1) - 1, f"copy inequality {power}, {n}, {m}")
                for i in range(1, m + 1):
                    top = Fraction((i + d + q - 1) // q, n)
                    bottom = Fraction((i + q - 1) // q, n)
                    require(top >= Fraction(i, m), "largest-donor rank")
                    require(bottom * Fraction(n*q, m) >= Fraction(i, m), "power dilation rank")
                cases += 1
    return cases


def verify_placements():
    """Build concatenations from nonmonotone words and square the all-pair inequalities."""
    cases = 0
    for power in POWER:
        for n in (2, 3, 4):
            scale, _, high = matrices(n, power)
            for raw in permutations(range(n)):
                word = list(raw)
                positions = full_recurrence(word, high)
                for m in (n + 1, 2*n, 2*n + 1):
                    q = (m + n - 1) // n
                    donors = sorted((label, copy, x + copy * (positions[-1] + scale))
                                    for copy in range(q) for label, x in zip(word, positions))
                    coordinates = [datum[2] for datum in donors[-m:]]
                    exponent = power / 2
                    top, bottom = exponent.numerator, exponent.denominator
                    for j in range(1, m):
                        for i in range(j):
                            delta = abs(coordinates[i] - coordinates[j])
                            require(delta**bottom * m**(2*top)
                                    >= scale**bottom * ((i + 1)*(j + 1))**top,
                                    f"pair in copied placement {power}, {raw}, {m}, {i}, {j}")
                    cases += 1
    return cases


@cache
def exact_square_span(roots):
    """Independent all-orders span when marks are squares of the supplied rationals."""
    best = None
    for order in set(permutations(roots)):
        positions = [0]
        for k in range(1, len(order)):
            positions.append(max(positions[j] + order[j]*order[k] for j in range(k)))
        if best is None or positions[-1] < best:
            best = positions[-1]
    return best


def verify_stability():
    roots = tuple(map(Fraction, ("0", "1/2", "1")))
    arrays = list(combinations_with_replacement(roots, 4))
    for a in arrays:
        for c in arrays:
            delta = abs(exact_square_span(a) - exact_square_span(c))
            require(delta <= 2 * sum(abs(x - y) for x, y in zip(a, c)), "square-root stability")
    return len(arrays)**2


def verify_word_lp():
    # For two equally frequent types and length two, the mixed word achieves st/2.
    cases = 0
    for s, t in ((0, 1), (Fraction(1, 2), 1), (1, 1), (Fraction(1, 2), 2)):
        s, t = Fraction(s), Fraction(t)
        roots = (s, t)
        target = s*t/2
        dual = (s*s/4, target - s*s/4)
        require(sum(dual) == target, "dual objective")
        for i in (0, 1):
            for j in (0, 1):
                require(dual[i] + dual[j] <= roots[i]*roots[j]/2, "word dual inequality")
        # At any q the 2q vertices partition into complete 2-letter words.
        for q in (1, 2, 3):
            span = exact_square_span((s,)*q + (t,)*q)
            require(target <= span/(2*q) <= target + t*t/2, "finite balanced-word bound")
            cases += 1
    return cases


def verify_squeeze():
    pi_low, pi_high = pi_bounds()
    cases = 0
    for power, table in ((1, LINEAR), (2, QUADRATIC)):
        for n, row in enumerate(table, 3):
            if n <= 7:
                b_low, b_high = exhaustive(n, Fraction(power))
            else:
                scale, low, high = matrices(n, Fraction(power))
                # A reverse pairing is a lower bound after paying one closing edge.
                b_low = Fraction(sum(low[i][n - 1 - i] for i in range(n)), scale) - 1
                b_high = Fraction(full_recurrence(list(range(n)), high)[-1], scale)
            left, right = map(Fraction, row)
            norm = n**(power + 1)
            require(b_high / (pi_low*n) - Fraction(1, n) <= left / norm,
                    f"lower squeeze p={power} n={n}")
            require(right / norm <= (b_low + 1) / (pi_high*n),
                    f"upper squeeze p={power} n={n}")
            cases += 1
    return cases


def verify_sources(folder):
    manuscript = (folder / "arxiv" / "p1_v4" / "bracket_rows.tex").read_text(encoding="utf-8")
    rows = re.findall(r"(?m)^(\d+) & ([0-9.]+) & ([0-9.]+) &", manuscript)
    require(rows == [(str(n), low, high) for n, (low, high) in enumerate(LINEAR, 3)],
            "Paper I bracket rows differ from reference input")
    examples = folder / "ringmin-squared" / "examples"
    for n, endpoints in enumerate(QUADRATIC, 3):
        data = json.loads((examples / f"small_n_interval_certificate_n{n}.json").read_text())
        require(data["instance"]["n"] == n, "wrong quadratic size")
        lower, upper = (data["result"][f"global_{which}_bound"] for which in ("lower", "upper"))
        require((lower["radius_decimal"], upper["radius_decimal"]) == endpoints,
                "quadratic bracket differs from source")
        require(lower["included"] is False and upper["included"] is True, "endpoint semantics")
    return len(rows) + len(QUADRATIC)


def verify_observations(path):
    pi_low, pi_high = pi_bounds()
    rows = json.loads(path.read_text(encoding="utf-8"), parse_float=Fraction)
    require(tuple(Fraction(row["power"]) for row in rows) == POWER, "power inventory")
    for row in rows:
        n, labels, power = row["n"], row["order"], Fraction(row["power"])
        require(type(n) is int and 2 <= n <= 4096, "invalid observation size")
        require(all(type(i) is int for i in labels) and sorted(labels) == list(range(1, n + 1)),
                "invalid observation word")
        scale, low, high = matrices(n, power)
        word = [label - 1 for label in labels]
        lower = Fraction(full_recurrence(word, low)[-1] + scale, scale*n) / pi_high
        upper = Fraction(full_recurrence(word, high)[-1] + scale, scale*n) / pi_low
        # The displayed ten decimals must agree with the independent enclosure.
        def rounded(x):
            return (2*x.numerator*10**10 + x.denominator) // (2*x.denominator)
        require(rounded(lower) == rounded(upper) == rounded(row["score"]),
                f"displayed decimal differs, p={power}")
        print(f"p={power} verified score x 10^10, rounded = {rounded(lower)}")
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path)
    parser.add_argument("--observations", type=Path)
    args = parser.parse_args()
    print(f"matching={verify_matching()} copies={verify_copies()} "
          f"placements={verify_placements()} squeeze={verify_squeeze()} "
          f"stability={verify_stability()} word_lp={verify_word_lp()}")
    if args.sources:
        print(f"source_brackets={verify_sources(args.sources)}")
    if args.observations:
        print(f"independent_word_scores={verify_observations(args.observations)}")
    print("PASS_PROFILE_FINITE")


if __name__ == "__main__":
    main()
