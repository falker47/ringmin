# Evidence

## Environment

```text
repository_head=01a944ad5d08234755dcd12fd7f4d9ba0b683d9c
platform=Windows, PowerShell
python=3.14.3
dependency_source=existing Python; stdlib only; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Two disjoint parity reversals give a high permutation for every m>=2 | exact finite construction theorem | proof Sections 2-3, explicit occurrence partition and involution | separate rotated-list constructor checks the formula | bounded checks do not establish the all-m quantifier |
| Complete cyclic predecessors, floor/parity/seam counts and exceptional mass | exact theorem | proof (5)-(10), four count regimes and finite m=600 witness | actual lists scored cyclically; all bracket-compatible floor pairs audited | unknown exact floors are overcovered, never guessed |
| Simultaneous recovery of prefix, fixed second block and diagonal tail | exact weak-recovery theorem | proof Section 4 and estimate (12) | nonsymmetric interval moments and affine coordinate enclosures audit the bookkeeping | external proof review remains separate; no general balance sufficiency |
| Empirical g-integrals converge to this continuum cost | proved corollary | continuity of g on D and (12) | analytic consequence, no radius scorer used | does not identify a full radius or geometric bound in this task |
| Bounded checks, source ownership and protected-path preservation | engineering fact / exact local computational checks | commands and audits below | stdlib only, no production/verifier/old-checker imports | not hosted CI, global finite certification or external acceptance |

Mathematical authority is research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md.
The sole thematic owner is knowledge/FIXED_ORDER_THEORY.md. Its continuum
entry now points to the separate recovery result; no claim was duplicated
in another ledger or PROJECT_KNOWLEDGE.md. The global C_hat owner is unchanged.

## Commands and checks

All checks are fresh LOCAL results. Neither hosted CI nor external review
was inspected or represented as completed.

| Command/check | Exit/result | Property checked | Not checked |
|---|---|---|---|
| Read-only Git status/rev-parse with per-command safe.directory | 0; clean tree, HEAD above | baseline and local scope | mathematical acceptance |
| `python --version` | 0; `Python 3.14.3` | existing runtime | unused third-party libraries |
| `python -S -u ops/TASK-20260905__second_block_recovery/check_recovery.py` | 0 on its first and only run; exact output below | bounded occurrences, cyclic cells, floor boxes, interval moments and negative gates | all-m proof, minimizer re-certification, root transfer or geometry |
| `Get-Content -Raw` for each new proof/checker/dossier; complete read-only `git diff` | 0; source content reviewed; closing dossier review recorded in log | full tracked and untracked content | automatic mathematical acceptance |
| Literal PowerShell here-string piped to `python -S -`, body below | 0; output below | eight allowed paths, whitespace, AST, links, ownership and protected dependencies | independent mathematical theorem certification |
| Read-only `git diff --check` and `git status --short --untracked-files=all`, with per-command safe.directory | 0; no whitespace output; 3 modified paths and 5 additions | tracked whitespace and final inventory | additions without the explicit source audit |
| `Get-FileHash` on the proof and checker with `-Algorithm SHA256` | 0; hashes below | source provenance after wording review | a committed generation artifact |

Exact checker output:

```text
PASS exact fixed gates: block separation, wrap separation, all small-m thresholds; 9 exact polynomial integration oracles
PASS bounded floor cover: 1244 prescribed orders, m=2..1201; 42 sizes with multiple bracket-compatible floor pairs
PASS independent lists: 759032 cyclic cells; exact occurrences, involution, both orientations, all junction/wrap pairs and complete counts
PASS coordinate enclosures: 732857 nonexceptional cells at m>=200 covered by <=5/m at the exact implicit parameters
PASS floor boundaries: all 600 residues twice; 8 alpha and 37 lambda lower-floor ties; empty/length-2 blocks; exact m=600 witness
PASS independent interval moments: 121 tests at 11 fixed sizes; nonsymmetric tests, second-block moment and (7L+32M)/m bound
PASS negative gates: 6 invalid inputs and 4 faulty occurrence/parity/predecessor variants rejected
NOTE: exact bounded bookkeeping checks; analytic proof supplies all-m continuous-test recovery. No parameter optimization, root transfer or geometric bound.
```

The bounded design stops at m=1201. It covers each residue modulo 600
twice; p and d have residual periods 6 and 200. The 42 ambiguous sizes
produce ALL integer floor pairs allowed by the imported strict rational
brackets, with no need to decide which one the exact parameters use.
Their possible alpha/lambda correlation can only remove cases from this
cover. Closed floor-box endpoints include hypothetical integer ties;
the 8/37 tie counts do not claim the implicit minimizers attain them.

The independent implementation rotates an increasing list and reverses
two slices. The checker compares it with the arithmetic rank formula,
counts both orientations, and scores every predecessor directly from
the list. It separately verifies finite baseline preservation. The four
faulty variants duplicate a high, omit the second reversal, reverse all
second-block positions instead of even ones, and keep the high marginal
but use the wrong predecessor incidence. Each is rejected.

The interval integrator substitutes affine high coordinates into eleven
polynomials and integrates powers exactly, separately from the finite
integer moment sums. Tests include t*x versus t*y, t*x^2 versus t*y^2,
t*(x-y), and (x-y)^2. A reflection substitution separately checks the
last integral lambda^3/3+epsilon^3/3, retaining the second block. The
intervals enclose the SAME exact alpha/lambda, not surrogate minimizers.
Nine exact monomial integrals audit the integrator itself. All arithmetic
uses integers/Fraction; no tolerance, precision setting, random seed,
floating quadrature, unbounded search or numerical sign premise is used.

No pytest suite, verify.py mode, old checker, radius scorer or paper build
was run: production code, finite certification logic/artifacts, root
theorems and publication files are unchanged. The imported minima and
continuum saving are dependencies, not newly re-certified claims.

The source audit below was passed literally between PowerShell `@'` and
`'@`, then piped to `python -S -`. Initial and closing audits are separate
from the mathematical checker; closing status edits are reviewed again.

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

