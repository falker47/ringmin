"""Certified exhaustive and heuristic searches over cyclic orderings."""

from __future__ import annotations

from dataclasses import dataclass
import heapq
from itertools import permutations
import multiprocessing as mp
import os
import pickle
import random
import time
from pathlib import Path
from typing import Iterable, Iterator

import numpy as np

from ringmin.evaluator import FullResult, chain_radius, full_radius, full_radius_value
from ringmin.geometry import TAU

BOUND_VERSION = "lb3"


def _write_progress(
    log_path: str | Path | None,
    stage: str,
    label: str,
    prefix: int | str | None,
    done: int,
    incumbent: float | None,
    message: str,
) -> None:
    if log_path is None:
        return
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    incumbent_text = "none" if incumbent is None else f"{incumbent:.17g}"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(
            f"{stamp}\tstage={stage}\tlabel={label}\tprefix={prefix}\t"
            f"done={done}\tincumbent={incumbent_text}\t{message}\n"
        )
        fh.flush()


@dataclass(frozen=True)
class ChainCandidate:
    lower_bound: float
    order: tuple[int, ...]
    R_chain: float


@dataclass(frozen=True)
class SearchResult:
    n: int
    best: FullResult
    certified: bool
    evaluated_full: int
    enumerated_chain: int
    fallback_used: bool
    values: tuple[int, ...] = ()
    runtime_seconds: float = 0.0
    stage_a_seconds: float = 0.0
    stage_b_seconds: float = 0.0
    stage_b_candidates: int = 0


def canonical_orders(n: int) -> Iterator[tuple[int, ...]]:
    """Yield canonical orders: n fixed at position 0, reflections removed."""
    if n < 3:
        raise ValueError("certified search is defined for n >= 3")
    yield from canonical_orders_values(tuple(range(1, n + 1)))


def canonical_orders_values(values: Iterable[int]) -> Iterator[tuple[int, ...]]:
    """Yield canonical cyclic orders for an arbitrary distinct radius set."""
    ordered_values = tuple(sorted(values))
    if len(ordered_values) < 3:
        raise ValueError("certified search is defined for at least 3 radii")
    if len(set(ordered_values)) != len(ordered_values):
        raise ValueError(f"values must be distinct: {ordered_values!r}")
    fixed = ordered_values[-1]
    rest = tuple(ordered_values[:-1])
    for perm in permutations(rest):
        order = (fixed,) + perm
        if order[1] < order[-1]:
            yield order


def stage_a_candidates(
    n: int,
    k: int = 5000,
    workers: int = 1,
    checkpoint_dir: str | Path | None = None,
    resume: bool = False,
    label: str | None = None,
) -> tuple[list[ChainCandidate], int]:
    """Stream all canonical orders and retain the k smallest chain radii."""
    return stage_a_candidates_values(
        tuple(range(1, n + 1)),
        k=k,
        workers=workers,
        checkpoint_dir=checkpoint_dir,
        resume=resume,
        label=label or f"n{n:02d}_{BOUND_VERSION}",
    )


def stage_a_candidates_values(
    values: Iterable[int],
    k: int = 5000,
    workers: int = 1,
    checkpoint_dir: str | Path | None = None,
    resume: bool = False,
    label: str = "values_lb3",
    log_path: str | Path | None = None,
) -> tuple[list[ChainCandidate], int]:
    """Parallel prefix-split Stage A for any canonical radius set."""
    ordered_values = tuple(sorted(values))
    if len(ordered_values) < 3:
        raise ValueError("certified search is defined for at least 3 radii")
    prefixes = ordered_values[:-1]
    if checkpoint_dir is None:
        checkpoint_root = None
    else:
        checkpoint_root = Path(checkpoint_dir)
        checkpoint_root.mkdir(parents=True, exist_ok=True)

    if workers <= 1:
        prefix_results = [
            _stage_a_prefix_worker(
                (
                    ordered_values,
                    prefix,
                    k,
                    checkpoint_root,
                    resume,
                    label,
                    32768,
                    Path(log_path) if log_path else None,
                )
            )
            for prefix in prefixes
        ]
    else:
        tasks = [
            (ordered_values, prefix, k, checkpoint_root, resume, label, 32768, Path(log_path) if log_path else None)
            for prefix in prefixes
        ]
        process_count = min(workers, len(tasks))
        with mp.Pool(processes=process_count) as pool:
            prefix_results = list(pool.imap_unordered(_stage_a_prefix_worker, tasks))

    heap: list[tuple[float, float, tuple[int, ...]]] = []
    count = 0
    for candidates, prefix_count in prefix_results:
        count += prefix_count
        for candidate in candidates:
            item = (-candidate.lower_bound, candidate.R_chain, candidate.order)
            if len(heap) < k:
                heapq.heappush(heap, item)
            elif candidate.lower_bound < -heap[0][0]:
                heapq.heapreplace(heap, item)

    merged = [ChainCandidate(-neg_lb, order, rc) for neg_lb, rc, order in heap]
    merged.sort(key=lambda candidate: candidate.lower_bound)
    return merged, count


