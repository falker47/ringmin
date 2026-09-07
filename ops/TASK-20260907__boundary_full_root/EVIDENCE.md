# Evidence

## Environment

    repository_head=e64c627b7e07da63ae0290d5b63c8258582471c7
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing Python; stdlib exact audit; mpmath 1.3.0 diagnostics
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Exact parameters and weak recovery | imported exact theorems | prior linked notes; fresh bounded gate reruns | input minima not re-proved | exact specified family |
| Full-root identity and all-pairs witness | exact theorem | new proof Sections 2-3 | analytic specialization of arbitrary-high criterion | fixed order |
| Uniform cost/radius errors and odd limit | exact theorem | new proof Sections 4-5, 8 | full-max estimates and separate necessary-cell squeeze | sufficient constants |
| C_b<C_2 and global limsup | proved corollaries | new proof Sections 6-9; boundary/start theorems and rational gates | no quadrature premise | no global optimality |
| Bounded arithmetic checks | exact finite arithmetic audit | check_full_root.py | no production/prior-checker imports; list versus formula; sine algebra versus atan intervals | prescribed finite sizes |
| Numerical geometry and costs | numerical observations | diagnose_full_root.py | alternate angle, Cartesian distances and all-pairs difference-constraint solver | not certificates |

Canonical proof: research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md.
Fixed-order definitions/results/comparisons have one owner in the fixed-order
ledger; the global limsup consequence has one owner in the global ledger.
PROJECT_KNOWLEDGE.md needs no navigation or central-guardrail change.

## Commands and checks

All following checks were freshly run LOCALLY. Hosted CI and external
mathematical review were not run. Older dossier outputs are not new evidence.
Git reads use command-local safe.directory, without changing configuration.

- `python --version`: exit 0, Python 3.14.3.
- `python -c "import mpmath, scipy; print('mpmath', mpmath.__version__); print('scipy', scipy.__version__)"`:
  exit 0, mpmath 1.3.0 and SciPy 1.17.1. SciPy is not used by the checks.
- `python -S ops/TASK-20260907__boundary_full_root/check_full_root.py`:
  exit 0. Complete material stdout:

```text
EXACT comparison gates: 42554539/3000000000 793/30000 19854539/3000000000
EXACT gamma = 42554539/303864862158400000 ; C_2-C_b > 7*gamma/88 = 297881773/26740107869939200000
PASS exact domain, entry, shell, Lipschitz, max/tie, score/root and deletion gates
PASS 38 floor triples; 14091 actual cells; 56364 rational branch signs; 213 independent angle/full-max enclosures
PASS 28030 disjoint retained odd gaps; all small cycles and both m=46 floors
PASS 8 complete-score and two-cell deletion interval bounds at c=1/32,1/2
PASS wrong shared predecessor, cyclic predecessor, union reflection and single-branch mutations detected; 4 invalid inputs rejected
NOTE: exact finite arithmetic audits; analytic all-m proofs and imported minima remain separate
```

The 31 sizes are m=2..16,32,45,46,47,91,92,93,99,100,101,199,200,201,
2047,2048,2049. Every triple compatible with the strict alpha/lambda/epsilon
brackets is covered, including both d=0,2 at m=46; independent correlations
are ignored only to enlarge the audit. All cells are scored at rational
R=1,m^2/8,m^2/2,2*m^2 with sign-safe chain/chord algebra.
Every m<=6 cell and the seams/selected block positions at larger sizes
receive independent half-angle arctangent enclosures. Outward rounding
uses a 10^-24 grid and a 32-term alternating series with signed remainder.
Eight complete-score checks at m=32,46,47 use c=1/32,1/2.
These computations audit the analytic constants and finite construction;
they neither decide the exact minimizer floors nor prove the all-m theorem.

- `python -S ops/TASK-20260906__boundary_recovery/check_recovery.py`:
  exit 0, exact half-wrap slack 27541513/1000000000; 587 compatible
  floor triples for m=2..512, 157886 cells, 155009 panel comparisons,
  all floor-box corners, both m=46 cases, four mutations and eight invalid
  inputs pass. This independently reruns the original recovery bookkeeping.
- `python -S ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py`:
  exit 0. Directed signed squares are
  -342531413518344092144807428477/441789962670730640526171361763841
  and 51974394530491111127115563/253438432681061908372345318521;
  pre-square residuals are positive and location slack is 8431/32000000.
  Both endpoint gates and the analytic distance-bound implication pass.
- `python -S ops/TASK-20260906__second_block_start_domain/check_domain.py`:
  exit 0. Positive margins printed are 7975867/25000000 for lambda,
  15186317/300000000 for a-lambda and 13023/25000 for b-a.
  No radical/root gate or domain scan is used by that analytic theorem.
- `python ops/TASK-20260907__boundary_full_root/diagnose_full_root.py`:
  final exit 0 at 60 decimal digits, after the diagnostic correction
  recorded below. Complete material stdout:

