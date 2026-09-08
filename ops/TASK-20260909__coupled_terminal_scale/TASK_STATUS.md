# Task Status

    task=TASK-20260909__coupled_terminal_scale
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-09
    updated_at=2026-09-09

## Objective and scientific question

Resolve whether G_{k,n}=o(n^2) for every fixed k>=1 when one deletes
only k from {k,...,n}. Use constructive tours and analytic angular,
seam and closure derivative bounds; explicitly cover k=1 and k=2.

## Expected delta and in scope

Eight paths: research/COUPLED_TERMINAL_ONE_LEVEL_ASYMPTOTICS.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; CURRENT_STATUS.md;
research/NEXT_RESEARCH_STEPS.md; this dossier's TASK_STATUS.md,
TASK_LOG.md, EVIDENCE.md and check_scale.py. Initial tree clean at
f03f6267ea98cf5c3a709595721ec322114c405b on main. The base finite proof
is an input, not independently accepted by this task.

## Protected paths and out of scope

All previous proofs/dossiers, other knowledge modules, PROJECT_KNOWLEDGE.md,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/, results/, src/,
tests/, scripts/, verify.py, README.md, REPORT.md, publication metadata
and CI. No third-block work, finite certification expansion, historical
paper change, factorial enumeration, exact finite minimax computation or
optimization of more widely separated subsets.

## Completion gates

- [x] Analytic resolution with explicit all-n and fixed-k statements.
- [x] Claims classified and k=1,k=2 covered explicitly.
- [x] Bounded exact, symbolic and independent diagnostic checks.
- [x] Sole owning ledger, status and roadmap updated.
- [x] Complete tracked and untracked diff/whitespace/protection audit.
- [x] READY_FOR_REVIEW for authorized integration; acceptance is separate.

Final record edits are inspected/restaged before commit and normal
origin/main push. Staged inspection and whitespace checks precede that
integration; the final handoff records actual SHA, push result and tree.

## Blockers and handoff

No blocker. The proof establishes 0<=G_{k,n}<=n/2 uniformly,
and exact equality G_{k,n}=0 for n>=48k(k+1)^2. Cutoffs are sufficient,
not sharp; comparison tours assert only chain closure. Independent
mathematical acceptance remains separate.

Exactly one proposed next atomic task: independently review this one-level
gain theorem and its constructive/derivative/cutoff arguments at committed
HEAD, reproducing the standalone checker and recording acceptance or
corrections before further research.
