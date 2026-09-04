"""Independent high-precision diagnostics for the increasing-order proof.

This task-local checker deliberately does not import ``src/ringmin``.  Its
finite output corroborates formulas and indexing; the written analytic proof
carries every all-n claim.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 70
TAU = 2 * mp.pi
C = 1 / TAU


def theta(radius: mp.mpf, a: int, b: int) -> mp.mpf:
    aa = mp.mpf(a)
    bb = mp.mpf(b)
    return 2 * mp.asin(mp.sqrt(aa * bb / ((radius + aa) * (radius + bb))))


def closure(radius: mp.mpf, n: int) -> mp.mpf:
    return mp.fsum(theta(radius, k, k + 1) for k in range(1, n)) + theta(
        radius, n, 1
    )


def chain_root(n: int) -> mp.mpf:
    lo = mp.mpf("1e-50")
    hi = mp.mpf(4 * n * n)
    assert closure(lo, n) > TAU > closure(hi, n)
    for _ in range(260):
        mid = (lo + hi) / 2
        if closure(mid, n) > TAU:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def audit_explicit_gaps(n: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    radius = C * n * n + mp.power(n, mp.mpf("1.5"))
    base = [theta(radius, k, k + 1) for k in range(1, n)]
    seam_min = theta(radius, n, 1)
    extra = TAU - (mp.fsum(base) + seam_min)
    envelope = theta(radius, n, n)
    assert extra > envelope > 0

    gaps = base + [seam_min + extra]
    assert abs(mp.fsum(gaps) - TAU) < mp.mpf("1e-60")
    positions = [mp.mpf(0)]
    for gap in base:
        positions.append(positions[-1] + gap)

    min_angular_slack = mp.inf
    min_cartesian_margin = mp.inf
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta(radius, i + 1, j + 1)
            forward = positions[j] - positions[i]
            backward = TAU - forward
            min_angular_slack = min(
                min_angular_slack, forward - sep, backward - sep
            )

            delta = min(forward, backward)
            a = mp.mpf(i + 1)
            b = mp.mpf(j + 1)
            distance_sq = (
                (radius + a) ** 2
                + (radius + b) ** 2
                - 2 * (radius + a) * (radius + b) * mp.cos(delta)
            )
            min_cartesian_margin = min(
                min_cartesian_margin, distance_sq - (a + b) ** 2
            )

    tolerance = mp.mpf("1e-55")
    assert min_angular_slack > -tolerance
    assert min_cartesian_margin > -tolerance
    return extra, extra - envelope, min_angular_slack


def main() -> None:
    print("n chain/n^2 scaled_seam_deficit sqrt(n)*extra guard_margin min_slack")
    for n in (8, 16, 32, 64, 128, 256):
        root = chain_root(n)
        seam_deficit = (
            theta(root, n, 1) + theta(root, 1, 2) - theta(root, n, 2)
        )
        extra, guard_margin, min_slack = audit_explicit_gaps(n)
        print(
            n,
            mp.nstr(root / (n * n), 16),
            mp.nstr(mp.power(n, mp.mpf("1.5")) * seam_deficit, 16),
            mp.nstr(mp.sqrt(n) * extra, 16),
            mp.nstr(guard_margin, 8),
            mp.nstr(min_slack, 5),
        )

    target = 4 * mp.pi * (1 - mp.sqrt(2))
    scaled_deficit = mp.power(n, mp.mpf("1.5")) * seam_deficit
    scaled_extra = mp.sqrt(n) * extra
    assert target < scaled_deficit < 0
    assert 0 < scaled_extra < 4 * mp.pi**2
    print("PASS: independent high-precision chain, seam, gap, and Cartesian checks")


if __name__ == "__main__":
    main()
