# Evidence

## Environment

```text
local_parent=c0075cf9dbe902571748299b21e368a0433c784e
remote_parent=5c98063a9a38d6f7f76d7ec7a073f3cdf8d5717a
common_base=98d6a6e340e4008ce35e789c54333ae43466b49d
platform=Windows
python=3.14.3
dependency_source=existing environment; no dependency installation
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Limitation |
|---|---|---|---|
| Combined histories retain both implementations/contexts | engineering fact | parent-tree audit and merge ancestry | not scientific acceptance |
| Original evidence bytes preserved | engineering fact | source/archive SHA-256 and index checks | hashes do not prove mathematics |
| Twelve finite brackets still verify | reproduced computer-certified finite result | complete standalone verification | no new independent review or all-n claim |
| Hosted CI outcome | post-commit engineering observation | exact-SHA run reported at handoff | local tests alone cannot establish this |

## Commands and checks

Git commands use command-local `-c safe.directory=<repository-root>` in the
sandbox. `git fetch origin`: exit 0, remote main updated from 98d6a6e to exactly
5c98063. `git merge-base HEAD origin/main`: the full common base above.
`git log --left-right --oneline HEAD...origin/main`: local c0075cf/ff1a51b,
remote 5c98063/c0d9d6e, exactly two commits each.

Before merge:
`python ops/TASK-20260919__global_bracket_verifier/check_preservation.py --source
../ringmin_strict_review_input/ringmin_strict_review --staged`: exit 0,
PASS_PRESERVATION_AND_SCOPE, 95 external files unchanged, 13 originals
byte-identical, zero dirty tracked paths, ZIP untracked.

`git merge --no-ff --no-commit origin/main`: exit 1, content conflict only in
CURRENT_STATUS.md. No scientific or numerical conflict.

All following Python checks ran in this task on the merged tree with Python
3.14.3. No source/test/proof bytes were changed by the resolution.

| Exact command | Exit / material result | Property and limit |
|---|---|---|
| `python -I -S verify_global_brackets.py --output ops/TASK-20260919__merge_global_bracket_verifier/VERIFICATION.json` | 0; PASS_GLOBAL_BRACKETS, pinned binding PASS; 4.588215900002979 s | Complete twelve-case exact-arithmetic check, independent of production/generator; derived reviewer implementation, not new scientific review |
| `python -m pytest tests/test_global_brackets.py -o addopts= -q -p no:cacheprovider --basetemp=reproducibility/.work/merge-global-brackets-strict` | 0; 44 passed in 22.72s | All STRICT regressions, P1/P2 mutations and original adversarial fixtures, small independent oracles |
| `python -m pytest -o addopts= -q -p no:cacheprovider --basetemp=reproducibility/.work/merge-global-brackets-full` | 0; 59 passed in 53.36s | Entire repository suite, including production-coupled checks; not a substitute for full verifier |
| `python scripts/frontier_logs.py restore` | 0; PASS 12 exact log archives; 9649682 original bytes; restored/existing readback identical | Hash-checked original evidence, no search regeneration |
| `python verify.py --start 3 --stop 14` | 0; incumbent=PASS local=PASS frontier=PASS for all twelve n | Historical standalone saved-evidence check; not interval replay of historical pruning |
| `python verify.py --start 3 --stop 8 --skip-frontier` | 0; incumbent=PASS local=PASS frontier=SKIP for all six n | Exact existing CI smoke gate, not global frontier proof |
| `python -m ruff check --no-cache verify_global_brackets.py tests/test_global_brackets.py ops/TASK-20260919__merge_global_bracket_verifier/check_merge.py` | 0; All checks passed! | Lint of integration and task audit |
| `python -m ruff format --check --no-cache verify_global_brackets.py tests/test_global_brackets.py ops/TASK-20260919__merge_global_bracket_verifier/check_merge.py` | 0; 3 files already formatted | Read-only formatting gate |
| `python ops/TASK-20260919__merge_global_bracket_verifier/check_merge.py --source ../ringmin_strict_review_input/ringmin_strict_review` | 0; PASS_MERGE_UNION_AND_PRESERVATION | All 656 nonconflicting paths, 95 external files, 13 original source/worktree/index identities, ZIP and whitespace |

Pytest and historical verifier commands used PowerShell `2>&1 | Tee-Object
-FilePath <dossier-output>` followed by `exit $LASTEXITCODE`. Their complete
outputs are STRICT_TESTS.txt, FULL_TESTS.txt, FULL_VERIFIER.txt and CI_SMOKE.txt.
The full suite uses only cache/output-location overrides; no tests are skipped
relative to the CI `python -m pytest` gate.

VERIFICATION.json records 47 witnesses, 908 angle intervals, 540 central
tangencies, 3,004 Cartesian pairs, 6,008 angular inequalities, 268,648 explicit
classes and 3,374,988,556 covered classes. Its verifier SHA-256 remains
`599b49afc3718738a4adf04ec797c4c0e52c5d53076bfbb00e826dde260d4e95`.
The canonical certificate digest remains
`6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0`.

## Artifact and provenance checks

Original artifacts are not regenerated. New outputs in this dossier record
executions on the merged tree; verifier and proof bytes must equal ff1a51b.
The task-specific parent-tree audit replaces the old checker's pre-merge path
allowlist, which deliberately excludes the now-authorized remote README changes.
It retains the same external 95-file and selected 13-file preservation checks.

## Failed checks and negative evidence

The initial Git ownership error and expected merge conflict are recorded in
TASK_LOG.md. No rebase, squash, reset, overwrite-checkout, forced push, tag,
release or Registry action is used.
The first formatting check of the new task audit script reported that one file
would be reformatted. `python -m ruff format --no-cache
ops/TASK-20260919__merge_global_bracket_verifier/check_merge.py` corrected it;
the final three-file check passes. No verifier/test formatting change occurred.

## Final diff inspection

The staged tree is compared by exact Git blob IDs and modes with the unique
three-way union of both complete parent trees. All 656 nonconflicting paths
match, including every local verifier/evidence addition and all eight remote
publication/journal paths. Only CURRENT_STATUS.md and nine new dossier files
differ from that union. There are no unstaged tracked changes. This verifies
integration preservation; it is not a fresh independent scientific source review.

The conflict resolution preserves the complete remote publication/review/journal
context verbatim, with an explicit historical attribution. It retains the local
verifier's scope/limits and prior rejected-push evidence by link, records current
verification, and gives exactly one next independent-review task.

All new files are read in full by the audit (including JSON parsing and explicit
trailing-space/blank-EOF checks), and status/dossier/checker content is inspected.
`git diff --check` and `git diff --cached --check` pass. The automatic remote
README, publication ledger, correction README and five journal documents are
retained exactly. Protected solver, verify.py, results, original inputs,
publication source/PDFs, citations, index, roadmap, AGENTS and review protocol
remain unchanged. Old task dossiers are preserved, not retroactively rewritten.

The ZIP is the sole remaining untracked file; SHA-256 remains
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.
No Registry connector call is made, and no baseline acceptance marker is added.

## Residual uncertainty

No independent scientific acceptance is performed. Journal blockers and
historical floating-point evidence limitations remain separate. Hosted CI is
queried after the normal push and reported for the exact resulting SHA; it
cannot be predicted or embedded as passed in its own commit.
