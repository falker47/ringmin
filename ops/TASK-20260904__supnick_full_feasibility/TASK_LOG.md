# Task Log

Append-only chronology.

## 2026-09-04 — Startup

- HEAD: 00b330c09ec5609fad900d0f302f21cd258241c0.
- Working tree clean before editing; Git needs a command-local ownership
  exception. The default status invocation failed ownership validation;
  the safe.directory invocation succeeded, with inaccessible-user-ignore
  warnings. A subsequent attempt to suppress those warnings with
  core.excludesFile=NUL failed because Git rejects NUL as an exclude file.
  No configuration was written; use the successful read-only form.
- Read AGENTS.md, stable knowledge, current status, roadmap, fixed-k theorem,
  relevant sequence theorem and dossier, task templates, angular and STN
  implementation, independent witness checker, and published angular and
  supermodularity proofs.
- A read of the prior dossier's diagnostic.py failed; directory inspection
  identified the actual name diagnose.py. No source dependency is missing.
- Mode STRICT. Expected delta and protected paths are in TASK_STATUS.md.

## 2026-09-04 — Analytic reduction before computation

- Candidate discriminator: every triangle defect is at least the seam
  defect for every R>0, independently of the order and closure parity.
- Lowering the middle radius increases neither positive edge term.
  Positive mixed partials then make the defect with middle k nonincreasing
  as either endpoint increases. Distinct integer endpoints are bounded by
  n-1 and n after sorting.
- If this exact lemma holds, fan triangulation of a simple m-edge path
  gives slack >= (m-1) Delta. Positivity of Delta is used only afterward.
- Planned diagnostic: k=6,7,8,9 only; 80 decimal digits, deterministic
  bisection, every unordered pair in both directions and every triangle
  with ordered endpoints. Stop on a discrepancy larger than 1e-60 and
  certify it before any claim promotion. No scan is a proof premise.

## 2026-09-04 — Proof completed

- Proved the triangle minimum for every R>0 by lowering the middle radius
  to k, then increasing the sorted endpoints to n-1,n using the positive
  mixed derivative. Explicit rectangular integral remainders give the
  inequality and all equality conditions without case gaps.
- Proved slack >= (m-1)Delta by a fan telescoping identity on each simple
  path. Applied it separately to the two cyclic arcs, including the long
  complements of adjacent pairs. The imported positive seam then gives
  dominance, full Cartesian non-overlap and the fixed-order equality.
- Recorded both exact edge parities and the angular central correction;
  no root approximation or symmetrized sum is used in the path argument.
- No global-optimum, R*(n) or floating claim was inferred.

## 2026-09-04 — Independent checks

- `python -I ops/TASK-20260904__supnick_full_feasibility/check_exact.py`:
  exit 0; six symbolic identities; four rank/parity constructions, 114
  edges, all rotations/reflections; 1590 pairs and 3180 paths; 11 rejection
  gates. No production or diagnostic imports, no numerical root.
- `python -I ops/TASK-20260904__supnick_full_feasibility/diagnose.py`:
  exit 0; k=6,7,8,9, 80 digits; every triangle, both pair paths and
  Cartesian non-overlap pass. The minimum is the two-edge seam each time.
  This is a numerical observation, not an exact/all-k certificate.
- No mathematical counterexample or failed verification was found.
- The first knowledge-ledger patch used a nonmatching radius-1 heading
  and was rejected atomically. An rg lookup located the actual heading;
  the corrected patch succeeded. No partial edit was left by that failure.

## 2026-09-04 — Final review and handoff

- Reviewed the complete tracked diff and read every untracked addition in
  full. The explicit nine-file audit checks UTF-8, LF, final newlines,
  trailing whitespace, exact scope and unchanged HEAD. Exit 0.
- git diff --check: exit 0, no output. Five proof/audit/import source hashes
  recorded in EVIDENCE.md. No protected or generated path changed.
- Updated stable knowledge with the proved lemma and fixed-order theorem;
  updated the resolved roadmap entry and current task state. Prior proof
  notes/dossiers and the historical paper remain unchanged.
- Final state: READY_FOR_REVIEW. Independent proof review and manual
  integration remain outstanding; no global-optimum or floating inference.
- Nine files changed: proof note; this dossier's three Markdown files and
  two scripts; PROJECT_KNOWLEDGE.md; CURRENT_STATUS.md; research roadmap.
- Exactly one next atomic task: prove or refute the equivalence between
  full feasibility at the Supnick chain root and Delta_{k,n}>=0 for all
  k>=1, n>=k+2, treating small cycles, both paths and equality before using
  the known seam-onset classification. It has not begun.
