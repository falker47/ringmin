# Task Status

```text
task=TASK-20260905__reflected_prefix_joint_minimum
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
task_base_head=5acbd8b894bfc052f9ad93ea106a34da1e2b7087
```

## Objective

Prove or refute unique joint minimization of the full-radius leading
coefficient on 0<=alpha<=1/2, 1/4<=lambda<1-alpha, after establishing
recovery and the coefficient formula for every fixed admissible pair.

## Scientific question and inputs

The unique global minimum of E on [0,1] at x_* and the unique minimum
of the fixed-x_* coefficient at alpha_hat are accepted inputs supplied
by the user. The new question is whether the complete two-parameter
family has the same unique minimum. Finite floors, all seam coincidences,
both alpha endpoints and arbitrarily small positive pre-wrap gaps remain
in scope. Fixed-order limits, actual feasibility and global limsup bounds
have separate quantifiers. No new external acceptance decision is made.

## In scope and expected delta

- New research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md.
- This dossier and a bounded, independent stdlib exact bookkeeping checker.
- knowledge/FIXED_ORDER_THEORY.md: new theorem's single thematic owner.
- knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md: cross-reference only; C_hat unchanged.
- CURRENT_STATUS.md and research/NEXT_RESEARCH_STEPS.md.

## Out of scope and protected paths

Finite-m family minimization, other alpha regimes, reflection crossing
the high wrap, general permutation/coupling or geometric optimization.
Previous proof notes and dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, README.md, REPORT.md, publication metadata, other
knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md remain protected. No Git/GitHub writes.

## Verification design

Use analytic recovery and positive-factor comparison of the two accepted
minima. New exact checks cover rational admissibility gates, finite floor
states for m=2..24, the corrected q=0 endpoint count, all exception unions,
nonexceptional coordinate errors, and specified near-wrap probes. Compare
the rank formula with independently rotated/reversed lists. No permutation
search, numerical integration, optimizer, random seed, old checker or
production/verifier import. Inspect all tracked and untracked additions.

## Completion gates

- [x] All-domain recovery and both full-cost branches derived.
- [x] Exact admissibility and unique joint minimum proved.
- [x] Fixed-order root, feasibility and global limsup separated.
- [x] Bounded independent exact checks pass.
- [x] Proof, dossier, owning ledger and navigation updated.
- [x] Complete tracked/untracked diff and whitespace checks pass.
- [x] Protected/generated paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. Complete imported full-feasibility and uniform-root theorems remain
explicit proof dependencies; their prior experiments are not rerun here.

## Handoff

The complete proof establishes the unique joint coefficient minimum at
(alpha_hat,(1+alpha_hat)*x_*). The new exact checker exits 0 for all
1692 valid cases and 8 invalid inputs. Complete tracked and untracked
review, all-file whitespace, source hashes, links and the protected-path
audit pass. The result is READY_FOR_REVIEW; external mathematical review
and manual integration remain separate. No Git/GitHub writes were made.

Exactly one next atomic task: independently review this joint theorem,
its bounded checker, accepted minimum dependencies and separate
full-feasibility/limsup deductions; record acceptance or precise corrections.

Suggested manual commit message:
`research: prove joint reflected-prefix family minimum`.
