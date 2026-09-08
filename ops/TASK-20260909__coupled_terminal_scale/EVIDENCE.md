# Evidence

## Environment

    repository_head=f03f6267ea98cf5c3a709595721ec322114c405b
    platform=Windows PowerShell sandbox
    python=3.14.3
    dependency_source=existing interpreter; exact checker uses standard library
    diagnostic_mpmath=1.3.0
    symbolic_SymPy=1.14.0
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| 0<=G_{k,n}<=n/2 for all k>=1,n>=k+3 | exact theorem | proof Sections 2-4, explicit deletion and integrated derivative | analytic; no production code or finite enumeration premise |
| G_{k,n}=0 and A_M<A_N for n>=48k(k+1)^2 | exact theorem | proof Section 5, explicit insertion, degree count and endpoint derivative | analytic; cutoff is sufficient, not sharp |
| k=1 cutoff 192 and k=2 cutoff 864 | proved corollaries | exact substitution, proof Section 6 | does not identify smallest equality thresholds |
| Fixed-k normalized B tends to 1/8; moving one-level gain is also negligible | proved asymptotic corollaries | uniform gain bound and imported terminal-array theorem | no global Ringmin limit or improved coefficient |
| Bounded comparison-tour evaluations | numerical observations | optional checker mode | diagnostic only; no minimax values or certification |

The new theorem does not rely on the prior strict-uniqueness or finite-gap
proof. Those finite results provide context; their exact arithmetic is
rerun separately. The arbitrary-radii Supnick theorem and terminal-array
limit are explicit mathematical imports.

## Commands and checks

- Initial Git reads: ownership guard failure, no mutation.
- Command-local safe.directory Git status: exit 0, clean tree (known
  global-ignore permission warnings). HEAD/branch/remote reads: exit 0.
- `python --version`: exit 0, `Python 3.14.3`.
- Existing dependency query: exit 0, `sympy=1.14.0; mpmath=1.3.0`.
- Symbolic audit piped through `python -B -`: exit 0, exact output
  `PASS: radial derivative, endpoint derivative, and arcsine elasticity identity; SymPy=1.14.0`.
  The exact source is recorded below.
- `python -B -I -S ops/TASK-20260909__coupled_terminal_scale/check_scale.py`:
  exit 0. Exact stdout:

  ```text
  PASS exact: 512 prescribed rank/deletion/insertion cases; both parities, N=3, rotations/reversals, omitted-chord negative controls.
  PASS exact: degree counts where applicable; 64 rational cutoff substitutions, including 192 and 864. No tour enumeration.
  ```

  This checks two independently transcribed rank descriptions, actual
  cyclic deletion/insertion and constants, without site packages or
  production imports. The bounded integer cases do not prove the all-n
  statements; Sections 2-5 of the analytic note do that.
- `python -B -I -S ops/TASK-20260908__coupled_terminal_subsets/check_exact.py`:
  exit 0. Eight rational closure gates pass by both arcsine and arctangent
  enclosures; final stdout:

  ```text
  PASS: 8 rational closure gates by two formulas; pi, gap constants,
  cyclic deletion and five/four rank obstruction. No tour enumeration.
  ```

  In the source's row order, the reported closure integer bounds (units
  1e-5) are (628726,628728), (628049,628051), (626827,626829),
  (630128,630131), (628508,628512), (628255,628258), (626690,626694),
  (630763,630766). This is a fresh arithmetic rerun, not independent
  acceptance of the earlier all-tour or minimality proofs. Its file is
  unchanged and the new gain theorem does not need these gates.
- `python -B ops/TASK-20260909__coupled_terminal_scale/check_scale.py --diagnostic`:
  exit 0. Exact mode also passes. mpmath 1.3.0, 50 decimal digits, 140
  bisections per prescribed root, guard 1e-30, no random seed. Arctangent
  roots are checked against direct arcsine closure sums on both modified
  tours. The upper radius bracket n^2 is justified analytically by (8).
  Printed diagnostic values (ten significant digits) are:

  | k | n | A_M/n^2 | A_N/n^2 | D(A_M) | J(A_N) |
  |---:|---:|---:|---:|---:|---:|
  | 1 | 4 | 0.05277834935 | 0.02707880516 | -1.018655286 | 1.475980113 |
  | 1 | 7 | 0.08475897048 | 0.08137523534 | -0.09430095836 | 0.2955829583 |
  | 1 | 8 | 0.08993798572 | 0.08948434053 | 0.02711525888 | 0.1946306539 |
  | 1 | 192 | 0.1236543925 | 0.1247129303 | 0.06876036205 | -0.001830104051 |
  | 1 | 193 | 0.1236614731 | 0.1247151468 | 0.06844730617 | -0.001817712213 |
  | 2 | 5 | 0.05284933039 | 0.02384130477 | -1.238287307 | 1.73348088 |
  | 2 | 12 | 0.105964378 | 0.1045427986 | -0.01222808359 | 0.1904307087 |
  | 2 | 13 | 0.108151145 | 0.1077203271 | 0.03004670546 | 0.1557721284 |
  | 2 | 864 | 0.124969857 | 0.1252238852 | 0.016569089 | -0.0001465524428 |
  | 2 | 865 | 0.1249699091 | 0.1252236642 | 0.01655114731 | -0.0001463299507 |

  Final stdout: `PASS diagnostic: ten prescribed comparisons and alternate-angle closures; no minimax computation, optimality claim or certification.`
  These are numerical observations only. In particular positive D at a
  large n is consistent with negative J and exact minimax equality: they
  describe different comparison tours. No tour/gap enumeration was run.

