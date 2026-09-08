# Evidence

## Environment and provenance

    repository_head=dbb41f32613837a200e4f2213e4ee1583b60cc8e
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependencies=existing stdlib; existing mpmath 1.3.0
    task_mode=STRICT

New canonical proof: research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md.
Exact parameters and brackets are imported unchanged from the recovery's
named defining theorems. No numerical optimizer, new parameter enclosure,
random seed, factorial search or production implementation is used.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Exact parameters, mu_3 and weak recovery | imported exact theorems | recovery and continuous source notes; fresh checkers | imported minima not re-proved |
| All-m geometric transfer | exact fixed-order theorem | new proof Sections 2-3 | actual permutation and every criterion hypothesis audited; not global optimality |
| Full-max quantitative limit | exact theorem | Sections 4-5; explicit 174, 3808, 1198 constants | branches may disagree; no numerical limit fit |
| Odd lower squeeze and limit | exact theorem | Section 6 | retained-cell necessity, no alternating criterion after deletion |
| Global limsup improvement | proved corollary | Section 7 and imported strict full-cost saving | no global normalized limit or sharp coefficient |
| Bounded rational identities/enclosures | exact finite arithmetic / engineering fact | new exact checker | independent of production/verify.py; adapted comparison checker and shared analytic algebra, not external proof review |
| Pair geometry and feasibility probes | numerical observations | new 50-digit diagnostic | alternate angle and independent all-pairs difference constraints; not certificates |

The fixed-order ledger owns the coefficient, fixed-order results and
strict comparison. The global ledger owns the global corollary and only
cross-refers to the coefficient definition. No claim is given a second
thematic owner. PROJECT_KNOWLEDGE.md needs no scope/navigation change.

## Commands and results freshly run in this task

Every listed checker ran as its own local process and exited 0. Names
below are exact repository-relative command arguments. No hosted CI or
external review output is being reported as a local check.

| Exact command | Exit/result | Property checked; limitation |
|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime only |
| `python -c "import mpmath; print(mpmath.__version__)"` | 0; 1.3.0 | existing numerical dependency |
| `python -S -u ops/TASK-20260908__third_block_full_root/check_full_root.py` | 0; full output below | exact gates, floor overcovers, actual seams, deletion, full maxima; not all-m proof |
| `python -u ops/TASK-20260908__third_block_full_root/diagnose_full_root.py` | 0; summary below | both paths, Cartesian geometry, independent all-pairs feasibility; numerical only |
| `python -S -u ops/TASK-20260908__third_block_recovery/check_recovery.py` | 0; 632 floor cases, 365867 cells, 362724 panel bounds; all PASS | independent list recovery and constants, no radius theorem |
| `python -S -u ops/TASK-20260908__third_adjacent_block/check_third_block.py` | 0; eight endpoint partitions, 168 moments, 24 branch probes, five controls; all PASS | continuous full-cost saving; no finite geometry |
| `python -S -u ops/TASK-20260907__boundary_full_root/check_full_root.py` | 0; 38 floor triples, 14091 cells, 56364 signs, 213 enclosures, 28030 retained gaps, eight score/deletion enclosures; all PASS | comparison method, independent arctangent and shell/max/root gates; previous two-block family |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable local contract inventory |

New exact checker output:

```text
EXACT half-wrap margin = 26541513/1000000000
PASS domain, shell, full-max/tie, saving and constants 174,3808,1198; root/deletion cutoff 2048
PASS 57 floor cases; 156632 actual cells; 626528 rational branch signs; 504 independent angle/full-max enclosures
PASS 313036 disjoint retained odd gaps; all small cycles and both m=46 floors
PASS 8 complete-score and two-cell deletion interval bounds at c=1/32,1/2
PASS incorrect shared/cyclic predecessors, merged second/third, lost/duplicated seam and single-branch controls; 5 invalid inputs
NOTE: exact finite arithmetic audits; analytic all-m proofs and imported minima remain separate
```

The predeclared exact sizes are m=2..16 and
{32,45,46,47,1999,2000,2001,2047,2048,2049,3999,4000,4001,5999,6000,6001}.
All strict-bracket-compatible (s,q,d) floors are overcovered; f is exact
integer division. Every cell receives sign-safe branch checks at
R in {1,m^2/8,m^2/2,2*m^2}. Seams and selected threshold interiors
receive directed rational square-root/arctangent enclosures at R=2*m^2.
Complete score enclosures use m=32,46,47 at c=1/32,1/2. The earlier
recovery checker separately covers all cases m=2..512 and 13 sizes
through 8000, with empty/identity/nonidentity/parity cases and seven
actual rejected mutations plus 12 invalid inputs. Ambiguous floors are
never decided from approximate roots; ignored correlations only add cases.

