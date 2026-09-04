"""Bounded numerical falsification aid; NOT an exact or all-k certificate.

Fixed range k=6,7,8,9 covers the first indices and both cycle parities.
Every triangle and both paths for every pair are checked. No production
implementation or exact-audit module is imported. No random inputs.
"""

from itertools import combinations

import mpmath as mp


def order(k, n):
    size = n - k + 1
    half = (size + 1) // 2
    arms = []
    for offset in (1, 2):
        arm = []
        for j in range(size):
            low, high = offset + 2 * j, size - offset - 2 * j
            if low <= half:
                arm.append(low + k - 1)
            if high > half:
                arm.append(high + k - 1)
        arms.append(arm)
    return arms[0] + arms[1][::-1] + [n]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    mp.mp.dps = 80
    guard = mp.mpf("1e-60")
    print(f"NUMERICAL OBSERVATION ONLY; mpmath={mp.__version__}; dps=80")
    print("k=6..9; 300 bisections; discrepancy guard=1e-60; no seeds")
    for k in (6, 7, 8, 9):
        n = 4 * k + 5
        tour = order(k, n)
        size = len(tour)
        require(sorted(tour) == list(range(k, n + 1)), "malformed order")

        # Law-of-cosines form, separate from the analytic audit's asin form.
        def angle(radius, a, b):
            return mp.acos(1 - 2 * mp.mpf(a * b) / ((radius + a) * (radius + b)))

        def closure(radius):
            return mp.fsum(angle(radius, a, tour[(i + 1) % size])
                           for i, a in enumerate(tour))

        lo, hi = mp.mpf("1e-20"), mp.mpf(4 * size * size)
        require(closure(lo) > 2 * mp.pi > closure(hi), "root bracket")
        for _ in range(300):
            mid = (lo + hi) / 2
            if closure(mid) > 2 * mp.pi:
                lo = mid
            else:
                hi = mid
        radius = (lo + hi) / 2
        angles = {(a, b): angle(radius, a, b)
                  for a in tour for b in tour}
        delta = angles[n, k] + angles[k, n - 1] - angles[n, n - 1]
        require(delta > guard, f"nonpositive seam at k={k}")
        triangles = 0
        for a, c in combinations(range(k, n + 1), 2):
            for b in range(k, n + 1):
                if b in (a, c):
                    continue
                defect = angles[a, b] + angles[b, c] - angles[a, c]
                require(defect >= delta - guard, f"triangle {(k, a, b, c)}")
                triangles += 1

        edges = [angles[a, tour[(i + 1) % size]] for i, a in enumerate(tour)]
        closure_error = abs(mp.fsum(edges) - 2 * mp.pi)
        require(closure_error < guard, "closure residual")
        positions = [mp.fsum(edges[:i]) for i in range(size)]
        centers = [(radius + a) * mp.exp(mp.j * p)
                   for a, p in zip(tour, positions)]
        minimum, winner = mp.inf, None
        pairs, paths = 0, 0
        for i, j in combinations(range(size), 2):
            d = j - i
            required = angles[tour[i], tour[j]]
            for length, arc in ((d, edges[i:j]),
                                (size - d, edges[j:] + edges[:i])):
                slack = mp.fsum(arc) - required
                require(slack >= (length - 1) * delta - guard,
                        f"path {(k, i, j, length)}")
                paths += 1
                if 2 <= d <= size - 2 and slack < minimum:
                    minimum, winner = slack, (tour[i], tour[j], length)
            distance_margin = abs(centers[i] - centers[j]) - (tour[i] + tour[j])
            require(distance_margin >= -guard, f"Cartesian {(k, i, j)}")
            pairs += 1
        require(abs(minimum - delta) < guard, "minimum does not match seam")
        require(set(winner[:2]) == {n - 1, n} and winner[2] == 2,
                "wrong seam winner")
        print(f"k={k} N={size} R~{mp.nstr(radius, 18)} "
              f"Delta~{mp.nstr(delta, 12)} min_pair_path={winner} "
              f"triangles={triangles} pairs={pairs} paths={paths} "
              f"closure_error<{mp.nstr(guard, 2)}")
    print("PASS: bounded diagnostic only; no counterexample detected")


if __name__ == "__main__":
    main()
