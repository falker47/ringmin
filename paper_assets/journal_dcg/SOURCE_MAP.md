# Mathematical and publication source map

This is artifact-local provenance, not a new stable claim ledger. Acceptance
of the source baseline and review of this manuscript are distinct. The user
supplied revision baseline `bfc2caff2ae6b1d1f149eb52cac4dc220dcf85d6`.
Initial preparation used `6c16af422d1cb38641c62d43b6e0e547921b9ba9` with
the seam package explicitly accepted; that computational pin is unchanged.
No Registry API was read
or changed. Older pending-review wording is preserved as historical context.

| Manuscript location | Classification | Controlling source and integration |
|---|---|---|
| Sections 2-4 | Definitions and exact theorems using a classical ordering theorem | Corrected public [v2](../v1_correction/ringmin_finite_v2.tex); direct mixed derivative; Supnick with explicit sign convention and rank rule |
| Section 5, Appendix A | Exact theorem and proved corollary | [Accepted seam package](../../research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md), sections 1-6 with all 27 original displays, 21 tags and six rational bridges; A.5 now spells out the existing threshold-boundary comparison in two additional unnumbered displays |
| Section 6, Appendix B | Exact mathematical basis for computer-assisted proof | [Bracket proof](../../research/GLOBAL_BRACKET_CERTIFICATE.md) and [integrated verifier](../../verify_global_brackets.py) |
| Section 7, Tables 2-3 | Computer-certified finite brackets and coverage counts | [Certificate](../../reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json); generated rational table inputs; complete local verifier result |
| Section 8, Table 4 | Historical numerical descriptions except the exhibited n<=7 necklace | Public v2 and [certification owner](../../knowledge/CERTIFICATION.md); not promoted to exact-optimum floating claims |
| Sections 9-10 | Limitations and engineering facts | Exact theorem scope, pinned code/data and actual reproduction; no new asymptotic claim |

## Seam proof gates

Appendix A contains the rank rule, both parity edge lists/counts, neighbors
of k, unique root, direct parity growth matching, root divergence, minimum
triangle defect and equality cases, fan cancellation, both directed paths,
closing edge, N=3 and N=4, forced-gap converse, positive threshold branch,
persistence and possible equality, six rational bridges and propagation.

No explicit k>=4 formula, all-k equality exclusion, global cascade, or exact
optimal contact classification is imported. Neither
`SUPNICK_FULL_FEASIBILITY.md` nor `SUPNICK_SEAM_SEQUENCES.md` is an essential
reference in the manuscript.

## Finite proof gates

- Circumference and all 908 angle intervals are checked by independent outward
  integer cosine arithmetic, including the tail direction.
- Lower weights and upper circumference prove strict necessary-cycle
  violations. Forward DP, reversal, full prefix coverage, reflection and every
  insertion gap are justified; equality is retained.
- Positive integer margins yield rational radius buffers and strict lower
  bounds for the infimum without assuming attainment.
- Every case has an exact rational Cartesian witness; all 47 are checked,
  including central tangency and every outer pair.
- Hashes identify recomputed evidence; they do not replace proof or attest
  historical execution. The local run reproduces the independent reviewer's
  implementation lineage.
- No historical frontier, Top-K cap, checkpoint, float64 envelope, production
  import or generator replay is a proof premise.

## Editorial decisions and venue checks

Omitted: corrective narrative, high-digit reconstruction appendix, worst-chain
comparisons, n>14 heuristic table, and historical asymptotic plots. Public
assets are preserved. The story proceeds from chain structure and full
geometry to seam theory, exact brackets, interpretation and limitations.
Public preprints are mentioned in text; five published works appear
in the numbered bibliography after the two additions below.

The [DCG guidelines](https://link.springer.com/journal/454/submission-guidelines)
and [aims and scope](https://link.springer.com/journal/454/aims-and-scope)
were checked on 2026-09-19. Editable TeX/PDF, abstract/keywords/MSC and
declarations are present. Section 2.2.3 of the institutional publisher copy of
the [Burkard et al. survey](https://pure.tue.nl/ws/files/2373438/Metis148543.pdf)
verifies the maximum Supnick-tour convention. The
[Supnick primary record](https://www.jstor.org/stable/1970124) identifies the
correct DOI. The authors' [temporal-network paper](https://ftp.cs.ucla.edu/pub/stat_ser/r113-L-reprint.pdf)
supports the difference-constraint reference. No policy text is copied.

## Pre-submission revision and related-work attribution

The abstract now says a fixed minimizing cyclic order, avoiding an unintended
uniqueness claim. The A.5 addition proves the already stated boundary using
strict decrease of reciprocal square roots and positivity before squaring;
it adds no theorem scope and leaves all existing displays and tags intact.

Mathews and Zymaris, *Spinors and the Descartes circle theorem*, Journal of
Geometry and Physics 212 (2025), 105458,
[DOI](https://doi.org/10.1016/j.geomphys.2025.105458): the
[author manuscript](https://www.danielmathews.info/wp-content/uploads/2023/10/spinors_and_descartes_theorem.pdf),
definition of an n-flower and related-work discussion (pp. 1-4), supports the
central and cyclic-neighbor tangency description. The
[institutional publication record](https://research.monash.edu/en/publications/spinors-and-the-descartes-circle-theorem/)
confirms the published title, authors, volume, article number and DOI.

Collins and Stephenson, *A circle packing algorithm*, Computational Geometry
25 (2003), 233-256,
[DOI](https://doi.org/10.1016/S0925-7721(02)00099-8): the
[publisher abstract](https://www.sciencedirect.com/science/article/pii/S0925772102000998)
and original article introduction/Section 1, pp. 233-235 (read in a
[full-text mirror](https://www.scribd.com/document/496278275/Collins-2003-Makale-a-Circle-Packing-Algorithm)),
specify an input tangency complex and boundary conditions. This is directly
pertinent to the narrow distinction from choosing Ringmin's cyclic order
with fixed radii and enforcing all pairwise non-overlap. No convergence,
optimality, or universal non-overlap assertion is attributed to that paper.

Both references were checked on 2026-09-19 and supply context only. Neither
is a new premise for the seam proof or finite certificate. No cover letter,
submission, release, deposit or ORCID lookup is part of this task. A pinned,
content-addressed Git commit identifies computational provenance; it is not
a permanent archival repository deposit. Release/archival DOI is deferred.
