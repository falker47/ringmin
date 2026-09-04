# Evidence

## Environment

```text
repository_head=cf78a3b5d7334d3933b62988acae0f048f7b638f
platform=Windows PowerShell sandbox; AMD64
python=3.14.3 (MSC v.1944 64 bit)
pytest=9.0.2
numpy=2.4.3
scipy=1.17.1
mpmath=1.3.0
dependency_source=existing workspace environment; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| `176<T_{8,37}` and `T_{8,38}<176` | exact inequalities | positive sign gates and rational square margins | stdlib Fraction plus separate integer cross-products | imports the fixed-k physical minus-root formula |
| `R_{8,37}<176<R_{8,38}` | exact inequalities | all 30/31 edges; rational sine bounds; elementary arcsine bounds; exact pi comparison | independent rank/parity edges; integer/table scorer | adjacent-chain roots, not full-order radii |
| `s_8=38`; deficit positive through 37, negative from 38 | exact theorem / proved corollary | `research/RADIUS8_SEAM_ONSET.md`, sections 1-6 | mathematical deduction after all endpoint gates pass | imports fixed-k monotonicity and sign theorem; requires proof review |
| Normal and optimized checks agree | engineering fact | same rational output in both modes | no production/diagnostic import, site packages disabled | same Python stdlib and source |
| Targeted invalid witnesses rejected | engineering fact | 25 task-local tests in both modes | tests coupled to checker for rejection; separate integer scorer | targeted mutations are not exhaustive program verification |
| Repository regression suite passes | engineering fact | 12 passed, one cache warning | production-coupled local suite | neither a proof nor global-frontier verification |

The previous diagnostic selected `n=37,38` and `q=176`. No diagnostic
artifact, numerical root, residual, precision tolerance or finite scan is
used as a premise. The proof concerns only the formal Supnick seam.

## Commands and checks

All commands below were executed locally in this task from the repository
root. None is a copied historical/CI success claim. `-I -S` isolates the
checker from site packages and `PYTHONPATH`; `-B` avoids bytecode artifacts.

| Exact command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | interpreter availability | dependency compatibility |
| `python -I -S -B ops/TASK-20260904__radius8_seam_onset/check_seam.py` | 0; output below | four exact bridge gates, complete edges and analytic rational witnesses | imported all-n proof or global optimization |
| `python -I -S -O -B ops/TASK-20260904__radius8_seam_onset/check_seam.py` | 0; same output | gates survive optimization | independent Python implementation |
| `python -I -S -B ops/TASK-20260904__radius8_seam_onset/check_mutations.py` | first run 1, 25 tests/one parser failure; corrected run 0, 25 tests in 0.025s, `OK` | integer scorer, source independence, note tables, targeted rejection | exhaustive mutation coverage |
| `python -I -S -O -B ops/TASK-20260904__radius8_seam_onset/check_mutations.py` | 0; 25 tests in 0.020s, `OK` | same checks in optimized mode | all-n numerical enumeration |
| `python -B -m pytest` | 0; `12 passed, 1 warning in 30.49s` | existing repository regression suite | standalone frontier certification |
| External convention/provenance script reproduced below, piped to `python -B -` | 0; `production_conventions=PASS endpoints=2 conventions=2` | production Supnick/interleave edge agreement, environment and hashes | production-independent oracle (this one check is deliberately coupled) |

Exact checker output, identical in normal and optimized runs:

```text
threshold n=37 A=479/2664 B=9/296 A2-B=13657/7096896 H=10205/58608 square_margin=297431/3434897664
threshold n=38 A=1003/5624 B=83/2812 A2-B=72425/31629376 H=21363/123728 square_margin=4523113/15308617984
pi lower_witness=1231847548/392109375 lower_margin=3418213/41563593750
pi upper_witness=5277328977275528/1679825970703125 upper_margin=303439072246/239975138671875
chain n=37 edges=30 upper_half_sum=62794038854497/20000000000000 margin=1915940711659/1060000000000000
chain n=38 edges=31 lower_half_sum=16459/5000 margin=5213/35000
exact_bridge=PASS inequalities=4 cyclic_edges=61 symmetry_variants=122
corollary=s_8=38 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only
```

The task-local suite has 3 positive/source/table tests and 22 rejection tests
(including four invalid endpoint values within one test). Rejections cover
missing closure/interior edges, duplicate edges/vertices, a rewired complete
cycle, a missing parity edge, bounds on the wrong side of the sine,
a negative bound with the same square, an out-of-domain arcsine bound,
an invalid cubic coefficient/domain, both invalid pi comparisons, reversed
threshold direction, negative pre-square sign, nonpositive curvature,
negative `A` with the same square, equality, wrong separator and wrong
endpoint direction. Every rejection test checks the expected failure reason.

The integer scorer independently recomputes every `Q_e` and `M_e` in the
note. It checks the upper sum by integer cross-multiplication using
`40 D^2 sum(m_e)+7 sum(m_e^3)`, with denominator `40 D^3`, and the lower
sum using `sum(m_e)/D`. Its threshold comparison starts from the integer
common denominator `8n(n-1)`, separately from the checker's Fraction path.

The pytest warning was `PytestCacheWarning`: the sandbox account could not
write the existing `.pytest_cache/v/cache/nodeids`. The suite itself
completed. No test failure was hidden and no package was installed.

External convention/provenance command actually executed:

```powershell
@'
from pathlib import Path
import hashlib, importlib.util, platform, sys
from importlib.metadata import version
p=Path('ops/TASK-20260904__radius8_seam_onset')
spec=importlib.util.spec_from_file_location('r8',p/'check_seam.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
sys.path.insert(0,str(Path('src').resolve()))
from ringmin.patterns import supnick_max_tour, interleave
for n in (37,38):
    expected=m.cyclic_edges(m.rank_tour(n))
    for function in (supnick_max_tour,interleave):
        got=m.cyclic_edges(function(range(8,n+1)))
        if set(expected)!=set(got) or len(got)!=n-7:
            raise RuntimeError('production convention mismatch')
print('production_conventions=PASS endpoints=2 conventions=2')
print('python='+sys.version.replace('\n',' '))
print('platform='+platform.system()+' '+platform.machine())
for package in ('pytest','numpy','scipy','mpmath'):
    print(package+'='+version(package))
for file in (p/'check_seam.py',p/'check_mutations.py',Path('research/RADIUS8_SEAM_ONSET.md'),Path('research/FIXED_K_SUPNICK_SEAM.md'),Path('paper_assets/ringmin_paper.tex')):
    print(file.as_posix()+' sha256='+hashlib.sha256(file.read_bytes()).hexdigest())
'@ | python -B -
```

No `verify.py` run, frontier verification, artifact regeneration or paper
build was performed: their inputs/logic are unchanged and they do not
validate the new endpoint arithmetic. Hosted CI was not inspected. No
external continuous-review acceptance is claimed for the uncommitted delta.

## Artifact and provenance checks

No finite optimum/frontier or publication artifact is generated or changed.
Exact proof tables are task-local mathematical witnesses, not global-search
certificates. Inputs are fixed `k=8,n=37,38,q=176,D=10000`, with upper/lower
integer numerators stored in `check_seam.py`. No random seed, numerical
precision or nondeterministic operation is involved.

The task base is `cf78a3b5d7334d3933b62988acae0f048f7b638f`; it does not
contain the new uncommitted checker. The SHA-256 hashes identify the actual
source used:

| File | SHA-256 |
|---|---|
| `check_seam.py` in this dossier | `c5594774cec6c0ed209f979a21004e85fe285eea97010859abeb57f511523127` |
| `check_mutations.py` in this dossier | `19fc832647dbb358b4a71a6184d1dfcb15a1e8a256b92b8ec70b80bcb8a45fed` |
| `research/RADIUS8_SEAM_ONSET.md` | `bf0144be2ba47daae25a0f8123c9053e08a3c78d40d2699aca22181ae944bae6` |
| Imported `research/FIXED_K_SUPNICK_SEAM.md` | `24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71` |
| Protected `paper_assets/ringmin_paper.tex` | `5042d01b0f0f54ed3badeaa494cd24411aa58a2aa2c865b3f02abb27fcbcc60a` |

The note was authored with table markers, then populated with the following
exact command (exit 0, `proof_tables_written=61 exact_integer_rows`). The
final note has no markers. Reproduction without rewriting the note is
available through `check_seam.py --tables`; the successful table test audits
all final rows against the source and integer cross-products.

```powershell
@'
from pathlib import Path
import importlib.util
p=Path('ops/TASK-20260904__radius8_seam_onset/check_seam.py')
spec=importlib.util.spec_from_file_location('exact_bridge',p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
note=Path('research/RADIUS8_SEAM_ONSET.md')
s=note.read_text(encoding='utf-8')
for n,rows in ((37,m.UPPER_ROWS),(38,m.LOWER_ROWS)):
    marker='TABLE'+str(n)
    if s.count(marker)!=1: raise RuntimeError('table marker count')
    s=s.replace(marker,m.table_text(n,rows))
note.write_text(s,encoding='utf-8',newline='\n')
print('proof_tables_written=61 exact_integer_rows')
'@ | python -B -
```

The Fraction checker and integer scorer share the same witness numerators;
the integer scorer is an independent arithmetic path, not an independently
authored proof. The rank/parity reconstruction comparison supplies separate
coverage checks. The all-integer deduction is in the mathematical note.

## Failed checks and negative evidence

Initial `git status --short` failed on sandbox ownership. Subsequent read-only
Git sets `safe.directory` to the resolved repository root for each command
and uses `-c core.excludesfile=`. No persistent configuration change was needed.

The first mutation-suite run failed only in parsing the note's first table:
`AssertionError: 0 != 30`. The parser selected the subsequent text block
because it did not strip the leading newline. The fix uses
`block.lstrip("\n").split("\n\n", 1)[0]`. All 25 tests then passed in both
modes. The checker, mathematical constants and proof were not changed.

One documentation patch was rejected before application because it combined
delete/add operations on `CURRENT_STATUS.md` in a single patch. It was
reissued as separate supported file edits. This was a patch-format failure,
not an approval rejection, permission bypass or mathematical failure.

## Final diff inspection

The complete tracked diff and all six untracked additions were inspected in
full. The explicit nine-file audit below exited 0 before handoff and was
repeated after the final state/evidence edits. Its output is:

```text
format_scope_audit=PASS files=9 dossier_files=5 untracked=6 protected_changes=0 provenance_hashes=5
git_diff_check=PASS exit=0 output=empty HEAD=unchanged
```

The tracked changes are exactly `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`
and `research/NEXT_RESEARCH_STEPS.md`. The six additions are the radius-8
proof and the five dossier files. Each of the nine is UTF-8 without BOM,
LF-only, has exactly one final newline and no trailing whitespace or NUL.
The dossier contains no cache or other extra file. The five recorded source
hashes still match. Ordinary Git diff omits untracked files; the explicit
byte checks cover them too.

Protected tracked paths were checked through the complete delta against
HEAD: no change to prior proof notes/dossiers, `AGENTS.md`, `src/`, `tests/`,
`scripts/`, `results/`, `verify.py`, `paper_assets/`, `README.md`, `REPORT.md`,
dependency or CI files. No generated publication/certificate file changed.

Actual audit invocation (local engineering/scope check, not mathematical
verification):

```powershell
@'
from pathlib import Path
import hashlib, subprocess
p = Path('ops/TASK-20260904__radius8_seam_onset')
git = ['git', '-c', 'safe.directory='+Path.cwd().as_posix(), '-c', 'core.excludesfile=']
def run(*args):
    return subprocess.run(git+list(args), check=True, capture_output=True).stdout
tracked = {'CURRENT_STATUS.md', 'PROJECT_KNOWLEDGE.md', 'research/NEXT_RESEARCH_STEPS.md'}
expected = tracked | {'research/RADIUS8_SEAM_ONSET.md'}
expected |= {p.as_posix()+'/'+name for name in
             ('TASK_STATUS.md','TASK_LOG.md','EVIDENCE.md','check_seam.py','check_mutations.py')}
status = run('status','--porcelain=v1','--untracked-files=all').decode('utf-8')
actual = {line[3:] for line in status.splitlines()}
if actual != expected:
    raise RuntimeError(('unexpected scope', actual ^ expected))
if set(run('diff','HEAD','--name-only').decode('utf-8').splitlines()) != tracked:
    raise RuntimeError('protected tracked change')
if run('rev-parse','HEAD').decode().strip() != 'cf78a3b5d7334d3933b62988acae0f048f7b638f':
    raise RuntimeError('HEAD changed')
for name in sorted(expected):
    raw = Path(name).read_bytes()
    value = raw.decode('utf-8')
    if raw.startswith(b'\xef\xbb\xbf') or b'\r' in raw or b'\x00' in raw:
        raise RuntimeError(('encoding',name))
    if not raw.endswith(b'\n') or raw.endswith(b'\n\n'):
        raise RuntimeError(('final newline',name))
    if any(line.rstrip()!=line for line in value.splitlines()):
        raise RuntimeError(('trailing whitespace',name))
if len(list(p.iterdir())) != 5 or any(f.is_dir() for f in p.iterdir()):
    raise RuntimeError('unexpected dossier file/cache')
evidence = (p/'EVIDENCE.md').read_text(encoding='utf-8')
for file in (p/'check_seam.py',p/'check_mutations.py',Path('research/RADIUS8_SEAM_ONSET.md'),
             Path('research/FIXED_K_SUPNICK_SEAM.md'),Path('paper_assets/ringmin_paper.tex')):
    if hashlib.sha256(file.read_bytes()).hexdigest() not in evidence:
        raise RuntimeError(('provenance hash',str(file)))
if run('diff','--check'):
    raise RuntimeError('unexpected diff-check output')
print(status,end='')
print('format_scope_audit=PASS files=9 dossier_files=5 untracked=6 protected_changes=0 provenance_hashes=5')
print('git_diff_check=PASS exit=0 output=empty HEAD=unchanged')
'@ | python -B -
```

## Residual uncertainty

The exact endpoint gates close with strictly positive rational margins.
The imported fixed-`k` and Supnick proofs and the new analytic inequalities
still require independent mathematical review; passing code is not a proof
of every imported premise. No onset with `9<=k<4325` is newly classified.
This task does not certify full feasibility, global optima, contact graphs
or floating circles. Hosted CI and the full finite global verifier were
not run or claimed. No commit or GitHub write was made.

Exactly one proposed next atomic task after acceptance: a bounded STRICT
radius-9 two-precision diagnostic on `37..50` with independent edge
reconstruction. That task has not begun.
