"""Bounded exact checks of the new joint-domain bookkeeping and sign gates.

No search over permutations, radius scoring, quadrature or optimization.
The two one-variable minimum theorems are accepted inputs, not tested here.
All finite comparisons use integers/Fraction and a second list construction.
Run with python -S; no files are written and no old checker is imported.
"""

from fractions import Fraction as Q


XL, XH = Q(719, 2500), Q(2877, 10000)
MAX_M = 24
PROBE_M = (2, 3, 4, 5, 7, 8, 15, 16, 23, 24)


def construct(m, alpha, lam):
    if type(m) is not int or m < 2:
        raise ValueError("m must be an integer >=2")
    alpha, lam = Q(alpha), Q(lam)
    if not (0 <= alpha <= Q(1, 2) and Q(1, 4) <= lam < 1-alpha):
        raise ValueError("pair outside the strict pre-wrap domain")
    s, q = (alpha*m)//1, 2*((lam*m/2)//1)
    ranks = [q+2-i if i <= q and i % 2 == 0 else i
             for i in range(1, m+1)]
    p = [m+1+(j+s-1) % m for j in ranks]
    return s, q, ranks, p


def audit_case(m, alpha, lam, coverage):
    alpha, lam = Q(alpha), Q(lam)
    s, q, ranks, p = construct(m, alpha, lam)
    r, beta, length = m-s, Q(s, m), Q(q, m)
    a, b, A = (1+alpha)/3, 1-alpha, 1+alpha
    assert 0 <= alpha-beta < Q(1, m)
    assert 0 <= lam-length < Q(2, m)
    assert s+q < m and r >= q+1 and q % 2 == 0
    assert Q(r-q) >= m*(b-lam) > 0

    # Separate construction: rotate an increasing high list, then reverse
    # its even slots. This uses neither the rank formula nor modular H.
    highs = list(range(m+1, 2*m+1))
    other = highs[s:]+highs[:s]
    other[1:q:2] = other[1:q:2][::-1]
    assert p == other
    assert sorted(p) == highs and len(set(p)) == m
    assert sorted(ranks) == list(range(1, m+1))
    assert [ranks[j-1] for j in ranks] == list(range(1, m+1))
    if q in (0, 2):
        assert ranks == list(range(1, m+1))

    cells = set(range(1, m+1))
    exc = {1, r, r+1}
    if q:
        exc.add(q+1)
    exc &= cells
    interior = set(range(2, q+1)) if q else set()
    ordinary = cells-exc-interior
    assert not exc & interior and len(exc) <= 4
    assert len(interior)+len(exc)+len(ordinary) == m
    if q:
        expected_exceptions = (4 if s else 3)-(r == q+1)
        assert len(interior) == q-1
        assert sum(i % 2 == 0 for i in interior) == q//2
        assert sum(i % 2 == 1 for i in interior) == q//2-1
    else:
        expected_exceptions = 2 if s == 0 or r == 1 else 3
        if r == 1:
            assert (m, s, alpha, exc) == (2, 1, Q(1, 2), {1, 2})
            coverage.add("q0_low_seam_equals_wrap_endpoint")
    assert len(exc) == expected_exceptions

    # All seam pairs use the independently built list's cyclic predecessor.
    def pair(i):
        return other[(i-2) % m], other[i-1]

    assert pair(1) == ((m+s, m+s+1) if s else (2*m, m+1))
    if q:
        assert pair(q+1) == (m+s+2, m+s+q+1)
        if r == q+1:
            coverage.add("junction_endpoint_shift" if s
                         else "junction_endpoint_zero_shift")
    if s:
        assert pair(r+1) == (2*m, m+1)
    assert other[r-1] == 2*m
    assert 1 <= Q(r, m)+alpha < 2
    assert 1+(Q(r, m)+alpha) % 1 == Q(r, m)+alpha

    for i in cells:
        t = Q(i, m)
        prev, curr = (Q(v, m) for v in pair(i))
        if i <= q:
            target = ((A+t, A+lam-t) if i % 2 == 0
                      else (A+lam-t, A+t))
        else:
            h = 1+(t+alpha) % 1
            target = h, h
        assert 1 <= prev <= 2 and 1 <= curr <= 2
        assert all(1 <= v <= 2 for v in target)

        if i in interior:
            if i % 2 == 0:
                assert (prev, curr) == (1+beta+t-Q(1, m),
                                       1+beta+length-t+Q(2, m))
            else:
                assert (prev, curr) == (1+beta+length-t+Q(3, m),
                                       1+beta+t)
                assert 0 < prev-target[0] <= Q(3, m)
        elif i in ordinary:
            assert i < r or i > r+1
            if i < r:
                assert t < b
                assert (prev, curr) == (1+beta+t-Q(1, m), 1+beta+t)
            else:
                assert t > b
                assert (prev, curr) == (beta+t-Q(1, m), beta+t)
            if q:
                assert i >= q+2
        if i not in exc:
            assert max(abs(prev-target[0]), abs(curr-target[1])) <= Q(3, m)

    if not q:
        coverage.add("q0")
    if q == 2:
        coverage.add("q2_identity")
    if not alpha:
        coverage.add("alpha0")
    if alpha == Q(1, 2):
        coverage.add("alpha_half_odd" if m % 2 else "alpha_half_even")
    if lam == Q(1, 4):
        coverage.add("lambda_lower_endpoint")
    if lam == a:
        coverage.add("diagonal_switch_tie")
    if lam > a:
        coverage.add("tail_after_diagonal_switch")
    if alpha == beta and lam == length:
        coverage.add("both_floors_exact")
    if alpha > beta and lam > length:
        coverage.add("both_floor_errors_positive")
    return s, q


