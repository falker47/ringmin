"""Supplement S1, L3 (dual and energy), L4 (signed deletion, floors), L5 (crossings)."""

from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction

from flint import arb

from p2_base import (BETA, C_TERM, D_closed, Order, Q_HI, ball, check, floor_q, need, supnick)

SIZES = (102, 103, 131, 200, 257)


def test_orders(n: int, rng: random.Random):
    """Named cyclic orders of k..n spanning the small- and large-energy regimes."""
    k = floor_q(n)
    labels = list(range(k, n + 1))
    best = supnick(labels)
    yield "supnick", best
    yield "sorted", labels                      # one maximal run of deleted labels
    yield "pyramid", labels[0::2] + labels[1::2][::-1]
    shuffled = labels[:]
    rng.shuffle(shuffled)
    yield "random", shuffled
    for swaps in (1, 3, 10):                    # near-optimal orders with a few defects
        perturbed = best[:]
        for _ in range(swaps):
            i, j = rng.sample(range(len(perturbed)), 2)
            perturbed[i], perturbed[j] = perturbed[j], perturbed[i]
        yield "supnick+%dswaps" % swaps, perturbed
    # small labels packed together next to large ones: many deleted-deleted edges
    half = len(labels) // 2
    yield "blocks", labels[:half][::-1] + labels[half:]


def cutoffs(n: int):
    """Admissible cutoffs: beta in (q, 23/100], l/n > q, l <= n-2."""
    out = []
    for beta in BETA + (Fraction(196, 1000), Fraction(1, 5), Fraction(22, 100), Fraction(2255, 10000)):
        ell = (beta * n).__floor__()
        if beta > Q_HI and Fraction(ell, n) > Q_HI and ell <= n - 2:
            out.append(beta)
    return out


def psi(x, s) -> arb:
    """psi(x) = c/2 + (1/2) int_c^x sqrt((s-t)/t) dt with c = s/2, via the primitive
    G(t) = sqrt(t(s-t)) + s arcsin sqrt(t/s) (verified symbolically in P2-L3a)."""
    x, s = ball(x), ball(s)

    def G(t):
        return (t * (s - t)).sqrt() + s * (t / s).sqrt().asin()

    c = s / 2
    return c / 2 + (G(x) - G(c)) / 2


@check("P2-L3a", "interval", "Lemma SM4.1 (SM4.2): d^2/8 <= f - psi(x) - psi(y) <= d^2/(8 alpha) on [alpha,1]^2")
def dual_inequality():
    import sympy as sp

    t, s_, x_, y_ = sp.symbols("t s x y", positive=True)
    G = sp.sqrt(t * (s_ - t)) + s_ * sp.asin(sp.sqrt(t / s_))
    need(sp.simplify(sp.diff(G, t) ** 2 - (s_ - t) / t) == 0)        # G' = +sqrt((s-t)/t)
    need(bool(sp.diff(G, t).subs({t: sp.Rational(1, 3), s_: sp.Rational(7, 6)}) > 0))
    # d/dy [sqrt(xy) - psi(y)] = (x+y-s)/(2 sqrt(y)(sqrt(x)+sqrt(s-y)))
    lhs = sp.sqrt(x_ / y_) / 2 - sp.sqrt((s_ - y_) / y_) / 2
    rhs = (x_ + y_ - s_) / (2 * sp.sqrt(y_) * (sp.sqrt(x_) + sp.sqrt(s_ - y_)))
    need(sp.simplify(lhs - rhs) == 0)
    count = 0
    for alpha in (Fraction(1, 6) + Fraction(1, 10**6), Fraction(19, 102), Fraction(39, 200), Fraction(1, 5), Fraction(1, 20), Fraction(2, 3)):
        s = 1 + alpha
        grid = [alpha + (1 - alpha) * Fraction(i, 24) for i in range(25)]
        table = {x: psi(x, s) for x in grid}
        for x in grid:
            # H(x, s-x) = 0: the assignment identity
            zero = (ball(x) * ball(s - x)).sqrt() - table[x] - psi(s - x, s)
            need(zero.overlaps(arb(0)) and zero.rad() < arb(10) ** (-60))
            for y in grid:
                H = (ball(x) * ball(y)).sqrt() - table[x] - table[y]
                d2 = (x + y - s) ** 2
                if d2 == 0:
                    need(H.overlaps(arb(0)))
                else:
                    need(H > ball(d2 / 8) and H < ball(d2 / (8 * alpha)), "alpha=%s x=%s y=%s" % (alpha, x, y))
                count += 1
    return "%d grid pairs, strict on both sides away from x+y=s" % count


