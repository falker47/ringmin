# Evidence

## Environment

```text
repository_head=c8f8c1e0ac665bfac794dc7214fab1112dafd120
platform=Windows / PowerShell
python=3.14.3
sympy=1.14.0
mpmath=1.3.0
dependency_source=existing local installation; no dependency changes
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| Triangle minimum and arbitrary simple-path bound | Exact theorem | Proof note sections 2-3 | Analytic; symbolic audit is not a proof assistant |
| Full feasibility at the root iff Delta>=0 | Exact theorem | Sections 4-5, both arcs and forced gaps | Fixed order only; no seam-sign premise |
| Complete integer classification and no equality | Proved corollary | Section 6 and cited exact seam theorems | Imports remain proof dependencies |
| Finite exact identities and small-cycle coverage | Independently reproduced finite result | check_exact.py | Guards transcription/indexing; no all-k proof |
| Finite root and Cartesian agreement | Numerical observation | diagnose.py | Falsification only, no interval certificate |

## Commands and checks

All commands below ran locally from the repository root. No package was
installed. Both scripts adapt the earlier boundary-family audit in this
repository but import neither it nor src/ringmin, verify.py, each other,
or the imported seam checkers. Their independence is from production,
not a claim of separately authored proof review.

### Exact audit

Commands (each exit 0):

```text
python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py
python -I -O ops/TASK-20260904__supnick_feasibility_classification/check_exact.py
```

Identical complete output from both final-source runs:

```text
EXACT IDENTITY AUDIT; SymPy=1.14.0; no numeric roots
PASS: 9 general identities; N=3/N=4 closure and all paths; rational N=3 root 6/23; 2 wrong-sign rejections
PASS: 32 rank/parity constructions, 276 edges; all rotations/reflections; both central-correction cases
PASS: 1482 unordered pairs, 2964 directed paths; formal telescoping and complementary coverage
PASS: 82 rejection gates total
LIMIT: finite audits guard transcription; the note supplies the all-k proof
```

The nine general identities are the original first/mixed derivatives,
transformed mixed derivative, increasing radius parametrization, Cartesian
contact identity, arbitrary path induction step, seam-complement excess
sign, triangle rectangular remainder and angular central correction.
Symbolic small-cycle checks cover N=3/N=4 complements and nonadjacent paths;
nonnegative excess symbols check the zero-sum closure argument in both sizes.
For the concrete radii 1,2,3 at R=6/23, all sine/cosine values are rational,
each angle is in (pi/2,pi), and their unit-complex product is exactly 1.
The angle sum lies in (3pi/2,3pi), forcing it to be 2pi. This corroborates
one exact small root without numerical root evaluation or a Soddy import.

The 32 cycles use k=1,2,6 and N=3..12, plus (k,n)=(6,29),(7,33).
Exact integer/Fraction edge counters independently compare rank and parity
constructions and the symmetrized sum including the even correction.
Every pair has two simple paths covering every edge once, including the
closing edge; formal fan coefficients and the Delta=0 equality pattern
are checked. Rejection gates catch wrong derivative/complement signs,
duplicate vertices, omitted closure and omitted even central correction.
No asserts disappear under -O. These checks audit algebra and indexing;
they do not mechanically prove the analytic inequalities for all k,n.

### Finite falsification check

Command (exit 0):

```text
python -I ops/TASK-20260904__supnick_feasibility_classification/diagnose.py
```

Complete output:

```text
NUMERICAL OBSERVATION ONLY; mpmath=1.3.0; dps=80
k=1..12; N=3..8 plus n=s_k-1,s_k,s_k+1; 300 bisections; guard=1e-55; no seeds
k=1: small cycles and both onset sides checked
k=2: small cycles and both onset sides checked
k=3: small cycles and both onset sides checked
k=4: small cycles and both onset sides checked
k=5: small cycles and both onset sides checked
k=6: small cycles and both onset sides checked
k=7: small cycles and both onset sides checked
k=8: small cycles and both onset sides checked
k=9: small cycles and both onset sides checked
k=10: small cycles and both onset sides checked
k=11: small cycles and both onset sides checked
k=12: small cycles and both onset sides checked
PASS: cases=106 feasible=82 infeasible=24 triangles=445470 directed_paths=29608
PASS: bounded diagnostic only; no counterexample detected
```

The domain, stopping rule, precision, guard and discriminator were fixed
in TASK_LOG.md before execution. Angles use the independent acos law-of-
cosines expression; every triple (up to endpoint reversal), every pair's
two paths, and Cartesian distances are scored. Signs close to the guard
are rejected as unresolved. The negative cases must overlap at the seam
and violate its complement upper bound; in positive cases with N>=4 the
minimum nonadjacent path slack must equal the seam. Root residuals must
be below 1e-55. Numerical evaluation and 300 bisections are not an interval
certificate, nor a claim of 300 effective bits at 80 decimal digits.
The expected signs are compared with the known theorem, not used to infer
it. Work is polynomial in the finite cycle sizes, with no order enumeration.

### Scope and whitespace audit

The following source ran as a PowerShell single-quoted here-string piped
to `python -I -` (exit 0), and is rerun after the final status update:

```python
from pathlib import Path
import hashlib
import subprocess
root = Path.cwd()
prefix = ['git', '-c', 'safe.directory=' + root.as_posix()]
def git(*args):
    return subprocess.run(prefix + list(args), check=True, capture_output=True, text=True).stdout
