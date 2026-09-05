# Evidence

## Environment

```text
repository_head=ae2b7ab2de614b798950fc2192437880078b5b3a
platform=Windows, PowerShell
python=3.14.3 (tags/v3.14.3:323c59a, Feb 3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
mpmath=1.3.0
dependency_source=existing canonical Python environment; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Recovery at every fixed alpha in I, for all integers m | exact theorem | proof note Section 2; floor/seam derivation | new derivation audited against original construction and bounded rational checks | the finite checks alone do not prove convergence |
| Correct full coefficient and negative alpha derivative | exact theorem | proof note Sections 3-4; full scaling with moving wrap | original unnormalized full-max quadrature and derivatives corroborate it | exact shift/minimizer theorems are imported |
| Three D enclosures, rational witness and coefficient gap | exact rational inequalities within the theorem | 128-panel concave enclosures, analytic E saving, rational arithmetic | new stdlib gate uses no old checker or numerical library; older gate rerun separately | isolated gates are not geometric certificates |
| Limit of R_full and actual full-feasible placements | exact fixed-order theorem | proof note Section 5 | imported arbitrary-permutation full criterion and uniform-root theorem; local geometry diagnostics | no new independent proof of those complete dependencies |
| Global limsup at most C_107 | proved corollary | proof note Section 6, feasibility then deletion | analytic deduction | no global optimum, matching lower bound or limit existence |
| Decimal coefficients/derivatives and finite geometry | numerical observations | canonical mpmath diagnostics below | independent of production and exact-gate integration method | finite diagnostics are not interval certificates or asymptotic proofs |

Detailed mathematics is only in research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md.
The fixed-order ledger owns coefficient definitions and comparisons; the
global ledger owns only their global feasibility/deletion consequences.

## Commands and checks

All commands below were actually run in this task and are LOCAL. The Git
commands use the per-command safe.directory setting for this repository;
they do not write configuration. Startup status was empty and the recorded
HEAD was returned. Git's global-ignore access warning did not change these
results; final changed-path and explicit untracked checks were also run.

| Fresh command/check | Exit/result | Checks | Does not check |
|---|---|---|---|
| `python -c "import sys, mpmath; print(sys.version); print('mpmath', mpmath.__version__)"` | 0; versions above | available existing environment | hosted environment or new dependency installation |
| `python -S -u ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py --exact-only` | 0; seven lines below | rational D, domain/saving/slope/comparison gates and 1143 bounded recovery cases | imported theorem proofs or a finite geometric optimum |
| `python -u ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py` | 0; exact lines plus eleven diagnostic lines below | independent full-max quadrature/derivatives and all-pairs geometry for eight sizes | certified numerical intervals for those diagnostics |
| `python -S -u ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only` | 0; thirteen lines below | fresh reproduction of the accepted x_* and C_rp gates | fresh external review or rerun of its mpmath mode |
| In-memory `python -S -` source/path audit, passed through a literal PowerShell here-string | 0; three PASS lines below | all nine paths, local links, imports/compilation, hashes, protected sources, whitespace | mathematical theorem correctness |
| Read-only `git diff`, `git status --short --untracked-files=all`, `git diff --check` with per-command safe.directory | 0; four tracked edits, five additions, no whitespace errors | complete tracked delta and explicit path inventory | untracked contents without the additional direct audit |

New exact-mode output, reproduced at the start of the full run:

```text
PASS domain: I=[53/500,107/1000]; 1/4<lambda<A/3<b; b-lambda>131/250; r>=q+2 for every m>=2
EXACT D(53/500) in [-291996313,-291678132]/1000000000000
EXACT D(267/2500) in [5455478,5771744]/1000000000000
EXACT D(107/1000) in [79817835,80133624]/1000000000000
PASS alpha isolation: 53/500<alpha_*<267/2500<107/1000; D(107/1000)<9/100000
PASS exact comparisons: E(x_*)<-1/1728; C_alpha derivative<-1/12000 on I; C_rp-C_107>1/60000000; C_107<14191368/100000000
PASS recovery audit: 1143 rational cases, m=2..128; occurrence, cyclic predecessors, all seams, 3/m errors and nonlinear moment bound
```

The three printed rational intervals are outward roundings of the exact
Fraction endpoints onto a 10^-12 display grid. Each integrand square root
uses 10^-20 rational endpoints whose squares are checked in every call.
Concavity, not a numerical quadrature-error estimator, encloses the integral.
The printed E/slope/coefficient PASS line checks the rational steps of the
analytic implication, importing the accepted minimum property of E.

Additional full-mode output:

```text
PASS independent 70-digit quadrature: three D enclosures, three original full-max cost identities and alpha derivatives; fixed x_* stationarity
NUMERICAL x_* = 0.28763080286063766035065565849026884062
NUMERICAL alpha_* = 0.10678476019990019934581367851595784583
NUMERICAL derivative at alpha_* = -0.00014871812754564260518579634856740763676
NUMERICAL lambda(107/1000) = 0.31840729876672589000817581394872760657
NUMERICAL C_107 = 0.14191364800672086870511803312106187786
NUMERICAL C_rp-C_107 = 0.000000030642426925162515567690279722031540626
NUMERICAL m=16 full radius/(2m)^2 = 0.128516569290565516971938
NUMERICAL m=64 full radius/(2m)^2 = 0.138446927396207002648414
PASS finite witness diagnostics: 8 sizes, exact bracket-determined floors, +/-relative 1e-35 root signs, 11062 all-pairs angular and Cartesian checks
NOTE: diagnostics are numerical observations, not finite global certificates or proof of an asymptotic limit.
```

The alpha probes are 53/500, alpha_* and 107/1000 at fixed x_*; the
centered derivative step is 10^-18, with agreement tolerance 10^-32.
Cost identities agree within 10^-60. Finite sizes are
m=2,3,7,8,10,16,32,64. Rational endpoint floors select each exact order.
The full score is bisected for 190 steps; radius +/- relative 10^-35
has the stated opposite numerical signs. At the upper radius, gaps close
within 10^-60 and all pairs pass angular slack >-10^-45 and Cartesian
squared-distance slack >-10^-40. This is an independent numerical geometry
check, with no production scorer or standalone-verifier call.

Fresh imported exact-checker output:

```text
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
```

This was run separately, never imported by check_alpha.py. The accepted
theorem's analytic uniqueness argument remains its proof dependency.

Skipped as unrelated: full pytest suite, verify.py with or without frontier,
paper build, generated assets, hosted CI and further parameter experiments.
No production, finite certificate or publication path changed, so those
checks would not verify the new mathematical discriminator.

## Artifact and provenance checks

No finite certificate, publication asset or generated result is changed.
The proof and checker are authored sources based on the recorded HEAD,
not certified result artifacts. The two checker modes above are their
reproduction commands; no random seed, optimizer or nondeterminism is used
by the rational gates. Numerical decimals depend on canonical mpmath.

SHA256 of the actual local source bytes (protected sources agree with HEAD
after normalizing line endings):

| Source | SHA256 |
|---|---|
| research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md | 27ec250aaf59a6dab3777312bd4b051571064d96cc7e0fe44e2bbc4c00466292 |
| ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py | 5b8d1aec7b3968580f2adf905476aed67129d5c82004dbc637443304051180c5 |
| research/SHIFTED_ALTERNATING_HALVES.md | baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db |
| research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md | 407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3 |
| research/PERMUTED_HALVES_REFLECTED_PREFIX.md | 485fefd9238d97799cf0801a395fb1ab077707c3b007e3a4361c2ef0588608b1 |
| research/PERMUTED_ALTERNATING_HALVES.md | c746d16feb0d1ca67fea75d77c1c26b69b74e1d1a56c916086f4715fbf6f86ab |
| research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md | 4c7b4ae99140884f40611abf62147724a5194eb3c6b58f6d7ef6d9661fe97c63 |
| ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py | 439ac0ead71a03788bcefe72f4296a787a1e830140747192495ab8c9caa8c8d0 |

## Failed checks and negative evidence

Startup Git ownership, global-ignore warning and rg path failures are
preserved in TASK_LOG.md, as is one rejected documentation patch with no
partial changes. All mathematical checks passed on their first run; the
predeclared witness and gate thresholds were not adjusted after results.
No hidden alpha dependence invalidates the formula. In particular the
moving-wrap term is present, the reflected block still has a chain part,
and the finite floors are not differentiated.

## Final diff inspection

The complete tracked diff was read; the proof, checker and dossier additions
were inspected directly in full. Ordinary git diff alone omits all five
untracked files. A separate in-memory stdlib audit explicitly reads all
nine files, rejects trailing whitespace, missing final newlines, repeated
blank final lines and UTF-8 BOMs, and checks the exact changed-path whitelist.
It parses local Markdown links, compiles the checker in memory, audits its
AST imports, hashes the eight sources above, and compares the six protected
sources to HEAD after newline normalization. It uses only read-only Git
queries and asserts that staged diff is empty and HEAD is unchanged.

Observed audit output, exit 0:

```text
PASS source/path audit: 4 tracked edits, 5 additions, 7 local links; staged diff empty; HEAD unchanged
PASS source audit: in-memory compilation; canonical imports; six protected theorem/checker sources agree with HEAD after newline normalization
PASS whitespace: all 9 files including untracked additions; git diff --check exit 0; protected and generated paths clean
```

The nine-file whitelist is exactly:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__reflected_prefix_alpha/EVIDENCE.md
?? ops/TASK-20260905__reflected_prefix_alpha/TASK_LOG.md
?? ops/TASK-20260905__reflected_prefix_alpha/TASK_STATUS.md
?? ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py
?? research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md
```

