# Evidence

## Environment

```text
repository_head=4f32b37241578064667b5db7214c3d16d83e4859
platform=Windows, PowerShell
python=3.14.3 (MSC v.1944 64 bit AMD64)
mpmath=1.3.0
dependency_source=existing canonical Python environment; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Closed-domain recovery and coefficient formula | exact theorem | proof Section 2; 120 bounded exact floor/seam cases | direct derivation and a second list construction | finite cases alone do not prove all-m convergence |
| F''>1/9, endpoint signs, unique family minimum | exact theorem | proof Section 3; rational implications checked | elementary analytic bounds | accepted K'' formula and x_* minimum are dependencies |
| Requested rational alpha_hat bracket | exact rational inequalities within the theorem | proof Section 4; new E and D enclosures | stdlib rational quadrature, no old checker/production imports | isolated gates are not finite geometric certificates |
| C_hat<C_107-1/22000000 and rational upper bound | exact theorem / proved comparison | proof Section 5; strong convexity and rational arithmetic | analytic deduction | accepted C_107 bound and pi inequality imported |
| Fixed-order full-radius limit and actual feasibility | exact theorem | proof Section 6 | imported arbitrary-permutation and uniform-root theorems | those complete dependencies are not re-proved here |
| Global limsup at most C_hat | proved corollary | proof Section 7; feasibility followed by deletion | analytic deduction | no global equality or normalized limit existence |
| Displayed decimal values | numerical observations | independent original full-max quadrature at 70 digits | separate quadrature engine and arithmetic | not exact intervals or proof premises |

Mathematical detail belongs only in
research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md. Definitions,
family/fixed-order statements and coefficient comparisons have one owner,
knowledge/FIXED_ORDER_THEORY.md; only the global deductions belong to
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md. No new stable claim was copied to
another thematic ledger or PROJECT_KNOWLEDGE.md.

## Commands and checks

Startup read-only Git status (with per-command safe.directory) was empty;
rev-parse returned the HEAD above. Python environment probe exited 0.
The initial unconfigured Git status failed on the ownership guard and was
repeated as documented in TASK_LOG.md. No Git configuration was written.

All commands below were freshly executed LOCAL checks. No hosted CI or
external-review result is asserted.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python -c "import sys, mpmath; print(sys.version); print('mpmath', mpmath.__version__)"` | 0; Python 3.14.3, mpmath 1.3.0 | existing environment | installation or hosted environment |
| `python -S -u ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py --exact-only` | 0; nine lines below | new rational gates and 120 recovery cases, with site packages disabled | imported theorem proofs or geometric global certification |
| `python -u ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py` | 0; exact output plus six diagnostic lines below | independent E/D/F' quadrature and original unnormalized full-max cost | interval certification of diagnostic decimals |
| In-memory `python -S -` audit below, supplied through a literal PowerShell here-string | 0; two PASS lines and eight hashes below | nine allowed files, seven links, imports/compilation, protected dependencies, whitespace | mathematical correctness |
| `git diff`, `git diff --check`, `git status --short --untracked-files=all`, with repository-scoped safe.directory | 0; four tracked edits, five additions, no whitespace error | tracked changes and full path inventory | untracked contents without the separate direct read and whitespace audit |

The exact-only and full checker modes were first run before the final source
audit, then rerun after adding the explicit XL>tau square-root gate. Both
final runs exited 0 with this exact-mode output:

```text
PASS analytic rational gates: wrap gap>1/15; Fsecond>46/405>1/9; Fprime(0)<-29/1245; Fprime(1/2)>13/108; Esecond<3
EXACT E(5753/20000) in [-844268665,-844268070]/1000000000000
EXACT E(x_*) in [-844272415,-844268070]/1000000000000
EXACT D(1093/10000) in [935124205,935201790]/1000000000000
EXACT Fprime(1093/10000) in [-1427184,-1344781]/1000000000000
EXACT D(10931/100000) in [938842182,938919761]/1000000000000
EXACT Fprime(10931/100000) in [2282349,2364747]/1000000000000
PASS isolation/comparison: 1093/10000<alpha_hat<10931/100000; C_107-C_hat>1/22000000; C_hat<14191364/100000000
PASS recovery: 120 exact cases, m=2..16; endpoint shifts, coincident seams, cyclic predecessors and 3/m errors
```

