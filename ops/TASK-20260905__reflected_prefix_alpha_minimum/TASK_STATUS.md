# Task Status

```text
task=TASK-20260905__reflected_prefix_alpha_minimum
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
task_base_head=4f32b37241578064667b5db7214c3d16d83e4859
```

## Objective and scientific question

Prove unique minimization in alpha on [0,1/2] at the accepted fixed x_*,
isolate the minimizer between 1093/10000 and 10931/100000, and derive a
strict improvement over C_107. Extend recovery to this closed domain and
keep the fixed-order full-radius, actual feasibility and global deletion
statements separate. Mode STRICT; no decimal is a proof premise.

## In scope and expected delta

- New research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md.
- This dossier and an independent, bounded check_alpha_minimum.py.
- knowledge/FIXED_ORDER_THEORY.md: family theorem and coefficient owner.
- knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md: global corollary owner.
- CURRENT_STATUS.md and research/NEXT_RESEARCH_STEPS.md.

## Out of scope and protected paths

Other alpha regimes, joint parameter optimization, general permutations or
couplings, global optimality and normalized global limit existence.
Previous proof notes and dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, publication metadata, README.md, REPORT.md, other
knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md remain protected. The user's subsequent explicit
request authorizes commit and push of exactly this nine-file task delta;
independent mathematical review remains separate from integration.

## Verification design

Prove global curvature and domain endpoint signs analytically. Isolate only
the required constants with stdlib rational square-root and concave-integral
bounds: E at the rational midpoint of the accepted x_* bracket, and D at
the two requested alpha endpoints. Bound the displacement from E(x_*)
analytically, including the full block switch. Fixed budgets: 2048 panels
per block integral, 256 per D integral, 64 switch bisections, square-root
grid 10^-24; no search or random seeds. Audit only m=2..16 and endpoint
parameters for the newly extended floor/seam domain. Optional independent
70-digit full-max quadrature checks the new gates and normalization.

## Completion gates

- [x] Whole-domain recovery, full cost and strict convexity.
- [x] Exact endpoint signs, tight bracket and strict coefficient comparison.
- [x] Separate full-root, feasibility and global deletion theorems.
- [x] Independent bounded exact checker and diagnostic cross-check.
- [x] Dossier, two owners, CURRENT_STATUS and roadmap updated.
- [x] Complete tracked/untracked inspection and whitespace checks.
- [x] Protected paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. The user supplies the existing coefficient formula and x_* result
as accepted inputs. Their complete proofs remain explicit dependencies;
this task does not record a new external acceptance decision for them.

## Handoff

The bounded task is READY_FOR_REVIEW. The analytic proof and isolated exact
gates confirm the requested bracket and prove C_hat<C_107-1/22000000.
Both checker modes exit 0. The complete file, provenance and whitespace
audit passes; protected sources, staged diff and HEAD are unchanged.
The imported full-feasibility/root theorems remain explicit dependencies;
no external acceptance or global optimality/limit claim is recorded.
The user subsequently requested commit and push; that authorization leaves
the mathematical review state READY_FOR_REVIEW.

Exactly one next atomic task: independently review this whole-domain
alpha-minimum theorem and its bounded checker, recording acceptance or
precise corrections without starting further parameter optimization.

Suggested manual commit message:
`research: prove exact alpha minimum of reflected prefix at fixed x`.
