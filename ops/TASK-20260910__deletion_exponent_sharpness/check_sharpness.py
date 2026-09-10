"""Bounded corroboration of Section 11; no general-tour enumeration.

Exact: accepted q bracket rechecked by rational Taylor gates, twelve exact
q/beta floors, five prescribed tours per size in three orientations,
reflected marginals, cyclic maximal runs, energy and midpoint strip counts.
Symbolic: first variation, Hessian and primitive identities.
Numerical: the sixty prescribed tours at 70 and 100 dps, direct costs and
the separate signed/marginal/run bounds. No production or artifact imports,
randomness, optimization, adaptive size search or all-n numerical claims.
"""

from collections import Counter
from fractions import Fraction as Q
from math import factorial, isqrt

import mpmath as mp
import sympy as sp


SIZES = tuple(range(102, 110)) + (512, 513, 2048, 2049)
PRECISIONS = (70, 100)
BETA = Q(23, 100)
TAU_LO = Q("0.7390851332151606416553120876738734040134")
TAU_HI = Q("0.7390851332151606416553120876738734040135")
Q_LO = Q("0.1950200913506069300798071259134151019366")
Q_HI = Q("0.1950200913506069300798071259134151019367")


def parameter_checks():
    def cosine(x, degree):
        return sum((-1)**j*x**(2*j)/factorial(2*j)
                   for j in range(degree//2+1))

    def sine(x, degree):
        return sum((-1)**j*x**(2*j+1)/factorial(2*j+1)
                   for j in range((degree+1)//2))

    assert cosine(TAU_LO, 82) > TAU_LO
    assert cosine(TAU_HI, 80) < TAU_HI
    lo, hi = sine(TAU_LO, 83), sine(TAU_HI, 81)
    assert Q_LO < (1-hi)/(1+hi) < (1-lo)/(1+lo) < Q_HI
    assert Q(3, 17) < Q_LO < Q_HI < Q(1, 5)
    assert Q(3, 17)-Q(1, 102) == Q(1, 6)
    assert Q(7, 6)-2*BETA > Q(1, 2)
    assert Q(6, 5)/(4*Q(1, 6)**2) == Q(54, 5) < 11
    assert Q(3, 2)**2*6 < 4**2
    assert 1/(4*Q(1, 6)) < 2
    assert 3+10*4 == 43 and 43+11 == 54
    assert 54*8 == 432 and 10*4 == 40
    print("exact q bracket, domain and remainder constants: PASS")


def supnick(k, n):
    # Direct canonical rank-arm construction; no production import.
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
    return tuple(k+r-1 for r in arms[0]+arms[1][::-1]+[size])


def fixtures():
    for n in SIZES:
        k = (Q_LO*n).__floor__()
        assert k == (Q_HI*n).__floor__()  # Certified floor at these sizes.
        ell = (BETA*n).__floor__()
        assert 1 <= k < ell <= n-2
        assert Q(k, n) > Q(1, 6)
        base = supnick(k, n)
        increasing = tuple(range(k, n+1))
        width = min(ell-k, isqrt(n)//2)
        assert width >= 1 and ell+width-1 < (n+k)//2

        def exchange(x):
            if ell-width <= x < ell:
                return x+width
            if ell <= x < ell+width:
                return x-width
            return x

        cut = len(base)//3
        tours = (
            base,
            increasing,
            increasing[::2]+increasing[1::2],
            tuple(exchange(x) for x in base),
            base[:cut][::-1]+base[cut:],
        )
        for index, tour in enumerate(tours):
            assert len(tour) == len(set(tour)) == n-k+1
            assert set(tour) == set(increasing)
            yield n, k, ell, index, tour


def edges(tour):
    return tuple(zip(tour, tour[1:]+tour[:1]))


def edge_counter(tour):
    return Counter(tuple(sorted(edge)) for edge in edges(tour))


def runs(tour, ell):
    # Independent extraction by cyclic survivor indices, including the wrap.
    keep = [i for i, value in enumerate(tour) if value >= ell]
    size = len(tour)
    output = []
    for left, right in zip(keep, keep[1:]+[keep[0]+size]):
        if right > left+1:
            path = tuple(tour[j % size] for j in range(left, right+1))
            output.append(path)
    return output


def exact_checks(cases):
    parities = set()
    count = strip_count = 0
    run_lengths = set()
    saw_wrap = False
    for n, k, ell, _, tour in cases:
        parities.add((len(tour) % 2, (n-ell+1) % 2))
        s_int = n+k
        for walk in (tour, tour[1:]+tour[:1], tour[::-1]):
            directed = [(x, s_int-y) for u, v in edges(walk)
                        for x, y in ((u, v), (v, u))]
            target = Counter({x: 2 for x in range(k, n+1)})
            assert Counter(x for x, _ in directed) == target
            assert Counter(z for _, z in directed) == target
            squared = sum((u+v-s_int)**2 for u, v in edges(walk))
            assert sum((x-z)**2 for x, z in directed) == 2*squared
            # A separate arbitrary test function checks exact cancellation.
            assert sum((x*x+3*x)-(z*z+3*z) for x, z in directed) == 0
            assert squared > 0
            ll = sum(u < ell and v < ell for u, v in edges(walk))
            blocks = runs(walk, ell)
            assert sorted(x for path in blocks for x in path[1:-1]) == list(range(k, ell))
            predicted = edge_counter(walk)
            for path in blocks:
                run_lengths.add(len(path)-2)
                for u, v in zip(path, path[1:]):
                    predicted[tuple(sorted((u, v)))] -= 1
                predicted[tuple(sorted((path[0], path[-1])))] += 1
            actual = edge_counter(tuple(x for x in walk if x >= ell))
            assert all(value >= 0 for value in predicted.values())
            assert +predicted == actual
            assert ll == sum(len(path)-3 for path in blocks)
            bad = sum(len(path)-2 for path in blocks if len(path) >= 4)
            assert bad <= 2*ll
            energy = Q(squared, n**3)
            assert Q(ll, n) <= 4*energy
            saw_wrap |= walk[0] < ell
            count += 1

        # Below half a step, exactly half a step, a step, a narrow strip,
        # and strips truncated by the domain. These are not tour searches.
        cutoff = Q(2*ell-1, 2*n)
        for h in (Q(1, 4*n), Q(1, 2*n), Q(1, n), Q(7, 3*n), Q(1, 100), Q(2)):
            mass = Q(sum(abs(Q(x, n)-cutoff) <= h for x in range(k, n+1)), n)
            assert mass <= 4*h
            if h < Q(1, 2*n):
                assert mass == 0
            strip_count += 1
    assert parities == {(0, 0), (0, 1), (1, 0), (1, 1)}
    assert saw_wrap and 1 in run_lengths and 2 in run_lengths and max(run_lengths) > 2
    print(f"exact finite floors: {len(SIZES)}; prescribed tours: {len(cases)}; all four parities PASS")
    print(f"exact marginals/energy/maximal runs: {count} orientations, wrap and run lengths 1/2/>2 PASS")
    print(f"exact midpoint-strip checks: {strip_count} PASS")


def symbolic_checks():
    x, y, z, s, t = sp.symbols("x y z s t", positive=True)
    g = sp.sqrt(y*z)-sp.sqrt(x*y)-sp.sqrt(x*z)
    p = (1-sp.sqrt(x/(s-x)))/2
    primitive = x/2+sp.sqrt(x*(s-x))/2-s*sp.asin(sp.sqrt(x/s))/2
    expressions = [
        g.subs({y: t, z: t})-(t-2*sp.sqrt(x*t)),
        sp.diff(g, y).subs({y: t, z: t})-(1-sp.sqrt(x/t))/2,
        sp.diff(g, z).subs({y: t, z: t})-(1-sp.sqrt(x/t))/2,
        sp.diff(g, y, 2)-(sp.sqrt(x)-sp.sqrt(z))/(4*y**sp.Rational(3, 2)),
        sp.diff(g, z, 2)-(sp.sqrt(x)-sp.sqrt(y))/(4*z**sp.Rational(3, 2)),
        sp.diff(g, y, z)-1/(4*sp.sqrt(y*z)),
        (sp.diff(p, x)+s/(4*sp.sqrt(x)*(s-x)**sp.Rational(3, 2))).subs(s, x+t),
        (sp.diff(primitive, x)-p).subs(s, x+t),
    ]
    assert all(sp.simplify(expression) == 0 for expression in expressions)
    print(f"independent symbolic first-variation/Hessian/primitive identities: {len(expressions)} PASS")


def numerical_checks(cases):
    for dps in PRECISIONS:
        mp.mp.dps = dps
        tolerance = mp.mpf(10)**(-dps+15)
        count = 0
        for n, k, ell, _, tour in cases:
            n_mp = mp.mpf(n)
            s = mp.mpf(n+k)/n
            cutoff = mp.mpf(2*ell-1)/(2*n)
            points = {i: mp.mpf(i)/n for i in range(k, n+1)}
            p = {i: (1-mp.sqrt(points[i]/(s-points[i])))/2 for i in points}

            def primitive(u):
                u = min(u, cutoff)
                return u/2+mp.sqrt(u*(s-u))/2-s*mp.asin(mp.sqrt(u/s))/2

            potentials = {i: primitive(points[i]) for i in points}

            def cost(walk):
                return mp.fsum(mp.sqrt(u*v) for u, v in edges(walk))/n_mp**2

            reference = mp.fsum(mp.sqrt(i*(n+k-i)) for i in range(k, n+1))/n_mp**2
            ideal = mp.fsum(n+k-i-2*mp.sqrt(i*(n+k-i)) for i in range(k, ell))/n_mp**2
            excess = cost(tour)-reference
            delta = cost(tuple(i for i in tour if i >= ell))-cost(tour)-ideal
            squared = sum((u+v-n-k)**2 for u, v in edges(tour))
            energy = mp.mpf(squared)/n_mp**3
            assert excess > 0 and energy <= 8*excess+tolerance
            linear_terms = []
            crossing_terms = []
            cancellation = []
            for u, v in edges(tour):
                for i, j in ((u, v), (v, u)):
                    z_index = n+k-j
                    x, z = points[i], points[z_index]
                    defect = x-z
                    px = p[i] if i < ell else mp.mpf(0)
                    potential_delta = potentials[i]-potentials[z_index]
                    crossing = (i < ell) != (z_index < ell)
                    error = px*defect-potential_delta
                    assert abs(error) <= mp.mpf(11)/2*defect**2+abs(defect)*crossing+tolerance
                    linear_terms.append(px*defect/n_mp)
                    crossing_terms.append(abs(defect)*crossing/(2*n_mp))
                    cancellation.append(potential_delta/(2*n_mp))
            linear = mp.fsum(linear_terms)
            crossing_mass = mp.fsum(crossing_terms)
            assert abs(mp.fsum(cancellation)) < tolerance
            assert abs(delta-linear) <= 43*energy+tolerance
            assert abs(linear) <= 11*energy+2*crossing_mass+tolerance
            for h in (mp.mpf(1)/(4*n), mp.mpf(1)/(2*n), energy**(mp.mpf(1)/3)):
                assert crossing_mass <= 4*h*h+energy/h+tolerance
            assert abs(delta) <= 54*energy+10*energy**(mp.mpf(2)/3)+tolerance
            assert abs(delta) <= 432*excess+40*excess**(mp.mpf(2)/3)+tolerance
            for path in runs(tour, ell):
                if len(path) == 3:
                    left, low, right = path
                    x, y, z = points[low], points[left], points[right]
                    t = s-x
                    actual = mp.sqrt(y*z)-mp.sqrt(x*y)-mp.sqrt(x*z)
                    ideal_local = t-2*mp.sqrt(x*t)
                    linear_local = p[low]*(y+z-2*t)
                    assert abs(actual-ideal_local-linear_local) <= 3*((y-t)**2+(z-t)**2)+tolerance
            count += 1
        print(f"numerical direct-cost/Taylor/cancellation/threshold/final bounds ({dps} dps): {count} PASS")
    print("Numerical diagnostics only; the uniform little-o theorem is analytic.")


if __name__ == "__main__":
    parameter_checks()
    cases = tuple(fixtures())
    exact_checks(cases)
    symbolic_checks()
    numerical_checks(cases)
    print("PASS: bounded deterministic support; no general tours enumerated or finite optima certified")
