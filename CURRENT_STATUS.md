# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=3c4ca3ba9c227d2f4a3bd46605ed36eaa145bf10
observed_on=2026-08-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260804__radius5_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute the proposed exact radius-5 formal Supnick seam onset
`s_5=25` by reusing `research/FIXED_K_SUPNICK_SEAM.md` without repeating its
general proof and closing only `n=24,25` at `R=75`.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after exact reruns,
independent reviews, and complete final-diff audit.

For `R_{5,n}=R_chain(sigma*_{5,n})`, where `sigma*_{5,n}` is the
chain-minimizing Supnick cycle on `{5,...,n}`, the exact classification is

```text
theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    > theta_{R_{5,n}}(n,n-1)       for 7 <= n <= 24,

theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    < theta_{R_{5,n}}(n,n-1)       for every n >= 25.
```

Thus the exact first strict radius-5 formal seam obstruction is `s_5=25`.
The new endpoint arithmetic proves

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.
```

The threshold sides use positive sign gates and rational square margins. The
root sides audit all `20` and `21` adjacent edges with exact rational bounds;
the all-`n` quantifiers then follow from the already-proved fixed-`k`
no-threshold range, sign criterion, root growth, and threshold decrease.

This theorem concerns one formal Supnick seam only. It does not prove full
fixed-order feasibility, determine `R*(n)`, classify a global contact graph,
or establish that circle `5` floats in any or every global optimum.

### Allowed delta

- `research/RADIUS5_SEAM_ONSET.md`;
- `ops/TASK-20260804__radius5_seam_onset/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- exact stdlib/`Fraction` checker through `n=250`: exit `0`; `183033`
  explicit gates passed with numerical diagnostics skipped;
- optimized/no-site exact checker through `n=250`: exit `0`; identical gates
  and output under `python -B -O -S`;
- opt-in `NUMERICAL_DIAGNOSTIC_ONLY` scan for `n=7..120` at 60/100 digits:
  exit `0`; maximum relative root delta `4.739224e-46`, maximum absolute
  deficit delta `1.495911e-46`;
- task-local/production convention comparison for `n=7..250`: exit `0`;
  `488` comparisons passed while the checker retained zero production
  imports;
- AST audit: exit `0`; zero `ast.Assert` nodes, float literals, and `ringmin`
  imports; exact top-level imports are standard-library modules only;
- in-memory wrong-upper-margin and exact-lower-equality mutations were
  rejected at the intended exact gates;
- `python -m pytest -p no:cacheprovider`: exit `0`; `12 passed in 29.45s`;
- three independent post-implementation reviews recomputed every threshold
  margin, all `41` table rows, rational totals, `pi` identities, quantifiers,
  and checker modes and found no mathematical or engineering defect.

### Completion gates

- final `git status --short --untracked-files=all` contains exactly the eight
  authorized paths;
- the complete tracked diff and all five untracked additions were read in
  full after the substantive edits;
- direct strict-UTF-8, no-BOM, LF-only, exactly-one-final-LF, and
  trailing-whitespace checks passed for all eight paths;
- final `git diff --check`: exit `0`, no output;
- explicit protected-path status: exit `0`, no paths;
- the task directory contains exactly its four intended files and no cache or
  generated output;
- the dossier records commands, diagnostics, negative evidence, reviews,
  limitations, and manual handoff.

### Residual limitations

- This theorem is post-arXiv-v1 work; the historical paper remains unchanged.
- A positive radius-5 formal seam deficit is not a proof of full feasibility.
- A negative deficit neither constructs a replacement chain nor says what
  happens in global optima.
- Every floating-point scan in this task is labeled diagnostic only; the
  proof is the fixed-`k` theorem plus the exact endpoint note.
- Hosted CI, certificate frontiers, `verify.py`, and paper builds are
  unrelated to this proof-note/checker delta and were not run.

## Exactly one next atomic task after acceptance

Run a bounded two-precision diagnostic localization for the radius-6 formal
seam on `25<=n<=100`, stopping at the first stable root/threshold sign change
or the end of the range, and search for a common rational endpoint separator
with denominator at most `1000`. This next task may nominate a candidate
`s_6`; it must not claim an exact theorem or anything about full feasibility,
`R*(n)`, or floating circles.
