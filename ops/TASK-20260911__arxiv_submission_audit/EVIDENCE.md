# Evidence

## Environment and identity

```text
reviewed_repository_head=3beb8d70c5b3748d370a92855847bdf574e5a14f
branch=main
platform=Windows / PowerShell
python=3.14.3
pypdf=6.14.2
tex=pdfTeX 1.40.28 / TinyTeX TeX Live 2025
latex=2025-11-01
l3=2026-01-19
format=2026-02-13
source_date_epoch=1789084800
mode=STRICT
```

The reviewed supplement is public at that immutable commit. Current task
integration is local only under the user's no-external-action instruction.
Prior final-packet runs are historical; fresh root and subagent runs below
are identified separately. No externally accepted baseline or hosted CI
status was changed or inferred. No installation was performed.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Existing global limit, LP characterization and block recovery | Exact theorems audited against actual proof notes | SCIENTIFIC_AUDIT.md, complete manuscript read, source rederivation | Separate internal reviewer; not external acceptance; bounded checkers do not prove infinite quantifiers |
| Existing explicit endpoints/fixed-order table | Exact theorems/corollaries and directed enclosures | ENDPOINT_FINITE_AUDIT.md, actual sources and fresh exact checkers | Separate internal reviewer; full dependency coverage explicitly scoped |
| Existing finite optima 3..14 | Numerical computer-certified finite results under inherited guards, independently reproduced locally | Fresh full verify.py output below, independently rehashed saved evidence | No production import; does not regenerate excluded orders or independently prove all-order interval error guards |
| One-file bundle compiles and matches candidate | Local engineering fact | clean_compile.ps1, check_bundle.py, BUNDLE_CHECK.json, PAGE_COMPARISON.json | Direct TeX compilation separate from candidate build.py; same installed TeX tree |
| Bibliographic fields and current arXiv guidance | Primary-source checked metadata | BIBLIOGRAPHY_ARXIV_AUDIT.md | Live web/publisher/GitHub API checks; no exhaustive novelty review |

Seven IMPORTANT corrections preserve existing hypotheses, definitions and
verification limits. No new scientific conclusion or finite optimum is
introduced. No owning knowledge ledger or proof note needs modification.

## Fresh root commands and exact results

All successful commands here exited 0. For pdflatex runtime access only,
commands were run outside the filesystem sandbox after tool approval.
The engine path is represented by its executable name to avoid storing a
machine-specific absolute path; the candidate build supplied its actual
installed path through the documented --engine option.

| Command | Material result | Checked property / limitation |
|---|---|---|
| `python --version` | `Python 3.14.3` | Local interpreter, existing installed dependencies |
| `pdflatex --version` | `pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)` | Actual local engine, not exact arXiv snapshot |
| `python scripts/frontier_logs.py restore` | `PASS 12 exact log archives; 9649682 original bytes; restored/existing readback identical` | Original saved evidence integrity; no search regeneration |
| `python verify.py --start 3 --stop 14` | All 12 sizes incumbent/local/frontier PASS, full output below | Full saved-frontier mode, not smoke; original numerical assumptions retained |
| `python paper_assets/v2/build.py --engine <installed-pdflatex>` | `PASS versioned PDF built; source/PDF/build hashes recorded` | Two-pass synchronized candidate PDF/manifest; publication math unchanged |
| `& ops/TASK-20260911__arxiv_submission_audit/clean_compile.ps1` | Three direct TeX passes exit 0; stable aux/out; no final warning | Fresh sole-source root, shell escape off, no Python compilation dependency |
| `python ops/TASK-20260911__arxiv_submission_audit/check_bundle.py <clean-directory>` | One source, 20 unique labels, 9 bibliography keys, 108 TeX-system inputs; 9 page contents/metadata match; 16 embedded fonts; no active content | Explicit fail-closed requirements, actual PDF objects and recorder inputs; not a general TeX security scanner |
| `pdfinfo <clean-directory>/ringmin_v2.pdf` | 9 letter pages, PDF 1.7, 333577 bytes; correct title/author; no forms, JavaScript or encryption | Independent Poppler PDF inspection |
| `pdftoppm -r 110 -png <clean-directory>/ringmin_v2.pdf <clean-directory>/page` | Exit 0; 9 PNGs | Every page visually inspected by root |
| `pdftoppm -r 110 -png paper_assets/v2/ringmin_v2.pdf reproducibility/.work/paper-v2/arxiv-final` | Exit 0; all 9 PNG pairs byte-identical | Complete candidate/clean visual equivalence |
| Source/metadata expansion and comparison | `PASS metadata abstract matches TeX after standard macro expansion: 1502 ASCII characters` | Full abstract copied without custom macros or malformed concatenated control words |

