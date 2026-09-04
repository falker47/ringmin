# Task Status

```text
task=TASK-20260904__increasing_order_full_asymptotics
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute the proposed all-`n` asymptotic upper coefficient
`1/(2*pi)` by analyzing the chain root and the full all-pairs problem for
the increasing cyclic order `(1,2,...,n)`.

## Scientific question

Determine rigorously whether the increasing order has

```text
R_full(1,2,...,n) = (1/(2*pi)+o(1)) n^2,
```

with an explicit feasible angular-gap distribution that controls both
directions of every pairwise constraint, especially paths crossing the
`(n,1)` seam when one endpoint is `o(n)`.

## In scope

- the exact leading asymptotic, with a quantitative remainder, of the
  increasing-order chain root;
- an explicit all-pairs feasible gap construction at a radius
  `(1/(2*pi)+o(1))n^2`;
- a rigorous seam audit, including a proof that chain closure alone is
  eventually infeasible;
- only the justified global `limsup` and `Theta(n^2)` consequences;
- an independent high-precision falsification/corroboration checker;
- the proof note, durable memory, roadmap, status, and this STRICT dossier.

## Out of scope

- existence or value of `lim R*(n)/n^2`;
- optimality or subleading optimality of the increasing order;
- a sharp estimate of `R_full(1,2,...,n)-n^2/(2*pi)`;
- finite global certification, production code, paper revision, or assets.

## Expected delta

Add one authoritative proof note and this four-file dossier. Update only
`PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the ranked roadmap. No
production, artifact, verifier, publication, or unrelated research file is
to change.

## Protected paths potentially affected

- `paper_assets/`: historical arXiv-v1 record; no change.
- `results/`, `verify.py`: finite certification; no change.
- `src/`, `tests/`, `scripts/`: production implementation; no change.
- `README.md`, `REPORT.md`, unrelated notes and prior dossiers: no change.

## Completion gates

- [x] chain-root asymptotic proved without presupposing its scale;
- [x] explicit gaps proved feasible for all pairs and both arcs;
- [x] seam and `o(n)` endpoint regimes controlled uniformly;
- [x] global consequences and non-implications stated exactly;
- [x] independent high-precision diagnostic run;
- [x] durable memory updated;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct untracked whitespace audit and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None identified.

## Handoff

The coefficient candidate is proved. The increasing order has chain root
`n^2/(2*pi)+O(n)` and full radius ratio tending to `1/(2*pi)` via explicit
all-pairs feasible gaps, even though its exact chain-root gaps eventually
fail at `(n,2)`. The only global deductions are the stated limsup and
`Theta(n^2)` after importing `C_term`. All analytic, independent diagnostic,
dependency, diff, text, index, and protected-path checks pass. Suggested
manual commit: `Prove increasing-order asymptotic upper bound`.

Exactly one proposed next atomic task: independently review the uniform
angular error, root transfer, seam obstruction, explicit two-path gap proof,
and limited global deductions; record acceptance or precise corrections.
