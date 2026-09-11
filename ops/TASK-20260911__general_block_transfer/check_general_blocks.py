"""Independent bounded checks of general reflected-block integer recovery.

Run: python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py
Stdlib only; explicit checks survive -O. No production/prior-checker imports,
implicit parameter solving, angular numerics, generated outputs, or files read.
The proof, not these bounded diagnostics, supplies all-m and all-k claims.
"""

from fractions import Fraction as Q
from itertools import product
from math import isqrt


def require(condition, message):
    if not condition:
        raise ValueError(message)


def build_order(m, s, lengths):
    """Reverse explicit even-rank lists, independently of the cell formulas."""
    require(m >= 2 and 0 <= s < m, "invalid shell or shift")
    require(all(length >= 0 and length % 2 == 0 for length in lengths),
            "invalid block length")
    require(m-s-sum(lengths) >= 2, "exit/wrap gate")
    ranks = list(range(m+1))
    blocks = []
    start = 0
    for length in lengths:
        evens = list(range(start+2, start+length+1, 2))
        for rank, image in zip(evens, reversed(evens), strict=True):
            ranks[rank] = image
        blocks.append((start, length))
        start += length
    high = lambda rank: m+1+(rank+s-1) % m
    order = [None]+[high(rank) for rank in ranks[1:]]
    order[0] = order[m]
    return order, blocks


def inventory(m, s, lengths, order, blocks):
    require(sorted(order[1:]) == list(range(m+1, 2*m+1)), "permutation")
    require(order[0] == order[m], "cyclic predecessor")
    high = lambda rank: m+1+(rank+s-1) % m
    wrap = m-s
    exceptional = ({1, wrap, wrap+1}
                   | {start+length+1 for start, length in blocks if length})
    exceptional.intersection_update(range(1, m+1))
    require(len(exceptional) <= len(lengths)+3, "exception count")
    interiors = {}
    for start, length in blocks:
        for i in range(start+2, start+length+1):
            require(i not in interiors and i not in exceptional, "disjoint cells")
            interiors[i] = (start, length)
    exits = {start+length+1: (start, length)
             for start, length in blocks if length}
    for i in range(1, m+1):
        if i in interiors:
            start, length = interiors[i]
            if i % 2 == 0:
                expected = (m+s+i-1, m+s+2*start+length+2-i)
            else:
                expected = (m+s+2*start+length+3-i, m+s+i)
        elif i == 1:
            expected = (high(m), high(1))
        elif i == wrap:
            expected = (2*m-1, 2*m)
        elif i == wrap+1:
            expected = (2*m, m+1)
        elif i in exceptional:
            require(i in exits, "unclassified exceptional cell")
            start, length = exits[i]
            expected = (high(start+2), high(start+length+1))
        else:
            expected = (high(i-1), high(i))
        require((order[i-1], order[i]) == expected, "literal cell inventory")
    return exceptional, interiors


def panel_endpoints(m, s, i, start, length, reverse_orientation=False):
    """Integer coordinates: odd cell receives minus, even cell plus."""
    left = i-1 if i % 2 else i-2
    swap = bool(i % 2) != reverse_orientation
    endpoints = []
    for t in (left, left+2):
        pair = (m+s+t, m+s+2*start+length-t)
        if swap:
            pair = pair[::-1]
        endpoints.append((t, *pair))
    return endpoints


def require_panel(actual, models, bound):
    for model in models:
        require(max(abs(u-v) for u, v in zip(actual, model)) <= bound,
                "panel coordinate bound")


def panels(m, s, order, exceptional, interiors):
    reflected = ordinary = 0
    for i in range(1, m+1):
        if i in exceptional:
            continue
        actual = (i, order[i-1], order[i])
        if i in interiors:
            start, length = interiors[i]
            require_panel(actual, panel_endpoints(m, s, i, start, length), 4)
            reflected += 1
        else:
            models = [(t, m+(t+s) % m, m+(t+s) % m) for t in (i-1, i)]
            require_panel(actual, models, 1)
            ordinary += 1
    return reflected, ordinary


