# Evidence

## Environment and identities

```text
repository_head=b1480803749e08197bce37442f0953c550e2a5e4
accepted_review_baseline=b1480803749e08197bce37442f0953c550e2a5e4
platform=Windows / PowerShell
python=3.14.3
dependency_source=existing local Python and bundled PDF runtime
symbolic_dependency=SymPy 1.14.0
latex=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
task_mode=STRICT
mathematical_source_commit=6c16af422d1cb38641c62d43b6e0e547921b9ba9
release_tag=v1.1.0-dcg-presubmission
release_commit=80919666c3c54f8ce20cf66c456d413f6a2c075f
version_doi=10.5281/zenodo.22849826
```

Live preflight: local HEAD, origin/main and remote main agree with the accepted
Registry row (State!A1:F2, status accepted, update 2026-09-26T18:55:35Z).
The Registry was only read. The later baseline is outside the frozen deposit.
The new patch is not automatically accepted.

## Claim ledger

| Claim | Classification | Evidence | Independence and limits |
|---|---|---|---|
| Release/DOI identity and citation | Observed provenance / engineering fact | Live Git tag, unchanged CFF and persisted Zenodo record | Documentary reconciliation; archived ZIP audit is not rerun |
| Source pin differs from archival and accepted baseline | Engineering fact | Full SHA identities and ancestry checks | No new acceptance decision |
| Existing finite brackets and seam scope | Inherited computer-certified finite result and exact theorem | Unchanged owning ledgers and protected inputs; required reruns recorded below | No new scientific conclusions; implementer checks are not independent review |
| Availability prose and bibliography updated | Editorial change | Complete diff, build and manuscript audit | No DCG submission or journal peer review |

## Commands and checks

All checks below were executed locally by the implementer. Git uses
command-scoped safe.directory, without persistent configuration changes.
The exact mathematical verifier is independent of production/generator;
rerunning its existing lineage is not a new independent review.

| Command/check actually run | Exit/result | Property and limits |
|---|---|---|
| `git status --short`, `git branch --show-current`, `git rev-parse HEAD origin/main` | 0; main; both SHAs equal base; only exempt ZIP untracked | Starting local state, not acceptance |
| `git ls-remote origin refs/heads/main refs/tags/v1.1.0-dcg-presubmission` | 0 on authorized retry; main = base, tag = release commit above | Live remote identity |
| Registry connector read `State!A1:F2` | accepted, base SHA, update 2026-09-26T18:55:35Z | Live read only; no new decision or Registry write |
| `python --version` | 0, `Python 3.14.3` | Runtime identity |
| `python -I -S verify_global_brackets.py --output ops/TASK-20260928__dcg_submission_compliance/global_brackets_verified.json` | 0, `PASS_GLOBAL_BRACKETS`, input binding PASS, 13 preserved files | Complete default verification of all twelve cases; --output only preserves the full report, without reducing scope |
| `python ops/TASK-20260919__journal_fixed_order_seam/check_exact.py --symbolic` | 0, `PASS: all requested bounded checks; analytic proof and independent review remain separate` | Existing exact/interval/symbolic checks; bounded checks do not replace the all-k analytic proof |
| `python paper_assets/journal_dcg/build.py` (authorized environment access) | 0, `Built ringmin_dcg.pdf: 19 pages; 0 overfull boxes; no unresolved references.` | Two pdflatex passes, no shell escape, normal PDF/manifest generation |
| Same build repeated | 0, identical PDF SHA-256 below | Local byte reproducibility, not cross-toolchain identity |
| `pdftoppm -r 85 -png paper_assets/journal_dcg/ringmin_dcg.pdf reproducibility/.work/journal_dcg/page` | 0, 19 PNG pages | Rendering for visual review |
| Bundled Python: `ops/TASK-20260919__finite_journal_manuscript/inspect_pdf.py` | 0, `PASS: 19 Poppler pages, extracted text without unresolved references/replacement characters.` | Existing read-only PDF extraction/contact-sheet audit; images inspected separately |
| `pdfinfo paper_assets/journal_dcg/ringmin_dcg.pdf` | 0, 19 A4 pages, PDF 1.7, 402481 bytes, no JavaScript/encryption | PDF metadata; not accessibility certification |
| `python ops/TASK-20260928__dcg_submission_compliance/check_manuscript.py --preflight-hashes reproducibility/.work/dcg_submission_compliance/preflight_hashes.json` | 0, full PASS summary below | Current adaptation of the preserved historical audit, plus raw-byte preflight comparison |
| `git diff --exit-code 6c16af422d1cb38641c62d43b6e0e547921b9ba9 80919666c3c54f8ce20cf66c456d413f6a2c075f -- verify_global_brackets.py reproducibility/global_brackets` | 0, no output | Same verifier and computational inputs at source pin and archived release |
| `git merge-base --is-ancestor` for source pin -> release and release -> base, within current audit | 0 for both | Three distinct sequential identities |
| Recursive full JSON comparison with the preserved 2026-09-19 revision report | PASS; only `/seconds` differs: 3.743162000027951 -> 3.743753199989442 | Every other field compared, including all per-case records |
| Relative-link check over the five changed current Markdown documents | 0, `PASS: 54 relative documentation links resolve` | Local file targets; no fresh venue-policy or linked-literature review |
| `git diff --check` | 0, no findings | Tracked whitespace; new additions also checked directly by current audit |