@check("P2-L3b", "interval", "(SM4.3)-(SM4.5): e >= E/8 >= 0, marginals of mu, assignment identity, on genuine cyclic orders")
def energy():
    rng = random.Random(3)
    count = 0
    least = None
    for n in SIZES:
        for name, cycle in test_orders(n, rng):
            o = Order(n, cycle)
            need(Fraction(1, 6) < o.alpha <= Q_HI and o.alpha < Fraction(1, 5))
            V = [Fraction(j, n) for j in range(o.k, n + 1)]
            need(sorted(o.s - x for x in V) == V)                      # reflection permutes V
            first, second, energy_ = {}, {}, Fraction(0)
            mass = Fraction(1, 2 * n)
            for u, v in o.edges:
                for a, b in ((u, v), (v, u)):
                    x, z = Fraction(a, n), o.s - Fraction(b, n)
                    first[x] = first.get(x, 0) + mass
                    second[z] = second.get(z, 0) + mass
                    energy_ += mass * (x - z) ** 2
            need(first == second == {x: Fraction(1, n) for x in V})    # both marginals are nu
            need(energy_ == o.E and sum(first.values()) == Fraction(n - o.k + 1, n))
            need(8 * o.e > ball(o.E), "%s n=%d" % (name, n))
            twice_psi = 2 * sum((psi(x, o.s) for x in V), arb(0)) / n
            need((twice_psi - o.Jn).overlaps(arb(0)) and (twice_psi - o.Jn).rad() < arb(10) ** (-55))
            ratio = float((8 * o.e / ball(o.E)).mid())                 # display only
            least = ratio if least is None else min(least, ratio)
            count += 1
    return "%d orders; smallest observed 8e/E = %.3f (must exceed 1)" % (count, least)


@check("P2-L4a", "exact", "Lemma SM5.1: nu{|x-B| <= h} <= 4h for every h > 0 (with equality at h = 1/(2n))")
def strip_mass():
    count = 0
    equality = False
    for n in (102, 103, 150):
        k = floor_q(n)
        for ell in (k + 1, k + 2, (BETA[0] * n).__floor__(), (BETA[2] * n).__floor__(), n - 2):
            B = Fraction(2 * ell - 1, 2 * n)
            hs = [Fraction(m, 4 * n) for m in range(1, 8 * n, 3)] + [Fraction(2 * m + 1, 2 * n) for m in range(0, 40)]
            hs += [Fraction(2 * m + 1, 2 * n) - Fraction(1, 10**9) for m in range(0, 40)]
            for h in hs:
                inside = sum(1 for j in range(k, n + 1) if abs(Fraction(j, n) - B) <= h)
                need(Fraction(inside, n) <= 4 * h, "n=%d l=%d h=%s" % (n, ell, h))
                equality = equality or Fraction(inside, n) == 4 * h
                count += 1
    need(equality)
    return "%d (n, l, h) triples; the constant 4 is attained" % count


