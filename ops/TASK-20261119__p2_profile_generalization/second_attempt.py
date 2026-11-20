"""Independent finite controls for the second profile-proof attempt."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import ceil, floor


def word_span(roots):
    """Enumerate every path, including both ends, for square-root marks."""
    last = len(roots) - 1
    best = 0
    for count in range(last):
        for interior in combinations(range(1, last), count):
            path = (0, *interior, last)
            weight = sum(roots[i] * roots[j] for i, j in zip(path, path[1:]))
            best = max(best, weight)
    return best


def finite_stability():
    arrays = pairs = 0
    for size in range(2, 7):
        minima = {}
        for marks in combinations_with_replacement(range(4), size):
            minima[marks] = min(word_span(order) for order in set(permutations(marks)))
        arrays += len(minima)
        for a, span_a in minima.items():
            assert span_a + 9 >= sum(x*y for x, y in zip(a, reversed(a)))
            for c, span_c in minima.items():
                assert abs(span_a-span_c) <= 6*sum(abs(x-y) for x, y in zip(a, c))
                pairs += 1
    return arrays, pairs


def binary_laws():
    comparisons = 0
    for denominator in range(1, 22):
        for numerator in range(denominator + 1):
            atom = Fraction(numerator, denominator)
            energy = 1-atom
            for types in range(1, 13):
                positive = Fraction(types-floor(types*atom), types)
                for word_length in range(2, 12):
                    joining_cost = Fraction(1, word_length)
                    lp = max(positive-joining_cost, 0)
                    assert lp-Fraction(1, types) <= energy <= lp+joining_cost
                    comparisons += 1
    return comparisons


def donor_ranks():
    comparisons = 0
    for size in range(2, 31):
        for target in range(size, 3*size+1):
            copies = ceil(Fraction(target, size))
            discarded = size*copies-target
            for rank in range(1, target+1):
                donor = ceil(Fraction(rank+discarded, copies))
                assert Fraction(donor, size) >= Fraction(rank, target)
                comparisons += 1
    return comparisons


if __name__ == "__main__":
    arrays, pairs = finite_stability()
    print("EXHAUSTIVE_ROOT_ARRAYS", arrays, "STABILITY", pairs, "REVERSE_PAIR", arrays)
    print("BINARY_ATOMIC_LP", binary_laws())
    print("TOP_DONOR_COMPARISONS", donor_ranks())
