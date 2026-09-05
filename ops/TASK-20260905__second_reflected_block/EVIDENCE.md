# Evidence

## Environment

```text
repository_head=a7c2afbeadcd2d8de69f79c073cf5f6379c06345
platform=Windows, PowerShell
python=3.14.3
dependency_source=existing Python; stdlib only; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| Each high marginal and local balance preserved exactly | exact continuum theorem | proof Section 2, reflection substitution and conditional swap | direct measure argument, separate polynomial pullbacks | necessary conditions do not supply finite recovery |
| Full-max formula and fixed-u variation | exact continuum theorem | proof Sections 3-6, both negative integral identities and the positive part at the switch | analytic proof; separate formal Taylor arithmetic | pointwise in fixed u; no moving-u classification |
| Strict continuum witness at u=1/3, epsilon=1/100 | exact counterexample | proof Section 7; four rational margins and two exact cost checks | rationalized integral bound plus independent midpoint upper enclosure | not a finite geometric upper bound |
| Baseline is not locally minimal among balanced couplings | proved continuum corollary | shrinking rational witness and total-variation bound | analytic consequence of replacement formula | original one-prefix family minimum remains valid |
| Width derivative is zero everywhere, despite strict descent off the switch | exact theorem / negative discriminator | proof (4)-(5), explicit small-width sign ranges | exact cancellation and remainder estimates | a negative width first derivative is not claimed |
| Source scope, imports and provenance | engineering fact | audit below and complete tracked/untracked review | read-only Git and stdlib source inspection | local verification is not external acceptance or hosted CI |

Mathematical detail is authoritative in
research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md. The sole thematic
owner is knowledge/FIXED_ORDER_THEORY.md. No new stable claim was copied
to another knowledge ledger or PROJECT_KNOWLEDGE.md; the global ledger
and existing C_hat bound are unchanged.

## Commands and checks

All results below are fresh LOCAL checks. No hosted CI, external review,
or historical checker output is represented as having been run here.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| Startup Git status/rev-parse with per-command safe.directory | 0; clean tree, HEAD above | baseline and scope | mathematical acceptance |
| `python --version` | 0; `Python 3.14.3` | existing runtime | third-party packages, which are unused |
| `python -S -u ops/TASK-20260905__second_reflected_block/check_second_block.py` | 0 on both runs; exact output below | domain/branch gates, formal Taylor algebra and rational cost enclosure | all-domain proof, baseline minima or finite recovery |
| Literal PowerShell here-string piped to `python -S -`, body below | 0; three audit lines and six hashes below | all eight paths including untracked whitespace, AST, links and dependencies | independent mathematical acceptance |
| Read-only `git diff`, `git diff --check`, `git status --short --untracked-files=all`, with the same safe.directory option | 0; three tracked edits and five additions; no whitespace errors | complete tracked delta and path inventory | untracked content without the separate full reads |

Exact checker output:

```text
PASS exact witness gates: prefix separation=42554539/3000000000>0; pre-wrap separation=164207/300000>0; chord gate=693/10000>0; M<3/2=15707/300000>0
PASS sign-safe radical oracle: 49 square-root cases including ties; 2 invalid inputs; 9 chord/mixed/chain endpoint probes
PASS reflection pullbacks: moments 0..8, mass and involution; conditional balance is the exact coordinate swap in the proof
PASS formal Taylor algebra: chord moment -1/24; 3 chain coefficients -1/(24*u*B); both rationalization moments
PASS switch: scaled root 1/8; positive-part moment 1/64; remainder 49/48; explicit positive margin 47/6144
PASS independent exact cost enclosure: 8 midpoint panels with rational root upper bounds prove raw Delta<-epsilon^3/36 at A=1+AH
NOTE: exact continuum checks only; no finite recovery, new global bound, re-certification of minima or numerical optimization.
```

The bounded design is fixed in the checker: 49 rational-square oracle
cases, 2 invalid radicands, 9 endpoint probes, reflection moments 0..8,
three exact chain Taylor probes, normalized chord/switch formal
coefficients and eight midpoint panels for ONE witness. It stops after
these checks; no search or optimization occurs. Square-root upper bounds
use integer squares on a dyadic grid of denominator 2^80. All subsequent
arithmetic and inequalities are exact Fraction/integer operations; there
is no floating precision, tolerance, random seed or numerical diagnostic.

The raw cost check is a rigorous upper enclosure: the chord is concave,
so midpoint quadrature bounds its integral from above, each root is
bounded from above by an integer-square gate, and the diagonal integral
is exact. The analytic increase of the cost difference with A permits
the single AH endpoint to cover the imported alpha bracket. This check
uses the original chord integrand, independently of the saving integral
used for the analytic witness. Both implementations use the same stated
mathematical cost; neither imports production, verify.py or earlier
checkers. The finite polynomial/endpoint probes support bookkeeping,
whereas the proof establishes all quantifiers.

No pytest suite, verify.py mode, paper build, finite radius scoring or
older minimizer checker was run: no implementation, finite certificate,
recovery or publication output changed. The imported minimizer theorems
remain dependencies, not freshly re-certified results.

Exact source-audit body, supplied between PowerShell `@'` and `'@`,
then piped to `python -S -`:

```python
from pathlib import Path
import ast
import hashlib
import re
import subprocess

