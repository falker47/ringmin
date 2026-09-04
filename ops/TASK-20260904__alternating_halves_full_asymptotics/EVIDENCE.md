# Evidence

## Environment

```text
repository_head=667f666afb6f74c010111364fd787bd09cf13590
platform=Windows PowerShell sandbox
python=3.14.3
mpmath=existing environment, 70 decimal digits in task-local checker
sympy=1.14.0
dependency_source=existing interpreter; no installation or network access
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `R_full(sigma_{2m})` is the unique root of `S_m(R)=sum_i max(A_i+B_{i-1},C_i)=2*pi` for every `m>=2` | exact finite fixed-order theorem | disjoint-cell necessity; displayed gap allocation; thick-shell high-cycle lemma; monotone lift to every low-high and low-low pair | direct 70-digit audit of both cyclic paths for all pairs at 23 finite sizes; production cross-check is separate | human proof review remains pending; finite diagnostics do not prove the universal quantifier |
| The only exact fixed-`R` obstruction families needed are adjacent pairs around each low valley and its consecutive-high chord | exact structural corollary | necessity uses these constraints; explicit gaps satisfying them satisfy all pairs | diagnostic reports chord/adjacent cell counts and all-pairs minimum slack | no claim that every listed constraint is essential at every finite `m` or that the recovered gap vector is unique |
| `R_chain(sigma_{2m})/(2m)^2->J/(2*pi)` | exact asymptotic theorem | uniform angular estimate, two adjacent-edge Riemann sums, seam bound, decreasing-root bracket | independent 70-digit chain roots through `n=640`; production roots through `n=160` | no sharp subleading expansion |
| `R_full(sigma_{2m})/(2m)^2->K/(2*pi)=0.14233385361931275491...<1/(2*pi)` | exact asymptotic theorem | exact root formula; triangular Riemann sum; analytic switch at `1/6`; exact integral evaluation and `K<1` inequality | symbolic 11-gate audit and 70-digit roots through `n=640` | decimal values are diagnostics only; no broader order is optimized |
| `limsup R*(n)/n^2<=K/(2*pi)` for all integer `n` | proved global corollary | minimization on even sizes and deletion of radius `2m` for odd sizes | logical audit separated from fixed-order numerical checks | no matching global lower bound, equality, normalized global limit, or global optimality |

The exact constants are

```text
J=0.8403167750249355302931142119123254816702...
J/(2*pi)=0.1337405685082586300956173740053113784491...
K=0.8943099777751159083841865331943078614178...
K/(2*pi)=0.1423338536193127549063856821900226040103...
1/(2*pi)=0.1591549430918953357688837633725143620345....
```

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` at startup | 0; empty | clean task base | ignored files |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin rev-parse HEAD` | 0; `667f666afb6f74c010111364fd787bd09cf13590` | exact base commit without changing Git config | worktree content |
| `python --version` | 0; Python 3.14.3 | interpreter identity | mathematics |
| `python -B ops/TASK-20260904__alternating_halves_full_asymptotics/check_diagnostic.py` | 0; five sizes `40..640`; final PASS | independent chain and formula roots, valley classification, exact gap closure, and both cyclic constraints for every pair at 70 digits | universal quantifiers or a sharp convergence rate |
| `python -B -O .../check_diagnostic.py --sizes 4 6 ... 38` | 0; all 18 even sizes pass | small cases, boundary behavior, all-pairs construction with assertions disabled | cases outside the finite selection |
| `python -B .../check_symbolic.py` | 0; 11 gates pass under SymPy 1.14.0 | both integrals, constant assembly, switch factorization, thick-shell polynomial gate, and exact square comparison | all-pairs combinatorial logic |
| `python -B -O .../check_symbolic.py` | 0; identical PASS | explicit gates survive optimized mode | mathematical independence from the displayed identities |
| production `full_radius_value` cross-check at `n=10,20,40` | 0; chain/full ratios match the independent root values | task formula versus production STN implementation | production is not independent evidence |
| production `full_radius_value` cross-check at `n=80` | 0; `0.1290933244968626`, `0.136825146522466` | larger production comparison | universal theorem |
| production `full_radius_value` cross-check at `n=160` | 0; `0.1313974885299687`, `0.1395572681252022` | reviewer-scale production comparison | exact digits beyond float64 or asymptotics |
| scoped final `git status --short --untracked-files=all` | 0; four intended tracked modifications and six intended untracked additions | final path inventory | ignored files |
| direct ten-file UTF-8/LF audit | 0; every path PASS | strict UTF-8, no BOM/CR, exactly one final LF | mathematical correctness |
| `rg -n "[\x20\x09]+$"` over all ten changed/added paths | 1; no matches | no trailing spaces or tabs, including untracked files | other formatting issues |
| `git diff --check` | 0; no output | tracked whitespace and conflict markers | untracked files, covered by direct audits |
| protected-path diff | 0; empty | no changes to paper, certification, implementation, tests, scripts, public overview, project index, build, or dependency paths | authorized proof, ledgers, roadmap, status, and dossier |
| `git diff --cached --name-only` | 0; empty | Git index remains untouched | unstaged worktree content |

Material output from the successful independent default checker:

```text
J=0.840316775024935530293114211912
K=0.894309977775115908384186533194
c_chain=0.133740568508258630095617374005
c_full=0.14233385361931275490638568219
n chain_ratio full_formula_ratio chord_cells adjacent_cells extra min_slack
40  0.124585566125532277 0.131466089223498975   5  15  1.42e-54 -2.94e-71
80  0.129093324496859904 0.136825146522528691  12  28  5.16e-54 -2.94e-71
160 0.131397488529969537 0.139557268125223375  25  55  1.74e-54 -3.57e-71
320 0.132563838199469881 0.140940266075415282  52 108  4.18e-54 -3.51e-71
640 0.133150854045114712 0.141635631882792259 105 215  3.69e-54 -3.62e-71
PASS: independent finite diagnostic and direct all-pairs gap audit
```

The `extra` column is the positive feasible-side bisection remainder after
180 steps. The negative `min_slack` values have magnitude below `4e-71` and
occur at intended tangencies under 70-digit rounding; the rejection threshold
is `-1e-55`. The three reviewer-scale ratios are reproduced independently.

## Failed checks and negative evidence

- The exploratory leading-order LP identified the chord/adjacency switch and
  seam allocation, but it was not a proof and was removed after the exact
  construction superseded it.
- A first optional SciPy Floyd-Warshall branch raised `NegativeCycleError` at
  the deliberately infeasible lower bracket rather than returning `False`.
  The independent high-precision formula-root and direct gap checks preceding
  it had passed. The redundant float64 path was removed rather than masking
  the exception.
- The first two symbolic-checker runs exited `1` at the correct `J` identity
  because SymPy retained `acosh(sqrt(2))` instead of normalizing it to the
  displayed logarithm. Exact positive-branch rewrite gates were added; the
  mathematical formula did not change.
- The first production cross-check command exited `1` with `SyntaxError`
  because literal backslash-`n` characters were passed to `python -c`. The
  corrected multiline command exited `0` and matched all selected roots.
- An unscoped final `git status` hit Git's dubious-owner guard. It was rerun
  read-only with command-local `safe.directory`; no Git configuration changed.

## Artifact and provenance checks

Not applicable: no production result, finite certificate, generated artifact,
or paper asset is in scope. The diagnostic scripts are task-local evidence and
write no output artifacts.

Final authoritative-note/checker SHA-256 values:

```text
da93a11ddd95c671c863f5879bd03a4725ba697c8360261474afff500899e014  research/ALTERNATING_HALVES_FULL_ASYMPTOTICS.md
f0b429efe2efae0cd1a24122c148808e727c448155ddcdea374eefe6a6889165  ops/TASK-20260904__alternating_halves_full_asymptotics/check_diagnostic.py
5d048c88afa6059ebf0832712df14aab3ee16a563a76c17a02c6987e69ea32a9  ops/TASK-20260904__alternating_halves_full_asymptotics/check_symbolic.py
```

## Final diff inspection

- Exactly four tracked files are modified:
  `CURRENT_STATUS.md`, the two owning thematic ledgers, and the roadmap.
- Exactly six files are added: the authoritative proof note and five dossier
  files (status, log, evidence, independent diagnostic, symbolic audit).
- The complete tracked diff and all six untracked files were inspected after
  final edits.
- Direct ten-file audits confirm strict UTF-8, no BOM/CR, exactly one final LF,
  and no trailing whitespace.
- `git diff --check` exits `0`; the Git index is empty.
- Protected `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `README.md`, `REPORT.md`,
  `paper_assets/`, `results/`, `verify.py`, `src/`, `tests/`, `scripts/`,
  build/dependency files, unrelated notes, and prior dossiers are unchanged.
- No generated file changed. Repository HEAD remains
  `667f666afb6f74c010111364fd787bd09cf13590`.

No pytest, production certificate verifier, paper build, or hosted CI run was
required: no production implementation, finite artifact, or publication
source changed. The production evaluator was used only for the stated
read-only cross-check.

## Residual uncertainty

Independent human proof review remains pending. The theorem does not optimize
any broader order family, find a sharp fixed-order subleading term, prove a
matching global lower coefficient or existence of `lim R*(n)/n^2`, identify
the exact switch cell at every finite `m`, or extend global certification
beyond `n=14`.
