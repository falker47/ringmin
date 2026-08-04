# Evidence

## Environment

```text
repository_head=14fd8f612893af5b6961cd4f607ab2e1b5eb3fe4
platform=Windows PowerShell
python=3.14.3
mpmath=1.3.0
dependency_source=existing project environment
task_mode=STRICT
```

Git read commands use a command-local `safe.directory` override because the sandbox account does not own the checkout. This does not write Git configuration or repository state.

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Radius `1` has Supnick neighbors `n` and `n-1` | exact theorem | parity-independent representative and parity edge formulas in the proof note | two read-only reviews plus comparison with production helpers through `n=200` | relies on the published Supnick fixed-tour theorem for chain minimality |
| `R_{n+1}>R_n` | exact theorem | delete-largest induced-tour comparison and strict fixed-`R` angle monotonicity | two independent proof reviews | concerns chain roots, not `R*(n)` |
| The explicit unit-pocket threshold `T_n` decreases on its positive domain | exact theorem | Descartes formula and positive derivative of its reciprocal | two independent proof reviews; exact `Fraction` base checks | concerns the `(n,1,n-1)` seam only |
| The seam inequality is reversed for `3<=n<=7` and holds for every `n>=8` | exact theorem, post-arXiv-v1 | opposing monotonicities plus exact rational bridges `R_7<6<T_7` and `T_8<51/10<R_8` | proof reviewed twice; exact bridge code remains active under `python -O` | no implication for global optima or universal floating behavior |
| The raw seam deficit is not monotone | numerical observation | 100-digit diagnostic values `Delta_19=-0.291721956355169441...`, `Delta_20=-0.291070673718319608...` | production-independent checker, stable against 60 digits | finite observation; used only to exclude a proof route |
| Checker and production Supnick conventions agree through `n=200` | local engineering verification | targeted comparison command | separate implementations compared | finite integration check, not proof of Supnick's theorem |
| Existing regression suite still passes | local engineering verification | `python -m pytest` | includes production tests and separate SLSQP checks | not a global certificate and not hosted CI |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python ops/TASK-20260804__radius1_seam_obstruction/check_seam.py --start 3 --stop 200 --digits 60 --stability-digits 100` | exit `0`; all exact/order/sign/stability checks pass | rational proof bridges, local order formulas, a broad finite sign scan, precision stability | the all-`n` theorem or production solver behavior |
| `python -O ops/TASK-20260804__radius1_seam_obstruction/check_seam.py --start 3 --stop 20 --digits 40 --stability-digits 60` | exit `0`; all checks pass | exact checks cannot disappear under optimized Python | values beyond the selected finite range |
| checker with `--start 3 --stop 10 --digits 40 --stability-digits 60` | exit `0`; reports `NOT_OBSERVED_IN_SELECTED_RANGE` | truthful negative-evidence labeling on a range without the `19,20` counterexample | nonmonotonicity outside that range |
| targeted proof-constructor/`supnick_max_tour`/`interleave` comparison | exit `0`; `production_supnick_equivalence=PASS n=3..200` | convention and cyclic-equivalence integration | fixed-`R` optimality theorem |
| `python -m pytest` | exit `0`; `12 passed in 29.89s` | current production regression suite | independent all-`n` proof, certificate frontier, hosted CI |

### Full checker material output

```text
independent_of_production=PASS (no ringmin imports)
exact_rational_bridges_n7_n8=PASS
order_convention_edge_sets=PASS n=3..200
diagnostic_sign_scan=PASS n=3..200 digits=100
precision_stability=PASS digits=60/100 max_relative_R_delta=4.6113363e-46 max_absolute_deficit_delta=7.9028869e-47
n=003 R_n=0.260869565217391304 T_n=NA deficit_lhs_minus_rhs=1.78442219577361451
n=007 R_n=4.15318955374381247 T_n=6.45897733982317934 deficit_lhs_minus_rhs=0.0943009583599419013
n=008 R_n=5.75603108614249173 T_n=5.02987303949859402 deficit_lhs_minus_rhs=-0.0271152588797906245
n=019 R_n=39.9695330808021121 T_n=2.26490066225165563 deficit_lhs_minus_rhs=-0.291721956355169441
n=020 R_n=44.579056085341043 T_n=2.20387669020946525 deficit_lhs_minus_rhs=-0.291070673718319608
n=200 R_n=4948.3582104704094 T_n=1.23529498246926924 deficit_lhs_minus_rhs=-0.0663342001558354962
raw_deficit_nonincreasing=REFUTED first_pair=(19, 20)
classification=FINITE_DIAGNOSTIC_ONLY; all-n proof is the proof note
```

## Artifact and provenance checks

- Artifact generation: not applicable.
- No optimum, frontier, progress log, certificate, heuristic table, publication asset, or verifier is in scope.
- The task-local checker will be diagnostic and will not be described as a global finite certificate or an all-`n` proof.

## Failed checks and negative evidence

- Raw Git reads failed the sandbox ownership check once; command-local `safe.directory` fixed read-only inspection without changing repository state.
- Direct monotonicity of the raw angular deficit is false at `n=19,20`.
- Deleting the largest vertex does not preserve the canonical Supnick order; only the induced-tour cost comparison is used.
- Adversarial review found and prompted fixes for one finite-range output label, one notation collision, optimized-mode bare assertions, and two proof-domain justifications. All were corrected and rerun.
- No mathematical, exact-arithmetic, high-precision, integration, or unit-test gate failed after those corrections.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three authorized tracked modifications and five authorized untracked additions:

  ```text
   M CURRENT_STATUS.md
   M PROJECT_KNOWLEDGE.md
   M research/NEXT_RESEARCH_STEPS.md
  ?? ops/TASK-20260804__radius1_seam_obstruction/EVIDENCE.md
  ?? ops/TASK-20260804__radius1_seam_obstruction/TASK_LOG.md
  ?? ops/TASK-20260804__radius1_seam_obstruction/TASK_STATUS.md
  ?? ops/TASK-20260804__radius1_seam_obstruction/check_seam.py
  ?? research/RADIUS1_SEAM_OBSTRUCTION.md
  ```

- Complete tracked diff: read in full.
- Untracked additions: all five read in full after the last substantive edits.
- Direct UTF-8 decoding, final-LF, and trailing-whitespace check: `PASS files=8`.
- `git diff --check`: exit `0`, no output. It covers tracked changes; the direct check covers the untracked additions.
- Protected-path diff over `paper_assets`, `src`, `tests`, `scripts`, `results`, `verify.py`, README/report, CI, dependencies, and publication metadata: exit `0`, no output.
- Protected paths unexpectedly changed: none.
- Generated files unexpectedly changed: none.

## Residual uncertainty

- Independent human review and manual commit remain pending.
- The theorem is post-arXiv-v1 work; the protected historical paper was not revised.
- The checker scan is finite and diagnostic. The all-`n` status rests on the exact proof, not on the scan through `n=200`.
- No claim is made about `R*(n)`, existence or universality of a floating circle, later cascade levels, hosted CI, or certificate frontiers.
- Hosted CI was not inspected and is not claimed green; local checks are recorded separately.
