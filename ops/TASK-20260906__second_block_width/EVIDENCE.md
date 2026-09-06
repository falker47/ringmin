# Evidence

## Environment

```text
repository_head=72954156a317dcb61d4d5b511b4b07440ce34ffc
platform=Windows, PowerShell
python=3.14.3
mpmath=1.3.0 (separate diagnostics only)
dependency_source=existing environment; exact checker uses standard library
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Complete full-max formula and every spatial branch | exact continuous theorem | proof Sections 2-3; raw-integral diagnostics | derived directly from the symmetric full cost | baseline measure definition imported |
| Analytic derivative signs and two stationary points | exact continuous theorem | proof Sections 4-5; three rational curvature gates and four slope gates | no sampled curvature or optimizer | imported exact baseline bracket |
| Unique global minimum in the requested bracket | exact continuous theorem | analytic uniqueness plus opposite rational derivative signs and positive endpoint cost | new stdlib interval arithmetic, no production/older checker import | imported E(x_*) enclosure and alpha uniqueness are not re-proved |
| Single positive-width zero and positive tail cost | exact continuous theorem | proof Section 6, D(h)>0 and D(L)>0 gates | original full-max primitives | only this width family |
| Printed extra minimizer digits | numerical observation | preliminary mpmath probe with prior diagnostic alpha decimal | floating high precision | not the exact bracket and not a proof premise |
| Four-width formula verification | numerical diagnostic | 70-digit original max quadrature, differentiated primitives | separate arithmetic and direct quadrature | rational alpha proxy only; no all-domain proof |

The authoritative mathematics is in
research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md. Only
knowledge/FIXED_ORDER_THEORY.md owns its stable summary. Global bounds,
finite certificates, production code and publication claims are unchanged.

## Commands and checks

Startup read-only status was empty; repository root and HEAD were verified.
Python --version exited 0 and reported Python 3.14.3.

All checks here were freshly executed locally; no hosted CI or independent
external review result is asserted.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | existing runtime | other environments |
| `python -S -u ops/TASK-20260906__second_block_width/check_width.py` | 0; exact output below | eleven critical interval inequalities, switch/domain gates and fail-closed arithmetic guards | imported theorem proofs or geometric feasibility |
| `python -` supplied the literal diagnostic program below through a PowerShell here-string | 0; three PASS/NOTE lines below and mpmath 1.3.0 | raw full-max integrals, derivatives and two critical enclosures at a rational proxy | signs, exact alpha identity or a parameter sweep |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check` | 0; no output | tracked whitespace | untracked whitespace, checked separately |
| Same repository-scoped `git diff --stat` and `git status --short --untracked-files=all` | 0; three tracked edits and five additions | allowed path inventory | mathematical correctness |

Final exact-mode output (all displayed intervals are outward rationals):

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

The program uses a 10^-40 integer grid with outward rounding, 64 terms
per elementary series and at most 80 rational switch bisections per
corner. Every numerical sign in the proof is separated by a rational
interval; none comes from the diagnostic computation. The PASS lines for
analytic implications refer to the written proof, not a numerical check
of all points. The imported E interval is explicitly sourced to Section 4
of the alpha-minimum proof. Refining the alpha enclosure keeps the same
exact minimizer and does not optimize another parameter.

The independent diagnostic was run exactly as this stdin Python program
(literal PowerShell wrapper: `@'`, the program, then `'@ | python -`):

