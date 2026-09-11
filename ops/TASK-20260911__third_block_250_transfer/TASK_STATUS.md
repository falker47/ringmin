# Task Status

```text
task=TASK-20260911__third_block_250_transfer
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Close the geometric transfer gap for the fixed third width 1/250, or
identify a rigorous obstruction and stop.

## Scientific or engineering question

For the exact imported alpha_hat, x_*, epsilon_b, prove all-pairs
feasibility at the recovered even full-cell root and convergence of both
even and deleted odd normalized fixed-order minima to C_3(1/250).

## In scope

- New proof `research/PERMUTED_HALVES_THIRD_BLOCK_250_TRANSFER.md`.
- Independent bounded checker and this dossier.
- Fixed-order owning ledger, consequent global upper corollary, current
  status and materially changed roadmap upper endpoint/review priority.

## Out of scope

Other widths/parameters, tour enumeration, lower-bound research, finite
global certification, production changes and arXiv-v1 revision.

## Expected delta

Add the fixed-width recovery/transfer proof and checker; propagate only
its proved limits and global upper consequence without renaming old C_3.

## Protected paths potentially affected

- Earlier research notes and dossiers: compare tracked changed paths.
- Lower-bound proof and ledger entries: verify unchanged ranges.
- `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `src/`, `tests/`, `verify.py`,
  `results/`, `paper_assets/`, `README.md`, `REPORT.md`, CI and metadata:
  verify no diff; no artifact regeneration.

## Completion gates

- [x] bounded proof and claim classifications complete;
- [x] independent checker and rejection controls pass;
- [x] durable canonical sources updated without duplicate ownership;
- [x] complete new-file and tracked diff review, whitespace/link checks;
- [x] protected paths/ranges unchanged;
- [x] state set to READY_FOR_REVIEW for independent mathematical review.

Staged inspection, commit and normal push follow this precommit handoff;
the final response records their actual outcome rather than pre-asserting it.

## Blockers

None. Git needs command-scoped safe.directory under the sandbox identity;
no global configuration is changed.

## Handoff

Exact recovery at fixed 1/250, all-m even full-root feasibility, and
quantitative even/odd normalized limits are proved in the new note. Only
the corresponding global limsup is propagated. Bounded independent exact
checks pass; detailed commands, results and limitations are in EVIDENCE.md.
No global sharpness/limit, finite optimum, new lower bound or width
optimization follows. Exactly one next atomic task: independently review
this fixed 1/250 transfer at committed HEAD and reproduce its checker.
