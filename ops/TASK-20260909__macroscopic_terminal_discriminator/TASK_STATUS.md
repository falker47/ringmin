# Task Status

    task=TASK-20260909__macroscopic_terminal_discriminator
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-09
    updated_at=2026-09-09

## Objective and scientific question

Derive the parity-uniform chain coefficient of the restriction of the
Supnick cycle on {floor(q*n),...,n} to {floor(beta*n),...,n}, for every
fixed 0<q<beta<1. Decide its exact comparison with C_term at the existing
terminal optimizer q_*=1/lambda_*. Distinguish a common-order obstruction
from a candidate quadratic incompatibility; do not optimize common tours.

## In scope and expected delta

Eight paths: research/MACROSCOPIC_TERMINAL_DISCRIMINATOR.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; CURRENT_STATUS.md;
research/NEXT_RESEARCH_STEPS.md; this dossier's TASK_STATUS.md,
TASK_LOG.md, EVIDENCE.md and check_discriminator.py.
Initial tree clean at 73a58f7a448ae61b5baa26afbfaf428a9c91c859 on main.
Only the global-bounds ledger owns the stable new result; the compact
index's scope and navigation remain appropriate without modification.

## Protected paths and out of scope

Previous proofs/dossiers, other knowledge modules, PROJECT_KNOWLEDGE.md,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/, results/, src/,
tests/, scripts/, verify.py, README.md, REPORT.md, publication metadata
and CI. No coupled minimax optimization, R_full, finite certification,
new upper construction, paper revision or unrelated cleanup.

## Completion gates

- [x] Exact discrete arc accounting, both parities and the middle cutoff.
- [x] Uniform angular estimate and root bracket, with floors retained.
- [x] Analytic comparison at q_* and explicit beta interval.
- [x] Bounded independent corroboration and symbolic cross-check.
- [x] Sole ledger, roadmap, status and evidence updated.
- [x] Complete tracked/untracked diff and whitespace/protection audit.
- [x] READY_FOR_REVIEW for authorized integration; acceptance is separate.

Final record edits are inspected/re-audited before staging. Staged diff and
whitespace gates precede the authorized commit and normal origin/main push;
the final handoff records actual SHA, push result and working-tree state.

## Blockers and handoff

No mathematical blocker. Imported Supnick optimality and terminal
optimization retain their existing status; this task is not their external
acceptance. The exact result is Psi(q_*,beta)>C_term throughout
[1/5,23/100], with the full parity-uniform chain-limit formula in the
canonical proof. This is only a candidate of quadratic incompatibility;
common-tour minimax gain remains unresolved.

Exactly one proposed next atomic task: independently review this
discriminator at committed HEAD, reproduce the checker, and record
acceptance or corrections before common-tour optimization or geometric work.
