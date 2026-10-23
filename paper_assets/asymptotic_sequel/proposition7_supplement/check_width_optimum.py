"""Exact rational support for THREE_LEVEL_COMMON_CHAIN.md, Section 12.

Run with python -I -S. Fixed cutoffs, fixed root bracket, no optimizer,
production imports, earlier-checker imports, saved results or dependencies.
The proof supplies global quantifiers; this file certifies its sign gates.
"""

from fractions import Fraction as F
from math import comb, factorial

if not __debug__:
    raise RuntimeError("This checker requires enabled assertions; omit -O.")

TAU = tuple(map(F, (
    "0.7390851332151606416553120876738734040134",
    "0.7390851332151606416553120876738734040135")))
Q = tuple(map(F, (
    "0.1950200913506069300798071259134151019366",
    "0.1950200913506069300798071259134151019367")))
PI = tuple(map(F, (
    "3.1415926535897932384626433832795028841971",
    "3.1415926535897932384626433832795028841972")))
BETA = (F(2091, 10000), F(10907, 50000), F(23, 100))
OLD = (F(451, 100000), F(451, 100000), F(367, 50000))
A, B = BETA[1]-BETA[0], BETA[2]-BETA[1]
S = A+B
X = tuple(map(F, ("0.00451910758124826", "0.00451910758124827")))


def point(x):
    return (F(x), F(x))


def add(u, v):
    return (u[0]+v[0], u[1]+v[1])


def sub(u, v):
    return (u[0]-v[1], u[1]-v[0])


def mul(u, v):
    products = [x*y for x in u for y in v]
    return (min(products), max(products))


def scale(c, u):
    return mul(point(c), u)


def div(u, v):
    assert 0 < v[0] <= v[1]
    return mul(u, (1/v[1], 1/v[0]))


def power(u, k):
    assert 0 <= u[0] <= u[1] and k >= 1
    return (u[0]**k, u[1]**k)


def total(values):
    result = point(0)
    for value in values:
        result = add(result, value)
    return result


def decimal_bounds(bounds, digits):
    low, high = bounds
    assert low <= high
    scale10 = 10**digits
    return (F((low*scale10).__floor__()-1, scale10),
            F((high*scale10).__ceil__()+1, scale10))


def show(name, bounds, digits=23):
    low, high = decimal_bounds(bounds, digits)
    assert 0 <= low < high

    def decimal(x):
        whole, fraction = divmod(int(x*10**digits), 10**digits)
        return f"{whole}.{fraction:0{digits}d}"

    print(f"{decimal(low)} < {name} < {decimal(high)}")


def transcendental_gates():
    def trig(x, count, odd):
        return sum(F((-1)**j, factorial(2*j+odd))*x**(2*j+odd)
                   for j in range(count))

    assert 0 < TAU[0] < TAU[1] < 1
    assert trig(TAU[0], 30, 0) > TAU[0]
    assert trig(TAU[1], 31, 0) < TAU[1]
    sine = (trig(TAU[0], 30, 1), trig(TAU[1], 31, 1))
    assert 0 < sine[0] < sine[1] < 1
    assert Q[0] < (1-sine[1])/(1+sine[1])
    assert (1-sine[0])/(1+sine[0]) < Q[1]

    def atan(x, count):
        return sum(F((-1)**j, 2*j+1)*x**(2*j+1) for j in range(count))

    tangent = F(1, 5)
    for _ in range(2):
        tangent = 2*tangent/(1-tangent*tangent)
    assert (tangent-F(1, 239))/(1+tangent/F(239)) == 1
    pi_low = 16*atan(F(1, 5), 32)-4*atan(F(1, 239), 31)
    pi_high = 16*atan(F(1, 5), 31)-4*atan(F(1, 239), 32)
    assert PI[0] < pi_low < pi_high < PI[1]
    print("PASS alternating rational Taylor gates: tau, q, pi")


def deletion(beta):
    """Integrated binomial series: exact 80 terms, tail, moving-q error."""
    assert Q[1] < beta <= F(23, 100)
    q, s = Q[0], 1+Q[0]
    u, v = (s-2*beta)/s, (1-q)/s
    assert 0 < u < v < 1
    integral = v-u
    for j in range(1, 81):
        cj = F(comb(2*j, j), 4**j*(2*j-1))
        integral -= cj*(v**(2*j+1)-u**(2*j+1))/(2*j+1)
    c81 = F(comb(162, 81), 4**81*161)
    tail = (v-u)*c81*v**162/(1-v*v)
    assert 0 < tail < integral
    linear = s*(beta-q)-(beta*beta-q*q)/2
    error = 4*(Q[1]-Q[0])
    bounds = (linear-s*s*integral/2-error,
              linear-s*s*(integral-tail)/2+error)
    # Safe outward compression prevents huge denominators in later gates.
    return decimal_bounds(bounds, 30)