@check("P2-L4b", "symbolic", "Lemmas SM5.2-SM5.3: Hessian of g and p'(x) as printed; the constants 4, 2, 6, 3 and 54/5 < 11")
def variation_constants():
    import sympy as sp

    x, y, z, s = sp.symbols("x y z s", positive=True)
    g = sp.sqrt(y * z) - sp.sqrt(x * y) - sp.sqrt(x * z)
    need(sp.simplify(sp.diff(g, y, 2) - (sp.sqrt(x) - sp.sqrt(z)) / (4 * y ** sp.Rational(3, 2))) == 0)
    need(sp.simplify(sp.diff(g, z, 2) - (sp.sqrt(x) - sp.sqrt(y)) / (4 * z ** sp.Rational(3, 2))) == 0)
    need(sp.simplify(sp.diff(g, y, z) - 1 / (4 * sp.sqrt(y * z))) == 0)
    w = sp.symbols("w", positive=True)                                           # w = s - x > 0
    need(sp.simplify(g.subs({y: w, z: w}) - (w - 2 * sp.sqrt(x * w))) == 0)       # equals D_alpha(x)
    need(sp.simplify(sp.diff(g, y).subs({y: w, z: w}) - (1 - sp.sqrt(x / w)) / 2) == 0)   # equals p(x)
    need(sp.simplify(sp.diff(g, z).subs({y: w, z: w}) - (1 - sp.sqrt(x / w)) / 2) == 0)
    p = (1 - sp.sqrt(x / (s - x))) / 2
    claimed = -s / (4 * sp.sqrt(x) * (s - x) ** sp.Rational(3, 2))
    need(sp.simplify((sp.diff(p, x) - claimed).subs(s, x + w)) == 0)
    # exact constants, for alpha > 1/6 and s = 1+alpha < 6/5
    alpha = Fraction(1, 6)
    need(Fraction(1, 16) / alpha ** 3 == Fraction(27, 2) and Fraction(27, 2) < 16)  # (1/(4 a^{3/2}))^2 <= (3 sqrt6/2)^2 < 4^2
    need(1 / (4 * alpha) == Fraction(3, 2) and Fraction(3, 2) < 2)
    need(Fraction(6, 5) / (4 * alpha ** 2) == Fraction(54, 5) and Fraction(54, 5) < 11)
    need(Fraction(7, 6) - Fraction(46, 100) == Fraction(53, 75) and Fraction(53, 75) > Fraction(1, 2))
    # Arb sweep of the actual ranges at genuine grids
    worst = [arb(0), arb(0), arb(0)]
    for n in (102, 150, 400):
        a = Fraction(floor_q(n), n)
        s_ = 1 + a
        grid = [a + (1 - a) * Fraction(i, 12) for i in range(13)]
        for xx, yy, zz in itertools.product(grid, repeat=3):
            gyy = abs(ball(xx).sqrt() - ball(zz).sqrt()) / (4 * (ball(yy) ** 3).sqrt())
            gyz = 1 / (4 * (ball(yy) * ball(zz)).sqrt())
            need(gyy < 4 and gyz < 2)
            worst[0], worst[1] = worst[0].max(gyy), worst[1].max(gyz)
        for xx in grid:
            dp = ball(s_) / (4 * ball(xx).sqrt() * (ball(s_ - xx) ** 3).sqrt())
            need(dp < ball(Fraction(54, 5)))
            need(abs((1 - (ball(xx) / ball(s_ - xx)).sqrt()) / 2) < 1)
            worst[2] = worst[2].max(dp)
    return "sympy identities hold; sampled maxima |g_yy|=%.3f, |g_yz|=%.3f, |p'|=%.3f" % tuple(float(w.mid()) for w in worst)