Protected paths inspected for unexpected changes: all earlier proof notes
and dossiers, paper_assets/, results/, src/, tests/, scripts/, verify.py,
publication metadata, README.md, REPORT.md, other knowledge ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md. The published
angular model in paper_assets/ringmin_paper.tex was also read directly.
No incidental protected or generated edits, new certificates, Git history
writes or GitHub writes occurred. Coefficient ownership and the separate
global implication were checked; the central index needs no new module.

## Residual uncertainty

The new theorem awaits independent external review; the user identifies the
HEAD lambda theorem as the accepted input. The exact shift/minimizer,
all-pairs criterion and uniform-root theorems remain explicit dependencies.
The new local checks do not re-prove all of them. No minimum over alpha or
both parameters, general permutation/coupling optimum, finite global optimum,
normalized global limit, or explicit asymptotic tolerance cutoff is proved.
The lower coefficient, finite certified scope and historical publication
record are unchanged. No hosted CI or external review is claimed as run.

## Final documentation and handoff check

After the complete dossier was read, the source/path audit was rerun with
an added check of every recorded SHA256 against the corresponding file.
It exited 0, with exact output:

```text
PASS final file audit: 4 tracked edits, 5 additions, 7 local links; staged diff empty; HEAD unchanged
PASS final provenance: all eight recorded hashes match; six protected theorem/checker sources agree with HEAD; checker compiles in memory with canonical imports
PASS final whitespace: all 9 files including untracked additions; git diff --check exit 0; protected and generated paths clean
```

