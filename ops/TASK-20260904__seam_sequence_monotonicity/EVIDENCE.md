# Evidence

## Environment

```text
repository_head=77c17be5970f6507b111f04ce90f2d67facfdfcf
platform=Windows / PowerShell
python=3.14.3, MSC v.1944 64 bit (AMD64)
mpmath=1.3.0 (existing environment, matching requirements.txt)
sympy=1.14.0 (existing installation, optional separate audit only)
primary_checker_dependencies=Python standard library
mode=STRICT
```

No dependency, Git history, configuration or GitHub state was written.
All checks below are local. No hosted CI run or external reviewer was
inspected. Protected production and global-certification components were
not re-certified by this task.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Both consecutive-k inequalities for every integer k>=6 | Exact theorem | research/SUPNICK_SEAM_SEQUENCES.md, sections 1-6 | Analytic proof plus exact finite algebraic certificates; no scan or effective-tail premise |
| s_k=4k+6 for every k>=6 | Proved corollary | Section 6, prior radius-6 bridge and fixed-k persistence | Bridge rerun exactly; imported general theorem still requires mathematical review |
| All formal seam onsets for positive integer k are classified | Proved corollary | New theorem plus existing k=1..5 theorems | Those five earlier theorems are imported, not re-audited here |
| Polynomial and rational gates close | Exact finite algebraic checks | check_exact.py and check_symbolic.py | Separate arithmetic implementations; no production/diagnostic import |
| Thirty diagnostic differences have the proposed signs | Numerical observation | diagnose.py, 80 digits | Not interval-certified and not a proof premise |
| Published assets and global-certification scope unchanged | Engineering fact | Final path/diff audit | No new global or full-feasibility result |

## Commands and exact results

Commands run from the repository root. The following short directory name
is only a notation in this table:
`D=ops/TASK-20260904__seam_sequence_monotonicity`.

| Exact command (expand D as above) | Exit and material output | Property checked / limitation |
|---|---|---|
| `python D/diagnose.py` | 0; `diagnostic_only=true dps=80 range=6..20 stop=first_failure`; all 30 `expected=True` | Bounded falsification guidance only; root indices 6..21 |
| `python -I -B D/check_exact.py` | 0; `exact_sequence_gates=PASS arithmetic=stdlib/Fraction optimized_safe=YES` | All finite proof gates; analytic inequalities are in the proof note |
| `python -I -B -O D/check_exact.py` | 0; identical output | Gates do not depend on Python assert statements |
| `python -I -B D/check_symbolic.py` | 0; both `symbolic_threshold_derivative_conjugate_and_five_gates=PASS` and `symbolic_F_A_B_w_g_derivatives=PASS` | Independent SymPy differentiation and coefficient reconstruction, no checker import |
| `python -I -B ops/TASK-20260805__radius6_seam_onset/check_seam.py --order-stop 30` | 0; `exact_stdlib_fraction_audit=PASS explicit_gates=2312 optimized_safe=YES`; `numerical_diagnostics=SKIPPED` | Existing exact k=6 bridge, domain, constants, full edge tables and construction conventions; no new onset artifacts |
| Read-only Git diff and whitespace commands below | 0; full diff displayed, whitespace check silent | Tracked changes only; supplemented by direct untracked review |

The final stdlib checker also prints exactly:

```text
derivative_upper_c5_at_6=-205349/72000 margin_below_minus_8over3=13349/72000
derivative_lower_c6_at_6=1398247/363000 margin_above_8over3=430247/363000
parity_constructions=4 cyclic_edges=104 central_correction=PASS
targeted_rejections=6 PASS
production_imports=0 diagnostic_imports=0 root_evaluations=0 k_scan=NONE
```

For each c=5,6, the ten-gate audit reports these exact degree/positive-count
pairs: radical coefficient (8,9), lower pre-square (10,11), lower margin
(20,20), upper pre-square (10,11), upper margin (20,20). Only the two margin
polynomials have an origin zero. Every closed endpoint t=1/6 passes.
The separate SymPy 1.14.0 implementation reconstructs all ten certificates.

The existing radius-6 checker specifically reports:

```text
exact_threshold_domain_and_R211over2_bridges=PASS n=24,25,29,30
exact_complete_edge_tables_and_chain_bridges_at_R211over2=PASS n=29,30
exact_pi_identities=PASS 333/106<pi<22/7
shifted_order_conventions_and_edge_sets=PASS n=8..30
```

The diagnostic's first differences were
`-3.41153444735340920347471783119625528781404819` (c=5) and
`4.04901793162944047668993178692733141386148415` (c=6).
At transition 20 the differences were
`-15.505019185481149780381143764075699796648037` and
`5.53070592840085821103850285894622970023522466`.
No extra scan, two-precision confirmation, or radius-onset diagnostic was run.

Read-only Git commands used a command-local owner exception; the final
portable PowerShell form actually run was:

```powershell
$taskRepo = (Get-Location).Path.Replace('\','/')
git -c "safe.directory=$taskRepo" diff -- PROJECT_KNOWLEDGE.md research/NEXT_RESEARCH_STEPS.md CURRENT_STATUS.md
git -c "safe.directory=$taskRepo" diff --check
```

`Get-Content` directly inspected the entire new proof and all three Python
files, with a second read of the proof's middle sections after a combined
response was truncated. Production pytest, the global verifier and the
paper build were skipped because their components are protected and
unchanged; they do not test these analytic or polynomial claims.

## Artifact and provenance checks

No results, paper assets, tables, CSVs, PDFs or onset artifacts were generated.
The proof and task-local checker sources are deterministic text additions
based on the HEAD above. Exact checker output is recreated by the listed
commands. The diagnostic depends on mpmath 1.3.0 and is not a certificate.
SymPy is optional for the separate audit; the primary verifier needs only
Python's standard library. No library was installed or upgraded.

Raw-file SHA-256 values for the new mathematical sources and the imported
sources inspected (computed using pathlib and hashlib):

| File | SHA-256 |
|---|---|
| `research/SUPNICK_SEAM_SEQUENCES.md` | `1312918f01aa755f11ff4221601c9ef000b4d703869bd695d06a6a5a7685a04f` |
| `research/FIXED_K_SUPNICK_SEAM.md` | `24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71` |
| `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` | `0eb5bfd94cd3c4d01c06939cd9a24be5d6df526cc373658d46062bfdcc059a43` |
| `research/RADIUS6_SEAM_ONSET.md` | `660b801e542280a609ae8f4edaf6d07c706c6c6a35c2569a2a320f02aa70aab5` |
| `paper_assets/ringmin_paper.tex` | `5042d01b0f0f54ed3badeaa494cd24411aa58a2aa2c865b3f02abb27fcbcc60a` |
| `ops/TASK-20260805__radius6_seam_onset/check_seam.py` | `ff095b9c8630d040bd7ab0ba868deca59c69afe9e2a623b3ed34d27151926622` |
| `ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py` | `8bbc39fd86c67f2ae5ce0dfc0965ba9633185786ced41c14fcc74bc25a9ee89b` |
| `ops/TASK-20260904__seam_sequence_monotonicity/check_symbolic.py` | `43eb4a7261a67ca502230e8ddd039dc592abe9e5760a5a5255163339d6910ddb` |
| `ops/TASK-20260904__seam_sequence_monotonicity/diagnose.py` | `1a072c261f95bd72b065ebb0735b19823ee92937af0c73133df23c39545eed08` |

## Failed checks and negative evidence

- Plain Git status failed dubious-ownership validation. Per-command
  safe.directory fixed the read without changing config. A later attempt
  to set core.excludesFile=NUL failed; it was dropped. Global ignore-file
  permission warnings do not conceal any changes in the explicit scope audit.
- The exploratory SymPy display count raised BooleanAtom TypeError, fixed
  by counting bool values; all mathematical coefficient signs passed.
- The first stdlib exact run exited 1 in its rejection suite, exposing a
  vacuous acceptance of the zero polynomial. A degree gate fixed it.
  All ten mathematical gates had already passed; final normal/-O runs
  reject the zero polynomial, negative/endpoint-invalid polynomials and
  reversed threshold margins (six checks).
- The first independent symbolic command exited 1 because simplify did not
  reduce the g'' radical expression to zero. Factor/together reduced it
  exactly to zero. The durable audit checks the cleared polynomial identity
  on the proof's positive-radicand domain and passes.
