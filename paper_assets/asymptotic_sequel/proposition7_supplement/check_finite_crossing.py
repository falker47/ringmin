"""Small exact checks for THREE_LEVEL_COMMON_CHAIN.md, Sections 7-10.

Run with python -I -S. No production, prior-checker, result or third-party
imports. Prescribed measures/tours only; no search, optimization or tour
enumeration. Analytic proofs, not these cases, supply universal quantifiers.
"""

from collections import defaultdict
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("This checker requires enabled assertions; omit -O.")


def validate(cuts, widths):
    if not cuts or len(cuts) != len(widths):
        raise ValueError("Use equally sized, nonempty cutoff and width lists.")
    if any(h <= 0 for h in widths):
        raise ValueError("Widths must be positive.")
    if any(a >= b for a, b in zip(cuts, cuts[1:])):
        raise ValueError("Cutoffs must be strictly ordered.")


def separated(cuts, widths):
    validate(cuts, widths)
    return all(widths[i] + widths[i+1] <= cuts[i+1] - cuts[i]
               for i in range(len(cuts)-1))


def marginals(atoms):
    left, right = defaultdict(F), defaultdict(F)
    for x, z, mass in atoms:
        assert mass > 0
        left[x] += mass
        right[z] += mass
    return dict(left), dict(right)


def crossing_totals(atoms, cuts, widths):
    """Direct atom scorer, with no use of the block/separation formula."""
    validate(cuts, widths)
    energy = F(0)
    crossing = [F(0) for _ in cuts]
    short = [F(0) for _ in cuts]
    long = F(0)
    max_crossed = 0
    equality_seen = False
    for x, z, mass in atoms:
        d = abs(x-z)
        energy += mass*d*d
        active = [i for i, b in enumerate(cuts) if (x-b)*(z-b) < 0]
        max_crossed = max(max_crossed, len(active))
        if active:
            assert active == list(range(active[0], active[-1]+1))
        for i in active:
            crossing[i] += mass*d
            if d <= widths[i]:
                short[i] += mass*widths[i]*d
                equality_seen |= d == widths[i]
            else:
                long += mass*widths[i]*d
    assert sum(h*k for h, k in zip(widths, crossing)) == sum(short)+long
    return energy, crossing, short, long, max_crossed, equality_seen


def assert_local_bound(atoms, cuts, widths):
    for x, z, _ in atoms:
        d = abs(x-z)
        long_weight = sum(h for b, h in zip(cuts, widths)
                          if (x-b)*(z-b) < 0 and h < d)
        assert long_weight <= d


def tour_measure(order, n, k):
    """Reconstruct each directed atom from one prescribed genuine cycle."""
    assert len(order) >= 3 and sorted(order) == list(range(k, n+1))
    atoms = []
    for u, v in zip(order, order[1:]+order[:1]):
        atoms.extend(((F(u, n), F(n+k-v, n), F(1, 2*n)),
                      (F(v, n), F(n+k-u, n), F(1, 2*n))))
    return atoms


def as_measure(atoms):
    result = defaultdict(F)
    for x, z, mass in atoms:
        result[x, z] += mass
    return dict(result)


def prescribed_measure_checks():
    count, tour_cases = 0, 0
    parities, multiplicities = set(), set()
    for n in (32, 33, 34, 35):
        k = 6
        order = list(range(k, n+1))
        grid = [F(j, n) for j in order]
        expected = {x: F(1, n) for x in grid}
        parities.add(len(grid) % 2)
        cycle = tour_measure(order, n, k)
        assert as_measure(cycle) == as_measure(tour_measure(order[7:]+order[:7], n, k))
        assert as_measure(cycle) == as_measure(tour_measure(order[::-1], n, k))
        measures = (
            [(x, x, F(1, n)) for x in grid],
            [(x, grid[-i-1], F(1, n)) for i, x in enumerate(grid)],
            cycle,
        )
        for m in (1, 2, 4, 8):
            labels = [k+3+3*i for i in range(m)]
            cuts = [F(2*j-1, 2*n) for j in labels]
            widths = [F(1+i % 2, n) for i in range(m)]
            assert separated(cuts, widths)
            # Every adjacent width sum equals its gap in the m>1 cases.
            assert all(widths[i]+widths[i+1] == cuts[i+1]-cuts[i]
                       for i in range(m-1))
            nested = order
            for ell in labels:
                nested = [j for j in nested if j >= ell]
                assert nested == [j for j in order if j >= ell]
                assert len(nested) >= 3
            for atoms in measures:
                left, right = marginals(atoms)
                assert left == right == expected
                for b, h in zip(cuts, widths):
                    for radius in (F(1, 4*n), F(1, 2*n), h, F(1)):
                        strip = sum(mass for x, mass in left.items()
                                    if abs(x-b) <= radius)
                        assert strip <= 4*radius
                assert_local_bound(atoms, cuts, widths)
                e, cross, short, long, reached, _ = crossing_totals(atoms, cuts, widths)
                for i, h in enumerate(widths):
                    strip = sum(mass for x, mass in left.items() if abs(x-cuts[i]) <= h)
                    assert short[i] <= h*h*strip <= 4*h**3
                assert long <= e
                assert sum(h*v for h, v in zip(widths, cross)) <= 4*sum(h**3 for h in widths)+e
                multiplicities.add(reached)
                count += 1
                tour_cases += atoms is cycle
    assert count == 48 and tour_cases == 16
    assert parities == {0, 1} and {1, 2, 4, 8} <= multiplicities
    print("PASS 48 prescribed measures: equal marginals, strips, single E, up to 8 crossings")
    print("PASS 16 tour/cutoff cases: oriented mass, wrap, rotation, reversal, nesting, both parities")


