# Evidence

## Environment

```text
repository_head=d90495981414e18344585c446ad8b68bf8276f54
platform=Windows PowerShell
python=3.14.3 (MSC v.1944 64 bit AMD64)
mpmath=1.3.0
dependency_source=existing project environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `32<T_{3,16}` and `T_{3,17}<32` | exact theorem (endpoint lemma) | rational radical reductions and three positive square margins in the proof note | independent derivations, checker `Fraction` audit, adversarial review | concerns only the Descartes seam thresholds |
| `R_{3,16}<32<R_{3,17}` | exact theorem (endpoint lemma) | all 29 chain edges bounded term by term; exact arcsine and pi inequalities | independent recomputation of every row and total; checker audit | concerns adjacent-chain roots only |
| `Delta_{3,n}>0` for `5<=n<=16` and `<0` for all `n>=17`; hence `s_3=17` | exact theorem | endpoint lemmas plus the fixed-`k` no-threshold, root-growth, threshold-decrease, and persistence theorem | three read-only proof reviews | one formal seam; no full-feasibility or global-optimum conclusion |
| Exact checker audit gates remain active under optimization | engineering fact (locally verified) | identical explicit-gate output normally and under `python -O -S`; AST has zero `Assert` nodes | local command and independent checker review | checker corroborates transcription; it is not a theorem source |
| Checker is production-independent | engineering fact (locally verified) | AST has zero `ringmin` imports; exact path also runs under `python -S` | AST audit and production comparison kept outside checker | it still shares displayed rational constants with the note |
| Selected finite numerical signs agree with the theorem | numerical observation | opt-in 60/100-digit scan through `n=120` | task-local high-precision implementation, no production import | finite diagnostic only; not the all-`n` proof |
| Task-local order convention agrees with production | engineering fact (locally verified) | targeted comparison over `n=5..200` | independent task-local and production constructors compared | finite integration check, not Supnick's theorem |
| Existing regression suite still passes | engineering fact (locally verified) | `python -m pytest -p no:cacheprovider` | production tests include separate geometric checks | not a seam proof, global certificate, or hosted CI run |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | exit `0`; no output | clean startup tree | mathematical correctness |
| `python -B ops/TASK-20260804__radius3_seam_onset/check_seam.py --order-stop 250` | exit `0`; `62,594` exact audit gates pass | rational tables, threshold margins, arcsine domains, edge formulas, endpoint orders | the imported all-`n` theorem or numerical roots |
| `python -B -O -S ops/TASK-20260804__radius3_seam_onset/check_seam.py --order-stop 250` | exit `0`; identical `62,594` gates pass | exact audit gates cannot disappear in optimized mode; stdlib-only exact path | high-precision diagnostics |
| `python -B ops/TASK-20260804__radius3_seam_onset/check_seam.py --order-stop 200 --diagnostics --start 5 --stop 120 --digits 60 --stability-digits 100` | exit `0`; `40,094` exact gates and all finite diagnostic gates pass | two-precision roots, signs, root/threshold comparisons, monotonicities, raw-deficit negative control | values beyond `n=120` or the all-`n` proof |
| targeted task-local/production comparison shown below | exit `0`; `392` comparisons pass for `n=5..200` | production integration of shifted Supnick convention | anti-Monge/Supnick theorem |
| AST import/`Assert` audit shown below | exit `0`; zero `ast.Assert`, zero production imports | optimized safety and checker independence at syntax level | runtime behavior of external packages |
| `python -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 29.90s` | current production regression suite | independent mathematical proof, certificates, hosted CI |
| three fresh read-only adversarial reviews of the actual note/checker/dossier | proof review found one arcsine-domain wording issue; checker review found none; scope review found dossier inconsistencies; all were corrected | arithmetic, edges, inequalities, quantifiers, scope, checker architecture, durable-memory consistency | independent human review after handoff |
| direct eight-file UTF-8/LF/whitespace audit | exit `0`; all eight authorized paths pass | strict UTF-8, no BOM, LF only, one final LF, no trailing whitespace | mathematical correctness |
| final `git diff --check` | exit `0`; no output | tracked-diff whitespace errors | untracked files, covered by the direct audit |
| protected-path `git status` | exit `0`; no output | absence of changes in paper, production, tests, scripts, results, verifier, generated/report, dependency, and existing-note paths | ignored files outside the explicit protected list |

### Post-correction checker material output

```text
independent_of_production=PASS (no ringmin imports)
exact_rational_transcription_audit=PASS explicit_gates=40094 optimized_safe=YES
exact_threshold_domain_and_R32_bridges=PASS n=12,13,16,17
exact_termwise_chain_bridges_at_R32=PASS n=16,17
shifted_order_conventions_and_edge_sets=PASS n=5..200
theorem_sources=research/RADIUS3_SEAM_ONSET.md+research/FIXED_K_SUPNICK_SEAM.md
numerical_diagnostics=PASS n=5..120 digits=60/100
precision_stability=PASS max_relative_R_delta=4.9938395e-46 max_absolute_deficit_delta=2.0053366e-46
n=005 R_3n=0.596032619373617232 T_3n=NA deficit_lhs_minus_rhs=1.96429623459383036
n=012 R_3n=15.0541630000962121 T_3n=NA deficit_lhs_minus_rhs=0.19093593918284572
n=013 R_3n=18.2047352790269857 T_3n=227.782487939842683 deficit_lhs_minus_rhs=0.131207897548364981
n=016 R_3n=29.1949884981699292 T_3n=35.8596372213588973 deficit_lhs_minus_rhs=0.0148958406974634525
n=017 R_3n=33.3751865107595882 T_3n=28.9244410135157347 deficit_lhs_minus_rhs=-0.010409465933444381
n=120 R_3n=1811.8161265178825 T_3n=5.00622398710689367 deficit_lhs_minus_rhs=-0.0833732252659577474
raw_deficit_nonincreasing=REFUTED first_pair=(40, 41)
classification=NUMERICAL_DIAGNOSTIC_ONLY; checker is corroborative only; theorem sources are the two proof notes
```

The diagnostic block is from the post-review run with `--order-stop 200`.
The two exact commands separately passed `62,594` gates through `n=250`; the
production comparison and AST audit were also repeated after the correction.

### Exact production-comparison command

```powershell
$env:PYTHONPATH='src'
@'
import importlib.util
from pathlib import Path

