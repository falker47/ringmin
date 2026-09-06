# Evidence

## Environment

```text
repository_head=f69ef120252ba0a89308b4fa17bbd28cab530148
platform=Windows, PowerShell
python=3.14.3
dependency_source=existing Python; stdlib only; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| All finite orders meet the arbitrary-permutation criterion and have feasible placements at their exact full roots | exact fixed-order theorem, by application of the imported criterion | proof Sections 2-3, actual cell tables and both directed paths for all pair types | explicit hypothesis matching; bounded cyclic lists and separate angular oracle | not a new independent proof of every imported theorem or a global finite certificate |
| Uniform empirical/full-score/root error | exact analytic theorem | proof Sections 4-5: global Lipschitz 4, recovery error 124/m, compact root bracket before root evaluation, estimate (15) | direct derivation from the angular formula; interval angular/full-max cross-checks | m>=2048 for the stated root error; cutoff not minimal |
| Both continuum branches and all eventual finite seam signs | exact inequalities | proof Section 6, rational sign gates and unsquared branch checks | sine oracle compared with independent half-angle arctangent intervals | finite seam sign cutoff 100000 is sufficient; smaller orders retain the full max |
| Exact C_2 and strict coefficient saving | exact coefficient identity / rational enclosure | proof (21)-(24), positive rationalized integral | denominator bounds, squared rational radical endpoints and proven arctangent remainders | implicit minimizers imported; no new optimization or decimal-root premise |
| Odd fixed-order limit | exact theorem | proof Section 8: deletion upper bound plus a separate necessary-cell lower squeeze | actual odd-cycle successor/edge incidence checks | does not apply the alternating sufficiency theorem to the odd cycle |
| Improved global limsup | proved corollary | proof Section 9, after feasibility and limits | analytic deduction, not finite search | no sharpness, global limit or finite global optimality |
| Local source/checker results | engineering facts / exact bounded checks | commands below | no production or verifier imports | not hosted CI or external acceptance |

Mathematical authority is research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md.
The fixed-order ledger owns the family, coefficient and root results;
the global ledger owns only the global consequence. The prior recovery
note supplies arbitrary-continuous-test recovery; feasibility does not
supply or replace it. The imported constants keep their source authority.

## Commands and checks

All results below are freshly run LOCAL checks. No hosted CI or external
review decision was inspected or represented as completed.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| Read-only Git status/rev-parse with per-command safe.directory | 0; clean startup tree, HEAD above | baseline and scope | mathematical acceptance |
| `python --version` | 0; Python 3.14.3 | existing runtime | unused libraries |
| `python -S -u ops/TASK-20260906__second_block_full_root/check_full_root.py` | 0 on both runs; final output below | exact branch/seam/constants, actual pairs, interval signs/errors, deletion and saving | all-m quantifiers, parameter re-optimization, global certification |
| `python -S -u ops/TASK-20260905__second_block_recovery/check_recovery.py` | 0; fresh dependency rerun, output below | recovery construction/floor/moment bookkeeping | a newly independent implementation of that existing checker |
| Complete `git diff` and direct `Get-Content` reads of new proof/checker/dossier | 0 | tracked and untracked source review | automatic proof acceptance |
| Literal PowerShell here-string piped to `python -S -`, body below | 0; output below | nine-path scope, whitespace including additions, AST, links, ownership, dependencies and source hashes | mathematical proof correctness by itself |
| Read-only `git diff --check` with per-command safe.directory, as in the audit body below | 0, no whitespace output | tracked diff whitespace | additions without the explicit audit |
| Read-only final Git status with `--untracked-files=all` | 0; 4 modifications, 5 additions | complete changed-path inventory | user approval to commit |

The first new-checker run already passed. The second was necessary after
adding independent interval checks of the angular/full-max error bound;
it retained the same counts and passed. No mathematical check failed.

Final new-checker output:

```text
PASS exact analytic gates: fixed domains, both continuum branches, Lipschitz 4, root/deletion cutoff 2048, all seam signs at m>=100000
PASS finite cover: 26 prescribed orders at 26 fixed sizes m=2..1201; 6136 actual cyclic cells; 24544 exact angular branch comparisons
PASS independent half-angle atan intervals: 157 separated signs and uniform angular/full-max error bounds; rational sqrt endpoints squared; 48-term proven remainders; exact synthetic tie gates
PASS deletion incidence: 12112 disjoint surviving directed edges; exactly two cells omitted and three odd-cycle gaps uncounted per case
PASS obstruction controls: chain-only seam, chord-only wrap, diagonalized wrap and keeping the deleted-high cell each violate an exact gate
PASS exact coefficient saving: 2290431561/10^18 < C_hat-C_2 < 2290454215/10^18; in particular C_2 < C_hat-1/(144000000*pi) and C_2 < 141913638/10^9
NOTE: exact local proof audits, not finite global certification or a numerical root/parameter optimizer; all-m feasibility and limits use the written proof.
```

The exact finite design stops at the explicit list m=2..16, 199, 200,
201, 399, 400, 401, 599, 600, 601, 1200, 1201. All floor pairs compatible
with the strict imported brackets are checked; this list happens to
have a unique pair at each size. The separate recovery rerun below
also covers the ambiguous floor cases. There is no enumeration of
other high permutations. Exact angular branch tests use R=1, m^2/8,
m^2/2, 2*m^2; independent angle intervals use R=2*m^2 on every cell
through m=12 and every seam at the other listed sizes.

The branch oracle uses rational sine squares and settles the half-angle
sum's branch before squaring. Synthetic tests include an exact tie,
both sides of it and a half-angle sum at pi/2. The independent oracle
uses theta=2*atan(sqrt(h*k/(R*(R+h+k)))). Each radical is enclosed at
denominator 10^24 using isqrt, then both endpoints are checked by
squaring. A 48-term even alternating atan sum is a lower bound, and
the next term supplies its upper remainder bound. There are no floating
values, estimated tolerances, numerical root searches, random seeds,
production imports or previous-checker imports in the new checker.

The four obstruction controls concern invalid simplifications: a
chain-only low seam contradicts its strict chord sign, a chord-only wrap
contradicts its strict chain sign, a diagonalized wrap has the wrong
actual pair, and a retained deleted-high cell contains radius 2m.
They are exact counterfactual gates, not recovered-family obstructions
or a broad mutation-testing claim. None of these simplifications is
used by the proof. The criterion supplies analytic all-pairs feasibility;
this task does not claim a fresh finite all-pairs LP or Cartesian scan.

Recovery dependency rerun output:

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

The final NOTE describes the unchanged recovery checker's own scope.
The full-root proof and new checker are separate work in this dossier.
The recovery script was not edited; its reproduced output is dependency
evidence, not a new proof by computation.

No pytest suite, verify.py mode, production scorer or paper build was
run: production, tests, certification logic/artifacts, public assets and
the standalone verifier are unchanged. The theorem is not a certificate
for any finite global optimum. No hosted CI statement is made.

The source audit is passed literally between PowerShell `@'` and
`'@`, then piped to `python -S -`. It is run before closing state edits
and again afterwards; closing review is recorded in TASK_LOG.md.

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