```text
PASS recomputed exact-family equations; full-max identity/split <1e-38; mixed branch and chord-only mutation; stationary residual <1e-22
DIAGNOSTIC x_star 0.287630802860637660350656
DIAGNOSTIC alpha_hat 0.109303696326414774245232
DIAGNOSTIC lambda 0.319069912790639673125505
DIAGNOSTIC epsilon_b 0.0434917480060125959004859
DIAGNOSTIC chain_interval_length 0.0000924172983369619330081206
DIAGNOSTIC D_b_min -0.00000235526264033607323443523
DIAGNOSTIC C_b 0.141913303918715098691458
DIAGNOSTIC C_2-C_b 0.000000185135400110487492214551
DIAGNOSTIC finite m= 2 floors= (0, 0, 0) rho/(2m)^2= 0.05277834934755347527
DIAGNOSTIC finite m= 46 floors= (5, 14, 2) rho/(2m)^2= 0.137039544764844791
DIAGNOSTIC finite m= 100 floors= (10, 30, 4) rho/(2m)^2= 0.1396434600458969767
DIAGNOSTIC finite m= 256 floors= (27, 80, 10) rho/(2m)^2= 0.1410211872801416257
PASS 18 finite roots/cost recovery; 104779 even/deleted-odd pair checks in both directions and Cartesian coordinates; min slack= -2.3498e-57
PASS 7 independent all-pairs even root +/- probes and odd STN roots with separate lower squeeze
PASS m=2048 compact brackets, complete uniform score/root bounds and two-cell omission bounds
DIAGNOSTIC m=2048 rho/(2m)^2= 0.1418012768915905268431 tau/(2m)^2= 0.1416089751721931320803
NOTE: 60-digit mpmath 1.3.0 ; numerical observations, not certificates or exact parameter definitions
```

The 18 finite-root sizes are m=2..12,32,45,46,47,92,100,256.
At m<=100 both directed angular separations and Cartesian non-overlap are
checked at the upper numerical root endpoint, also after deleting 2m;
m<=6 additionally checks three allocations of each cell's excess.
Geometry tolerance is 10^-35. All-pairs difference constraints, built
without cell maxima and solved by Bellman-Ford using the alternate angle,
test the even root at relative +/-10^-12 for m=2..8 and compute odd roots
by 100 bisections. Their odd lower comparison uses the independently
necessary retained cells; the odd solver never invokes alternating sufficiency.
Difference-constraint relaxation tolerance is 10^-48; odd squeeze diagnostic
tolerance is 10^-25. The defining parameter and ordinary even-root bisections
use 140 steps. At m=2048 secant roots are checked on both sides at relative
10^-30; uniform score bounds are probed at c=1/32,C_b,1/2.
All diagnostic floors are floating observations; the exact checker overcovers
every bracket-compatible choice. No printed decimal is a proof premise.

No production test suite, frontier verifier or paper build was run: this
task changes no production code, certificate/pruning logic or publication
asset. The standalone proof audits and independent geometry solver target
the actual delta. They do not extend the finite certified global scope.

## Artifact and provenance checks

No certificate or publication artifact was generated. Checkers write only
stdout, with fixed sizes and no randomness. The input snapshot is the base
SHA above; the containing task commit identifies the final source.
The source audit below prints SHA256 for the proof and two new checkers.
No numerical JSON/CSV, parameter replacement or large experiment is added.

## Failed checks and negative evidence

The first numerical run exited 1 at the alpha-root sign bracket.
The independent diagnostic transcribed the chord term of K' as a/4;
differentiating its defining integral gives a/2. That single diagnostic
term was corrected and the complete diagnostic rerun passed. No analytic
claim or exact gate used the failed run. The full-max diagnostic also
rejects a chord-only replacement of the new reflected block.

Startup read failures (Git ownership and guessed filenames) were resolved
without changes to configuration or protected sources. A combined patch
was rejected because it tried delete/add on CURRENT_STATUS.md in one
transaction; it applied no changes. The replacement was issued as an update.

## Final diff inspection

The following bounded source audit is run from the repository root as
`python -S -` with the code supplied on stdin. It checks all ten task
paths, explicit untracked whitespace, import independence, links, ownership
and 13 protected texts against the base SHA. The complete path inventory
also excludes incidental changes elsewhere, including generated assets.

