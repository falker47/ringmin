# Evidence

## Environment

```text
repository_head=e23663ea4c831ccfd50380063894b5d8574cabd7
platform=Windows PowerShell
python=3.14.3
mpmath=1.3.0
dependency_source=existing project environment
task_mode=STRICT
```

Git read commands use a command-local `safe.directory` override when needed
because the sandbox account does not own the checkout. This does not write Git
configuration or repository state.

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| The shifted Supnick order has seam neighbors `n-1,n` | exact theorem | rank construction and parity formulas in the proof note | three read-only derivations; task-local dual-constructor checks | relies on the published Supnick theorem for fixed-`R` chain minimality |
| `R_{k,n}` exists uniquely, strictly increases, and tends to infinity | exact theorem | implicit-root argument, vertex deletion, explicit cosecant lower bound | three independent proof audits | concerns chain roots, not `R*(n)` |
| The positive Descartes threshold exists exactly for `n>=4k+1` and has the displayed `kappa_{k,n}` | exact theorem | exact boundary comparison, physical branch substitution, rationalization | three proof audits; task-local `Fraction` gates | concerns only seam `(n,k,n-1)` |
| Negative deficits form a nonempty terminal tail and equality occurs at most once | exact theorem | strict growth of `R-T` and divergence | three proof audits | does not identify `s_k` for `k>=3` |
| Existing onsets `s_1=8`, `s_2=13` follow as corollaries | exact proved corollary | general theorem plus exact bridges in the existing notes | existing independent task evidence plus current audits | endpoint arithmetic remains in the existing notes |
| Checker scan agrees over selected finite cases | numerical diagnostic | task-local independent scan at two precisions | production-independent | not an all-`k` proof or exact onset classification |
| Task-local convention agrees with production helpers | local engineering verification | 1,580-case targeted comparison | independent and production constructors compared | finite integration check, not Supnick's theorem |
| Existing regression suite still passes | local engineering verification | `python -m pytest` | production tests include separate geometric checks | not a global certificate or hosted CI |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python ops/TASK-20260804__fixed_k_supnick_seam/check_seam.py --max-k 3 --extra 8 --digits 40 --stability-digits 60` | exit `0`; all gates passed | initial exact algebra/order and finite numerical diagnostics | the all-`k` theorem or exact `k>=3` onset |
| `python ops/TASK-20260804__fixed_k_supnick_seam/check_seam.py --max-k 12 --extra 40 --digits 60 --stability-digits 100` | exit `0`; all exact/order/sign/monotonicity/stability checks pass | broad finite audit of displayed formulas and numerical implications | the all-`k` proof or exact `k>=3` onset |
| `python -O ops/TASK-20260804__fixed_k_supnick_seam/check_seam.py --max-k 4 --extra 12 --digits 40 --stability-digits 60` | exit `0`; all gates pass | checks that exact gates survive optimized mode | values beyond the selected finite range |
| targeted task-local/`supnick_max_tour`/`interleave` comparison | exit `0`; `production_shifted_supnick_equivalence=PASS ... cases=1580` | shifted convention and production integration | fixed-`R` optimality theorem |
| `python -m pytest` | exit `0`; `12 passed in 34.50s` | current production regression suite | independent all-`k` proof, certificate frontier, hosted CI |
| three read-only adversarial reviews of the actual note/checker | no actionable issue | parity, algebra/domain, inequalities, quantifiers, checker, scope | independent human review after handoff |

### Full checker material output

```text
independent_of_production=PASS (no ringmin imports)
exact_algebra_and_domain=PASS k=1..12
shifted_order_conventions_and_edges=PASS k=1..12 through n=4k+1+40
diagnostic_root_threshold_deficit_scan=PASS digits=60/100
precision_stability=PASS max_relative_R_delta=4.9972035e-47 max_absolute_deficit_delta=2.5066708e-47 max_direct_stable_kappa_delta=1.4287342e-101
k=001 physical_domain_start=5 first_negative_observed_in_finite_scan=8
k=002 physical_domain_start=9 first_negative_observed_in_finite_scan=13
k=003 physical_domain_start=13 first_negative_observed_in_finite_scan=17
k=004 physical_domain_start=17 first_negative_observed_in_finite_scan=21
k=005 physical_domain_start=21 first_negative_observed_in_finite_scan=25
k=006 physical_domain_start=25 first_negative_observed_in_finite_scan=30
k=007 physical_domain_start=29 first_negative_observed_in_finite_scan=34
k=008 physical_domain_start=33 first_negative_observed_in_finite_scan=38
k=009 physical_domain_start=37 first_negative_observed_in_finite_scan=42
k=010 physical_domain_start=41 first_negative_observed_in_finite_scan=46
k=011 physical_domain_start=45 first_negative_observed_in_finite_scan=50
k=012 physical_domain_start=49 first_negative_observed_in_finite_scan=54
near_zero_equality_or_inconclusive=NONE
classification=FINITE_DIAGNOSTIC_ONLY; no exact onset for k>=3 is inferred
```

The observed first-negative indices for `k>=3` are numerical diagnostics
only. They are not used in the proof or promoted to exact onset claims.

## Artifact and provenance checks

- Artifact generation: not applicable.
- No optimum, frontier, progress log, certificate, heuristic table,
  publication asset, or verifier is in scope.
- The task-local checker is diagnostic and is not described as a global
  finite certificate or an all-`k` proof.

## Failed checks and negative evidence

- A raw combined Git read encountered the sandbox dubious-ownership guard;
  command-local `safe.directory` permits read-only inspection without state
  changes.
- Direct monotonicity of the raw angular deficit is not assumed and is known
  false already for the existing `k=1,2` sequences.
- The algebraic plus root is extraneous; its unsquared right-hand side is
  negative.
- No exact `k=3` endpoint bridge has been attempted. Finite checker output is
  retained only as diagnostic evidence.
- The first direct trailing-whitespace command used the PowerShell regex
  `[ `t]+$` in a single-quoted string, where the terminal `t` was interpreted
  as a literal match. It falsely flagged a heading ending in `t`. The command
  changed no file; the corrected regex `[ \t]+$` passed all eight paths.
- No mathematical, exact-algebra, high-precision, production-comparison, unit
  test, or review gate failed.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly three authorized tracked
  modifications and five authorized untracked additions:

  ```text
   M CURRENT_STATUS.md
   M PROJECT_KNOWLEDGE.md
   M research/NEXT_RESEARCH_STEPS.md
  ?? ops/TASK-20260804__fixed_k_supnick_seam/EVIDENCE.md
  ?? ops/TASK-20260804__fixed_k_supnick_seam/TASK_LOG.md
  ?? ops/TASK-20260804__fixed_k_supnick_seam/TASK_STATUS.md
  ?? ops/TASK-20260804__fixed_k_supnick_seam/check_seam.py
  ?? research/FIXED_K_SUPNICK_SEAM.md
  ```

- Complete tracked diff: read in full after substantive edits.
- Untracked additions: all five read in full after substantive edits.
- Direct strict-UTF-8, no-BOM, final-LF, and trailing-whitespace check:
  `UTF8_NO_BOM_FINAL_LF_TRAILING_WS=PASS files=8`.
- `git diff --check`: exit `0`, no output. It covers tracked changes; the
  direct check covers untracked additions.
- Explicit protected-path status: exit `0`, no changed path. Git emitted
  warnings that the sandbox could not read the user's global ignore file;
  this did not alter the repository or suppress any tracked diff.
- Protected paths unexpectedly changed: none.
- Generated files unexpectedly changed: none.

## Residual uncertainty

- Independent human review and manual commit remain pending.
- The all-`k` status rests on the exact proof, not on the finite checker scan.
- No exact onset for `k>=3`, no global optimum, and no floating-circle claim
  is made.
