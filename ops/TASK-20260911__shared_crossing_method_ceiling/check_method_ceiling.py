"""Exact arithmetic support for THREE_LEVEL_COMMON_CHAIN.md, Section 13.

Run with python -I -S. Fixed finite sums and Fraction gates only; no
production, prior-checker, saved-result or third-party imports. The proof
supplies the universal m/cutoff/width quantifiers, not the controls here.
"""

from fractions import Fraction as Q
from math import comb, factorial

if not __debug__:
    raise RuntimeError("This checker requires enabled assertions; omit -O.")

B = Q(23, 100)
TAU = (Q("0.739085133215160"), Q("0.739085133215161"))
PARAM = (Q("0.195020091350606"), Q("0.195020091350608"))
Q_LO, Q_HI = Q("0.19502009"), Q("0.19502010")
D_LO, D_HI, D_UP = map(Q, ("0.00241410289", "0.00241410290", "0.002414103"))
PI_LO, PI_HI = Q("3.14159"), Q("3.14160")


def trig(x, count, odd):
    return sum(Q((-1)**j, factorial(2*j+odd))*x**(2*j+odd)
               for j in range(count))


def atan(x, count):
    return sum(Q((-1)**j, 2*j+1)*x**(2*j+1) for j in range(count))


def parameter_gates():
    assert 0 < TAU[0] < TAU[1] < 1
    assert trig(TAU[0], 12, 0) > TAU[0]
    assert trig(TAU[1], 13, 0) < TAU[1]
    sine_lo, sine_hi = trig(TAU[0], 12, 1), trig(TAU[1], 13, 1)
    assert 0 < sine_lo < sine_hi < 1
    assert PARAM[0] < (1-sine_hi)/(1+sine_hi)
    assert (1-sine_lo)/(1+sine_lo) < PARAM[1]
    assert Q_LO < PARAM[0] < PARAM[1] < Q_HI < Q(1, 5)
    print("PASS rational Taylor root/sine gates: 0.19502009 < q < 0.19502010")

    # Machin tangent identity and its branch: 0 < angle < 4/5 < 1 < pi/2.
    tangent = Q(1, 5)
    for expected in (Q(5, 12), Q(120, 119)):
        tangent = 2*tangent/(1-tangent*tangent)
        assert tangent == expected
    assert (tangent-Q(1, 239))/(1+tangent*Q(1, 239)) == 1
    assert 4*atan(Q(1, 5), 2)-Q(1, 239) > 0
    assert 4*Q(1, 5) < 1
    pi_lo = 16*atan(Q(1, 5), 6)-4*atan(Q(1, 239), 7)
    pi_hi = 16*atan(Q(1, 5), 7)-4*atan(Q(1, 239), 6)
    assert PI_LO < pi_lo < pi_hi < PI_HI
    print("PASS rational Machin gates: 3.14159 < pi < 3.14160")


def deletion_gates():
    q, s = PARAM[0], 1+PARAM[0]
    u, v = (s-2*B)/s, (1-q)/s
    assert 0 < u < v < 1
    partial = v-u
    for j in range(1, 41):
        coefficient = Q(comb(2*j, j), 4**j*(2*j-1))
        following = Q(comb(2*j+2, j+1), 4**(j+1)*(2*j+1))
        assert 0 < following/coefficient == Q(2*j-1, 2*j+2) < 1
        partial -= coefficient*(v**(2*j+1)-u**(2*j+1))/(2*j+1)
    tail = (v-u)*Q(comb(82, 41), 4**41*81)*v**82/(1-v*v)
    assert 0 < tail < partial
    radical_lo, radical_hi = s*s/4*(partial-tail), s*s/4*partial
    # Moving-r gate: r in (1/6,1/5); x <= B < (1+r)/2.
    assert Q(1, 6) < PARAM[0] < PARAM[1] < Q(1, 5)
    assert 2*B < 1+PARAM[0] and 0 < B-PARAM[0] < 1
    linear = s*(B-q)-(B*B-q*q)/2
    error = 4*(PARAM[1]-PARAM[0])
    d_lo, d_hi = linear-2*radical_hi-error, linear-2*radical_lo+error
    assert D_LO < d_lo < d_hi < D_HI < D_UP
    # Integrand positivity, hence monotonicity of D(beta) up to B.
    assert 5*B < 1+Q_LO and Q_LO > 0
    print("PASS 40-term integral/tail: 0.00241410289 < D(b) < 0.00241410290")


def width_controls():
    # Single-cutoff positive F, zero F, and admissible F<0 with H>B-q.
    h = Q(1, 100)
    assert h*D_LO-8*h**3 > 0
    assert h*h < D_LO/8 and h < Q(3, 100) < B-Q_HI
    assert D_UP/8 < Q(3, 100)**2  # Universal F>0 implication for m=1.
    h = Q(0)
    assert max(h*D_UP-8*h**3, 0)/(PI_LO*(16+432*h)) == 0
    h = Q(1, 20)
    assert h > B-Q_LO and h*D_UP-8*h**3 < 0
    assert max(h*D_UP-8*h**3, 0) == 0
    print("PASS m=1 controls: positive/zero/negative F; unconditional H bound rejected")

    # Weak equality, an internal zero, endpoint zeros, and all-zero widths.
    cases = (
        ((Q(1, 5), B), (Q(1, 100), Q(1, 50))),
        ((Q(1, 5), Q(21, 100), B), (Q(1, 100), Q(0), Q(1, 50))),
        ((Q(1, 5), Q(21, 100), Q(22, 100), B),
         (Q(0), Q(1, 100), Q(0), Q(1, 100))),
        ((Q(1, 5), B), (Q(0), Q(0))),
    )
    for beta, widths in cases:
        assert len(beta) == len(widths) >= 2
        assert Q_HI < beta[0] < beta[-1] <= B
        assert all(h >= 0 for h in widths)
        adjacent = [widths[i]+widths[i+1] for i in range(len(widths)-1)]
        gaps = [beta[i+1]-beta[i] for i in range(len(beta)-1)]
        assert all(0 <= a <= g for a, g in zip(adjacent, gaps))
        total = sum(widths)
        assert total+sum(widths[1:-1]) == sum(adjacent)
        assert total <= sum(adjacent) <= beta[-1]-beta[0] < B-Q_HI
    print("PASS m>=2 controls: adjacent equality, internal/endpoint zeros, H=0")


def ceiling_gate():
    upper = (B-Q_LO)*D_UP/(16*PI_LO)
    target = Q(21, 12500000)
    assert upper == Q(8444510567073, 5026544000000000000)
    assert target-upper == Q(83352927, 5026544000000000000) > 0
    print(f"PASS uniform ceiling U={upper}")
    print(f"PASS 1.68e-6 - U={target-upper} > 0")


if __name__ == "__main__":
    parameter_gates()
    deletion_gates()
    width_controls()
    ceiling_gate()
    print("PASS Section 13 arithmetic; universal quantifiers and scope use the proof")