The bundled Python executable and Poppler were resolved through
`load_workspace_dependencies` (bundle 26.923.10815); no package was installed.
The existing `check_exact.py` and PDF inspection helper remain untouched.

Exact current manuscript audit output:

```text
PASS: 728 preflight protected files byte-identical (including exempt ZIP).
PASS: 27 seam displays preserved, 21 tags, six vectors, 12 endpoint and coverage rows.
PASS: abstract 184 whitespace words; six keywords; all declarations; resolved source references.
PASS: complete baseline TeX recovered outside three editorial blocks; entire seam appendix unchanged.
PASS: six resolved bibliography entries; CFF/Zenodo citation; three distinct provenance identities and ancestry.
PASS: fresh full report bound to twelve certificate rows and positive margins; verifier and artifact hashes.
PASS: protected tracked paths and exempt ZIP unchanged; only allowed task paths; all text UTF-8/whitespace.
LIMIT: transcription and scope audit, not independent mathematical review or hosted CI.
```

The full verifier reports 908 angle intervals, 47 witnesses, 540 central
tangencies, 3,004 outer pairs, 6,008 angular inequalities, 268,648 explicit
classes and 3,374,988,556 covered classes. The
[fresh full report](global_brackets_verified.json) is retained separately from
the original evidence. Its endpoints/counts/margins agree with the unchanged
certificate and prior report. No original result artifact is overwritten.

The seam checker passes six rational bridges with independent arctangent checks,
128 rank cycles, 128 parity-growth matches, 30,976 directed fan identities,
512 exact boundary comparisons (k=1..256), twelve interval roots, 670 positive
directed slacks and three negative seams. SymPy checks original-kernel
derivatives, three pocket identities, threshold algebra, arcsine and pi bounds.

The historical manuscript audit is frozen evidence. Its five-entry bibliography,
no-deposit wording, older edit scope and A.5-addition gates describe a different
task. The new copy retains its transcription/report/table checks, replaces those
obsolete editorial gates and requires equality of the entire baseline TeX after
removing only the three authorized editorial blocks. It requires exact equality
of the complete seam appendix, a stricter preservation gate for this task.

## Artifact and provenance checks

Normal source command: `python paper_assets/journal_dcg/build.py`. Generated
PDF and manifest belong to the task commit containing them. The frozen DOI
does not include this editorial patch. Byte reproducibility is toolchain-bound.

The generated [manifest](../../paper_assets/journal_dcg/BUILD_MANIFEST.json)
records source hashes, protected mathematical input hashes, citation-source
hashes and all three distinct identities. Its editorial revision baseline is
updated by the builder; the computational source pin is unchanged. No manifest
field is hand-edited. SOURCE_DATE_EPOCH=1789776000 and the original template,
font/toolchain and PDF identifier suppression remain unchanged.

Final PDF SHA-256 (two successful builds):

```text
f5b3eed1374afe2f75b6195d8806825ae512dcf5eb3ad46cbf8a7ae07112e284
```

Visual inspection covered all 19 pages in four contact sheets and enlarged
pages 9-11 (reproduction and declarations) and 19 (archival bibliography).
No clipping, overlap or missing glyph was observed. Both log checks and text
extraction show no unresolved reference. The log has no overfull/underfull box
or LaTeX/package warning; the match for `Rerun` is only a package description.
The additional provenance increases pagination from 18 to 19; the final page
continues the bibliography. The title-page preparation date is preserved.

