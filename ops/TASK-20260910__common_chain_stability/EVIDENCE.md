# Evidence

## Environment

    repository_head=0d46f6c7c2b0d44272b29803e1ba743f36732545
    platform=Windows / PowerShell
    python=3.14.3
    mpmath=1.3.0
    sympy=1.14.0
    dependency_source=existing local Python; no installation
    task_mode=STRICT

## Claim ledger

The authoritative proof is research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md.
The classification is exact theorem, after arXiv v1; bounded
computations corroborate specific identities and inequalities only.
External independent acceptance and hosted CI are separate.

| Claim | Classification | Evidence | Independence and limits |
|---|---|---|---|
| Uniform root sandwich | Exact theorem | Section 2, two angular formulas | Analytic; cosine-root diagnostics are numerical |
| Quadratic dual slack and deletion tradeoff | Exact theorem | Sections 3-4 | Analytic; assignment reference is not a cycle |
| Rational margin, floors and constants | Exact theorem | Sections 5-7 | Analytic all-order/all-integer implication |
| Bounded checks below | Exact arithmetic / numerical observations as labeled | Standalone checker | No production imports; not external review or certification |

## Commands and checks

Startup python --version
and dependency import/version checks exited 0 with the versions above.
Git status --short, rev-parse HEAD, branch --show-current and remote -v
used a command-local safe.directory equal to the resolved repository root;
all exited 0:
clean tree, base SHA above, main, origin=https://github.com/falker47/ringmin.git.
Git emitted sandbox ignore-file permission warnings, without hiding tracked
changes or preventing these commands.

The exact checker command, run locally from the repository root, was
`python ops/TASK-20260910__common_chain_stability/check_stability.py`.
The initial version passed. After adding direct floor comparisons, the
final version exited 0 in approximately 3.4 seconds with this full output:

```text
rational gates: 12 PASS
edge margin over 1/5000: 13/340000
final numerator margin over 4*delta: 49999999/5000000000000
exact run accounting: 376 masks, 1128 orientations PASS
symbolic identities: 5 PASS
numerical dual inequalities (70 dps): 98 PASS
numerical floor bounds, exact rational endpoints: 8 PASS
prescribed numerical tours (70 dps): 16, all four parities PASS
independent cosine/bisection root sandwiches: 8 PASS
PASS: bounded corroboration only; all-n theorem is analytic
```

Rational gates use Fraction with no rounding. Run accounting checks
every deletion mask leaving at least three survivors on cycles of sizes
4..8, in three orientations, using exact formal edge multiplicities.
Symbolic checks use SymPy. The remaining computations use mpmath at 70
decimal digits: 98 dual grid pairs; eight floor comparisons for rational
q=19/100,199/1000 at n=102,103,200,201; four prescribed tours at each of
n=40,41,80,81; and two cosine/bisection roots per size. The dual numerical
comparison allows 10^-60 cancellation error; roots use 160 bisection steps.
These do not infer q_* floors from decimals or test all orders numerically.

The following scope audit was run through `python -` from the repository
root (PowerShell literal here-string input). It exited 0. It is independent
of production mathematics; it checks scope and source hygiene only:

```python
from pathlib import Path
import ast, re, subprocess
root = Path.cwd()
base = '0d46f6c7c2b0d44272b29803e1ba743f36732545'
dossier = 'ops/TASK-20260910__common_chain_stability/'
expected = {'CURRENT_STATUS.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md',
            'research/NEXT_RESEARCH_STEPS.md',
            'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md'}
expected.update(dossier + name for name in
                ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_stability.py'))
def git(*args):
    return subprocess.check_output(
        ['git', '-c', 'safe.directory='+root.as_posix(), *args],
        text=True).splitlines()
changed = set(git('diff', '--name-only', base))
changed |= set(git('ls-files', '--others', '--exclude-standard'))
assert changed == expected, (changed, expected)
for name in sorted(expected):
    content = (root/name).read_text(encoding='utf-8')
    assert content.endswith('\n') and not content.endswith('\n\n'), name
    assert all(line == line.rstrip() and '\t' not in line
               for line in content.splitlines()), name
proof = root/'research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md'
links = re.findall(r'\]\(([^)]+)\)', proof.read_text(encoding='utf-8'))
assert all((proof.parent/link).is_file() for link in links)
source = (root/dossier/'check_stability.py').read_text(encoding='utf-8')
parsed = ast.parse(source)
imports = {node.module for node in ast.walk(parsed)
           if isinstance(node, ast.ImportFrom)}
imports.update(alias.name for node in ast.walk(parsed)
               if isinstance(node, ast.Import) for alias in node.names)
assert imports == {'collections', 'fractions', 'itertools', 'math', 'mpmath', 'sympy'}
owners = [p.name for p in (root/'knowledge').glob('*.md')
          if 'COMMON_CHAIN_QUANTITATIVE_STABILITY.md' in p.read_text(encoding='utf-8')]
assert owners == ['GLOBAL_BOUNDS_ASYMPTOTICS.md']
assert not git('diff', '--check')
protected = [p for p in git('ls-files') if p not in expected]
assert not (set(git('diff', '--name-only', base)) - expected)
print(f'scope/whitespace: {len(expected)} paths PASS (including untracked)')
print(f'local proof links: {len(links)} PASS; standalone imports and sole ledger owner PASS')
print(f'protected tracked paths: {len(protected)} unchanged against base; diff --check PASS')
```

Material output:

```text
scope/whitespace: 8 paths PASS (including untracked)
local proof links: 5 PASS; standalone imports and sole ledger owner PASS
protected tracked paths: 438 unchanged against base; diff --check PASS
```

Full pytest, verify.py (including frontier mode), paper builds and hosted
CI were not run: production code, finite certificates and publication
assets are unchanged, and this task explicitly stops before those layers.

## Artifact and provenance checks

No result/certificate, publication or generated numerical artifact is
created. The task-local checker is source, uses no production imports or
saved results, and has deterministic bounded input ranges. No random seeds.

## Failed checks and negative evidence

Initial unconfigured Git read: dubious-ownership error. Resolved through
a command-local safe.directory setting, without modifying configuration.
One exploratory source read used check_exact.py instead of the actual
linked check_discriminator.py; corrected before analysis. Finite Supnick
uniqueness was rejected as sufficient evidence for uniform stability.
A combined documentation patch was rejected before mutation due to
duplicate operations on CURRENT_STATUS.md; reapplied as separate updates.
The first git add of the eight inspected paths exited 1: permission denied
creating .git/index.lock in the sandbox. The identical explicit path list
was staged with tool-approved elevation and exited 0. No approval rejection
or unrelated staging occurred. This evidence addition is restaged before
the final staged inspection.

## Final diff inspection

Complete new proof, checker and dossier read; full tracked diff inspected.
The explicit audit above covers all eight paths, including untracked
additions, and all 438 protected tracked files agree with base. Five local
proof links resolve. Only GLOBAL_BOUNDS_ASYMPTOTICS.md owns the new stable
claim; previous proofs retain their historical scopes. git diff --check
exited 0. No generated or protected source changed.

Final record edits receive the same audit before staging. The authorized
integration sequence inspects the complete staged diff, runs its whitespace
check, commits only these eight paths, normally pushes origin/main, and
compares the remote main SHA with HEAD. The final handoff records those
observed results; this pre-commit record does not claim a future push or CI.

## Residual uncertainty

The constants and sufficient n cutoff are intentionally conservative.
No sharp tradeoff, best constants, geometric transfer, finite certification,
upper construction, broader optimization or external acceptance is supplied.
