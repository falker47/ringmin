"""Replay Figure 2 from exact endpoints and witness orders.

At the lower endpoint each rounded-down angle and rounded-up circumference
relaxes the true constraints. The Held–Karp recurrence bounds the remaining
adjacent cost of every completion of a prefix. If even that relaxation fails,
every completion fails. From each surviving top-radius cycle, insert each
omitted label in every slot after the anchor. Deletion preserves both arc
constraints, so a failed partial cycle cannot have a feasible extension.
The anchor fixes rotation. Choosing the smaller neighbor first fixes reflection
on the initial subset and selects one representative of every full dihedral
class. The final test uses both arc directions for all pairs.

At the upper endpoint the opposite rounding directions give a construction:
feasible difference constraints supply positions on the shorter circle,
whose closing gap can be enlarged to yield the true circumference. Arb then
checks squared Euclidean distances between independently reconstructed centers.
"""

from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
import re

from flint import arb, ctx, fmpq


# Every angle and arc is in integer 10^-32 radian units. All divisions round
# outwards. No floating-point value enters a feasibility decision.
SCALE = 10**32


def ceildiv(a, b):
    return -((-a) // b)


def scaled_root(x):
    lo = isqrt((x.numerator * SCALE**2) // x.denominator)
    return lo, lo + 1


def atan_ticks(x):
    """Enclose SCALE * atan(x / SCALE), for an integer 0 <= x < SCALE."""
    if not 0 <= x < SCALE:
        raise ValueError("atan argument outside Taylor interval")
    pl = ph = x
    lo = hi = 0
    i = 0
    while True:
        denominator = 2 * i + 1
        a = pl // denominator
        b = ceildiv(ph, denominator)
        if b <= 1:
            # Alternating-series remainder has the sign of the next term.
            return (lo, hi + b) if i % 2 == 0 else (lo - b, hi)
        if i % 2 == 0:
            lo, hi = lo + a, hi + b
        else:
            lo, hi = lo - b, hi - a
        pl = pl * x * x // SCALE**2
        ph = ceildiv(ph * x * x, SCALE**2)
        i += 1


def tau_ticks():
    # Machin identity: pi/4 = 4 atan(1/5) - atan(1/239).
    al, ah = atan_ticks(SCALE // 5)
    bl = atan_ticks(SCALE // 239)[0]
    bh = atan_ticks(ceildiv(SCALE, 239))[1]
    return 32 * al - 8 * bh, 32 * ah - 8 * bl


def angle_table(n, radius, upper):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in range(1, u):
            # Twice the half-angle identity applied to the manuscript's atan
            # form gives theta=4 atan(sqrt(uv)/(sqrt((R+u)(R+v))+
            # sqrt(R(R+u+v)))).
            a, b = scaled_root(Fraction(u * v))
            c, d = scaled_root((radius + u) * (radius + v))
            e, f = scaled_root(radius * (radius + u + v))
            if upper:
                arg = ceildiv(b * SCALE, c + e)
                value = 4 * atan_ticks(arg)[1]
            else:
                arg = a * SCALE // (d + f)
                value = 4 * atan_ticks(arg)[0]
            table[u][v] = table[v][u] = value
    return table


def positions(order, angle, period, padding=0):
    """Exact positive-cycle test for x[j]>=x[i]+theta_ij-period*[i>j]."""
    count = len(order)
    position = [0] * count
    for _ in range(count):
        changed = False
        for i, u in enumerate(order):
            for j, v in enumerate(order):
                if i == j:
                    continue
                needed = position[i] + angle[u][v] + padding - (period if j < i else 0)
                if position[j] < needed:
                    position[j] = needed
                    changed = True
        # With a zero-valued source to all vertices, an optimal simple path
        # uses at most count-1 edges. An update on pass count implies a
        # positive cycle, hence an inconsistent constraint system.
        if not changed:
            return position
    return None


def no_lower_order(n, angle, period):
    # Rotations have unique representative beginning with n. First enumerate
    # cyclic orders of the top radii. A complete feasible order keeps its
    # orientation and all cyclic-arc inequalities after deletions.
    anchor = n

    @lru_cache(None)
    def tail(last, mask):
        if not mask:
            return angle[last][anchor]
        remaining = mask
        optimum = None
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length()
            value = angle[last][v] + tail(v, mask ^ bit)
            optimum = value if optimum is None else min(optimum, value)
            remaining ^= bit
        return optimum

    # Select the top subset with largest minimum angular tour length. Each
    # subset is a valid necessary test; this choice only affects runtime.
    def labels(start):
        return ((1 << (n - 1)) - 1) ^ ((1 << (start - 1)) - 1)

    start = max(range(1, n - 1), key=lambda a: tail(n, labels(a)))
    mask = labels(start)

    def insert(order, v):
        if positions(order, angle, period) is None:
            return False
        if not v:
            return True
        for j in range(1, len(order) + 1):
            if insert(order[:j] + (v,) + order[j:], v - 1):
                return True
        return False

    def visit(order, mask, used):
        last = order[-1]
        if used + tail(last, mask) > period:
            return False
        if not mask:
            return order[1] < order[-1] and insert(order, start - 1)
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length()
            if visit(order + (v,), mask ^ bit, used + angle[last][v]):
                return True
            remaining ^= bit
        return False

    try:
        return not visit((n,), mask, 0)
    finally:
        tail.cache_clear()


def cartesian_disjoint(order, coordinates, radius):
    """Check actual center distances without using the pair angle formula."""
    with ctx.workprec(256):
        central = arb(fmpq(radius.numerator, radius.denominator))
        centers = []
        for u, position in zip(order, coordinates, strict=True):
            sine, cosine = arb(fmpq(position, SCALE)).sin_cos()
            centers.append(((central + u) * cosine, (central + u) * sine))
        for i, (x, y) in enumerate(centers):
            for j in range(i):
                dx, dy = x - centers[j][0], y - centers[j][1]
                if not dx * dx + dy * dy >= (order[i] + order[j]) ** 2:
                    return False
    return True


def run(root):
    table = root / "paper_assets/journal_p2_v4/figures/bracket_rows.tex"
    source = (
        root
        / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
    )
    rows = re.findall(
        r"^(\d+)\s*&\s*(\d+\.\d+)\s*&\s*(\d+\.\d+)\s*&\s*(\d+)",
        table.read_text(encoding="utf-8"),
        re.M,
    )
    cases = json.loads(source.read_text(encoding="utf-8"))["certificate"]["cases"]
    expected = list(range(3, 15))
    if [int(row[0]) for row in rows] != expected or [
        case["n"] for case in cases
    ] != expected:
        raise ValueError("Figure 2 row coverage")
    tau_low, tau_high = tau_ticks()
    for (ns, lower, upper, count), case in zip(rows, cases, strict=True):
        n = int(ns)
        lo, hi = Fraction(lower), Fraction(upper)
        yield (
            f"Figure 2 n={n} endpoints and normalized width",
            (
                lo == Fraction(case["L"])
                and hi == Fraction(case["U"])
                and (hi - lo) / n**2 == Fraction(1, 10**11 * n**2)
            ),
        )
        low_angles = angle_table(n, lo, False)
        yield (
            f"Figure 2 n={n} global lower (all cyclic orders)",
            no_lower_order(n, low_angles, tau_high),
        )
        upper_angles = angle_table(n, hi, True)
        orders = [tuple(row["order"]) for row in case["upper_witnesses"]]
        canonical = {min(order[1:], order[:0:-1]) for order in orders}
        valid = len(canonical) == len(orders) == int(count) > 0 and all(
            len(order) == n and order[0] == n and sorted(order) == list(range(1, n + 1))
            for order in orders
        )
        # 10^-26 radians per constraint buys strict slack for the separate
        # Cartesian interval check. It only tightens the upper construction.
        placements = (
            [positions(order, upper_angles, tau_low, 10**6) for order in orders]
            if valid
            else []
        )
        angular = valid and all(p is not None for p in placements)
        yield f"Figure 2 n={n} {count} feasible upper witnesses (angles)", angular
        yield (
            f"Figure 2 n={n} {count} upper witnesses (Cartesian)",
            (
                angular
                and all(
                    cartesian_disjoint(order, p, hi)
                    for order, p in zip(orders, placements, strict=True)
                )
            ),
        )