All displayed intervals are outward rational roundings of Fraction
endpoints onto a 10^-12 grid, not decimal approximations used as input.
The first PASS line verifies the rational implications of the analytic
proof; it does not numerically sample or prove the all-domain inequalities.
The E enclosure uses 2048 concave panels per active branch, 64 unsquared
switch bisections and the analytic 3/800000000 displacement bound. D uses
256 concave panels per integral. All radical endpoints use a 10^-24 grid
and are checked by exact squaring. No numerical quadrature-error estimator
or floating-point sign enters any exact gate.

The 120 recovery cases are exactly alpha in
{0,1093/10000,10931/100000,1/2}, x in {719/2500,2877/10000}, m=2..16.
They compare the rank involution with reversal of the even entries of a
shifted list and inspect occurrence, actual cyclic predecessor, junction,
wrap and ordinary coordinate errors. They include r=q+1 with a nonempty
block and q=0,r=1 at m=2,alpha=1/2. These rational test parameters do not
stand in for the implicit minimizers' finite floors. Four invalid gate
inputs are also rejected as specified.

Additional full-mode output:

```text
PASS independent 70-digit diagnostics: E and both D/Fprime enclosures; four original full-max cost identities including alpha=0,1/2
NUMERICAL alpha_hat = 0.10930369632641477424523225745801230942
NUMERICAL E(x_*) = -0.00084426854028715746307587675747719648474
NUMERICAL C_hat = 0.14191349134456084326890229893638278332
NUMERICAL C_107-C_hat = 0.00000015666216002543621573418467909454536218
NOTE: numerical observations only; imported full-feasibility/root theorems are not re-certified here.
```

The diagnostic independently integrates each original active full-max
branch, including its chain part, at alpha=0,107/1000,alpha_hat,1/2.
The identity with 2*K+A^2*E agrees to absolute error below 10^-60.
Both D and F' values and the E values fall inside the new rational
intervals. mpmath's root finder is used ONLY for these observations.
The earlier exploratory 40-digit stdin probe exited 0 and suggested the
same bracket; the final checker supersedes that probe as reproducible
evidence. It was never used to select exact signs or finite floors.

Skipped as outside this delta: production pytest, verify.py in either
frontier mode, finite geometry scans, older checkers, publication builds,
generated assets and hosted CI. The user supplied the accepted inputs;
replaying their broader experiments would not verify the new discriminator.

## Artifact and provenance checks

No result/certificate or publication asset is generated or modified.
The proof and checker are authored sources based on the recorded HEAD.
No random seed, search experiment or finite certificate extension applies.
The rational checker has fixed deterministic budgets and writes no files.

SHA256 of the local source bytes (dependency text also compared against
HEAD after line-ending normalization):

| Source | SHA256 |
|---|---|
| research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md | ad166ea8ccfdc1a60073e5ff2f005a4299b678416f0f1358ca096a58571c6751 |
| ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py | 19ed6ee315d22c5cfe525778cf032bfac8d89a803d23826ed5bd5f2bf9850521 |
| research/SHIFTED_ALTERNATING_HALVES.md | baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db |
| research/PERMUTED_HALVES_REFLECTED_PREFIX.md | 485fefd9238d97799cf0801a395fb1ab077707c3b007e3a4361c2ef0588608b1 |
| research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md | 407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3 |
| research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md | 27ec250aaf59a6dab3777312bd4b051571064d96cc7e0fe44e2bbc4c00466292 |
| research/PERMUTED_ALTERNATING_HALVES.md | c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab |
| research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md | 4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63 |

No generation commit exists for the uncommitted authored additions; their
base HEAD and exact source hashes above provide the local provenance.

## Failed checks and negative evidence

The old neighborhood's r>=q+2 statement cannot be extended to every small
m in the new domain. The proof must use unioned exceptions, including
q=0,r=1 at m=2,alpha=1/2. No claim outside [0,1/2] is tested or inferred.

One editing batch was rejected before mutation because it attempted delete
and add operations on CURRENT_STATUS.md in the same patch. The tracked diff
was confirmed empty and the changes were reapplied as ordinary updates.
This was an editing-tool failure, not a failed mathematical gate. No
mathematical or checker failure occurred; no failed experiment was hidden.

A direct PowerShell Git status invocation with core.excludesFile=NUL
reported that NUL could not be used as an exclude file (the Python audit's
same setting had succeeded). Status was repeated without that optional
setting and exited 0 with the expected nine-file inventory; the harmless
global-ignore access warning remained. The subsequent diff check exited 0.

## Final diff inspection

- Complete four-file tracked diff inspected, including the replacement of
  the previous task status and the roadmap's single next priority.
