# Evidence

## Environment

```text
repository_head=00b330c09ec5609fad900d0f302f21cd258241c0
platform=Windows / PowerShell
python=3.14.3
dependency_source=existing local Python installation
mpmath=1.3.0
sympy=1.14.0
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| D_5(k)<0 and the positive seam | Imported exact theorem | SUPNICK_SEAM_SEQUENCES.md and FIXED_K_SUPNICK_SEAM.md | Explicitly authorized imports; not reproved or rerun here |
| Every triangle defect is minimized at the seam triple | Exact theorem | Proof note section 2, positive partial derivatives and rectangular integral remainders | Direct analytic proof independent of production; human review pending |
| Each m-edge path has slack >=(m-1)Delta | Exact theorem | Proof note sections 3-4, explicit fan telescoping in both directions | Valid for arbitrary simple path length; finite audit is not its proof |
| Seam is the unique minimum up to reversal; full feasibility and fixed-order radius equality | Exact theorem / proved corollary | Proof note sections 1 and 4, positive seam and Cartesian reconstruction | Restricted to n=4k+5, k>=6; no global or floating claim |
| Both parity edge formulas and the angular central correction agree | Exact identity | Proof note section 5; formal coefficient audit | General formula justified analytically; four finite constructions guard indexing |
| k=6,7,8,9 satisfy the diagnostic checks | Numerical observation | diagnose.py, 80 digits | Separate acos implementation; no exact/all-k certification |
| Protected tracked paths and HEAD unchanged | Engineering fact | Exact nine-file scope audit and Git diff | Local checkout only; hosted CI not inspected |

## Commands and checks

All commands ran locally from the repository root on the environment above.
No package was installed or dependency file changed. Startup reads and
environment queries are recorded in TASK_LOG.md.

### Independent symbolic and combinatorial audit

Command:

```text
python -I ops/TASK-20260904__supnick_full_feasibility/check_exact.py
```

Exit 0; complete output:

```text
EXACT IDENTITY AUDIT; SymPy=1.14.0; no numeric roots
PASS: 6 symbolic identities; 1 wrong-sign rejection
PASS: 4 rank/parity constructions, 114 edges; all rotations/reflections; both central-correction cases
PASS: 1590 unordered pairs, 3180 directed paths; formal telescoping and complementary coverage
PASS: 11 rejection gates total
LIMIT: finite audits guard transcription; the note supplies the all-k proof
```

The six identities cover the direct first and mixed derivatives, the
transformed mixed derivative, the radius parametrization derivative,
Cartesian contact and the arbitrary-length path induction step. Exact
Fraction/Counter coefficients cover closure, the central correction and
both arcs for every pair in four cycles. Rejection gates detect a wrong
derivative sign, duplicate vertices, omitted closure and omitted even
central corrections. This script imports neither production code nor the
diagnostic, uses no floating root and does not reprove the seam imports.
It is a symbolic/combinatorial audit, not a proof assistant.

### Bounded diagnostic

Command:

```text
python -I ops/TASK-20260904__supnick_full_feasibility/diagnose.py
```

Exit 0; complete output:

```text
NUMERICAL OBSERVATION ONLY; mpmath=1.3.0; dps=80
k=6..9; 300 bisections; discrepancy guard=1e-60; no seeds
k=6 N=24 R~105.414978663059847 Delta~0.000166024936227 min_pair_path=(28, 29, 2) triangles=6072 pairs=276 paths=552 closure_error<1.0e-60
k=7 N=27 R~138.362765175605376 Delta~0.000687330949323 min_pair_path=(32, 33, 2) triangles=8775 pairs=351 paths=702 closure_error<1.0e-60
k=8 N=30 R~175.775773695489369 Delta~0.0009095084062 min_pair_path=(36, 37, 2) triangles=12180 pairs=435 paths=870 closure_error<1.0e-60
k=9 N=33 R~217.660495695801207 Delta~0.000986076078749 min_pair_path=(40, 41, 2) triangles=16368 pairs=528 paths=1056 closure_error<1.0e-60
PASS: bounded diagnostic only; no counterexample detected
```

The k range, precision, stopping count and guard were fixed before running.
Each triple is checked with sorted endpoints and every possible distinct
middle vertex, so all six roles of a given three-element set are covered
up to endpoint symmetry. Both cyclic arcs, including adjacent complements,
and all Cartesian distances are checked. The angle is evaluated using
acos from the law of cosines, separate from the analytic asin derivative
audit. The numbers are rounded diagnostics: 300 bisections at 80 digits
are not an interval certificate and do not promise 300 effective bits.
No diagnostic result is a premise of the exact theorem.

### Scope, whitespace and source provenance

The following Python source was executed as a PowerShell single-quoted
here-string piped to `python -I -` (exit 0). It checks untracked additions
explicitly; ordinary git diff alone would omit them.

```python
from pathlib import Path
import hashlib
import subprocess

root = Path.cwd()
prefix = ['git', '-c', 'safe.directory=' + root.as_posix()]
def git(*args):
    return subprocess.run(prefix + list(args), check=True, capture_output=True, text=True).stdout

