"""Independent SciPy SLSQP cross-validation."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Iterable

import numpy as np

from ringmin.geometry import TAU, as_order


@dataclass(frozen=True)
class SLSQPCheckResult:
    R: float
    positions: tuple[float, ...]
    success: bool
    message: str
    min_constraint: float


def _ordered_random_phis(n: int, rng: random.Random) -> np.ndarray:
    raw = np.array([rng.expovariate(1.0) for _ in range(n)], dtype=np.float64)
    gaps = raw / raw.sum() * TAU
    phis = np.cumsum(gaps)[:-1]
    return phis


def _pair_margin(radii: tuple[float, ...], phis: tuple[float, ...], R: float, i: int, j: int) -> float:
    delta = phis[j] - phis[i]
    dist2 = (R + radii[i]) ** 2 + (R + radii[j]) ** 2
    dist2 -= 2.0 * (R + radii[i]) * (R + radii[j]) * math.cos(delta)
    return dist2 - (radii[i] + radii[j]) ** 2


def _min_pair_margin(radii: tuple[float, ...], phis: tuple[float, ...], R: float) -> float:
    best = math.inf
    for i in range(len(radii)):
        for j in range(i + 1, len(radii)):
            best = min(best, _pair_margin(radii, phis, R, i, j))
    return best


def slsqp_fixed_order(
    order: Iterable[int | float],
    starts: int = 20,
    seed: int = 0,
) -> SLSQPCheckResult:
    """Minimize R with fixed cyclic order using SLSQP and cos constraints."""
    from scipy.optimize import minimize

    radii = as_order(order)
    n = len(radii)
    rng = random.Random(seed)
    bounds = [(0.0, TAU)] * (n - 1) + [(1e-9, 4.0 * n * n)]

    def unpack(x: np.ndarray) -> tuple[tuple[float, ...], float]:
        return (0.0, *x[: n - 1].tolist()), float(x[-1])

    def objective(x: np.ndarray) -> float:
        return float(x[-1])

    constraints = []
    for i in range(n - 1):
        constraints.append(
            {
                "type": "ineq",
                "fun": lambda x, i=i: (x[i] if i == 0 else x[i] - x[i - 1]),
            }
        )
    for i in range(n):
        for j in range(i + 1, n):
            constraints.append(
                {
                    "type": "ineq",
                    "fun": lambda x, i=i, j=j: _pair_margin(
                        radii, unpack(x)[0], float(x[-1]), i, j
                    ),
                }
            )

    best: SLSQPCheckResult | None = None
    for _ in range(starts):
        x0 = np.empty(n, dtype=np.float64)
        x0[: n - 1] = _ordered_random_phis(n, rng)
        x0[-1] = 4.0 * n * n
        opt = minimize(
            objective,
            x0,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-12, "maxiter": 1000, "disp": False},
        )
        phis, R = unpack(opt.x)
        min_constraint = min(
            _min_pair_margin(radii, phis, R),
            min(phis[i + 1] - phis[i] for i in range(n - 1)),
        )
        candidate = SLSQPCheckResult(
            R=R,
            positions=phis,
            success=bool(opt.success) and min_constraint >= -1e-6,
            message=str(opt.message),
            min_constraint=min_constraint,
        )
        if candidate.success and (best is None or candidate.R < best.R):
            best = candidate

    if best is None:
        raise AssertionError(f"SLSQP fixed-order validation failed for order={radii!r}")
    return best


def slsqp_unconstrained_global(
    n: int,
    starts: int = 80,
    seed: int = 0,
) -> SLSQPCheckResult:
    """Unconstrained-order SLSQP multistart with all pairwise cos constraints."""
    from scipy.optimize import minimize

    radii = tuple(float(r) for r in range(1, n + 1))
    rng = random.Random(seed)
    bounds = [(0.0, TAU)] * (n - 1) + [(1e-9, 4.0 * n * n)]

    def unpack(x: np.ndarray) -> tuple[tuple[float, ...], float]:
        return (0.0, *x[: n - 1].tolist()), float(x[-1])

    def objective(x: np.ndarray) -> float:
        return float(x[-1])

    constraints = []
    for i in range(n):
        for j in range(i + 1, n):
            constraints.append(
                {
                    "type": "ineq",
                    "fun": lambda x, i=i, j=j: _pair_margin(
                        radii, unpack(x)[0], float(x[-1]), i, j
                    ),
                }
            )

    best: SLSQPCheckResult | None = None
    base_angles = np.linspace(0.0, TAU, n, endpoint=False)
    for _ in range(starts):
        assigned = base_angles.copy()
        rng.shuffle(assigned)
        assigned += np.array([rng.uniform(-0.04, 0.04) for _ in range(n)])
        assigned = np.mod(assigned - assigned[0], TAU)
        x0 = np.empty(n, dtype=np.float64)
        x0[: n - 1] = assigned[1:]
        x0[-1] = 4.0 * n * n
        opt = minimize(
            objective,
            x0,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": 1e-12, "maxiter": 1000, "disp": False},
        )
        phis, R = unpack(opt.x)
        min_constraint = _min_pair_margin(radii, phis, R)
        candidate = SLSQPCheckResult(
            R=R,
            positions=phis,
            success=bool(opt.success) and min_constraint >= -1e-6,
            message=str(opt.message),
            min_constraint=min_constraint,
        )
        if candidate.success and (best is None or candidate.R < best.R):
            best = candidate

    if best is None:
        raise AssertionError(f"SLSQP unconstrained validation failed for n={n}")
    return best
