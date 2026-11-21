# SIAM template provenance

On 21 November 2026 the SIDMA author instructions specified a one-paragraph abstract of at most 250 words, inline figures, and a supplementary-materials index describing and justifying each item. The SIAM author resources listed the standard journal macros and separate article, supplement and shared-information templates. These are live, undated policy pages. [SIDMA author instructions](https://epubs.siam.org/journal/sidma/instructions-for-authors) · [SIAM journal author resources](https://epubs.siam.org/journal-authors)

## Source bytes

SHA-256 values below are of the downloaded bytes or, for archive members, the uncompressed member bytes. The bundle release is 16 December 2025. The class declares version 1.4.8. The shared, article and supplement examples carry the bundle version. The BST header identifies the January 1988 style and records its latest change on 20 November 2018. The HTML template is undated.

| Official file | SHA-256 |
|---|---|
| [Standard distribution ZIP](https://epubs.siam.org/pb-assets/macros/standard/siamart_251216.zip) | `b0caa37505e7de560ce7c59f9644baec9283f61b6b445fa44bd09e4f0bfaca6a` |
| [siamart251216.cls](https://epubs.siam.org/pb-assets/macros/standard/siamart251216.cls) | `33f2eb091c8bcbda9baed2e868489460da868047b0a518b4ce1b2f2c15fda530` |
| [siamplain.bst](https://epubs.siam.org/pb-assets/macros/standard/siamplain.bst) | `a5df7c482dc7d4459f08b91c28437c3779284dcd82591acf1c977de7508ac6c7` |
| [ex_article.tex](https://epubs.siam.org/pb-assets/macros/standard/ex_article.tex) | `a8d64b565e6e31aee347eb653f27c2494db8ce18246300cacd5622b153eabed0` |
| [ex_shared.tex](https://epubs.siam.org/pb-assets/macros/standard/ex_shared.tex) | `b66df18ceda54ec909d1c8d619709cbb7623d40f57e33c03015825f7b42fc6f5` |
| [ex_supplement.tex](https://epubs.siam.org/pb-assets/macros/standard/ex_supplement.tex) | `18c0bc6af1dc1313a27f31aabd8e883efbdc635497d68be69e74671eba04a385` |
| [docsiamart.tex](https://epubs.siam.org/pb-assets/macros/standard/docsiamart.tex) | `99da5fb774a55fd982ddf5eea88f7555dba5930f4980c16ae7a65cdf220586e5` |
| [SMindex.html](https://epubs.siam.org/pb-assets/files/SMindex.html) | `4adc05bd2c14cb5b47b05dd20222e7a592c6e83d5ff293a57c01403d3a0b6f02` |

## Local distribution and use

The official ZIP was 1,205,515 bytes and contained 12 members. The class header requires distribution with its companion documentation source. SIAM publishes that source separately and omits it from the ZIP. The repository copy contains every original member byte-for-byte plus SIAM's standalone `docsiamart.tex`. The 13-member ZIP has SHA-256 `9883890f66dbf64ff57bd94a207b51c5991fc8751d39b40ef6bf3484b3ea8b8f`. The build verifies this digest and reads the original class and BST from the archive. [Vendored distribution](../../paper_assets/journal_p2_sidma/siamart_251216.zip)

The two source files use the official review options and import each other's labels with `\externaldocument[prefix][nocite]{file}`. Prefixes keep the two local `eq:line` labels distinct. A shared file supplies author information and the running title. The article uses the repository's previously published Paper I contact address. [Published author block](../../paper_assets/ringmin_paper.tex)
