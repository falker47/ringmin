# Standalone asymptotic sequel

**READY_FOR_REVIEW.** Unsubmitted; independent external review is pending.

*Minimum central circles: an effective characterization of the global
asymptotic constant*, Maurizio Falconi.

The [source](ringmin_asymptotic.tex) and [PDF](ringmin_asymptotic.pdf) present
the global asymptotic theorem, its effective finite-word LP characterization,
explicit error, geometric recovery and explicit bounds. The historical
finite/Supnick study is cited as arXiv:2607.28654; its algorithm, finite tables
and Supnick proof are not republished here. Minimal angular/chain/full
definitions are included for self-containment.

## Contents

1. Problem and relation to prior finite work.
2. Exact angular comparison.
3. Existence by genuine-label concatenation.
4. Effective finite-word characterization.
5. Explicit geometric upper constructions.
6. An explicit global lower endpoint.
7. Reproducibility and open questions.

See the [claim map](../../ops/TASK-20260911__publication_architecture/SEQUEL_CLAIM_MAP.md)
and [policy/overlap audit](../../ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md).
The complete mathematical supplement is pinned to the public commit
`3beb8d70c5b3748d370a92855847bdf574e5a14f` in the bibliography. Its exact
theorems remain distinct from bounded checker evidence and external acceptance.

## Source-only build and metadata

The complete [source bundle](source_bundle/) contains only
`ringmin_asymptotic.tex`, with inline bibliography and no external assets.
From its root run the following command until references stabilize (three
passes in the recorded build):

```text
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ringmin_asymptotic.tex
```

Alternatively, from the repository root:

```text
python paper_assets/build_publications.py sequel
```

The builder copies only declared inputs into a fresh ignored directory,
requires stable references and zero box/glyph/citation warnings, then records
input/PDF/build hashes in [BUILD_MANIFEST.json](BUILD_MANIFEST.json).
The [review metadata](REVIEW_METADATA.json) agree with the source and PDF;
they are not an authorization to submit. Python is unnecessary for direct TeX
compilation. Use pdfLaTeX with geometry, AMS packages, booktabs, longtable,
hyperref, T1 and Latin Modern. Local TL2025 packages are newer than arXiv's
frozen snapshot; actual arXiv PDF inspection remains a later human gate.

## Publication sequence and boundary

First independently review this standalone. A later author-controlled
submission may request a new identifier. Only if a real identifier is assigned
should a separate atomic task finalize the [corrective original-paper v2](../v1_correction/README.md).
Moderators may require versioning or consolidation even without large textual
overlap. In that event prepare the fully integrated fallback specified in the
policy audit; the old nine-page candidate is insufficient. No submission,
release, tag or external acceptance is part of this task.