Citation metadata come from unchanged [CITATION.cff](../../CITATION.cff) and the
persisted [Zenodo record](../TASK-20260926__archive_evidence_integration/evidence/zenodo_record.json).
The software title and creator agree. The record supplies publication date
2026-09-19, year 2026 and deposited version `v1.1.0-dcg-presubmission`; CFF
omits the literal leading `v`, as already documented in the archived comparison.
The inserted bibliography entry is:

> Falconi, M.: Ringmin: minimum central circle software and exact finite
> certificates. Version v1.1.0-dcg-presubmission. Zenodo (2026).
> https://doi.org/10.5281/zenodo.22849826

The paper cites this entry in both reproduction and availability text. No
metadata, ORCID, new release/tag or DOI was invented. CFF and its preferred
finite-paper citation are unchanged. This task uses the preserved Zenodo record;
it does not repeat the historical ZIP-to-Git archival audit or claim a fresh
Zenodo HTTP acquisition.

## Failed checks and negative evidence

See append-only TASK_LOG for the initial prompt SHA conflict, sandbox connection
failure, corrected template lookup, rejected duplicate-path patch and failed
audit-copy preparation. The latter failed before writing its output. Two
sandbox builds exited 1 because LaTeX could not access AppData; authorized
same-command retries passed. Git also emits an unreadable global-ignore warning
in the sandbox; explicit tracked/index checks and the exempt ZIP hash cover the
task scope. No auto-review rejection occurred. No mathematical check failed.
Sandbox staging initially failed on index.lock and passed with tool-authorized
access. The first staged-byte assertion rejected the publication ledger's Git
CRLF-to-LF normalization; explicit text-only normalization resolved that check.
The PDF text-converter configured in Git lacked helper commands, so full-diff
inspection used `--no-textconv`. The PDF itself was checked by hash, extraction
and rendering, independently of that converter. These are environment/check
limitations, not mathematical or artifact changes.

## Final diff inspection

All nine modified existing paths are explicitly allowlisted by the current
audit; five new dossier files contain task-local status, log, evidence, the
adapted audit and its fresh full verifier report. No thematic claim is duplicated:
only the owning publication ledger's obsolete archival wording changes; the
index and mathematical ledgers remain unchanged.

The full tracked text diff and new checker were read; the complete report was
parsed, bound to the certificate and recursively compared with prior evidence.
All new Markdown is reviewed in full and all new text receives direct UTF-8,
final-newline and trailing-whitespace checks. PDF review uses rendered pages.

Protected scope is all 727 initial tracked paths outside the nine allowed paths,
plus the exempt ZIP. Raw SHA-256 comparison with the pre-edit snapshot passes
for all 728 files. It includes seam appendix, both table inputs, proof notes,
verifiers, tests, certificate/original evidence, src/results, public arXiv v1/v2,
asymptotic sequel, CFF and historical dossiers. The optional raw snapshot stays
in ignored local work storage; the audit's ordinary Git-based checks are portable.
Exempt ZIP SHA-256:

```text
e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db
```

Only the regenerated DCG PDF/manifest change among generated publication assets.
The main TeX preserves every byte of textual content outside the three permitted
editorial blocks after normalizing checkout newlines. Complete staged inspection
covered all 14 paths: all staged content matches the inspected working content
(only publication-ledger CRLF normalization), all JSON parses, the entire fresh
report comparison differs only in /seconds, and the PDF hash matches the inspected
output. `git diff --cached --no-textconv --check` passed with no findings;
`git diff --exit-code` confirmed no unstaged tracked change at that check.
The full `--no-textconv` staged diff includes all 14 sections and the binary PDF.
Final dossier-only updates are re-staged and checked before commit. The final
handoff records exact commit, normal-push result, remote SHA and remaining tree
state, avoiding a circular self-commit identity in this document.

## Residual uncertainty

Local editorial checks and reproduction do not constitute independent review,
journal peer review, proof-assistant formalization or historical execution
attestation. No hosted CI success is claimed.
No fresh venue-guideline review, journal submission, cover letter or external
peer review occurs. The finite scope, all numerical endpoints, counts and
floating quantifiers remain unchanged. Registry baseline stays at the initial
accepted SHA; this implementation is READY_FOR_REVIEW only after its local gates.

Exactly one next atomic task: independent review of the exact submission-compliance
commit; if accepted, prepare the final DCG submission package and cover letter.
