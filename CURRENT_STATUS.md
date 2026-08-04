# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=14fd8f612893af5b6961cd4f607ab2e1b5eb3fe4
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__radius1_seam_obstruction
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute, for every integer `n>=8`, the radius-1 seam obstruction in the formal chain-optimal Supnick necklace, without drawing conclusions about the global geometric optimum or the full floating cascade.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after local verification and final-diff audit.

For `R_n=R_chain(sigma_n*)`, the exact threshold is

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    > theta_{R_n}(n,n-1)       for 3 <= n <= 7,

theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)       for every n >= 8.
```

The proof in `research/RADIUS1_SEAM_OBSTRUCTION.md` derives parity-explicit Supnick closure sums, proves `R_n` strictly increases, converts the seam to an explicit strictly decreasing Descartes threshold, and closes the crossing with exact rational bounds at `n=7,8`. A task-local independent checker corroborates the finite diagnostics but is not the all-`n` proof.

### Allowed delta

- `research/RADIUS1_SEAM_OBSTRUCTION.md`;
- `ops/TASK-20260804__radius1_seam_obstruction/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- independent checker, `n=3..200`, 60/100 digits: exit `0`; exact bridges, order/edge formulas, signs, and precision stability pass;
- optimized-mode checker, `n=3..20`, 40/60 digits: exit `0`; unconditional exact checks pass under `python -O`;
- production Supnick/interleave equivalence through `n=200`: exit `0`;
- `python -m pytest`: exit `0`; `12 passed in 29.89s`;
- two independent read-only proof/checker reviews: no remaining issue.

### Completion gates

- final `git status --short` contains exactly the eight authorized paths;
- the complete tracked diff and all five untracked additions were read in full;
- direct UTF-8, final-newline, and trailing-whitespace checks passed for all eight paths;
- `git diff --check`: exit `0`, no output;
- protected and generated paths are absent from the delta;
- the dossier contains commands, exact outputs, failed approaches, limitations, and handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- It proves only unrealizability of one formal chain across one seam.
- It does not determine `R*(n)`, establish a floating circle in any or every global optimum, or prove the radius-`k` cascade.
- Hosted CI and certificate frontiers are not relevant verification layers for this documentation/checker-only delta and are not claimed inspected.

## Exactly one next atomic task after acceptance

Prove or refute the radius-2 analogue: for the chain-optimal Supnick order `sigma_{2,n}*` on `{2,...,n}` and `R_{2,n}=R_chain(sigma_{2,n}*)`, determine whether

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)
```

holds for every integer `n>=13`, with the exact lower-side threshold classified. Do not begin that task in this chat.