```python
import mpmath as m
import runpy
from fractions import Fraction as Q
m.mp.dps=70
check=runpy.run_path('ops/TASK-20260906__second_block_width/check_width.py')
A=1+m.mpf(1093037)/10**7; u=m.mpf(1)/3; B=A+u; h=A/3-u; L=2-A-u
v=lambda s,e:m.sqrt((u+s)/(B+s))+m.sqrt((u+s)/(B+e-s))-1
tau=m.findroot(lambda e:v(e,e),(m.mpf('.03119'),m.mpf('.03120')))
def z(e):
    return e if e<=tau else m.findroot(lambda s:v(s,e),(e/10,e/5))
def chord(s,e):return m.sqrt((B+s)*(B+e-s))
def chain(s,e):return m.sqrt(u+s)*(m.sqrt(B+s)+m.sqrt(B+e-s))
def diag(s):return max(B+s,2*m.sqrt((u+s)*(B+s)))
def raw(e):
    cuts=sorted(set([m.mpf(0),e,z(e),min(e,h)]))
    return m.quad(lambda s:max(chord(s,e),chain(s,e))-diag(s),cuts)
def primitive_f(t,c):return ((2*t+c)*m.sqrt(t*(t+c))-c*c*m.log((m.sqrt(t)+m.sqrt(t+c))/m.sqrt(c)))/4
def circle(v,R):return (v*m.sqrt(R*R-v*v)+R*R*m.asin(v/R))/2
def closed(e):
    zz=z(e); w=min(e,h); M=B+e/2; T=B+u+e
    return circle(zz-e/2,M)-circle(-e/2,M)+primitive_f(u+e,A)-primitive_f(u+zz,A)+circle(u+e-T/2,T/2)-circle(u+zz-T/2,T/2)-B*w-w*w/2-2*(primitive_f(u+e,A)-primitive_f(u+w,A))
def slope(e):
    zz=z(e)
    return max(chord(e,e),chain(e,e))-diag(e)+(m.quad(lambda s:m.sqrt((B+s)/(B+e-s)),[0,zz])+m.quad(lambda s:m.sqrt((u+s)/(B+e-s)),[zz,e]))/2
errors=[]
for e in [m.mpf(1)/100,m.mpf(1)/32,m.mpf(1)/10,m.mpf(2)/5]:
    errors += [abs(raw(e)-closed(e)),abs(m.diff(closed,e)-slope(e))]
    if e>tau:
        zz=z(e); t=u+zz; y=B+e-zz; r=m.sqrt(t/(A+t)); zp=(1-r)**2/(2-r+2*r*r)
        J=m.quad(lambda s:m.sqrt(B+s)/(B+e-s)**m.mpf('1.5'),[0,zz])+m.quad(lambda s:m.sqrt(u+s)/(B+e-s)**m.mpf('1.5'),[zz,e])
        q=u+e; pprime=(A+2*q)/(2*m.sqrt(q*(A+q)))+m.sqrt(B)/(2*m.sqrt(q))
        dprime=1 if e<h else (A+2*q)/m.sqrt(q*(A+q))
        Q1=zp*(m.sqrt(B+zz)-m.sqrt(u+zz))/(2*m.sqrt(y))
        formula=pprime-dprime+m.sqrt(q/B)/2-J/4+Q1
        errors += [abs(m.diff(z,e)-zp),abs(m.diff(slope,e)-formula)]
assert max(errors)<m.mpf('1e-60')
for at_wrap in (False,True):
    box=check['critical_delta'](check['Box'](Q(11093037,10**7)),at_wrap)
    value=raw(L if at_wrap else h)
    assert m.mpf(box.lo)/check['SCALE']<value<m.mpf(box.hi)/check['SCALE']
assert abs(z(2*h)-h)<m.mpf('1e-60')
print('PASS independent 70-digit diagnostics: 4 fixed widths, 14 primitive/derivative identities; maximum error < 1e-60')
print('PASS raw full-max quadrature inside both exact critical cost boxes; z(2*h)=h to < 1e-60')
print('NOTE: rational proxy alpha=1093037/10^7 only; diagnostics prove no signs or parameter identity')
print('mpmath',m.__version__)
```

Output:

```text
PASS independent 70-digit diagnostics: 4 fixed widths, 14 primitive/derivative identities; maximum error < 1e-60
PASS raw full-max quadrature inside both exact critical cost boxes; z(2*h)=h to < 1e-60
NOTE: rational proxy alpha=1093037/10^7 only; diagnostics prove no signs or parameter identity
mpmath 1.3.0
```

These diagnostics import the new checker only to compare the two raw
costs against its intervals; their raw cost uses the original max and
independent quadrature. They do not constitute an independent proof of
the interval arithmetic engine. All sign proofs use the exact run.

Skipped as outside this delta: production pytest, verify.py in either
frontier mode, prior recovery checkers, finite geometric experiments,
publication builds and hosted CI. No production, certificate or published
asset changed, and the user explicitly excluded new finite permutations.

## Artifact and provenance checks

No result/certificate or publication asset is generated. New files are
authored proof/checker sources based on the HEAD above, pending manual review.

Exact local source-byte SHA256 values (no generation commit is claimed for
these uncommitted authored additions):

| Source | SHA256 |
|---|---|
| research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md | 72d632bbc11a071c7de0ae49413698d7f2513cc59575db6ab9d01b739f193e3b |
| ops/TASK-20260906__second_block_width/check_width.py | 06d84e7e1a8efcbc0525a3322ad8b0be34f4693525adb087c6f00c0a51fa7d6d |

## Failed checks and negative evidence