def float_ratios(n, k, cycle, beta):
    """Float evaluation used ONLY to steer the adversarial search below."""
    s = 1 + k / n
    ell = math.floor(beta * n)
    B = (ell - 0.5) / n
    m = len(cycle)

    def f(u, v):
        return math.sqrt(u * v) / n

    W0 = sum(f(cycle[i], cycle[(i + 1) % m]) for i in range(m)) / n
    surv = [v for v in cycle if v >= ell]
    W = sum(f(surv[i], surv[(i + 1) % len(surv)]) for i in range(len(surv))) / n
    Dn = sum(s - j / n - 2 * math.sqrt(j / n * (s - j / n)) for j in range(k, ell)) / n
    E = sum((cycle[i] / n + cycle[(i + 1) % m] / n - s) ** 2 for i in range(m)) / n
    Lam = K = 0.0
    for i in range(m):
        u, left, right = cycle[i], cycle[i - 1], cycle[(i + 1) % m]
        x = u / n
        if u < ell:
            Lam += (1 - math.sqrt(x / (s - x))) / 2 * ((x + left / n - s) + (x + right / n - s)) / n
        for nb in (left, right):
            zz = s - nb / n
            if (x - B) * (zz - B) < 0:
                K += abs(x - zz) / (2 * n)
    Delta = W - W0 - Dn
    return abs(Delta - Lam) / (43 * E), abs(Lam) / (11 * E + 2 * K), abs(Delta) / (54 * E + 2 * K)


def adversarial(n, beta, which, rng, steps=1500):
    k = floor_q(n)
    cycle = supnick(range(k, n + 1))
    best = float_ratios(n, k, cycle, beta)[which]
    for _ in range(steps):
        i, j = rng.sample(range(len(cycle)), 2)
        cycle[i], cycle[j] = cycle[j], cycle[i]
        value = float_ratios(n, k, cycle, beta)[which]
        if value >= best:
            best = value
        else:
            cycle[i], cycle[j] = cycle[j], cycle[i]
    return cycle


@check("P2-L4c", "interval", "Lemmas SM5.2-SM5.3: |Delta-Lambda| <= 43E, |Lambda| <= 11E+2K, |Delta| <= 54E+2K (structured, random and adversarial orders)")
def signed_deletion():
    rng = random.Random(4)
    worst = [0.0, 0.0, 0.0]
    count = 0

    def audit(n, cycle, beta):
        nonlocal count
        o = Order(n, cycle)
        c = o.cut(beta)
        E, K = ball(o.E), ball(c["K"])
        gap = abs(c["Delta"] - c["Lambda"])
        need(gap < 43 * E, "43E fails at n=%d beta=%s" % (n, beta))
        need(abs(c["Lambda"]) < 11 * E + 2 * K, "11E+2K fails at n=%d beta=%s" % (n, beta))
        need(abs(c["Delta"]) < 54 * E + 2 * K, "54E+2K fails at n=%d beta=%s" % (n, beta))
        for slot, value in enumerate((gap / (43 * E), abs(c["Lambda"]) / (11 * E + 2 * K), abs(c["Delta"]) / (54 * E + 2 * K))):
            worst[slot] = max(worst[slot], float(value.mid()))     # display only
        count += 1

    for n in SIZES:
        for _name, cycle in test_orders(n, rng):
            for beta in cutoffs(n):
                audit(n, cycle, beta)
    for n in (102, 131):
        for beta in (BETA[0], BETA[2]):
            for which in range(3):
                audit(n, adversarial(n, beta, which, rng), beta)
    return ("%d (order, cutoff) cases; largest observed ratios to the bounds: %.3f, %.3f, %.3f (each must stay below 1)"
            % (count, worst[0], worst[1], worst[2]))


