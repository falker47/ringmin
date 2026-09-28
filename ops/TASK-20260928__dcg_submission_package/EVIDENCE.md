# Evidence

## Environment and baseline

```text
repository=falker47/ringmin
repository_head_at_start=6749d6b165f982136117481be322c8beaec223ce
accepted_registry_baseline=6749d6b165f982136117481be322c8beaec223ce
registry_updated_at_utc=2026-09-28T09:15:13Z
platform=Windows; PowerShell
python=3.14.3
compiler=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
task_mode=STRICT
```

Startup local HEAD, cached origin/main, live remote HEAD/main and the Registry
agreed. The bounded Registry read is preserved in [registry_state.json](registry_state.json);
the last read returned the same row. Registry access was read-only. All Git
commands requiring it used a per-command `safe.directory` set to the resolved
repository root; no global Git configuration was changed. Commands below are
root-relative, with that machine-local option elided.

Only the existing untracked arXiv ZIP was exempted, explicitly by the user in
this task. Its SHA-256 remains
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.
It is excluded from package, staging and commit. No other unrelated changes
were present. A pre-edit raw-byte snapshot covered 742 files; 740 are protected,
after excluding only current status and the roadmap. The local snapshot and
raw TeX logs/renders remain in ignored `reproducibility/.work/dcg_submission_package/`.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Five packaged manuscript files equal accepted source/PDF | Engineering fact | Git blob comparisons, raw SHA-256, five empty no-index diffs | Exact byte comparison; not a new mathematical review |
| Package compiles without repository inputs | Engineering fact | Two clean external builds, recorder input checks | Uses installed standard TeX distribution; not a journal server test |
| Compiled PDF equals accepted PDF | Engineering fact | Both build hashes match accepted Git PDF | Local toolchain identity only |
| Package inventory and manifest are deterministic | Engineering fact | Fixed ZIP order/times/modes, stored entries, sorted JSON, raw-byte checksums | No scientific code/certificates packaged |
| Abstract/keywords/declarations and source transcriptions retained | Engineering fact | Existing audit plus package metadata checks and byte identity | Prior global-verifier report is inherited evidence |
| Journal instructions/portal observations | Dated observed facts | Live publisher/portal links below, checked 2026-09-28 | Pages/form can change before human upload |
| Existing mathematical statements | Inherited exact theorems and computer-certified finite results, as classified in accepted manuscript | Unchanged accepted files and their original evidence chain | This task neither extends nor re-certifies them |

## Commands and observed results

| Command/check | Exit/result | Property checked and limits |
|---|---|---|
| `git status --short`; `git rev-parse HEAD refs/remotes/origin/main`; `git remote -v` | 0 with safe.directory; only exempt ZIP untracked | Local baseline/branch context |
| `git ls-remote origin HEAD refs/heads/main` | 0 on authorized network retry; both equal accepted baseline | Live remote identity |
| Registry connector read `State!A1:F2` | accepted baseline above; repeated unchanged | Live acceptance record, not a new decision |
| `python ops/TASK-20260928__dcg_submission_compliance/check_manuscript.py` | 0; six PASS lines and LIMIT in [stdout](manuscript_audit.txt) | Existing audit run before adding package paths, because its scope whitelist belongs to the prior task |
| `python ops/TASK-20260928__dcg_submission_package/package_submission.py --build` | 0; `PASS_PACKAGE` | Builds/copies only this package and records local evidence |
| `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder ringmin_dcg.tex` | 0 four times; 19 pages in each completed build | Two passes in each of two fresh external directories; source ZIP entries only |
| `pdfinfo paper_assets/dcg_submission/ringmin_dcg.pdf` | 0; 19 A4 pages, 402481 bytes, PDF 1.7, no encryption or JavaScript | PDF structure, not proof correctness |
| `pdftoppm -r 60 -png paper_assets/dcg_submission/ringmin_dcg.pdf reproducibility/.work/dcg_submission_package/page` | 0; all 19 pages rendered | Visual inspection of all five contact sheets: no observed clipping/overlap |
| `python ops/TASK-20260928__dcg_submission_package/package_submission.py` | 0; [PASS report](verification_report.json) | 11 package files, 10 checksums, 5 accepted copies, 740 protected files; direct whitespace check includes untracked text |
| `git diff --no-index -- paper_assets/journal_dcg/NAME paper_assets/dcg_submission/NAME` for each of the four TeX files and PDF | 0 for all five; empty diffs | Complete new manuscript copies inspected against their accepted sources |
| `git diff --check` | 0; no whitespace errors | Tracked diff; separate checker covers untracked additions |

The existing audit reports 27 seam displays, 21 tags, six vectors, 12 endpoint
and coverage rows, 184 whitespace words, six keywords, five declarations and
six resolved bibliography entries. Its line saying "fresh full report" belongs
to the unchanged historical checker: this execution checks the report saved
in the prior dossier, and does not rerun the mathematical verifier. The final
package keeps every audited manuscript byte. No unit suite, global certificate
verifier or symbolic theorem checker was rerun, because there is no change to
their scientific inputs or implementation. No hosted CI claim is made.

The fresh package checks also confirm MSC `52C26, 52C15, 05C85, 90C27`, the
corresponding-author line, Statements and Declarations, the data/code
availability paragraph with DOI and bibliography citation, and explicit
substantive ChatGPT/Codex disclosure. The accepted prose, including dated
provenance statements, remains verbatim. Cover letter and checklist were read
in full for stale preparation wording, invented claims and private data.