- A duplicate delete/add target caused one patch to be rejected before any
  edit. The authorized updates were then applied normally.
- No counterexample or failed mathematical inequality was found. There was
  no fallback to individual radius-onset proofs or artifacts.

## Final diff inspection

The complete tracked diff and all seven untracked additions were inspected
directly, including the final three dossier documents. The inline Python
audit below (executed from a PowerShell here-string piped to `python -`)
exited 0 and printed:

```text
delivery_audit=PASS files=10 untracked=7 hashes=9 protected_changes=0
format=UTF-8/LF final_newlines=PASS trailing_whitespace=0 HEAD=unchanged
```

The status contains exactly three modified tracked files (CURRENT_STATUS,
PROJECT_KNOWLEDGE and the roadmap) and seven untracked additions (the new
proof note and six dossier files). `git diff --check` exits 0 with no output.
The scope comparison excludes every protected path, including paper_assets/,
results/, src/, tests/, verify.py, README.md, REPORT.md, scripts/ and all
prior research notes/dossiers. No generated asset changed.

Reproducible delivery audit:

```python
from pathlib import Path
from hashlib import sha256
import re
import subprocess

root = Path.cwd()
dossier = 'ops/TASK-20260904__seam_sequence_monotonicity'
files = {'TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'diagnose.py', 'check_exact.py', 'check_symbolic.py'}
allowed = {'CURRENT_STATUS.md', 'PROJECT_KNOWLEDGE.md', 'research/NEXT_RESEARCH_STEPS.md', 'research/SUPNICK_SEAM_SEQUENCES.md'} | {dossier+'/'+name for name in files}
def require(ok, message):
    if not ok:
        raise ValueError(message)
def git(*args):
    result = subprocess.run(['git', '-c', 'safe.directory='+root.as_posix(), *args], capture_output=True, text=True, encoding='utf-8')
    require(result.returncode == 0, result.stderr)
    return result.stdout
status = git('status', '--short', '--untracked-files=all')
require({line[3:] for line in status.splitlines()} == allowed, 'scope mismatch: '+status)
require(sum(line.startswith('?? ') for line in status.splitlines()) == 7, 'untracked count')
require({p.name for p in (root/dossier).iterdir()} == files, 'dossier inventory')
for name in sorted(allowed):
    data = (root/name).read_bytes()
    content = data.decode('utf-8')
    require(not data.startswith(bytes((239, 187, 191))) and b'\r' not in data, 'encoding '+name)
    require(data.endswith(b'\n') and not data.endswith(b'\n\n'), 'newline '+name)
    require(all(line == line.rstrip() for line in content.splitlines()), 'whitespace '+name)
evidence = (root/dossier/'EVIDENCE.md').read_text(encoding='utf-8')
hashes = re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \|$', evidence, re.MULTILINE)
require(len(hashes) == 9, 'source hash count')
for name, digest in hashes:
    require(sha256((root/name).read_bytes()).hexdigest() == digest, 'hash '+name)
require(git('rev-parse', 'HEAD').strip() == '77c17be5970f6507b111f04ce90f2d67facfdfcf', 'HEAD changed')
require(git('diff', '--check') == '', 'tracked whitespace')
require(set(git('diff', '--name-only').splitlines()) == {'CURRENT_STATUS.md', 'PROJECT_KNOWLEDGE.md', 'research/NEXT_RESEARCH_STEPS.md'}, 'protected tracked change')
print('delivery_audit=PASS files=10 untracked=7 hashes=9 protected_changes=0')
print('format=UTF-8/LF final_newlines=PASS trailing_whitespace=0 HEAD=unchanged')
print(status)
```

## Residual uncertainty

The analytic proof and imported fixed-k/radius-6 theorems require independent
mathematical review; neither checker is a proof assistant. The four finite
parity constructions are corroboration of the general identity, not its
proof. No formal seam onset remains unclassified, but all-pairs feasibility,
global optima and floating claims remain separate. Global certification is
still 3<=n<=14. No hosted CI or external review result is claimed.

Exactly one next atomic task is in CURRENT_STATUS.md: prove or refute full
all-pairs feasibility of the formal Supnick placement on {k,...,4k+5} at its
chain root for all integer k>=6. It has not begun.
