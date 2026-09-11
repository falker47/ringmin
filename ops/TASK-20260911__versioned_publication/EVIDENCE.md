# Publication evidence

Mode STRICT; local Windows/PowerShell, Python 3.14.3. Mathematical scope and
independent internal checks are in the goal's [claim matrix](../GOAL-20260911__conclude_study/CLAIM_MATRIX.md).
Three manuscript audits map source statements to the final paper and retain
initial findings and verified corrections. The fixed-order source audit
also supplies a fresh exact certificate for all twelve endpoint bridges.

## Source and build

New publication location: paper_assets/v2/. Historical v1 and its synchronized
assets are protected. The single change to an already committed research proof
replaces "least circumference" by "infimum circumference" for degenerate
mark sets; it leaves the all-positive n>=3 theorem intact. The global reviewer
checked it in both source and manuscript.

Exact build command used:

```text
python paper_assets/v2/build.py --engine PATH_TO_INSTALLED_PDFLATEX
```

The engine was the installed TinyTeX pdfTeX 1.40.28 / TeX Live 2025. The actual
executable path is machine-local and intentionally not embedded in a repository
artifact. build.py gives exact subprocess options and two passes. Fixed epoch
1789084800 controls date metadata. Latin Modern fonts are embedded as scalable
Type 1 fonts. BUILD_MANIFEST.json records the exact TeX/build/PDF SHA-256 and
compiler version. Same-package/font assumptions are explicit.

The first sandbox build exited 1 on runtime access; the first direct escalated
command exited 1 on its relative output argument. The build script then
compiled but exited 1 on an overfull bibliography box, deliberately refusing
to install that PDF. Corrected bibliography/font build exited 0:
`PASS versioned PDF built; source/PDF/build hashes recorded`.

## Rendering and inspection

Commands used the bundled Poppler executables, with these exact arguments:

```text
pdftoppm -r 110 -png paper_assets/v2/ringmin_v2.pdf reproducibility/.work/paper-v2/page
pdfinfo paper_assets/v2/ringmin_v2.pdf
```

Both exited 0. Initial clean build: nine letter-size pages, PDF 1.7, 332034
bytes, no encryption, JavaScript or forms. The builder viewed all pages 1-9
and verified readable math, unclipped bounds/long fractions, correct chain
classification table, and wrapped bibliography paths. Renderings remain
ignored build intermediates. Final metadata/AI-assistance disclosure and repeat
build are recorded below.

Final build and an unchanged repeat both exited 0. Both produced exactly
332580 bytes, nine pages, with SHA-256
`a3b0d50f40a843024d84065fcafd181ce8d048ab67e9185cc5d3c748a8ee1c0a`.
The final source hash is
`528498d131b2d942c15b39b642aa33f8e9b8424bb081d6f826e2479dc986122f`.
The final pdfinfo confirms the title/author, fixed date, nine pages and no
JavaScript/forms. Final Poppler rendering used prefix `final` instead of
`page`; both commands exited 0. Pages 1-7 are byte-identical PNGs to the
already inspected pages, and the builder separately viewed final pages 8-9
after the disclosure shifted the references. All nine final pages are checked.
No overflowing box, missing glyph or unresolved reference remains.

The final changes since the manuscript reviewers' recorded source snapshots
are bibliography wrapping/font selection, PDF metadata and the AI-assistance
disclosure. Mathematical statements and coefficients remain as reviewed.

## Complete delta checks

The source manifest for this final packet records SHA-256 over canonical LF
text bytes and exact binary bytes; the build manifest separately records the
actual Windows build inputs. The packet is in the final containing commit,
avoiding a circular literal self-hash. Text additions are reviewed in full,
all local Markdown file targets are checked outside code spans, and complete
staged content is compared to inspected files with only Git EOL normalization.
The earlier source-manifest comparison initially compared Windows-export text
to raw LF Git blobs and failed on ci.yml; the corrected check verified all
546 hashes and proved all 522 differences were solely CRLF/LF conversion.
No source discrepancy remained.

Final pre-stage validation: all 568 source-manifest entries match; all 27
publication-delta paths are expected; 78 local Markdown file targets resolve.
Every new/modified text is valid UTF-8 with a final newline and no newly
introduced trailing whitespace. One unchanged README Markdown hard break is
preserved. The first blanket whitespace check flagged that old intentional
break; comparison with HEAD confirmed it was not introduced by this task.
`git diff --check` exits 0. Historical paper assets, original results,
production src, AGENTS.md, review protocol, CITATION.cff and REPORT have an
empty path-scoped diff from the starting HEAD. No stable mathematical claim
was duplicated into a second thematic owner.

## Limits

The paper supplies full proofs of its central new asymptotic result and exact
references to the included full proof supplement for other substantial claims.
The source manifest and containing Git commit identify that supplement. A
bounded literature check does not certify exhaustive novelty or priority.
The generated REPORT is a finite-result mirror and needed no regeneration.
All validation is local/internal; hosted CI and external acceptance are
unclaimed. No historical paper or certificate was regenerated.
