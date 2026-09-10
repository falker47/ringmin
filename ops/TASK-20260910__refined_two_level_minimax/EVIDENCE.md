# Evidence

## Environment

```text
repository_head=aa11e5a3fe3648b476566fb953cd50fec846f536
platform=Windows / PowerShell
python=3.14.3
optional_sympy=1.14.0
optional_mpmath=1.3.0
dependency_source=existing environment; default checker uses only standard library
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Exact scalar minimum for all real d | Exact theorem | Section 12.1, coefficient identities | Analytic proof; checker imports no production code; no realizing tour |
| D, cubic root, eta_new, total coefficient and A brackets | Exact rational enclosures | Section 12.2 and exact Fraction/isqrt gates | New midpoint integral implementation; no floating premise or prior checker imports |
| Finite minimax and error propagation for every n>=102 | Exact analytic theorem | Section 12.3, inverse derivative and secant identity | Uses proved Sections 2, 5 and 11; handles nonpositive lower D estimate |
| Global finite and liminf lower bounds | Proved corollary | Section 12.4 full-feasible deletion | Analytic all-pairs argument; no chain-feasibility shortcut or optimum certificate |
| 80/120-dps coefficient agreement | Numerical observation | Optional new diagnostics | Independent quadrature/bisection; not a proof premise |
| Section 11 prescribed-tour checks reproduced | Independently reproduced finite diagnostics | Existing checker run in this task | Production-independent; does not replace the all-tour proof or external review |
| Original Sections 2-11 and 458 other tracked paths unchanged | Engineering fact | Source comparison and Git audit | Local preservation check, not hosted CI |

The single stable claim owner is the common-chain entry in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`. The index and other thematic
ledgers are unchanged. The roadmap only updates the endpoint and next review
scope; it does not supply a competing proof or record an external acceptance.

## Commands and checks

All commands below were run locally in this task. `git` reads use the
per-command option `-c safe.directory=<repository-root>` because of the
sandbox account's ownership mismatch. The placeholder denotes this checkout,
not a saved configuration change. Exact Python paths are repository-relative.

| Command/check | Exit/result | Property checked | Excluded scope |
|---|---|---|---|
| `python -I ops/TASK-20260910__refined_two_level_minimax/check_refined_minimax.py` | 0; all exact gates PASS | Default standard-library checks work in isolated mode | No geometric realization or all-tour search |
| `python -I ops/TASK-20260910__refined_two_level_minimax/check_refined_minimax.py --diagnostics` | 0; exact, SymPy, 80/120-dps PASS | Final checker algebra and independent numerical corroboration | Floating diagnostics do not establish exactness |
| `python ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py` | 0; output below | Relevant Section 11 dependency diagnostics | No external acceptance or all-n computational proof |
| `python ops/TASK-20260910__two_level_minimax_bound/check_minimax.py` | 0; old D and eta_60 gates PASS | Independent old transformed-integral enclosure agrees | Does not establish the new coefficient |
| `git diff --check` | 0; no output | Tracked patch whitespace | Untracked files checked separately |
| `git diff --exit-code aa11e5a3fe3648b476566fb953cd50fec846f536 -- . ':(exclude)CURRENT_STATUS.md' ':(exclude)research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md' ':(exclude)knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md' ':(exclude)research/NEXT_RESEARCH_STEPS.md'` | 0; no diff | All other tracked paths preserved | Does not inspect untracked content |
| Inline Python source/whitespace/link/import audit | 0; output below | All eight additions/edits, original proof body, links, import independence and allowed paths | Documentation/engineering check only |

The checker was also run without `-I` with diagnostics before the final
wording-only clarification of its degree-40 output label; exit 0. The final
isolated diagnostics run above checks the final code. Startup reads and an
exploratory 70-dps mpmath calculation succeeded; the latter was used only to
choose candidate rational endpoints, which the exact gates subsequently prove.

Final new checker output:

```text
exact parameter/domain gates: PASS (tau, q, pi; n>=102)
exact coefficient identities: PASS (crossing, cubes, secant error)
independent exact D enclosure: PASS (degree 40, tail, isqrt)
exact monotone cubic gates: PASS
1.3284070181357731944366841527895847e-7 < eta_new < 1.3284070181357731944366841527895848e-7
0.14056921368595858012283567471592395015 < C+eta_new < 0.14056921368595858012283567471592395016
exact finite-error gates: PASS; A<2.592306; 257<eta_new/eta_60<258
finite corollary: n>=10^13 gives R*(n)>=B_n>(C+1.3284e-7)*n^2
independent SymPy crossing/inverse-derivative identities: PASS
numerical diagnostic (80 dps): eta_new=0.0000001328407018135773194436684152789584769975 PASS
numerical diagnostic (120 dps): eta_new=0.0000001328407018135773194436684152789584769975 PASS
Diagnostics are observations, not premises of the rational enclosures.
PASS: bounded independent scalar support; no geometric optimality certificate
```

Section 11 dependency output:

