# Task Log

Append entries; failed attempts and contradictory evidence are retained.

## 2026-08-04 20:50 +02:00 - Startup

- Repository root resolved to the current working tree.
- Initial `git status --short`: exit `0`, no output; the tree was clean.
- Observed `HEAD`: `e23663ea4c831ccfd50380063894b5d8574cabd7`
  (`research: prove all-n radius-2 seam threshold`).
- Read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the ranked
  roadmap, both existing seam proof notes and task-local checkers, the
  radius-2 dossier, all dossier templates, the relevant angular/Descartes/
  Supnick portions of the paper, production pattern helpers, and relevant
  tests.
- Mode: `STRICT`.
- Expected delta: one general proof note, this dossier, one task-local
  checker, live status, and conditional stable-memory/roadmap updates only.
- Protected paths: paper/arXiv assets, production source and tests, scripts,
  results/certificates/frontiers, verifier, README/report, CI, dependencies,
  publication metadata, generated assets, and the existing `k=1,2` notes.
- A combined read-only Git command encountered the sandbox ownership guard;
  later Git reads use command-local `safe.directory`. No Git configuration or
  repository state changed.
- Known risks: branching parity on `n` instead of `N=n-k+1`; accepting the
  extraneous squared Descartes root; taking a reciprocal before the physical
  threshold domain; assuming raw-deficit monotonicity; mistaking a seam
  theorem for global realizability or floating behavior; accidentally
  classifying the exact `k=3` onset from a finite scan.

## 2026-08-04 20:50 +02:00 - Exact derivation

- Shifted the rank-level Supnick construction by `k-1`, derived both parity
  edge/closure formulas, and proved that `k` has neighbors `n-1,n`.
- Proved existence and uniqueness of `R_{k,n}`, strict growth by deleting the
  largest vertex from a fixed-`R` minimizing cycle, and divergence from the
  exact lower bound `R_{k,n}>=k(csc(pi/(n-k+1))-1)`.
- Reduced the seam sign to the bounded Descartes curvature compared with
  `1/k`.
- Proved that a positive crossing exists exactly for `n>=4k+1`, derived the
  physical minus root and rejected the plus root in the unsquared equation.
- Proved `T_{k,n}` strictly decreases while `R_{k,n}` strictly increases and
  diverges. Thus `R_{k,n}-T_{k,n}` strictly increases to infinity, giving at
  most one equality and a nonempty persistent obstruction tail.
- Three independent read-only derivations audited the order, root,
  Descartes algebra/domain, threshold monotonicity, divergence, transition
  quantifiers, checker design, and the `k=1,2` specializations. They found no
  missing lemma or counterexample.
- Claim status promoted from conjectural to exact theorem for the formal
  fixed-`k` seam only. Exact onsets for `k>=3` remain unresolved.

## 2026-08-04 20:52 +02:00 - Proof note and checker draft

- Added `research/FIXED_K_SUPNICK_SEAM.md` with the complete exact proof and
  explicit non-implications.
- Added a production-independent task-local checker using explicit
  `_require` gates, `Fraction` algebra, two order constructors, parity edge
  checks, stable/direct threshold formulas, and two-precision mpmath scans.
- Initial diagnostic run for `k=1..3`: exit `0`; exact algebra/domain,
  convention, edge, Descartes-sign, root/threshold monotonicity, and precision
  gates passed. Its observed finite `k=3` sign change is explicitly not used
  to classify an exact onset.
- Full verification and final audit remain.

## 2026-08-04 20:56 +02:00 - Verification and independent review

- Full task-local checker for `k=1..12` through `n=4k+41`, at 60/100
  decimal digits: exit `0`. Exact algebra/domain, shifted order, parity-edge,
  root growth, threshold decrease, Descartes-sign, finite persistence, and
  precision-stability gates all passed. Maximum relative root delta was
  `4.9972035e-47`; maximum absolute deficit delta was `2.5066708e-47`;
  maximum direct/stable kappa delta was `1.4287342e-101`.
- Optimized-mode checker for `k=1..4`, 40/60 digits: exit `0`; every explicit
  exact and numerical gate remained active under `python -O` and passed.
- Read-only comparison with production `supnick_max_tour` and `interleave`:
  exit `0`; both are cycle-equivalent to the task-local shifted convention
  for 1,580 cases (`k=1..20`, tour sizes `3..80`).
- `python -m pytest`: exit `0`; `12 passed in 34.50s`.
- Three independent read-only agents audited the actual proof and checker.
  They found no actionable issue in the parity formulas, root arguments,
  Descartes orientation/domain, physical branch, rationalization, threshold
  monotonicity, equality quantifiers, corollaries, optimized-mode safety,
  finite-scan labeling, or non-implication scope.
- One reviewer suggested only a clarity improvement to the plus-root
  rejection. The note now states directly that the unsquared equation
  requires a nonnegative side while the plus root makes it strictly negative.
- Reviewer-run diagnostics are independent corroboration and are not
  represented as commands run by the primary task.

## 2026-08-04 20:58 +02:00 - Durable memory

- Updated `PROJECT_KNOWLEDGE.md` only after the complete proof and three
  reviews: general fixed-`k` eventual seam persistence is now an exact
  theorem; exact onsets for `k>=3` and all global-floating claims remain open.
- Updated the ranked roadmap: the next atomic task is reduced to exact
  endpoint inequalities at `n=16,17` for the proposed radius-3 onset, reusing
  the general theorem rather than repeating it.
- Replaced the live current-status entry with this task and exactly one next
  atomic task.
- Final complete-delta, encoding/whitespace, and protected-path audit remains
  before `READY_FOR_REVIEW`.

## 2026-08-04 21:04 +02:00 - Final audit and handoff

- `git status --short --untracked-files=all` contains exactly the three
  authorized tracked modifications and five authorized untracked additions.
- Read the complete tracked diff and all five untracked files in full after
  the substantive edits.
- The first direct whitespace command used an incorrect PowerShell regex
  character class and falsely flagged the final `t` in a heading as trailing
  whitespace. No file was changed in response. The corrected `[ \t]+$`
  check passed.
- Direct strict-UTF-8, no-BOM, final-LF, and trailing-whitespace audit:
  `UTF8_NO_BOM_FINAL_LF_TRAILING_WS=PASS files=8`.
- `git diff --check`: exit `0`, no output; direct checks cover the five
  untracked additions omitted by ordinary Git diff.
- Explicit protected-path status over paper assets, production source/tests,
  scripts, results, verifier, README/report, CI, dependencies, publication
  metadata, and existing seam notes/dossiers: exit `0`, no changed path.
- Git warned that the sandbox account could not read the user's global ignore
  file; the explicit status and tracked-diff checks were unaffected.
- Final mathematical status: `PROVED`. Task state: `READY_FOR_REVIEW`.
- Residual uncertainty: independent human review and manual commit remain; no
  exact `k>=3` onset, global-optimum, floating-circle, hosted-CI, or
  certificate claim is made.
- Exactly one next atomic task after acceptance: prove or refute the proposed
  radius-3 onset `s_3=17` using exact endpoint inequalities at `n=16,17`.
