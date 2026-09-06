# Evidence

## Environment

```text
repository_head=d169dd86b8aaadd19a822528e53c29f88bb9bd6f
platform=Windows, PowerShell
python=3.14.3
mpmath=1.3.0 (independent diagnostics only)
dependency_source=existing environment; exact checker uses stdlib only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Exact baseline and coarse brackets | imported exact theorems | joint prefix note, Section 1 | accepted source dependencies | minima are not re-proved here |
| Exhaustive all-chord/mixed/entry-tie partition and C^1 matching | exact continuous theorem | new proof, Sections 2-3; unsquared monotonicity, implicit function theorem and dominated difference quotients | analytic derivation from full max | clipped switch is not asserted smooth at entry |
| D_u>=epsilon^3/[48*(A+u+epsilon)^2]>0 | exact continuous theorem | new proof, Section 4; first half always chord, exact positive derivative integrands | no numerical gate or width minimum is a premise | 0<u<u+epsilon<A/3; zero-width derivative is zero |
| Touching-block coupling and weak/cost continuity | exact continuous theorem | reflection marginal identity and continuous-test formula in Section 5 | direct measure argument | distinct reflections, no finite recovery |
| Strict boundary dominance and equality of infima | proved continuous corollary | integrated derivative bound and explicit interior sequence, Section 5 | both inequalities proved analytically | no boundary-width attainment, location or uniqueness |
| Baseline admissibility margins | exact rational arithmetic / engineering check | minimal standalone Fraction checker | no production or previous-checker imports | brackets themselves are imported |
| Sampled identities, differences, lower bounds and limits | numerical observations | literal 70-digit program below | independent of all checker and production code | rational diagnostic parameters, not exact minimizer definitions |

Authoritative mathematics: research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md.
The only stable owning ledger is knowledge/FIXED_ORDER_THEORY.md.
All existing proof notes and earlier dossiers retain their original content.

## Commands and checks

All results below were freshly obtained locally. No hosted CI or external
independent mathematical review is claimed. For Git commands the prefix is
`git -c safe.directory=<repository root in forward-slash form>`; the
literal audit program below constructs that exact argument from Path.cwd(),
without changing persistent configuration.

| Exact command or argv after that Git prefix | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime identity | other environments |
| `python -S -u ops/TASK-20260906__second_block_start_domain/check_domain.py` | 0; output below | bracket ordering and three rational admissibility margins | continuum proof or imported minima |
| `python -S -u ops/TASK-20260906__second_block_start/check_start.py` | 0; output below | regression of the prior local rectangle and radical gate | new theorem, external acceptance or re-proof of its imported width result |
| `python -`, literal diagnostic stdin below | 0; output below | raw full max, branch formulas, two derivative representations, boundary probes | exact continuum signs |
| `python -S -`, literal audit stdin below | 0; output below | all eight authored/modified paths, whitespace, imports, links, ownership and protection | mathematical acceptance |
| `diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` | 0; full three-file tracked diff inspected | complete tracked delta | new untracked content, read separately |
| `diff --check` | 0; no output | tracked whitespace | untracked whitespace, checked explicitly below |
| `status --short --untracked-files=all` | 0; three tracked modifications, five new task files and the pre-existing request image | complete task/input inventory | mathematical claims |

New exact-checker output:

```text
EXACT lambda > 7975867/25000000 > 0
EXACT a-lambda > 15186317/300000000 > 0
EXACT b-a > 13023/25000 > 0
PASS imported bracket order and three baseline-admissibility margins
NOTE: no radical/root gates remain; continuum sign, switches and infimum reduction are proved analytically
```

These are the only new computational proof gates. The first-half sign,
switch regularity and boundary reduction are analytic for arbitrary
positive A in the stated domain. No parameter rectangle, radical root
enclosure or width-stationarity gate is required.

Fresh prior-local-checker output:

```text
PASS rectangle: |u-1/3|<=1/10^6, EL<=epsilon<=EH; disjoint, pre-wrap, diagonal chord, block mixed
EXACT 4*pi*partial_u Delta C(1/3,epsilon_*) in [66955912,74512461]/10^12
PASS strict quantitative gate: 1/20000 < 4*pi*partial_u Delta C < 1/10000
PASS exact ties, square-root enclosures and four invalid-input guards
NOTE: analytic sign and endpoint cancellation are proved in the note; imported minima and extra decimal digits are not certified here
```

This regression is supplementary. Neither epsilon_* nor the refined alpha
enclosure used there is a dependency of the new theorem.

### Independent bounded diagnostics

Budget fixed before computation: 70 decimal digits, three rational positive
A values, three rational normalized starts, exactly 180 bisections per
implicit root, three widths per start (strict all-chord, entry tie, strict
mixed), and central-difference step A/10^14. The switch is solved from the
raw cost difference k-c. The raw integral keeps BOTH maxima, including the
removed diagonal, and splits quadrature at their cuts. No seed, optimizer,
finite permutation, previous checker, production module or verify.py is used.

The rational A/start probes are deliberately not definitions or numerical
recomputations of alpha_hat and x_*. They test the universal analytic lemma.
Errors are normalized by A for derivatives and A^2 for costs. Entry-tie
central differences have a weaker tolerance because only C^1 is claimed.
Boundary probes concern continuity and fixed-width comparisons only.

The exact stdin program was run with a PowerShell single-quoted
here-string: `@'`, the following text, then `'@ | python -`.

```python
import mpmath as m
m.mp.dps = 70
R = lambda p, q=1: m.mpf(p)/q
BISECTIONS = 180

