# Evidence

## Environment

```text
repository_head=ac2e7f239212b99079bef5ab3431474af0ad25e3
platform=Windows, PowerShell
python=3.14.3
mpmath=1.3.0 (independent diagnostics only)
dependency_source=existing environment; exact checker uses stdlib only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Full-max derivative with physical and translated endpoints | exact continuous theorem | proof Sections 2-4 | derived from the measure difference, no production imports | baseline measure definition imported |
| Smooth implicit switch and diagonal-chord neighborhood | exact continuous theorem | unsquared monotonicity/implicit differentiation; rational rectangle gates | new exact Fraction arithmetic | only the stated local domain |
| Strict positive start derivative | exact continuous theorem | nonnegative chord integrand and strictly positive chain integrand | analytic proof, no numerical sign premise | no continuation outside the neighborhood |
| Quantitative derivative enclosure at epsilon_* | exact continuous theorem with a rational interval gate | width-stationarity elimination plus integer square-root enclosures | new standalone stdlib checker | exact alpha/width brackets imported |
| Nonstationarity and leftward descent; local width-minimum branch | proved continuous corollary | smoothness, positive start derivative, imported positive width curvature | analytic directional derivative and implicit function theorem | no joint optimum elsewhere or global branch continuation |
| Extra digits and raw-max comparisons | numerical observations | separate 70-digit root solving/quadrature/central differences | no task/checker/production imports | floating diagnostics do not prove signs |

Authoritative mathematics: research/PERMUTED_HALVES_SECOND_BLOCK_START.md.
Only knowledge/FIXED_ORDER_THEORY.md owns the stable claim. The earlier
width note changes only its final follow-up link. The exact alpha and
width minima are imported from the linked accepted sources; rerunning
the width checker does not independently re-prove those theorems.

## Commands and checks

All checks below were freshly executed locally. No independent external
review, hosted CI result, production test run or global finite certificate
verification is claimed.

| Exact command/check | Exit/result | Property checked | Not checked |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime identity | other environments |
| `python -S -u ops/TASK-20260906__second_block_start/check_start.py` | 0; full output below | rectangle/domain/switch inequalities, one terminal radical enclosure, four invalid-input guards | analytic derivation or imported minima |
| `python -S -u ops/TASK-20260906__second_block_width/check_width.py` | 0; full output below | imported checker still separates all eleven critical enclosures and its domain/guard gates | independent proof of all imported baseline results |
| `python -`, literal diagnostic stdin program below | 0; full output below | independent raw-full-max and moving-endpoint identities | exact signs, certified extra digits |
| `python -S -`, literal source-audit program below | 0; full output below | all nine allowed paths, tracked/untracked whitespace, AST/imports, links, owner and protected sources | mathematical proof acceptance |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check` | 0; no output | tracked whitespace | untracked whitespace, covered by explicit audit |
| Same repository-scoped `git diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md` and `git status --short --untracked-files=all` | 0; four inspected tracked edits and five additions | complete tracked delta and path inventory | external acceptance |

The exact new checker output is:

```text
PASS rectangle: |u-1/3|<=1/10^6, EL<=epsilon<=EH; disjoint, pre-wrap, diagonal chord, block mixed
EXACT 4*pi*partial_u Delta C(1/3,epsilon_*) in [66955912,74512461]/10^12
PASS strict quantitative gate: 1/20000 < 4*pi*partial_u Delta C < 1/10000
PASS exact ties, square-root enclosures and four invalid-input guards
NOTE: analytic sign and endpoint cancellation are proved in the note; imported minima and extra decimal digits are not certified here
```

The entire accepted alpha/width rectangle is enclosed, without replacing
either exact minimizer by a rational midpoint. The switch is not solved
or discretized in the checker. Integer square roots use a 10^-30 grid;
every resulting rational squared enclosure is checked. Monotone positive
endpoint expressions and outward rounding produce the displayed 10^-12
interval. The proof supplies all continuum arguments.

Fresh width-checker output:

```text
EXACT Fprime(10930369/10^8) in [-6646,-1825]/10^12
EXACT Fprime(10930371/10^8) in [774,5594]/10^12
PASS same alpha_hat isolated in (10930369/10^8,10930371/10^8)
PASS domain/switch order: 3119/10^5<tau<312/10^4<EL<EH<h<1/20<L
EXACT Mprime endpoint square at a in [1539769696812,1540056908541]/10^12
EXACT Mprime endpoint square at b in [252449493925,252720030240]/10^12
EXACT Jprime square gate in [1822946993601,1823333688076]/10^12
PASS analytic implications: Psiprime>77/160 on (tau,h); Psisecond<0 on (h,L)
EXACT Psi(31248/10^6) in [-601358,-371047]/10^12
EXACT Psi(1/32) in [2452125,2682436]/10^12
EXACT Psi(1/3) in [1100874055,1101089693]/10^12
EXACT Psi(2/5) in [-2864872963,-2864658070]/10^12
EXACT 4*pi*Delta C(h) in [19529281,19708132]/10^12
EXACT 4*pi*Delta C(L) in [473194165,473693306]/10^12
PASS ties and five invalid-input guards
PASS unique continuous global minimum: 31248/10^6<epsilon_*<1/32
NOTE: no finite permutations, radius transfer, global bound or imported-minimum re-proof
```

### Independent falsifiable diagnostics

The diagnostic was bounded before execution: 70 decimal digits, three
implicit baseline/width roots (each findroot call capped at 30 steps),
three fixed (u,epsilon) pairs and six central differences with step
10^-16. Every cost is the original full max, with its block and diagonal
cuts included in quadrature. The diagnostic imports only mpmath; it does
not call the new checker, previous checkers, production code or verify.py.

This is the literal stdin program, run through a PowerShell single-quoted
here-string (`@'`, the program, then `'@ | python -`):

