# Evidence

## Environment

```text
repository_head=7ac01f36bb7ed2c7f800867e3689c6f01c20b43b
platform=Windows-11-10.0.26200-SP0; PowerShell
python=3.14.3 (MSC v.1944 64 bit AMD64)
dependencies=existing environment; mpmath 1.3.0, scipy 1.17.1, numpy 2.4.3, sympy 1.14.0
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limits |
|---|---|---|---|
| Exact fixed-R cellwise equivalence for all shifts | Exact theorem | Proof Sections 2-3 | Fresh shell proof and both paths for all endpoint types; finite audits corroborate only |
| Every shift-ratio sequence has the stated chain/full limits | Exact asymptotic theorem | Proof Sections 4-5 | Uniform estimates include moving wraps and alpha endpoints; no finite scan premise |
| Unique full-coefficient minimizer within the shift family | Exact theorem | Proof Section 6 | Analytic derivative signs and curvature; no numerical optimizer premise |
| Strictly improved all-integer global limsup | Proved corollary | Proof Section 7 | Deletion of an actual feasible even configuration; no global equality or global limit |
| Rational witness coefficient enclosures | Computer-certified finite result (constant inequalities only) | check_exact.py, directed Fraction sqrt/log/pi bounds | Independent of production and floating arithmetic; not a certificate of any Ringmin global optimum |
| Decimal alpha_* and coefficients | Numerical observation | check_diagnostic.py derivative-integral root and split quadrature | 70-digit mpmath, non-interval; exact minimizer is defined implicitly |
| Finite witness angular and Cartesian feasibility | Numerical observation | Direct all-pairs audit | No production imports; 1e-55 guard, not a global certificate |
| LP bracket agrees with finite cell root | Numerical observation | Separate full linear-inequality model, HiGHS | Float64 and numerical feasibility tolerances; does not prove all-n equivalence |

## Commands and checks

- Read-only Git status with command-local safe.directory and an empty
  core.excludesFile: exit 0, no output (clean tree).
- Python environment query: exit 0, versions recorded above.
- See TASK_LOG.md for initial ownership, exclude-file and guessed-path failures.

### Exact arithmetic and symbolic checker

Command (repository root, local):

```text
python ops/TASK-20260905__shifted_alternating_halves/check_exact.py
```

Exit 0, exact stdout:

```text
PASS: symbolic primitive, switch, shell, derivatives and boundary gates (sympy 1.14.0)
PASS: exact rational sign and Machin identity gates
PROVED ENCLOSURE: 0.14199597949 < K(107/1000)/(2*pi) < 0.14199597951
PROVED ENCLOSURE: 0.14233385361 < K(0)/(2*pi) < 0.14233385363
PASS: rational witness strictly improves the unshifted coefficient
```

SymPy corroborates algebra; the enclosure uses only integer/Fraction arithmetic.
The sqrt grid is 10^-35, log arguments are reduced to [1,2] before 80
positive atanh-series terms and an explicit geometric tail, and pi uses
80-term alternating atan bounds in the Machin identity. It does not prove
the combinatorial all-pairs theorem or a global packing certificate.

### Bounded independent diagnostic

Command (repository root, local):

```text
python -u ops/TASK-20260905__shifted_alternating_halves/check_diagnostic.py
```

Exit 0, exact stdout:

```text
alpha_star=0.106784760199900199345813678515957845828
C_shift=0.1419959781277142849792181240454246687915
C_107_1000=0.1419959794984599508468255894688355006728
PASS: split direct quadrature matches all three functional regimes
n=80 s=4 chain_ratio=0.12776634130343687457 full_ratio=0.13633906053774542595
n=160 s=9 chain_ratio=0.12946587071966768764 full_ratio=0.13912814336111895982
n=320 s=17 chain_ratio=0.13053449486047406448 full_ratio=0.14055734405570568141
PASS: 65 finite cases; 160490 directed pair checks
PASS: 44 all-shift cases m=2..9, LP infeasible below / feasible above cell roots
PASS: rotation/reflection, positive closure slack, seam/transition and domain checks
min_angular_slack=-3.6222716e-71
min_normalized_cartesian_slack=-1.2617654e-70
Numerical observations only; no global-optimum or all-n certification.
```

The deterministic parameter list is all shifts for m=2..9; nine seam/transition
shifts each at m=12,20; and s=round(0.107m) at m=40,80,160. The stopping rule
is this fixed list, 160 bisections per chain/full root, and 70 decimal digits.
Each main audit checks every unordered pair's two directions and a separately
constructed Cartesian squared distance. The normalized Cartesian residual
divides by (R+a)(R+b); both residual guards are -1e-55. The printed tiny
negative residuals are rounding, not exact negative slacks. Additional
rotation/reflection audits at m<=5 are not included in the printed 160490
main directed-pair count. R=2*full_root checks at m<=3 exercise extra closure.

The independent scipy LP uses all pair lower/upper difference constraints;
it does not use the cellwise formula except to select probe radii. At every
shift for m=2..9 it is infeasible at root-eta and feasible at root+eta,
eta=1e-5*max(1,root), with primal/dual feasibility tolerances 1e-9. This is
finite float64 corroboration, not rigorous interval feasibility or global
certification. The direct gap witness is calculated in mpmath independently
of this LP, the production code, and verify.py.

### Checks intentionally not run

No production pytest suite, standalone frontier verifier, publication build,
artifact regeneration or hosted CI query: production, verification,
certificate and published claims are not changed. Local math checks do not
replace any certificate verifier and do not assert hosted CI is green.

## Artifact and provenance checks

No certificate or publication artifact was generated. Task-local diagnostic
output is preserved above; no results/ file or machine-specific path was
created. Input definitions, fixed parameter list, guards and no-RNG policy are
in the retained sources. Source base is the HEAD recorded above plus this
uncommitted task diff; there is no invented generation commit for new files.

Command: Get-FileHash -Algorithm SHA256 on the two checker paths; exit 0.

```text
check_exact.py
FAB91545A030F6458924463F9A8023BEDDE754D1526560654ADD2DB3AFA0D7CF
check_diagnostic.py
2CFD03778C32301D5AAF2186103503FD54B2799B004F17137DE0A657EC111C9F
```

Reproduction requires the recorded existing dependencies. Floating output can
vary below the reported guards across implementations; rational inequalities
are exact. No finite certification artifact provenance is affected.

## Failed checks and negative evidence

Startup plain Git reads failed due to sandbox ownership. Command-local
safe.directory resolved this without writing configuration. A command-local
NUL exclude-file experiment failed, while an empty excludesFile worked. The
initial guessed fixed_order.py source path was absent; rg located the actual
modules. One duplicate-path update patch was rejected atomically and then
replaced with a single update. These were tool/environment failures, not
mathematical counterexamples. Both retained checker commands passed on their
first execution. Alpha=0 being optimal is disproved within the shift family.

## Final diff inspection

The full tracked diff was inspected for all four modified tracked files;
all six untracked files were read in full with Get-Content -Encoding utf8.
Later status-only edits were read again. Final inventory:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__shifted_alternating_halves/EVIDENCE.md
?? ops/TASK-20260905__shifted_alternating_halves/TASK_LOG.md
?? ops/TASK-20260905__shifted_alternating_halves/TASK_STATUS.md
?? ops/TASK-20260905__shifted_alternating_halves/check_diagnostic.py
?? ops/TASK-20260905__shifted_alternating_halves/check_exact.py
?? research/SHIFTED_ALTERNATING_HALVES.md
```

