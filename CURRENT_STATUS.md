# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=512e8ffb113221666438e11877f317ca7a70646f
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__one_gap_terminal_subset_variation
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Determine the first variation of the optimized terminal-subset coefficient
when one fixed normalized interior band is deleted.

**Exact continuum theorem / proved first-order local-optimality corollary.**
For a finite union `A` of normalized intervals, with increasing quantile
`Q_A` and length `L`, the arbitrary-radii Supnick chain root has coefficient

```text
C(A)=(2/pi) integral_0^(L/2) sqrt(Q_A(t)Q_A(L-t)) dt.
```

Let `alpha=1/lambda_*`, `s=1+alpha`, and delete a band of total normalized
width `epsilon` centered at a fixed `x in (alpha,1)`. If
`theta=asin sqrt(x/s)`, then, with `n->infinity` taken before
`epsilon->0+`,

```text
C_epsilon(x)=C_term+epsilon V(x)+o(epsilon),
V(x)=(s/pi)[pi/4-theta-sin(theta)cos(theta)]<0.
```

The sign follows exactly from `tau=cos(tau)`: the bracket vanishes at the
excluded lower endpoint `alpha`, and its derivative with respect to `theta`
is `-2cos(theta)^2<0`. Hence every fixed interior one-gap deletion is
strictly worse for sufficiently small positive width. There is no positive
first variation and therefore no stronger concrete one-gap lower bound to
construct.

Authoritative proof:
`research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`.

### Allowed delta

The new proof note, this file, `PROJECT_KNOWLEDGE.md`, the roadmap, and
`ops/TASK-20260904__one_gap_terminal_subset_variation/`.

### Verification gates

- Analytic proof retains both Supnick parities, seam and even central edge,
  quantile discontinuities, uniform angular/root scaling, all three gap
  positions, and the iterated order of limits.
- Task-local symbolic identity audit: pass.
- Independent finite rank-edge and continuum diagnostic: pass.
- Complete tracked diff and all six untracked additions inspected. The exact
  three-modification/six-addition scope, strict UTF-8/LF/final-newline and
  whitespace checks, empty index, protected paths, and `git diff --check`
  pass.

### Blockers and limitations

No mathematical blocker identified. The result is pointwise for every fixed
interior center. It does not establish a uniform statement for centers moving
toward `alpha`, a diagonal `epsilon_n` limit, multi-gap or combined-subset
optimality, a matching upper bound, or the true global leading asymptotics.

The arXiv-v1 paper/assets, production code, search, tests, `verify.py`,
results, finite certificates, and prior proof notes/dossiers are protected.
The recorded finite global certification scope remains `3<=n<=14`.

## Exactly one next atomic task after acceptance

Independently review the continuum quantile pairing, parity and reindexing,
first variation, exact sign, and iterated-limit statement; record acceptance
or precise corrections.
