# Evidence

## Environment

```text
repository_head=3eb1ec321e2f5a334826ee70c2258f82b9703f66
platform=Windows PowerShell sandbox; AMD64
python=3.14.3 (MSC v.1944 64 bit)
mpmath=1.3.0
dependency_source=existing workspace environment; no installation
task_mode=STRICT
```

## Outcome and claim ledger

**NUMERICAL DIAGNOSTIC.** Both runs give a negative `D=R_{8,n}-T_{8,n}`
for `33<=n<=37` and positive `D` for `38<=n<=46`. The first stable
crossing is between adjacent endpoints `37,38`. The numerical candidate
for `s_8` is `38`; its exact classification remains open in this task.

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| The two constructed edge sets agree for all 14 inputs | engineering fact | full tours and edges in `diagnostic.json`; permutation, distinct-edge, degree, seam and cyclic symmetry gates | rank construction versus parity formulas; no production import | does not reprove Supnick optimality |
| Roots and physical thresholds have stable signs | numerical observation | 90/150-digit paths, residuals, numerical brackets and run differences | separate inputs, contexts, algorithms and threshold evaluations | shared mpmath; no interval certificate |
| Crossing at `37/38`, candidate `38` | numerical observation | complete bounded table and sign comparison | both paths agree | no exact endpoint proof or theorem for `s_8` |
| `176` separates both endpoint pairs with positive margins | numerical observation | guarded search and all eight stored margins | checked against both runs | exact rational choice; inequalities remain numerical |
| Artifact recomputes byte for byte | engineering fact | normal generation, optimized recomputation | production-independent, but coupled to this generator | local execution, not hosted CI or an independent exact verifier |

## Reconstruction and numerical method

The authoritative definitions are in
`research/FIXED_K_SUPNICK_SEAM.md`, sections 1, 2 and 4. The exact
uniform window is imported from
`research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md`; it is not reproved.

Run A uses 90 decimal digits. With `N=n-7` and `h=ceil(N/2)`, build the
two rank arms from the low ranks `1+2j,2+2j` and high ranks
`N-1-2j,N-2-2j`, keeping low ranks at most `h` and high ranks above
`h`. Concatenate `A,reverse(B),N`, shift ranks by `7`, and extract
every cyclic adjacent edge including the closing edge.

Run B starts afresh at 150 decimal digits and directly constructs the
parity edge formulas of section 1. For `N=2h`, these are

```text
{(8,n),(h+7,h+8)}
union {(i,n+7-i): 8<=i<=h+6}
union {(i,n+9-i): 9<=i<=h+7}.
```

For `N=2h+1`, these are

```text
{(8,n)}
union {(i,n+7-i): 8<=i<=h+7}
union {(i,n+9-i): 9<=i<=h+8}.
```

Each undirected edge is sorted internally. Exact integer comparisons
check the two sorted lists, `N` distinct edges, the complete permutation
of `8..n`, degree two, seam edges `(8,n-1),(8,n)`, and all rotations
and reflections. There are seven cases of each parity. `diagnostic.json`
stores all 14 complete rank tours and parity edge sets, including 30 edges
at `n=37` and 31 at `n=38`.

In each run solve `F(R)=C_{8,n}(R)-2*pi=0` from the independently
checked initial bracket `[0,n^2]`. The value at zero is the continuous
limit `(N-2)*pi`. Run A uses

```text
C(R) = sum_edges 2 asin sqrt(ab/((R+a)(R+b)))
```

with `fsum` and bisection until bracket width is less than
`10^(-(dps-15))`. Run B uses the equivalent positive-radius identity

```text
C(R) = sum_edges 2 atan sqrt(ab/(R*(R+a+b)))
```

with reverse-order ordinary multiprecision summation and mpmath's Ridder
solver, tolerance `10^(-(dps-15))`, `verify=True`. Both solvers have
an explicit limit of `4*dps` iterations. No root or starting interval
from A is supplied to B.

Both thresholds evaluate the exact fixed-`k` physical minus-root formula

