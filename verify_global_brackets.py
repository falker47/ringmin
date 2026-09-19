#!/usr/bin/env python3
"""Complete verifier of the twelve supplied Ringmin global brackets.

No imports from the packet or Ringmin. Stdlib only. Angles are independently
checked using cos(theta)=1-2q and outward cosine-series enclosures at 224 bits.
Adapted from the separately preserved 2026-09-17 reviewer_verify.py. The lower
computation uses forward Held-Karp paths (reverse of completion paths); geometry
uses exact Cartesian coordinates and cross-product polar ordering. See
research/GLOBAL_BRACKET_CERTIFICATE.md for the proof and provenance boundary.
"""

from __future__ import annotations
import argparse
import ast
import hashlib
import itertools
import json
import math
import platform
import re
import sys
import time
from fractions import Fraction as F
from functools import cmp_to_key
from pathlib import Path

B = 1 << 224
S = 1 << 128
ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT / "reproducibility/global_brackets/originals"
PAYLOAD_SHA256 = "6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0"
GENERATOR_SHA256 = "e785b43bd2a24cf74d807479b5719e5f1b5e762027e41c4a69af07a655531549"
INPUT_CASES_SHA256 = "cb24657c443010573cf85a54f9991e4288b46054094fd3069fe3d917a63a56f0"
WINDOWS_SHA256 = "96bdf9b53977724f1b8c0640425365bf32897fd4415104f17bfd1afbfa52c693"
MODEL = "outer circles of radii 1..n externally tangent to central circle, pairwise interior-disjoint"
ENDPOINTS = [
    (3, "0.26086956521", "0.26086956522", 1),
    (4, "0.84445358956", "0.84445358957", 1),
    (5, "1.69549408120", "1.69549408121", 1),
    (6, "2.79491951889", "2.79491951890", 1),
    (7, "4.15318955374", "4.15318955375", 1),
    (8, "5.76779428458", "5.76779428459", 1),
    (9, "7.72672655261", "7.72672655262", 1),
    (10, "9.97990738586", "9.97990738587", 4),
    (11, "12.48872048718", "12.48872048719", 6),
    (12, "15.25887043044", "15.25887043045", 9),
    (13, "18.31756304721", "18.31756304722", 10),
    (14, "21.66539518221", "21.66539518222", 11),
]


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def sha(x):
    return hashlib.sha256(x).hexdigest()


