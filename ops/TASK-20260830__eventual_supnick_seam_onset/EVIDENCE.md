# Evidence

## Environment

```text
repository_head=19f0123b437f160a174695bb2a9a71b1d301166f
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `R_{k,4k+c}/k^2->rho` for `c=5,6` | exact asymptotic theorem for adjacent-chain roots | both parity formulas, quantitative Riemann sums, uniform denominator/arcsine error, and two-point root bracket | independent chain derivation and post-file review | formal adjacent-chain root only; cutoff not effective |
| `T_{k,4k+c}/k^2->24/(2c-1)` for `c=5,6` | exact asymptotic theorem for formal seam thresholds | exact conjugate factorization, coefficient positivity, denominator and reciprocal bounds | independent threshold derivation, checker, and post-file review | Descartes threshold only |
| `24/11<rho<8/3` | exact theorem | circular-segment identity, signed geometric remainders, `pi<22/7`, `pi>3`, and positive rational margins | independently recomputed; exact checker corroboration | no decimal approximation or global radius claim |
| `s_k=4k+6` for every sufficiently large integer `k` | exact theorem, post-arXiv-v1 | the two separated endpoint limits plus imported fixed-`k` sign criterion and persistence | three adversarial reviews | existential cutoff only; formal seam only |
| Checker is stdlib/`Fraction`-only and scan-free over `k,n` | engineering fact | normal/optimized runs and AST audit | independent reviewer reruns | checker does not mechanize analytic convergence or imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| scoped `git status --short --untracked-files=all` | exit `0`; no paths | clean startup tree | mathematical correctness |
| `python --version` | exit `0`; `Python 3.14.3` | active interpreter | proof correctness or dependency completeness |
| `python -B ops/TASK-20260830__eventual_supnick_seam_onset/check_asymptotic_onset.py` | exit `0`; `68` explicit gates; `parameter_scans=NONE` | exact parity cases, endpoints, factorizations, coefficient signs, uniform rational constants, signed remainders, and `rho` margins | analytic convergence or imported theorem |
| `python -B -O -S ops/TASK-20260830__eventual_supnick_seam_onset/check_asymptotic_onset.py` | exit `0`; identical output and `68` gates | optimization-safe, no-site, stdlib-only execution | hosted environments |
| AST/source audit | exit `0`; zero `assert`, float, non-stdlib, or production-import nodes | source discipline and checker separation | mathematical proof by itself |
| three independent post-file reviews | all `PASS`; no actionable defect | chain analysis, threshold/rho algebra, final logic, scope, and checker | hosted CI or formal proof assistant |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 29.79s` | repository regression suite | the new theorem or certificate frontiers |
| direct eight-file format audit | exit `0`; strict UTF-8/no BOM, LF-only, one final LF, zero trailing whitespace | tracked and untracked text integrity | mathematical correctness |
| `git -c safe.directory=... diff --check` | exit `0`; no output | whitespace errors in the tracked diff | untracked additions, covered directly |
| protected-path status and task-directory audit | exit `0`; no protected paths; four files and zero subdirectories | scope containment and absence of generated cache | hosted state |

## Artifact and provenance checks

- artifact path: not applicable; no result or certificate artifact is in
  scope;
- generating source/command: not applicable;
- input/version: the two imported proof notes at task-base `HEAD`;
- generation commit: not applicable;
- schema/hash: not applicable;
- independent verifier: task-local exact checker plus three independent
  read-only derivations/reviews;
- reproducibility limitation: the checker corroborates new algebra and the
  two symbolic cases `c=5,6`; it does not mechanize the imported theorem,
  the Riemann-sum convergence, or the elementary calculus identities.

## Failed checks and negative evidence

- The first unscoped Git startup command was rejected by Git's sandbox
  ownership protection. A per-invocation `safe.directory` option allowed the
  read-only check; no Git configuration was changed.
- No finite parameter scan is admissible as proof and none has been run.
- A high-precision decimal evaluation was used privately only to orient the
  search for coarse rational margins. It is absent from the proof and
  checker, and no numerical value is evidence for the theorem.
- The first combined final-delta display was truncated after `14465` tokens.
  No completeness claim was based on it; the three tracked diffs and dossier
  files were then reread in complete bounded outputs, while the already
  reviewed proof and checker were unchanged.
- The first direct-format command had a Python quoting syntax error and exited
  `1` before reading a file. The corrected command initially found an extra
  final blank line in `CURRENT_STATUS.md`; after that fix it found the same
  packaging defect in the new proof note and checker. All three were removed,
  and the final eight-file audit exited `0` with zero errors.
- The first `git diff --check` accordingly exited `1` on the extra blank line
  in `CURRENT_STATUS.md`. The post-fix final command exited `0` with no
  output.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths, comprising three tracked modifications and five untracked additions;
- complete tracked `git diff` inspected: yes, all three modified files in
  full after substantive edits;
- untracked additions inspected directly: yes, all five read in full, with
  separate adversarial proof/checker reviews;
- direct whitespace/encoding check: all eight paths passed strict UTF-8,
  no-BOM, LF-only, exactly-one-final-LF, and trailing-whitespace gates;
- `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none under the two imported theorem
  notes, `src/`, `tests/`, `scripts/`, `results/`, `verify.py`,
  `paper_assets/`, public summaries, or build/config paths;
- generated files unexpectedly changed: none; the task directory contains
  exactly four intended files and zero subdirectories.

## Residual uncertainty

The theorem supplies no explicit cutoff and does not classify any specified
open `s_k` with `k>=8`. The checker is corroborative rather than a formal
proof assistant. Hosted CI, certificate frontiers, `verify.py`, and paper
builds are unrelated and were not run. No full-feasibility, global-optimum,
contact-graph, or floating-circle conclusion follows.