def widths(x):
    return (sub(point(A), x), x, sub(point(B), x))


def numerator(h, ds):
    return sub(total(mul(u, d) for u, d in zip(h, ds)),
               scale(8, total(power(u, 3) for u in h)))


def denominator(h):
    return add(point(16), scale(432, total(h)))


def quotient(h, ds):
    return div(numerator(h, ds), denominator(h))


def stationary(x, ds):
    h = widths(x)
    slope = add(sub(sub(ds[1], ds[0]), ds[2]),
                scale(24, sub(add(power(h[0], 2), power(h[2], 2)),
                              power(h[1], 2))))
    return add(mul(slope, denominator(h)), scale(432, numerator(h, ds)))


def symbolic_identity_gates():
    """Check the two proof identities as formal polynomials, not samples."""
    zero = (0, 0, 0, 0)

    def constant(c):
        return {zero: c}

    def variable(i):
        return {tuple(int(j == i) for j in range(4)): 1}

    def plus(*polynomials):
        result = {}
        for polynomial in polynomials:
            for powers, coefficient in polynomial.items():
                result[powers] = result.get(powers, 0)+coefficient
        return {powers: c for powers, c in result.items() if c}

    def times(*polynomials):
        result = constant(1)
        for polynomial in polynomials:
            terms = {}
            for powers, coefficient in result.items():
                for other, c in polynomial.items():
                    key = tuple(x+y for x, y in zip(powers, other))
                    terms[key] = terms.get(key, 0)+coefficient*c
            result = {powers: c for powers, c in terms.items() if c}
        return result

    h, u = variable(0), variable(1)
    difference = plus(h, times(constant(-1), u))
    left = plus(times(h, h, h), times(constant(-1), u, u, u),
                times(constant(-3), u, u, difference))
    right = times(difference, difference, plus(h, times(constant(2), u)))
    assert left == right

    t, linear, cubes, mass = (variable(i) for i in range(4))
    ell = plus(constant(16), times(constant(432), mass))
    ell_t = plus(constant(16), times(constant(432), t, mass))
    numerator_at_one = plus(linear, times(constant(-8), cubes))
    numerator_at_t = plus(times(t, linear), times(constant(-8), t, t, t, cubes))
    left = plus(times(numerator_at_one, ell_t),
                times(constant(-1), numerator_at_t, ell))
    right = times(plus(constant(1), times(constant(-1), t)), plus(
        times(constant(16), linear),
        times(constant(-128), plus(constant(1), t, times(t, t)), cubes),
        times(constant(-3456), mass, t, plus(constant(1), t), cubes)))
    assert left == right
    print("PASS formal polynomial identities: global cubic remainder and scaling loss")


def polynomial_gates(ds):
    # Coefficients of N(x), and G=N'L+432N, in ascending powers.
    d0, d1, d2 = (d[0] for d in ds)
    c0 = A*d0+B*d2-8*(A**3+B**3)
    c1 = d1-d0-d2+24*(A*A+B*B)
    coefficients = (c0, c1, -24*S, F(8))
    ell = 16+432*S
    expected = (ell*c1+432*c0, -48*ell*S,
                24*ell+10368*S, F(-6912))
    derived = []
    for k in range(4):
        next_term = (k+1)*coefficients[k+1] if k < 3 else 0
        derived.append(ell*next_term+432*(1-k)*coefficients[k])
    assert tuple(derived) == expected
    # G'=48(x-S)(ell-432x), verified as a polynomial identity.
    assert tuple(k*derived[k] for k in range(1, 4)) == (
        -48*S*ell, 48*(ell+432*S), F(-20736))
    assert 0 < X[0] < X[1] < A < B < S
    assert 16+432*(S-A) > 0
    assert stationary(point(0), ds)[0] > 0
    assert stationary(point(A), ds)[1] < 0
    left, right = stationary(point(X[0]), ds), stationary(point(X[1]), ds)
    assert left[0] > 0 and right[1] < 0
    print("PASS exact cubic identities; G'<0 on [0,a]; isolated root signs")


