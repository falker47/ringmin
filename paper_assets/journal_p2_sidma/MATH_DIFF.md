# Mathematical comparison

The SIDMA port preserves the reviewed mathematical text of the article and S1. The regression test compares the entire scientific body of each document, including the proofs, quantifiers, prose constants, tables, figure captions and data-availability instructions. It also compares both abstracts and every notation definition. It reads the source documents directly and pins their SHA-256 digests after LF normalization. [Comparison test](../../tests/test_journal_p2_sidma.py)

| Reviewed source | SHA-256 |
|---|---|
| Paper II, PR #11, `7dcad4f6c40ff0e48eb53cb7a8c6f5622d361509` | `18f810d43aecb651c9c529583d9aabba796d093cac0e73be050dfef587d42c40` |
| PR #4 source bundle, `lower_supplement/supplement.tex` | `ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4` |

## Scope of the comparison

The only change inside a mathematical expression is an optional line break after the comma in the reflected-block cost interval. The article abstract spells out its three decimal macros and the symbol for the limiting coefficient. Their expansions match the reviewed definitions exactly. All other formula tokens, labels and their order match, including formulas without numbers.

The source comparison permits the two SIAM paragraph headings, one supplemental theorem link, the author’s LaTeX comment, the page break before the article references, and S1’s typesetting of one filename and link to the companion ZIP. The class supplies the running heads, numbering, bibliographic layout and supplementary title. The earlier arXiv Proposition 7 remains identified as such. Its counterpart here is Proposition 7.1, linked in both directions to Theorem SM1.1.

The ordered SHA-256 digests below use complete formula strings separated by a newline. Counts treat each inline dollar pair and each outer display as one expression. A multiline alignment counts as one display and may own several equation labels. Section totals include formulas in captions and tables. Hashes in the statement tables are the first 16 hexadecimal digits of the SHA-256 of the full environment.

## Article

| Section | Inline | Displays | Equation labels |
|---|---:|---:|---|
| Abstract | 13 | 0 | — |
| The minimum central circle | 27 | 0 | — |
| Exact Angular Comparison | 39 | 5 | `eq:theta`, `eq:line`, `eq:recurrence`, `eq:squeeze` |
| Existence by Genuine-Label Concatenation | 26 | 2 | `eq:limit`, `eq:copies` |
| A finite linear-programming characterization | 53 | 5 | `eq:types`, `eq:lp`, `eq:effective` |
| Prescribed radius profiles | 115 | 8 | `eq:profile-squeeze`, `eq:profile-change` |
| A certified upper bound | 22 | 2 | — |
| An Explicit Global Lower Endpoint | 34 | 4 | — |
| Finite values and open questions | 6 | 0 | — |
| Data and code availability | 1 | 0 | — |
| Acknowledgment | 0 | 0 | — |

The 336 inline formulas and 26 displays have 11 equation labels. The complete ordered formula digest is `5df909405130525e0f1bb70d8cc5e9c7a89f6881e702e3f7abac0b49c16daeaa`.

| SIAM statement | Source label | SHA-256 prefix |
|---|---|---|
| Definition 2.1 | `def:line` | `4efe2b38b6398fb4` |
| Lemma 2.2 | `lem:closing` | `c4b9b2378b10a056` |
| Lemma 2.3 | `lem:squeeze` | `6acd3c9e5e01ea67` |
| Theorem 3.1 | `thm:existence` | `fefec4b3f6ac8708` |
| Theorem 4.1 | `thm:lp` | `23e201ab4d5be92c` |
| Lemma 5.1 | `lem:profile-squeeze` | `f61ffbf871636523` |
| Lemma 5.2 | `lem:profile-copy` | `0179f47ecab25bf2` |
| Theorem 5.3 | `thm:profile-law` | `e07d717097f7a049` |
| Theorem 5.4 | `thm:profile-words` | `b93470b6637d53bc` |
| Corollary 5.5 | `cor:profile-adjacent` | `5524b387d8cde5d0` |
| Corollary 5.6 | `cor:profile-powers` | `5ad983556f21906f` |
| Proposition 6.1 | `prop:cert-upper` | `c018867fa6f5fb4d` |
| Remark 6.2 | Unlabelled reflected-block remark | `34db57f60578a0d7` |
| Proposition 7.1 | `prop:lower` | `51bd14ed243f5c7f` |