dossier = 'ops/TASK-20260904__supnick_full_feasibility/'
expected = {'CURRENT_STATUS.md', 'PROJECT_KNOWLEDGE.md', 'research/NEXT_RESEARCH_STEPS.md', 'research/SUPNICK_FULL_FEASIBILITY.md'}
expected.update(dossier + name for name in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_exact.py', 'diagnose.py'))
status = git('status', '--short', '--untracked-files=all')
changed = {line[3:] for line in status.splitlines()}
if changed != expected:
    raise RuntimeError(('scope mismatch', changed ^ expected))
for name in sorted(expected):
    raw = (root / name).read_bytes()
    content = raw.decode('utf-8')
    if raw.startswith(b'\xef\xbb\xbf') or b'\r' in raw or not raw.endswith(b'\n'):
        raise RuntimeError(('encoding/newline', name))
    for line_no, line in enumerate(content.splitlines(), 1):
        if line.rstrip() != line:
            raise RuntimeError(('trailing whitespace', name, line_no))
if git('rev-parse', 'HEAD').strip() != '00b330c09ec5609fad900d0f302f21cd258241c0':
    raise RuntimeError('HEAD changed')
git('diff', '--check')
print(status, end='')
print('PASS: exact 9-file scope; UTF-8 without BOM, LF, final newline, no trailing whitespace')
print('PASS: git diff --check; HEAD unchanged; no protected tracked path changed')
for name in ('research/SUPNICK_FULL_FEASIBILITY.md', dossier + 'check_exact.py', dossier + 'diagnose.py', 'research/FIXED_K_SUPNICK_SEAM.md', 'research/SUPNICK_SEAM_SEQUENCES.md'):
    print(hashlib.sha256((root / name).read_bytes()).hexdigest(), name)
```

Material output:

```text
PASS: exact 9-file scope; UTF-8 without BOM, LF, final newline, no trailing whitespace
PASS: git diff --check; HEAD unchanged; no protected tracked path changed
```

The five printed SHA-256 values are recorded below. The same audit is
repeated after the final dossier/status update. `git diff --check` is also
run directly with a command-local safe.directory value: exit 0, no output.
Read-only status commands may warn that the sandbox cannot access the
owner's global ignore file; the repository-local status and nine-file
scope comparison still succeed. No global Git setting is changed.

### Checks deliberately not run

Production pytest, the standalone global verifier and a paper build were
not run: no production, certification, result or publication source changes.
They would not prove this new analytic statement. The earlier fixed-k and
sequence checks are historical imported evidence, not independently run
commands in this task. Hosted CI and external reviewer results were not
inspected. No global certification beyond 3<=n<=14 is claimed.

## Artifact and provenance checks

No publication or result artifact is generated or regenerated. The only
new computational sources are the task-local audit and diagnostic, with
explicit versions, inputs and outputs above. They are local uncommitted
work based on the recorded HEAD, not certificates generated by that HEAD.

SHA-256 of the proof/audit sources and the two unchanged imported notes:

| Source | SHA-256 |
|---|---|
| research/SUPNICK_FULL_FEASIBILITY.md | 27b6aa44fa8bc78cd040162b54505e5c787c970941161c9ebbccafcb5caeeefb |
| ops/TASK-20260904__supnick_full_feasibility/check_exact.py | e8aa49e24a9c0fa8750cb652ee3b1e603f2e9655a18a59da4b39f81346daa460 |
| ops/TASK-20260904__supnick_full_feasibility/diagnose.py | 44577c48844ab89decd9efcad044e3e8980f06a6ef6b5f36d79a48aa85b49674 |
| research/FIXED_K_SUPNICK_SEAM.md | 24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71 |
| research/SUPNICK_SEAM_SEQUENCES.md | 1312918f01aa755f11ff4221601c9ef000b4d703869bd695d06a6a5a7685a04f |

## Failed checks and negative evidence

Startup ownership, ignore-file and filename lookup failures, and one
atomic patch-context rejection, are preserved in TASK_LOG.md. They do not
supply mathematical evidence. There were no failed mathematical checks
or detected counterexamples. In particular, the proof does not use the
unjustified inference from a positive seam directly to full feasibility:
the triangle and path lemmas supply that missing implication here.

## Final diff inspection

- `git status --short --untracked-files=all`: three tracked modifications
  (CURRENT_STATUS.md, PROJECT_KNOWLEDGE.md, research/NEXT_RESEARCH_STEPS.md)
  and six additions (the proof note and the five dossier files).
- Complete tracked diff inspected. All six untracked additions read in
  full, including the proof, both scripts and final dossier text.
- Explicit nine-file UTF-8/LF/final-newline/trailing-whitespace audit passes,
  including every untracked addition. `git diff --check`: exit 0, no output.
- No tracked changes outside the exact authorized set. In particular,
  AGENTS.md, paper_assets/, results/, src/, tests/, verify.py, README.md,
  REPORT.md, generation scripts, dependencies and all prior notes/dossiers
  are unchanged. No generated or publication artifact was written.
- HEAD remains 00b330c09ec5609fad900d0f302f21cd258241c0. No Git-history,
  index or GitHub write was performed.

## Residual uncertainty

No mathematical gap remains in the stated argument subject to the
explicitly imported theorems. The proof and equality conditions still
require independent human review; the scripts are not proof assistants.
Finite numerical roots are observations only. General fixed-order
classification outside the requested boundary family remains a separate
task. No hosted CI, external review, global optimum or floating conclusion
is represented as established by this work.
