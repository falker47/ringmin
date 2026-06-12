from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import pickle
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def load_pickle(path: Path) -> dict[str, object]:
    with path.open("rb") as fh:
        return pickle.load(fh)


def candidate_key(order: tuple[int, ...]) -> str:
    return ",".join(str(x) for x in order)


def canonical_count(n: int) -> int:
    return math.factorial(n - 1) // 2


def git_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unknown"


def content_hash(payload: dict[str, object]) -> str:
    clone = dict(payload)
    clone["content_sha256_excluding_hash"] = None
    encoded = json.dumps(clone, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def progress_log_complete(n: int, prefix_counts: dict[int, int]) -> tuple[bool, str, list[int]]:
    log_path = ROOT / "results" / "checkpoints" / f"progress_n{n:02d}_lb3.log"
    if not log_path.exists():
        return False, str(log_path.relative_to(ROOT)), sorted(prefix_counts)
    completed: set[int] = set()
    with log_path.open(encoding="utf-8") as fh:
        for line in fh:
            if "stage=stage_a" not in line or "prefix complete" not in line:
                continue
            parts = dict(
                item.split("=", 1)
                for item in line.strip().split("\t")
                if "=" in item
            )
            try:
                prefix = int(parts["prefix"])
                done = int(parts["done"])
            except (KeyError, ValueError):
                continue
            if prefix_counts.get(prefix) == done:
                completed.add(prefix)
    missing = sorted(set(prefix_counts) - completed)
    return not missing, str(log_path.relative_to(ROOT)), missing


def extract_one(n: int, margin: float) -> dict[str, object]:
    checkpoint_dir = ROOT / "results" / "checkpoints"
    optimum_path = ROOT / "results" / f"n{n:02d}" / "optimum.json"
    optimum = json.loads(optimum_path.read_text(encoding="utf-8"))
    incumbent = float(optimum["R_float64"])
    threshold = incumbent + margin

    stage_b_path = checkpoint_dir / f"stage_b_n{n:02d}_lb3.pkl"
    stage_b = load_pickle(stage_b_path)
    k = int(stage_b["k"])
    evaluated = int(stage_b["stage_b_candidates"])

    prefix_rows: list[dict[str, object]] = []
    all_candidates: list[object] = []
    frontier_by_key: dict[str, object] = {}
    complete = True
    prefix_counts: dict[int, int] = {}
    top_excluded_guards: list[float] = []
    for prefix in range(1, n):
        path = checkpoint_dir / f"stage_a_n{n:02d}_lb3_p{prefix}.pkl"
        if not path.exists():
            complete = False
            prefix_rows.append(
                {
                    "prefix": prefix,
                    "count": 0,
                    "retained": 0,
                    "frontier_count": 0,
                    "max_retained_lb": "",
                    "covered": False,
                }
            )
            continue
        payload = load_pickle(path)
        candidates = list(payload["candidates"])
        count = int(payload["count"])
        prefix_counts[prefix] = count
        all_candidates.extend(candidates)
        max_lb = max((float(candidate.lower_bound) for candidate in candidates), default=float("inf"))
        has_excluded = count > len(candidates)
        top_excluded_guard = max_lb if has_excluded else None
        if top_excluded_guard is not None:
            top_excluded_guards.append(top_excluded_guard)
        covered = (not has_excluded) or max_lb >= threshold
        complete = complete and covered
        prefix_frontier = 0
        for candidate in candidates:
            if float(candidate.lower_bound) < threshold:
                key = candidate_key(tuple(int(x) for x in candidate.order))
                frontier_by_key[key] = candidate
                prefix_frontier += 1
        prefix_rows.append(
            {
                "prefix": prefix,
                "count": count,
                "retained": len(candidates),
                "frontier_count": prefix_frontier,
                "max_retained_lb": "" if max_lb == float("inf") else f"{max_lb:.17g}",
                "top_excluded_guard_float64": (
                    "" if top_excluded_guard is None else f"{top_excluded_guard:.17g}"
                ),
                "covered": covered,
            }
        )

    total_enumerated = sum(prefix_counts.values())
    expected_total = canonical_count(n)
    enumeration_count_matches = total_enumerated == expected_total
    log_complete, progress_log_path, missing_log_prefixes = progress_log_complete(n, prefix_counts)

    global_candidates = sorted(
        all_candidates,
        key=lambda candidate: (float(candidate.lower_bound), float(candidate.R_chain), tuple(candidate.order)),
    )
    global_top = global_candidates[:k]
    evaluated_keys = {
        candidate_key(tuple(int(x) for x in candidate.order))
        for candidate in global_top[:evaluated]
    }
    global_heap_covers_threshold = len(global_candidates) <= k or float(global_top[-1].lower_bound) >= threshold
    global_top_excluded_guard = min(top_excluded_guards) if top_excluded_guards else None

    orders = []
    for candidate in sorted(
        frontier_by_key.values(),
        key=lambda item: (float(item.lower_bound), float(item.R_chain), tuple(item.order)),
    ):
        order = tuple(int(x) for x in candidate.order)
        orders.append(
            {
                "order": list(order),
                "lower_bound_float64": float(candidate.lower_bound),
                "R_chain_float64": float(candidate.R_chain),
                "stage_b_evaluated": candidate_key(order) in evaluated_keys,
            }
        )

    out_dir = ROOT / "results" / "frontiers"
    out_dir.mkdir(parents=True, exist_ok=True)
    artifact = {
        "n": n,
        "bound_version": "lb3",
        "canonicalization_rule": (
            "largest radius fixed at position 0; enumerate permutations of remaining "
            "radii; keep only orders with position1 < last position to quotient reflection"
        ),
        "total_canonical_orders": total_enumerated,
        "expected_total_canonical_orders": expected_total,
        "enumeration_count_matches": enumeration_count_matches,
        "definition": "canonical orders with float64 LB < incumbent_R_float64 + 2e-10",
        "incumbent_R_float64": incumbent,
        "incumbent_R_mpmath": optimum.get("R_mpmath_full")
        or optimum.get("R_mpmath_30")
        or optimum["R"],
        "threshold_float64": threshold,
        "margin": margin,
        "stage_a_checkpoint_source": "results/checkpoints/stage_a_nNN_lb3_p*.pkl",
        "stage_b_checkpoint_source": f"results/checkpoints/stage_b_n{n:02d}_lb3.pkl",
        "progress_log": progress_log_path,
        "progress_log_complete": log_complete,
        "progress_log_missing_prefixes": missing_log_prefixes,
        "generation_commit_hash": git_hash(),
        "k": k,
        "stage_b_candidates": evaluated,
        "frontier_size": len(orders),
        "float64_lb_error_guard": "1e-11",
        "top_excluded_guard_float64": (
            "" if global_top_excluded_guard is None else f"{global_top_excluded_guard:.17g}"
        ),
        "completeness_condition": (
            "complete iff every prefix heap retained all orders or its kth retained LB "
            "is >= threshold; global top-excluded guard is the minimum prefix kth LB"
        ),
        "complete": complete
        and global_heap_covers_threshold
        and enumeration_count_matches
        and log_complete,
        "prefix_coverage": prefix_rows,
        "global_heap_covers_threshold": global_heap_covers_threshold,
        "orders": orders,
    }
    artifact["content_sha256_excluding_hash"] = content_hash(artifact)
    out_path = out_dir / f"n{n:02d}_frontier.json"
    out_path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "n": n,
        "frontier_size": len(orders),
        "evaluated_in_frontier": sum(1 for row in orders if row["stage_b_evaluated"]),
        "complete": artifact["complete"],
        "k": k,
        "stage_b_candidates": evaluated,
        "global_heap_covers_threshold": global_heap_covers_threshold,
        "path": str(out_path.relative_to(ROOT)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=3)
    parser.add_argument("--stop", type=int, default=14)
    parser.add_argument("--margin", type=float, default=2e-10)
    args = parser.parse_args()

    rows = [extract_one(n, args.margin) for n in range(args.start, args.stop + 1)]
    summary_path = ROOT / "results" / "frontiers" / "summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(
            f"n={row['n']} frontier={row['frontier_size']} "
            f"evaluated={row['evaluated_in_frontier']} complete={row['complete']} "
            f"k={row['k']} stage_b={row['stage_b_candidates']} path={row['path']}"
        )
    print(f"wrote {summary_path}")
    return 0 if all(row["complete"] for row in rows) else 2


if __name__ == "__main__":
    raise SystemExit(main())
