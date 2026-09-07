# Evidence

## Environment

    repository_head=7b43946dffa40b96a72b15924ea987fbcd9d3b9d
    platform=Windows; PowerShell; local workspace
    python=3.14.3
    dependency_source=existing Python; standard library only
    task_mode=STRICT

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Exact x_*, alpha_hat and epsilon_b | imported exact theorems | baseline prefix/alpha/boundary notes | not re-proved | user-accepted baseline |
| True permutation for every m>=2; all cells | exact finite construction | new proof Sections 2-3 | analytic rank argument | the specified family |
| Quantitative recovery of the adjacent-block coupling | exact weak-recovery theorem | new proof Sections 4-5 | direct panel and parameter comparison | no geometric transfer |
| Bounded finite identities and rational gates | exact finite arithmetic audit | check_recovery.py | separate list constructor; no production imports | 2<=m<=512; all-m proof separate |

Canonical proof: research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md.
Sole stable owner: knowledge/FIXED_ORDER_THEORY.md.

## Commands and checks

All results below are fresh LOCAL checks. The exact input minimization
theorems are imported from the user-accepted baseline; they were not
re-proved or numerically recomputed. No hosted CI or external independent
mathematical acceptance of this delta is claimed.

Git commands use the command-local prefix
`git -c safe.directory=<repository root in forward-slash form>`.
The literal source audit below obtains that path from Path.cwd(); no
persistent Git configuration is changed.

| Exact command / Git argv after that prefix | Exit and material result | Property checked | Limitation |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | local runtime | no dependency install |
| `python -S -u ops/TASK-20260906__boundary_recovery/check_recovery.py` | 0; complete output below | rational gates, floor boxes, all finite pairs and panel bounds | bounded range; analytic proof separate |
| `python -S -`, literal stdin below | 0; output below | paths, whitespace, AST/imports, links, owner, protected sources and hashes | engineering audit |
| `diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` | 0; complete tracked diff inspected | three-file memory delta | additions read directly |
| `diff --check` | 0; no output | tracked whitespace | untracked additions checked separately below |
| `status --short --untracked-files=all` | 0; three modified and five new task paths only | complete path inventory | no unrelated changes |
| `rev-parse HEAD`, `branch --show-current`, `remote -v` | each 0; accepted SHA, main, existing origin at falker47/ringmin | integration target | read-only |
| `rg --files --hidden -g AGENTS.md -g '!.git/**'` | 0; AGENTS.md only | applicable contract inventory | read-only |

Exact checker stdout:

```text
EXACT half-wrap slack = 27541513/1000000000 > 0
PASS rational domain and small-case gates; strict-upper floor ties
PASS m=2..512: 587 floor triples; 157886 actual cyclic cells
PASS 155009 nonexception panel bounds; all exception pairs and counts
PASS all closed floor-box corners: coordinate and boundary-mass constants
PASS m=46 both d=0,2; m=100 example; 4 rejected mutations; 8 invalid inputs
NOTE: exact finite audit only; input minima and all-m weak proof are separate; no numerical diagnostics or radius transfer
```

The fixed budget was m=2..512 before execution. Arithmetic is entirely
integer/Fraction with no tolerance or random seed. Independent list
rotation/reversal and direct predecessor scoring are compared to the
proof's formula; the checker imports only fractions and writes no files.
All three strict parameter brackets are clipped into closed floor boxes.
Their Cartesian product overcovers the same exact parameters, including
correlations and limiting ties. It never chooses a decimal minimizer or
asserts that every enumerated floor triple is realized by the true minima.

The four deliberately rejected mutations cover a duplicate radius,
reflection of the union, the isolated-entry predecessor at the shared
seam, and an incorrect cyclic predecessor. The last two preserve the
high predecessor marginal, so occurrence counts alone cannot detect them.
Eight malformed constructor inputs are rejected with ValueError.

Only rational domain/small-case gates and affine coordinate bookkeeping
are needed here. No minimum sign gate, stationarity solver, certified
root enclosure, quadrature, moment mesh or numerical diagnostic is run.
Skipped as inapplicable: production pytest, either mode of verify.py,
previous-task checkers, finite geometric searches, paper builds and
hosted CI. No affected production/certification path requires those checks.

## Artifact and provenance checks

No result artifact, certificate, generated publication asset or production
output is created. The checker is a source program that writes no files.
The containing task commit identifies the integrated source revision.

| Authored source | SHA256 of local source bytes |
|---|---|
| research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md | fde3404e890e277ca279e80829454dec12fe636f61e91046b741452246f13fcb |
| ops/TASK-20260906__boundary_recovery/check_recovery.py | 1f56cc88c5a6eedea05fa531aded92d3333cf35a02ddc31a86683575f2952631 |

These are authored sources, not generated result artifacts. No previous
proof or checker is copied into the new proof's dependency chain except
the explicitly linked accepted definitions and minimization theorems.

## Failed checks and negative evidence

- Plain Git reads failed the ownership guard. Command-local safe.directory
  resolved it; the earlier combined command's final exit 0 did not make
  the failing subcommands successful.
- An isolated-entry formula at the shared seam would have the wrong
  predecessor. The actual first-block exit must be retained once.
- No positive gap, refined numerical epsilon or weak-to-root inference
  is a premise of this task.
- The finite checker passed on its first execution from the authored
  file. No failed numerical root, search or diagnostic is hidden.
