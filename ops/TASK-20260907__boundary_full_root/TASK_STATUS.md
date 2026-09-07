# Task Status

    task=TASK-20260907__boundary_full_root
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-07
    updated_at=2026-09-07

## Objective

Transfer the exact adjacent-block recovery to full radii for every m>=2,
prove explicit uniform normalized errors and the odd fixed-order limit,
and deduce the separate global bound with coefficient C_b<C_2.

## Scientific or engineering question

Keep exactly alpha_hat, lambda=(1+alpha_hat)*x_* and epsilon_b.
The second reflected block is mixed. Verify the arbitrary-high criterion
on every actual cell, transfer the complete maximum, and distinguish
deletion feasibility from the necessary-cell lower squeeze.

## In scope and expected delta

Ten paths: research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md; this dossier's
TASK_STATUS.md, TASK_LOG.md, EVIDENCE.md, check_full_root.py and
diagnose_full_root.py; knowledge/FIXED_ORDER_THEORY.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; CURRENT_STATUS.md;
research/NEXT_RESEARCH_STEPS.md.

## Out of scope and protected paths

All previous proofs/dossiers; other ledgers and PROJECT_KNOWLEDGE.md;
AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md; paper_assets/, results/,
src/, tests/, scripts/, verify.py, README.md, REPORT.md, publication
metadata and CI. No parameter optimization, additional block, global
enumeration, certificate regeneration or paper revision.

## Completion gates

- [x] Exact all-m full-root and all-pairs construction proved.
- [x] Complete mixed cost, uniform errors and odd lower squeeze proved.
- [x] Exact comparison gates establish C_b<C_2.
- [x] Independent bounded arithmetic and numerical checks pass.
- [x] Dossier, sole claim owners, status and roadmap updated.
- [x] Complete tracked/untracked sources inspected; whitespace clean.
- [x] Protected paths unchanged; state READY_FOR_REVIEW.
- [x] Staged diff and whitespace checked before authorized commit/push.

## Blockers

None. Prior theorems are imported as mathematical dependencies;
independent external acceptance remains separate.

## Handoff

The canonical proof and bounded checks are complete. The exact checker
passes 38 floor triples and 14091 cells; the numerical diagnostic passes
104779 pair checks and independent small even/odd all-pairs root checks.
The ten-path source audit, import/ownership gates and protected-text
comparisons pass. Staged diff and whitespace checks pass. Commit/push follows;
the containing
SHA, observed push result and final tree state belong to the final handoff.
This state is not external mathematical acceptance.

Exactly one next atomic task: independently review the boundary full-root
transfer, its mixed cost, uniform estimates, deletion lower squeeze and
strict comparison with C_2.
