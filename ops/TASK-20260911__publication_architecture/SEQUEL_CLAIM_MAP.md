# Standalone sequel: architecture, claim map and source checks

    mode=STRICT
    authoring_subtask=standalone asymptotic manuscript
    starting_head=227d09d480c2d88d09d3450c9015fc9737440c17
    scientific_supplement=3beb8d70c5b3748d370a92855847bdf574e5a14f
    initial_source_sha256=cc85749ed20fb0a64724f162c256443b8e069f928c111ca9865a3f34c502e6b9
    final_source_sha256=28853635a65267e1772352436f29d6c19d0a0b8ace823aa72a0d77f52ad8622f
    internal_review_is_external_acceptance=false

## Authorized scope and startup

Read the complete publication-architecture goal attachment and the applicable
AGENTS contract. The startup `git status --short` returned no changed paths;
`git rev-parse HEAD` returned the starting commit above. Both used the explicit
repository safe-directory override. Git printed a user-global ignore-file
permission warning but exited 0. Current status/index, relevant publication,
global, fixed-order and certification ledger sections, both prior manuscripts,
the prior submission handoff and the final mathematical review packet were
read. Earlier detailed scientific-source inspection in this same subagent
session remains applicable; the proof notes have not changed.

This subagent owns only `paper_assets/asymptotic_sequel/ringmin_asymptotic.tex`
and this task-local file. The root owns builds, metadata, bundles, publication
navigation, integration and the corrective-paper author's work. No new
research, claim ledger, certificate, production-code, verifier, Git-state or
external-state write was made by this subagent.

## Manuscript architecture

Title: **Minimum central circles: an effective characterization of the global
asymptotic constant**. The visible and PDF-metadata titles agree.

The initial completed source contains 532 lines and 25,693 UTF-8 bytes.
Its table of contents is:

1. Problem and relation to prior finite work.
2. Exact angular comparison.
3. Existence by genuine-label concatenation.
4. Effective finite-word characterization.
   - Finite types and a uniform quantization error.
   - Balanced words and the quantified boundary relaxation.
   - Exact certificates and computational meaning.
5. Explicit geometric upper constructions.
6. An explicit global lower endpoint.
7. Reproducibility and open questions.

An unnumbered Acknowledgment and References follow. The main all-n proof
remains self-contained. The longer endpoint and quantitative transfer
dependencies are identified by authoritative proof-note paths at one real,
immutable public supplement commit. No future arXiv identifier is invented.

The abstract advertises the all-n theorem, effective error and geometric
recovery. It makes no claim that finite optima or fixed-order classification
are this paper's new contribution. The introduction explicitly attributes
the Supnick/anti-Monge connection, finite framework, certified 3..14 range
and original 1/8 conjecture to arXiv:2607.28654v1. The old conjecture is
identified as disproved; historical finite results retain their numerical
guard and scope. No workflow labels, draft status or claims of internal or
external acceptance occur in the scientific narrative. AI assistance is
disclosed without presenting it as independent acceptance.

## Overlap audit: substantive blocks