def bisect(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(BISECTIONS):
        mid = (lo+hi)/2
        if f(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def branches(A, u, e, s):
    t = u+s
    X, Y = A+u+s, A+u+e-s
    c = m.sqrt(X*Y)
    k = m.sqrt(t)*(m.sqrt(X)+m.sqrt(Y))
    d = max(X, 2*m.sqrt(t*X))
    return c, k, d

def cut(A, u, e):
    gap = lambda s: branches(A,u,e,s)[1]-branches(A,u,e,s)[0]
    if gap(e) <= 0:
        return e
    if gap(0) >= 0:
        return m.mpf(0)
    return bisect(gap, m.mpf(0), e)

def raw(A, u, e):
    if e == 0:
        return m.mpf(0)
    z = cut(A,u,e)
    w = min(e,max(m.mpf(0),A/3-u))
    cuts = sorted(set([m.mpf(0),z,w,e]))
    def integrand(s):
        c,k,d = branches(A,u,e,s)
        return max(c,k)-d
    return m.quad(integrand,cuts)

def formulas(A, u, e):
    B = A+u
    z = cut(A,u,e)
    chord = lambda s: (m.sqrt(B+s)-m.sqrt(B+e-s))**2/(2*m.sqrt((B+s)*(B+e-s)))
    chain = lambda s: (m.sqrt((B+s)/(u+s))+m.sqrt((u+s)/(B+s))+m.sqrt((B+e-s)/(u+s))+m.sqrt((u+s)/(B+e-s)))/2-1
    translated = m.quad(chord,[0,z])+m.quad(chain,[z,e])
    I = m.quad(lambda s:m.sqrt((B+s)/(B+e-s)),[0,z])
    I += m.quad(lambda s:m.sqrt((u+s)/(B+e-s)),[z,e])
    c0 = m.sqrt(B*(B+e))
    p = m.sqrt(u+e)*(m.sqrt(B+e)+m.sqrt(B))
    P = max(c0,p)
    moving = P-c0-e+I
    width = P-(B+e)+I/2
    split = m.quad(lambda s:branches(A,u,e,s)[0],[0,z])
    split += m.quad(lambda s:branches(A,u,e,s)[1],[z,e])
    split -= B*e+e*e/2
    return translated,moving,width,split,z

identity_errors, smooth_errors, tie_errors = [],[],[]
boundary_errors, switch_errors = [],[]
for A in (R(1),1+(R(1093,10000)+R(10931,100000))/2,R(3,2)):
    lam = A*R(719,2500)
    for ratio in (R(5753,20000),R(1,3)-R(1,100),R(1,3)-R(1,10000)):
        u = A*ratio
        h = A/3-u
        endpoint_gap = lambda e: branches(A,u,e,e)[1]-branches(A,u,e,e)[0]
        tau = bisect(endpoint_gap,m.mpf(0),h)
        step = A*R(1,10**14)
        for index,e in enumerate((tau/2,tau,(tau+h)/2)):
            value,moving,width,split,z = formulas(A,u,e)
            cost = raw(A,u,e)
            assert z > e/2
            assert value >= e**3/(48*(A+u+e)**2)
            identity_errors += [abs(value-moving)/A,abs(cost-split)/(A*A)]
            fu = (raw(A,u+step,e)-raw(A,u-step,e))/(2*step)
            fe = (raw(A,u,e+step)-raw(A,u,e-step))/(2*step)
            errors = [abs(fu-value)/A,abs(fe-width)/A]
            (tie_errors if index==1 else smooth_errors).extend(errors)
            lower = e**3/48*(1/(A+lam+e)-1/(A+u+e))
            assert cost-raw(A,lam,e) >= lower > 0
        # Both one-sided derivative limits at the block-entry endpoint.
        at = formulas(A,u,tau)[0]
        left = formulas(A,u-step,tau)[0]
        right = formulas(A,u+step,tau)[0]
        switch_errors.extend([abs(left-at)/A,abs(right-at)/A])
        assert cut(A,u-step,tau) == tau
        assert cut(A,u+step,tau) < tau
        # Endpoint continuity only; no boundary-width optimization.
        boundary_errors.extend([
            abs(raw(A,u,h)-raw(A,u,h-step))/(A*A),
            abs(raw(A,lam,tau)-raw(A,lam+step,tau))/(A*A),
            abs(raw(A,u,step))/(A*A)])
        assert raw(A,u,0) == 0

assert len(identity_errors)==54 and max(identity_errors)<R(1,10**45)
assert len(smooth_errors)==36 and max(smooth_errors)<R(1,10**25)
assert len(tie_errors)==18 and max(tie_errors)<R(1,10**12)
assert len(switch_errors)==18 and max(switch_errors)<R(1,10**12)
assert len(boundary_errors)==27 and max(boundary_errors)<R(1,10**12)
print('PASS 70-digit diagnostics: 27 rational-scale/implicit-width pairs; 54 raw/split and translated/moving identities, normalized error < 1e-45')
print('PASS 36 smooth central differences, normalized error < 1e-25; 18 entry-tie central differences, normalized error < 1e-12')
print('PASS 27 positive derivative lower bounds and 27 strict fixed-width boundary comparisons')
print('PASS 18 one-sided entry-switch slope checks and 27 boundary continuity checks, normalized error < 1e-12')
print('NOTE: rational probes are not definitions of alpha_hat or x_*; quadrature/bisection diagnostics do not prove continuum claims')
print('mpmath',m.__version__)
```

It exited 0 with:

```text
PASS 70-digit diagnostics: 27 rational-scale/implicit-width pairs; 54 raw/split and translated/moving identities, normalized error < 1e-45
PASS 36 smooth central differences, normalized error < 1e-25; 18 entry-tie central differences, normalized error < 1e-12
PASS 27 positive derivative lower bounds and 27 strict fixed-width boundary comparisons
PASS 18 one-sided entry-switch slope checks and 27 boundary continuity checks, normalized error < 1e-12
NOTE: rational probes are not definitions of alpha_hat or x_*; quadrature/bisection diagnostics do not prove continuum claims
mpmath 1.3.0
```

Skipped as outside this delta: production pytest, standalone verify.py in
either mode, the complete width checker, publication builds and hosted CI.
The new proof uses no width minimum, production implementation, finite
certificate or publication asset. No sub-agent or independent external
reviewer was invoked.

## Artifact and provenance checks

No result, certificate, publication or generated asset was created.
Authored sources are based on the HEAD recorded above. The containing
task commit identifies their integrated revision; the final handoff
reports its SHA and normal-push result.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md | deabe45a223a9b60963275c850e766233ee5073bdb5ab7af5d57a0849d269264 |
| ops/TASK-20260906__second_block_start_domain/check_domain.py | a321de337e137fa2c704483ced2ac3fa8c199bc6a16b050507afbcf28d498b02 |

Neither exact checker nor the diagnostic writes an output file. The
pre-existing request image is unchanged and excluded from staging.

## Failed checks and negative evidence

- Some combined reads exceeded the display budget. Focused reads recovered
  the pertinent definitions, derivations and task records.
- Plain Git reads failed at the repository ownership guard. A command-local
  safe.directory argument in forward-slash form resolved the issue.
  A later attempt using the PowerShell PWD expansion did not resolve that
  guard; its diff/status subcommands failed even though the final date
  command made that combined shell invocation exit 0. Those failed
  subcommands are not counted as successful checks. The explicit
  repository-scoped commands were rerun with exit checks and exited 0.
  The personal-ignore-file permission warning did not prevent these reads.
- No mathematical checker or diagnostic failed. Source review clarified
  that z>epsilon/2 requires positive width and that the switch-velocity
  formula is used within strict regimes before taking entry limits.
- The only zero-width derivative is zero; it is outside the requested
  strict-sign domain. No positive-width exception was found or needed.

## Final diff inspection

The entire new proof and checker were read from disk, and the complete
three-file tracked diff was inspected. The dossier is read in full after
recording this evidence. Eight task paths are authorized; the existing
request image remains the only excluded untracked input.

The literal audit below was run with `python -S -`, using the same
single-quoted PowerShell here-string wrapper. It is also rerun over the
completed dossier before staging. It checks untracked source whitespace
explicitly, not just git diff output.

```python
from pathlib import Path
import ast, hashlib, re, subprocess

root = Path.cwd()
base = 'd169dd86b8aaadd19a822528e53c29f88bb9bd6f'
git = ['git','-c','safe.directory='+root.as_posix()]
def run(*args):
    result = subprocess.run(git+list(args),text=True,encoding='utf-8',capture_output=True)
    assert result.returncode == 0,(args,result.returncode,result.stderr)
    return result.stdout

task = 'ops/TASK-20260906__second_block_start_domain/'
proof = 'research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md'
allowed = {'CURRENT_STATUS.md','knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md',proof}
allowed |= {task+name for name in ('TASK_STATUS.md','TASK_LOG.md','EVIDENCE.md','check_domain.py')}
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
        assert [node.module for node in ast.walk(tree) if isinstance(node,ast.ImportFrom)] == ['fractions']
        assert not any(isinstance(node,ast.Import) for node in ast.walk(tree))
        assert not any(isinstance(node,ast.Constant) and isinstance(node.value,float) for node in ast.walk(tree))
    if name == proof:
        for target in re.findall(r'\]\(([^)]+)\)',source):
            assert (Path(name).parent/target).is_file(),target
            links += 1
protected = [
    'AGENTS.md','PROJECT_KNOWLEDGE.md','RINGMIN_REVIEW_PROTOCOL.md',
    'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md','verify.py',
    'paper_assets/ringmin_paper.tex','README.md','REPORT.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_START.md',
    'research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md',
    'research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md',
    'research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md',
    'ops/TASK-20260906__second_block_start/check_start.py',
    'ops/TASK-20260906__second_block_start/EVIDENCE.md']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show','HEAD:'+name),name
owners = [p.as_posix() for p in Path('knowledge').glob('*.md')
          if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'],owners
for name in (proof,task+'check_domain.py'):
    print('SHA256',name,hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS source audit: 8 allowed paths; tracked/untracked whitespace; checker AST, Fraction-only import and no float literals')
print(f'PASS {links} proof links and one owning ledger; {len(protected)} protected texts equal HEAD')
print('PASS git diff --check; unchanged HEAD; empty staged diff; only the existing request image excluded')

```

The recorded output is:

```text
SHA256 research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md deabe45a223a9b60963275c850e766233ee5073bdb5ab7af5d57a0849d269264
SHA256 ops/TASK-20260906__second_block_start_domain/check_domain.py a321de337e137fa2c704483ced2ac3fa8c199bc6a16b050507afbcf28d498b02
PASS source audit: 8 allowed paths; tracked/untracked whitespace; checker AST, Fraction-only import and no float literals
PASS 5 proof links and one owning ledger; 16 protected texts equal HEAD
PASS git diff --check; unchanged HEAD; empty staged diff; only the existing request image excluded
```

Sixteen selected contract, dependency and publication texts match HEAD
after newline normalization. The complete Git path inventory additionally
excludes any change to other existing proof notes/dossiers, other knowledge
ledgers, paper_assets/, results/, src/, tests/, scripts/ or publication
metadata. The single new stable claim owner is the fixed-order ledger;
PROJECT_KNOWLEDGE.md and the public record are unchanged.

Authorized integration under AGENTS.md Section 3 stages only the eight
inspected paths, inspects the complete cached diff, checks its whitespace,
commits and pushes normally to the existing origin/main, then verifies the
remote SHA and remaining request-image-only working-tree state. Integration
and mathematical acceptance remain separate.

The completed dossier was read in full and the source audit was rerun,
again exiting 0 with the identical output above. The sandbox granted
the index write, and `git add --` with exactly the eight allowed paths
exited 0. `diff --cached --check` and `diff --exit-code` both exited 0
without diff output. The complete cached diff was read in two explicit
path groups (proof/checker/ledgers/status/roadmap, then the three dossier
files). `status --short --untracked-files=all` showed exactly eight
staged task paths and the excluded request image. This final evidence/log
addition is inspected and restaged before the containing commit.

## Residual uncertainty

The continuous sign, applicable switch endpoints and boundary-infimum
reduction are resolved by exact reasoning. Imported baseline minima,
external independent acceptance and hosted CI remain separate. No
boundary-width attainment, location or uniqueness is established. There
is no claim about a sign beyond the chord-diagonal domain, finite
permutations, R_full transfer or a new R*(n) bound.
