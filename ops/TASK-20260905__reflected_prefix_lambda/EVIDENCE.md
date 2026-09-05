# Evidence

## Environment

```text
repository_head=5b576762e11cfdb9e86dd8c9b4c9cc9d81598244
platform=Windows / PowerShell / local workspace
python=3.14.3 [MSC v.1944 64 bit (AMD64)]
mpmath=1.3.0
dependency_source=pre-existing canonical requirements.txt environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitations |
|---|---|---|---|
| Complete three-regime variation and exactly two stationary points | Exact theorem | Proof Sections 2-5 and isolated rational signs | Analytic all-domain derivative/curvature inequalities; finite probes are not the proof |
| Unique global family minimum in (159/500,319/1000) | Exact theorem with rational endpoint gates | Sections 4-7 | Concavity comparison controls the final descent; fixed alpha only |
| C_ref(891/1000)<C_ref(89/100) | Exact counterexample / disproved monotonicity claim | Section 5 | Derivative is strictly negative throughout the entire rational interval |
| C_rp<C_30-1/100000 and C_rp<14191369/100000000 | Exact coefficient inequalities | Section 7 integer interval gates | Explicit rational witness 159/500; decimal minimizer not used |
| Full-radius limit for sigma_m(lambda_*) | Exact fixed-order asymptotic theorem | Section 8 | Imports preceding all-integer recovery, exact full feasibility and uniform root transfer |
| Global limsup bounded by C_rp | Proved corollary | Section 8 | Actual even feasibility and deletion for odd sizes; no optimum or lower-bound assertion |
| Interval arithmetic oracle checks and source/path audits | Independently reproduced finite result / engineering fact | Checker and final audit below | Local, independent of production and old checkers; not external acceptance |
| Printed stationary points and C_rp decimal | Numerical observation | 70-digit original full-max quadrature | Not interval certificates; separate from the integer gates |

Authoritative proof: research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md.
The fixed-order ledger solely owns the variation, minimizer, coefficients
and their comparisons. The global ledger owns only the resulting global
upper-bound corollary. The compact index already routes to both owners
and does not need a change. Earlier proof notes retain their task scope.

## Commands and checks

All checks below are local. No hosted CI or external reviewer acceptance
was inspected or claimed. No Git/GitHub state was written. Read-only Git
queries use the per-command option
`-c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin`.

Environment command, exit 0:

```text
python -c "import sys, mpmath; print(sys.version); print('mpmath',mpmath.__version__)"
3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
mpmath 1.3.0
```

Primary reproducible command, exit 0, complete final mathematical output:

```text
python -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py
PASS interval arithmetic: 2835 point and 297 box Fraction oracle checks; square and domain gates
PASS analytic square gates: z(1/3)>2/7; Phi'>41/72 in the middle; Phi'<-1/420 in the tail
EXACT D(53/500) in (-3/10000,-1/5000); enclosure=[-291784193,-291784192]/1000000000000
EXACT D(107/1000) in (7/100000,9/100000); enclosure=[80028360,80028361]/1000000000000
EXACT Phi(719/2500) in (-1/20000,-1/25000); enclosure=[-45419090,-45419089]/1000000000000
EXACT Phi(2877/10000) in (1/10000,11/100000); enclosure=[102023574,102023575]/1000000000000
EXACT Phi(4/5) in (-1/500,-1/1000); enclosure=[-1828639838,-1828639837]/1000000000000
EXACT E(1) in (3/250,13/1000); enclosure=[12494451212,12494451213]/1000000000000
EXACT alpha_* in (10678476019/100000000000,10678476021/100000000000); lambda_* in (159/500,319/1000)
EXACT descending counterexample interval: [89/100,891/1000] lies after x=4/5 and before the wrap
EXACT C_ref(159/500) in (14191368/100000000,14191369/100000000); enclosure=[141913685638,141913685659]/1000000000000
EXACT C_30 in (14192459/100000000,14192460/100000000); enclosure=[141924592047,141924592066]/1000000000000
PASS exact gates: C_rp<C_ref(159/500)<C_30-1/100000; C_rp<14191369/100000000
DIAGNOSTIC alpha_*=0.10678476019990019934581367851595785
DIAGNOSTIC tau=0.28197168006119485314661638605239742
DIAGNOSTIC lambda_min=0.31834538917021562118799984238752004
DIAGNOSTIC lambda_max=0.87275088111738991353888985739456419
DIAGNOSTIC C_rp=0.1419136786491477938676336008113416
PASS independent full-max diagnostics: 11 derivatives and curvatures; both switch continuity checks
PASS diagnostic quadrature agrees with exact slope/coefficient enclosures and descending counterexample
NOTE: decimals and derivative diagnostics are numerical observations; exact gates use integers only.
```

The exact portion imports only __future__, argparse, fractions and math.
It uses 50-place integer intervals, outward floor/ceiling arithmetic,
integer square roots, 64-term atan/log series with explicit remainder
bounds and 100 dyadic bisections for each isolated block switch. Every
undecided branch/sign or invalid operation is rejected. No ordinary float
or mpmath operation supplies an exact inequality. The deliberately invalid
float-constructor test checks that such input is rejected.

Fraction oracles independently check 2835 signed point operations, 297
points in nondegenerate rectangle operations, exact square inequalities
and malformed domains. The analytic square gates audit the rational
parts of the proof's inequalities; the proof, not this finite test set,
justifies their complete-domain extension.

The independent diagnostic uses the original unnormalized block/tail
full max at fixed alpha, with its actual switches, not the integer
primitive implementation. It differentiates that quadrature and the
separately integrated first derivative, checks the derived curvature
and implicit switch derivative at eleven fixed probes, and verifies
continuity on both sides of both transitions. Three exact slope boxes
and both coefficient boxes contain the independently integrated values.
All tolerances (1e-55 for formula comparisons, 1e-18 probes for continuity)
and parameter probes are fixed in the checker. These numerical tests
corroborate formulas; they do not certify signs or geometric feasibility.

Earlier runs of the initial checker, both full and with `--exact-only`,
exited 0 before the interval-box/curvature audit was added. The final full
run above supersedes their mathematical output. There was no failed
mathematical assertion. A standard-library-only rerun is recorded in the
final audit below.

Three exploratory `python -` calculations used mpmath at 40 digits and
exited 0: nine prescribed derivative probes; four auxiliary E values;
then the fixed alpha root, three coefficients and four D probes. They
selected falsifiable endpoint gates. Their material observations were
reproduced at 70 digits by the retained checker; their printed values
are not proof evidence. The E extension to x=1 was only an auxiliary
comparison, not a reflection across the high wrap.

Skipped: pytest, verify.py in both smoke and frontier modes, historical
checkers, finite-radius experiments, and paper builds. No production code,
finite certificate, recovery construction or publication source changed;
these commands would not prove the new variation theorem. Imported full
feasibility and root-transfer results were read, not newly certified.

## Artifact and provenance checks

No production result/certificate or publication artifact was generated.
The task-local checker is deterministic, takes its constants from the
retained source, writes only stdout, and uses no random seed. Its generation
base is the HEAD above plus this uncommitted working-tree delta. The exact
branch bounds terminate after a fixed number of steps; the separate
diagnostic uses mpmath root finding only for numerical observations.

Source hashes from local `Get-FileHash -Algorithm SHA256` and the final
Python hashlib audit (proof hash refreshed after endpoint wording review):

```text
research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md
407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3
ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py
439ac0ead71a03788bcefe72f4296a787a1e830140747192495ab8c9caa8c8d0
research/PERMUTED_HALVES_REFLECTED_PREFIX.md (unchanged)
485fefd9238d97799cf0801a395fb1ab077707c3b007e3a4361c2ef0588608b1
research/SHIFTED_ALTERNATING_HALVES.md (unchanged)
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db
research/PERMUTED_ALTERNATING_HALVES.md (unchanged)
c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md (unchanged)
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63
```

The four imported source hashes also agree with the preceding task's
recorded hashes. The final audit compares their contents to current HEAD
blobs (normalizing line endings), as well as the full changed-path whitelist.

## Failed checks and negative evidence

Default read-only rev-parse commands encountered dubious repository
ownership under the sandbox account. A repeat with per-command
safe.directory succeeded, returning the expected root and HEAD. Startup
status was clean; no persistent Git setting was changed. Two permission
warnings referred to the global ignore file, not a modified repository.

Initial template paths lacked the _TEMPLATE suffix; corrected after an rg
file search, and all three actual templates were read before editing.
These exploratory command issues did not change files or mathematical
inputs. No checker assertion failed.

The proposed entire right-side increase is rigorously disproved by the
rational interval in proof Section 5. The source of the failed route is
extending middle-branch convexity across the diagonal switch; the exact
tail has the opposite curvature. The predicted minimizer's uniqueness
and rational bracket survive, as the endpoint/concavity proof shows.

## Final diff inspection

The complete four-file tracked diff, full proof/checker and all three
dossier additions were read directly. Inspection clarified an endpoint
derivative statement: Phi' is negative on (0,tau), and only Phi itself is
extended negatively to tau by continuity. The proof does not claim a
two-sided second derivative there. The checker source did not change.

Standard-library-only reproduction, exit 0:

```text
python -S -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only
```

Its complete output is exactly the thirteen result lines of the primary
output above from `PASS interval arithmetic: ...` through
`PASS exact gates: ...`; no DIAGNOSTIC lines
are printed. This demonstrates that site packages and mpmath are not
required for the rational gates.

The local file audit ran as `python -`, receiving a literal PowerShell
here-string, using pathlib, ast, hashlib, re and subprocess. It performed
read-only Git queries with argument lists: diff --name-only,
ls-files --others --exclude-standard, diff --cached --name-only,
rev-parse HEAD, show HEAD:<each imported proof>, diff --check and
status --short --untracked-files=all. It required the exact path whitelist
below and an empty staged diff. For all nine changed files it required
UTF-8 without BOM, a final newline, no extra terminal blank line and no
trailing whitespace. It resolved every local Markdown link, compiled the
checker in memory and required only __future__, argparse, fractions,
math and the diagnostic mpmath import. All four imported proofs were
compared with HEAD, normalizing line endings, and source SHA256 values
were recomputed. No file or bytecode was written by the audit.

Exit 0, exact material output:

```text
PASS file audit: 4 tracked edits, 5 additions, 6 local links; staged diff empty; HEAD unchanged
PASS source audit: in-memory compilation; canonical imports; four imported proofs agree with HEAD
PASS whitespace: all 9 files including untracked additions; git diff --check exit 0; protected paths clean
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__reflected_prefix_lambda/EVIDENCE.md
?? ops/TASK-20260905__reflected_prefix_lambda/TASK_LOG.md
?? ops/TASK-20260905__reflected_prefix_lambda/TASK_STATUS.md
?? ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py
?? research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md
```

The two printed new-source hashes are recorded in the provenance section.
All preceding proof notes/dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, metadata, README, REPORT, other knowledge modules,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md were checked
for unexpected diffs and remain unchanged. The paper's angular-model
source and publication markers were inspected read-only; no paper build
or certificate re-verification is claimed. There were no generated-file
changes, Git history writes or GitHub writes. Final state: READY_FOR_REVIEW.

## Residual uncertainty

Independent external review remains pending, including the exact
interval code and imported recovery, full feasibility, uniform root
transfer and alpha_* definition. The theorem optimizes only this
fixed-alpha family on its existing domain. It does not optimize alpha,
recover arbitrary couplings, solve the relaxation or all permutations,
prove a geometric global optimum or normalized global limit, or extend
the finite certified scope. Numerical diagnostics are explicitly separate
from the rational proof gates. The published snapshot remains unchanged.

## Same-task resumption: independently executed checks in the renewed turn

The renewed request concerns precisely this unfinished, uncommitted task.
Startup found its four tracked edits and five additions already present at
the same HEAD, with no unrelated changes. The preceding chronology and
outputs were retained as inherited evidence; the checks listed here were
actually rerun in this turn. This is author-side completion verification,
not an external review or acceptance decision.

| Fresh command | Exit | Observed result |
|---|---:|---|
| `python -c "import sys, mpmath; print(sys.version); print('mpmath',mpmath.__version__)"` | 0 | Same complete Python 3.14.3 / mpmath 1.3.0 output recorded above |
| `python -S -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only` | 0 | All thirteen exact-result lines above reproduced, including 2835 point and 297 box oracle checks and all rational sign/coefficient gates |
| `python -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py` | 0 | All twenty-one mathematical output lines above reproduced; eleven derivative/curvature probes, both transition checks and independent full-max quadrature comparisons pass |

The analytic review rederived the scale factor A^2/(4*pi), the two
moving-boundary derivatives and the strict curvature bounds. In particular,
the tail derivative decreases strictly after the diagonal transition;
the positive auxiliary E(1) and concavity exclude a competing global
minimum on that final branch. The source proof and checker needed no
correction. Their SHA256 values remain exactly those recorded above.

The complete tracked diff and each untracked addition were read. A fresh
standard-library in-memory audit, passed to `python -S -` through a literal
PowerShell here-string, checked the exact nine-file whitelist, empty staged
diff, unchanged HEAD, all-file whitespace and local links, checker imports
and compilation, six source hashes and equality of the four imported
proofs to HEAD after line-ending normalization. It performed only read-only
Git queries with the per-command safe.directory setting. Exact output:

```text
PASS resumed file audit: 4 tracked edits, 5 additions, 6 local links; staged diff empty; HEAD unchanged
PASS resumed source audit: in-memory compilation; canonical imports; six hashes agree; four imported proofs agree with HEAD
PASS resumed whitespace: all 9 files including untracked additions; git diff --check exit 0; protected paths clean
```

The audit exited 0. The final path list is the same nine paths in the
preceding final-diff inspection. Protected/publication and generated paths
remain unchanged. The paper's angular-model source was inspected read-only.
The same skipped checks and dependency limitations above apply; no hosted
CI, historical computation or external review is claimed as newly run.

## User-authorized commit/push preparation

After the mathematical handoff, the user explicitly requested commit and
push. This later instruction authorizes integration of exactly this task's
nine files despite the earlier manual-integration rule. The current status
and dossier scope record that exception; the proof, checker, classifications
and proposed next independent review are unchanged.

The integration turn freshly ran both commands below, each with exit 0:

```text
python -S -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only
python -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py
```

Their thirteen and twenty-one result lines respectively match the complete
outputs above. The full tracked diff was inspected and git diff --check
exited 0; the staged diff was empty before preparing the commit. Branch
main and local origin/main both pointed to the recorded task-base HEAD;
the configured origin is the stated falker47/ringmin repository. This local
reference check is not a fresh remote-state or hosted-CI check. The final
precommit audit covers every tracked edit and untracked addition, including
whitespace and source hashes. Commit/push outcomes are reported by the Git
operations themselves; this precommit record asserts no future success or
external mathematical acceptance.
