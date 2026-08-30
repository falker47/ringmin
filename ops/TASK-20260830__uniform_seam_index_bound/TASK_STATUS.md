# Task Status

```text
task=TASK-20260830__uniform_seam_index_bound
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-30
updated_at=2026-08-30
```

## Objective

Prove and integrate the exact uniform bound

```text
4k+1 <= s_k <= 4k+14              for every integer k>=1
```

for the first strict-obstruction index of the formal Supnick seam, reusing
the existing fixed-`k` theorem.

## Scientific question

Does the fixed-`k` no-threshold range give the lower bound, and does the
single symbolic choice `n=4k+14` with `S_k=k(21k+83)/22` give an exact strict
bridge `T_{k,n}<S_k<R_{k,n}` for every integer `k>=1`?

## In scope

- one authoritative proof note for the uniform formal-seam theorem;
- an exact task-local stdlib/`Fraction` checker for polynomial identities,
  denominator/sign gates, and strictness;
- normal and optimized/no-site checker runs, the repository regression suite,
  and a complete delta audit;
- durable knowledge, current status, and roadmap synchronization only after
  the exact proof and checker pass.

## Out of scope

- the radius-8 diagnostic localization or any finite onset scan;
- changing or reproving the authoritative fixed-`k` theorem;
- exact classification of any new individual `s_k`;
- full fixed-order feasibility, `R*(n)`, global optima, contact graphs,
  floating circles, or global asymptotics;
- solver, test, certificate, verifier, paper, or publication-asset changes.

## Expected delta

- `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md`;
- this four-file task dossier, including `check_uniform_bound.py`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- `CURRENT_STATUS.md`.

## Protected paths potentially affected

- `research/FIXED_K_SUPNICK_SEAM.md`: read-only imported theorem;
- `src/`, `tests/`: production implementation and tests remain unchanged;
- `results/`, `verify.py`: certificate chain is unrelated and protected;
- `paper_assets/`: historical arXiv-v1 publication assets remain unchanged.

## Completion gates

- [x] exact proof complete within the stated formal-seam scope;
- [x] claims and non-implications classified correctly;
- [x] symbolic checker verifies identities, denominators, signs, and strictness;
- [x] checker passes normally and under `python -O -S`;
- [x] independent proof/checker review passes;
- [x] durable memory updated only after exact verification;
- [x] relevant regression tests pass;
- [x] `git status --short --untracked-files=all` inspected;
- [x] complete tracked and untracked delta inspected;
- [x] direct format checks and `git diff --check` pass;
- [x] no incidental generated or protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The uniform formal-seam theorem, exact symbolic checker, durable-memory
updates, independent reviews, regression run, and complete delta audit are
finished. Manual review and integration remain with the user. After
acceptance, exactly one next atomic task is the bounded radius-8 numerical
diagnostic on `33<=n<=46`; it is not started here.