def canonical(x):
    return json.dumps(
        x, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("ascii")


def unique(pairs):
    out = {}
    for k, v in pairs:
        need(k not in out, "duplicate JSON key: " + k)
        out[k] = v
    return out


def read(path):
    def bad(x):
        raise ValueError("nonfinite JSON: " + x)

    return json.loads(
        Path(path).read_bytes(), object_pairs_hook=unique, parse_constant=bad
    )


def ceildiv(a, b):
    need(b > 0, "nonpositive denominator")
    return -((-a) // b)


def sint(x):
    need(isinstance(x, str) and str(int(x)) == x, "noncanonical scaled integer")
    return int(x)


def fields(obj, names, where):
    need(
        type(obj) is dict and set(obj) == set(names.split()), "schema fields: " + where
    )


def decimal(x):
    need(
        type(x) is str and re.fullmatch(r"(0|[1-9][0-9]*)\.[0-9]+", x),
        "exact decimal string required",
    )
    return F(x)


def schema(report):
    """Reject malformed proof objects before arithmetic; PASS labels are not evidence."""
    need(type(report) is dict, "report object")
    need(
        report.get("report_type") == "fresh_global_interval_certificate_candidate",
        "report type",
    )
    c = report["certificate"]
    fields(
        c,
        "model version scale_denominator tau_lower_scaled tau_upper_scaled placement_padding_scaled input_cases_sha256 cases",
        "certificate",
    )
    need(c["model"] == MODEL and c["version"] == "0.1.0", "model/version")
    need(
        type(c["input_cases_sha256"]) is str
        and re.fullmatch("[0-9a-f]{64}", c["input_cases_sha256"]),
        "input digest syntax",
    )
    need(type(c["cases"]) is list and len(c["cases"]) == 12, "case coverage")
    for row in c["cases"]:
        fields(
            row,
            "n L U bracket_width lower_bound upper_witnesses angle_intervals_scaled candidate_claim status",
            "case",
        )
        need(type(row["n"]) is int and 3 <= row["n"] <= 14, "case n domain")
        decimal(row["L"])
        decimal(row["U"])
        need(
            row["bracket_width"] == "1/100000000000"
            and row["candidate_claim"] == "L < global_infimum_radius <= U",
            "bracket claim schema",
        )
        need(type(row["lower_bound"]) is dict, "lower proof object")
        need(type(row["angle_intervals_scaled"]) is list, "pair table list")
        for rec in row["angle_intervals_scaled"]:
            fields(rec, "a b L_lower L_upper U_lower U_upper", "angle")
            need(type(rec["a"]) is int and type(rec["b"]) is int, "pair label types")
        need(
            type(row["upper_witnesses"]) is list and row["upper_witnesses"],
            "MISSING existential upper witness n=" + str(row["n"]),
        )
        for w in row["upper_witnesses"]:
            fields(
                w,
                "order positions_scaled_integers minimum_verified_all_pairs_slack_scaled pair_constraints_checked status exact_cartesian_check",
                "witness",
            )
            need(
                type(w["order"]) is list
                and type(w["positions_scaled_integers"]) is list,
                "witness lists",
            )
            need(type(w["pair_constraints_checked"]) is int, "pair count type")
            d = w["exact_cartesian_check"]
            fields(
                d,
                "status stereographic_parameters central_tangencies_checked outer_pairs_checked minimum_squared_distance_gap",
                "Cartesian witness",
            )
            need(
                type(d["central_tangencies_checked"]) is int
                and type(d["outer_pairs_checked"]) is int,
                "Cartesian count types",
            )
            need(type(d["stereographic_parameters"]) is list, "parameter list")
            for par in d["stereographic_parameters"]:
                fields(par, "numerator denominator", "parameter")
            fields(
                d["minimum_squared_distance_gap"],
                "numerator denominator",
                "distance gap",
            )


def cos_bounds(x: F, terms: int = 112):
    """Bounds B*cos(x) using alternating series, exact outward integer arithmetic.

    The first omitted absolute term bounds the remainder: the tail terms are
    decreasing after the chosen cutoff. No claim that early terms decrease is
    made (for x>sqrt(2) they need not). All operations prior to cutoff retain
    independent lower/upper bounds on each positive absolute term.
    """
    need(isinstance(x, F) and 0 <= x <= 4 and terms >= 4, "cos domain/cutoff")
    xx = x * x
    a, d = xx.numerator, xx.denominator
    low = high = B
    lo = hi = 0
    for k in range(terms):
        if k % 2:
            lo -= high
            hi -= low
        else:
            lo += low
            hi += high
        den = d * (2 * k + 1) * (2 * k + 2)
        low = low * a // den
        high = ceildiv(high * a, den)
    need(xx < (2 * terms + 1) * (2 * terms + 2), "cos tail must decrease")
    if terms % 2:
        lo -= high
    else:
        hi += high
    need(lo <= hi, "cos endpoint ordering")
    return lo, hi


def verify_tau(lo, hi):
    need(6 * S < lo < hi < 7 * S, "tau location")
    # On (0,pi), cos is strictly decreasing. pi>3 is a standard elementary
    # bound. The zero enclosed in (1.5,1.75) is pi/2; therefore tau=2*pi.
    need(cos_bounds(F(lo, 4 * S))[0] > 0, "tau lower fails independent cosine test")
    need(cos_bounds(F(hi, 4 * S))[1] < 0, "tau upper fails independent cosine test")


def verify_angle(q, lo, hi):
    need(0 < q < F(9, 10), "angle q domain")
    need(0 < lo <= hi < 3 * S and hi - lo <= 2, "angle interval schema/domain")
    target = 1 - 2 * q
    # Both endpoints are in (0,3), where cos is decreasing since pi>3.
    need(F(cos_bounds(F(lo, S))[0], B) > target, "false angular LOWER endpoint")
    need(F(cos_bounds(F(hi, S))[1], B) < target, "false angular UPPER endpoint")


def norm_order(seq):
    seq = tuple(seq)
    k = seq.index(max(seq))
    a = seq[k:] + seq[:k]
    return min(a, a[:1] + a[:0:-1])


def cycle_cost(seq, W):
    return sum(W[a][b] for a, b in zip(seq, seq[1:] + seq[:1]))


def forward_dp(vertices, anchor, W):
    """D[(mask,j)] is the minimum path anchor -> vertices(mask), ending in j."""
    m = len(vertices)
    D = {}
    need(m > 0 and len(set(vertices)) == m and anchor not in vertices, "DP vertices")
    for mask in range(1, 1 << m):
        members = [j for j in range(m) if mask >> j & 1]
        for j in members:
            prev = mask ^ (1 << j)
            D[mask, j] = (
                W[anchor][vertices[j]]
                if not prev
                else min(
                    D[prev, k] + W[vertices[k]][vertices[j]] for k in members if k != j
                )
            )
    full = (1 << m) - 1
    return D, min(D[full, j] + W[vertices[j]][anchor] for j in range(m))


def audit_lower(n, W, T):
    need(type(n) is int and 3 <= n <= 14, "lower n domain")
    expected = math.factorial(n - 1) // 2
    counts = [0, 0, 0]
    margins = []
    witness_hash = hashlib.sha256()
    normal = set()
    raw_noncanonical = 0

    def inspect(seq):
        nonlocal raw_noncanonical
        seq = tuple(seq)
        found = False
        for k in range(3):
            subset = tuple(v for v in seq if v > k)
            if len(subset) >= 3:
                gap = cycle_cost(subset, W) - T
                if gap > 0:
                    counts[k] += 1
                    margins.append(gap)
                    witness_hash.update(bytes(seq) + bytes([k]))
                    found = True
                    break
        need(found, "UNPROVEN lower order " + repr(seq))
        can = norm_order(seq)
        need(can not in normal, "duplicate explicit cyclic-order class")
        normal.add(can)
        raw_noncanonical += int(seq != can)

    if n <= 9:
        for p in itertools.permutations(range(1, n)):
            if p < p[::-1]:
                inspect((n,) + p)
        need(len(normal) == expected, "small exhaustive coverage")
        return dict(
            canonical_orders_covered=expected,
            explicit_full_orders_checked=len(normal),
            witness_counts_full_remove1_remove12=counts,
            minimum_explicit_angular_margin_scaled=str(min(margins)),
            explicit_order_witness_sha256=witness_hash.hexdigest(),
            raw_noncanonical_explicit_tuples=raw_noncanonical,
        )
    stats = skeleton_cover(n, W, T, inspect)
    need(
        len(normal) == stats["explicit_full_orders_checked"], "unique insertion classes"
    )
    return dict(
        canonical_orders_covered=expected,
        explicit_full_orders_checked=len(normal),
        witness_counts_full_remove1_remove12=counts,
        minimum_explicit_angular_margin_scaled=str(min(margins)) if margins else None,
        explicit_order_witness_sha256=witness_hash.hexdigest(),
        raw_noncanonical_explicit_tuples=raw_noncanonical,
        **{k: v for k, v in stats.items() if k != "explicit_full_orders_checked"},
    )


def skeleton_cover(n, W, T, inspect):
    """Partition all skeletons; send every retained insertion to inspect.

    The callback must prove each explicit full order in audit_lower. Keeping the
    traversal separate also permits exact small set oracles without pretending
    that a structural test proves geometric infeasibility.
    """
    need(type(n) is int and 4 <= n <= 14, "skeleton n domain")
    vals = tuple(range(2, n))
    m = len(vals)
    full = (1 << m) - 1
    need(
        all(W[a][b] == W[b][a] for a in range(1, n + 1) for b in range(1, n + 1)),
        "reverse DP requires symmetric weights",
    )
    D, root = forward_dp(vals, n, W)
    # Reversal: a completion v -> M -> anchor has cost D[M union {v},v].
    dp_stream = [
        [mask, j, str(D[mask | (1 << j), j])]
        for mask in range(1 << m)
        for j in range(m)
        if not mask >> j & 1
    ]
    stack = [((n,), full, 0, None)]
    nodes = prunes = pruned = kept = reversed_leaves = explicit = 0
    prune_margins = []
    pruning_hash = hashlib.sha256()
    while stack:
        seq, mask, cost, j = stack.pop()
        nodes += 1
        bound = root if j is None else cost + D[mask | (1 << j), j]
        if bound > T:
            prunes += 1
            pruned += math.factorial(mask.bit_count())
            prune_margins.append(bound - T)
            pruning_hash.update(b"P" + bytes(seq) + b":" + str(mask).encode() + b";")
        elif not mask:
            need(bound == cost + W[seq[-1]][n], "closing edge mismatch")
            if seq != norm_order(seq):
                reversed_leaves += 1
                continue
            kept += 1
            pruning_hash.update(b"E" + bytes(seq) + b";")
            for gap in range(len(seq)):
                p = gap + 1
                inspect(seq[:p] + (1,) + seq[p:])
                explicit += 1
        else:
            for k in range(m - 1, -1, -1):
                if mask >> k & 1:
                    v = vals[k]
                    stack.append((seq + (v,), mask ^ (1 << k), cost + W[seq[-1]][v], k))
    need(
        reversed_leaves == kept and pruned + 2 * kept == math.factorial(n - 2),
        "oriented skeleton coverage",
    )
    need(pruned % 2 == 0 and explicit == (n - 1) * kept, "reflection / insertion count")
    need(
        pruned * (n - 1) // 2 + explicit == math.factorial(n - 1) // 2, "full coverage"
    )
    return dict(
        explicit_full_orders_checked=explicit,
        dp_states=len(D) + 1,
        dp_root_cost_minus_tau_hi_scaled=str(root - T),
        dp_table_sha256=sha(canonical(dp_stream)),
        nodes=nodes,
        pruned_subtrees=prunes,
        pruned_oriented_completions=pruned,
        canonical_skeletons_expanded=kept,
        reversed_leaves_omitted=reversed_leaves,
        full_canonical_orders_covered_by_pruning=pruned * (n - 1) // 2,
        minimum_prune_angular_margin_scaled=str(min(prune_margins))
        if prune_margins
        else None,
        pruning_and_skeleton_stream_sha256=pruning_hash.hexdigest(),
    )


def compare_polar(a, b):
    def half(p):
        return 0 if (p[1] > 0 or p[1] == 0 and p[0] > 0) else 1

    ha, hb = half(a), half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    cross = a[0] * b[1] - a[1] * b[0]
    return -1 if cross > 0 else 1 if cross < 0 else 0


def audit_geometry(row, HU, tau_lo, pad):
    n = row["n"]
    R = F(row["U"])
    ws = row["upper_witnesses"]
    need(
        isinstance(ws, list) and len(ws) > 0,
        "MISSING existential upper witness n=" + str(n),
    )
    pairs = tangent = angular = 0
    minima = []
    seen = set()
    for w in ws:
        order = w["order"]
        need(
            len(order) == n
            and all(type(v) is int for v in order)
            and set(order) == set(range(1, n + 1)),
            "witness radius set",
        )
        co = norm_order(order)
        need(co not in seen, "duplicate witness order")
        seen.add(co)
        x = [sint(v) for v in w["positions_scaled_integers"]]
        need(
            len(x) == n
            and x[0] == 0
            and all(a < b for a, b in zip(x, x[1:]))
            and x[-1] < tau_lo,
            "angular ordering",
        )
        ag = []
        for i, j in itertools.combinations(range(n), 2):
            d = x[j] - x[i]
            h = HU[order[i]][order[j]]
            ag.extend([d - h, tau_lo - d - h])
            angular += 2
        need(
            min(ag) >= pad
            and sint(w["minimum_verified_all_pairs_slack_scaled"]) == min(ag),
            "angular slack",
        )
        need(w["pair_constraints_checked"] == n * (n - 1), "angular pair count")
        data = w["exact_cartesian_check"]
        pars = data["stereographic_parameters"]
        need(len(pars) == n, "stereographic parameter count")
        centers = []
        directions = []
        for r, p in zip(order, pars):
            num, den = sint(p["numerator"]), sint(p["denominator"])
            need(den > 0, "parameter denominator")
            t = F(num, den)
            dx = (1 - t * t) / (1 + t * t)
            dy = 2 * t / (1 + t * t)
            cx = (R + r) * dx
            cy = (R + r) * dy
            need(cx * cx + cy * cy == (R + r) ** 2, "central tangency")
            tangent += 1
            centers.append((cx, cy))
            directions.append((dx, dy))
        need(directions[0] == (1, 0), "Cartesian anchor")
        need(
            sorted(directions, key=cmp_to_key(compare_polar)) == directions
            and len(set(directions)) == n,
            "Cartesian polar order",
        )
        gaps = []
        for i, j in itertools.combinations(range(n), 2):
            dx = centers[i][0] - centers[j][0]
            dy = centers[i][1] - centers[j][1]
            gap = dx * dx + dy * dy - (order[i] + order[j]) ** 2
            need(gap > 0, "Cartesian overlap")
            gaps.append(gap)
            pairs += 1
        mn = data["minimum_squared_distance_gap"]
        den = sint(mn["denominator"])
        need(den > 0, "distance gap denominator")
        want = F(sint(mn["numerator"]), den)
        need(min(gaps) == want, "stored Cartesian minimum")
        need(
            data["central_tangencies_checked"] == n
            and data["outer_pairs_checked"] == n * (n - 1) // 2,
            "Cartesian count metadata",
        )
        minima.append(str(want))
    return dict(
        witnesses=len(ws),
        central_tangencies=tangent,
        outer_pairs=pairs,
        angular_inequalities=angular,
        minimum_squared_gap_per_witness=minima,
    )


def verify(report):
    """Check mathematical content and computed trace metadata, without historical pins.

    input_cases_sha256 and report provenance are explicitly unchecked here;
    verify_pinned_inputs supplies that separate content-binding obligation.
    """
    schema(report)
    c = report["certificate"]
    need(sha(canonical(c)) == report["certificate_sha256"], "certificate digest")
    need(sint(c["scale_denominator"]) == S, "scale denominator")
    tau_lo, tau_hi = sint(c["tau_lower_scaled"]), sint(c["tau_upper_scaled"])
    verify_tau(tau_lo, tau_hi)
    pad = sint(c["placement_padding_scaled"])
    need(pad == ceildiv(S, 10**16), "positive constructive padding")
    need(
        [r["n"] for r in c["cases"]] == list(range(3, 15))
        and all(type(r["n"]) is int for r in c["cases"]),
        "case coverage",
    )
    rows = []
    total_angles = 0
    for row in c["cases"]:
        n = row["n"]
        L, U = decimal(row["L"]), decimal(row["U"])
        need(0 < L < U and U - L == F(1, 10**11), "bracket width")
        recs = row["angle_intervals_scaled"]
        want_pairs = set(itertools.combinations(range(1, n + 1), 2))
        need(
            len(recs) == len(want_pairs)
            and {(r["a"], r["b"]) for r in recs} == want_pairs,
            "pair table completeness",
        )
        WL = [[0] * (n + 1) for _ in range(n + 1)]
        HU = [[0] * (n + 1) for _ in range(n + 1)]
        deriv = []
        for r in recs:
            a, b = r["a"], r["b"]
            need(type(a) is int and type(b) is int, "pair labels")
            for key, Q in [("L", L), ("U", U)]:
                q = F(a * b) / ((Q + a) * (Q + b))
                lo, hi = sint(r[key + "_lower"]), sint(r[key + "_upper"])
                verify_angle(q, lo, hi)
                total_angles += 1
                if key == "L":
                    WL[a][b] = WL[b][a] = lo
                    z = q / (1 - q)
                    deriv.append(max(F(1), z) * (1 / (L + a) + 1 / (L + b)))
                else:
                    HU[a][b] = HU[b][a] = hi
        # Check existence before expensive full lower computation.
        geo = audit_geometry(row, HU, tau_lo, pad)
        lower = audit_lower(n, WL, tau_hi)
        verify_lower_metadata(row, lower)
        m = min(
            int(lower[k])
            for k in (
                "minimum_explicit_angular_margin_scaled",
                "minimum_prune_angular_margin_scaled",
            )
            if lower.get(k) is not None
        )
        need(m > 0, "strict lower margin")
        # For Q>=L, |phi_ab'(Q)| <= max(1,q/(1-q))*(1/(L+a)+1/(L+b)).
        # Every selected cycle uses at most n edges. This gives a constructive
        # positive buffer beyond L, without assuming attainment of the infimum.
        eps = F(m, 2 * S) / (n * max(deriv))
        need(0 < eps < U - L, "strictness buffer inconsistent with U")
        rows.append(
            dict(
                n=n,
                L=str(L),
                U=str(U),
                lower=lower,
                geometry=geo,
                strict_lower_radius_buffer=str(eps),
                minimum_angular_margin_scaled=str(m),
            )
        )
    return dict(
        status="PASS_GLOBAL_BRACKETS",
        certificate_sha256=report["certificate_sha256"],
        angles_verified_by_cosine=total_angles,
        tau_verified_by_cosine_zero=True,
        witnesses=sum(r["geometry"]["witnesses"] for r in rows),
        central_tangencies=sum(r["geometry"]["central_tangencies"] for r in rows),
        outer_pairs=sum(r["geometry"]["outer_pairs"] for r in rows),
        angular_inequalities=sum(r["geometry"]["angular_inequalities"] for r in rows),
        explicit_order_classes=sum(
            r["lower"]["explicit_full_orders_checked"] for r in rows
        ),
        all_order_classes_covered=sum(
            r["lower"]["canonical_orders_covered"] for r in rows
        ),
        cases=rows,
    )


def verify_lower_metadata(row, lower):
    expected = {
        k: v for k, v in lower.items() if k != "raw_noncanonical_explicit_tuples"
    }
    expected["status"] = "PASS_COMPLETE_LOWER_BOUND"
    expected["method"] = (
        "fresh_direct_canonical_enumeration"
        if row["n"] <= 9
        else "fresh_integer_completion_pruning_and_insertion"
    )
    if row["n"] >= 10:
        expected["skeleton_vertices"] = list(range(2, row["n"] + 1))
    # Serialization distinguishes bool/float/int, unlike Python equality.
    need(
        canonical(row["lower_bound"]) == canonical(expected),
        "lower metadata n=" + str(row["n"]) + " (including DP/pruning digests)",
    )


def verify_pinned_inputs(report, originals=ORIGINALS):
    """Identify input bytes and CASES as data; never execute the generator."""
    source = (originals / "source/ringmin_global_interval_replay.py").read_bytes()
    need(sha(source) == GENERATOR_SHA256, "original generator bytes")
    tree = ast.parse(source)
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "CASES" for t in node.targets)
    ]
    need(len(assignments) == 1, "unique CASES assignment")
    value = assignments[0].value
    need(
        isinstance(value, ast.Call)
        and isinstance(value.func, ast.Attribute)
        and isinstance(value.func.value, ast.Name)
        and value.func.value.id == "json"
        and value.func.attr == "loads"
        and len(value.args) == 1
        and not value.keywords,
        "CASES literal schema",
    )
    cases = json.loads(ast.literal_eval(value.args[0]), object_pairs_hook=unique)
    c = report["certificate"]
    need(
        sha(canonical(cases)) == INPUT_CASES_SHA256 == c["input_cases_sha256"],
        "CASES input digest binding",
    )
    need(report["script_sha256"] == GENERATOR_SHA256, "declared script digest binding")
    need(len(cases) == len(c["cases"]) == 12, "pinned case count")
    for case, row, ep in zip(cases, c["cases"], ENDPOINTS):
        need(
            (row["n"], decimal(row["L"]), decimal(row["U"]))
            == (ep[0], F(ep[1]), F(ep[2])),
            "pinned endpoints",
        )
        need(
            (case["n"], decimal(case["L"]), decimal(case["U"]), case["orders"])
            == (
                row["n"],
                decimal(row["L"]),
                decimal(row["U"]),
                [w["order"] for w in row["upper_witnesses"]],
            ),
            "CASES endpoints/orders binding",
        )
        need(len(row["upper_witnesses"]) == ep[3], "pinned witness count per row")
    windows_path = (
        originals / "source/global_interval_replay_20260917T101809Z_3399172f.json"
    )
    need(sha(windows_path.read_bytes()) == WINDOWS_SHA256, "original Windows bytes")
    windows = read(windows_path)
    candidate = read(originals / "source/ringmin_global_interval_candidate.json")
    need(
        sha(canonical(c)) == report["certificate_sha256"] == PAYLOAD_SHA256,
        "pinned certificate digest",
    )
    need(
        canonical(c)
        == canonical(windows["certificate"])
        == canonical(candidate["certificate"]),
        "original payload correspondence",
    )


