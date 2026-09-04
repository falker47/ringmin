"""Bounded independent numerical falsification checks, never proof premises.

No production or standalone-verifier imports. Direct mpmath angular and
Cartesian audits are checked against a separate scipy all-pairs LP near
the finite cell root for the smallest cycles. Deterministic; no RNG.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np
from scipy.optimize import linprog


def order(m, s):
    if not isinstance(m, int) or not isinstance(s, int) or m < 2 or not 0 <= s < m:
        raise ValueError("require integer m>=2 and 0<=s<m")
    return tuple(r for i in range(1, m+1) for r in (i, m+1+(i+s-1) % m))


def angle(R, a, b):
    return 2 * mp.asin(mp.sqrt(mp.mpf(a*b)/((R+a)*(R+b))))


def cells(m, s, R):
    radii = order(m, s)
    gaps = [angle(R, radii[i], radii[(i+1) % (2*m)]) for i in range(2*m)]
    chain = mp.fsum(gaps)
    for i in range(m):
        before = (2*i-1) % (2*m)
        chord = angle(R, radii[before], radii[2*i+1])
        gaps[2*i] += max(mp.mpf(0), chord-gaps[before]-gaps[2*i])
    return chain, mp.fsum(gaps), gaps


def roots(m, s):
    values = []
    for index in (0, 1):
        lo, hi = mp.mpf("1e-12"), mp.mpf(16*m*m)
        assert cells(m, s, lo)[index] > 2*mp.pi > cells(m, s, hi)[index]
        for _ in range(160):
            mid = (lo+hi)/2
            if cells(m, s, mid)[index] > 2*mp.pi:
                lo = mid
            else:
                hi = mid
        values.append(hi)
    assert values[0] <= values[1] + mp.mpf("1e-45")
    return values


def audit(m, s, R, rotation=0, reflected=False):
    radii = order(m, s)
    _, total, gaps = cells(m, s, R)
    assert total <= 2*mp.pi
    gaps[-1] += 2*mp.pi-total
    if reflected:
        indices = [(-i) % len(radii) for i in range(len(radii))]
        gaps = [gaps[(i-1) % len(radii)] for i in indices]
        radii = tuple(radii[i] for i in indices)
    radii = radii[rotation:] + radii[:rotation]
    gaps = gaps[rotation:] + gaps[:rotation]
    assert abs(mp.fsum(gaps)-2*mp.pi) < mp.mpf("1e-60")
    positions = [mp.mpf(0)]
    for gap in gaps[:-1]:
        positions.append(positions[-1]+gap)
    cart = [((R+r)*mp.cos(t), (R+r)*mp.sin(t)) for r, t in zip(radii, positions)]
    min_angle, min_cart = mp.inf, mp.inf
    counts = {"HH": 0, "LH": 0, "LL": 0}
    for i in range(len(radii)):
        for j in range(i+1, len(radii)):
            a, b = radii[i], radii[j]
            arc = positions[j]-positions[i]
            requirement = angle(R, a, b)
            min_angle = min(min_angle, arc-requirement, 2*mp.pi-arc-requirement)
            dx, dy = cart[i][0]-cart[j][0], cart[i][1]-cart[j][1]
            min_cart = min(min_cart, (dx*dx+dy*dy-(a+b)**2)/((R+a)*(R+b)))
            counts["HH" if min(a,b)>m else "LL" if max(a,b)<=m else "LH"] += 2
    assert all(counts.values())
    assert min_angle > -mp.mpf("1e-55"), (m, s, min_angle)
    assert min_cart > -mp.mpf("1e-55"), (m, s, min_cart)
    return min_angle, min_cart, sum(counts.values())


def lp_feasible(radii, R):
    n = len(radii)
    rows, bounds = [], []
    for i in range(n):
        for j in range(i+1, n):
            theta = float(angle(mp.mpf(R), radii[i], radii[j]))
            row = np.zeros(n)
            row[j], row[i] = 1, -1
            rows.extend((row, -row))
            bounds.extend((2*np.pi-theta, -theta))
    result = linprog(np.zeros(n), A_ub=rows, b_ub=bounds,
                     bounds=[(0, 0)]+[(None, None)]*(n-1), method="highs",
                     options={"primal_feasibility_tolerance": 1e-9,
                              "dual_feasibility_tolerance": 1e-9})
    assert result.status in (0, 2), result.message
    return result.status == 0


def continuum():
    d = mp.log(3)/8-mp.mpf(1)/12

    def F(c, t):
        if c == 0:
            return t*t/2
        q = mp.sqrt(t*(t+c))
        return (2*t+c)*q/4-c*c*mp.log((2*t+c+2*q)/c)/8

    def K(alpha):
        b = 1-alpha
        if alpha <= mp.mpf(".5"):
            return F(1+alpha, b)+F(alpha, 1)-F(alpha, b)+d*(1+alpha)**2
        if alpha <= mp.mpf(".75"):
            return b*b/4+(1+alpha)*b/2+F(alpha, 1)-F(alpha, b)
        return b/2+F(alpha, 1)+d*alpha*alpha

    def derivative(alpha):
        a, b = (1+alpha)/3, 1-alpha
        return (a/2 + mp.quad(lambda t: mp.sqrt(t/(t+1+alpha)), [a, b])/2
                + mp.quad(lambda t: mp.sqrt(t/(t+alpha)), [b, 1])/2
                -(mp.sqrt(2)-1)*mp.sqrt(b))

    best = mp.findroot(derivative, (mp.mpf(".10"), mp.mpf(".12")))
    assert abs(mp.diff(K, best)) < mp.mpf("1e-60")
    for alpha in (mp.mpf(0), mp.mpf(".107"), mp.mpf(".5"), mp.mpf(".6"),
                  mp.mpf(".75"), mp.mpf(".9"), mp.mpf(1)):
        b = 1-alpha
        points = sorted({mp.mpf(0), b, mp.mpf(1),
                         min(b, (1+alpha)/3), max(b, alpha/3)})

        def integrand(t):
            h = t+1+alpha if t < b else t+alpha
            return max(mp.sqrt(t*h), h/2)

        direct = mp.fsum(mp.quad(integrand, [left, right])
                         for left, right in zip(points, points[1:]))
        assert abs(direct-K(alpha)) < mp.mpf("1e-60"), alpha
    print("alpha_star=" + mp.nstr(best, 40))
    print("C_shift=" + mp.nstr(K(best)/(2*mp.pi), 40))
    print("C_107_1000=" + mp.nstr(K(mp.mpf(".107"))/(2*mp.pi), 40))
    print("PASS: split direct quadrature matches all three functional regimes")


def main():
    mp.mp.dps = 70
    continuum()
    cases = [(m, s) for m in range(2, 10) for s in range(m)]
    cases += [(m, s) for m in (12, 20) for s in sorted({0, 1, m//2-1, m//2,
                                                    m//2+1, 3*m//4-1, 3*m//4,
                                                    3*m//4+1, m-1})]
    cases += [(m, round(mp.mpf(".107")*m)) for m in (40, 80, 160)]
    directions = 0
    worst_angle, worst_cart = mp.mpf(0), mp.mpf(0)
    for m, s in cases:
        chain, full = roots(m, s)
        for factor in ((1, 2) if m <= 3 else (1,)):
            ang, car, count = audit(m, s, full*factor)
            worst_angle, worst_cart = min(worst_angle, ang), min(worst_cart, car)
            directions += count
        if m <= 5:
            audit(m, s, full, rotation=1)
            audit(m, s, full, reflected=True)
        if m <= 9:
            eta = mp.mpf("1e-5")*max(1, full)
            assert not lp_feasible(order(m,s), full-eta), (m,s,"lower LP")
            assert lp_feasible(order(m,s), full+eta), (m,s,"upper LP")
        if m >= 40:
            print(f"n={2*m} s={s} chain_ratio={mp.nstr(chain/(4*m*m),20)} "
                  f"full_ratio={mp.nstr(full/(4*m*m),20)}")
    for invalid in ((1,0),(2,-1),(2,2),(2,0.5)):
        try:
            order(*invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("missing domain rejection")
    print(f"PASS: {len(cases)} finite cases; {directions} directed pair checks")
    print("PASS: 44 all-shift cases m=2..9, LP infeasible below / feasible above cell roots")
    print("PASS: rotation/reflection, positive closure slack, seam/transition and domain checks")
    print("min_angular_slack="+mp.nstr(worst_angle,8))
    print("min_normalized_cartesian_slack="+mp.nstr(worst_cart,8))
    print("Numerical observations only; no global-optimum or all-n certification.")


if __name__ == "__main__":
    main()
