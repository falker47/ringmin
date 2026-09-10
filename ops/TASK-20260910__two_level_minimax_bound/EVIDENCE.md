# Evidence

## Environment

    repository_head=67742eddd05b4b61fc24c84820473ed8ee6bdc7a
    platform=Windows / PowerShell
    python=3.14.3
    mpmath=1.3.0
    sympy=1.14.0
    dependency_source=existing local Python; no installation
    task_mode=STRICT

The user supplies the base HEAD as accepted. That is provenance for this
task, not a new external acceptance decision. All checks below are local.

## Claim ledger

Authoritative proof: research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md,
Section 9. Sole thematic owner: knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md,
the existing common-chain-stability entry.

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| The scalar minimum is D^2/3600 | Exact theorem | Section 9.1, explicit factorization on the entire nonnegative domain | Analytic; scalar equality is not a tour construction |
| The actual D and eta_60 lie in stated rational intervals | Exact arithmetic supporting an analytic theorem | Section 9.2, rational Taylor gates, integrated binomial series and positive tail | No production implementation, saved result or floating premise |
| Uniform finite minimax bound and non-strict liminf | Exact theorem / proved corollary | Sections 9.1 and 9.3, uniform floors before minimization | Depends on accepted root, dual and deletion estimates; both parities covered |
| R* inherits the bound | Proved global corollary | Full-feasible deletion, Section 8 and Section 9.3 | No deletion-feasibility claim at a chain root |
| Quadrature and primitive agree with exact enclosure | Numerical observation / symbolic identities | Optional 80/120-dps checks and SymPy | Separate evaluation paths, not external mathematical review |
| Sharpness of the stated scalar relaxation | Exact limitation | Equality at e=D^2/3600, W'=W | Not a ceiling on improved run estimates, other coupling inequalities or R* |

## Commands and checks

Startup commands read the contract, index, status, pertinent ledger,
roadmap and linked sources. Plain Git status/HEAD reads failed with dubious
ownership. Subsequent Git reads used a command-local safe.directory option
set to the resolved repository root; no machine-specific path is retained.
They confirmed clean main at the base SHA and
origin=https://github.com/falker47/ringmin.git. No global config changed.
Ignore-file permission warnings did not affect results.

The Python version/import command exited 0: Python 3.14.3, mpmath 1.3.0,
SymPy 1.14.0. One initial 80-dps scalar diagnostic used
`findroot(cos(t)-t, (.73,.75))` and direct quadrature for D; it was a
numerical observation, subsequently replaced as a premise by exact
enclosures. It also evaluated an unrounded constant, without claiming
that the bound from (9) limits refinements of its underlying proof.

### Exact standalone run

Command from repository root:

```text
python ops/TASK-20260910__two_level_minimax_bound/check_minimax.py
```

Exit 0. Complete output:

```text
exact parameter gates: tau, q_*, pi PASS (40 decimal places)
exact integral enclosure: 80 integrated binomial terms + positive tail PASS
0.00241410289623904895465331017 < D < 0.00241410289623904895465331018
5.1529885884211781970537738e-10 < eta_60 < 5.1529885884211781970537739e-10
exact minimax/domain/error gates: PASS; 515 < eta_60/10^-12 < 516
finite corollary: n>=10^14 gives B_n/n^2 >= C+eta_60-3/n > C+5.152e-10
PASS: bounded analytic support; no tour enumeration or finite optimum certification
```

This run uses the Python standard library only. Fixed work: cosine degrees
80/82, sine degrees 81/83, atan sums through indices 40/41, 80 integrated
binomial terms, and exact rational comparison gates. It does not generate
tours, evaluate q floors, call production code or read certificates.

### Independent evaluation paths

Command from repository root:

```text
python ops/TASK-20260910__two_level_minimax_bound/check_minimax.py --diagnostics
```

Final run exit 0. It repeats all exact output above and adds:

```text
independent symbolic identities: minimax factorization, integral primitive PASS
independent numerical diagnostic (80 dps): D=0.0024141028962390489546533101733178406, eta_60=0.0000000005152988588421178197053773854931809 PASS
independent numerical diagnostic (120 dps): D=0.0024141028962390489546533101733178406, eta_60=0.0000000005152988588421178197053773854931809 PASS
Numerical diagnostics only; exact enclosures above do not depend on mpmath.
PASS: bounded analytic support; no tour enumeration or finite optimum certification
```

SymPy checks the minimax factorization and differentiates the elementary
antiderivative on x>0,s-x>0. At each of the two fixed precisions, mpmath
evaluates D by direct quadrature and by that primitive, and compares the
results with the independent exact enclosure. No stochastic seed or
unbounded search is present. The all-order theorem is analytic.

### Analytic failure-mode audit

- Retained the same e=W-J_n on both branches; did not drop its positive
  contribution to the restricted cost.
- The scalar factorization covers e=0, the crossing, and all larger e.
  Its hypotheses hold for finite D_n, not only for limiting D.
