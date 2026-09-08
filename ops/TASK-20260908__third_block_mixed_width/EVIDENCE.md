# Evidence

## Environment

    repository_head=b21c2dff20ca7419db56545c67386b369b8d24ac
    platform=Windows; PowerShell
    python=3.14.3
    dependency_source=standard library only; python -S
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Full mixed derivative, positive curvature, unique minimum | Exact continuous theorem | New proof Sections 2-4 | Analytic; no production dependency | Exact accepted inputs are premises |
| Rational width bracket | Exact continuous theorem with two rational gates | Proof Section 5 and standalone checker | Fraction arithmetic; no production/old-checker imports | Gates only; not a width scan or proof by sampling |
| Cost ordering and rational saving | Proved continuous corollary | Proof Section 6 | Analytic rational bounds | No finite recovery or geometric/global implication |
| Source protection and reproducibility | Engineering fact | Final source audit below | Local Git and stdlib checks | External review and hosted CI separate |

## Commands and checks

Startup Git reads used command-local safe.directory set to the resolved
repository root, as in the reproducible audit below. `rev-parse HEAD`,
`status --short`, `remote -v`, and `branch --show-current`
exited 0: exact requested SHA, clean tree, origin falker47/ringmin and main.
Ordinary Git first failed dubious ownership (exit 1); no persistent config
was changed. Successful reads emit a nonfatal personal-ignore permission warning.
`python -S --version` exited 0: `Python 3.14.3`.

All three following commands were independently run locally in this task,
each with exit 0. They use stdlib only and import no production module.
The prior width checker includes independent raw-integral enclosures; the
new checker and prior boundary checker perform rational sign gates only.
None is a finite geometric certificate or a hosted-CI result.

`python -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py`

```text
EXACT inherited epsilon slack = 431/32000000
EXACT lower residual = 1088173975683910831/2175907136349689169
EXACT lower signed square = -963745517404602389188679409068317/4734571866017504812540302482915910561 < 0
EXACT upper residual = 226493965596937/453065245150063
EXACT upper signed square = 34763358497298510706339907/205268116362886684743388903969 > 0
EXACT stationary upper slack = 35511/800000000
EXACT diagonal cutoff slack = 354539/3000000000
EXACT cost denominator slack = 24416513/1000000000
EXACT cost difference bracket = -2187/2048000000000 , -24389/72000000000000
EXACT saving over 1/250 > 12389/72000000000000
PASS two directed rational sign gates and positive pre-square residuals
PASS inherited bounds and analytic location/cost implications
NOTE: continuous proof supplies uniqueness; no finite recovery or geometric transfer
```

`python -S ops/TASK-20260908__third_block_width/check_width.py`

```text
EXACT a-v-D_g > 1986317/1200000000 > 0
EXACT b-v-D_g > 1045151441/2000000000 > 0
EXACT 3/2-M(D_g) > 100234467/4000000000 > 0
EXACT A-3v-4d_1 > 386317/100000000 > 0
EXACT a-v-d_1 > 786317/300000000 > 0
PASS 0<1/1000<1/250<D_g; uniform gate has strict actual sign at D_g
PASS 24 raw full-max/closed-cost and Leibniz/closed-derivative enclosures
PASS 120 new-slab reflection moments; 24 high partitions; 8 chain/tie endpoint controls
EXACT raw old-minus-new lower = 283676612415711588261712186381902839/160000000000000000000000000000000000000000000
PASS independent saving >1/576000000; cost saving >1/9216000000 via pi<4
PASS 5 radical sign/tie controls; zero inverse sine; 6 invalid inputs
NOTE: analytic proof supplies all-width signs; no refinement, recovery, radius/global transfer or hosted CI
```

`python -S ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py`

```text
EXACT lower residual = 10516971471577279/21018800219582721
EXACT lower signed square = -342531413518344092144807428477/441789962670730640526171361763841 < 0
EXACT upper residual = 251647560246539/503426690473461
EXACT upper signed square = 51974394530491111127115563/253438432681061908372345318521 > 0
EXACT location slack = 8431/32000000 > 0
PASS imported bracket order and two directed endpoint sign gates
PASS analytic distance-bound implication: 43/1000 < epsilon_b < 11/250
NOTE: continuum proof and imported minima are separate; no numerical root or integral is certified here
```

The full pytest suite, finite certificate verifier (including frontier),
finite recovery diagnostics and paper build were not run: no production,
certificate, finite-recovery or publication change is in scope. The proof
independently differentiates the full split cost twice, retains the nonzero
second-derivative switch term, and proves the uniform signs; the new
checker does not purport to test those continuum arguments by sampling.

