# Evidence

## Environment

    repository_head=648a8eae98c987dbcc11aa28fdcf55cb946d0ef8
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing Python installation; mpmath 1.3.0 for diagnostics only
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Baseline x_* and alpha_hat definitions and uniqueness | imported exact theorems | linked prefix/alpha notes | not re-proved here | coarse brackets imported |
| Full-max formulas and all endpoints; C^1 but not C^2 at entry | exact continuous theorem | proof Sections 2-4 | direct analytic derivation | stated chord-diagonal domain |
| Unique attained mixed minimum and endpoint/zero classification | exact continuous theorem | analytic curvature and endpoint bounds, Sections 4-5 | no numerical gates needed | this continuous family only |
| 43/1000<epsilon_b<11/250 | exact continuous theorem with rational gates | two entry comparisons and analytic distance bound, Section 6 | Fraction-only standalone checker | relies on imported baseline brackets |
| Joint infimum value and closed-triangle minimum | proved continuous corollary | prior start monotonicity plus this width theorem | analytic composition | no finite or geometric transfer |
| Printed digits and sampled formula checks | numerical observations | diagnose_boundary.py | no production or exact-checker imports; raw full max | noncertified quadrature/bisection |

Canonical proof: research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md.
Sole stable owning ledger: knowledge/FIXED_ORDER_THEORY.md.

## Commands and checks

All results are fresh local checks. No hosted CI or external independent
mathematical review is claimed. Git uses the command-local prefix
`git -c safe.directory=<repository root in forward-slash form>`.
The literal audit below constructs that exact argument from Path.cwd();
no persistent Git configuration is changed.

| Exact command / Git argv after that prefix | Exit and material result | Property checked | Limitation |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime identity | local installation |
| `python -S -u ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py` | 0; output below | two rational entry gates and order/distance margins | analytic theorem and baseline minima are separate |
| `python -B -u ops/TASK-20260906__second_block_boundary_minimum/diagnose_boundary.py` | 0; excerpt below | raw full max, defining equations, derivatives and endpoints | noncertified numerical observations |
| `python -S -`, literal audit stdin below | 0; output below | nine paths, whitespace, AST/imports, links, owner and protection | engineering audit |
| `diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` | 0; full tracked diff inspected | authorized memory delta | new untracked sources read separately |
| `diff --check` | 0; no output | tracked whitespace | untracked whitespace checked by the audit |
| `status --short --untracked-files=all` | 0; three tracked modifications, six new task sources, one related request image | path inventory | image excluded |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable contract inventory | read-only |

Exact checker output:

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

Only these two directed entry signs are nontrivial rational proof gates.
Positive residuals precede squaring. The parameter corners follow from
monotonicity in x and epsilon/A; they do not replace the exact minima.
All curvature, attainment, uniqueness and endpoint signs are analytic.
No integral enclosure, refined alpha bracket or mesh is needed.

### Independent bounded numerical diagnostics

The final budget, fixed before running, is 70 decimal digits and 180
bisections per root, starting from the imported coarse x/alpha brackets.
The diagnostic recomputes both baseline parameters from their defining
equations. E(x_*) uses the literal full-max integral; K' retains the
moving-wrap jump. Six cost probes, four central differences with step
1/10^13, three mixed-curvature comparisons, entry and upper one-sided
differences, and endpoint/cubic/curvature-jump/order checks are specified
in diagnose_boundary.py. There is no random seed or finite construction.

The raw scorer retains BOTH maxima, including the removed diagonal.
Its cut uses k-c, separately from the closed formula's ratio switch.
The diagnostic imports no production, checker or verify.py code and
writes no files. Its material stdout excerpt is:

```text
PASS 70-digit diagnostics: baseline x and alpha recomputed from defining equations; 180 bisections per root
PASS 6 raw-full-max/primitive identities <1e-48; 4 smooth central differences <1e-23
PASS 3 mixed curvature identities <1e-23 and values >1; entry C1 and upper one-sided differences <1e-12
PASS endpoint bounds, cubic limit, entry curvature jump, root ordering and analytic distance bound
DIAGNOSTIC x_star 0.28763080286063766035065566
DIAGNOSTIC alpha_hat 0.10930369632641477424523226
DIAGNOSTIC lambda 0.31906991279063967312550492
DIAGNOSTIC h 0.050697985984831918289572495
DIAGNOSTIC tau_b 0.043385872797734668541952536
DIAGNOSTIC epsilon_b 0.043491748006012595900485859
DIAGNOSTIC epsilon_b-tau_b 0.0001058752082779273585333225
DIAGNOSTIC D_b_min -0.0000023552626403360732344352346
DIAGNOSTIC D_b_h 0.000037120321574067752906089517
DIAGNOSTIC positive_zero 0.045249957869611416989725416
NOTE: all printed decimals, numerical roots, quadratures and sampled checks are noncertified
mpmath 1.3.0
```