| Block | Classification | Treatment in the sequel |
|---|---|---|
| Central-circle problem and chain/full/global distinction | Minimal duplicated background needed for self-containment | Brief explicit definitions; elementary chain-root identity is given locally. |
| Cosine-law pair angle and both directed arcs | Minimal duplicated background needed for self-containment | Re-derived because the all-n geometric squeeze starts here. This is not advertised as a new model. |
| Anti-Monge/Supnick theorem and canonical tour proof | Historical-paper core; cross-reference only in sequel | One attributed introductory sentence. No theorem/proof/table duplicated. |
| STN/Floyd-Warshall oracle, finite pruning and frontier machinery | Historical-paper core; cross-reference only in sequel | The prior finite framework is named and cited; algorithm and reproduction narrative removed from sequel. |
| Certified optimum tables, optimal cycles and floating regimes | Historical-paper core; cross-reference only in sequel | Only attributed certified scope 3..14 with original numerical guard remains. No finite table or regime analysis reproduced. |
| Post-v1 Supnick fixed-order seam classification | Cross-reference only / omitted as unnecessary to sequel | The large classification table and its proof outline from the former replacement candidate are removed. It is not a premise of the all-n proof. |
| Line-span problem and longest-path recurrence | Standalone-sequel core | Definition and proof retained, with all predecessor constraints. |
| Bounded closing cost and exact geometric squeeze | Standalone-sequel core | Complete proofs retained. |
| Genuine-label concatenation and normalized limit | Standalone-sequel core | Complete theorem/proof retained for all large integer sizes and both parities. |
| Finite types, balanced-word LP and directed certificates | Standalone-sequel core | Complete proof and exact error/computability discussion retained. |
| General finite/countable block transfer | Standalone-sequel core | Quantitative theorem and construction retained with strict T<1-alpha domain. |
| Four-block explicit upper endpoint and coupled lower endpoint | Standalone-sequel core | Exact definitions, proved scope, quantitative values and supplementary dependency paths retained. Neither endpoint is declared sharp. |
| Historical 1/8 and stronger deficit conjectures | Obsolete/superseded statement | Explicitly disproved and attributed to the preceding paper. No finite result is invalidated. |
| Global floating cascade/contact structure | Cross-reference/open question | No asserted all-n contact or floating conclusion; remains open. |
| Prior internal review packet and acceptance workflow | Task provenance, not a scientific contribution | Removed from scientific narrative/bibliography; preserved in repository history and task evidence. |

The sequel intentionally reuses the audited asymptotic core from the
unsubmitted former replacement candidate. That is the source material the
user authorized for this task, not a second publication of v1. Against v1,
the duplicated content is limited to the model and background necessary to
state the new proofs. Substantial prior finite-method, table and regime
prose is not republished. The root's combined overlap audit also assesses
the separately authored conservative correction.

## Retained theorem and material-claim map

Line locations below refer to the initial completed 532-line source; labels
identify the claims if a later layout correction shifts lines.

