# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=c8f8c1e0ac665bfac794dc7214fab1112dafd120
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__supnick_feasibility_classification
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Classify full feasibility at the Supnick chain root for all integers
k>=1,n>=k+2. **Exact theorem / proved fixed-order corollary:** full
feasibility at R_{k,n} is equivalent to Delta_{k,n}>=0. Closure forces
all adjacent gaps tight. The generalized triangle and path lemmas establish
sufficiency in both directions, including adjacent complements, N=3,
N=4 and equality; a negative Delta violates the seam complement upper bound.

After that equivalence, the known strict signs give feasibility for
k+2<=n<s_k and infeasibility at the root for n>=s_k, with s_1=8, s_2=13,
s_3=17, s_4=21, s_5=25 and s_k=4k+6 for k>=6. No integer equality occurs.
The authoritative proof is research/SUPNICK_FULL_FEASIBILITY.md.

### Allowed delta

- The full-feasibility proof note, PROJECT_KNOWLEDGE.md and the roadmap.
- This file and ops/TASK-20260904__supnick_feasibility_classification/.

### Verification gates

- Local isolated exact audit, normal and optimized: exit 0; 9 general
  identities, exact N=3/N=4 checks, rational triangle root 6/23, 32 cycles,
  276 edges, 2964 directed paths, all rotations/reflections, 82 rejection gates.
- Separate 80-digit finite diagnostic: exit 0; 106 cases (82 feasible,
  24 infeasible), 445470 triangle defects and 29608 directed paths;
  Cartesian agreement and no counterexample. Falsification only.
- Complete tracked diff and all five additions inspected. Exact nine-file
  scope and UTF-8/LF/whitespace audit pass; git diff --check exits 0.
  HEAD, index and protected tracked paths unchanged.

### Blockers and limitations

No mathematical blocker identified; independent proof review and manual
integration remain pending. Imported exact seam theorems remain explicit
proof dependencies; no checker is a proof assistant. All conclusions are
fixed-order, with no global-optimum or floating-circle inference.

Production code, tests, verify.py, results, prior notes/dossiers and
arXiv-v1 assets are unchanged. Production pytest, the global verifier and
paper build are not required for this proof-only delta; hosted CI has not
been inspected. The recorded global certification scope remains 3<=n<=14.

## Exactly one next atomic task after acceptance

Independently review the complete fixed-order equivalence, including the
generalized triangle/path lemmas, closure-forced necessity, equality,
small cycles and imported strict-sign dependencies; record acceptance or
precise corrections. This review has not begun.
