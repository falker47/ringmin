# Mock Referee Report — Ringmin finite paper

Date: 2026-09-16

Manuscript: *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima*

Current public record: arXiv:2607.28654, corrective v2 announced by arXiv as public on 2026-09-16. This report reviews the corrective manuscript in `paper_assets/v1_correction/ringmin_finite_v2.tex`; it does not modify the public arXiv source.

## Overall assessment

The paper has a coherent mathematical core and is substantially stronger than the superseded v1 framing. Its main structure is now easy to audit:

1. an exact angular reformulation of the circle non-overlap constraints;
2. a fixed-order theorem obtained from strict anti-Monge structure and Supnick's classical TSP theorem;
3. an all-pairs geometric feasibility formulation as a simple temporal network;
4. finite global-optimum claims for `3 <= n <= 14` backed by saved search/frontier evidence and an independent high-precision verifier;
5. a careful separation between proved statements, computer-certified finite statements, numerical evidence, heuristics and open questions;
6. an explicit correction of the false v1 asymptotic conjectures, delegated to the separate sequel `arXiv:2609.13630`.

The manuscript is worth developing into a journal submission. I would not submit the arXiv corrective source unchanged, however. The principal work before submission is not cosmetic: the numerical-certification claim should be hardened or narrowed, and the fixed-order seam results currently cited to a repository snapshot should be made self-contained or given a stable publication-quality source.

## Major issue 1 — what exactly is certified?

The manuscript claims global optima through `n=14` with an absolute radius guard of `1e-10`. The evidence chain is unusually well documented: exhaustive canonical enumeration was performed historically; lower-bound pruning/frontier artifacts were saved; `verify.py` independently recomputes incumbents and retained frontier lower bounds at 50 digits; the current dossier records `incumbent=PASS local=PASS frontier=PASS` for every `n=3..14`.

The remaining rigor boundary is important. The branch-and-bound lower bounds were produced in float64. The manuscript supports the numerical guard by an error analysis and calibration against 50-digit recomputation, including `100000` random samples per `n` for `8 <= n <= 14`, but the independent verifier rechecks the retained frontier and coverage metadata rather than recomputing every excluded order with directed interval arithmetic. The repository itself correctly states this limitation.

A mathematically demanding referee can therefore ask whether "certified global optimum" is meant in the formal computer-assisted-proof sense or in the reproducible numerical-certification sense. Random calibration is strong evidence but is not, by itself, a proof of a worst-case floating-point error bound over billions of pruned orders.

### Required resolution before submission

Choose one of two defensible routes:

**Route A — strengthen the certificate.** Make every pruning comparison rigorous under an outward-rounded/interval or analytically bounded evaluation of the lower bound. The ideal journal artifact would allow the saved enumeration summaries to be checked against a formally valid numerical error envelope without rerunning the entire search.

**Route B — narrow the terminology.** If Route A is disproportionate, retain the numerical results but state the exact certification model in the abstract, theorem/table language and algorithm section. Avoid wording that could be read as a machine-checkable proof with interval guarantees. Explicitly distinguish exhaustive combinatorial coverage from the numerical reliability assumptions used by the pruning comparison.

For a journal submission, Route A is materially stronger.

## Major issue 2 — the fixed-order seam theorem is not self-contained

The corrective paper cites `research/SUPNICK_FULL_FEASIBILITY.md`, `research/SUPNICK_SEAM_SEQUENCES.md` and a pinned GitHub snapshot as `fixedseams`. These results are used for statements beyond the originally certified finite range, including eventual unrealizability of the canonical Supnick necklace for every fixed terminal radius and exact early seam thresholds.

That is adequate provenance for a research repository, but weak as a journal reference. The current Discrete & Computational Geometry author instructions say that the reference list should contain published or accepted works; unpublished material should otherwise be handled in text. A mutable repository document is also harder for a referee to evaluate than a theorem and proof in the submission.

### Required resolution before submission

Prefer, in order:

