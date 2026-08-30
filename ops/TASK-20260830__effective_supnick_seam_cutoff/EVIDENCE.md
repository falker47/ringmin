# Evidence

## Environment

```text
repository_head=3ad9835631b2a4d434972eedfe10cd8924a05d39
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=pyproject.toml; checker uses standard library only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `20/9<rho<41/16` | exact inequality | signed rational bounds for `alpha,pi` and task checker | yes, closure reviewer | uses the analytic identities proved in the proof note |
| closure root brackets at `c=5,6` for every `k>=4325` | exact theorem | existing error (17), symbolic error monotonicity, exact margins | yes, closure reviewer | formal Supnick chain only |
| threshold brackets at `c=5,6` for every `k>=4325` | exact theorem | positive `H/Q`, error (28), exact reciprocal margins | yes, threshold reviewer | imports threshold derivation from the same proof note |
| `s_k=4k+6` for every integer `k>=4325` | exact theorem | endpoint brackets plus imported sign/persistence theorem | three read-only reviews | no minimal-cutoff, full-feasibility, `R*(n)`, or floating claim |
| checker is stdlib/`Fraction`-only and scan-free over `k,n` | engineering fact | normal/optimized runs, AST/import audit, 15 mutation rejections | yes, engineering reviewer rerun | checker is corroborative, not a proof assistant |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | exit `0`; no paths at startup | clean initial tree | mathematical correctness |
| `python --version` | exit `0`; `Python 3.14.3` | active interpreter | proof correctness |
| scoped `git rev-parse HEAD` | exit `0`; task-base hash recorded | exact base revision | working-tree correctness after edits |
| independent `Fraction` scratch evaluation | exit `0`; all displayed margins positive | arithmetic orientation before file updates | checker source integrity |
| three independent read-only audits | all `PASS`; no mathematical defect | closure/`rho`, threshold/inversion, and adversarial checker design | hosted CI or formal mechanization |
| `python -B .../check_effective_cutoff.py --self-test-mutations` | exit `0`; `156` core gates, `15/15` mutations rejected | exact rational proof gates and changed-constant rejection | production-independent | analytic lemmas and imported theorem remain proof dependencies |
| `python -B -O -S .../check_effective_cutoff.py --self-test-mutations` | exit `0`; identical `156`/`15` output | optimization-safe and no-site stdlib execution | hosted environments |
| AST/source audit | exit `0`; zero `assert`, float, disallowed import, or parameter-range nodes | source discipline and scan/dependency separation | mathematical proof by itself |
| optimized/no-site import audit | exit `0`; zero output/error/gates | absence of import side effects | execution of the audit entry point |
| three independent post-file reviews | all final `PASS` after five checker repairs | actual proof/checker fractions, directions, quantifiers, coverage, and scope | formal proof assistant or hosted CI |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; final `12 passed in 27.39s` | repository regression suite | the new theorem or certificate frontiers |
| direct eight-file format audit | exit `0`; UTF-8/no BOM, LF-only, one final LF, no NUL/trailing whitespace | tracked and untracked text integrity | mathematical correctness |
| scoped `git diff --check` | exit `0`; no output | whitespace errors in tracked diff | untracked files, checked directly |
| protected-path and task-tree audit | exit `0`; no protected paths; exactly four task files | scope containment and no generated cache | hosted state |

## Artifact and provenance checks

- artifact path: not applicable; no result or certificate artifact changes;
- generating source/command: not applicable;
- input/version: `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` and imported
  `research/FIXED_K_SUPNICK_SEAM.md` at task-base `HEAD`;
- generation commit: not applicable;
- schema/hash: checker SHA-256
  `B43FB0EED080CC4E8DED641CF572EA6C1EB4EE45E34242B23073FE43C6163160`;
- independent verifier: task-local exact checker plus three independent
  read-only derivations;
- reproducibility limitation: the checker corroborates rational algebra and
  imports the analytic inequalities and fixed-`k` theorem as proved sources.

## Failed checks and negative evidence

- An unscoped read-only `git rev-parse HEAD` was rejected by Git's sandbox
  ownership check. A per-invocation `safe.directory` option returned the
  task-base hash; no Git configuration was changed.
- The coarse threshold estimate `<17/k` cannot close the `c=6` comparison at
  `K=4325`; the proof necessarily retains the exact `4193/(256k)` constant.
- The first normal and optimized/no-site mutation-audit invocations exited
  `1` after the `139` core gates passed, because the harness incorrectly
  required a mutation anchor to occur once rather than twice (definition plus
  mutation table). No mutation had run. The fingerprint was corrected to
  exactly two occurrences. The next two reruns exited `1` at the second
  mutation because the threshold numerator intentionally has two mutation
  variants and therefore three total occurrences. The final fingerprint is
  one live occurrence plus the number of table entries sharing the anchor;
  post-fix results are recorded separately.
- A later engineering review found that the passing checker still omitted
  explicit coverage for proof identity (60), threshold-tail monotonicity, and
  one rational arcsine square gate. It also found that mutation rejection was
  too broad (`Exception`) and did not directly test strict-zero rejection.
  The mathematical margins remained correct. All five coverage defects were
  fixed before durable-memory promotion; the fresh full reruns passed.
- The first two AST/import audit commands had PowerShell quoting syntax
  errors and exited `1` before reading the checker. The corrected import audit
  passed; the first corrected AST command then falsely treated imported alias
  names as module names and exited `1`. Its module-aware replacement passed
  and was rerun after the final checker edits.
- An unscoped `git diff --check` reported that the directory was not a Git
  repository under the sandbox ownership boundary. The per-invocation
  `safe.directory` rerun exited `0`; no Git configuration was changed.
- Final status/protected-path commands with the attempted read-only override
  `core.excludesFile=NUL` exited `1` because Git refuses `NUL` as an exclude
  file. Replacing it with the repository-local `.git/info/exclude` path made
  both commands exit `0`, with the expected eight paths and no protected
  path respectively.
- No finite scan over `k` or `n` has been run or used as evidence.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths, four tracked modifications plus four untracked dossier additions;
- complete `git diff` inspected: yes, all four tracked files in full;
- untracked additions inspected directly: yes, all four in full, with the
  checker read in four bounded chunks after final substantive edits;
- direct whitespace/encoding check: all eight paths passed strict UTF-8,
  no-BOM, LF-only, exactly-one-final-LF, no-NUL, and trailing-whitespace gates;
- scoped `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none under imported/prior notes and
  dossiers, `src/`, `tests/`, `scripts/`, `results/`, `verify.py`,
  `paper_assets/`, public summaries, or build/config paths;
- generated files unexpectedly changed: none; the new task directory has
  exactly four files and no subdirectory.

## Residual uncertainty

The checker corroborates rather than formally mechanizes the analytic
inequalities and imported fixed-`k` theorem. Hosted CI, certificate
frontiers, `verify.py`, and paper builds are unrelated and were not run. The
theorem intentionally does not claim that `4325` is minimal, classify the
finite unresolved range `8<=k<4325`, prove full feasibility, determine
`R*(n)`, or establish global floating-circle behavior.
