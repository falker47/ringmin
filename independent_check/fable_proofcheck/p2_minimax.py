"""Supplement S1, L6 (finite minimax), L7 (width optimum, enclosure), L8 (limits)."""

from __future__ import annotations

import itertools
import math
import random
import re
from fractions import Fraction

from flint import arb

from p2_base import (BETA, C_TERM, D_closed, D_quadrature, MAIN, Order, Q_HI, ROOT, WIDTH_A, WIDTH_B,
                     ball, chain_sum, check, floor_q, hull, need, printed, supnick, supplement_text,
                     two_pi)

A_, B_ = WIDTH_A, WIDTH_B
D_SUM = A_ + B_
ELL = 16 + 432 * D_SUM


def D_values():
    values = [D_closed(beta) for beta in BETA]
    for value, beta in zip(values, BETA):
        need(value.overlaps(D_quadrature(beta)))          # two independent evaluations agree
    return values


def sq(x) -> arb:
    x = ball(x)
    return x * x          # arb ** int goes through exp/log and is NaN at an exact zero


def cube(x) -> arb:
    x = ball(x)
    return x * x * x


def F(h, D):
    return sum((D[i] * ball(h[i]) for i in range(3)), arb(0)) - 8 * sum((cube(x) for x in h), arb(0))


def script_L(h):
    return 16 + 432 * sum((ball(x) for x in h), arb(0))


def G(z, D):
    """G = N'L + 432N on the edge h = (a-z, z, b-z), from the definitions (not the expanded cubic)."""
    z = ball(z)
    h = (ball(A_) - z, z, ball(B_) - z)
    N = F(h, D)
    N_prime = -(D[0] - 24 * sq(h[0])) + (D[1] - 24 * sq(h[1])) - (D[2] - 24 * sq(h[2]))
    return N_prime * script_L(h) + 432 * N


def z_star(D, steps=200):
    lo, hi = Fraction(0), A_
    need(G(lo, D) > 0 and G(hi, D) < 0)
    for _ in range(steps):
        mid = (lo + hi) / 2
        value = G(mid, D)
        if value > 0:
            lo = mid
        elif value < 0:
            hi = mid
        else:
            break
    return lo, hi


def optimum():
    D = D_values()
    lo, hi = z_star(D)
    Z = hull(lo, hi)
    U = (ball(A_) - Z, Z, ball(B_) - Z)
    rho = F(U, D) / script_L(U)
    return D, (lo, hi), U, rho


@check("P2-L6a", "exact", "Proposition SM7.1: inf over e >= 0 of max{e, F/H - (L/H - 1)e} equals F_+/L when L > H > 0")
def scalar_minimax():
    rng = random.Random(6)
    for _ in range(400):
        H = Fraction(rng.randint(1, 500), 10**4)
        L = 8 * (54 * H + 2)
        need(L == 16 + 432 * H and L > H)
        Fn = Fraction(rng.randint(-300, 300), 10**5)
        target = max(Fn, Fraction(0)) / L

        def envelope(e):
            return max(e, Fn / H - (L / H - 1) * e)

        need(envelope(target) == target)                       # attained at e = F_+/L
        for _ in range(40):
            e = Fraction(rng.randint(0, 10**6), 10**7)
            need(envelope(e) >= target)
    return "400 random (H, F_n), 40 trial values of e each"


def gates(n, h):
    """The finite gates (SM7.1), exactly."""
    ells = [(beta * n).__floor__() for beta in BETA]
    return (n >= 102 and Fraction(ells[0], n) > Q_HI and ells[0] < ells[1] < ells[2] <= n - 2
            and h[0] + h[1] <= Fraction(ells[1] - ells[0], n) and h[1] + h[2] <= Fraction(ells[2] - ells[1], n))


