"""Bounded corroboration of the analytic one-level theorem; no tour search.

Default: standard-library exact cyclic/rational checks.
--diagnostic: ten prescribed comparison cases using mpmath, never a certificate.
Run without -O. No production imports, saved artifacts, or random seeds.
"""

import argparse
from collections import Counter
from fractions import Fraction as Q


def supnick(k, n):
    size = n - k + 1
    assert size >= 3
    middle = (size + 1) // 2
    arms = []
    for parity in (1, 2):
        arm = []
        for low in range(parity, middle + 1, 2):
            arm.append(low)
            high = size - low
            if high > middle:
                arm.append(high)
        arms.append(arm)
    return tuple(k + rank - 1 for rank in arms[0] + arms[1][::-1] + [size])


def edges(tour):
    assert len(tour) == len(set(tour)) >= 3
    return Counter(tuple(sorted((a, b)))
                   for a, b in zip(tour, tour[1:] + tour[:1]))


def rank_edges(k, n):
    size = n - k + 1
    h, parity = divmod(size, 2)
    pairs = [(j, size - j) for j in range(1, h + parity)]
    pairs += [(j, size + 2 - j) for j in range(2, h + 1 + parity)]
    pairs += [(1, size)]
    if not parity:
        pairs += [(h, h + 1)]
    return Counter((k + a - 1, k + b - 1) for a, b in pairs)


def insert(tour, k, n):
    # Find the single prescribed edge, not a collection of candidate gaps.
    for i, a in enumerate(tour):
        b = tour[(i + 1) % len(tour)]
        if {a, b} == {k + 1, n}:
            return tour[:i + 1] + (k,) + tour[i + 1:]
    raise AssertionError("missing prescribed insertion edge")


def exact_checks():
    cases = 0
    for k in range(1, 9):
        for n in range(k + 3, k + 67):
            larger, smaller = supnick(k, n), supnick(k + 1, n)
            assert set(larger) == set(range(k, n + 1))
            assert set(smaller) == set(range(k + 1, n + 1))
            assert edges(larger) == rank_edges(k, n)
            assert edges(smaller) == rank_edges(k + 1, n)
            deleted = tuple(a for a in larger if a != k)
            expected = edges(larger)
            expected.subtract({(k, n - 1): 1, (k, n): 1})
            expected.update({(n - 1, n): 1})
            assert edges(deleted) == +expected
            # Negative control: omission of the induced closing chord fails.
            wrong = expected.copy()
            wrong.subtract({(n - 1, n): 1})
            assert edges(deleted) != +wrong
            for oriented in (smaller, smaller[1:] + smaller[:1], smaller[::-1]):
                inserted = insert(oriented, k, n)
                assert tuple(a for a in inserted if a != k) == oriented
                expected = edges(oriented)
                expected.subtract({(k + 1, n): 1})
                expected.update({(k, k + 1): 1, (k, n): 1})
                assert edges(inserted) == +expected
                assert set(inserted) == set(range(k, n + 1))
            if n >= max(4 * k, 40):
                q = n // 4
                high, low = n - q, q - k
                hh = sum(count for (a, b), count in edges(smaller).items()
                         if a > q and b > q)
                assert hh >= high - low >= Q(n, 2)
                assert Q(n, 5) >= 8
            cases += 1
    for k in range(1, 65):
        cutoff = 48 * k * (k + 1) ** 2
        assert cutoff >= max(4 * k, 40, k + 3)
        # Squared positive sides of the comparison in proof (13).
        assert Q(cutoff, 12 * (k + 1)) == 4 * k * (k + 1)
    assert 48 * 1 * 2**2 == 192
    assert 48 * 2 * 3**2 == 864
    print(f"PASS exact: {cases} prescribed rank/deletion/insertion cases; "
          "both parities, N=3, rotations/reversals, omitted-chord negative controls.")
    print("PASS exact: degree counts where applicable; 64 rational cutoff "
          "substitutions, including 192 and 864. No tour enumeration.")


def diagnostic():
    import mpmath as mp

    mp.mp.dps = 50
    guard = mp.mpf("1e-30")
    tau = 2 * mp.pi
    cases = ((1, 4), (1, 7), (1, 8), (1, 192), (1, 193),
             (2, 5), (2, 12), (2, 13), (2, 864), (2, 865))

    def angle(radius, a, b):
        return 2 * mp.atan(mp.sqrt(mp.mpf(a * b) / (radius * (radius + a + b))))

    def score(radius, tour, alternate=False):
        if alternate:
            return mp.fsum(count * 2 * mp.asin(mp.sqrt(
                mp.mpf(a * b) / ((radius + a) * (radius + b))))
                for (a, b), count in edges(tour).items())
        return mp.fsum(count * angle(radius, a, b)
                       for (a, b), count in edges(tour).items())

    def root(tour, n):
        lo, hi = mp.mpf(0), mp.mpf(n * n)
        # Upper bracket follows independently from theta<2 sqrt(ab)/R.
        assert score(hi, tour) < tau
        for _ in range(140):
            mid = (lo + hi) / 2
            if score(mid, tour) > tau:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    print("DIAGNOSTIC ONLY: mpmath=" + mp.__version__
          + "; dps=50; bisections=140; guard=1e-30; ten fixed cases.", flush=True)
    for k, n in cases:
        larger, smaller = supnick(k, n), supnick(k + 1, n)
        deleted = tuple(a for a in larger if a != k)
        inserted = insert(smaller, k, n)
        am, an = root(larger, n), root(smaller, n)
        defect_d = angle(am, n - 1, n) - angle(am, k, n - 1) - angle(am, k, n)
        defect_j = angle(an, k, k + 1) + angle(an, k, n) - angle(an, k + 1, n)
        assert abs(score(am, larger, True) - tau) < guard
        assert abs(score(an, smaller, True) - tau) < guard
        assert abs(score(am, deleted, True) - tau - defect_d) < guard
        assert abs(score(an, inserted, True) - tau - defect_j) < guard
        assert score(am + mp.mpf(n) / 2, deleted, True) <= tau + guard
        if n >= 48 * k * (k + 1)**2:
            assert an > n and am < an and defect_j < -guard
            assert score(an, inserted, True) < tau - guard
        print(f"k={k}, n={n}: A_M/n^2={mp.nstr(am/n**2, 10)}, "
              f"A_N/n^2={mp.nstr(an/n**2, 10)}, "
              f"D(A_M)={mp.nstr(defect_d, 10)}, "
              f"J(A_N)={mp.nstr(defect_j, 10)}", flush=True)
    print("PASS diagnostic: ten prescribed comparisons and alternate-angle "
          "closures; no minimax computation, optimality claim or certification.")


def main():
    if not __debug__:
        raise RuntimeError("run this assertion-based checker without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostic", action="store_true")
    args = parser.parse_args()
    exact_checks()
    if args.diagnostic:
        diagnostic()


if __name__ == "__main__":
    main()
