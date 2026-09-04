# Evidence

## Environment

```text
repository_head=2a7ccef05a2217146387e92507b2eab9910a174f
platform=Windows / PowerShell / local sandbox
python=3.14.3, MSC v.1944 64 bit
mpmath=1.3.0
sympy=1.14.0
dependency_source=pre-existing environment; no installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Two changing cells; m=2 invariance | Exact identity | Proof note Section 1; full atan cell sums | Scorer independent of production and local threshold formula | Full-feasibility interpretation uses the preceding theorem |
| Branch threshold, local increment, exchange/equality conditions | Exact conditional theorem | Sections 2-4; symbolic identities and finite branch checks | Symbolic and alternate-angle checks, not a separate human proof review | Ordering conditions are sufficient, not necessary in compensating cases |
| m-2 candidate reduction; exclusion of shifts | Proved structural corollary | Section 5; all-chain branch and strict swaps | Finite numerical exclusion audit corroborates | Only fixed-R, 0<R<=1; not all candidates optimal |
| m=3 swap sign reversal | Disproved universal ordering rule; exact local counterexample | Section 6; Fraction branch tests and angular enclosures | Exact checker uses no production or earlier checker | Does not exclude every possible conditional exchange rule |
| Low/high Monge and anti-Monge signs both fail; high/high weak increasing differences survive | Exact theorem / disproved claims | Section 6 derivative proof and exact endpoint branches | Rational witness checks separate from proof | These are different coordinate pairs |
| 872 orders and bounded high-precision scans | Numerical observations | Scripts/output below | Alternate atan scorer, no production/verifier imports | Neither all-R proof nor global certificate |

The single thematic owner is knowledge/FIXED_ORDER_THEORY.md. The proof
note is authoritative for mathematical details; the dossier is task-local
evidence. No global certificate, published claim, production algorithm or
asymptotic bound is modified.

## Commands and checks

Startup read-only checks: clean status and HEAD above. The first ordinary
git status exited 1 (ownership); the per-command safe.directory variant
exited 0. Python/dependency inspection exited 0 with the versions above.

All commands in this dossier were LOCAL. No hosted CI run was inspected,
no continuous-reviewer result is claimed, and no acceptance was recorded.
Git read commands use the per-command safe.directory exception; no Git
config, history, index or GitHub state was written. The sandbox warns that
the user's global ignore file is unreadable, but repository status works.

### Pre-proof finite falsification

```text
python ops/TASK-20260905__adjacent_high_swap/check_falsification.py
exit=0
m=2 complete
chord_sign_fails (3, (4, 5, 6), 0.1, 1, -0.006717127704814807, 1, 3, 6, 6)
chain_sign_fails (3, (4, 5, 6), 100, 1, 0.0029808354318363317, 1, 3, 6, 6)
coordinate_dominance_fails (3, (4, 5, 6), 100, 1, 0.0029808354318363317, 1, 3, 6, 6)
m=3 complete
cyclic_shifts_not_minimal (4, (6, 8, 7, 5), 10, 4.385769117521286, 4.393107989781858)
m=4 complete
m=5 complete
m=6 complete
low_high_submodularity_fails (3, 1, 2, 4, 5, 6, 0.1, 0.002996866639877638)
low_high_supermodularity_fails (3, 1, 2, 4, 5, 6, 100, -0.002214528987655784)
COUNTS {'orders': 872, 'swaps': 15114, 'fixed_radius_shift_comparisons': 5232}
Finite float64 observations only; no universal proof or global certificate.
```

The script also prints FIRST_WITNESSES, repeating exactly the six witness
records above. Tuple fields for swaps are m,P,R,j,Delta,l,r,u,v;
shift records contain m,P,R,S_P,min_shift_S; cross-difference records
contain m,t,t',a,x,y,R,M. Domain: all permutations m=2..6, no symmetry
quotient, six radii {0.1,1,2,5,10,100}, ascending cyclic swaps, no RNG.
Signs within 1e-10 are undecided. The first lexicographic robust failures
are retained. The final guard refinement described in TASK_LOG reran
this command with identical witness records/counts, exit 0.

This is an independent direct-cell stdlib scorer, but uses the criterion
under study. It does not independently re-prove the preceding all-pairs
feasibility theorem, decide all radii or certify global optima.

### Exact and independent local checks

```text
python ops/TASK-20260905__adjacent_high_swap/check_exact_and_local.py
exit=0
PASS symbolic: angular derivatives, pocket addition, threshold polynomial
PASS exact swap m=3 R=1: -17413/1000000 < Delta < -4353/250000
PASS exact swap m=3 R=100: 149/50000 < Delta < 2981/1000000
PASS exact low/high cross difference: positive at R=1, negative at R=100
PASS exact m=4 R=1: (8, 6, 5, 7) beats all four shifts by > 1/125
PASS exact m=4 R=10: (6, 8, 7, 5) beats all four shifts by > 7/1000
PASS exact branch equality and infinite-threshold boundary probes
PASS numeric m=2: all permutations/seams and small-R exclusion
PASS numeric m=3: all permutations/seams and small-R exclusion
PASS numeric m=4: all permutations/seams and small-R exclusion
PASS numeric m=5: all permutations/seams and small-R exclusion
PASS numeric m=6: all permutations/seams and small-R exclusion
PASS numeric: orders=872, swaps=30228, conditional_probes=12000
integer_swap_branch_pairs=CC,CH,CM,HC,MC
max_abs_local_vs_full_atan_error=2.8978173e-70
PASS positive-real cell probes: all nine branch pairs, finite endpoints, infinite equality
max_abs_positive_real_increment_error=9.0556791e-72
Exact local inequalities plus finite 70-digit corroboration; no global certificate.
```

Both the initial and final refined versions exited 0. The source uses
SymPy for exact derivative, pocket-addition and threshold-polynomial
identities. Fraction branch tests check the sign before squaring. For
angular enclosures, set q=ab/((R+a)(R+b)) in (0,1), enclose sqrt(q)
between consecutive multiples of 10^-40 using integer isqrt, and use

```text
asin(sqrt(q))=sqrt(q) sum_{n>=0} c_n q^n,
c_0=1,
c_{n+1}/c_n=(2n+1)^2/[2(n+1)(2n+3)] in (0,1),
0 < sum_{n>=300} c_n q^n <= q^300/(1-q).
```

All these operations and tail bounds are rational; no float decides the
retained enclosures. The checker asserts angular enclosure width <10^-20
on its inputs. Interval addition/subtraction/max is outward by construction.
This proves the local strict signs and their margins, not a global-optimum
certificate or any universal rule inferred from sampling.

The mpmath part uses 70 decimal digits, a 10^-60 comparison guard, all
872 permutations at the same six radii and BOTH orientations of every
cyclic adjacent swap. It compares the threshold/asin local formula against
full direct cell sums using theta=2 atan2(sqrt(ab),sqrt(R(R+a+b))). It
checks the two changing cells, unchanged middle/other cells, m=2, m=3,
wraps, conditional signs and the small-R necessary candidate reduction.

The integer domain realizes only five increment-branch pairs. Six additional
positive-real cells are constructed with desired threshold b0 in {2,4.5,10},
R=10, x=4,y=5 and the fixed high a=6 or 7; their low is exactly defined by
the pocket formula. Their nine paired increments are compared explicitly.
These probes are NOT integer-half permutation instances. An exact rational
finite crossing (R,t,a,B)=(1,2/15,1,2/3) exercises both clipped endpoints
and an interior crossing; (R,t,a)=(4,1,4) exercises the infinite-threshold
equality boundary. All universal domain/equality claims rely on the proof.

No script imports src/ringmin, verify.py, or another task checker. Their
independence is from production and from the local numerical formula on
the comparison side, not a separate human review of the proof.

### Exploratory commands and skipped layers

Two task-local PowerShell here-strings piped to `python -` exited 0.
The first used mpmath at 40 digits and the alternate atan formula for
P=(4,5,6),(5,4,6) at R=0.1,1,100, then 145 bisections on [0.001,100]
for the four m=4 shifts and P=(6,8,7,5). It observed roots about
5.84042172736689719725 for that P and 5.78356008585700147567 for
(7,8,5,6). These are non-interval numerical observations, kept only to
reject transferring the R=10 comparison to root dominance.

The second compared the four shifts and their adjacent swaps at
R=1,2,5,10,100, yielding the simpler R=1 witness subsequently checked
exactly. These exploratory outputs are superseded for stable sign/shift
claims by the retained exact checker; no general root search was run.

Production pytest, the global certificate verifier, all-pairs LP reruns,
paper build and hosted CI were not run: their code, artifact inputs,
published claims and prior theorem are protected and unchanged. This
task verifies the local mathematical delta and does not recertify them.

## Artifact and provenance checks

No production or publication artifacts regenerated. The only computed
outputs retained are the task-local evidence above; both checkers print
their results and write no output files. Exact run commands and finite
inputs are specified above. Source provenance is the base HEAD plus these
uncommitted task sources, not a claim that the base commit contains them.

SHA256 of the final source bytes (Get-FileHash -Algorithm SHA256, exit 0):

```text
check_falsification.py
5df8a79bc7a24223c0f605abb64408df6efdfef3c1906b8e0cd3b42c3bb2587c
check_exact_and_local.py
e86d95ae0f05d3caf6b62f82a85cc7f0f382c8873cc4cd2cb84722230225b9e0
research/PERMUTED_HALVES_ADJACENT_SWAP.md
4f0916670376ecfe563984522464c542eb7e1e82187fe412c2abf5ef5df1f260
```

The two script paths are relative to this dossier. No RNG, multiprocessing,
checkpoint or factorial computation beyond m=6 is used. Reproduction needs
the stated existing Python, mpmath and SymPy environment; SymPy is used by
this task checker and was not added to project dependencies.

## Failed checks and negative evidence

The universal chain-only, chord-only and low/high coordinate-order rules
failed the pre-proof scan. Both low/high Monge orientations failed too.
The robust minimal m=3 swap is proved with exact branches/enclosures in
the note; m=2 invariance proves its minimality. This does not disprove
high/high weak supermodularity or the threshold-conditioned exchanges.

No proof/checker run failed. The initial Git ownership failure and the
rejected duplicate-path apply_patch operation are recorded in TASK_LOG;
both were resolved locally without changing Git state or unrelated work.

## Final diff inspection

The complete tracked diff was inspected with
`git -c safe.directory=<repository-root> diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md`.
Every untracked addition was read in full with Get-Content -Encoding utf8;
truncated tool-output portions were requested again. Final small edits to
the rational gates, symbol definitions and handoff were inspected too.

An additional inline Fraction check (`python -`, exit 0) computed
e=1/t-1/100-1/a-1/b and 4D-e^2 for the eight triples in Section 6,
confirming every rational value there. This exposes the exact branch proof
in the note instead of requiring its reader to run a checker.

The local inline stdlib audit (`python -`) reads Git's tracked diff and
untracked inventory, requires exact equality with the nine-file whitelist,
requires an empty staged diff, reads every allowed file as UTF-8, checks
final newline/trailing whitespace/conflict markers, and compares source
SHA256 with the recorded values. It invokes the same per-command Git
exception and `git diff --check`. Exit 0, material output:

```text
PASS whitelist: exactly 3 tracked modifications and 6 untracked additions; staged diff empty
PASS UTF-8, final newline, trailing whitespace and conflict-marker audit: all 9 files
PASS every other tracked path protected, including paper, results, src, tests and verifier
PASS recorded script SHA256: check_falsification.py
PASS recorded script SHA256: check_exact_and_local.py
PASS git diff --check: exit 0, no output
```

This explicitly checks untracked text, which ordinary git diff --check
omits. The source-note hash was updated after adding the rational gates.
No stable claim was duplicated in another thematic ledger; the canonical
index's existing navigation remains accurate. The protected-path audit
covers all other tracked paths, including the preceding proof, prior
research/dossiers, paper_assets/, results/, src/, tests/, scripts/,
verify.py, README, REPORT, publication metadata, other ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md.

Final status inventory:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__adjacent_high_swap/EVIDENCE.md
?? ops/TASK-20260905__adjacent_high_swap/TASK_LOG.md
?? ops/TASK-20260905__adjacent_high_swap/TASK_STATUS.md
?? ops/TASK-20260905__adjacent_high_swap/check_exact_and_local.py
?? ops/TASK-20260905__adjacent_high_swap/check_falsification.py
?? research/PERMUTED_HALVES_ADJACENT_SWAP.md
```

## Residual uncertainty

Independent human proof review and acceptance remain pending. The exact
exchange conditions are sufficient; their failure does not determine
the sign without the explicit increment comparison. Local minimality
does not imply global minimality. The small-R reduction is not extended
to full-radius roots, general permutations or asymptotics. The geometric
fixed-order interpretation imports the preceding proof, which this task
does not independently recertify. No global bounds, certificates,
publication record or production behavior were changed. No hosted CI
claim or external review decision is made.
