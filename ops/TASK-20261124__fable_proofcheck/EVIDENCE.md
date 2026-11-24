# Evidence

This file is identical on `fable/proofcheck-p1` and `fable/proofcheck-p2`.

## Environment

```text
paper_i_base=review/p1-square-radii@91ce1cbf42543b6bcaea8ac94688c34d29066087
paper_ii_base=review/p2-square-radius-project@51dfc1b8c9ba02faa665cb20f60ce2d87f761c00
platform=Windows 11 Home 10.0.26300
python=3.14.3
dependency_source=other (python-flint 0.9.0, sympy 1.14.0, standard library)
task_mode=STRICT
observed_on=2026-11-24
```

## Claim ledger

The full table, statement by statement, is in
[`docs/referee/proofcheck-2026-11.md`](../../docs/referee/proofcheck-2026-11.md).
This ledger records only how each kind of evidence is to be read.

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| The proofs in scope contain no error and no gap | referee judgement | hand reconstruction of every proof, compared with the text | yes: reconstructed before reading the author's proof | one reviewer, no external referee |
| Finite identities, table entries, signs and counts printed in the manuscripts | independently reproduced finite result | `exact` checks | yes: new code, no repository import | only the printed instances |
| Inequalities involving transcendental functions at specific arguments | independently reproduced finite result | `interval` checks with Arb | yes | relies on the correctness of Arb |
| Derivative formulas | exact theorem (elementary), machine-confirmed | `symbolic` checks with sympy | yes | relies on sympy simplification to zero |
| Statements quantified over all `n`, all orders or all radii | exact theorem, verified by hand | the hand argument; machine checks on finite ranges as corroboration | yes | the finite ranges do not prove the statement |
| `L_n < R*(n)` for `n = 3..14` | independently reproduced finite result | `P1-V5`, from the printed endpoints only | yes: no certificate read | Arb weights; same mathematical method as the paper |
| `R*(n) <= U_n` for `n = 8..14` | not verified here | earlier certificate verification | — | outside the scope of this task |
| The four reworded passages change wording only | engineering fact | each replacement is listed in the regression test of its paper and in `MATH_DIFF.md`; the rest of the scientific text is compared verbatim | the comparison is the repository's own test | Theorem 3.2 now states `N >= 3`, which the chain radius already required |

## Commands and checks

All commands were run locally in this task, from the root of the respective worktree.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python -I -B independent_check/fable_proofcheck` on `fable/proofcheck-p1` | exit 0, `46 items, 0 failures` (40 checks, 6 controls) | Paper I statements listed in the report | certificates, upper witnesses for `n >= 8`, square radii |
| `python -I -B independent_check/fable_proofcheck` on `fable/proofcheck-p2` | exit 0, `28 items, 0 failures` (20 checks, 8 controls) | S1 lemmas L1–L8, limit existence, enclosure (SM1.4) | Section SM13, upper bounds of Paper II |
| `python -m pytest independent_check/fable_proofcheck -q -p no:cacheprovider` on both branches | all passed (47 and 29 tests) | the same items through pytest, plus a registry test | — |
| `python -m pytest -p no:cacheprovider -o addopts=""` on `fable/proofcheck-p2`, eight full runs (two before the commits, six after) | six runs `110 passed, 1 skipped`; two runs with 13 and 12 failures | the existing suite is unaffected by the new files | the skip is pre-existing: “official external setup inputs unavailable”; see the intermittent failures below |
| `python -m pytest -p no:cacheprovider -o addopts=""` on `fable/proofcheck-p1`, four full runs before the wording commits | three runs `101 passed`; one run `1 failed, 100 passed` | the existing suite is unaffected by the new files | see the intermittent failures below |

## Commands after the approved wording commits

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python paper_assets/journal_p1_jogo/build.py` after each Paper I commit | `PDF pages=27 pdflatex_passes=3 bibtex_runs=1 unresolved=0 max_overfull_pt=0 overfull_above_1pt=0` | the manuscript builds with resolved references and no overfull box | visual layout |
| `python paper_assets/journal_p2_sidma/build.py` | `main.pdf: 10 pages` and `supplement.pdf: 15 pages`, final logs clean | both SIDMA documents build with reciprocal references | visual layout |
| `python -m pytest tests/test_journal_p1_jogo.py`, `tests/test_journal_p2_sidma.py` | `7 passed` each | the scientific text equals the reviewed text with the listed replacements | — |
| `python -I -B independent_check/p2` | `130 passed, 0 failed` | the pre-existing Paper II checker still accepts the supplement | — |
| `python -I -B independent_check/fable_proofcheck` on both branches | `46 items, 0 failures`; `28 items, 0 failures` | the new checks still read the tables and constants they verify | — |
| full existing suite on both branches | Paper I `two runs: 1 failed, 100 passed (the intermittent generator test again), then 101 passed`; Paper II `110 passed, 1 skipped` | nothing else depends on the reworded sentences | hosted CI |

