"""Pre-proof finite discriminators; stdlib only, no production imports.

Numerical observations, not interval or global certificates. No RNG.
"""

from itertools import permutations
import math


RADII = (0.1, 1, 2, 5, 10, 100)
GUARD = 1e-10


def cells(p, radius):
    def angle(a, b):
        return 2 * math.asin(math.sqrt(a*b/((radius+a)*(radius+b))))

    return [max(angle(i, p[i-2]) + angle(i, p[i-1]),
                angle(p[i-2], p[i-1])) for i in range(1, len(p)+1)]


def main():
    first = {}
    counts = dict(orders=0, swaps=0, fixed_radius_shift_comparisons=0)

    def retain(key, record):
        if key not in first:
            first[key] = record
            print(key, record, flush=True)

    for m in range(2, 7):
        shifts = [tuple(range(m+1+s, 2*m+1)) + tuple(range(m+1, m+1+s))
                  for s in range(m)]
        shift_min = {r: min(math.fsum(cells(p, r)) for p in shifts) for r in RADII}
        for p in permutations(range(m+1, 2*m+1)):
            counts['orders'] += 1
            for radius in RADII:
                before = cells(p, radius)
                score = math.fsum(before)
                counts['fixed_radius_shift_comparisons'] += 1
                if score < shift_min[radius] - GUARD:
                    retain('cyclic_shifts_not_minimal', (m, p, radius, score,
                                                         shift_min[radius]))
                for j in range(m):
                    k = (j+1) % m
                    if p[j] > p[k]:
                        continue
                    q = list(p)
                    q[j], q[k] = q[k], q[j]
                    after = cells(q, radius)
                    delta = math.fsum(a-b for a, b in zip(after, before))
                    left, right = j+1, (j+2) % m+1
                    u, v = p[j-1], p[(j+2) % m]
                    counts['swaps'] += 1
                    record = (m, p, radius, j+1, delta, left, right, u, v)
                    expected = {j, (j+2) % m} if m > 2 else set()
                    assert all(a == b for i, (a, b) in enumerate(zip(after, before))
                               if i not in expected), record
                    if m == 2:
                        assert delta == 0
                        continue
                    if abs(delta) > GUARD and delta*(left-right) < 0:
                        retain('chain_sign_fails', record)
                    if abs(delta) > GUARD and (delta*(u-v) < 0 or u == v):
                        retain('chord_sign_fails', record)
                    if left < right and u <= v and delta > GUARD:
                        retain('coordinate_dominance_fails', record)
        print(f'm={m} complete', flush=True)

    # Does F_low(u,b) have increasing/decreasing differences in low and b?
    def cost(low, u, b, radius):
        def angle(a, c):
            return 2 * math.asin(math.sqrt(a*c/((radius+a)*(radius+c))))
        return max(angle(low, u)+angle(low, b), angle(u, b))

    for m in range(2, 7):
        for low in range(1, m):
            for highlow in range(low+1, m+1):
                for u, x, y in permutations(range(m+1, 2*m+1), 3):
                    if x > y:
                        continue
                    for radius in RADII:
                        cross = (cost(highlow, u, y, radius)-cost(highlow, u, x, radius)
                                 - cost(low, u, y, radius)+cost(low, u, x, radius))
                        if cross < -GUARD:
                            retain('low_high_supermodularity_fails',
                                   (m, low, highlow, u, x, y, radius, cross))
                        if cross > GUARD:
                            retain('low_high_submodularity_fails',
                                   (m, low, highlow, u, x, y, radius, cross))
    print('COUNTS', counts)
    print('FIRST_WITNESSES', first)
    print('Finite float64 observations only; no universal proof or global certificate.')


if __name__ == '__main__':
    main()
