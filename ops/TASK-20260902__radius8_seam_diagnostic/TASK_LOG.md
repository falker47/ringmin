# Task Log

Append-only task chronology. Times are local Europe/Rome.

## 2026-09-02 16:45 — Startup and expected delta

- Base HEAD: `3eb1ec321e2f5a334826ee70c2258f82b9703f66`.
- Working tree clean after a per-invocation safe-directory override.
- Read the operating contract, knowledge ledger, current status, roadmap,
  fixed-`k` theorem, uniform-window statement/proof setup, radius-7 endpoint
  precedent and evidence, prior diagnostic implementation, production order
  convention, standalone verifier root implementation, relevant paper
  theorem, dependency files, and all three dossier templates.
- Mode STRICT; expected changes limited to this five-file dossier,
  `CURRENT_STATUS.md`, and the radius-8 roadmap entry.
- Initial Git queries failed on sandbox ownership. The safe-directory
  override succeeded with warnings about the inaccessible global ignore
  file. An attempted `core.excludesfile=NUL` override failed because Git
  cannot use NUL as an exclude file; no configuration or repository change.
- Available numerical environment: Python `3.14.3`, mpmath `1.3.0`.

## 2026-09-02 16:45 — Predeclared diagnostic protocol

- Domain is hard bounded to `k=8`, all integers `33..46`. The first stable
  negative-to-positive crossing will be reported; complete the requested
  table through 46, without testing a wider range. If absent, record an
  inconsistency for investigation and stop.
- Run A: 90 digits, rank-tour cyclic edges, arcsine closure, bisection.
- Run B: fresh 150-digit context, parity edge formulas, arctangent closure,
  Ridder root solver with independent start bracket and no warm start.
- Both use the exact Descartes formula; run B evaluates its rationalized
  conjugate with exact rational coefficients. mpmath is shared, so this is
  algorithm/construction/precision independence, not library independence.
- Local numerical root brackets have half-width `10^(-(dps-30))`; compare
  the runs with absolute guard `1e-55`. These are diagnostic guards, not
  directed-rounding enclosures or exact certificates.
- Search denominators `1..1000` in increasing order for the first fraction
  inside the intersection of both endpoint gaps at both precisions, after
  shrinking each gap by `1e-55`.
- No randomness, seeds, parallel workers, or production imports. Artifact
  stores full tours/edge sets, roots, thresholds, differences, residuals,
  numerical brackets, cross-precision differences, separator and margins.

## 2026-09-02 16:51 — Numerical execution and independent stored-data audit

- `python -B ops/TASK-20260902__radius8_seam_diagnostic/diagnose.py --write`
  exited `0`: 14 rows, two computational paths, stable crossing `37/38`,
  candidate only `38`, separator `176/1`.
- `python -B -O ops/TASK-20260902__radius8_seam_diagnostic/diagnose.py --check`
  exited `0`: identical outcome, `reproduction=BYTE_IDENTICAL`.
- Separate stdlib Decimal/AST/input-mutation audit exited `0`: all 14 rows
  checked, two out-of-range calls and three malformed edge/tour cases
  rejected; source hashes match. Exact invocation/output in `EVIDENCE.md`.
- Maximum stored cross-run difference is `4.0219045879874642e-76`, below
  `1e-55`; minimum absolute sign margin is about `8.2728536469`.
- Smallest separator margin is about `0.2242263045`. Every result remains
  NUMERICAL DIAGNOSTIC; no endpoint proof was attempted.

## 2026-09-02 16:54 — Documentation and complete-content review

- Updated current status and only the radius-8 roadmap entry; the single
  proposed next task is the exact `37/38` endpoint bridge with `176`.
- Read the entire generator and all artifact fields (compact JSON rendering
  of every row), then the full evidence and tracked delta.
- A portable Git invocation using `safe.directory="$PWD"` returned a
  direct comparison of the two supplied files (exit `1`) rather than the
  repository diff. It was rejected as review evidence. Repeating with the
  known absolute safe directory returned the correct tracked diff, exit `0`.
- Review found and corrected one unmatched inline-code delimiter in current
  status. No numerical source or artifact changed after reproduction.

## 2026-09-02 16:56 — Final gates and manual handoff

- Full tracked/untracked format/scope audit exited `0`: seven authorized
  files, five dossier files, zero protected changes, no cache directories.
- `git diff --check` exited `0`, no output. Explicit whitespace/UTF-8/LF
  checks include all five untracked additions.
- State set to `READY_FOR_REVIEW`; final audit repeated after the status
  edits. No Git history or GitHub state was written.
- Changed files: this dossier's `TASK_STATUS.md`, `TASK_LOG.md`,
  `EVIDENCE.md`, `diagnose.py`, `diagnostic.json`; `CURRENT_STATUS.md`;
  the radius-8 roadmap entry. Exact knowledge and proof notes are unchanged.
- Residual limitation: numerical evidence only, with a shared mpmath
  backend. There is no exact onset proof or certification extension.
- Exactly one next atomic task: the STRICT exact `37/38` endpoint bridge
  using `176`. It was proposed, not started.
