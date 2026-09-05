# Evidence

## Environment

```text
repository_head=4b40aebddad73f09e453b5f17c3100852c780991
platform=Windows / PowerShell
python=3.14.3 MSC v.1944 64 bit AMD64
dependency_source=pre-existing interpreter packages; no installs
numpy=2.4.3
scipy=1.17.1
mpmath=1.3.0
sympy=1.14.0
task_mode=STRICT
```

## Claim ledger

Mathematical authority is
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md. This dossier
records verification, not a duplicate proof.

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Uniform cell/score/root limit for every P | exact continuum theorem | note Sections 2-4, symbolic normalization and bounded atan probes | alternate angular formula; no production imports | finite probes do not prove uniformity |
| Necessary uniform marginals and local balance | exact theorem | note Section 3, exact cyclic reindexing and affine-map audit | proof plus exact rational finite identities | no sufficiency/recovery theorem |
| Equal relaxed minima with/without balance | proved corollary | note Section 5, cost-preserving symmetrization | direct analytic argument | not a finite-permutation symmetrization |
| Explicit admissible coupling strictly below shift target | exact construction / disproved relaxation certificate | note Section 6, algebraic saving and rational 1/2496 gate | proof independent of floating arithmetic or LP | does not identify minimum or yield a geometric configuration |
| Decimal reflected cost and finite score/root observations | numerical observation | full 70-digit checker output below | alternate atan, direct split integrals, rationalized saving and closed block | not interval certificates or global results |

The exact full criterion and the unique analytic shift minimum are imported
from their two unchanged proof notes; neither is re-proved or declared
independently accepted by this task. Standard Kantorovich terminology was
checked in Brendan Pass's primary survey, arXiv:1406.0026, linked in the
proof note. The new argument uses no external duality/optimizer theorem.

## Commands and checks

Startup reads and environment query exited 0 except the initial Git reads
(exit 1, dubious ownership). Subsequent read-only Git commands with a
per-command safe.directory override exited 0; status listed no changes.
User-global ignore-file access emitted permission warnings.

Executed locally from the repository root:

```text
python -c "import sys, numpy, scipy, mpmath, sympy; print(sys.version); print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('mpmath', mpmath.__version__); print('sympy', sympy.__version__)"
exit=0
3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
numpy 2.4.3
scipy 1.17.1
mpmath 1.3.0
sympy 1.14.0

python ops/TASK-20260905__three_marginal_relaxation/check_relaxation.py --exact-only
exit=0
PASS exact: scalar guards, reflection saving >1/2496, coefficient denominator 9984*pi
PASS exact: affine marginal endpoints/Jacobians and split shift image
PASS exact: denominator/asin identities and cell/score normalization

python ops/TASK-20260905__three_marginal_relaxation/check_relaxation.py
exit=0
PASS exact: scalar guards, reflection saving >1/2496, coefficient denominator 9984*pi
PASS exact: affine marginal endpoints/Jacobians and split shift image
PASS exact: denominator/asin identities and cell/score normalization
PASS bounded: 27 prescribed orders; exact empirical marginal/seam identities
PASS bounded: 54 score probes, 2928 cells; max error/bound=0.5166216303390701
PASS bounded: 27 alternate-atan full roots; residual <1e-55
NOTE: finite root/score probes corroborate, but do not prove, the uniform limit
DIAGNOSTIC alpha_*=0.106784760199900199345813678516
DIAGNOSTIC 4*pi*C_shift=1.78437408690129664464990080638
DIAGNOSTIC reflected cost=1.78384473220943377149189954992
DIAGNOSTIC saved cost=0.000529354691862873158001256464274
DIAGNOSTIC reflected cost/(4*pi)=0.141953853419784853295004377697
PASS bounded: split direct integral, rationalized saving and closed block agree <1e-60
NOTE: reflected cost is a feasible relaxation cost, not the relaxation minimum or a geometric bound
```

The checker uses SymPy and Fraction for exact gates, then mpmath at 70
digits, 240 bisections/root, root/score guard 1e-55 and integral comparison
guard 1e-60. Its predeclared sizes are m=2,3,4,8,16,32,64,128. At most
four explicit orders per size (increasing, decreasing, shift by
floor(107*m/1000), alternating extremes) are deduplicated. Score probes
use c=1/10,1/7,1/5 only where m*c>=1, the expansion's stated domain.
Root-transfer probes with the universal comparison interval use m>=32;
the proof independently establishes an eventual uniform interval and does
not use that diagnostic cutoff as an effective theorem. All selected
roots were checked, including m=2 and m=3. Seeds are not applicable.

