# Evidence

## Environment and acceptance provenance

```text
repository_head=6c16af422d1cb38641c62d43b6e0e547921b9ba9
platform=Windows 11 / PowerShell
python=3.14.3
symbolic_dependency=SymPy 1.14.0 (existing local installation)
pdf_runtime=Codex bundled workspace Python; pypdf and Pillow; Poppler renderer
latex=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
task_mode=STRICT
```

The user supplied this accepted baseline and explicitly identified the seam
package as publication-quality accepted material. The Registry was neither
read nor changed. Prior pending-review text in protected proof notes/dossiers
is preparation-time history. This task reproduces existing exact computation
and prepares a new manuscript; it is not a fresh independent review of either.
The user also explicitly exempted the existing untracked public-v2 source ZIP,
and confirmed no specific funding or relevant competing interests.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Angular model, anti-Monge/chain result | Definition and exact theorem | Public v2, direct derivative, Supnick primary theorem and published survey | Classical theorem is cited; no novelty claimed for Supnick itself |
| Selected seam theorem | Exact theorem and proved corollaries | Accepted source, full Appendix A, exact/symbolic checker | Existing independent bounded checker; transcription audit is not an all-k proof |
| Twelve strict global brackets | Computer-certified finite result | Exact protected certificate, complete verifier and rational witnesses | Independent of production and generator; same reviewer-implementation lineage |
| Floating regimes | Historical numerical descriptions, except exhibited n<=7 necklace | Public v2, carefully qualified manuscript Section 8 | No promotion to optimal-contact or existential floating theorem at the exact infimum |
| PDF/source fidelity | Engineering fact | Build, hashes, source audit and 18-page visual inspection | No hosted CI, peer review or publication acceptance implied |

## Commands actually run and exact material results

Commands below were run locally from the repository root. Git commands use
`-c safe.directory=<repository-root>` because of sandbox ownership; no
persistent Git configuration was changed. `<bundled-python>` denotes the
Python runtime returned by `load_workspace_dependencies`, not a new install.

| Command | Exit/result | What it checks; what it does not check |
|---|---|---|
| `python --version` | 0, `Python 3.14.3` | Runtime identity |
| `python -I -S verify_global_brackets.py --output ops/TASK-20260919__finite_journal_manuscript/global_brackets_verified.json` | 0, `PASS_GLOBAL_BRACKETS`, `pinned_input_verification: PASS`, 13 preserved files | Complete mathematical certificate and pinned binding; no historical search replay or execution attestation |
| `python -m pytest tests/test_global_brackets.py -q` | 0, 44 dots and `[100%]` | Existing regression/oracle tests; does not replace complete verifier |
| `python -m pytest tests/test_global_brackets.py --collect-only -o addopts='' -q` | 0, `44 tests collected in 0.02s` | Confirms the test count suppressed by configured quiet output; collection is not execution |
| `python ops/TASK-20260919__journal_fixed_order_seam/check_exact.py --symbolic` | 0; all requested checks PASS (counts below) | Bounded exact and symbolic checks independent of production; not an all-k computation or independent reviewer decision |
| `python ops/TASK-20260919__finite_journal_manuscript/transpose_seam.py` | 0, sections 1-6, 21 tags, classification array and three rational tables | Mechanical first pass plus manual review; no mathematical strengthening |
| `python paper_assets/journal_dcg/export_tables.py` | 0, 12 endpoint and 12 coverage rows; all widths `1/100000000000` | Exact publication transcription; not certificate verification |
| `pdflatex --version` (tool escalation) | 0, pdfTeX 1.40.28 / TeX Live 2025 | Compiler identity |
| `python paper_assets/journal_dcg/build.py` (tool escalation) | Final runs 0: `18 pages; 0 overfull boxes; no unresolved references` | Two-pass TeX build and manifest; no mathematical proof |
| Same build repeated without changes | 0, identical PDF SHA-256 `b88f54715fcf3468274131c08eeb7d23d7260b38ba163f1facc5a7030bee710a` | Byte reproducibility on this toolchain; no cross-platform byte guarantee |
| `pdftoppm -r 85 -png paper_assets/journal_dcg/ringmin_dcg.pdf reproducibility/.work/journal_dcg/page` | 0, 18 PNG pages | Poppler rendering; all pages visually inspected, with enlarged bridge tables |
| `pdfinfo paper_assets/journal_dcg/ringmin_dcg.pdf` | 0, 18 A4 pages, PDF 1.7, no JavaScript or encryption | PDF metadata; not tagged accessibility certification |
| `<bundled-python> ops/TASK-20260919__finite_journal_manuscript/inspect_pdf.py` | 0, 18 pages, no unresolved-reference/replacement text; contact sheets created | Extraction and visual-review preparation; extraction alone cannot prove layout correctness |
| `python ops/TASK-20260919__finite_journal_manuscript/check_manuscript.py` | 0, exact result below | Formula/table transcription, scope, hashes, protected paths and whitespace; not mathematical acceptance |
| `git diff --check` and `git diff --cached --check` | 0, no whitespace findings | Tracked/staged whitespace; new files also directly checked |