path = Path('ops/TASK-20260804__radius3_seam_onset/check_seam.py')
spec = importlib.util.spec_from_file_location('radius3_check', path)
if spec is None or spec.loader is None:
    raise RuntimeError('could not load task-local checker')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
from ringmin.patterns import interleave, supnick_max_tour

cases = 0
for n in range(5, 201):
    values = tuple(range(3, n + 1))
    local = check.shifted_supnick_tour(n)
    published = tuple(supnick_max_tour(values))
    production_style = tuple(interleave(values))
    if local != published:
        raise RuntimeError(f'supnick_max_tour mismatch at n={n}')
    if not check.cycle_equivalent(local, production_style):
        raise RuntimeError(f'interleave mismatch at n={n}')
    cases += 2
print(f'production_shifted_supnick_equivalence=PASS n=5..200 comparisons={cases}')
'@ | python -B -
```

Output:

```text
production_shifted_supnick_equivalence=PASS n=5..200 comparisons=392
```

### Exact AST-audit result

The executed read-only AST script parsed the task-local checker, counted
`ast.Assert` nodes, collected `Import` and `ImportFrom` modules, and rejected
`ringmin` or `ringmin.*`. It returned:

```text
ast_assert_nodes 0
ringmin_import_nodes 0
top_level_mpmath_import_nodes 0
all_mpmath_import_nodes 1
```

## Artifact and provenance checks

- Artifact generation: not applicable.
- No optimum, frontier, progress log, certificate, heuristic result artifact,
  publication asset, or global verifier is changed or required.
- The task-local script is a corroborative checker, not a certificate for the
  exact all-`n` theorem and not a global Ringmin verifier.

## Failed checks and negative evidence

- An initial combined read included `git rev-parse` in the sandbox and hit
  Git's dubious-ownership guard. It changed no state; clean status was checked
  with the permitted command and HEAD was read from the Git ref file.
- An initial parallel exact-check invocation was surfaced as failed because
  `rg` correctly returned exit `1` when it found no `assert`. Separate checker
  runs passed, and the later AST audit emitted an explicit zero-count PASS.
- The first checker review found two issues: wording that made the checker
  sound constitutive of the proof, and a raw-deficit loop outside its intended
  high-precision context. Both were corrected; targeted normal/optimized
  reruns and re-review passed with no remaining actionable issue.
- A later independent proof audit found that the sentence `asin(s)>s for
  every s>0` omitted the real-domain restriction. The proof already used only
  `0<s_e<1`; the note now states that domain explicitly and the checker gate
  checks it. This was a wording/domain-guard correction, not a failed endpoint
  inequality.
- The raw radius-3 deficit is not nonincreasing. The finite diagnostic finds
  its first increase at `(40,41)`, so the proof correctly uses monotonicity of
  `R_{3,n}-T_{3,n}` instead.
- Deleting `17` from `sigma*_{3,17}` does not yield a cycle dihedrally
  equivalent to `sigma*_{3,16}`. The imported root-growth theorem correctly
  avoids assuming that canonical tours are preserved by deletion.
- The first final `git diff --check` returned exit `1` because
  `CURRENT_STATUS.md` had a new blank line at EOF. A direct audit found the
  same harmless formatting issue in the untracked proof note. Both blank
  lines were removed; the final diff and direct audits pass.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three authorized tracked
  modifications and five authorized untracked additions:

  ```text
   M CURRENT_STATUS.md
   M PROJECT_KNOWLEDGE.md
   M research/NEXT_RESEARCH_STEPS.md
  ?? ops/TASK-20260804__radius3_seam_onset/EVIDENCE.md
  ?? ops/TASK-20260804__radius3_seam_onset/TASK_LOG.md
  ?? ops/TASK-20260804__radius3_seam_onset/TASK_STATUS.md
  ?? ops/TASK-20260804__radius3_seam_onset/check_seam.py
  ?? research/RADIUS3_SEAM_ONSET.md
  ```

- Complete tracked diff: read in full after substantive edits.
- Untracked additions: all five read in full after substantive edits.
- Direct strict-UTF-8, no-BOM, LF-only, exactly-one-final-LF, and
  trailing-whitespace check: `PASS files=8`.
- Final `git diff --check`: exit `0`, no output.
- Explicit protected-path status: exit `0`, no output.
- An ignored task-local `__pycache__` created by the production integration
  command was inspected and removed; it was regenerable and contained no
  project data.
- Protected paths unexpectedly changed: none.
- Generated files unexpectedly changed: none.

## Residual uncertainty

- Independent human review and manual commit remain pending.
- The theorem is confined to one formal seam and does not prove full
  realizability, global optimality, or floating-circle behavior.
- Finite numerical diagnostics are not the all-`n` proof.
- Hosted CI and global certificate-frontier verification are out of scope and
  are not claimed inspected.
