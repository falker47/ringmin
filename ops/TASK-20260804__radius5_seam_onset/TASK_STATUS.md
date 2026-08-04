# Task Status

```text
task=TASK-20260804__radius5_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove or refute the proposed exact radius-5 formal Supnick seam onset
`s_5=25` by reusing `research/FIXED_K_SUPNICK_SEAM.md` in full and closing
only the exact endpoint bridge at `n=24,25` with the rational separator
`R=75`.

## Scientific question

For the chain-minimizing Supnick cycle on `{5,...,n}`, establish or refute
exactly

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.
```

**Outcome:** all four inequalities hold exactly. The already-proved fixed-`k`
theorem therefore gives `Delta_{5,n}>0` for `7<=n<=24` and
`Delta_{5,n}<0` for every `n>=25`. Thus `s_5=25` is now an exact theorem for
the formal seam `(n,5,n-1)`.

## In scope

- one authoritative radius-5 endpoint proof note;
- complete 20- and 21-edge Supnick tables at `R=75`;
- a task-local checker whose default exact path uses only the standard
  library and `fractions.Fraction` arithmetic;
- optional finite high-precision scans labeled diagnostic only;
- durable memory/status/roadmap updates only if the exact all-`n` formal-seam
  classification is established.

## Out of scope

- reproving or changing the general fixed-`k` theorem;
- full fixed-order feasibility or any all-pairs placement claim;
- claims about `R*(n)`, global optima, contact graphs, or floating circles;
- changes to the arXiv-v1 paper, certification artifacts, production code,
  tests, or `verify.py`.

## Expected delta

- `research/RADIUS5_SEAM_ONSET.md`;
- `ops/TASK-20260804__radius5_seam_onset/{TASK_STATUS.md,TASK_LOG.md,EVIDENCE.md,check_seam.py}`;
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
- [x] checker audits every adjacent edge and exact margin with `Fraction`;
- [x] exact checker passes normally and under optimized/no-site execution;
- [x] opt-in numerical diagnostics, if run, remain labeled non-proof;
- [x] task-local/production convention comparison is run without adding a
  production import to the checker;
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
radius-6 endpoint candidate on `25<=n<=100` described in the ranked roadmap.
