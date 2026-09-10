# Evidence

## Environment

```text
repository_head=273662513c2816d10ce12a5ba821fe04bbfea5aa
platform=Windows / PowerShell
python=3.14.3
mpmath=1.3.0
sympy=1.14.0
dependency_source=existing local Python; no installation
task_mode=STRICT
```

The user supplies the base as accepted. All new checks are local;
independent external mathematical review and hosted CI remain separate.

## Claim ledger

Authoritative source: research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md,
Section 11. Sole owner: the existing common-chain entry in
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md.

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Uniform bound (30) on absolute Delta | Exact theorem | Section 11, finite marginal cancellation and run accounting | Analytic; imports accepted dual bound; no geometric feasibility claim |
| Uniform o(sqrt(e)); no square-root-sharp tour family | Proved corollary | Divide the uniform bound by sqrt(e) | Does not prove optimality of 2/3 |
| Refine the two-level deletion argument | Method implication | The accepted absolute-value step discards a provable cancellation | No new minimax/global coefficient or comparison with upper bounds |

## Commands and checks

Startup inspection and environment import completed. Git ownership failure
was resolved with command-local safe.directory, without changing config.

Command from the repository root:

```text
python ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py
```

Exit 0. Complete output:

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

Fixed sizes are n=102,...,109,512,513,2048,2049. Rational cosine degrees
80/82 and sine degrees 81/83 recheck the accepted 40-place q bracket;
the two rational endpoints have identical floors after multiplication by
each prescribed n. Beta floors use exact Fraction arithmetic. There is
no numerical decision about a transcendental floor.

The five actual tours at each size are the canonical Supnick cycle,
increasing order, increasing even/odd-position concatenation, a value
exchange between the two adjacent blocks straddling ell, and a reversal
of the first third of the Supnick traversal. The block half-width is
min(ell-k,isqrt(n)//2). All are proved finite permutations directly by
set/length checks; no search or ranking of general tours is present.
Exact checks also rotate and reverse each tour. Independent run extraction
uses cyclic survivor-index intervals, and its Counter edge replacement
must equal the direct restriction, with wrap and lengths 1,2,>2 represented.

Six exact strip widths per prescribed tour include values below, at and
above half a mesh step and a width truncating both domain endpoints.
The exact first/second marginals and squared-energy identity are checked
as integer counts; an arbitrary polynomial test gives a separate exact
cancellation check. SymPy differentiates g, p and an elementary primitive;
it is not a proof of their uniform derivative bounds.

At each fixed precision, direct radical costs supply e and Delta. The
checker separately evaluates the primitive, signed first variation,
Taylor remainder, nonisolated-run remainder, crossing mass and final
bounds. Comparisons use tolerance 10^(-dps+15), namely 10^-55 and 10^-85.
They are numerical observations, not interval certificates or premises
of (30). No production implementation, saved artifact or random seed is
used. Independence here means separate evaluation paths and separation
from production, not an external mathematical review.

### Analytic failure-mode audit

- W, J_n, D_n, q, beta and ambient normalization remain exactly those of
  the accepted proof. E is the squared-defect statistic, not excess e.
- Each original edge has two orientations of mass 1/(2*n). Both reflected
  marginals are nu, whose atoms have mass 1/n. Consequently the signed
  linear deletion term is twice the mu integral, while its second moment
  is exactly E. Reflection fixed points in odd size do not add tour loops.
- Taylor's theorem uses the complete two-variable Hessian of g, including
  cross terms; the operator-norm bound controls both signs of each defect.
  Isolated deleted vertices cannot share an incident original edge.
- Nonisolated run discrepancies and their removed linear terms are both
  accounted for. LL edges have uniformly positive squared defect, so these
  terms are O(E), including a long run crossing the written start.
- F is continuous with derivative P away from B. The Bregman remainder
  holds in either segment direction; a jump is charged only on crossings.
  The equal finite marginals cancel its primitive difference exactly.
- B is the midpoint between consecutive grid values. The strip is empty
  below half a mesh step, and its mass is at most 4*h otherwise. This
  removes every mesh-error term without assuming h>=1/n or a lower bound
  on e. Boundary truncation only helps.
- Short crossings lie in the first-marginal strip; long ones are charged
  to E/h. The choice h=E^(1/3) is legal for every E>0. E=0 is treated
  separately and is impossible for a genuine cycle with distinct neighbors.
- Every step is uniform for n>=102 and both outer/inner parities. Dividing
  (30) proves the uniform little-o statement; no limit/minimum interchange,
  root approximation or finite floor error is involved.
- The improved inequality supplies additional constraints on actual tours;
  it does not contradict Section 9's scalar sharpness for its old premises.
  No conclusion about optimality of 2/3 or a new global coefficient is drawn.

## Artifact and provenance checks

Publication and finite-result artifacts: not applicable; no regeneration.
The only support source is this dossier's bounded checker; its complete
fixed inputs, ranges and precisions are in that file and described above.
The base code commit is recorded in Environment. The final source rerun
also exited 0 with the complete output above. `Get-FileHash` with SHA256
returned:

```text
4b666c712c2b36cb3fb16c0f24453d6843a3f266d516468819f61ba64342042f
```

There is no generated result schema or certificate provenance chain to update.

## Failed checks and negative evidence

All mathematical checks passed. The square-root sharpness candidate is
excluded analytically by the improved uniform bound, not by failed searches.
The startup Git ownership failure and one rejected documentation patch
context are recorded in TASK_LOG.md. Neither changed mathematical content.

## Final diff inspection

The complete four-file tracked diff and all four new dossier files were
read in full. An inline standard-library Python audit (`python -` from
PowerShell) ran Git with a command-local safe.directory for the resolved
repository root. It compared base-relative changed paths and untracked
additions with exactly the eight authorized paths; read every line for
trailing whitespace/tabs and final newlines; parsed the checker AST and
imports; resolved every proof link; checked sole thematic ownership and
the one-next-task status heading; and compared the entire old proof from
`git show BASE:research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md` with the
new prefix. BASE is the exact Environment SHA. Exit 0, output:

```text
scope/whitespace: exactly 8 paths, including all additions PASS
entire accepted proof preserved as prefix PASS
proof links: 11 PASS; sole thematic ownership and one next task PASS
protected tracked paths: 449 unchanged PASS
checker AST/import separation PASS
git diff --check: exit 0; local audit PASS
```

The audit's path inputs come from `git diff --name-only BASE`,
`git ls-files --others --exclude-standard` and `git ls-files`.
Protection covers all earlier proof notes and dossiers, the compact index,
other thematic owners, contract/review protocol, paper_assets/, results/,
src/, tests/, scripts/, verify.py, README.md, REPORT.md, metadata and CI.
The accepted proof has only an appended Section 11. No generated file
changed. Git's ordinary diff was not used as the only check of additions.

Final record edits receive the same audit; then precisely these eight
paths are staged. The complete staged diff and `git diff --cached --check`
must pass before commit and normal origin/main push. The final response
records observed integration results rather than predicting them here.

## Residual uncertainty

Independent external review remains pending. Exponent 2/3 is not claimed
optimal. No new scalar coefficient, full-feasible tour, geometric optimum,
normalized limit, finite certificate, upper construction or paper change.
Production pytest, verify.py (including frontier mode) and paper builds
were not run: no corresponding code or artifact changed. General-tour
enumeration, coefficient optimization and full-feasibility experiments
were not run. Hosted CI for the final SHA is not claimed inspected.