| Source block | Epistemic class and domain | Canonical owner and actual proof dependency |
|---|---|---|
| Introduction 56-63 | Attributed historical theorem/framework and computer-certified finite report, 3<=n<=14 with 1e-10 numerical guard | `knowledge/FIXED_ORDER_THEORY.md#anti-monge-supnick-chain-order`; `knowledge/CERTIFICATION.md`; actual v1 Sections 3-5 and unchanged certificate/verifier provenance. No new finite certification claim. |
| Angular kernel and chain root, 85-100 | Definition and elementary exact identities; positive radii, n>=3 for positive chain root | `knowledge/DEFINITIONS.md`; v1 model; cosine law; `GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md` Sections 1-2. Local added uniqueness sentence follows decreasing sum with limits n*pi and zero. |
| Line definition/recurrence, 102-122 | Definition and exact fixed-word optimum; finite marks in [0,1], zeros allowed | Global ledger normalized-limit entry; `GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md` Section 1. |
| `lem:closing`, 124-133 | Exact theorem; both pair arcs controlled | Same owner; global proof Section 2. Unit closing gap gives b<=B<=b+1. |
| `lem:squeeze`, 135-155 | Exact global bound for every n>=3 | Same owner/proof Section 2; exact asin/atan inequalities, not Taylor approximations. |
| `thm:existence`, 159-192 | Exact all-n global limit and intrinsic infimum identity | Same owner; global proof Section 3; actual quantile reassignment and all-pair concatenation. No finite computation, Supnick or endpoint result is a premise. |
| Finite-type limits, 196-217 | Exact subadditivity and quantization inequalities, all k>=1 | Same owner; global proof Section 4, including k=1 and zero-type case. |
| `thm:lp`, 232-258 | Exact effective global bracket, all k>=1,r>=2, joint limit | Same owner; global proof Section 5; empirical word lower bound and rational minimizing-vertex batch recovery. |
| Directed LP certificates, 261-282 | Exact computability in principle; finite rational endpoint verification | Same owner; global proof Section 6. Width `(1/k+1/r)/pi` plus controlled radical/pi arithmetic. No efficient algorithm or elementary expression is asserted. |
| `thm:blocks`, 303-363 | Exact finite/countable recovery with all-pairs geometry; fixed nonnegative lengths, T<1-alpha | `knowledge/FIXED_ORDER_THEORY.md#general-finite-and-countable-reflected-block-recovery`; `PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md` Sections 1-5, with `PERMUTED_ALTERNATING_HALVES.md` Sections 1-6 for the actual full root. |
| Exact x_*, alpha_hat, epsilon_b, Delta_*, 365-390 | Exact implicit auxiliary minimizers and rational enclosures within their specified families | Four actual proof notes named in bibliography `upperinputs`; global ledger reflected-prefix/boundary/mixed-width entries. These are not global optimizers. |
| `eq:U4`, 392-411 | Exact proved upper construction, U4=C4(1/20000), strict saving >1/4608000000000000 | Global ledger general-transfer/fourth upper entry; `PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md` Sections 1-5 plus general transfer Section 5. All old exact parameters stay fixed. |
| Lower endpoint definitions and `prop:lower`, 413-472 | Exact global lower corollary, unique auxiliary width optimum and directed rational enclosure | Global ledger four-level-width owner; `THREE_LEVEL_COMMON_CHAIN.md` Sections 7,9,11-12 and `COMMON_CHAIN_QUANTITATIVE_STABILITY.md` Sections 2-5,11. Same-order shared energy and strict-width limiting argument preserved. |
| Disproof of both v1 asymptotic conjectures | Disproved historical conjectures | Strict lower enclosure gives C_*>1/8; v1's actual conjecture statements are explicitly attributed. |
| Closing limitations, 474-494 | Scope/open questions | No elementary constant, efficient computation, endpoint sharpness, new finite optimum or universal floating cascade is claimed. Supplementary finite checks remain corroboration, not infinite proof. |

All ten proof-note paths in the bibliography were checked with `git cat-file
-e 3beb8d70c5b3748d370a92855847bdf574e5a14f:<path>` and exist in that exact
snapshot. The direct references replace task-audit citations; the mathematical
proof dependencies themselves are unchanged.

## Fresh bounded mathematical checks

Environment: local Windows PowerShell, CPython 3.14.3, existing installed
dependencies. No clean environment, dependency reinstall, hosted CI, external
review or exhaustive search regeneration is claimed. These standalone
research checkers do not import production Ringmin. SciPy in the word checker
proposes candidates, then exact Fraction gates verify the finite certificates.

The following existing checker commands were freshly run for this task.
All printed their full successful terminal output. The mathematical checker
results are local bounded evidence; the analytic sources carry all infinite
quantifiers. Normal assertion-enabled mode was used.