The symbolic command was the following PowerShell single-quoted here-string
body piped to `python -B -`:

```python
import sympy as s
R,a,b=s.symbols('R a b', positive=True)
u=s.sqrt(a*b/((R+a)*(R+b)))
theta=2*s.asin(u)
radial=-u/s.sqrt(1-u*u)*(1/(R+a)+1/(R+b))
endpoint=s.sqrt(R*b)/((R+a)*s.sqrt(a)*s.sqrt(R+a+b))
assert s.simplify(s.diff(theta,R)-radial)==0
assert s.simplify(s.diff(theta,a)-endpoint)==0
x=s.symbols('x', positive=True)
assert s.simplify(s.diff(x/s.sqrt(1-x*x)-s.asin(x),x)-x*x/(1-x*x)**s.Rational(3,2))==0
print('PASS: radial derivative, endpoint derivative, and arcsine elasticity identity; SymPy='+s.__version__)
```

The last identity is applied analytically only on 0<x<1. The source proof
supplies its domain, zero endpoint and inequality direction. This audit
checks derivative identities, not the universal tour reduction or theorem.

All checks are local. No production tests, certificate/frontier verifier,
paper build or hosted CI is claimed; corresponding sources/artifacts are
unchanged. Symbolic and diagnostic checks are independent of production,
but do not replace review of the analytic proof and imported theorems.

## Artifact and provenance checks

No production artifact generated or regenerated. New proof and bounded
checker are tracked together; diagnostics write stdout only, with no
nondeterminism. SHA-256 of the final mathematical source and checker:

```text
8b0d8156107e0ffcf348892f84dfa5f0f172a0c726aa6d95f290285318492b53  research/COUPLED_TERMINAL_ONE_LEVEL_ASYMPTOTICS.md
a3e23d4b1b6267a90d5dafb4ebc0cb3cefa38ddcf66df42999980e0916bc1519  ops/TASK-20260909__coupled_terminal_scale/check_scale.py
```

## Failed checks and negative evidence

The initial ownership refusal and truncated reads are recorded in TASK_LOG.
A combined documentation patch was rejected because it attempted both
delete and add operations on CURRENT_STATUS.md. A read-only diff confirmed
no tracked edits occurred; the ledger/roadmap patch was reapplied and the
status was written separately. No proof or checker failure occurred.
The finite strict gain does not imply persistence: the explicit smaller-tour
insertion proves its eventual disappearance. No stronger asymptotic lower
bound is inferred from chain incompatibility or from a feasible comparison.

## Final diff inspection

- Full proof and checker read directly; all three dossier additions read
  in full. Complete tracked diff inspected for CURRENT_STATUS, the sole
  owning global-bounds ledger and roadmap.
- A standalone audit piped to `python -B -I -S -` exits 0, with stdout:

  ```text
  PASS: exact eight-path delta, empty initial index, UTF-8/LF/whitespace including all untracked additions, local proof links, sole ledger owner, isolated checker imports, nine protected source texts unchanged.
  ```

  The audit compares the union of `git diff --name-only BASE` and
  `git ls-files --others --exclude-standard` with the exact eight allowed
  paths. It checks every file for UTF-8 without BOM, LF endings, one final
  newline, no trailing whitespace or conflict markers; resolves every
  local Markdown proof link; verifies the sole knowledge owner; and checks
  the checker AST's imports are exactly argparse, collections, fractions
  and the optional mpmath. These are engineering checks, not proof gates.
- The same audit compares normalized working texts with `git show BASE:path`
  for nine imported/protected sources: paper_assets/ringmin_paper.tex,
  research/COUPLED_TERMINAL_SUBSETS.md, research/FIXED_K_SUPNICK_SEAM.md,
  research/FINITE_INDUCED_SUBSET_DOMINANCE.md,
  ops/TASK-20260908__coupled_terminal_subsets/check_exact.py,
  src/ringmin/patterns.py, verify.py, PROJECT_KNOWLEDGE.md and AGENTS.md.
  All nine are unchanged. The exact path-delta check protects every other
  tracked file, including results, paper/generated assets, third-block
  work, previous dossiers, other ledgers, tests, scripts, README, REPORT,
  review protocol, publication/build metadata and CI.
- `git diff --check`: exit 0, no output. `git status --short
  --untracked-files=all`: exit 0, exactly three modifications and five
  additions; known global-ignore permission warnings only. Read-only Git
  uses the command-local safe.directory for the resolved repository root.
- CURRENT_STATUS.md's final line ending from the PowerShell write was
  normalized to LF before the explicit audit; no content change.
- Final record-only updates are inspected/restaged before authorized
  integration, with a complete staged diff and whitespace check. The
  actual commit SHA, push result and remaining tree state belong to the
  final handoff, avoiding a self-referential commit hash in these files.
- Explicit eight-path staging succeeded with tool escalation (exit 0).
  Complete staged diff inspected, with a focused second read of the
  dossier/checker portion truncated in the aggregate output.
  `git diff --cached --check` and `git diff --exit-code` both exit 0.
  These final evidence/log additions are inspected/restaged before commit;
  the mathematical source and checker hashes above remain unchanged.

## Residual uncertainty

Independent mathematical acceptance remains separate; no formal proof
assistant is used. The sufficient thresholds and n/2 bound are not sharp.
No complete finite equality classification, all-pairs feasibility, global
optimum, global normalized limit, multilevel coupling result or certificate
expansion follows. Hosted CI at the eventual SHA has not been inspected.