## Artifact and provenance checks

The checks themselves read `main.tex`, `supplement.tex` and `numbers.tex` as
data and write nothing. The wording commits regenerated two PDFs.

- artifact paths: `paper_assets/journal_p1_jogo/main.pdf`; `paper_assets/journal_p2_sidma/supplement.pdf`.
- generating commands: `python paper_assets/journal_p1_jogo/build.py`; `python paper_assets/journal_p2_sidma/build.py`.
- inputs: the manuscript sources at the wording commits on `fable/proofcheck-p1` and `fable/proofcheck-p2`.
- environment: Windows 11, pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025, TinyTeX), BibTeX 0.99d, Python 3.14.3.
- SHA-256 after the last wording commit: `main.pdf` (Paper I) `8b011a7e7f496c27b430df59a5c1fcad9bcf6c85cae1a6b547489181873993f7`; `supplement.pdf` `a112891445fe1654d8e2aec485f19def8922c7b9e25698837b067d91a51fc56e`.
- unchanged: `paper_assets/journal_p2_sidma/main.pdf`, SHA-256 `46bde88501f5a84317dd06ab8502f4159e2e1eefccbd385161ed9de9f1b21596`, rebuilt byte-identical.
- determinism: before any edit, the same commands reproduced the three tracked PDFs byte for byte in this environment. Reproduction in another TeX distribution was not tested.
- independent verifier: not applicable to a PDF; the text is guarded by the two regression tests.

## Failed checks and negative evidence

* **Intermittent failure of a pre-existing test, Paper I branch.** In two of
  six full runs on `fable/proofcheck-p1` (once before and once after the
  wording commits),
  `tests/test_general_radii.py::test_linear_generator_reproduces_tracked_certificate_from_a_clean_checkout`
  failed. It passed in the other four full runs and in seven isolated runs,
  and 25 consecutive runs of
  `paper_assets/general_radii/certify_radii.py --linear 3` reproduced the
  tracked certificate each time. The test does not import or read any file
  added by this task. The cause was not determined. It is reported, not
  fixed, because it is outside the scope.
* **Intermittent failures of pre-existing tests, Paper II branch.** In two
  of eight full runs on `fable/proofcheck-p2`, 13 and 12 tests of
  `tests/test_line_upper.py` (the `test_rejects_tampering` cases among them)
  failed with a Windows `OSError`. Only the truncated summary line
  `OSError: [Win...` was captured; the failure did not recur in three further
  logged runs, so the error code is unknown. The file passes when run alone
  (`14 passed`). These tests use temporary directories and do not read any
  file added by this task. A race in temporary-directory handling between
  consecutive pytest sessions on Windows is my conjecture, not an
  established cause.
* **Defects found in the new checker during development**, all repaired and
  none concerning a manuscript claim: a sympy relational rejected by the
  strict truth test; two sympy identities needing the assumption
  `s - x > 0`; `arb ** int` returning NaN at an exact zero; an index error in
  a test-instance generator; a self-imposed tolerance `1e-37` on an
  enclosure whose stated accuracy is 30 decimal places.
* **Negative controls.** Fourteen deliberately false variants are rejected
  (`P1-X1`…`P1-X6`, `P2-X1`…`P2-X8`), so the checks are able to fail.
* **Attempts to falsify.** Brute force over all tours (`N <= 9`), all ordered
  triples for the triangle defect, all nonadjacent pairs at 118 chain roots,
  adversarial orders for the deletion estimates, and line spans against the
  lower bound of Theorem SM1.1 produced no counterexample.

## Final diff inspection

- `git status --short`: clean after every commit. First delivery: `CURRENT_STATUS.md` modified and new files under `docs/referee/`, `independent_check/fable_proofcheck/`, `ops/TASK-20261124__fable_proofcheck/`. Wording commits: the manuscript source, its PDF, `MATH_DIFF.md` and the regression test of the paper concerned.
- complete `git diff` inspected: yes, for `CURRENT_STATUS.md` and for every line of the four wording commits.
- untracked additions inspected directly: yes, every new file was written in this task and reviewed before staging.
- direct whitespace check for untracked additions: `git diff --cached --check` after staging, no output.
- `git diff --check`: no output.
- protected paths unexpectedly changed: none. The first delivery changed no file under `paper_assets/`, `results/`, `src/`, `tests/` or the verifiers. The wording commits changed only the files named above, with the author's approval.
- generated files unexpectedly changed: none.

## Residual uncertainty

* The cited literature was not consulted; Theorem 3.2 of Paper I was made
  independent of its citation by a separate proof.
* The certificates and the upper witnesses for `n >= 8` were not re-verified.
* Interval results depend on Arb, symbolic results on sympy.
* No hosted CI run exists for these commits; nothing is claimed about it.
* The intermittent test failures above are unexplained.
