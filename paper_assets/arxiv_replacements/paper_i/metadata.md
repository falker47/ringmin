# Paper I — replacement candidate for arXiv:2607.28654

Use the existing record. The upload file is `paper_i_source.zip`; `paper_i.pdf` is the locally compiled preview. The manuscript retains its v3 title, abstract, author, printed date, six keywords and four MSC classes. This candidate was prepared on 10 November 2026.

## Portal metadata

**Title**

```text
Minimum central circles: chain order, seam obstructions, and exact finite certification
```

**Author**

```text
Maurizio Falconi
```

**Abstract**

```text
We minimize the radius of a central circle externally tangent to pairwise non-overlapping circles of radii $1,2,\ldots,n$. We first study the adjacent-chain relaxation, which imposes only the constraints between consecutive circles. Its angular kernel has strict anti-Monge structure, so Supnick's classical theorem supplies a fixed minimizing cyclic order at every central radius. A monotonicity argument transfers this order to the chain-radius problem. Full geometric feasibility requires every pairwise angular constraint. We give a self-contained criterion for feasibility of the canonical Supnick necklace on $\{k,\ldots,n\}$ at its chain root, expressed by one seam deficit. For every fixed $k$ the seam eventually fails and its failure persists. We prove the complete classifications for $k=1,2,3$, whose first failures occur at $n=8,13,17$, respectively. For the global infimum, we certify rational brackets $L_n<R^*(n)\le U_n$ of exact width $10^{-11}$ for every $3\le n\le14$. The lower proof combines independently enclosed angles, integer dynamic programming, and complete cyclic-order coverage; the upper proof uses exact rational Cartesian witnesses. The certificate does not depend on floating-point pruning in the numerical search. We distinguish these finite brackets and fixed-order theorems from numerical descriptions of floating circles and from unresolved claims about all optimal placements.
```

**Comments**

```text
18 pages. Streamlined the reproducibility statement, data availability and author declarations. Proofs and finite certificates unchanged. Standalone asymptotic sequel: arXiv:2609.13630. Source code and certificates: https://github.com/falker47/ringmin
```

Use the existing primary category `cs.CG`, with no cross-list. Retain MSC 2020 `52C26, 52C15, 05C85, 90C27` and the arXiv non-exclusive distribution license 1.0. Leave journal reference, external journal DOI and report number empty. The arXiv-issued DOI belongs to the existing record. The Zenodo DOI identifies the frozen software and certificate deposit. [Public metadata for v3](https://arxiv.org/abs/2607.28654v3)

## Why the page count changed between v2 and v3

The public v2 is 12 pages. Its main text presents the chain-order theorem, the earlier finite search and numerical results, with a correction of the v1 asymptotic conjectures. It includes two figures and an appendix of high-precision values and figures beginning on page 10. [Public v2 PDF](https://arxiv.org/pdf/2607.28654v2)

The 18-page v3 reorganizes the finite paper around two arguments. Section 5 (p. 4) states when the canonical chain satisfies the full constraints. Appendix A starts on p. 11 and runs into p. 18. It handles both parities and directed paths, the closing gap, small cycles, equality, and the rational comparisons that establish the three onset thresholds. Section 6 (pp. 5–7) supplies the exact lower-bound and witness arguments for the finite brackets. Appendix B (p. 18) gives the integer recurrence and the remainder bound used in the angle checks. The earlier figures and numerical appendix no longer occupy those pages. Expanded proof and certification content accounts for the main difference. Some space on pp. 9–11 also went to repeated provenance and declarations. The additions and removals rule out attributing the entire six-page difference to a single appendix or to the AI statement. [Public v3 PDF](https://arxiv.org/pdf/2607.28654v3)

The candidate still has 18 pages. Section 10 and the declarations now fit on pp. 9–10. Appendix A begins on p. 10, Appendix B on p. 17. Section 5 already points readers to the complete seam proof and §6.2 points to the exact cosine recurrence. Keeping both titles, both cross-references and both appendices preserves these routes from a claim to its proof. Keywords describe the packing problem, the two geometric fields, the tour and matrix structure, and certified computation. The four classifications provide a compact index consistent with the public arXiv metadata.

The revision puts the computational source pin, the separate archived release, the certificate-field digest, the full verification command and its evidence limits in §10. Data availability now points there directly. The declarations combine funding and competing interests and retain sole authorship. The AI disclosure names OpenAI ChatGPT/Codex, the five documented uses and the author's responsibility for the research, text, proofs and code. No new tool or personal attestation was added.

## Source and build checks

The [public v3 source tarball](https://arxiv.org/src/2607.28654v3) (SHA-256 `92cadeacb469db6947f4b5b74d2ab3bf8e4313927496ac98b350cd46b1288bf7`) is the baseline. Its main TeX hash is `a7a16560134d8882e7195f022348a47901f7f494befb1fdeb5f0bd3c3fe02794`. The candidate uses arXiv's published, normalized `00README.json` (pdfLaTeX, TeX Live 2025, one top-level manuscript). The following checks ran locally.

- An archive comparison found matching inventories. The arXiv configuration, both table inputs and the entire seam appendix are byte-identical to public v3. In the main TeX the prefix before §10 and suffix from `\appendix` through the bibliography are byte-identical. The intervening edits contain no mathematical displays, inline math or formal proof environments. The source pin, release commit, certificate-field hash, verifier command and reported check counts agree with v3. A separate run of the pinned verifier is recorded in the task dossier. It reproduced the existing check counts with exit 0 under Python 3.14.3.
- The ZIP passed its CRC check. Comparing decompressed bytes with `src/` matched all five members. Two fresh extractions each built with three identical passes of `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape ringmin_dcg.tex` from the extraction root. The environment used pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025), `SOURCE_DATE_EPOCH=1794268800`, `FORCE_SOURCE_DATE=1` and `TZ=UTC`. All six passes exited 0. Both final logs were free of unresolved references, LaTeX/package warnings, missing characters and overfull/underfull boxes. Both builds produced the same 18-page PDF.
- All 18 pages were rendered with Poppler. The page overview and enlarged views of pp. 9, 10 and 18 showed the verifier instructions, declaration block, appendix transition and bibliography within the page margins. The printed text in the source retains the same 11-point article class and 28 mm margins. All internal link actions in the PDF resolved to named destinations (108 destinations, 76 link annotations overall).
- The PDF contains 11 unique external URLs. Nine returned HTTP 200 on following redirects, including the pinned Git source and source map and the archived software DOI. The SIAM landing page and the Math Stack Exchange question returned 403 to automated HEAD requests. Crossref and the Stack Exchange API separately returned HTTP 200 with the matching cited article title and question ID/title, respectively. The portal's own compilation and preview are separate gates.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `paper_i_source.zip` | 24144 | `836f4c1b2735cb19bd8007bc12d561c9614891b2f020b1ed4f426f3355ac601d` |
| `paper_i.pdf` | 400445 | `9ce5881c45f6f28b45ab084fa5dffd5b4f1096a647a11d8956aa2ac233745377` |