root = Path.cwd()
base = "01a944ad5d08234755dcd12fd7f4d9ba0b683d9c"
task = "ops/TASK-20260905__second_block_recovery/"
proof = "research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md"
checker = task+"check_recovery.py"
tracked = {"CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md", "research/NEXT_RESEARCH_STEPS.md"}
allowed = tracked | {proof, checker, task+"TASK_STATUS.md", task+"TASK_LOG.md", task+"EVIDENCE.md"}
def git(*args):
    return subprocess.run(["git", "-c", "safe.directory="+root.as_posix(), *args], capture_output=True, check=True).stdout
assert git("rev-parse", "HEAD").decode().strip() == base
assert not git("diff", "--cached", "--name-only").strip()
rows = git("status", "--short", "--untracked-files=all").decode().splitlines()
assert {row[3:] for row in rows} == allowed, rows
assert sum(row.startswith(" M ") for row in rows) == 3
assert sum(row.startswith("?? ") for row in rows) == 5
assert set(git("diff", "--name-only", "HEAD").decode().splitlines()) == tracked
for name in sorted(allowed):
    body = (root/name).read_text(encoding="utf-8")
    assert body.endswith("\n") and "\t" not in body, name
    assert all(line == line.rstrip() for line in body.splitlines()), name
source = (root/checker).read_text(encoding="utf-8")
tree = ast.parse(source, filename=checker)
assert {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)} == {"fractions"}
assert not any(isinstance(node, ast.Import) for node in ast.walk(tree))
assert not any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
compile(source, checker, "exec")
links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", (root/proof).read_text(encoding="utf-8"))
for link in links:
    assert ((root/proof).parent/link).resolve().exists(), link