The complete verifier reported 908 angle intervals, 47 witnesses, 540 central
tangencies, 3,004 outer pairs, 6,008 angular inequalities, 268,648 explicit
full classes, and 3,374,988,556 full classes covered. Per-case margins,
strictness buffers, counts and digests are preserved in
[global_brackets_verified.json](global_brackets_verified.json).

The seam checker passed six bridges, 128 rank cycles, 128 parity-growth
matches, 30,976 directed fan identities, 512 threshold-boundary comparisons,
12 independently enclosed roots, 670 positive directed slacks and three
negative seams. SymPy checked the kernel derivatives, three pocket identities,
threshold algebra, arcsine estimate and pi integral. Its all-k justification
remains the included analytic proof, not these bounded checks.

The final manuscript audit reported:

```text
PASS: 27 seam displays preserved, 21 tags, six vectors, 12 endpoint and coverage rows.
PASS: abstract 184 whitespace words; scope, source references, artifact hashes, UTF-8/whitespace.
PASS: protected tracked paths unchanged; exempt ZIP unchanged; only allowed task paths.
PASS: complete stored reproduction report bound to all twelve certificate rows and positive recorded margins.
LIMIT: transcription and scope audit, not independent mathematical review or hosted CI.
```

## Artifact and provenance checks

The [build manifest](../../paper_assets/journal_dcg/BUILD_MANIFEST.json)
records every TeX input and builder/exporter hash, protected mathematical-input
hashes, compiler, two-pass command, fixed SOURCE_DATE_EPOCH=1789776000,
suppressed metadata and final PDF hash. The generation commit is the commit
containing this manifest, discoverable by its file history; no circular
self-hash is invented. New artifact text is pinned to LF through local Git
attributes and explicit exporter newlines. Protected source-text hashes
normalize CRLF to LF; preserved originals retain exact byte hashing, as
specified in the manifest. No nondeterministic research experiment was run.

The [source map](../../paper_assets/journal_dcg/SOURCE_MAP.md) records the
complete proof dependency chain and primary bibliography/venue checks.
Publicly supplied author contact details were reused; no private information
or ORCID was inferred. Venue facts were checked against official DCG pages.

Protected tracked files are compared to the accepted baseline by allowlisting
only four navigation files and the new artifact/dossier. The exempt untracked
ZIP retains SHA-256
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.
It is never staged. Rendered images and compiler logs stay in ignored work
storage, not the publication artifact.

## Failed attempts and corrections

- Plain Git failed with dubious ownership; command-local safe.directory
  resolved it. The sandbox cannot read the user's global ignore file and
  prints a warning; explicit observed paths and ZIP bytes were checked.
- Sandbox TinyTeX could not resolve the AppData directory. The same compiler
  ran through tool-enforced escalation. No automatic approval rejection occurred.
- Initial build failed because optional microtype was not installed. Removed
  that dependency instead of changing the user's TeX installation.
- An initial table-row-only input caused `Misplaced noalign` at bottomrule.
  Exporting complete tabular environments resolved it.
- The first converter changed inline `P_n(0)` into a reference. The unresolved
  reference gate caught it; conversion now excludes inline mathematics.
- A shell-quoted one-line contact-sheet command failed with SyntaxError.
  Replaced it with the explicit inspected `inspect_pdf.py` script.
- `pdftotext` was not on PATH. Bundled pypdf extracted text successfully;
  Poppler rendering and visual inspection supplied layout verification.
- A multi-file patch with delete/add on the same CURRENT_STATUS path was
  rejected before applying. Separate valid updates completed the intended edits.
- Bibliography checking corrected the draft Supnick DOI to `10.2307/1970124`.
  Final visual review widened the bridge-sum column and kept the classification
  array with its introductory item. Both changes were rebuilt and re-rendered.

## Final diff inspection and limits

The complete new manuscript/appendix, scripts, generated tables, manifest,
source map and dossier were read; the PDF was inspected visually. The exact
verifier result is generated evidence whose aggregate and per-case binding
are checked against its source, not hand-authored mathematics. Direct UTF-8
and whitespace checks include untracked text additions. The four navigation
diffs update source acceptance attribution, publication artifact navigation,
task state and the sole next review priority. No proof note, solver, test,
result, certificate, public source/PDF or asymptotic asset changes.

Only those task paths are staged. The staged diff and whitespace gate precede
the authorized commit and normal push to existing origin/main. Final commit,
remote SHA and remaining working-tree state are reported in the handoff;
this pre-commit dossier cannot contain its own commit identifier. There is no
hosted-CI claim. Independent STRICT review of the complete manuscript remains
the sole next atomic task; no submission or external review is performed here.
