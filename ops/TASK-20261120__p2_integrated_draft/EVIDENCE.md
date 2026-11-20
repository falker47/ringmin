# Integration evidence

## Environment and inputs

Local Windows 11 x64, CPython 3.14.3, pytest 9.0.2, Matplotlib 3.10.9,
NumPy 2.4.3, SciPy 1.17.1, pdfTeX 1.40.28 (TeX Live 2025) and Poppler.
Tests used the integration tree's `src` on `PYTHONPATH`. The PDF builder
fixes the source epoch and performs three passes in a fresh directory.
The generator sources and their final PDFs belong to the same integration commit.

| Ref or input | Revision |
|---|---|
| PR target, codex/paper-ii-journal-candidate | `7d257221d9034ca5f895f062e45e782d8e77b6c2` |
| PR #10, journal base | `3a5c3c91fb9d744d90ca6776f41bb7704fd1a2c7` |
| PR #6, finite placements | `eb9467dfa1429d622402e26e2f33017f984d2b1f` |
| PR #8, profile proof | `f2f46294a1cfb869b36ecc147d5b19df432214b3` |
| First merge | `a5d350814cbaba982c90896b034dbb8f00096722` |
| Second merge, comparison tree for editorial changes | `9b5e38122a198e710fa9a527bee4478bd9faa5f8` |

Both merges used `git merge --no-ff --no-edit` on the named remote-tracking
branches, with exit 0 and the ort strategy. Each has its intended two
parents. For each merge, the output of
`git diff-tree --no-commit-id --raw --no-abbrev -r <first-parent> <merge>`
matched the same command from the PR target to the incoming tip byte for
byte, including object IDs and file modes. Counts were 35 paths for PR #6
and 14 for PR #8. The integration worktree was clean after both merges.

## Mathematical evidence

