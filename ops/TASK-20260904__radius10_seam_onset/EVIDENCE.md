# Evidence

## Environment

```text
repository_head=4fc2bae962fb534f8758bab930a0863e3006bff7
platform=Windows-11-10.0.26200-SP0
python=3.14.3 (tags/v3.14.3:323c59a, Feb 3 2026) MSC v.1944 64 bit AMD64
dependency_source=stdlib for endpoint proof; existing environment for pytest
task_mode=STRICT
```

All commands below were run locally from the repository root. No package
installation, seed, floating root or nondeterministic proof input is used.
`python -c "import platform,sys; print(platform.platform()); print(sys.version)"`
returned exit 0 with the environment above. Startup Git required a
per-command safe.directory setting for this checkout; external ignore-file
permission warnings did not prevent status inspection. No configuration
was persisted and no Git history or GitHub state was written.

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Complete 36/37-edge cycles including closure/multiplicity | Exact finite identities | Proof section 3; separate rank and parity constructions; all 146 symmetry variants | Two edge implementations, no production import | Applies to the two stated endpoints |
| Positive curvatures and directed threshold comparisons at 270 | Exact rational inequalities | Section 2 signs and square margins | Integer cross-products separately reconstruct Fraction outputs | Physical minus root imported from fixed-k theorem |
| Both complete chain comparisons with pi | Exact inequalities | Sections 4-6; 73 strict rational witnesses; polynomial/integral analytic bounds | Separate integer scorer for all witness margins/sums | Integral arguments require mathematical review |
| s_10=46; positive deficit 12..45, negative for every n>=46 | Exact theorem / proved corollary | Four endpoint gates plus fixed-k sign and monotonicity theorem | No numerical scan or eventual-onset formula | Formal seam only; imported theorem is not reproved by finite checks |
| Test/verification results | Engineering facts | Commands below | Local current task; rejection tests are checker-coupled | No hosted CI or external-review claim |

## Commands and checks

Every path in the table is relative to the repository root. Isolated
`-I -S -B` execution excludes site packages and avoids writing bytecode.
The optimized invocations keep explicit exception gates active.

| Exact command | Exit and material output | Property / limitation |
|---|---|---|
| `python -I -S -B ops/TASK-20260904__radius10_seam_onset/check_seam.py --tables` | 0; exact_bridge=PASS, inequalities=4, cyclic_edges=73, symmetry_variants=146; all 73 rows printed | Exact endpoint arithmetic and analytic identities; mathematical fixed-k dependency remains |
| `python -I -S -O -B ops/TASK-20260904__radius10_seam_onset/check_seam.py` | 0; identical exact output | Gates remain active under -O |
| `python -I -S -B ops/TASK-20260904__radius10_seam_onset/score_witnesses.py` | 0; independent_integer_scorer=PASS, endpoints=2, witnesses=73 | No checker execution or Fraction arithmetic; complete integer reconstruction and note agreement |
| `python -I -S -O -B ops/TASK-20260904__radius10_seam_onset/score_witnesses.py` | 0; same integer output | Independent scoring under optimization |
| `python -I -S -B ops/TASK-20260904__radius10_seam_onset/check_mutations.py` | 0; Ran 28 tests in 0.063s; OK | Rejection/domain/transcription tests, including 73 individual witness corruptions |
| `python -I -S -O -B ops/TASK-20260904__radius10_seam_onset/check_mutations.py` | 0; Ran 28 tests in 0.062s; OK | Same suite with -O; no independent-review claim |
| `python -m pytest` | 0; `12 passed in 27.86s` | Existing production regression suite; not a certificate or proof premise |
| `git diff --check` (per-command safe.directory override) | 0; no output | Tracked whitespace; additions checked explicitly below |
| `python -I -S -B -` (final audit source below) | 0; delivery_audit=PASS, files=10, untracked=7, hashes=5, protected_changes=0 | Exact scope, current HEAD, recorded hashes, UTF-8/LF and whitespace on all ten files |

Successful exact checker output:

```text
threshold n=45 A=287/1980 B=1/50 A2-B=3961/3920400 H=839/5940 directed_margin=1751/35283600
threshold n=46 A=149/1035 B=101/5175 A2-B=1294/1071225 H=871/6210 directed_margin=5989/38564100
pi lower=281476/89625 margin=107/179250 upper=670143059704/213311234375 margin=1845738322/1493178640625
chain n=45 edges=36 upper_half_sum=15404369802693/5000000000000 margin=295630197307/5000000000000
chain n=46 edges=37 lower_half_sum=8011/2500 margin=1077/17500
exact_bridge=PASS inequalities=4 cyclic_edges=73 symmetry_variants=146
corollary=s_10=46 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only
```

Separate integer scorer output:

```text
independent_integer_scorer=PASS endpoints=2 witnesses=73
upper_numerator=15404369802693 denominator=5000000000000
lower_numerator=32044 denominator=10000
note_tables=PASS note_tours=PASS threshold_cross_products=PASS
```

Not run: global `verify.py` (neither full nor smoke mode), paper build,
hosted CI or external reviewer. No global artifact, verifier or publication
source changed. The production suite was explicitly requested and run;
it does not broaden the two-endpoint domain of the proof.

## Artifact and provenance checks

No global/publication artifact was generated. The proof note fully records
all 73 witnesses and integer square margins. `check_seam.py --tables`
reproduces the tables; `score_witnesses.py` reconstructs every witness from
integer isqrt and the expanded denominator, and independently checks the
complete cycles, threshold cross-products and aggregates.

