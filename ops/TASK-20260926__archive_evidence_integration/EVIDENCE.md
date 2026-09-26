# Evidence

## Environment and identity

```text
task=POST-RING-6_ARCHIVE_EVIDENCE_INTEGRATION
mode=STRICT
phase=implementation
platform=Windows / PowerShell
python=3.14.3
initial_local_head=80919666c3c54f8ce20cf66c456d413f6a2c075f
base_head=7201f788b586ae059078dde6221d58b0ce8f79a1
accepted_review_baseline=80919666c3c54f8ce20cf66c456d413f6a2c075f
historical_numerical_audit_baseline=c0d9d6e66afc8ec94918adbe23345bdc7a7fa43b
release_tag=v1.1.0-dcg-presubmission
release_commit=80919666c3c54f8ce20cf66c456d413f6a2c075f
version_doi=10.5281/zenodo.22849826
```

Accepted-baseline source: Review State Registry, live `ringmin` row,
`State!A1:J5` at initial preflight and `State!A1:F2` at 18:30 UTC on 2026-09-26.
Both returned status `accepted`, schema `2`, update `2026-09-19T18:33:13Z` and
the accepted SHA above. These are current read-only observations, not Registry
writes or a new acceptance. The historical [Registry extract](evidence/registry_state.json)
is a derivative of the previous audit's read, not a substitute for those reads.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Audit reported PASS for the release at `80919666...` | Historical archival observation | [Full report](evidence/AUDIT.md), [structured evidence](evidence/EVIDENCE.json), [checkpoint](evidence/CHECKPOINT.md) | Integration consistency check; audit not repeated |
| 701/701 files matched, 13/13 originals matched | Historical integrity result | [Inventory](evidence/ARCHIVE_INVENTORY.csv), [comparison](evidence/archive_comparison.json), [original checks](evidence/originals_check.json) | No new ZIP-to-Git comparison or scientific computation |
| One complete execution returned PASS_GLOBAL_BRACKETS, exit 0, input binding PASS | Historical execution of the archived verifier | [Execution](evidence/verifier_execution.json), [stdout](evidence/verifier.stdout.txt), [stderr](evidence/verifier.stderr.txt), [commands](evidence/commands.jsonl) | No verifier executed here; not independent proof review |
| Original copies and public hashes are preserved | Engineering fact | [Manifest](EVIDENCE_MANIFEST.json), local copy manifest, current checks below | Documentary self-check, not independent review |
| Finite scientific claim is unchanged | Inherited computer-certified finite result | [Owning ledger](../../knowledge/CERTIFICATION.md#independent-exact-arithmetic-global-brackets), unchanged protected paths | `L_n < R*(n) <= U_n`, `n=3,...,14`, exact width `10^-11`; no extension or new acceptance |

The fixed-order seam theorem is unchanged and separate. Archiving, recorded
execution, cross-check, proof, independent review and editorial peer review
remain distinct. Neither release nor integration implies journal acceptance.

## Original persistence and public derivations

Durable directory locator (full absolute path and mapping are local, avoiding
machine-specific paths in the public repository):

```text
Documents/RingminEvidence/POST-RING-6_ARCHIVE_EVIDENCE_INTEGRATION_20260926T182736Z_9ae979aa/
  COPY_MANIFEST.json
  originals/
```

All 68 original top-level audit files were copied, 8,481,814 bytes total,
including the downloaded archive and auxiliary original outputs. The extracted
checkout was not copied. No source was deleted or altered and no existing
destination was overwritten. The local copy manifest records each absolute
source/copy path, SHA-256, size before/after and byte-identity result. Its
SHA-256 is `05d8f60cc418e621c75e92b67d6e133326158a803a652656e87c4bdc5defe8c3`
and size is 47,197 bytes; [the public manifest](EVIDENCE_MANIFEST.json) binds it.

The public selection is 28 evidence files, with 20 `BYTE_IDENTICAL` and eight
`DERIVED` entries. The manifest maps original basenames and durable-relative
paths to public paths, with original and public sizes/hashes and transformations.
`DERIVED` never means byte-identical. [The preparation script](prepare_public_evidence.py)
reproduces the selection from a durable copy into a new output directory.

Transformations: replace local repository/audit/home path roots and private
Registry URL with named aliases; omit the unrelated project's Registry row;
add DERIVED banners to three Markdown reports; serialize changed JSON/JSONL
and Markdown as UTF-8/LF. Timestamps, commands, outcomes, counts, mathematical
text, DOI, tag and commit identities are retained. Embedded historical file
hashes still describe their original targets; only the public manifest describes
the derivative file bytes. The selected outputs undergo content inspection and
credential/URL-pattern scanning before publication.

PersonalContext, full Registry history, raw HTML, auxiliary source-read outputs,
helper programs, archive ZIP and extracted source tree are not published here.
All top-level originals remain available in the durable directory; references
to omitted audit files in historical reports resolve there, not to reconstructed
files. Raw HTTP records preserve acquisition timestamps, status, target URLs
and hashes; DOI HTML and ZIP payloads are local only. The public material
includes complete reports, structured results, inventory, command/verifier logs,
metadata responses, before/after preservation snapshots and their bindings.
It contains no duplicate source snapshot or new scientific artifact.

## Archive identity and differences

The [record](evidence/zenodo_record.json), [tag](evidence/github_tag.json),
[release](evidence/github_release.json) and [metadata comparison](evidence/metadata_comparison.json)
are historical captures. Current Git reads confirm the same tag target; this
task does not re-query or modify Zenodo. The CFF version is
`1.1.0-dcg-presubmission`; the deposited version includes the literal `v`,
matching the tag. The report documents that distinction and the `/tree/tag`
relation rather than `/releases/tag/`; neither is silently normalized.

Only the software DOI is added to current CFF. Its preferred arXiv-v2 paper
citation is unchanged. The DOI identifies release `80919666...`; it does not
identify the integration commit or include this dossier. No concept DOI,
ORCID or editorial status is added to current metadata. Historical responses
retain their observed fields with the original limitations.

## Commands and checks

All integration checks are local and independent of production/scientific
code, but performed by the implementer, not an independent reviewer. Git
commands use command-scoped `safe.directory`; no persistent config change.

| Command/check actually run | Exit/result | Property and limit |
|---|---|---|
| `git status --porcelain=v1 --untracked-files=all`, `git diff --exit-code`, `git diff --cached --exit-code` before sync | 0; only exempt ZIP untracked | Clean tracked/index state; no science checked |
| `git fetch --no-tags origin main`; `git merge-base --is-ancestor 80919666c3c54f8ce20cf66c456d413f6a2c075f origin/main` | 0 | Authorized fetch; initial local HEAD ancestor of remote |
| `git ls-remote origin refs/heads/main refs/tags/v1.1.0-dcg-presubmission` | 0; main `7201f788...`, tag `80919666...` | Live Git identity, not acceptance |
| `git merge --ff-only origin/main`; `git rev-parse HEAD origin/main` | 0; `Fast-forward`; both `7201f788...` | No merge commit/history rewrite; post-sync status and ZIP unchanged |
| Task-local `python -B ringmin_archive_integration_copy.py` | 0; PASS, 68 files, 8,481,814 bytes | Source/copy SHA-256 and size before/after |
| `python -B ops/TASK-20260926__archive_evidence_integration/prepare_public_evidence.py DURABLE_ROOT NEW_OUTPUT_DIRECTORY` | 0; PASS, 28 public files, 8 derived, 20 byte-identical | Public selection/redaction, not audit reproduction |

The following current checks also completed successfully (exit 0):

| Command/check | Exact material output/result | Scope |
|---|---|---|
| `python -B ops/TASK-20260926__archive_evidence_integration/check_evidence.py --durable DURABLE_ROOT` | `PASS: 28 evidence hashes; JSON/CSV and 24 log records; 701 inventory rows; 13 recorded originals; one historical verifier record`; 68 original copies and sources match | Parses all new evidence, compares recorded identities/results/logs, hashes actual copies; no science rerun |
| Same command with `--staged --durable DURABLE_ROOT` | `PASS: all 28 staged evidence blobs match declared SHA-256 and sizes` | Reads bytes with `git show :path`; original CRLF preserved by dossier attributes |
| `python -B -c 'from cffconvert.cli.cli import cli; cli()' --validate` | `Citation metadata are valid according to schema version 1.2.0.` | Existing isolated CFF tooling; unchanged preferred-citation also checked bytewise modulo checkout EOL |
| Direct inspection of all 35 dossier additions | UTF-8, JSON parsing, no trailing whitespace, no private-path/email findings | Every addition read; payload structures and entire command log inspected; no scientific validation |
| `git diff --check`; `git diff --cached --check` | No output, exit 0 | Working and staged whitespace; direct scan also includes untracked additions |
| Protected-path diffs against full `7201f788...` and `80919666...` | No output, exit 0, excluding only four allowed documents before new dossier staging | All 697 protected initial tracked paths unchanged, including historical dossiers |
| Raw SHA-256/size comparison with historical repository-preservation capture | `PASS: 698 protected files byte-identical to historical audit preservation snapshot (697 tracked + exempt ZIP)` | Additional raw-byte preservation check, now included in the task checker |

`DURABLE_ROOT` denotes the full local path reported in the handoff; the locator
above identifies it without publishing machine-specific paths. For CFF only,
the process-local `PYTHONPATH` was set to the resolved existing directory
`reproducibility/.work/archival_metadata/cff-tools`. No package was installed
or dependency changed. The sandbox could not read those installed tool files
(PermissionError, exit 1); the authorized elevated retry returned the schema
success above. This was an environment-access failure, not invalid CFF.

Public verification uses `check_evidence.py` from a checkout with the base
commit available in Git; it does not require the omitted private ZIP or local
originals. The optional `--durable` mode additionally checks those files and
the historical Windows raw-byte preservation snapshot. During final inspection
these local-only checks were separated from the default public mode.
Re-running the public preparation into a fresh temporary directory reproduced
all 28 published files and the manifest byte-for-byte; no audit was re-executed.

No unit suite, global/historical verifier, pilot, replay, build, checkpoint
recovery, scientific search or independent review is executed.

## Failed attempts and negative evidence

Initial Git ownership/network failures and the temporary fast-forward blocker
are retained in [TASK_LOG.md](TASK_LOG.md). The permission block was resolved
only by explicit user authorization. PersonalContext console rendering hit a
code-page error; escaped JSON allowed historical-context inspection. A preliminary
path scanner matched the tail of `https://` and a regex literal in the command
log; these were false positives, not leaked absolute paths. The final scanner
uses the actual private-root pattern. A combined patch was rejected for targeting
CURRENT_STATUS.md twice and then reapplied with one update per path.
No missing audit input, identity discrepancy or scientific defect was repaired
or concealed to complete this task.

## Final diff inspection and residual uncertainty

Working diff and all additions have been inspected, with machine-readable
payloads fully parsed and hash-bound. Complete staged diff inspection covered
exactly 39 permitted paths, all staged bytes and no binary patch or foreign
addition; the 28 staged evidence hashes passed. Final re-staging of these
handoff notes and whitespace checks precede commit/push.
Only four existing documents and this 35-file dossier are in scope; no ZIP,
cache, extracted checkout or foreign path is staged. Protected scope is all
697 initial tracked paths outside
the four authorized documents, compared against `7201f788...` and the initial
local snapshot where applicable. The exempt ZIP SHA-256 is
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.

Hashes establish preserved bytes, not authenticity of historical execution.
That execution's unchecked-metadata limitations remain in its stdout. No current
hosted-CI success is claimed here. Independent review of the exact pushed
integration commit and full delta from accepted `80919666...` remains the single
next task after successful integration; Registry promotion and scientific claim
changes are both NONE.
