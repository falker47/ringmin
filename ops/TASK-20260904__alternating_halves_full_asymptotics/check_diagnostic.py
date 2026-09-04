"""Independent finite diagnostics for the alternating-halves asymptotic.

Nothing in this file is a premise of the proof.  It deliberately does not
import ``src/ringmin``.  The direct gap audit uses mpmath and checks every pair
in both cyclic directions for the displayed explicit construction.
"""

from __future__ import annotations

import argparse

import mpmath as mp


def alternating_order(n: int) -> tuple[int, ...]:
    if n < 4 or n % 2:
        raise ValueError("n must be even and at least 4")
    m = n // 2
    return tuple(v for i in range(1, m + 1) for v in (i, m + i))


def theta_mp(R: mp.mpf, a: int, b: int) -> mp.mpf:
    return 2 * mp.asin(mp.sqrt(mp.mpf(a * b) / ((R + a) * (R + b))))


def bisect_decreasing(function, target: mp.mpf, lo: mp.mpf, hi: mp.mpf) -> mp.mpf:
    if not function(lo) > target > function(hi):
        raise AssertionError("invalid decreasing-function bracket")
    for _ in range(180):
        mid = (lo + hi) / 2
        if function(mid) > target:
            lo = mid
        else:
            hi = mid
    return hi


def chain_sum_mp(n: int, R: mp.mpf) -> mp.mpf:
    radii = alternating_order(n)
    return mp.fsum(theta_mp(R, radii[i], radii[(i + 1) % n]) for i in range(n))


def valley_sum_and_gaps(
    n: int, R: mp.mpf
) -> tuple[mp.mpf, list[mp.mpf], int, int]:
    m = n // 2
    low = list(range(1, m + 1))
    high = list(range(m + 1, n + 1))
    p = [theta_mp(R, low[i], high[i]) for i in range(m)]
    q: list[mp.mpf] = []
    chord_cells = 0
    adjacent_cells = 0
    for i in range(m):
        ni = (i + 1) % m
        baseline = theta_mp(R, high[i], low[ni])
        chord = theta_mp(R, high[i], high[ni])
        extra = max(mp.mpf(0), chord - p[ni] - baseline)
        if extra > 0:
            chord_cells += 1
        else:
            adjacent_cells += 1
        # Put the valley excess into the outgoing low-to-high gap.  In cyclic
        # list order that gap is p[ni], not the baseline high-to-low gap.
        q.append(baseline)
        p[ni] += extra
    gaps = [value for i in range(m) for value in (p[i], q[i])]
    return mp.fsum(gaps), gaps, chord_cells, adjacent_cells


def direct_gap_audit(n: int, R: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    radii = alternating_order(n)
    base, gaps, _, _ = valley_sum_and_gaps(n, R)
    extra = 2 * mp.pi - base
    if extra <= 0:
        raise AssertionError("construction has no closure slack")
    gaps[-1] += extra
    if abs(mp.fsum(gaps) - 2 * mp.pi) > mp.mpf("1e-60"):
        raise AssertionError("gap closure failure")
    prefix = [mp.mpf(0)]
    for gap in gaps:
        prefix.append(prefix[-1] + gap)
    min_slack = mp.inf
    for i in range(n):
        for j in range(i + 1, n):
            required = theta_mp(R, radii[i], radii[j])
            forward = prefix[j] - prefix[i]
            wrap = 2 * mp.pi - forward
            min_slack = min(min_slack, forward - required, wrap - required)
    max_angle = theta_mp(R, n, n)
    if min_slack < -mp.mpf("1e-55"):
        raise AssertionError(f"all-pairs gap failure: {min_slack}")
    return extra, max_angle, min_slack


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[40, 80, 160, 320, 640])
    args = parser.parse_args()

    mp.mp.dps = 70
    J = 3 * mp.sqrt(2) / 4 - mp.log(3 + 2 * mp.sqrt(2)) / 8
    K = J - mp.mpf(1) / 12 + mp.log(3) / 8
    c_chain = J / (2 * mp.pi)
    c_full = K / (2 * mp.pi)
    print(f"J={mp.nstr(J, 30)}")
    print(f"K={mp.nstr(K, 30)}")
    print(f"c_chain={mp.nstr(c_chain, 30)}")
    print(f"c_full={mp.nstr(c_full, 30)}")
    print("n chain_ratio full_formula_ratio chord_cells adjacent_cells extra min_slack")
    for n in args.sizes:
        scale = mp.mpf(n * n)
        chain_root = bisect_decreasing(
            lambda R: chain_sum_mp(n, R), 2 * mp.pi, mp.mpf("0.05") * scale, mp.mpf("0.25") * scale
        )
        valley_root = bisect_decreasing(
            lambda R: valley_sum_and_gaps(n, R)[0],
            2 * mp.pi,
            mp.mpf("0.05") * scale,
            mp.mpf("0.25") * scale,
        )
        base, _, chord_cells, adjacent_cells = valley_sum_and_gaps(n, valley_root)
        extra, _, min_slack = direct_gap_audit(n, valley_root)
        if abs(base + extra - 2 * mp.pi) > mp.mpf("1e-60"):
            raise AssertionError("root closure mismatch")
        print(
            n,
            mp.nstr(chain_root / scale, 18),
            mp.nstr(valley_root / scale, 18),
            chord_cells,
            adjacent_cells,
            mp.nstr(extra, 12),
            mp.nstr(min_slack, 8),
        )
    print("PASS: independent finite diagnostic and direct all-pairs gap audit")


if __name__ == "__main__":
    main()