Generation inputs: k=10, endpoints 45/46, R=270, D=10000, fixed-k formulas,
and exact analytic constants from the proof note. The upper integer rule
is `isqrt((D^2 ab)//Q_e)+1`; the strict lower rule is
`isqrt((D^2 ab-1)//Q_e)`. These rules and output commands fully reproduce
the tables. No production solver or prior diagnostic generated the witnesses.
The checker and rejection harness adapt the radius-9 structure; the separate
integer scorer is independently implemented and imports neither checker.

Source baseline: `4fc2bae962fb534f8758bab930a0863e3006bff7` plus the
uncommitted new sources identified below. This does not claim these new
files already belong to that commit. `Get-FileHash -Algorithm SHA256` on
these five paths returned exit 0; the final audit recomputes them.

| Path | SHA-256 |
|---|---|
| `research/FIXED_K_SUPNICK_SEAM.md` | `24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71` |
| `research/RADIUS10_SEAM_ONSET.md` | `c8b7d88017ffe429517aa330137d1a5e1c377e69a3dfca2555e8fa351577655a` |
| `ops/TASK-20260904__radius10_seam_onset/check_seam.py` | `5c0b57bf369ed2d24630802b81ee16be06193faae2322f2e5695d7a3a03f1ae2` |
| `ops/TASK-20260904__radius10_seam_onset/score_witnesses.py` | `1c83af0dc36fcff3a976fb644104998a27110bc65cba8180037ad6c035c046df` |
| `ops/TASK-20260904__radius10_seam_onset/check_mutations.py` | `4549f2639e269f962b0f7a6af1f6731a2ccc9dc2c0f01c65087e669121a5e4b5` |

## Failed checks and negative evidence

No mathematical gate, witness candidate or test run failed. The first
separator 270 closes all four gates after reconstruction; no alternative
endpoint was searched. The startup ownership error and ignore warnings
are environment issues only, recorded in the log.

Deliberately invalid inputs are rejected: incomplete/duplicate cyclic
edges, invalid tour/edge domains and an alternative Hamiltonian cycle;
each of 73 one-unit witness corruptions; exact synthetic sine equality
in both directions; nonpositive/noninteger bounds; wrong arcsine domain
or coefficient; valid term bounds with failing aggregate; wrong direction
or separator; nonpositive curvature; zero/negative pre-square H; threshold
equality/reversed margins; invalid pi bounds/atan domain; missing tables,
modified square/threshold margins, malformed tour and a shared altered
witness in both the note and checker literals. The last case establishes
that mere transcription agreement does not suffice for independent scoring.

## Final diff inspection

- Complete `git diff` read for all three tracked documents.
- All seven untracked additions read in full, including tables and scripts.
- Exact ten-path allowlist below includes every changed path; six files in
  the new dossier, one new proof note, three modified memory documents.
- Direct UTF-8/LF, one final newline and no trailing-whitespace checks cover
  tracked and untracked files; ordinary Git whitespace checking also passes.
- Protected paths inspected through the complete status/diff allowlist:
  `src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`, scripts,
  CI/configuration, README/REPORT, AGENTS, all earlier proof notes/dossiers.
  Zero protected or generated-asset changes; HEAD unchanged.

Final audit source (pipe the following to `python -I -S -B -`):

```python
from hashlib import sha256
from pathlib import Path
import re
import subprocess

root = Path.cwd()
dossier = "ops/TASK-20260904__radius10_seam_onset/"
names = {"TASK_STATUS.md", "TASK_LOG.md", "EVIDENCE.md", "check_seam.py",
         "score_witnesses.py", "check_mutations.py"}
allowed = {"PROJECT_KNOWLEDGE.md", "CURRENT_STATUS.md",
           "research/NEXT_RESEARCH_STEPS.md", "research/RADIUS10_SEAM_ONSET.md"}
allowed.update(dossier+name for name in names)

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def git(*args):
    result = subprocess.run(["git", "-c", "safe.directory="+root.as_posix(), *args],
                            capture_output=True, text=True, encoding="utf-8")
    need(result.returncode == 0, result.stderr)
    return result.stdout

status = git("status", "--short", "--untracked-files=all")
need({line[3:] for line in status.splitlines()} == allowed, "scope mismatch")
need(sum(line.startswith("?? ") for line in status.splitlines()) == 7, "untracked count")
need({p.name for p in (root/dossier).iterdir()} == names, "dossier contents")
for path in sorted(allowed):
    data = (root/path).read_bytes()
    content = data.decode("utf-8")
    need(not data.startswith(bytes((239, 187, 191))) and b"\r" not in data, path)
    need(data.endswith(b"\n") and not data.endswith(b"\n\n"), path)
    need(all(line == line.rstrip() for line in content.splitlines()), path)
evidence = (root/dossier/"EVIDENCE.md").read_text(encoding="utf-8")
hashes = re.findall(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$", evidence, re.MULTILINE)
need(len(hashes) == 5, "hash count")
for path, digest in hashes:
    need(sha256((root/path).read_bytes()).hexdigest() == digest, "hash "+path)
need(git("rev-parse", "HEAD").strip() == "4fc2bae962fb534f8758bab930a0863e3006bff7", "HEAD")
need(git("diff", "--check") == "", "whitespace diff")
print("delivery_audit=PASS files=10 untracked=7 hashes=5 protected_changes=0")
print("format=UTF-8/LF final_newlines=PASS trailing_whitespace=0 HEAD=unchanged")
```

## Residual uncertainty

The four endpoint gates and their fixed-k corollary are exact mathematical
claims awaiting independent review and manual integration. The checker is
not a proof assistant or a reproof of Supnick/fixed-k theory. Rejection
tests are coupled to it; the scorer shares only the stated mathematical
formulas and recorded inputs, and executes no checker arithmetic.
No global optimum, full feasibility, contact graph or floating property
has been proved. Remaining exact onset range: 11<=k<4325. Exactly one next
atomic task is proposed in CURRENT_STATUS.md; it has not begun.
