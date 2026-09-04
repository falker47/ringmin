# Task Log

## 2026-09-04 — Startup and bounded exact construction

- Base HEAD: `2a3af790de73e1694cbb510245e14015f810e3b0`; clean working tree.
- Read AGENTS, knowledge, status, roadmap, fixed-k theorem, previous radius-8
  proof/checker/dossier, templates, package configuration and relevant
  production/verifier/publication geometry and Supnick passages.
- Mode STRICT; expected delta and protected paths recorded in TASK_STATUS.
- Initial plain Git commands reported dubious ownership. Per-command
  `-c safe.directory=<repository-root>` permitted
  read-only inspection without modifying persistent configuration. Git also
  warned that the sandbox cannot read the user's external ignore file.
- Executed an inline stdlib/Fraction and integer-isqrt calculation only at
  n=41,42, R=220. Reconstructed the parity edges and every denominator-10000
  bound independently of previous diagnostics. No floating root or scan.
- Preliminary exact half-sums: upper `194613679989/62500000000`, below
  `157/50` by `1636320011/62500000000`; lower `4063/1250`, above `22/7`
  by `941/8750`. Both threshold sign/square gates are positive.
- These calculations motivate the complete proof/checker; the formal onset
  is not promoted until all edge, analytic and arithmetic gates pass.

## 2026-09-04 — Rejected initial strict witness and correction

- First `python -I -S -B .../check_seam.py --tables`: exit 1 at
  `strict lower sine square margin`, after both threshold gates and pi bounds
  passed. The initial integer-floor construction gave m=1000 at edge (20,30)
  for n=42, where the sine is exactly 1/10. Its square margin is zero.
- This rejects that witness; it does not refute the endpoint inequality.
  No onset was promoted. Reconstructed the strict lower witness as m=999;
  the general strict integer rule is `isqrt((D^2 ab-1)//Q_e)`.
- The corrected lower sum is `32503/10000`, exceeding `22/7` by
  `7521/70000`. The zero-margin candidate is retained as a rejection test.

## 2026-09-04 — Proof/checker validation and test-parser correction

- Corrected checker passed with `-I -S -B --tables` and `-I -S -O -B`:
  all four inequalities, 67 edges, 134 rotations/reflections. Exact outputs
  agree. Wrote the complete proof and all tables, including the strict
  arcsine majorant and self-contained Machin/signed-remainder pi proof.
- First mutation run: 24 tests, 2 failures, exit 1. Both failures were in
  Markdown extraction (leading blank line selected the wrong table block;
  unescaped braces in the tour regex were interpreted as a repetition).
  Fixed extraction with lstrip/first blank block and re.escape. The 22
  other tests, including every rejection test, passed in that run.
- First parser-fix patch was rejected for a mismatched log context; no
  partial edit was applied. Corrected the context and reapplied it.

## 2026-09-04 — Final verification and handoff

- Corrected mutation suite: 24 tests, OK, normal exit 0 (0.052s) and
  optimized exit 0 (0.050s). The integer scorer reconstructs all 67 bounds
  and verifies every table margin and both aggregate/threshold comparisons.
- Only after the complete bridge passed, synchronized knowledge, current
  status and roadmap with the exact formal-seam result s_9=42.
- Read the entire tracked diff and all six untracked files in full. A
  nine-file allowlist audit checked UTF-8/LF, final newline, trailing
  whitespace, the complete dossier directory and all four recorded hashes.
  Exit 0: delivery_audit=PASS, files=9, untracked=6, hashes=4,
  protected_changes=0. `git diff --check`: exit 0, no output; HEAD unchanged.
- In the startup command above the machine-specific safe-directory argument
  is represented by <repository-root>; no command semantics or failure
  history has been removed. No persistent Git configuration was changed.
- Production suite, global verifier, hosted CI and paper build were not run:
  their components are unchanged and all new proof arithmetic is covered
  by the scoped exact checks. No claim of external review or CI success.
- State READY_FOR_REVIEW. Nine changed files: proof note, two checker/test
  scripts, three dossier documents, knowledge, current status and roadmap.
  No Git/GitHub writes; manual integration only.
- Exactly one next atomic task after acceptance: attempt an exact radius-10
  bridge at n=45,46, finding a rational separator and closing four strict
  gates before any onset promotion. That task has not begun.