def rational_gates():
    assert Q(1, 4) < XL < XH < Q(1, 3)
    assert XL-Q(1, 4) == Q(47, 1250)
    assert Q(1, 2)-Q(3, 2)*XH == Q(1369, 20000) > 0
    eta = (Q(1, 3)-XH)/2
    assert eta == Q(1369, 60000) > 0
    cutoff = Q(1, 3)-eta
    assert cutoff == Q(18631, 60000) > XH
    # Endpoint values of the affine gates in the analytic domain proof.
    for alpha in (Q(0), Q(1, 2)):
        A, b = 1+alpha, 1-alpha
        assert Q(1, 4)/A <= Q(1, 4) < XL < XH < Q(1, 3) <= b/A <= 1
        assert b-A/3 == (2-4*alpha)/3 >= 0
        assert b-alpha/3 == 1-Q(4, 3)*alpha >= Q(1, 3)
    print("PASS rational gates: lower margin 47/1250; wrap margin 1369/20000; "
          "eta 1369/60000; boundary cutoff 18631/60000>XH")


def main():
    rational_gates()
    coverage, states, floor_cases, probes = set(), set(), 0, 0
    for m in range(2, MAX_M+1):
        for s in range(m//2+1):
            alpha_lo = Q(s, m)
            for q in range(0, m-s, 2):
                lam_lo = max(Q(1, 4), Q(q, m))
                lam_hi = min(Q(q+2, m), 1-alpha_lo)
                if lam_lo >= lam_hi:
                    continue
                # These inequalities exactly characterize a nonempty
                # admissible floor state. Use its lower endpoint first.
                assert audit_case(m, alpha_lo, lam_lo, coverage) == (s, q)
                states.add((m, s, q))
                floor_cases += 1
                # A second witness in its relative interior checks errors
                # in both floors. The alpha=1/2 face may have zero width.
                alpha_hi = min(Q(s+1, m), Q(1, 2), 1-lam_lo)
                alpha_mid = (alpha_lo+alpha_hi)/2
                mid_hi = min(Q(q+2, m), 1-alpha_mid)
                lam_mid = (lam_lo+mid_hi)/2
                assert audit_case(m, alpha_mid, lam_mid, coverage) == (s, q)
                floor_cases += 1
    print(f"PASS floor bookkeeping: {len(states)} admissible (m,s,q) states, "
          f"{floor_cases} endpoint/interior cases, m=2..{MAX_M}")

    for alpha in (Q(0), Q(1, 10), Q(1, 3), Q(1, 2)):
        for gap in (Q(1, 2**8), Q(1, 2**40)):
            for m in PROBE_M:
                audit_case(m, alpha, 1-alpha-gap, coverage)
                probes += 1
    for alpha in (Q(0), Q(1, 4)):
        for m in PROBE_M:
            audit_case(m, alpha, (1+alpha)/3, coverage)
            probes += 1
    print(f"PASS boundary probes: {probes} cases; gaps 1/256 and 1/2^40; "
          "both alpha endpoints/parities and lambda=A/3 ties")

    required = {
        "q0", "q2_identity", "alpha0", "alpha_half_odd", "alpha_half_even",
        "q0_low_seam_equals_wrap_endpoint", "junction_endpoint_shift",
        "junction_endpoint_zero_shift", "lambda_lower_endpoint",
        "diagonal_switch_tie", "tail_after_diagonal_switch",
        "both_floors_exact", "both_floor_errors_positive",
    }
    assert required <= coverage, sorted(required-coverage)
    print(f"PASS {len(required)} coverage gates: occurrence/involution, cyclic "
          "pairs, coincident exception counts, complete partitions, 3/m errors")

    invalid = (
        (1, Q(0), Q(1, 4)),
        (Q(5, 2), Q(0), Q(1, 4)),
        (2, -Q(1, 100), Q(1, 4)),
        (2, Q(51, 100), Q(1, 4)),
        (2, Q(0), Q(249, 1000)),
        (2, Q(0), Q(1)),
        (2, Q(1, 2), Q(1, 2)),
        (2, Q(1, 4), Q(4, 5)),
    )
    for args in invalid:
        try:
            construct(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid input accepted: {args}")
    print(f"PASS domain rejection: {len(invalid)} cases including excluded wrap")
    print("NOTE: bounded exact bookkeeping only; accepted minima and imported "
          "full-feasibility/root theorems are not re-certified.")


if __name__ == "__main__":
    main()
