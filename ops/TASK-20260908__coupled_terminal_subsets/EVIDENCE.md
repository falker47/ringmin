# Evidence

## Environment

    repository_head=3c415b36ade354cfd9beff637ec98bb5cc6b7d0a
    platform=Windows PowerShell sandbox
    python=3.14.3
    dependency_source=existing interpreter; checker uses standard library only
    dependency_audit_versions=mpmath 1.3.0; SymPy 1.14.0
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Limit |
|---|---|---|---|
| The universal minimax equality fails with gap >1/6000 at n=M=8,N=7 | exact counterexample | proof Sections 2-4: symmetric perturbation, rational gates, uniform derivative bound | exact minimax value not computed |
| Ambient size 8 is minimal when M=n is allowed | exact theorem | Section 5: accepted triangle/seam theorems and cyclic path partition | imports those analytic theorems, not finite global certificates |
| If M<n, the minimal ambient counterexample is n=13,M=12,N=11 with gap >1/5000 | exact counterexample / exact minimality theorem | Section 7: same universal perturbation with explicit new constants and radius-2 positive range | no classification of all triples |
| Supnick chain minimizers are unique up to dihedral symmetry for distinct radii; compatibility already fails at M=5,N=4 | exact theorem / exact rank obstruction | Sections 2 and 6 | compatibility is stronger than the minimax equality |
| Coupled bounds can beat the independent maximum at finite n | proved lower-bound corollary | actual deletion plus either strict counterexample | no asymptotic gain or improved C_term |

The proof is analytic, with explicit rational arithmetic. No tour
enumeration supplies any proof step. Floating discovery values are
numerical observations only. The universal matrix-level Supnick theorem
is an explicit classical premise; the perturbed matrix need not be an
angular kernel. The external survey was inspected at Sections 2.2.3 and
2.3, publisher pp.507-508; its link is in the proof.

## Commands and checks

- Initial Get-Content/read-only Git batch: Git status/log refused dubious
  ownership; the PowerShell batch's final exit 0 was not a Git success.
- Command-local safe.directory Git status: exit 0, no changed paths;
  known global-ignore permission warnings. HEAD and branch read: exit 0,
  exact base above, main aligned with origin/main.
- `python --version`: exit 0, Python 3.14.3.
- Standalone discovery here-string piped to `python -B -I -S -`: exit 0;
  fixed n=4..9 range and seven n=8 insertions as logged. Independent of
  production, floating-point and noncertifying; no artifacts generated.
- One additional fixed-candidate discovery at n=13,M=12,N=11 by the same
  independent formula: exit 0; three diagnostic roots recorded in TASK_LOG.
- `python -B -I -S ops/TASK-20260908__coupled_terminal_subsets/check_exact.py`:
  exit 0. Final output:

  ```text
  PASS: 8 rational closure gates by two formulas; pi, gap constants,
  cyclic deletion and five/four rank obstruction. No tour enumeration.
  ```

  The eight outward closure intervals, in units 1/10^5, are
  `(628726,628728)`, `(628049,628051)`, `(626827,626829)`,
  `(630128,630131)`, `(628508,628512)`, `(628255,628258)`,
  `(626690,626694)`, `(630763,630766)`. Each is reproduced by both
  arcsine and arctangent enclosures. This checks arithmetic/rank
  transcription and is independent of production; it does not itself
  prove the matrix theorem, all-tour reduction, analytic derivatives or
  minimal ambient size. The script must run without Python's -O option.
- The following exact-bridge source was piped to `python -B -` in
  PowerShell; exit 0, both paths printed `PASS exact bridges only; no
  numerical scan`, followed by `mpmath=1.3.0`:

  ```python
  import runpy
  import mpmath
  for path in ('ops/TASK-20260804__radius1_seam_obstruction/check_seam.py', 'ops/TASK-20260804__radius2_seam_threshold/check_seam.py'):
   runpy.run_path(path)['check_exact_bridges']()
   print(path + ': PASS exact bridges only; no numerical scan')
  print('mpmath=' + mpmath.__version__)
  ```

  These are newly rerun historical exact endpoint checks, not a full
  execution of either prior diagnostic script and not independent review
  of their all-n proofs. Neither imports production.
