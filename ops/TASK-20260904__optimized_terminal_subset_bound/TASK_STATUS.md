# Task Status

```text
task=TASK-20260904__optimized_terminal_subset_bound
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Generalize the induced terminal-subset chain asymptotic from `n=4k+5` to
every fixed ratio `n/k -> lambda>1`, prove the exact optimization over
`lambda`, and record the best unconditional normalized lower bound supplied
by this deletion method.

## Scientific question

For integer sequences `k->infinity`, `n/k->lambda>1`, determine the limit of
`R_{k,n}/k^2` with both Supnick parities and uniform angular errors controlled.
Then maximize the induced coefficient in `R*(n)/n^2` analytically, including
boundary behavior and justified existence/uniqueness of the optimizer.

## In scope

- `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`;
- `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and
  `research/NEXT_RESEARCH_STEPS.md` if the theorem is completed;
- this dossier and task-local exact/symbolic independent gates.

## Out of scope

- production search and pruning;
- finite certificate artifacts and `verify.py`;
- `paper_assets/`, including the arXiv-v1 source and generated assets;
- new upper bounds, floating-set claims, or a proof of the true asymptotics;
- Git index/history and GitHub state.

## Expected delta

Replace the special-ratio asymptotic section by a parity-explicit sequential
limit theorem, analytically optimize its normalized coefficient, update the
three active memory files, and add independent exact/symbolic checkers plus
this dossier.

## Protected paths potentially affected

- `src/`, `tests/`, `scripts/`: inspect only; no implementation delta.
- `verify.py`, `results/`: no finite-certification delta.
- `paper_assets/`: historical arXiv-v1 record remains byte-unchanged.
- prior research notes and dossiers: dependencies only, not rewritten.

## Completion gates

- [x] generalized proof complete within stated scope;
- [x] exact optimization and boundary/uniqueness proof complete;
- [x] claims classified correctly;
- [x] independent exact/symbolic gate run;
- [x] numerical diagnostic clearly separated from proof premises;
- [x] durable memory updated only after the theorem succeeded;
- [x] `git status --short` inspected;
- [x] complete `git diff` and all untracked additions inspected;
- [x] direct whitespace check and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None. Independent human proof review and manual integration remain pending.

## Handoff

The general fixed-ratio limit and unique optimizer are proved. Exact and
symbolic independent gates pass, and the scoped final diff is clean. The
result is a lower bound only; true global asymptotics and stronger methods
remain open.

Suggested manual commit: `Optimize the terminal-subset asymptotic bound`.

Exactly one proposed next atomic task: independently review the generalized
limit, parity/end-point and uniform-error arguments, exact optimization, and
all-integer deduction; record acceptance or precise corrections.