Independent numerical summary:

```text
PASS 14 floor cases; 19822 even/deleted-odd pairs: both directed paths and Cartesian distances
PASS 54 independent all-pairs difference-constraint probes; even root sides and odd squeeze sides
NOTE: 50-digit numerical observations, tolerance 1e-32, probe offset 1e-12*max(1,rho); no exact certificate or implicit-floor oracle
```

The numerical sizes are m=2..12,16,46, including both permitted m=46
widths (identity reversals, equal orders). Every even root uses 120
bisection steps with the full asin maximum. At rho+step, both even
and deleted-odd placements pass alternate-atan directed pair bounds
and independent Cartesian distances. A Bellman-Ford solver with all
pair constraints, no cell-score input and explicit returned-witness
constraint checks, accepts at rho+step and rejects even rho-step.
For m>=4 it also rejects the odd order at tau-step. This tests the
separate lower and upper squeeze sides, not equality of the odd optimum
with either endpoint. No odd root, global optimum or cost limit is
estimated. Numerical all-pairs loops are bounded at m=46; large third
thresholds receive linear cell/seam audits, not factorial searches.

Fresh continuous checker also returned the independent raw full-max upper
enclosure -22276595597267606801027/800000000000000000000000000000000,
strictly below -1/36000000000, and the exact conversion
C_b-C_3>1/576000000000. This is a rational integral enclosure rather
than subtraction of nearby decimal coefficients. The new theorem
identifies its C_3 with the geometric limit analytically.

Skipped as inapplicable: production pytest, verify.py smoke/frontier,
paper builds and hosted CI. No production logic, finite certificate,
publication asset or CI definition changes. The all-m proof is separate
from every bounded computation; external mathematical acceptance is pending.

## Artifact and provenance checks

No generated result, finite certificate or publication artifact. New
proof and checker files are authored sources, and checkers write no
files. The exact checker transparently adapts the prior boundary checker
at the recorded base HEAD, with no imports of that checker or production.
The numerical solver is standalone. The containing commit identifies
their integrated source revision; source hashes are recorded by the
audit below. No new generation-commit claim is made about old artifacts.

## Failed checks and negative evidence

Initial plain Git reads failed the sandbox ownership guard. A command-local
safe.directory equal to the resolved repository root fixed reads without
changing persistent Git configuration. Personal-ignore access warnings
were nonfatal. One apply_patch request was rejected because it attempted
delete/add operations on CURRENT_STATUS.md in a single patch; no file
changed. Splitting the roadmap patch from the status replacement succeeded.
Some combined source displays exceeded the output budget; truncated
portions were read separately before final inspection.

All positive mathematical/checker runs passed on their first execution.
Negative controls are expected detections, not positive-test failures.
No all-pairs, deletion or squeeze obstruction was found. The numerical
checks cover only small cases; exact threshold checks and analytic proof
supply their distinct evidence layers.

## Final diff inspection

Audit invocation: run `python -S -` with the following exact Python source
on stdin from the repository root. It explicitly checks untracked source
whitespace, which ordinary git diff omits, and checks both ledger owners
by their separate sections. Command-local safe.directory changes no config.

