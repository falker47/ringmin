# Task Status

```text
task=TASK-20260904__one_gap_terminal_subset_variation
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Determine whether the optimized terminal interval underlying `C_term` is
first-order locally optimal among single induced subsets obtained by deleting
one fixed `O(epsilon n)` interior band.

## Scientific question

Starting from the normalized interval `[1/lambda_*,1]`, derive the
arbitrary-radii Supnick continuum functional for one interior gap, compute its
one-sided first variation as `epsilon->0+`, and prove its sign for every fixed
interior normalized center. Treat both Supnick parities, rank reindexing, and
the order of limits explicitly.

## In scope

- a new authoritative proof note for the one-gap continuum variation;
- this dossier and task-local symbolic/finite checks;
- `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the sole roadmap if the
  theorem is completed.

## Out of scope

- general multi-gap or moving-center optimization;
- upper bounds or the true Ringmin leading coefficient;
- floating-circle or contact-graph claims;
- finite certification, production search, and paper revision.

## Expected delta

Add one proof note and one STRICT dossier, then update the three active memory
files with the exact sign result. No existing proof note or publication asset
is to be rewritten.

## Protected paths potentially affected

- `paper_assets/`: historical arXiv-v1 record; no change.
- `verify.py`, `results/`: finite certification; no change.
- `src/`, `tests/`, `scripts/`: production implementation; no change.
- prior research notes and dossiers: dependencies only; no change.

## Completion gates

- [x] continuum functional and proof complete within stated scope;
- [x] first variation and exact sign proof complete;
- [x] parity, reindexing, and iterated limits explicit;
- [x] claims classified correctly;
- [x] relevant independent symbolic and finite checks run;
- [x] durable memory updated;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct whitespace check and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None identified.

## Handoff

The continuum functional and one-gap variation are proved, every fixed
interior center has strictly negative variation, and the independent checks
and final scope/whitespace audits pass. Suggested manual commit:
`Prove one-gap local optimality of the terminal bound`.

Exactly one proposed next atomic task: independently review the continuum
pairing, first variation, exact sign, and iterated-limit statement; record
acceptance or precise corrections.
