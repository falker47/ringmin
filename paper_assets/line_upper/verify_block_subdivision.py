"""Independent integer midpoint enclosure of the published max integrand.

No antiderivatives, root isolation, Arb, or generator imports are used.
All abscissae are ticks on a common grid. Derivative and switch-panel
bounds are proved in NOTE.md.
"""
from fractions import Fraction
from math import ceil, floor, isqrt

BASE = 100000
N = 32768
GRID = 2 * N * BASE
ROOT_SCALE = 10**10


def candidates(t, x, y):
    scale2 = ROOT_SCALE**2
    legs = isqrt(t*x*scale2) + isqrt(t*y*scale2)
    chord = isqrt(x*y*scale2)
    return legs, chord


def integral(start, stop, offset, reflected):
    step = 2*(stop-start)
    a = start*2*N
    offset_ticks = offset*2*N
    mirror = offset_ticks + (start+stop)*2*N
    low_sum = high_sum = smooth = uncertain = 0
    for _ in range(N):
        b = a+step
        x0, x1 = offset_ticks+a, offset_ticks+b
        y0, y1 = (mirror-b, mirror-a) if reflected else (x0, x1)
        lower_legs, lower_chord = candidates(a, x0, y0)
        upper_legs, upper_chord = candidates(b, x1, y1)
        # Floors enclose a root to one unit; the sum of two to two.
        legs_active = lower_legs >= upper_chord+1 and 4*a >= GRID
        chord_active = lower_chord >= upper_legs+2 or 4*b <= GRID
        if legs_active or chord_active:
            half = (a+b)//2
            midlegs, midchord = candidates(half, (x0+x1)//2, (y0+y1)//2)
            value = midlegs if legs_active else midchord
            low_sum += value
            high_sum += value+(2 if legs_active else 1)
            smooth += 1
        else:
            low_sum += max(lower_legs, lower_chord)
            high_sum += max(upper_legs+2, upper_chord+1)
            uncertain += 1
        a = b
    h = Fraction(step, GRID)
    unit = h / (GRID*ROOT_SCALE)
    error = Fraction(100,24)*smooth*h**3
    return low_sum*unit-error, high_sum*unit+error, uncertain


def pi_bounds():
    def alternating(q):
        partial = sum(Fraction((-1)**k, q**(2*k+1)*(2*k+1)) for k in range(24))
        return partial, partial+Fraction(1,49*q**49)
    a, b = alternating(5)
    c, d = alternating(239)
    return 16*a-4*d, 16*b-4*c


def enclose(pieces=None):
    # Independently encode consecutive endpoints and the diagonal wrap.
    if pieces is None:
        pieces = [(0,31903,110930,True), (31903,36273,110930,True),
                  (36273,36853,110930,True), (36853,36858,110930,True),
                  (36858,89070,110930,False), (89070,100000,10930,False)]
    lo = hi = Fraction(0)
    uncertain = 0
    for item in pieces:
        l, u, k = integral(*item)
        lo += l
        hi += u
        uncertain += k
    lower_pi, upper_pi = pi_bounds()
    return lo/(4*upper_pi), hi/(4*lower_pi), uncertain


if __name__ == "__main__":
    lo, hi, count = enclose()
    scale = 10**13
    l, u = floor(lo*scale), ceil(hi*scale)
    if u-l > scale//10**9:
        raise SystemExit("FAIL interval too wide")
    print(f"RATIONAL_BLOCK_INTEGER {l//scale}.{l%scale:013d}"
          f" {u//scale}.{u%scale:013d} uncertain_panels={count}")
    dl, du, _ = enclose([(0,89300,110700,False), (89300,100000,10700,False)])
    l, u = floor(dl*scale), ceil(du*scale)
    print(f"DIAGONAL_INTEGER {l//scale}.{l%scale:013d} {u//scale}.{u%scale:013d}")
