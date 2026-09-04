# Task Log

## 2026-09-04 — Startup

- HEAD: `4fc2bae962fb534f8758bab930a0863e3006bff7`.
- Tree clean before editing. Initial `git status --short` reported dubious
  ownership; per-command safe.directory override succeeded, with external
  ignore-file permission warnings. No Git configuration or history changed.
- Read AGENTS, knowledge, current status, roadmap, fixed-k theorem,
  radius-9 proof/checker/tests/evidence, dossier templates, relevant paper
  angular/Supnick definitions, production rank-tour code, tests and verifier.
- STRICT, only k=10 and n=45,46 with candidate separator 270.
- Expected delta: new proof note and six dossier files; three memory files.
  Protect all production, global certificate, historical and generated assets.

## 2026-09-04 — Exact preliminary endpoint arithmetic

- Inline `python -I -S -B -`, using Fraction and integer isqrt only: exit 0.
- Independently specialized parity formulas yield 36 and 37 edges.
- Recomputed threshold directed margins: `1751/35283600` and
  `5989/38564100`; both positive, agreeing with the suggested values.
- Strict integer witnesses at denominator 10000 give upper half-sum
  `15404369802693/5000000000000 < 157/50` (margin
  `295630197307/5000000000000`) and lower half-sum `8011/2500 > 22/7`
  (margin `1077/17500`).
- This preliminary calculation is not yet a complete proof: rank-tour
  agreement, analytic bounds, proof-note transcription and rejection gates
  remain to be checked. No other n or floating value was evaluated.

## 2026-09-04 — Complete proof and verification

- Reconstructed rank tours independently of the parity families: all 73
  cyclic edges agree, including closure and multiplicity; all 146 symmetry
  variants pass. Both threshold signs and chain gates close.
- Wrote the proof note with complete tables, positive pre-square gates,
  exact polynomial arcsine bound, and Machin identity with branch and
  signed-integral remainder arguments. Only then deduced s_10=46 through
  the fixed-k theorem.
- Adapted the radius-9 checker/test structure locally, with no runtime
  import of earlier checkers. New integer-only scorer reads AST literals
  without executing the checker and independently reconstructs witnesses,
  expanded denominators, cycle coverage, threshold cross-products and sums.
- Normal/optimized checker and scorer pass. Normal/optimized rejection
  suite: 28 tests, OK (0.063s / 0.062s). Includes one-unit corruption of
  each of the 73 witnesses, synthetic equality rejection, malformed
  cycles, sign/direction/domain errors, aggregate failure and note tampering.
- `python -m pytest`: exit 0, 12 passed in 27.86s. No dependency changes.
- No unexpected mathematical or test failure. Invalid synthetic inputs
  were rejected as intended; no alternative n or floating root was evaluated
  in the proof task. Existing production regression tests retain their own
  domains and numerical methods, independently of the proof premises.

## 2026-09-04 — Handoff

- Synchronized knowledge, current status and roadmap after the four gates
  passed; exact onset is now s_10=46, unresolved range 11<=k<4325.
- Complete proof/code and tracked diff reviewed; all untracked additions
  inspected, source hashes recorded. Final ten-file scope and whitespace
  checks recorded in EVIDENCE.md; no protected or generated asset changed.
- Final state: READY_FOR_REVIEW. No commit, GitHub write, external review
  or hosted CI claim. Full global verifier/paper build not run (unchanged).
- Exactly one next atomic task: STRICT radius-11 bridge attempt at n=49,50.
  Candidate s_11=50 remains unproved; that task has not begun.