@check("P2-L6b", "interval", "Proposition SM7.1: the whole chain of inequalities (SM7.2)-(SM7.3) on genuine orders, down to the chain roots")
def finite_proposition():
    D, (zlo, zhi), _, _ = optimum()
    z0 = (zlo + zhi) / 2
    rng = random.Random(8)
    count = 0
    slack = None
    for t, n in ((Fraction(1, 2), 222), (Fraction(1, 2), 301), (Fraction(9, 10), 1107)):
        need(n >= math.ceil(1 / ((1 - t) * A_)))
        h = tuple(t * x for x in (A_ - z0, z0, B_ - z0))
        need(gates(n, h))
        H = sum(h)
        Q3 = sum(x ** 3 for x in h)
        L = 16 + 432 * H
        k = floor_q(n)
        orders = [supnick(range(k, n + 1))]
        perturbed = orders[0][:]
        for _ in range(4):
            i, j = rng.sample(range(len(perturbed)), 2)
            perturbed[i], perturbed[j] = perturbed[j], perturbed[i]
        orders.append(perturbed)
        if n < 400:
            shuffled = list(range(k, n + 1))
            rng.shuffle(shuffled)
            orders.append(shuffled)
        for cycle in orders:
            o = Order(n, cycle)
            cuts = [o.cut(beta) for beta in BETA]
            E, e = ball(o.E), o.e
            W = [o.W0] + [c["W"] for c in cuts]
            # Lemma SM5.3 at each cutoff and Lemma SM6.1 with the common measure
            for c in cuts:
                need(abs(c["W"] - o.W0 - c["Dn"]) < 54 * E + 2 * ball(c["K"]))
            need(sum(hi * c["K"] for hi, c in zip(h, cuts)) <= 4 * Q3 + o.E)
            Fn = sum((ball(hi) * c["Dn"] for hi, c in zip(h, cuts)), arb(0)) - 8 * ball(Q3)
            weighted = sum((ball(hi) * c["W"] for hi, c in zip(h, cuts)), arb(0))
            need(weighted > ball(H) * (o.Jn + e) + Fn - ball(L) * e)
            Fn_plus = Fn.max(arb(0))
            best = W[0].max(W[1]).max(W[2]).max(W[3])
            need(best > o.Jn + Fn_plus / ball(L))
            # first inequality of (SM7.3), at the level of chain roots: some sigma_i has root >= rho
            first = (o.Jn + Fn_plus / ball(L)) / arb.pi() - ball(Fraction(1, n))
            rho = first * n * n
            need(rho > 0)
            cycles = [cycle] + [c["survivors"] for c in cuts]
            need(any(chain_sum(cyc, rho) > two_pi() for cyc in cycles))
            # second inequality of (SM7.3)
            eta = F(h, D).max(arb(0)) / (arb.pi() * ball(L))
            A_h = 1 + (5 + 19 * ball(H) / (2 * ball(L))) / arb.pi()
            need(first > C_TERM + eta - A_h / n)
            margin = float((first - (C_TERM + eta - A_h / n)).mid() * n)
            slack = margin if slack is None else min(slack, margin)
            count += 1
    return "%d orders at n=222, 301, 1107 with h = t u; least n*(lhs-rhs) of the last inequality = %.2f" % (count, slack)


