# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=a7c2afbeadcd2d8de69f79c073cf5f6379c06345
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__second_reflected_block
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

The second shrinking reflected block preserves both high marginals and
local balance. Its width derivative vanishes everywhere. The first
nonzero full-cost term is cubic negative at each fixed u except A/3,
where a retained chord interval gives a quadratic positive term.
The rational block [1/3,1/3+1/100] is strictly cheaper in the continuum.
Proof: research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md. The existing
global limsup upper bound remains unchanged; no finite recovery is claimed.

### Allowed delta

New second-block proof, its task dossier and bounded exact checker;
knowledge/FIXED_ORDER_THEORY.md as sole owner; this file and the roadmap.

### Verification gates

- Analytic full-max formula, exact marginals/balance, all fixed-u signs
  and equality cases; explicit width ranges and switch remainder bound.
- Stdlib exact checker passes rational gates, sign-safe radical comparison,
  reflection moments, formal Taylor algebra and an independent exact
  eight-panel upper enclosure of the witness cost.
- Complete tracked diff and all five additions inspected. The eight-file
  source/whitespace audit, four dependency comparisons and four local
  links pass. git diff --check exits 0; HEAD/staged diff and all protected
  or generated paths are unchanged. READY_FOR_REVIEW.

### Blockers and limitations

No blocker. Baseline coefficient and exact minimizer brackets are imported.
No finite recovery, multiparameter optimization, general permutation
enumeration, moving-u theorem, wrap-crossing block, geometric global bound
or certificate extension is in scope. No Git/GitHub writes.

Protected: previous proof notes and dossiers, paper_assets/, results/,
src/, tests/, scripts/, verify.py, publication metadata, README.md, REPORT.md,
other knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md.

## Exactly one next atomic task

Construct deterministic high permutations recovering the fixed second
block [1/3,1/3+1/100] at alpha_hat, lambda_hat, before transferring its
full-radius cost or a geometric upper-bound consequence. Keep parameters
fixed and do not enumerate general permutations.