def optimality_gates(ds):
    h = widths(X)
    n, ell = numerator(h, ds), denominator(h)
    rho = div(n, ell)
    assert n[0] > 0 and rho[0] > 0
    multipliers = [sub(sub(ds[i], scale(24, power(h[i], 2))),
                       scale(432, rho)) for i in (0, 2)]
    assert multipliers[0][0] > F("0.00035")
    assert multipliers[1][0] > F("0.00059")
    eta = div(rho, PI)
    old_h = tuple(point(u) for u in OLD)
    old_rho = quotient(old_h, ds)
    assert numerator(old_h, ds)[0] > 0
    old_eta = div(old_rho, PI)
    gain = sub(eta, old_eta)
    assert gain[0] > 0
    relative_percent = scale(100, div(gain, old_eta))
    gradient1 = sub(sub(ds[0], point(24*OLD[0]**2)), scale(432, old_rho))
    assert gradient1[0] > F("0.00035")
    assert A-OLD[0]-OLD[1] == F(1, 50000)
    assert B-OLD[1]-OLD[2] == F(1, 100000)
    # A concrete rational strict improvement, using only available slack.
    improved = (OLD[0]+F(1, 100000), OLD[1], OLD[2])
    improved_h = tuple(point(u) for u in improved)
    assert A-improved[0]-improved[1] == F(1, 100000)
    assert B-improved[1]-improved[2] == F(1, 100000)
    improved_gain = sub(div(quotient(improved_h, ds), PI), old_eta)
    assert improved_gain[0] > F("0.000000000048")
    # Uniform scaling loss <= (1-t) sum(h_i D_i)/(pi L*) < (1-t)*5e-7.
    linear = total(mul(u, d) for u, d in zip(h, ds))
    assert div(linear, mul(PI, ell))[1] < F(1, 2000000)
    c = div(mul(TAU, add(point(1), Q)), scale(2, PI))
    print("PASS positive F and KKT multipliers; unique-global proof applies")
    print("PASS accepted witness is not local: positive first-coordinate derivative")
    for i, interval in enumerate(ds, 1):
        show(f"D_{i}", interval)
    show("x_star", X)
    for i, interval in enumerate(h, 1):
        show(f"h_star_{i}", interval)
    for name, interval in (("lambda_1", multipliers[0]),
                           ("lambda_2", multipliers[1]),
                           ("eta_width", eta), ("eta_4", old_eta),
                           ("eta_width-eta_4", gain),
                           ("relative_gain_percent", relative_percent),
                           ("C_term+eta_width", add(c, eta)),
                           ("strict_rational_witness_gain", improved_gain)):
        show(name, interval)


def floor_gates():
    assert A == F(113, 12500) and B == F(593, 50000)
    assert BETA[0]-Q[1] > A and 1/A > 102
    assert Q[0]-F(1, 102) > F(1, 6)
    # beta_i*50000 are all integers: residue 1 recurs indefinitely.
    assert tuple(b*50000 for b in BETA) == (10455, 10907, 11500)
    assert all(0 < b < 1 for b in BETA)
    for k in (1, 2):  # Corroboration; the proof handles every k>=1.
        n = 50000*k+1
        ell = [(b*n).__floor__() for b in BETA]
        assert ell == [10455*k, 10907*k, 11500*k]
        assert F(ell[1]-ell[0], n) == A*(n-1)/n < A
        assert F(ell[2]-ell[1], n) == B*(n-1)/n < B
    # Example of the proved strict-scaling gate, not an asymptotic exchange.
    t = F(9999, 10000)
    threshold = (1/((1-t)*A)).__ceil__()
    assert threshold == 1106195
    assert threshold*(1-t)*A >= 1
    assert threshold*(1-t)*B >= 1
    assert threshold*(BETA[0]-Q[1]) > 1
    # The displayed improved rational witness retains the old finite threshold.
    assert 100000*F(1, 100000) == 1
    assert 100000*(BETA[0]-Q[1]) > 1
    print("PASS boundary floor failure for n=50000k+1; no eventual unchanged gate")
    print("PASS strict scaling: t=9999/10000, N=1106195; loss < 5e-11")
    print("PASS improved rational witness: both margins 1/100000, N=100000")


if __name__ == "__main__":
    symbolic_identity_gates()
    transcendental_gates()
    deletion_bounds = tuple(deletion(beta) for beta in BETA)
    polynomial_gates(deletion_bounds)
    optimality_gates(deletion_bounds)
    floor_gates()
    print("PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers")
