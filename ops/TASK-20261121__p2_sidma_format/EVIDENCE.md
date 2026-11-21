# Verification evidence

## Environment and inputs

Local Windows, Python 3.14.3, pdfTeX 1.40.28 and BibTeX 0.99d from TeX Live 2025. The build sets `SOURCE_DATE_EPOCH=1793664000` and `FORCE_SOURCE_DATE=1`. Both documents use the same dated SIAM class and unmodified BST. The build needs Python, `pdflatex`, `bibtex` and the standard packages loaded by the SIAM class. The review PDFs were generated locally. [SIAM release and file hashes](TEMPLATE_PROVENANCE.md)

The generating inputs are the new SIDMA sources in this commit, based on `7dcad4f6c40ff0e48eb53cb7a8c6f5622d361509`. The PR #4 package `paper_assets/paper_ii_journal/source_bundle.zip` has SHA-256 `99365502198e79003565adf3201dcbff5289ffd5a7713a690093db81788f5b9e`. Its S1 source is the mandated fallback in this worktree. The current class numbers the original v3 Proposition 7 as Proposition 7.1 of the integrated article.

## Local checks

| Command or check | Result | Property |
|---|---|---|
| `python paper_assets/journal_p2_sidma/build.py` | Exit 0. Main 10 pages, supplement 13 pages | Three interleaved pdfLaTeX passes per document and one BibTeX run for each. Both final logs have zero unresolved references or citations. The maximum reported overfull box is 0 pt for the article and 0.42084 pt for S1. |
| Second clean build in a fresh directory | Both PDFs byte-identical | Local reproducibility with the specified toolchain. |
| Poppler rendering and PDF annotation inspection | 23 pages rendered and inspected | Both figures, the dependency table, the article references and the S1 arithmetic displays fit. The external PDF link on article page 8 resolves to Theorem SM1.1 on S1 page 1, and the S1 link returns to Proposition 7.1 on article page 8. The companion link uses the local ZIP filename. |
| `python -m pytest tests/test_journal_p2_sidma.py` | 5 passed | Both complete scientific bodies, abstracts and notation definitions, figures, decimals, archive members, bibliography keys and DOI strings. The log gate rejects unresolved links and both vertical and horizontal overflow beyond 1 pt. |
| In-memory source mutations | Both rejected | Changing a plus to a minus in the main word-bound formula or changing one S1 endpoint digit fails the whole-body comparison. |
| `python -I -S paper_assets/line_upper/verify_line_certificate.py paper_assets/line_upper/certificates/p1_n03200.json` | Exit 0, `PASS p1_n03200.json n=3200 p=1 pairs=5118400 span=4531424532506678377/3200000000000000 B=140958576058/1000000000000` | Independent standard-library recomputation on the existing finite witness. |
| `python -I -S verify.py` in the extracted companion's `lower_supplement/` | Exit 0, `PASS certificate equals fresh rational recomputation`, `PASS manifest: 12 output hashes; 0 repository input hashes`, `PASS supplement checks; analytic proof supplies universal quantifiers` | Fresh rational and finite checks with the original standalone verifier. |
| `python -m pytest`, with `PYTHONPATH` set to the worktree's `src` | Exit 0, 108 passed, 1 skipped, 4 subtests passed | Full local suite. The pre-existing external profile-input test skips when the optional setup folder is absent. |
| `python -m pytest` in an isolated source copy with the five official profile reference fixtures | Exit 0, 109 passed, 4 subtests passed | Repeated the full suite with the Paper I bracket rows and the four quadratic certificates for sizes 3–6 from the existing profile worktree. The temporary copy preserved the repository path restrictions. |

The article abstract has one paragraph and 166 whitespace-delimited source tokens, counting inline mathematics. Its three decimal expansions match the reviewed macros. The acknowledgment text matches verbatim. The requested Claude reminder is a source comment.

## Artifact hashes

| File | SHA-256 |
|---|---|
| `main.pdf` | `279aa9bae7b661bc32167e1605b28fba247e187ac9df9b34409e944a50ebe2dc` |
| `supplement.pdf` | `3bc5dfcc41fe7957b8c9981729de001de75988e80a09440c7a11ee698afbfaac` |
| `s1_support.zip` | `6e083d0e8b52d6bd32d57859c946e38854cb637fd30695b3935307b605fdd33d` |

All 13 S1 archive entries match their PR #4 counterparts. The manifest checks the included historical source and PDF. The SIAM release comparison verified all 12 original upstream members and the separately downloaded documentation source. Figure hashes, statement fingerprints, equation-label inventories and ordered formula digests appear in the [mathematical comparison](../../paper_assets/journal_p2_sidma/MATH_DIFF.md).

## Scope and limitations

The mathematical-text and artifact comparisons are engineering checks. The finite verifier reruns independently reproduce the inherited certificates. The analytic proofs, the distinction between a feasible witness and a global result, and the certified bracket retain their original status. PDF byte reproducibility was checked on one TeX distribution. Independent editorial review is pending.

## Diff inspection

Inspection covered the scientific bodies against the pinned inputs, both bibliographies, shared setup, builder, regression tests, index and dossier. The two archived distributions were checked member by member. The added PDFs were rendered and compared to a second build. The authorized delta is confined to the new package, its one test module and this dossier. The arXiv-style source, PR #4 package, certificate inputs and verifiers, global ledgers, README and workflows are protected.

`git diff --check` and `git diff --cached --check` exited 0 with no output. All 20 staged paths were additions. Each staging-area blob matched its inspected file, with LF normalization for text. The protected-path comparison against the base exited 0 with no changes.
