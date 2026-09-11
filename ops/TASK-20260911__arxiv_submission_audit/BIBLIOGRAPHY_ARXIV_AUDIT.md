# Bibliography, attribution and arXiv requirements audit

Checked 2026-09-11. Mode: STRICT. This is an independent bounded subtask of
the submission audit, not external referee acceptance or a new mathematical
result. The initial manuscript was `paper_assets/v2/ringmin_v2.tex` at
`3beb8d70c5b3748d370a92855847bdf574e5a14f`. Protected historical v1 was read,
not changed. This subtask writes only this audit file; the parent owns
candidate corrections, builds and final disposition.

## Scope and evidence discipline

Read the goal objective, operating contract, canonical index/current status,
the relevant publication-history and roadmap sections, the complete candidate,
the final packet and its `LITERATURE.md`, historical v1 bibliography/title and
`CITATION.cff`. Read-only local Git checked both supplementary checkpoints.
Live primary web sources and read-only GitHub connector calls supplied the
external checks below. Retrieval failures are distinguished from invalid
records; no conclusion of nonexistence is drawn from a web-cache miss.

No numerical certificate verifier, TeX build, hosted CI or mathematical
acceptance gate was run by this subtask. Those belong to the parent evidence.

## Findings and disposition

| ID | Severity | Finding | Disposition observed by this subtask |
| --- | --- | --- | --- |
| BIB-01 | IMPORTANT | Initial `pdftitle` omitted `certified finite optima`, although the visible title contained it. | Corrected in the parent's current TeX; PDF metadata still requires the parent's rebuilt-PDF check. |
| BIB-02 | IMPORTANT | The initial supplement references did not pin every cited document. In particular, the mathematical checkpoint `13ddb411...` does not contain the final fixed-order audit or final review packet. | Corrected in the parent's current TeX by explicitly identifying the complete snapshot `3beb8d70...` and linking the immutable repository tree. That tree was independently retrieved from GitHub and all nine cited paths exist. |
| BIB-03 | IMPORTANT | The candidate's date suffix `not submitted` and the sentence denying any external submission would become stale when this file is uploaded as v2. | Corrected in final source: removed those two transient statements; the internal/external review distinction and AI disclosure remain. |
| BIB-04 | OPTIONAL | Supnick's DOI is not included in the initial bibliography. | No metadata error: author/title/issue/pages/year already correct. DOI `10.2307/1970124` is verified and may be added; this is not a readiness gate. |

No external bibliographic entry was found to have an incorrect author, title,
publication year, volume, issue, page range or supplied identifier. The
classification of the named mathematical results is outside this bibliography
subtask and is not inferred from the existence of their references.

## Every external bibliography entry

### `v1`

