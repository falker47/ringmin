# Task Status

```text
task=TASK-20260904__radius8_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove the exact radius-8 endpoint bridge at `n=37,38`, separator `176`,
then apply the existing fixed-`k` theorem if and only if all four gates close.

## Scientific question

Do exact threshold sign/square comparisons and complete rational bounds on
the 30/31-edge chain sums prove `R_{8,37}<176<T_{8,37}` and
`T_{8,38}<176<R_{8,38}`? Initially these are numerical observations only.
The resulting all-integer seam classification would be a proved corollary
of `research/FIXED_K_SUPNICK_SEAM.md`, not a global optimum certificate.

## In scope and expected delta

- New `research/RADIUS8_SEAM_ONSET.md`.
- This dossier: status, append-only log, evidence, exact `check_seam.py`,
  and task-local `check_mutations.py`.
- `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the relevant roadmap entries.

## Out of scope and protected paths

Other radius experiments; revisions to prior proof notes/dossiers; production
`src/`, `tests/`, `scripts/`; `results/`, `verify.py`; `paper_assets/`,
`README.md`, `REPORT.md`; `AGENTS.md`, dependency and CI files. Inspect the
complete Git delta to confirm these remain unchanged. No Git/GitHub writes.

## Completion gates

- [x] All four exact inequalities close with explicit sign and square gates.
- [x] Complete cyclic edge sets checked against independent parity formulas.
- [x] Exact arcsine and pi comparisons justified in the proof and checker.
- [x] Checker runs normally and under `-O`; targeted mutations are rejected.
- [x] Repository regression suite run and results recorded.
- [x] Detailed proof and compact knowledge/status/roadmap synchronized.
- [x] Complete tracked and untracked delta, whitespace and protected scope audited.
- [x] State set to `READY_FOR_REVIEW` for manual integration.

## Blockers

None. Read-only Git uses a per-command safe-directory setting for the sandbox
account; no persistent configuration is changed.

## Handoff

The four exact bridge inequalities hold; the fixed-`k` theorem gives
`Delta_{8,n}>0` for `10<=n<=37`, `Delta_{8,n}<0` for every `n>=38`,
and therefore `s_8=38`. Neither the prior artifact nor its numerical values
enter the proof. Normal/optimized exact and mutation checks pass; the
regression suite reports 12 passed with a pytest-cache permission warning.
All nine files passed complete diff/content review and explicit whitespace,
scope and provenance checks. No protected path changed. Independent
mathematical review of the imported theorem and new proof remains the user's
integration gate. No commit or GitHub write was performed.

Suggested manual commit message:
`research: prove exact radius-8 Supnick seam onset at n=38`

Exactly one next atomic task after acceptance: a bounded STRICT radius-9
two-precision seam diagnostic on `37..50`, with independent edge
reconstruction and a rational separator if possible. It has not begun.
