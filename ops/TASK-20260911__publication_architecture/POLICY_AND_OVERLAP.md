# Publication policy and manuscript overlap audit

Mode: STRICT. Policy check date: 2026-09-11. This file is task-local editorial
evidence, not a new global publication ledger or external acceptance.

## Initial decision and policy evidence

Preferred architecture: a genuinely standalone asymptotic sequel, followed
only after its real permanent identifier exists by a conservative corrective
v2 of `arXiv:2607.28654`. The older nine-page replacement is provenance and
not the recommended upload. This is an editorial judgment subject to arXiv
moderation, not advance permission from arXiv.

- The current [submission guidance](https://info.arxiv.org/help/submit/index.html)
  directs corrections and errata to the original identifier rather than a
  new submission. The proposed corrective finite paper follows that rule.
- The [moderation policy](https://info.arxiv.org/help/moderation/index.html)
  permits moderators to require consolidation or versioning when submissions
  are similar or a new submission appears to revise recent work. It also
  requires substantive, refereeable scientific work. It does not state that
  every later theorem about the same mathematical problem must be a version.
- The [text-overlap guidance](https://info.arxiv.org/help/overlap.html)
  distinguishes author/citation relationships, discusses substantial reused
  text, and permits an author's disclosure of overlap in Comments. An overlap
  notice itself does not imply misconduct or absence of original research.
  The public guidance supplies no numeric safe-harbor similarity threshold.
- The [replacement guidance](https://info.arxiv.org/help/replace.html)
  preserves earlier public versions and asks that Comments explain the change
  while retaining still-valid prior information.
- Root additionally read the full current
  [version-availability guidance](https://info.arxiv.org/help/versions.html),
  including related works, splitting/merging and similarity. It states that
  the latest version is the default, replacements contain full text, and
  related errata/supplements/expanded or condensed versions can share an ID.
  Its splitting example replaces an already posted long work with one part
  and posts other parts under new IDs. Here the asymptotic source was never
  posted, so that example does not itself dictate the sequence. The similarity
  rule expressly allows moderators to require consolidation even without
  substantial verbatim overlap when close concepts/results and reader benefit
  warrant it. This supports the stated residual risk and the fully integrated
  fallback, not a guarantee that the standalone will receive a new identifier.

These official pages were reopened for this task. Searches of the official
help/FAQ and the content-type/format policies did not locate a separate
universal rule forbidding the editorial division here. The guessed URL
`help/faq/split.html` was unavailable; that is not evidence of an exception
or permission. The applicable risk is the explicit similarity/revision rule
above. Mere conceptual relatedness is therefore not treated as a veto.

The substantive distinction supporting the preferred choice is testable:
the first paper's main contribution is fixed-order chain theory plus a finite
all-pairs optimization/certification framework and tables; the sequel's main
contribution is an all-size limit with a constructive effective variational
characterization and explicit asymptotic endpoint constructions. The first
does not prove the latter. The sequel must cite the first and retain only
the common model needed to read its new proofs.

No evidence currently makes the standalone architecture clearly untenable.
An integrated fallback manuscript is therefore not being manufactured as a
third competing candidate. The required contingency is explicit below.

## Documented future sequence, not executed

1. Independently review the standalone asymptotic manuscript, then let the
   author submit it as a distinct new work with transparent prior-work citation.
2. Only if arXiv accepts it as distinct and assigns an actual permanent
   identifier, perform a later atomic task replacing the machine-detectable
   placeholder in the conservative finite correction, rebuild and re-audit
   that source bundle, and then have the author submit its replacement.
   Until then the correction is `AWAITING_STANDALONE_ARXIV_ID`.
3. If moderators require integration/versioning, honor that decision. Prepare
   a genuinely integrated replacement retaining the v1 Supnick theorem and
   proof, all-pairs/STN model, certification method and guards, main
   `3<=n<=14` tables, finite-regime interpretation and reproducibility, followed
   by the new global asymptotic theory. Rebuild and re-audit that integrated
   work. The asymptotics-heavy nine-page candidate is not sufficient unchanged.

No fictitious identifier, submission, moderation appeal or publication write
is authorized by this audit. Both candidate manuscripts remain for independent
review; internal review is not external scientific acceptance.

## Initial overlap inventory before candidate finalization

This inventory was written from the historical `paper_assets/ringmin_paper.tex`
and the preserved `paper_assets/v2/ringmin_v2.tex` before the two new candidate
sources were finalized. Labels identify original source objects; statements
without labels are identified by section and role. Final reconciliation and
prose diagnostics are appended below after the new sources stabilize.

Classes: **H** historical-paper core; **S** standalone-sequel core;
**B** minimal duplicated background needed for self-containment;
**X** cross-reference only in the other manuscript; **O** obsolete or
superseded statement. A compound `H/X` means preserve in the corrective
historical paper and refer to it without reproducing it in the sequel.

| Source object or major block | Class | Intended allocation and qualification |
| --- | --- | --- |
| Historical title/abstract: Supnick plus certified finite optima | H | Preserve scientific identity in correction; sequel gets a distinct asymptotic title and abstract. |
| Historical Introduction: Dan's question, UQ origin and Henigman computation | H/X | Preserve attribution in correction; sequel cites prior paper without reproducing its introductory narrative. |
| Common central-tangency/nonoverlap problem and `R*(n)` | B | Needed in both; short definition, not duplicated long prose. |
| `eq:closure`, `R_chain`, `R_full`, global minimum distinction | B | Historical development retained; sequel uses only definitions and inequalities needed for limits and endpoints. |
| `lem:angular`, cosine-law pair condition and both arcs | B | Self-contained geometric preliminaries in both; sequel's arctangent form and squeeze serve new proofs. |
| Historical definition of floating circle | H/X | Existential strictly slack definition preserved in correction; sequel only names unresolved contact questions. |
| Historical definition of Descartes pocket | H/X | Preserve finite geometry with strict versus non-strict fit distinguished; no full pocket treatment in sequel. |
| `lem:supermodular`, mixed derivative proof | H/X | Preserve original proof; sequel attributes Supnick background rather than republishing proof. |
| `thm:A`, fixed Supnick tour, chain lower bound and conditional full optimum | H/X | Historical theorem stays primary; sequel's endpoint source may cite it, with no chain/full inference. |
| Arbitrary-radii and n=10 remark following `thm:A` | H/X | Keep relevant historical explanation only. |
| `prop:worst`, complementary worst chain arrangement | H/X | Keep finite range and chain-level scope in correction; no sequel theorem. |
| Section 4 STN inequalities/Floyd-Warshall/bisection/witness algorithm | H/X | Preserve original optimization method; sequel uses a different line-word recurrence. |
| Section 4 induced-subset lower bounds/canonical enumeration/stopping rule | H/X | Preserve original finite search framework and guards; not an asymptotic LP algorithm. |
| Section 4 calibration/frontier/verifier/numerical evidence and timings | H/X | Preserve scope and distinguish saved verification from search generation; no duplicated benchmark prose in sequel. |
| Essential-pair and floating interpretation | H/X | Correct any conflation of individual nonessential constraints with simultaneous strict slack; finite core stays historical. |
| Introduction finite-regime table | H/X | Retain in correction; remove table from sequel. |
| `tab:main`, certified optima 3..14 | H/X | Preserve every result row in correction; sequel cites scope only. |
| `fig:n14`, saved n=14 geometry | H/X | Preserve figure in correction, with existential witness semantics; no sequel copy. |
| `prop:break1`, first finite seam failure | H/X plus O | Preserve original finite facts; acknowledge later formal seam theorem without importing full classification. |
| `prop:break2`, free/paid finite floater mechanism | H/X | Preserve values and stated finite ranges only. |
| `prop:break3`, second finite breakdown | H/X | Preserve finite witness and seam statements with correct quantifiers. |
| Historical structural-summary remark | H/X plus O | Preserve finite observations; remove universal/inevitable cascade inference. |
| `conj:cascade` | O/H | Formal seam eventual failure is superseded by proof; eventual floating in every optimum remains explicitly unproved, not refuted by coefficient correction. |
| `tab:heur`, n=15..18 best-known arrangements | H/X | Retain as historical heuristic upper bounds, never certified optima. |
| Historical `sqrt(ab)` chain integral and `n^2/8` chain coefficient | H | Retain only as chain asymptotics/explanation of the earlier mistake; not the full optimum asymptote. |
| Historical inference from few floaters to coefficient 1/8 | O | Explain that nonadjacent geometric cost is not discharged; do not recycle as conditional proof. |
| `conj:asym`, full coefficient 1/8 and deficit `O(sqrt(n))` | O | Explicitly mark disproved/superseded by sequel; no active conjecture in correction. |
| `fig:radii-vs-n`, historical finite comparison chart | H/O | Preserve data/figure as historical comparison; caption must not call 1/8 the global asymptote. |
| Historical empirical deficit numbers | H/O | May retain as finite diagnostics only, never evidence for the disproved limit. |
| Historical proposed full upper bound using unrealizable Supnick necklace | O | Remove or explicitly correct; retain chain/full guardrail. |
| Historical open problems and acknowledgments | H/X plus O | Retain relevant unresolved questions and attribution; update only superseded statements. |
| `tab:worst` and both `appendix_tables.tex` tables | H/X | Preserve original finite data and flags; sequel contains none of these tables. |
| Per-n figure/reproducibility navigation and historical references | H/X | Remain with finite paper, apart from shared public-repository/AI-disclosure background. |
| Old-v2 introductory scope and shelf relation | S/B | Reframe as sequel and explicitly credit v1; shelf interpretation belongs to new asymptotic narrative. |
| Line-mark definition `b(a)`, `b_n`, ordered-word `ell(w)` | S/X | Fully in sequel; correction refers to theorem result without copying definitions/proofs. |
| `eq:recurrence`, longest increasing-index path scorer | S/X | Sequel algorithm only; independent of historical STN search. |
| `lem:closing`, unit boundary cost | S/X | Sequel lemma/proof only. |
| `lem:squeeze`, exact comparison with full ring geometry | S/X | Sequel lemma/proof only. |
| `thm:existence`, genuine-label concatenation and positive limit | S/X | Sequel central theorem/proof; correction cites its conclusion. |
| Finite-type limits and quantization `e_k-1/k<=E<=e_k` | S/X | Sequel only. |
| Balanced-word LP `eq:lp` | S/X | Sequel definition/program only. |
| `thm:lp`, matching error `(1/k+1/r)/pi` | S/X | Sequel central theorem/proof; no duplicate in correction. |
| Directed radicals, rational primal/dual certificates, computability and exponential count | S/X | Sequel computational interpretation only; no claim of practical efficiency. |
| Reflected-block measure/slabs and complete max-cell cost | S/X | Sequel definitions only. |
| `thm:blocks`, finite/countable transfer to permutations and all pairs | S/X | Sequel theorem/proof only, including total-length condition. |
| Explicit parameter definitions/isolations and fourth-block saving `U_4` | S/X | Sequel endpoint construction only; correction cites the fact coefficient exceeds 1/8. |
| `prop:lower`, `C_term+eta_width` and directed enclosure | S/X | Sequel endpoint proposition and proof outline only. |
| Old-v2 full fixed-order seam classification table | X | Exclude from both main texts unless needed for a narrowly justified correction; refer to repository proof notes. Not part of asymptotic core. |
| Old-v2 finite-certification summary | X | Sequel uses a short attributed scope statement; correction retains the substantive original treatment. |
| Old-v2 reproduction/checker/review-status blocks | S/H | Each manuscript describes its own evidence; shared AI assistance and acceptance boundary may be minimal common background. |
| Old-v2 open questions | S/X | Retain practical evaluation, endpoint sharpness, structure/subleading terms as genuinely open; no new research. |

## Final-source reconciliation and textual diagnostic

The initial inventory contains **51** object/block rows. Both new sources were
then read, after their owning agents declared them stable. The final inspected
source SHA256 values are:

- Sequel: `28853635a65267e1772352436f29d6c19d0a0b8ace823aa72a0d77f52ad8622f`.
- Correction: `4724d3d6f222e22293a61b5bbed70685550c8a341f4a070f535ebd6fbfc7d2af`.

The final allocation agrees with the inventory:

| Reconciliation item | Observed final allocation |
| --- | --- |
| Historical mathematical objects | Correction retains all three definition environments, both lemmas, the optimal-order theorem, and all four propositions with the same labels. The worst-order proposition now explicitly stays at chain level; finite diagnostics retain their scope. The two former conjecture labels now belong to status remarks, not active conjecture environments. |
| Historical algorithms and data | Correction retains the STN/Floyd-Warshall/bisection method, induced-subset bounds, canonical enumeration, numerical guards, verifier commands, finite-regime table, main 3..14 table, heuristic 15..18 table, complementary-tour table, both figures and included appendix tables. Its existential floating definition and joint slack test are explicit. Exact data-preservation/build checks are the correction audit's responsibility. |
| New asymptotic mathematical objects | Sequel retains the line definition, closing and squeeze lemmas, existence, effective LP and general-block theorems, lower-endpoint proposition, recurrence, quantization and rational-certificate algorithm, four-block saving and countable transfer. Its seven numbered sections contain the new proof narrative. |
| Minimal common mathematical background | Both define the same geometric problem and chain/full distinction and derive the angle condition. These facts are needed for self-contained reading. The sequel gives no second Supnick derivative proof, finite search algorithm, finite-regime table or floating/pocket theory. |
| Cross-references | Sequel Section 1 credits the finite paper and its 3..14 scope, directs readers there for its tables and algorithm, and says the asymptotic proof does not depend on that finite computation. Correction Section 6 cites the sequel's conclusion and effective characterization without reproducing its proofs. |
| Obsolete material | Correction explicitly records both the 1/8 coefficient and square-root deficit conjectures as false. Its historical comparison figure is identified accordingly. Fixed-order seam results do not decide global floating quantifiers. Sequel neither repeats the old fixed-order classification table nor claims a global floating cascade. |
| Publication status | Correction visibly contains both `AWAITING_STANDALONE_ARXIV_ID` and `PENDING_STANDALONE_ARXIV_ID`, describes itself as a proposed correction, and says it is not ready for submission. Its reference to the sequel is plainly in preparation. Sequel cites the actual v1 identifier and version. |

The semantic reuse is the same model, notation and elementary angular background,
plus a short statement of what the other work established. Substantial original
finite proofs, algorithms and tables have one home, and substantial new
asymptotic proofs have the other. No bibliography, table or mathematical overlap
was treated as safe merely because it disappears under prose normalization.

### Reproducible local prose diagnostic

On 2026-09-11 a read-only Python 3.14.3 script was run from the repository root
through a PowerShell single-quoted here-string piped to `python -`; exit **0**.
It normalizes CRLF/LF, strips TeX comments, math, figures/tables, headings,
citations/references and command names, then compares lowercase alphanumeric
tokens of blank-line paragraphs. The corpus starts at `begin{document}` and
ends before the bibliography: abstract, main prose and acknowledgment are
included; bibliography, the later finite appendix and external inputs are
excluded. Those exclusions are covered by the semantic inventory above.

| Diagnostic | Sequel | Correction |
| --- | ---: | ---: |
| Normalized prose tokens | 2307 | 2805 |
| Nonempty normalized paragraphs | 60 | 52 |
| Paragraphs of at least 40 tokens | 26 | 30 |
| Tokens covered by a shared within-paragraph 12-token sequence | 0 | 0 |
| Shared-token coverage under this metric | 0.0% | 0.0% |

There are **zero** distinct shared 12-token sequences; **zero** paragraph pairs
of at least 40 tokens each have `difflib.SequenceMatcher(..., autojunk=False)`
ratio at least 0.75, including zero identical substantial paragraphs. The
longest exact normalized contiguous span is five tokens,
`tangent to the central circle` (sequel paragraph 2, correction paragraph 11
in the normalized corpus). Thresholds 40, 12 and 0.75 are explicitly chosen
local diagnostics, **not arXiv thresholds**. The result does not detect all
paraphrases or establish originality, priority, acceptance or lack of
conceptual overlap.

An initial exploratory run did not normalize CRLF before finding paragraphs
and therefore counted the correction as one paragraph. That output was
discarded; the reported run below corrects line endings first. A subsequent
valid run on the earlier correction found 2767 tokens/51 paragraphs; after
the final pocket-scope and layout corrections the script was rerun on the
final hash above, producing the reported 2805 tokens/52 paragraphs with the
same zero shared-sequence and substantial-paragraph counts.

Exact diagnostic code (read-only; run from the repository root):

```python
import hashlib,json,re,sys
from pathlib import Path
from difflib import SequenceMatcher
paths={"sequel":"paper_assets/asymptotic_sequel/ringmin_asymptotic.tex",
       "correction":"paper_assets/v1_correction/ringmin_finite_v2.tex"}
def normalize(s):
    s=s.replace("\r\n","\n").replace("\r","\n")
    s=s.split(r"\begin{document}",1)[1].split(r"\begin{thebibliography}",1)[0]
    s=re.sub(r"(?<!\\)%[^\n]*","",s)
    s=re.sub(r"\\begin\{(figure\*?|table\*?|center|tabular|verbatim|equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}"," ",s,flags=re.S)
    s=re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$.*?(?<!\\)\$"," ",s,flags=re.S)
    s=re.sub(r"\\(?:label|cite|ref|eqref|url|nolinkurl)(?:\[[^\]]*\])?\{[^{}]*\}"," ",s)
    s=re.sub(r"\\(?:section|subsection|paragraph)\*?\{[^{}]*\}"," ",s)
    s=re.sub(r"\\(?:begin|end)\{[^{}]*\}(?:\[[^\]]*\])?"," ",s)
    s=re.sub(r"\\[A-Za-z]+\*?"," ",s)
    return [re.findall(r"[a-z0-9]+",p.lower()) for p in re.split(r"\n[ \t]*\n",s) if re.findall(r"[a-z0-9]+",p.lower())]
raw={k:Path(v).read_bytes() for k,v in paths.items()}
p={k:normalize(v.decode("utf-8")) for k,v in raw.items()}
a,b=p.values()
eligible={k:sum(len(x)>=40 for x in ps) for k,ps in p.items()}
matches=[]
longest=(0,None)
for i,x in enumerate(a):
    for j,y in enumerate(b):
        sm=SequenceMatcher(None,x,y,autojunk=False)
        z=sm.find_longest_match()
        if z.size>longest[0]:
            longest=(z.size,{"sequel_paragraph":i+1,"correction_paragraph":j+1,"tokens":" ".join(x[z.a:z.a+z.size])})
        if min(len(x),len(y))>=40 and sm.ratio()>=.75:
            matches.append({"sequel_paragraph":i+1,"correction_paragraph":j+1,"sequel_tokens":len(x),"correction_tokens":len(y),"ratio":round(sm.ratio(),6),"exact":x==y})
def grams(ps):
    out={}
    for i,p in enumerate(ps):
        for j in range(len(p)-11):
            out.setdefault(tuple(p[j:j+12]),[]).append((i,j))
    return out
ga,gb=grams(a),grams(b)
common=set(ga)&set(gb)
coverage={}
for k,ps,g in [("sequel",a,ga),("correction",b,gb)]:
    covered=set()
    for key in common:
        for i,j in g[key]:
            covered.update((i,n) for n in range(j,j+12))
    total=sum(map(len,ps))
    coverage[k]={"normalized_tokens":total,"paragraphs":len(ps),"eligible_40_token_paragraphs":eligible[k],"covered_12gram_tokens":len(covered),"coverage_percent":round(len(covered)/total*100,6)}
print(json.dumps({"python":sys.version,"sha256":{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
"diagnostic":coverage,"shared_distinct_12grams":len(common),"paragraph_matches_40_tokens_at_075":matches,
"longest_normalized_contiguous_match":longest,"shared_12grams":[" ".join(x) for x in sorted(common)]},indent=2))
```

## Bibliography audit

Every historical bibliography item and every external scholarly item in the
sequel was checked against the following primary records, with the earlier
task's [bibliography audit](../TASK-20260911__arxiv_submission_audit/BIBLIOGRAPHY_ARXIV_AUDIT.md)
retaining the detailed earlier shelf/Supnick/survey and v1 checks. Check date:
2026-09-11. No primary result supplied evidence of a nonexistent reference.

| Entry | Primary metadata and observed result |
| --- | --- |
| Historical `mse` | [Original question](https://math.stackexchange.com/questions/4619480/circles-of-radius-1-2-3-n-all-touch-a-middle-circle-how-to-make-the-m): Dan, question 4619480, asked 16 January 2023 at 11:46. The question title in the correction matches the public title, including the middle-circle minimization question. This is a web question, so journal volume/pages/DOI do not apply. |
| Historical `uq` | [Official UQ question listing](https://uq.stanford.edu/questions) identifies the same question, UQ ID 295, date 1/16/2023, and links to the original MSE item. The [individual record](https://uq.stanford.edu/question/295) was not retrievable by this web tool. The preserved June 2026 access date belongs to the historical citation; this audit checked the listing on 11 September. The site's status badge is not a current theorem authority. |
| Historical `supnick` | [JSTOR journal issue](https://www.jstor.org/stable/i307286): Fred Supnick, *Extreme Hamiltonian Lines*, Annals of Mathematics, second series, 66(1), 179-201, July 1957; [DOI 10.2307/1970124](https://doi.org/10.2307/1970124). The article URL returned a JavaScript stub, while the issue record supplied the metadata. Correction's abbreviated author and omitted issue/DOI do not change its identity. |
| Historical `bdvvw` | [Publisher DOI record](https://epubs.siam.org/doi/abs/10.1137/S0036144596297514?download=true&journalCode=siread) and [authors' institutional full text](https://pure.tue.nl/ws/files/2373438/Metis148543.pdf): Rainer E. Burkard, Vladimir G. Deineko, Rene van Dal, Jack A. A. van der Veen, Gerhard J. Woeginger; *Well-Solvable Special Cases of the Traveling Salesman Problem: A Survey*, SIAM Review 40(3), 496-546 (1998); DOI 10.1137/S0036144596297514. Correction now expands the previously abbreviated title and includes the DOI. Name transliteration/TeX accent variants do not identify a different author. |
| Historical `mathews-zymaris-spinors` | [Authors' institutional publication record](https://research.monash.edu/en/publications/spinors-and-the-descartes-circle-theorem/) and [publisher record](https://www.sciencedirect.com/science/article/pii/S0393044025000427): Daniel V. Mathews and Orion Zymaris; *Spinors and the Descartes circle theorem*, Journal of Geometry and Physics 212, article 105458, 14 pages, June 2025; DOI 10.1016/j.geomphys.2025.105458. Direct publisher fetch was blocked (403); its indexed record and the successfully opened institutional record agree. |
| Historical `hifi` | [Publisher record](https://onlinelibrary.wiley.com/doi/10.1155/2009/150624): Mhand Hifi and Rym M'Hallah; *A Literature Review on Circle and Sphere Packing Problems: Models and Methodologies*, Advances in Operations Research 2009(1), article 150624, 22 pages, first published 5 July 2009; DOI 10.1155/2009/150624. Correction now supplies volume, article number, length and DOI. |
| Sequel `v1` | [Actual v1 record](https://arxiv.org/abs/2607.28654v1), reopened in this task: Maurizio Falconi; *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima*; arXiv:2607.28654v1 (2026), cs.CG, DOI 10.48550/arXiv.2607.28654. It reports ten pages and two figures with source/certificate repository link; no cross-list was displayed. MSC classes 52C26, 52C15, 05C85, 90C27. The displayed June submission date and July-style identifier are recorded as an external metadata mismatch; the citation's verified year/ID are retained without guessing a correction. |
| Sequel `shelf` | [Publisher record](https://jocg.org/index.php/jocg/article/view/3056): Helmut Alt, Kevin Buchin, Steven Chaplick, Otfried Cheong, Philipp Kindermann, Christian Knauer, Fabian Stehn; *Placing your coins on a shelf*, Journal of Computational Geometry 9(1), 312-327 (2018); DOI 10.20382/jocg.v9i1a10. All seven authors, title, issue, pages, year and DOI match. |
| Correction `sequel` | Same author and exact title as the actual proposed sequel source. No arXiv identifier yet exists in the task evidence. `PENDING_STANDALONE_ARXIV_ID` is an explicit dependency marker, not a fabricated external record. |
| Proof supplements | Author-owned repository proof documents, explicitly described as supplements rather than refereed publications. Commit and individual paths are verified below. No journal metadata or DOI is asserted. |

The direct MSE page fetch exposes Dan's question and comments but hides some
comments behind an expansion control. The Rei Henigman computation/comment
quoted by the historical narrative was not exposed in the retrieved page and
could not be independently checked through the available indexed searches.
Its preserved attribution is therefore **historical, externally unverified in
this audit**; no absence or contradiction is inferred. The audit does not use
that computation as evidence for a new result.

The shelf article acknowledges an established minimum-span disk model; the
sequel explicitly credits it and proves its own asymptotic/label-recovery
statements directly. It imports no complexity or approximation result and
does not infer priority from a narrow search. The correction credits classical
Supnick ordering and the survey's minimum/maximum-tour taxonomy, while its
chain-to-radius argument remains conditional on full realizability. Descartes
and general packing references are used for their stated tangency/context
roles, not as claims that the global central-circle problem was already solved.

### Public and pinned supplementary proof references

The read-only GitHub connector fetched
[the complete recursive pinned tree](https://api.github.com/repos/falker47/ringmin/git/trees/3beb8d70c5b3748d370a92855847bdf574e5a14f?recursive=1);
the response reported `truncated: false`. Every direct proof path in the final
two bibliographies exists at the common public snapshot, with these Git blob
object IDs. The earlier audit additionally verified the repository's public
visibility and this commit's accessible metadata. A Git tree read checks
existence/version attribution, not the mathematical correctness of its files.

| Path under `research/` | Git blob ID at `3beb8d70c5b3748d370a92855847bdf574e5a14f` |
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
| `SUPNICK_FULL_FEASIBILITY.md` | `94a6664993e40ea65390a9c110f76d2e3b096589` |
| `SUPNICK_SEAM_SEQUENCES.md` | `f0a1d148e73f0a162c158410686110f60ecfa3dd` |

All these references explicitly inherit the snapshot from the supplement
entry. The sequel cites the actual proof inputs, not merely internal
review-verdict documents. Its principal line/LP argument is also present in
the manuscript, so the external supplements chiefly carry the detailed
endpoint dependencies and reproducibility. The correction's preserved generic
repository URL remains a reproduction entry point; its newly imported
fixed-order theorem citations are pinned.

Both manuscripts disclose AI assistance in an acknowledgment and retain human
authorship/responsibility. The [current official AI-tool policy](https://info.arxiv.org/help/moderation/index.html#policy-for-authors-use-of-generative-ai-language-tools)
permits AI tools, requires the authors to take responsibility and disclose
significant use, and does not permit tools as authors. The wording identifies
software, drafting and proof/checking assistance without representing an
internal AI check as external peer review.

## Editorial handoff and limitations

The preferred architecture remains defensible after the final-source check.
For the eventual standalone Comments, accurately mention its relationship to
arXiv:2607.28654 and its new global asymptotic characterization; add the actual
final page count and pinned supplement information. Do not call it a
replacement of the whole earlier paper or present overlap diagnostics as
arXiv approval. For the later corrective replacement, preserve useful original
Comments information and state the actual correction and real sequel ID after
that ID is assigned. This report supplies no upload-ready corrective metadata.

This subtask independently audited editorial allocation, reference metadata,
repository pinning, current official policy and normalized textual reuse.
It neither rebuilt the PDFs nor reran mathematical certificates; those gates
are recorded by the parent and the manuscript-owning audit agents. It changed
only this report, performed no Git mutation or publication write, and preserves
the distinction among internal checks, independent scientific review, and
arXiv moderation.

Final report checks: the diagnostic code was extracted from this Markdown
and executed unchanged in an isolated Python namespace, exit 0, reproducing
the final source hashes and counts above. The report's explicit untracked-file
whitespace check found zero trailing-whitespace lines, and its two code-fence
markers were balanced. An earlier wrapper successfully printed the diagnostic
but then failed its report-size display because the embedded script reused
the wrapper's variable `p`; isolation corrected that wrapper-only error.
