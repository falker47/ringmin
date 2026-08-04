# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=d90495981414e18344585c446ad8b68bf8276f54
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__radius3_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute the proposed exact radius-3 Supnick seam onset `s_3=17` by
reusing the fixed-`k` persistence theorem and closing the exact endpoint
bridge at `n=16,17`, preferentially with the rational separator `R=32`.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after the post-review
domain correction, exact reruns, and complete final-diff audit.

For `R_{3,n}=R_chain(sigma*_{3,n})`, where `sigma*_{3,n}` is the
chain-minimizing Supnick cycle on `{3,...,n}`, the exact classification is

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17.
```

Thus the exact first strict radius-3 seam obstruction is `s_3=17`. The new
endpoint arithmetic proves

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.
```

The threshold bounds use rational square comparisons. The chain bounds cover
every adjacent edge and use termwise rational bounds on the arcsine arguments
with exact final margins. The all-`n` quantifiers then follow from the
already-proved root growth, threshold decrease, no-threshold range, and
persistence theorem.

This theorem concerns one formal Supnick seam only. It does not determine
`R*(n)`, prove full feasibility before the onset, or establish that circle `3`
floats in any or every global optimum.

### Allowed delta

- `research/RADIUS3_SEAM_ONSET.md`;
- `ops/TASK-20260804__radius3_seam_onset/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- exact stdlib-only checker through `n=250`: exit `0`; `62,594` explicit
  rational/order gates passed with numerical diagnostics skipped;
- optimized stdlib-only checker through `n=250`: exit `0`; the same `62,594`
  gates and output passed under `python -O -S`;
- opt-in checker diagnostic for `n=5..120` at 60/100 digits: exit `0`; signs,
  root/threshold comparisons, opposing monotonicities, and precision
  stability passed; first raw-deficit increase observed at `(40,41)`;
- task-local/production convention comparison for `n=5..200`: exit `0`;
  `392` comparisons passed while the checker itself retained zero production
  imports;
- AST audit: exit `0`; zero `ast.Assert` nodes and zero `ringmin` imports;
- `python -m pytest -p no:cacheprovider`: exit `0`; `12 passed in 29.90s`;
- three fresh independent read-only reviews rechecked the proof, checker, and
  dossier; one omitted real-domain qualifier for `asin` and two dossier
  consistency issues were corrected, while the checker audit found no defect.

### Completion gates

- final `git status --short --untracked-files=all` contains exactly the eight
  authorized paths;
- the complete tracked diff and all five untracked additions were read in
  full after the substantive edits;
- direct strict-UTF-8, no-BOM, LF-only, exactly-one-final-LF, and
  trailing-whitespace checks passed for all eight paths;
- final `git diff --check`: exit `0`, no output;
- explicit protected-path status: exit `0`, no output;
- the incidental task-local Python cache was removed; no protected or
  generated path remains in the delta;
- the dossier records exact commands, outputs, corrections, negative
  evidence, limitations, and handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- A positive radius-3 seam deficit is not a proof of full realizability.
- A negative seam deficit neither constructs a replacement chain nor says
  what happens in global optima.
- The finite high-precision scan is diagnostic only; the proof is the two
  proof notes and their exact inequalities.
- Hosted CI, global certificate frontiers, and `verify.py` are unrelated to
  this proof-note/checker delta and are not claimed inspected.

## Exactly one next atomic task after acceptance

Prove or refute the finite diagnostic candidate `s_4=21` by establishing an
exact endpoint bridge for `R_{4,n}` and `T_{4,n}` at `n=20,21`, reusing the
fixed-`k` theorem and making no claim about `R*(n)`, full feasibility, or
global floating circles.
