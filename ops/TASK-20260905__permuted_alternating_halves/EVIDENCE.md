# Evidence

## Environment

```text
repository_head=6bc4ac31b96ffcccb8fcfacf7478ae148a82bb2e
accepted_baseline=6bc4ac31b96ffcccb8fcfacf7478ae148a82bb2e
platform=Windows-11-10.0.26200-SP0; PowerShell
python=3.14.3 (MSC v.1944 64 bit AMD64)
dependencies=existing environment; numpy 2.4.3, scipy 1.17.1, mpmath 1.3.0, sympy 1.14.0
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limits |
|---|---|---|---|
| Proposed equivalence for all m>=2, all P, all R>0 | Exact theorem | research/PERMUTED_ALTERNATING_HALVES.md, Sections 2-5 | Direct shell proof and both paths for every type; finite checks are not premises |
| Full feasible gap set equals the local cell polytope | Exact theorem | Same proof, (3) and Section 4 | Covers arbitrary allowed splits, both paths and exact closure |
| Unique full root, all optimal gaps and chain/full equality test | Proved immediate fixed-order corollaries | Proof Section 6 | No optimization over P, global optimum or new asymptotic bound |
| Small-permutation cell/LP agreement | Numerical observation | check_falsification.py before proof | Independent all-pairs LP and alternate angular formula; finite float64 probes only |
| Shell algebra/sign and finite path decomposition checks | Engineering fact / exact finite algebra and combinatorial checks | check_witness.py exact_gates and topology | SymPy/Fraction/integer checks; no production imports, not an all-m proof |
| Constructed witness angular and Cartesian checks | Numerical observation | check_witness.py | 70-digit, non-interval; independent scorer, bounded samples, no global certificate |
| Coefficient 1/8 is already disproved | Existing disproved claim, cross-reference only | knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md | Roadmap wording repaired; no new global result or duplication into another thematic ledger |

## Commands and checks

Read-only Git with command-local safe.directory and empty core.excludesFile:
status --short, exit 0, no output; rev-parse HEAD returned the SHA above.
Python version/dependency query: exit 0, versions above. Baseline registry
read via Google Drive: accepted SHA equals local HEAD; no write performed.

### Pre-proof bounded independent falsification

Executed locally from the repository root, before writing the proof:

```text
python -u ops/TASK-20260905__permuted_alternating_halves/check_falsification.py
```

Exit 0, complete stdout:

```text
PASS m=2: 2 permutations, 14 independent LP probes
PASS m=3: 6 permutations, 42 independent LP probes
PASS m=4: 24 permutations, 168 independent LP probes
PASS m=5: 120 permutations, 840 independent LP probes
PASS m=6: 720 permutations, 5040 independent LP probes
PASS: 872 permutations, 6104 probes, no discrepancy
min_abs_cell_margin=2.27313241e-05
Numerical falsification only; no all-m proof or global certificate.
```

Complete input: all m! permutations at each m=2..6, no symmetry quotient
and no RNG. Each order has probes R=m^2 times {1e-6,.01,.1,1,100} and
rho_float times {1-1e-5,1+1e-5}. The latter uses 64 bisections of the
conjectured cell sum on [1e-9,16m^2]. No root equality is inferred from
this computation. Probe margins within 1e-7 would fail as undecided;
none occurred. Enumeration counts are checked against factorial(m).

The LP uses unconstrained angular positions apart from fixing position 0
to zero, and BOTH difference inequalities for every unordered pair.
It never uses the cell inequalities as constraints. Its angle is computed
as 2*atan2(sqrt(ab),sqrt(R(R+a+b))), independently of the cell sum's asin
implementation. HiGHS primal/dual tolerances are 1e-9; successful LP
positions are checked against the full matrix with a -1e-7 residual guard.
Only statuses 0 (feasible) and 2 (infeasible) are accepted. These are
numerical LP outcomes, not exact Farkas or interval certificates.

Stopping rule was fixed before the run: first discrepancy prints m,P,R
and both results and stops, for later exact analysis; otherwise stop at
m=6. No discrepancy arose, so no candidate counterexample was discarded.
This is exhaustive in P on the stated finite m range, not exhaustive in R
and not an exhaustive global search over all circle orders.

### Post-proof exact gates and high-precision witness audit

Executed locally from the repository root:

```text
python -u ops/TASK-20260905__permuted_alternating_halves/check_witness.py
```

Exit 0, complete stdout:

```text
PASS: exact shell polynomial and positive rational branch gates
PASS: exact topology for 872 permutations, 107388 directed paths
topology_counts={'HH': 24328, 'LH adjacent': 10076, 'LH via highs': 48656, 'LL common high': 5038, 'LL via highs': 19290}; seam_paths=53694
PASS: high-precision cases=2, latest m=2
PASS: high-precision cases=8, latest m=3
PASS: high-precision cases=32, latest m=4
PASS: high-precision cases=152, latest m=5
PASS: high-precision cases=157, latest m=6
PASS: 157 roots, 1303 path audits, 1146 closed Cartesian audits
directed_pair_counts={'HH': 22354, 'LH': 56728, 'LL': 22354}; total=101436
min_angular_slack=-4.16561238e-70
min_normalized_cartesian_slack=-1.26591541e-70
PASS: three root splits, unclosed paths, extra closure in every small-cycle gap, symmetries
70-digit numerical observations only; exact gates are algebra/topology, not global certification.
```

The exact portion checks the shell polynomial with SymPy and the rational
positive branch margin 5/8 using Fraction. Topology independently traverses
both directions of every unordered pair for all permutations m=2..6,
identifies each actual complete valley and treats each partial end segment.
It verifies simplicity, high/low dominance, all five endpoint subcases,
and exactly 53694 seam-crossing paths among the 107388 directed paths.
This finite decomposition check corroborates the universal argument in the
proof; it does not itself prove all-m coverage.

The high-precision portion uses 70 decimal digits and 180 bisections on
[1e-9,16m^2], retaining the upper endpoint and requiring cell residual
between 0 and 1e-48. Inputs: all permutations m=2..5 (152) and the five
explicit m=6 permutations

```text
(7,8,9,10,11,12), (12,11,10,9,8,7), (7,12,8,11,9,10),
(12,7,11,8,10,9), (10,7,12,8,11,9).
```

Every case checks root constructions with cell excess split left/middle/
right, both path sums before closure at rho/10, and closure slack at 2*rho.
At m<=4, extra closure is tested in every gap and root placements are also
rotated/reflected; at m=5,6 closure is tested in gaps 0,m,2m-1, including
the low seam. All unclosed and closed paths use the independent atan2
scorer; every closed placement separately reconstructs center coordinates
and checks squared distance minus (a+b)^2, normalized by (R+a)(R+b).
Angular and normalized Cartesian residual guards are both -1e-55; closure
guard is 1e-60. Tiny negative reported values are within rounding guards,
not exact overlap claims. Counts include all transformations and splits.
Each checker imports neither src/ringmin nor verify.py nor any prior
checker. Independence of the LP is also structural: it solves the complete
position system rather than evaluating the proposed construction.

### Verification intentionally not run

No production pytest, standalone incumbent/frontier verifier, paper build,
artifact regeneration or hosted CI inspection was run: production,
certification, publication and their claims are unchanged. Local research
checks do not replace a global-pruning certificate or assert hosted CI green.

## Artifact and provenance checks

No certificate or publication artifacts are affected. Retained task-local
checker sources plus this dossier preserve the finite input specification
and outputs. Generation source is the recorded base plus the uncommitted
task diff; no generation commit is invented for new files.

Executed Get-FileHash -Algorithm SHA256 on both retained checker paths:
exit 0. Source hashes:

```text
check_falsification.py
37CD3E0C2F528F47738D9010E921726738011655EB098F884430F6A3BCCCE431
check_witness.py
BD9D763BCA27F391E4C79660CD111304D609DCD4DF9E709DA2CB102E99F64BBB
```

Reproduce with the recorded environment. Floating residuals may vary below
the guards on other platforms; polynomial, rational and path-count checks
are exact. No retained-frontier, generation-commit or certificate schema
has been changed, and no result in results/ has been regenerated.

## Failed checks and negative evidence

Initial plain Git calls failed due to sandbox ownership; a command-local
exception resolved them without changing configuration. User ignore-file
warnings were resolved with command-local empty core.excludesFile.
Both checker commands passed on first execution. No false mathematical
lemma, numerical discrepancy or unresolved input was suppressed. The
shifted proof's fixed-R shell/path argument extends unchanged in substance;
its later adjacent-high-difference-one asymptotic argument is shift-specific
and has not been generalized. The unshifted note's monotone single-edge
selection is not used for arbitrary P.

## Final diff inspection

Read the complete tracked git diff for CURRENT_STATUS.md,
knowledge/FIXED_ORDER_THEORY.md and research/NEXT_RESEARCH_STEPS.md.
Read all six untracked additions in full with Get-Content -Encoding UTF8:
the proof note, both checkers and all three dossier documents. Final
status/evidence edits receive another diff/readback and the same scope
audit. The proof's diagnostic description was narrowed to the actual three
tested cell-excess splits; its exact arbitrary-split theorem is unchanged.

Executed this local Python stdin audit from the repository root (PowerShell
single-quoted here-string piped to python -):

```python
from pathlib import Path
import subprocess
repo = Path.cwd()
git = ['git', '-c', 'safe.directory=' + repo.as_posix(), '-c', 'core.excludesFile=']
def read(*args):
    return subprocess.check_output(git + list(args), text=True).splitlines()