- Finite D_n is positive because 1+a-5*x>1/60 for deleted x, and D_n<2.
  The n=102 boundary uses strict q>3/17; its auxiliary rational equality
  is not mistaken for a strict inequality.
- Root and floor estimates are order-uniform, so finite minimization
  precedes the liminf. Both parities, wrap edges and consecutive deletions
  retain the accepted proof's coverage.
- The integral substitution reverses endpoints correctly. Positive
  binomial coefficients make the truncated primitive an upper integral
  bound; the geometric tail and q error are applied outward before
  squaring a positive D interval and dividing by the opposite pi endpoint.
- The finite loss is at most 3/n. Strict finite bounds are asserted only
  at a smaller eta'; the exact eta_60 liminf is non-strict. Strict liminf
  comparisons at smaller rational endpoints follow from strict enclosure.
- For every full order, the two chain roots share nested restrictions.
  Directed gaps and the existing all-pairs constraints include the wrap.
  Take fixed-order infima, then a finite minimum, to obtain R*>=B_n.
- The scalar equality witness is deliberately not called realizable.
  Sharpness is restricted to (9)'s aggregate scalar information, not to
  its unrounded proof inequalities or the broader two-level method.

## Artifact and provenance checks

Finite result and publication artifacts: not applicable; no regeneration.
Task support source:
`ops/TASK-20260910__two_level_minimax_bound/check_minimax.py`.

    SHA256=c9912c7a2120f83cb20f4f46e8614fce302d0b384c4bc800a5fad0c78db4a44f

All exact input brackets, term counts and diagnostics are in that source.
Its base code commit is recorded above; the task commit containing the
checker is identified by Git and the final handoff. No self-referential
generation SHA is embedded. Numerical printouts are corroboration only.

## Failed checks and negative evidence

- Initial plain Git reads failed with dubious ownership; the command-local
  workaround succeeded without changing global configuration.
- The first checker run exited 1 after successful parameter/integral/gap
  enclosures. It incorrectly asserted 3/17-1/102>1/6. Replaced that gate
  with the exact equality; strict a>1/6 still follows from q>3/17.
- One apply_patch invocation was rejected before mutation because it
  attempted delete/add of CURRENT_STATUS.md in one patch. Reissued it as
  an update; no partial scientific edit resulted.
- No counterexample to the new analytic statement was found. The scalar
  equality does refute any stronger universal conclusion from the same
  aggregate inequalities alone; it says nothing about actual tour equality.

## Final diff inspection

The complete four-file tracked diff was read, and all four new dossier
files, including the checker, were inspected in full. Explicit whitespace
checks included untracked files; ordinary Git diff alone was not used for
them. The local audit exited 0 with this output:

```text
scope and whitespace: exactly 8 paths, including all additions PASS
input proof Sections 2-7 and old finite theorem unchanged; Section 8 only threshold renaming PASS
proof links: 9 PASS; sole thematic ownership and one next task PASS
protected tracked paths: 445 unchanged PASS
checker SHA256: c9912c7a2120f83cb20f4f46e8614fce302d0b384c4bc800a5fad0c78db4a44f
git diff --check: exit 0; local audit PASS
```

The audit obtains the base-relative changed paths with
`git diff --name-only 67742eddd05b4b61fc24c84820473ed8ee6bdc7a`
and additions with `git ls-files --others --exclude-standard`, then
requires their union to equal the eight authorized paths. It checks every
line for trailing whitespace/tabs, checks final newlines, parses the
checker with ast, resolves all nine proof links, and compares input proof
Sections 2-7 and the original finite statement with `git show BASE:path`.
Section 8 differs only by renaming its old threshold B_n to U_n, avoiding
a collision with the user's minimax B_n. Only the global-bounds thematic
ledger contains eta_60. All 445 other tracked paths are unchanged.

Protected coverage includes the compact index, other knowledge modules,
all other proofs, prior dossiers and checkers, AGENTS.md and review protocol,
paper_assets/, results/, src/, tests/, scripts/, verify.py, README.md,
REPORT.md, publication metadata and CI. No generated file changed.

Final record edits receive the same audit before staging. Authorized
integration stages precisely the inspected eight paths, inspects the
complete staged diff, and runs `git diff --cached --check` before commit
and normal origin/main push. The observed commit, push and clean-tree
result belong to the final handoff, not a prediction in this pre-commit
record.

## Residual uncertainty and skipped checks

Independent external mathematical review is pending. The scalar optimum
need not be achievable by common tours. No sharp global coefficient,
normalized limit, finite optimum certificate, upper construction or paper
revision follows. Hosted CI for the task SHA is not claimed inspected.

Production pytest, verify.py (including frontier mode), finite tour checks,
and paper builds were not run: no corresponding implementation, certificate
or publication asset changed, and the user excluded finite certification
and enumeration. The relevant checks are the bounded exact/symbolic and
high-precision diagnostics described above.