@check("P2-L7a", "exact", "Section SM8: N(z), the expansion of G, G' = N''L and the cubic certificate (SM8.4) as polynomial identities")
def width_identities():
    rng = random.Random(7)

    def rnd():
        return Fraction(rng.randint(-40, 40), rng.randint(1, 9))

    for _ in range(300):
        D1, D2, D3, a, b, z = (rnd() for _ in range(6))
        d, ell = a + b, 16 + 432 * (a + b)
        c0 = a * D1 + b * D3 - 8 * (a ** 3 + b ** 3)
        c1 = D2 - D1 - D3 + 24 * (a * a + b * b)

        def Fq(h):
            return D1 * h[0] + D2 * h[1] + D3 * h[2] - 8 * sum(x ** 3 for x in h)

        N = c0 + c1 * z - 24 * d * z * z + 8 * z ** 3
        need(Fq((a - z, z, b - z)) == N)
        N1 = c1 - 48 * d * z + 24 * z * z
        N2 = -48 * d + 48 * z
        Lz = ell - 432 * z
        need(16 + 432 * ((a - z) + z + (b - z)) == Lz)
        Gz = N1 * Lz + 432 * N
        need(Gz == ell * c1 + 432 * c0 - 48 * ell * d * z + (24 * ell + 10368 * d) * z * z - 6912 * z ** 3)
        G1 = -48 * ell * d + 2 * (24 * ell + 10368 * d) * z - 3 * 6912 * z * z
        need(G1 == N2 * Lz == 48 * (z - d) * Lz)
        # N'(z) = -F_1 + F_2 - F_3 on the edge
        h = (a - z, z, b - z)
        need(N1 == -(D1 - 24 * h[0] ** 2) + (D2 - 24 * h[1] ** 2) - (D3 - 24 * h[2] ** 2))
    # cubic certificate: build a consistent KKT system and test (SM8.4) at arbitrary h
    for _ in range(300):
        u = [Fraction(rng.randint(1, 60), 97) for _ in range(3)]
        lam1, lam2 = Fraction(rng.randint(0, 50), 13), Fraction(rng.randint(0, 50), 17)
        g = (lam1, lam1 + lam2, lam2)
        rho = (sum(gi * ui for gi, ui in zip(g, u)) + 16 * sum(x ** 3 for x in u)) / 16
        D = [gi + 24 * ui * ui + 432 * rho for gi, ui in zip(g, u)]
        a, b = u[0] + u[1], u[1] + u[2]

        def Fq(h):
            return sum(Di * hi for Di, hi in zip(D, h)) - 8 * sum(x ** 3 for x in h)

        def Lq(h):
            return 16 + 432 * sum(h)

        need(Fq(u) - rho * Lq(u) == 0)
        h = [rnd() for _ in range(3)]
        rhs = lam1 * (h[0] + h[1] - a) + lam2 * (h[1] + h[2] - b) - 8 * sum((hi - ui) ** 2 * (hi + 2 * ui) for hi, ui in zip(h, u))
        need(Fq(h) - rho * Lq(h) == rhs)
        need(all(hi ** 3 - ui ** 3 - 3 * ui * ui * (hi - ui) == (hi - ui) ** 2 * (hi + 2 * ui) for hi, ui in zip(h, u)))
    need(A_ == Fraction(113, 12500) and B_ == Fraction(593, 50000) and A_ < D_SUM)
    need(ELL - 432 * A_ == 16 + 432 * B_ > 0)
    return "600 random rational instances"


def series_enclosure(beta, q_lo, q_hi):
    """Section SM9.2, transcribed: the binomial-series endpoints d_{i,-}, d_{i,+}."""
    s0 = 1 + q_lo
    v = (1 - q_lo) / s0
    w = (s0 - 2 * beta) / s0
    need(0 < w < v < 1)
    c = [None] + [Fraction(math.comb(2 * j, j), 4 ** j * (2 * j - 1)) for j in range(1, 82)]
    for j in range(1, 81):
        need(c[j + 1] / c[j] == Fraction(2 * j - 1, 2 * j + 2))
    P = v - w - sum(c[j] * (v ** (2 * j + 1) - w ** (2 * j + 1)) / (2 * j + 1) for j in range(1, 81))
    T = (v - w) * c[81] * v ** 162 / (1 - v * v)
    I_lo, I_hi = s0 * s0 / 4 * (P - T), s0 * s0 / 4 * P
    base = s0 * (beta - q_lo) - (beta * beta - q_lo * q_lo) / 2
    return base - 2 * I_hi - 4 * (q_hi - q_lo), base - 2 * I_lo + 4 * (q_hi - q_lo)