`<clean-directory>` is the fresh directory returned by clean_compile.ps1.
The final executed directory was
`reproducibility/.work/arxiv-clean-1523dfe3b87845d59bb0b7160993dade`.
It contained exactly ringmin_v2.tex before the first TeX invocation. Its
first transcript reports no existing aux file. Final aux/out hashes stabilized
by pass three; pass-2 and pass-3 transcripts are identical and warning-free.
The final log has no unresolved references/citations, duplicate labels,
missing glyphs, package warnings, or overfull/underfull boxes.

Exact full-verifier output:

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

Fresh separate-subagent exact checkers and their exact commands/results are
in SCIENTIFIC_AUDIT.md and ENDPOINT_FINITE_AUDIT.md. They cover line recovery,
1119 LP inequalities/18 corrupt-certificate rejections, 30034 small block
orders, all explicit upper inputs, lower width optimum and fixed-order
identities. The lower width checker intentionally rejects -O with exit 1;
this is a successful fail-closed control, not an ordinary PASS run. A separate
stdlib audit verified 12 archive/log hash pairs, 9649682 decoded bytes and
47 distinct canonical retained orders. The packaging reviewer also ran
check_bundle.py with -O: exit 0, byte-identical BUNDLE_CHECK.json, and checked
all three BUILD_MANIFEST input/output hashes.

## Artifact provenance and visual inspection

The only uploaded file is the unchanged byte copy of final candidate TeX,
SHA-256 `189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a`.
Candidate PDF SHA-256:
`c3fc42c1f8796d86938260dc7764277458982306315668d244a94686bc9f3ef9`.
Clean PDF SHA-256:
`2d3deef7df68e4ef69353fed17d8c4e15577402c88eebed5a93b6fd3ebc23b3b`.
The candidate and clean PDFs differ only in their sole trailer /ID arrays;
a complete byte comparison after normalizing that field proves this.
Fixed UTC metadata is identical. BUNDLE_CHECK.json records all 108 TeX input
hashes and all 16 embedded font-program hashes without local absolute paths.
PAGE_COMPARISON.json records hashes of every rendered page and visual coverage.
ARXIV_MANIFEST.json and ARXIV_METADATA.json remain outside the source bundle.

Page-by-page root inspection:

| Page | Material content checked | Result |
|---|---|---|
| 1 | Visible title/author/date, complete abstract, scope and shelf correction | Readable, no clipping; strict slab hypothesis explicit |
| 2 | Pair kernel, line recurrence, closing lemma and angular squeeze | All radicals/inequality directions/equation numbers legible |
| 3 | Existence proof, actual labels, quantization | Complete text and consistent symbols; no dropped proof lines |
| 4 | Balanced LP, boxed theorem and directed arithmetic | Box and fractions fit; no unresolved references |
| 5 | General block theorem, integer construction and explicit g/G_m | Correct normalization and predecessor; long bound fits |
| 6 | Full geometry, exact upper inputs and fourth saving | Integral, rational brackets and decrement denominator clear |
| 7 | Lower endpoint definitions/enclosure/proof, fixed-order introduction | Decimal endpoints and limiting order match source |
| 8 | Complete six-row table, numerical-guard qualification, pinned supplement, commands and AI disclosure | Table, long SHA and prose all fit; no external-acceptance claim |
| 9 | All 9 bibliography entries and intended URLs | Wrapping readable, complete authors/titles/pages and pinned reference |

