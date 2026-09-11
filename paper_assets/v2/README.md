# Superseded replacement candidate - historical provenance

**EDITORIALLY_SUPERSEDED.** Do not use this directory as the next upload.
The current architecture is the [standalone sequel](../asymptotic_sequel/README.md)
plus the [conservative correction](../v1_correction/README.md), described in
the canonical [publication history](../../knowledge/PUBLICATION_HISTORY.md).
The source, PDF, upload source and original build/audit evidence below are
preserved. The build command below reproduces a historical candidate only.

This is an unsubmitted post-v1 candidate by Maurizio Falconi. The historical
`paper_assets/ringmin_paper.tex`, its PDF, tables, figures and citation metadata
remain unchanged. Internal adversarial validation is not independent external
acceptance or the author's final publication approval.

- [Candidate PDF](ringmin_v2.pdf) and [LaTeX source](ringmin_v2.tex).
- [Superseded arXiv replacement handoff](ARXIV_SUBMISSION.md), with the historical
  source-only [bundle](arxiv_submission/), then-verified metadata and hashes.
- [Final review packet](../../ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md),
  [claim matrix](../../ops/GOAL-20260911__conclude_study/CLAIM_MATRIX.md) and
  [complete command index](../../ops/GOAL-20260911__conclude_study/VERIFICATION.md).
- The main new theorem is proved self-contained in Sections 2-4. The
  explicit endpoints and fixed-order classification use the full proof notes
  identified by the bibliography and claim matrix. Ship the repository at the
  reviewed commit with this PDF: it is the proof/checker supplement.

## Build

From the repository root, with Python and a TeX distribution providing
`pdflatex`, `geometry`, AMS packages, `booktabs`, `longtable`, `hyperref`,
T1 encoding and Latin Modern fonts:

```text
python paper_assets/v2/build.py
```

Use `--engine PATH_TO_PDFLATEX` when the executable is not on PATH. The script
runs two passes into the ignored `reproducibility/.work/paper-v2/`, rejects
unresolved references or overflowing boxes, and writes only the versioned PDF
and [BUILD_MANIFEST.json](BUILD_MANIFEST.json). Metadata uses a fixed UTC epoch.
The manifest records source/build/PDF hashes and the actual pdfTeX version.
Matching PDF bytes requires the same TeX packages/fonts and input bytes;
the command does not install packages or alter historical v1 files.

The recorded build used pdfTeX 1.40.28 / TeX Live 2025, with scalable Latin
Modern fonts. Poppler rendered every page for visual inspection. The main
paper has nine pages. Full layout and repeat-build evidence is in the
[publication dossier](../../ops/TASK-20260911__versioned_publication/EVIDENCE.md).
The corrected submission candidate was independently compiled from only its
upload source in a fresh directory and inspected on every page; the final
[submission audit evidence](../../ops/TASK-20260911__arxiv_submission_audit/EVIDENCE.md)
supersedes the initial candidate hashes for this submission handoff. The PDF
and build manifest remain synchronized. The public proof supplement is pinned
to the reviewed commit in the manuscript; the arXiv bundle does not include
repository audits or build scripts.