1. incorporate the fixed-order seam theorem and the proof actually needed by this paper into a journal appendix;
2. or package it as a stable, citable preprint with a permanent identifier and cite that source;
3. otherwise remove claims that materially depend on it from the journal paper and keep only the certified finite statements needed for the main result.

The first option gives the finite paper the cleanest standalone story.

## Major issue 3 — isolate the genuinely new contribution from the classical Supnick theorem

The anti-Monge calculation is short and clean, and the application of Supnick yields a fixed optimal chain tour. Because the key tour theorem is classical, the introduction should make especially clear which contribution is new:

- recognizing/proving the angular cost matrix has the required strict anti-Monge structure for every `R`;
- transferring the fixed-`R` tour optimum to the variable chain-radius problem;
- showing why the chain relaxation is not the full geometry;
- formulating and solving the all-pairs finite problem;
- identifying and carefully quantifying the floating-circle regimes in the certified range.

The present text already moves in this direction. A journal version should sharpen it further so that the paper is not read as merely an application of a known TSP pattern.

## Major issue 4 — convert the corrective narrative into a standalone journal narrative

The arXiv v2 correctly foregrounds that it is a correction. A journal paper should instead read as the definitive finite-paper presentation. Historical correction details can be compressed into a short note in the introduction or related-work discussion.

In particular:

- state the current theorem/results directly;
- retain a concise sentence explaining that an earlier preprint conjectured the wrong asymptotic coefficient and that the separate sequel resolves the asymptotic problem;
- remove submission-workflow wording and repository-state language from the manuscript proper;
- preserve the explicit epistemic separation between theorem, finite computation, heuristic evidence and open problem.

## Major issue 5 — reproducibility should have a stable archival target

The repository has excellent provenance, including generation hashes, historical logs, frontier JSON, a standalone verifier and task evidence. For journal review, pin a release/tag and preferably an archival DOI or equivalent immutable snapshot. The manuscript should point to that immutable release rather than relying only on the moving `main` branch.

The paper should also state clearly that `verify.py --start 3 --stop 14` rechecks saved evidence and does not regenerate the multi-hour exhaustive searches.

## Minor and presentation issues

- Give a completely explicit even/odd definition of the Supnick tour rather than relying only on an ellipsis in the displayed sequence.
- Define the anti-Monge/Supnick sign convention once, because different sources use opposite Monge conventions.
- Preserve the useful distinction between "there exists an optimal placement in which a circle is floating" and universal slack across all optimal placements.
- Keep the warning that 50-digit reconstruction is not a 50-digit global certificate.
- Consider moving the historical `n=15..18` heuristic table to supplementary material unless it directly serves the journal narrative.
- The abstract is 192 words, which is within the current DCG 150–250-word requirement.
- Add 4–6 journal keywords and retain the MSC codes.
- Add the target journal's required Statements and Declarations section.
- The existing acknowledgment of AI assistance is directionally appropriate; for DCG/Springer, generative LLM use beyond copy-editing must be documented in a suitable manuscript section, with the author retaining accountability.
- Check final figures against the target journal's accessibility requirements, including captions, contrast and non-color-only encoding.

## What I would preserve

Do not weaken the manuscript's strongest editorial feature: its explicit epistemic ledger. The paper is much more credible because it says exactly which statements are proved, computer-supported, heuristic, disproved, or open. Likewise, preserve the independent verifier and the separation between the finite paper and the asymptotic sequel.

## Pre-submission acceptance criteria

I would regard the paper as journal-ready when all of the following hold:

- [ ] Numerical-certification language has either a rigorous worst-case error envelope or deliberately narrower terminology.
- [ ] The fixed-order seam result needed by the paper is self-contained or has a stable publication-quality reference.
- [ ] The journal manuscript is standalone rather than primarily a correction notice.
- [ ] Novelty relative to Supnick is stated precisely.
- [ ] Code/data are pinned to an immutable release/archive.
- [ ] DCG metadata are present: 4–6 keywords, MSC, declarations, author details and ORCID if available.
- [ ] LLM/AI assistance is disclosed in a form compliant with the selected journal policy.
- [ ] The final source/PDF and computational archive are cross-checked against the claims submitted for review.
