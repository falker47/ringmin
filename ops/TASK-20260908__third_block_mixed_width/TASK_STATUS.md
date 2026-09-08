# Task Status

    task=TASK-20260908__third_block_mixed_width
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-08
    updated_at=2026-09-08

## Objective and scientific question

Resolve the full continuous third-block width cost on tau_3<Delta<=h,
with alpha_hat, x_*, lambda and epsilon_b fixed at the accepted definitions.
Derive the derivative with the interior full-max switch retained; decide
monotonicity and, if it fails, prove a unique stationary point, rational
location and strict comparison with the current widths.

## Expected delta and scope

Eight paths: research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md;
knowledge/FIXED_ORDER_THEORY.md; CURRENT_STATUS.md;
research/NEXT_RESEARCH_STEPS.md; this dossier's TASK_STATUS.md,
TASK_LOG.md, EVIDENCE.md and check_mixed_width.py. The checker is limited
to two directed rational endpoint sign gates and rational implications.
Initial tree clean on main at b21c2dff20ca7419db56545c67386b369b8d24ac.

## Protected paths and out of scope

All prior proofs/dossiers, other knowledge modules, PROJECT_KNOWLEDGE.md,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/, results/, src/,
tests/, scripts/, verify.py, README.md, REPORT.md, publication metadata
and CI. No fixed-input reoptimization, width scan, finite recovery,
R_full transfer, new global coefficient, finite certificate or paper
revision. Protection was checked against the accepted input HEAD.

## Completion gates

- [x] Exact derivative and full-max switch cancellation.
- [x] Analytic curvature and endpoint signs on the whole mixed interval.
- [x] Unique stationary point, rational bracket and current-width comparison.
- [x] New bounded checker and relevant dependency checks.
- [x] Sole stable owner, status and roadmap updated.
- [x] Complete source/diff inspection and tracked/untracked whitespace audit.
- [x] Protected paths unchanged against the accepted baseline.
- [x] READY_FOR_REVIEW for authorized integration; external acceptance separate.

## Blockers and handoff

No blocker. Imported exact parameter theorems are premises. All three
checkers and the source audit exit 0. The audit verifies eight allowed
paths, four proof links, sole owner, Fraction-only checker with exactly
two gates, explicit untracked whitespace and 17 protected texts equal
baseline. Full source and complete staged diff were read. Explicit
eight-path staging, cached whitespace and absence of unstaged differences
each exit 0. Final record-only edits are inspected and restaged before
normal commit/push under Section 3; the final handoff records actual SHA,
push and remaining tree. Mathematical sources are unchanged.

One proposed next atomic task: independently review this mixed-width
continuous theorem and its two rational sign gates, stopping before any
finite/geometric transfer.