```python
import mpmath as m
m.mp.dps=70
def switch(A,u,e):
    v=lambda s:m.sqrt((u+s)/(A+u+s))+m.sqrt((u+s)/(A+u+e-s))-1
    if v(e)<=0:return e
    if v(0)>=0:return m.mpf(0)
    return m.findroot(v,(0,e),maxsteps=30)
def raw(A,u,e):
    B=A+u
    z=switch(A,u,e); w=min(e,max(m.mpf(0),A/3-u))
    cuts=sorted(set([m.mpf(0),z,w,e]))
    return m.quad(lambda s:
        max(m.sqrt((B+s)*(B+e-s)),m.sqrt(u+s)*(m.sqrt(B+s)+m.sqrt(B+e-s)))
        -max(B+s,2*m.sqrt((u+s)*(B+s))),cuts)
def width_slope(A,u,e):
    B=A+u; z=switch(A,u,e)
    p=max(m.sqrt(B*(B+e)),m.sqrt(u+e)*(m.sqrt(B+e)+m.sqrt(B)))
    d=max(B+e,2*m.sqrt((u+e)*(B+e)))
    I=m.quad(lambda s:m.sqrt((B+s)/(B+e-s)),[0,z])
    I+=m.quad(lambda s:m.sqrt((u+s)/(B+e-s)),[z,e])
    return p-d+I/2
x=m.findroot(lambda x:width_slope(m.mpf(1),m.mpf(0),x),
             (m.mpf(719)/2500,m.mpf(2877)/10000),maxsteps=30)
estar=raw(m.mpf(1),m.mpf(0),x)
def alpha_eq(alpha):
    A=1+alpha; a=A/3; b=1-alpha
    shift=a/2+(m.quad(lambda t:m.sqrt(t/(t+A)),[a,b])
               +m.quad(lambda t:m.sqrt(t/(t+alpha)),[b,1]))/2
    shift-=(m.sqrt(2)-1)*m.sqrt(b)
    return shift+A*estar
alpha=m.findroot(alpha_eq,(m.mpf(10930369)/10**8,m.mpf(10930371)/10**8),maxsteps=30)
A=1+alpha; u0=m.mpf(1)/3
e0=m.findroot(lambda e:width_slope(A,u0,e),(m.mpf(31248)/10**6,m.mpf(1)/32),maxsteps=30)
def translated(A,u,e):
    B=A+u; z=switch(A,u,e)
    chord=lambda s:(2*B+e)/(2*m.sqrt((B+s)*(B+e-s)))-1
    chain=lambda s:(m.sqrt(B+s)+m.sqrt(B+e-s))/(2*m.sqrt(u+s))+m.sqrt(u+s)*(1/m.sqrt(B+s)+1/m.sqrt(B+e-s))/2-1
    return m.quad(chord,[0,z])+m.quad(chain,[z,e])
def moving(A,u,e):
    B=A+u; z=switch(A,u,e)
    p=m.sqrt(u+e)*(m.sqrt(B+e)+m.sqrt(B))
    c0=m.sqrt(B*(B+e))
    I=m.quad(lambda s:m.sqrt((B+s)/(B+e-s)),[0,z])+m.quad(lambda s:m.sqrt((u+s)/(B+e-s)),[z,e])
    return p-c0-e+I
points=[(u0,e0),(u0-m.mpf(1)/(2*10**6),m.mpf(31248)/10**6),
        (u0+m.mpf(1)/(2*10**6),m.mpf(1)/32)]
errors=[]; fd_errors=[]; step=m.mpf(1)/10**16
for u,e in points:
    z=switch(A,u,e); t=u+z; X=A+t; Y=A+u+e-z
    denom=A*(Y/X)**m.mpf('1.5')+Y+t
    zu=-(A*(Y/X)**m.mpf('1.5')+Y-t)/denom
    ze=t/denom
    G=2*(A+u)+e-m.sqrt((A+u)*(A+u+e))-m.sqrt(u+e)*(m.sqrt(A+u)+m.sqrt(A+u+e))
    value=translated(A,u,e)
    errors += [abs(value-moving(A,u,e)),
               abs(value-2*width_slope(A,u,e)-G),
               abs(m.diff(lambda v:switch(A,v,e),u)-zu),
               abs(m.diff(lambda v:switch(A,u,v),e)-ze),
               abs(1+zu-2*ze)]
    fd_errors += [abs((raw(A,u+step,e)-raw(A,u-step,e))/(2*step)-value),
                  abs((raw(A,u,e+step)-raw(A,u,e-step))/(2*step)-width_slope(A,u,e))]
assert max(errors)<m.mpf('1e-60')
assert max(fd_errors)<m.mpf('1e-28')
value=translated(A,u0,e0)
assert m.mpf(66955912)/10**12<value<m.mpf(74512461)/10**12
assert raw(A,u0-m.mpf(1)/(2*10**6),e0)<raw(A,u0,e0)
print('PASS 70-digit diagnostics: 3 fixed pairs, 15 endpoint/switch identities; max error < 1e-60')
print('PASS 6 raw-full-max central differences, step=1e-16; max error < 1e-28')
print('PASS raw cost decreases for u reduced by 1/(2*10^6) at the diagnostic width root')
print('DIAGNOSTIC alpha_hat =',m.nstr(alpha,35))
print('DIAGNOSTIC epsilon_* =',m.nstr(e0,35))
print('DIAGNOSTIC 4*pi*partial_u Delta C =',m.nstr(value,35))
print('NOTE: independently solved floating roots and quadrature; exact signs and brackets come only from the proof/checkers')
print('mpmath',m.__version__)
```

Its exact output was:

```text
PASS 70-digit diagnostics: 3 fixed pairs, 15 endpoint/switch identities; max error < 1e-60
PASS 6 raw-full-max central differences, step=1e-16; max error < 1e-28
PASS raw cost decreases for u reduced by 1/(2*10^6) at the diagnostic width root
DIAGNOSTIC alpha_hat = 0.10930369632641477424523225745801231
DIAGNOSTIC epsilon_* = 0.031248317406489870744289859840183207
DIAGNOSTIC 4*pi*partial_u Delta C = 0.000071922296194889773562884341952312177
NOTE: independently solved floating roots and quadrature; exact signs and brackets come only from the proof/checkers
mpmath 1.3.0
```

