# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=460d705ff349340975feb51ea886d7a0f1aab08c
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__permuted_halves_local_stability
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Prove uniform local stability of the exact permuted-halves full-radius
root under boundedly many adjacent high-position swaps, and determine
what the first-two-high counterexample can change asymptotically.

The analytic proof, bounded checks and final diff review are complete.
The weighted root bound gives O_K(m)=o(m^2), with an explicit
one-swap family proving linear sharpness. The first swap of an interior
shift gives O(1/m), including eventually the best finite shifts. The
authoritative proof and exact quantifiers are in
research/PERMUTED_HALVES_LOCAL_STABILITY.md; the sole stable claim owner
is knowledge/FIXED_ORDER_THEORY.md. Global coefficients are unchanged.

### Allowed delta

The new local-stability proof note, owning fixed-order ledger, ranked
roadmap, this file and ops/TASK-20260905__permuted_halves_local_stability/.

### Verification gates

- Local checker: exit 0; three symbolic derivative identities and exact
  rational scalar gates, including the uniform m>=32 chord condition.
- Targeted reused rational scorer: four endpoint signs recheck the two
  m=4 root brackets and their strict gap; no enumeration or asset write.
- Independent 70-digit atan diagnostics: 67 swaps, 201 score/contraction
  probes, 90 distinct roots, and the sharper/linear examples at m=32,48,64;
  all passed. Numerical probes are not uniform proofs or interval roots.
- Final content, whitespace, local links, hashes and protected-path audit
  passed: 3 tracked modifications and 5 new files; empty staged diff.
  git diff --check exited 0 with empty stdout. All eight files were
  inspected explicitly, including every untracked addition.

### Blockers and limitations

No blocker. Independent human review remains pending. The full fixed-order
criterion and shift-family limit are imported mathematical dependencies.
No factorial enumeration, arbitrary-permutation optimization, global
R*(8) certification, production verifier run or hosted CI claim is made.
The m=4 minimality search was not rerun; only its two root brackets were
rechecked. Existing global bounds and finite certified scope are unchanged.

Protected: the preceding proof notes and prior dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, publication metadata, README,
REPORT, other knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md. No Git/GitHub state writes.

## Exactly one next atomic task

Independently review the uniform local-stability theorem: audit the
weighted two-cell bound, branch-safe root transfer, cyclic/small cases,
linear sharpness and O(1/m) shift refinement; reproduce the bounded
checker and inspect the imported fixed-order and shift-limit dependencies.
Record acceptance or precise corrections without beginning general
permutation optimization.