| Result | Classification and source | Check and scope |
|---|---|---|
| Limit of bounded empirical laws, finite geometric squeeze and quantile word bracket | Exact theorems with written proofs in [PR #8's note](../../research/PROFILE_GENERALIZATION.md). | Checked the hypotheses, zero marks, both arcs, donor domination, sorted square-root matching, equal indexed counts and word-joining cost against the authoritative note. Finite controls support individual steps. |
| Power-profile limit and adjacent-pair lower bound | Proved corollaries of the profile theorem and rearrangement. | For p=2 the reverse-quantile integral is ∫₀¹ t(1−t) dt = 1/6. Dividing by π gives the lower bound on C₂. |
| Two strict upper bounds | Proved corollaries using independently checked finite rational placements. | All-pairs line feasibility and the strict decimal comparisons certify each witness. The respective finite-template infimum transfers the bound to the limiting coefficient. |
| Lower endpoint and historical four-block comparison | Published analytic lower theorem with directed enclosure in S1. Certified cost for the specified rational parameters in [PR #6](../../paper_assets/line_upper/NOTE.md). | Replayed S1 and the Arb enclosure. The rational cost and the implicit v3 parameter choice are distinct. |

The separate 20 November review outside Codex was reported by the author.
It used an independent all-pairs implementation and an Arb lower bound for
π. The checks below are fresh local runs. External human mathematical
review of the profile theorem is pending.

## Commands and results

Commands below start at the repository root. Both individual certificate
commands printed in the manuscript are supported by the same verifier.
`TEMP` denotes a fresh output directory.

| Command | Exit and observed result |
|---|---|
| `python -I -S paper_assets/line_upper/verify_line_certificate.py paper_assets/line_upper/certificates/p1_n03200.json paper_assets/line_upper/certificates/p2_n03200.json` | 0. Both PASS lines appear below. This standard-library verifier reads coordinates directly and checks all pairs independently of the search. |
| `python -I -S verify_global_brackets.py` | 0. `PASS_GLOBAL_BRACKETS`, pinned inputs PASS, 47 witnesses and 3,374,988,556 order classes covered for the Paper I scope. |
| `python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/verify.py` | 0. `PASS certificate equals fresh rational recomputation`, 12 manifest output hashes and seven repository input hashes. |
| `python paper_assets/line_upper/block_antiderivatives.py` | 0. `RATIONAL_BLOCK_ARB 0.14191330499527 0.14191330499528`; the separate implicit U₄ enclosure was [0.141895293745, 0.141931316245]. |
| `python -I -S paper_assets/paper_ii_profiles/checks/verify_finite.py --sources INPUTS` | 0. 754 matching cases, 70 copy bounds, 480 placements, 16 squeeze comparisons, 225 stability checks, 12 word LPs, 16 source brackets, `PASS_PROFILE_FINITE`. INPUTS was the cached PR #8 reference directory. |
| `python paper_assets/journal_p2_v4/make_figures.py` | 0. The shelf PDF is byte-identical to PR #10. The two-panel finite-bracket plot matches both certified macros. |
| `python paper_assets/journal_p2_v4/build.py` | 0. `BUILD_PASS pages=10 main_pages=9 passes=3 unresolved=0 overfull=0`. Main text ends with §8 on page 9, followed by data availability. Acknowledgment and references are on page 10. |
| `python paper_assets/journal_p2_v4/build.py --output TEMP/main.pdf` and `python paper_assets/journal_p2_v4/make_figures.py --brackets INPUTS/arxiv/p1_v4/bracket_rows.tex --output TEMP/figures` | Both 0. The fresh PDF and both figures matched the delivered files byte for byte. INPUTS here was the extracted PR #10 copy of the official source. |
| `python -m pytest` in the integration worktree | 0. `103 passed, 1 skipped, 4 subtests passed in 64.56s`. The optional external-source test skips when its input folder is absent. |
| `python -m pytest` in a temporary copy of the same sources with the five optional inputs | 0. `104 passed, 4 subtests passed in 65.46s`. The fixtures were the original Paper I bracket table and four pinned small-n data files used by PR #8's existing test. |
| `pdftoppm -png -r 95 paper_assets/journal_p2_v4/main.pdf TEMP/page` | 0. Inspected all ten rendered pages, including theorem and table layout, both figures, the verifier commands and references. A separate 160 dpi render checked the numerical labels on the enlarged band. |

~~~text
PASS p1_n03200.json n=3200 p=1 pairs=5118400 span=4531424532506678377/3200000000000000 B=140958576058/1000000000000
PASS p2_n03200.json n=3200 p=2 pairs=5118400 span=9108638531/10240000 B=88581212993/1000000000000
~~~

## Source fidelity and artifact hashes

Compared the six retained complete statement environments directly against
PR #10 after newline normalization. From the cached official v3 TeX,
the nine surviving numbered equations and seven other displays reproduce
the independent digests in the regression test. The author and date
commands and the full acknowledgment text match v3 and PR #10. Neither
source declares a separate affiliation. PDF extraction independently found
all three decimal macros on page 1, plus the intended title and author in
its metadata.

| SHA-256 input or output | Digest |
|---|---|
| Official v3 main.tex | `792473ac5b2f0b39bcf9bb3e0d0d576c70aa42bc55c941bc914e4eb8354e98e4` |
| Profile proof note, Git blob contents | `8dca4e741405a0017c6dbfe0ccffbeab42ce80885232a53fb070ef18280f4dd4` |
| Linear witness, Git blob contents | `e48c671bad569202c13dbcdcd86487b35e75f141190c4082136a2602fd1dcdfb` |
| Quadratic witness, Git blob contents | `10282bd9c8e7d36ef038436d37cea364f13218556228ca1266a93ade9cd15807` |
| Isolated line verifier, Git blob contents | `42015b4fc74083868767092d71bfc97891db26e99bac434d53ec5594aa9083ab` |
| Paper I bracket table, LF | `58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1` |
| Preserved S1 PDF | `a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568` |
| Integrated main.pdf | `ce31fc74366d148d24ebff99e4eece4b5211d5a683b5f29f6f69bccc16c48eaa` |
| line_geometry.pdf | `8486eed978e53d766fe4314616dd6081086f657859c44ddd39348fd796131726` |
| finite_brackets.pdf | `da886372abc670f60c6a66fce49b1b5db1e811956649c6e8b912730987c5b40b` |

The raw Windows text checkouts may use CRLF. The table marks Git content
hashes explicitly. The frozen PDFs are reproducible in the stated local
environment. Other TeX, font or plotting installations can yield different bytes.

## Negative controls and diff inspection

The initial build exposed one 66.63 pt overfull line in the historical
remark. Allowing a break between slab lengths removed it. The build tests
reject unresolved references, citations, and missing figures. Separate TeX
fixtures accept 14 main pages plus a reference page and reject 15 main
pages. The figure test reads the actual band coordinates on both axes and
changes both endpoint macros to check their propagation.

The post-merge editorial paths comprise eleven journal-package files, the
journal test, and three dossier files. The previous reflected-cell PDF
leaves with its source section. S1, the archived paper packages, the new
input packages, research, global status, ledgers, README and workflows
were compared against the second merge. The versioned figure table and DOI
registry also retain their input blobs. The shelf diagram was regenerated
and matched its original bytes. Before staging, the complete tracked diff
and all three new files were inspected. A separate UTF-8, whitespace and
local-link scan passed on the dossier. The explicit staging command
reported the repository's figures/ ignore rule. Readback confirmed that
all 15 intended paths were staged, including the two figure updates and
one deletion. Each staged file matched the inspected bytes (LF for text).
Both `git diff --check` and `git diff --cached --check` returned 0 with
no output, as did the staged whitespace check against the PR target. The
post-merge diff restricted to paths outside the allowed set was empty.
Hosted workflow results are keyed to the pushed revision in the PR handoff.

## Residual uncertainty

The witnesses establish feasible upper bounds. Their optimality and the
exact values of C* and C₂ remain open. A full human review of the profile
proof is the outstanding scientific dependency.
