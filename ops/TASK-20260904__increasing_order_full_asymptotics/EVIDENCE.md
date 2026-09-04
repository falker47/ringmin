# Evidence

## Environment

```text
repository_head=ca3d0ee2d705a1528fce08a50ff33d321b4b22b3
platform=Windows PowerShell sandbox
python=3.14.3
mpmath=existing environment, 70 decimal digits in task-local checker
dependency_source=existing interpreter; no installation or network access
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `R_chain(1,2,...,n)=n^2/(2*pi)+O(n)` | exact asymptotic theorem | uniform angular estimate, exact increasing edge-weight bounds, root bracketing and reciprocal transfer | high-precision chain roots through `n=256` | finite roots corroborate but do not prove the limit |
| The increasing chain-root placement is eventually infeasible | exact asymptotic obstruction | closure-forced tightness and the exact fixed-endpoint limit for the `(n,2)` seam path | independent 70-digit deficit evaluation | checker sees a finite onset only; the sign tail rests on the nonzero analytic limit |
| The explicit gaps at `Rhat_n=n^2/(2*pi)+n^(3/2)` satisfy every pairwise constraint eventually | exact constructive theorem | `sqrt(n)E_n->4*pi^2`, uniform `max theta=O(1/n)`, ordered-triple inequality, and separate checks of both cyclic paths | direct high-precision all-pairs and Cartesian audit for six sizes through `n=256`, without importing `src/ringmin` | finite diagnostic is not the all-`n` proof and does not establish a sharp additive scale |
| `R_full(1,2,...,n)/n^2->1/(2*pi)` | proved fixed-order corollary | chain lower bound plus explicit feasible upper construction | independent finite gap audit | no fixed-order subleading asymptotic |
| `limsup R*(n)/n^2<=1/(2*pi)` and `R*(n)=Theta(n^2)` with the imported `C_term` lower bound | proved global corollary | minimization over orders plus accepted terminal-subset theorem | accepted exact/symbolic `C_term` audits rerun | no global limit, endpoint sharpness, or increasing-order optimality |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` at startup | 0; empty | clean task base | ignored files |
| unscoped `git rev-parse HEAD` | 128; dubious-owner guard | exposed environment ownership restriction | repository content |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin rev-parse HEAD` | 0; `ca3d0ee2d705a1528fce08a50ff33d321b4b22b3` | exact base commit without changing Git config | worktree content |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| first `python -B ops/TASK-20260904__increasing_order_full_asymptotics/check_highprec.py` | 1; all pairwise checks passed, final over-tight convergence assertion failed at `n=256` (`-4.09459...` versus limiting `-5.205...`) | retained negative evidence about an unjustified finite-rate threshold | no theorem was rejected; the failed threshold was not a proof premise |
| corrected `python -B ops/TASK-20260904__increasing_order_full_asymptotics/check_highprec.py` | 0; six sizes `8..256`, final PASS | independent chain roots, seam sign trend, exact gap closure, every directed pair constraint, and Cartesian reconstruction at 70 digits | universal quantifiers or sharp subleading rate |
| `python -B -I -S ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py` | 0; 894 parity comparisons and exact brackets pass | accepted exact dependency and `C_term` interval | new upper construction |
| `python -B ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py` | 0; 16 identities pass under SymPy 1.14.0 | accepted integral, coefficient, derivative, uniqueness, and boundary identities | new full-feasibility proof |
| first direct eight-file text audit | 1; false trailing-whitespace reports on every file due to a single-quoted PowerShell `` `t`` regex | exposed a checker quoting error | file whitespace; separately checked with `Select-String` and corrected audit |
| corrected direct eight-file text audit | 0; every file PASS | strict UTF-8, no BOM/CR, one final LF, and no trailing whitespace in all changed/added files | mathematical correctness |
| `git diff --check` | 0; no output | tracked whitespace and conflict markers | untracked files, handled by direct audit |

