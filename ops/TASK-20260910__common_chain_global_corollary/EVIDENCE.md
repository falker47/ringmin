# Evidence

## Environment

    repository_head=26b596cad859c75b396a8a77e1dcf769a793a2b8
    platform=Windows / PowerShell
    python=3.14.3
    mpmath=1.3.0
    sympy=1.14.0
    dependency_source=existing local Python; no installation
    task_mode=STRICT

## Claim ledger

The authoritative derivation is Section 8 of
research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md. Sections 1-7 supply the
unchanged quantitative premise. Mathematical acceptance by an external
independent reviewer remains separate from this task's checks.

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Full-feasible deletion bounds both induced chain roots at the same R | Exact theorem application | Section 8; published angular reformulation | Analytic, all pairs; does not assert chain-root feasibility |
| Every fixed-order R_full exceeds the threshold, then so does R* | Proved global corollary | Section 8; fixed-order infima followed by a finite minimum | Analytic; depends on the existing all-order stability theorem |
| Normalized liminf is at least C_term+10^-12 | Proved corollary | Section 8; eventual inequality | No strict liminf, sharpness or convergence claim |
| Constants and distance identity | Exact arithmetic / symbolic identities | Local command below | No production imports or saved results; not external review |

## Commands and checks

All commands below were local. Initial plain Git reads failed with dubious
ownership. Read-only Git commands with a command-local safe.directory
set to the resolved repository root succeeded:
`status --short` was empty; `rev-parse HEAD` returned the base SHA above;
`branch --show-current` returned main; `remote -v` returned
origin=https://github.com/falker47/ringmin.git for fetch and push. Sandbox
ignore-file access warnings appeared; no global Git configuration changed.
`python --version` and the mpmath/sympy import/version command exited 0,
with the versions recorded above.

The following exact check was run from the repository root via a PowerShell
literal here-string piped to `python -`. Its final form exited 0:

```python
from fractions import Fraction as Q
import runpy
import sympy as sp
checks = runpy.run_path('ops/TASK-20260910__common_chain_stability/check_stability.py')
checks['rational_gates']()
R, a, b, z = sp.symbols('R a b z', positive=True)
distance_slack = (R+a)**2 + (R+b)**2 - 2*(R+a)*(R+b)*z - (a+b)**2
angular_slack = 2*(R+a)*(R+b)*(1-2*a*b/((R+a)*(R+b))-z)
assert sp.cancel(distance_slack-angular_slack) == 0
print('Cartesian/angular slack identity: PASS')
N = 10**14
epsilon, delta = Q(1, 10**12), Q(1, 10**5)
assert N >= 102 and Q(3,17)-Q(1,N) > Q(1,6)
assert Q(23,100)-Q(1,N) > Q(1,5)
assert (1-Q(23,100))*N+1 >= 3
assert delta > epsilon
print('cutoff/floor nesting and cardinality gates: PASS')
print(f'delta-epsilon = {delta-epsilon} > 0')
print('PASS: exact algebra/rational checks only; no enumeration or numerical experiment')
```

Full output:

```text
rational gates: 12 PASS
edge margin over 1/5000: 13/340000
final numerator margin over 4*delta: 49999999/5000000000000
Cartesian/angular slack identity: PASS
cutoff/floor nesting and cardinality gates: PASS
delta-epsilon = 9999999/1000000000000 > 0
PASS: exact algebra/rational checks only; no enumeration or numerical experiment
```

The gates use Fraction and exact symbolic cancellation. Their applicability
for all n>=N follows analytically from decreasing 1/n. The distance identity
uses z=cos(Delta); positivity of (R+a)(R+b) and monotonicity of cosine on
[0,pi] yield the angular equivalence. The exact symbolic check is independent
of production code; the rational gates deliberately reuse the premise's
checker. They corroborate algebra only, not every step of the all-order proof.
No other function in that checker was called, and its main block did not run.

### Analytic failure-mode audit

- New surviving neighbors use original full pair constraints, including
  nonadjacent original pairs. No deletion rule for a merely formal chain
  or unproved angular triangle inequality is used.
- The smaller separation min(g,2*pi-g) controls every directed gap,
  including g>pi and the closing gap. Their sum is exactly 2*pi.
- Restriction is associative on nested sets, so the two tours cannot be
  selected independently. Original radii and the normalization n^2 persist.
- The threshold contradiction is proved for each fixed-order infimum by
  bounding two fixed chain roots. Only then is the finite minimum taken.
  An arbitrary infimum of quantities strictly above a threshold need not
  be strictly above it; that invalid shortcut is not part of the proof.
