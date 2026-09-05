# Evidence

## Environment

```text
repository_head=5acbd8b894bfc052f9ad93ea106a34da1e2b7087
platform=Windows, PowerShell
python=3.14.3
dependency_source=existing Python; stdlib only; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Recovery for every fixed pair on the whole domain | exact theorem | proof Sections 2-3, explicit modulus bound (10) | direct all-m argument; second finite list construction | bounded cases alone do not prove weak convergence |
| Full coefficient formula with both switches and endpoints | exact fixed-order theorem | proof Sections 4-5 | full-max replacement identity, imported root theorem | full-root dependency is inspected, not re-proved |
| Strict admissibility of x_* at every alpha | exact theorem / rational gates | proof (17)-(18), exact Fraction arithmetic | new affine domain calculation | accepted exact x_* bracket is an input |
| Unique joint minimum and upper-boundary separation | exact family-minimization theorem | proof Section 6, identity (19) and equality conditions | analytic deduction from the two user-accepted minima | neither input is newly externally accepted or re-certified |
| Actual finite full feasibility at each root | exact theorem using imported criterion | proof Section 7 | explicit gaps and the existing both-directed-path theorem | no fresh finite geometric experiment |
| Global limsup at most the existing C_hat | proved corollary | proof Section 8, separate feasibility/deletion | analytic deduction | no improved coefficient, global equality or normalized limit |

Mathematical detail is authoritative in
research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md.
The only thematic owner of recovery, definitions, the coefficient formula
and joint/fixed-order results is knowledge/FIXED_ORDER_THEORY.md.
The global ledger retains the existing limsup bound and adds only a
cross-reference to the family result. No new stable claim is duplicated
in another thematic ledger or PROJECT_KNOWLEDGE.md.

## Commands and checks

All results below are fresh LOCAL checks. No hosted CI, external review,
or historical checker output is being represented as a current result.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| Startup Git status and rev-parse, with repository-scoped safe.directory | 0; clean tree, HEAD above | starting scope and provenance | mathematical acceptance |
| `python --version` | 0; `Python 3.14.3` | existing runtime | third-party libraries, which are unused |
| `python -S -u ops/TASK-20260905__reflected_prefix_joint_minimum/check_joint_minimum.py` | 0; six lines below | new exact rational gates, 1692 valid bookkeeping cases and 8 invalid inputs | all-domain proof, accepted minima or finite geometric certification |
| Literal PowerShell here-string piped to `python -S -`, exact audit body below | 0; three audit lines and eight hashes below | allowed paths, whitespace including untracked files, imports/compilation, links and unchanged dependencies | independent mathematical proof review |
| Read-only `git diff`, `git diff --check`, `git status --short --untracked-files=all`, each with repository-scoped safe.directory | 0; four tracked edits, five additions, no whitespace error | tracked delta and full path inventory | untracked content without the separate full reads |

Exact checker output:

```text
PASS rational gates: lower margin 47/1250; wrap margin 1369/20000; eta 1369/60000; boundary cutoff 18631/60000>XH
PASS floor bookkeeping: 796 admissible (m,s,q) states, 1592 endpoint/interior cases, m=2..24
PASS boundary probes: 100 cases; gaps 1/256 and 1/2^40; both alpha endpoints/parities and lambda=A/3 ties
PASS 13 coverage gates: occurrence/involution, cyclic pairs, coincident exception counts, complete partitions, 3/m errors
PASS domain rejection: 8 cases including excluded wrap
NOTE: bounded exact bookkeeping only; accepted minima and imported full-feasibility/root theorems are not re-certified.
```

The finite audit has a fixed stopping rule: m=2..24 and all floor indices
s=0..floor(m/2), even q<m-s whose parameter cell is nonempty. Such a cell
exists exactly when max(1/4,q/m)<min((q+2)/m,1-s/m). Its first witness is
alpha=s/m, lambda=max(1/4,q/m). A second witness uses the relative-interior
midpoints specified in the checker, retaining the alpha=1/2 face.

The further 80 near-wrap probes are exactly alpha in {0,1/10,1/3,1/2},
b-lambda in {1/256,1/2^40}, and m in {2,3,4,5,7,8,15,16,23,24}.
Twenty more probes use lambda=(1+alpha)/3, alpha in {0,1/4}, at the same
ten m. No parameter grid is used to infer a minimum or an all-domain sign.

Each valid case compares the formula for J/H with rotation of an increasing
high list followed by reversal of its even slots. It checks exact
occurrence/involution, the actual cyclic/junction/wrap pairs, the unioned
exception counts, every cell's partition membership, branch agreement and
every nonexceptional 3/m error. It includes the q=0,r=1 endpoint count.
All arithmetic is exact integers/Fraction; no precision, tolerance, seed,
quadrature, finite radius scorer or permutation optimizer is involved.

The rational gate checks concern only the newly used domain margins,
upper-boundary cutoff and endpoint values of analytic affine gates.
They do not sample the signs of E or differentiate the previous alpha
formula. No new E, D, alpha_hat or x_* computation is needed.

Skipped as outside this proof-only delta: previous minimization checkers,
production pytest, verify.py in either frontier mode, geometric scans,
publication builds, generated assets and hosted CI. The code, certificate
artifacts and imported proofs that would justify those runs are unchanged.

## Artifact and provenance checks

No result/certificate or publication asset is generated or modified.
The proof and checker are authored sources based on the HEAD above;
they are uncommitted and have no separate generation commit.
The checker is deterministic, has fixed budgets and writes no files.

The audit below also compares six imported proof sources to HEAD after
CRLF/LF normalization. Its SHA256 lines are hashes of the actual local
source bytes, not normalized hashes:

```text
PASS source audit: 9 allowed files (4 modified, 5 new); all-file whitespace, checker AST/imports and in-memory compilation
PASS provenance: 7 local proof links; HEAD and staged diff unchanged; protected/generated paths unchanged
PASS dependencies: 6 proof sources agree with HEAD after newline normalization
20836fdf27dafa381a71cbc442461d99df363837196e78f9066007e34dbf32fa  research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md
29ee5149e8d68f88c4550ae1f8afce325023f6ab27d1745805c909f0364dae85  ops/TASK-20260905__reflected_prefix_joint_minimum/check_joint_minimum.py
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db  research/SHIFTED_ALTERNATING_HALVES.md
c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab  research/PERMUTED_ALTERNATING_HALVES.md
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63  research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md
485fefd9238d97799cf0801a395fb1ab077707c3b007e3a4361c2ef0588608b1  research/PERMUTED_HALVES_REFLECTED_PREFIX.md
407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3  research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md
ad166ea8ccfdc1a60073e5ff2f005a4299b678416f0f1358ca096a58571c6751  research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md
```

Exact audit body, executed through a literal PowerShell here-string
(`@'` / `'@ | python -S -`). It performs no filesystem writes:

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

root = Path.cwd().resolve()
base = "5acbd8b894bfc052f9ad93ea106a34da1e2b7087"
dossier = "ops/TASK-20260905__reflected_prefix_joint_minimum/"
proof = "research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md"
checker = dossier+"check_joint_minimum.py"
allowed = {
    "CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md",
    "knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md", "research/NEXT_RESEARCH_STEPS.md",
    proof, checker, dossier+"TASK_STATUS.md", dossier+"TASK_LOG.md",
    dossier+"EVIDENCE.md",
}

def git(*args):
    return subprocess.run(
        ["git", "-c", "safe.directory="+root.as_posix(), *args],
        check=True, capture_output=True).stdout

assert git("rev-parse", "HEAD").decode().strip() == base
assert not git("diff", "--cached", "--name-only").strip()
rows = git("status", "--short", "--untracked-files=all").decode().splitlines()
assert {row[3:] for row in rows} == allowed, rows
assert sum(row.startswith(" M ") for row in rows) == 4, rows
assert sum(row.startswith("?? ") for row in rows) == 5, rows
for name in sorted(allowed):
    body = (root/name).read_text(encoding="utf-8")
    assert body.endswith("\n"), name
    assert "\t" not in body, name
    assert all(line == line.rstrip() for line in body.splitlines()), name
source = (root/checker).read_text(encoding="utf-8")
parsed = ast.parse(source, filename=checker)
assert {node.module for node in ast.walk(parsed)
        if isinstance(node, ast.ImportFrom)} == {"fractions"}
assert not any(isinstance(node, ast.Import) for node in ast.walk(parsed))
compile(source, checker, "exec")
links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)",
                   (root/proof).read_text(encoding="utf-8"))
for link in links:
    assert ((root/proof).parent/link).resolve().exists(), link
git("diff", "--check")
print("PASS source audit: 9 allowed files (4 modified, 5 new); "
      "all-file whitespace, checker AST/imports and in-memory compilation")
print(f"PASS provenance: {len(links)} local proof links; "
      "HEAD and staged diff unchanged; protected/generated paths unchanged")
dependencies = [
    "research/SHIFTED_ALTERNATING_HALVES.md",
    "research/PERMUTED_ALTERNATING_HALVES.md",
    "research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md",
]
for name in dependencies:
    actual = (root/name).read_bytes()
    expected = git("show", "HEAD:"+name)
    assert actual.replace(b"\r\n", b"\n") == expected.replace(b"\r\n", b"\n"), name
print("PASS dependencies: 6 proof sources agree with HEAD after newline normalization")
for name in [proof, checker, *dependencies]:
    print(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
```

