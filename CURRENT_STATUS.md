# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=2ea596414dd582b8ebf810983c96a0f4883ac4f0
observed_on=2026-08-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260805__radius7_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove or refute the proposed exact radius-7 formal Supnick seam onset
`s_7=34` by importing `research/FIXED_K_SUPNICK_SEAM.md` in full and closing
only `n=33,34` at the common rational separator `R=140`.

### Mathematical outcome

**Status:** `PROVED`; task state `READY_FOR_REVIEW` after exact reruns,
independent reviews, and complete final-diff audit.

For `R_{7,n}=R_chain(sigma*_{7,n})`, where `sigma*_{7,n}` is the
chain-minimizing Supnick cycle on `{7,...,n}`, the exact classification is

```text
theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    > theta_{R_{7,n}}(n,n-1)       for 9 <= n <= 33,

theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    < theta_{R_{7,n}}(n,n-1)       for every n >= 34.
```

Thus the exact first strict radius-7 formal seam obstruction is `s_7=34`.
The new endpoint arithmetic proves

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34}.
```

The threshold sides use positive sign gates and rational square margins. The
root sides audit all `27` and `28` adjacent edges with exact rational bounds;
the all-`n` quantifiers then follow from the already-proved fixed-`k`
no-threshold range, sign criterion, root growth, and threshold decrease.

This theorem concerns one formal Supnick seam only. It does not prove full
fixed-order feasibility, determine `R*(n)`, classify a global contact graph,
or establish that circle `7` floats in any or every global optimum.

### Allowed delta

- `research/RADIUS7_SEAM_ONSET.md`;
- `ops/TASK-20260805__radius7_seam_onset/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- exact stdlib/`Fraction` checker through `n=250`: exit `0`; `180182`
  explicit gates passed with numerical diagnostics skipped;
- optimized/no-site exact checker through `n=250`: exit `0`; identical gates
  and output under `python -B -O -S`;
- opt-in `NUMERICAL_DIAGNOSTIC_ONLY` scan for `n=9..120` at 60/100 digits:
  exit `0`; maximum relative root delta `4.9137935e-46`, maximum absolute
  deficit delta `5.013963e-47`;
- task-local/production convention comparison for `n=9..250`: exit `0`;
  `484` comparisons passed while the checker retained zero production imports;
- AST audit: exit `0`; zero `assert` nodes, float literals, `ringmin` imports,
  and top-level `mpmath` imports; exactly one lazy `mpmath` import;
- in-memory corrupted-upper-margin and zero-lower-bound mutations were
  rejected at the intended exact gates;
- `python -B -m pytest -p no:cacheprovider`: exit `0`; `12 passed in 33.90s`;
- two independent proof-note/checker reviews recomputed all `55` table rows,
  threshold margins, rational totals, `pi` identities, root directions,
  quantifiers, checker modes, CLI gates, and representative corruptions and
  found no mathematical or engineering defect.

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
- A positive radius-7 formal seam deficit is not a proof of full feasibility.
- A negative deficit neither constructs a replacement chain nor says what
  happens in global optima.
- Every floating-point scan in this task is labeled diagnostic only; the proof
  is the fixed-`k` theorem plus the exact endpoint note.
- Hosted CI, certificate frontiers, `verify.py`, and paper builds are unrelated
  to this proof-note/checker delta and were not run.

## Exactly one next atomic task after acceptance

Run a bounded two-precision diagnostic localization for the radius-8 formal
seam on `33<=n<=140`, stopping at the first stable root/threshold sign change
or the end of the range, and search for a common rational endpoint separator
with denominator at most `1000`. This next task may nominate a candidate
`s_8`; it must not claim an exact theorem or anything about full feasibility,
`R*(n)`, contact graphs, or floating circles.
