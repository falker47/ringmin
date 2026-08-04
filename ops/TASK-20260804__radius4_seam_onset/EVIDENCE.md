# Evidence

## Environment

```text
repository_head=b49d0fa604eab7aa6b7d64dbfa27d85e3785a2f6
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `50<T_{4,20}` and `T_{4,21}<50` | exact theorem (endpoint lemma) | positive pre-square gates and exact rational square margins in `research/RADIUS4_SEAM_ONSET.md` | independently recomputed twice; checker `Fraction` audit | concerns only the Descartes threshold of the formal seam |
| `R_{4,20}<50<R_{4,21}` | exact theorem (endpoint lemma) | complete `17`- and `18`-edge rational tables, strict arcsine bounds, and exact bounds for `pi` | all 35 rows/totals independently regenerated; checker `Fraction` audit | concerns adjacent-chain roots only |
| `Delta_{4,n}>0` for `6<=n<=20` and `<0` for every `n>=21`; hence `s_4=21` | exact theorem, post-arXiv-v1 | the two endpoint lemmas plus the existing fixed-`k` threshold/sign/monotonicity theorem | independent endpoint audits, adversarial proof/checker reviews, and exact checker corroboration | formal seam `(n,4,n-1)` only; no full/global/floating claim |
| High-precision endpoint/root/deficit values | numerical observation | opt-in mpmath scan at 60/100 digits | precision comparison and independent agent reruns | diagnostic only; no finite scan proves the all-`n` claim |
| Checker has no production dependency on its exact path | engineering fact | AST/import audit, `python -S`, and separate production-convention comparison | yes | checker corroborates the endpoint note; it does not replace the imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short` | exit `0`; no paths; sandbox ignore-file warnings only | clean startup tree | mathematical correctness |
| `python -B ops/TASK-20260804__radius4_seam_onset/check_seam.py --order-stop 250` | exit `0`; `184478` explicit gates; diagnostics skipped | complete exact `Fraction` transcription, margins, edge tables, parity formulas, and endpoint bridges | proof of the imported fixed-`k` theorem or either standard geometric/integral fact about `pi` |
| `python -B -O -S ops/TASK-20260804__radius4_seam_onset/check_seam.py --order-stop 250` | exit `0`; same `184478` gates/output | optimization-safe explicit gates and no default dependency on site packages/mpmath | numerical diagnostics |
| checker with `--diagnostics --start 6 --stop 120 --digits 60 --stability-digits 100` | exit `0`; `NUMERICAL_DIAGNOSTIC_ONLY`; max relative root delta `9.5663122e-48`, max absolute deficit delta `4.5796177e-49` | finite convention/sign/domain/monotonicity and precision diagnostics | exact endpoint proof or all-`n` certification |
| external task-local/production convention comparison, `n=6..250` | exit `0`; `490` comparisons | equivalence with production `supnick_max_tour` and `interleave` while checker retains no production import | mathematical optimality of Supnick's theorem |
| AST audit | exit `0`; zero `ast.Assert`, float literals, and `ringmin` imports | gate persistence, exact-source literals, and production independence | dynamic behavior by itself |
| in-memory first-row margin mutation | exit `0`; intended `AuditFailure` caught | corrupted table margin is rejected | every possible tamper |
| `python -m pytest -p no:cacheprovider` with bytecode disabled | exit `0`; `12 passed in 30.40s` | repository regression suite | global frontier certification or the new all-`n` proof |
| two adversarial read-only reviews | `PASS`; all 35 rows, totals, threshold margins, pi/arcsine steps, quantifiers, and checker modes rechecked | independent proof/checker scrutiny | hosted CI |

## Artifact and provenance checks

- artifact path: not applicable; no certificate or generated publication
  artifact is in scope;
- generating source/command: not applicable;
- input/version: `research/FIXED_K_SUPNICK_SEAM.md` at repository `HEAD`;
- generation commit: not applicable;
- schema/hash: not applicable;
- independent verifier: task-local stdlib-only exact checker implemented and
  rerun in normal and optimized/no-site modes;
- reproducibility limitation: the checker corroborates the new endpoint
  arithmetic but intentionally imports neither production code nor a proof of
  the fixed-`k` theorem; mpmath is needed only for opt-in diagnostics.

## Failed checks and negative evidence

- Initial plain `git status --short` was rejected by Git's dubious-ownership
  guard for the sandbox account. Read-only Git checks therefore use a
  command-local `-c safe.directory=...`; no Git configuration was changed.
- `NUMERICAL_DIAGNOSTIC_ONLY`: initial binary64 scratch selection showed
  `sum asin(s_e)≈3.01764856` at `n=20`, refuting reuse of the radius-3
  `sum<3<pi` bridge. It selected candidate rational grids but supplied no
  proof premise; every retained row was later recomputed with `Fraction`.
- One adversarial checker review noted that the lower table's sign gate used
  `0<q^2` instead of spelling out `0<q`. All stored values were positive and
  no result was wrong; the gate was tightened to `0<q` and both exact modes
  were rerun successfully.
- Final handoff review noted that the note displayed the independent
  `151/11025` positivity margin at `n=21` but the checker did not yet
  recompute it separately. The stronger separator gate already proved
  positivity, so no theorem changed; the explicit `Fraction` gate was added
  and all checker modes were rerun.
- No counterexample to the proposed endpoint classification was found.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths (`CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, the roadmap, the new
  proof note, and four task-local dossier/checker files);
- complete `git diff` inspected: yes, all three tracked modifications read in
  full;
- untracked additions inspected directly or with a no-index diff: yes, all
  five additions read in full after substantive edits;
- direct whitespace check for untracked additions: passed together with all
  tracked paths under a strict byte/text audit;
- `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none; explicit status emitted no
  paths;
- generated files unexpectedly changed: none; the task directory contains
  exactly its four intended files.

## Residual uncertainty

The exact theorem intentionally depends on
`research/FIXED_K_SUPNICK_SEAM.md`; the task-local checker does not reprove
that source. A positive formal seam deficit is not full feasibility, and a
negative one says nothing about a replacement chain or global optimum.
Finite floating scans remain diagnostic. Hosted CI, `verify.py`, certificate
frontiers, and paper builds are unrelated to this delta and were not run.