## Failed checks and negative evidence

- Plain Git startup commands exited 1 on the ownership guard. Repeating
  with per-command safe.directory succeeded without writing configuration.
  Git warned that the user-global ignore file was inaccessible; this was
  not a repository change or mathematical blocker.
- The first dossier patch was rejected before application because it
  requested delete/add of one path in a single patch. It was corrected.
- A later log-only patch used a nonexistent context line and was rejected
  without changes; the entry was then appended with the correct context.
- The new exact checker passed on its first run. No counterexample was
  found. Direct proof review corrected a reference to the exceptional
  cells and disambiguated the compact-box name; no proof gate changed.

## Final diff inspection

- Complete `git diff` inspected: CURRENT_STATUS.md, the fixed-order ledger,
  the global-ledger cross-reference and the roadmap only.
- All five untracked additions read in full: the proof, checker and three
  dossier files. Ordinary Git diff was not used to claim their inspection.
- Explicit whitespace check across all nine allowed files passes, including
  every untracked addition; the exact checker source compiles in memory.
- `git diff --check` exits 0 with no output. The full status inventory is
  exactly four modified files and five additions, as asserted by the audit.
- Seven local proof links exist. Eight source hashes are recorded above;
  the six imported proofs match HEAD after line-ending normalization.
- No incidental change to previous proof notes/dossiers, paper_assets/,
  results/, src/, tests/, scripts/, verify.py, README.md, REPORT.md,
  publication metadata, other knowledge ledgers, PROJECT_KNOWLEDGE.md,
  AGENTS.md or RINGMIN_REVIEW_PROTOCOL.md. Generated assets are unchanged.
- No claim duplication across thematic owners. HEAD is unchanged and the
  staged diff is empty. Task state is READY_FOR_REVIEW, not external acceptance.
- The final read-only gate repeats the audit above after the handoff-only
  metadata changes and re-inspects final status/diff. The mathematical
  checker is not rerun: its source and premises remain unchanged.

## Residual uncertainty

The two user-accepted minimum theorems and imported full-feasibility/root
theorems remain explicit dependencies. This task does not re-prove or
externally accept them. Independent external review of the new extension
is pending. The result establishes leading-coefficient optimality within
the stated fixed-parameter family and actual feasibility of its orders.
Finite-m family minima, other alpha regimes, recovery at/crossing the wrap,
general permutation/coupling minima, geometric global optimality,
normalized global limit existence and enlarged finite certification are
not established. The global upper coefficient stays C_hat.
