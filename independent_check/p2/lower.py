"""Check S1 by Arb enclosures of the defining equations, independent of its quadrature.

The semicircle antiderivative evaluates the three integrals. Two sign bisections
start from the full domains of the roots. Saved enclosures are comparison
targets only. All comparisons of balls below require definite inequalities.
"""

import json
import re
from fractions import Fraction
from zipfile import ZipFile

from flint import arb, ctx, fmpq


def ball(value):
    value = Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def enclosed(value, endpoints):
    left, right = map(ball, endpoints)
    return left < value and value < right


def decreasing_root(function, left, right):
    """Isolate one root of a continuous strictly decreasing function."""
    left, right = Fraction(left), Fraction(right)
    if not (function(ball(left)) > 0 and function(ball(right)) < 0):
        raise ArithmeticError("root endpoint signs do not bracket a zero")
    for _ in range(180):
        mid = (left + right) / 2
        result = function(ball(mid))
        if result > 0:
            left = mid
        elif result < 0:
            right = mid
        else:
            # The last opposite-sign endpoints still enclose the root.
            break
    return ball(left).union(ball(right))


def terminal_integral(q, beta):
    """Integral of (1+q-x)-2 sqrt(x(1+q-x)) on [q,beta]."""
    scale = 1 + q

    def primitive(x):
        # y=(2x-s)/s sends the radical to (s/2)*sqrt(1-y^2).
        y = 2 * x / scale - 1
        arc = y * (1 - y * y).sqrt() + y.asin()
        return scale * x - x * x / 2 - scale**2 * arc / 4

    return primitive(beta) - primitive(q)


def one(pattern, source):
    matches = re.findall(pattern, source)
    if len(matches) != 1:
        raise ValueError(
            f"expected one manuscript expression matching {pattern!r}, found {len(matches)}"
        )
    return matches[0]


def run(root):
    with ctx.workprec(320):
        return lower_checks(root)


