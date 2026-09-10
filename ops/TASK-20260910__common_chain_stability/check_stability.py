"""Bounded corroboration for the analytic common-chain stability theorem.

Exact: rational gates; 376 deletion masks on cycles of size 4..8, each
in three orientations; five symbolic identities. Numerical: 98 dual
inequalities, eight rational-endpoint floor comparisons, 16 prescribed
tours at n=40,41,80,81, and eight chain roots.
No tour optimization, production imports, saved results or random seeds.
The numerical checks do not certify q_* floors or any all-n assertion.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import factorial

import mpmath as mp
import sympy as sp


def rational_gates():
    def cosine(x, degree):
        return sum((-1)**j * x**(2*j) / factorial(2*j)
                   for j in range(degree // 2 + 1))

    def sine(x, degree):
        return sum((-1)**j * x**(2*j+1) / factorial(2*j+1)
                   for j in range((degree + 1) // 2))

    margins = [
        cosine(Q(73, 100), 6) - Q(73, 100),
        Q(3, 4) - cosine(Q(3, 4), 4),
        sine(Q(73, 100), 7) - Q(2, 3),
        Q(7, 10) - sine(Q(3, 4), 5),
        Q(3, 17) - Q(1, 102) - Q(1, 6),
        Q(23, 100) - Q(1, 102) - Q(1, 5),
        Q(7, 6) - Q(23, 50) - Q(1, 2),
        Q(20, 17) - Q(23, 100) - Q(9, 10),
        Q(20, 17) - 5*Q(23, 100) - Q(9, 340),
        Q(3, 100)*Q(27, 3400) - Q(1, 5000),
        (Q(5, 2)*Q(1, 10**6))**2 - Q(5, 10**12),
        Q(1, 5000) - Q(3, 20000) - Q(20, 10**14) - Q(4, 100000),
    ]
    assert all(margin >= 0 for margin in margins)
    assert all(margins[i] > 0 for i in (0, 1, 2, 3, 5, 6, 7, 9, 10, 11))
    assert Q(1, 1) / 6 > 0 and Q(4, 10**12) + Q(10, 10**14) <= Q(5, 10**12)
    print(f"rational gates: {len(margins)} PASS")
    print(f"edge margin over 1/5000: {margins[9]}")
    print(f"final numerator margin over 4*delta: {margins[11]}")


def edges(tour):
    assert len(tour) == len(set(tour)) >= 3
    return Counter(tuple(sorted((u, v)))
                   for u, v in zip(tour, tour[1:] + tour[:1]))


def deletion_runs(tour, removed):
    start = next(i for i, value in enumerate(tour) if value not in removed)
    walk = tour[start:] + tour[:start]
    walk = walk + walk[:1]
    left = walk[0]
    run = []
    blocks = []
    for value in walk[1:]:
        if value in removed:
            run.append(value)
        else:
            if run:
                blocks.append((left, tuple(run), value))
            left, run = value, []
    assert not run
    return blocks


def run_accounting():
    masks = checks = 0
    for size in range(4, 9):
        base = tuple(range(size))
        for count in range(1, size - 2):
            for selected in combinations(base, count):
                removed = set(selected)
                masks += 1
                for tour in (base, base[2:] + base[:2], base[::-1]):
                    blocks = deletion_runs(tour, removed)
                    assert sorted(x for _, run, _ in blocks for x in run) == sorted(removed)
                    predicted = edges(tour)
                    for left, run, right in blocks:
                        path = (left,) + run + (right,)
                        for u, v in zip(path, path[1:]):
                            predicted[tuple(sorted((u, v)))] -= 1
                        predicted[tuple(sorted((left, right)))] += 1
                    assert all(value >= 0 for value in predicted.values())
                    actual = edges(tuple(x for x in tour if x not in removed))
                    assert +predicted == actual
                    ll = sum(value for (u, v), value in edges(tour).items()
                             if u in removed and v in removed)
                    assert ll == sum(len(run)-1 for _, run, _ in blocks)
                    bad = sum(len(run) for _, run, _ in blocks if len(run) >= 2)
                    assert bad <= 2*ll
                    checks += 1
    print(f"exact run accounting: {masks} masks, {checks} orientations PASS")


def symbolic_identities():
    p, pp, v, vv, w, r, u, z = sp.symbols("p pp v vv w r u z", positive=True)
    expressions = [
        p*v + pp*vv - p*vv - pp*v - (pp-p)*(vv-v),
        (p-w)/(2*v) - (p*p-w*w)/(2*v*(p+w)),
        w*w - 2*p*w - w*w*(w*w-4*p*p)/(w*w+2*p*w),
        (u*z/((r+u)*(r+z))) / (1-u*z/((r+u)*(r+z)))
        - u*z/(r*(r+u+z)),
    ]
    x, s = sp.symbols("x s", positive=True)
    h = sp.sqrt(x*(s-x))/2 + s*(sp.asin(sp.sqrt(x/s))-sp.pi/4)/2
    expressions.append(sp.diff(h, x) - sp.sqrt(s-x)/(2*sp.sqrt(x)))
    assert all(sp.simplify(expression) == 0 for expression in expressions)
    print(f"symbolic identities: {len(expressions)} PASS")


def potential(x, a):
    s = 1+a
    return mp.sqrt(x*(s-x))/2 + s*(mp.asin(mp.sqrt(x/s))-mp.pi/4)/2


def dual_checks():
    count = 0
    for a in (mp.mpf(1)/6, mp.mpf(1)/5):
        grid = [a + (1-a)*j/6 for j in range(7)]
        for x in grid:
            for y in grid:
                defect = x+y-1-a
                slack = mp.sqrt(x*y)-potential(x, a)-potential(y, a)
                assert slack + mp.mpf("1e-60") >= defect**2/8
                assert slack <= defect**2/(8*a) + mp.mpf("1e-60")
                count += 1
    print(f"numerical dual inequalities (70 dps): {count} PASS")


def floor_checks():
    count = 0
    for q_exact in (Q(19, 100), Q(199, 1000)):
        q = mp.mpf(q_exact.numerator)/q_exact.denominator
        beta = mp.mpf(23)/100
        for n in (102, 103, 200, 201):
            k = (q_exact*n).__floor__()
            ell = (Q(23, 100)*n).__floor__()
            a = mp.mpf(k)/n
            f = lambda x, endpoint: mp.sqrt(x*(1+endpoint-x))
            d = lambda x, endpoint: 1+endpoint-x-2*f(x, endpoint)
            reference = mp.fsum(f(mp.mpf(i)/n, a) for i in range(k, n+1))/n
            deletion = mp.fsum(d(mp.mpf(i)/n, a) for i in range(k, ell))/n
            integral_reference = mp.quad(lambda x: f(x, q), [q, 1])
            integral_deletion = mp.quad(lambda x: d(x, q), [q, beta])
            assert abs(reference-integral_reference) <= mp.mpf(6)/n
            assert abs(deletion-integral_deletion) <= mp.mpf(10)/n
            count += 1
    print(f"numerical floor bounds, exact rational endpoints: {count} PASS")


def supnick(k, n):
    size = n-k+1
    middle = (size+1)//2
    arms = []
    for parity in (1, 2):
        arm = []
        for low in range(parity, middle+1, 2):
            arm.append(low)
            if size-low > middle:
                arm.append(size-low)
        arms.append(arm)
    return tuple(k+j-1 for j in arms[0]+arms[1][::-1]+[size])


def cost(tour, n):
    return mp.fsum(mp.sqrt(u*v) for u, v in zip(tour, tour[1:]+tour[:1]))/n**2


def root_by_cosine(tour):
    # Separate law-of-cosines angular formula and monotone bisection.
    pairs = tuple(zip(tour, tour[1:]+tour[:1]))

    def closure(radius):
        return mp.fsum(mp.acos(((radius+u)**2+(radius+v)**2-(u+v)**2)
                              /(2*(radius+u)*(radius+v))) for u, v in pairs)

    low, high = mp.mpf(0), mp.mpf(max(tour)**2)
    assert closure(high) < 2*mp.pi
    for _ in range(160):
        middle = (low+high)/2
        if closure(middle) > 2*mp.pi:
            low = middle
        else:
            high = middle
    return (low+high)/2


def tour_checks():
    count = roots = 0
    parities = set()
    for n in (40, 41, 80, 81):
        # Rational surrogate endpoints test finite lemmas, never q_* floors.
        k = n//5
        ell = k+max(2, n//25)
        a = mp.mpf(k)/n
        s = 1+a
        assert a >= mp.mpf(1)/6 and s-2*mp.mpf(ell)/n > mp.mpf(1)/2
        optimal = supnick(k, n)
        increasing = tuple(range(k, n+1))
        cut = len(optimal)//2
        tours = (optimal, increasing, increasing[::2]+increasing[1::2],
                 optimal[:cut][::-1]+optimal[cut:])
        reference = mp.fsum(mp.sqrt(mp.mpf(i)/n*(s-mp.mpf(i)/n))
                            for i in range(k, n+1))/n
        ideal = mp.fsum(s-mp.mpf(i)/n
                       - 2*mp.sqrt(mp.mpf(i)/n*(s-mp.mpf(i)/n))
                       for i in range(k, ell))/n
        for tour_index, tour in enumerate(tours):
            assert set(tour) == set(range(k, n+1)) and len(set(tour)) == len(tour)
            restricted = tuple(i for i in tour if i >= ell)
            parities.add((len(tour) % 2, len(restricted) % 2))
            outer, inner = cost(tour, n), cost(restricted, n)
            excess = outer-reference
            squared = mp.fsum((mp.mpf(u+v)/n-s)**2
                              for u, v in zip(tour, tour[1:]+tour[:1]))/n
            assert excess >= 0 and squared <= 8*excess + mp.mpf("1e-60")
            assert abs(inner-outer-ideal) <= 60*mp.sqrt(excess)
            if tour_index == 0:
                assert excess <= 1/(8*a*n*n)
            if tour_index == 1:
                for candidate, weight in ((tour, outer), (restricted, inner)):
                    radius = root_by_cosine(candidate)/n**2
                    assert weight/mp.pi-mp.mpf(1)/n <= radius <= weight/mp.pi
                    roots += 1
            count += 1
    assert parities == {(0, 0), (0, 1), (1, 0), (1, 1)}
    print(f"prescribed numerical tours (70 dps): {count}, all four parities PASS")
    print(f"independent cosine/bisection root sandwiches: {roots} PASS")


if __name__ == "__main__":
    mp.mp.dps = 70
    rational_gates()
    run_accounting()
    symbolic_identities()
    dual_checks()
    floor_checks()
    tour_checks()
    print("PASS: bounded corroboration only; all-n theorem is analytic")
