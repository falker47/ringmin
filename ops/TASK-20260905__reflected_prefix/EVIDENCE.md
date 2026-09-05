# Evidence

## Environment

```text
repository_head=bbcdb0330dc080d619152074c6bbbf7d4980651c
platform=Windows / PowerShell / local workspace
python=3.14.3 [MSC v.1944 64 bit (AMD64)]
mpmath=1.3.0
numpy=2.4.3 (available, not imported by this checker)
scipy=1.17.1 (available, not imported by this checker)
dependency_source=requirements.txt; pre-existing canonical environment
task_mode=STRICT
```

The new checker uses only __future__, fractions, math and mpmath. No
installation, new task-local dependency or SymPy is needed. The previous
recovery checker's SymPy import is not inherited or modified.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Each high radius occurs exactly once at every m | Exact theorem | Proof Section 2 | All-m parity bijection; separate list-reversal finite audit |
| Continuous-test recovery for each fixed 1/4<=lambda<1-alpha_* | Exact theorem | Sections 2-3 | Modulus bound and Riemann sums; finite polynomial checks do not prove weak convergence |
| Full cost retains both possible branches | Exact theorem | Section 4 | Monotone ratio, tail switch and wrap; independent quadrature/primitive diagnostics |
| The explicit 3/10 prefix improves C_ref strictly | Exact theorem | Section 5 | Analytic midpoint bound plus rational square/saving gates; no numeric premise |
| Full-radius coefficient converges to C_30 | Exact fixed-order asymptotic theorem | Section 6 | Imported exact full criterion and uniform root theorem; independent angular-formula diagnostics |
| Global limsup is bounded above by C_30 | Proved corollary | Section 6 | Actual even placements and deletion for odd sizes; no optimality or lower-bound claim |
| Finite exact checker identities hold | Independently reproduced finite result / engineering fact | Exact stdout below | Independent of production/verifier/old checkers, not external human review |
| Printed coefficients, root brackets and distances | Numerical observation | 60/120-digit diagnostics below | Not directed intervals or global certificates |

Authoritative mathematical source: research/PERMUTED_HALVES_REFLECTED_PREFIX.md.
The fixed-order ledger owns recovery, branch and coefficient claims; the
global ledger owns only the separate upper-bound corollary, using a
cross-reference for the constant and its comparison. The unchanged compact
index already routes to these owners. No stable claim needs another owner.

## Commands and checks

All commands were local from the repository root; no hosted CI run was
inspected. Read-only Git queries used the per-command option
`-c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin`.

Environment command, exit 0:

```text
python -c "import sys, numpy, scipy, mpmath; print(sys.version); print('numpy',numpy.__version__,'scipy',scipy.__version__,'mpmath',mpmath.__version__)"
3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
numpy 2.4.3 scipy 1.17.1 mpmath 1.3.0
```

Primary reproducible verification command and COMPLETE output, exit 0:

```text
python -u ops/TASK-20260905__reflected_prefix/check_prefix.py
PASS rational: D(1/12)<-17383/2250000; branch margin=466441/12960000; cost gap>37/457600
PASS occurrences: 17423 legal (m,s,q), m=2..64; 839207 predecessor cells
PASS seams: 527 coincident r=q+1, 1055 q=0, 1053 q=2; invalid inputs rejected
PASS coordinates: 4315 rational (alpha,lambda,m) tests; 123407 ordinary pairs within 3/m
PASS moments: 216 exact nonsymmetric polynomial tests, alpha=1/10, lambda=3/10,1/2,3/4
DIAGNOSTIC alpha_*=0.10678476019990019934581367851596
DIAGNOSTIC lambda=0.25 z=0.25 C=0.1419538534197848532950043776969
DIAGNOSTIC lambda=0.3 z=0.3 C=0.14192459205640585230215006575955
DIAGNOSTIC lambda=0.5 z=0.33812228102687903601 C=0.14272614939194170774853934272738
DIAGNOSTIC lambda=0.75 z=0.37044356300461628599 C=0.14347441106309895022623255819325
PASS full cost: quadrature vs elementary primitives; both block/tail branches and switch boundary
DIAGNOSTIC m=2 q=0 root/n^2=0.05277834934755347527172 empirical/(4pi)=0.179247611573759723128
DIAGNOSTIC m=3 q=0 root/n^2=0.07828196733438747351978 empirical/(4pi)=0.1680438200853571583765
DIAGNOSTIC m=7 q=2 root/n^2=0.1129067027154989587821 empirical/(4pi)=0.153661765266469453494
DIAGNOSTIC m=8 q=2 root/n^2=0.1161324547783468767557 empirical/(4pi)=0.1523035914424651505892
DIAGNOSTIC m=9 q=2 root/n^2=0.1189939713175774229939 empirical/(4pi)=0.1510714580262849073538
DIAGNOSTIC m=20 q=6 root/n^2=0.1310775117325882884354 empirical/(4pi)=0.1457229517365774759516
DIAGNOSTIC m=64 q=18 root/n^2=0.1383919751533773716408 empirical/(4pi)=0.1430656092834457572284
DIAGNOSTIC m=128 q=38 root/n^2=0.140137069867806768281 empirical/(4pi)=0.1424848241475216525056
DIAGNOSTIC m=256 q=76 root/n^2=0.1410277311952030391736 empirical/(4pi)=0.1422043002608128228468
PASS roots: 9 full roots bracketed by independent atan scoring; 1165 angular/Cartesian pairs
NOTE: 60/120-digit diagnostics are not interval certificates; all-m recovery and strict improvement are analytic.
```

The finite domain was fixed in the checker before running it; TASK_STATUS
lists the discriminator, ranges and stopping rule. The list implementation
rotates then reverses even positions. A separate integer rank formula
checks it, with every occurrence and predecessor, all small cases, exact
exception counts and malformed-input rejection. Coordinate comparisons
use exact Fraction values, including alpha*m integer. Polynomial moments
use independent binomial expansion and termwise rational integration;
they are not obtained from the empirical sums or SymPy. Their acceptance
gate is the proved Lipschitz bound, not monotonic decay of finite errors.

The continuous diagnostics compare direct quadrature of the full max with
elementary circular/F_c primitives, including genuine block switches at
1/2 and 3/4 and the boundary at which a switch first enters. These are
formula tests, not a search for a second witness. Alpha is obtained from
its defining derivative and checked by a separate directly integrated
derivative. For the nine root sizes, its floors agree at 60 and 120 digits
and lie more than 1e-20 from either adjacent integer at 120 digits. That
is diagnostic stability, not a rigorous enclosure of the exact floor.

Full roots are bisected for 165 iterations with the asin kernel, then
bracketed at root +/- 1e-35*max(1,root) using independently implemented
`2*atan(sqrt(ab/(R*(R+a+b))))`. For m>=64 the explicit uniform score/root
bounds from the imported theorem are also checked. At m=2,3,7,8,9,20,
the cell gaps plus positive closure slack at the upper probe are rebuilt,
and every pair's two directed angular constraints and complex-plane
Cartesian distance are checked. Tolerances are 1e-45 angular and 1e-40
distance. These local diagnostics corroborate full feasibility, not global
optimality or a finite certified scope extension.

A preliminary one-off `python -c` mpmath calculation at 40 digits tested
only 1/4 against the suggested 3/10, and inspected midpoint values for
D(1/12); it exited 0. It was exploratory, not evidence for an inequality.
All material numerical values are reproduced by the retained command above
at 60 digits, and all rational margins by its Fraction gates. A separate
one-off Fraction arithmetic check returned the same derivative upper bound,
five square margins and gap before they were recorded in the proof.

Skipped: pytest, production verify.py (both frontier and smoke modes),
historical checkers and paper builds. No production implementation,
certificate artifact or publication source changed, and none of these
commands proves the new analytic theorem. No hosted CI or external
independent acceptance is claimed.

## Artifact and provenance checks

No production result/certificate or publication artifact was generated.
Task-local source: check_prefix.py, deterministic stdout recorded above.
Inputs and precision are fixed in that source; there is no random seed
or nondeterminism. The generation base is the HEAD recorded above plus
this uncommitted working-tree delta. The user performs any later commit.