- All five untracked additions read directly in full; source review checks
  the analytic domain, endpoint signs, full max, rounding direction, finite
  exceptions, theorem dependencies and epistemic labels.
- Explicit whitespace check covers all nine files, including the untracked
  additions; git diff --check exits 0. No staged changes, HEAD unchanged.
- The exact changed-path whitelist excludes previous proofs/dossiers,
  paper_assets/, results/, src/, tests/, scripts/, verify.py, publication
  metadata, README.md, REPORT.md, other ledgers, PROJECT_KNOWLEDGE.md,
  AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md. No protected or generated file
  was modified. No Git/GitHub state was written.
- Seven relative proof links resolve; eight source hashes recorded; six
  imported dependency texts match HEAD; canonical imports and in-memory
  Python compilation pass. This is a local audit, not hosted CI.

Final audit output (the eight hash lines above precede these lines):

```text
PASS file audit: 4 tracked edits, 5 additions; 7 local links; allowed imports and in-memory compilation; 6 unchanged dependency sources
PASS all-file whitespace and git diff --check; staged diff empty; HEAD unchanged; no protected or generated tracked paths changed
```


Reproduce the final source audit from the repository root by passing this
Python body to `python -S -` in a literal PowerShell here-string. The
safe.directory and excludesFile settings are per-command only; no Git
configuration is changed. This is the actual final audit body:

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

git = ['git', '-c', 'safe.directory='+Path.cwd().as_posix(), '-c', 'core.excludesFile=NUL']
def readgit(*args):
    return subprocess.check_output(git+list(args), text=True, encoding='utf-8')
task = 'ops/TASK-20260905__reflected_prefix_alpha_minimum'
proof = 'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md'
checker = task+'/check_alpha_minimum.py'
tracked = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md', 'research/NEXT_RESEARCH_STEPS.md'}
added = {proof, checker, *(task+'/'+name+'.md' for name in ('TASK_STATUS', 'TASK_LOG', 'EVIDENCE'))}
assert set(readgit('diff', '--name-only').splitlines()) == tracked
assert set(readgit('ls-files', '--others', '--exclude-standard').splitlines()) == added
assert not readgit('diff', '--cached', '--name-only')
assert readgit('rev-parse', 'HEAD').strip() == '4f32b37241578064667b5db7214c3d16d83e4859'
for name in sorted(tracked|added):
    data = Path(name).read_text(encoding='utf-8')
    assert data.endswith('\n') and all(line == line.rstrip(' \t') for line in data.splitlines()), name
links = re.findall(r'\]\(([^)]+)\)', Path(proof).read_text(encoding='utf-8'))
for target in links:
    assert (Path(proof).parent/target).is_file(), target
source = Path(checker).read_text(encoding='utf-8')
tree = ast.parse(source)
imports = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
imports |= {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
assert imports == {'__future__', 'argparse', 'fractions', 'math', 'mpmath'}
compile(source, checker, 'exec')
deps = ['SHIFTED_ALTERNATING_HALVES', 'PERMUTED_HALVES_REFLECTED_PREFIX', 'PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA', 'PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA', 'PERMUTED_ALTERNATING_HALVES', 'PERMUTED_HALVES_THREE_MARGINAL_RELAXATION']
for name in deps:
    path = 'research/'+name+'.md'
    assert Path(path).read_text(encoding='utf-8') == readgit('show', 'HEAD:'+path), path
for path in [proof, checker]+['research/'+name+'.md' for name in deps]:
    digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    assert digest in Path(task+'/EVIDENCE.md').read_text(encoding='utf-8'), path
    print(digest, path)
subprocess.run(git+['diff', '--check'], check=True)
print(f'PASS file audit: 4 tracked edits, 5 additions; {len(links)} local links; allowed imports and in-memory compilation; 6 unchanged dependency sources')
print('PASS all-file whitespace and git diff --check; staged diff empty; HEAD unchanged; no protected or generated tracked paths changed')
```

## Residual uncertainty

Imported accepted minimizer, arbitrary-permutation full feasibility and
uniform root-transfer theorems are dependencies. Numerical cross-checks
are observations only. External review of the new theorem is pending.
No general permutation/coupling optimum, finite global optimum or
normalized global limit is claimed.

The family theorem concerns the coefficient at each fixed alpha; it does
not identify finite-m minimizers or interchange a minimum with a limit.
The rational upper bound on C_hat is conservative. No finite accuracy
cutoff, external proof acceptance or hosted CI result is claimed.
