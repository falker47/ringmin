# Task Log

Append entries; retain failed attempts and contradictory evidence.

## 2026-09-11 — Startup

- Base HEAD: `0e09cf774aa11543e86887ccc2a6fb6b3563644e`; branch `main`,
  existing remote `origin` for `falker47/ringmin`.
- Working tree clean after command-local safe.directory; initial plain
  Git calls failed on the sandbox/repository ownership mismatch. Default
  global-ignore reads warned about permissions; command-local
  `core.excludesFile=` removes the warning without configuration changes.
- Read the contract, compact index, current status, relevant common-chain
  ledger/roadmap, proof Sections 1-6, 9.2 and 11, fixed-k rank/edge
  definitions, and specifically linked Section 11.5 checker/evidence.
- STRICT mode. Expected delta and protected paths are in TASK_STATUS.md.
- No general tours, geometry or new coefficients are in scope.

## 2026-09-11 — Analytic discriminator

- All deleted labels are isolated. The seam label k keeps neighbors n-1,n;
  unchanged deleted interior labels keep S-j-1,S-j+1; newly deleted block
  labels j have neighbors S-j-m-1,S-j-m+1.
- The exact cost change can therefore be summed by deleted labels, with
  every induced replacement edge counted once. The shifted deleted block
  has negative first variation of order m^-2; unshifted interior first
  variations cancel, and the seam is only order m^-4.
- Next: prove a uniform Taylor remainder and check the exact formula by
  independently constructing/restricting the prescribed cyclic tours.

## 2026-09-11 — Analytic completion

- Added Section 11.6 with exact radical formula (39f), first variation
  (39g), strict finite sign and uniform two-term expansion (39c).
- The one-sided grid and quadratic neighbor expansion combine to the
  negative second coefficient. Actual floor errors, unchanged interior
  labels and the seam enter only the O(m^-4) remainder.
- Classification: exact theorem and proved sharp-exponent corollary;
  the detailed proof remains solely in the research note. Updated only
  the existing common-chain ledger owner, current task and research priority.

## 2026-09-11 — Verification

- `python -I ops/TASK-20260911__signed_discrepancy_family/check_signed_discrepancy.py`:
  exit 0. Six exact floors, both N parities, 18 cyclic presentations;
  exact signed radical equality, induced replacement edges and wrap,
  signed defect sums, energy formula and interval-verified negative Delta.
- Exact rational gate encloses the positive limit between 0.203 and 0.204.
  Printed asymptotic remainders are finite corroboration only.
- The same checker with `-I -O` exits 1 intentionally with
  `Do not run this assert-based checker with -O`.
- Complete tracked diff inspected and one-off scope/whitespace/link audit
  passed: four tracked edits, four additions, 466 other tracked paths
  unchanged, old proof unchanged except two forward references, identical
  Section 12, sole ledger owner, eight clean files and 36 valid links.
- `git diff --check`: exit 0, no output. No mathematical check failed.

## 2026-09-11 — Handoff

- State: READY_FOR_REVIEW. Four documentation files and this four-file
  dossier/checker comprise the task. Final staged inspection, authorized
  normal commit/push and remote/clean-tree check follow this record.
- No blocker or unresolved family-scale question. General optimal
  constants, minimax realization and geometry remain outside this result.
- Exactly one next atomic task: independently review Section 11.6 and its
  Section 11.5 dependencies at committed HEAD and reproduce the checker.
