# Evidence

## Environment

- Task mode: STRICT; local branch codex/ringmin-editorial-review.
- Base: 7d257221d9034ca5f895f062e45e782d8e77b6c2, the current remote
  Paper II candidate at startup. Paper I source also matches remote main
  c26400b328c2f8fa338b588e61abb98266a265f9 and the frozen DCG package.
- Windows; Python 3.14.3 for build/scope/package scripts; pdfTeX
  3.141592653-2.6-1.40.28 (TeX Live 2025).
- Visual rendering uses bundled Python 3.12.14, pypdfium2 5.14.0 and Pillow
  12.3.0. No dependency installation or production code change.
- Original main and both existing Paper II worktrees were read only.
  Elevated final status inspection confirms the original main still has
  only its pre-existing untracked arXiv ZIP; both Paper II worktrees are clean.
  The registered prop7-journal-supplement checkout is absent; it was not recreated.

## Claim ledger

| Claim | Classification | Evidence | Independence / limitation |
|---|---|---|---|
| Exposition is easier to follow | Editorial assessment | Per-paper reports and complete prose diff | Judgment, not a measured reader study |
| Protected source content is preserved | Engineering fact | check_scope.py, baseline Git blobs, startup hashes, semantic diff review | Textual checks plus a separate assistant; not formal semantic proof |
| Both revised main PDFs compile with stable numbering | Engineering fact | Baseline/revised/repeated isolated builds and compare_builds.py | Local TeX environment only |
| Main PDFs repeat byte for byte | Engineering fact | Matching revised/repeat SHA-256 | Does not predict other TeX/font versions |
| S1/S2 and public/scientific assets are unchanged | Engineering fact | 835-file protected inventory; inner/outer package verifier | Hash identity does not establish mathematical truth |
| Mathematical results in the papers | Inherited exact theorems and finite certificates, with their original qualifications | Existing owning ledgers and proof/certificate sources | No new verification, certification or acceptance in this task |

The source check protects formal statements, definitions, remarks, proofs,
tables, mathematical environments and delimited formulas, labels/references,
citations, preambles, bibliography, disclosures, Paper I's appendices and
Paper II's entire lower-endpoint section. It does not pretend to parse all of
TeX. A separate assistant read the complete prose diff for meaning changes.
Its report is SCOPE_REVIEW.md. This is internal AI-assisted review, separate
from the human author and any ongoing independent mathematical review.

## Commands and actual results

All following task commands ran from the isolated repository root unless a
different working directory is stated. Every completed command below returned
exit 0; negative/failed attempts are recorded separately.

| Exact command | Material output | Property / limitation |
|---|---|---|
| git fetch origin main codex/paper-ii-journal-candidate | remote main 75a2f44..c26400b; candidate d925f85..7d25722 | Fetched current versions, no existing checkout changed |
| git switch -c codex/ringmin-editorial-review | Switched to a new branch | Local isolated branch, no remote write |
| python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py baseline | paper_i 19 pages, paper_ii 9 pages; zero final-log warnings after corrected detector | Three passes each, exact baseline sources, isolated temporary directories |
| python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py revised | paper_i 19 pages, paper_ii 9 pages; zero final-log warnings after prose layout repair | Three passes each; no supplement compilation |
| python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py repeat | Same page counts and exact revised PDF hashes; zero warnings | Separate temporary build directories |
| python ops/TASK-20261107__two_paper_editorial_review/compare_builds.py | 58/20 label numbers and 6/8 bibliography numbers unchanged; identical_repeat_pdf true for both | Auxiliary numbering and local repeat identity; page destinations may move |
| python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py deliver | Delivered only the two main PDFs and synchronized their build provenance | Checks current inputs/output hashes before writing |
| python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py export | 39 archive members | Local source bundle synchronization; S1/S2 copied unchanged |
| python -I -S paper_assets/paper_ii_journal/verify_package.py | PASS archive: 38 payload hashes; PASS candidate manifest: 26 payload hashes | Existing independent package checker; no mathematical assertion |
| python ops/TASK-20261107__two_paper_editorial_review/check_scope.py | Paper I: 19 protected environments, 249 delimited formulas, 16 math environments; Paper II: 14, 268, 11; 835 tracked protected files byte-identical | Six in-memory formula/proof/disclosure corruption controls detected |
| git apply --check --reverse --unidiff-zero ops/TASK-20261107__two_paper_editorial_review/MANUSCRIPT_DIFF.patch | No output | Stored patch matches the current manuscript delta; read-only check |
| python -I -S verify_package.py (fresh extracted archive directory) | PASS candidate manifest: 38 payload hashes | Portable package integrity; no TeX or arithmetic replay |
| git diff --check | No output | Tracked whitespace; additions separately checked |
| git status --short | Only the explicit task allowlist and this dossier before staging | Original ZIP is in the other checkout and never staged |