Compared with starting HEAD, mathematical values, equation numbering, the
fixed-order table, theorem statements and substantive conclusions remain
unchanged; the abstract now includes the existing restriction, and body
notation/limitations/provenance are clarified. Pagination stays nine pages
although added definitions and removed transient status lines reflow text.

## Failed checks and negative evidence

- Initial unqualified Git reads failed on sandbox ownership. A process-local
  safe.directory override succeeded; no global Git setting changed.
- Initial sandbox pdflatex --version could not resolve the AppData long name.
  Tool-approved local execution succeeded; there was no approval rejection.
- The new hygiene scanner initially mistook the `s:/` in `https://` for a
  Windows drive path and exited 1. The drive regex was corrected to require
  a word boundary. No actual machine path was found in the source.
- The first recorder audit then rejected TinyTeX's distribution-root texmf.cnf.
  It was inspected and narrowly admitted only beside an actual texmf-dist
  directory. All recorded inputs were rechecked successfully, including -O.
- A draft multi-file patch combining delete/add of CURRENT_STATUS was rejected
  atomically; another evidence append had mismatched context. Neither changed
  any file. Corrected writes were inspected after application.
- An intermediate clean build passed before removal of transient no-submission
  text. The final source was subsequently rebuilt and all affected gates
  repeated; only the final hashes above govern this handoff.

## Scope limits and skipped checks

No new research, original exhaustive enumeration, expanded finite scope,
new all-n inference, dependency install, hosted CI inspection or external
acceptance decision occurred. The existing test suite was not rerun because
production, verifier and test code are unchanged; its prior 15-pass result
remains historical only. Fresh full verifier and specific existing exact
checkers are the proportionate scientific gates for this manuscript audit.
The local TL2025 package tree is newer than arXiv's 2025-08-03 snapshot.
Actual arXiv processing, metadata confirmation and page-by-page server PDF
inspection remain manual. Optional bibliography/date observations are recorded
in ARXIV_SUBMISSION.md; no manuscript blocker remains.

## Final diff inspection and integration

Final complete diff, additions, UTF-8/whitespace, link and protected-path
results are appended after their execution below. The current user instruction
forbids external actions, so the authorized integration is a local commit
without push. Mathematical acceptance is still independently pending.

### Executed final pre-stage checks

- Complete tracked diff inspected: CURRENT_STATUS and v2 source/README/build
  manifest only; PDF checked through complete page/object/byte comparisons.
- Every addition inspected in full, including the copied 581-line TeX,
  both task scripts, metadata, JSON reports, handoff and all reviewer records.
- Explicit direct Python check over all changed and untracked paths exited 0:
  `PASS 20 expected task paths; 19 full UTF-8 text checks; 22 local links;
  no trailing whitespace or actual machine paths`.
- All JSON parsed; actual upload file count, size and SHA-256 matched manifest.
  Plain-text metadata was derived from decoded JSON to avoid copying doubled
  JSON backslashes into the arXiv abstract field.
- `git diff --check` exited 0. A base-commit path-scoped diff over AGENTS,
  review protocol, index, research, knowledge, results, src, scripts, verifier,
  CITATION, REPORT and all non-v2 paper assets returned no paths, exit 0.
- The blanket final path scanner first matched the checker's own literal
  detector strings and exited 1. It was narrowed to concrete absolute path
  syntax; source and recorded outputs contain no actual machine paths. This
  was an audit-script false positive, not a source-bundle finding.
- No stable claim was duplicated into a thematic ledger. The roadmap remains
  unchanged because this task made no scientific priority change.

### Executed staged review

`git add` of the 20 explicit inspected paths exited 0. Staged status and
complete content were reviewed; an exact blob comparison confirmed every
staged file equals the fully inspected working bytes, allowing only Git's
CRLF/LF conversion. `git diff --cached --check` exited 0, and no unstaged
delta remained. Final documentation additions are inspected and restaged
before the local commit. Its containing SHA and post-commit status are
reported in the final response; no push will be attempted.