@check("P2-L7b", "interval", "Sections SM8-SM9: D_i, signs of G, z_*, multipliers, eta_width and the enclosure (SM1.4), all recomputed")
def width_optimum():
    text = supplement_text()
    D, (zlo, zhi), U, rho = optimum()
    # printed enclosures of D_i
    for i, value in enumerate(D, start=1):
        found = re.search(r"(0\.\d+)&<D_%d<(0\.\d+)" % i, text)
        need(found is not None)
        need(ball(Fraction(found.group(1))) < value and value < ball(Fraction(found.group(2))))
    # the paper's own series formulas, exactly as specified, enclose the same numbers
    q_lo, q_hi = printed("q_-"), printed("q_+")
    for beta, value in zip(BETA, D):
        d_lo, d_hi = series_enclosure(beta, q_lo, q_hi)
        need(d_lo < d_hi and ball(d_lo) < value and value < ball(d_hi))
        need(d_hi - d_lo < Fraction(1, 10**30))      # the 80-term tail bound T is about 1e-33
    # signs of G at 0, a, z_-, z_+
    z_minus, z_plus = printed("z_-"), printed("z_+")
    need(G(0, D) > 0 and G(A_, D) < 0 and G(z_minus, D) > 0 and G(z_plus, D) < 0)
    need(0 < z_minus < zlo < zhi < z_plus < A_)
    need(all(x > 0 for x in U))
    # multipliers and the KKT relation
    g = [D[i] - 24 * sq(U[i]) - 432 * rho for i in range(3)]
    need(F(U, D) > 0)
    need(g[0] > ball(Fraction(35, 10**5)) and g[2] > ball(Fraction(59, 10**5)))
    need((g[1] - g[0] - g[2]).overlaps(arb(0)) and (g[1] - g[0] - g[2]).rad() < arb(10) ** (-50))
    eta = rho / arb.pi()
    found = re.search(r"(0\.\d+)&<\\etaw<(0\.\d+)", text)
    need(ball(Fraction(found.group(1))) < eta and eta < ball(Fraction(found.group(2))))
    # the main enclosure (SM1.4), in the supplement and in the article
    bound = C_TERM + eta
    lo_s, hi_s = (Fraction(int(x), 10**23) for x in re.findall(r"\\frac\{(\d{23})\}\{10\^\{23\}\}", text)[:2])
    need(ball(lo_s) < bound and bound < ball(hi_s))
    main = MAIN.read_text(encoding="utf-8")
    block = main[main.index("\\label{prop:lower}"):main.index("\\label{prop:lower}") + 400]
    lo_m, hi_m = (Fraction("0" + x) for x in re.findall(r"(\.\d{23})", block)[:2])
    need((lo_m, hi_m) == (lo_s, hi_s))
    numbers = (ROOT / "paper_assets" / "journal_p2_sidma" / "numbers.tex").read_text(encoding="utf-8")
    c_lower = Fraction(re.search(r"\\CstarLower\}\{(0\.\d+)\}", numbers).group(1))
    need(c_lower <= lo_s and lo_s - c_lower < Fraction(1, 10**10) and ball(Fraction(1, 8)) < bound)
    return "C_term + eta_width = %s" % bound.str(30)


@check("P2-L7c", "interval", "Lemma SM8.1: u is the unique global maximizer of eta on the whole polyhedron (grid of P, faces and vertices)")
def global_maximum():
    D, _, U, rho = optimum()
    best = rho / arb.pi()
    count = 0
    steps = 14
    for i, j, l in itertools.product(range(steps + 1), repeat=3):
        h = (A_ * Fraction(i, steps), min(A_, B_) * Fraction(j, steps), B_ * Fraction(l, steps))
        if h[0] + h[1] > A_ or h[1] + h[2] > B_:
            continue
        value = F(h, D)
        need(value - rho * script_L(h) < 0)                         # (SM8.4), strictly, away from u
        need(value.max(arb(0)) / (arb.pi() * script_L(h)) < best)
        count += 1
    for j in range(steps + 1):                                       # the edge carrying the optimum
        z = A_ * Fraction(j, steps)
        h = (A_ - z, z, B_ - z)
        need(F(h, D).max(arb(0)) / (arb.pi() * script_L(h)) < best)
        count += 1
    for h in ((0, 0, 0), (A_, 0, B_), (0, A_, B_ - A_), (A_, 0, 0), (0, 0, B_)):   # vertices
        need(F(h, D).max(arb(0)) / (arb.pi() * script_L(h)) < best)
        count += 1
    return "%d points of P, none reaches eta(u)" % count