def sqrt_bounds(value):
    require(value >= 0, "negative radical")
    scale = 10**40
    low = Q(isqrt(value.numerator*scale**2//value.denominator), scale)
    high = low+Q(1, scale)
    require(low**2 <= value < high**2, "directed root")
    return low, high


def full_max_bounds(point):
    t, x, y = point
    require(0 <= t <= 1 and 1 <= x <= 2 and 1 <= y <= 2, "cost domain")
    tl, th = sqrt_bounds(t)
    xl, xh = sqrt_bounds(x)
    yl, yh = sqrt_bounds(y)
    cl, ch = sqrt_bounds(x*y)
    return max(tl*(xl+yl), cl), max(th*(xh+yh), ch)


def radical_probes(m, s, order, blocks, exceptional, interiors):
    indices = set(exceptional) | {m, max(1, m//2)}
    for start, length in blocks:
        if length:
            indices.update((start+2, start+length,
                            start+2*max(1, length//4)))
    raw = modulus = 0
    for i in sorted(indices):
        actual_integer = (i, order[i-1], order[i])
        actual = tuple(Q(value, m) for value in actual_integer)
        low, high = full_max_bounds(actual)
        require(1 <= low <= high < 3, "literal full-max range")
        raw += 1
        if i in exceptional:
            continue
        if i in interiors:
            start, length = interiors[i]
            models = panel_endpoints(m, s, i, start, length)
        else:
            models = [(t, m+(t+s) % m, m+(t+s) % m) for t in (i-1, i)]
        for model_integer in models:
            model = tuple(Q(value, m) for value in model_integer)
            ml, mh = full_max_bounds(model)
            distance = max(abs(u-v) for u, v in zip(actual, model))
            if distance:
                require(max(high-ml, mh-low) <= 4*distance,
                        "directed full-max Lipschitz probe")
            else:
                require(actual == model and (low, high) == (ml, mh),
                        "zero-distance cost identity")
            modulus += 1
    return raw, modulus


def rejects(call, expected_message):
    try:
        call()
    except ValueError as error:
        require(str(error) == expected_message, "wrong rejection reason")
    else:
        raise ValueError("corruption was accepted")


def main():
    orders = cells = reflected = ordinary = 0
    for m in range(2, 25):
        for s in range(m):
            for k in range(1, 5):
                for lengths in product((0, 2, 4, 6), repeat=k):
                    if m-s-sum(lengths) < 2:
                        continue
                    order, blocks = build_order(m, s, lengths)
                    exceptional, interiors = inventory(m, s, lengths, order, blocks)
                    nr, no = panels(m, s, order, exceptional, interiors)
                    orders += 1
                    cells += m
                    reflected += nr
                    ordinary += no
    require((orders, cells, reflected) == (30034, 580560, 173010),
            "original bounded-domain coverage")
    print("PASS exact small domain:", orders, "orders;", cells, "cells;",
          reflected, "reflected and", ordinary, "ordinary panel assignments")

    # Interior rational surrogates: these are NOT the implicitly defined
    # parameters. No finite floor claim about an exact minimizer is inferred.
    brackets = ((Q(1093, 10000), Q(10931, 100000)),
                (Q(719, 2500), Q(2877, 10000)),
                (Q(43, 1000), Q(7, 160)),
                (Q(29, 5000), Q(27, 4000)))
    eta = Q(1, 20000)
    large_orders = large_cells = raw = modulus = 0
    expected_fourth = {39999: 0, 40000: 2, 40001: 2,
                       79999: 2, 80000: 4, 80001: 4}
    for weight in (Q(1, 4), Q(1, 2), Q(3, 4)):
        params = tuple(lo+(hi-lo)*weight for lo, hi in brackets)
        require(all(lo < value < hi for value, (lo, hi) in zip(params, brackets)),
                "surrogate outside strict bracket")
        alpha, x, epsilon, delta = params
        lengths_real = ((1+alpha)*x, epsilon, delta, eta)
        require(alpha+sum(lengths_real) < Q(1, 2), "surrogate geometric gate")
        for m, last_length in expected_fourth.items():
            shift = (alpha*m).__floor__()
            lengths = tuple(2*(length*m/2).__floor__() for length in lengths_real)
            require(lengths[-1] == last_length, "fourth-block onset floor")
            order, blocks = build_order(m, shift, lengths)
            exceptional, interiors = inventory(m, shift, lengths, order, blocks)
            panels(m, shift, order, exceptional, interiors)
            nr, nm = radical_probes(m, shift, order, blocks, exceptional, interiors)
            raw += nr
            modulus += nm
            large_orders += 1
            large_cells += m
    print("PASS rational-surrogate diagnostics:", large_orders, "orders;",
          large_cells, "cells; fourth lengths 0,2,2,2,4,4")
    print("PASS directed literal full max:", raw, "probes;", modulus,
          "panel Lipschitz probes")

    m, shift, lengths = 32, 1, (12, 6, 0, 0)
    order, blocks = build_order(m, shift, lengths)
    duplicate = order.copy()
    duplicate[1] = duplicate[2]
    rejects(lambda: inventory(m, shift, lengths, duplicate, blocks), "permutation")
    predecessor = order.copy()
    predecessor[0] = predecessor[1]
    rejects(lambda: inventory(m, shift, lengths, predecessor, blocks),
            "cyclic predecessor")
    actual = (3, order[2], order[3])
    wrong_panel = panel_endpoints(m, shift, 3, 0, 12, reverse_orientation=True)
    rejects(lambda: require_panel(actual, wrong_panel, 4), "panel coordinate bound")
    rejects(lambda: sqrt_bounds(Q(-1)), "negative radical")
    print("PASS 4 negative controls: duplicate high, cyclic predecessor,",
          "reversed panel orientation, negative radical")
    print("NOTE finite arithmetic and rational-surrogate diagnostics only;")
    print("analytic proof supplies arbitrary parameters/k/m, full geometry and limits")


if __name__ == "__main__":
    main()
