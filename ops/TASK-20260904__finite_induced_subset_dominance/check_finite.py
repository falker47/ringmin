"""Independent finite audit of induced-subset terminal dominance.

This diagnostic uses only the Python standard library and does not import
the ringmin production package.  The exact theorem is proved analytically in
research/FINITE_INDUCED_SUBSET_DOMINANCE.md; floating roots here are
corroborative only.
"""

from __future__ import annotations

from itertools import combinations
from math import asin, pi, sqrt


def supnick_rank_edges(size: int) -> tuple[tuple[int, int], ...]:
    """Return the one-based undirected edge multiset from the parity formulas."""
    if size < 3:
        raise ValueError("a cycle needs at least three ranks")
    half = size // 2
    edges: list[tuple[int, int]] = []
    if size % 2 == 0:
        edges.extend((j, size - j) for j in range(1, half))
        edges.extend((j, size + 2 - j) for j in range(2, half + 1))
        edges.extend(((1, size), (half, half + 1)))
    else:
        edges.extend((j, size - j) for j in range(1, half + 1))
        edges.extend((j, size + 2 - j) for j in range(2, half + 2))
        edges.append((1, size))
    return tuple(tuple(sorted(edge)) for edge in edges)


def validate_cycle(size: int, edges: tuple[tuple[int, int], ...]) -> None:
    degrees = [0] * size
    assert len(edges) == size
    assert len(set(edges)) == size
    for left, right in edges:
        assert 1 <= left < right <= size
        degrees[left - 1] += 1
        degrees[right - 1] += 1
    assert degrees == [2] * size


def angle(radius: float, left: int, right: int) -> float:
    return 2.0 * asin(sqrt(left * right / ((radius + left) * (radius + right))))


def closure(radius: float, radii: tuple[int, ...]) -> float:
    edges = supnick_rank_edges(len(radii))
    return sum(angle(radius, radii[i - 1], radii[j - 1]) for i, j in edges)


def chain_root(radii: tuple[int, ...]) -> float:
    low = 0.0
    high = 1.0
    while closure(high, radii) > 2.0 * pi:
        high *= 2.0
    for _ in range(100):
        middle = (low + high) / 2.0
        if closure(middle, radii) > 2.0 * pi:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def main() -> None:
    subsets = 0
    root_comparisons = 0
    strict_cases = 0
    equality_cases = 0
    largest_gap = 0.0

    for size in range(3, 12):
        validate_cycle(size, supnick_rank_edges(size))

    for n in range(3, 12):
        best_root = -1.0
        best_subset: tuple[int, ...] | None = None
        best_terminal_root = -1.0
        for size in range(3, n + 1):
            terminal = tuple(range(n - size + 1, n + 1))
            terminal_root = chain_root(terminal)
            best_terminal_root = max(best_terminal_root, terminal_root)
            for subset in combinations(range(1, n + 1), size):
                subsets += 1
                assert all(value <= n - size + rank for rank, value in enumerate(subset, 1))
                root = chain_root(subset)
                root_comparisons += 1
                tolerance = 2e-12 * max(1.0, terminal_root)
                assert root <= terminal_root + tolerance
                if subset == terminal:
                    equality_cases += 1
                    assert abs(root - terminal_root) <= tolerance
                else:
                    strict_cases += 1
                    assert root < terminal_root - tolerance
                    largest_gap = max(largest_gap, terminal_root - root)
                if root > best_root:
                    best_root = root
                    best_subset = subset
        assert best_subset is not None
        assert best_subset == tuple(range(best_subset[0], n + 1))
        assert abs(best_root - best_terminal_root) <= 2e-12 * max(1.0, best_root)

    print(
        "finite induced-subset audit: PASS "
        f"subsets={subsets} root_comparisons={root_comparisons} "
        f"strict={strict_cases} equality={equality_cases} "
        f"largest_gap={largest_gap:.12g} n=3..11"
    )


if __name__ == "__main__":
    main()
