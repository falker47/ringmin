# Venue and Submission Plan

Date: 2026-09-16

## Target selection

### Primary target — Discrete & Computational Geometry

Current journal page: https://link.springer.com/journal/454

Why it is the strongest thematic fit:

- the journal explicitly covers packing, covering, configurations and arrangements;
- it covers geometric algorithms and complexity;
- it accepts work with a distinct geometric flavor in mathematical programming and combinatorial optimization;
- the paper combines discrete geometry, an anti-Monge/Supnick optimization theorem and a computational all-pairs feasibility/certification component.

This is the target around which the first journal version should be prepared.

Current author requirements relevant to this manuscript (checked 2026-09-16):

- submission through Editorial Manager;
- complete editable source files at submission/revision;
- LaTeX manuscript plus compiled PDF;
- title page with author/affiliation or unaffiliated city/country, active corresponding-author e-mail and ORCID if available;
- abstract 150–250 words — the corrective v2 abstract is 192 words;
- 4–6 keywords;
- MSC classification codes;
- Statements and Declarations, including competing interests;
- generative LLM use beyond AI-assisted copy editing must be documented in Methods or another suitable section, with human accountability for the final text;
- the journal's reference instructions prefer works published or accepted for publication; unpublished work is better handled in text or replaced by a stable publication-quality source.

Author instructions: https://link.springer.com/journal/454/submission-guidelines
Aims and scope: https://link.springer.com/journal/454/aims-and-scope
Submission portal: https://www.editorialmanager.com/dcgj/

## Alternatives

### Computational Geometry: Theory and Applications

Journal page: https://shop.elsevier.com/journals/computational-geometry/0925-7721

The journal publishes fundamental research in theoretical and applied computational geometry, including design and analysis of geometric algorithms and numerical, graph-theoretical and combinatorial aspects. It is a strong alternative if the manuscript is framed more strongly around the exact geometric feasibility algorithm, combinatorial search and computational evidence.

### Discrete Applied Mathematics

Journal page: https://shop.elsevier.com/journals/discrete-applied-mathematics/0166-218X

The scope emphasizes algorithmic/applicable discrete mathematics and applications of combinatorial mathematics. It is plausible if the journal version foregrounds the Supnick/anti-Monge and combinatorial-optimization structure, but the match to the circle-packing/discrete-geometry core is less direct than DCG.

## Submission strategy

Do not submit the corrective arXiv source verbatim. Keep `paper_assets/v1_correction/` immutable as the public-v2 source and develop a separate journal manuscript.

Recommended order:

1. Resolve the two referee-level blockers identified in `REFEREE_REPORT.md`:
   - numerical-certification rigor/terminology;
   - publication-quality treatment of the fixed-order seam theorem.
2. Create `paper_assets/journal_dcg/` from the mathematical content of the corrective v2, not by overwriting it.
3. Reframe the introduction from "correction" to definitive finite-paper presentation.
4. Add DCG metadata and compliance sections.
5. Pin the computational archive to an immutable repository release and, if practical, an archival DOI.
6. Run the complete verifier and manuscript build against the exact journal candidate.
7. Produce a final mock-referee pass against the journal manuscript.
8. Prepare the cover letter only after the manuscript passes that review.
9. Submit through Editorial Manager.

## ORCID

No ORCID is inferred from name matching. The author should create or confirm the correct ORCID directly at https://orcid.org/ before final journal submission. Once the exact 16-digit identifier is supplied, add it to the journal title-page metadata and submission account. The scientific author name should remain `Maurizio Falconi` unless the author deliberately chooses otherwise.

## Candidate keywords for the DCG version

These are working metadata, not yet frozen:

- circle packing
- discrete geometry
- computational geometry
- traveling salesman problem
- Monge matrices
- certified computation

## Existing MSC codes

The corrective v2 already lists:

- 52C26
- 52C15
- 05C85
- 90C27

Recheck the final set when the journal manuscript scope is frozen.

## Decision gate

Proceed with **Discrete & Computational Geometry** as the working target. Do not submit until the certification and self-containedness blockers have explicit resolutions; venue formatting and cover-letter work should not distract from those substantive issues.
