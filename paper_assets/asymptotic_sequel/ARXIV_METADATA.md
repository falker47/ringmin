# arXiv submission metadata

Copy the fields below for a **NEW** submission. Upload only the contents of
`source_bundle/`; the PDF, manifest and metadata stay outside that directory.
Inspect arXiv's compiled PDF before finalizing the submission.

## Title

Minimum central circles: an effective characterization of the global asymptotic constant

## Authors

Maurizio Falconi

## Abstract

```text
Let ${R^\ast}(n)$ be the least radius of a central circle to which nonoverlapping circles of radii $1,\ldots,n$ are externally tangent. We prove that ${R^\ast}(n)={C_\ast} n^2+o(n^2)$ and characterize ${C_\ast}$ by finite linear programs with an explicit error tending to zero. The reduction preserves arbitrary orders and all pairwise constraints: the limiting problem places marked points on a line at pairwise separation at least the geometric mean of their marks. Concatenation with a bounded boundary cost proves existence, and balanced finite-word programs supply matching effective upper and lower bounds. Their certified gap is $(1/k+1/r)/\pi$, before directed arithmetic error, for $k$ mark types and words of length $r$. A quantitative reflected-block recovery theorem supplies genuine permutations and full ring geometry, with a countable extension and a strict four-block improvement. The explicit interval is $C_{\mathrm{term}}+\eta_{\mathrm{width}}\le{C_\ast}\le U_4$; neither endpoint is asserted sharp. In particular, the coefficient $1/8$ proposed in the preceding finite study is false. An elementary expression for ${C_\ast}$, efficient high-precision evaluation and global floating-circle structure remain open.
```

## Comments

8 pages, no figures. Asymptotic sequel to arXiv:2607.28654v1. Proves existence and an effective finite-program characterization of the global asymptotic constant. Proofs and code: https://github.com/falker47/ringmin/tree/3beb8d70c5b3748d370a92855847bdf574e5a14f

## Classification

- Primary category: `cs.CG` (Computational Geometry).
- Recommended cross-list: `math.MG` (Metric Geometry), subject to arXiv classification.
- MSC2020: Primary `52C15`; Secondary `52C26`, `90C05`.

## License and source

- Preserve the prior paper's author-selected [arXiv.org perpetual, non-exclusive license](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html).
  The repository's MIT code license does not select a paper license.
- Processor: `pdflatex`.
- Main source: `ringmin_asymptotic.tex`.
- Leave journal reference, DOI and report number blank; none is assigned here.

The manuscript is 8 pages. Exact source/PDF hashes are in
[BUILD_MANIFEST.json](BUILD_MANIFEST.json). The machine-readable copy is
[ARXIV_METADATA.json](ARXIV_METADATA.json). This is prepared metadata, not a
record of submission, moderation or external mathematical acceptance.
