# Evidence

## Environment

    repository_head=cc35e14418362a38dee110c92ee4de4b607823a6
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing runtime; stdlib only with python -S
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Fixed input definitions and brackets | imported exact theorems | boundary-minimum Sections 1, 6 and boundary measure equation (4) | not re-proved here | no new parameter enclosure |
| All-width domain and marginal preservation | exact continuous theorem | new proof Sections 2-3 | direct rational inequalities and arbitrary-test substitution | not finite recoverability |
| Exact cost, derivative and strict decrease | exact continuous theorem | new proof Sections 3-4 | analytic integration and scaled deficit; separate raw integral checks | full-max chord domain only |
| First switch tau_3 and mixed correction | exact continuous theorem | new proof Section 3, unsquared monotone endpoint equation | analytic uniqueness and branch partition | no minimum or derivative sign after entry claimed |
| Delta=1/250 improvement | exact continuous theorem / explicit rational saving | new proof Section 5 and independent raw integral enclosure | raw quadrature does not use centered saving bound | no new geometric/global transfer |
| Bounded checker probes | exact rational finite checks and rigorous enclosures | output below | no production or prior-checker imports | supplement, not replace, all-width proofs |
| Source and protection audit | engineering fact | final audit below | baseline Git comparison | local; not hosted CI or external acceptance |

Canonical proof: research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md.
Sole stable owner: knowledge/FIXED_ORDER_THEORY.md.

## Commands and checks

All listed mathematical checks were freshly run locally in this task,
each as a separate process. Git commands use command-local safe.directory;
the literal source audit below derives that argument from Path.cwd().
No persistent Git configuration changed.

| Exact command or Git arguments after that prefix | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | local runtime | other machines |
| `python -S -u ops/TASK-20260908__third_block_width/check_width.py` | 0; complete output below | new gates, raw/closed cost and derivative, independent saving and controls | imported minima or finite/global transfer |
| `python -S -u ops/TASK-20260908__third_adjacent_block/check_third_block.py` | 0; output below | unchanged width-1/1000 baseline | variable-width theorem by itself |
| `python -S -u ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py` | 0; output below | accepted epsilon bracket's rational gates | imported alpha/x minima or analytic curvature |
| `status --short`, `rev-parse HEAD`, `remote -v`, `branch --show-current` | 0; clean, requested HEAD, existing origin, main | starting scope and integration target | hosted CI |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable repository contracts | mathematical correctness |

New checker output:

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

The fixed budgets are eight parameter corners, the three widths
1/1000, 1/250 and D_g, 16 quadrature panels, five moment degrees and eight
inverse-sine terms. The positive inverse-sine series is obtained by
integrating the binomial series of (1-q^2)^(-1/2); successive term ratios
are q^2*(2*j+1)^2/[2*(j+1)*(2*j+3)]<q^2. The next term divided by
1-q^2 bounds the tail. Square-root intervals use denominator 10^40 and
are checked by exact squaring. Trapezoid/midpoint and monotone rectangle
directions are justified analytically in the proof, as is the B-corner
comparison. No statistical extrapolation, float tolerance, seed,
minimizer computation, width scan or numerical root for tau_3 is used.

Fresh baseline checker output:

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

Fresh boundary-minimum checker output:

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

Skipped as inapplicable: production pytest; either mode of verify.py;
finite recovery/full-root checkers; parameter diagnostics; finite search;
publication builds; hosted CI. No production, finite certificate, finite
recovery or publication source is modified. No hosted run is called green.

## Artifact and provenance checks

No result artifact, certificate or generated/publication asset was created.
Authored proof/check sources and task records only. The checker writes no
files. Input commit is recorded above; the containing commit identifies
the integrated revision. SHA256 of the inspected local source bytes:

| Source | SHA256 |
|---|---|
| research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md | ed22cefb86784bd253a6a153062740486db07d4f6520188d565aa10d09ad304f |
| ops/TASK-20260908__third_block_width/check_width.py | db3042a2f4cd25517448e59d02799bc38baa060c6a53c3b87ff66589174365bd |

