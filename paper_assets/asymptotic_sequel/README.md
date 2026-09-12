# Standalone asymptotic sequel

**ARXIV_SUBMISSION_CANDIDATE.** This is the single standalone artifact prepared
for manual NEW arXiv submission. Task state: `READY_FOR_REVIEW`; no submission
or external mathematical acceptance is claimed.

*Minimum central circles: an effective characterization of the global
asymptotic constant*, Maurizio Falconi. September 12, 2026. Eight pages.

The [manuscript](ringmin_asymptotic.tex) and [PDF](ringmin_asymptotic.pdf)
present the angular-to-line reduction, global limit, effective finite-word LP
characterization, full geometric recovery and explicit endpoints. The finite
study is cited as arXiv:2607.28654v1; finite algorithms and tables stay there.
The [architecture claim map](../../ops/TASK-20260911__publication_architecture/SEQUEL_CLAIM_MAP.md)
still describes the unchanged science. The proof supplement remains pinned to
`3beb8d70c5b3748d370a92855847bdf574e5a14f`.

## Exact upload and metadata

- Upload only [source_bundle/ringmin_asymptotic.tex](source_bundle/ringmin_asymptotic.tex).
  It is byte-identical to the manuscript and contains its bibliography.
- Copy the fields in [ARXIV_METADATA.md](ARXIV_METADATA.md), also available as
  [JSON](ARXIV_METADATA.json). The prior author's non-exclusive arXiv license
  choice is preserved in the guidance; no new identifier, journal reference
  or DOI is supplied.
- [BUILD_MANIFEST.json](BUILD_MANIFEST.json) identifies exact filenames, byte
  sizes, SHA-256 hashes, processor, main file, TeX environment and builder.
  Metadata, manifest, PDF and this README are outside the upload directory.
- The [finalization evidence](../../ops/TASK-20260912__standalone_submission_candidate/EVIDENCE.md)
  records independent package checks, every-page inspection, references,
  overlap and fresh bounded mathematical checks.

## Rebuild

From the source bundle in a clean directory, run this command three times:

```text
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ringmin_asymptotic.tex
```

Or from the repository root:

```text
python paper_assets/build_publications.py sequel
```

The builder copies only declared inputs into a fresh ignored directory,
requires at least three passes with stable references and zero box, glyph or
citation warnings, and regenerates the manifest and both metadata formats.
Python is unnecessary for direct compilation. The source uses geometry, AMS
packages, booktabs, longtable, hyperref, T1 and Latin Modern. Scoped LF
attributes preserve source bytes on checkout. Identical PDF bytes additionally
require the recorded TeX package/font snapshot and source-date epoch; the
epoch is fixed at September 11 for reproducibility, independently of the
manuscript's September 12 date. The build report records system-input hashes.

## Publication boundary

The next human action is to manually create a **NEW** arXiv submission with
this bundle and inspect arXiv's compiled PDF before finalizing. Local builds
do not establish equivalence to arXiv's TeX distribution or moderation approval.
The [policy/overlap audit](../../ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md)
explains the residual possibility of consolidation or versioning.

The [corrective finite-paper v2](../v1_correction/README.md) remains
`AWAITING_STANDALONE_ARXIV_ID`; it cannot be finalized until a real identifier
exists. The [former replacement](../v2/README.md) remains
`EDITORIALLY_SUPERSEDED`. Historical sources and audit evidence are preserved.
