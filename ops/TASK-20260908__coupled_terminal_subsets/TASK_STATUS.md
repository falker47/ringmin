# Task Status

    task=TASK-20260908__coupled_terminal_subsets
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-08
    updated_at=2026-09-09

## Objective and scientific question

Decide whether minimizing the maximum of the two induced chain radii on
nested terminal sets T_N subset T_M always equals the maximum of their
separate Supnick minima, for integers 3<=N<M<=n. Resolve compatibility
analytically or give an exact counterexample with positive separation.

## Expected delta and scope

Eight paths: research/COUPLED_TERMINAL_SUBSETS.md;
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md; CURRENT_STATUS.md;
research/NEXT_RESEARCH_STEPS.md; this dossier's TASK_STATUS.md,
TASK_LOG.md, EVIDENCE.md and check_exact.py. Start at clean main, accepted
input HEAD 3c415b36ade354cfd9beff637ec98bb5cc6b7d0a (user-supplied acceptance;
the prior task's tracked status still says READY_FOR_REVIEW).

## Protected paths and out of scope

All prior proofs/dossiers, other knowledge modules, PROJECT_KNOWLEDGE.md,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/, results/, src/,
tests/, scripts/, verify.py, README.md, REPORT.md, publication metadata
and CI. No third-block refinement or Delta_* transfer, new finite global
certification, paper revision, general coupled-bound optimization or
asymptotic improvement claim.

## Completion gates

- [x] Exact counterexamples and positive separations.
- [x] Smallest ambient n under both inclusion conventions.
- [x] Compatibility distinguished from equality of the minimax bound.
- [x] Analytic proof with independently reproduced exact arithmetic gates.
- [x] Sole stable owner, status and scientific roadmap updated.
- [x] Full diff/addition inspection and whitespace/protected-path checks.
- [x] READY_FOR_REVIEW for authorized integration; external acceptance separate.

Final record-only updates are inspected/restaged before commit and normal
origin/main push; the final handoff records the actual SHA, push and tree.

## Blockers and handoff

No blocker. The proof gives an exact gap >1/6000 at n=M=8,N=7,
the smallest ambient counterexample when M=n is allowed. If M<n is
required, n=13,M=12,N=11 is minimal and has gap >1/5000. The all-tour
argument is analytic, using strict anti-Monge perturbation, the published
matrix-level Supnick theorem, and uniform root derivative bounds. Eight
rational closure gates pass by two formulas; the accepted triangle/seam
results exclude every smaller ambient n in the respective domain.

Residual limits: classical matrix theorem and analytic seam/path results
are imported; no exact minimax/global optimum, asymptotic gain or new
certificate. One proposed next atomic task: independently review this
coupled-subset theorem and reproduce its exact gates, stopping before
asymptotic amplification or further optimization.
