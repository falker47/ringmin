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

## Post-review correction evidence — 2026-09-02

### External decision and bounded correction

The external review of commit
`1db59857413b66b36b14e03af9281a956951fd40` accepted the mathematical theorem
and checker but returned overall `REJECT`: the primary-open-problems section
of `PROJECT_KNOWLEDGE.md` still asked to make the already effective theorem
effective. The same review classified the duplicate resolved roadmap section
as nonblocking editorial redundancy.

The correction changes only durable documentation and this dossier:

- the open problem now concerns exactly the unresolved finite range
  `8<=k<4325`, beginning with a future diagnostic for `s_8`;
- the roadmap's two substantially duplicate resolved effective-onset sections
  are consolidated into one without changing its sole active priority;
- `CURRENT_STATUS.md` was checked and required no change;
- `K_eff=4325`, the proof algebra, checker, production code, tests,
  certificates, verifier, paper, and publication assets are unchanged.

### Authoritative-source coherence

A repository-wide Markdown/TeX search for `make the eventual identity`,
`no effective cutoff`, `no explicit cutoff`, related non-effectivity wording,
and `sufficiently large` found no stale current-state claim after the edit.
The sole direct `no explicit cutoff` occurrence is retained in the evidence
of `TASK-20260830__eventual_supnick_seam_onset`, where it accurately records
the limitation of that earlier qualitative task. Other `sufficiently large`
occurrences are historical task objectives or intermediate statements in the
proof chain and are followed by the effective bridge.

The corrected semantic audit returned `PASS` for all of the following:

- explicit proved tail `s_k=4k+6` for every integer `k>=4325`;
- valid but not claimed minimal cutoff in knowledge, status, roadmap, and
  dossier;
- unresolved range exactly `8<=k<4325`;
- radius-8 work labeled as a future diagnostic only;
- one consolidated effective-onset roadmap section and one active priority;
- absence of the rejected current open-problem wording.

An independent read-only documentary audit reached the same conclusion. Its
classification of historical matches agrees with the semantic audit and it
found no remaining authoritative contradiction.

### Commands and results

| Command/check | Exit/result | Interpretation |
|---|---|---|
| repository-wide `rg` stale-wording audit over `*.md` and `*.tex` | exit `0`; only the historical predecessor dossier contains direct `no explicit cutoff` wording | no stale current authoritative claim |
| UTF-8 semantic coherence audit | exit `0`; every predicate `PASS`, `stale_current_cutoff_claims=NONE`, `radius8_diagnostic_started=NO` | knowledge, status, roadmap, proof note, and dossier agree |
| independent read-only documentary audit | `PASS`; no files changed | corroborates the classification of current versus historical statements |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 27.96s` | repository regression suite; does not re-prove the theorem |
| scoped `git diff --check HEAD` | exit `0`; no whitespace output | final tracked documentation delta is whitespace-clean |
| protected-path diff audit | exit `0`; no path output | proof, checker, code, tests, certificates, verifier, paper, and publication assets are unchanged |
| five-file UTF-8/text audit | exit `0`; no BOM, NUL, CRLF, trailing whitespace, or missing final LF | documentary file integrity |
| complete `git diff HEAD` inspection | exactly five intended modified files | scope containment and final handoff review |

Two early coherence-audit implementations reported false negatives: Windows
PowerShell's default decoding obscured UTF-8 em-dash headings, and an
exact-string predicate crossed a Markdown line break. Explicit UTF-8 decoding
and semantic predicates corrected the audit; these were audit-script defects,
not repository defects. A sandbox ownership rejection of an initial read-only
Git batch was likewise resolved with a per-invocation `safe.directory` option;
no Git configuration or history was changed.

### Post-review claim classification and limits

- theorem status: unchanged exact theorem for the formal Supnick seam;
- documentation status: authoritative current sources synchronized;
- engineering status: regression suite passed; no implementation changed;
- certification status: no optimum, artifact, frontier, or verifier change;
- publication status: arXiv v1 and all publication assets unchanged;
- unresolved mathematics: cutoff minimality and all exact onsets in
  `8<=k<4325` remain open;
- excluded action: no `s_8` diagnostic was started.
