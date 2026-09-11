# Conservative corrective v2 of the finite paper

**AWAITING_STANDALONE_ARXIV_ID.** Review candidate; not ready for submission.

*Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP
and certified finite optima*, Maurizio Falconi.

The [source](ringmin_finite_v2.tex) and [PDF](ringmin_finite_v2.pdf) retain the
original paper's Supnick theorem, all-pairs/STN model, certification method,
finite tables and geometric regimes. All obsolete coefficient-1/8 statements
are identified as disproved by the [standalone sequel](../asymptotic_sequel/README.md).
Floating claims distinguish existence of strict-slack placements at reported
radii from universal properties of all optima. The sequel's LP theory and endpoint proofs are cited,
not reproduced. Historical public-v1 files and default citation are unchanged.

The citation deliberately contains `PENDING_STANDALONE_ARXIV_ID`, with a
visible pending-publication status on the first page. No fictitious identifier
or upload-ready metadata is supplied. Once a real identifier exists, a separate
atomic task must replace this marker, remove the draft notice, rebuild and
re-audit source/PDF/metadata before any author-controlled submission.

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
record with the pending status, not a copy-ready submission form. The actual
arXiv server environment has not been exercised.

The [correction audit](../../ops/TASK-20260911__publication_architecture/CORRECTION_AUDIT.md)
lists every changed claim, retained finite scope and contents. The current
single next task is independent review of the standalone. This correction
does not require starting a second review/submission task now.
