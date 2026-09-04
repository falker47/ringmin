# Task Status

```text
task=TASK-20260904__finite_induced_subset_dominance
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute exact finite terminal dominance for the Supnick chain root
of every induced subset, and determine the sharp consequence for completely
arbitrary subset sequences and all cardinality regimes.

## Scientific question

For every `n`, `3<=N<=n`, and
`S={r_1<...<r_N} subset {1,...,n}`, decide whether the terminal set
`T={n-N+1,...,n}` satisfies

```text
R_chain(Supnick(S))<=R_chain(Supnick(T)),
```

then determine whether this closes every improvement of `C_term` obtainable
from one induced-subset chain bound without regularity assumptions on the
subset sequence.

## In scope

- an exact rank-edge and root-transfer proof, including equality;
- a terminal triangular-array limit covering every cardinality regime;
- the sharp finite envelope and arbitrary-sequence corollary;
- one small independent corroborative enumerator;
- the authoritative proof note, relevant cross-references, durable memory,
  status, roadmap, and this STRICT dossier.

## Out of scope

- genuinely coupled use of constraints from several induced subsets;
- `R_full`, geometric upper bounds, or true global asymptotics;
- finite certification, production search, result artifacts, or paper revision.

## Expected delta

Add one authoritative proof note and a four-file STRICT dossier; update the
two earlier subset notes only where their old `n`-dependent limitation is
superseded; synchronize `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the
ranked roadmap. No production, artifact, verifier, or publication file is
to change.

## Protected paths potentially affected

- `paper_assets/`: historical arXiv-v1 record; no change.
- `verify.py`, `results/`: finite certification; no change.
- `src/`, `tests/`, `scripts/`: production implementation; no change.
- unrelated research notes and prior dossiers: no change.

## Completion gates

- [x] finite proof and equality condition complete;
- [x] arbitrary terminal-array limit covers interior and both boundaries;
- [x] no-limit compactness and finite-envelope deductions complete;
- [x] claims and non-implications classified correctly;
- [x] independent finite corroboration run;
- [x] accepted dependency checks rerun;
- [x] durable memory updated;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct untracked whitespace audit and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None identified.

## Handoff

Finite terminal dominance, strict equality, all cardinality regimes, the
arbitrary-sequence bound, and sharp finite envelope are closed exactly.
All task-local, imported-dependency, diff, text, index, and protected-path
checks pass. Suggested manual commit: `Prove finite induced-subset dominance`.

Exactly one proposed next atomic task: independently review the rank-edge
convention, strict root transfer, both boundary limits, compactness/envelope
deduction, and coupled-method limitation; record acceptance or corrections.