Both scripts first passed from stdin and then from authored files.
Those are local reproductions, not external independent acceptance.
A subsequent checker docstring clarification changes no calculation.

Skipped as inapplicable: production pytest, verify.py in either mode,
prior width/start checkers, finite searches, publication builds and
hosted CI. No production, certificate or old proof file changed.
The new proof does not depend on the old u=1/3 width minimum or its
refined alpha gates.

## Artifact and provenance checks

No finite result, certificate, permutation, publication or generated
asset is created. These are authored proof/check sources and task records.
The scripts write no output files. The containing task commit identifies
the integrated revision.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md | b5fb608178709fd29e3c535d7ddc9b337bec008e9bee7142a9f794b53778ad62 |
| ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py | c3c475e9a9df25242b4225f993e26f99ef55914287ba6f8df32b5c2aba396b8c |
| ops/TASK-20260906__second_block_boundary_minimum/diagnose_boundary.py | a003027c71f333672824f50d43bac57e1149a765db87529eb63475250699afb8 |

The inspected related request image has SHA256
46b078fb584cc91c3d46f818036c38cd024d3d8fb3b3bdf6d9d987f06af6dfec.
It remains an excluded pre-existing input; no authoring command targets it.

## Failed checks and negative evidence

- Plain Git reads failed the ownership guard; command-local safe.directory
  resolved it. The combined shell's final exit 0 did not make its earlier
  failing Git subcommands successful. Personal-ignore permission warnings
  did not prevent the subsequent scoped Git reads.
- Some combined reads exceeded the display budget; focused reads recovered
  the required definitions and proof sections.
- An approximate-input 40-digit secant diagnostic failed convergence,
  exit 1. Fixed-budget bisection then passed. Its approximate x=0.28765
  was exploratory, never an exact definition or proof premise.
- A delete-and-add patch of CURRENT_STATUS.md was rejected as two
  operations on one path. A later evidence patch had out-of-order hunks
  and was rejected. Neither attempt changed its target; single update
  patches resolved both authoring issues.
- Global convexity is false: all-chord curvature is negative and mixed
  curvature positive, with a jump at entry. C^1 matching still holds.
- No finite recovery, radius limit or new geometric bound is inferred.

## Final diff inspection

The complete new proof, both scripts and dossier were read directly.
The complete three-file tracked diff was inspected. Nine task paths are
allowed; the related predecessor request image remains unchanged and
excluded. New untracked sources receive an explicit whitespace check.

Run the following literal program with `python -S -`, using a PowerShell
single-quoted here-string (`@'`, program, then `'@ | python -S -`):