## Failed checks and negative evidence

- Ordinary initial Git reads failed ownership validation, exit 1.
  Command-local safe.directory resolved it; personal-ignore permission
  warnings accompany successful Git reads and do not conceal a dirty tree.
- The first checker run passed every mathematical gate. Its exact output
  exposed a manually transcribed b-v-D_g margin in the draft proof;
  corrected to 1045151441/2000000000 before final review.
- At Delta=h the reflected endpoint is strictly chain and the removed
  diagonal ties, at every checked corner. Analytic equation (12) identifies
  the earlier first switch tau_3; the chord expression cannot be extended
  to a positive chain interval. This is not a demonstrated sign reversal.

## Final diff inspection

Read the complete three-file tracked diff and the new proof, checker and
dossier sources in full. The following literal audit was piped to
`python -S -`; exit 0. It includes explicit whitespace checks on every
untracked addition, which ordinary git diff omits.

```python
from pathlib import Path
import ast, hashlib, re, subprocess
root = Path.cwd()
base = 'cc35e14418362a38dee110c92ee4de4b607823a6'
git = ['git', '-c', 'safe.directory='+root.as_posix()]
def run(*args):
    r = subprocess.run(git+list(args), capture_output=True, text=True, encoding='utf-8')
    assert r.returncode == 0, (args, r.returncode, r.stderr)
    return r.stdout
task = 'ops/TASK-20260908__third_block_width/'
proof = 'research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md', proof}
allowed |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_width.py')}
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
        assert imports == ['fractions', 'itertools', 'math'], imports
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
    'research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md',
    'research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md',
    'ops/TASK-20260908__third_adjacent_block/check_third_block.py',
    'ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'], owners
for name in (proof, task+'check_width.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 8 allowed paths; tracked/untracked whitespace; standalone AST/imports and no floats')
print(f'PASS {links} proof links; sole owning ledger; {len(protected)} protected texts equal baseline')
print('PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta')
```

Material output, after the two SHA256 lines above:

```text
PASS 8 allowed paths; tracked/untracked whitespace; standalone AST/imports and no floats
PASS 5 proof links; sole owning ledger; 16 protected texts equal baseline
PASS tracked/staged whitespace; unchanged HEAD; no protected/generated path in delta
```

The audit compares 16 named protected texts after newline normalization;
the complete changed-path inventory additionally excludes every other
previous proof/dossier, paper_assets/, results/, src/, tests/, scripts/,
other ledger, publication and CI path. PROJECT_KNOWLEDGE.md needs no change
because scope, central guardrails and thematic navigation are unchanged.
The global ledger has no new claim or modification.

All source and whitespace checks are local engineering evidence, separate
from the mathematical proof and from external acceptance. After recording
these final status/evidence/log updates, repeat the source audit, stage
only the eight inspected paths, inspect the complete staged diff and its
whitespace, commit and push normally to existing origin/main under Section 3
of AGENTS.md. The final handoff records the actual SHA, push and tree.

The repeated source audit exited 0 with unchanged proof/checker hashes.
Explicit `git add --` of the eight allowed paths exited 0 with tool-granted
escalation. The complete cached diff was inspected in two nontruncated
parts: proof/checker, then the other six paths. `git diff --cached --check`
and `git diff --exit-code` each exited 0 with no diff output; the former
also emitted the known personal-ignore warning. This final record-only
update is inspected, restaged and whitespace-checked before committing.

## Residual uncertainty

Exact parameters and their accepted brackets are imported premises;
external mathematical acceptance remains separate. Bounded rational probes
do not establish universal quantifiers, which are proved analytically.
No third-width minimizer or monotonicity beyond tau_3 is claimed.
No finite recovery, full-root transfer or global bound at the larger width
is supplied. The existing global coefficient stays C_3(1/1000).
Exactly one next atomic task: independently review this continuous theorem
and checker, stopping before finite or geometric transfer.
