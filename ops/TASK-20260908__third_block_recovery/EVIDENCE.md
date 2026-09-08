# Evidence

## Environment

    repository_head=6f86fd1a98e9eb56cfbc78bc6444d8f816167879
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing Python; stdlib only, python -S
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Exact constants and brackets | imported exact theorems | boundary-minimum Sections 1, 6 | not re-proved | no midpoint or refined root |
| mu_3 definition | imported probability coupling | third adjacent block Sections 1-3 | no cost claim required | continuous target only |
| Permutation, cyclic pairs, floors, parity and counts | exact finite construction / theorem | new proof Sections 2-3 | direct algebra | no geometric feasibility |
| Quantitative arbitrary-test weak convergence | exact theorem | new proof Sections 4-5 | direct integral coupling | no R_full transfer |
| Finite identities and negative controls | bounded exact arithmetic / engineering fact | standalone checker | separate list constructor; no production imports | not the all-m proof or an implicit-floor oracle |

Canonical proof: research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md.
Sole stable owner: knowledge/FIXED_ORDER_THEORY.md.

## Commands and checks

All results below were freshly run locally in this task with the existing
Python 3.14.3 runtime. Each checker ran as its own process and exited 0.
The command-local Git option is safe.directory followed by the resolved
repository root, as in the source audit below; no persistent config changed.

| Exact command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime | other environments |
| `python -S -u ops/TASK-20260908__third_block_recovery/check_recovery.py` | 0; output below | rational gates, 632 floor cases, all cyclic cells and panels, mutations | imported minima, arbitrary implicit-floor decisions, all-m proof |
| `python -S -u ops/TASK-20260906__boundary_recovery/check_recovery.py` | 0; output below | unchanged two-block construction bookkeeping | independent mathematical acceptance |
| `python -S -u ops/TASK-20260908__third_adjacent_block/check_third_block.py` | 0; output below | target coupling's rational/marginal/branch checks | finite recovery or geometric transfer |
| `python -S -`, source audit below | 0; PASS output below | eight-path scope, tracked/untracked whitespace, imports, links, protected sources | external mathematical review |
| `git diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` with command-local prefix | 0; full tracked diff inspected | stable owner and current-state/priority delta | additions read separately in full |
| `git diff --check` and `git diff --cached --check` with same prefix | 0; no output at source audit | tracked/staged whitespace | untracked additions audited explicitly |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable local contracts | none |

New checker final output:

```text
EXACT half-wrap slack = 26541513/1000000000 > 0
PASS rational domain/onset gates; strict bracket floor ties; exact delta floors
PASS m=2..512 plus 13 declared sizes: 632 floor cases; 365867 cyclic cells
PASS 362724 nonexception panel bounds; all pairs, counts, parity and bijections
PASS all closed floor-box corners: coordinate constant 11; boundary-mass constant 13
PASS m=1; m=46 both widths; third lengths 0,2,4,6,8; both midpoint parities
PASS exact m=2000 floors (218,638,86,2); actual shared seam (2858,2943)
PASS 7 rejected mutations (including lost/duplicated second-third seam); 12 invalid inputs
NOTE: exact finite audit; implicit floors overcovered, minima imported, all-m proof separate; no radius transfer
```

The checker range was fixed before its first run: m=2..512 and
{1998,1999,2000,2001,2002,3998,3999,4000,4001,5999,6000,6001,8000}.
At each size it overcovers every strict-bracket floor triple and all closed
box corners. f is always computed by exact integer division, never from a
bracket or sampled constant. There are no random seeds, numerical roots,
floats, quadratures, unbounded enumeration or search for better parameters.
The first checker run also exited 0; after adding explicit assertions for
the uniquely determined m=2000 example it was rerun with the output above.
The added example is within the original predeclared range.

Fresh boundary-recovery checker output:

```text
EXACT half-wrap slack = 27541513/1000000000 > 0
PASS rational domain and small-case gates; strict-upper floor ties
PASS m=2..512: 587 floor triples; 157886 actual cyclic cells
PASS 155009 nonexception panel bounds; all exception pairs and counts
PASS all closed floor-box corners: coordinate and boundary-mass constants
PASS m=46 both d=0,2; m=100 example; 4 rejected mutations; 8 invalid inputs
NOTE: exact finite audit only; input minima and all-m weak proof are separate; no numerical diagnostics or radius transfer
```

Fresh third-continuous checker output:

```text
EXACT v lower > 9050867/25000000 > 0
EXACT A-3v-4delta > 1586317/100000000 > 0
EXACT a-v-delta > 1686317/300000000 > 0
EXACT b-v-delta > 526541513/1000000000 > 0
EXACT 3/2-M > 27041513/1000000000 > 0
PASS 8 endpoint partitions, 168 reflection moments, 24 full-max branch probes and 5 sign/tie controls
EXACT 8-panel raw full-max upper = -22276595597267606801027/800000000000000000000000000000000
PASS independent integral enclosure < -1/36000000000
PASS analytic pi<4 conversion: C_b-C_3 > 1/576000000000
NOTE: continuum proof and imported minima are separate; no finite recovery or radius/global transfer
```

