# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=b49d0fa604eab7aa6b7d64dbfa27d85e3785a2f6
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__radius4_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute the proposed exact radius-4 formal Supnick seam onset
`s_4=21` by reusing `research/FIXED_K_SUPNICK_SEAM.md` without repeating its
general proof and closing only `n=20,21`, preferably at `R=50`.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after exact reruns,
independent reviews, and complete final-diff audit.

For `R_{4,n}=R_chain(sigma*_{4,n})`, where `sigma*_{4,n}` is the
chain-minimizing Supnick cycle on `{4,...,n}`, the exact classification is

```text
theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    > theta_{R_{4,n}}(n,n-1)       for 6 <= n <= 20,

theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    < theta_{R_{4,n}}(n,n-1)       for every n >= 21.
```

Thus the exact first strict radius-4 formal seam obstruction is `s_4=21`.
The new endpoint arithmetic proves

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.
```

The threshold sides use positive rational square margins. The root sides
audit all `17` and `18` adjacent edges with exact rational bounds; the
all-`n` quantifiers then follow from the already-proved fixed-`k`
no-threshold range, sign criterion, root growth, and threshold decrease.

This theorem concerns one formal Supnick seam only. It does not prove full
fixed-order feasibility, determine `R*(n)`, classify a global contact graph,
or establish that circle `4` floats in any or every global optimum.

### Allowed delta

- `research/RADIUS4_SEAM_ONSET.md`;
- `ops/TASK-20260804__radius4_seam_onset/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- exact stdlib-only checker through `n=250`: exit `0`; `184478` explicit
  `Fraction`/order gates passed with numerical diagnostics skipped;
- optimized/no-site exact checker through `n=250`: exit `0`; identical gates
  and output under `python -B -O -S`;
- opt-in `NUMERICAL_DIAGNOSTIC_ONLY` scan for `n=6..120` at 60/100 digits:
  exit `0`; precision stability, endpoint signs, threshold domain, and
  opposing monotonicities passed;
- task-local/production convention comparison for `n=6..250`: exit `0`;
  `490` comparisons passed while the checker retained zero production
  imports;
- AST audit: exit `0`; zero `ast.Assert` nodes, float literals, and `ringmin`
  imports;
- in-memory wrong-margin mutation was rejected at the intended exact gate;
- `python -m pytest -p no:cacheprovider`: exit `0`; `12 passed in 30.40s`;
- independent threshold, table, proof, and checker reviews recomputed every
  new margin and found no mathematical defect. One direct-positivity gate was
  made more explicit and both exact modes passed again.

### Completion gates

- final `git status --short --untracked-files=all` contains exactly the eight
  authorized paths;
- the complete tracked diff and all five untracked additions were read in
  full after the substantive edits;
- direct strict-UTF-8, no-BOM, LF-only, exactly-one-final-LF, and
  trailing-whitespace checks passed for all eight paths;
- final `git diff --check`: exit `0`, no output;
- explicit protected-path status: exit `0`, no output;
- the task directory contains exactly its four intended files; no cache or
  generated output remains;
- the dossier records commands, diagnostics, negative evidence, reviews,
  limitations, and manual handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- A positive radius-4 formal seam deficit is not a proof of full feasibility.
- A negative deficit neither constructs a replacement chain nor says what
  happens in global optima.
- Every floating-point scan in this task is labeled diagnostic only; the
  proof is the fixed-`k` theorem plus the exact endpoint note.
- Hosted CI, certificate frontiers, `verify.py`, and paper builds are
  unrelated to this proof-note/checker delta and were not run.

## Exactly one next atomic task after acceptance

Run a bounded two-precision diagnostic localization for the radius-5 formal
seam on `21<=n<=80`, stopping at the first stable root/threshold sign change
or the end of the range, and search for a common rational endpoint separator
with denominator at most `1000`. This next task may nominate a candidate
`s_5`; it must not claim an exact theorem or anything about full feasibility,
`R*(n)`, or floating circles.
