# Evidence

## Drafting environment (historical)

```text
repository=falker47/ringmin
observed_head=9f67244b6226619df99a5eea2249f3fca8a32669
inspection=GitHub connector and public repository pages
local_checkout_available=false
commands_run_in_repository=none
task_mode=STRICT
```

The distributed draft was intentionally left `IN_PROGRESS`; none of its command claims were treated as executed evidence.

## Applying environment

```text
repository=falker47/ringmin
branch=main
PRE_BOOTSTRAP_HEAD=9f67244b6226619df99a5eea2249f3fca8a32669
observed_on=2026-08-04
platform=Windows PowerShell
python=3.14.3
numpy=2.4.3
scipy=1.17.1
mpmath=1.3.0
matplotlib=3.10.9
pytest=9.0.2
dependency_source=requirements.txt versions already installed; tests import the working-tree src directory through tests/conftest.py
task_mode=STRICT
```

Raw Git reads initially failed the sandbox ownership check. Subsequent read-only Git commands set `safe.directory` to the resolved repository root for that command only; no configuration or repository state was written.

Initial `git status --short` output:

```text
?? ringmin_continuous_review_kit/
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| The workflow delta contains only the eleven authorized additions | engineering fact | final expanded status, direct file inventory, empty tracked diff | yes, direct filesystem and Git inspection | additions remain untracked for manual review |
| Chain, fixed-order full feasibility, global optimum, finite certification, heuristic candidate, and conjecture remain distinct | documentation and mathematical-scope fact | paper source, `verify.py`, evaluator/search code, and cross-document review | review independent of the kit draft | no new theorem or certificate was produced |
| Local regression suite passes | local engineering verification | `python -m pytest`, exit 0 | test suite includes independent SLSQP cross-checks but also production-coupled tests | not a global certificate |
| Smoke verifier passes for `n=3..8` | local incumbent and fixed-order bracket verification | `--skip-frontier` output below, exit 0 | standalone verifier does not import `src/ringmin` | frontier/global-pruning verification is skipped |
| Full verifier passes locally for `n=3..14` | independently reproduced finite-verifier result | full output below, exit 0 | standalone high-precision implementation | not exhaustive re-enumeration; depends on local Git-ignored progress logs |
| Values for `n=15..18` remain non-exhaustive candidates | heuristic upper-bound classification | public paper and heuristic artifacts | source classification inspected | candidates were not recomputed in this task |
| No pre-existing tracked file changed | engineering fact | `git diff --name-status HEAD` produced no output | Git object comparison | ignored-file contents were not regenerated or claimed as delta |
| Hosted CI is not claimed green | hosted-state limitation | CI configuration inspected; no hosted run for the SHA inspected | local checks are separate | hosted status remains `NOT INSPECTED` |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python -m pytest` | exit `0`; `12 passed in 31.54s` | local regression suite | full certificate frontier |
| `python verify.py --start 3 --stop 8 --skip-frontier` | exit `0`; six incumbent/local passes; frontier `SKIP` | smoke range and fixed-order local bracket | global pruning/frontier |
| `python verify.py --start 3 --stop 14` | exit `0`; all twelve incumbent/local/frontier rows pass | local full verifier over tracked artifacts plus local provenance logs | fresh-clone portability or exhaustive re-enumeration |
| workflow inventory, relative-path, Markdown-link, newline, and trailing-whitespace audit | exit `0`; all checks `PASS` | all eleven new files directly | scientific truth beyond the inspected sources |
| cross-project-name and machine-specific-path scan | exit `0`; `PASS` | installed workflow text | pre-existing out-of-scope repository files |
| `git diff --name-status HEAD` | exit `0`; no output | tracked pre-existing files unchanged | untracked additions |
| `git status --short --untracked-files=all` | exit `0`; exactly eleven authorized files | complete untracked addition inventory | file semantics |
| `git status --short` | exit `0`; seven grouped untracked entries | final working-tree scope | file contents |
| `git diff --check` | exit `0`; no output | whitespace errors in tracked diffs | untracked additions, which were checked directly |

## Exact mandatory command output

### `python -m pytest`

Exit code: `0`

