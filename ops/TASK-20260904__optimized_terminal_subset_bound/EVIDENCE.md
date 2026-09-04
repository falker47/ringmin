# Evidence

## Environment

```text
repository_head=22bc88834c38421efba068fd573206dae3bdb07b
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing interpreter; stdlib fractions; SymPy 1.14.0 and mpmath 1.3.0 for independent checks
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `R_{k,n}/k^2->rho(lambda)` whenever `k->infinity,n/k->lambda>1` | exact theorem | proof sections 3-4: parity-explicit edge measure, uniform angular error and root bracket | exact endpoint checker plus independent symbolic identities | imports the published arbitrary-radii Supnick theorem; no proof assistant |
| `liminf R*(n)/n^2>=c(lambda)` for every fixed `lambda>1` | proved corollary | deletion inequality and `k=floor(n/lambda)` in sections 2 and 7 | analytic deduction independent of production | lower bound only; no normalized monotonicity or limit claim |
| Unique maximum at `lambda_*=(1+sin(tau))/(1-sin(tau))`, `tau=cos(tau)` | exact theorem about the derived coefficient | closed form and derivative-sign proof in sections 5-6 | separate SymPy identities and exact rational root bracket | optimizes proportional terminal subsets, not all lower-bound methods |
| `C_term=tau/[pi(1+sin(tau))]≈0.14056908084525677` | exact expression plus numerical observation | critical-point identity; exact rational enclosure and 80-digit diagnostic | stdlib rational Taylor/Machin bounds and mpmath | displayed long decimal is diagnostic, not a proof premise |
| Boundary coefficients `0` and `1/8`; old `lambda=4` coefficient is strictly smaller | exact theorem | continuity limits and positive derivative at `q=3/5` | SymPy boundary gates; earlier exact constant audit | says nothing about true global boundary regimes outside the fixed-ratio theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | 0; no output | clean startup tree | ignored files |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| `python -B -I -S ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py` | 0; 894 edge comparisons; exact rational optimizer intervals | independent edge convention and exact reported-digit brackets | analytic convergence, Supnick optimality or true global asymptotics |
| `python -B ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py` | 0; 16 exact identities; SymPy 1.14.0 | parity endpoints/counts, integral, coefficient, derivative and boundaries | uniqueness sign argument or imported theorem |
| `python -B -O -S ops/TASK-20260830__eventual_supnick_seam_onset/check_asymptotic_onset.py` | 0; 68 gates, 4 parity subsequences | compatibility with the former `lambda=4` asymptotic | generalized moving-ratio limit |
| `python -B -I -S ops/TASK-20260904__induced_subset_asymptotic_bound/check_exact_arithmetic.py` | 0; exact separation and four residues | compatibility with `rho/16>3/22>1/8` | new optimizer |
| 80-digit `mpmath` diagnostic | 0; root residual `<5e-82`, `lambda≈5.1276768104994935`, `c≈0.14056908084525677` | candidate reproduction | analytic optimization or global asymptotics |

## Artifact and provenance checks

Not applicable: no production artifact, result, certificate, or paper asset is
in scope.

Exact task-local checker output:

```text
supnick_parity_edge_sets=PASS comparisons=894 sizes=3..300
tau_root_exact_signs=PASS interval=[0.73908513321516,0.73908513321517]
lambda_interval=[5.127676810499484582227744032,5.127676810499623339634166029]
coefficient_interval=[0.1405690808452560635706323813,0.1405690808452585862724095207]
classification=EXACT_RATIONAL_AND_FINITE_AUDIT; analytic limits and imported Supnick theorem are not mechanized
```

Separate symbolic output:

```text
parity_endpoint_and_count_identities=PASS identities=8
integral_and_coefficient_identities=PASS identities=3
optimization_derivative_and_boundaries=PASS identities=5
sympy=1.14.0 imports_ringmin=NO classification=EXACT_SYMBOLIC_AUDIT
```

High-precision diagnostic output:

```text
python_mpmath=1.3.0 dps=80
tau=0.739085133215160641655312087673873404013411759
lambda=5.12767681049949348567043625046435615116040323
coefficient=0.140569080845256766545516231047508671196278611
residual=-4.6558e-82
classification=NUMERICAL_DIAGNOSTIC_ONLY
```

## Failed checks and negative evidence

- Unscoped `git rev-parse HEAD` failed Git's ownership protection. The scoped
  read-only retry succeeded without a configuration write.
- No counterexample was found. Rejected shortcuts include treating parity
  endpoints as identical before the limit, using a pointwise arcsine expansion,
  inferring the optimizer from sampled values, or assuming `R*(n)/n^2` is
  monotone. The proof explicitly avoids each one.

## Final diff inspection

- `git status --short --untracked-files=all`: four intended tracked
  modifications and five intended untracked additions; exit 0. Git emitted
  only the known unreadable-global-ignore warning.
- `git diff --name-only`: exactly `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, the authoritative proof note, and the roadmap.
- `git ls-files --others --exclude-standard`: exactly the five files in this
  task dossier. Every one was read in full.
- `git diff --cached --name-only`: exit 0, empty; index unchanged.
- Complete tracked diff inspected without truncation; proof note reread in
  three complete bounded chunks after the final mathematical edit.
- Direct nine-file text audit: strict UTF-8, no BOM/CR, LF endings, exactly one
  final newline and no trailing whitespace; exit 0.
- The first PowerShell trailing-whitespace regex was invalid for its purpose:
  inside a single-quoted string, `` `t `` matched the literal characters
  backtick and `t`, causing a false positive. `rg` returned no matching lines;
  the corrected `[ \x09]` audit passed. No file edit resulted from the failed
  check.
- `git diff --check`: exit 0, no output.
- Protected-path diff over `AGENTS.md`, `README.md`, `paper_assets/`,
  `results/`, `verify.py`, `src/`, `tests/`, `scripts/`, `REPORT.md`, build and
  dependency files: exit 0, empty.
- No generated file changed. Repository HEAD remains
  `22bc88834c38421efba068fd573206dae3bdb07b`.

Final SHA-256 values:

```text
78731d83f88c4d6aeceaee52740df03e3d8073cb994add4daa9fce975a3ddd9e  research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md
c7594725ba5cd7315b45f156483144fc1c2e0c27899efb4e4202420dcc88acd6  ops/TASK-20260904__optimized_terminal_subset_bound/check_exact.py
b145a4666ecaab9b4ecd95418fe59302ff2a30e1eba2ce4f8c2936d44a9b906c  ops/TASK-20260904__optimized_terminal_subset_bound/check_symbolic.py
```

## Residual uncertainty

Independent human proof review and manual integration are pending. The exact
checker is corroborative, not a formal proof assistant or a reproof of the
imported Supnick theorem. No claim is made about a matching upper bound,
existence or value of the true normalized limit, nonterminal or combined
deletions, floating-circle behavior, or certification beyond `n=14`. Hosted CI
is irrelevant and was not inspected; the historical arXiv-v1 record is intact.
