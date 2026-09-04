# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=00b330c09ec5609fad900d0f302f21cd258241c0
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__supnick_full_feasibility
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Prove or refute seam dominance for every nonadjacent pair in both cyclic
directions of the Supnick cycle on `{k,...,4k+5}`, for every integer k>=6.

**Classification: exact theorem / proved fixed-order corollary.** At the
exact chain root, every nonadjacent pair's path with m edges has slack
at least `(m-1)Delta>=Delta>0`, where Delta is the critical seam slack.
Only the two-edge seam attains the minimum, up to reversal. The formal
placement is fully feasible, and `R_full(sigma)=R_chain(sigma)` for this
fixed order and radius set.

The authoritative proof is `research/SUPNICK_FULL_FEASIBILITY.md`. It
minimizes every triangle defect analytically, telescopes along both paths,
and treats both exact edge parities including the even central correction.
The imported `D_5(k)<0` theorem supplies positivity after those comparisons.
No finite diagnostic is a proof premise.

### Allowed delta

- The full-feasibility proof note.
- `ops/TASK-20260904__supnick_full_feasibility/`: dossier, independent
  symbolic/combinatorial audit and separate bounded diagnostic.
- `PROJECT_KNOWLEDGE.md`, the relevant roadmap entries, and this file.

### Verification gates

- Isolated SymPy 1.14.0 audit: exit 0; six symbolic identities, four
  independent rank/parity constructions (114 edges), rotations/reflections,
  1590 unordered pairs / 3180 directed paths, and 11 rejection gates pass.
- Separate 80-digit diagnostic, k=6,7,8,9: exit 0; every triangle, both
  paths of every pair and Cartesian distances checked. Minimum nonadjacent
  slack is the two-edge seam in each case. Numerical observation only.
- Complete tracked diff and all six additions inspected. The nine-file
  UTF-8/LF/whitespace/scope audit and five source hashes pass; git diff
  --check exits 0 with no output. HEAD and protected paths unchanged.

### Blockers and limitations

No mathematical blocker. Independent proof review and manual integration
remain outstanding. The audit is independent
of production code but is not a proof assistant or a reproof of the
imported seam theorems. No global-optimum or floating claim is made.

Global certification remains 3<=n<=14. Production code, tests, verify.py,
results, prior notes/dossiers and arXiv-v1 assets are unchanged. The global
verifier, production pytest suite and paper build are not required for
this proof-only task; hosted CI and an external reviewer have not been inspected.

## Exactly one next atomic task after acceptance

Prove or refute equivalence between full feasibility of the formal Supnick
placement at its chain root and `Delta_{k,n}>=0` for all integers k>=1,
n>=k+2. Treat small cycles, both directions and equality explicitly, then
apply the known seam-onset classification within the fixed-order problem.
This task has not begun.
