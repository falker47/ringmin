# Conservative corrective v2 of the finite paper

**ARXIV_REPLACEMENT_CANDIDATE.** Corrective v2; not submitted.

*Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP
and certified finite optima*, Maurizio Falconi.

The [source](ringmin_finite_v2.tex) and [PDF](ringmin_finite_v2.pdf) retain the
original paper's Supnick theorem, all-pairs/STN model, certification method,
finite tables and geometric regimes. All obsolete coefficient-1/8 statements
are identified as disproved by the [standalone sequel](../asymptotic_sequel/README.md).
Floating claims distinguish existence of strict-slack placements at reported
radii from universal properties of all optima. The sequel's LP theory and endpoint proofs are cited,
not reproduced. Historical public-v1 files and default citation are unchanged.

The citation identifies the standalone sequel as
[arXiv:2609.13630](https://arxiv.org/abs/2609.13630), with the finalized
replacement status on the first page. The author-run builder has produced the
current 12-page PDF, manifest and metadata, and the existing package checker
passes against its actual isolated clean-build directory. The author also
independently compiled this four-input source bundle with
`SOURCE_DATE_EPOCH=1789084800` and `FORCE_SOURCE_DATE=1`; the existing package
checker passes against that independent clean build. This task performs no
submission.

## Contents

1. Introduction.
2. The model.
3. The optimal cyclic order is a fixed Supnick tour.
4. Exact algorithm and certification.
5. Certified optima for 3 <= n <= 14 and finite regimes.
6. Correction of the v1 asymptotic conjectures.
7. Open problems.

Acknowledgments and references follow, then Appendix A, High-precision values
and figures. Every original numerical table is retained.

## Source-only build

The [source bundle](source_bundle/) contains exactly:

- `ringmin_finite_v2.tex`;
- `appendix_tables.tex`;
- `figures/n14.png`;
- `figures/radii_vs_n.png`.

Tables and images are byte-identical copies of the historical assets. Captions
clarify the obsolete comparison curve without regenerating the historical
figure. From the bundle root, repeat until references stabilize:

```text
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder ringmin_finite_v2.tex
```

Or, from the repository root:

```text
python paper_assets/build_publications.py correction
```

Python is not needed for direct TeX compilation. The required packages are
geometry, AMS packages, booktabs, graphicx, hyperref, T1 and Latin Modern.
The [manifest](BUILD_MANIFEST.json) records exact bundle hashes, compiler and
stable passes. [REVIEW_METADATA.json](REVIEW_METADATA.json) is a consistency
record with the finalized identifier and replacement status, not a submission
record. The builder, package audit and independent direct bundle compile have
passed for the current local artifact. The actual arXiv server environment has
not been exercised.

The [correction audit](../../ops/TASK-20260911__publication_architecture/CORRECTION_AUDIT.md)
lists every changed claim, retained finite scope and contents. The current
finalization [task dossier](../../ops/TASK-20260915__finalize_corrective_v2/TASK_STATUS.md)
records the identifier update and final local verification. The next author
action is to create the replacement submission for arXiv:2607.28654v1 using
only this directory's `source_bundle/`, then inspect arXiv's compiled PDF
before finalizing the replacement.