def boundary_and_sharpness_checks():
    # d=h belongs to SHORT; the midpoint strip bound is attained at radius 1/2.
    atoms = [(F(0), F(1), F(1)), (F(1), F(0), F(1))]
    assert sum(abs(x-F(1, 2)) <= F(1, 2) for x in (F(0), F(1))) == 4*F(1, 2)
    result = crossing_totals(atoms, [F(1, 2)], [F(1)])
    assert result[2] == [F(2)] and result[3] == 0 and result[5]
    # Cutoff endpoints are not strict crossings; identity pairs have d=0.
    endpoint = crossing_totals(atoms, [F(0), F(1)], [F(1, 2)]*2)
    assert endpoint[1] == [0, 0]
    assert separated([F(0), F(1)], [F(1, 2)]*2)

    # Construct the necessity witness algebraically for each prescribed overlap.
    for gap, left, right in ((F(1), F(3, 5), F(3, 5)),
                             (F(1), F(2), F(1, 10)),
                             (F(1, 10), F(1, 5), F(3, 10))):
        total = left+right
        d = (max(gap, left, right)+total)/2
        epsilon = (d-gap)/2
        x, z = -epsilon, gap+epsilon
        assert x < 0 < gap < z and abs(x-z) == d
        assert max(left, right) < d < total
        assert total*d > d*d

    x, z, h = F(-1, 20), F(21, 20), F(3, 5)
    assert 2*h*(z-x) == F(33, 25) > (z-x)**2 == F(121, 100)
    cuts, widths = list(map(F, (0, 1, 3))), [F(3, 4), F(3, 4), F(1, 4)]
    assert sum(widths) <= cuts[-1]-cuts[0] and not separated(cuts, widths)
    d = F(5, 4)
    assert (widths[0]+widths[1])*d > d*d

    # On this bounded support, overlapping widths need no long energy at all.
    cuts, widths = [F(1, 3), F(2, 3)], [F(1), F(1)]
    assert not separated(cuts, widths)
    assert_local_bound(atoms, cuts, widths)
    e, cross, short, long, _, _ = crossing_totals(atoms, cuts, widths)
    assert long == 0 and sum(h*k for h, k in zip(widths, cross)) <= 4*sum(h**3 for h in widths)+e
    for b in cuts:
        # The bound needed at width 1 holds; also the full strip condition
        # holds here: first atom at distance 1/3, second at distance 2/3.
        for radius in (F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(1)):
            assert sum(abs(x-b) <= radius for x in (F(0), F(1))) <= 4*radius
    print("PASS boundaries and sharpness: d=h, cutoff endpoints, adjacent necessity, bounded-domain exception")


def unseparated_counterexample():
    n = 200
    labels = list(range(39, 201))
    transform = {j: j+60 if 60 <= j <= 119 else j-60 if 120 <= j <= 179 else j
                 for j in labels}
    assert sorted(transform.values()) == labels
    assert all(transform[transform[j]] == j for j in labels)
    assert all(transform[239-j] == 239-transform[j] for j in labels)
    atoms = [(F(j, n), F(transform[j], n), F(1, n)) for j in labels]
    left, right = marginals(atoms)
    assert left == right == {F(j, n): F(1, n) for j in labels}
    edge_measure = as_measure([(x, F(239, 200)-z, w) for x, z, w in atoms])
    assert edge_measure == {(y, x): w for (x, y), w in edge_measure.items()}
    cuts = [F(j, 400) for j in (237, 239, 241, 243)]
    widths = [F(1, 10)]*4
    assert not separated(cuts, widths)
    # Check all actual strip jump distances, sufficient for every radius.
    for b in cuts:
        for radius in sorted({abs(x-b) for x in left}):
            assert sum(mass for x, mass in left.items() if abs(x-b) <= radius) <= 4*radius
    counts = [sum((x-b)*(z-b) < 0 for x, z, _ in atoms) for b in cuts]
    assert counts == [118, 120, 118, 116]
    e, cross, _, _, reached, _ = crossing_totals(atoms, cuts, widths)
    assert reached == 4 and e == F(27, 500)
    assert cross == [F(177, 1000), F(9, 50), F(177, 1000), F(87, 500)]
    lhs = sum(h*k for h, k in zip(widths, cross))
    rhs = 4*sum(h**3 for h in widths)+e
    assert lhs == F(177, 2500) and rhs == F(7, 100)
    assert lhs-rhs == F(1, 1250)
    print("PASS exact unseparated counterexample: 177/2500 > 7/100; excess 1/1250")


