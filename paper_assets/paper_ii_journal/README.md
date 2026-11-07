# Paper II: Author Review Package

This separate journal manuscript of arXiv:2609.13630 includes the local
7 November 2026 prose revision of the 3 November author-review candidate. The next journal is not selected.
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

## Approved Prose Refinements - 7 November 2026

The abstract and narrative transitions in main.tex have been revised for
readability. All mathematical expressions, statements, proofs, the entire
lower-endpoint section, references and AI acknowledgment are preserved.
S1 and S2, including their sources, PDFs and checkers, remain byte-identical
to the 3 November baseline. Their previous build/review evidence is inherited,
not rerun here. The current main PDF has its own environment record in
BUILD_REPORT.json; top-level historical environment fields still describe
the inherited supplement records.

See the [earlier editorial report](../../ops/TASK-20261107__two_paper_editorial_review/PAPER_II_REPORT.md)
and [current verification evidence](../../ops/TASK-20261107__two_paper_approved_refinements/EVIDENCE.md).
The approved follow-up clarifies finite-word convergence, endpoint provenance
and the two references to prescribed normalized radii.
Run `python ops/TASK-20261107__two_paper_approved_refinements/approved_build.py build`
from the repository root for repeated main-only builds and delivery.
For export, copy that task wrapper to an ignored work directory outside this
package and run its `export --root <repository-root>` mode. It preserves every
supplement byte and records the current main compiler separately from inherited
supplement contexts in both manifests. The earlier general authoring
commands below rebuild all documents and are not this task's generation route.
This local review does not update the existing PR or the original branch.

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

At the 3 November freeze, main and S2 were regenerated with TeX Live 2023.
S1's original TeX Live 2025 PDF was preserved; that recorded TeX Live 2023
check build had different bytes. BUILD_REPORT.json retains those historical
supplement records, including both S1 digests and the explicit difference.
This prose revision rebuilds only main with its separately recorded environment.
S1's original manifest still binds its unchanged delivered bytes.
`check_reproducibility.py --require-delivered` remains a stronger optional check
requiring all three delivered PDFs to match fresh builds. The recorded
3 November TeX Live 2023 replay failed that stronger gate for S1. It was not
rerun in this prose task; no current all-document build result is claimed.

To author a later revision, run `python build.py`, finalize package documentation,
then run `python build.py --export`. Re-export after any packaged file changes.
CI checks package integrity and aggregate mathematics; the separate push-only
LaTeX job checks repeated builds in its own environment, with no publication or
artifact upload. Exact-commit CI evidence belongs in the draft PR handoff.

## Scientific and Editorial Scope

The 3 November revision made the total permutation J explicit and updated
documentary state. This 7 November revision changes only main-manuscript prose
and its synchronized outputs. Results, constants, formal arguments, S1, S2
and the public arXiv sources are unchanged. Neither endpoint is claimed sharp, and no new finite optimum or
efficient high-precision algorithm is claimed. The component reviews are
internal AI-assisted evidence, not external peer review or approval of the
whole PR. Merge, Registry promotion, arXiv replacement, journal submission and
editor communication remain separate decisions.