```text
python -I -S ops/TASK-20260911__global_variational_limit/check_line_recovery.py
PASS: 1089 rational words; 13995 independent paths; 13941 pair/closure checks; 1089 all-pair concatenations; 94620 genuine-label quantiles; 4 negative controls rejected.

python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py
PASS k=1 r=2: 1 words; 1 primal blocks; lambda in [0.500000000,0.500000000]; all rational primal/dual gates
PASS k=1 r=5: 1 words; 1 primal blocks; lambda in [0.800000000,0.800000000]; all rational primal/dual gates
PASS k=2 r=2: 4 words; 1 primal blocks; lambda in [0.353553390,0.353553391]; all rational primal/dual gates
PASS k=2 r=3: 8 words; 2 primal blocks; lambda in [0.436886723,0.436886724]; all rational primal/dual gates
PASS k=3 r=4: 81 words; 2 primal blocks; lambda in [0.409906398,0.409906399]; all rational primal/dual gates
PASS k=4 r=5: 1024 words; 3 primal blocks; lambda in [0.396136075,0.396136076]; all rational primal/dual gates
PASS 1119 complete word inequalities; 18 corrupt certificates rejected
Scope: bounded exact LP certificates; no finite Ringmin optimum, simple closed form, or asymptotic proof by computation.

python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py
PASS exact small domain: 30034 orders; 580560 cells; 173010 reflected and 254543 ordinary panel assignments
PASS rational-surrogate diagnostics: 18 orders; 1080000 cells; fourth lengths 0,2,2,2,4,4
PASS directed literal full max: 342 probes; 438 panel Lipschitz probes
PASS 4 negative controls: duplicate high, cyclic predecessor, reversed panel orientation, negative radical
NOTE finite arithmetic and rational-surrogate diagnostics only;
analytic proof supplies arbitrary parameters/k/m, full geometry and limits

python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
EXACT A-3w > 354539/1000000000 > 0
EXACT A-3w-4eta_0 > 154539/1000000000 > 0
EXACT a-w-eta_0 > 204539/3000000000 > 0
EXACT b-w-eta_0 > 520991513/1000000000 > 0
EXACT 3/2-M > 21016513/1000000000 > 0
PASS 16 corner partitions, 448 reflection moments, 48 branch probes, 6 sign/tie controls
EXACT 16-panel raw full-max increment <= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
PASS bounded exact support; analytic proof supplies interval and cubic term
NOTE no root solving, width scan, finite recovery, transfer or output files

python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py
PASS formal polynomial identities: global cubic remainder and scaling loss
PASS alternating rational Taylor gates: tau, q, pi
PASS exact cubic identities; G'<0 on [0,a]; isolated root signs
PASS positive F and KKT multipliers; unique-global proof applies
PASS accepted witness is not local: positive first-coordinate derivative
0.00136820131190299900276 < D_1 < 0.00136820131190299900279
0.00196196296152142894680 < D_2 < 0.00196196296152142894683
0.00241410289623904895464 < D_3 < 0.00241410289623904895467
0.00451910758124825999999 < x_star < 0.00451910758124827000001
0.00452089241875172999999 < h_star_1 < 0.00452089241875174000001
0.00451910758124825999999 < h_star_2 < 0.00451910758124827000001
0.00734089241875172999999 < h_star_3 < 0.00734089241875174000001
0.00035105290142936543670 < lambda_1 < 0.00035105290142936940356
0.00059414888796317986218 < lambda_2 < 0.00059414888796318518264
0.00000038803240421408705 < eta_width < 0.00000038803240421408841
0.00000038785322987836585 < eta_4 < 0.00000038785322987836588
0.00000000017917433572119 < eta_width-eta_4 < 0.00000000017917433572254
0.04619642739017392470216 < relative_gain_percent < 0.04619642739051527365913
0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392
0.00000000004864271653624 < strict_rational_witness_gain < 0.00000000004864271653627
PASS boundary floor failure for n=50000k+1; no eventual unchanged gate
PASS strict scaling: t=9999/10000, N=1106195; loss < 5e-11
PASS improved rational witness: both margins 1/100000, N=100000
PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers
```

The first four checks were grouped in two PowerShell invocations, each
exiting 0. The width checker printed its complete PASS output before a
separate inline source-language assertion failed in the same invocation;
that invocation exited 1 for the source helper, not the mathematical checker.
The root can rerun individual commands if separate process exit evidence is
required. Earlier optimized runs from the mathematical final packet are
historical evidence and are not relabeled as fresh runs here.

## Source verification and retained failed attempts

A Python comparison checked that the full source region from the line
definition through the LP/computability section is exactly unchanged from
the audited former replacement source. The entire upper-construction section
is likewise exactly unchanged. Thus no root/LP/transfer/endpoint formula was
altered by repackaging. The added chain-root explanatory paragraph and new
background/conclusion were directly read and checked against the authoritative
model. The changed lower prose removes workflow references and keeps the
strict-width/n-limit argument intact.

Final source helper output, exit 0:

