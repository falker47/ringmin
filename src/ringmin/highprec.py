"""High-precision verification helpers."""

from __future__ import annotations

import mpmath as mp


def theta_mp(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    x2 = (a * b) / ((R + a) * (R + b))
    value = 2 * mp.asin(mp.sqrt(x2))
    if not (0 < value < mp.pi):
        raise AssertionError(f"mp theta outside (0, pi): {value}")
    return value


def full_radius_mp(order: tuple[int | float, ...], digits: int = 50) -> mp.mpf:
    """Slow high-precision full STN bisection."""
    mp.mp.dps = digits
    radii = tuple(mp.mpf(r) for r in order)
    tau = 2 * mp.pi

    def feasible(R: mp.mpf) -> bool:
        dist = closed_stn_mp(radii, R)
        return all(dist[i][i] >= mp.mpf("-1e-40") for i in range(len(radii)))

    lo = mp.mpf("1e-9")
    hi = mp.mpf(4 * len(radii) * len(radii))
    while not feasible(hi):
        hi *= 2
    for _ in range(240):
        mid = (lo + hi) / 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid
    return hi


def closed_stn_mp(radii: tuple[mp.mpf, ...], R: mp.mpf) -> list[list[mp.mpf]]:
    tau = 2 * mp.pi
    n = len(radii)
    dist = [[mp.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = mp.mpf("0")
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta_mp(R, radii[i], radii[j])
            dist[i][j] = min(dist[i][j], tau - sep)
            dist[j][i] = min(dist[j][i], -sep)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                candidate = dist[i][k] + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def recover_positions_mp(order: tuple[int | float, ...], R: mp.mpf, digits: int = 50) -> tuple[mp.mpf, ...]:
    mp.mp.dps = digits
    radii = tuple(mp.mpf(r) for r in order)
    dist = closed_stn_mp(radii, R)
    if any(dist[i][i] < mp.mpf("-1e-40") for i in range(len(radii))):
        raise AssertionError("cannot recover mpmath positions from infeasible STN")
    positions = [dist[0][i] for i in range(len(radii))]
    positions[0] = mp.mpf("0")
    return tuple(positions)


def pair_slack_mp(
    order: tuple[int | float, ...],
    R: mp.mpf,
    positions: tuple[mp.mpf, ...],
    i: int,
    j: int,
) -> tuple[mp.mpf, mp.mpf]:
    mp.mp.dps = max(mp.mp.dps, 50)
    radii = tuple(mp.mpf(r) for r in order)
    sep = theta_mp(R, radii[i], radii[j])
    delta = positions[j] - positions[i]
    return delta - sep, (2 * mp.pi - sep) - delta
