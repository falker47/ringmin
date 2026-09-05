# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=4b40aebddad73f09e453b5f17c3100852c780991
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__three_marginal_relaxation
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Determine whether the continuum three-marginal relaxation can certify
C_shift against all high permutations, using the exact full criterion.
The analytic proof gives a uniform empirical cost/root limit, necessary
marginals and an explicit balanced coupling strictly below the shift
target. The authoritative proof is
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md; the sole stable
claim owner is knowledge/FIXED_ORDER_THEORY.md.

### Allowed delta

The new proof note, owning fixed-order ledger, ranked roadmap, this file
and ops/TASK-20260905__three_marginal_relaxation/.

### Verification gates

- Exact symbolic/rational gates: exit 0; reflection saving, affine marginal
  maps, angular error identities and cell/score normalization passed.
- Bounded independent 70-digit atan/root/integral checker: exit 0;
  27 prescribed orders, 54 score probes, 2928 cells and 27 roots passed;
  the split integral and closed-form block agree within 1e-60.
- Final complete tracked/untracked content and whitespace inspection passed:
  3 tracked modifications, 5 additions, 3 local links and 4 recorded hashes;
  empty staged diff and no protected/generated changes. git diff --check
  exited 0 with empty stdout. All eight files were inspected explicitly.

### Blockers and limitations

No blocker. Independent human review remains pending. The exact full
criterion and analytic shift-family minimum are imported dependencies.
No factorial search or LP was run. The exact relaxation value, equality
with a permuted-halves optimum and realization of the coupling by
permutations remain unproved. No global bound or finite certificate is
changed; no production verifier or hosted CI claim is made.

Protected: preceding proof notes and dossiers, paper_assets/, results/,
src/, tests/, scripts/, verify.py, publication metadata, README, REPORT,
other knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md. No Git/GitHub state writes.

## Exactly one next atomic task

Independently review the three-marginal obstruction: audit uniform
cell/root scaling, limiting marginal and seam arguments, symmetrization,
the explicit coupling and strict analytic gap; reproduce the bounded
checker and inspect the imported full-criterion/shift-minimum dependencies.
Record acceptance or precise corrections without starting permutation
recovery or optimization.