owners = [path.as_posix() for path in Path("knowledge").glob("*.md") if proof in path.read_text(encoding="utf-8")]
assert owners == ["knowledge/FIXED_ORDER_THEORY.md"], owners
assert "SECOND_BLOCK_RECOVERY" not in Path("PROJECT_KNOWLEDGE.md").read_text(encoding="utf-8")
deps = [
    "research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md",
    "research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md",
    "research/PERMUTED_ALTERNATING_HALVES.md",
    "knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md",
]
for name in deps:
    assert (root/name).read_bytes().replace(b"\r\n", b"\n") == git("show", "HEAD:"+name).replace(b"\r\n", b"\n"), name
git("diff", "--check")
print("PASS source audit: 8 allowed paths (3 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation")
print(f"PASS authority: {len(links)} local proof links; sole fixed-order ledger owner; 7 dependencies/global ledger unchanged")
print("PASS scope: HEAD and staged diff unchanged; protected/generated paths unchanged; git diff --check exits 0")
for name in (proof, checker):
    print(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
```

## Artifact and provenance checks

No published/generated artifact, finite certificate, production code or
verifier was regenerated. These are working-tree source hashes on the
baseline above, not a certificate generation commit. Hashes use actual
local file bytes; the seven comparisons against HEAD normalize CRLF/LF
only. The initial proof hash preceded the final notation clarification;
the final hash below was obtained after that clarification.

```text
PASS source audit: 8 allowed paths (3 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation
PASS authority: 6 local proof links; sole fixed-order ledger owner; 7 dependencies/global ledger unchanged
PASS scope: HEAD and staged diff unchanged; protected/generated paths unchanged; git diff --check exits 0
4782ba5ee10299d3dcbb01f0fc98ccfc90c1db37f658b4fe43fae0590bfe70c7  research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md
ed3b7c4d9ede014b0f1514ebf97b254302f8d91bdf1955acfd58f88decebc5ba  ops/TASK-20260905__second_block_recovery/check_recovery.py
```

## Failed checks and negative evidence

Plain rev-parse hit the ownership guard; per-command read-only
safe.directory resolved it without writing config. Git also warns that
the user-global ignore file is inaccessible. One document patch was
rejected for targeting CURRENT_STATUS.md twice; ordinary update patches
resolved it with no partial change. The mathematical checker had no
failed run. The four deliberately faulty variants are negative test
evidence about the implementation, not realizability counterexamples.

## Final diff inspection

- Three tracked edits: CURRENT_STATUS.md, knowledge/FIXED_ORDER_THEORY.md,
  research/NEXT_RESEARCH_STEPS.md. Complete tracked diff inspected.
- Five additions: recovery proof, checker, TASK_STATUS.md, TASK_LOG.md,
  EVIDENCE.md in this dossier. Full proof/checker reads completed;
  final full dossier reads and closing-state audit recorded in TASK_LOG.
- Explicit all-eight-file whitespace check, including additions: no
  trailing whitespace/tabs or missing terminal newline. AST confirms
  exact-only arithmetic/imports; in-memory compilation succeeds.
- `git diff --check`: exit 0, no output. All six proof links exist;
  the recovery claim has exactly one thematic ledger owner.
- Protected paths checked by the changed-path inventory: previous proof
  notes/dossiers, paper_assets/, results/, src/, tests/, scripts/,
  verify.py, publication metadata, README.md, REPORT.md, other ledgers,
  PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md unchanged.
  Seven key proof/global-ledger files also agree directly with HEAD.
- HEAD and staged diff unchanged. No Git history or GitHub writes.

## Residual uncertainty

The exact finite recovery question is resolved constructively. This is
one coupling at fixed alpha_hat, lambda=(1+alpha_hat)*x_* and width 1/100;
there is no moving-block or general balanced-coupling recovery theorem.
No new full-radius limit, finite-m radius comparison, geometric/global
bound, certificate scope or contact/floating claim is asserted.
The imported minima and continuum saving retain their source authority
and separate external-review status. Local tests alone do not accept
those theorems or this proof. No hosted CI result was inspected.

Exactly one next atomic task is the separately justified full-root
transfer for this same fixed recovered family, as stated in TASK_STATUS.md
and CURRENT_STATUS.md. It was not begun here.
