from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.artifacts import write_search_artifacts
from ringmin.search import certified_search


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--stop", type=int, required=True)
    parser.add_argument("--k", type=int, default=5000)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    for n in range(args.start, args.stop + 1):
        search = certified_search(
            n,
            k=args.k,
            workers=args.workers,
            checkpoint_dir=ROOT / "results" / "checkpoints",
            resume=args.resume,
        )
        payload = write_search_artifacts(search, root=ROOT / "results")
        print(
            f"n={n} certified={search.certified} R={payload['R']} "
            f"order={payload['ordering']} floating={payload['floating_circles']} "
            f"full={search.evaluated_full} chain={search.enumerated_chain} "
            f"stage_b={search.stage_b_candidates} "
            f"runtime={search.runtime_seconds:.3f}s"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