root = Path.cwd()
base = "a7c2afbeadcd2d8de69f79c073cf5f6379c06345"
task = "ops/TASK-20260905__second_reflected_block/"
proof = "research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md"
checker = task+"check_second_block.py"
allowed = {
    "CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md",
    "research/NEXT_RESEARCH_STEPS.md", proof, checker,
    task+"TASK_STATUS.md", task+"TASK_LOG.md", task+"EVIDENCE.md",
}
def git(*args):
    result = subprocess.run(
        ["git", "-c", "safe.directory="+root.as_posix(), *args],
        capture_output=True, check=True)
    return result.stdout

assert git("rev-parse", "HEAD").decode().strip() == base
assert not git("diff", "--cached", "--name-only").strip()
rows = git("status", "--short", "--untracked-files=all").decode().splitlines()
assert {row[3:] for row in rows} == allowed, rows
assert sum(row.startswith(" M ") for row in rows) == 3
assert sum(row.startswith("?? ") for row in rows) == 5
assert set(git("diff", "--name-only", "HEAD").decode().splitlines()) == {
    "CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md",
    "research/NEXT_RESEARCH_STEPS.md",
}
for name in sorted(allowed):
    body = (root/name).read_text(encoding="utf-8")
    assert body.endswith("\n") and "\t" not in body, name
    assert all(line == line.rstrip() for line in body.splitlines()), name
source = (root/checker).read_text(encoding="utf-8")
tree = ast.parse(source, filename=checker)
assert {node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)} == {"fractions", "math"}
assert not any(isinstance(node, ast.Import) for node in ast.walk(tree))
assert not any(isinstance(node, ast.Constant) and isinstance(node.value, float)
               for node in ast.walk(tree))
compile(source, checker, "exec")
links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)",
                   (root/proof).read_text(encoding="utf-8"))
for link in links:
    assert ((root/proof).parent/link).resolve().exists(), link
git("diff", "--check")
print("PASS source audit: 8 allowed files (3 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation")
print(f"PASS provenance: {len(links)} local proof links; HEAD/staged diff unchanged; protected/generated paths unchanged")
dependencies = [
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md",
    "research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md",
    "research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md",
]
for name in dependencies:
    actual = (root/name).read_bytes()
    expected = git("show", "HEAD:"+name)
    assert actual.replace(b"\r\n", b"\n") == expected.replace(b"\r\n", b"\n"), name
print("PASS dependencies: 4 proof sources agree with HEAD after newline normalization")
for name in [proof, checker, *dependencies]:
    print(hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name)
```

## Artifact and provenance checks

No published/generated artifact, certificate, production code or verifier
was regenerated. These are source hashes on the baseline above plus the
new working-tree proof/checker, not a generation commit for a certificate.
Hash bytes use the local file's actual newline convention; dependency
comparisons against HEAD normalize CRLF/LF only.

```text
PASS source audit: 8 allowed files (3 modified, 5 new); all-file whitespace, exact-only AST and in-memory compilation
PASS provenance: 4 local proof links; HEAD/staged diff unchanged; protected/generated paths unchanged
PASS dependencies: 4 proof sources agree with HEAD after newline normalization
ba4107949f5c6cbbf5b423e6f2379562478665edee61bbe68f25e1790b7242e8  research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md
25d8faf18f4093bfe4e6406a07e792a3034c88e69cc116e142447413605210f9  ops/TASK-20260905__second_reflected_block/check_second_block.py
20836fdf27dafa381a71cbc442461d99df363837196e78f9066007e34dbf32fa  research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md
407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3  research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md
ad166ea8ccfdc1a60073e5ff2f005a4299b678416f0f1358ca096a58571c6751  research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63  research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md
```

## Failed checks and negative evidence

- Plain Git first exited 1 on the ownership guard. Per-command
  safe.directory enabled read-only inspection without writing config.
  Git also warned that the user-global ignore file was inaccessible.
- The exact checker passed on its first run. Source review then added
  the zero-radicand boundary to its private root-bound helper and removed
  an irrelevant arithmetic assertion. The updated checker passed.
- The strictly negative ordinary width-derivative hypothesis is false:
  that derivative vanishes for every admissible u. Strict descent occurs
  at cubic order off the switch. A chain-only calculation at u=a would
  miss the positive quadratic chord contribution.

## Final diff inspection

- Complete tracked diff inspected for CURRENT_STATUS.md,
  knowledge/FIXED_ORDER_THEORY.md and research/NEXT_RESEARCH_STEPS.md.
- All five untracked additions read in full: proof, checker and the three
  dossier files. Closing dossier/status edits are reviewed again at handoff.
- Explicit whitespace check covers all eight files, including additions:
  no trailing whitespace/tabs or missing terminal newline.
- `git diff --check`: exit 0, no output.
- Exact allowed-path audit: three modified, five new; HEAD and staged
  diff unchanged. No Git history or GitHub writes.
- Protected/generated paths checked unchanged: previous proof notes and
  dossiers, paper_assets/, results/, src/, tests/, scripts/, verify.py,
  publication metadata, README.md, REPORT.md, other knowledge ledgers,
  PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md.
- Proof/checker links and four source dependencies pass; no stable claim
  was duplicated across thematic ledgers.

## Residual uncertainty

Finite permutation recovery of the second block is unproved here.
Necessary marginals/balance are not treated as sufficient. The exact
continuum saving does not improve the recorded geometric limsup bound
C_hat. No moving-u, wrap-crossing or arbitrary larger-width sign
classification, general coupling/permutation optimum or global geometric
optimum is claimed. Imported baseline minima and the new proof retain
their separate external-review status. Local gates do not certify them
by themselves, and no hosted CI result was inspected.
