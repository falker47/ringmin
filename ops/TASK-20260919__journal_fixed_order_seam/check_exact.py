"""Bounded independent audit of the journal seam package, not a proof assistant.

No production imports, numerical solver, saved root, or old checker is used.
Default: stdlib exact arithmetic. --symbolic: additionally require SymPy.
Every gate remains active under python -O.
"""

from collections import Counter
from fractions import Fraction as F
from math import isqrt
import argparse


def require(ok, message):
    if not ok:
        raise ValueError(message)


def tour(k, n):
    size = n - k + 1
    half = (size + 1) // 2
    lists = []
    for offset in (1, 2):
        seq = []
        for j in range(size):
            low, high = offset + 2 * j, size - offset - 2 * j
            if low <= half:
                seq.append(low)
            if high > half:
                seq.append(high)
        lists.append(seq)
    return [k + i - 1 for i in lists[0] + lists[1][::-1] + [size]]


def edge(a, b):
    return tuple(sorted((a, b)))


def edges(k, n):
    size, total = n - k + 1, n + k
    h = size // 2
    out = [(k, n)]
    if size % 2 == 0:
        out += [(k + h - 1, k + h)]
        low_stop, high_stop = k + h - 1, k + h
    else:
        low_stop, high_stop = k + h, k + h + 1
    out += [(i, total - 1 - i) for i in range(k, low_stop)]
    out += [(i, total + 1 - i) for i in range(k + 1, high_stop)]
    return out


# Publication table, in the parity edge-list order (not tour traversal order).
ROWS = [
    (1, 7, F(6), 100, [28, 27, 34, 37, 37, 41, 43], "upper", F(741, 250)),
    (1, 8, F(51, 10), 1000, [316, 466, 307, 390, 428, 414, 462, 487], "lower", F(327, 100)),
    (2, 12, F(17), 1000, [209, 204, 236, 257, 270, 276, 250, 274, 291, 301, 306], "upper", F(1457520693, 500000000)),
    (2, 13, F(14), 1000, [245, 348, 240, 278, 304, 320, 330, 291, 320, 340, 353, 361], "lower", F(373, 100)),
    (3, 16, F(32), 100, [17, 23, 17, 19, 20, 21, 22, 22, 20, 21, 22, 23, 24, 24], "upper", F(14885133, 5000000)),
    (3, 17, F(32), 100, [17, 16, 18, 20, 21, 22, 22, 22, 19, 21, 22, 23, 24, 24, 24], "lower", F(63, 20)),
]


