# Implementation

This thematic ledger owns stable implementation and verification-architecture
facts, including full-verifier evidence restoration. It is not a
substitute for code, tests, artifacts, or verifier inspection.

## Current implementation facts

**Status:** engineering facts at the bootstrap snapshot.

- `src/ringmin/evaluator.py` separates the adjacent-chain relaxation from fixed-order all-pairs STN feasibility.
- `src/ringmin/search.py` implements canonical cyclic enumeration, vectorized lower bounds, Stage-B full evaluation, checkpoints, and an exhaustive fallback when the retained candidate frontier is insufficient.
- The production lower bound version is `lb3`, using the maximum of the full-order chain radius and selected induced-order chain radii after removing `{1}` and `{1,2}` where defined.
- `verify.py` reimplements the relevant geometry, STN, local bracket, artifact, canonical-count, frontier, guard, and progress-log checks using the standard library and `mpmath`, without importing `src/ringmin`.
- The test suite contains property checks and SciPy SLSQP cross-checks, but it is not a replacement for the independent verifier.
- Hosted CI runs the unit suite and `verify.py --start 3 --stop 8 --skip-frontier`; this is a smoke gate, not full `3..14` global-certificate verification.

### Full-verifier evidence restoration

**Status:** engineering fact, independently reproduced locally from a clean source export on Windows.

The tracked frontier JSON files refer to `results\checkpoints\progress_nNN_lb3.log`, while `results/checkpoints/` is Git-ignored. Their exact historical bytes are now distributed as deterministic gzip archives in `reproducibility/frontier_logs/`, with original/archive hashes and capture provenance. Run `python scripts/frontier_logs.py restore` before the full verifier. Restoration validates every archive and existing target before creating missing logs, refuses differing existing evidence, and checks readback. It preserves evidence rather than regenerating a search.

The verifier accepts relative paths with either separator and rejects absolute, drive-qualified and parent-traversal paths. It still imports no production code. A tracked-source clean export with these changes, initially without ignored logs, passed restoration, all 15 tests, smoke verification and complete `3..14` frontier verification. POSIX execution was not available and is not claimed. Exact source hashes, commands, outputs and failure controls are in the [reproduction dossier](../ops/TASK-20260911__portable_frontier_evidence/EVIDENCE.md). Hosted CI remains a separate smoke gate; no exact-SHA hosted status is inferred.

## Non-implications owned by this module

- Generated README/report/table agreement does not replace source and verifier agreement.