def _stage_a_prefix_worker(
    args: tuple[
        tuple[int, ...],
        int,
        int,
        Path | None,
        bool,
        str,
        int,
        Path | None,
    ],
) -> tuple[list[ChainCandidate], int]:
    values, prefix, k, checkpoint_root, resume, label, chunk_size, log_path = args
    checkpoint_path: Path | None = None
    if checkpoint_root is not None:
        checkpoint_path = checkpoint_root / f"stage_a_{label}_p{prefix}.pkl"
        if resume and checkpoint_path.exists():
            with checkpoint_path.open("rb") as fh:
                payload = pickle.load(fh)
            _write_progress(log_path, "stage_a", label, prefix, payload["count"], None, "loaded checkpoint")
            return payload["candidates"], payload["count"]

    fixed = values[-1]
    remaining = tuple(value for value in values[:-1] if value != prefix)
    heap: list[tuple[float, float, tuple[int, ...]]] = []
    count = 0
    chunk: list[tuple[int, ...]] = []
    for perm in permutations(remaining):
        if prefix >= perm[-1]:
            continue
        order = (fixed, prefix, *perm)
        chunk.append(order)
        if len(chunk) == chunk_size:
            count += _consume_stage_a_chunk(chunk, heap, k)
            _write_progress(log_path, "stage_a", label, prefix, count, None, "chunk")
            chunk = []
    if chunk:
        count += _consume_stage_a_chunk(chunk, heap, k)
        _write_progress(log_path, "stage_a", label, prefix, count, None, "chunk")
    candidates = [ChainCandidate(-neg_lb, order, rc) for neg_lb, rc, order in heap]
    candidates.sort(key=lambda candidate: candidate.lower_bound)
    if checkpoint_path is not None:
        tmp = checkpoint_path.with_suffix(".tmp")
        with tmp.open("wb") as fh:
            pickle.dump({"candidates": candidates, "count": count}, fh, protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(tmp, checkpoint_path)
    _write_progress(log_path, "stage_a", label, prefix, count, None, "prefix complete")
    return candidates, count


def _consume_stage_a_chunk(
    chunk: list[tuple[int, ...]],
    heap: list[tuple[float, float, tuple[int, ...]]],
    k: int,
) -> int:
    orders_array = np.asarray(chunk, dtype=np.float64)
    lower_bounds, full_chains = _lower_bounds_numpy(orders_array)
    for lb, rc, order in zip(lower_bounds.tolist(), full_chains.tolist(), chunk, strict=True):
        item = (-lb, rc, order)
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif lb < -heap[0][0]:
            heapq.heapreplace(heap, item)
    return len(chunk)


def _lower_bounds_numpy(orders: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return LB=max(chain(order), chain(order without 1), chain(order without 1,2))."""
    full = _chain_radii_numpy(orders)
    lower = full.copy()
    for removed in ((1.0,), (1.0, 2.0)):
        if not all(np.any(orders[0] == value) for value in removed):
            continue
        if orders.shape[1] - len(removed) < 3:
            continue
        keep = np.ones_like(orders, dtype=bool)
        for value in removed:
            keep &= orders != value
        induced = orders[keep].reshape(orders.shape[0], orders.shape[1] - len(removed))
        lower = np.maximum(lower, _chain_radii_numpy(induced))
    return lower, full


def _chain_radii_numpy(orders: np.ndarray) -> np.ndarray:
    """Vectorized version of Evaluator A for Stage A streaming."""
    n = orders.shape[1]
    lo = np.full(orders.shape[0], 1e-9, dtype=np.float64)
    hi = np.full(orders.shape[0], 4.0 * n * n, dtype=np.float64)
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        total = np.zeros_like(mid)
        for i in range(n):
            a = orders[:, i]
            b = orders[:, (i + 1) % n]
            x2 = (a * b) / ((mid + a) * (mid + b))
            total += 2.0 * np.arcsin(np.sqrt(x2))
        mask = total > TAU
        lo = np.where(mask, mid, lo)
        hi = np.where(mask, hi, mid)
    return 0.5 * (lo + hi)


def certified_search(
    n: int,
    k: int = 5000,
    workers: int = 1,
    checkpoint_dir: str | Path | None = None,
    resume: bool = False,
) -> SearchResult:
    """Run the two-stage certified global search."""
    return certified_search_values(
        tuple(range(1, n + 1)),
        k=k,
        workers=workers,
        checkpoint_dir=checkpoint_dir,
        resume=resume,
        label=f"n{n:02d}_{BOUND_VERSION}",
        result_n=n,
    )


def certified_search_values(
    values: Iterable[int],
    k: int = 5000,
    workers: int = 1,
    checkpoint_dir: str | Path | None = None,
    resume: bool = False,
    label: str = "values",
    result_n: int | None = None,
    stage_b_chunk_size: int = 1024,
) -> SearchResult:
    """Run the two-stage certified global search on any distinct radius set."""
    ordered_values = tuple(sorted(values))
    if not label.endswith(BOUND_VERSION):
        label = f"{label}_{BOUND_VERSION}"
    checkpoint_root = Path(checkpoint_dir) if checkpoint_dir is not None else None
    if checkpoint_root is not None:
        checkpoint_root.mkdir(parents=True, exist_ok=True)
    log_path = checkpoint_root / f"progress_{label}.log" if checkpoint_root is not None else None
    started = time.perf_counter()
    stage_a_started = time.perf_counter()
    candidates, enumerated = stage_a_candidates_values(
        ordered_values,
        k=k,
        workers=workers,
        checkpoint_dir=checkpoint_root,
        resume=resume,
        label=label,
        log_path=log_path,
    )
    stage_a_seconds = time.perf_counter() - stage_a_started
    stage_b_started = time.perf_counter()
    incumbent: FullResult | None = None
    evaluated = 0
    stop_reached = False
    stage_b_candidates = 0
    next_index = 0
    stage_b_checkpoint = (
        checkpoint_root / f"stage_b_{label}.pkl" if checkpoint_root is not None else None
    )
    if resume and stage_b_checkpoint is not None and stage_b_checkpoint.exists():
        with stage_b_checkpoint.open("rb") as fh:
            payload = pickle.load(fh)
        if payload.get("version") == BOUND_VERSION and payload.get("k") == k:
            next_index = payload["next_index"]
            evaluated = payload["evaluated"]
            stage_b_candidates = payload.get("stage_b_candidates", evaluated)
            stop_reached = payload.get("stop_reached", False)
            if payload.get("incumbent_order") is not None:
                incumbent = full_radius(
                    tuple(payload["incumbent_order"]),
                    R_chain=payload["incumbent_chain"],
                )
            _write_progress(
                log_path,
                "stage_b",
                label,
                "main",
                next_index,
                incumbent.R_full if incumbent else None,
                "loaded checkpoint",
            )

    while not stop_reached and next_index < len(candidates):
        if incumbent is not None and candidates[next_index].lower_bound >= incumbent.R_full - 1e-9:
            stop_reached = True
            break
        end_index = min(next_index + stage_b_chunk_size, len(candidates))
        batch = candidates[next_index:end_index]
        results = _evaluate_candidate_batch(batch, workers)
        evaluated += len(results)
        stage_b_candidates += len(results)
        for order, result_chain, lower_bound, result_full in results:
            if result_full + 1e-10 < lower_bound:
                raise AssertionError(
                    f"R_full < lower bound for order={order!r}: {result_full} < {lower_bound}"
                )
            if incumbent is None or result_full < incumbent.R_full:
                incumbent = full_radius(order, R_chain=result_chain)
        next_index = end_index
        _save_stage_b_checkpoint(
            stage_b_checkpoint,
            k,
            next_index,
            evaluated,
            stage_b_candidates,
            incumbent,
            stop_reached=False,
        )
        _write_progress(
            log_path,
            "stage_b",
            label,
            "main",
            next_index,
            incumbent.R_full if incumbent else None,
            f"candidate chunk evaluated={len(results)}",
        )

    if not stop_reached and next_index >= len(candidates):
        stop_reached = False

    if incumbent is None:
        raise AssertionError("no candidates evaluated")

    fallback_used = False
    if not stop_reached:
        fallback_used = True
        fallback = _fallback_scan_values(
            ordered_values,
            threshold=incumbent.R_full,
            workers=workers,
            chunk_size=32768,
            checkpoint_root=checkpoint_root,
            resume=resume,
            label=label,
            log_path=log_path,
        )
        evaluated += fallback["evaluated"]
        stage_b_candidates += fallback["evaluated"]
        if fallback["best_order"] is not None and fallback["best_full"] < incumbent.R_full:
            incumbent = full_radius(fallback["best_order"], R_chain=fallback["best_chain"])
        stop_reached = True
    _save_stage_b_checkpoint(
        stage_b_checkpoint,
        k,
        next_index,
        evaluated,
        stage_b_candidates,
        incumbent,
        stop_reached=stop_reached,
    )

    stage_b_seconds = time.perf_counter() - stage_b_started
    return SearchResult(
        n=result_n if result_n is not None else ordered_values[-1],
        best=incumbent,
        certified=stop_reached,
        evaluated_full=evaluated,
        enumerated_chain=enumerated,
        fallback_used=fallback_used,
        values=ordered_values,
        runtime_seconds=time.perf_counter() - started,
        stage_a_seconds=stage_a_seconds,
        stage_b_seconds=stage_b_seconds,
        stage_b_candidates=stage_b_candidates,
    )


def _evaluate_candidate_batch(
    batch: list[ChainCandidate],
    workers: int,
) -> list[tuple[tuple[int, ...], float, float, float]]:
    if workers <= 1 or len(batch) <= 1:
        return [_evaluate_candidate(candidate) for candidate in batch]
    process_count = min(workers, len(batch))
    with mp.Pool(processes=process_count) as pool:
        return list(pool.imap_unordered(_evaluate_candidate, batch))


def _evaluate_candidate(candidate: ChainCandidate) -> tuple[tuple[int, ...], float, float, float]:
    result_chain, result_full = full_radius_value(candidate.order, R_chain=candidate.R_chain)
    return candidate.order, result_chain, candidate.lower_bound, result_full


def _save_stage_b_checkpoint(
    path: Path | None,
    k: int,
    next_index: int,
    evaluated: int,
    stage_b_candidates: int,
    incumbent: FullResult | None,
    stop_reached: bool,
) -> None:
    if path is None:
        return
    payload = {
        "version": BOUND_VERSION,
        "k": k,
        "next_index": next_index,
        "evaluated": evaluated,
        "stage_b_candidates": stage_b_candidates,
        "stop_reached": stop_reached,
        "incumbent_order": tuple(int(x) for x in incumbent.order) if incumbent else None,
        "incumbent_chain": incumbent.R_chain if incumbent else None,
        "incumbent_full": incumbent.R_full if incumbent else None,
    }
    tmp = path.with_suffix(".tmp")
    with tmp.open("wb") as fh:
        pickle.dump(payload, fh, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(tmp, path)


def _fallback_scan_values(
    values: tuple[int, ...],
    threshold: float,
    workers: int,
    chunk_size: int,
    checkpoint_root: Path | None,
    resume: bool,
    label: str,
    log_path: Path | None,
) -> dict[str, object]:
    prefixes = values[:-1]
    tasks = [
        (values, prefix, threshold, chunk_size, checkpoint_root, resume, label, log_path)
        for prefix in prefixes
    ]
    if workers <= 1:
        results = [_fallback_prefix_worker(task) for task in tasks]
    else:
        process_count = min(workers, len(tasks))
        with mp.Pool(processes=process_count) as pool:
            results = list(pool.imap_unordered(_fallback_prefix_worker, tasks))

    best_order: tuple[int, ...] | None = None
    best_chain = math_inf = float("inf")
    best_full = math_inf
    evaluated = 0
    for result in results:
        evaluated += result["evaluated"]
        if result["best_order"] is not None and result["best_full"] < best_full:
            best_order = result["best_order"]
            best_chain = result["best_chain"]
            best_full = result["best_full"]
    return {
        "evaluated": evaluated,
        "best_order": best_order,
        "best_chain": best_chain,
        "best_full": best_full,
    }


def _fallback_prefix_worker(
    args: tuple[tuple[int, ...], int, float, int, Path | None, bool, str, Path | None],
) -> dict[str, object]:
    values, prefix, threshold, chunk_size, checkpoint_root, resume, label, log_path = args
    checkpoint_path: Path | None = None
    if checkpoint_root is not None:
        checkpoint_path = checkpoint_root / f"fallback_{label}_p{prefix}.pkl"
        if resume and checkpoint_path.exists():
            with checkpoint_path.open("rb") as fh:
                payload = pickle.load(fh)
            if (
                payload.get("version") == BOUND_VERSION
                and abs(payload.get("threshold", 0.0) - threshold) <= 1e-10
            ):
                _write_progress(
                    log_path,
                    "stage_b_fallback",
                    label,
                    prefix,
                    payload["done"],
                    payload["threshold"],
                    "loaded checkpoint",
                )
                return payload["result"]
    fixed = values[-1]
    remaining = tuple(value for value in values[:-1] if value != prefix)
    chunk: list[tuple[int, ...]] = []
    evaluated = 0
    done = 0
    best_order: tuple[int, ...] | None = None
    best_chain = float("inf")
    best_full = float("inf")

    def consume(current: list[tuple[int, ...]]) -> None:
        nonlocal evaluated, best_order, best_chain, best_full
        if not current:
            return
        orders_array = np.asarray(current, dtype=np.float64)
        lower_bounds, full_chains = _lower_bounds_numpy(orders_array)
        for lb, rc, order in zip(lower_bounds.tolist(), full_chains.tolist(), current, strict=True):
            if lb < threshold:
                _, result_full = full_radius_value(order, R_chain=rc)
                evaluated += 1
                if result_full < best_full:
                    best_order = order
                    best_chain = rc
                    best_full = result_full

    for perm in permutations(remaining):
        if prefix >= perm[-1]:
            continue
        chunk.append((fixed, prefix, *perm))
        done += 1
        if len(chunk) == chunk_size:
            consume(chunk)
            _write_progress(
                log_path,
                "stage_b_fallback",
                label,
                prefix,
                done,
                threshold,
                f"chunk evaluated={evaluated}",
            )
            chunk = []
    consume(chunk)
    result = {
        "evaluated": evaluated,
        "best_order": best_order,
        "best_chain": best_chain,
        "best_full": best_full,
    }
    if checkpoint_path is not None:
        tmp = checkpoint_path.with_suffix(".tmp")
        with tmp.open("wb") as fh:
            pickle.dump(
                {
                    "version": BOUND_VERSION,
                    "threshold": threshold,
                    "done": done,
                    "result": result,
                },
                fh,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        os.replace(tmp, checkpoint_path)
    _write_progress(
        log_path,
        "stage_b_fallback",
        label,
        prefix,
        done,
        threshold,
        f"prefix complete evaluated={evaluated}",
    )
    return result


def random_canonical_order(n: int, rng: random.Random) -> tuple[int, ...]:
    rest = list(range(1, n))
    rng.shuffle(rest)
    order = (n, *rest)
    if order[1] > order[-1]:
        order = (order[0], *reversed(order[1:]))
    return tuple(order)


def heuristic_search(n: int, restarts: int = 200, seed: int = 0) -> FullResult:
    """Non-exhaustive local search using R_full as objective."""
    rng = random.Random(seed)
    best: FullResult | None = None

    def consider(order: Iterable[int]) -> None:
        nonlocal best
        result = full_radius(tuple(order))
        if best is None or result.R_full < best.R_full:
            best = result

    for _ in range(restarts):
        current_order = random_canonical_order(n, rng)
        current = full_radius(current_order)
        improved = True
        while improved:
            improved = False
            base = list(current.order)
            neighbors: list[tuple[float, ...]] = []
            for _ in range(min(50, n * n)):
                move = rng.randrange(3)
                candidate = base[:]
                if move == 0:
                    i, j = rng.sample(range(1, n), 2)
                    candidate[i], candidate[j] = candidate[j], candidate[i]
                elif move == 1:
                    i, j = rng.sample(range(1, n), 2)
                    value = candidate.pop(i)
                    candidate.insert(j, value)
                else:
                    i, j = sorted(rng.sample(range(1, n), 2))
                    candidate[i : j + 1] = reversed(candidate[i : j + 1])
                neighbors.append(tuple(candidate))
            for neighbor in neighbors:
                result = full_radius(neighbor)
                if result.R_full < current.R_full:
                    current = result
                    improved = True
            consider(tuple(int(x) for x in current.order))

    if best is None:
        raise AssertionError("heuristic search produced no result")
    return best