```python
from pathlib import Path
import ast, hashlib, re, subprocess
base = 'dbb41f32613837a200e4f2213e4ee1583b60cc8e'
git = ['git', '-c', 'safe.directory='+Path.cwd().as_posix()]
def run(*args):
    result = subprocess.run(git+list(args), capture_output=True,
                            text=True, encoding='utf-8')
    assert result.returncode == 0, (args, result.returncode, result.stderr)
    return result.stdout
task = 'ops/TASK-20260908__third_block_full_root/'
proof = 'research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md',
           'research/NEXT_RESEARCH_STEPS.md', proof}
allowed |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md',
                            'check_full_root.py', 'diagnose_full_root.py')}
assert run('rev-parse', 'HEAD').strip() == base
entries = run('status', '--porcelain=v1', '--untracked-files=all', '-z').split('\0')
assert {e[3:] for e in entries if e} == allowed
assert set(run('diff', base, '--name-only').splitlines()) <= allowed
assert run('diff', '--check') == ''
assert run('diff', '--cached', '--check') == ''
for name in sorted(allowed):
    source = Path(name).read_text(encoding='utf-8')
    assert source.endswith('\n') and not source.endswith('\n\n'), name
    assert all(line == line.rstrip() for line in source.splitlines()), name
    assert all(ord(c) >= 32 or c in '\t\n' for c in source), name
    if name.endswith('.py'):
        tree = ast.parse(source, filename=name)
        compile(tree, name, 'exec')
        imports = [n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
        imports += [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
        expected = ['fractions', 'math'] if name.endswith('/check_full_root.py') else ['fractions', 'mpmath']
        assert imports == expected, imports
        assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(tree))
links = re.findall(r'\]\(([^)]+)\)', Path(proof).read_text(encoding='utf-8'))
assert all((Path(proof).parent/target).is_file() for target in links)
protected = ['AGENTS.md', 'PROJECT_KNOWLEDGE.md', 'RINGMIN_REVIEW_PROTOCOL.md',
             'verify.py', 'paper_assets/ringmin_paper.tex', 'README.md', 'REPORT.md',
             'research/PERMUTED_ALTERNATING_HALVES.md',
             'research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md',
             'research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md',
             'research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md',
             'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
fixed = Path('knowledge/FIXED_ORDER_THEORY.md').read_text(encoding='utf-8')
global_ledger = Path('knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md').read_text(encoding='utf-8')
fixed_entry = fixed.split('### Three-block full-root transfer and quantitative even/odd limits')[1].split('\n## ')[0]
global_entry = global_ledger.split('### Three-block full-root transfer: improved global upper bound')[1].split('\n### ')[0]
assert '1198/m' in fixed_entry and 'limsup R*' not in fixed_entry
assert 'limsup R*(n)/n^2<=C_3<C_b' in global_entry and '1198/m' not in global_entry
owners = {p.name for p in Path('knowledge').glob('*.md') if Path(proof).name in p.read_text(encoding='utf-8')}
assert owners == {'FIXED_ORDER_THEORY.md', 'GLOBAL_BOUNDS_ASYMPTOTICS.md'}
for name in (proof, task+'check_full_root.py', task+'diagnose_full_root.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 10 allowed paths; tracked/untracked whitespace; standalone AST/imports')
print('PASS', len(links), 'proof links; separate claim owners;', len(protected), 'protected texts equal baseline')
print('PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta')
```

The audit exited 0, with these source hashes:

| Source | SHA256 |
|---|---|
| canonical proof | 93d9d487303a2c8b8c6fc4c1e962079513583e1e484f4c3557bd5c66c760949e |
| check_full_root.py | 2189f286c4e005744ef9e649f0150d07772f08ba8662ef155a23a9b705062eb6 |
| diagnose_full_root.py | d357d71381f4aaac24b01e956a54f6eba02da4957807f5a41102b8ff3d071a6a |

```text
PASS 10 allowed paths; tracked/untracked whitespace; standalone AST/imports
PASS 7 proof links; separate claim owners; 12 protected texts equal baseline
PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta
```

The four existing documentation diffs and all six additions were read
completely; the last proof sections were read separately after one
combined display truncated. The complete delta contains only the ten
declared paths, excluding all previous proof notes/dossiers, publication
assets, certificates, production, tests, scripts and other ledgers. Twelve
named protected texts also equal the base after newline normalization.
Both claim owners are audited by their distinct sections; the global
entry cross-refers to the fixed-order coefficient.

The audit was rerun over the completed dossier before staging: exit 0
with identical hashes and PASS lines. The explicit ten-path git add
exited 0 with tool-granted escalation under standing authorization.
The complete `git diff --cached --no-ext-diff --no-color` was inspected
as ten file diffs; every `git show :path` equals its already inspected
working source after newline normalization. The four existing-file
staged diffs were also displayed in full. `git diff --cached --check`
and `git diff --check` exited 0 with no output; `git diff` was empty.
The cached stat at that inspection was ten files, 1362 insertions and
62 deletions. This final small status/evidence/log update is inspected
and restaged before commit, with no proof/checker source changes.

Authorized commit and push use existing origin/main; the final handoff
records the containing SHA, actual push and remaining tree. Commit/push
is separate from mathematical acceptance.

## Residual uncertainty

Exact definitions/brackets and recovery/continuous theorems remain imported
premises. The proof establishes fixed-order limits and a global upper bound;
global optimality, a normalized global limit, sharpness and finite-n
improvement cutoffs remain unproved. No new certificate, floating-circle
result or parameter optimization. External review and exact-SHA hosted CI
have not been performed in this task.