Material output from the successful independent checker:

```text
n chain/n^2 scaled_seam_deficit sqrt(n)*extra guard_margin min_slack
8   0.09749243472264164   3.992329185804889   12.68953633368272  4.0918450  -4.5278e-72
16  0.1246171370729806    0.3130051824314164  16.01586342416476  3.7381598  -9.0557e-72
32  0.1406329311201934   -1.733823145930988   19.52276924075198  3.2807490  -1.3584e-71
64  0.1494955010154611   -2.895230387484515   23.00370718535954  2.7711730  -1.2452e-71
128 0.1541989108886061   -3.616499589949680   26.26205105676941  2.2600606  -1.7545e-71
256 0.1566361931872419   -4.094591643686840   29.14960455202712  1.7872127  -3.5091e-71
PASS: independent high-precision chain, seam, gap, and Cartesian checks
```

The tiny negative `min_slack` values are below `4e-71` and occur on exact
adjacent tangencies under 70-digit rounding; the asserted tolerance is
`1e-55`. The proof itself uses exact inequalities.

## Artifact and provenance checks

Not applicable: no production result, finite certificate, generated artifact,
or paper asset is in scope.

Final authoritative-note/checker SHA-256 values:

```text
c1fe2dac6b6ddab8d3b183a510c7efdeccfbf5cbfcd8a5e3f4bc07d62f141501  research/INCREASING_ORDER_FULL_ASYMPTOTICS.md
09a52f21345ca516384b3320f5905bdac0429b3a49d1770bd74b4adf1baf97db  ops/TASK-20260904__increasing_order_full_asymptotics/check_highprec.py
```

## Failed checks and negative evidence

- The unscoped read-only HEAD query hit Git's dubious-owner guard and was
  rerun with command-local `safe.directory`; no Git configuration changed.
- The first independent-checker run retained above rejected an unjustified
  expectation about convergence speed at `n=256`. The threshold was weakened
  to the sign/order consequences actually expected from the proof. All
  pairwise angular and Cartesian checks had already passed in that failed run.
- The first direct text-audit regex used a backtick tab escape inside a
  single-quoted PowerShell string, where it remained literal and matched
  ordinary line-final `t` characters. A separate `Select-String` check found
  no trailing-whitespace lines, and the corrected `\x09` audit passed all
  files. No content edit was needed for this checker failure.
- The exact chain-root gaps are not fully feasible asymptotically: the
  `(n,2)` two-edge seam deficit has the strict negative limit shown in the
  proof. This rules out closure-only reasoning but not the leading coefficient.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three intended tracked
  modifications and five intended untracked additions; known global-ignore
  warnings only.
- Complete tracked diff inspected after the proof and synchronization edits.
- All five untracked additions were read in full after their final content
  edits: the proof note and four dossier files.
- Direct eight-file audit: strict UTF-8, no BOM/CR, exactly one final LF, and
  no trailing whitespace; exit 0 after the retained regex-checker correction.
- `git diff --check`: exit 0, no output.
- `git diff --cached --name-only`: exit 0, empty; the index is unchanged.
- Protected-path diff over `AGENTS.md`, `README.md`, `REPORT.md`,
  `paper_assets/`, `results/`, `verify.py`, `src/`, `tests/`, `scripts/`,
  build and dependency files: exit 0, empty.
- No generated file changed. Repository HEAD remains
  `ca3d0ee2d705a1528fce08a50ff33d321b4b22b3`.

No pytest, production verifier, certificate regeneration, paper build, or
hosted CI run was required: no corresponding implementation, artifact, or
publication source changed.

## Residual uncertainty

Independent human proof review remains pending. The theorem does not locate
the least `n` for the construction, find the sharp additive scale of the
fixed-order full radius, establish global optimality of the increasing order,
show that either known coefficient endpoint is sharp, or prove existence of
`lim R*(n)/n^2`. The finite certification scope remains `3<=n<=14`.
