# Evidence

## Environment

```text
repository_head=512e8ffb113221666438e11877f317ca7a70646f
platform=Windows PowerShell sandbox
python=3.14.3
sympy=1.14.0
mpmath=1.3.0
dependency_source=existing interpreter; task-local checks import no ringmin production code
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `C(A)=(2/pi) integral_0^(|A|/2) sqrt(Q_A(t)Q_A(|A|-t))dt` for finite-union induced subsets | exact continuum theorem | proof sections 2 and 6: exact parity rank edges, Riemann sums, uniform angular/root bracket | exact independent rank-tour comparison plus finite continuum diagnostic | imports the published arbitrary-radii Supnick theorem; no proof assistant |
| Unified fixed-center one-gap variation `V(x)=(s/pi)[pi/4-theta-sin(theta)cos(theta)]` | exact theorem about the continuum functional | proof sections 3-4: three exact reindexing cases and Leibniz differentiation | separate SymPy primitive and derivative identities | iterated `n` then `epsilon` limit only |
| `V(x)<0` for every fixed `x in (alpha,1)` | exact theorem | `Phi'=-2cos(theta)^2<0` and `Phi(theta_alpha)=(tau-cos(tau))/2=0` | symbolic endpoint/derivative audit; prior exact rational bracket for `tau` rerun | no uniform margin as `x` approaches `alpha` |
| No fixed-center interior one-gap perturbation improves `C_term` to first order | proved corollary | negative one-sided derivative plus deletion lower-bound direction | analytic deduction | no moving-center, diagonal-limit, multi-gap, combined-subset, or true-asymptotic conclusion |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | 0; no output at startup | clean task base | ignored files |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin rev-parse HEAD` | 0; `512e8ffb113221666438e11877f317ca7a70646f` | exact base commit | worktree content |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| `python -B ops/TASK-20260904__one_gap_terminal_subset_variation/check_symbolic.py` | 0; 8 identities and parity counts through size 100 pass; SymPy 1.14.0 | primitive, lower/upper/median variation, common formula, sign derivative and optimized endpoint | Riemann convergence, imported Supnick theorem, or global geometry |
| `python -B ops/TASK-20260904__one_gap_terminal_subset_variation/check_finite.py` | 0; 298 exact edge-set comparisons, 9 continuum diagnostics across both parities | independent rank convention and numerical behavior below/at/above median | analytic limit or sign proof |
| `python -B -I -S ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py` | 0; 894 edge comparisons and exact rational optimizer intervals pass | accepted dependency and exact reported constants | new gap variation |
| `python -B ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py` | 0; 16 symbolic identities pass | accepted dependency's parity, integral, optimizer and boundary identities | new reindexing formulas |
| direct nine-file text audit | 0; strict UTF-8, no BOM/CR, LF, one final newline, no trailing whitespace | tracked modifications and untracked additions | mathematical correctness |
| `git diff --check` | 0; no output | tracked whitespace/conflict markers | untracked files, handled by direct audit |

Exact task-local symbolic output:

```text
primitive_and_variations=PASS identities=5
optimized_endpoint_sign=PASS identities=3
supnick_parity_edge_counts=PASS sizes=3..100
sympy=1.14.0 imports_ringmin=NO classification=EXACT_SYMBOLIC_AUDIT
```

Exact finite diagnostic output:

```text
supnick_rank_edge_sets=PASS comparisons=298 sizes=3..300
finite_continuum_diagnostics=PASS comparisons=9 parities=even,odd
max_weight_error=0.00062639286
variation_diagnostics=PASS max_error=3.918724e-10
mpmath=1.3.0 imports_ringmin=NO
classification=FINITE_NUMERICAL_DIAGNOSTIC_ONLY; analytic sign is not inferred
```

Rerun dependency output includes the exact brackets

```text
tau in [0.73908513321516,0.73908513321517]
lambda_* in [5.127676810499484582227744032,
             5.127676810499623339634166029]
C_term in [0.1405690808452560635706323813,
           0.1405690808452585862724095207].
```

These decimals and finite diagnostics are not premises of the sign proof.

## Artifact and provenance checks

Not applicable: no production result, finite certificate, generated artifact,
or paper asset is in scope.

Final source/checker SHA-256 values:

```text
326a1b79e8da35a4b6de005811f5cd59ec5181a1e7dc585a303ab519a4784c79  research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md
d7533dac01723719611a25300ecb3cf1f8c33d4bdc38816c32f699dc73ae4497  ops/TASK-20260904__one_gap_terminal_subset_variation/check_symbolic.py
0b0af1c79e79eded3e9a122eb9f06500d3b05a7be30bff2863278502d2342ce7  ops/TASK-20260904__one_gap_terminal_subset_variation/check_finite.py
```

## Failed checks and negative evidence

- The first symbolic primitive check asked SymPy to simplify square roots
  without encoding the proof-domain inequality `0<y<s`; it returned a
  branch-sensitive nonzero form. The checker was corrected to use the exact
  parametrization `y=s sin(theta)^2`, `0<theta<pi/2`, and then passed. This
  was a checker-domain issue, not contrary mathematical evidence.
- One multi-command final Git inspection omitted the task's per-command
  read-only `safe.directory` option. Git rejected it under the sandbox's
  ownership check and subsequent segments ran outside repository context.
  Every command was rerun with the scoped option; no Git configuration or
  history was changed.
- No positive first variation exists for a fixed interior center. The only
  zero of the continuous sign function on the relevant closed range is the
  non-interior lower endpoint `x=alpha`. This rules out a uniform negative
  margin as centers move toward that endpoint and is why no moving-center
  conclusion is recorded.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three intended tracked
  modifications and six intended untracked additions; only the known
  unreadable-global-ignore warning; exit 0.
- `git diff --name-only`: exactly `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, and `research/NEXT_RESEARCH_STEPS.md`.
- `git ls-files --others --exclude-standard`: exactly the proof note and five
  dossier files. Every addition was read in full.
- `git diff --cached --name-only`: exit 0, empty; the index is unchanged.
- Complete tracked diff inspected after the final edits; proof note reread in
  two complete bounded chunks, and every dossier/checker file read directly.
- Direct nine-file text audit: strict UTF-8, no BOM/CR, LF endings, exactly
  one final newline, and no trailing whitespace; exit 0.
- `git diff --check`: exit 0, no output.
- Protected-path diff over `AGENTS.md`, `README.md`, `paper_assets/`,
  `results/`, `verify.py`, `src/`, `tests/`, `scripts/`, `REPORT.md`, build and
  dependency files, and prior proof notes/dossiers: exit 0, empty.
- No generated file changed. Repository HEAD remains
  `512e8ffb113221666438e11877f317ca7a70646f`.

No pytest, production verifier, certificate regeneration, paper build, or
hosted CI run was required: no corresponding implementation, artifact, or
publication source changed.

## Residual uncertainty

Independent human proof review and manual integration remain pending. The
symbolic checker is corroborative, not a formal proof assistant or a reproof
of the imported Supnick theorem. The theorem is pointwise for fixed interior
`x` and uses the iterated limit `n->infinity` before `epsilon->0+`. No claim
is made for moving centers, diagonal limits, multiple gaps, combined subsets,
matching upper bounds, true global asymptotics, floating circles, contact
graphs, or certification beyond `n=14`.