The last output's scope refers to the prior checker/theorem. This task's
new theorem adds finite weak recovery only. No CI run or external review
is claimed. Skipped as inapplicable: production pytest, verify.py in both
modes, full-root/deletion diagnostics, finite searches and paper builds.
No production logic, finite certificate or publication asset is modified.

## Artifact and provenance checks

No generated result/certificate/publication asset. New proof/checker are
authored sources. The checker writes no files. The containing commit
identifies the integrated revision; exact input HEAD is recorded above.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md | bced795d2aa4be51eda168b8a62a6374d3fcc326e532e55fc81614e5086aa57a |
| ops/TASK-20260908__third_block_recovery/check_recovery.py | 6f0948b3ba110d5ae6438bcbe547b31adb28802a1d6c8c8e33b1e29150a5dac5 |

## Failed checks and negative evidence

Initial plain Git reads failed the ownership guard. Command-local
safe.directory resolved this; persistent Git configuration is unchanged.
Personal-ignore permission warnings did not prevent successful Git reads.
All mathematical checks passed. Deliberate negative controls are expected
rejections, not failed positive evidence. The full source display exceeded
the combined output budget once; the truncated middle of the new checker
was read separately, completing the inspection.

## Final diff inspection

The new proof and checker, three-file tracked diff and initial dossier were
read completely. The literal audit below passed before integration and is
repeated over the completed dossier before staging. It explicitly inspects
untracked additions, which ordinary git diff omits.

```python
from pathlib import Path
import ast, hashlib, re, subprocess
root = Path.cwd()
base = '6f86fd1a98e9eb56cfbc78bc6444d8f816167879'
git = ['git', '-c', 'safe.directory='+root.as_posix()]
def run(*args):
    r = subprocess.run(git+list(args), capture_output=True, text=True, encoding='utf-8')
    assert r.returncode == 0, (args, r.returncode, r.stderr)
    return r.stdout
task = 'ops/TASK-20260908__third_block_recovery/'
proof = 'research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md', proof}
allowed |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_recovery.py')}
assert run('rev-parse', 'HEAD').strip() == base
entries = run('status', '--porcelain=v1', '--untracked-files=all', '-z').split('\0')
assert {e[3:] for e in entries if e} == allowed
assert set(run('diff', base, '--name-only').splitlines()) <= allowed
assert run('diff', '--check') == ''
assert run('diff', '--cached', '--check') == ''
links = 0
for name in sorted(allowed):
    source = Path(name).read_text(encoding='utf-8')
    assert source.endswith('\n') and not source.endswith('\n\n'), name
    assert all(line == line.rstrip() for line in source.splitlines()), name
    assert all(ord(c) >= 32 or c in '\t\n' for c in source), name
    if name.endswith('.py'):
        tree = ast.parse(source, filename=name)
        compile(tree, name, 'exec')
        assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(tree))
        imports = [n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
        imports += [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
        assert imports == ['fractions', 'itertools'], imports
    if name == proof:
        for target in re.findall(r'\]\(([^)]+)\)', source):
            assert (Path(name).parent/target).is_file(), target
            links += 1
protected = [
    'AGENTS.md', 'PROJECT_KNOWLEDGE.md', 'RINGMIN_REVIEW_PROTOCOL.md',
    'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md', 'verify.py',
    'paper_assets/ringmin_paper.tex', 'README.md', 'REPORT.md',
    'research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md',
    'research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md',
    'research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md',
    'ops/TASK-20260906__boundary_recovery/check_recovery.py',
    'ops/TASK-20260908__third_adjacent_block/check_third_block.py']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'], owners
for name in (proof, task+'check_recovery.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 8 allowed paths; tracked/untracked whitespace; standalone AST, imports and no floats')
print(f'PASS {links} proof links; one owning ledger; {len(protected)} protected texts equal baseline')
print('PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta')
```

Material output after the two hashes recorded above:

```text
PASS 8 allowed paths; tracked/untracked whitespace; standalone AST, imports and no floats
PASS 5 proof links; one owning ledger; 14 protected texts equal baseline
PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta
```

Fourteen named protected texts were compared with the starting commit after
newline normalization. The complete path inventory also excludes changes
to all prior proofs/dossiers, paper_assets/, results/, src/, tests/, scripts/,
verify.py, other knowledge modules and publication metadata. Only
FIXED_ORDER_THEORY.md owns the new stable claim. The index and global
ledger remain unchanged. The completed dossier and integration diff are
inspected before commit; authorized integration uses existing origin/main.
The containing SHA, observed push result and final working-tree state
belong to the final handoff, without asserting mathematical acceptance.

The completed dossier was read in full and the literal audit rerun: exit 0
with identical source hashes and all PASS lines. The explicit eight-path
git add exited 0 with tool-granted escalation. The complete cached diff
was read in two bounded groups covering all eight paths. The cached
whitespace and unstaged diff checks produced no diff output; the source
audit separately enforces their exit codes before commit. The final small
status/evidence/log update records these facts and is inspected/restaged;
no proof or checker source changed after its final successful run.

## Residual uncertainty

Imported exact definitions/brackets remain premises; independent external
mathematical review is pending. Ambiguous implicit floors are overcovered,
not selected numerically. No R_full, full-root convergence, deletion, new
global bound or optimization of the third reflection is established.
