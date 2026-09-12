# Standalone reference and overlap audit

Mode: STRICT. Checked 2026-09-12 by a separate internal audit agent.
This report records bibliographic, editorial and engineering evidence, not
external acceptance, a mathematical proof audit or an arXiv moderation decision.
Only this report was edited by the audit agent; historical audit evidence,
the finite correction and the published v1 were left unchanged.

## References and primary records

All six bibliography entries in the final standalone were inspected, including
the revised descriptive hyperlinks. No blocking reference defect was found.

- `v1`: the [actual version record](https://arxiv.org/abs/2607.28654v1)
  confirms Maurizio Falconi, *Arranging circles of radii 1,2,...,n around a
  central circle: a Supnick TSP and certified finite optima*, 2026, cs.CG.
  The historical coefficient conjecture is explicitly present in its abstract.
  The cited identifier is now literally `arXiv:2607.28654v1`; no future sequel
  identifier is supplied. The external record still displays a June submission
  date despite the July-style identifier. This audit preserves the verified
  year/version without inventing a correction to external metadata.
- `shelf`: the [journal record](https://jocg.org/index.php/jocg/article/view/3056)
  confirms Helmut Alt, Kevin Buchin, Steven Chaplick, Otfried Cheong, Philipp
  Kindermann, Christian Knauer and Fabian Stehn; *Placing your coins on a shelf*,
  Journal of Computational Geometry 9(1), 312-327 (2018),
  DOI `10.20382/jocg.v9i1a10`. The [authors' full preprint](https://arxiv.org/pdf/1707.01239)
  defines the shelf span and the geometric-mean footpoint separation in its
  introduction and Lemma 1. The sequel correctly credits this underlying model
  while proving its angular reduction, label recovery and effective word
  characterization directly. It imports no shelf complexity or approximation
  theorem. This is a bounded comparison, not an exhaustive priority search.
- `blocks`, `upperinputs`, `lower`, `supplement`: the final entries explicitly
  describe supplementary proofs and retain the common immutable snapshot.
  Their descriptive direct links identify the actual proof documents, not
  review verdicts or moving branches. The complete snapshot URL is printed
  in the bibliography. This is a suitable public citation form for these
  author-owned supplements; no journal or peer-review status is implied.

The read-only GitHub connector fetched [repository metadata](https://api.github.com/repos/falker47/ringmin)
(`visibility: public`) and the [complete recursive tree](https://api.github.com/repos/falker47/ringmin/git/trees/3beb8d70c5b3748d370a92855847bdf574e5a14f?recursive=1)
(`truncated: false`). All ten directly cited proof files exist at this commit.
Local `git ls-tree` agreed with the live blob IDs. Scoped `git show` heading
inspection also confirmed every numbered section cited in the bibliography.

| File under `research/` | Git blob at `3beb8d70c5b3748d370a92855847bdf574e5a14f` |
| --- | --- |
| `PERMUTED_ALTERNATING_HALVES.md` | `b1e7c39d42e5686ee312fb41bbbaf0e5faebe573` |
| `PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md` | `219215cc3346a7e91e0c6181ca0b496326e872aa` |
| `PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md` | `91580e7e26b0d5223eded6e92b2c12c18f08b610` |
| `PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md` | `f69fc0d16590d89eb405fee23ec5f4b57e047745` |
| `PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md` | `d8bfb7099956a373a281631d1082f874e302b674` |
| `PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md` | `8d60ba3e6ca93356c021e85da2c7bfa5d6688d31` |
| `PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md` | `24c570f14d755e94a91088c7b1abeb4410dd6bc2` |
| `COMMON_CHAIN_QUANTITATIVE_STABILITY.md` | `b8dc84ba5d99719a7360f221cfefda79984ae54a` |
| `THREE_LEVEL_COMMON_CHAIN.md` | `eb6dd88fbdb4bab90bb6f0755556f59fc6f99035` |
| `GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md` | `7a01d3c1491d9127d84026c250a0121e80043909` |

Local existence command, exit 0, returned exactly the ten blobs above:

```powershell
$taskRepoRoot=(Get-Location).Path.Replace('\','/')
git -c "safe.directory=$taskRepoRoot" ls-tree -r 3beb8d70c5b3748d370a92855847bdf574e5a14f -- research/PERMUTED_ALTERNATING_HALVES.md research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md research/THREE_LEVEL_COMMON_CHAIN.md research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md
```

Unqualified Git initially failed the sandbox ownership check; the
command-scoped `safe.directory` setting for the current repository
allowed read-only inspection without changing Git configuration.
Using the native backslash path also failed the ownership check; converting
the current path to forward slashes yielded the successful portable command.

## Metadata and publication architecture

The prepared metadata retains cs.CG primary and recommends one math.MG
cross-list, consistent with its Euclidean/discrete geometry scope in the
[official taxonomy](https://arxiv.org/category_taxonomy). Cross-listing is an
editorial recommendation, subject to moderation, and should be limited to
directly relevant audiences ([guidance](https://info.arxiv.org/help/cross.html)).
The [official MSC2020 classification](https://msc2020.org/MSC_2020.pdf) supports
52C15 (Primary), 52C26 and 90C05 (Secondary) for planar packing, circle packing
and linear programming.

The v1 license link resolves to the [arXiv non-exclusive distribution license](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html).
The final handoff preserves that existing author choice. No Creative Commons
license is inferred from repository licensing, and this preparation selects no
license on the author's behalf. The [official license guidance](https://info.arxiv.org/help/license/index.html)
leaves the choice to the submitter and makes each posted version's license
irrevocable.

The final abstract has 1231 characters, below the official 1920-character
limit. The title, author and processor fields agree with the manuscript;
Comments identify eight pages, no figures, the prior v1 and the pinned
supplement. Journal reference and DOI are not invented. The
[metadata guidance](https://info.arxiv.org/help/prep.html) calls for ASCII and
expanded TeX macros. The [TeX submission guidance](https://info.arxiv.org/help/submit_tex.html)
excludes extraneous/generated files and requires the author to inspect the
server-generated PDF. [Current TeX Live guidance](https://info.arxiv.org/help/faq/texlive.html)
does not establish equivalence between local packages and the server snapshot.

The semantic allocation in the historical
[architecture audit](../TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md)
still holds: the standalone contains the all-size limit, effective word LPs,
full-geometry recovery and endpoints; the finite study remains the reference
for Supnick ordering, finite search and tables. Common model definitions and
elementary angular background are needed for self-containment. Final editorial
changes introduce no second finite-paper treatment or new scientific result.
The correction remains `AWAITING_STANDALONE_ARXIV_ID`, and the old replacement
remains `EDITORIALLY_SUPERSEDED`.

[Version guidance](https://info.arxiv.org/help/versions.html) permits moderators
to require consolidation even without substantial literal overlap. The
[overlap guidance](https://info.arxiv.org/help/overlap.html) supplies no numeric
safe harbor. The acknowledgment remains consistent with human responsibility
and disclosure under the [AI-tool policy](https://info.arxiv.org/help/moderation/index.html).
No numerical diagnostic below supplies moderation approval or external review.

## Exact rerun of the historical prose diagnostic

Both runs used Windows PowerShell and local Python 3.14.3, with exit 0.
The first extracts and executes the exact historical Python block unchanged
in an isolated namespace. Its normalization removes comments, math,
figures/tables, headings, citation/reference commands and command names; it
includes abstract/main prose/acknowledgment but excludes bibliography, later
appendix and external inputs. The semantic audit above covers these exclusions.
Thresholds 12 tokens, 40 tokens and ratio 0.75 are local diagnostics, not arXiv
thresholds; paraphrases, priority and mathematical correctness are not tested.

Exact command from repository root:

```powershell
@'
from pathlib import Path
import re
source = Path('ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md').read_text(encoding='utf-8')
code = re.search(r'```python\n(.*?)\n```', source, re.S).group(1)
exec(compile(code, '<architecture-prose-diagnostic>', 'exec'), {'__name__': '__main__'})
'@ | python -
```

Exact stdout, final standalone versus unchanged correction:

```json
{
  "python": "3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]",
  "sha256": {
    "sequel": "5248445a3a1b92c494466fdfe266555023bbc13606f93ffc07ec229538b886e6",
    "correction": "4724d3d6f222e22293a61b5bbed70685550c8a341f4a070f535ebd6fbfc7d2af"
  },
  "diagnostic": {
    "sequel": {
      "normalized_tokens": 2311,
      "paragraphs": 60,
      "eligible_40_token_paragraphs": 26,
      "covered_12gram_tokens": 0,
      "coverage_percent": 0.0
    },
    "correction": {
      "normalized_tokens": 2805,
      "paragraphs": 52,
      "eligible_40_token_paragraphs": 30,
      "covered_12gram_tokens": 0,
      "coverage_percent": 0.0
    }
  },
  "shared_distinct_12grams": 0,
  "paragraph_matches_40_tokens_at_075": [],
  "longest_normalized_contiguous_match": [
    5,
    {
      "sequel_paragraph": 2,
      "correction_paragraph": 11,
      "tokens": "tangent to the central circle"
    }
  ],
  "shared_12grams": []
}
```

Optional historical-v1 comparison uses exactly the same code/exclusions,
changing only the second input path. Its output keys retain `correction`
solely because the diagnostic was otherwise left unchanged; they denote v1
in this second output.

```powershell
@'
from pathlib import Path
import re
source = Path('ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md').read_text(encoding='utf-8')
code = re.search(r'```python\n(.*?)\n```', source, re.S).group(1)
code = code.replace('paper_assets/v1_correction/ringmin_finite_v2.tex', 'paper_assets/ringmin_paper.tex')
exec(compile(code, '<architecture-prose-diagnostic-v1-input>', 'exec'), {'__name__': '__main__'})
'@ | python -
```

Exact stdout:

```json
{
  "python": "3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]",
  "sha256": {
    "sequel": "5248445a3a1b92c494466fdfe266555023bbc13606f93ffc07ec229538b886e6",
    "correction": "5042d01b0f0f54ed3badeaa494cd24411aa58a2aa2c865b3f02abb27fcbcc60a"
  },
  "diagnostic": {
    "sequel": {
      "normalized_tokens": 2311,
      "paragraphs": 60,
      "eligible_40_token_paragraphs": 26,
      "covered_12gram_tokens": 0,
      "coverage_percent": 0.0
    },
    "correction": {
      "normalized_tokens": 2320,
      "paragraphs": 50,
      "eligible_40_token_paragraphs": 25,
      "covered_12gram_tokens": 0,
      "coverage_percent": 0.0
    }
  },
  "shared_distinct_12grams": 0,
  "paragraph_matches_40_tokens_at_075": [],
  "longest_normalized_contiguous_match": [
    5,
    {
      "sequel_paragraph": 2,
      "correction_paragraph": 6,
      "tokens": "tangent to the central circle"
    }
  ],
  "shared_12grams": []
}
```

## Access and verification limits

Direct DOI fetch was blocked by the web tool; the successful publisher record
independently confirms it. The GitHub web view returned a cache miss; the live
public API tree succeeded. Shelf publisher/institutional PDF fetches failed;
the authors' arXiv PDF succeeded. These transport failures are not evidence
of broken citations. A guessed local `BUILD_AND_VERIFICATION.md` and template
`EVIDENCE.md` did not exist; no conclusions relied on them. Actual evidence
and template filenames were subsequently located without changing those files.

This audit did not rebuild PDFs, run mathematical certificates, change any
external record or advance external Review State. Its only mutation is this
task-local report. The parent records final artifact, whitespace and Git checks.
