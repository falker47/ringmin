# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=6bc4ac31b96ffcccb8fcfacf7478ae148a82bb2e
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__permuted_alternating_halves
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Prove or refute the exact cellwise full-feasibility criterion for
sigma_P=(1,P_1,...,m,P_m), with every permutation P of {m+1,...,2m},
every m>=2 and every R>0, after bounded independent falsification.

`research/PERMUTED_ALTERNATING_HALVES.md` proves the equivalence without
shift or monotonicity assumptions. A permutation-free shell triangle
inequality contracts every high path. Both directions for HH, LH and LL
pairs, all six pairs at m=2, m=3, the low seam and arbitrary high jumps
are explicit. The entire feasible gap set has only the local cell
inequalities and total length 2*pi.

Immediate fixed-order corollaries give the unique full-radius root, all
optimal gap vectors, and an exact chain/full equality criterion. The
owning ledger is `knowledge/FIXED_ORDER_THEORY.md`; the roadmap explicitly
states that the older coefficient 1/8 is disproved. No optimization or
asymptotics over permutations was started.

### Allowed delta

The new proof note, the owning fixed-order ledger, the ranked roadmap,
this file and `ops/TASK-20260905__permuted_alternating_halves/`.

### Verification gates

- Pre-proof falsification: exit 0, all 872 permutations for m=2..6,
  6104 independent all-pairs LP probes, no discrepancy.
- Exact proof with both directions and immediate corollaries: complete.
- Exact shell algebra, finite path topology and 70-digit angular/Cartesian
  corroboration: exit 0; 107388 exact path decompositions, 157 roots,
  1303 numerical path audits and 1146 Cartesian audits within guard.
- Complete tracked/untracked diff, whitespace and protected-path checks:
  pass; exactly three tracked and six new authorized files, no staged files.
- `git diff --check`: exit 0, no output; explicit whitespace and newline
  audit over all nine files also passed, including untracked additions.

### Blockers and limitations

No blocker. Independent human proof review remains pending. Finite LP and
high-precision checks are numerical observations, not proof premises or
global certificates. Existing global bounds and finite certified scope
are unchanged. Paper, production code, tests, verifier, certificates,
generated assets, README, REPORT, prior notes/dossiers, global ledger,
review protocol, AGENTS.md and PROJECT_KNOWLEDGE.md are protected. No
hosted CI claim is made.

## Exactly one next atomic task

Independently review the arbitrary-permutation fixed-order criterion,
both paths, small cycles, all wraps, optimal gap parametrization and
chain/full equality test; reproduce the bounded checks and record
acceptance or precise corrections without starting permutation asymptotics.
