# Evidence

## Environment

```text
repository_head=5f9be1ab107ce6fba2eba586e9d30eb859c7d330
platform=Windows PowerShell
python=3.14.3
mpmath=1.3.0
dependency_source=existing project environment
task_mode=STRICT
```

Git read commands use a command-local `safe.directory` override because the
sandbox account does not own the checkout. This does not write Git
configuration or repository state.

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Radius `2` has shifted-Supnick neighbors `n` and `n-1` | exact theorem | shifted rank construction and parity edge formulas in the proof note | three read-only reviews; finite production comparison through `n=200` | relies on the published Supnick fixed-tour theorem for chain minimality |
| `R_{2,n+1}>R_{2,n}` | exact theorem | delete-largest fixed-`R` minimum-cost comparison | three independent proof reviews | concerns chain roots, not `R*(n)` |
| The positive radius-2 threshold exists exactly for `n>=9` and `T_{2,n}` strictly decreases | exact theorem | Descartes formula, exact `n=8,9` domain split, fixed-`x` comparison | three proof reviews; exact `Fraction` endpoint checks | concerns only the `(n,2,n-1)` seam |
| `Delta_{2,n}>0` for `4<=n<=12` and `<0` for every `n>=13` | exact theorem, post-arXiv-v1 | opposing monotonicities and rational bridges `R_{2,12}<17<T_{2,12}`, `T_{2,13}<14<R_{2,13}` | proof reviewed three ways; all rational checks active under `python -O` | no implication for global optima or floating behavior |
| The raw radius-2 seam deficit is not monotone | numerical observation | 100-digit values at `n=29,30` | production-independent checker, stable against 60 digits | finite observation used only to exclude a proof route |
| Proof/checker conventions agree with both production Supnick helpers through `n=200` | local engineering verification | targeted integration command | independent and production constructors compared | finite integration check, not Supnick's theorem |
| Existing regression suite still passes | local engineering verification | `python -m pytest` | production tests include separate SLSQP checks | not a global certificate or hosted CI |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python ops/TASK-20260804__radius2_seam_threshold/check_seam.py --start 4 --stop 200 --digits 60 --stability-digits 100` | exit `0`; all exact/order/sign/stability checks pass | displayed rational proof bridges, shifted formulas, broad finite signs, precision stability | the all-`n` theorem or production solver |
| `python -O ops/TASK-20260804__radius2_seam_threshold/check_seam.py --start 4 --stop 30 --digits 40 --stability-digits 60` | exit `0`; all checks pass | exact gates cannot disappear in optimized Python | values beyond the selected finite range |
| targeted proof-constructor/`supnick_max_tour`/`interleave` comparison | exit `0`; `production_shifted_supnick_equivalence=PASS n=4..200` | shifted convention and integration | fixed-`R` optimality theorem |
| `python -m pytest` | exit `0`; `12 passed in 28.36s` | current production regression suite | independent all-`n` proof, certificate frontier, hosted CI |
| three read-only adversarial reviews of the actual note/checker | no actionable issue | parity, threshold algebra/domain, arithmetic, checker, scope | independent human review after handoff |

### Full checker material output

```text
independent_of_production=PASS (no ringmin imports)
exact_rational_domain_and_bridges_n8_n9_n12_n13=PASS
shifted_order_convention_edge_sets=PASS n=4..200
diagnostic_sign_scan=PASS n=4..200 digits=100
precision_stability=PASS digits=60/100 max_relative_R_delta=4.1752866e-46 max_absolute_deficit_delta=1.4682707e-46
n=004 R_2n=0.433260882561464321 T_2n=NA deficit_lhs_minus_rhs=1.91194046983464796
n=008 R_2n=5.72699779376383304 T_2n=NA deficit_lhs_minus_rhs=0.367847400326976598
n=009 R_2n=7.72140803937930436 T_2n=103.86422859204304 deficit_lhs_minus_rhs=0.235903030513651784
n=012 R_2n=15.2588704304484934 T_2n=17.0111511689019437 deficit_lhs_minus_rhs=0.0122280835946630972
n=013 R_2n=18.2775435001740572 T_2n=13.9066575717018489 deficit_lhs_minus_rhs=-0.0300467054585452879
n=029 R_2n=100.967133368505975 T_2n=5.29133616530599343 deficit_lhs_minus_rhs=-0.18210378851879555
n=030 R_2n=108.275574297185619 T_2n=5.17214762946877428 deficit_lhs_minus_rhs=-0.182099652502621371
n=200 R_2n=4989.19887208983961 T_2n=2.71686140600357998 deficit_lhs_minus_rhs=-0.061216035299553456
raw_deficit_nonincreasing=REFUTED first_pair=(29, 30)
classification=FINITE_DIAGNOSTIC_ONLY; all-n proof is the proof note
```

## Artifact and provenance checks

- Artifact generation: not applicable.
- No optimum, frontier, progress log, certificate, heuristic table,
  publication asset, or verifier is in scope.
- The task-local checker is diagnostic and is not described as a global
  finite certificate or an all-`n` proof.

## Failed checks and negative evidence

- Raw `git rev-parse HEAD` failed the sandbox ownership check; command-local
  `safe.directory` permitted the read-only inspection without changing state.
- One read-only reviewer accidentally used `supnick_min_tour`, obtaining
  plausible but wrong radii. The mismatch was investigated; the values and
  associated scan were discarded, and the reviewer reproduced the correct
  `supnick_max_tour` results. This did not affect the order-independent
  Descartes algebra.
- Direct monotonic decrease of the raw deficit is false at `n=29,30`.
- Deleting the largest vertex does not need to preserve the canonical shifted
  Supnick representative; only the induced-cycle cost comparison is used.
- No mathematical, exact-arithmetic, high-precision, integration, or unit
  test gate failed after the wrong-helper diagnostic was corrected.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three authorized tracked
  modifications and five authorized untracked additions:

  ```text
   M CURRENT_STATUS.md
   M PROJECT_KNOWLEDGE.md
   M research/NEXT_RESEARCH_STEPS.md
  ?? ops/TASK-20260804__radius2_seam_threshold/EVIDENCE.md
  ?? ops/TASK-20260804__radius2_seam_threshold/TASK_LOG.md
  ?? ops/TASK-20260804__radius2_seam_threshold/TASK_STATUS.md
  ?? ops/TASK-20260804__radius2_seam_threshold/check_seam.py
  ?? research/RADIUS2_SEAM_THRESHOLD.md
  ```

- Complete tracked diff: read in full.
- Untracked additions: all five read in full after the substantive edits.
- Direct strict-UTF-8, no-BOM, final-LF, and trailing-whitespace check:
  `UTF8_FINAL_LF_TRAILING_WS=PASS files=8`.
- `git diff --check`: exit `0`, no output. It covers tracked changes; the
  direct check covers untracked additions.
- Protected-path diff and status over `paper_assets`, `src`, `tests`,
  `scripts`, `results`, `verify.py`, README/report, CI, dependencies, and
  publication metadata: exit `0`, no changed path. Git emitted warnings that
  the sandbox could not read the user's global ignore file; this did not
  alter the repository or suppress any tracked diff.
- Protected paths unexpectedly changed: none.
- Generated files unexpectedly changed: none.

## Residual uncertainty

- Independent human review and manual commit remain pending.
- The theorem is post-arXiv-v1 work; the protected historical paper was not
  revised.
- The checker scan is finite and diagnostic. The all-`n` status rests on the
  exact proof, not on the scan through `n=200`.
- No claim is made about `R*(n)`, existence or universality of a floating
  radius-2 circle, later cascade levels, hosted CI, or certificate frontiers.
