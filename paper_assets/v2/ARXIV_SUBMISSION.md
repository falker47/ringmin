# arXiv v2 replacement handoff

**ARXIV_READY** for the author's manual replacement workflow after the STRICT
audit of 2026-09-11. This is local submission preparation, not arXiv processing
or external mathematical acceptance. No submission, release or push occurred.
No new scientific conclusion was introduced.

## Exact upload inventory

Upload only [arxiv_submission/ringmin_v2.tex](arxiv_submission/ringmin_v2.tex),
at the root of the submission. The directory contains this single file:

| Filename | Bytes | SHA-256 |
|---|---:|---|
| `ringmin_v2.tex` | 28286 | `189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a` |

The bibliography is inline. There are no external inputs, figures or custom
styles/fonts. Do not upload generated PDF, Python/PowerShell, audit records,
metadata/manifest JSON, auxiliaries, logs or old v1 assets.
[ARXIV_MANIFEST.json](ARXIV_MANIFEST.json) records exact byte hashes; Git EOL
conversion in another checkout can change text hashes. The scientific
supplement is publicly pinned to `3beb8d70c5b3748d370a92855847bdf574e5a14f`.

## All findings

No BLOCKER remains. All IMPORTANT findings were corrected and re-reviewed.

| ID | Severity | Finding | Final status |
|---|---|---|---|
| SCI-1 | IMPORTANT | Abstract omitted the strict slab-length hypothesis. | Corrected: `T<1-alpha`, with `0<=alpha<1`, is explicit. |
| SCI-2 | IMPORTANT | Shelf wording doubled the physical center span. | Corrected with `2(max x_i-min x_i)`. |
| SCI-3 | IMPORTANT | The block proof used undefined `g` and `G_m`. | Corrected using the existing maximum and empirical-sum definitions. |
| EF-1 | IMPORTANT | Finite verification could obscure inherited numerical guards. | Corrected: saved frontier/coverage checks are distinguished from interval evaluation of every excluded order. No wrong optimum was found. |
| BIB-01 | IMPORTANT | PDF title differed from the visible title. | Corrected; source, PDF and proposed metadata agree. |
| BIB-02 | IMPORTANT | Some supplement references lacked an immutable complete snapshot. | Corrected with a verified public commit containing every cited path. |
| BIB-03 | IMPORTANT | Two transient no-submission statements would become stale on upload. | Removed; AI disclosure and review boundaries retained. |
| BIB-04 | OPTIONAL | Supnick DOI absent. | Not changed: existing citation is correct; verified DOI `10.2307/1970124` is optional. |
| META-1 | OPTIONAL | Public v1 displays a June submission date with a `2607` identifier. | External inconsistency recorded, not corrected or used to infer another identity/date. The paper cites the verified year only. |

Detailed coverage and primary-source links:
[scientific audit](../../ops/TASK-20260911__arxiv_submission_audit/SCIENTIFIC_AUDIT.md),
[endpoint/finite audit](../../ops/TASK-20260911__arxiv_submission_audit/ENDPOINT_FINITE_AUDIT.md),
[bibliography/arXiv audit](../../ops/TASK-20260911__arxiv_submission_audit/BIBLIOGRAPHY_ARXIV_AUDIT.md).
These are separate internal reviews, not external acceptance.

## Clean compilation and PDF

Actual clean-build command from repository root:

```powershell
& ops/TASK-20260911__arxiv_submission_audit/clean_compile.ps1
```

It creates a fresh temporary directory containing only the upload TeX,
verifies its hash, changes to that root, and invokes directly:

```text
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ringmin_v2.tex
```

**Three passes, each exit 0**, stabilized .aux/.out; no unresolved references,
duplicate labels, missing glyphs, package warnings or overfull/underfull boxes.
No Python is required to compile the bundle. Local environment: pdfTeX
1.40.28 / TinyTeX TeX Live 2025; LaTeX2e 2025-11-01, L3 2026-01-19,
format 2026-02-13. All 108 external recorded inputs belong to the TeX system.

Every clean PDF page was visually inspected. The final nine pages match the
corrected candidate in text, painting instructions, dimensions, font programs,
metadata and PNG bytes. Both PDFs are 333,577 bytes; only their trailer IDs
differ. There are 16 embedded scalable Type 1 Latin Modern fonts, five intended
HTTPS destinations, no JavaScript, attachments, forms or active actions.
The manuscript has one table, 11 numbered equations, nine bibliography entries,
20 unique labels and no figures.

- Candidate PDF SHA-256: `c3fc42c1f8796d86938260dc7764277458982306315668d244a94686bc9f3ef9`.
- Clean PDF SHA-256: `2d3deef7df68e4ef69353fed17d8c4e15577402c88eebed5a93b6fd3ebc23b3b`.
- [Dependency/font/object evidence](../../ops/TASK-20260911__arxiv_submission_audit/BUNDLE_CHECK.json).

[arXiv currently defaults to TeX Live 2025](https://info.arxiv.org/help/faq/texlive.html),
frozen at 2025-08-03. The local tree is newer; this task did not execute the
exact frozen server image. The source uses standard supported packages/fonts,
but the server-produced PDF remains a manual gate. No 00README file is needed
for the ordinary UI workflow.

## Proposed metadata

[ARXIV_METADATA.txt](ARXIV_METADATA.txt) contains every field ready to copy,
including the full abstract with ordinary single TeX backslashes. It is derived
from [ARXIV_METADATA.json](ARXIV_METADATA.json); neither file is an upload input.

- **Title:** Minimum central circles: certified finite optima and an effective global asymptotic constant
- **Authors:** Maurizio Falconi
- **Abstract:** final manuscript abstract, with custom macros expanded;
  1,502 ASCII characters, mathematical content checked against the source/PDF.
- **Primary category:** retain `cs.CG`; no new cross-list.
- **MSC:** retain `52C26, 52C15, 05C85, 90C27` if offered.
- **Processor:** `pdflatex`; TeX Live `2025`; main file `ringmin_v2.tex`.
- **Replacement:** `arXiv:2607.28654`; preserve existing license and actual
  journal/publication fields. No journal metadata is invented.

Replacement **Comments**:

```text
9 pages, 0 figures. Substantially revised: proves existence and an effective variational characterization of the global asymptotic constant, disproves the earlier n^2/8 conjecture, and adds exact fixed-order feasibility results. Certified finite scope remains 3<=n<=14. Source code, proofs and certificate artifacts: https://github.com/falker47/ringmin
```

These explain the changes, update obsolete page/figure counts and preserve
the repository information from the [public v1 record](https://arxiv.org/abs/2607.28654v1).

## Evidence and limits

Existing exact theorems were checked against their sources. No closed formula
or efficient algorithm for `C_*`, optimum beyond `n=14`, global floating
cascade or external acceptance was introduced. Finite results retain the
original numerical guards. Fresh root execution of
`python verify.py --start 3 --stop 14` passed all twelve incumbent, local and
saved-frontier checks after restoration of 12 original logs. Independent
bounded checkers and artifact integrity checks also passed. Exhaustive
generation was not rerun; no hosted CI status is claimed.
Historical v1, proof notes, ledgers, production code and certificates are
unchanged. Full exact command results are in
[EVIDENCE.md](../../ops/TASK-20260911__arxiv_submission_audit/EVIDENCE.md).

## Exactly one next atomic task

The author performs the manual arXiv replacement preview: verify the inherited
record/metadata and sole upload file, select pdflatex / TeX Live 2025, and
inspect every page of **arXiv's own compiled PDF** against the reviewed local
candidate before deciding to finalize the replacement. This external workflow
was not started here.
