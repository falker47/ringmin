# Evidence

## Environment

    repository_head=73a58f7a448ae61b5baa26afbfaf428a9c91c859
    platform=Windows; PowerShell
    python=3.14.3
    dependency_source=existing environment; no installation
    mpmath=1.3.0
    sympy=1.14.0
    task_mode=STRICT

## Claim ledger

The analytic proof is authoritative; the bounded checker is corroborative.
All commands below were run locally in this task. Independence here means
separation from production code, not external mathematical acceptance.

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| Exact induced edge families in both parities | exact finite identity | proof Sections 2-3; 13,113 bounded restrictions | rank traversal versus edge formulas; no production imports; bounded checks alone are not the proof |
| Psi and parity-uniform normalized O(1/n) error | exact chain-limit theorem | analytic Riemann sums, angular error, root bracket, Sections 2-4 | all-n quantifiers analytic; numerical roots only corroborate |
| Strict comparison on [1/5,23/100] | exact strict-comparison theorem | derivative positivity and four rational Taylor gates, Section 5 | entire interval follows analytically, without a beta scan |
| Positive common-tour minimax gain | unresolved claim | Section 6 explains the missing tradeoff/stability implication | no new lower bound or optimization |
| Sample roots and coefficient decimals | numerical observation | optional alternate-atan/asin diagnostic | not a certificate or proof premise |

## Commands and checks

From the repository root:

```powershell
python --version
python -c "import mpmath, sympy; print('mpmath',mpmath.__version__); print('sympy',sympy.__version__)"
python ops/TASK-20260909__macroscopic_terminal_discriminator/check_discriminator.py --symbolic --diagnostic
```

The environment commands exited 0 with Python 3.14.3, mpmath 1.3.0 and
SymPy 1.14.0. The corrected checker exited 0 with this material output:

```text
PASS exact arcs: 13113 restrictions; 6627 below, 6348 above, 138 middle; all four parity pairs; rotations/reversals.
PASS exact negative controls: omitted top seam rejected in both regimes.
PASS rational Taylor gate 1: 10924138073711/720000000000000 > 0
PASS rational Taylor gate 2: 37/2048 > 0
PASS rational Taylor gate 3: 102214670540903/504000000000000000 > 0
PASS rational Taylor gate 4: 751/40960 > 0
PASS rational interval implications: 3/17<q_*<1/5; (1+q_*)/5>4/17>23/100, margin 9/1700.
PASS symbolic: primitive, chord derivative, sign identity, midpoint continuity, replacement-chord integral (5 identities).
PASS diagnostic: 28 prescribed roots; alternate-angle agreement <2e-12; all parity pairs; max normalized error 2.320e-03.
DIAGNOSTIC C_term=0.140569080845; Psi(q_*,1/5)-C_term=0.000174024111589; Psi(q_*,23/100)-C_term=0.000768432818138.
```

The diagnostic uses 50-digit mpmath integrals and optimizer values, then
64 bisections with the alternate atan kernel in Python binary64, checked
against the asin closure. The seven parameter pairs and four sizes
256,257,1024,1025 are prescribed in source. Floors involving implicit q_*
are numerical observations only. No seeds or nondeterministic search
are used. A finite diagnostic radius may still lie below C_term*n^2;
there is no finite-size cutoff claim.

No pytest, production evaluator, all-pairs test, verify.py mode, artifact
regeneration or paper build was run: only research documents and the
standalone checker change, and no production or certification claim is
affected. No hosted CI run or independent reviewer result was inspected.

## Reproducible scope/protection audit

The following source was executed as a PowerShell single-quoted here-string
piped to `python -`, from the repository root (exit 0). It uses a
per-command, forward-slash-normalized safe.directory, without persistent
Git configuration changes.

