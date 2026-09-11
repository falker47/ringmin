# Evidence

## Environment

```text
repository_head=d2fd4fc42f1cd5bfae883a40027d5f0bda704c7c
platform=Windows / PowerShell
python=3.14.3
dependency_source=standard library only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence / limitation |
|---|---|---|---|
| Unique split minimum for E>0; boundary E=0 | Exact scalar theorem | Section 11.3 factorization; coefficient identity | No tour saturation asserted |
| Improved all-tour deletion envelope | Proved corollary | Existing (36)-(39), optimized split and E<=8e | The unchanged all-tour inputs are analytic premises |
| Global scalar minimum and finite error | Exact theorem | Section 12 crossing and secant identities | Aggregate scalar sharpness only |
| New parameter, integral and coefficient brackets | Exact rational enclosures | New standalone checker | No floats, production, saved results or old-checker imports |
| New finite/asymptotic global lower bound | Proved corollary | Uniform chain bounds and nested full-feasible deletion | No geometric sharpness, limit or finite optimum certification |

No stable claim is owned by another ledger; the common-chain entry alone
owns the update. This dossier records evidence, not a second proof ledger.

## Commands and checks

Startup: `python --version` returned `Python 3.14.3` (exit 0).
Command-local safe.directory Git status returned no changed paths (exit 0);
HEAD/branch/remote inspections returned the snapshot in TASK_LOG.

All checks here were run locally by the implementing task. No external
reviewer or exact-SHA hosted CI result is claimed.

| Command/check | Exit/result | Property checked | Not checked |
|---|---|---|---|
| `python -I ops/TASK-20260911__optimized_midpoint_split/check_split.py` | 0; exact output below | New identities and rational enclosures | General tours or full geometry |
| `python -I -O ops/TASK-20260911__optimized_midpoint_split/check_split.py` | 1; `Run without -O; exact verification uses assertions.` | Disabled assertions cannot produce a false PASS | Other Python implementations |
| Repository audit below, run through `python -I -` | 0; scope/ranges/whitespace/links/import checks PASS | Protected paths and every new file | Mathematical correctness of unchanged dependencies |
| `git -c "safe.directory=$taskRepo" diff --check` | 0, no output | Tracked whitespace | Untracked files, checked separately |
| `git -c "safe.directory=$taskRepo" diff --` for the four changed tracked paths | 0; complete diff inspected | Scope, equations, classification and documentation | External review |
| Direct reads of every new dossier file and checker | Complete | Additions omitted by ordinary git diff | Hosted CI |

For the portable PowerShell Git commands above, the exact setup is
`$taskRepo = (Get-Location).Path.Replace('\', '/')`. This is a command-local
safe.directory setting only. Staged inspection/whitespace and authorized
commit/push follow the completed precommit dossier; their SHA and remote
result are reported in the final response.

Checker output, exactly:

```text
PASS exact identities: split, E-to-e, scalar crossing, inverse derivative, secant, improvement
PASS rational input gates: tau, q, pi
PASS rational D enclosure: 80 endpoint terms, positive tail, moving-q error
0.0092836183568361125168565556 < t_* < 0.0092836183568361125168565557
2.546841764900829732093748e-7 < eta_split < 2.546841764900829732093749e-7
0.1405693355294332566284894404 < C+eta_split < 0.1405693355294332566284894405
2.592952349827745447477519 < A < 2.592952349827745447477520
PASS comparison: 1.917 < eta_split/eta_new < 1.918; old sqrt bound nonbinding
PASS finite gate: n>=10^12 gives R*(n)>=B_n>(C+2.5468e-7)*n^2
PASS bounded independent identities/enclosures; no tour or geometry certificate
```

Analytic audit: (33) allows every h>0; no mesh restriction blocks its
minimizer. The E=0 infimum is not attained, and the measure identities
handle that case separately. The coefficients 43+11=54, 2*3=6,
54*8=432 and 6*8^(2/3)=24 propagate without new hypotheses. The scalar
proof includes d<=0, e=0, the crossing and unbounded e. The finite loss
uses the newly computed derivative; the clipped argument covers
19/(2*n)>=D. The unchanged (47) deletes only from full feasible
configurations, preserves original radii and common nested orders, and
includes the closing gap. Neither a chain-feasibility inference nor an
attainment assumption enters the transfer.

`pytest`, the independent optimum/frontier verifier, paper builds and tour
experiments were not run: no production code, finite certificate, frontier,
paper asset or tour-family theorem changed. They would not verify the new
scalar identities; the bounded exact checker is the proportionate check.

## Reproducible repository audit

Pass this block to `python -I -` from the repository root (or execute the
block extracted from this file). It only reads files and invokes read-only
Git commands; the base SHA is fixed so it also works after the task commit.

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

root = Path.cwd()
git = ['git', '-c', f'safe.directory={root.as_posix()}']
base = 'd2fd4fc42f1cd5bfae883a40027d5f0bda704c7c'
changed = {'CURRENT_STATUS.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md',
           'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md',
           'research/NEXT_RESEARCH_STEPS.md'}
dossier = Path('ops/TASK-20260911__optimized_midpoint_split')
new = {f'{dossier.as_posix()}/{name}' for name in
       ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_split.py')}
assert {p.as_posix() for p in dossier.iterdir()} == new
names = set(subprocess.check_output(git + ['diff', base, '--name-only'],
                                   text=True).splitlines())
assert changed <= names <= changed | new
tracked = set(subprocess.check_output(git + ['ls-tree', '-r', '--name-only', base],
                                     text=True).splitlines())
proof = 'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md'
old = subprocess.check_output(git + ['show', f'{base}:{proof}'],
                              text=True, encoding='utf-8')
current = Path(proof).read_text(encoding='utf-8')
for start, end in [('## 2. Uniform reduction', '## 11. The square-root'),
                   ('### 11.5 The crossing exponent', '## 12. Refined two-level')]:
    assert old[old.index(start):old.index(end)] == current[current.index(start):current.index(end)]
start = '### 11.1 Exact finite measure'
assert old[old.index(start):old.index('If E>0 choose h=E^(1/3).')] == current[
    current.index(start):current.index('For E>0, set u=')]
for name in sorted(changed | new):
    data = Path(name).read_bytes()
    assert data.endswith(b'\n') and not data.endswith(b'\n\n'), name
    assert all(line.rstrip(b' \t') == line for line in data.splitlines()), name
    if name.endswith('.md'):
        body = data.decode('utf-8')
        assert body.count(chr(96) * 3) % 2 == 0, name
        for link in re.findall(r'\]\(([^)]+)\)', body):
            if re.match(r'\w+://', link):
                continue
            destination, sep, anchor = link.partition('#')
            target = Path(name).parent / destination if destination else Path(name)
            assert target.exists(), (name, link)
            if sep:
                headings = re.findall(r'^#{1,6} +(.+)$', target.read_text(encoding='utf-8'), re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                assert anchor in slugs, (name, link)
source = (dossier / 'check_split.py').read_text(encoding='utf-8')
tree = ast.parse(source)
assert {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)} == {'fractions', 'math'}
assert not any(isinstance(n, ast.Import) for n in ast.walk(tree))
assert all(s not in source for s in ('read_text(', 'read_bytes(', 'open('))
assert hashlib.sha256(source.encode()).hexdigest() == '3ec5095ebbb1b686f40613b08045f977e8fe783bd73192c2d35dbb9abc8a6bbc'
print(f'PASS scope: {len(tracked - changed)} other base paths unchanged; four expected additions')
print('PASS protected ranges: Sections 2-10, 11.1-11.3 through (39), 11.5-11.6')
print('PASS eight files: whitespace, fences, local links/anchors; isolated checker imports/hash')
```

## Artifact and provenance checks

No result/certificate/publication artifact is regenerated. The new checker
is task-local source, with exact rational inputs displayed in the proof;
the eventual task commit records its generating source. No random seeds,
production imports, prior-checker imports or saved result inputs.
Checker SHA256:
`3ec5095ebbb1b686f40613b08045f977e8fe783bd73192c2d35dbb9abc8a6bbc`.

## Failed checks and negative evidence

The initial plain Git status failed on ownership before editing. A local
command option resolved it. A later attempt to use the unnormalized
PowerShell path repeated the ownership failure; forward-slash normalization
restored the successful portable command above. No config change was made.

Direct proof inspection caught a stale 40 in the transcribed d^2/m(d)
identity after the main replacements; it was corrected to 24 before final
review. This was a documentation transcription error, not an obstruction
to the optimized proof. The checker already verified the correct identity's
bound. No failed mathematical gate was replaced with numerical evidence.

A preliminary Decimal calculation at precision 70 with the displayed D
bracket midpoint and 250 cubic bisections guided the choice of rational
endpoints (local `python -I -`, exit 0). Its approximate outputs began
t=0.0092836183568361125168565556364 and eta=2.54684176490082973209e-7.
This numerical observation is not a premise; all retained endpoints were
subsequently proved with exact rational inequalities.

## Final diff inspection

The four tracked changes and four new dossier files were inspected in full.
Direct whitespace checking includes all untracked additions; ordinary Git
diff checking is recorded separately. The repository audit compares against
the fixed base, verifies 470 other tracked paths unchanged, and protects
the original floor/root/deletion inputs and the two tour-family proofs.
No generated output, paper asset, certificate, production/verifier/test
code, central index, other ledger or previous dossier changed. The owning
ledger's open-problem cross-reference and relevant roadmap endpoint were
updated with the same coefficient; no parallel thematic owner was added.

## Residual uncertainty

Optimality for the stated split does not establish the best tour crossing
constant, a tour realizing the scalar minimum, a sharp global geometric
coefficient or a normalized limit. External review and hosted CI are separate.
