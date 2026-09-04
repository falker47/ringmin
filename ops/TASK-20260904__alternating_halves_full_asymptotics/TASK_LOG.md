# Task Log

Append entries; do not erase failed attempts or contradictory evidence.

## 2026-09-04 - Startup

- Repository HEAD: `667f666afb6f74c010111364fd787bd09cf13590`.
- Working tree: clean before opening this task.
- Read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the pertinent
  definitions, fixed-order and global-asymptotic ledgers, the roadmap, the
  increasing-order asymptotic proof/dossier, evaluator code, and templates.
- Task mode: STRICT. Expected delta and protected paths are recorded in
  `TASK_STATUS.md`.
- Initial discriminator: derive the exact chain coefficient; then formulate
  the minimum leading gap mass forced by local valleys and longer pair paths.
  A candidate constant is acceptable only with a constructive all-pairs upper
  bound and a matching pairwise lower obstruction.
- Reviewer values are retained only as an external finite diagnostic, never as
  a proof premise.

## 2026-09-04 - Analysis

- The adjacent square-root Riemann sum gives the chain constant
  `J/(2*pi)`, with
  `J=3sqrt(2)/4-log(3+2sqrt(2))/8`.
- Partitioned the cyclic gaps into disjoint cells around each low radius.
  Every cell is forced by the maximum of its two adjacent constraints and
  the chord joining its high neighbors.
- An exploratory leading-order LP initially exposed the switch between
  consecutive-high chords and adjacent pairs and a boundary allocation at
  the seam. It was deleted after the exact construction made it redundant.
- Proved a thick-shell triangle inequality for `a<=b<=c<=2a`, then used it
  to show that an increasing high-radius cycle satisfying its adjacent chords
  satisfies every high-high pair in both directions, including the seam.
- Allocating each positive valley deficit to the low-to-high outgoing gap
  gives total `S_m(R)`. Contracting valleys, applying the thick-shell lemma,
  and lifting by angular monotonicity proves all high-high, low-high, and
  low-low constraints. Together with the disjoint-cell lower bound this proves
  the exact finite formula `R_full=the unique root of S_m(R)=2*pi`.
- Uniform angular scaling gives the continuum maximum. High chords dominate
  for `i/(2m)<1/6`, adjacent pairs dominate above `1/6`, and the seam is an
  exact but `O(1/n)` cell. Integration gives
  `K=J-1/12+log(3)/8` and full coefficient `K/(2*pi)`.
- Exact integral inequalities prove `J<K<1`; hence the fixed-order full limit
  is strictly below `1/(2*pi)` without numerical input.
- Deleting radius `2m` from the even construction transfers only the upper
  bound `limsup R*(n)/n^2<=K/(2*pi)` to odd sizes. No global equality or limit
  is inferred.

## 2026-09-04 - Diagnostic development and retained failures

- A first optional SciPy Floyd-Warshall branch raised `NegativeCycleError` at
  the deliberately infeasible lower bracket instead of returning a Boolean.
  The preceding 70-digit formula-root and direct gap checks had passed. The
  redundant float64 branch was removed; the final checker directly audits
  both cyclic paths for every pair without importing production code.
- The first two symbolic-checker runs stopped at the `J` identity because
  SymPy retained an equivalent `acosh(sqrt(2))` normal form. The checker was
  corrected with the exact identities
  `acosh(sqrt(2))=log(1+sqrt(2))` and
  `(1+sqrt(2))^2=3+2sqrt(2)`; no proof formula changed.
- The first production cross-check command used literal backslash-`n`
  characters and exited with `SyntaxError`. It was rerun with actual command
  newlines and matched the independent formula at every selected size.
- A later unscoped `git status` hit the environment's dubious-owner guard;
  final Git reads use command-local `safe.directory` and do not alter Git
  configuration.

## 2026-09-04 - Verification

- Independent 70-digit default diagnostic over `n=40,80,160,320,640`: exit
  `0`; all formula roots, exact closure, and directed all-pairs gaps passed.
  The last three full ratios are `0.139557268125223375`,
  `0.140940266075415282`, and `0.141635631882792259`.
- Optimized-mode independent diagnostic over every even `n=4..38`: exit `0`;
  all 18 small cases passed, including the chain/full equality at `n=4,6,8`
  and the first observed chord-controlled cell at `n=10`.
- Symbolic checker in normal and optimized modes: both exit `0`; all 11
  integral, constant-assembly, switch, shell-gate, and exact inequality gates
  passed under SymPy 1.14.0.
- Production-coupled fixed-order cross-checks at `n=10,20,40,80,160`: exit
  `0`; all displayed chain/full ratios agree with the independent roots to
  float64 tolerance.
- Final documentary, diff, protected-path, and whitespace checks are recorded
  in `EVIDENCE.md`.

## 2026-09-04 - Handoff

- Final state: `READY_FOR_REVIEW`.
- The exact finite fixed-order formula, its chain/full limits, strict
  improvement over `1/(2*pi)`, and the limited all-integer global limsup
  corollary are synchronized in the proof note, owning ledgers, roadmap, and
  current status.
- Residual uncertainty is independent human proof review; no broader order,
  sharp subleading term, global equality, or certification extension was
  attempted.
- Exactly one next atomic task: independently review the alternating-halves
  cellwise characterization, thick-shell/seam all-pairs proof, constants, and
  deletion corollary without optimizing another order family.
