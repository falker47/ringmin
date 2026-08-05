# Task Status

```text
task=TASK-20260805__radius7_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-05
updated_at=2026-08-05
```

## Objective

Prove or refute the proposed exact radius-7 formal Supnick seam onset
`s_7=34` by importing `research/FIXED_K_SUPNICK_SEAM.md` in full and closing
only `n=33,34` at the common rational separator `R=140`.

## Scientific question

For the chain-minimizing Supnick cycle on `{7,...,n}`, do exact endpoint
bounds establish

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34},
```

and hence, using only the imported persistence theorem, prove `s_7=34` for
the single formal seam `(n,7,n-1)`?

## In scope

- one authoritative radius-7 endpoint proof note;
- complete 27- and 28-edge Supnick closure tables at `R=140`;
- exact rational threshold, arcsine-domain, termwise-bound, and `pi` gates;
- a task-local exact-by-default checker, optimized execution, optional
  60/100-digit diagnostics, and a separate production-convention comparison;
- durable memory/status/roadmap updates only after an exact conclusion.

## Out of scope

- reproving or changing the general fixed-`k` theorem;
- full fixed-order feasibility or any all-pairs placement claim;
- claims about `R*(n)`, global optima, contact graphs, or floating circles;
- changes to solver code, tests, certificates, `verify.py`, paper, or
  publication assets.

## Expected delta

- `research/RADIUS7_SEAM_ONSET.md`;
- this dossier, including `check_seam.py`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- `CURRENT_STATUS.md`.

## Protected paths potentially affected

- `research/FIXED_K_SUPNICK_SEAM.md`: read-only theorem source;
- `src/`, `tests/`: production implementation and regression suite, no
  source changes authorized;
- `results/`, `verify.py`: certificate chain, unrelated and protected;
- `paper_assets/`: historical publication assets, no changes authorized.

## Completion gates

- [x] endpoint proof completed or refuted within the stated scope;
- [x] claims and non-implications classified correctly;
- [x] checker audits every adjacent edge and exact margin with `Fraction`;
- [x] exact checker passes normally and under optimized/no-site execution;
- [x] 60/100-digit diagnostics remain explicitly non-proof;
- [x] task-local/production convention comparison passes without a production
  import in the exact checker;
- [x] independent reviews of the actual proof note and checker pass;
- [x] relevant regression tests pass;
- [x] durable memory updated only after an exact conclusion;
- [x] `git status --short --untracked-files=all` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct whitespace checks and `git diff --check` pass;
- [x] no incidental generated or protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The exact endpoint theorem, checker, diagnostic separation, independent
reviews, regression run, durable-memory updates, and complete diff audit are
finished. The result is limited to one formal Supnick seam. After acceptance,
the sole next atomic task is the bounded radius-8 diagnostic localization on
`33<=n<=140`; it is not started here.
