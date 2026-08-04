# Task Status

```text
task=TASK-20260804__radius3_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove or refute the proposed exact radius-3 Supnick seam onset `s_3=17`
by reusing the fixed-`k` persistence theorem and establishing exact endpoint
bridges at `n=16,17`, preferentially with the rational separator `R=32`.

## Scientific question

For the chain-minimizing Supnick cycle `sigma*_{3,n}` on `{3,...,n}`, put

```text
R_{3,n} = R_chain(sigma*_{3,n})
```

and let `Delta_{3,n}` be its seam deficit at `(n,3,n-1)` as defined in
`research/FIXED_K_SUPNICK_SEAM.md`. Determine, with exact quantifiers, whether

```text
Delta_{3,n} > 0  for 5 <= n <= 16,
Delta_{3,n} < 0  for every n >= 17.
```

At task start, the radius-3 onset was only a finite published computation and
an open post-v1 exact claim. The endpoint proof now resolves it as an exact
theorem; the general existence and persistence theorem was already proved.

## In scope

- `research/RADIUS3_SEAM_ONSET.md`;
- this task dossier and one production-independent checker;
- exact rational threshold and chain-sum bridges at `R=32` for `n=16,17`;
- `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` only if the exact classification survives
  independent verification and review.

## Out of scope

- any statement about `R*(n)` or global optimality;
- fixed-order full feasibility before the seam onset;
- floating circles in any or every global optimum;
- production code, certificate range, result artifacts, `verify.py`, tests,
  paper/publication assets, generated reports, or release metadata.

## Expected delta

Add one authoritative radius-3 proof note, this dossier, and one
self-contained checker. Replace the live status entry and conditionally
update compact knowledge and the ranked roadmap after the exact proof passes.

## Protected paths potentially affected

The following paths must remain byte-for-byte unchanged and will be audited:

- `paper_assets/` and all public arXiv-v1 assets;
- `src/`, `tests/`, `scripts/`, `results/`, and `verify.py`;
- `README.md`, `REPORT.md`, `.github/`, dependency metadata, and all existing
  proof notes and dossiers.

## Completion gates

- [x] exact threshold bridges `32<T_{3,16}` and `T_{3,17}<32` proved;
- [x] exact termwise chain bridges `R_{3,16}<32<R_{3,17}` proved;
- [x] fixed-`k` monotonicity and persistence applied with correct quantifiers;
- [x] exact onset classification and non-implications stated correctly;
- [x] independent checker run in default exact-audit and optimized modes;
- [x] diagnostic numerics kept separate from the exact rational audit;
- [x] production convention compared read-only;
- [x] relevant regression tests passed;
- [x] independent proof/checker reviews closed;
- [x] durable memory synchronized only after the exact result holds;
- [x] `git status --short` and complete tracked/untracked delta re-inspected;
- [x] `git diff --check` and direct whitespace checks re-run;
- [x] no incidental protected or generated file changes;
- [x] state reset to `READY_FOR_REVIEW` after the post-review correction.

## Blockers

None.

## Handoff

The exact theorem, rational checker audit, opt-in numerical diagnostics,
production convention comparison, regression suite, and three independent
reviews pass. The complete tracked/untracked delta, whitespace, and
protected-path audits were repeated after the post-review correction and
pass. The task is `READY_FOR_REVIEW`; manual review and commit remain with the
user.

Exactly one proposed next atomic task after acceptance: prove or refute the
finite diagnostic candidate `s_4=21` with an exact endpoint bridge at
`n=20,21`, preserving the same seam-only scope.