The exact final audit was run locally using a PowerShell literal here-string
piped to `python -`, with the following body (exit 0):

```python
from pathlib import Path
import subprocess
root = Path.cwd()
git = ['git', '-c', 'safe.directory='+root.as_posix(), '-c', 'core.excludesFile=']
def read(*args):
    return subprocess.check_output(git+list(args), text=True).splitlines()
tracked = read('diff', '--name-only')
untracked = read('ls-files', '--others', '--exclude-standard')
expected_tracked = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md', 'knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md', 'research/NEXT_RESEARCH_STEPS.md'}
dossier = 'ops/TASK-20260905__shifted_alternating_halves/'
expected_new = {'research/SHIFTED_ALTERNATING_HALVES.md'} | {dossier+name for name in ['TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_exact.py', 'check_diagnostic.py']}
assert set(tracked) == expected_tracked, tracked
assert set(untracked) == expected_new, untracked
assert not read('diff', '--cached', '--name-only')
for name in tracked+untracked:
    text = (root/name).read_text(encoding='utf-8')
    assert text.endswith('\n'), name
    assert all(line == line.rstrip(' \t') for line in text.splitlines()), name
print('PASS: 4 tracked and 6 untracked files match the authorized scope; no staged files')
print('PASS: explicit whitespace/newline checks for all 10 files, including every untracked addition')
print('PASS: no protected or generated path changed')
subprocess.run(git+['diff', '--check'], check=True)
print('PASS: git diff --check (exit 0, no output)')
```

Stdout is exactly the four PASS lines in that body; the Git check is silent.
The scope inventory is stronger than checking only selected protected paths:
no tracked or untracked change outside the allowed set is present. In
particular paper_assets/, results/, verify.py, src/, tests/, scripts/,
README.md, REPORT.md, AGENTS.md, PROJECT_KNOWLEDGE.md, prior proof notes and
prior dossiers have no diff. No artifact generation occurred. Ignored local
progress logs were not regenerated or audited; they are irrelevant to this
fixed-order proof task. This is an engineering scope check, not a theorem
verifier. No stable claim was duplicated between thematic owners.

## Residual uncertainty

Independent human proof review will remain pending. No hosted CI, global
certificate expansion, global equality or normalized global limit is claimed.
