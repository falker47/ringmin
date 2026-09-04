# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=2a7ccef05a2217146387e92507b2eab9910a174f
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__adjacent_high_swap
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Resolve the exact fixed-R variation of the permuted alternating-halves
criterion under an adjacent high swap, after bounded sign falsification.

`research/PERMUTED_HALVES_ADJACENT_SWAP.md` gives the two changing cells,
the explicit finite/infinite branch threshold, the closed local increment,
conditional exchange with equality cases, a small-R necessary candidate
structure and a minimal robust sign reversal. It identifies the failed
low/high increasing-differences property while preserving the high/high
one. Cyclic shifts are excluded in an exact stated small-R subdomain.
The sole stable claim owner is `knowledge/FIXED_ORDER_THEORY.md`.

### Allowed delta

The new swap proof note, the owning fixed-order ledger, the ranked roadmap,
this file and `ops/TASK-20260905__adjacent_high_swap/`.

### Verification gates

- Pre-proof bounded falsification: exit 0, 872 permutations for m=2..6,
  15114 ascending cyclic swaps and 5232 fixed-R shift comparisons.
- Exact proof: complete, including m=2, m=3, both seam swaps, threshold
  equality/infinity, sign/equality conditions and the small-R reduction.
- Symbolic/rational and independent 70-digit checker: exit 0; retained
  counterexamples enclosed exactly; 30228 swaps and 12000 conditional
  probes, maximum local/full atan discrepancy 2.8978173e-70.
- Additional positive-real probes cover all nine increment-branch pairs
  and finite/infinite threshold endpoints, separately from integer swaps.
- Final tracked/untracked content, whitespace and protected-path audit:
  passed; exactly three tracked modifications and six new allowed files,
  empty staged diff and no protected/generated changes. Explicit text
  audit covers all nine files; git diff --check exited 0, no output.

### Blockers and limitations

No blocker. Independent human proof review remains pending. Exact local
inequalities and finite numerical observations are distinguished in the
dossier; no global certificate or hosted CI claim is made. Necessary local
conditions do not prove arbitrary local minima global. The small-R
reduction is not transferred to closure radii. General permutation/root
optimization and asymptotics were not started; existing bounds and finite
certified scope are unchanged.

Protected: the preceding fixed-order proof, other prior notes/dossiers,
paper_assets/, results/, src/, tests/, scripts/, verify.py, publication
metadata, README, REPORT, other knowledge ledgers, PROJECT_KNOWLEDGE.md,
AGENTS.md and the review protocol. No Git/GitHub state writes.

## Exactly one next atomic task

Independently review the adjacent-high-swap theorem: locality and wraps,
finite/infinite threshold branches, conditional signs and equality,
small-R reduction and minimal counterexample. Check its fixed-order
dependency, reproduce the bounded checks and record acceptance or precise
corrections without beginning general permutation/asymptotic optimization.
