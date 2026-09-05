# Evidence

## Environment

```text
repository_head=49714545aeb77c0384753d1f29560b7a4c03d429
platform=Windows / PowerShell / local workspace
python=3.14.3 [MSC v.1944 64 bit (AMD64)]
sympy=1.14.0
mpmath=1.3.0 (available; not needed by the recovery checker)
dependency_source=pre-existing environment; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Every P_m contains each high radius once | Exact theorem | Proof Section 2, separate odd/even/tail bijections | Analytic all-m proof; bounded list reversal is an independent implementation check |
| mu_m^(P_m) converges weakly to the specified mu_ref | Exact theorem | Sections 3-4, all m atoms counted, modulus bound and parity Riemann sums | No numerical premise; exact moments only corroborate a finite list |
| rho_m/(2m)^2 tends to C_ref<C_shift-1/(9984*pi) | Exact fixed-order asymptotic theorem | Section 5, continuous g and imported uniform full-radius transfer | Uses existing full-criterion/root theorem; not a chain-root inference |
| limsup R*(n)/n^2<=C_ref | Proved global upper-bound corollary | Section 6, actual even placements and deletion for odd sizes | No lower-bound improvement, equality or global optimum |
| Prescribed finite diagnostics pass | Independently reproduced finite result / engineering fact | Exact command and stdout below | Independent of production code, not independent human review or global certification |

Authoritative proof: research/PERMUTED_HALVES_MU_REF_RECOVERY.md.
The fixed-order ledger owns recovery/coefficient claims; only the global
ledger owns the distinct deletion corollary. No stable claim was copied
into a second thematic owner. PROJECT_KNOWLEDGE.md remains unchanged because
its module routing, central definitions and scope already cover these results.

## Commands and checks

All commands ran locally from the repository root. No hosted CI or external
independent review was inspected or is claimed.

```text
python -c "import sys, mpmath, sympy; print(sys.version); print('mpmath', mpmath.__version__); print('sympy', sympy.__version__)"
exit=0
3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
mpmath 1.3.0
sympy 1.14.0

