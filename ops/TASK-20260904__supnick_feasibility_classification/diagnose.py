"""Bounded numerical falsification aid; NOT an exact or all-k certificate.

Fixed range k=1..12, N=3..8 and the three indices around each known onset.
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
    guard = mp.mpf("1e-55")
    print(f"NUMERICAL OBSERVATION ONLY; mpmath={mp.__version__}; dps=80")
    print("k=1..12; N=3..8 plus n=s_k-1,s_k,s_k+1; "
          "300 bisections; guard=1e-55; no seeds")
    totals = [0, 0, 0, 0, 0]  # cases, feasible, infeasible, triangles, paths
    for k in range(1, 13):
        onset = {1: 8, 2: 13, 3: 17, 4: 21, 5: 25}.get(k, 4*k+6)
        for n in sorted(set(range(k+2, k+8)) | {onset-1, onset, onset+1}):
            run_case(k, n, onset, guard, totals)
        print(f"k={k}: small cycles and both onset sides checked", flush=True)
    print(f"PASS: cases={totals[0]} feasible={totals[1]} infeasible={totals[2]} "
          f"triangles={totals[3]} directed_paths={totals[4]}")
    print("PASS: bounded diagnostic only; no counterexample detected")


def run_case(k, n, onset, guard, totals):
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
    expected_feasible = n < onset
    require(abs(delta) > guard, f"unresolved seam sign at {(k, n)}")
    require((delta > 0) == expected_feasible, f"classification sign at {(k, n)}")
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
    angular_feasible, cartesian_feasible = True, True
    pairs, paths = 0, 0
    for i, j in combinations(range(size), 2):
        d = j - i
        required = angles[tour[i], tour[j]]
        for length, arc in ((d, edges[i:j]),
                            (size - d, edges[j:] + edges[:i])):
            slack = mp.fsum(arc) - required
            require(slack >= (length - 1) * delta - guard,
                    f"path {(k, i, j, length)}")
            angular_feasible &= slack >= -guard
            paths += 1
            if 2 <= d <= size - 2 and slack < minimum:
                minimum, winner = slack, (tour[i], tour[j], length)
        distance_margin = abs(centers[i] - centers[j]) - (tour[i] + tour[j])
        cartesian_feasible &= distance_margin >= -guard
        pairs += 1
    require(angular_feasible == expected_feasible, f"both arcs {(k, n)}")
    require(cartesian_feasible == expected_feasible, f"Cartesian {(k, n)}")
    seam_sum = angles[n, k] + angles[k, n-1]
    complement_excess = (2*mp.pi-seam_sum) - (2*mp.pi-angles[n, n-1])
    require(abs(complement_excess+delta) < guard, "complement sign identity")
    if expected_feasible and size >= 4:
        require(abs(minimum - delta) < guard, "minimum does not match seam")
        require(set(winner[:2]) == {n - 1, n} and winner[2] == 2,
                "wrong seam winner")
    if not expected_feasible:
        seam_i, seam_j = tour.index(n), tour.index(n-1)
        margin = abs(centers[seam_i]-centers[seam_j]) - (2*n-1)
        require(margin < -guard and complement_excess > guard,
                "negative seam must overlap and violate complement upper bound")
    totals[0] += 1
    totals[1 if expected_feasible else 2] += 1
    totals[3] += triangles
    totals[4] += paths


if __name__ == "__main__":
    main()