```python
from pathlib import Path
import ast
import re
import subprocess

root = Path.cwd()
base = '73a58f7a448ae61b5baa26afbfaf428a9c91c859'
git = ['git', '-c', 'safe.directory=' + root.as_posix()]
task = 'ops/TASK-20260909__macroscopic_terminal_discriminator/'
expected = {'CURRENT_STATUS.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md',
            'research/NEXT_RESEARCH_STEPS.md',
            'research/MACROSCOPIC_TERMINAL_DISCRIMINATOR.md'}
expected |= {task + name for name in
             ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_discriminator.py')}
def output(*args):
    return subprocess.check_output(git + list(args)).decode('utf-8')
changed = set(output('diff', base, '--name-only').splitlines())
new = set(output('ls-files', '--others', '--exclude-standard').splitlines())
assert changed | new == expected, (changed | new) ^ expected
links = 0
for name in expected:
    data = (root / name).read_text(encoding='utf-8')
    assert data.endswith('\n') and not data.endswith('\n\n'), name
    assert all(line == line.rstrip() for line in data.splitlines()), name
    for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', data):
        if '://' not in link:
            assert (root / name).parent.joinpath(link).exists(), (name, link)
            links += 1
tree = ast.parse((root / (task + 'check_discriminator.py')).read_text(encoding='utf-8'))
imports = {item.name.split('.')[0] for node in ast.walk(tree)
           if isinstance(node, ast.Import) for item in node.names}
imports |= {node.module.split('.')[0] for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)}
assert imports <= {'argparse', 'collections', 'fractions', 'math', 'sympy', 'mpmath'}
owners = [p.name for p in (root / 'knowledge').glob('*.md')
          if '### Macroscopic terminal deletion: exact prescribed-order discriminator'
          in p.read_text(encoding='utf-8')]
assert owners == ['GLOBAL_BOUNDS_ASYMPTOTICS.md'], owners
protected = ['AGENTS.md', 'PROJECT_KNOWLEDGE.md', 'RINGMIN_REVIEW_PROTOCOL.md',
             'paper_assets/ringmin_paper.tex', 'verify.py', 'src/ringmin/patterns.py',
             'research/FIXED_K_SUPNICK_SEAM.md',
             'research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md',
             'research/COUPLED_TERMINAL_SUBSETS.md',
             'research/COUPLED_TERMINAL_ONE_LEVEL_ASYMPTOTICS.md']
for name in protected:
    assert (root / name).read_text(encoding='utf-8') == output('show', base + ':' + name).replace('\r\n', '\n'), name
subprocess.run(git + ['diff', '--check'], check=True)
print(f'PASS scope: exactly {len(expected)} task paths; all other tracked paths unchanged.')
print(f'PASS audit: whitespace including untracked additions; {links} local links; isolated imports; sole ledger owner.')
print(f'PASS protection: {len(protected)} dependency/contract/publication source comparisons; git diff --check exit 0.')
```

Material output:

```text
PASS scope: exactly 8 task paths; all other tracked paths unchanged.
PASS audit: whitespace including untracked additions; 5 local links; isolated imports; sole ledger owner.
PASS protection: 10 dependency/contract/publication source comparisons; git diff --check exit 0.
```

Git additionally warned that the sandbox account could not read the user's
global ignore file; the tracked diff and explicit task-file inventory
passed. Protected/generated directories have no tracked delta.
The initial run compared HEAD; the final rerun above pins the identical
task-base SHA so this audit also works after the task is committed.

## Final diff inspection

- Read the complete new proof and checker from disk, including a separate
  tail read to cover tool-output truncation. Read all three dossier files.
- Inspected the complete tracked diff for the global ledger, roadmap and
  CURRENT_STATUS.md. Only the global ledger owns the stable new claim.
- The explicit audit above checks all eight files, including the five
  previously untracked additions; ordinary diff alone would omit them.
- `git diff --check` exited 0. No protected or generated file changed.
- Final record edits are inspected and audited again before staging.
  Staged-diff inspection and `git diff --cached --check` are mandatory
  integration gates; actual commit/push/tree results belong to the final
  handoff and Git history, avoiding a self-referential commit hash.

## Artifact and provenance checks

Not applicable: no certificate, numerical result artifact, production
output or publication asset is generated. The standalone checker is source
code in this dossier. It uses no production import or saved certificate.

## Failed checks and negative evidence

Plain startup Git commands exited 1 due to ownership; a per-command
safe.directory override for the verified root permitted read-only checks.
The guessed src/ringmin/orders.py lookup failed; the actual source is
src/ringmin/patterns.py. No mathematical premise depends on either attempt.
The first checker execution exited 1 with a missing closing parenthesis
in the optional diagnostic. After that syntax-only fix, all checks passed.
A multi-file patch was rejected before applying because it tried to delete
and add CURRENT_STATUS.md in one patch; ordinary update patches succeeded.
A Git diff attempt using the unnormalized PowerShell root failed; the
forward-slash-normalized per-command root used above succeeded. No persistent
configuration was changed, and no mathematical counterexample was suppressed.

## Residual uncertainty

The positive discriminator alone is not a lower bound on the coupled
minimax: other common tours might trade outer cost against restricted cost.
External mathematical acceptance and hosted CI remain separate.

## 2026-09-10 — Fresh reproduction of the already committed result

The repeated user request exactly matches the result already present at
clean HEAD cf73a1be7db42eb85d11b55712123286ea449317. This section records
commands actually run in the resumed task, separately from the historical
commands above. It is a local reproduction, not an external acceptance.
The complete analytic proof and checker were read with their canonical
rank-edge, published ordering and exact optimizer dependencies. No correction
to the proof, sole global ledger entry or roadmap was required.