Initial plain Git calls hit the ownership guard, as recorded in TASK_LOG.md.
The first in-memory source audit exited 1 when the default Windows cp1252
decoder could not decode Git's UTF-8 AGENTS.md output. The corrected audit
below specifies encoding='utf-8' and exited 0. No source repair was needed.

The exploratory automatic second-derivative values at tau/h were
discarded because the applicable second derivative need not exist there.
The written proof instead matches first derivatives and treats curvature
on open regimes. The final exact inequalities all passed; there was no
failed or unreported mathematical gate. The final descending segment
prevents using whole-right-side increase as a route to global uniqueness;
the proof includes a separate positive endpoint comparison.

## Final diff inspection

- Complete tracked diff read: CURRENT_STATUS.md, the one added fixed-order
  ledger entry, and the roadmap's new resolved task/current discriminator
  plus retained deferred reviews.
- All five new files read in full: the proof, checker and three dossier files.
- Eight allowed paths total; three tracked edits and five additions.
- Explicit whitespace/control-character scan includes every untracked
  addition; all pass. AST compilation creates no bytecode file.
- Six links in the proof resolve. Only the fixed-order ledger changed;
  no duplicate stable entry was added to another thematic module.
- Twelve protected contract/index/global/publication/dependency texts
  compared to HEAD after newline normalization, all equal; complete status
  confirms no other protected or generated path changed.
- HEAD remains 72954156a317dcb61d4d5b511b4b07440ce34ffc and staged diff is empty.
- `git diff --check`, status and staged-diff checks all exit 0. Git's
  unreadable personal ignore warning does not change those exit codes.

The corrected audit was run with `python -S -`, supplied through the same
literal PowerShell here-string mechanism. This is its complete program:

```python
from pathlib import Path
import ast, hashlib, re, subprocess
base='72954156a317dcb61d4d5b511b4b07440ce34ffc'
git=['git','-c','safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin']
def run(*args):
    p=subprocess.run(git+list(args),text=True,encoding='utf-8',capture_output=True)
    assert p.returncode==0,(args,p.returncode,p.stderr)
    return p.stdout
allowed={
'CURRENT_STATUS.md','knowledge/FIXED_ORDER_THEORY.md','research/NEXT_RESEARCH_STEPS.md',
'research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md',
'ops/TASK-20260906__second_block_width/TASK_STATUS.md',
'ops/TASK-20260906__second_block_width/TASK_LOG.md',
'ops/TASK-20260906__second_block_width/EVIDENCE.md',
'ops/TASK-20260906__second_block_width/check_width.py'}
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
    assert all(not any(ord(c)<32 and c not in '\t\n' for c in line) for line in content.splitlines()),name
    if name.endswith('.py'):
        tree=ast.parse(content,filename=name)
        compile(tree,name,'exec')
        assert {node.module for node in ast.walk(tree) if isinstance(node,ast.ImportFrom)}=={'fractions','math'}
        assert not any(isinstance(node,ast.Import) for node in ast.walk(tree))
    if name.endswith('SECOND_BLOCK_WIDTH.md'):
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
'research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md',
'research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md']
for name in protected:
    assert Path(name).read_text(encoding='utf-8')==run('show',f'HEAD:{name}'),name
for name in ['research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md','ops/TASK-20260906__second_block_width/check_width.py']:
    print('SHA256',name,hashlib.sha256(Path(name).read_bytes()).hexdigest())
print(f'PASS source audit: 8 allowed paths; all tracked/untracked whitespace; AST and stdlib-only imports; {links} proof links')
print(f'PASS protection: {len(protected)} dependency/contract/publication texts equal HEAD; no other changed paths; HEAD and staged state unchanged')
print('PASS git diff --check (exit 0), git status (exit 0), git diff --cached (exit 0)')
```

It exited 0 and printed the two hashes above, followed by:

```text
PASS source audit: 8 allowed paths; all tracked/untracked whitespace; AST and stdlib-only imports; 6 proof links
PASS protection: 12 dependency/contract/publication texts equal HEAD; no other changed paths; HEAD and staged state unchanged
PASS git diff --check (exit 0), git status (exit 0), git diff --cached (exit 0)
```

## Residual uncertainty

Imported baseline theorems and independent external review remain separate.
Extra decimal digits are not certified. No finite recovery at epsilon_*,
full-radius limit, global bound, finite optimization/certificate, start
variation or joint block optimum has been established here. The exact
checker is local stdlib evidence for isolated analytic premises, not a
geometric certificate or a substitute for external proof review.
