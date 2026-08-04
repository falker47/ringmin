# Task Log

Append entries; failed attempts and contradictory evidence are retained.

## 2026-08-04 19:18 +02:00 - Startup

- Repository root resolved to the current working tree.
- Initial `git status --short`: exit `0`, no output; the tree was clean.
- Observed `HEAD`: `5f9be1ab107ce6fba2eba586e9d30eb859c7d330`
  (`research: prove all-n radius-1 seam obstruction`).
- Read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the ranked
  roadmap, the radius-1 proof and dossier, all dossier templates, the
  model/Descartes/Supnick/seam/open-problem portions of the paper, production
  pattern/geometry/chain helpers, and relevant tests.
- Mode: `STRICT`.
- Expected delta: radius-2 proof note, task-local checker and dossier, live
  status, and conditional stable-memory/roadmap updates only.
- Protected paths: paper/arXiv assets, production source and tests, scripts,
  results/certificates/frontiers, verifier, README/report, CI, dependencies,
  publication metadata, and generated assets.
- A raw `git rev-parse HEAD` was rejected by Git's dubious-ownership guard;
  the read-only command succeeded with command-local `safe.directory`. No Git
  configuration or repository state changed.
- Known risks: confusing a formal seam with global geometric optimality;
  using the unshifted Supnick parity convention; accepting an extraneous
  squared Descartes root; overlooking the `n <= 8` no-threshold domain;
  assuming the raw deficit is monotone; treating finite diagnostics as proof.

## 2026-08-04 19:18 +02:00 - Analytic reduction in progress

- Shifted the index-level Supnick construction from `{1,...,n-1}` to
  `{2,...,n}` and derived candidate parity edge/closure formulas.
- Reduced the seam sign to comparison of the increasing implicit chain root
  with a radius-2 Descartes threshold whose reciprocal increases with `n`.
- Found exact candidate bridges `R_{2,12}<17<T_{2,12}` and
  `T_{2,13}<14<R_{2,13}`.
- Three independent read-only reviews are auditing the shifted convention,
  threshold algebra/domain, exact bridge bounds, and possible counterexamples.
- Claim status remains `IN_PROGRESS` until the written proof, checker, and
  adversarial verification pass.

## 2026-08-04 19:21 +02:00 - Exact proof completed

- Fixed the shifted Supnick representative as the rank-`n-1` maximum tour on
  `-theta`, translated by `i -> i+1`, and derived both parity edge sets and
  closure sums.
- Proved `R_{2,n+1}>R_{2,n}` using fixed-`R` chain minimality and deletion of
  the largest vertex; no false induced-order equality is used.
- Derived the bounded-pocket curvature
  `P_n(x)=x+alpha_n+2 sqrt(alpha_n x+beta_n)` and the exact seam sign
  criterion relative to `1/2`.
- Proved that no positive threshold exists for `4<=n<=8`, while for `n>=9`
  the unique threshold is
  `T_{2,n}=1/kappa_{2,n}` with
  `kappa_{2,n}=1/2+1/n+1/(n-1)-2 sqrt((2n+1)/(2n(n-1)))`.
- Proved `T_{2,n}` strictly decreases by comparing `P_{n+1}(x)` with
  `P_n(x)` at fixed `x`, without differentiating or assuming raw-deficit
  monotonicity.
- Closed the crossing exactly with
  `R_{2,12}<17<T_{2,12}` and `T_{2,13}<14<R_{2,13}`. The chain sides use
  rational sine bounds and elementary arcsine inequalities; the threshold
  sides use rational square comparisons.
- Mathematical classification promoted from conjecture to exact theorem:
  positive deficit for `4<=n<=12`, negative deficit for every `n>=13`.

## 2026-08-04 19:23 +02:00 - Independent checker added

- Added task-local `check_seam.py`; it imports no production package.
- Exact `Fraction` checks cover the `n=8,9` threshold-domain boundary, both
  `n=12,13` threshold inequalities, all chain-table entries, and the aggregate
  arcsine bounds.
- Two independent shifted-order constructors and parity edge formulas are
  checked over a user-selected finite range.
- High-precision roots, thresholds, and deficit signs are recomputed at two
  precision levels. The finite scan is diagnostic only, not the all-`n`
  proof.
- The scan found that the raw deficit is not nonincreasing:
  `Delta_{2,29}=-0.18210378851879555...` but
  `Delta_{2,30}=-0.18209965250262137...`.

## 2026-08-04 19:24 +02:00 - Adversarial-review correction

- One read-only reviewer initially reported incompatible chain radii
  `R_{2,12}=16.698...` and `R_{2,13}=20.162...`.
- Audit showed that the reviewer had called the complementary
  `supnick_min_tour`, not the chain-minimizing `supnick_max_tour` for
  `-theta`. Corrected production diagnostics give
  `R_{2,12}=15.258870430448...` and `R_{2,13}=18.277543500174...`, agreeing
  with the independent checker and the proof convention.
- The mistaken finite values and their raw-deficit scan were discarded. The
  analytic Descartes derivation was order-independent and unaffected.

## 2026-08-04 19:28 +02:00 - Verification and durable memory

- Full independent checker `n=4..200`, 60/100 digits: exit `0`; every exact,
  shifted-order, parity-edge, sign, threshold, and stability check passed.
  Maximum relative root delta was `4.1752866e-46`; maximum absolute deficit
  delta was `1.4682707e-46`.
- Optimized-mode checker `n=4..30`, 40/60 digits: exit `0`; exact checks
  remained active and passed under `python -O`.
- Production `supnick_max_tour` exact-representative and `interleave`
  cycle-equivalence comparison through `n=200`: exit `0`.
- `python -m pytest`: exit `0`; `12 passed in 28.36s`.
- Three independent read-only reviews audited the actual proof note and
  checker. All reported no remaining issue in the shifted convention,
  Descartes algebra/domain, monotonicities, exact arithmetic, optimized-mode
  safety, or epistemic scope.
- Updated `PROJECT_KNOWLEDGE.md` and the roadmap only after the exact theorem
  and reviews were stable. The sole proposed next task is the radius-3 seam
  analogue; it was not started.
- Final complete-delta and protected-path audit remains before the
  `READY_FOR_REVIEW` transition.

## 2026-08-04 19:31 +02:00 - Final audit and handoff

- `git status --short --untracked-files=all` contains exactly the three
  authorized tracked modifications and five authorized untracked additions.
- Read the complete tracked diff and every untracked addition in full after
  the substantive edits.
- Direct strict-UTF-8, no-BOM, final-LF, and trailing-whitespace audit:
  `UTF8_FINAL_LF_TRAILING_WS=PASS files=8`.
- `git diff --check`: exit `0`, no output; direct checks cover the untracked
  files omitted by ordinary Git diff.
- Explicit protected-path diff and status: exit `0`, no changed path. No
  production, test, script, result, certificate, verifier, paper,
  README/report, CI, dependency, publication, or generated path changed.
- Final mathematical status: `PROVED`. Task state: `READY_FOR_REVIEW`.
- Residual uncertainty: independent human review and manual commit remain;
  no global-optimum, floating-circle, later-cascade, hosted-CI, or certificate
  claim is made.
- Exactly one next atomic task after acceptance: prove or refute the radius-3
  seam classification on `{3,...,n}` with proposed onset `n=17`, including
  the physical threshold domain and exact endpoint bounds.