## Artifact and provenance checks

Not applicable: no numerical result, finite certificate or publication
artifact is generated. The new proof and bounded checker are source files.
Their accepted mathematical input is the repository SHA above; all inherited
definitions and inequalities are linked explicitly in the proof.

## Failed checks and negative evidence

The all-chord formula has a strictly negative derivative, but continuation
as the full cost beyond tau_3 omits a positive chain contribution. The full
mixed derivative crosses zero exactly once; decreasing monotonicity on the
whole mixed interval is refuted analytically. No failed finite sign gate.
One documentation patch was rejected before application because it combined
delete/add operations on CURRENT_STATUS.md; retried as single-file edits.
No mathematical source or verification result was changed by that failure.

## Final diff inspection

Read the complete mathematical proof/checker, all three dossier files and
the complete tracked diff. The following literal audit was piped to
`python -S -` and exited 0. It explicitly inspects untracked additions,
which ordinary git diff omits.

```python
from pathlib import Path
import ast, hashlib, re, subprocess
root = Path.cwd()
base = 'b21c2dff20ca7419db56545c67386b369b8d24ac'
git = ['git', '-c', 'safe.directory='+root.as_posix()]
def run(*args):
    r = subprocess.run(git+list(args), capture_output=True, text=True, encoding='utf-8')
    assert r.returncode == 0, (args, r.returncode, r.stderr)
    return r.stdout
task = 'ops/TASK-20260908__third_block_mixed_width/'
proof = 'research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md', proof}
allowed |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_mixed_width.py')}
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
        assert not any(isinstance(n, (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)) for n in ast.walk(tree))
        imports = [n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
        imports += [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
        assert imports == ['fractions'], imports
        gates = [n for n in ast.walk(tree) if isinstance(n, ast.Call)
                 and isinstance(n.func, ast.Name) and n.func.id == 'endpoint_gate']
        assert len(gates) == 2
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
    'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md',
    'research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md',
    'research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md',
    'research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md',
    'research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md',
    'ops/TASK-20260908__third_block_width/check_width.py',
    'ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'], owners
for name in (proof, task+'check_mixed_width.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 8 allowed paths; tracked/untracked whitespace; standalone Fraction-only AST')
print('PASS exactly two endpoint gates; no floats, loops or comprehensions in checker')
print(f'PASS {links} proof links; sole owning ledger; {len(protected)} protected texts equal baseline')
print('PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta')
```

Exact output:

```text
SHA256 research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md 7e98610b45e029646ec7858a413e1cb7fce0dd1403f06a98bb22bfb90c4bd200
SHA256 ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py fd742d2586f64891b21648eceec45d714e3cd26d183f3353a4d07307b669600e
PASS 8 allowed paths; tracked/untracked whitespace; standalone Fraction-only AST
PASS exactly two endpoint gates; no floats, loops or comprehensions in checker
PASS 4 proof links; sole owning ledger; 17 protected texts equal baseline
PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta
```

The 17 named protected texts are compared after newline normalization.
The complete changed-path inventory additionally excludes every other
protected/derived path, including results/, src/, tests/, scripts/,
paper_assets/, prior dossiers and proof notes, other ledgers and CI.
PROJECT_KNOWLEDGE.md needs no change: scope, central guardrails and thematic
navigation are unchanged. No stable claim has a second thematic owner.

The full source audit is repeated on final records before staging exactly
these eight paths under the standing authorization. Inspect the complete
staged diff and its whitespace before normal commit/push to existing
origin/main. The final handoff records the actual containing commit,
push result and remaining working-tree state. No hosted CI is asserted.

The repeated audit exited 0 with unchanged mathematical-source hashes.
Explicit `git add --` of the eight allowed paths exited 0 with tool-granted
escalation under the standing authorization. The complete staged diff was
read in separate parts, with EVIDENCE.md reread alone after one aggregate
output was truncated. `git diff --cached --check` and `git diff --exit-code`
each exited 0 with no diff output; the former emitted the known nonfatal
personal-ignore warning. This final record-only update is inspected and
restaged, followed by whitespace and unstaged-difference checks, before
normal commit/push. No mathematical source changed after verification.

## Residual uncertainty

Exact parameter definitions and their accepted theorem bounds are imported,
not reoptimized or independently re-proved. All continuum quantifiers come
from the analytic proof. The checker supplies only bounded rational signs.
No finite recovery, R_full transfer, new global limsup coefficient, finite
certification or paper revision. External mathematical review and hosted
CI remain separate; neither is claimed here.