```text
a = 1/8 + 1/n + 1/(n-1),
b = (2n+7)/(8n(n-1)),
T = 1/(a-2 sqrt(b)).
```

A evaluates it directly. B computes `a,b,a^2-4b` as exact Fractions,
then evaluates the conjugate `(a+2 sqrt(b))/(a^2-4b)` at 150 digits.
Positivity is checked before use. Each run separately checks the
unsquared physical equation

```text
1/T + alpha + 2 sqrt(alpha/T + beta) - 1/8 = 0,
alpha = 1/n + 1/(n-1), beta = 1/(n(n-1)).
```

The root acceptance gates are `|F(R)|<10^(-(dps-25))` and numerical
signs `F(R-pad)>0>F(R+pad)`, with
`pad=10^(-(dps-30))`: `1e-60` for A and `1e-120` for B.
The physical residual must be below `10^(-(dps-20))`.
The artifact stores the midpoint, half-width and both residuals, so each
local numerical bracket is recoverable without an omitted endpoint.
All are ordinary multiprecision computations, without directed rounding.

Each `(n,run)` uses a fresh cloned mpmath context. A is completed before
B starts. There is no random seed, warm start, multiprocessing, production
import, empirical formula for an onset, or scan of another `k`.
The comparison context has 170 digits. Stored A/B values use at most
80/140 significant digits, respectively; extra printed digits are not an
accuracy guarantee. Absolute run differences below refer to those
serialized values. Residuals printed as zero are rounded numerical zeros.

## Complete bounded table

Values below are rounded to ten decimal places from run B; full values
for both runs are in `diagnostic.json`. Every row has the same sign in A.

| n | Edges | R | T | R-T |
|---:|---:|---:|---:|---:|
| 33 | 26 | 137.5953158087 | 1567.3680361388 | -1429.7727203302 |
| 34 | 27 | 146.7525993441 | 527.2345714336 | -380.4819720895 |
| 35 | 28 | 156.1667351461 | 321.1345316978 | -164.9677965516 |
| 36 | 29 | 165.8431751430 | 232.9842586679 | -67.1410835250 |
| 37 | 30 | 175.7757736955 | 184.0486273424 | -8.2728536469 |
| 38 | 31 | 185.9698616893 | 152.9154539683 | 33.0544077210 |
| 39 | 32 | 196.4195148064 | 131.3611488548 | 65.0583659517 |
| 40 | 33 | 207.1299385038 | 115.5514483701 | 91.5784901336 |
| 41 | 34 | 218.0954148324 | 103.4576788048 | 114.6377360276 |
| 42 | 35 | 229.3210225771 | 93.9058604351 | 135.4151621420 |
| 43 | 36 | 240.8012367243 | 86.1694839569 | 154.6317527674 |
| 44 | 37 | 252.5410101920 | 79.7748596139 | 172.7661505781 |
| 45 | 38 | 264.5349987407 | 74.3999425011 | 190.1350562396 |
| 46 | 39 | 276.7880315560 | 69.8181438766 | 206.9698876794 |

No root or threshold was computed outside `33..46`. The full table is
required by the user; identifying the first crossing did not trigger a
larger scan. No inconsistency with the uniform window was found.

## Precision stability and margins

The separate Decimal audit of the stored values returned:

```text
max_abs_run_difference_R=3.9832649043950781E-76
max_abs_run_difference_T=2.1422500017714343E-77
max_abs_run_difference_D=4.0219045879874642E-76
max_abs_A_closure_residual=1.0987163717325013E-77
max_abs_A_physical_threshold_residual=7.6704585395276977E-92
max_abs_B_closure_residual=1.8329618180997628E-150
max_abs_B_physical_threshold_residual=0 (rounded numerical value)
min_abs_D=8.272853646949242341492730728061789055232437213739...
```

The predeclared absolute stability/sign/separator guard is `g=1e-55`.
It is a conservative diagnostic screen, not a mathematically proved
error bound. All 28 local brackets and physical-threshold residual
gates passed; both runs also show increasing `R,D` and decreasing `T`.

