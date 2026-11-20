# Results and scope

**Computer-certified finite results.** For radii $1^2,2^2,\ldots,n^2$ and each integer $3\le n\le14$, the open/closed interval in the [results table](README.md#exact-endpoints) contains the global optimum. All twelve widths equal $10^{-11}$. For $n=14$ the endpoints are $173.72227944147<R_2^*(14)\le173.72227944148$. The new independent standard-library verifier accepts every quadratic certificate. [Certificates](certificates/)

**Independently reproduced finite results.** For radii $1,2,\ldots,n$, all twelve regenerated brackets coincide as exact rational numbers with Paper I v4. The generator uses its published endpoints and one previous witness order as input, reconstructs a fresh rational placement, and recomputes the angular bounds and complete combinatorial partition. The new checker takes each certificate alone as input. The two pipelines share the original mathematical method. The tests compare the fractions to the protected companion artifact. [Paper I v4](https://arxiv.org/abs/2607.28654v4)

**Finite comparison.** For each of $n=3,4,5,6$, both endpoints of the new quadratic bracket lie strictly inside the corresponding guarded interval in the pinned Ringmin-squared README. The new rows use exact rational Cartesian witnesses and integer lower-bound checks. The older results retain their documented mpmath.iv backend assumptions.

| $n$ | Earlier guarded interval | New exact interval |
|---:|:---|:---|
| 3 | $(0.3832870361,0.3834870362]$ | $(0.38338703613,0.38338703614]$ |
| 4 | $(1.4955284118,1.4957284119]$ | $(1.49562841187,1.49562841188]$ |
| 5 | $(3.9342277171,3.9344277172]$ | $(3.93432771714,3.93432771715]$ |
| 6 | $(8.4678350760,8.4680350761]$ | $(8.46793507608,8.46793507609]$ |

Source for the earlier intervals. [Ringmin-squared at 1d0a5dea](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/README.md)

**Exact theorem and proved corollary, written proof pending independent review.** For any distinct positive integer radii and any deletion depth leaving at least three core labels, insertion has the multiplicity derived in the method note. A complete strict integer lower exclusion gives a positive rational strictness buffer. [Method and proofs](METHOD_NOTE.md)

**Engineering facts.** The isolated verifier checked 908 angular lower enclosures, 204 central tangencies and 908 strict outer-pair inequalities across 24 witnesses. It recomputed the partition of every cyclic-order class in every row. All explicit leaves in the committed rows were excluded by a full cycle or a cycle obtained by deleting a prefix of the rank list. At quadratic $n=14$, 362,846 oriented core completions were pruned and 17 canonical cores survived. Each generated $10\cdot11\cdot12\cdot13=17{,}160$ insertions, for 291,720 explicit full words and 3,113,510,400 full classes overall.

The endpoints bracket an infimum. The true optimum inside an interval, an optimal order, its contacts and the possible floating circles remain undetermined by these certificates. Each stored placement concerns its own upper endpoint. The finite range ends at $n=14$. Asymptotic bounds and optimal placements for other input families require separate arguments. Research acceptance remains with the independent reviewer.
