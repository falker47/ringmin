from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import binding_structure, full_radius
from ringmin.search import certified_search


def pocket_radius(R: float, a: float, b: float) -> float:
    curvature = (
        1.0 / R
        + 1.0 / a
        + 1.0 / b
        + 2.0 * math.sqrt(1.0 / (R * a) + 1.0 / (a * b) + 1.0 / (R * b))
    )
    return 1.0 / curvature


def arc_slacks(result, index: int) -> list[tuple[int, int, float, float, float, float]]:
    out = []
    radii = result.order
    phis = result.positions
    for j in range(len(radii)):
        if j == index:
            continue
        i, k = sorted((index, j))
        from ringmin.geometry import TAU, theta

        sep = theta(result.R_full, radii[i], radii[k])
        delta = phis[k] - phis[i]
        forward = delta - sep
        wrap = (TAU - sep) - delta
        out.append((i, k, radii[i], radii[k], forward, wrap))
    return out


def main() -> int:
    subset = certified_search(8, k=5000)
    # The canonical search above is for {1..8}; audit wants {2..8}, so enumerate directly.
    from itertools import permutations

    values = tuple(range(2, 9))
    best = None
    count = 0
    for perm in permutations(values[:-1]):
        order = (8, *perm)
        if order[1] > order[-1]:
            continue
        count += 1
        result = full_radius(order)
        if best is None or result.R_full < best.R_full:
            best = result
    assert best is not None
    print("AUDIT_A subset={2..8}")
    print(f"enumerated={count}")
    print(f"R={best.R_full:.17g}")
    print(f"order={[int(x) for x in best.order]}")
    print("AUDIT_B pockets")
    for i, a in enumerate(best.order):
        b = best.order[(i + 1) % len(best.order)]
        print(f"pair=({int(a)},{int(b)}) pocket={pocket_radius(best.R_full, a, b):.17g}")

    print("AUDIT_C criterion")
    print("implemented=floatable iff STN remains feasible at R_full after increasing every pairwise theta constraint involving the circle by 1e-9")
    print("R_evaluated=R_full")
    print("existence=STN feasibility over all placements, not only recovered shortest-path placement")
    print("tight_tol=1e-9 feasibility_diag_tol=1e-11")

    print("AUDIT_D certified n=8..10")
    for n in (8, 9, 10):
        search = certified_search(n, k=5000)
        result = search.best
        bindings, floating = binding_structure(result.order, result.R_full, result.positions)
        print(f"n={n} R={result.R_full:.17g} order={[int(x) for x in result.order]} floating={[int(x) for x in floating]}")
        print("bindings")
        for binding in bindings:
            adjacent = (binding.j == binding.i + 1) or (binding.i == 0 and binding.j == len(result.order) - 1)
            print(
                f"  ({binding.i},{binding.j}) radii=({int(binding.radius_i)},{int(binding.radius_j)}) "
                f"kind={binding.kind} slack={binding.slack:.17g} adjacent={adjacent}"
            )
        one_index = list(result.order).index(1.0)
        print("circle_1_slacks")
        for item in arc_slacks(result, one_index):
            i, j, ri, rj, forward, wrap = item
            print(
                f"  ({i},{j}) radii=({int(ri)},{int(rj)}) "
                f"forward={forward:.17g} wrap={wrap:.17g}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