For the adjacent pair define, over both runs,

```text
L = max(R_{8,37},T_{8,38}) + g,
U = min(T_{8,37},R_{8,38}) - g.
```

The guarded interval is approximately

```text
L = 175.775773695489369130566663345168906137632258922280289053079...
U = 184.048627342438611472059394073230695192864696136019335379555...
```

For denominators `d=1..1000` in increasing order, choose
`p=floor(L*d)+1` and accept the first `L<p/d<U`. The first denominator
already succeeds: `q=176/1`. No assertion about the best possible
separator is made. The four margins below agree in both runs at the
shown precision; all eight margins are retained in the artifact.

| Numerical margin | Value |
|---|---:|
| `q-R_{8,37}` | 0.224226304510630869433336654831 |
| `T_{8,37}-q` | 8.048627342438611472059394073231 |
| `q-T_{8,38}` | 23.084546031718215289069411177125 |
| `R_{8,38}-q` | 9.969861689327153066003627825939 |

The separator's denominator is exact; its placement between the four
mathematical values has only numerical evidence in this task.

## Commands and checks

All executions below are local. Run from the repository root.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` and dependency inspection | exit `0`; Python `3.14.3`, mpmath `1.3.0` | available numerical environment | other environments |
| `python -B ops/TASK-20260902__radius8_seam_diagnostic/diagnose.py --write` | exit `0`; `rows=14; independent paths=2`; `STABLE_NUMERICAL_CROSSING`, endpoints `[37,38]`, fraction `176` | both bounded numerical paths and generation | exact endpoint inequalities |
| `python -B -O ops/TASK-20260902__radius8_seam_diagnostic/diagnose.py --check` | exit `0`; identical numerical output and `reproduction=BYTE_IDENTICAL` | full recomputation, exact stored-byte equality, gates survive optimization | algorithm-independent artifact verification |
| Decimal/source/mutation audit below | exit `0`; `audit=PASS rows=14 range_rejections=2 edge_mutations_rejected=3` | stored arithmetic, source hashes, domain, corrupted inputs, no float literals/assert/production imports in generator | transcendental root accuracy or all possible mutations |

The numerical output from both full executions begins

```text
NUMERICAL DIAGNOSTIC; k=8; n=33..46; dps=90,150; rows=14; independent paths=2
```

and returns `candidate_only=38`, endpoints `[37,38]`, and
`status=STABLE_NUMERICAL_CROSSING`. The complete row output is recoverable
by either command above. The additional audit was executed exactly as follows:

```powershell
@'
import ast
import hashlib
import importlib.util
import json
from decimal import Decimal, localcontext
from pathlib import Path
p = Path("ops/TASK-20260902__radius8_seam_diagnostic")
spec = importlib.util.spec_from_file_location("radius8_diagnostic", p / "diagnose.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
report = json.loads((p / "diagnostic.json").read_text(encoding="utf-8"))
nodes = list(ast.walk(ast.parse((p / "diagnose.py").read_text(encoding="utf-8"))))
assert not any(isinstance(x, ast.Assert) for x in nodes)
assert not any(isinstance(x, ast.Constant) and isinstance(x.value, float) for x in nodes)
imports = sorted({x.name for node in nodes if isinstance(node, ast.Import) for x in node.names}
                 | {node.module for node in nodes if isinstance(node, ast.ImportFrom)})
assert not any(x == "ringmin" or x.startswith("ringmin.") for x in imports)
assert [r["n"] for r in report["rows"]] == list(range(33, 47))
rejections = 0
for n in (32, 47):
    try:
        mod.rank_tour(n)
    except ValueError:
        rejections += 1
tour, edges = mod.rank_tour(37), mod.parity_edges(37)
for bad_tour, bad_edges in ((tour, edges[:-1]), (tour, edges[:-1] + edges[:1]),
                            (tour[:-1] + [tour[0]], edges)):
    try:
        mod.audit_edges(37, bad_tour, bad_edges)
    except ValueError:
        rejections += 1
assert rejections == 5
with localcontext() as ctx:
    ctx.prec = 170
    for r in report["rows"]:
        for method in ("A", "B"):
            v = {k: Decimal(s) for k, s in r[method].items()}
            assert abs(v["R"] - v["T"] - v["D"]) < Decimal("1e-75")
            assert (1 if v["D"] > 0 else -1) == r["sign"]
            assert v["closure_at_R_minus_pad"] > 0 > v["closure_at_R_plus_pad"]
        assert r["sign"] == (-1 if r["n"] <= 37 else 1)
    for key in ("R", "T", "D"):
        value = max(abs(Decimal(r["A"][key]) - Decimal(r["B"][key])) for r in report["rows"])
        print(f"max_abs_run_difference_{key}={value:.16E}")
    for method in ("A", "B"):
        for key in ("closure_residual", "physical_threshold_residual"):
            value = max(abs(Decimal(r[method][key])) for r in report["rows"])
            print(f"max_abs_{method}_{key}={value:.16E}")
    print("min_abs_D=" + str(min(abs(Decimal(r[m]["D"])) for r in report["rows"] for m in ("A","B"))))
for source, expected in report["source_sha256"].items():
    assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected
for name in ("diagnose.py", "diagnostic.json"):
    print(name + "_sha256=" + hashlib.sha256((p / name).read_bytes()).hexdigest())
print("audit=PASS rows=14 range_rejections=2 edge_mutations_rejected=3 imports=" + ",".join(imports))
'@ | python -B -
```

The stdlib Decimal audit is independent of mpmath for comparisons of stored
decimal strings. It does not independently recompute transcendental values.
The three mutations remove an edge, duplicate an edge, and duplicate a tour
vertex. Rejected `n=32,47` calls perform validation only; they compute no
out-of-range geometry.

Repository pytest, `verify.py`, frontier verification and paper builds
were not run: production, global certificates, exact proof notes and
publication sources are unchanged, so these gates would not validate this
numerical endpoint diagnostic. Hosted CI was not inspected.

## Artifact and provenance checks

- Artifact: `ops/TASK-20260902__radius8_seam_diagnostic/diagnostic.json`.
- Schema `1`: classification, base HEAD, versions, source hashes, fixed
  parameters, method descriptions, 14 rows, and diagnostic outcome.
- Generation base: `3eb1ec321e2f5a334826ee70c2258f82b9703f66`.
  The generator is an uncommitted task addition, identified by its hash;
  the base commit alone does not contain it.
- Inputs: fixed `k=8,n=33..46`; the fixed-`k` and uniform-window proof
  notes identified by embedded SHA-256 values. Those hashes were checked.
- `diagnose.py` SHA-256:
  `6eef172a18d4d3527f0d881d65092370ecc4d51b1063b38867abe36ee7a8e95e`.
- `diagnostic.json` SHA-256:
  `8d510329ac6c21917d42839d858c5e805ba5981ab7a2c0fa5c71f4ee202e42c8`.
- Determinism: no time/path/random fields; normal and optimized modes
  reproduce identical bytes with this environment and unchanged source
  bytes. Version changes or source line-ending changes alter metadata/hashes
  and can prevent byte equality; numerical portability is not claimed.
- No existing certified or heuristic result artifact was overwritten.

## Failed checks and negative evidence

The initial Git commands failed on sandbox ownership. A per-command
safe-directory override succeeded; a later attempt to suppress the global
ignore warning with `core.excludesfile=NUL` failed because Git cannot
use NUL as an exclude file. An empty `core.excludesfile=` worked.
No persistent Git configuration or history was changed.

No sign disagreement, missing edge, ambiguous near-zero sign, absence of a
bounded separator, or range inconsistency occurred in the actual scan.
Malformed-input failures in the audit were intentional. No failed numerical
run was discarded.

## Final diff inspection

The complete tracked diff was inspected, and all five untracked files were
read in full; every JSON field was reviewed in a compact rendering.
A separate byte-level format audit covers formatting omitted by that
rendering. The final read-only Git/format audit below exited `0` and
returned:

```text
format_scope_audit=PASS files=7 dossier_files=5 protected_changes=0
git_diff_check=PASS exit=0 output=empty
```

`git status --porcelain=v1 --untracked-files=all` contains precisely two
tracked modifications (`CURRENT_STATUS.md`, the roadmap) and five new
dossier files. All seven are strict UTF-8 without BOM, LF-only, with
exactly one final LF, no NUL and no trailing whitespace. The dossier has
exactly five files and no generated cache directories. `git diff --check`
returned exit `0`, no output; untracked whitespace is covered explicitly.

The protected-path audit compares the entire tracked delta against the
two permitted modifications. It confirms no change to
`PROJECT_KNOWLEDGE.md`, `AGENTS.md`, research proof notes, production
source/tests/scripts, results/certificates, `verify.py`, paper assets,
public summaries, dependency files, or prior dossiers. No incidental
generated file changed.

Exact audit invocation, also repeated after the final status edits:

```powershell
@'
from pathlib import Path
import subprocess
p = Path("ops/TASK-20260902__radius8_seam_diagnostic")
git = ["git", "-c", "safe.directory=" + Path.cwd().as_posix(), "-c", "core.excludesfile="]
def run(*args):
    return subprocess.run(git + list(args), check=True, capture_output=True).stdout
expected = {"CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md"}
expected |= {p.as_posix() + "/" + n for n in
             ("TASK_STATUS.md", "TASK_LOG.md", "EVIDENCE.md", "diagnose.py", "diagnostic.json")}
status = run("status", "--porcelain=v1", "--untracked-files=all").decode("utf-8")
actual = {line[3:] for line in status.splitlines()}
if actual != expected:
    raise RuntimeError(("unexpected scope", actual ^ expected))
for name in sorted(expected):
    raw = Path(name).read_bytes()
    text = raw.decode("utf-8")
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or b"\x00" in raw:
        raise RuntimeError(("encoding/line endings", name))
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise RuntimeError(("final newline", name))
    if any(line.rstrip() != line for line in text.splitlines()):
        raise RuntimeError(("trailing whitespace", name))
if len(list(p.iterdir())) != 5 or any(x.is_dir() for x in p.iterdir()):
    raise RuntimeError("unexpected dossier file/cache")
changed_tracked = set(run("diff", "HEAD", "--name-only").decode("utf-8").splitlines())
if changed_tracked != {"CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md"}:
    raise RuntimeError(("protected tracked delta", changed_tracked))
if run("diff", "--check"):
    raise RuntimeError("unexpected diff-check output")
print(status, end="")
print("format_scope_audit=PASS files=7 dossier_files=5 protected_changes=0")
print("git_diff_check=PASS exit=0 output=empty")
'@ | python -B -
```

The initial attempted portable Git diff using `safe.directory="$PWD"`
returned a two-file direct comparison (exit `1`), not a repository
diff, and was not counted. The correct repository diff was then inspected
with the explicit safe directory. The final script derives an absolute
forward-slash path and passes an argument list directly to Git.

## Residual uncertainty and next atomic task

All endpoint signs and separator inequalities remain NUMERICAL DIAGNOSTIC.
The two runs share mpmath, the same analytic definitions and a common
reporting harness. They are independent computational paths, not independent
libraries or an exact verifier. Numerical residuals and reproducibility do
not establish a named exact onset. No theorem, interval certificate,
full-pair feasibility, global optimum, contact graph or floating-circle
conclusion is supplied. `PROJECT_KNOWLEDGE.md` is intentionally unchanged.

Exactly one proposed next task: a dedicated STRICT exact endpoint proof at
`n=37,38` with `q=176`, auditing both threshold comparisons and all
30/31 chain edges against exact bounds for `pi`, before applying the
existing fixed-`k` theorem. That task has not begun.
