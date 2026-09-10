# Task Status

    task=TASK-20260910__two_level_minimax_bound
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-10
    updated_at=2026-09-10

## Objective and scientific question

Optimize the asymptotic two-level minimax consequence of the accepted
root sandwich, nonnegative dual excess and deletion estimate at q=q_*
and beta=23/100. Enclose the actual deletion integral by exact rational
arithmetic and transfer the result to R* only by full-feasible deletion.
Distinguish sharpness of the scalar estimate from sharpness for tours.

## In scope and expected delta

Eight paths: research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; research/NEXT_RESEARCH_STEPS.md;
CURRENT_STATUS.md; and this dossier's TASK_STATUS.md, TASK_LOG.md,
EVIDENCE.md and check_minimax.py. Base supplied as accepted by the user:
67742eddd05b4b61fc24c84820473ed8ee6bdc7a, clean main.

## Protected paths and out of scope

Input proof Sections 2-7 and the previous finite theorem; all other proof
notes and previous dossiers/checkers; other knowledge modules;
PROJECT_KNOWLEDGE.md; AGENTS.md; RINGMIN_REVIEW_PROTOCOL.md; paper_assets/;
results/; src/; tests/; scripts/; verify.py; README.md; REPORT.md;
publication metadata and CI. No enumeration, finite optimum certification,
upper construction, paper revision or optimization over q and beta.

## Completion gates

- [x] Analytic scalar minimax and its precisely scoped optimality.
- [x] Exact rational integral/coefficient enclosures and symbolic checks.
- [x] Separate full-feasible deletion; finite and liminf quantifiers.
- [x] Sole ledger, roadmap, current status and dossier updated.
- [x] Complete tracked/untracked inspection, whitespace and protected scope.
- [x] READY_FOR_REVIEW; external mathematical acceptance remains separate.

Final record edits receive the same audit. Staged inspection and whitespace
checks precede authorized commit and normal origin/main push. The observed
SHA, push result and working-tree state are reported in the final handoff;
this pre-commit record does not assert a future integration outcome.

## Blockers and handoff

No mathematical blocker. The exact eta_60=D^2/(3600*pi) exceeds 515 times
the old gap, with a rigorous rational enclosure. The proof gives a uniform
finite loss 3/n and transfers to R* only by full-feasible deletion.
Scalar sharpness for estimate (9) is not geometric sharpness or a ceiling
on its refinements. Independent external review remains separate.
Exactly one next atomic task: independently review the asymptotic minimax
extension and its dependencies at the committed HEAD.