@check("P2-L8", "exact", "Section SM10: for h = t u the gates (SM7.1) hold for every n >= N(t) = ceil(1/((1-t)a)); they fail for h = u at n = 50000j+1")
def ordered_limit():
    need(BETA[0] - Q_HI > A_ and 1 / A_ > 102 and B_ > A_)          # the rational gates of Section SM10
    count = 0
    rng = random.Random(9)
    for t in (Fraction(1, 2), Fraction(9, 10), Fraction(99, 100), Fraction(999, 1000)):
        N = math.ceil(1 / ((1 - t) * A_))
        need(N >= 102 and N * (BETA[0] - Q_HI) > 1 and N * (1 - t) * A_ >= 1)
        sample = list(range(N, N + 4000)) + [rng.randint(N, 10**7) for _ in range(4000)]
        for n in sample:
            ells = [(beta * n).__floor__() for beta in BETA]
            need(n >= 102 and Fraction(ells[0], n) > Q_HI and ells[0] < ells[1] < ells[2] <= n - 2)
            # h_1+h_2 = t a and h_2+h_3 = t b whatever z_* is
            need(Fraction(ells[1] - ells[0], n) >= t * A_ and Fraction(ells[2] - ells[1], n) >= t * B_, "t=%s n=%d" % (t, n))
            count += 1
    for j in range(1, 200):
        n = 50000 * j + 1
        ells = [(beta * n).__floor__() for beta in BETA]
        need(ells == [10455 * j, 10907 * j, 11500 * j])
        need(Fraction(ells[1] - ells[0], n) == A_ * Fraction(n - 1, n) < A_)
        need(Fraction(ells[2] - ells[1], n) == B_ * Fraction(n - 1, n) < B_)
    return "%d sizes satisfy the gates; the unshrunk optimum fails at n = 50000j+1, j < 200" % count


def span(order) -> arb:
    """Least span of a fixed left-to-right order of marks: x_i = max_{j<i} (x_j + sqrt(w_i w_j))."""
    xs = []
    for i, w in enumerate(order):
        x = arb(0)
        for j in range(i):
            x = x.max(xs[j] + (ball(w) * ball(order[j])).sqrt())
        xs.append(x)
    return xs[-1] if xs else arb(0)


def line_optimum(n) -> arb:
    marks = [Fraction(i, n) for i in range(1, n + 1)]
    best = None
    for perm in itertools.permutations(marks):
        if perm[0] > perm[-1]:
            continue                                   # reversal gives the same span
        value = span(perm)
        best = value if best is None else best.min(value)
    return best


@check("P2-L8b", "interval", "Section SM11: squeeze (SM11.3), concatenation bound of Lemma SM11.1, and (b_n+1)/n >= pi(C_term+eta_width), by brute force")
def limit_existence():
    _, _, _, rho = optimum()
    floor_value = arb.pi() * (C_TERM + rho / arb.pi())     # E_inf = pi C_* >= this
    b = {1: arb(0)}
    for n in range(2, 8):
        b[n] = line_optimum(n)
        need(not ((b[n] + 1) / n < floor_value))           # would contradict Theorem SM1.1
        need((b[n] + 1) / n > floor_value)
    for n in range(2, 8):
        for N in range(n, 8):
            k = -(-N // n)
            bound = ball(Fraction(n * k, N)) * (k * (b[n] + 1) - 1)
            need(not (b[N] > bound), "concatenation bound fails at n=%d N=%d" % (n, N))
    # squeeze against the chain root of the Supnick necklace, which is Rstar(n) for n <= 7 (Paper I)
    for n in range(3, 8):
        cycle = supnick(range(1, n + 1))
        low = (b[n] / (arb.pi() * n) - ball(Fraction(1, n))) * n * n
        high = (b[n] + 1) / (arb.pi() * n) * n * n
        if low > 0:
            need(not (chain_sum(cycle, low) < two_pi()))   # Rstar(n) >= low
        need(chain_sum(cycle, high) < two_pi())            # chain root < high (and Rstar = chain root here)
    # heuristic orders for larger n: any feasible order gives (span+1)/n >= inf = E_inf
    worst = None
    for n in (20, 60, 150):
        marks = [Fraction(i, n) for i in range(1, n + 1)]
        ordered = supnick(marks)
        cut = ordered.index(max(marks))
        candidates = [ordered[cut:] + ordered[:cut], ordered, marks[0::2] + marks[1::2][::-1]]
        for cand in candidates:
            ratio = (span(cand) + 1) / n
            need(ratio > floor_value)
            worst = ratio if worst is None else worst.min(ratio)
    return "b_2..b_7 exact by enumeration; least heuristic (span+1)/n = %.5f > pi(C_term+eta) = %.5f" % (
        float(worst.mid()), float(floor_value.mid()))
