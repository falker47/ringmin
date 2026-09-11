"""Bounded exact audit for Delta=1/250; run with python -I -S.

No project imports, files, third-party libraries or implicit-root estimates.
Float bisection proposes rational brackets only. Every reported root sign
and all-pairs placement is checked with outward integer intervals.
The finite checks supplement, rather than replace, the analytic theorem.
"""

from fractions import Fraction as Q
from itertools import product
from math import asin, ceil, floor, fsum, isqrt, pi, sqrt

if not __debug__:
    raise SystemExit("ERROR: assertions must be enabled")

AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
LL, LH = (1 + AL) * XL, (1 + AH) * XH
EL, EH, DELTA = Q(43, 1000), Q(11, 250), Q(1, 250)
SIZES = tuple(range(2, 513)) + (998, 999, 1000, 1001, 1002,
                               1499, 1500, 1501, 2047, 2048, 2049,
                               2499, 2500, 2501)
ROOT_SIZES = (2, 3, 6, 7, 9, 10, 46, 499, 500, 501,
              999, 1000, 1001, 1500)
SCALE = 10**32
TERMS = 64


def floor_cases(m):
    # Strict lower < parameter < upper. Correlation is ignored to add cases.
    return product(range(floor(AL * m), ceil(AH * m)),
                   range(floor(LL * m / 2), ceil(LH * m / 2)),
                   range(floor(EL * m / 2), ceil(EH * m / 2)))


