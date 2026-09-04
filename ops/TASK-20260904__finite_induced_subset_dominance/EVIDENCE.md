# Evidence

## Environment

```text
repository_head=32f97d2b3bf37aa1603df02a6e44af17a2b98bba
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing interpreter; task-local checker is standard-library only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Every induced subset is chain-dominated by the terminal subset of the same finite cardinality, strictly unless terminal | exact finite theorem | rank upper bound, common Supnick rank edges, strict angular monotonicity, decreasing-root transfer | standard-library enumeration of 3797 subsets | imports published arbitrary-radii Supnick theorem |
| Moving terminal subsets with `k/n->q` have normalized limit `Phi(q)` for every `q in [0,1]` | exact asymptotic theorem | parity rank Riemann sums, uniform angular expansion, root bracket; separate vanishing proof at `q=1` | accepted parity/continuum checks rerun | analytic limit, not finite certification |
| Every arbitrary single-subset sequence has `limsup B_n/n^2<=C_term`; attainment forces cardinality ratio `L_*` | proved corollary | finite dominance, compactness of cardinality ratios, exact unique terminal optimization | exact optimizer and finite envelope diagnostics rerun | no asymptotic subset-shape uniqueness; not a genuinely coupled-subset method or full geometry |
| The finite all-subset envelope divided by `n^2` tends to `C_term` | proved sharpness corollary | exact finite maximization plus terminal-array upper compactness and optimizer lower sequence | finite envelope diagnostic | no claim about lower-order envelope asymptotics |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short --untracked-files=all` | 0; no paths at startup; known global-ignore warnings only | clean task base | ignored files |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin rev-parse HEAD` | 0; `32f97d2b3bf37aa1603df02a6e44af17a2b98bba` | exact base commit | worktree content |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| `python -B ops/TASK-20260904__finite_induced_subset_dominance/check_finite.py` | 0; 3797 subsets, 3752 strict cases, 45 equalities pass for `n=3..11` | independent finite rank bounds, roots, equality, and terminal envelopes | all-`n` proof or asymptotic limits |
| `python -B -I -S ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py` | 0; 894 edge comparisons and exact optimizer intervals pass | accepted rank parities and exact reported optimizer brackets | new finite dominance or analytic limits |
| `python -B ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py` | 0; 16 identities pass; SymPy 1.14.0 | accepted integral, coefficient, derivative, uniqueness gates and boundaries | new compactness argument |
| `python -B ops/TASK-20260904__one_gap_terminal_subset_variation/check_finite.py` | 0; 298 edge-set and 9 continuum comparisons pass | independent rank convention and both parity behaviors | exact triangular-array limit |
| direct ten-file text audit | 0; strict UTF-8, no BOM/CR, one final LF, no trailing whitespace | every tracked modification and untracked addition | mathematical correctness |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check` | 0; no output | tracked whitespace and conflict markers | untracked files, handled by direct audit |
| scoped protected-path `git diff --name-only` | 0; no output | no paper, production, certificate, test, script, build, or dependency drift | ignored external state |

## Artifact and provenance checks

Not applicable: no production result, finite certificate, generated artifact,
or paper asset is in scope.

Final authoritative-note/checker SHA-256 values:

```text
8d8acdf134d80eaee749d2b5da4f7f52d32672bda2a3f12b35932eb44028004b  research/FINITE_INDUCED_SUBSET_DOMINANCE.md
b4b6e0267b17e529faed79f848a1f2f8e55871df647d1dc873642f4ac89dc319  ops/TASK-20260904__finite_induced_subset_dominance/check_finite.py
```

## Failed checks and negative evidence

- An unscoped read-only `git rev-parse HEAD` hit Git's dubious-owner guard.
  It was rerun with command-local `safe.directory`; no Git configuration or
  history was changed.
- No mathematical counterexample has been found. The finite checker remains
  corroborative and is not a premise of the proof.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly five intended tracked
  modifications and five intended untracked additions; exit 0 with only the
  known unreadable-global-ignore warnings.
- `git diff --name-only`: exactly `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, and the three relevant prior research/status files.
- `git ls-files --others --exclude-standard`: exactly the proof note and four
  dossier files. Every addition was read in full.
- `git diff --cached --name-only`: exit 0, empty; the index is unchanged.
- Complete tracked diff inspected after analytic and synchronization edits.
- Direct ten-file audit: strict UTF-8, no BOM/CR, LF endings, exactly one
  final newline, and no trailing whitespace; exit 0.
- `git diff --check`: exit 0, no output.
- Protected-path diff over `AGENTS.md`, `README.md`, `REPORT.md`,
  `paper_assets/`, `results/`, `verify.py`, `src/`, `tests/`, `scripts/`,
  build and dependency files: exit 0, empty.
- No generated file changed. Repository HEAD remains
  `32f97d2b3bf37aa1603df02a6e44af17a2b98bba`.

No pytest, production verifier, certificate regeneration, paper build, or
hosted CI run was required: no corresponding implementation, artifact, or
publication source changed.

## Residual uncertainty

Independent human proof review remains pending. The theorem imports the
published arbitrary-radii Supnick result and the accepted exact optimizer of
the terminal coefficient. It makes no statement about genuinely coupled
subset constraints, `R_full`, matching upper bounds, true asymptotics, or
certification beyond `n=14`.