```text
exact q bracket, domain and remainder constants: PASS
exact finite floors: 12; prescribed tours: 60; all four parities PASS
exact marginals/energy/maximal runs: 180 orientations, wrap and run lengths 1/2/>2 PASS
exact midpoint-strip checks: 360 PASS
independent symbolic first-variation/Hessian/primitive identities: 8 PASS
numerical direct-cost/Taylor/cancellation/threshold/final bounds (70 dps): 60 PASS
numerical direct-cost/Taylor/cancellation/threshold/final bounds (100 dps): 60 PASS
Numerical diagnostics only; the uniform little-o theorem is analytic.
PASS: bounded deterministic support; no general tours enumerated or finite optima certified
```

Old minimax checker material output:

```text
exact parameter gates: tau, q_*, pi PASS (40 decimal places)
exact integral enclosure: 80 integrated binomial terms + positive tail PASS
0.00241410289623904895465331017 < D < 0.00241410289623904895465331018
5.1529885884211781970537738e-10 < eta_60 < 5.1529885884211781970537739e-10
exact minimax/domain/error gates: PASS; 515 < eta_60/10^-12 < 516
finite corollary: n>=10^14 gives B_n/n^2 >= C+eta_60-3/n > C+5.152e-10
PASS: bounded analytic support; no tour enumeration or finite optimum certification
```

Inline Python audit, executed as a PowerShell single-quoted here-string piped
to `python -`, checked all four edited paths and the four task files using
`Path.read_text`, terminal newline and `line == line.rstrip()`. It compared
the baseline `git show` substring beginning at `## 2.` to the current
substring ending before `## 12.`, after removing terminal whitespace.
Markdown link destinations and heading anchors were resolved locally;
`ast.parse` confirmed the complete import set was exactly
`argparse,fractions,math,mpmath,sympy`. `git diff --name-only <base>` was
compared with the four authorized existing files and `git ls-files` counted
the remaining preserved paths. Exact output:

```text
PASS: whitespace over 8 files; original proof Sections 2-11 unchanged
PASS: 29 local Markdown links/anchors
PASS: checker imports restricted to standard library and optional mpmath/SymPy
PASS: 458 other tracked paths unchanged from base
```

Analytic transfer audit: each surviving new edge uses its existing full
pairwise distance constraint. Its directed gap dominates the required angle
even above pi; the gaps sum to 2*pi including wrap. Nested restrictions share
the same outer sigma. Roots are fixed before taking fixed-order infima, then
the global finite minimum. All normalization uses the original n and radii.
Neither root is claimed fully feasible. The coefficient conclusion is a
non-strict liminf; finite strictness uses a strictly smaller rational gain.

Not run: production pytest, standalone optimum/frontier verification,
paper compilation or hosted CI. No production, certificate, publication or
CI file changes require those layers; none is claimed green or re-certified.

## Artifact and provenance checks

No result or publication artifact is generated. Checker inputs are explicit
rational constants tied to proof Sections 9 and 12. No production or result
imports; deterministic bounded work, no seeds or machine-specific paths.

Final checker SHA256, obtained with `Get-FileHash -Algorithm SHA256`:

```text
3875CEBFBDBDE47FF302EB60EF0A411C29655AF34EF58929C3BD3EC936B3D2A9
```

The source commit is the task commit whose SHA is reported after authorized
integration; the input/dependency baseline is recorded above. There is no
generated certificate schema, result hash or nondeterministic experiment.

## Failed checks and negative evidence

Initial Git ownership errors and the rejected duplicate-target documentation
patch are recorded in TASK_LOG. Per-command ownership handling and a corrected
patch resolved them. Git also emitted harmless global-ignore permission
warnings during sandbox reads. No mathematical check failed.

The old sqrt inequality is strictly nonbinding at the new crossing for
0<d<2, proved by a rational inequality. It cannot improve this scalar
minimum when added back. This negative result is confined to the stated
information, not the broader common-tour method.

## Final diff inspection

- Exactly four existing files modified and four task files added; all read
  in full or through the complete diff. A truncated aggregate tool display
  was completed with a separate roadmap diff and proof-tail read.
- All untracked additions were inspected directly; explicit whitespace audit
  covers them. `git diff --check` also passed for tracked files.
- The owning ledger alone contains the reusable claim; roadmap and current
  status point to the proof. No duplicate thematic owner or index expansion.
- Protected paths inspected by baseline diff: `paper_assets/`, `results/`,
  `src/`, `verify.py`, `tests/`, `.github/`, publication/release metadata,
  all other research notes, prior dossiers and the knowledge index. All 458
  tracked paths outside the four authorized edits remain unchanged.
- Original proof Sections 2-11 preserved. No generated files changed.
- This precommit dossier records the completed scientific/diff gates.
  Staged diff/whitespace inspection, authorized commit, normal push to the
  existing `origin/main`, and remote/clean-tree confirmation follow this
  snapshot; their exact outcomes and committed SHA are reported in the final
  handoff. Integration does not constitute external mathematical acceptance.

## Residual uncertainty

No optimal exponent 2/3, sharp geometric coefficient, actual minimizing tour,
normalized limit, expanded certification or hosted CI status is claimed.
Independent external mathematical review remains separate.