The public [arXiv v1 record](https://arxiv.org/abs/2607.28654v1) is retrievable
and identifies Maurizio Falconi as sole author, the title **Arranging circles
of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite
optima**, version 1, year 2026, identifier `2607.28654v1`. This agrees with
the candidate's historical reference and the protected local v1/CITATION
record. The [public v1 HTML](https://arxiv.org/html/2607.28654v1) confirms the
chain/full distinction and presents the asymptotic coefficient and floating
cascade as conjectural beyond the certified scope. A reference to v1 therefore
does not establish the later theorem or an enlarged finite certificate.

Public metadata observed:

- Primary category: Computational Geometry (`cs.CG`). No cross-list displayed.
- Existing Comments: `10 pages, 2 figures; source code and certificate artifacts available at https://github.com/falker47/ringmin`.
- Existing MSC: `52C26, 52C15, 05C85, 90C27`.
- arXiv-issued DOI shown: `10.48550/arXiv.2607.28654`.
- The page reports submission on 25 June 2026 despite the `2607` identifier
  prefix. This is recorded as an observed external metadata inconsistency,
  not evidence that the identifier is invalid. The candidate cites only the
  verified year; no date correction is inferred or introduced.

### `shelf`

The [JoCG primary journal record](https://jocg.org/index.php/jocg/article/view/3056)
lists all seven authors in the candidate's order: Helmut Alt, Kevin Buchin,
Steven Chaplick, Otfried Cheong, Philipp Kindermann, Christian Knauer and
Fabian Stehn. It gives **Placing your coins on a shelf**, *Journal of
Computational Geometry* 9(1), 312-327 (2018), published 2018-09-05,
DOI `10.20382/jocg.v9i1a10`. All supplied bibliographic fields match.

The journal abstract defines nonoverlapping disks touching the horizontal
axis and minimizes their horizontal envelope span. The candidate's geometric
identification is elementary: centers `(2*x_i,a_i)` give exactly
`|x_i-x_j| >= sqrt(a_i*a_j)`; for marks at most one the disk envelope adds at
most two to twice the scaled center span. The candidate explicitly credits
the existing shelf model, proves its asymptotic claims itself, and imports
neither the shelf paper's approximation nor complexity theorems. This is
appropriate attribution; the bounded literature check establishes no priority
over all literature.

The DOI resolver returned an internal fetch error on repeated web attempts;
the primary journal landing page directly records the DOI and full citation.
This is sufficient bibliographic verification, not a claim that every resolver
request succeeded.

### `supnick`

The [journal's JSTOR issue record](https://www.jstor.org/stable/i307286)
identifies Fred Supnick, **Extreme Hamiltonian Lines**, *Annals of Mathematics*
66(1), 179-201, July 1957, DOI `10.2307/1970124`. Candidate initials and
sentence-style capitalization are consistent. The DOI resolves to
`https://www.jstor.org/stable/1970124?origin=crossref`, but that individual
page yielded only a JavaScript stub to the reader; full metadata came from
the issue record, not the stub. The original article full text was not
retrieved. The specific theorem use was checked through the accessible
published survey below.

### `survey`

The [SIAM primary article record](https://epubs.siam.org/doi/abs/10.1137/S0036144596297514?download=true&journalCode=siread)
and the [publisher PDF held by Eindhoven University](https://pure.tue.nl/ws/files/2373438/Metis148543.pdf)
identify Rainer E. Burkard, Vladimir G. Deineko, Rene van Dal, Jack A. A. van
der Veen and Gerhard J. Woeginger; **Well-Solvable Special Cases of the
Traveling Salesman Problem: A Survey**; *SIAM Review* 40(3), 496-546 (1998);
DOI `10.1137/S0036144596297514`. The candidate matches all fields. The printed
PDF uses the alternate accented transliteration of Deineko; the publisher's
web record uses `Deineko`, matching the candidate. This is not an author error.

The PDF's Theorem 2.5 (printed p. 502) treats a minimum tour on Supnick
matrices. Its maximum-TSP discussion (printed p. 507), attributed to Supnick,
gives the complementary fixed maximum tour; Proposition 2.13 (printed p. 508)
relates symmetric Monge matrices and Supnick matrices up to irrelevant
diagonal entries. Applying that maximum theorem to the negative angular
matrix supports the candidate's chain-minimization attribution. It does not
establish full geometric feasibility or the floating structure, and the
candidate explicitly preserves that boundary.

Direct SIAM/DOI fetches initially timed out; the publisher's PDF-link route
successfully produced its primary record. The university PDF provided the
theorem text. No claim is inferred from a failed DOI request.

## Every repository bibliography entry and immutable accessibility

The public [repository page](https://github.com/falker47/ringmin) was retrieved.
The web reader missed its exact commit/blob URLs, so the read-only GitHub
connector was used as a separate access path:

1. `github_fetch` of `https://api.github.com/repos/falker47/ringmin` returned
   `private=false`, `visibility=public`, default branch `main`.
2. `github_fetch` of
   `https://api.github.com/repos/falker47/ringmin/git/commits/3beb8d70c5b3748d370a92855847bdf574e5a14f`
   returned that exact SHA, the message `Prepare versioned asymptotic manuscript
   and final external review packet`, and tree
   `b01287496f96d4263874336e48456be3e44d1471`.
3. `github_fetch` of
   `https://api.github.com/repos/falker47/ringmin/git/trees/b01287496f96d4263874336e48456be3e44d1471?recursive=1`
   returned `truncated=false` and every path in the table below.
4. `github_fetch_file(repository_full_name="falker47/ringmin", ref="3beb8d70c5b3748d370a92855847bdf574e5a14f", path="ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md", start_line=1, end_line=24)`
   returned the actual packet opening and blob
   `c63120bc7e74b16257ae919647ae5fd6dfe393c9`.

All calls succeeded with `isError=false`. This verifies public repository
status and exact commit/file accessibility through GitHub's API. It does not
claim that the separate unauthenticated web cache successfully rendered every
deep link, or that a mathematical review accepted that commit.

| Bibliography key | Cited path at snapshot `3beb8d70...` | Git blob SHA |
| --- | --- | --- |
| `blocks` | `research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md` | `219215cc3346a7e91e0c6181ca0b496326e872aa` |
| `blocks` | `research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md` | `91580e7e26b0d5223eded6e92b2c12c18f08b610` |
| `upperinputs` | `ops/GOAL-20260911__conclude_study/UPPER_INTERNAL_AUDIT.md` | `0dd11e73c51b19aadb483a59d60aac5680e7ec9e` |
| `lower` | `research/THREE_LEVEL_COMMON_CHAIN.md` | `eb6dd88fbdb4bab90bb6f0755556f59fc6f99035` |
| `lower` | `ops/GOAL-20260911__conclude_study/LOWER_INTERNAL_AUDIT.md` | `668ae1fe444bd199625ec80eb06b574a38ab65d0` |
| `fixed` | `research/SUPNICK_FULL_FEASIBILITY.md` | `94a6664993e40ea65390a9c110f76d2e3b096589` |
| `fixed` | `research/SUPNICK_SEAM_SEQUENCES.md` | `f0a1d148e73f0a162c158410686110f60ecfa3dd` |
| `fixed` | `ops/GOAL-20260911__conclude_study/FIXED_ORDER_INTERNAL_AUDIT.md` | `8a0fb89b7d6343cf0ea1bc2cbb730e7f89e960c5` |
| `packet` | `ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md` | `c63120bc7e74b16257ae919647ae5fd6dfe393c9` |

The correct common reader entry point is the
[immutable supplementary snapshot](https://github.com/falker47/ringmin/tree/3beb8d70c5b3748d370a92855847bdf574e5a14f).
The older mathematical checkpoint is valid provenance for documents that
already existed then, but must not be the implicit location for later audits.

## AI disclosure and attribution scope

The candidate discloses AI use in proof exploration, software, drafting and
internal adversarial checking, names only Maurizio Falconi as author, and
separates internal checks from the author's approval and external review.
The disclosed roles agree with the repository README and historical v1's
acknowledgment. No unobserved tool/model names or model versions should be
invented for a more specific disclosure.

The current [arXiv moderation policy](https://info.arxiv.org/help/moderation/index.html),
under generative AI language tools, asks that significant use be reported,
keeps responsibility with human authors, and excludes generative tools from
authorship. The existing disclosure meets those relevant points; arXiv does
not require external reviewer acceptance before submission. The failed guessed
`help/policies/ai.html` URL was not treated as evidence of absent policy.

The candidate credits v1 for the historical study and does not claim discovery
of the underlying circle question. Historical v1 explicitly attributes the
original question to Dan on Mathematics Stack Exchange. No new priority claim
is introduced by this audit, and no exhaustive novelty review was performed.

## Current official arXiv processing requirements

These are observed current documentation facts, checked on 2026-09-11,
not a claim that the arXiv service has compiled this candidate.

- [TeX Live at arXiv](https://info.arxiv.org/help/faq/texlive.html): supported
  versions are 2023 and 2025; 2025 is default, with its package snapshot dated
  2025-08-03. `pdflatex` is the supported LaTeX PDF-mode processor. The source
  uses ordinary article/AMS packages and needs no XeLaTeX, LuaLaTeX or custom
  font-loader feature.
- [TeX submission guide](https://info.arxiv.org/help/submit_tex.html): builds
  start at the submission root, even for a nested main file. Upload required
  source dependencies only; omit generated TeX PDF, auxiliaries, logs, backups
  and unused assets. JavaScript embedded in PDFs is disallowed. The submitter
  must inspect arXiv's resulting PDF. This candidate's inline bibliography
  and lack of file inclusions make a single root-level TeX file sufficient.
- [Submission overview](https://info.arxiv.org/help/submit/index.html): TeX
  source is the preferred format, and a PDF produced from available TeX is
  not an alternative source submission. Filenames and file references are
  case-sensitive. The normal UI exposes compiler and top-level-file choices.
- [00README format](https://info.arxiv.org/help/00README.html): normal UI
  submissions do not require, and are not recommended to pre-create,
  `00README.json`. If specialized control were needed, the documented fields
  include `process.compiler="pdflatex"` and a top-level source filename.
  No such customization is needed here. Recommendation: one TeX upload;
  select `pdflatex` and TeX Live 2025 in the UI.

### Package/font evidence and limitation

The [package list linked by arXiv's submission guide](https://info.arxiv.org/help/texlive_package_list.html)
still labels itself TeX Live 2023. It lists `latex`, `amsmath`, `amscls`,
`amsfonts`, `booktabs`, `geometry`, `hyperref`, `lm` and tools. These supply
the candidate's `article`, `fontenc`, AMS theorem/symbol/math, table, geometry,
hyperlink and Latin Modern dependencies. The
[official TeX Live 2025 font list](https://info.arxiv.org/help/faq/font-info-tl2025.html)
also lists Latin Modern fonts. The presence of its OpenType fonts is not by
itself a check of pdfLaTeX Type 1 embedding; actual embedding belongs to the
parent's PDF inspection.

The initial candidate names no private style/font and includes no custom
package version constraint. Available documentation supports ordinary
portability. This audit did not obtain a separate complete arXiv TL2025
package manifest or execute that exact frozen server image; the parent's
clean build must name its actual local distribution precisely. Final server
compatibility and its rendered pages must be checked during the manual arXiv
preview, not described as already tested.

## Proposed metadata and final UI checks

Use the final visible manuscript title exactly, without its TeX line break:

`Minimum central circles: certified finite optima and an effective global asymptotic constant`

Authors: `Maurizio Falconi`.

Abstract: the following exact mathematical content is expanded from final
source SHA-256 `189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a`.
It expands the two custom macros, uses standard `\mathrm` for subscripts,
and separates `\le` from the expanded `C_\ast` so they do not become the
invalid command `\leC`. It is 1502 ASCII characters, below the current
1920-character limit. Copy the single paragraph without the code fence:

```text
Let $R^\ast(n)$ be the least radius of a central circle to which nonoverlapping circles of radii $1,\ldots,n$ are externally tangent. We prove that $R^\ast(n)=C_\ast n^2+o(n^2)$ and characterize $C_\ast$ by finite linear programs with an explicit error tending to zero. The reduction preserves arbitrary orders and all pairwise constraints: the limiting problem places marked points on a line at pairwise separation at least the geometric mean of their marks. Concatenation with a bounded boundary cost proves existence, and balanced finite-word programs supply matching effective upper and lower bounds. Their certified gap is $(1/k+1/r)/\pi$, before directed arithmetic error, for $k$ mark types and words of length $r$. We also transfer every finite or countable adjacent reflected-block construction whose total slab length is strictly below $1-\alpha$, where $0\le\alpha<1$ is the shift parameter, to genuine permutations and full ring geometry, including a strict four-block improvement. The best retained explicit interval is $C_{\mathrm{term}}+\eta_{\mathrm{width}}\le C_\ast\le U_4$. The original computer-certified scope $3\le n\le14$ and exact fixed-order Supnick feasibility theory remain distinct from global asymptotics. The earlier $n^2/8$ conjecture is false. Efficient evaluation of the variational constant, an elementary expression and global floating-circle structure remain open. This candidate has undergone internal adversarial checks; independent external acceptance is pending.
```

Primary category: preserve `cs.CG`. Cross-lists: preserve none, since none
appear in the existing record; no additional category is inferred. Preserve
the existing MSC values if the replacement UI retains that field. Leave
journal-reference and publication-DOI fields unchanged unless the author has
actual publication metadata; the arXiv-issued DOI is not a new journal DOI.

Suggested replacement Comments, using the parent's checked nine-page count:

`9 pages, 0 figures. Substantially revised: proves existence and an effective variational characterization of the global asymptotic constant, disproves the earlier n^2/8 conjecture, and adds exact fixed-order feasibility results. Certified finite scope remains 3<=n<=14. Source code, proofs and certificate artifacts: https://github.com/falker47/ringmin`

This preserves the still-valid repository information from v1 while updating
the obsolete page/figure counts and explaining the substantive replacement.
The [replacement guide](https://info.arxiv.org/help/replace.html) asks for a
reason in Comments and warns that old comments are not accumulated. The
[metadata guide](https://info.arxiv.org/help/prep.html) calls for ASCII-compatible
metadata, expanded custom macros, a short abstract, and truthful category and
publication fields. The page count is parent-reported clean-build evidence;
the final TeX hash, abstract and corrected bibliography were directly read
again by this subtask.

The manual UI stage must verify the inherited record/category/comments,
compiler `pdflatex`, TL2025 selection, sole top-level TeX filename and uploaded
file list. Inspect every page of arXiv's own generated PDF, including title,
equations, bibliography, links and metadata, and compare to the locally
audited final PDF. No submission, release or other external write was made.

## Local command outcomes

- Initial plain `git status --short` failed because the sandbox account did
  not own the checkout. No global configuration was changed.
- Repeating with process-local `git -c safe.directory=<repository-root> status --short`
  succeeded with no changed paths at this subtask's start; it warned that the
  user's global ignore file was unreadable. Parent had independently verified
  the clean starting tree.
- Read-only `git cat-file -t 13ddb411...` returned `commit`.
- Read-only `git ls-tree` at `13ddb411...` returned the seven mathematical
  proof/upper/lower-audit paths above, and no final fixed audit or packet.
- Read-only `git ls-tree` at `3beb8d70...` returned both previously missing
  final audit and packet paths. GitHub's complete tree independently agreed.
- Initial PowerShell regex extraction of the candidate abstract and the two
  explicit macro replacements returned length `1392`. After the parent's
  addition of the already-required block-transfer domain condition, the
  final exact expanded abstract above was checked separately for ASCII and
  the 1920-character limit. This is a source/metadata check, not a PDF
  extraction or mathematical verification.

All successful scoped local reads exited zero. Final whitespace inspection
of this new audit file is recorded by the parent alongside the complete final
diff. No production implementation, historical v1 or certificate artifact was
edited by this subtask.

Command display convention: `<repository-root>` replaces only the local
`safe.directory` path, to avoid storing a machine-specific absolute path.
All other shown command arguments and results retain their recorded meaning.
