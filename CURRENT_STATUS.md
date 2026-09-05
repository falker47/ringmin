# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=1636bf23cfadac46fb785bf6b1afda7e2787a466
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__permuted_halves_root_search
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Test whether the best cyclic high shift minimizes the exact full-radius
root rho_P among all high permutations, exhaustively within m=2..8,
with stopping at the first minimum-size counterexample.

The bounded search completed all 32 permutations at m=2,3,4, then stopped.
Exact rational separators establish m=4 as the least counterexample:
(8,7,5,6) uniquely minimizes over all 24, and strictly beats the unique
best shift (7,8,5,6). The detailed proof and scope are in
research/PERMUTED_HALVES_ROOT_SEARCH.md; the sole stable claim owner is
knowledge/FIXED_ORDER_THEORY.md. The local explanation uses a mixed/chain
swap, rigorously evaluated at the shift root.

### Allowed delta

The new root-search proof note, owning fixed-order ledger, ranked roadmap,
this file and ops/TASK-20260905__permuted_halves_root_search/.

### Verification gates

- Exhaustive 80-digit search: exit 0, m=2,3,4, 32 roots, all shifts.
- Independent 110-digit atan scorer and recursive enumeration: exit 0,
  same finite minimizers; maximum root midpoint discrepancy 1.79291546936e-71.
- Rational certificate: exit 0; all six m=3 orders, all 24 m=4 orders,
  all four shifts, four short root brackets and negative local root swap.
- Five artifact-corruption rejection checks: passed. Independent numerical
  witness reconstruction: 56 directed paths and 28 Cartesian pairs passed.
- Final tracked/untracked content, whitespace, provenance and protected-path
  audit passed: 3 tracked modifications and 8 new allowed files, empty
  staged diff; all 11 files checked explicitly. git diff --check exited 0,
  no output; no incidental protected/generated-file changes.

### Blockers and limitations

No blocker. Independent human review remains pending. The conjecture is
refuted by a finite certificate; no all-m minimizing structure is claimed.
m=5..8 were not run under the authorized stop rule. No general asymptotic
optimization, global R*(8) certification, production verifier run or hosted
CI claim is made. Existing global bounds and finite certified scope remain
unchanged. One erroneous chain-only diagnostic assertion was corrected to
the mixed/chain formula; its failed run is retained in the task log.

Protected: the preceding proof notes and prior dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, publication metadata, README,
REPORT, other knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md. No Git/GitHub state writes.

## Exactly one next atomic task

Independently review the minimal root counterexample: reproduce the 32
roots and rational separators, verify enumeration coverage and m=2,3
exclusion, audit the mixed/chain swap at the shift root and the imported
fixed-order criterion, and record acceptance or precise corrections.
Do not begin general permutation or asymptotic optimization.
