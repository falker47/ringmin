# Task Status

```text
task=TASK-20260905__three_marginal_relaxation
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective and scientific question

Determine whether the continuum three-marginal relaxation of the exact
permuted-halves full criterion can certify C_shift against all high
permutations. Derive the uniform scaling and necessary limiting marginals,
then prove either a sufficient dual lower bound or an explicit strictly
cheaper admissible coupling.

## In scope and expected delta

- research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md;
- knowledge/FIXED_ORDER_THEORY.md, the sole owner of these family claims;
- research/NEXT_RESEARCH_STEPS.md and CURRENT_STATUS.md;
- this dossier and a bounded independent checker.

## Out of scope and protected paths

All preceding proof notes and dossiers, other knowledge ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/,
results/, src/, tests/, scripts/, verify.py, README.md, REPORT.md and
publication/release metadata. No Git/GitHub writes, factorial enumeration,
permutation optimization, continuum recovery theorem or new global bound.

## Verification design

The exact full criterion and the analytic shift-family minimum are imported
from their authoritative proof notes. Derive angular remainder estimates
uniformly in every high permutation, including the low seam. Audit exact
rational/algebraic gates for the coupling, its marginals and a positive
cost gap. Bounded deterministic diagnostics may use four prescribed orders
at m=2,3,4,8,16,32,64,128 and c=1/10,1/7,1/5, plus 70-digit integrals.
Use an alternate angular formula and guard 1e-55; no numerical optimization
or LP is required after the analytic reflection construction was found.
Neither numerical integration nor finite probes are proof premises.

## Completion gates

- [x] uniform cell/root limit and necessary marginal conditions proved;
- [x] explicit coupling or dual resolves the discriminator rigorously;
- [x] bounded independent checks and exact scalar gates pass;
- [x] owning ledger, roadmap, current status and dossier synchronized;
- [x] complete tracked/untracked content and whitespace review;
- [x] no incidental protected/generated changes;
- [x] READY_FOR_REVIEW handoff.

## Blockers

None. Clean startup at HEAD 4b40aebddad73f09e453b5f17c3100852c780991.
Git reads use a per-command safe.directory override; no persistent Git
configuration was changed. Default git startup failed on sandbox ownership;
the override succeeded, with user-global ignore-file permission warnings.

## Handoff

The explicit coupling resolves the discriminator negatively, with an
analytic strict cost saving. Exact gates and every bounded diagnostic
passed locally. All eight changed files passed the final file audit.
Independent human review of
the proof and its imported dependencies remains required. The relaxation
value, optimal permuted-halves radii and R*(n) remain separate.

Suggested manual commit: research: refute three-marginal certification of shifts

Exactly one next atomic task: independently review this continuum
obstruction, including the uniform limit, necessary marginals, balance,
coupling, strict gap and imported full-criterion/shift-minimum dependencies;
reproduce the checker and record acceptance or precise corrections.