No imports of src/ringmin, verify.py or prior checker modules occur. The
exact gates are coupled to the stated analytic formulas; their purpose is
to audit algebra, not replace the proof. Alternate-angle numerical scoring
is independent of production code but imports the exact cell criterion as
a mathematical dependency. No independent human/continuous review or
hosted CI is claimed.

Not run: pytest, verify.py (including frontier/smoke modes), prior exhaustive
experiments, paper builds and artifact regeneration. No production code,
finite certificate or publication asset changed, so these checks would not
validate the new continuum theorem. No LP, factorial search or recovery
experiment was run.

## Artifact and provenance checks

No production certificate or publication asset is generated. The only new
computational source is the task-local checker, run by the two commands
above. Numerical output is retained verbatim in this file, not as a saved
optimality artifact. Base HEAD is recorded above; the user will commit the
working-tree delta manually. SHA256 (Get-FileHash -Algorithm SHA256):

```text
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63
ops/TASK-20260905__three_marginal_relaxation/check_relaxation.py
807c45e4f1dd9376d8ad4245a0d59c07dd01446ff3b6027ef31e10e23eb83c8a
research/PERMUTED_ALTERNATING_HALVES.md (unchanged dependency)
c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab
research/SHIFTED_ALTERNATING_HALVES.md (unchanged dependency)
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db
```

No nondeterministic sampling. The decimal diagnostics can depend on the
recorded mpmath version; the analytic result and rational gates do not.

## Failed checks and negative evidence

No mathematical check failed. A direct analytic coupling was found
before running any LP; no factorial search, discrete optimization or
numerical dual is used as proof.

The negative mathematical outcome is the strict relaxed saving: the
target lower bound is false, including after necessary local balance is
retained. It is not evidence of a cheaper finite permutation.
One documentation patch was rejected for duplicate operations targeting
CURRENT_STATUS.md and then corrected; no mathematical source was lost.

## Final diff inspection

Complete tracked diff inspected: exactly CURRENT_STATUS.md,
knowledge/FIXED_ORDER_THEORY.md and research/NEXT_RESEARCH_STEPS.md.
All five untracked additions were read in full: the proof, checker and
three dossier documents. Ordinary git diff omits those additions; they
received explicit content and whitespace inspection separately.

Read-only Git queries used the per-command safe.directory override for
the repository root, as at startup. diff --check exited 0, empty stdout;
status --short --untracked-files=all listed exactly:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__three_marginal_relaxation/EVIDENCE.md
?? ops/TASK-20260905__three_marginal_relaxation/TASK_LOG.md
?? ops/TASK-20260905__three_marginal_relaxation/TASK_STATUS.md
?? ops/TASK-20260905__three_marginal_relaxation/check_relaxation.py
?? research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md
```

The one-off audit was passed to `python -` through a literal PowerShell
here-string. It used pathlib, subprocess, re and hashlib only, built the
per-command safe.directory option from Path.cwd(), and queried
`git diff --name-only`, `git ls-files --others --exclude-standard` and
`git diff --cached --name-only`. It required exact equality to the eight
paths above and an empty staged diff. Each file was read in full as UTF-8
and checked for a final newline, no extra terminal blank line, no BOM and
no trailing whitespace on any line. Each non-HTTP Markdown link was
resolved against its containing file. The four recorded SHA256 values
were recomputed and required to occur in this evidence document.

```text
exit=0
PASS file audit: 3 tracked changes, 5 additions, 3 local links, 4 recorded SHA256 hashes; staged diff empty; protected paths clean
```

All protected paths lie outside that exact whitelist. In particular the
two imported proof sources, preceding dossiers, paper_assets/, results/,
src/, tests/, scripts/, verify.py, metadata, README, REPORT, other knowledge
ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md
have no working-tree diff. The published angular source was inspected at
startup; no paper or asset was regenerated. The sole owning thematic
ledger is FIXED_ORDER_THEORY.md, with navigation/status updates only in
the roadmap and CURRENT_STATUS.md. No duplicate thematic claim was added.

## Residual uncertainty

The exact relaxation value and its relation to recoverable permutation
limits are not to be inferred from one feasible coupling. Imported full
criterion/shift-minimization dependencies and new proof await independent
human review. No global geometric optimality or certificate is asserted.