Source hashes from local `Get-FileHash -Algorithm SHA256`:

```text
research/PERMUTED_HALVES_REFLECTED_PREFIX.md
485fefd9238d97799cf0801a395fb1ab077707c3b007e3a4361c2ef0588608b1
ops/TASK-20260905__reflected_prefix/check_prefix.py
871cec1b0e1dc991525689e1e57b316f5148ecdbcabecf39a72c782d4a540e26
research/PERMUTED_HALVES_MU_REF_RECOVERY.md (unchanged)
68036e0fdf24a28b48193665c1c9dc95954489117ce75d56fcf7080eb2b9122a
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md (unchanged)
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63
research/PERMUTED_ALTERNATING_HALVES.md (unchanged)
c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab
research/SHIFTED_ALTERNATING_HALVES.md (unchanged)
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db
```

## Failed checks and negative evidence

Default Git status failed on sandbox ownership in the initial multi-read
shell command; its individual exit was not captured because later reads
completed. Repeated read-only Git queries with per-command safe.directory
succeeded, with global-ignore permission warnings. No persistent setting
or Git state was changed. One apply_patch invocation failed validation
because it tried delete/add operations on CURRENT_STATUS.md together;
it made no changes and was replaced by a normal update.

No mathematical or checker assertion failed. The naive all-chord formula
for arbitrary longer prefixes is invalid once v_lambda(lambda)>1; the
proof and checker retain that branch transition. The explicit witness
3/10 is certified to avoid it. Prefixes crossing the high wrap are outside
this theorem's stated domain, not silently covered by the same formula.

## Final diff inspection

The complete four-file tracked diff and all five untracked additions were
read and inspected. The checker was read separately after a combined tool
display was truncated. An explicit empirical-measure definition was added
to the proof during this inspection; the executed checker source did not
change. There are no incidental generated or protected-file changes.

The local one-off audit ran as `python -`, receiving a literal PowerShell
here-string (no filesystem or bytecode writes). It used pathlib, ast,
hashlib, re and subprocess. Read-only Git argument lists queried
`diff --name-only`, `ls-files --others --exclude-standard`,
`diff --cached --name-only`, `diff --check`, and
`status --short --untracked-files=all`. The exact four/five path whitelist
below was required, with the staged diff empty. It decoded every changed
file as UTF-8 and checked no BOM, final newline, no extra terminal blank
line and no trailing whitespace, including all untracked additions.
It resolved all five Markdown links in the additions, recomputed all six
recorded SHA256 hashes, compiled the checker in memory and used AST
inspection to require only the four declared imports.

Exit 0, exact output:

```text
PASS file audit: 4 tracked changes, 5 additions, 5 local links, 6 SHA256 hashes; staged diff empty; protected paths clean
PASS source audit: in-memory compilation; imports only __future__, fractions, math, mpmath
PASS whitespace: all 9 files including untracked additions; git diff --check exit 0
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__reflected_prefix/EVIDENCE.md
?? ops/TASK-20260905__reflected_prefix/TASK_LOG.md
?? ops/TASK-20260905__reflected_prefix/TASK_STATUS.md
?? ops/TASK-20260905__reflected_prefix/check_prefix.py
?? research/PERMUTED_HALVES_REFLECTED_PREFIX.md
```

All preceding proofs and dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, metadata, README, REPORT, other knowledge ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md were checked
for unexpected diffs and remain unchanged. The four imported proof hashes
also agree with the preceding recovery dossier. These are source/path
checks, not new paper builds or finite-certificate verification. No Git
history or GitHub state was written. Final task state: READY_FOR_REVIEW.

## Residual uncertainty

Independent external proof review remains pending, including imported
exact full feasibility, uniform root transfer and alpha_* definition.
The new theorem concerns this explicit one-parameter construction on
lambda<1-alpha_*, with improvement proved only for the specified witness.
It does not optimize alpha or lambda, characterize general recovery,
determine a relaxation optimum or global optimum, or prove a normalized
global limit. The published snapshot and finite certified scope are intact.