- Strictness for finite n yields a non-strict liminf bound. The restricted
  delta is not promoted to a global coefficient delta.

Full pytest, verify.py, the complete pre-existing stability checker, numerical
experiments, new enumeration, paper builds and hosted CI were not run.
The task changes only mathematical documentation and explicitly excludes
finite certification, upper constructions and publication work.

## Artifact and provenance checks

Not applicable: no certificate, generated numerical result, figure, paper
asset or new checker is created. The original theorem checker is read and
its exact rational function alone is reused unchanged. No random seeds.

## Failed checks and negative evidence

Initial unconfigured Git reads failed due to sandbox ownership, as above.
The first algebra command exited 1 at `sp.expand(expression)==0` after
the 12 rational gates passed: expand did not cancel rational factors.
Using sp.cancel on the same expression resolved it; the identity and all
remaining gates passed with exit 0. This was a symbolic-normalization issue,
not a counterexample to deletion or to the corollary.

## Final diff inspection

The complete tracked diff and every untracked dossier file were read in
full. A ledger sentence was corrected and the published angular-source
link added during inspection. The following exact audit ran via the same
PowerShell literal here-string to `python -`, exiting 0:

```python
from pathlib import Path
import re, subprocess
root = Path.cwd()
base = '26b596cad859c75b396a8a77e1dcf769a793a2b8'
dossier = 'ops/TASK-20260910__common_chain_global_corollary/'
expected = {'CURRENT_STATUS.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md',
            'research/NEXT_RESEARCH_STEPS.md',
            'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md'}
expected.update(dossier+name for name in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md'))
def git(*args):
    return subprocess.check_output(
        ['git', '-c', 'safe.directory='+root.as_posix(), *args], text=True)
changed = set(git('diff', '--name-only', base).splitlines())
changed |= set(git('ls-files', '--others', '--exclude-standard').splitlines())
assert changed == expected, (changed, expected)
for name in sorted(expected):
    content = (root/name).read_text(encoding='utf-8')
    assert content.endswith('\n') and not content.endswith('\n\n'), name
    assert all(line == line.rstrip() and '\t' not in line for line in content.splitlines()), name
proof = 'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md'
old = git('show', base+':'+proof)
new = (root/proof).read_text(encoding='utf-8')
body = lambda text: text.split('## 2. ',1)[1].split('## 8. ',1)[0]
assert body(old) == body(new)
statement = lambda text: text.split('Import only',1)[1].split('No search at the cutoff is needed or proposed.',1)[0]
assert statement(old) == statement(new)
links = re.findall(r'\]\(([^)]+)\)', new)
assert all((root/proof).parent.joinpath(link).is_file() for link in links)
owners = [p.name for p in (root/'knowledge').glob('*.md')
          if 'COMMON_CHAIN_QUANTITATIVE_STABILITY.md' in p.read_text(encoding='utf-8')]
assert owners == ['GLOBAL_BOUNDS_ASYMPTOTICS.md']
assert not git('diff', '--check')
protected = set(git('ls-files').splitlines()) - expected
assert not (set(git('diff', '--name-only', base).splitlines()) & protected)
print(f'scope/whitespace: {len(expected)} paths PASS (including untracked)')
print('input statement/constants and proof Sections 2-7: unchanged PASS')
print(f'local proof links: {len(links)} PASS; sole ledger owner PASS')
print(f'protected tracked paths: {len(protected)} unchanged against base; diff --check PASS')
```

Full material output (apart from the same Git ignore-file warnings):

```text
scope/whitespace: 7 paths PASS (including untracked)
input statement/constants and proof Sections 2-7: unchanged PASS
local proof links: 7 PASS; sole ledger owner PASS
protected tracked paths: 442 unchanged against base; diff --check PASS
```

This is a local engineering check of scope and document hygiene, independent
of production mathematics. It does not prove the corollary or constitute
hosted CI. No protected or generated file changed. Final record edits receive
the same audit, including explicit whitespace checks on the new additions.
The authorized integration sequence inspects the staged diff, checks its
whitespace, commits only these paths, normally pushes origin/main and compares
remote main with HEAD. The final handoff records the observed integration
results; this pre-commit record makes no hosted-CI or future-push assertion.

## Residual uncertainty

The existing stability theorem and this corollary await independent external
mathematical acceptance. The cutoff and constants are conservative and were
not optimized. No finite optimum or new certification, sharp global
coefficient, strict liminf above the stated bound, normalized limit, upper
construction or paper revision is supplied.
