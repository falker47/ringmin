"""Exact checks for the tail-cycle and edge-splitting part of the lower bound."""

from fractions import Fraction
from itertools import permutations, product


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def numerator(total, t, weight):
    # The local floor G is this polynomial divided by 2(2-weight).
    return weight * (4 * total * t - total**2 - 2 * weight * t**2)


def tail_polynomial(r, n):
    # Six times the tail sum.
    return (n - r + 1) * (r**2 + 4 * r * n + r + n**2 - n)


def polynomial_identities():
    # After denominators are cleared, each variable in the first three
    # identities has degree at most two. A polynomial of degree <= d in
    # each variable vanishing on a (d+1)-point grid is identically zero
    # by repeated univariate interpolation. Weight 2 is a legal grid node
    # precisely because these checks contain no division by 2-weight.
    grid = range(3)
    for u, v, total, t, weight in product(grid, repeat=5):
        w = u + v
        d = 2 - weight
        gain = t * w - u * v
        lhs = 2 * d * (w - total)**2 + 4 * d * weight * gain
        rhs = (2 * numerator(total, t, weight) + d * weight * (u - v)**2
               + (d * w - 2 * (total - weight * t))**2)
        require(lhs == rhs, "base-edge completion of squares")

    for n, r, t, weight in product(grid, repeat=4):
        total = n + r
        j = weight * ((total - 1) * t - n * (r - 1))
        excess = weight * ((n - r)**2 + 4 * (n - t)
                           + 2 * weight * (r - 1 - t) * (n - t))
        require(2 * (2 - weight) * j - numerator(total, t, weight) == excess,
                "recursive floor less base floor")
        step = numerator(total, t + 1, weight) - numerator(total, t, weight)
        require(step == 2 * weight * (2 * total - weight * (2 * t + 1)),
                "increment of the base floor")

    # The candidate tail polynomial has degree at most three in each
    # variable. Check its initial value and first difference, obtained by
    # adding r(n+1) and increasing every previous summand by its label.
    for r, n in product(range(4), repeat=2):
        require(tail_polynomial(r, r) == 6 * r**2, "initial tail sum")
        step = 3 * (n - r + 1) * (n + r) + 6 * r * (n + 1)
        require(tail_polynomial(r, n + 1) - tail_polynomial(r, n) == step,
                "exact tail polynomial")


def edges(cycle):
    return list(zip(cycle, cycle[1:] + cycle[:1]))


def value(cycle):
    return sum(u * v for u, v in edges(cycle))


def check_finite():
    """Verify polynomial identities, then enumerate every unoriented 7-cycle."""
    polynomial_identities()
    n, r = 7, 5
    total = n + r
    tail_floor = sum(u * (total - u) for u in range(r, n + 1))
    weights = ((1, Fraction(1, 2), Fraction(1, 4)), (1, 1, 0))
    cutoffs = (4, 3, 1)
    lengths = [a - b for a, b in zip((r,) + cutoffs, cutoffs)]
    rows = 0
    double_inserted = seam = False
    for rest in permutations(range(1, n)):
        # Fix rotation with n first and identify the two orientations.
        if rest[0] > rest[-1]:
            continue
        rows += 1
        order = (n,) + rest
        tail = tuple(u for u in order if u >= r)
        base_value = value(tail)
        slack = {tuple(sorted((u, v))): Fraction((u + v - total)**2, 2)
                 for u, v in edges(tail)}
        require(base_value - tail_floor == sum(slack.values()), "base-cycle slack")
        gains = {}
        charges = {}
        prefix = {r: base_value}
        for t in range(r - 1, 0, -1):
            larger_tail = tuple(u for u in order if u >= t)
            index = larger_tail.index(t)
            u, v = larger_tail[index - 1], larger_tail[(index + 1) % len(larger_tail)]
            seam |= index == len(larger_tail) - 1
            double_inserted |= max(u, v) < r
            key = tuple(sorted((u, v)))
            gains[t] = t * (u + v) - u * v
            if min(u, v) >= r:
                require(key in slack, "reused original edge")
                charges[t] = slack.pop(key)
            else:
                require(t < min(u, v) < r, "recursive endpoint")
                charges[t] = 0
            prefix[t] = value(larger_tail)
            require(prefix[t] - prefix[t + 1] == gains[t], "induced tail increment")

        for row in weights:
            weight_at = {t: w for s, length, w in zip(cutoffs, lengths, row)
                         for t in range(s, s + length)}
            mixture = (1 - row[0]) * prefix[r] + sum(
                (w - next_w) * prefix[s]
                for s, w, next_w in zip(cutoffs, row, row[1:] + (0,)))
            charged = sum(charges[t] + weight_at[t] * gains[t] for t in gains)
            require(mixture == tail_floor + charged + sum(slack.values()),
                    "convex prefix telescope and one-use partition")
            floor = tail_floor
            for s, length, w in zip(cutoffs, lengths, row):
                local = Fraction(numerator(total, s, w), 2 * (2 - w))
                for t in range(s, s + length):
                    require(charges[t] + w * gains[t] >= local, "local floor")
                floor += length * local
            require(max(prefix.values()) >= mixture >= floor, "complete finite bound")
    require(rows == 360 and seam and double_inserted, "history coverage")
    return f"Finite charging: exact polynomial identities and {rows} unoriented 7-cycles x 2 weight rows."
