# Task Status

```text
task=TASK-20260904__finite_union_terminal_dominance
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Close the logical gap in the single-induced-subset asymptotic lower bound by
proving that, at fixed normalized measure, the terminal interval maximizes
the already established quantile functional.

## Scientific question

For every fixed finite union of intervals `A subset [0,1]` of measure
`0<L<=1`, prove

```text
Q_A(t) <= 1-L+t,
C(A) <= C([1-L,1]) <= C_term,
```

with exact equality conditions. State precisely which fixed-subset
quantifiers the theorem covers and which diagonal, coupled-subset, or
geometric conclusions remain outside it.

## In scope

- the authoritative note that proves the continuum functional, including
  removal of its unnecessary positive-support restriction;
- one narrow cross-reference/limitation correction in the terminal theorem
  whose formerly open fixed-nonterminal case is now resolved;
- one task-local exact finite-grid audit of the quantile inequality and its
  equality case;
- this dossier, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the roadmap.

## Out of scope

- `n`-dependent normalized subsets or diagonal limits;
- coupled use of several induced subsets;
- geometric upper bounds or the true Ringmin coefficient;
- finite certification, production code, and paper revision.

## Expected delta

Extend the existing functional note to all positive-measure fixed finite
unions in `[0,1]`, then add one elementary distribution/quantile argument and
its equality proof; add this STRICT dossier and checker; update only the
three active memory/roadmap files and the one dependency note needed to
remove the superseded open claim.

## Protected paths potentially affected

- `paper_assets/`: historical arXiv-v1 record; no change.
- `verify.py`, `results/`: finite certification; no change.
- `src/`, `tests/`, `scripts/`: production implementation; no change.
- prior proof notes and dossiers other than the functional note: dependencies
  only, except the necessary limitation correction in
  `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`.

## Completion gates

- [x] continuum functional domain covers all stated fixed finite unions;
- [x] quantile dominance and equality proof complete within stated scope;
- [x] deduction from the accepted terminal optimization complete;
- [x] fixed versus `n`-dependent and single versus coupled-subset limits exact;
- [x] claims classified correctly;
- [x] task-local and dependency checks run;
- [x] durable memory updated;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct whitespace check and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None identified.

## Handoff

The continuum functional now covers all fixed positive-measure finite unions
in `[0,1]`. Terminal quantile dominance, both equality cases, dependency
checks, and final scope/whitespace audits pass. Suggested manual commit:
`Prove terminal dominance for fixed induced subsets`.

Exactly one proposed next atomic task: independently review the support-zero
functional extension, quantile/equality proof, terminal-optimizer import, and
fixed-subset quantifiers; record acceptance or precise corrections.