## Artifact identity and reproducibility

Package: `paper_assets/dcg_submission/` (11 files). The deterministic source
ZIP contains only `bracket_rows.tex`, `coverage_rows.tex`, `ringmin_dcg.tex`,
`seam_appendix.tex`, in that order, at ZIP root. No custom class/style, external
figure or bibliography database is needed. The archive DOI is cited without
duplicating scientific code or certificate data as supplements.

Full source/payload hashes and byte sizes are in
[SUBMISSION_MANIFEST.json](../../paper_assets/dcg_submission/SUBMISSION_MANIFEST.json).
[SHA256SUMS](../../paper_assets/dcg_submission/SHA256SUMS) hashes every package
file except itself, including the manifest. Anchor hashes:

```text
manifest_sha256=9a4a9fafec1dcd855702c3402acdd645dd05b064468e86859d3bbff7824ed01f
sha256sums_sha256=10afe360c4bc9963e52ea66da5ff78a13b1fb20010b01364cc7ffa6502631e1a
source_zip_sha256=d70173624d1e1eb748b71fe39a31fb0f865d65b51e4e96f4eed27e649c8d6b92
pdf_sha256=f5b3eed1374afe2f75b6195d8806825ae512dcf5eb3ad46cbf8a7ae07112e284
```

Generation source: [package_submission.py](package_submission.py), invoked
with `--build`. Generation commit is the task commit containing these files;
resolve it with `git log -- paper_assets/dcg_submission/SUBMISSION_MANIFEST.json`.
Input commit is the accepted baseline above. The source ZIP uses uncompressed
entries with fixed timestamps and modes; the manifest uses sorted keys, fixed
preparation metadata and UTF-8/LF. The final checker verifies deterministic
serialization and re-creates identical ZIP bytes without executing TeX again.

[build_report.json](build_report.json) records all four compiler exit codes,
each final PDF hash, pages, empty unresolved/overfull lists, local inputs and
system input basenames. Both builds used `SOURCE_DATE_EPOCH=1789776000`,
`FORCE_SOURCE_DATE=1`, only the current directory plus standard TeX search,
and an empty personal TeX tree. Recorder inputs were checked against the
repository root; none came from it. Temporary build directories were removed
after verification. Other TeX/font versions may produce different PDF bytes.

## Live journal observations and human fields

Checked the live [submission guidelines](https://link.springer.com/journal/454/submission-guidelines)
against the accepted preparation record. No material change was found to the
requirements enumerated in the [upload checklist](../../paper_assets/dcg_submission/UPLOAD_CHECKLIST.md);
no template migration is mandatory. The linked
[editorial board](https://link.springer.com/journal/454/editorial-board) has
three Editors-in-Chief while the guideline list has two. The public
[Editorial Manager page](https://www.editorialmanager.com/dcge/default.aspx)
displayed a development warning. These observations are preserved for the
human uploader; they do not prevent assembling and reviewing the exact package.

The author must privately complete contact/address/telephone/fax fields as
requested, choose a current Co-Editor-in-Chief, supply an ORCID only if real
and available, and personally confirm the live form's author attestations.
No home address, phone number, invented ORCID, portal login, editor selection
or unverified exclusive-submission assertion is in the package. Public author
name, city/country and email are copied from the accepted manuscript.

## Failed checks and recovery

Initial Git ownership/network and TeX host-profile restrictions were resolved
by a per-command safe.directory option and authorized escalation. Git's
sandbox warning about an unreadable global ignore file was nonfatal; recorded
scope and raw-byte checks passed. One Windows glob form and one web link
reference were corrected. One patch was rejected for duplicate target
operations before applying edits; its corrected retry succeeded. These
attempts are recorded in TASK_LOG.md; no failed compilation or altered
scientific source was hidden.

## Final diff inspection and review boundary

Only `CURRENT_STATUS.md` and the finite-submission section of the roadmap
change among pre-existing tracked files. All new files lie in the package or
this dossier. Full accepted-copy no-index diffs are empty. Authored text,
manifest, reports, source ZIP membership and PDF pages were inspected.
Direct UTF-8/whitespace validation includes every new text file; binary files
are bound by hashes. Protected publication, mathematical, scientific-code,
certificate and verifier paths remain byte-identical, as does the exempt ZIP.
No stable claim changed, so no thematic ledger or canonical index was edited.

Scoped staging, complete staged inspection and `git diff --cached --check`
precede the normal commit/push under AGENTS.md section 3. The final response
records the observed integration result and exact SHA; this dossier does not
claim a future push already succeeded. Repository acceptance, hosted CI and
journal peer review remain separate. No Editorial Manager form was submitted.

Staging included exactly 21 inspected paths. Every index blob matched its
fully inspected working-file bytes, no unstaged tracked delta remained, and
the exempt ZIP was absent. `git diff --cached --check` exited 0. A display-only
PDF text converter reported missing helper programs during a binary diff;
raw blob comparisons passed, and final diff capture disables text conversion
and external diff drivers. No PDF bytes were changed by this warning.

Exactly one next atomic task: independent review of the exact committed
submission package; if accepted, human upload through Editorial Manager.
