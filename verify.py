from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp

DIGITS = 50
mp.mp.dps = DIGITS
TAU = 2 * mp.pi

DIAG_TOL = mp.mpf("1e-35")
WITNESS_ANGLE_TOL = mp.mpf("1e-8")
CARTESIAN_TOL = mp.mpf("1e-8")
TIGHT_TOL = mp.mpf("1e-20")
FLOATING_SLACK = mp.mpf("1e-9")
DEFAULT_ETA = mp.mpf("1e-12")
PRUNE_GUARD = mp.mpf("1e-10")


def theta(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    x2 = (a * b) / ((R + a) * (R + b))
    value = 2 * mp.asin(mp.sqrt(x2))
    if not (0 < value < mp.pi):
        raise AssertionError(f"theta outside (0, pi): R={R}, a={a}, b={b}, theta={value}")
    return value


def theta_derivative(R: mp.mpf, a: mp.mpf, b: mp.mpf) -> mp.mpf:
    x = mp.sqrt((a * b) / ((R + a) * (R + b)))
    return -x * (1 / (R + a) + 1 / (R + b)) / mp.sqrt(1 - x * x)


def chain_sum(R: mp.mpf, order: tuple[int, ...]) -> mp.mpf:
    radii = tuple(mp.mpf(r) for r in order)
    return mp.fsum(theta(R, radii[i], radii[(i + 1) % len(radii)]) for i in range(len(radii)))


def chain_sum_derivative(R: mp.mpf, order: tuple[int, ...]) -> mp.mpf:
    radii = tuple(mp.mpf(r) for r in order)
    return mp.fsum(
        theta_derivative(R, radii[i], radii[(i + 1) % len(radii)])
        for i in range(len(radii))
    )


def chain_radius(order: tuple[int, ...]) -> mp.mpf:
    lo = mp.mpf("1e-9")
    hi = mp.mpf(4 * len(order) * len(order))
    target = TAU
    start = None
    if chain_sum(lo, order) <= target or chain_sum(hi, order) >= target:
        raise AssertionError(f"chain bracket failed for {order}")
    for _ in range(180):
        mid = (lo + hi) / 2
        if chain_sum(mid, order) > target:
            lo = mid
        else:
            hi = mid
    start = (lo + hi) / 2
    # A few Newton steps sharpen the root and make the returned value insensitive
    # to the fixed bisection iteration count.
    R = start
    for _ in range(5):
        residual = chain_sum(R, order) - target
        if abs(residual) < mp.mpf("1e-45"):
            return R
        R -= residual / chain_sum_derivative(R, order)
    return R


def induced_order(order: tuple[int, ...], removed: set[int]) -> tuple[int, ...]:
    return tuple(value for value in order if value not in removed)


def lower_bound(order: tuple[int, ...]) -> mp.mpf:
    values = [chain_radius(order)]
    without_1 = induced_order(order, {1})
    if len(without_1) >= 3:
        values.append(chain_radius(without_1))
    without_1_2 = induced_order(order, {1, 2})
    if len(without_1_2) >= 3:
        values.append(chain_radius(without_1_2))
    return max(values)


def closed_stn(
    order: tuple[int, ...],
    R: mp.mpf,
    slack_index: int | None = None,
    slack_pair: tuple[int, int] | None = None,
    slack: mp.mpf = mp.mpf("0"),
) -> list[list[mp.mpf]]:
    radii = tuple(mp.mpf(r) for r in order)
    n = len(radii)
    dist = [[mp.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = mp.mpf("0")
    for i in range(n):
        for j in range(i + 1, n):
            sep = theta(R, radii[i], radii[j])
            if slack_index is not None and (i == slack_index or j == slack_index):
                sep += slack
            if slack_pair is not None and (i, j) == slack_pair:
                sep += slack
            upper = TAU - sep
            lower = -sep
            if upper < -lower:
                dist[0][0] = -mp.inf
                return dist
            if upper < dist[i][j]:
                dist[i][j] = upper
            if lower < dist[j][i]:
                dist[j][i] = lower
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == mp.inf:
                continue
            for j in range(n):
                candidate = dik + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def feasible(order: tuple[int, ...], R: mp.mpf, **kwargs: object) -> bool:
    dist = closed_stn(order, R, **kwargs)
    return all(dist[i][i] >= -DIAG_TOL for i in range(len(order)))


def recover_positions(order: tuple[int, ...], R: mp.mpf) -> tuple[mp.mpf, ...]:
    dist = closed_stn(order, R)
    if any(dist[i][i] < -DIAG_TOL for i in range(len(order))):
        raise AssertionError("cannot recover positions from infeasible STN")
    positions = [dist[0][i] for i in range(len(order))]
    positions[0] = mp.mpf("0")
    return tuple(positions)


def pair_slacks(
    order: tuple[int, ...],
    R: mp.mpf,
    positions: tuple[mp.mpf, ...],
    i: int,
    j: int,
) -> tuple[mp.mpf, mp.mpf]:
    sep = theta(R, mp.mpf(order[i]), mp.mpf(order[j]))
    delta = positions[j] - positions[i]
    return delta - sep, (TAU - sep) - delta


def check_witness(
    payload: dict[str, Any],
    order: tuple[int, ...],
    R: mp.mpf,
    messages: list[str],
) -> bool:
    raw_positions = payload.get("positions")
    if not isinstance(raw_positions, list) or len(raw_positions) != len(order):
        messages.append("missing or malformed witness positions")
        return False
    positions = tuple(mp.mpf(str(value)) for value in raw_positions)
    ok = True
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            forward, wrap = pair_slacks(order, R, positions, i, j)
            if forward < -WITNESS_ANGLE_TOL or wrap < -WITNESS_ANGLE_TOL:
                ok = False
                messages.append(
                    f"witness angular violation {(order[i], order[j])}: "
                    f"forward={mp.nstr(forward, 12)} wrap={mp.nstr(wrap, 12)}"
                )

    centers: list[tuple[mp.mpf, mp.mpf]] = []
    for radius, phi in zip(order, positions, strict=True):
        rho = R + radius
        centers.append((rho * mp.cos(phi), rho * mp.sin(phi)))
    for i in range(len(order)):
        xi, yi = centers[i]
        for j in range(i + 1, len(order)):
            xj, yj = centers[j]
            dist = mp.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            required = mp.mpf(order[i] + order[j])
            if dist < required - CARTESIAN_TOL:
                ok = False
                messages.append(
                    f"witness cartesian violation {(order[i], order[j])}: "
                    f"dist={mp.nstr(dist, 12)} required={required}"
                )
    return ok


def verify_incumbent(root: Path, n: int) -> tuple[bool, list[str], dict[str, str]]:
    payload = json.loads((root / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
    order = tuple(int(x) for x in payload["ordering"])
    R = mp.mpf(payload.get("R_mpmath_full") or payload.get("R_mpmath_30") or payload["R"])
    messages: list[str] = []
    ok = True

    if int(payload.get("n", n)) != n:
        ok = False
        messages.append("payload n mismatch")
    if not payload.get("certified"):
        ok = False
        messages.append("payload certified flag is not true")
    for field in ("R", "ordering", "floating_circles", "essential_tight_pairs", "positions"):
        if field not in payload:
            ok = False
            messages.append(f"missing required optimum field {field}")
    if "generation_commit_hash" not in payload:
        ok = False
        messages.append("missing generation_commit_hash")
    if "R_source" not in payload:
        ok = False
        messages.append("missing R_source")

    if not feasible(order, R):
        ok = False
        messages.append("STN infeasible at claimed R*")
    ok = check_witness(payload, order, R, messages) and ok

    positions = recover_positions(order, R)
    essentials = payload.get("essential_tight_pairs", [])
    for pair in essentials:
        i = int(pair["i"])
        j = int(pair["j"])
        forward, wrap = pair_slacks(order, R, positions, i, j)
        slack = forward if pair["kind"] == "forward" else wrap
        if abs(slack) > TIGHT_TOL:
            ok = False
            messages.append(
                f"essential pair {(order[i], order[j])} {pair['kind']} slack={mp.nstr(slack, 12)}"
            )
        if feasible(order, R, slack_pair=(i, j), slack=FLOATING_SLACK):
            ok = False
            messages.append(f"essential pair {(order[i], order[j])} is not essential under +1e-9")

    floaters = tuple(int(x) for x in payload.get("floating_circles", []))
    essential_indices = {int(pair["i"]) for pair in essentials} | {int(pair["j"]) for pair in essentials}
    zero_essential = tuple(order[i] for i in range(len(order)) if i not in essential_indices)
    if floaters != zero_essential:
        ok = False
        messages.append(f"floating/essential mismatch: floaters={floaters} zero={zero_essential}")
    for floater in floaters:
        try:
            idx = order.index(floater)
        except ValueError:
            ok = False
            messages.append(f"floater {floater} absent from order")
            continue
        if not feasible(order, R, slack_index=idx, slack=FLOATING_SLACK):
            ok = False
            messages.append(f"floater {floater} lacks strict-slack STN placement")

    return ok, messages, {"R": mp.nstr(R, 20)}


def verify_local_radius(root: Path, n: int, eta: mp.mpf) -> tuple[bool, list[str], dict[str, str]]:
    payload = json.loads((root / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
    order = tuple(int(x) for x in payload["ordering"])
    R = mp.mpf(payload.get("R_mpmath_full") or payload.get("R_mpmath_30") or payload["R"])
    messages: list[str] = []
    ok = True
    if not feasible(order, R + eta):
        ok = False
        messages.append(f"STN infeasible at R*+eta eta={eta}")
    if feasible(order, R - eta):
        ok = False
        messages.append(f"STN feasible at R*-eta eta={eta}")
    return ok, messages, {"eta": mp.nstr(eta, 5)}


def content_hash(payload: dict[str, Any]) -> str:
    clone = dict(payload)
    clone["content_sha256_excluding_hash"] = None
    encoded = json.dumps(clone, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def expected_canonical_count(n: int) -> int:
    return math.factorial(n - 1) // 2


def progress_log_has_prefixes(root: Path, payload: dict[str, Any]) -> tuple[bool, list[str]]:
    messages: list[str] = []
    log_path = root / str(payload.get("progress_log", ""))
    if not log_path.exists():
        return False, [f"progress log missing: {payload.get('progress_log')}"]
    expected = {
        int(row["prefix"]): int(row["count"])
        for row in payload.get("prefix_coverage", [])
        if int(row.get("count", 0)) >= 0
    }
    completed: set[int] = set()
    with log_path.open(encoding="utf-8") as fh:
        for line in fh:
            if "stage=stage_a" not in line or "prefix complete" not in line:
                continue
            parts = dict(item.split("=", 1) for item in line.strip().split("\t") if "=" in item)
            try:
                prefix = int(parts["prefix"])
                done = int(parts["done"])
            except (KeyError, ValueError):
                continue
            if expected.get(prefix) == done:
                completed.add(prefix)
    missing = sorted(set(expected) - completed)
    if missing:
        messages.append(f"progress log lacks prefix-complete proof for {missing}")
    return not missing, messages


def verify_frontier(root: Path, n: int) -> tuple[bool, list[str], dict[str, str]]:
    path = root / "results" / "frontiers" / f"n{n:02d}_frontier.json"
    if not path.exists():
        return False, ["frontier artifact missing"], {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    incumbent = mp.mpf(payload["incumbent_R_mpmath"])
    threshold = mp.mpf(str(payload["threshold_float64"]))
    float64_guard = mp.mpf(str(payload.get("float64_lb_error_guard", "0")))
    ok = True
    messages: list[str] = []

    if payload.get("content_sha256_excluding_hash") != content_hash(payload):
        ok = False
        messages.append("frontier content hash mismatch")
    if int(payload.get("n", -1)) != n:
        ok = False
        messages.append("frontier n mismatch")
    expected_total = expected_canonical_count(n)
    if int(payload.get("expected_total_canonical_orders", -1)) != expected_total:
        ok = False
        messages.append("expected canonical count field mismatch")
    if int(payload.get("total_canonical_orders", -1)) != expected_total:
        ok = False
        messages.append("total canonical orders mismatch")
    if not payload.get("enumeration_count_matches"):
        ok = False
        messages.append("enumeration_count_matches false")
    if not payload.get("complete"):
        ok = False
        messages.append("frontier artifact marked incomplete")
    if not payload.get("progress_log_complete"):
        ok = False
        messages.append("progress_log_complete false")
    log_ok, log_messages = progress_log_has_prefixes(root, payload)
    if not log_ok:
        ok = False
        messages.extend(log_messages)
    if len(payload.get("orders", [])) != int(payload.get("frontier_size", -1)):
        ok = False
        messages.append("frontier_size does not match order list length")
    if "largest radius fixed" not in payload.get("canonicalization_rule", ""):
        ok = False
        messages.append("canonicalization rule missing expected fixed-largest statement")

    guard_text = str(payload.get("top_excluded_guard_float64", ""))
    if guard_text:
        top_guard = mp.mpf(guard_text)
        if top_guard - float64_guard < threshold:
            ok = False
            messages.append(
                f"top-excluded guard too small: guard={top_guard} threshold={threshold} "
                f"float64_guard={float64_guard}"
            )

    max_abs_error = mp.mpf("0")
    max_overestimate = mp.mpf("0")
    frontier_min_lb: mp.mpf | None = None
    undercut_count = 0
    not_evaluated = 0
    for entry in payload.get("orders", []):
        order = tuple(int(x) for x in entry["order"])
        stored = mp.mpf(str(entry["lower_bound_float64"]))
        actual = lower_bound(order)
        frontier_min_lb = actual if frontier_min_lb is None else min(frontier_min_lb, actual)
        diff = actual - stored
        max_abs_error = max(max_abs_error, abs(diff))
        if diff < 0:
            max_overestimate = max(max_overestimate, -diff)
        if actual < incumbent - PRUNE_GUARD:
            undercut_count += 1
        if not entry.get("stage_b_evaluated", False):
            not_evaluated += 1

    if undercut_count:
        ok = False
        messages.append(f"{undercut_count} frontier orders have mp LB < incumbent-1e-10")
    if not_evaluated:
        ok = False
        messages.append(f"{not_evaluated} frontier orders were not Stage-B evaluated")
    if max_overestimate > float64_guard:
        ok = False
        messages.append(
            f"frontier float64 overestimate {mp.nstr(max_overestimate, 12)} exceeds guard {float64_guard}"
        )

    stats = {
        "frontier_size": str(len(payload.get("orders", []))),
        "total_canonical_orders": str(payload.get("total_canonical_orders", "")),
        "max_abs_lb_error": mp.nstr(max_abs_error, 12),
        "max_float64_overestimate": mp.nstr(max_overestimate, 12),
        "frontier_min_lb": "none" if frontier_min_lb is None else mp.nstr(frontier_min_lb, 20),
        "source": str(payload.get("stage_a_derivation", payload.get("stage_a_checkpoint_source", ""))),
    }
    return ok, messages, stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Independent high-precision ringmin verifier")
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--stop", type=int, default=14)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--eta", default=str(DEFAULT_ETA))
    parser.add_argument("--skip-frontier", action="store_true")
    args = parser.parse_args()

    eta = mp.mpf(args.eta)
    if eta >= mp.mpf("1e-10"):
        raise SystemExit("eta must remain much smaller than 1e-10")

    all_ok = True
    for n in range(args.start, args.stop + 1):
        inc_ok, inc_messages, inc_stats = verify_incumbent(args.root, n)
        local_ok, local_messages, local_stats = verify_local_radius(args.root, n, eta)
        frontier_ok = True
        frontier_messages: list[str] = []
        frontier_stats: dict[str, str] = {}
        if not args.skip_frontier:
            frontier_ok, frontier_messages, frontier_stats = verify_frontier(args.root, n)
        all_ok = all_ok and inc_ok and local_ok and frontier_ok
        print(
            f"n={n:02d} "
            f"incumbent={'PASS' if inc_ok else 'FAIL'} "
            f"local={'PASS' if local_ok else 'FAIL'} "
            f"frontier={'SKIP' if args.skip_frontier else ('PASS' if frontier_ok else 'FAIL')} "
            f"eta={local_stats['eta']} "
            f"frontier_size={frontier_stats.get('frontier_size', 'NA')} "
            f"total={frontier_stats.get('total_canonical_orders', 'NA')}"
        )
        for message in inc_messages + local_messages + frontier_messages:
            print(f"  - {message}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