- The following source was piped to `python -B -`; exit 0:

  ```python
  import sympy as s
  R,a,b=s.symbols('R a b', positive=True)
  u=s.sqrt(a*b/((R+a)*(R+b)))
  theta=2*s.asin(u)
  mixed=s.sqrt(R)/(2*s.sqrt(a*b)*(R+a+b)**s.Rational(3,2))
  radial=-u/s.sqrt(1-u*u)*(1/(R+a)+1/(R+b))
  assert s.simplify(s.diff(theta,a,b)-mixed)==0
  assert s.simplify(s.diff(theta,R)-radial)==0
  print('PASS: angular mixed and radial derivative identities; SymPy='+s.__version__)
  ```

  Output: `PASS: angular mixed and radial derivative identities;
  SymPy=1.14.0`. Independent symbolic identity check; does not prove
  the uniform inequalities or combinatorial perturbation step.
- Direct source/protection audit piped to `python -B -I -S -`: exit 0.
  It compares the union of baseline `git diff --name-only` and
  `git ls-files --others --exclude-standard` to the exact eight allowed
  paths; explicitly checks UTF-8, no BOM/CR, one final LF, no trailing
  whitespace or conflict markers in all eight files; resolves all local
  proof links; verifies the sole knowledge owner; parses all eight proof
  table rows and compares their integers and inequalities with the exact
  expressions; and compares eight imported source texts with `git show`
  at the base SHA. All checks passed. The initial index was empty.
- `git diff --check`: exit 0, no output. `git status --short
  --untracked-files=all`: exit 0, exactly three intended modifications
  and five additions; known unreadable-global-ignore warnings only.

All results above are local. Git reads use command-local safe.directory
for the resolved repository root; no global configuration is changed.
No pytest, production verifier, frontier audit, paper build or hosted CI
was run: corresponding code/artifacts were not changed. No claim about
hosted CI for the committed SHA is made.

## Artifact and provenance checks

Not applicable to production artifacts: no results, certificates or paper
assets are changed. The proof and bounded checker are tracked together.
SHA-256 of final mathematical source and checker:

```text
5f4e5a05cef636b900aee99a54a9e5f8bc4512ac36353ed749ee1466c23487fc  research/COUPLED_TERMINAL_SUBSETS.md
4fe10bada6cd5b3251b80c3d7866683174070a8c2565dda1483f47fe29c22e7a  ops/TASK-20260908__coupled_terminal_subsets/check_exact.py
```

No nondeterministic computation or production artifact generation.

## Failed checks and negative evidence

The first checker draft failed an incorrect hand-entered aggregate
interval; the explicit rational evaluation corrected it before acceptance.
The final checker passes every table row through both angular formulas.
Git ownership guard and rejected duplicate-target documentation patch are
logged. A read-only dependency lookup initially guessed check_seam2.py
and a Windows wildcard path, exited 1; discovered actual filenames were
read successfully. No source was modified by these failed reads.

Compatibility of minimizers is stronger than the displayed minimax
identity. The five/four-rank example is retained to prevent treating these
as equivalent claims.

## Final diff inspection

- Complete new proof and checker read in full; all dossier additions
  inspected directly, including this final record.
- Complete tracked diff inspected: CURRENT_STATUS, the single owning
  global-bounds ledger, and roadmap only.
- Eight-path audit explicitly includes every untracked addition;
  whitespace and conflict-marker checks pass.
- Every other tracked path is unchanged. Direct baseline text checks
  also pass for the paper, radius-1 and radius-2 seam notes, fixed-k note,
  Supnick path note, finite subset note, patterns.py and verify.py.
- No protected or generated file changed: paper_assets/, results/, src/,
  tests/, scripts/, verify.py, README.md, REPORT.md, prior proofs/dossiers,
  third-block assets, other knowledge modules, index, contract, review
  protocol, publication/build metadata and CI are preserved.
- Final record-only updates will be inspected and staged with the exact
  eight paths; staged diff and whitespace checks precede the authorized
  commit and normal origin/main push. Actual SHA, push and tree state
  are reported in the final handoff, avoiding a self-referential hash.
- Explicit eight-path staging succeeded with tool escalation (exit 0)
  after the sandbox refused index.lock creation. Complete staged diff
  inspected; `git diff --cached --check` and `git diff --exit-code` each
  exit 0. Final log/evidence additions are inspected/restaged before the
  authorized commit; the mathematical source hashes above are unchanged.

## Residual uncertainty

Independent proof review and hosted CI are separate from local checks.
The analytic result imports the classical matrix theorem and the cited
exact path/seam facts. No formal proof-assistant certification, exact
minimax/global optimum, all-triple classification, asymptotic gain or
certification beyond n=14 is claimed. The task stops at this question.
