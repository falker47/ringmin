# Evidence

## Environment

```text
repository_head=4e1aaef297d7946e9afe7f348a39ba607d985288
platform=Windows / PowerShell
python=3.14.3
dependency_source=standard library only, python -I -S
task_mode=STRICT
```

The user identifies the base HEAD as accepted. All checks below are fresh
LOCAL checks in this task. No hosted-CI or external-review result is implied.
Git uses a per-command safe.directory setting resolved from the repository
root; no persistent configuration changes are needed.

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| Unique global width maximizer on the closed region | Exact theorem | Proof Section 12.1-12.2: monotone cubic, positive multipliers, global strict cubic remainder | Analytic universal quantifiers; not tour enumeration or a geometric optimum |
| Root, multipliers and maximum-gain intervals | Rigorous rational enclosures supporting the theorem | New standalone checker, Taylor/binomial bounds and rational interval operations | No production, earlier-checker, saved-result or third-party imports; follows the stated enclosure method |
| Accepted widths are not locally maximizing | Proved corollary | Positive first-coordinate derivative, positive feasible slack and explicit rational improvement | Pertains to this width functional |
| Strict-domain supremum and global liminf transfer | Proved corollary | Fixed scaling, continuity and accepted Section 9 | No equality for actual minimax tours or normalized global limit |
| Boundary failure for every n=50000k+1 | Exact theorem | Exact floors in (43) | Checker corroborates k=1,2; universal statement is algebraic |
| Explicit strict finite gates and scaling loss | Proved corollary | Section 12.4 and formal polynomial/rational checks | Loss and A(h)/n remain present at finite n |

## Commands and checks

All paths below are repository-relative. Python commands are exact.

| Command/check | Exit/result | Property checked | Limit |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | Local interpreter | No dependency installation |
| `python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | 0; transcript below | All new arithmetic and formal-polynomial gates | Universal optimality is the accompanying analytic proof |
| `python -I -S ops/TASK-20260911__four_level_rational_witness/check_four_level.py` | 0; final line `PASS fixed four-level witness; universal quantifiers use the proved corollary` | Existing accepted witness independently rerun | Earlier checker is unmodified and is not imported |
| `python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 0; all seven PASS lines | 48 prescribed measures, 16 tour/cutoff cases, scalar signs, exact counterexample, boundaries and negative controls | Bounded corroboration; analytic dependency supplies all-order claims |
| `python -I -S -O ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | Expected 1; `RuntimeError: This checker requires enabled assertions; omit -O.` | Fail closed when assertions are disabled | Not a mathematical failure |
| `python -I -S -` with in-memory bracket controls | 0; rejects `(0.00451,0.004515)` and `(0.004525,0.00453)` | Both false isolating intervals fail the endpoint-sign gate | Controls do not mutate the source |
| `python -I -S -` with AST import audit | 0; only `fractions`, `math` | Standalone separation | Shares the published analytic enclosure formula |
| Review script below, run via `python -I -S -` | 0 | Exact scope, prefix preservation, all-file whitespace, 32 links, eight displayed interval pairs | Full human-readable diff inspection also performed |
| `git diff --check` with per-command root trust | 0; no output | Tracked whitespace | Explicit all-file check also covers untracked files |

Main checker transcript (final source):

```text
PASS formal polynomial identities: global cubic remainder and scaling loss
PASS alternating rational Taylor gates: tau, q, pi
PASS exact cubic identities; G'<0 on [0,a]; isolated root signs
PASS positive F and KKT multipliers; unique-global proof applies
PASS accepted witness is not local: positive first-coordinate derivative
0.00136820131190299900276 < D_1 < 0.00136820131190299900279
0.00196196296152142894680 < D_2 < 0.00196196296152142894683
0.00241410289623904895464 < D_3 < 0.00241410289623904895467
0.00451910758124825999999 < x_star < 0.00451910758124827000001
0.00452089241875172999999 < h_star_1 < 0.00452089241875174000001
0.00451910758124825999999 < h_star_2 < 0.00451910758124827000001
0.00734089241875172999999 < h_star_3 < 0.00734089241875174000001
0.00035105290142936543670 < lambda_1 < 0.00035105290142936940356
0.00059414888796317986218 < lambda_2 < 0.00059414888796318518264
0.00000038803240421408705 < eta_width < 0.00000038803240421408841
0.00000038785322987836585 < eta_4 < 0.00000038785322987836588
0.00000000017917433572119 < eta_width-eta_4 < 0.00000000017917433572254
0.04619642739017392470216 < relative_gain_percent < 0.04619642739051527365913
0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392
0.00000000004864271653624 < strict_rational_witness_gain < 0.00000000004864271653627
PASS boundary floor failure for n=50000k+1; no eventual unchanged gate
PASS strict scaling: t=9999/10000, N=1106195; loss < 5e-11
PASS improved rational witness: both margins 1/100000, N=100000
PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers
```

### Reproducible final audit

Run this Python block from the repository root with `python -I -S -`.
It uses base-relative tracked changes, so it can also run after committing.

```python
from pathlib import Path
import re
import subprocess
import sys

