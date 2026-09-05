# Task Log

Append-only chronology; failed attempts and negative evidence are retained.

## 2026-09-05 — Startup

- HEAD: 4b40aebddad73f09e453b5f17c3100852c780991; clean working tree.
- Read AGENTS.md, PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, pertinent
  fixed-order/global ledger sections, the roadmap, task templates, the
  exact arbitrary-permutation and shifted-halves proof notes, local-root
  bounds, the preceding shift exact checker, prior task status and the
  published angular model. Initial combined ledger output was truncated;
  relevant dependency sections were then read in focused calls.
- Mode STRICT; expected delta and protected paths are in TASK_STATUS.md.
- Initial plain Git reads failed on ownership. Per-command safe.directory
  resolved this without a persistent configuration write. Ignore-file
  permission warnings remained; no changed tracked/untracked paths listed.

## 2026-09-05 — Analytic discriminator

- Derivation exposes a necessary additional condition: the (t,x) and
  (t,y) marginals agree in any weak empirical limit, beyond the three
  one-dimensional uniform marginals. It does not require independence.
- Found a symmetric reflection coupling on t in [0,1/4], where every
  high pair uses the chord branch. Reflection reduces the geometric mean
  relative to the shift's diagonal while preserving marginal measures.
- No LP or permutation search was launched. The intended negative result
  is a strict relaxation gap, with no claim of permutation realizability.

## 2026-09-05 — Verification

Pending exact gates, bounded diagnostics and final review.

## 2026-09-05 — Exact proof and bounded checker completed

- Wrote the authoritative proof: explicit uniform errors including t near
  zero and seams, root bracketing before the scale-dependent expansion,
  empirical marginal identities, balance, symmetrization and reflection.
- The coupling is specified using the existing exact alpha_*, not a
  numerical approximation; its strict saving >1/2496 is elementary.
- check_relaxation.py --exact-only: exit 0, all three exact gate groups.
- Full checker: exit 0; 27 prescribed orders, 54 score probes, 2928
  cells, 27 independent atan roots and three integral evaluations passed.
  The largest observed cell-error/bound ratio was 0.5166216303390701.
- No LP or factorial search; finite probes and decimal integrals remain
  numerical observations, while the note supplies the theorem.
- One documentation patch was rejected before application because it
  contained both Delete and Add operations for CURRENT_STATUS.md. Retried
  as ordinary ledger/roadmap updates and a single current-status rewrite.
  This was a patch-format error, not mathematical negative evidence.
- Background terminology was checked against Brendan Pass's primary
  survey (arXiv:1406.0026); its link is in the note. Neither strong duality
  nor any optimizer structure from external literature is a premise.

## 2026-09-05 — Final audit and handoff

- Read the entire new proof and every task-local source/document; inspected
  the complete tracked diff. The exact note/checker hashes are in EVIDENCE.
- File audit exited 0: exactly 3 tracked changes and 5 additions; all eight
  files passed direct whitespace/BOM/final-newline checks, all 3 local
  Markdown links resolve, and all 4 source/dependency SHA256 hashes match.
- Empty staged diff; git diff --check exited 0 with empty stdout. The
  changed-path whitelist excludes every protected/generated path. Only
  the fixed-order ledger owns the new stable claims; no index or second
  thematic ledger changed.
- Final state READY_FOR_REVIEW. No Git/GitHub write and no second research
  task started. The exact relaxed optimum and permutation recovery remain
  outside this result; no global bound or certification changed.
- Exactly one next atomic task: independently review the continuum
  obstruction, its coupling and strict gap, reproduce the checker and
  audit the two imported mathematical dependencies; record acceptance
  or precise corrections.