The initial comparison ran as an inline Python program, then was saved
unchanged as compare_builds.py and rerun. It checks the actual .aux files
from the ignored build area. The final build records retain command flags,
fixed SOURCE_DATE_EPOCH, compiler, input/output hashes and actual TeX system
input hashes without embedding machine paths. Recorder checks reject
undeclared local inputs or inputs outside the declared TeX distribution roots.
Logs and renders are kept only in the ignored local work area.

## Artifact and provenance checks

- Paper I main PDF: 19 pages, SHA-256
  c1a693f28e37bdfc0c0b2724a18204d71dc41a14adc4fd9d83b46009e6ed711c.
- Paper II main PDF: 9 pages, SHA-256
  deda77d01c02d33c7f921b9fedc13db78f7ebe6deda3c25cac7c683f1c929766.
- Current bundle hash and full payload inventory are bound by the synchronized
  paper_assets/paper_ii_journal/MANIFEST.json.
- Generation revision is the local task commit containing these sources and
  manifests. The base commit is the input revision, not the output revision.
- Paper I BUILD_MANIFEST.json is updated only for the actual current main build.
- Paper II BUILD_REPORT.json replaces only the main record. Supplement records
  retain their earlier values, compiler provenance and preserved-PDF policy.
  Added per-document notes explicitly distinguish fresh main from inherited
  S1/S2 records. No aggregate new supplement build is claimed.
- No public preprint PDF, frozen submission package, figure, table or certificate
  is regenerated. The local review bundle is synchronized because it contains
  the edited main source/PDF; it is not uploaded or submitted.
- All 19 Paper I pages and all 9 Paper II pages were visually inspected;
  PDF_I_REVIEW.md and PDF_II_REVIEW.md state methods and limitations.

## Failed checks and negative evidence

- Sandboxed git ls-remote failed with getaddrinfo thread error. Read-only
  GitHub connector succeeded; an authorized elevated normal fetch succeeded.
- Sandboxed Git commands in the new/older worktrees failed with cwd permission
  errors; elevated commands succeeded. The original checkout was never reset.
- Initial apply_patch could not create the dossier directory. Elevated writes
  were subsequently used only in the new authorized worktree.
- An overbroad log detector counted six info/package-loading lines in each
  baseline as warnings. It was narrowed to actual diagnostic prefixes and
  baseline compilation repeated: no real baseline warning.
- First revised Paper I build had one new overfull hbox, 52.93068pt at the
  historical reproduction paragraph. The prose sentence was shortened and
  both revised/repeat builds then had zero warnings.
- Preliminary math-span parsers in the two editorial checks misread the
  author's double-backslash spacing as a display opener. Parsers were corrected
  and controls rerun. The failed initial source-edit guard wrote nothing.
- Initial direct whitespace review caught extra EOF blank lines in the two
  new build audit helpers; they were removed and the check passed.
- Bundled PyMuPDF was unavailable; existing PDFium/Pillow supported rendering.
- The app thread inventory accepts at most 50 items; larger requests failed.
  No exhaustive live-chat inventory or completion of the external S2 review
  is asserted.

## Final diff inspection

The complete manuscript diff is MANUSCRIPT_DIFF.patch (zero context to avoid
structural blank-context whitespace in the stored patch), reproducible by:

    git diff --unified=0 7d257221d9034ca5f895f062e45e782d8e77b6c2 -- paper_assets/journal_dcg/ringmin_dcg.tex paper_assets/paper_ii_journal/main.tex

Per-paper reports record every edit cluster, examples, semantic caveats,
coverage of unchanged sections and author decisions. Task helpers are audit
instrumentation only; production code/tests/builders/checkers remain unchanged.
The complete tracked diff and new reports/helpers were read. All 21 dossier
files passed direct whitespace checks and all JSON files parsed; generated
hash inventories were checked programmatically against their bound files.
The staged inventory and staged whitespace check complete the final freeze. Commit integration outcome is reported
in the chat; no circular commit self-hash is embedded here.

## Residual uncertainty and skipped work

- No pytest, global bracket verifier, frontier verifier, aggregate mathematical
  replay or supplement compile was run: no scientific logic/input/proof changed,
  and the user expressly protects the concurrent review. Historical results
  quoted in manuscripts or inherited documents are not fresh task results.
- No hosted CI inspected for this local commit; no push is authorized.
- Proof validity, journal acceptance and the author's personal verification are
  not established by this editorial task.
- Paper I retains dated DCG-related provenance despite the author-supplied DAM
  identity. No live journal disposition is inferred or metadata rewritten.
- Paper II keeps its 3 November title-page date and existing AI disclosure.
  Endpoint-symbol density, the precise referent of introductory bounds,
  genuine-label terminology and historical AI-tool details remain in its report.
- The final sentence of Paper II Definition 1 now continues onto page 3.
  It remains readable; no proof/formula was changed to control pagination.
- All judgments of readability remain proposals for the author.

Exactly one next atomic task: author review of both editorial diffs and the
deferred wording/version decisions. No submission or new mathematical task
is started here.
