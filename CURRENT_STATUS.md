# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=e23663ea4c831ccfd50380063894b5d8574cabd7
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__fixed_k_supnick_seam
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove the general fixed-radius Supnick seam theorem for all integers `k>=1`
and `n>=k+2`, including the canonical shifted order, implicit-root behavior,
exact Descartes-threshold domain and formula, eventual crossing, possible
equality, and persistent obstruction. Recover `k=1,2` from the existing exact
endpoint notes without classifying the exact `k=3` onset.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after local verification
and final-diff audit.

For `R_{k,n}=R_chain(sigma*_{k,n})`, the canonical Supnick order on
`{k,...,n}` has seam neighbors `n-1,n`. The root exists uniquely, strictly
increases with `n`, and tends to infinity. With

```text
Delta_{k,n}
  = theta_{R_{k,n}}(n,k) + theta_{R_{k,n}}(k,n-1)
    - theta_{R_{k,n}}(n,n-1),
```

one has `Delta_{k,n}>0` for the exact no-threshold range
`k+2<=n<=4k`. For `n>=4k+1`,

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))),
T_{k,n} = 1/kappa_{k,n},

Delta_{k,n} < 0  iff  R_{k,n} > T_{k,n}.
```

The thresholds strictly decrease to `k`, so `R_{k,n}-T_{k,n}` strictly
increases to infinity. Hence every fixed `k` has a finite first strict seam
obstruction; it persists thereafter, and equality can occur at most once.
The specialized endpoint bridges in the existing notes recover exact onsets
`s_1=8`, `s_2=13`. No exact onset for `k>=3` is claimed.

### Allowed delta

- `research/FIXED_K_SUPNICK_SEAM.md`;
- `ops/TASK-20260804__fixed_k_supnick_seam/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- independent checker for `k=1..12` through `n=4k+41`, 60/100 digits:
  exit `0`; exact algebra/domain, shifted order/edge formulas, Descartes
  signs, root/threshold monotonicities, persistence diagnostics, and precision
  stability pass;
- optimized-mode checker for `k=1..4`, 40/60 digits: exit `0`; explicit exact
  gates remain active and pass under `python -O`;
- production `supnick_max_tour`/`interleave` comparison over 1,580 shifted
  cases: exit `0`;
- `python -m pytest`: exit `0`; `12 passed in 34.50s`;
- three independent read-only reviews of the actual proof/checker: no
  actionable mathematical, convention, checker, or scope issue.

### Completion gates

- final `git status --short` contains exactly the eight authorized paths;
- the complete tracked diff and all five untracked additions were read in
  full after the substantive edits;
- direct strict-UTF-8, no-BOM, final-LF, and trailing-whitespace checks passed
  for all eight paths;
- `git diff --check`: exit `0`, no output;
- protected and generated paths are absent from the delta;
- the dossier contains commands, exact outputs, negative evidence,
  limitations, and handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- It proves eventual unrealizability of one formal Supnick chain across one
  seam for each fixed `k`; a positive seam deficit does not prove full
  realizability.
- It does not identify `s_k` for `k>=3`, determine `R*(n)`, or establish that
  radius `k` floats in any or every global optimum.
- The checker scan is finite diagnostic evidence, not the all-`k` proof.
- Hosted CI and certificate frontiers are not relevant verification layers
  for this documentation/checker-only delta and are not claimed inspected.

## Exactly one next atomic task after acceptance

Prove or refute the proposed exact radius-3 onset `s_3=17` by establishing
exact endpoint inequalities at `n=16,17` for the already-defined
`R_{3,n}` and `T_{3,n}`. Reuse the general monotonicity/persistence theorem;
do not treat a finite scan as proof or make claims about `R*(n)` or global
floating circles.
