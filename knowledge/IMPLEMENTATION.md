# Implementation

This thematic ledger owns stable implementation and verification-architecture
facts, including the known full-verifier portability limitation. It is not a
substitute for code, tests, artifacts, or verifier inspection.

## Current implementation facts

**Status:** engineering facts at the bootstrap snapshot.

- `src/ringmin/evaluator.py` separates the adjacent-chain relaxation from fixed-order all-pairs STN feasibility.
- `src/ringmin/search.py` implements canonical cyclic enumeration, vectorized lower bounds, Stage-B full evaluation, checkpoints, and an exhaustive fallback when the retained candidate frontier is insufficient.
- The production lower bound version is `lb3`, using the maximum of the full-order chain radius and selected induced-order chain radii after removing `{1}` and `{1,2}` where defined.
- `verify.py` reimplements the relevant geometry, STN, local bracket, artifact, canonical-count, frontier, guard, and progress-log checks using the standard library and `mpmath`, without importing `src/ringmin`.
- The test suite contains property checks and SciPy SLSQP cross-checks, but it is not a replacement for the independent verifier.
- Hosted CI runs the unit suite and `verify.py --start 3 --stop 8 --skip-frontier`; this is a smoke gate, not full `3..14` global-certificate verification.

### Full-verifier portability limitation

**Status:** engineering and certification-reproducibility limitation at the bootstrap snapshot.

The tracked frontier JSON files refer to `results\checkpoints\progress_nNN_lb3.log`, while `results/checkpoints/` is Git-ignored. Those logs were present in this Windows checkout and the full local `3..14` verifier passed. A fresh clone cannot reproduce the current full-verifier run without restoring or regenerating the logs; the stored backslash paths also require portable handling before a POSIX full-frontier run can be claimed. Hosted CI avoids this dependency by using `--skip-frontier`. This limitation does not turn the smoke verifier into a global certificate and was not repaired in the documentation-only bootstrap task.

## Non-implications owned by this module

- Generated README/report/table agreement does not replace source and verifier agreement.

