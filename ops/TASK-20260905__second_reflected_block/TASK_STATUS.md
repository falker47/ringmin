# Task Status

```text
task=TASK-20260905__second_reflected_block
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
task_base_head=a7c2afbeadcd2d8de69f79c073cf5f6379c06345
```

## Objective

Resolve the shrinking second reflected-block direction of the baseline
coupling at (alpha_hat,lambda_hat), lambda_hat=(1+alpha_hat)*x_*.
Derive the exact width first variation and first nonzero term, retain
both full-max branches, and prove a sign with exact gates.

## Scientific question and inputs

For each fixed lambda_hat<u<1-alpha_hat and 0<epsilon<1-alpha_hat-u,
replace only the diagonal slab [u,u+epsilon] by the symmetric pair of
high coordinates A+t and A+2*u+epsilon-t. The baseline coefficient,
the exact alpha_hat/x_* brackets and local-balance definition are
imported from the current proof notes. Their minima are not recomputed.
The new result concerns the continuum full-cost functional only.

## In scope and expected delta

- research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md: authoritative proof.
- This dossier and check_second_block.py: bounded stdlib exact gates.
- knowledge/FIXED_ORDER_THEORY.md: sole owner of the new continuum claim.
- CURRENT_STATUS.md and research/NEXT_RESEARCH_STEPS.md.

## Out of scope and protected paths

Finite permutation recovery, multiparameter optimization, moving block
centers, wrap-crossing blocks, general permutation enumeration and new
geometric/global bounds. Previous proof notes and dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, README.md, REPORT.md,
publication metadata, other knowledge ledgers, PROJECT_KNOWLEDGE.md,
AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md remain protected.
No Git history or GitHub writes are authorized.

## Verification design

Prove exact integral identities separately on the two smooth branches;
use the positive-part formula at the diagonal switch. Check rational
admissibility of one fixed witness, branch gates without unsafe squaring,
reflection moments, formal Taylor coefficients and explicit remainder
constants. A separate eight-panel midpoint upper enclosure with rational
square-root bounds checks the raw witness cost. All checks are bounded,
deterministic and stdlib-only; no numerical minimizer, floating quadrature,
permutation score or search is used.
Inspect all tracked and untracked changes and unchanged dependencies.

## Completion gates

- [x] Full-max formula and exact marginals/balance established.
- [x] Width derivative, first nonzero terms and equality cases proved.
- [x] Exact rational continuum counterexample established.
- [x] Bounded independent exact checker passes.
- [x] Continuum and finite recovery/global consequences separated.
- [x] Proof, dossier, owning ledger and navigation updated.
- [x] Complete tracked/untracked review and whitespace checks pass.
- [x] Protected/generated paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. Imported baseline theorems remain explicit dependencies; no new
external acceptance of them or of this task is recorded.

## Handoff

The exact continuum proof is complete. The width derivative vanishes
everywhere; the first nonzero term is cubic negative for fixed u!=a and
quadratic positive at a=A/3. One rational block gives a strict continuum
gap. The final checker exits 0; the eight-file source/whitespace audit,
four dependency comparisons, links and complete diff review pass.
Protected/generated paths, HEAD and the staged diff are unchanged.
READY_FOR_REVIEW; no finite recovery or global improvement is claimed.

Exactly one next atomic task: construct deterministic high permutations
recovering the fixed block [1/3,1/3+1/100] at the baseline, before using
the full-root transfer for a geometric bound. Do not optimize parameters.

Suggested manual commit message:
`research: prove second reflected-block continuum descent`.