All 14 formal statements and all 12 proof environments are present in order.

## S1

| Section | Inline | Displays | Equation labels |
|---|---:|---:|---|
| Abstract | 1 | 1 | — |
| Statement, notation and proof dependencies | 17 | 3 | `eq:parameters`, `eq:Di`, `eq:objective`, `eq:mainbound` |
| Angular geometry and deletion (L1) | 24 | 3 | `eq:kernel`, `eq:sandwich` |
| Exact terminal parameters (L2) | 25 | 3 | `eq:J` |
| One outer order, its dual and its energy (L3) | 36 | 8 | `eq:gridgate`, `eq:dual`, `eq:E`, `eq:measure`, `eq:marginals` |
| Signed deletion, seams and finite errors (L4) | 99 | 12 | `eq:cutgate`, `eq:43`, `eq:54`, `eq:floorerrors` |
| One shared crossing budget (L5) | 21 | 2 | `eq:shared` |
| Finite minimax and transfer to the global problem (L6) | 31 | 6 | `eq:finitegates`, `eq:globalfinite`, `eq:finite` |
| The unique global width optimum (L7) | 33 | 6 | `eq:G`, `eq:Gprime`, `eq:zbracket`, `eq:cubiccertificate` |
| Reproducible rational arithmetic (L2 and L7) | 46 | 12 | — |
| The ordered passage to the limit (L8) | 26 | 5 | `eq:fixedlimit`, `eq:liminf` |
| Existence of the global limit | 53 | 5 | `eq:line`, `eq:bB`, `eq:globalsqueeze` |
| Verification scope and provenance | 1 | 0 | — |

The 413 inline formulas and 66 displays have 29 equation labels. The complete ordered formula digest is `254a450ad05a863106c86c63f305c8e5fdce973d610ecf97ed1441ba69ff64b7`.

| SIAM statement | Source label | SHA-256 prefix |
|---|---|---|
| Theorem SM1.1 | `thm:main` | `81b7211e3a92c3a4` |
| Lemma SM2.1 | `lem:sandwich` | `16752860ecafaa3f` |
| Lemma SM2.2 | `lem:deletiongeometry` | `a57a7fe8ca590869` |
| Lemma SM3.1 | `lem:terminal` | `5ecd71e2f57c59d7` |
| Lemma SM4.1 | `lem:dual` | `31f7cd37ca081dcf` |
| Lemma SM5.1 | `lem:strip` | `c7df31e0882f441a` |
| Lemma SM5.2 | `lem:variation` | `3077bfe036617002` |
| Lemma SM5.3 | `lem:54` | `70c30140f9c5a977` |
| Lemma SM5.4 | `lem:floors` | `520b38551edd4153` |
| Lemma SM6.1 | `lem:crossing` | `308d3c2fe366a637` |
| Proposition SM7.1 | `prop:finite` | `8d168dc22ef093d1` |
| Lemma SM8.1 | `lem:KKT` | `575856051a570b4c` |
| Lemma SM11.1 | `lem:existence` | `91149114c9fa6eec` |

All 13 formal statements and all 12 proof environments are present in order.

## Constants, figures and auxiliary evidence

The reviewed decimal definitions are `0.1405694688`, `0.140958576058` and `0.088581212993`. Both copies of `numbers.tex` have SHA-256 `41ac4263b42657c41427114c80ebec4f7fb1c180363cd349ea7ca6d6fc9c8cea`. The full-text comparison also covers constants outside math mode, the rational endpoints in S1, the finite-error coefficients, the width constraints and every entry of the certificate array and L1–L8 dependency table.

| Figure | PDF shared by both versions | SHA-256 |
|---|---|---|
| `fig:line` | `line_geometry.pdf` | `8486eed978e53d766fe4314616dd6081086f657859c44ddd39348fd796131726` |
| `fig:finite` | `finite_brackets.pdf` | `da886372abc670f60c6a66fce49b1b5db1e811956649c6e8b912730987c5b40b` |

S1 has no external figures. The 13 entries in its companion ZIP are byte-identical to the corresponding frozen package entries. SIAM BibTeX retains all 12 article references and 5 S1 references, including the original 12 DOI values in the article.

Run `python -m pytest tests/test_journal_p2_sidma.py` from the repository root to repeat the source, figure, certificate-input and bibliographic checks. The analytic results and finite certificate claims retain their classifications from the reviewed sources.
