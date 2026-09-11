"""Bounded independent exact checks for the global line recovery proof.

Uses only the Python standard library. Square marks make every separation
weight rational. This checks finite arithmetic cores, not the infinite-limit
theorem or the production finite certificates. All guards survive python -O.
"""

from fractions import Fraction
from itertools import combinations, product


class CheckFailure(RuntimeError):
    """An exact verification guard failed."""


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


def minimum_positions(roots):
    positions = [Fraction(0)]
    for i in range(1, len(roots)):
        positions.append(
            max(positions[j] + roots[i] * roots[j] for j in range(i))
        )
    return positions


def verify_line(roots, positions):
    require(len(roots) == len(positions), "line cardinality mismatch")
    for i, j in combinations(range(len(roots)), 2):
        require(
            positions[j] - positions[i] >= roots[i] * roots[j],
            f"line pair {(i, j)} violates its separation",
        )


def verify_circle(roots, positions, circumference):
    verify_line(roots, positions)
    for i, j in combinations(range(len(roots)), 2):
        require(
            circumference - positions[j] + positions[i] >= roots[i] * roots[j],
            f"complementary arc for pair {(i, j)} violates its separation",
        )


def verify_reassignment(source_marks, labels):
    size = len(source_marks)
    require(
        sorted(labels) == [Fraction(i, size) for i in range(1, size + 1)],
        "assigned labels are not the genuine uniform-label multiset",
    )
    for i, (source, label) in enumerate(zip(source_marks, labels)):
        require(source >= label, f"reassignment increases mark at index {i}")


def must_reject(name, check):
    try:
        check()
    except CheckFailure:
        return
    raise CheckFailure(f"negative control accepted: {name}")


def main():
    alphabet = (Fraction(0), Fraction(1, 2), Fraction(1))
    words = paths = pairs = concatenations = quantiles = 0
    for size in range(2, 7):
        for roots in product(alphabet, repeat=size):
            positions = minimum_positions(roots)
            verify_circle(roots, positions, positions[-1] + 1)
            pairs += size * (size - 1) // 2

            # Independent oracle: enumerate every increasing-index path,
            # without calling the recurrence for its value.
            longest = Fraction(0)
            for bits in product((0, 1), repeat=size - 2):
                indices = [0] + [i + 1 for i, bit in enumerate(bits) if bit]
                indices.append(size - 1)
                cost = sum(
                    (roots[i] * roots[j] for i, j in zip(indices, indices[1:])),
                    Fraction(0),
                )
                longest = max(longest, cost)
                paths += 1
            require(longest == positions[-1], "path/recurrence disagreement")
            require(
                minimum_positions(roots[::-1])[-1] == positions[-1],
                "reversal changes minimum span",
            )

            # Directly verify every pair after a two-block concatenation.
            joined = positions + [x + positions[-1] + 1 for x in positions]
            verify_line(roots + roots, joined)
            require(joined[-1] == 2 * (positions[-1] + 1) - 1, "join span")
            concatenations += 1
            words += 1

    for template_size in range(2, 21):
        for target_size in range(template_size, 101):
            copies = (target_size + template_size - 1) // template_size
            retained = sorted(
                Fraction(j, template_size)
                for j in range(1, template_size + 1)
                for _ in range(copies)
            )[:target_size]
            scale = Fraction(template_size * copies, target_size)
            labels = [Fraction(i, target_size) for i in range(1, target_size + 1)]
            verify_reassignment([scale * mark for mark in retained], labels)
            for i, mark in enumerate(retained, 1):
                require(
                    mark == Fraction((i + copies - 1) // copies, template_size),
                    "retained quantile formula disagrees with actual copies",
                )
                quantiles += 1

    must_reject(
        "omitted nonadjacent constraint",
        lambda: verify_line((Fraction(1), Fraction(0), Fraction(1)), [0, 0, 0]),
    )
    must_reject(
        "missing closing gap",
        lambda: verify_circle((Fraction(1), Fraction(1)), [0, 1], 1),
    )
    must_reject(
        "invalid quantile reassignment",
        lambda: verify_reassignment(
            [Fraction(1, 2), Fraction(1)], [Fraction(1), Fraction(1, 2)]
        ),
    )
    must_reject(
        "omitted quantile scale",
        lambda: verify_reassignment(
            [Fraction(1, 2), Fraction(1, 2), Fraction(1)],
            [Fraction(1, 3), Fraction(2, 3), Fraction(1)],
        ),
    )
    print(
        f"PASS: {words} rational words; {paths} independent paths; "
        f"{pairs} pair/closure checks; {concatenations} all-pair concatenations; "
        f"{quantiles} genuine-label quantiles; 4 negative controls rejected."
    )


if __name__ == "__main__":
    main()
