# Task Status

```text
task=TASK-20260904__supnick_full_feasibility
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute seam dominance for every nonadjacent pair, in both cyclic
directions, of the Supnick chain on {k,...,4k+5} for every integer k>=6.
The intended consequence is fixed-order full feasibility at the exact
chain root, without a global-optimum or floating conclusion.

## Scientific question

The triangle defect has its exact minimum at middle radius k and endpoints
n-1,n for every R>0. At the chain root, the imported positive seam and
telescoping give slack >=(m-1)Delta for each m-edge path. This proves the
requested dominance and fixed-order full feasibility, with explicit
equality conditions and both parities. Classification: exact theorem /
proved fixed-order corollary, awaiting independent human review.

## In scope and expected delta

- research/SUPNICK_FULL_FEASIBILITY.md: authoritative proof or counterexample.
- This dossier, an independent symbolic/combinatorial audit and a small
  bounded numerical diagnostic for falsifying the intermediate lemma.
- PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md and the relevant roadmap entry.

## Out of scope and protected paths

AGENTS.md, paper_assets/, results/, src/, tests/, verify.py, README.md,
REPORT.md, generation scripts, dependencies and all prior notes/dossiers.
No global certification, global optimization, floating or paper revision.

## Completion gates

- [x] Resolve dominance with exact all-k reasoning or a certified counterexample.
- [x] Treat both cyclic paths, adjacent complements and both order parities.
- [x] Audit analytic identities independently of production/diagnostic code.
- [x] Classify claims and evidence; update durable memory.
- [x] Review tracked diff and every untracked addition; check whitespace.
- [x] Confirm protected paths unchanged; set READY_FOR_REVIEW.

## Blockers

None. Git ownership needs a command-local safe.directory override; no Git
configuration or history is written.

## Handoff

The proof in research/SUPNICK_FULL_FEASIBILITY.md establishes the exact
bound for every pair/path choice and identifies the two-edge seam as the
unique minimum up to reversal. Full feasibility is checked geometrically
and R_full=R_chain is concluded for this fixed order only.

The isolated exact audit passes six symbolic identities, 114 parity edges,
3180 directed paths and 11 rejection gates. Separate bounded diagnostics
pass for k=6,7,8,9; no finite scan is a proof premise. All nine changed
files are in scope, whitespace checks pass, and protected paths are unchanged.
The imported seam theorems were not reproved in this task. Independent
human proof review and manual integration remain outstanding.

Suggested manual commit: Prove Supnick seam dominance and fixed-order feasibility.

Exactly one next atomic task: prove or refute equivalence between full
feasibility at the Supnick chain root and Delta_{k,n}>=0 for all integers
k>=1, n>=k+2, treating small cycles, both paths and equality before applying
the known seam-onset classification. Keep it within the fixed-order problem.
That task has not begun.
