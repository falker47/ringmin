# Evidence

## Environment

    repository_head=ea35045da1032e64a6e7712d082b00fa30e8cb57
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing Python; stdlib only, python -S
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Exact baseline parameters and brackets | imported exact theorems | boundary-minimum Sections 1, 6; boundary measure equation (4) | not re-proved here | no refined bracket or midpoint parameter |
| Probability coupling, endpoint contact, marginals and local balance | exact continuous theorem | new proof Section 3, arbitrary continuous tests | direct change of variable | not a finite recoverability theorem |
| Coordinate and full-max branch domain | exact continuous theorem with rational gates | new proof Sections 2, 4; Fraction checker | no production or prior-checker imports | fixed third width/start and accepted box |
| Centered identity and C_b-C_3>1/576000000000 | exact continuous theorem / rational strict saving | new proof Section 5 | analytic identity; independent raw-cost enclosure | no radius/global implication |
| Corner moments, endpoint partitions and branch probes | exact finite arithmetic checks | 8 corners, 168 moments, 24 branch probes | stdlib exact rational calculations | these probes do not prove continuum quantifiers |
| Eight-panel integral upper enclosure | rigorous rational integral bound | concavity and monotonicity in proof Section 6; literal full-max scorer | different calculation from centered identity | imported branch proof required |
| Path, import, whitespace and protection checks | engineering facts | source audit below | Git baseline comparison | local; no hosted CI |

Canonical proof: research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md.
Sole stable owner: knowledge/FIXED_ORDER_THEORY.md.

## Commands and checks

All results below were freshly run locally in this task. Git uses the
command-local argument safe.directory derived from the repository root,
as in the literal audit below; no persistent configuration changed.

| Exact command / Git argv after that prefix | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime | other environments |
| `python -S -u ops/TASK-20260908__third_adjacent_block/check_third_block.py` | 0; exact output below | domain, branches, endpoint/marginal probes and integral enclosure | imported minima; finite recovery; external acceptance |
| `python -S -u ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py` | 0; PASS output below | accepted width bracket's rational entry/distance gates | imported minima and analytic curvature |
| `python -S -u ops/TASK-20260906__second_block_start_domain/check_domain.py` | 0; three positive rational margins below | baseline domain | analytic continuous sign theorem |
| `python -S -`, source audit below | 0; three PASS lines below | eight-path scope, imports, links, whitespace and protected texts | external mathematical review |
| `diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` | 0; complete tracked diff read | sole owner and current-state/priority delta | new files inspected separately in full |
| `diff --check` and `diff --cached --check` | 0; no output at source audit | tracked/staged whitespace | untracked additions explicitly audited too |
| `status --porcelain=v1 --untracked-files=all -z` | 0; exactly eight authorized paths | scope and inventory | ignored-file content |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable contracts | none |

The prior boundary and domain commands were initially run sequentially in
one PowerShell call, ending with exit 0. Their complete fresh output was
inspected, including all PASS lines and no exception; the final shell exit
belongs to the domain command. The boundary checker was then rerun alone:
exit 0 with identical output, separately confirming its process result.

New checker output:

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

The proof supplies the universal measure identities and branch reduction.
The numerical budgets were fixed in the authored checker before its first
run: eight bracket corners, degrees 0 through 6, endpoints/midpoint, five
sign/tie controls, eight quadrature panels and rational root denominator
10^30. There are no floats, numerical root refinements, random seeds,
parameter scans, optimizers or diagnostic decimals. The bound is certified
by rational rounding, concavity and monotonicity; it is not a sampled sign.

Fresh prior boundary checker output:

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

Fresh prior domain checker output:

```text
EXACT lambda > 7975867/25000000 > 0
EXACT a-lambda > 15186317/300000000 > 0
EXACT b-a > 13023/25000 > 0
PASS imported bracket order and three baseline-admissibility margins
NOTE: no radical/root gates remain; continuum sign, switches and infimum reduction are proved analytically
```

Skipped as inapplicable: production pytest, verify.py in either mode,
finite recovery/full-root checkers, numerical minimizer diagnostics,
finite searches, publication builds and hosted CI. The task changes no
production logic, finite certificate, historical proof or publication asset.

## Artifact and provenance checks

