# Task Status

```text
task=TASK-20260804__radius4_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove or refute the proposed exact radius-4 formal Supnick seam onset
`s_4=21` by reusing `research/FIXED_K_SUPNICK_SEAM.md` in full and closing
only the exact endpoint bridge at `n=20,21`, preferentially with the rational
separator `R=50`.

## Scientific question

For the chain-minimizing Supnick cycle on `{4,...,n}`, determine exactly
whether

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.
```

**Outcome:** all four inequalities hold exactly. The already-proved fixed-`k`
theorem therefore gives `Delta_{4,n}>0` for `6<=n<=20` and
`Delta_{4,n}<0` for every `n>=21`. Thus `s_4=21` is now an exact theorem for
the formal seam `(n,4,n-1)`.

## In scope

- one authoritative radius-4 endpoint proof note;
- a task-local stdlib-only checker with exact `Fraction` audits of all
  threshold margins, adjacent-edge tables, and rational totals;
- optional finite high-precision scans labeled diagnostic only;
- durable memory/status/roadmap updates only if the exact classification is
  established.

## Out of scope

- reproving the general fixed-`k` theorem;
- full fixed-order feasibility or any all-pairs placement claim;
- claims about `R*(n)`, global optima, contact graphs, or floating circles;
- changes to the arXiv-v1 paper, certification artifacts, production code,
  tests, or `verify.py`.

## Expected delta

- `research/RADIUS4_SEAM_ONSET.md`;
- `ops/TASK-20260804__radius4_seam_onset/{TASK_STATUS.md,TASK_LOG.md,EVIDENCE.md,check_seam.py}`;
- conditional exact-classification updates to `PROJECT_KNOWLEDGE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, and `CURRENT_STATUS.md`.

## Protected paths potentially affected

- `research/FIXED_K_SUPNICK_SEAM.md`: read-only theorem source;
- `paper_assets/`: historical publication assets, no changes authorized;
- `results/`, `verify.py`: certificate chain, unrelated and protected;
- `src/`, `tests/`: production implementation and regression suite, no source
  changes authorized.

## Completion gates

- [x] endpoint proof completed or refuted within the stated scope;
- [x] claims and non-implications classified correctly;
- [x] checker audits every adjacent edge and every exact margin with
  `Fraction`;
- [x] exact checker passes with diagnostics disabled and under `python -O -S`;
- [x] opt-in numerical diagnostics, if run, are labeled non-proof;
- [x] task-local/production convention comparison is run without importing
  production code into the checker;
- [x] relevant regression tests pass;
- [x] durable memory updated only after an exact conclusion;
- [x] `git status --short --untracked-files=all` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] `git diff --check` and direct untracked whitespace checks pass;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

Exact theorem, checker, durable-memory synchronization, and final diff audit
are complete. Residual scope is confined to the formal seam. The next atomic
task, after acceptance, is the bounded diagnostic localization of the
radius-5 endpoint candidate described in the ranked roadmap.