def atan_poly(x, terms):
    return sum(((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                for j in range(terms)), F(0))


PI_LO = 16 * atan_poly(F(1, 5), 10) - 4 * atan_poly(F(1, 239), 3)
PI_HI = 16 * atan_poly(F(1, 5), 11) - 4 * atan_poly(F(1, 239), 2)


def sqrt_bounds(value):
    scale = 1 << 65
    low = isqrt(value.numerator * scale * scale // value.denominator)
    return F(low, scale), F(low + 1, scale)


def half_angle_bounds(r, a, b):
    # Independent identity: half-angle = atan sqrt(ab/[r(r+a+b)]).
    square = F(a * b) / (r * (r + a + b))
    lo, hi = sqrt_bounds(square)
    if hi <= F(1, 2):
        return atan_poly(lo, 30), atan_poly(hi, 31)
    # atan(z) = pi/4 + atan((z-1)/(z+1)), with an odd signed series.
    wlo, whi = (lo - 1) / (lo + 1), (hi - 1) / (hi + 1)
    require(-F(3, 4) < wlo <= whi < F(3, 4), "atan reduction domain")

    def signed_bound(w, lower):
        if w < 0:
            return -atan_poly(-w, 31 if lower else 30)
        return atan_poly(w, 30 if lower else 31)

    return PI_LO / 4 + signed_bound(wlo, True), PI_HI / 4 + signed_bound(whi, False)


def closure_bounds(r, cycle):
    bounds = [half_angle_bounds(r, a, b) for a, b in zip(cycle, cycle[1:] + cycle[:1])]
    return sum((lo for lo, _ in bounds), F(0)), sum((hi for _, hi in bounds), F(0))


def check_bridges():
    expected_h = [F(8, 7), F(3061, 2856), F(1381, 2244), F(643, 1092), F(69, 160), F(691, 1632)]
    expected_margins = [F(4, 147), F(47737, 8156736), F(239, 5035536), F(673, 1192464), F(671, 230400), F(7465, 2663424)]
    expected_minima = [F(43, 30000), F(4333, 26270000), F(32, 359375), F(3, 32500), F(23, 70000), F(1, 5625)]
    for row_index, (k, n, r, den, nums, direction, total) in enumerate(ROWS):
        es = edges(k, n)
        require(len(es) == len(nums), "table edge count")
        qs = [F(x, den) for x in nums]
        squares = [F(a * b) / ((r + a) * (r + b)) for a, b in es]
        margins = [q * q - s if direction == "upper" else s - q * q for q, s in zip(qs, squares)]
        require(min(margins) > 0, "radical bound direction")
        require(min(margins) == expected_minima[row_index], "displayed minimum square margin")
        if direction == "upper":
            if k == 1:
                require(max(qs) < F(1, 2), "linear arcsin domain")
                got = F(6, 5) * sum(qs)
            else:
                require(max(qs) < F(1, 3), "cubic arcsin domain")
                got = sum(q + q ** 3 / 5 for q in qs)
            require(got == total < 3 < PI_LO, "upper sum")
        else:
            require(sum(qs) == total > F(22, 7) > PI_HI, "lower sum")
        alpha, beta, c = F(1, n) + F(1, n - 1), F(1, n * (n - 1)), F(1, k)
        h = c + alpha - 1 / r
        margin = 4 * (alpha * c + beta) - h * h
        if direction == "lower":
            margin = -margin
        require(h == expected_h[row_index] > 0, "threshold pre-square sign")
        require(margin == expected_margins[row_index] > 0, "threshold square margin")
        low, high = closure_bounds(r, tour(k, n))
        require(high < PI_LO if direction == "upper" else low > PI_HI, "independent atan closure")
        print(f"bridge k={k} n={n}: PASS; min square margin={min(margins)}; sum={total}; threshold margin={margin}; independent atan PASS")


def check_combinatorics():
    cycles = paths = growth = 0
    for k in range(1, 9):
        for size in range(3, 19):
            n = k + size - 1
            seq = tour(k, n)
            es = edges(k, n)
            require(sorted(seq) == list(range(k, n + 1)), "permutation")
            actual = Counter(edge(a, b) for a, b in zip(seq, seq[1:] + seq[:1]))
            require(actual == Counter(edge(a, b) for a, b in es), "rank/parity edges")
            require(seq[1] == n - 1 and seq[-1] == n, "seam neighbors")
            h = size // 2
            if size % 2:
                matched = [(a, b + 1) for a, b in es]
                added = (k + h, k + h + 1)
            else:
                central = (k + h - 1, k + h)
                matched = [(a, b) if (a, b) == central else (a, b + 1) for a, b in es]
                added = (k + h, k + h + 1)
            require(Counter(edge(a, b) for a, b in matched + [added]) ==
                    Counter(edge(a, b) for a, b in edges(k, n + 1)), "growth parity matching")
            growth += 1
            for oriented in (seq, seq[::-1]):
                for start in range(size):
                    rotated = oriented[start:] + oriented[:start]
                    for length in range(1, size):
                        path = rotated[:length + 1]
                        direct = Counter(edge(a, b) for a, b in zip(path, path[1:]))
                        direct[edge(path[0], path[-1])] -= 1
                        fan = Counter()
                        for j in range(1, length):
                            fan[edge(path[0], path[j])] += 1
                            fan[edge(path[j], path[j + 1])] += 1
                            fan[edge(path[0], path[j + 1])] -= 1
                        require(dict(+direct) == dict(+fan) and dict(-direct) == dict(-fan), "fan identity")
                        paths += 1
            cycles += 1
    print(f"combinatorics: PASS; {cycles} cycles, {growth} parity-growth matches, {paths} directed fan identities (all starts, both orientations)")
    # Exact no-threshold integer boundary: compare c-alpha with 2 sqrt(beta).
    for k in range(1, 257):
        for n in (4 * k, 4 * k + 1):
            d = F(1, k) - F(1, n) - F(1, n - 1)
            require(d > 0, "boundary pre-square sign")
            margin = d * d - F(4, n * (n - 1))
            require(margin < 0 if n == 4 * k else margin > 0, "threshold boundary")
    print("threshold domain: PASS; 512 exact boundary comparisons (k=1..256)")


def check_root_paths():
    cases = [(k, n) for k, onset in ((1, 8), (2, 13), (3, 17))
             for n in (k + 2, k + 3, onset - 1, onset)]
    total_paths = 0
    for k, n in cases:
        seq = tour(k, n)
        lo, hi = F(k, 8), F(n * n)
        require(closure_bounds(lo, seq)[0] > PI_HI, "root lower bracket")
        require(closure_bounds(hi, seq)[1] < PI_LO, "root upper bracket")
        for _ in range(38):
            middle = (lo + hi) / 2
            low, high = closure_bounds(middle, seq)
            if high < PI_LO:
                hi = middle
            elif low > PI_HI:
                lo = middle
            else:
                raise ValueError("inconclusive root enclosure; no floating fallback")
        # Kernel decreases with R, so these enclose all angles at the root.
        pair_bounds = {edge(a, b): (half_angle_bounds(hi, a, b)[0], half_angle_bounds(lo, a, b)[1])
                       for i, a in enumerate(seq) for b in seq[i + 1:]}
        onset = {1: 8, 2: 13, 3: 17}[k]
        if n < onset:
            for orientation in (seq, seq[::-1]):
                for start in range(len(seq)):
                    rotated = orientation[start:] + orientation[:start]
                    for length in range(2, len(seq)):
                        path = rotated[:length + 1]
                        lower = sum(pair_bounds[edge(a, b)][0] for a, b in zip(path, path[1:]))
                        lower -= pair_bounds[edge(path[0], path[-1])][1]
                        require(lower > 0, "nonpositive independent directed slack")
                        total_paths += 1
        else:
            upper = pair_bounds[edge(n, k)][1] + pair_bounds[edge(k, n - 1)][1] - pair_bounds[edge(n, n - 1)][0]
            require(upper < 0, "onset seam sign")
        print(f"root/pairs k={k} n={n}: PASS ({'all directed multi-edge slacks positive' if n < onset else 'seam strictly negative'})")
    print(f"independent interval roots: PASS; {len(cases)} cases, {total_paths} positive directed slacks, 3 negative seams")


def check_symbolic():
    import sympy as s
    r, a, b = s.symbols("R a b", positive=True)
    theta = 2 * s.asin(s.sqrt(a * b / ((r + a) * (r + b))))
    first = s.sqrt(r * b / a) / ((r + a) * s.sqrt(r + a + b))
    mixed = s.sqrt(r) / (2 * s.sqrt(a * b) * (r + a + b) ** s.Rational(3, 2))
    require(s.simplify(s.diff(theta, a) - first) == 0, "kernel first derivative")
    require(s.simplify(s.diff(theta, a, b) - mixed) == 0, "kernel mixed derivative")
    x, u, v, q, c, alpha, beta = s.symbols("x u v q c alpha beta")
    w = x + u + v + 2 * q
    relation = q * q - (x * u + x * v + u * v)
    expressions = [
        (x + u + q) ** 2 - (x * u + (x + u) * w),
        (x + v + q) ** 2 - (x * v + (x + v) * w),
        (x + u + q) * (x + v + q) - x * x - q * (2 * x + u + v + 2 * q),
    ]
    for expression in expressions:
        require(s.rem(s.expand(expression), relation, q) == 0, "pocket tangent identity")
    kap = c + alpha - 2 * q
    require(s.rem(s.expand(alpha * kap + beta - (q - alpha) ** 2), q * q - alpha * c - beta, q) == 0, "threshold identity")
    z = s.symbols("z")
    require(s.expand((1 + 3 * z / 5) ** 2 * (1 - z) - 1 - z * (5 - 21 * z - 9 * z * z) / 25) == 0, "arcsin bound identity")
    integral = s.integrate(z ** 4 * (1 - z) ** 4 / (1 + z * z), (z, 0, 1))
    require(s.simplify(integral - (s.Rational(22, 7) - s.pi)) == 0, "pi bound integral")
    print(f"symbolic: PASS; SymPy {s.__version__}; original-kernel derivatives, 3 pocket identities, threshold, arcsin and pi integral")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbolic", action="store_true")
    args = parser.parse_args()
    require(F(3) < PI_LO < PI_HI < F(22, 7), "pi rational enclosure")
    check_bridges()
    check_combinatorics()
    check_root_paths()
    if args.symbolic:
        check_symbolic()
    print("PASS: all requested bounded checks; analytic proof and independent review remain separate")
