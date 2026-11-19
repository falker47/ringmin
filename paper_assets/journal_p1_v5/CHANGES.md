# Editorial changes for the Paper I journal draft

This version is a draft for the Journal of Global Optimization. The source is arXiv:2607.28654v4. Its arXiv archive SHA-256 is `e5d499657a47cea462fcaedae78f2dab1eb69f594315cd91aa9a61c71b5081ab`.

| Change | Purpose and check |
| --- | --- |
| New title, abstract and introduction | The opening gives the strict lower and feasible upper endpoints, their exact width and finite range, followed by the two proof obligations. The abstract contains 156 whitespace-delimited words. |
| Related work | Sixteen cited records have DOI checks, including the six original references. Equal-circle packings in a square, unit squares in a circle, shelf packing, contact graphs and exact computation explain the relationship to global optimization. All bibliographic links are active DOI links in the PDF. |
| Structural results | The adjacent-chain theorem and the seam theorem now lead from the geometric relaxation to finite global exclusion. Every original quantified statement is retained. The complete seam proof and numerical table inputs are transcribed from v4. |
| Six figures | Each panel has a caption and source. Figures 2 and 3 show the transition from a feasible closing chain to a forced overlap. Figure 4 highlights the two disks from the historical numerical description and independently checks all strict distances at the upper endpoint. |
| Finite and asymptotic results | The figure of normalized brackets compares the finite intervals with the companion paper's rigorous lower bound on the limiting constant. Its upper endpoint remains the requested visible macro placeholder. |
| Scope paragraph | The final discussion distinguishes an individual reconstruction, existence of slack at an optimum, and universal contact claims. Quantifiers in the formal results and in the reconstruction table stay with the claims. |
| Reproduction details | One Data and code availability section gives the pinned verifier revision, release DOI, exact certificate digest, Python requirement and full verifier command. References precede the appendices. |
| Author and declarations | The original author, affiliation, contact, manuscript date, and Statements and Declarations (including the AI-use paragraph) are preserved. |

The v4 and draft texts contain **53 and 7** counted negations, respectively. Count case-insensitive whole words `no, not, never, none, neither, nor, without, cannot` in the TeX source from the start of the abstract through the end of the main text before Statements and Declarations. Exclude line comments and the URL arguments of `href` and `url`. Proofs, captions and table text in this interval are included. The appendix and declarations have their own transcription controls.

The DOI metadata correct the proposed author order for the square-in-circle article to Montanher, Neumaier, Markót, Domes and Schichl. The online publication year is 2018 and the journal issue year used in the bibliography is 2019. Crossref's record for the proposed Szabó monograph lacked author metadata, including the first chapter record. The cited chapter by Szabó, Csendes, Casado and García instead has a verified author list and covers bounds for equal-circle packing. The title search for the proposed Stephenson book returned reviews. Its scope is covered here by the verified primary circle-packing paper of Collins and Stephenson.

Build from the repository root with `python paper_assets/journal_p1_v5/make_figures.py`, then `python paper_assets/journal_p1_v5/build.py`. The builder performs three passes in a new temporary directory and validates the final log and A4 page count. This instance has **18 pages**, with the appendix beginning on **page 11**, hence **10 main-text pages including references**, and zero overfull boxes. See [claim mapping](CLAIMS_DIFF.md), [reference checks](refs_verification.json) and [figure provenance](figures/README.md).