The user's prediction 7.19222961949e-5 is consistent with this independently
computed numerical value and the rational enclosure. It is not a premise
for any sign, branch decision, bracket or theorem.

Skipped as outside the delta: production pytest, verify.py in either
frontier mode, finite recovery/geometry experiments, publication builds
and hosted CI. No corresponding code, certificate or published asset
changed. No independent reviewer or agent was invoked.

## Artifact and provenance checks

No certificate/result or publication asset was generated. These are
authored research and checker sources based on the HEAD above. The
containing task commit identifies the integrated revision; its SHA and
normal-push result are reported in the final handoff.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_SECOND_BLOCK_START.md | 40068b6cbb1006243d17428648ece7dbd700b1da68e4cfaa53c6608b91b7489e |
| ops/TASK-20260906__second_block_start/check_start.py | c6236b4828bd3d5661d52db865b867b061ddb74736629f64d01367df6660d71d |

No nondeterministic output file is produced by either exact checker or
the diagnostic program. Baseline source content remains unchanged.

## Failed checks and negative evidence

- Initial plain Git reads exited 1 at the ownership guard. Repeating them
  with the repository-scoped safe.directory option exited 0. No persistent
  configuration or remote was modified. The personal ignore-file warning
  did not change successful read-only Git exit codes.
- Initial template reads used nonexistent unsuffixed names. The actual
  *_TEMPLATE.md files were then found and read; no edit resulted.
- One combined patch was rejected before application because it attempted
  both deletion and addition of CURRENT_STATUS.md in the same patch.
  The existing file was subsequently updated in place. A proof line-break
  typo was fixed during the complete source inspection.
- No exact mathematical gate or independent numerical diagnostic failed.
  Whole-family stationarity at the width minimum is refuted, not left
  open; joint minimization elsewhere remains unaddressed.

## Final diff inspection

The full tracked diff and all five new files were read. The nine allowed
paths comprise four tracked changes and five additions. Explicit checks
include untracked-file whitespace, AST compilation without bytecode,
stdlib-only checker imports, all five links in the new proof, and exactly
one owning ledger. Twelve protected contract/dependency/publication texts
match HEAD after newline normalization. The complete existing width-proof
body is identical to HEAD; only its final follow-up navigation changes.

This exact audit program was run with `python -S -`, using the same literal
single-quoted PowerShell here-string wrapper:

```python
from pathlib import Path
import ast, hashlib, re, subprocess
base='ac2e7f239212b99079bef5ab3431474af0ad25e3'
git=['git','-c','safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin']
def run(*args):
    p=subprocess.run(git+list(args),text=True,encoding='utf-8',capture_output=True)
    assert p.returncode==0,(args,p.returncode,p.stderr)
    return p.stdout
allowed={
'CURRENT_STATUS.md','knowledge/FIXED_ORDER_THEORY.md','research/NEXT_RESEARCH_STEPS.md',
'research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md','research/PERMUTED_HALVES_SECOND_BLOCK_START.md',
'ops/TASK-20260906__second_block_start/TASK_STATUS.md',
'ops/TASK-20260906__second_block_start/TASK_LOG.md',
'ops/TASK-20260906__second_block_start/EVIDENCE.md',
'ops/TASK-20260906__second_block_start/check_start.py'}
assert run('rev-parse','HEAD').strip()==base
assert run('diff','--cached','--name-only')==''
status=run('status','--short','--untracked-files=all')
assert {line[3:] for line in status.splitlines()}==allowed,status
assert run('diff','--check')==''
links=0
for name in sorted(allowed):
    content=Path(name).read_text(encoding='utf-8')
    assert content.endswith('\n')
    assert all(line==line.rstrip() for line in content.splitlines()),name
    assert all(ord(c)>=32 or c in '\t\n' for c in content),name
    if name.endswith('.py'):
        tree=ast.parse(content,filename=name)
        compile(tree,name,'exec')
        assert {node.module for node in ast.walk(tree) if isinstance(node,ast.ImportFrom)}=={'fractions','math'}
        assert not any(isinstance(node,ast.Import) for node in ast.walk(tree))
    if name.endswith('SECOND_BLOCK_START.md'):
        for dest in re.findall(r'\]\(([^)]+)\)',content):
            assert (Path(name).parent/dest).is_file(),dest
            links+=1
protected=[
'AGENTS.md','PROJECT_KNOWLEDGE.md','RINGMIN_REVIEW_PROTOCOL.md',
'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md','verify.py','paper_assets/ringmin_paper.tex',
'research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md',
'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md',
'research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md',
'research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md',
'ops/TASK-20260906__second_block_width/check_width.py',
'ops/TASK-20260906__second_block_width/EVIDENCE.md']
for name in protected:
    assert Path(name).read_text(encoding='utf-8')==run('show',f'HEAD:{name}'),name
width='research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md'
assert Path(width).read_text(encoding='utf-8').split('**Subsequent continuous discriminator:**')[0]==run('show',f'HEAD:{width}').split('**Exactly one next atomic discriminator:**')[0]
assert [p.as_posix() for p in Path('knowledge').glob('*.md') if 'PERMUTED_HALVES_SECOND_BLOCK_START.md' in p.read_text(encoding='utf-8')]==['knowledge/FIXED_ORDER_THEORY.md']
for name in ['research/PERMUTED_HALVES_SECOND_BLOCK_START.md','ops/TASK-20260906__second_block_start/check_start.py']:
    print('SHA256',name,hashlib.sha256(Path(name).read_bytes()).hexdigest())
print(f'PASS source audit: 9 allowed paths; all tracked/untracked whitespace; AST and stdlib-only imports; {links} proof links; single ledger owner')
print(f'PASS protection: {len(protected)} dependency/contract/publication texts equal HEAD; width proof body unchanged')
print('PASS git diff --check (exit 0), git status (exit 0), unchanged HEAD and empty staged diff')
```

It exited 0 with:

```text
SHA256 research/PERMUTED_HALVES_SECOND_BLOCK_START.md 40068b6cbb1006243d17428648ece7dbd700b1da68e4cfaa53c6608b91b7489e
SHA256 ops/TASK-20260906__second_block_start/check_start.py c6236b4828bd3d5661d52db865b867b061ddb74736629f64d01367df6660d71d
PASS source audit: 9 allowed paths; all tracked/untracked whitespace; AST and stdlib-only imports; 5 proof links; single ledger owner
PASS protection: 12 dependency/contract/publication texts equal HEAD; width proof body unchanged
PASS git diff --check (exit 0), git status (exit 0), unchanged HEAD and empty staged diff
```

Protected/generated directories have no changes in the complete status.
AGENTS.md, PROJECT_KNOWLEDGE.md, publication content, finite certification
scope, global-bound ledger, production implementation and verifier remain
untouched. After this pre-staging audit, the following exact command exited
0 (the sandbox's .git permission was granted):

```text
git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin add -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md research/PERMUTED_HALVES_SECOND_BLOCK_START.md ops/TASK-20260906__second_block_start/TASK_STATUS.md ops/TASK-20260906__second_block_start/TASK_LOG.md ops/TASK-20260906__second_block_start/EVIDENCE.md ops/TASK-20260906__second_block_start/check_start.py
```

With the same repository-scoped Git prefix, `diff --cached --check`
exited 0 with no whitespace output, `diff --cached` exited 0 and its
complete content was inspected (the long combined display was supplemented
by focused dossier reads). `diff --exit-code` exited 0 with no output;
`status --short --untracked-files=all` showed exactly the nine staged
paths and no other edits. This evidence/log addition is inspected and
restaged before commit. Integration and mathematical acceptance are separate.

## Residual uncertainty

The exact sign is resolved within the continuous family. The imported
baseline and width-minimum proofs, and independent external acceptance of
this theorem, remain separate. Extra decimal digits are not certified.
No location or existence result for a joint minimizer elsewhere is
established here. Nor is a continuation to a boundary, finite permutation
realization at epsilon_*, R_full transfer, geometric/global bound or
hosted-CI result established.