root = Path.cwd()
base = "f69ef120252ba0a89308b4fa17bbd28cab530148"
task = "ops/TASK-20260906__second_block_full_root/"
proof = "research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md"
checker = task+"check_full_root.py"
modified = {"CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md",
            "knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md", "research/NEXT_RESEARCH_STEPS.md"}
added = {proof, checker, task+"TASK_STATUS.md", task+"TASK_LOG.md", task+"EVIDENCE.md"}
allowed = modified | added

def git(*args):
    return subprocess.run(["git", "-c", "safe.directory="+root.as_posix(), *args],
                          capture_output=True, check=True).stdout

assert git("rev-parse", "HEAD").decode().strip() == base
assert not git("diff", "--cached", "--name-only").strip()
rows = git("status", "--short", "--untracked-files=all").decode().splitlines()
assert {line[3:] for line in rows} == allowed, rows
assert {line[3:] for line in rows if line.startswith(" M ")} == modified
assert {line[3:] for line in rows if line.startswith("?? ")} == added
assert set(git("diff", "--name-only", "HEAD").decode().splitlines()) == modified
for name in sorted(allowed):
    body = (root/name).read_text(encoding="utf-8")
    assert body.endswith("\n") and "\t" not in body, name
    assert all(line == line.rstrip() for line in body.splitlines()), name
source = (root/checker).read_text(encoding="utf-8")
tree = ast.parse(source, filename=checker)
assert {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)} == {"fractions", "math"}
assert not any(isinstance(n, ast.Import) for n in ast.walk(tree))
assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(tree))
compile(source, checker, "exec")
links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", (root/proof).read_text(encoding="utf-8"))
for link in links:
    assert ((root/proof).parent/link).resolve().exists(), link
owners = {p.as_posix() for p in Path("knowledge").glob("*.md")
          if proof in p.read_text(encoding="utf-8")}