```text
PASS source: 20 unique labels, 6 bibliography entries; all references resolve; UTF-8/whitespace/control and publication-language checks
SHA256 cc85749ed20fb0a64724f162c256443b8e069f928c111ca9865a3f34c502e6b9
PASS all 10 cited proof paths exist at pinned scientific snapshot
```

The helper reads UTF-8 source, checks unique labels and bibliography keys,
resolves every ref/eqref/cite, checks all lines for trailing whitespace and
forbidden control characters, and rejects literal publication-workflow phrases.
The complete `git diff --no-index -- paper_assets/v2/ringmin_v2.tex
paper_assets/asymptotic_sequel/ringmin_asymptotic.tex` was inspected; its exit
1 is the expected indication of differences, not a verification error.

Failed attempts retained for audit:

- The first in-memory source transformation used a non-raw Python string for
  a TeX paragraph; its explicit control-character guard detected the escaped
  `\full` before any file write and raised `RuntimeError`. The same operation
  was corrected to use raw strings and then wrote clean source successfully.
- Two early generic source-language scans were too broad: `candidate` matched
  legitimate LP solver candidates, and `replacement` matched the unchanged
  mathematical phrase “numerical replacements for the parameters.” Neither
  indicated workflow leakage. The final scan uses actual workflow phrases;
  it passed. No scientific sentence was edited merely to satisfy those scans.

Protected-path check:

```text
git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --exit-code 227d09d480c2d88d09d3450c9015fc9737440c17 -- paper_assets/ringmin_paper.tex paper_assets/ringmin_paper.pdf paper_assets/v2/ringmin_v2.tex paper_assets/v2/ringmin_v2.pdf
```

Exit 0, no diff. Both historical v1 and previously audited replacement
source/PDF remain intact. The root records clean compilation, PDF visual
inspection, final bundle hashes, cross-review and the combined publication
handoff separately. This source-authoring handoff is not external acceptance.

## Final source and layout closeout

The root's first clean compilation completed three passes but its strict
layout gate found an overfull box of 15.74173pt in the supplement paragraph.
The exact log line showed the long sentence prefix followed by the commit
hash. The sole corrective source change removed “mathematical” from
“The mathematical supplement ...”; the same immutable commit and sentence
meaning remain. The final source is still 532 lines and has SHA-256
`28853635a65267e1772352436f29d6c19d0a0b8ace823aa72a0d77f52ad8622f`.
The root owns the rebuild and PDF inspection; no build result is attributed
to this authoring subagent.

To remove ambiguity from the earlier combined shell invocation, the exact
width checker command above was rerun on its own. It exited **0**, producing
the same complete output shown above. Its protected mathematical
source and the manuscript's constant are unchanged; this rerun establishes
separate process-exit evidence after the unrelated helper's failure.

Final source and untracked claim-map checks both exited 0:

```text
PASS UTF-8/whitespace/control check: paper_assets/asymptotic_sequel/ringmin_asymptotic.tex
PASS UTF-8/whitespace/control check: ops/TASK-20260911__publication_architecture/SEQUEL_CLAIM_MAP.md
PASS 20 unique labels and 6 bibliography entries; all references resolve
FINAL SOURCE SHA256 28853635a65267e1772352436f29d6c19d0a0b8ace823aa72a0d77f52ad8622f
```

The source changes introduce no new scientific conclusion. All user-required
limitations remain explicit. The old replacement source/PDF and v1 source/PDF
were preserved, and no fake standalone identifier or publication-readiness
claim was written into this manuscript. The draft is handed to the root for
independent source/PDF cross-review and final task integration.

As an additional read-only cross-review, this subagent read the colleague's
entire corrective source. Its finite identity, asymmetric publication role
and separation of false asymptotic conjectures from surviving finite results
are coherent. One remaining exact-vs-numerical pocket/radius wording concern
in the “Free vs. paid floater” proposition was sent to the root for the
corrective author to resolve. This subagent made no edit to that source;
its final resolution belongs to the combined task's independent review.
