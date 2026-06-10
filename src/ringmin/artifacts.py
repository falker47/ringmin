"""Result artifact serialization."""

from __future__ import annotations

import json
from pathlib import Path

from ringmin.evaluator import FullResult
from ringmin.geometry import TAU, theta
from ringmin.search import SearchResult


def _radius_value(radius: float) -> int | float:
    return int(radius) if float(radius).is_integer() else radius


def _binding_payload(result: FullResult, layer: str) -> list[dict[str, object]]:
    if layer == "recovered":
        bindings = result.recovered_tight_pairs
    elif layer == "essential":
        bindings = result.essential_tight_pairs
    else:
        raise ValueError(f"unknown binding layer {layer!r}")
    return [
        {
            "i": binding.i,
            "j": binding.j,
            "radius_i": _radius_value(binding.radius_i),
            "radius_j": _radius_value(binding.radius_j),
            "kind": binding.kind,
            "slack": binding.slack,
            "adjacent": (binding.j == binding.i + 1)
            or (binding.i == 0 and binding.j == len(result.order) - 1),
        }
        for binding in bindings
    ]


def _floating_slacks(result: FullResult) -> list[dict[str, object]]:
    floating = set(result.floating_radii)
    rows: list[dict[str, object]] = []
    for i, ri in enumerate(result.order):
        if ri not in floating:
            continue
        for j, rj in enumerate(result.order):
            if i == j:
                continue
            a, b = sorted((i, j))
            sep = theta(result.R_full, result.order[a], result.order[b])
            delta = result.positions[b] - result.positions[a]
            rows.append(
                {
                    "i": a,
                    "j": b,
                    "radius_i": _radius_value(result.order[a]),
                    "radius_j": _radius_value(result.order[b]),
                    "forward_slack": delta - sep,
                    "wrap_slack": (TAU - sep) - delta,
                }
            )
    return rows


def result_payload(result: FullResult, certified: bool, extra: dict[str, object] | None = None) -> dict[str, object]:
    payload: dict[str, object] = {
        "ordering": [_radius_value(r) for r in result.order],
        "R": format(result.R_full, ".17g"),
        "R_float64": result.R_full,
        "R_chain_float64": result.R_chain,
        "positions": list(result.positions),
        "recovered_tight_pairs": _binding_payload(result, "recovered"),
        "essential_tight_pairs": _binding_payload(result, "essential"),
        "binding_pairs": _binding_payload(result, "essential"),
        "binding_pairs_legacy_note": "binding_pairs is an alias of essential_tight_pairs",
        "floating_circles": [_radius_value(radius) for radius in result.floating_radii],
        "floating_definition": (
            "c is floating iff there exists an optimal configuration where c touches only "
            "the central circle; implemented by inflating all pairwise theta constraints "
            "involving c by 1e-9 at R_full and checking STN feasibility"
        ),
        "floating_constraint_slacks": _floating_slacks(result),
        "certified": certified,
    }
    if extra:
        payload.update(extra)
    return payload


def write_search_artifacts(search: SearchResult, root: str | Path = "results") -> dict[str, object]:
    out_dir = Path(root) / f"n{search.n:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = result_payload(
        search.best,
        search.certified,
        {
            "n": search.n,
            "values": list(search.values) if search.values else None,
            "evaluated_full": search.evaluated_full,
            "stage_b_candidates": search.stage_b_candidates,
            "enumerated_chain": search.enumerated_chain,
            "fallback_used": search.fallback_used,
            "runtime_seconds": search.runtime_seconds,
            "stage_a_seconds": search.stage_a_seconds,
            "stage_b_seconds": search.stage_b_seconds,
        },
    )
    (out_dir / "optimum.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    certificate = (
        f"n={search.n}\n"
        f"certified={search.certified}\n"
        f"R_full={payload['R']}\n"
        f"ordering={payload['ordering']}\n"
        f"enumerated_chain={search.enumerated_chain}\n"
        f"evaluated_full={search.evaluated_full}\n"
        f"stage_b_candidates={search.stage_b_candidates}\n"
        f"fallback_used={search.fallback_used}\n"
        f"runtime_seconds={search.runtime_seconds:.6f}\n"
        f"stage_a_seconds={search.stage_a_seconds:.6f}\n"
        f"stage_b_seconds={search.stage_b_seconds:.6f}\n"
    )
    (out_dir / "certificate.txt").write_text(certificate, encoding="utf-8")
    return payload