def scalar_and_floor_checks():
    for widths in ([F(1, 100)], [F(3, 1000), F(9, 1000)], [F(1, 1000)]*8):
        total = sum(widths)
        denominator = 16+432*total
        assert denominator > total > 0
        for numerator in (F(-1), F(0), F(1, 100000)):
            optimum = max(numerator, 0)/denominator
            value = lambda e: max(e, numerator/total-(denominator/total-1)*e)
            assert value(optimum) == optimum
            for e in (F(0), optimum/2, optimum, optimum+1):
                assert value(e) >= optimum
            for n in (102, 1000):
                error = 19*total/F(2*n)
                assert max(numerator-error, 0) >= max(numerator, 0)-error
                # Allow simultaneous adverse errors at all m cutoffs.
                errors = [-F(19, 2*n)]*len(widths)
                assert sum(h*v for h, v in zip(widths, errors)) == -error
        assert 8*(54*total+2) == denominator
    total = F(3, 1000)+F(9, 1000)
    assert total == F(3, 250)
    assert F(3, 1000)**3+F(9, 1000)**3 == F(189, 250000000)
    assert 16+432*total == F(2648, 125)

    # Concrete sufficient N for four fixed cutoffs, using the coarser
    # already-proved optimizer enclosure only as a dependency input.
    q_low, q_high = F("0.19502009"), F("0.19502010")
    beta = [F(1, 5), F(21, 100), F(11, 50), F(23, 100)]
    widths = [F(1, 1000)]*4
    start = 1000
    assert q_low-F(1, 102) > F(1, 6) and q_high < F(1, 5)
    assert start*(beta[0]-q_high) > 1
    assert all(start*(beta[i+1]-beta[i]-widths[i]-widths[i+1]) >= 1 for i in range(3))
    assert 1+F(1, 6)-2*beta[-1] == F(53, 75) > F(1, 2)
    for n in (1000, 1001, 1002, 1003):
        ell = [(b*n).__floor__() for b in beta]
        assert F(ell[0], n) > q_high and ell[-1] <= n-2
        cuts = [F(2*j-1, 2*n) for j in ell]
        assert separated(cuts, widths)

    # Macroscopic equality alone does not survive finite floors.
    beta = [F(1, 5), F(23, 100)]
    widths = [F(1, 100), F(1, 50)]
    n = 104
    cuts = [F(2*(b*n).__floor__()-1, 2*n) for b in beta]
    assert separated(beta, widths) and not separated(cuts, widths)
    assert cuts[1]-cuts[0] == F(3, 104) < sum(widths) == F(3, 100)
    print("PASS scalar signs, finite errors, 2-cutoff recovery, 4-cutoff domain, finite-floor negative control")


def other_negative_controls():
    widths = [F(1, 1000)]*4
    energy = F(1, 1000000)
    independent = [4*h*h+energy/h for h in widths]
    assert all(h*k <= 4*h**3+energy for h, k in zip(widths, independent))
    assert sum(h*k for h, k in zip(widths, independent)) > 4*sum(h**3 for h in widths)+energy
    # A cutoff on a grid point invalidates the tiny-strip estimate.
    n = 1000
    assert F(1, n) > 4*F(1, 8*n)
    for cuts, widths in (([], []), ([F(0)], []), ([F(0)], [F(0)]),
                          ([F(0)], [F(-1)]), ([F(0), F(0)], [F(1)]*2),
                          ([F(1), F(0)], [F(1)]*2)):
        try:
            validate(cuts, widths)
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed parameters were accepted.")
    print("PASS negative controls: independent budgets, on-grid cutoff, malformed parameters")


if __name__ == "__main__":
    prescribed_measure_checks()
    boundary_and_sharpness_checks()
    unseparated_counterexample()
    scalar_and_floor_checks()
    other_negative_controls()
    print("PASS all finite shared-crossing checks; universal claims are analytic")
