# Evidence

## Environment

```text
repository_head=98d6a6e340e4008ce35e789c54333ae43466b49d
platform=Windows
python=3.14.3
dependency_source=existing environment; standalone verifier uses stdlib only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Selected originals retain their bytes | engineering fact | manifest and source snapshot | SHA-256 identifies content, not mathematical validity |
| Twelve global brackets | computer-certified finite result, locally reproduced | VERIFICATION_FINAL.json | independent of production/generator; adapted from reviewer code, not a fresh external review |
| Strict lower endpoint for infimum | proved implication of positive finite margins | proof note and exact buffers | finite n=3,...,14 only |
| P1 and P2 regressions rejected | engineering/falsification evidence | TARGETED_TESTS.txt and new tests | tests complement proof and full run |

## Commands and checks

Startup: `git status --short` showed only the expressly exempted ZIP;
`git rev-parse HEAD` returned the base above. `git diff --check`: exit 0.
`python --version`: Python 3.14.3. `py -0p`: no installed Pythons found;
the working `python` executable is used instead.

Original generator SHA-256:
`e785b43bd2a24cf74d807479b5719e5f1b5e762027e41c4a69af07a655531549`.
Original Windows JSON SHA-256:
`96bdf9b53977724f1b8c0640425365bf32897fd4415104f17bfd1afbfa52c693`.
Original candidate file SHA-256:
`cfb95a8354c9ea0529f5ece85118712a3e94c36aed1e14a43b6f32c6e98549db`.
Canonical `certificate` digest (not whole-file digest):
`6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0`.

## Artifact and provenance checks

Selected files and their byte hashes: `reproducibility/global_brackets/manifest.json`.
All supplied source files: `SOURCE_HASHES.json`. Historical report environment,
timestamps and script fingerprints do not authenticate an execution. Historical
review results are not counted as commands run in this task.

## Failed checks and negative evidence

Startup ownership and inaccessible-cache/ignore messages did not modify files.
Required-input blockers were resolved by explicit user messages. P1/P2 findings
are preserved in the original STRICT review and exercised by regressions.

## Current local executions

All commands below were executed in this task from the repository root, using
existing Python 3.14.3. No dependencies were installed.

| Exact command | Exit and material output | Checks / limits |
|---|---|---|
| `python -I -S verify_global_brackets.py --output ops/TASK-20260919__global_bracket_verifier/VERIFICATION.json` | 0; PASS_GLOBAL_BRACKETS; 5.36 s | Initial complete proof and pins; earlier source fingerprint retained as chronology |
| `python -m pytest tests/test_global_brackets.py -q -p no:cacheprovider --basetemp=reproducibility/.work/global-brackets-pytest` | 1; three failures | Tau fixture expectation and two invalid inherited stdin handles; corrected, not hidden |
| `python -m pytest tests/test_global_brackets.py -o addopts= -q -p no:cacheprovider --basetemp=reproducibility/.work/global-brackets-pytest-2` | 0; **44 passed in 21.92s** | Rehashed P1/P2 failures, exact small DP/insertion/cosine oracles, isolated CLI; no production or generator imports |
| `python -m pytest -o addopts= -q -p no:cacheprovider --basetemp=reproducibility/.work/global-brackets-full-tests` | 0; **59 passed in 55.75s** | Entire suite, including production-coupled tests and historical log restoration in scratch; no Stage A search |
| `python -I -S verify_global_brackets.py --output ops/TASK-20260919__global_bracket_verifier/VERIFICATION_FINAL.json` | 0; **PASS_GLOBAL_BRACKETS**, pinned input PASS; 4.02 s | Final code; 908 intervals, 47 witnesses, 540 central tangencies, 3,004 Cartesian pairs, 6,008 angular inequalities, 268,648 explicit classes, 3,374,988,556 covered classes |
| `python -m ruff check verify_global_brackets.py tests/test_global_brackets.py` | 0; **All checks passed!** | New-code lint; no mathematical certification |

Pytest output was saved with PowerShell `2>&1 | Tee-Object -FilePath` to
TARGETED_TESTS.txt and FULL_TESTS.txt; `exit $LASTEXITCODE` preserved pytest's
exit status. Formatting used `python -m ruff format` only on new files.
Initial lint found an unused import and a combined import; both corrected.

Final verifier SHA-256:
`599b49afc3718738a4adf04ec797c4c0e52c5d53076bfbb00e826dde260d4e95`.
No original generator or reviewer executable was run. Archived reports are
historical runs; current outputs come from the adapted implementation.

## Preservation and final diff inspection

`python ops/TASK-20260919__global_bracket_verifier/check_preservation.py --source
../ringmin_strict_review_input/ringmin_strict_review` checks the external snapshot,
archive equality, allowed dirty paths, protected paths and full-content whitespace.
Add `--staged` after staging to check original bytes in Git's index.
The external path is an argument, not an embedded machine-specific source path.

All 95 supplied files remain unchanged; all 13 selected originals equal their
source bytes. STRICT_REVIEW_IT.md has one inherited blank EOF; a file-specific
whitespace attribute preserves it without rewriting evidence. Every other task
addition is checked for trailing whitespace and blank EOF, including untracked
files omitted by ordinary `git diff --check`.

Complete source/test/proof/dossier content was inspected. Imported JSON is read
in full, parsed and compared byte for byte to the supplied source; the candidate
is semantically checked by the full verifier and the three negative certificates
by regressions. Historical reports are not promoted to current run evidence.

Protected tracked paths checked against base: `src/ringmin/`, `verify.py`,
`results/`, `paper_assets/`, README, REPORT, CITATION, AGENTS, review protocol,
knowledge index and roadmap. No changes. The exempt ZIP is never staged,
modified, moved or included in task paths.

Final staged audit command above with `--staged`: exit 0,
`PASS_PRESERVATION_AND_SCOPE`; 95 external files unchanged, 13 originals
byte-identical in source/worktree/index, 31 added or modified files read in full,
protected tracked paths unchanged, exempt ZIP untracked. Both `git diff --check`
and `git diff --cached --check` exited 0. Staged code/document diffs were read;
all archived additions were parsed/read and byte-compared in full.
Initial sandbox `git add` failed on index.lock; authorized escalation succeeded.

## Integration and hosted evidence boundary

Task changes are prepared on main from the recorded base for authorized commit
and normal push. The exact resulting commit cannot be embedded in its own
content; it is the commit introducing this dossier and is reported at handoff.
GitHub Actions now runs the complete default command in addition to the existing
test suite/smoke gate. No historical Stage A workflow is invoked. Hosted status
must be read for that exact SHA after push; none is inferred from local results.
No baseline or Review State Registry is promoted.

### Actual integration attempt

- `git commit -m "Integrate independent complete global bracket verifier"`:
  exit 0, commit `ff1a51b6827535dd16f92d13389ffe0f4ad866b4`, 31 task paths.
- `git push origin main`: exit 1, rejected with `fetch first` because remote
  history is not contained in the requested starting checkout.
- Read-only GitHub API `repos/falker47/ringmin/branches/main` returned
  `5c98063a9a38d6f7f76d7ec7a073f3cdf8d5717a`. Comparison from the starting base
  reported ahead_by=2, behind_by=0. The remote-only commits are
  `c0d9d6e66afc8ec94918adbe23345bdc7a7fa43b` and
  `5c98063a9a38d6f7f76d7ec7a073f3cdf8d5717a`; they include changes to
  CURRENT_STATUS.md, README, publication history and correction-package status.
- Exact-SHA Actions query
  `repos/falker47/ringmin/actions/runs?head_sha=ff1a51b6827535dd16f92d13389ffe0f4ad866b4&per_page=5`
  returned total_count=0. **No hosted CI pass is claimed.**
- No history reconciliation or force push was attempted. The standing Git
  authorization forbids merge/rebase without explicit user approval. A local
  documentation-only follow-up records this blocker; implementation bytes and
  all verification results above remain applicable.

## Residual uncertainty

No new independent external review, Registry acceptance, proof-assistant proof,
historical Stage A audit or journal-readiness claim is part of this task.