def lower_checks(root):
    paper = root / "paper_assets" / "journal_p2_sidma"
    main = (paper / "main.tex").read_text(encoding="utf-8")
    supplement = (paper / "supplement.tex").read_text(encoding="utf-8")
    numbers = (paper / "numbers.tex").read_text(encoding="utf-8")
    cert_path = (
        root / "paper_assets/asymptotic_sequel/proposition7_supplement/certificate.json"
    )
    cert = json.loads(cert_path.read_bytes())
    checks = []

    def check(label, ok):
        checks.append((label, bool(ok)))

    def saved(label, value, bounds):
        check("S1 certificate " + label, enclosed(value, bounds))

    expected_fields = {
        "schema",
        "semantics",
        "scientific_commit",
        "tau",
        "q",
        "pi",
        "C_term",
        "D",
        "beta",
        "G_signs",
        "z_star",
        "widths",
        "F_at_u",
        "L_at_u",
        "rho",
        "eta_width",
        "multipliers",
        "lower_coefficient",
        "strict_target",
    }
    check(
        "S1 certificate numerical inventory",
        set(cert) == expected_fields
        and cert["schema"] == "ringmin-proposition7-rational-v1"
        and all(len(cert[field]) == 3 for field in ("D", "beta", "widths"))
        and len(cert["multipliers"]) == 2
        and set(cert["G_signs"]) == {"zero", "a", "z_minus", "z_plus"},
    )

    with ZipFile(paper / "s1_support.zip") as bundle:
        check(
            "S1 distributed certificate identical",
            bundle.read("lower_supplement/certificate.json") == cert_path.read_bytes(),
        )

    # L2. The derivative of cos(t)-t is negative on [0,1].
    tau = decreasing_root(lambda t: t.cos() - t, 0, 1)
    q = (1 - tau.sin()) / (1 + tau.sin())
    pi = arb.pi()
    terminal = tau * (1 + q) / (2 * pi)
    for name, value, symbol in (("tau", tau, "T"), ("q", q, "q"), ("pi", pi, r"\\pi")):
        saved(name, value, cert[name])
        endpoints = [
            one(symbol + "_" + re.escape(sign) + r"&=(\d+\.\d+)", supplement)
            for sign in ("-", "+")
        ]
        check("S1 printed " + name, enclosed(value, endpoints))
    saved("C_term", terminal, cert["C_term"])

    cuts = one(
        r"\\left\(\\frac\{(\d+)\}\{(\d+)\},\\frac\{(\d+)\}\{(\d+)\},\\frac\{(\d+)\}\{(\d+)\}\\right\)",
        supplement,
    )
    beta = [Fraction(int(cuts[i]), int(cuts[i + 1])) for i in range(0, 6, 2)]
    main_cuts = one(r"\\beta_3\)=\((\d+/\d+),(\d+/\d+),(\d+/\d+)\)", main)
    check("S1 and main cutoffs agree", list(map(Fraction, main_cuts)) == beta)
    a, b = beta[1] - beta[0], beta[2] - beta[1]
    check(
        "S1 fixed cutoffs and widths",
        list(map(Fraction, cert["beta"])) == beta
        and a == Fraction(113, 12500)
        and b == Fraction(593, 50000),
    )
    check(
        "S1 grid domain n>=102",
        ball(Fraction(3, 17)) < q < ball(Fraction(1, 5))
        and Fraction(3, 17) - Fraction(1, 102) == Fraction(1, 6),
    )
    check(
        "S1 shrink threshold N(t)",
        ball(beta[0] - a) > q and 1 / a > 102 and b >= a and (1 - beta[2]) * 102 >= 2,
    )
    # For n=50000j+1 each beta*n has integer offset 50000*beta*j
    # and fractional part beta. Adjacent floor differences then equal (n-1)*a,b.
    check(
        "S1 failed boundary widths n=50000j+1",
        [50000 * x for x in beta] == [10455, 10907, 11500]
        and all(0 < x < 1 for x in beta),
    )
    gains = [terminal_integral(q, ball(cutoff)) for cutoff in beta]
    for i, gain in enumerate(gains, start=1):
        saved(f"D{i}", gain, cert["D"][i - 1])
        printed = one(r"(\d+\.\d+)&<D_" + str(i) + r"<(\d+\.\d+)", supplement)
        check(f"S1 printed D{i}", enclosed(gain, printed) and gain > 0)

    # L7. Work directly with the gradients on the active edge, avoiding
    # the expanded cubic coefficients and their cancellations.
    def objective(widths):
        return sum(w * (d - 8 * w * w) for w, d in zip(widths, gains))

    def edge(z):
        return [ball(a) - z, z, ball(b) - z]

    def polynomial(z):
        widths = edge(z)
        gradients = [d - 24 * w * w for w, d in zip(widths, gains)]
        slope = gradients[1] - gradients[0] - gradients[2]
        return slope * (16 + 432 * sum(widths)) + 432 * objective(widths)

    z = decreasing_root(polynomial, 0, a)
    z_bracket = one(r"z_-=(\d+\.\d+),\\qquad z_\+=(\d+\.\d+)\.", supplement)
    check("S1 printed z_*", enclosed(z, z_bracket))
    saved("z_star", z, cert["z_star"])
    for name, point, sign in (
        ("zero", 0, 1),
        ("a", a, -1),
        ("z_minus", z_bracket[0], 1),
        ("z_plus", z_bracket[1], -1),
    ):
        value = polynomial(ball(point))
        saved("G(" + name + ")", value, cert["G_signs"][name])
        check("S1 sign G(" + name + ")", sign * value > 0)
    widths = edge(z)
    for i, width in enumerate(widths):
        saved(f"width {i + 1}", width, cert["widths"][i])
    f_value = objective(widths)
    denominator = 16 + 432 * sum(widths)
    rho = f_value / denominator
    eta = rho / pi
    lower = terminal + eta
    for key, value in (
        ("F_at_u", f_value),
        ("L_at_u", denominator),
        ("rho", rho),
        ("eta_width", eta),
        ("lower_coefficient", lower),
    ):
        saved(key, value, cert[key])
    check(
        "S1 strictly positive widths and positive objective",
        all(w > 0 for w in widths) and f_value > 0,
    )
    thresholds = one(
        r"\\lambda_1=g_1>(\d+\.\d+),\\qquad \\lambda_2=g_3>(\d+\.\d+)", supplement
    )
    for i, threshold in enumerate(thresholds):
        j = 2 * i
        multiplier = gains[j] - 24 * widths[j] ** 2 - 432 * rho
        saved(f"lambda {i + 1}", multiplier, cert["multipliers"][i])
        check(f"S1 KKT multiplier {i + 1}", multiplier > ball(threshold))

    eta_target = one(r"(\d+\.\d+)&<\\etaw<(\d+\.\d+)\.", supplement)
    check("S1 printed eta_width", enclosed(eta, eta_target))
    endpoints = one(
        r"\\frac\{(\d+)\}\{10\^\{23\}\}\s*<\\Cterm\+\\etaw<\s*\\frac\{(\d+)\}\{10\^\{23\}\}",
        supplement,
    )
    target = [Fraction(int(n), 10**23) for n in endpoints]
    check(
        "S1 theorem strict_target",
        list(map(Fraction, cert["strict_target"])) == target
        and enclosed(lower, target),
    )
    abstract = one(r"(\d+\.\d+)<\\Cterm\+\\etaw\s*<(\d+\.\d+)\.", supplement)
    proposition = one(
        r"\s(\.\d+)\s*< C_\{\\rm term\}\+\\eta_\{\\rm width\}\s*< (\.\d+)\.", main
    )
    check(
        "S1 abstract and main proposition strict enclosure",
        all(enclosed(lower, t) for t in (abstract, proposition)),
    )
    heading = one(r"coefficient \$(\d+\.\d+)<C_\\ast", main)
    macro = one(r"\\newcommand\{\\CstarLower\}\{(\d+\.\d+)\}", numbers)
    unit = Fraction(1, 10 ** len(macro.split(".")[1]))
    check(
        "numbers.tex CstarLower rounded down",
        ball(macro) < lower < ball(Fraction(macro) + unit),
    )
    check(
        "main abstract lower endpoint",
        ball(heading) < lower and Fraction(heading) == Fraction(macro),
    )
    check("main lower endpoint excludes 1/8", lower > ball(Fraction(1, 8)))
    return checks
