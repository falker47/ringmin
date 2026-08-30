# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=3ad9835631b2a4d434972eedfe10cd8924a05d39
observed_on=2026-08-30
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260830__effective_supnick_seam_cutoff
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective

Prove one explicit integer cutoff `K_eff` such that the first
strict-obstruction index of the formal fixed-radius Supnick seam satisfies

```text
s_k = 4k+6                         for every integer k>=K_eff,
```

testing `K_eff=4325` with `r=13/5` for `c=5` and `r=11/5` for `c=6` and
without using a finite scan as proof.

### Mathematical outcome

**Status:** exact theorem proved; task state `READY_FOR_REVIEW` after exact
checks, independent post-file reviews, regression tests, durable-memory
synchronization, and complete final-delta inspection.

The quantitative closure and threshold estimates already recorded in
`research/EVENTUAL_SUPNICK_SEAM_ONSET.md` close at

```text
K_eff = 4325.
```

The exact rational separators are

```text
11/5 < 20/9 < rho < 41/16 < 13/5.
```

For every integer `k>=4325`, exact denominator, arcsine-remainder, and
symbolic-tail bounds give

```text
R_{k,4k+5} < (13/5)k^2,
R_{k,4k+6} > (11/5)k^2.
```

Writing `X_c=k^2 kappa_{k,4k+c}=H_c/Q_c>0`, the unrelaxed threshold error

```text
|X_c-(2c-1)/24| <= 4193/(256k)
```

gives the opposite threshold brackets. The critical exact gate is

```text
256*4325-264*4193 = 248 > 0.
```

Thus the formal deficit is positive at `4k+5` and negative at `4k+6`; the
imported fixed-`k` sign and persistence theorem proves

```text
s_k = 4k+6                         for every integer k>=4325.
```

No scan over `k` or `n` is a premise, and the cutoff is not claimed minimal.
The theorem concerns one formal seam only; it does not prove full
feasibility, determine `R*(n)`, classify contact graphs, or imply global
floating-circle behavior.

### Allowed delta

- `research/EVENTUAL_SUPNICK_SEAM_ONSET.md`;
- `ops/TASK-20260830__effective_supnick_seam_cutoff/*`;
- `PROJECT_KNOWLEDGE.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- this file.

### Verification completed

- exact stdlib/`Fraction` checker: exit `0`; `156` explicit gates, symbolic
  tail variable `m>=0`, and no `k,n` scan;
- normal and optimized/no-site mutation runs: exit `0`; identical theorem
  output and all `15` altered constants rejected;
- AST/source audit: exit `0`; zero `assert`, float, production import, or
  parameter-range nodes; imports only `fractions`, `pathlib`, and `sys`;
- optimized/no-site import audit: exit `0`; no output, error, or gate side
  effect;
- three independent post-file reviews returned final `PASS` after all
  checker-coverage findings were corrected;
- `python -B -m pytest -p no:cacheprovider`: exit `0`;
  final post-fix run `12 passed in 27.39s`.

### Completion gates

- final status contains exactly the eight authorized paths;
- the four tracked diffs and all four untracked dossier files were inspected
  in full after substantive edits;
- strict UTF-8/no-BOM, LF-only, exactly-one-final-LF, no-NUL, and
  trailing-whitespace audit passed on all eight files;
- scoped `git diff --check`: exit `0`, no output;
- explicit protected-path status: no changed paths; the task directory has
  exactly four files and no generated cache;
- the dossier records successful and failed checks without erasing the
  checker-harness and coverage corrections;
- certificate frontiers, `verify.py`, and paper builds are unrelated to this
  proof-note/checker delta and were not run.

### Residual limitations

- `4325` is a proved valid cutoff, not a minimality claim.
- Exact onsets in the finite range `8<=k<4325` remain unresolved except for
  the already proved `k<=7` cases.
- The checker corroborates exact algebra and rational inequalities; it does
  not reprove the analytic estimates or the imported fixed-`k` theorem.
- The theorem is post-arXiv-v1; the historical paper remains unchanged.
- A positive formal seam deficit is not full feasibility, and a negative one
  neither constructs a replacement chain nor describes a global optimum.

## Exactly one next atomic task after acceptance

Run the bounded two-precision radius-8 diagnostic on `33<=n<=46`, using
independently reconstructed Supnick edges and the exact threshold formula,
and report only a numerical onset candidate plus any rational separator of
denominator at most `1000`; do not promote it to an exact theorem.
