# Evidence

## Environment

```text
repository_head=3c4ca3ba9c227d2f4a3bd46605ed36eaa145bf10
platform=Windows PowerShell sandbox
python=3.14.3
mpmath=1.3.0 (opt-in diagnostics only)
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `75<T_{5,24}` and `T_{5,25}<75` | exact theorem (endpoint lemma) | positive pre-square gates and exact rational square margins in `research/RADIUS5_SEAM_ONSET.md` | independently recomputed by two agents; checker `Fraction` audit | concerns only the Descartes threshold of the formal seam |
| `R_{5,24}<75<R_{5,25}` | exact theorem (endpoint lemma) | complete 20- and 21-edge rational tables, strict termwise arcsine bounds, and exact polynomial/integral bounds for `pi` | all 41 rows, totals, and `pi` identities independently regenerated; checker `Fraction` audit | concerns adjacent-chain roots only |
| `Delta_{5,n}>0` for `7<=n<=24` and `<0` for every `n>=25`; hence `s_5=25` | exact theorem, post-arXiv-v1 | the two endpoint lemmas plus the existing fixed-`k` threshold/sign/monotonicity theorem | three post-implementation adversarial reviews and exact checker corroboration | formal seam `(n,5,n-1)` only; no full/global/floating claim |
| High-precision endpoint/root/deficit values | numerical observation | opt-in mpmath scan at 60/100 digits | precision comparison and independent reviewer reruns | diagnostic only; no finite scan proves the all-`n` claim |
| Checker exact path is stdlib/`Fraction`-only and production-independent | engineering fact | `python -B -O -S`, AST/import audit, fresh-process review, and separate production-convention comparison | yes | checker corroborates endpoint arithmetic; it does not reprove the imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short` | exit `0`; no paths; sandbox ignore-file warnings only | clean startup tree | mathematical correctness |
| `python -B ops/TASK-20260804__radius5_seam_onset/check_seam.py --order-stop 250` | exit `0`; `183033` explicit gates; diagnostics skipped | exact `Fraction` transcription, sign/square margins, all table rows, parity formulas, rational totals, and polynomial identities | proof of the imported fixed-`k` theorem |
| `python -B -O -S ops/TASK-20260804__radius5_seam_onset/check_seam.py --order-stop 250` | exit `0`; same `183033` gates and output | optimization-safe explicit gates and stdlib-only default path | numerical diagnostics |
| checker with `--diagnostics --start 7 --stop 120 --digits 60 --stability-digits 100` | exit `0`; `NUMERICAL_DIAGNOSTIC_ONLY`; max relative root delta `4.739224e-46`, max absolute deficit delta `1.495911e-46` | finite convention/sign/domain/monotonicity and precision diagnostics | exact endpoint proof or all-`n` certification |
| external task-local/production convention comparison, `n=7..250` | exit `0`; `488` comparisons | equivalence with production `supnick_max_tour` and `interleave` while checker retains no production import | mathematical optimality of Supnick's theorem |
| AST audit | exit `0`; zero `ast.Assert`, float literals, and `ringmin` imports; only stdlib top-level imports | gate persistence, exact-source literals, and production independence | dynamic behavior by itself |
| in-memory wrong-upper-margin and exact-lower-equality mutations | exit `0`; both intended `AuditFailure` gates caught | corrupted margin and a non-strict `s=q=1/8` row are rejected | every possible tamper |
| `python -m pytest -p no:cacheprovider` with bytecode disabled | exit `0`; `12 passed in 29.45s` | repository regression suite | global frontier certification or the new all-`n` proof |
| three adversarial post-implementation reviews | `PASS`; threshold algebra, all 41 rows, totals, `pi` identities, quantifiers, and checker modes rechecked | independent proof/checker scrutiny | hosted CI |

## Artifact and provenance checks

- artifact path: not applicable; no certificate or generated publication
  artifact is in scope;
- generating source/command: not applicable;
- input/version: `research/FIXED_K_SUPNICK_SEAM.md` at repository `HEAD`;
- generation commit: not applicable;
- schema/hash: not applicable;
- independent verifier: task-local stdlib/`Fraction` exact checker implemented
  and rerun in normal and optimized/no-site modes;
- reproducibility limitation: the checker corroborates the new endpoint
  arithmetic but intentionally imports neither production code nor a proof of
  the fixed-`k` theorem; mpmath is needed only for opt-in diagnostics.

## Failed checks and negative evidence

- Initial plain `git status --short` was rejected by Git's dubious-ownership
  guard for the sandbox account. Read-only Git checks therefore use a
  command-local `-c safe.directory=...`; no Git configuration was changed.
- The `n=25` threshold separator is close: its exact positive square margin
  is only `1/360000`. This rules out decimal sign evidence; the proof and
  checker retain independent positivity gates and the exact margin.
- At edge `(5,25)`, `s=1/8` lies exactly on the naive `1/200` lower grid. A
  non-strict `q=1/8` mutation was rejected; the proof deliberately uses
  `q=3/25` with positive margin `49/40000`.
- A first `n=24` upper-table design on a `1/500` grid was mathematically valid
  but had aggregate gap only `46821/125000000` below `3`. Before finalizing,
  it was replaced by the independently proposed `1/1000` table with the
  larger exact gap `37352109/5000000000`; no theorem premise depended on the
  diagnostic selection process.
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
