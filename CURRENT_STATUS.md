# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=5f9be1ab107ce6fba2eba586e9d30eb859c7d330
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__radius2_seam_threshold
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute the exact radius-2 seam classification in the formal
chain-optimal Supnick necklace on `{2,...,n}`, including every shifted-order,
implicit-root, Descartes-threshold, domain, monotonicity, and exact endpoint
step required for an all-`n` result.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after local verification
and final-diff audit.

For `R_{2,n}=R_chain(sigma*_{2,n})`, the exact threshold is

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    > theta_{R_{2,n}}(n,n-1)       for 4 <= n <= 12,

theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)       for every n >= 13.
```

The proof in `research/RADIUS2_SEAM_THRESHOLD.md` derives the exact shifted
Supnick convention and parity closure sums, proves `R_{2,n}` strictly
increases, proves that the positive radius-2 Descartes threshold exists
exactly for `n>=9` and strictly decreases, handles `n=4..8` before that
domain, and closes the crossing with rational bounds
`R_{2,12}<17<T_{2,12}` and `T_{2,13}<14<R_{2,13}`. A task-local independent
checker corroborates finite diagnostics but is not the all-`n` proof.

### Allowed delta

- `research/RADIUS2_SEAM_THRESHOLD.md`;
- `ops/TASK-20260804__radius2_seam_threshold/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- independent checker, `n=4..200`, 60/100 digits: exit `0`; exact domain and
  bridge arithmetic, shifted order/edge formulas, signs, and precision
  stability pass;
- optimized-mode checker, `n=4..30`, 40/60 digits: exit `0`; unconditional
  exact checks remain active and pass under `python -O`;
- production `supnick_max_tour`/`interleave` comparison through `n=200`:
  exit `0`;
- `python -m pytest`: exit `0`; `12 passed in 28.36s`;
- three independent read-only proof/checker reviews: no remaining issue.

### Completion gates

- final `git status --short` contains exactly the eight authorized paths;
- the complete tracked diff and all five untracked additions were read in
  full;
- direct strict-UTF-8, no-BOM, final-newline, and trailing-whitespace checks
  passed for all eight paths;
- `git diff --check`: exit `0`, no output;
- protected and generated paths are absent from the delta;
- the dossier contains commands, exact outputs, failed approaches,
  limitations, and handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- It proves only unrealizability of one formal chain across one seam.
- It does not determine `R*(n)`, establish that radius `2` floats in any or
  every global optimum, or prove the radius-`k` cascade.
- Hosted CI and certificate frontiers are not relevant verification layers for this documentation/checker-only delta and are not claimed inspected.

## Exactly one next atomic task after acceptance

Prove or refute the radius-3 analogue: for the chain-optimal Supnick order
`sigma*_{3,n}` on `{3,...,n}` and
`R_{3,n}=R_chain(sigma*_{3,n})`, determine whether

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17
```

with the physical threshold domain and both sides of the crossing proved
exactly. Do not begin that task in this chat.
