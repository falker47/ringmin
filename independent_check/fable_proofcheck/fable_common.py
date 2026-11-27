"""Shared registry and arithmetic helpers for the November 2026 proof check.

Every conclusion drawn in this package rests on one of two kinds of arithmetic:

* exact integers / ``fractions.Fraction``;
* Arb balls (python-flint), whose comparisons are true only when they hold
  for every point of both balls.

No float decides anything.  The package imports nothing from ``src/ringmin``,
``verify.py`` or any earlier checker in this repository; manuscripts are read
only as data (printed constants and table rows).

This file is identical on the Paper I and Paper II proof-check branches.
"""

from __future__ import annotations

import functools
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx, fmpq

PREC = 256

ROOT = Path(__file__).resolve().parents[2]

# (identifier, kind, claim, function); kind is 'exact', 'interval' or 'symbolic'
CHECKS: list[tuple[str, str, str, object]] = []
# (identifier, description, function); a control must raise AssertionError
CONTROLS: list[tuple[str, str, object]] = []


def working_precision():
    """Context for importing the check modules and running each check.

    Arb's precision is global to the process, and other code may leave any
    value set.  Inside this context it is PREC bits; on exit the caller's value
    is restored, so the checks neither depend on nor change it.
    """
    return ctx.workprec(PREC)


def _at_working_precision(function):
    @functools.wraps(function)
    def run():
        with working_precision():
            return function()

    return run


def check(ident: str, kind: str, claim: str):
    def wrap(function):
        CHECKS.append((ident, kind, claim, _at_working_precision(function)))
        return function

    return wrap


def control(ident: str, description: str):
    """Register a negative control: a deliberately false claim that the
    checking code must reject by raising AssertionError."""

    def wrap(function):
        CONTROLS.append((ident, description, _at_working_precision(function)))
        return function

    return wrap


def need(condition, message: str = "") -> None:
    """Require a condition that is *certainly* true.

    Arb comparisons return False when undecided, so an undecided comparison
    is a failure, never a pass.
    """
    if condition is not True:
        raise AssertionError(message or "required condition is not certainly true")


def ball(value) -> arb:
    """Exact conversion of an int/Fraction to an Arb ball."""
    if isinstance(value, arb):
        return value
    value = Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def hull(lo, hi) -> arb:
    """An Arb ball containing the closed interval [lo, hi]."""
    return ball(lo).union(ball(hi))


def two_pi() -> arb:
    return 2 * arb.pi()


def not_outside(value: arb, lo, hi) -> bool:
    """True unless the ball is certainly outside [lo, hi] (a consistency test)."""
    return not (value < ball(lo)) and not (value > ball(hi))