Commands from the repository root (PowerShell):

```powershell
python --version
python -c "import mpmath, sympy; print('mpmath',mpmath.__version__); print('sympy',sympy.__version__)"
python ops/TASK-20260909__macroscopic_terminal_discriminator/check_discriminator.py --symbolic --diagnostic
$ringminGitRoot = (Get-Location).Path.Replace('\', '/')
git -c "safe.directory=$ringminGitRoot" rev-parse HEAD
git -c "safe.directory=$ringminGitRoot" ls-remote origin refs/heads/main
```

The environment commands exited 0: Python 3.14.3, mpmath 1.3.0 and
SymPy 1.14.0. The checker exited 0 with the exact same arc counts,
rational fractions and interval implications recorded above. Material
output includes:

```text
PASS exact arcs: 13113 restrictions; 6627 below, 6348 above, 138 middle; all four parity pairs; rotations/reversals.
PASS exact negative controls: omitted top seam rejected in both regimes.
PASS symbolic: primitive, chord derivative, sign identity, midpoint continuity, replacement-chord integral (5 identities).
PASS diagnostic: 28 prescribed roots; alternate-angle agreement <2e-12; all parity pairs; max normalized error 2.320e-03.
DIAGNOSTIC C_term=0.140569080845; Psi(q_*,1/5)-C_term=0.000174024111589; Psi(q_*,23/100)-C_term=0.000768432818138.
```

The bounded checks remain independent of production imports and are only
corroborative. The all-integer limit and comparison on the whole beta
interval follow from Sections 2-5 of the proof, not these diagnostics.
Production tests, certificate verification, paper builds and hosted CI
were not run: no corresponding source, artifact or claim changed.

The live remote query initially exited 1 because the sandbox could not
connect to GitHub. Retried with the tool's approved network permissions,
it exited 0 and returned the same SHA as local HEAD:

```text
cf73a1be7db42eb85d11b55712123286ea449317    refs/heads/main
```

No persistent Git configuration was changed. The initial plain Git
ownership failure was resolved with the per-command safe.directory for
the verified root. The global-ignore permission warning did not prevent
tracked/untracked inventory or whitespace checks.

Before making the four documentation edits, the Python source in
"Reproducible scope/protection audit" above was executed verbatim from its
fenced block via a PowerShell here-string piped to `python -`. It exited 0:

```text
PASS scope: exactly 8 task paths; all other tracked paths unchanged.
PASS audit: whitespace including untracked additions; 5 local links; isolated imports; sole ledger owner.
PASS protection: 10 dependency/contract/publication source comparisons; git diff --check exit 0.
PASS current tracked/untracked state: ''
```

The resumed delta comprises only CURRENT_STATUS.md and this dossier's
TASK_STATUS.md, TASK_LOG.md and EVIDENCE.md. The complete four-file diff was
inspected. The following audit was run as a PowerShell single-quoted
here-string piped to `python -` (exit 0), and rerun after this record edit:

```python
from pathlib import Path
import subprocess
root = Path.cwd()
git = ['git', '-c', 'safe.directory=' + root.as_posix()]
base = 'cf73a1be7db42eb85d11b55712123286ea449317'
task = 'ops/TASK-20260909__macroscopic_terminal_discriminator/'
expected = {'CURRENT_STATUS.md'} | {task + p for p in
    ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md')}
def output(*args):
    return subprocess.check_output(git + list(args)).decode('utf-8')
assert set(output('diff', base, '--name-only').splitlines()) == expected
assert not output('ls-files', '--others', '--exclude-standard').strip()
for name in expected:
    data = (root / name).read_text(encoding='utf-8')
    assert data.endswith('\n') and not data.endswith('\n\n'), name
    assert all(line == line.rstrip() for line in data.splitlines()), name
subprocess.run(git + ['diff', '--check'], check=True)
print('PASS resumed scope: exactly 4 documentation paths; no untracked additions; every other tracked path unchanged.')
print('PASS resumed whitespace: all 4 complete files; git diff --check exit 0.')
```

Material output:

```text
PASS resumed scope: exactly 4 documentation paths; no untracked additions; every other tracked path unchanged.
PASS resumed whitespace: all 4 complete files; git diff --check exit 0.
```

This checks scope and whitespace, not theorem validity. In particular the proof,
checker, global ledger, roadmap, production/verifier code, results and
arXiv-v1 assets retain their committed content. Staged inspection and
`git diff --cached --check` precede commit/push; actual integration results
are reported in the final handoff. Mathematical classification and the
single next task (external independent review) are unchanged.
