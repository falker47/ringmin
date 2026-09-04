# Task Log

## 2026-09-05 — Startup and bounded discriminator

- HEAD: 2a7ccef05a2217146387e92507b2eab9910a174f; working tree clean.
- Initial ordinary git status failed on sandbox ownership. Read-only
  per-command safe.directory resolved this without changing Git config;
  the sandbox emitted warnings about the user-global ignore file.
- Read AGENTS.md, canonical index/status, pertinent fixed-order ledger,
  cell theorem, roadmap, preceding dossier/checker, templates, angular
  anti-Monge proof and exact seam branch discussion, and environment.
- Mode STRICT. The expected delta and protected paths are in TASK_STATUS.
- Algebraic locality: the middle cell is symmetric; only the two external
  cells can change, except that m=2 makes every cell invariant.
- Before universal exchange proofs, predeclared finite sign/shift probes
  in TASK_STATUS. Retain failures rather than extending the factorial range.

## 2026-09-05 — Pre-proof falsification completed

- check_falsification.py exited 0: 872 orders, 15114 oriented cyclic
  swaps and 5232 fixed-radius shift comparisons for m=2..6.
- Same m=3 swap (4,5,6)->(5,4,6) reverses sign between R=0.1 and
  R=100. Low/high increasing differences and their reverse both fail.
- First retained shift witness: m=4, P=(6,8,7,5), R=10 beats every
  increasing cyclic shift. No rule was promoted from the scan to proof.
- Targeted 40-digit atan checks (no imports from checker/production)
  corroborated the m=3 branches at R=0.1,1,100 and this shift witness.
  The R=10 witness does NOT beat the best shift's full-radius root:
  its root is about 5.84042, versus 5.78356 for shift (7,8,5,6).
  Fixed-R score dominance must not be transferred blindly to roots.
- A bounded check of the four m=4 shifts and their four swaps at
  R=1,2,5,10,100 found the simpler R=1 improvement
  (8,5,6,7)->(8,6,5,7). This motivates a small-R structural corollary,
  not a general optimization experiment.

## 2026-09-05 — Exact route selected after falsification

- Derive an explicit branch threshold in the moving high using the
  positive pocket-curvature branch and a direct half-angle proof.
- Express each cell increment as two angular increments separated by
  a clipped threshold. Their difference gives an exhaustive branch rule.
- Prove conditional exchange by pointwise ordering of derivative anchors;
  retain the high/high supermodularity that survives and identify the
  low/high increasing-differences property that fails.
- In the exact subdomain 0<R<=1 every cell is chain-active. Local exchange
  then gives a necessary candidate structure with only m-2 choices for
  m>=3, and rules out every cyclic shift for m>=4 in that subdomain.
- Post-proof checks are bounded: exact Fraction branch/sqrt/asin intervals
  for the retained witnesses, symbolic threshold/derivative algebra,
  and 70-digit independent atan audits of the formula, seams and all
  branch types for m=2..6 on the original six radii. No RNG.

## 2026-09-05 — Verification and integration

- Both retained scripts exited 0 on the first post-proof run. The exact
  checker proved the rational enclosures, symbolic identities and branch
  gates; 30228 actual swaps agreed with the independent atan scorer to
  less than 3e-70, with 12000 conditional sign probes.
- The small integer domain realizes five branch pairs (CC, CH, CM, HC,
  MC). Additional positive-real cell probes, explicitly not integer
  permutations, exercise all nine pairs and exact threshold boundaries.
- Final checker refinement applies the float64 guard to Delta itself
  before sign multiplication, and explicitly compares the nine pairs of
  positive-real increments. Both scripts reran, exit 0; retained first
  witnesses and aggregate counts were unchanged.
- Proof, sole owning ledger and roadmap integrated. The numerical
  full-root comparison above was kept task-local; the stable proof note
  makes only the exact fixed-R and conditional root implications.
- A combined delete/add patch for CURRENT_STATUS.md was rejected by
  apply_patch as duplicate operations on the same path, without changing
  that file. Replaced its content with one UTF-8 write, exit 0.
- Final status, content/whitespace inspection and protected-path audit
  remain the completion gate; no production tests or global verifier are
  required because their source, inputs and claims are unchanged.

## 2026-09-05 — Final review and handoff

- Inspected the complete tracked diff and every untracked file directly;
  re-read portions omitted by tool-output truncation. No unrelated change.
- Added the exact rational branch gates to Section 6 for direct human
  review. An inline Fraction check reproduced all eight triples, exit 0.
  Clarified local symbol definitions in the owning ledger.
- Explicit whitelist/text audit exited 0: exactly three tracked changes,
  six new files, no staged files, all nine UTF-8/newline/whitespace checks
  passed, and every other tracked path protected. git diff --check
  exited 0 with no output. Source hashes checked and evidence synchronized.
- Claims have one thematic owner; PROJECT_KNOWLEDGE navigation still
  suffices. No generated asset, global bound or certified scope changed.
- State: READY_FOR_REVIEW; independent human review pending.
- Exactly one next atomic task: independently review the local exchange
  theorem, its fixed-order dependency, branch/equality cases, small-R
  reduction and minimal counterexample; reproduce the bounded checks and
  record acceptance or precise corrections, without general optimization.
