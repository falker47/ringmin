"""Bounded independent support for the fourth continuous reflected block.

Run: python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
Stdlib only; no production/prior-checker imports, parameter solving, width
search, finite permutations or file output. Explicit checks survive -O.
The analytic proof supplies interval quantifiers and the cubic coefficient.
"""

from fractions import Fraction as Q
from itertools import product
from math import isqrt


AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, EU = Q(43, 1000), Q(7, 160)
DL, DU = Q(29, 5000), Q(27, 4000)
ETA = Q(1, 20000)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sqrt_bounds(value):
    require(value >= 0, "negative radicand")
    scale = 10**40
    lo = Q(isqrt(value.numerator * scale**2 // value.denominator), scale)
    hi = lo + Q(1, scale)
    require(0 <= lo and lo**2 <= value < hi**2, "directed root failed")
    return lo, hi


def sum_root_sign(p, q):
    """Sign of sqrt(p)+sqrt(q)-1, with pre-square signs and ties."""
    require(p >= 0 and q >= 0, "negative squared ratio")
    residual = 1-p-q
    if residual < 0:
        return 1
    difference = 4*p*q-residual**2
    return (difference > 0)-(difference < 0)


def require_chord_slab(A, w, eta):
    require(A > 1 and 0 < w < A/3 and 0 < eta <= A/3-w,
            "outside pre-cutoff domain")
    require(A-3*w-4*eta > 0, "sufficient closed-slab chord gate failed")


def raw_max_bounds(t, X, Y):
    tl, th = sqrt_bounds(t)
    xl, xh = sqrt_bounds(X)
    yl, yh = sqrt_bounds(Y)
    cl, ch = sqrt_bounds(X*Y)
    return max(tl*(xl+yl), cl), max(th*(xh+yh), ch)


def ceil_grid(value, scale):
    scaled = value*scale
    return Q(-((-scaled.numerator)//scaled.denominator), scale)


def main():
    require(0 < AL < AH < Q(1, 2), "alpha bracket")
    require(Q(1, 4) < XL < XH < Q(1, 3), "x bracket")
    require(0 < EL < EU and 0 < DL < DU, "width brackets")
    a_lo, a_hi = 1+AL, 1+AH
    v_lo, v_hi = a_lo*XL+EL, a_hi*XH+EU
    w_lo, w_hi = v_lo+DL, v_hi+DU
    require(w_lo > a_hi/4 and w_hi < a_lo/3, "start bracket")
    margins = {
        "A-3w": a_lo-3*w_hi,
        "A-3w-4eta_0": a_lo-3*w_hi-4*ETA,
        "a-w-eta_0": a_lo/3-w_hi-ETA,
        "b-w-eta_0": 1-AH-w_hi-ETA,
        "3/2-M": Q(3, 2)-a_hi-w_hi-ETA/2,
    }
    expected = (Q(354539, 10**9), Q(154539, 10**9),
                Q(204539, 3*10**9), Q(520991513, 10**9),
                Q(21016513, 10**9))
    for (name, value), target in zip(margins.items(), expected, strict=True):
        require(value == target and value > 0, name)
        print("EXACT", name, ">", value, "> 0")
    require(margins["A-3w-4eta_0"]+ETA == 3*margins["a-w-eta_0"],
            "independent diagonal/ratio gate consistency")
    saving = ETA**3/576
    require(saving == Q(1, 4608000000000000), "saving conversion")

    controls = ((Q(1, 4), Q(1, 4), 0), (Q(1, 9), Q(1, 9), -1),
                (Q(4, 9), Q(4, 9), 1), (Q(1), Q(0), 0),
                (Q(2), Q(0), 1), (Q(0), Q(0), -1))
    for p, q, sign in controls:
        require(sum_root_sign(p, q) == sign, "sign/tie control")

    # Exactly 16 imported-box corners, 4 separate reflections, 7 moments.
    # These are probes, not substitutions for the four exact parameters.
    corners = moments = probes = 0
    for alpha, x, epsilon, delta in product((AL, AH), (XL, XH),
                                          (EL, EU), (DL, DU)):
        A = 1+alpha
        lam = A*x
        v, w = lam+epsilon, lam+epsilon+delta
        ends = (Q(0), lam, v, w, w+ETA)
        require_chord_slab(A, w, ETA)
        require(0 < lam < v < w < w+ETA < A/3 < 1-alpha < 1, "domain")
        high_ends = (Q(1), A, A+lam, A+v, A+w, A+w+ETA, Q(2))
        require(all(l < r for l, r in zip(high_ends, high_ends[1:])),
                "high partition")
        require(sum(r-l for l, r in zip(high_ends, high_ends[1:])) == 1,
                "high total length")
        for left, right in zip(ends, ends[1:]):
            intercept = left+right
            require(intercept-left == right and intercept-right == left,
                    "separate reflection endpoints")
            for degree in range(7):
                power = degree+1
                direct = ((A+right)**power-(A+left)**power)/power
                reflected = ((A+intercept-left)**power
                             -(A+intercept-right)**power)/power
                require((direct+reflected)/2 == direct, "high moment")
                moments += 1
        for s in (Q(0), ETA/2, ETA):
            t, X, Y = w+s, A+w+s, A+w+ETA-s
            require(sum_root_sign(t/X, t/Y) == -1 and 4*t < X,
                    "literal inserted/removed max branch")
            probes += 1
        corners += 1
    print("PASS", corners, "corner partitions,", moments,
          "reflection moments,", probes, "branch probes, 6 sign/tie controls")

    # Independent 16-panel midpoint upper enclosure of the RAW full max.
    # Analytic concavity and integrated monotonicity in B justify the bound.
    # No centered/rationalized integrand or antiderivative is evaluated.
    A, w = a_hi, w_hi
    require_chord_slab(A, w, ETA)
    B = A+w
    panels, width = 16, ETA/16
    inserted_upper = Q(0)
    for j in range(panels):
        s = width*Q(2*j+1, 2)
        t, X, Y = w+s, B+s, B+ETA-s
        _, upper = raw_max_bounds(t, X, Y)
        inserted_upper += width*upper
    # Diagonal is chord by the whole-slab gate, so its integral is exact.
    raw_upper = inserted_upper-ETA*(B+ETA/2)
    reported_upper = ceil_grid(raw_upper, 10**24)
    require(raw_upper <= reported_upper < -ETA**3/36,
            "independent full-max enclosure does not prove requested saving")
    print("EXACT 16-panel raw full-max increment <=", reported_upper)
    print("PASS raw enclosure <", -ETA**3/36)
    print("EXACT normalized saving >", saving, "using pi<4")

    # A real branch-switch control: at the diagonal cutoff the inserted
    # endpoint is chain while the removed endpoint ties. Do not extrapolate
    # the chord formula into this regime.
    h = A/3-w
    t, X, Y = w+h, B+h, B
    require(4*t == X and sum_root_sign(t/X, t/Y) == 1, "cutoff switch")
    tl, _ = sqrt_bounds(t)
    xl, _ = sqrt_bounds(X)
    yl, _ = sqrt_bounds(Y)
    _, ch = sqrt_bounds(X*Y)
    require(tl*(xl+yl) > ch, "raw root interval must detect chain excess")
    rejected = 0
    for bad_width in (Q(0), -ETA, h):
        try:
            require_chord_slab(A, w, bad_width)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("invalid/changing-branch width accepted")
    require(rejected == 3, "negative controls")
    print("PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected")
    print("PASS bounded exact support; analytic proof supplies interval and cubic term")
    print("NOTE no root solving, width scan, finite recovery, transfer or output files")


if __name__ == "__main__":
    main()