tracked = set(read('diff', '--name-only'))
new = set(read('ls-files', '--others', '--exclude-standard'))
dossier = 'ops/TASK-20260905__permuted_alternating_halves/'
assert tracked == {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md', 'research/NEXT_RESEARCH_STEPS.md'}, tracked
assert new == {'research/PERMUTED_ALTERNATING_HALVES.md'} | {dossier + p for p in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_falsification.py', 'check_witness.py')}, new
assert not read('diff', '--cached', '--name-only')
for name in sorted(tracked | new):
    data = (repo / name).read_bytes()
    text = data.decode('utf-8')
    assert data.endswith(b'\n') and not data.endswith(b'\n\n'), name
    assert all(line == line.rstrip() for line in text.splitlines()), name
    assert '\x00' not in text, name
assert subprocess.run(git + ['diff', '--check'], check=False).returncode == 0
print('PASS: exactly 3 tracked and 6 new allowed files; no staged or protected/generated changes')
print('PASS: explicit whitespace/UTF-8/final-newline audit over all 9 files, including untracked additions')
print('PASS: git diff --check exit 0, no output')
```

Exit 0, exact stdout:

```text
PASS: exactly 3 tracked and 6 new allowed files; no staged or protected/generated changes
PASS: explicit whitespace/UTF-8/final-newline audit over all 9 files, including untracked additions
PASS: git diff --check exit 0, no output
```

The audit covers untracked text explicitly, which ordinary git diff --check
omits. The whitelist and empty staged diff protect every other tracked
path, including paper_assets/, results/, src/, tests/, scripts/, verify.py,
README.md, REPORT.md, publication metadata, earlier proof notes/dossiers,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, PROJECT_KNOWLEDGE.md and other
knowledge modules. No certificate, generated asset or publication record
changed incidentally. No stable claim was added to multiple thematic
modules; the sole fixed-order owner and existing index navigation agree.

Final status --short --untracked-files=all inventory:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__permuted_alternating_halves/EVIDENCE.md
?? ops/TASK-20260905__permuted_alternating_halves/TASK_LOG.md
?? ops/TASK-20260905__permuted_alternating_halves/TASK_STATUS.md
?? ops/TASK-20260905__permuted_alternating_halves/check_falsification.py
?? ops/TASK-20260905__permuted_alternating_halves/check_witness.py
?? research/PERMUTED_ALTERNATING_HALVES.md
```

## Residual uncertainty

Independent human proof review remains pending. The theorem is fixed-order
for the specified halves and does not optimize P, prove any new global
asymptotic bound, extend certified n, or classify contact/floating behavior
in global optima. High-precision and LP checks are finite non-interval
observations; the written proof is the authority for all m and all R.
No hosted CI run was inspected and no acceptance decision is made here.