```python
from pathlib import Path
import ast, hashlib, re, subprocess

base = 'e64c627b7e07da63ae0290d5b63c8258582471c7'
git = ['git', '-c', 'safe.directory='+Path.cwd().as_posix()]
def run(*args):
    return subprocess.run(git+list(args), check=True, capture_output=True,
                          text=True, encoding='utf-8').stdout
task = 'ops/TASK-20260907__boundary_full_root/'
proof = 'research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md'
expected = {proof, 'CURRENT_STATUS.md', 'research/NEXT_RESEARCH_STEPS.md',
            'knowledge/FIXED_ORDER_THEORY.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md'}
expected |= {task+n for n in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md',
                              'check_full_root.py', 'diagnose_full_root.py')}
changed = set(run('diff', '--name-only', base).splitlines())
changed |= set(run('ls-files', '--others', '--exclude-standard').splitlines())
assert changed == expected, changed ^ expected
for name in sorted(expected):
    body = Path(name).read_text(encoding='utf-8')
    assert body.endswith('\n') and '\x00' not in body
    assert all(line == line.rstrip() for line in body.splitlines()), name
for filename, allowed in [('check_full_root.py', {'fractions', 'math'}),
                          ('diagnose_full_root.py', {'mpmath'})]:
    name = task+filename
    tree = ast.parse(Path(name).read_text(encoding='utf-8'))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(n.name for n in node.names)
        if isinstance(node, ast.ImportFrom):
            imported.add(node.module)
    assert imported == allowed
    compile(tree, name, 'exec')
    if filename == 'check_full_root.py':
        assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float)
                       for n in ast.walk(tree))
links = re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', Path(proof).read_text(encoding='utf-8'))
for link in links:
    assert (Path(proof).parent/link).is_file(), link
fixed = Path('knowledge/FIXED_ORDER_THEORY.md').read_text(encoding='utf-8')
glob = Path('knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md').read_text(encoding='utf-8')
assert fixed.count('### Boundary recovery: exact full root, uniform limit and odd lower squeeze') == 1
assert glob.count('### Boundary full-root transfer: improved global upper bound') == 1
assert 'D_b(epsilon_b)/(4*pi)' not in glob
entry = fixed.split('### Boundary recovery: exact full root, uniform limit and odd lower squeeze')[1]
entry = entry.split('## Conjectural global interpretation')[0]
assert 'limsup' not in entry
protected = ['AGENTS.md', 'PROJECT_KNOWLEDGE.md', 'RINGMIN_REVIEW_PROTOCOL.md',
             'research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md',
             'research/PERMUTED_ALTERNATING_HALVES.md',
             'research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md',
             'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md',
             'research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md',
             'research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md',
             'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md',
             'src/ringmin/evaluator.py', 'verify.py', 'paper_assets/ringmin_paper.tex']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
run('diff', '--check')
assert run('rev-parse', 'HEAD').strip() == base
for name in (proof, task+'check_full_root.py', task+'diagnose_full_root.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 10-path source audit; tracked/untracked whitespace; checker AST/import independence')
print('PASS', len(links), 'proof links; separate claim owners;', len(protected), 'protected texts equal baseline')
print('PASS git diff --check; unchanged baseline HEAD; complete expected path inventory')
```

After the final proof/source review, this audit exited 0 with:

```text
SHA256 research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md b30168d6cc0d9f9634194beba34280241a71ea33b791124ccbebcb23461ac53c
SHA256 ops/TASK-20260907__boundary_full_root/check_full_root.py 51319cd326a0b1a339de4a22f092494f29d72af541e9049f5b55dc2c4cb1b8e5
SHA256 ops/TASK-20260907__boundary_full_root/diagnose_full_root.py c77d5695a8279b3f4a6deda16160364e4fb8df5de2b01ddfcb952df24958ba72
PASS 10-path source audit; tracked/untracked whitespace; checker AST/import independence
PASS 8 proof links; separate claim owners; 13 protected texts equal baseline
PASS git diff --check; unchanged baseline HEAD; complete expected path inventory
```

The complete tracked diff and all six untracked additions were read directly,
including every proof section, both complete checkers and all dossier files.
Only the four intended existing documents have tracked changes; all previous
proofs/dossiers, other ledgers, publication assets, certificates, production,
tests, scripts, verifier and repository contract/index remain unchanged.
State is READY_FOR_REVIEW. Staging is limited to these ten paths; the full
cached diff, cached whitespace and index/worktree equality are checked before
normal commit/push to existing origin/main under AGENTS.md Section 3.
Integration does not imply acceptance. The containing SHA and observed push
and clean-tree results are reported in the final user handoff.

### Staged verification

The explicit ten-path git add exited 0 with tool-granted access to the
protected index. The cached diff was inspected by source/document groups;
an initially truncated combined display was supplemented by separate full
proof/ledger reads and the missing diagnostic/evidence slices.

With the same command-local Git prefix, these commands each exited 0:

```text
git diff --cached --check
git diff --exit-code
git status --short --untracked-files=all
```

The first two produced no diff output. Status listed exactly four modified
documents and six added task paths, all staged, with no unstaged or
untracked path. Status/log/evidence then recorded these completed gates;
only those reviewed metadata changes are restaged before integration.
The recorded source audit is rerun and the staged texts are compared
against all ten inspected working files before commit.

## Residual uncertainty

All-m conclusions rely on the analytic proofs and their imported inputs.
Finite checks cannot replace them. No global optimum, global normalized
limit, finite improvement cutoff, external mathematical acceptance or
hosted CI result is claimed. Published arXiv-v1 assets remain historical.