folder = 'ops/TASK-20260904__supnick_feasibility_classification/'
expected = {'CURRENT_STATUS.md', 'PROJECT_KNOWLEDGE.md', 'research/NEXT_RESEARCH_STEPS.md', 'research/SUPNICK_FULL_FEASIBILITY.md'}
expected.update(folder + n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_exact.py', 'diagnose.py'))
status = git('status', '--short', '--untracked-files=all')
changed = {line[3:] for line in status.splitlines()}
if changed != expected:
    raise RuntimeError(('scope mismatch', changed ^ expected))
for name in sorted(expected):
    raw = (root / name).read_bytes()
    content = raw.decode('utf-8')
    if raw.startswith(b'\xef\xbb\xbf') or b'\r' in raw or not raw.endswith(b'\n'):
        raise RuntimeError(('encoding/newline', name))
    for index, line in enumerate(content.splitlines(), 1):
        if line.rstrip() != line:
            raise RuntimeError(('trailing whitespace', name, index))
if git('rev-parse', 'HEAD').strip() != 'c8f8c1e0ac665bfac794dc7214fab1112dafd120':
    raise RuntimeError('HEAD changed')
if git('diff', '--cached', '--name-only').strip():
    raise RuntimeError('index changed')
git('diff', '--check')
print('PASS: exact 9-file scope; UTF-8/LF/final newline/no trailing whitespace, including 5 untracked files')
print('PASS: git diff --check; HEAD and index unchanged; protected tracked paths unchanged')
for name in ('research/SUPNICK_FULL_FEASIBILITY.md', folder+'check_exact.py', folder+'diagnose.py', 'research/FIXED_K_SUPNICK_SEAM.md', 'research/SUPNICK_SEAM_SEQUENCES.md'):
    print(hashlib.sha256((root/name).read_bytes()).hexdigest(), name)
```

Material output:

```text
PASS: exact 9-file scope; UTF-8/LF/final newline/no trailing whitespace, including 5 untracked files
PASS: git diff --check; HEAD and index unchanged; protected tracked paths unchanged
```

The five hashes are below. Git was used read-only with command-local
safe.directory, leaving global configuration unchanged. Direct
`git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check`
also exits 0 with no output.

### Checks not run

Production pytest, verify.py and the paper build were not run because
production, certification and publication paths are unchanged. They do
not validate this analytic proof. The imported seam checkers were not
rerun; their earlier outputs remain historical evidence, not independent
reproduction in this task. Hosted CI and an external reviewer were not
inspected. No new global certificate or optimality claim is made.

## Artifact and provenance checks

No result or publication artifacts generated. Task-local scripts and proof
are uncommitted sources based on the recorded HEAD, not artifacts generated
by that commit. The commands, deterministic inputs and versions are above.

| Source | SHA-256 |
|---|---|
| research/SUPNICK_FULL_FEASIBILITY.md | 271469c769d2c02f4e7952a302b2eea72834dfb7a2f42257c325ab4d7a4073a7 |
| This dossier: check_exact.py | 1d950671937e6d6525b04575628871efce3bb28ce6b294c448ae20bc87a3fc65 |
| This dossier: diagnose.py | 681a65b6ee0806434d83bc84f0f3abec71382a752f8fc86c83f07abce4adb465 |
| research/FIXED_K_SUPNICK_SEAM.md | 24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71 |
| research/SUPNICK_SEAM_SEQUENCES.md | 1312918f01aa755f11ff4221601c9ef000b4d703869bd695d06a6a5a7685a04f |

## Failed checks and negative evidence

Startup ownership/ignore-file and filename issues are in TASK_LOG.md.
No mathematical check failed and no counterexample was detected. The
negative cases in the diagnostic are expected fixed-order infeasibility,
not failures of the equivalence. Positive seam alone was never assumed
to imply feasibility: the triangle/path argument establishes that step.

## Final diff inspection

- All four tracked diffs inspected, and all five untracked additions read
  in full. The final status/dossier update is inspected again afterward.
- Explicit whitespace audit includes all nine files, including the five
  additions omitted by ordinary git diff. UTF-8, LF, final newline and
  trailing-whitespace checks pass; git diff --check exits 0.
- Exact scope comparison confirms no changes to AGENTS.md, src/, tests/,
  verify.py, results/, paper_assets/, README.md, REPORT.md, generation
  scripts, dependencies, other proof notes or prior dossiers.
- HEAD and index unchanged. No Git-history or GitHub writes. No generated
  publication or result artifacts. Manual commit remains the user's action.

## Residual uncertainty

Human proof review and manual integration remain pending. No gap was
identified within the stated analytic argument and explicit imports;
the symbolic audit is not a proof assistant and the finite diagnostic
cannot prove universal or exact-root claims. Delta=0 is handled in the
equivalence before the imported strict signs exclude it for all integer
k,n. No hosted CI, global-optimum or floating-circle conclusion is claimed.