def recover(m, s, q, d):
    assert all(type(t) is int for t in (m, s, q, d))
    f = 2 * (m // 500)
    assert m >= 2 and 0 <= s < m
    assert 0 <= f <= d <= q and q % 2 == d % 2 == 0
    assert 2 * (s + q + d + f) < m
    highs = list(range(m + 1, 2 * m + 1))
    p = highs[s:] + highs[:s]
    for a, length in ((0, q), (q, d), (q + d, f)):
        slots = list(range(a + 1, a + length, 2))
        for k in range(len(slots) // 2):
            left, right = slots[k], slots[-1 - k]
            p[left], p[right] = p[right], p[left]
    return p


def displayed(m, s, q, d):
    e, z = q + d, q + d + 2 * (m // 500)
    ranks = []
    for i in range(1, m + 1):
        j = i
        if i % 2 == 0:
            if i <= q:
                j = q + 2 - i
            elif i <= e:
                j = q + e + 2 - i
            elif i <= z:
                j = e + z + 2 - i
        ranks.append(j)
    assert sorted(ranks) == list(range(1, m + 1))
    assert all(ranks[ranks[i] - 1] == i + 1 for i in range(m))
    return [m + 1 + (j + s - 1) % m for j in ranks]


def cell_audit(m, s, q, d, p):
    f, e, r = 2 * (m // 500), q + d, m - s
    z = e + f
    assert p == displayed(m, s, q, d)
    assert sorted(p) == list(range(m + 1, 2 * m + 1))
    assert r >= z + 2 and p[r - 1] == 2 * m
    exceptions = {1: (m + s, m + s + 1) if s else (2 * m, m + 1),
                  r: (2 * m - 1, 2 * m)}
    if s:
        exceptions[r + 1] = (2 * m, m + 1)
    if q:
        exceptions[q + 1] = (m + s + 2, m + s + q + 1)
    if d:
        exceptions[e + 1] = (m + s + q + 2, m + s + e + 1)
    if f:
        exceptions[z + 1] = (m + s + e + 2, m + s + z + 1)
    interiors = {}
    for a, length in ((0, q), (q, d), (e, f)):
        for i in range(a + 2, a + length + 1):
            assert i not in exceptions and i not in interiors
            interiors[i] = (a, length)
        evens = list(range(a + 2, a + length + 1, 2))
        fixed = sum(p[i - 1] == m + 1 + (i + s - 1) % m for i in evens)
        assert fixed == (length % 4 == 2)
    for i in range(1, m + 1):
        pair = p[i - 2], p[i - 1]
        if i in exceptions:
            assert pair == exceptions[i]
        elif i in interiors:
            a, length = interiors[i]
            if i % 2 == 0:
                expected = m + s + i - 1, m + s + 2 * a + length + 2 - i
                panel, limit = (i - 2, i), 2
            else:
                expected = m + s + 2 * a + length + 3 - i, m + s + i
                panel, limit = (i - 1, i + 1), 4
            assert pair == expected
            # Affine coordinate errors attain their max at panel endpoints.
            for u in panel:
                hi = m + s + u, m + s + 2 * a + length - u
                if i % 2:
                    hi = hi[::-1]
                assert max(abs(i - u), abs(pair[0] - hi[0]),
                           abs(pair[1] - hi[1])) <= limit
        else:
            base = m + s if i < r else s
            assert pair == (base + i - 1, base + i)
            for u in (i - 1, i):
                assert max(abs(i - u), *(abs(h - base - u) for h in pair)) <= 1
    actual = len(interiors), len(exceptions), m - len(interiors) - len(exceptions)
    expected = ((0, 2, m - 2) if q == 0 else
                (q - 1, 3, m - q - 2) if s == 0 else
                (q - 1, 4, m - q - 3) if d == 0 else
                (q + d - 2, 5, m - q - d - 3) if f == 0 else
                (q + d + f - 3, 6, m - q - d - f - 3))
    assert actual == expected and min(actual) >= 0 and sum(actual) == m
    # Check surviving arcs from the actual deleted cycle, not an odd criterion.
    cycle = [h for i, high in enumerate(p, 1) for h in (i, high) if h != 2 * m]
    nxt = dict(zip(cycle, cycle[1:] + cycle[:1]))
    used, j = set(), r % m + 1
    for i in range(1, m + 1):
        left, right = p[i - 2], p[i - 1]
        assert (2 * m in (left, right)) == (i in (r, j))
        if i in (r, j):
            continue
        assert nxt[left] == i and nxt[i] == right
        for edge in ((left, i), (i, right)):
            assert edge not in used
            used.add(edge)
    assert nxt[r] == j and len(used) == 2 * m - 4
    assert len(cycle) - len(used) == 3
    return len(exceptions)


def gates():
    assert Q(1, 2) - AH - LH - EH - DELTA == Q(23541513, 10**9) > 0
    ell = (1 + AL) * (1 - 3 * XH) - 3 * EH
    assert ell == Q(1986317, 10**8)
    assert ell - 4 * DELTA == Q(386317, 10**8) > 0
    assert ell / 3 - DELTA == Q(786317, 3 * 10**8) > 0
    assert 1 + AH + LH + EH + DELTA / 2 == Q(1474458487, 10**9) < Q(3, 2)
    assert 0 < DELTA < EL < EH < LL < LH
    assert 6 * LH < 2 < 7 * LL and 9 * AH < 1 < 10 * AL
    assert 45 * EH < 2 < 47 * EL
    assert Q(1, 1000)**3 / -24 + DELTA**3 / 36 == Q(1, 576000000)
    for m, f in ((499, 0), (500, 2), (999, 2), (1000, 4), (1500, 6)):
        assert 2 * (m // 500) == f
    assert [(s, 2 * q, 2 * d) for s, q, d in floor_cases(500)] == [(54, 158, 20)]
    assert list(floor_cases(1000)) == [(109, 159, 21)]
    m = 2048
    err = Q(1024, m) + Q(16384, 3 * m**2)
    omit = Q(96, m) + Q(2048, m**2) + Q(32768, 3 * m**3)
    assert err < 1 and omit < 1
    assert 16 - err - omit > 14 > 2 * Q(22, 7)
    assert 3 + err < 4 < 2 * 3
    assert 4 * 4 + 11 * 4 + 38 * 3 == 174
    assert 174 + 1024 == 1198
    assert 2 * Q(1, 2 * Q(1, 32)**2) == 1024
    assert 2 * Q(1, 12 * Q(1, 32)**3) == Q(16384, 3)
    assert Q(3, 4) * Q(7, 4) > 1  # asin-error rationalization denominator
    assert 2 - 1 - Q(3, 8) == Q(5, 8)  # high-shell small-angle branch
    # Residual-box vertices enclose every affine panel/union error, including ties.
    for ra, rl, re, rd in product((Q(0), Q(1)), (Q(0), Q(2)),
                                  (Q(0), Q(2)), (Q(0), Q(2))):
        assert ra + 3 * rl + 2 * re + rd <= 13
        assert ra + rl <= 3 and ra + 2 * rl + re <= 7
        assert ra + 2 * rl + 2 * re + rd <= 11
    # Positive radicands and the centered chord/rationalization identity.
    for alpha, x, eps in product((AL, AH), (XL, XH), (EL, EH)):
        a = 1 + alpha
        v = a * x + eps
        b, mid = a + v, a + v + DELTA / 2
        assert b > 4 * (v + DELTA) and v + DELTA < a / 3 < 1 - alpha
        for u in (Q(0), DELTA / 2, DELTA):
            rad = (b + u) * (b + DELTA - u)
            assert rad == mid**2 - (u - DELTA / 2)**2 > 0


def updiv(a, b):
    assert b > 0
    return -((-a) // b)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def isub(a, b):
    return a[0] - b[1], a[1] - b[0]


def imul(a, b):
    assert min(*a, *b) >= 0
    return a[0] * b[0] // SCALE, updiv(a[1] * b[1], SCALE)


def idiv(a, b):
    assert a[0] >= 0 and b[0] > 0
    return a[0] * SCALE // b[1], updiv(a[1] * SCALE, b[0])


def sqrtq(value):
    value = Q(value)
    assert value >= 0
    k = isqrt(value.numerator * SCALE**2 // value.denominator)
    hi = k if k * k * value.denominator == value.numerator * SCALE**2 else k + 1
    assert Q(k, SCALE)**2 <= value <= Q(hi, SCALE)**2
    return k, hi


def isqrt_interval(value):
    assert value[0] >= 0
    lo, hi = isqrt(value[0] * SCALE), isqrt(value[1] * SCALE)
    if hi * hi < value[1] * SCALE:
        hi += 1
    return lo, hi


def atan_interval(value):
    assert value[0] >= 0
    factor = 1
    while value[1] > SCALE // 2:
        # atan(x)=2 atan(x/(1+sqrt(1+x*x))), x>=0.
        value = idiv(value, iadd((SCALE, SCALE),
                                isqrt_interval(iadd((SCALE, SCALE), imul(value, value)))))
        factor *= 2
        assert factor <= 16
    square, power, total = imul(value, value), value, (0, 0)
    for k in range(TERMS):
        term = power[0] // (2 * k + 1), updiv(power[1], 2 * k + 1)
        total = iadd(total, term) if k % 2 == 0 else isub(total, term)
        power = imul(power, square)
    # TERMS is even: the partial sum is below atan, next term bounds remainder.
    assert TERMS % 2 == 0
    return factor * total[0], factor * (total[1] + updiv(power[1], 2 * TERMS + 1))


def theta(R, h, k):
    assert R > 0 and min(h, k) > 0
    # Independent of the asin formula that proposes the floating root bracket.
    rad = Q(h * k) / (R * (R + h + k))
    assert rad / (1 + rad) == Q(h * k) / ((R + h) * (R + k))
    lo, hi = atan_interval(sqrtq(rad))
    return 2 * lo, 2 * hi


def score(R, p, omitted=()):
    total, rows = (0, 0), []
    for i, right in enumerate(p, 1):
        a, b, c = theta(R, p[i - 2], i), theta(R, i, right), theta(R, p[i - 2], right)
        row = max(a[0] + b[0], c[0]), max(a[1] + b[1], c[1])
        rows.append((a, b, c))
        if i not in omitted:
            total = iadd(total, row)
    return total, rows


def bracket(p, tau, omitted=()):
    m = len(p)
    lo, hi = 0.0, float(2 * m**2)
    for _ in range(60):
        R = (lo + hi) / 2
        vals = []
        for i, right in enumerate(p, 1):
            if i in omitted:
                continue
            left = p[i - 2]
            a = 2 * asin(sqrt(i * left / ((R + i) * (R + left))))
            b = 2 * asin(sqrt(i * right / ((R + i) * (R + right))))
            c = 2 * asin(sqrt(left * right / ((R + left) * (R + right))))
            vals.append(max(a + b, c))
        if fsum(vals) > 2 * pi:
            lo = R
        else:
            hi = R
    lower, upper = Q(floor(lo * 10**6) - 1, 10**6), Q(ceil(hi * 10**6) + 1, 10**6)
    below, _ = score(lower, p, omitted)
    above, rows = score(upper, p, omitted)
    assert lower > 0 and below[0] > tau[1] and above[1] < tau[0]
    assert upper - lower <= Q(1, 100000)
    return lower, upper, rows


def placement(rows, p, tau, omit_chord=None):
    xs = [a[1] for a, _, _ in rows]
    ys = [max(b[1], c[1] - a[1]) for a, b, c in rows]
    if omit_chord is not None:
        ys[omit_chord] = rows[omit_chord][1][1]
    assert sum(xs) + sum(ys) < tau[0]
    # Angles are rational. The last cyclic gap absorbs exact 2*pi - sum.
    vertices, angles, phi = [], [], 0
    for i, high in enumerate(p):
        vertices.extend((i + 1, high))
        angles.extend((phi, phi + ys[i]))
        if i + 1 < len(p):
            phi += ys[i] + xs[i + 1]
    assert tau[0] - angles[-1] >= xs[0]
    return vertices, angles


def all_pairs(R, vertices, angles, tau):
    universal = theta(R, max(vertices), max(vertices))[1]
    count = detailed = 0
    for j, right in enumerate(vertices):
        for i in range(j):
            forward = angles[j] - angles[i]
            backward = tau[0] - forward
            assert min(forward, backward) > 0
            # Monotonicity supplies a certified uniform bound for long paths.
            if min(forward, backward) < universal:
                need = theta(R, vertices[i], right)[1]
                assert forward >= need and backward >= need
                detailed += 1
            count += 1
    return count, detailed


def reject(action):
    try:
        action()
    except AssertionError:
        return 1
    raise AssertionError("negative control was incorrectly accepted")


def main():
    gates()
    cases = cells = seams = 0
    for m in SIZES:
        for s, q2, d2 in floor_cases(m):
            q, d = 2 * q2, 2 * d2
            p = recover(m, s, q, d)
            seams += cell_audit(m, s, q, d, p)
            cases += 1
            cells += m
    print(f"EXACT gates/floors/cells/panels/deletion: sizes={len(SIZES)} cases={cases} cells={cells} seams={seams}")
    # Machin's identity with alternating-series directed intervals.
    # tan(2 atan(1/5))=5/12; tan(4 atan(1/5))=120/119.
    # Both doubled angles stay below pi/2; subtracting atan(1/239)
    # gives a positive angle below pi/2 with tangent 1, hence pi/4.
    t2 = 2 * Q(1, 5) / (1 - Q(1, 5)**2)
    t4 = 2 * t2 / (1 - t2**2)
    assert 0 < t2 < 1 and t4 == Q(120, 119)
    assert (t4 - Q(1, 239)) / (1 + t4 / 239) == 1
    assert atan_interval((0, 0)) == (0, 0)
    a = atan_interval((SCALE // 5, SCALE // 5))
    b = atan_interval((SCALE // 239, updiv(SCALE, 239)))
    pi_box = 16 * a[0] - 4 * b[1], 16 * a[1] - 4 * b[0]
    assert 3 * SCALE < pi_box[0] < pi_box[1] < Q(22, 7) * SCALE
    assert pi_box[1] - pi_box[0] < 10**6
    tau = 2 * pi_box[0], 2 * pi_box[1]
    roots = odd_roots = pairs = detailed = negatives = 0
    for m in ROOT_SIZES:
        for s, q2, d2 in floor_cases(m):
            q, d = 2 * q2, 2 * d2
            p = recover(m, s, q, d)
            low, high, rows = bracket(p, tau)
            vertices, angles = placement(rows, p, tau)
            n, k = all_pairs(high, vertices, angles, tau)
            pairs += n
            detailed += k
            keep = [i for i, h in enumerate(vertices) if h != 2 * m]
            n, k = all_pairs(high, [vertices[i] for i in keep], [angles[i] for i in keep], tau)
            pairs += n
            detailed += k
            if m >= 4:
                r = m - s
                _, retained_hi, _ = bracket(p, tau, (r, r % m + 1))
                assert retained_hi < low
                odd_roots += 1
            roots += 1
            if m == 1000:
                # Removing a genuinely binding interior chord must fail geometry.
                bad = next(i for i, (a, b, c) in enumerate(rows)
                           if i > 0 and c[0] > a[1] + b[1] + 1000)
                vv, aa = placement(rows, p, tau, omit_chord=bad)
                negatives += reject(lambda: all_pairs(high, vv, aa, tau))
            print(f"EXACT root/all-pairs m={m} floors=({s},{q},{d}) f={2*(m//500)} bracket=[{low},{high}]")
    m, s, q, d = 1000, 109, 318, 42
    p = recover(m, s, q, d)
    duplicate = p.copy()
    duplicate[0] = duplicate[1]
    negatives += reject(lambda: cell_audit(m, s, q, d, duplicate))
    merged = list(range(m + 1, 2 * m + 1))
    merged = merged[s:] + merged[:s]
    merged[1:q:2] = merged[1:q:2][::-1]
    merged[q + 1:q + d + 4:2] = merged[q + 1:q + d + 4:2][::-1]
    negatives += reject(lambda: cell_audit(m, s, q, d, merged))
    false_predecessor = p.copy()
    false_predecessor[q + d - 1], false_predecessor[q + d] = (
        false_predecessor[q + d], false_predecessor[q + d - 1])
    negatives += reject(lambda: cell_audit(m, s, q, d, false_predecessor))
    negatives += reject(lambda: recover(1, 0, 0, 0))
    negatives += reject(lambda: recover(500, 54, 159, 22))
    assert pairs > 10**6 and negatives >= 6
    print(f"EXACT rational root brackets: even={roots} retained_odd={odd_roots}; width<=1/100000")
    print(f"EXACT directed all-pairs witnesses: unordered_pairs={pairs} detailed_angles={detailed}; both paths checked")
    print(f"EXACT negative controls rejected={negatives}; integer interval scale=10^32 terms={TERMS}")
    print("PASS: bounded exact evidence only; all-m theorem and external review remain separate")


if __name__ == "__main__":
    main()
