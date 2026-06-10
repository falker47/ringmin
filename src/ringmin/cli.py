"""Command-line interface for ringmin."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ringmin.artifacts import write_search_artifacts
from ringmin.evaluator import FullResult, full_radius
from ringmin.search import certified_search, heuristic_search


def _parse_order(value: str) -> tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def _result_json(result: FullResult, certified: bool | None = None) -> str:
    payload = {
        "order": result.order,
        "R_chain": result.R_chain,
        "R_full": result.R_full,
        "positions": result.positions,
        "binding_pairs": [binding.__dict__ for binding in result.binding_pairs],
        "floating_radii": result.floating_radii,
    }
    if certified is not None:
        payload["certified"] = certified
    return json.dumps(payload, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ringmin")
    sub = parser.add_subparsers(dest="command", required=True)

    solve = sub.add_parser("solve")
    solve.add_argument("--order", required=True)

    sweep = sub.add_parser("sweep")
    sweep.add_argument("--n", type=int, required=True)
    sweep.add_argument("--k", type=int, default=5000)
    sweep.add_argument("--workers", type=int, default=1)
    sweep.add_argument("--checkpoint-dir", default="results/checkpoints")
    sweep.add_argument("--n14", action="store_true")
    sweep.add_argument("--resume", action="store_true")
    sweep.add_argument("--no-write", action="store_true")

    heuristic = sub.add_parser("heuristic")
    heuristic.add_argument("--n", type=int, required=True)
    heuristic.add_argument("--restarts", type=int, default=200)
    heuristic.add_argument("--seed", type=int, default=0)

    verify = sub.add_parser("verify")
    verify.add_argument("--n", type=int, required=True)

    sub.add_parser("report")

    args = parser.parse_args(argv)
    if args.command == "solve":
        print(_result_json(full_radius(_parse_order(args.order))))
        return 0
    if args.command == "sweep":
        if args.n == 14 and not args.n14:
            raise SystemExit("n=14 requires --n14")
        result = certified_search(
            args.n,
            k=args.k,
            workers=args.workers,
            checkpoint_dir=args.checkpoint_dir,
            resume=args.resume,
        )
        if not args.no_write:
            write_search_artifacts(result)
        print(_result_json(result.best, certified=result.certified))
        return 0
    if args.command == "heuristic":
        result = heuristic_search(args.n, restarts=args.restarts, seed=args.seed)
        print("HEURISTIC")
        print(_result_json(result, certified=False))
        return 0
    if args.command == "verify":
        from ringmin.highprec import full_radius_mp

        order_path = Path(f"results/n{args.n:02d}/optimum.json")
        payload = json.loads(order_path.read_text(encoding="utf-8"))
        print(mp_format(full_radius_mp(tuple(payload["ordering"]))))
        return 0
    if args.command == "report":
        print("REPORT.md generation is part of milestone M3.")
        return 0
    raise AssertionError(f"unhandled command {args.command!r}")


def mp_format(value: object) -> str:
    return str(value)


if __name__ == "__main__":
    raise SystemExit(main())