```python
from pathlib import Path
import ast, hashlib, re, subprocess

root = Path.cwd()
base = '648a8eae98c987dbcc11aa28fdcf55cb946d0ef8'
git = ['git','-c','safe.directory='+root.as_posix()]


def run(*args):
    result = subprocess.run(git+list(args),text=True,encoding='utf-8',capture_output=True)
    assert result.returncode == 0,(args,result.returncode,result.stderr)
    return result.stdout


task = 'ops/TASK-20260906__second_block_boundary_minimum/'
proof = 'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md'
allowed = {'CURRENT_STATUS.md','knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md',proof}
allowed |= {task+name for name in
            ('TASK_STATUS.md','TASK_LOG.md','EVIDENCE.md','check_boundary.py','diagnose_boundary.py')}
input_image = '.codex-remote-attachments/01a07644-59f6-76a2-8b3c-9f0fd686ecfe/8c2c4bc5-ab3c-41c1-9a86-9fd36fb32aaa/1-Photo-1.jpg'
assert run('rev-parse','HEAD').strip() == base
assert run('diff','--cached','--name-only') == ''
entries = run('status','--porcelain=v1','--untracked-files=all','-z').split('\0')
assert {entry[3:] for entry in entries if entry} == allowed|{input_image}
assert set(run('diff','--name-only').splitlines()) == {
    'CURRENT_STATUS.md','knowledge/FIXED_ORDER_THEORY.md','research/NEXT_RESEARCH_STEPS.md'}
assert run('diff','--check') == ''
links = 0
for name in sorted(allowed):
    source = Path(name).read_text(encoding='utf-8')
    assert source.endswith('\n'),name
    assert all(line == line.rstrip() for line in source.splitlines()),name
    assert all(ord(c)>=32 or c in '\t\n' for c in source),name
    if name.endswith('.py'):
        tree = ast.parse(source,filename=name)
        compile(tree,name,'exec')
        assert not any(isinstance(n,ast.Constant) and isinstance(n.value,float)
                       for n in ast.walk(tree)),name
        imports = [n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]
        imports += [a.name for n in ast.walk(tree) if isinstance(n,ast.Import) for a in n.names]
        expected = ['fractions'] if name.endswith('check_boundary.py') else ['mpmath']
        assert imports == expected,(name,imports)
    if name == proof:
        for target in re.findall(r'\]\(([^)]+)\)',source):
            assert (Path(name).parent/target).is_file(),target
            links += 1

protected = [
    'AGENTS.md','PROJECT_KNOWLEDGE.md','RINGMIN_REVIEW_PROTOCOL.md',
    'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md','verify.py',
    'paper_assets/ringmin_paper.tex','README.md','REPORT.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_START.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md',
    'research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md',
    'ops/TASK-20260906__second_block_start_domain/check_domain.py',
    'ops/TASK-20260906__second_block_start_domain/EVIDENCE.md']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show','HEAD:'+name),name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'],owners
for name in (proof,task+'check_boundary.py',task+'diagnose_boundary.py',input_image):
    print('SHA256',name,hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS source audit: 9 allowed paths; tracked/untracked whitespace; two script ASTs, exact imports and no float literals')
print(f'PASS {links} proof links; one owning ledger; {len(protected)} protected texts equal HEAD')
print('PASS git diff --check; unchanged HEAD; empty staged diff; only related request image excluded')
```

It exited 0 and printed the four SHA256 values recorded above, followed by:

```text
PASS source audit: 9 allowed paths; tracked/untracked whitespace; two script ASTs, exact imports and no float literals
PASS 7 proof links; one owning ledger; 17 protected texts equal HEAD
PASS git diff --check; unchanged HEAD; empty staged diff; only related request image excluded
```

Seventeen selected protected texts match HEAD after newline normalization.
The complete path inventory also excludes changes to other old proofs,
dossiers, ledgers, paper_assets/, results/, src/, tests/, scripts/,
verify.py and publication metadata. No stable claim was copied to another
thematic ledger; PROJECT_KNOWLEDGE.md remains unchanged.

The completed dossier is audited again before staging. Authorized
integration under AGENTS.md Section 3 stages only the nine inspected
paths, inspects the complete cached diff and its whitespace, commits
and pushes normally to existing origin/main, and verifies the remote SHA
and request-image-only remainder. The final handoff records the observed
containing commit and push outcome. Integration is separate from
external mathematical acceptance.

The completed evidence and current status were read in full. The literal
source audit was rerun after those updates: exit 0, identical four hashes
and all three PASS lines above. READY_FOR_REVIEW is set for integration;
it is not a claim of external review acceptance.

The initial nine-path git add exited 1 because the sandbox denied
.git/index.lock creation. The identical command, with granted escalation,
exited 0. The complete cached diff was inspected in explicit path groups;
a focused dossier read recovered a truncated display. The commands
diff --cached --check and diff --exit-code each exited 0 without diff
output. Status showed exactly nine staged task paths and the excluded
image. This final evidence/log update is inspected and restaged before
the containing commit; no mathematical source changes after its hash audit.

## Residual uncertainty

The continuous question is resolved by the proof, subject to independent
external mathematical review. Extra decimal digits are noncertified;
baseline theorems remain imported dependencies. No finite recovery of
this touching-block optimizer, new R_full limit or R*(n) bound is proved.
The scope is the specified continuous chord-diagonal subdomain.
Hosted CI and external review are not claimed.