python ops/TASK-20260905__mu_ref_recovery/check_recovery.py
exit=0
PASS symbolic: parity involution, predecessor formulas, complete cell counts, strict-gap normalization
PASS bounded exact: 4159 prescribed (m,s) orders, m=2..128; permutation and cyclic occurrence checks
PASS bounded exact: 12311 rational alpha representatives; 1009576 ordinary triple comparisons <=3/m
PASS bounded exact: all seam/junction/wrap counts and endpoints, all m mod 8, invalid-input rejection
DIAGNOSTIC m=8: maximum of eight exact moment errors = 108707/384000
DIAGNOSTIC m=9: maximum of eight exact moment errors = 37020139/139968000
DIAGNOSTIC m=15: maximum of eight exact moment errors = 905873/3456000
DIAGNOSTIC m=16: maximum of eight exact moment errors = 64263/256000
DIAGNOSTIC m=31: maximum of eight exact moment errors = 12678501699/118210688000
DIAGNOSTIC m=32: maximum of eight exact moment errors = 216979/2048000
DIAGNOSTIC m=64: maximum of eight exact moment errors = 916707/16384000
DIAGNOSTIC m=128: maximum of eight exact moment errors = 8224937/262144000
DIAGNOSTIC m=256: maximum of eight exact moment errors = 30866371/2097152000
DIAGNOSTIC m=512: maximum of eight exact moment errors = 13543371/2097152000
DIAGNOSTIC m=1024: maximum of eight exact moment errors = 231310997/67108864000
PASS bounded exact: 88 polynomial moments against independently integrated mu_ref at alpha=1/10; proved Lipschitz bound
NOTE: finite checks audit formulas; the continuous-test proof establishes recovery at the exact alpha_*
```

The bounded domain was declared before execution in TASK_STATUS.md: every
m=2..128, every integer 0<=s<m/2, and two interior representatives of
each admissible alpha interval plus its positive lower endpoint. The
extra lower-endpoint representative specifically tests alpha*m integer.
All m mod 8 and q=0,2 occur. There is one prescribed permutation per (m,s),
with no permutation enumeration or comparison of objective values.

The implementation constructs a shifted list and reverses its even slots;
the oracle evaluates the displayed index formula separately. It checks
each predecessor, the explicit exceptional set/counts and every ordinary
coordinate against the target using Fraction. SymPy audits identities and
integrates eight polynomial tests exactly at alpha=1/10, with the declared
eleven m values. Their acceptance gate is the proved Lipschitz bound,
not monotonic decrease of errors. No float, numerical quadrature, random
seed, optimizer, production import, verify.py import or old-checker import
is used. The formula/moment oracles remain coupled to the mathematical
statement, as expected; they do not replace its continuous-test proof.

Skipped: pytest, production verify.py including frontier/smoke modes,
previous numerical checkers, LPs, full-radius numerical solves and paper
builds. No production/certificate/publication change calls for them, and
none would prove the new all-m weak limit. The existing analytic uniform
root transfer is a reviewed-in-this-task mathematical dependency, not a
new numerical assertion or a claim of external acceptance.

## Artifact and provenance checks

No production certificate or publication artifact is generated. The new
computational source is check_recovery.py, with command/input domain above;
its exact stdout is retained here. No saved optimum or generated data file
is created. There is no nondeterminism. The generating working-tree base
is the HEAD above; the user performs any later commit manually.

SHA256, computed locally with Get-FileHash -Algorithm SHA256:

```text
research/PERMUTED_HALVES_MU_REF_RECOVERY.md
68036e0fdf24a28b48193665c1c9dc95954489117ce75d56fcf7080eb2b9122a
ops/TASK-20260905__mu_ref_recovery/check_recovery.py
8352142e9d2138b5b88b353946bf2fc9d4eb0eb4cdd45a4b18e0e9e0008fd2c6
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md (unchanged dependency)
4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63
research/PERMUTED_ALTERNATING_HALVES.md (unchanged dependency)
c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab
research/SHIFTED_ALTERNATING_HALVES.md (unchanged dependency)
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db
```

## Failed checks and negative evidence

Default git rev-parse failed on ownership; the subsequent read-only override
succeeded with global ignore-file permission warnings. No mathematical
experiment has failed; no search or numerical minimization was run.
The first Git failure occurred inside a multiple-read shell invocation;
its individual exit code was not captured. The enclosing batch completed
with exit 0 after its later reads. Read-only queries were rerun successfully
with the per-command safe.directory override; no persistent configuration
was changed. A final proof-only notation correction changed the exceptional
set's name to X_m, preserving B_m for the prerequisite's family optimum.

## Final diff inspection

The complete four-file tracked diff was inspected, including CURRENT_STATUS.
All five untracked additions were read in full: the proof, checker and
three dossier documents. They were checked explicitly because ordinary
git diff and git diff --check omit them. All nine changed files passed
the explicit content/whitespace audit.

Read-only Git queries used the per-command safe.directory option. The
status command was git status --short --untracked-files=all with that
option; its exact list is:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__mu_ref_recovery/EVIDENCE.md
?? ops/TASK-20260905__mu_ref_recovery/TASK_LOG.md
?? ops/TASK-20260905__mu_ref_recovery/TASK_STATUS.md
?? ops/TASK-20260905__mu_ref_recovery/check_recovery.py
?? research/PERMUTED_HALVES_MU_REF_RECOVERY.md
```

The one-off audit was run as python - with a literal PowerShell here-string.
It used pathlib, ast, hashlib, re and subprocess. It built read-only Git
arguments with ['git','-c','safe.directory='+Path.cwd().as_posix()], queried
diff --name-only, ls-files --others --exclude-standard and
diff --cached --name-only, and required the exact whitelist above and an
empty staged diff. It read every changed file in full as UTF-8 and checked
no BOM, a final newline, no extra terminal blank line, and no trailing
whitespace. It resolved all four non-HTTP Markdown links and verified all
five recorded SHA256 hashes. It compiled the checker in memory without
writing bytecode and used AST import inspection to require exactly
__future__, fractions and sympy.

```text
exit=0
PASS file audit: 4 tracked changes, 5 additions, 4 local links, 5 recorded SHA256 hashes; staged diff empty; protected paths clean
PASS source audit: checker compiles without bytecode writes; imports only __future__, fractions, sympy
```

git diff --check, with the same read-only safe.directory option, produced
empty stdout and no whitespace errors. Status exited 0 with the known
global-ignore permission warnings. Protected paths are every path outside
the whitelist: previous proofs/dossiers, paper_assets/, results/, src/,
tests/, scripts/, verify.py, metadata, README, REPORT, all other ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md.
Their working-tree diffs are empty; the three imported proof hashes also
match their pre-task values. No generated/publication/certificate path
changed and no Git/GitHub state was written. The publication/code paths
were inspected for relevance at startup, not subjected to new certificate
or paper-build verification.

## Residual uncertainty

External independent review remains pending. Recovery of this one coupling
does not identify the relaxation minimum, the best permuted-halves
coefficient or a global optimum.
No general sufficiency theorem for the balanced marginal constraints is
claimed. The imported exact full criterion, uniform root transfer and
alpha_* definition remain dependencies. The existing finite global
certification scope and published arXiv-v1 assets are unchanged.