The mathematical sources and checker remained unchanged. The status files
were then marked READY_FOR_REVIEW and the handoff was appended to the log.
Exactly one next atomic task is the independent review specified in
TASK_STATUS.md and CURRENT_STATUS.md. Integration remains manual.

## User-authorized integration preparation

The subsequent explicit request, "Commit e push", authorizes committing
and pushing exactly this task's nine files. CURRENT_STATUS.md and
TASK_STATUS.md record that exception; the proof, checker and classifications
are unchanged. READY_FOR_REVIEW does not become an external acceptance.

Fresh integration-turn commands, both exit 0:

```text
python -S -u ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py --exact-only
python -u ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py
```

The seven exact output lines and eleven additional diagnostic lines match
the complete outputs above, including 1143 rational recovery cases and
11062 all-pairs checks. The complete tracked diff and the nine-path scope
were inspected, git diff --check exited 0, and the staged diff was empty.
Read-only Git queries identify main and the configured falker47/ringmin
origin. HEAD...origin/main has local divergence counts 0 and 0 at the
task-base SHA; this is not a fresh remote-state or hosted-CI check.

The final precommit audit checks all tracked edits and untracked additions,
whitespace, links and the recorded source hashes. Commit/push outcomes are
reported by the Git operations themselves; this precommit record asserts
no future operation success or independent mathematical acceptance.
