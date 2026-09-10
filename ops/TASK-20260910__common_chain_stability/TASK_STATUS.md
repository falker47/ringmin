# Task Status

    task=TASK-20260910__common_chain_stability
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-10
    updated_at=2026-09-10

## Objective and scientific question

Prove or refute quantitative asymptotic stability for every common chain
tour on T_q(n), q=q_*=1/lambda_*, restricted to T_beta(n), beta=23/100.
Require explicit positive epsilon and delta, uniform root/edge reduction,
anti-Monge structure, and all integer floors and parities.

## In scope and expected delta

Eight paths: research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; research/NEXT_RESEARCH_STEPS.md;
CURRENT_STATUS.md; this dossier's TASK_STATUS.md, TASK_LOG.md, EVIDENCE.md
and check_stability.py. Initial tree clean at
0d46f6c7c2b0d44272b29803e1ba743f36732545 on main.
Only the global ledger owns the new stable claim. The index needs no change.

## Protected paths and out of scope

All previous proof notes/dossiers; other knowledge modules;
PROJECT_KNOWLEDGE.md; AGENTS.md; RINGMIN_REVIEW_PROTOCOL.md;
paper_assets/; results/; src/; tests/; scripts/; verify.py; README.md;
REPORT.md; publication metadata and CI. No R_full transfer, finite
certification, upper construction or broader common-tour optimization.

## Completion gates

- [x] Analytic theorem, explicit constants and uniform floors/parities.
- [x] Bounded independent arithmetic, symbolic and deletion checks.
- [x] Sole ledger, roadmap, current status and dossier updated.
- [x] Complete tracked/untracked inspection, whitespace and protected scope.
- [x] READY_FOR_REVIEW; external mathematical acceptance remains separate.

Final record edits are re-audited before staging. Staged inspection and
whitespace checks precede authorized commit and normal origin/main push.
The final handoff reports the actual integration SHA, push result and tree;
this pre-commit record does not assert a future remote result.

## Blockers and handoff

No mathematical blocker. The exact positive theorem gives epsilon=10^-12,
delta=10^-5 for all n>=10^14 and all common tours. The cutoff is conservative;
no broader optimization or geometric consequence is established here.
Exactly one next atomic task: independently review the quantitative common
chain stability theorem and checker at committed HEAD, recording acceptance
or corrections without extending to geometric or optimization work.
