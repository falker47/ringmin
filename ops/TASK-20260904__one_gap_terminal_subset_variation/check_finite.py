"""Finite diagnostics for the one-gap continuum Supnick functional.

The analytic proof does not rely on these floating-point observations. The
tour constructor and edge formulas are independent of ringmin production code.
"""

from __future__ import annotations

import mpmath as mp


def supnick_tour_ranks(n: int) -> tuple[int, ...]:
    if n < 3:
        raise ValueError("n must be at least 3")
    h = (n + 1) // 2
    left: list[int] = []
    right: list[int] = []
    j = 0
    while True:
        changed = False
        low_left = 1 + 2 * j
        high_left = n - 1 - 2 * j
        if low_left <= h:
            left.append(low_left)
            changed = True
        if high_left > h:
            left.append(high_left)
            changed = True

        low_right = 2 + 2 * j
        high_right = n - 2 - 2 * j
        if low_right <= h:
            right.append(low_right)
            changed = True
        if high_right > h:
            right.append(high_right)
            changed = True
        if not changed:
            break
        j += 1
    tour = tuple(left + list(reversed(right)) + [n])
    if sorted(tour) != list(range(1, n + 1)):
        raise AssertionError((n, tour))
    return tour


def cycle_edges(tour: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        tuple(sorted((tour[i], tour[(i + 1) % len(tour)])))
        for i in range(len(tour))
    }


def formula_edges(n: int) -> set[tuple[int, int]]:
    if n % 2 == 0:
        h = n // 2
        edges = {(1, n), (h, h + 1)}
        edges.update((j, n - j) for j in range(1, h))
        edges.update((j, n + 2 - j) for j in range(2, h + 1))
    else:
        h = (n - 1) // 2
        edges = {(1, n)}
        edges.update((j, n - j) for j in range(1, h + 1))
        edges.update((j, n + 2 - j) for j in range(2, h + 2))
    return {tuple(sorted(edge)) for edge in edges}


def finite_weight(n: int, alpha: mp.mpf, x: mp.mpf, epsilon: mp.mpf) -> tuple[int, mp.mpf]:
    radii = [
        j
        for j in range(1, n + 1)
        if alpha <= mp.mpf(j) / n <= x - epsilon / 2
        or x + epsilon / 2 <= mp.mpf(j) / n <= 1
    ]
    tour = supnick_tour_ranks(len(radii))
    weight = mp.fsum(mp.sqrt(radii[i - 1] * radii[j - 1]) for i, j in cycle_edges(tour))
    return len(radii), weight / (n * n)


def continuum_weight(alpha: mp.mpf, x: mp.mpf, epsilon: mp.mpf) -> mp.mpf:
    s = 1 + alpha
    m = s / 2
    f = lambda y, total: mp.sqrt(y * (total - y))
    if x < m:
        j = mp.quad(lambda y: f(y, s), [alpha, x - epsilon / 2])
        j += mp.quad(lambda y: f(y, s + epsilon), [x + epsilon / 2, m + epsilon / 2])
    elif x > m:
        p = s - x
        j = mp.quad(lambda y: f(y, s), [alpha, p - epsilon / 2])
        j += mp.quad(lambda y: f(y, s - epsilon), [p - epsilon / 2, m - epsilon / 2])
    else:
        j = mp.quad(lambda y: f(y, s), [alpha, m - epsilon / 2])
    return 2 * j


def variation(alpha: mp.mpf, x: mp.mpf) -> mp.mpf:
    s = 1 + alpha
    theta = mp.asin(mp.sqrt(x / s))
    return s / mp.pi * (mp.pi / 4 - theta - mp.sin(theta) * mp.cos(theta))


def main() -> None:
    mp.mp.dps = 60
    for n in range(3, 301):
        actual = cycle_edges(supnick_tour_ranks(n))
        expected = formula_edges(n)
        if actual != expected or len(actual) != n:
            raise AssertionError((n, actual ^ expected))

    tau = mp.findroot(lambda t: t - mp.cos(t), mp.mpf("0.74"))
    alpha = (1 - mp.sin(tau)) / (1 + mp.sin(tau))
    s = 1 + alpha
    m = s / 2
    epsilon = mp.mpf("0.02")
    centers = (alpha + mp.mpf("0.12"), m, mp.mpf("0.88"))

    parity_seen: set[int] = set()
    max_error = mp.mpf("0")
    comparisons = 0
    for x in centers:
        target = continuum_weight(alpha, x, epsilon)
        for base in (2000, 4000, 8000):
            for n in range(base, base + 8):
                count, observed = finite_weight(n, alpha, x, epsilon)
                parity_seen.add(count % 2)
                error = abs(observed - target)
                max_error = max(max_error, error)
                comparisons += 1
                if error > mp.mpf("0.003"):
                    raise AssertionError((x, n, count, observed, target, error))
                break

    delta = mp.mpf("1e-8")
    max_variation_error = mp.mpf("0")
    for x in centers:
        c0 = 2 * continuum_weight(alpha, x, mp.mpf("0")) / (2 * mp.pi)
        c1 = 2 * continuum_weight(alpha, x, delta) / (2 * mp.pi)
        quotient = (c1 - c0) / delta
        predicted = variation(alpha, x)
        max_variation_error = max(max_variation_error, abs(quotient - predicted))
        if predicted >= 0 or abs(quotient - predicted) > mp.mpf("1e-7"):
            raise AssertionError((x, quotient, predicted))

    if parity_seen != {0, 1}:
        raise AssertionError(parity_seen)

    print("supnick_rank_edge_sets=PASS comparisons=298 sizes=3..300")
    print(f"finite_continuum_diagnostics=PASS comparisons={comparisons} parities=even,odd")
    print(f"max_weight_error={mp.nstr(max_error, 8)}")
    print(f"variation_diagnostics=PASS max_error={mp.nstr(max_variation_error, 8)}")
    print(f"mpmath={mp.__version__} imports_ringmin=NO")
    print("classification=FINITE_NUMERICAL_DIAGNOSTIC_ONLY; analytic sign is not inferred")


if __name__ == "__main__":
    main()
