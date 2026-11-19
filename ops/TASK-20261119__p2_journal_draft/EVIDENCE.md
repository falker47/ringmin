# Evidence

## Environment and provenance

The local base is `codex/paper-ii-journal-candidate@7d257221d9034ca5f895f062e45e782d8e77b6c2`. Windows, CPython 3.14.3, Matplotlib 3.10.9, pytest 9.0.2 and pdfTeX 1.40.28 (TeX Live 2025) were used. Poppler supplied pdfinfo and pdftoppm. The generation programs and outputs are in the same commit.

| Official read-only source or output | SHA-256 |
|---|---|
| Paper II v3 main.tex | `792473ac5b2f0b39bcf9bb3e0d0d576c70aa42bc55c941bc914e4eb8354e98e4` |
| S1 lower_supplement/supplement.tex | `ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4` |
| S2 upper_supplement.tex | `941d6ae995a7f7f23ab80f7db73d1a73c1c2d9ed97d160cd35e95bcfd2c6cb42` |
| Paper I v4 bracket_rows.tex, copied verbatim | `58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1` |
| Journal draft main.pdf | `485bbabf97fc04cd47f39f4c8229653ab50112adc2bcf6de78654e038b58eee5` |
| Figure 1, line_geometry.pdf | `8486eed978e53d766fe4314616dd6081086f657859c44ddd39348fd796131726` |
| Figure 2, reflected_cells.pdf | `049a3be2ae69a06403512e6a61abf247998a2fd6b60d8ec62b1fc6dc79ee4ea3` |
| Figure 3, finite_brackets.pdf | `c84eae499caa7db4421b3ecfa4bd236ab1cea3b1c646046ee15c22908de9dd52` |

## Classification

| Claim | Classification and evidence | Scope |
|---|---|---|
| Limit, finite-program bound, reflected-block transfer and explicit lower bound | Existing exact theorems and proved corollaries in Paper II v3 and its supplements. See [claim map](../../paper_assets/journal_p2_v4/CLAIMS_DIFF.md). | This branch audits equivalence of the journal presentation. |
| Lower display endpoint and width example at k = r = 64 | Proved arithmetic corollaries, checked by rational inequalities. | The LP example precedes the directed arithmetic contribution. |
| Displayed finite intervals | Existing computer-certified finite results from Paper I v4. Exact widths and normalization verified from the pinned table. | Data illustration for twelve finite sizes. |
| Bibliography, figure replay, build and source fidelity | Engineering facts from local checks below. | PDF bytes can depend on the TeX and Matplotlib versions. |
| Potential profile extension | Separate mathematical work under review. | Mentioned only as a conditional alternative title in the editorial note. |

## Commands and independent checks

All commands executed locally. Temporary directory arguments below are abbreviated as TEMP.

| Command or operation | Exit and material output | Property |
|---|---|---|
| Read-only Crossref work API, DOI.org Handle API and arXiv metadata | HTTP 200 on the final individual records. Twelve distinct DOIs, complete citation coverage. | Each citation has title, authors, year, venue, verification URL and status. The DOI for Paper II identifies the deposit containing S1 and S2. |
| Direct arXiv checks of v1 and the Walters locator | Exact original conjecture found in `ringmin_paper.tex`; arXiv:1209.6458 points to Walters Theorem 4.9 for Fekete's lemma. | Attribution and textbook locator. |
| `python paper_assets/journal_p2_v4/make_figures.py` | 0, three PDF hashes above. | Deterministic rendering of the two schematics and the finite comparison plot. |
| Same generator with `--brackets .codex_inputs/arxiv/p1_v4/bracket_rows.tex --output TEMP` | 0, three IDENTICAL_FIGURE outputs. | Exact replay from the independent original table. |
| `python paper_assets/journal_p2_v4/build.py`, then with `--output TEMP/main.pdf` | 0 and 0, BUILD_PASS pages=9 passes=3 unresolved=0 overfull=0; IDENTICAL_PDF. | Isolated three-pass compilation, nine pages including references, identical output. |
| CPython independent source comparison and rational checks | 0, FULL_FORMAL_STATEMENTS_PRESERVED 7, ABSTRACT_WHITESPACE_TOKENS 129, EXACT_LOWER_ROUNDING_AND_WIDTH_EXAMPLE_PASS and EXACT_FIGURE_MODELS_PASS 12. | Full source statements differ only by documented editorial allowances. Exact rational comparison covers the lower decimal, geometry of two mutually tangent disks, rank reversal, normalized finite widths and the illustrative LP width. |
| `python -m pytest` | 0, 73 passed, 4 subtests passed in 56.21s. | Entire local repository suite, including T5 and its negative build controls. |
| `python -B -m pytest -q tests/test_journal_p2_v4.py -p no:cacheprovider` | 0, five tests, 100%. | Abstract number guard, DOI coverage, v3 source digests, deterministic figures/optional numeric upper line and build failures on missing figures or unresolved citations/references. |
| `pdftoppm -png` on the final manuscript and the figure PDFs | 0, nine pages and three individual figures rendered and inspected. | Visual check of the math, label placement, page transitions, captions and bibliography. |

## Negative results, diff and review limits

The default sandbox DNS lookup and one Crossref rate-limited query required a permitted retry. An optional caption package was unavailable. Native article captions produced the verified build. The command-size limitation during file delivery was resolved by writing separately scoped groups.

The complete new text, JSON records, TeX, scripts, tests and manifests were reviewed directly. All four generated PDFs were rendered, byte-replayed and hashed. An explicit untracked-file scan checked whitespace, final newlines and UTF-8 in every new text file. The repository-wide figures/ ignore rule also covers the new figure folder. Its five authorized files are individually staged by explicit path. Git's staged and base-relative path/whitespace checks complete the scoped audit. No original tracked content is part of this delta.

The placeholder is intentional. The journal draft adds no new numerical upper claim. The manuscript has received no external peer review through this workflow. Hosted CI and submission remain outside the local branch checks.
