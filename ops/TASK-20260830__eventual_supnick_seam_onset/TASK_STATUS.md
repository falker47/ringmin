# Task Status

```text
task=TASK-20260830__eventual_supnick_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-30
updated_at=2026-08-30
```

## Objective

Prove or refute that the first strict-obstruction index of the formal
fixed-radius Supnick seam satisfies

```text
s_k = 4k+6
```

for every sufficiently large integer `k`, using only the parity-explicit
formulas in `research/FIXED_K_SUPNICK_SEAM.md` at `n=4k+c`, `c=5,6`.

## Scientific question

Can both parity subsequences be controlled uniformly well enough to prove

```text
R_{k,4k+c}/k^2 -> rho,
T_{k,4k+c}/k^2 -> 24/(2c-1),
rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx,
```

certify exactly `24/11<rho<8/3`, and combine the two endpoint signs with the
existing fixed-`k` sign and persistence theorem?

## In scope

- one authoritative proof note treating exactly `c=5,6` and both parities;
- uniform denominator and arcsine remainder bounds for the chain limit;
- an exact rationalization and uniform denominator control for the threshold
  limit;
- an exact elementary certificate for `24/11<rho<8/3`;
- one task-local standard-library exact checker with no parameter scan;
- durable knowledge, current status, and roadmap synchronization only after
  the complete proof and independent review pass.

## Out of scope

- an explicit effective cutoff for "sufficiently large";
- finite localization of any unresolved individual onset;
- full fixed-order feasibility, `R*(n)`, global optima, contact graphs, or
  floating-circle claims;
- changes to solver code, tests, certificates, `verify.py`, the historical
  paper, or publication assets.

## Expected delta

- `research/EVENTUAL_SUPNICK_SEAM_ONSET.md`;
- this four-file task dossier, including `check_asymptotic_onset.py`;
- `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and
  `research/NEXT_RESEARCH_STEPS.md` only after the result is complete.

## Protected paths potentially affected

- `research/FIXED_K_SUPNICK_SEAM.md`: read-only imported theorem and formulas;
- `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md`: read-only prior theorem;
- `src/`, `tests/`: production implementation and regression tests unchanged;
- `results/`, `verify.py`: certificate chain unrelated and protected;
- `paper_assets/`: arXiv-v1 history and publication assets unchanged.

## Completion gates

- [x] both parity-explicit chain limits proved with uniform error controls;
- [x] both threshold limits proved with uniform denominator/sign controls;
- [x] exact strict bounds on `rho` proved without numerical premises;
- [x] eventual onset identity deduced with correct signs and quantifiers;
- [x] claims and non-implications classified correctly;
- [x] exact checker passes normally and under optimized/no-site execution;
- [x] independent mathematical and checker reviews pass;
- [x] relevant regression tests pass;
- [x] durable memory updated only after exact verification;
- [x] `git status --short --untracked-files=all` inspected;
- [x] complete tracked and untracked delta inspected;
- [x] direct format checks and `git diff --check` pass;
- [x] no incidental generated or protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The theorem, exact checker, independent reviews, regression run, durable
memory synchronization, and complete delta audit are finished. Manual review
and integration remain with the user. After acceptance, exactly one next
atomic task is to derive a valid explicit cutoff for the eventual identity;
that task is not started here.
