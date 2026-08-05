# Task Status

```text
task=TASK-20260805__radius6_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-05
updated_at=2026-08-05
```

## Objective

Prove or refute the proposed exact radius-6 formal Supnick seam onset
`s_6=30` by importing `research/FIXED_K_SUPNICK_SEAM.md` in full and closing
only `n=29,30` at the common rational separator `R=211/2`.

## Scientific question

For the chain-minimizing Supnick cycle on `{6,...,n}`, do exact endpoint
bounds establish

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30},
```

and hence, using only the imported persistence theorem, prove `s_6=30` for
the single formal seam `(n,6,n-1)`?

## In scope

- one authoritative radius-6 endpoint proof note;
- complete 24- and 25-edge Supnick closure tables at `R=211/2`;
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

- `research/RADIUS6_SEAM_ONSET.md`;
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

The exact endpoint theorem, checker, 60/100-digit diagnostic separation,
production-convention comparison, regression run, durable-memory updates, and
diff audit are complete. The result is limited to one formal Supnick seam.
After acceptance, the sole next atomic task is the bounded radius-7 diagnostic
localization on `29<=n<=120`; it is not started here.