- Source review replaced the unjustified descriptive word
  "transcendental" for the parameters by "implicitly defined"; no
  irrationality or transcendence assertion is needed or made.

## Final diff inspection

The full new proof was read directly and the complete three-file tracked
diff was inspected. The checker and all dossier files are also read in
full before integration; their untracked status does not omit them from
whitespace or source checks. The exact source audit was run as follows,
with a PowerShell single-quoted here-string (`@'`, program, then
`'@ | python -S -`):

```python
from pathlib import Path
import ast, hashlib, re, subprocess

root = Path.cwd()
base = '7b43946dffa40b96a72b15924ea987fbcd9d3b9d'
git = ['git', '-c', 'safe.directory='+root.as_posix()]
def run(*args):
    result = subprocess.run(git+list(args), text=True, encoding='utf-8', capture_output=True)
    assert result.returncode == 0, (args, result.returncode, result.stderr)
    return result.stdout

task = 'ops/TASK-20260906__boundary_recovery/'
proof = 'research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md'
allowed = {proof, 'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
           'research/NEXT_RESEARCH_STEPS.md'}
allowed |= {task+name for name in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_recovery.py')}
assert run('rev-parse', 'HEAD').strip() == base
assert run('diff', '--cached', '--name-only') == ''
entries = run('status', '--porcelain=v1', '--untracked-files=all', '-z').split('\0')
assert {entry[3:] for entry in entries if entry} == allowed
assert set(run('diff', '--name-only').splitlines()) == allowed-{proof}-{p for p in allowed if p.startswith(task)}
assert run('diff', '--check') == ''
for name in sorted(allowed):
    source = Path(name).read_text(encoding='utf-8')
    assert source.endswith('\n') and all(line == line.rstrip() for line in source.splitlines()), name
    assert all(ord(c) >= 32 or c in '\t\n' for c in source), name
source = Path(task+'check_recovery.py').read_text(encoding='utf-8')
tree = ast.parse(source)
compile(tree, task+'check_recovery.py', 'exec')
assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(tree))
imports = [n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
imports += [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
assert imports == ['fractions'], imports
links = re.findall(r'\]\(([^)]+)\)', Path(proof).read_text(encoding='utf-8'))
assert all((Path(proof).parent/link).is_file() for link in links)
owners = [p.as_posix() for p in Path('knowledge').glob('*.md') if Path(proof).name in p.read_text(encoding='utf-8')]
assert owners == ['knowledge/FIXED_ORDER_THEORY.md'], owners
protected = ['AGENTS.md', 'PROJECT_KNOWLEDGE.md', 'RINGMIN_REVIEW_PROTOCOL.md',
             'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md', 'verify.py', 'paper_assets/ringmin_paper.tex',
             'research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md',
             'research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md',
             'research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md',
             'research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md',
             'ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py']
for name in protected:
    assert Path(name).read_text(encoding='utf-8') == run('show', base+':'+name), name
for name in (proof, task+'check_recovery.py'):
    print('SHA256', name, hashlib.sha256(Path(name).read_bytes()).hexdigest())
print('PASS 8-path source audit; tracked/untracked whitespace; checker AST, Fraction-only imports, no float literals')
print(f'PASS {len(links)} proof links; one owning ledger; {len(protected)} protected texts equal baseline')
print('PASS complete path inventory; git diff --check; unchanged baseline HEAD; empty staged diff')
```

Exit 0, the two hashes above, followed by:

```text
PASS 8-path source audit; tracked/untracked whitespace; checker AST, Fraction-only imports, no float literals
PASS 6 proof links; one owning ledger; 11 protected texts equal baseline
PASS complete path inventory; git diff --check; unchanged baseline HEAD; empty staged diff
```

The complete path inventory permits only the eight task paths. Thus old
proofs/dossiers, other ledgers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, publication metadata, CI, README.md and REPORT.md
have no delta. Eleven selected protected texts additionally match the
accepted baseline after newline normalization. No generated path changed.
Only knowledge/FIXED_ORDER_THEORY.md owns the new stable claim;
PROJECT_KNOWLEDGE.md needs no navigation or central-guardrail update.

The final dossier and current status are audited again before staging.
Authorized integration under AGENTS.md Section 3 stages only these
eight inspected paths, inspects the complete cached diff and whitespace,
commits and pushes normally to existing origin/main. The final handoff
records the containing SHA, observed push verification and remaining
tree state. Integration is not independent mathematical acceptance.

### Final integration gates on 2026-09-07

The complete checker and dossier were read directly. After documentation
updates the literal source audit above was rerun by extracting its Python
code fence and executing it via `python -S -`: exit 0, identical hashes
and all three recorded PASS lines. The approved eight-path `git add`
then exited 0 with tool-granted access to the read-protected Git index.

The cached diff was inspected by explicit source and documentation path
groups. A truncated batched display is supplemented by earlier complete
source reads and indexed-source equality. `diff --cached --check` and
`diff --exit-code` each exited 0 without diff output. `status --short
--untracked-files=all` showed exactly eight staged paths; `rev-parse HEAD`
still returned the accepted baseline. This date/status/log update is the
only remaining source delta before restaging those same paths. Final
commit/push results and SHA are recorded in the final user handoff.

## Residual uncertainty

External mathematical review and hosted CI are separate. Exact input
minimization theorems are imported; finite checks do not prove an all-m
claim. No full-root transfer, R_full or R*(n) conclusion is supplied.