assert owners == {"knowledge/FIXED_ORDER_THEORY.md", "knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md"}
fixed_entry = Path("knowledge/FIXED_ORDER_THEORY.md").read_text(encoding="utf-8").split(
    "### Fixed second reflected block: full-root transfer and odd-order limit")[1].split("\n## ")[0]
global_entry = Path("knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md").read_text(encoding="utf-8").split(
    "### Fixed second-block transfer: improved global upper bound")[1].split("\n### ")[0]
assert "limsup R*(n)" not in fixed_entry
assert "J=integral" not in global_entry and "C_2=C_hat" not in global_entry
assert "SECOND_BLOCK_FULL_ROOT" not in Path("PROJECT_KNOWLEDGE.md").read_text(encoding="utf-8")
deps = [
    "research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md",
    "research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md",
    "research/PERMUTED_ALTERNATING_HALVES.md",
    "research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md",
    "ops/TASK-20260905__second_block_recovery/check_recovery.py",
]
for name in deps:
    assert (root/name).read_bytes().replace(b"\r\n", b"\n") == git(
        "show", "HEAD:"+name).replace(b"\r\n", b"\n"), name
git("diff", "--check")
print("PASS source audit: 9 allowed paths (4 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation")
print(f"PASS authority: {len(links)} local proof links; separate fixed-order/global ownership; 8 dependencies unchanged")
print("PASS scope: HEAD and staged diff unchanged; protected/generated paths unchanged; git diff --check exits 0")
for name in (proof, checker, deps[-1]):
    print(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
```

## Artifact and provenance checks

No publication-facing/generated artifact, finite certificate or production
source was regenerated. Hashes below refer to actual local working-tree
bytes on the baseline above, not to a new commit or certificate generation
commit. Dependency comparisons against HEAD normalize only CRLF/LF.

```text
PASS source audit: 9 allowed paths (4 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation
PASS authority: 7 local proof links; separate fixed-order/global ownership; 8 dependencies unchanged
PASS scope: HEAD and staged diff unchanged; protected/generated paths unchanged; git diff --check exits 0
86a38b4d7b46ee81b2792677e93c26ec0f2447487bdd1350354378a91fe041c6  research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md
33417b26c4a621b0793b05391478d3b9b9d4fb0f8c4f336359220e5b87798ed7  ops/TASK-20260906__second_block_full_root/check_full_root.py
ed3b7c4d9ede014b0f1514ebf97b254302f8d91bdf1955acfd58f88decebc5ba  ops/TASK-20260905__second_block_recovery/check_recovery.py
```

## Failed checks and negative evidence

Plain rev-parse hit the ownership guard; a per-command read-only
safe.directory override resolved it without changing configuration.
Git also warns that its global ignore file is inaccessible. These
warnings do not obstruct the successful status/diff/provenance checks.
Both mathematical checker runs and the separate recovery rerun passed.
The counterfactual gates above isolate why dropping a branch or using
the wrong incidence would be invalid; no hypothesis of this construction
has failed.

## Final diff inspection

- Four tracked edits: CURRENT_STATUS.md, both pertinent thematic ledgers
  and research/NEXT_RESEARCH_STEPS.md; complete diff inspected.
- Five additions: proof, checker and this three-file dossier. Full direct
  source reads include the additions omitted by ordinary git diff.
- Explicit nine-file whitespace check: no tabs, trailing whitespace or
  missing terminal newline. Exact-only imports/AST and compilation pass.
- Seven proof links resolve. New fixed-order claims occur only in their
  owner; the global consequence occurs in its separate owning ledger.
  PROJECT_KNOWLEDGE.md needs no navigation/scope change.
- Protected inventory: all prior proof notes/dossiers, paper_assets/,
  results/, src/, tests/, scripts/, verify.py, publication metadata,
  README.md, REPORT.md, other ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md
  and RINGMIN_REVIEW_PROTOCOL.md unchanged. Eight key dependencies
  additionally compared directly against HEAD.
- git diff --check exits 0. HEAD and staged diff are unchanged.
  No Git history or GitHub write was made.

## Residual uncertainty

The fixed recovered family's full-root transfer is resolved. Constants,
block endpoints and widths are unchanged. The exact imported minimizers
were not re-certified. No larger-family or general-coupling optimum,
global sharpness, normalized global limit, finite comparison cutoff,
contact/floating assertion or expanded finite certificate is established.
The finite seam-sign cutoff is conservative, while all-m feasibility
retains the full max without needing a branch classification at small m.
Independent external proof review and manual integration remain separate.

Exactly one next atomic task: independent review of this fixed full-root
theorem and its dependency matching, including odd necessity and the
global corollary, without optimizing parameters or further blocks.
