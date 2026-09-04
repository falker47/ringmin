# Evidence

## Environment

```text
repository_head=d50fd5eb6d130d6da4193793d4073b83fd881d2d
platform=Windows PowerShell sandbox
python=3.14.3
sympy=1.14.0
mpmath=1.3.0
dependency_source=existing interpreter; task-local checker imports no ringmin production code
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| The continuum functional holds for positive-measure fixed finite unions in `[0,1]` | exact continuum theorem | section 2: parity rank sums plus uniform denominator/arcsine error using only `1<=a,b<=n`, then root bracket | prior exact parity audit and finite continuum diagnostic rerun | imports arbitrary-radii Supnick theorem; finite diagnostic predates the zero-support extension |
| `Q_A(t)<=1-L+t` for fixed finite-union `A subset [0,1]` | exact theorem | section 7: tail capacity and generalized inverse | exact exhaustive rational-grid audit | audit is finite; analytic proof supplies continuum quantifier |
| `C(A)<=C([1-L,1])`, with equality only modulo null sets | exact theorem | pointwise integrand comparison, almost-everywhere equality on both quantile halves, distribution reconstruction | exact grid equality pattern | one fixed normalized subset |
| `C(A)<=C_term`, with unique measure and shape at equality | proved corollary | accepted unique terminal-length optimization plus preceding fixed-measure theorem | accepted exact/symbolic optimizer checks rerun | no `n`-dependent/coupled-subset or geometric upper-bound conclusion |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short --untracked-files=all` | 0; no paths at startup | clean task base | ignored files |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin rev-parse HEAD` | 0; `d50fd5eb6d130d6da4193793d4073b83fd881d2d` | exact base commit | worktree content |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| `python -B ops/TASK-20260904__finite_union_terminal_dominance/check_quantile.py` | 0; 8178 sets, 45057 rank cells, 78 terminal equality masks pass | exact quantile direction and equality pattern for all unions of grid cells with denominators 1 through 12 | continuum proof or asymptotic root |
| `python -B ops/TASK-20260904__one_gap_terminal_subset_variation/check_symbolic.py` | 0; 8 identities and parity counts through size 100 pass | accepted functional dependency's parity formulas and variation identities | new quantile theorem |
| `python -B ops/TASK-20260904__one_gap_terminal_subset_variation/check_finite.py` | 0; 298 edge-set comparisons and 9 continuum diagnostics across both parities | accepted rank formulas and finite behavior of the functional | exact limits, zero-support extension, or new dominance theorem |
| `python -B -I -S ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py` | 0; 894 edge comparisons and exact optimizer intervals pass | accepted terminal optimizer dependency and reported brackets | new fixed-measure comparison |
| `python -B ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py` | 0; 16 identities pass | accepted terminal integral, derivative, uniqueness, and boundary identities | generalized-inverse equality proof |
| direct nine-file text audit | 0; strict UTF-8, no BOM/CR, one final LF, no trailing whitespace | every tracked modification and untracked addition | mathematical correctness |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check` | 0; no output | tracked whitespace and conflict markers | untracked files, handled by direct audit |
| scoped protected-path `git diff --name-only` | 0; no output | no paper, production, certificate, test, generated overview/report, build, or dependency drift | ignored external state |

## Artifact and provenance checks

Not applicable: no production result, finite certificate, generated artifact,
or paper asset is in scope.

Final authoritative-note/checker SHA-256 values:

```text
ddd8e07d8528c3d5343f2e9c3399a7b1c98412fe5b49829d6b525662118708df  research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md
f8e9204055c0ca19bd9054c7e3cc6dfdc4d08ab57ce006ad2c46675372c22e98  ops/TASK-20260904__finite_union_terminal_dominance/check_quantile.py
```

## Failed checks and negative evidence

- The first unscoped read-only `git status` hit the sandbox's dubious-owner
  guard. It was rerun with a command-local `safe.directory`; no Git
  configuration or history was changed.
- The first template lookup used `ops/_TEMPLATES`, but the repository stores
  them at root `_TEMPLATES`. The correct files were then read in full.
- One combined patch attempted both deletion and addition of
  `CURRENT_STATUS.md`; `apply_patch` rejected the duplicate target
  atomically. The file was subsequently updated in place.
- No contrary mathematical evidence was found. The exact finite-grid audit
  found equality only for terminal cell unions at every tested measure.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly five intended tracked
  modifications and four intended untracked additions; only the known
  unreadable-global-ignore warning; exit 0.
- `git diff --name-only`: exactly `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, the two relevant research notes, and the roadmap.
- `git ls-files --others --exclude-standard`: exactly the three dossier files
  and task-local checker. Every addition was read in full.
- `git diff --cached --name-only`: exit 0, empty; the index is unchanged.
- Complete tracked diff inspected separately for every modified file after
  the analytic and synchronization edits.
- Direct nine-file audit: strict UTF-8, no BOM/CR, LF endings, exactly one
  final newline, and no trailing whitespace; exit 0.
- `git diff --check`: exit 0, no output.
- Protected-path diff over `AGENTS.md`, `README.md`, `REPORT.md`,
  `paper_assets/`, `results/`, `verify.py`, `src/`, `tests/`, `scripts/`,
  build and dependency files: exit 0, empty.
- No generated file changed. Repository HEAD remains
  `d50fd5eb6d130d6da4193793d4073b83fd881d2d`.

No pytest, production verifier, certificate regeneration, paper build, or
hosted CI run was required: no corresponding implementation, artifact, or
publication source changed.

## Residual uncertainty

Independent human proof review and manual integration remain pending. The
task-local exhaustive audit is finite and corroborative, not a proof
assistant. The continuum theorem still imports the published arbitrary-radii
Supnick ordering theorem. The result optimizes one fixed normalized
finite-union subset; it does not cover `n`-dependent/diagonal subsets,
growing component counts, coupled multiple-subset lower bounds, geometric
upper bounds, the true asymptotic coefficient, or certification beyond
`n=14`.