def verify_archive():
    manifest = read(ORIGINALS.parent / "manifest.json")
    seen = set()
    for rec in manifest["files"]:
        rel = Path(rec["path"])
        need(
            not rel.is_absolute() and ".." not in rel.parts and rec["path"] not in seen,
            "archive path",
        )
        seen.add(rec["path"])
        data = (ORIGINALS / rel).read_bytes()
        need(
            len(data) == rec["bytes"] and sha(data) == rec["sha256"],
            "archive bytes: " + rec["path"],
        )
    actual = {
        p.relative_to(ORIGINALS).as_posix() for p in ORIGINALS.rglob("*") if p.is_file()
    }
    need(actual == seen, "archive member set")
    return len(seen)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ORIGINALS / "source/ringmin_global_interval_candidate.json",
    )
    parser.add_argument(
        "--mathematical-only",
        action="store_true",
        help="verify all twelve brackets without asserting original payload/input identity",
    )
    parser.add_argument(
        "--output", type=Path, help="create a new JSON result; refuse overwrites"
    )
    args = parser.parse_args(argv)
    start = time.perf_counter()
    try:
        report = read(args.certificate)
        result = verify(report)
        if args.mathematical_only:
            result["pinned_input_verification"] = "NOT_CHECKED"
        else:
            verify_pinned_inputs(report)
            result["preserved_original_files"] = verify_archive()
            result["pinned_input_verification"] = "PASS"
        result.update(
            python=sys.version,
            platform=platform.platform(),
            seconds=time.perf_counter() - start,
            verifier_sha256=sha(Path(__file__).read_bytes()),
            unchecked_metadata=[
                "Historical runtime/platform/timestamps, regression labels, input frontier blob provenance and generation-execution authenticity."
            ]
            + (
                [
                    "input_cases_sha256 and script_sha256 bindings, original payload identity."
                ]
                if args.mathematical_only
                else []
            ),
        )
        if args.output:
            with args.output.open("x", encoding="utf-8", newline="\n") as f:
                json.dump(result, f, indent=2, allow_nan=False)
                f.write("\n")
        print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))
        return 0
    except (
        ValueError,
        KeyError,
        TypeError,
        IndexError,
        OSError,
        ZeroDivisionError,
    ) as exc:
        print("FAIL_GLOBAL_BRACKETS: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