@check("P2-L4d", "interval", "Lemma SM5.4: |J_n - pi C_term| <= 5/n and |D_n - D(beta)| <= 19/(2n)")
def floors():
    target = C_TERM * arb.pi()
    worst_J = worst_D = 0.0
    count = 0
    sizes = list(range(102, 330)) + list(range(331, 3000, 97)) + [10007, 50001]
    reference = {beta: D_closed(beta) for beta in BETA + (Fraction(196, 1000), Fraction(1, 5), Fraction(22, 100), Fraction(2255, 10000))}
    for n in sizes:
        k = floor_q(n)
        s = 1 + Fraction(k, n)
        roots = {j: (ball(Fraction(j, n)) * ball(s - Fraction(j, n))).sqrt() for j in range(k, n + 1)}
        Jn = sum(roots.values(), arb(0)) / n
        need(abs(Jn - target) < ball(Fraction(5, n)))
        worst_J = max(worst_J, float((abs(Jn - target) * n).mid()))
        for beta in cutoffs(n):
            ell = (beta * n).__floor__()
            Dn = sum((ball(s - Fraction(j, n)) - 2 * roots[j] for j in range(k, ell)), arb(0)) / n
            need(abs(Dn - reference[beta]) < ball(Fraction(19, 2 * n)), "n=%d beta=%s" % (n, beta))
            worst_D = max(worst_D, float((abs(Dn - reference[beta]) * n).mid()))
            count += 1
    return "%d sizes, %d cutoffs; observed n|J_n-J| <= %.3f (bound 5), n|D_n-D| <= %.3f (bound 9.5)" % (len(sizes), count, worst_J, worst_D)


def crossing_sides(mu, Bs, hs):
    """Exact evaluation of both sides of (SM6.1) for a finite measure mu = [(x, z, mass)]."""
    energy_ = sum(m * (x - z) ** 2 for x, z, m in mu)
    left = Fraction(0)
    for B, h in zip(Bs, hs):
        left += h * sum(m * abs(x - z) for x, z, m in mu if (x - B) * (z - B) < 0)
    return left, 4 * sum(h ** 3 for h in hs) + energy_


@check("P2-L5", "exact", "Lemma SM6.1: sum h_i K_i <= 4 sum h_i^3 + E under adjacent separation h_i+h_{i+1} <= B_{i+1}-B_i")
def crossing_budget():
    rng = random.Random(5)
    count = 0
    tightest = None
    for trial in range(400):
        n = rng.choice((102, 131, 180))
        k = floor_q(n)
        V = [Fraction(j, n) for j in range(k, n + 1)]
        s = 1 + Fraction(k, n)
        kind = trial % 3
        if kind == 0:      # the measure (SM4.4) of a genuine cyclic order
            labels = supnick(range(k, n + 1)) if trial % 2 else rng.sample(range(k, n + 1), n - k + 1)
            mu = []
            for i, u in enumerate(labels):
                for v in (labels[i - 1], labels[(i + 1) % len(labels)]):
                    mu.append((Fraction(u, n), s - Fraction(v, n), Fraction(1, 2 * n)))
        elif kind == 1:    # an arbitrary coupling with first marginal nu
            image = V[:]
            rng.shuffle(image)
            mu = [(x, z, Fraction(1, n)) for x, z in zip(V, image)]
        else:              # second coordinate off the grid, first marginal still nu
            mu = [(x, Fraction(rng.randint(0, 1000), 997), Fraction(1, n)) for x in V]
        m = rng.randint(1, 5)
        cuts = sorted(rng.sample(range(k + 1, n - 1), m))
        Bs = [Fraction(2 * c - 1, 2 * n) for c in cuts]
        hs = []
        for i in range(m):
            room = Fraction(1, 2)
            if i > 0:
                room = min(room, Bs[i] - Bs[i - 1])
            if i < m - 1:
                room = min(room, Bs[i + 1] - Bs[i])
            hs.append(room / 2 if rng.random() < 0.5 else room * Fraction(rng.randint(1, 500), 1000))
        for i in range(m - 1):
            need(hs[i] + hs[i + 1] <= Bs[i + 1] - Bs[i])
        for B, h in zip(Bs, hs):       # hypothesis of the lemma (Lemma SM5.1 supplies it on the grid)
            need(sum(mass for x, _, mass in mu if abs(x - B) <= h) <= 4 * h)
        left, right = crossing_sides(mu, Bs, hs)
        need(left <= right, "trial %d" % trial)
        slack = float(left / right) if right else 0.0
        tightest = slack if tightest is None else max(tightest, slack)
        count += 1
    return "%d exact rational instances; largest lhs/rhs = %.3f" % (count, tightest)