base = '4e1aaef297d7946e9afe7f348a39ba607d985288'
git = ['git', '-c', 'safe.directory=' + Path.cwd().as_posix()]
dossier = Path('ops/TASK-20260911__four_level_width_optimum')
paths = [Path('CURRENT_STATUS.md'),
         Path('knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md'),
         Path('research/NEXT_RESEARCH_STEPS.md'),
         Path('research/THREE_LEVEL_COMMON_CHAIN.md'), *sorted(dossier.glob('*'))]
assert len(paths) == 8
tracked = subprocess.check_output(git + ['diff', '--name-only', base], text=True).splitlines()
untracked = subprocess.check_output(git + ['ls-files', '--others', '--exclude-standard'], text=True).splitlines()
assert set(tracked + untracked) == {p.as_posix() for p in paths}
old = subprocess.check_output(git + ['show', base + ':research/THREE_LEVEL_COMMON_CHAIN.md'])
proof = paths[3].read_text(encoding='utf-8')
assert proof.startswith(old.decode('utf-8').replace('\r\n', '\n'))
links = 0
for p in paths:
    content = p.read_text(encoding='utf-8')
    assert content.endswith('\n') and not content.endswith('\n\n'), p
    assert not content.startswith('\ufeff'), p
    assert all(line == line.rstrip() for line in content.splitlines()), p
    if p.suffix != '.md':
        continue
    content = re.sub(r'```.*?```', '', content, flags=re.S)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if '://' in target:
            continue
        file, _, anchor = target.partition('#')
        dest = (p.parent / file).resolve() if file else p.resolve()
        assert dest.is_file(), (p, target)
        if anchor:
            headings = re.findall(r'^#{1,6}\s+(.+)$', dest.read_text(encoding='utf-8'), re.M)
            anchors = [re.sub(r'[^\w\- ]', '', h.replace('`', '').lower()).replace(' ', '-') for h in headings]
            assert anchor in anchors, (p, target)
        links += 1
print('PASS exact eight-path scope; proof Sections 1-11 preserved; protected paths unchanged')
print('PASS whitespace/UTF-8/final-newline checks on all eight files, including additions')
print(f'PASS {links} local Markdown links and anchors')
output = subprocess.check_output([sys.executable, '-I', '-S', str(dossier / 'check_width_optimum.py')], text=True)
names = {'D_1', 'D_2', 'D_3', 'eta_width', 'eta_width-eta_4',
         'relative_gain_percent', 'C_term+eta_width', 'strict_rational_witness_gain'}
count = 0
for low, name, high in re.findall(r'([0-9.]+) < (\S+) < ([0-9.]+)', output):
    if name in names:
        assert low in proof and high in proof, name
        count += 1
assert count == 8
print('PASS eight displayed interval pairs agree with the exact checker')
```

## Artifact and provenance checks

No result or publication artifacts are regenerated. The new checker is
source support for an analytic theorem, not a geometric certificate. Its
inputs are the unchanged exact cutoffs, accepted width witness, series
lengths, rational transcendental brackets and a fixed root bracket. All
operations are deterministic; there are no seeds, random samples or
third-party dependencies. The final commit records its generation source
and this dossier; the baseline is identified above.

## Failed checks and negative evidence

- Initial plain Git inspection failed ownership validation (exit 1).
  Resolved by per-command root trust; no configuration file was changed.
- One multi-operation patch was rejected atomically for duplicate targeting
  of CURRENT_STATUS.md; reapplied without duplicate operations.
- Diagnostic bounded scalar root isolation used rational interior values
  of accepted D_i brackets. It was not a proof premise. The final checker
  instead rederives enclosures and checks two fixed endpoints with exact signs.
- Two deliberately false root brackets are rejected; `-O` is rejected.
- At n=50000k+1 both boundary floor gates fail for every k>=1. This is a
  limitation of unchanged widths, not a counterexample to the liminf result.

## Final diff inspection

Four tracked paths changed: CURRENT_STATUS.md, the existing global ledger,
the roadmap and an appended proof section. Four new paths: this evidence,
TASK_STATUS.md, TASK_LOG.md and check_width_optimum.py in this dossier.
All were read in full; the proof diff was reread after aggregate output
truncation. Direct whitespace inspection covers every new file. The
accepted proof prefix (Sections 1-11), all older dossiers, other ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md, src/, tests/, verify.py, results/,
paper_assets/, README.md, REPORT.md, metadata and workflows are unchanged.
No duplicated thematic owner or incidental generated output was added.

Precommit state is READY_FOR_REVIEW. Staged-diff inspection and its
whitespace check precede the authorized commit and normal push; the final
response records the commit/remote/working-tree outcome. No historical
review is presented as a current independent check.

## Residual uncertainty

No remaining gap in this bounded variational analysis is asserted.
Independent mathematical acceptance remains pending. No sharp geometric
coefficient, normalized global limit or new finite optimum is established.
The production pytest suite, independent finite certificate verifier and
paper build were not run because none of their inputs or logic changed;
they would not certify this new variational proof. Hosted CI for the final
SHA has not been inspected.
