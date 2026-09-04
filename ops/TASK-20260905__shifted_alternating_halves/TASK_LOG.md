# Task Log

Append-only chronology; dates and times below are Europe/Rome.

## 2026-09-05 00:08 — Startup and expected delta

- HEAD: 7ac01f36bb7ed2c7f800867e3689c6f01c20b43b; working tree clean.
- Read AGENTS.md, PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, pertinent definition,
  fixed-order and global ledgers, roadmap, previous alternating-halves proof
  and dossier/checkers, angular model in the paper, verifier STN source, and
  dossier templates. Production files located using rg --files.
- STRICT; expected delta and protected paths are in TASK_STATUS.md.
- Initial Git read failed on dubious ownership. Command-local safe.directory
  resolved it. An attempted core.excludesFile=NUL failed; an empty command-local
  excludesFile succeeded. No configuration was changed. A guessed source path
  fixed_order.py did not exist; rg --files found evaluator.py and geometry.py.
- Analytic discriminator before computation: the high-shell angular kernel
  satisfies every triangle inequality, so contract valley cells and check
  each endpoint type. Then use h_alpha(t)=1+{t+alpha} in the cellwise maximum.
- Numerical scope: small all-shift cases plus selected wrap/transition and
  scaling cases; deterministic, bounded, independent all-pairs and Cartesian
  checks. Exact proof must precede any numerical claim of improvement.

## 2026-09-05 00:13 — Analytic resolution and first numerical discriminator

- Reproved the shell triangle inequality for arbitrary middle highs. Whole
  high paths can be contracted regardless of wrap location, and both paths
  for each endpoint type inherit the needed bound. The exact finite
  characterization survives every shift, including m=2.
- Derived the integral max functional with moving jump and three branches
  split at alpha=1/2,3/4. The moving jump contributes a negative boundary term
  to K', and K'(0)<0 has an elementary rational sign proof.
- Proved strict convexity on [0,1/2], opposite derivative signs at its ends,
  strict concavity on [1/2,3/4] and decrease on [3/4,1]. This proves a unique
  family minimizer and a strict improvement without a numerical premise.
- A 50-digit task-local Python stdin calculation evaluated the piecewise
  primitive and mp.findroot(mp.diff(K)): exit 0. It returned
  alpha=0.106784760199900199345813678515957845828 and coefficient
  0.1419959781277142849792181240454246687915. At 0.107 it returned
  0.1419959794984599508468255894688355006728. These observations match the
  user's signal; the retained checker independently repeats the evaluation
  using the split derivative integral.
- Added the authoritative proof note and bounded checkers. No failed
  mathematical lemma or numerical counterexample arose.

## 2026-09-05 00:18 — Verification

- check_exact.py: exit 0; primitive/switch/shell/derivative algebra and
  rational sign gates pass. Directed Fraction bounds prove the rational-shift
  coefficient lies in (0.14199597949,0.14199597951), strictly below baseline.
- check_diagnostic.py: exit 0; 65 finite cases and 160490 directed pair
  checks pass, including Cartesian reconstruction. Separate scipy HiGHS LP
  checks bracket all 44 all-shift cell roots for m=2..9.
- Direct split quadrature agrees with all three elementary functional
  branches; independent derivative-integral root agrees with differentiation
  of the primitive. Rotation/reflection, positive closure slack and invalid
  input checks pass. Exact outputs and guards are in EVIDENCE.md.
- Read evaluator.py and geometry.py for architecture context. No production,
  verifier or certificate tests are needed: those paths and claims are
  unchanged. These task checks are local and do not assert hosted CI status.

## 2026-09-05 00:22 — Durable memory

- Added the fixed-order theorem to its sole thematic owner and the deletion
  corollary to the global owner. Updated the strongest-bound navigation and
  roadmap priority; no paper or historical proof was revised.
- CURRENT_STATUS.md identifies this task and exactly one next independent
  review. PROJECT_KNOWLEDGE.md, README and REPORT need no scoped change.
- A patch using delete and add for CURRENT_STATUS.md in one operation was
  rejected before applying changes. Replaced it using a single update patch.
- Final full tracked/untracked and protected-path inspection remains.

## 2026-09-05 00:26 — Handoff

- Inspected the complete tracked diff and read all six untracked files in
  full. Mathematical claims remain in one fixed-order owner and one global
  owner; the central index is unchanged and routes correctly.
- Scope audit: exit 0, exactly four tracked and six untracked allowed files,
  no staged files and no protected or generated path changed. Explicit
  whitespace/newline checks cover all ten files. git diff --check: exit 0,
  no output. Final status edits receive the same audit again before handoff.
- State: READY_FOR_REVIEW. No Git history or GitHub state was written.
- Residual uncertainty: independent human proof review; no global optimum,
  sharp global coefficient, normalized global limit or subleading theorem.
- Exactly one next task: independently review the shifted-family proof,
  rational enclosure and deletion corollary, recording acceptance or precise
  corrections without extending to another order family.
