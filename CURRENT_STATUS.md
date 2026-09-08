# Current Status

## Repository snapshot

    repository=falker47/ringmin
    task_base_head=73a58f7a448ae61b5baa26afbfaf428a9c91c859
    observed_on=2026-09-09
    phase=post-arXiv-v1 active research

## Current task

    task=TASK-20260909__macroscopic_terminal_discriminator
    mode=STRICT
    state=READY_FOR_REVIEW

### Objective and current result

Derive the exact asymptotic coefficient of the restriction of S_q(n) to
T_beta(n) for fixed 0<q<beta<1. The proof in
research/MACROSCOPIC_TERMINAL_DISCRIMINATOR.md gives the two integral
branches, the midpoint transition and a parity-uniform O(1/n) normalized
root error. At q_*=1/lambda_*, analytic rational inequalities prove
Psi(q_*,beta)>C_term for every beta in [1/5,23/100]. This is a candidate
of quadratic incompatibility of the prescribed order, not a positive
lower bound on the minimax over common tours. C_term is unchanged.

### Allowed delta

Eight paths: new canonical proof; scoped STRICT dossier with one standalone
bounded checker; global-bounds ledger; this file; roadmap. Initial tree
clean at the base HEAD above. Only the global-bounds ledger owns the new
stable theorem. The compact index needs no change.

### Verification gates

- Analytic proof covers the actual surviving and replacement arcs, both
  parities, floors, midpoint, angular error and prior root bracket.
- Local standalone checks pass 13,113 prescribed restrictions, four exact
  rational Taylor gates and interval implications, five symbolic identities
  and 28 optional numerical chain-root diagnostics. Numerics are diagnostic.
- Complete new sources and tracked diff inspected. The eight-path audit
  passes whitespace including untracked additions, five local links,
  isolated imports, sole ownership and ten protected source comparisons.
  git diff --check exits 0. Final record edits are inspected/re-audited.
- Authorized staging, staged-diff checks, commit and normal origin/main push
  follow; the final handoff records actual SHA, push result and tree.
- Independent mathematical acceptance and hosted CI remain separate.

### Blockers and limitations

No blocker. Supnick optimality and the terminal optimizer are imported.
The positive restricted-order excess is not uniform over competing common
tours. No minimax optimization, stronger global lower coefficient, R_full,
certificate, new upper construction or paper revision is supplied.

Protected: previous proofs/dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, README.md, REPORT.md, publication metadata and CI;
other knowledge modules, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md.

## Exactly one next atomic task

Independently review the macroscopic discriminator at committed HEAD:
exact induced edges and counts, floors/parities and midpoint, root transfer,
rational interval comparison and the distinction from a minimax lower
bound. Reproduce the standalone checker and record acceptance or corrections;
stop before common-tour optimization, R_full, certification or upper work.