```text
............                                                             [100%]
12 passed in 31.54s
```

### `python verify.py --start 3 --stop 8 --skip-frontier`

Exit code: `0`

```text
n=03 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
n=04 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
n=05 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
n=06 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
n=07 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
n=08 incumbent=PASS local=PASS frontier=SKIP eta=1.0e-12 frontier_size=NA total=NA
```

### `python verify.py --start 3 --stop 14`

Exit code: `0`

```text
n=03 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=1
n=04 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=3
n=05 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=12
n=06 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=60
n=07 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=360
n=08 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=2520
n=09 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=20160
n=10 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=4 total=181440
n=11 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=6 total=1814400
n=12 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=9 total=19958400
n=13 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=10 total=239500800
n=14 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=11 total=3113510400
```

### `git status --short`

The sandbox invocation added command-local ownership handling and a null global-excludes file; these do not alter repository state. Exit code: `0`.

```text
?? AGENTS.md
?? CURRENT_STATUS.md
?? PROJECT_KNOWLEDGE.md
?? RINGMIN_REVIEW_PROTOCOL.md
?? _TEMPLATES/
?? ops/
?? research/
```

### `git diff --check`

Exit code: `0`; no output.

Ordinary Git diff does not include the untracked additions. The direct audit over all eleven files separately returned:

```text
PASS: all 11 authorized workflow files exist
PASS: no trailing whitespace and every workflow file ends with LF
PASS: reconciled relative path references exist
PASS: no broken relative Markdown links
PASS: no cross-project names or machine-specific absolute paths in installed workflow files
PASS: no tracked pre-existing file changed
PASS: start.md was not created
```

The final post-update audit then returned:

```text
PASS: 11 authorized files only; full direct content/path/link/UTF-8/whitespace audit clean
PASS: temporary kit absent; start.md absent; no cross-project or machine-specific residue
PASS: no tracked pre-existing file changed; live states READY_FOR_REVIEW
```

## Artifact and provenance checks

- No source, test, result, certificate, frontier, progress log, checkpoint, paper, generated asset, CI file, requirement, citation, or publication artifact was modified.
- Existing optimum/frontier artifacts record generation commit `fea000523a1ec4193d8ba9c4637563fd65e86d1a`; this task did not regenerate them or prove source-tree identity with that commit.
- The full verifier additionally reads `results/checkpoints/progress_nNN_lb3.log`. Those logs were present for `n=3..14` in this checkout but the directory is Git-ignored.
- All twelve tracked frontier files store the progress-log field with Windows-style backslashes. A fresh clone, especially on POSIX, cannot reproduce the current full-frontier run without restoring or regenerating the logs and handling the paths portably.
- Artifact generation is not applicable to this workflow-only delta.

## Failed checks and negative evidence

- Initial raw Git reads failed with the sandbox ownership guard. Command-local ownership handling resolved the read-only inspection without changing Git configuration.
- The first UTF-8 transfer approach stopped before applying a patch because the orchestration runtime lacked its Base64 decoder; it created no file. The explicit UTF-8 `apply_patch` retry succeeded.
- An attempted `core.excludesFile=NUL` override was rejected by Git before inspection. The successful final Git commands used `/dev/null` for that command only.
- No scientific, test, smoke-verifier, or full-verifier gate failed.

## Final diff inspection

- `git status --short`: exactly the seven grouped entries shown above, representing the eleven authorized untracked workflow files.
- Complete tracked diff: empty.
- Untracked additions: all eleven files read in full and checked directly.
- Direct whitespace check for untracked additions: pass.
- `git diff --check`: exit `0`, no output; limitation explicitly recorded.
- Protected paths unexpectedly changed: none.
- Generated files unexpectedly changed: none.
- Temporary input removed: only `ringmin_continuous_review_kit/`, containing fourteen untracked kit files, after exact-target verification.

## Residual uncertainty

- Hosted CI for the bootstrap SHA was not inspected; no hosted-green claim is made.
- A fresh clone does not contain the ignored progress logs required by the current full verifier, and the stored paths are Windows-oriented.
- The workflow bootstrap adds documentation and process controls only. It neither proves the next seam theorem nor extends finite certification beyond `n=14`.