No finite result, certificate, permutation, publication or generated asset
is created. These are authored proof/check sources and task records.
The checker writes no files. The containing commit identifies the integrated
revision; the exact input commit is recorded above.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md | 8b7db9094532d52bc929b571c07696435b35d9a2182e8b1accf804d070cf4a72 |
| ops/TASK-20260908__third_adjacent_block/check_third_block.py | eb0eb9d8e7f83ec861da60213379065f879359c75ea0776edc92e1a34c84846c |

## Failed checks and negative evidence

- Initial Git reads failed the ownership guard; command-local safe.directory
  resolved it. Personal-ignore permission warnings do not change the successful
  status result. The attempted NUL exclude override failed and was abandoned.
- An apply_patch request containing delete/add operations for CURRENT_STATUS.md
  was rejected as duplicate targets before making changes. The unchanged diff
  was checked; ordinary updates then succeeded. No unrelated path was touched.
- The first evidence writer warned about an invalid escape in its embedded
  audit source. Rewriting with a raw string preserved all literal escapes;
  the corrected evidence is checked by the final source audit.
- All mathematical checks passed on their first run. No claimed improvement
  relies on dropping a max branch or continuing a finite-width asymptotic.
  No finite or geometric extension was attempted.

## Final diff inspection

The new proof and checker were read in full; the complete three-file tracked
diff was inspected. The literal source audit below exited 0, checking every
new untracked source directly for whitespace, as ordinary git diff omits it.

```python
from pathlib import Path
import ast, hashlib, re, subprocess

root = Path.cwd()
base = 'ea35045da1032e64a6e7712d082b00fa30e8cb57'
git = ['git', '-c', 'safe.directory='+root.as_posix()]

def run(*args):
    r = subprocess.run(git+list(args), capture_output=True, text=True, encoding='utf-8')
    assert r.returncode == 0, (args, r.returncode, r.stderr)
    return r.stdout

task = 'ops/TASK-20260908__third_adjacent_block/'
proof = 'research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md', proof}
allowed |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md',
                            'check_third_block.py')}
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
        assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float)
                       for n in ast.walk(tree))
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
    'research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md',
    'research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md',
    'ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py',
    'ops/TASK-20260906__second_block_start_domain/check_domain.py']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'], owners
for name in (proof, task+'check_third_block.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 8 allowed paths; tracked/untracked whitespace; standalone checker AST, imports and no floats')
print(f'PASS {links} proof links; one owning ledger; {len(protected)} protected texts equal baseline')
print('PASS tracked and staged diff whitespace; unchanged HEAD; no protected or generated path in delta')
```

Material audit output, after the two hashes recorded above:

```text
PASS 8 allowed paths; tracked/untracked whitespace; standalone checker AST, imports and no floats
PASS 5 proof links; one owning ledger; 15 protected texts equal baseline
PASS tracked and staged diff whitespace; unchanged HEAD; no protected or generated path in delta
```

The 15 named protected texts were compared with the starting commit after
newline normalization. The complete path inventory additionally excludes
changes to all earlier proofs/dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, other knowledge modules and publication metadata.
Only FIXED_ORDER_THEORY.md owns the new stable claim; the global ledger
and compact index remain unchanged.

The final completed dossier and status are inspected and the audit repeated
before staging. Section 3 of AGENTS.md authorizes staging these eight paths,
inspecting the complete cached diff and its whitespace, committing and
normally pushing to existing origin/main. The final handoff records the
observed containing SHA, push result and remaining tree state. These Git
actions do not assert mathematical acceptance or hosted CI success.

The completed dossier/current status were read in full and the source audit
rerun: exit 0, identical proof/checker hashes and all PASS lines. The explicit
eight-path git add exited 0 with tool-granted escalation. The full cached
diff was inspected; a separate cached TASK_LOG.md read recovered a truncated
display segment. Both diff --cached --check and diff --exit-code exited 0,
with no diff output. This small final status/evidence/log update is inspected
and restaged before the commit; no mathematical source changed after its audit.

## Residual uncertainty

The continuous question is resolved by an analytic proof with exact rational
gates and an independent integral enclosure, subject to external mathematical
review. Baseline definitions and brackets are imported exact premises.
No finite recovery, R_full transfer, new global bound, finite-n comparison,
parameter optimization or general coupling optimum is proved.
Exactly one next atomic task: independently review this continuous theorem
and its bounded checks, stopping before recovery or geometric transfer.
