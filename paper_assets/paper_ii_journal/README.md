# Paper II: Author Review Package

This separate journal manuscript of arXiv:2609.13630 is the 3 November 2026
editorial candidate for the author's review. The next journal is not selected.
JoCG submission #6357 was declined after preliminary assessment on 28 October;
the supplied decision record contains no specific mathematical objection.
The 24 October JoCG preparation remains historical provenance.

Start with [main.pdf](main.pdf), then read S1 and S2 for the complete endpoint
proofs. [CLAIM_PROOF_MAP.md](CLAIM_PROOF_MAP.md) maps the logical dependencies;
[REVIEW_COVERAGE.md](REVIEW_COVERAGE.md) consolidates the four component reviews,
their exact revisions and their limits. [READINESS.md](READINESS.md) separates
those inherited reviews from verification of this editorial revision.
[EDITORIAL_CHECKLIST.md](EDITORIAL_CHECKLIST.md) identifies the remaining author
decisions. [EDITORIAL_REQUIREMENTS.md](EDITORIAL_REQUIREMENTS.md) records the
current official requirements of the proposed venues without selecting one.

## Package Index

| Item | Role |
|---|---|
| main.tex / main.pdf | Model, global-limit and finite-word LP proofs, endpoint theorems |
| S1: Proposition 7 supplement | Preserved lower-endpoint proof L1--L8, rational certificate and checkers |
| upper_supplement.tex / upper_supplement.pdf (S2) | Reflected-block transfer, implicit parameters and fourth-block saving |
| REVIEW_COVERAGE.md | Dated component-review coverage and transfer to this editorial revision |
| EDITORIAL_CHECKLIST.md | Verified metadata, existing AI disclosure and author-only decisions |
| checks/ / verify_math.py | Bounded arithmetic and recovery checks; no test replaces an all-n proof |
| build.py / BUILD_REPORT.json | Isolated builds, actual TeX input hashes and preserved S1 delivery metadata |
| verify_package.py / MANIFEST.json | Delivered-file integrity and source/package identity |
| source_bundle.zip | Portable sources, PDFs, documentation, checkers and unchanged S1; internal manifest |

In a checkout, S1 is [the existing package](../asymptotic_sequel/proposition7_supplement/README.md),
pinned to `75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae`. In the ZIP it is copied
byte for byte into `lower_supplement/`. No old ops dossier is needed to read
or execute the scientific package. Private review links document provenance;
the proofs and executable checks are included locally.

## Reproduce

Python >=3.11 and pdfLaTeX with standard packages, including lineno, suffice
for builds and endpoint arithmetic. SciPy is needed only by the optional
word-LP discovery/checker. From this directory or an extracted archive:

```sh
python -I -S verify_package.py
python -I -S check_reproducibility.py
python -I verify_math.py --with-lp
```

The aggregate arithmetic command runs S1 and its integrity controls once,
line recovery, the five upper checkers and the rational LP cases. Omit
`--with-lp` and use `-I -S` for a standard-library-only replay.

The builder uses three no-shell-escape passes in a fresh external temporary
directory for each standalone source and rejects unresolved references,
missing characters and box warnings. It records actual input and output
hashes. The reproducibility command builds each document twice and requires
identical results within that environment, without changing delivered files.

Main and S2 were regenerated with the environment recorded in BUILD_REPORT.json.
S1's original TeX Live 2025 PDF is deliberately preserved. Its new TeX Live 2023
check build has different bytes; the report records both digests and explicitly
marks the difference. S1's original manifest still binds its delivered bytes.
`check_reproducibility.py --require-delivered` remains a stronger optional check
requiring all three delivered PDFs to match fresh builds. It fails for S1 in
this mixed-provenance package; this is not recorded as a passing gate.

To author a later revision, run `python build.py`, finalize package documentation,
then run `python build.py --export`. Re-export after any packaged file changes.
CI checks package integrity and aggregate mathematics; the separate push-only
LaTeX job checks repeated builds in its own environment, with no publication or
artifact upload. Exact-commit CI evidence belongs in the draft PR handoff.

## Scientific and Editorial Scope

This revision makes the total permutation J explicit and updates documentary
state. Results, constants, abstracts, S1 and the public arXiv sources are
unchanged. Neither endpoint is claimed sharp, and no new finite optimum or
efficient high-precision algorithm is claimed. The component reviews are
internal AI-assisted evidence, not external peer review or approval of the
whole PR. Merge, Registry promotion, arXiv replacement, journal submission and
editor communication remain separate decisions.
