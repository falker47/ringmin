#!/usr/bin/env python3
"""Bounded NUMERICAL DIAGNOSTIC, never an exact radius-8 onset certificate.

Run --write to save diagnostic.json, or --check to recompute it byte for byte.
No production imports, warm starts, parameter-range overrides, or randomness.
The two independent computational paths share the mpmath library.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

import mpmath


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
K, START, STOP = 8, 33, 46
PRECISIONS = (90, 150)
GUARD = "1e-55"
BASE_HEAD = "3eb1ec321e2f5a334826ee70c2258f82b9703f66"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def domain(n):
    require(type(n) is int and START <= n <= STOP, "outside fixed n=33..46")


def tour_edges(tour):
    return sorted(tuple(sorted((a, b))) for a, b in zip(tour, tour[1:] + tour[:1]))


def rank_tour(n):
    """Construct the A_N, reverse(B_N), N rank representative, then shift."""
    domain(n)
    size = n - K + 1
    middle = (size + 1) // 2
    arms = []
    for start in (1, 2):
        arm = []
        for j in range(size):
            low, high = start + 2 * j, size - start - 2 * j
            if low <= middle:
                arm.append(low)
            if high > middle:
                arm.append(high)
        arms.append(arm)
    return [K + rank - 1 for rank in arms[0] + arms[1][::-1] + [size]]


def parity_edges(n):
    """Separate direct edge-set construction from fixed-k section 1."""
    domain(n)
    size = n - K + 1
    half = size // 2
    edges = [(K, n)]
    if size % 2 == 0:
        edges.append((K + half - 1, K + half))
        first_stop, second_stop = K + half - 1, K + half
    else:
        first_stop, second_stop = K + half, K + half + 1
    edges.extend((i, n + K - 1 - i) for i in range(K, first_stop))
    edges.extend((i, n + K + 1 - i) for i in range(K + 1, second_stop))
    return sorted(tuple(sorted(edge)) for edge in edges)


def audit_edges(n, tour, edges):
    domain(n)
    size = n - K + 1
    require(sorted(tour) == list(range(K, n + 1)), "invalid permutation")
    require(len(edges) == len(set(edges)) == size, "edge count/duplicates")
    require(all(K <= a < b <= n for a, b in edges), "edge endpoint/domain")
    require(Counter(v for edge in edges for v in edge) ==
            Counter({v: 2 for v in range(K, n + 1)}), "vertex degrees")
    require(tour_edges(tour) == edges, "rank/parity edge disagreement")
    require((K, n) in edges and (K, n - 1) in edges, "seam edges missing")
    for shift in range(size):
        rotated = tour[shift:] + tour[:shift]
        require(tour_edges(rotated) == edges, "rotation disagreement")
        require(tour_edges(rotated[::-1]) == edges, "reflection disagreement")


def closure(ctx, edges, radius, method):
    if radius == 0:
        return (len(edges) - 2) * ctx.pi
    if method == "A":
        terms = [2 * ctx.asin(ctx.sqrt(a * b / ((radius + a) * (radius + b))))
                 for a, b in edges]
        return ctx.fsum(terms) - 2 * ctx.pi
    # asin(sqrt(ab/((R+a)(R+b)))) = atan(sqrt(ab/(R*(R+a+b))))
    return sum((2 * ctx.atan(ctx.sqrt(a * b / (radius * (radius + a + b))))
                for a, b in reversed(edges)), ctx.mpf(0)) - 2 * ctx.pi


def threshold(ctx, n, method):
    if method == "A":
        curvature = (ctx.mpf(1) / K + ctx.mpf(1) / n + ctx.mpf(1) / (n - 1)
                     - 2 * ctx.sqrt(ctx.mpf(2 * n + K - 1) / (K * n * (n - 1))))
        require(curvature > 0, "nonpositive Descartes curvature")
        return 1 / curvature
    # Exact rational coefficients; conjugate of the same physical minus root.
    a = Fraction(1, K) + Fraction(1, n) + Fraction(1, n - 1)
    b = Fraction(2 * n + K - 1, K * n * (n - 1))
    denominator = a * a - 4 * b
    require(denominator > 0, "nonpositive conjugate denominator")
    lift = lambda x: ctx.mpf(x.numerator) / x.denominator
    return (lift(a) + 2 * ctx.sqrt(lift(b))) / lift(denominator)


def calculate(n, method, dps):
    domain(n)
    ctx = mpmath.mp.clone()
    ctx.dps = dps
    # Each calculation reconstructs its own inputs; B consumes no A result.
    edges = tour_edges(rank_tour(n)) if method == "A" else parity_edges(n)
    f = lambda radius: closure(ctx, edges, radius, method)
    lo, hi = ctx.mpf(0), ctx.mpf(n * n)
    require(f(lo) > 0 and f(hi) < 0, "initial root bracket")
    tolerance = ctx.power(10, -(dps - 15))
    if method == "A":
        for _ in range(4 * dps):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
            if hi - lo < tolerance:
                break
        require(hi - lo < tolerance, "bisection iteration limit")
        radius = (lo + hi) / 2
    else:
        radius = ctx.findroot(f, (lo, hi), solver="ridder", tol=tolerance,
                              maxsteps=4 * dps, verify=True)
    target = threshold(ctx, n, method)
    pad = ctx.power(10, -(dps - 30))
    residual = f(radius)
    left, right = f(radius - pad), f(radius + pad)
    require(radius > pad and target > 0, "positive radius/threshold")
    require(abs(residual) < ctx.power(10, -(dps - 25)), "root residual")
    require(left > 0 and right < 0, "local numerical root bracket")
    alpha = ctx.mpf(1) / n + ctx.mpf(1) / (n - 1)
    beta = ctx.mpf(1) / (n * (n - 1))
    physical = 1 / target + alpha + 2 * ctx.sqrt(alpha / target + beta) - ctx.mpf(1) / K
    require(abs(physical) < ctx.power(10, -(dps - 20)), "physical Descartes equation")
    values = dict(R=radius, T=target, D=radius - target, closure_residual=residual,
                  radius_half_width=pad, closure_at_R_minus_pad=left,
                  closure_at_R_plus_pad=right, physical_threshold_residual=physical)
    return {key: ctx.nstr(value, dps - 10) for key, value in values.items()}


def common_separator(ctx, before, after):
    guard = ctx.mpf(GUARD)
    lowers = [ctx.mpf(before[m]["R"]) for m in ("A", "B")]
    lowers += [ctx.mpf(after[m]["T"]) for m in ("A", "B")]
    uppers = [ctx.mpf(before[m]["T"]) for m in ("A", "B")]
    uppers += [ctx.mpf(after[m]["R"]) for m in ("A", "B")]
    lower, upper = max(lowers) + guard, min(uppers) - guard
    result = dict(guarded_lower=ctx.nstr(lower, 75), guarded_upper=ctx.nstr(upper, 75),
                  denominator_limit=1000, fraction=None)
    for denominator in range(1, 1001):
        numerator = int(ctx.floor(lower * denominator)) + 1
        value = ctx.mpf(numerator) / denominator
        if lower < value < upper:
            rational = Fraction(numerator, denominator)
            result["fraction"] = str(rational)
            result["margins"] = {}
            for method in ("A", "B"):
                b, a = before[method], after[method]
                margins = dict(q_minus_R_before=value - ctx.mpf(b["R"]),
                               T_before_minus_q=ctx.mpf(b["T"]) - value,
                               q_minus_T_after=value - ctx.mpf(a["T"]),
                               R_after_minus_q=ctx.mpf(a["R"]) - value)
                require(min(margins.values()) > guard, "separator margins")
                result["margins"][method] = {k: ctx.nstr(v, 65) for k, v in margins.items()}
            break
    return result


def build_report():
    ctx = mpmath.mp.clone()
    ctx.dps = 170
    rows = []
    for n in range(START, STOP + 1):
        tour, edges = rank_tour(n), parity_edges(n)
        audit_edges(n, tour, edges)
        rows.append(dict(n=n, size=n - K + 1, tour=tour, edges=edges))
    # Complete A before starting B. Separate contexts and algorithms per (n, run).
    for method, dps in zip(("A", "B"), PRECISIONS):
        for row in rows:
            row[method] = calculate(row["n"], method, dps)
    for row in rows:
        deltas = {key: abs(ctx.mpf(row["A"][key]) - ctx.mpf(row["B"][key]))
                  for key in ("R", "T", "D")}
        require(max(deltas.values()) < ctx.mpf(GUARD), "precision instability")
        signs = [int(ctx.sign(ctx.mpf(row[m]["D"]))) for m in ("A", "B")]
        require(signs[0] == signs[1] and signs[0] != 0, "unstable/zero sign")
        require(min(abs(ctx.mpf(row[m]["D"])) for m in ("A", "B")) > ctx.mpf(GUARD),
                "sign inside diagnostic guard")
        row["sign"] = signs[0]
        row["absolute_run_differences"] = {k: ctx.nstr(v, 18) for k, v in deltas.items()}
    for before, after in zip(rows, rows[1:]):
        for method in ("A", "B"):
            for key, sign in (("R", 1), ("T", -1), ("D", 1)):
                require(sign * (ctx.mpf(after[method][key]) - ctx.mpf(before[method][key])) > 0,
                        "numerical monotonicity disagreement")
    crossings = [(a, b) for a, b in zip(rows, rows[1:]) if a["sign"] < 0 < b["sign"]]
    outcome = {"status": "INCONSISTENCY_NO_STABLE_CROSSING_IN_33_46",
               "endpoints": None, "candidate_only": None, "separator": None}
    if crossings:
        before, after = crossings[0]
        outcome = dict(status="STABLE_NUMERICAL_CROSSING", endpoints=[before["n"], after["n"]],
                       candidate_only=after["n"], separator=common_separator(ctx, before, after))
    sources = [Path(__file__).resolve(), ROOT / "research/FIXED_K_SUPNICK_SEAM.md",
               ROOT / "research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md"]
    return dict(schema=1, classification="NUMERICAL DIAGNOSTIC", task_base_head=BASE_HEAD,
                python=platform.python_version(), mpmath=mpmath.__version__,
                source_sha256={p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sources},
                parameters=dict(k=K, start=START, stop=STOP, precisions=list(PRECISIONS),
                                absolute_stability_guard=GUARD, random_seed=None),
                methods=dict(A="rank cyclic edges; asin/fsum; bisection; direct Descartes",
                             B="parity edges; atan/reverse sum; Ridder; rationalized Descartes",
                             independence="separate contexts, reconstruction, solve and threshold evaluation; shared mpmath"),
                rows=rows, outcome=outcome)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    payload = json.dumps(report, indent=2) + "\n"
    path = HERE / "diagnostic.json"
    if args.write:
        path.write_text(payload, encoding="utf-8", newline="\n")
    else:
        require(path.read_bytes() == payload.encode("utf-8"), "stored report differs from recomputation")
    print("NUMERICAL DIAGNOSTIC; k=8; n=33..46; dps=90,150; rows=14; independent paths=2")
    for row in report["rows"]:
        print(f'n={row["n"]} edges={row["size"]} sign={row["sign"]:+d} '
              f'R={row["B"]["R"][:24]} T={row["B"]["T"][:24]} D={row["B"]["D"][:25]}')
    print(json.dumps(report["outcome"], sort_keys=True))
    print("reproduction=BYTE_IDENTICAL" if args.check else "artifact=diagnostic.json")


if __name__ == "__main__":
    main()
