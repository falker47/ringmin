"""Negative controls for Paper II: false variants that the checks must reject."""

from __future__ import annotations

import random
from fractions import Fraction

from flint import arb

from p2_base import BETA, C_TERM, Order, Q, ball, control, floor_q, need, supnick
from p2_energy import test_orders
from p2_minimax import A_, B_, F, G, gates, optimum, script_L


@control("P2-X1", "E <= 4e (the paper proves E <= 8e) for the Supnick order at n = 102")
def energy_constant_halved():
    o = Order(102, supnick(range(floor_q(102), 103)))
    need(4 * o.e > ball(o.E))


@control("P2-X2", "|Delta - Lambda| <= E/1000 (the paper proves 43E) for the test orders at n = 102")
def variation_constant_tiny():
    rng = random.Random(4)
    for _name, cycle in test_orders(102, rng):
        o = Order(102, cycle)
        c = o.cut(BETA[0])
        need(abs(c["Delta"] - c["Lambda"]) < ball(o.E) / 1000)


@control("P2-X3", "|J_n - pi C_term| <= 2/(5n) (the paper proves 5/n) for 102 <= n < 330")
def floor_constant_tiny():
    target = C_TERM * arb.pi()
    for n in range(102, 330):
        k = floor_q(n)
        s = 1 + Fraction(k, n)
        Jn = sum(((ball(Fraction(j, n)) * ball(s - Fraction(j, n))).sqrt() for j in range(k, n + 1)), arb(0)) / n
        need(abs(Jn - target) < ball(Fraction(2, 5 * n)))


@control("P2-X4", "the unshrunk optimum u satisfies the finite gates at n = 50001")
def unshrunk_gates():
    _, (zlo, zhi), _, _ = optimum()
    z0 = (zlo + zhi) / 2
    need(gates(50001, (A_ - z0, z0, B_ - z0)))


@control("P2-X5", "G(a) > 0, so that G has no root on [0, a]")
def wrong_sign_of_G():
    D, _, _, _ = optimum()
    need(G(A_, D) > 0)


@control("P2-X6", "C_term + eta_width exceeds the printed upper endpoint of (SM1.4)")
def bound_above_enclosure():
    _, _, _, rho = optimum()
    need(C_TERM + rho / arb.pi() > ball(Fraction(14056946887766098063392, 10**23)))


@control("P2-X7", "the vertex h = (a, 0, b) does at least as well as u")
def vertex_beats_optimum():
    D, _, _, rho = optimum()
    h = (A_, 0, B_)
    need(F(h, D).max(arb(0)) / script_L(h) > rho)


@control("P2-X8", "q > 1/5")
def wrong_q_gate():
    need(Q > ball(Fraction(1, 5)))
