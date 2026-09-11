# Submission-focused scientific audit

    mode=STRICT
    reviewer=separate internal scientific subagent
    reviewed_base=3beb8d70c5b3748d370a92855847bdf574e5a14f
    reviewed_on=2026-09-11
    independent_external_acceptance=not performed or implied
    initial_candidate_sha256=528498d131b2d942c15b39b642aa33f8e9b8424bb081d6f826e2479dc986122f
    final_candidate_sha256=189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a
    final_scientific_outcome=NO_OPEN_SCIENTIFIC_FINDINGS

This is a fresh, bounded scientific and readability review for submission.
It is independent of the current builder's packaging work, but remains an
internal subagent review. It does not replace external acceptance under the
repository review protocol. No new research was performed. This subagent
edited only this audit file and made no Git or external-state mutations.

The complete 565-line initial `paper_assets/v2/ringmin_v2.tex` was read.
All TeX line references below identify that initial candidate at the base
commit, so they remain unambiguous if corrections shift the final lines.
The root reviewer owns final correction status and final candidate hashes.

## Outcome and actionable findings

No material mathematical defect was found in the global limit, the balanced
word LP characterization, the finite/countable block transfer theorem, or
the transcription of the retained explicit endpoint and fixed-order claims.
Three small but substantive exposition corrections were requested:

| ID | Severity | Initial location | Finding and required minimal correction | Status at this audit's first handoff |
|---|---|---|---|---|
| SCI-1 | IMPORTANT | TeX 37-39, abstract | “Every finite or countable adjacent reflected-block construction” omits the essential strict total-length hypothesis. `PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md` Sections 1 and 5 require `T<1-alpha`; no equality/wrap-crossing extension is part of this submission. Include that restriction in the abstract, matching TeX 274-275 and 299-300. | Sent to builder; awaiting corrected-source readback |
| SCI-2 | IMPORTANT | TeX 68-72, shelf interpretation | The centers are `(2x_i,a_i)`, so their physical horizontal center span is already `2(max x_i-min x_i)`. “Twice the center span” introduces an unintended extra factor of two. State that the envelope span differs from `2(max x_i-min x_i)` by at most two (or from the horizontal center span by at most two). | Sent to builder; awaiting corrected-source readback |
| SCI-3 | IMPORTANT | TeX 285-287, 318-321, 338-340 | The proof uses `g` and `G_m` without actually defining them. Define `g(t,X,Y)` as the displayed literal maximum and `G_m=(1/m) sum_i g(i/m,P_(i-1)/m,P_i/m)`. This fixes the normalization needed to verify the score/root estimate. Both definitions already occur in the authoritative block note Section 3. | Sent to builder; awaiting corrected-source readback |

These are corrections to existing scope, coordinates and notation. None
changes a theorem, endpoint, numerical certificate or research conclusion.
No cosmetic expansion is requested. In particular, the supplementary proof
dependency outlines need not be replaced by lengthy new proofs in the paper.

## Startup, source scope and authority

Read the user-supplied goal objective, repository `AGENTS.md`,
`PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant current roadmap
entry, and the named final packet, claim matrix and verification record.
An initial `git -c safe.directory=<repository-root>
status --short` returned no changed paths. Git printed warnings that the
user-global ignore file was unreadable; the command exited 0. Concurrent
changes by the root and other delegated reviewers are authorized task work.

The principal proof sources read in full were:

- `research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md`, Sections 1-6.
- `research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md`, Sections 1-5.
- `research/PERMUTED_ALTERNATING_HALVES.md`, Sections 1-6 (complete mathematical proof before its bounded evidence section).
- `research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md`, Sections 1-5.
- `research/SUPNICK_FULL_FEASIBILITY.md`, Sections 1-6.

The following targeted authoritative sections and exact definitions were
also read and checked against the claims made by this manuscript:

- `research/THREE_LEVEL_COMMON_CHAIN.md`, Sections 7, 9 and 12 in full; the retained cutoffs and numerical enclosures in Sections 11-12.
- `research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md`, Sections 1-2 and the defining complete integral; `research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md`, Sections 1-2 and the exact isolation statements in Section 5.
- The definitions, uniqueness statements and dependency paths for `E`, `x_*`, `K`, and `alpha_hat` in `PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md` and `PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md`, followed through the previously recorded complete minimal upper audit.
- `research/FIXED_K_SUPNICK_SEAM.md`, the theorem, canonical order, edge formulas and root definitions; `research/SUPNICK_SEAM_SEQUENCES.md`, the all-k theorem and Section 6 induction/threshold conclusion.
- The explicit lower, upper and fixed-order dependency audit records named by the final packet, as historical internal evidence, not fresh external acceptance.
- The corresponding targeted global/fixed-order/certification ledger entries, `verify.py` precision and guard definitions, the original v1 conjecture wording, and the recorded twelve-size clean-source full-verifier output.

This is a submission claim audit, not a claim to have independently repeated
every historical proof dependency and exhaustive generation run in the
supplement. Bibliographic verification, package building, PDF rendering and
arXiv metadata are delegated to the root/other reviewers.

## Abstract: every sentence and quantitative clause

| Initial TeX lines | Claim | Assessment and authority |
|---|---|---|
| 27-28 | Definition of the minimized central radius with external tangency/non-overlap. | Correct model definition; cosine-law derivation and global note Section 2. |
| 28-30 | `R*(n)=C_* n^2+o(n^2)` with finite LP characterization and vanishing error. | Exact theorem; global note Sections 3-6. The proof covers all orders and both parities. |
| 30-33 | All-pair line separation by geometric means. | Correct: marks are normalized radii, not their square roots; global note Sections 1-2. |
| 33-35 | Bounded boundary concatenation and balanced programs give matching bounds. | Correct, including actual target-label reassignment and finite rational batches; Sections 3 and 5. |
| 35-36 | Gap `(1/k+1/r)/pi` before directed arithmetic error. | Correct theorem width, not a computed decimal error or an efficient algorithm; Sections 5-6. |
| 37-39 | Every finite/countable block construction transfers, with a strict four-block improvement. | Transfer/improvement valid in the source's domain. SCI-1 requests the omitted strict-total-length qualifier. |
| 39-40 | Explicit interval `C_term+eta_width <= C_* <= U_4`. | Correct; neither endpoint asserted sharp. Lower source Section 12 and general block source Section 5. |
| 41-42 | Original certified `3..14` and exact fixed-order theory stay distinct from global asymptotics. | Correct class and scope. No additional certified size or global contact theorem is implied. |
| 43 | Earlier coefficient `1/8` is false. | Correct consequence of exact lower enclosure, which is strictly greater than `1/8`. |
| 43-45 | Efficient evaluation, elementary expression, global floating structure remain open. | Correct limitations; no finite experiment is offered as an all-n argument. |
| 45-46 | Internal checks, external acceptance pending. | Matches final packet and current review status; no external acceptance inference. |

## Introduction: every assertion

| Initial TeX lines | Claim | Assessment and authority |
|---|---|---|
| 51-52 | Outer-to-central tangency is required; outer-to-outer tangency is optional. | Correct problem domain. |
| 52-55 | Adjacent chain, fixed-order full and global quantities. | Correct distinct definitions and minimization domain. |
| 56-57 | Chain is a lower bound; a feasible construction is an upper bound. | Correct inequality direction; no chain/full or feasible/optimal conflation. |
| 59-61 | V1 reports finite optima and proposes `1/8`; later lower bounds disprove it. | Checked against v1 conjecture statements and the lower endpoint source. Historical wording is left in v1. |
| 60-61 | V1 is historical. | Correct publication scope; no claim that an arXiv record has already been replaced. |
| 62-63 | Effective leading coefficient is proved in the main line/LP sections. | Correct; the proof is self-contained from the elementary angular model. |
| 64-66 | Main proof is independent of the long explicit endpoint chains; those are supplied separately. | Correct dependency separation. The endpoint mechanisms are not needed to prove existence or computability. |
| 68-70 | Shelf geometry equivalence. | Directly rederived: `(2 dx)^2+(a_i-a_j)^2 >= (a_i+a_j)^2` iff `|dx|>=sqrt(a_i a_j)`. |
| 71-72 | Envelope comparison. | SCI-2: correct bound after removing the factor-two center-span ambiguity. In symbols `2 span(x) <= envelope <= 2 span(x)+2`. |
| 72-76 | Shelf model attribution; no model novelty or imported approximation/complexity theorem. | No unsupported priority claim in the manuscript. Exact bibliographic data are assigned to the bibliography reviewer. |

## Principal proof and theorem audit

### Angular comparison and line reduction (TeX 80-143)

Both forms of theta are identical for positive `R,u,v`. The half-angle
cosine-law argument controls the smaller angle by requiring both directed
arcs, so no complement constraint disappears. The lower angular estimate
uses `asin(z)>=z` and the upper estimate uses `atan(z)<=z`, in the correct
directions without a Taylor hypothesis.

The fixed-word all-predecessor recurrence, ordered coordinates, path
interpretation, deletion/mark monotonicity and homogeneity were rederived.
The `j=i-1` predecessor makes coordinates nondecreasing even with zero
marks. The minimum over finitely many orders is attained. The closing
lemma covers both arcs: the complementary arc contains a full unit gap.
Scaling the angular circumference by `(R+n)/(2n)` gives exactly
`pi(R+n)/n`, and the reverse construction at `R=n(b_n+1)/pi` satisfies
every original pair. Thus both bounds in the squeeze theorem at TeX
123-129 have the correct normalization and all-n domain `n>=3`.

### Existence theorem (TeX 147-180)

The construction keeps actual points, not merely marginal distributions.
For `q=ceil(N/n)`, the ith smallest copied mark is `ceil(i/q)/n`;
multiplication by `nq/N` makes it at least `i/N`. Assigning each distinct
target label exactly once and decreasing its copied mark preserves every
pair constraint. Marks temporarily greater than one are explicitly dealt
with by homogeneity after the original unit-gap construction.

Dividing the constructed span by `N` gives the stated limsup bound for
each fixed `n`; taking `n` along the liminf subsequence proves existence.
The infimum identity follows in both directions. The simple large-mark
subsequence proves `E>=1/4` in the limit, hence strict positivity. No
assumption about Supnick, full feasibility of a chain, a continuum
minimizer, parity or an optimizer contact graph enters the argument.

### Finite types and LP theorem (TeX 184-270)

The type subadditivity proof and the lower/upper bins were checked,
including `k=1` and zero marks. Adding the q top marks costs at most q
including the join; the resulting error is `1/k`. Uniform grid marks
are squeezed coordinatewise by the sorted type multisets.

For the LP lower bound, splitting an optimal ordered multiset into
consecutive r-vertex words gives sum of word spans at most the full span.
The discarded fewer-than-r counts vanish after normalization; compactness
gives a feasible balanced limiting distribution. This yields
`lambda<=e_k` with no erroneous finite exact-balance assertion.

The feasible constraint polytope is rational and compact. A minimizing
vertex is rational despite algebraic costs. If D clears its denominators,
each type occurs exactly `Dr/k` times, necessarily an integer; concatenating
the literal word placements and repeating batches yields `e_k<=lambda+1/r`.
Combining with type quantization gives the displayed bracket and joint
limit, with no unproved cyclic compatibility constraint on the LP weights.

Each increasing path has at most `r-1` edges; directed radical enclosures
therefore control word span and LP value with the stated normalization.
Rational endpoint LPs can be solved by finite vertex enumeration and their
primal/dual inequalities checked without an algebraic equality oracle.
The exponential `k^r` cost and lack of a practical precision guarantee
are explicit. TeX 220-228 and 249-270 contain no efficient-algorithm claim.

### General block theorem (TeX 274-346)

The measure, separate high marginals, adjacent-slab domain and literal max
match the full authoritative proof. In the finite construction, every
rounded block has even endpoints and reverses precisely its even ranks.
Disjoint involutions composed with the cyclic high shift give a genuine
permutation. The strict length margin implies `m-s-a_k>=2`, including
floor ties, zero blocks, length-two identities and both parities.

The cell inventory includes every block exit/shared entry, cyclic
predecessor and both possible wrap cells. The maximum is globally
4-Lipschitz in the maximum coordinate norm because the chord dominates
below `t=1/4`, avoiding the square-root derivative at zero. The panel,
rounding and exceptional-cell error terms reproduce
`(6k^2+28k+36)/m`; adding the angular error gives the theorem's
`6k^2+28k+1060` coefficient. SCI-3 requests that the manuscript make
the already-used `g` and `G_m` definitions explicit.

The arbitrary-high proof was read for all three pair classes and both
directed paths. A whole high path contracts using the shell triangle
inequality. Mixed endpoints either use their incident high gap or a
nonempty high path whose endpoints dominate their radius requirements.
The two-low case uses a shared high or a nonempty intervening high path.
The local cells are consequently sufficient as well as necessary, even
at `m=2`, and the score's unique root is the actual fixed-order full
minimum. It is not claimed to be a global optimum.

At `c=1/32` and `c=1/2`, `m>=2048` brackets the true normalized root
before substitution into the error estimate. The countable proof keeps
`sum ell_j < 1-alpha`, truncates to finite constructions and uses the
bounded literal cost to control the omitted tail. A diagonal sequence
pays the `k^2/m` error and tail error; it supplies actual orders. Odd-size
upper bounds are obtained by deleting the largest label from a feasible
even placement, with the normalization ratio tending to one. No
countable exact finite formula, equality-margin extension, infinite
partition optimum or measure-only recovery assumption is asserted.

## Retained endpoints, finite theory and quantitative transcription

| Initial TeX lines | Checked mathematical statement | Result and source |
|---|---|---|
| 348-358 | Exact E, unique x_* on `[0,1]`, K, alpha root, `A` and `lambda`. | Same literal integral normalization and parameters as the four input proofs; no replacement by a decimal or midpoint. |
| 359-365 | Separate mixed second and third widths, minimized on their fixed-start domains. | Matches boundary minimum Section 1 and mixed third-width Section 1, including closed endpoints. No joint optimizer is claimed. |
| 366-373 | `.1093<alpha_hat<.10931`, `.2876<x_*<.2877`, `.043<epsilon_b<7/160`, `29/5000<Delta_*<27/4000`. | Exact rational isolations agree with sources; the sharper epsilon upper bound is supplied in third-width Section 5. |
| 375-378 | C3, C4 and `U4=C4(1/20000)`. | Correct separate slab lengths and the fixed exact Delta_* baseline; not the old unqualified rational-width C3. |
| 379-387 | Fourth increment integral, strict chord branches, positive denominator bounds. | Recomputed by centering the fourth slab and rationalizing its chord decrement; fourth note Sections 2, 4-5. |
| 388-390 | `C_*<=U4<C3(Delta_*)-1/4608000000000000`. | Correct saving: `eta^3/576` at `eta=1/20000`; full-geometric transfer is paid by the general theorem. Fresh exact checker agrees. |
| 391-394 | Cubic decrement and one-sided quartic remainder; no four-block/global optimality claim. | Signs and coefficients agree with fourth note Section 5. |
| 398-409 | Tau, q, C_term, three cutoffs, D_i and F. | Exact definitions match lower note Sections 9, 11-12. The auxiliary q and radius normalization are not confused. |
| 410-419 | Closed feasible width region and unique scalar maximizer. | Width differences exactly `a=113/12500`, `b=593/50000`; derivative numerator is `N'L+432N`. The manuscript's z_* avoids the upper proof's x_* name. |
| 420-430 | Lower bound and two rational decimal endpoints; both v1 asymptotic claims false. | Exact source Section 12.3 and fresh directed arithmetic checker reproduce both endpoints. Strict `L>1/8` refutes both conjectures, not just a numerical fit. |
| 431-454 | Dependency-explicit lower proof outline. | The shared energy is charged once, yielding denominator `16+432 sum h`; exact cubic remainder gives global uniqueness. Strict width scaling then n-limit and final t-limit respect finite floor failures. No unsupported closed-boundary eventual gate. |
| 459-463 | Increasing-radius anti-Monge/Supnick chain order. | Correct sign and chain scope in the manuscript; the primary citation details/sign import are covered by the bibliography reviewer and historical fixed audit. No uniqueness theorem is asserted. |
| 465-478 | Complete table for every integer `k>=1,n>=k+2`. | Matches full-feasibility Section 6: first strict failures 8,13,17,21,25 and `4k+6` for all `k>=6`. The last row derives from an all-k proof plus the exact k=6 bridge, not extrapolation. |
| 479-484 | Seam iff, minimum triangle defect, both-path telescoping and no global floating claim. | Read and rederived from full-feasibility Sections 2-4; closure forces every adjacent gap. Integer signs are strict while the iff theorem correctly allows equality. |
| 486-493 | Finite certified scope `3..14`, `1e-10` tolerance, `1e-12` brackets, 50 digits, twelve-size pass and n=14 coverage. | Consistent with verifier constants, ledger and historical clean-run output. `13!/2=3113510400` is the canonical cycle count. The recorded run is historical local evidence, not a fresh run by this subagent. |
| 494-495 | Larger-n candidates remain heuristic. | Correct limited evidence class; no new certified size. |

## Reproducibility and concluding sentences

TeX 499-504 correctly distinguishes bounded checker evidence from analytic
infinite quantifiers. Fresh execution below independently corroborates the
stated line, word, full-max and width finite cores; no sampled computation
is substituted for the proof. TeX 506-516 describes the existing original
log restoration and correctly labels `--skip-frontier` as smoke. The full
frontier result referenced by the paper is traceable to the original
clean-run record; I did not regenerate exhaustive searches or rerun that
full verifier in this subtask.

TeX 517 makes no claim of hosted CI or external acceptance. Every sentence
of TeX 519-527 is consistent with the scope: the normalized constant is
effectively characterized, practical evaluation and structural questions
remain open, no closed form or contact conclusion is inferred, and internal
AI-assisted checks are not author approval or external review. No global
floating cascade is asserted in the conclusion or elsewhere. No new
scientific conclusion is needed to correct any finding in this audit.

## Fresh executable verification by this subagent

Environment: local Windows PowerShell, CPython 3.14.3, existing installed
dependencies; no dependency installation or clean environment is claimed.
All five checker commands below exited 0. They run standalone research
checkers, not production Ringmin code. The LP checker uses the installed
SciPy proposal solver followed by exact rational validation. Evidence is
bounded local computation, not external acceptance or an all-n proof.

```text
python -I -S ops/TASK-20260911__global_variational_limit/check_line_recovery.py
PASS: 1089 rational words; 13995 independent paths; 13941 pair/closure checks;
1089 all-pair concatenations; 94620 genuine-label quantiles;
4 negative controls rejected.

python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py
PASS k=1 r=2: 1 words; 1 primal blocks; lambda in [0.500000000,0.500000000]
PASS k=1 r=5: 1 words; 1 primal blocks; lambda in [0.800000000,0.800000000]
PASS k=2 r=2: 4 words; 1 primal blocks; lambda in [0.353553390,0.353553391]
PASS k=2 r=3: 8 words; 2 primal blocks; lambda in [0.436886723,0.436886724]
PASS k=3 r=4: 81 words; 2 primal blocks; lambda in [0.409906398,0.409906399]
PASS k=4 r=5: 1024 words; 3 primal blocks; lambda in [0.396136075,0.396136076]
All rational primal/dual gates passed.
PASS 1119 complete word inequalities; 18 corrupt certificates rejected

python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py
PASS exact small domain: 30034 orders; 580560 cells;
173010 reflected and 254543 ordinary panel assignments
PASS rational-surrogate diagnostics: 18 orders; 1080000 cells;
fourth lengths 0,2,2,2,4,4
PASS directed literal full max: 342 probes; 438 panel Lipschitz probes
PASS 4 negative controls: duplicate high, cyclic predecessor,
reversed panel orientation, negative radical

python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py
PASS formal polynomial identities: global cubic remainder and scaling loss
PASS alternating rational Taylor gates: tau, q, pi
PASS exact cubic identities; G'<0 on [0,a]; isolated root signs
PASS positive F and KKT multipliers; unique-global proof applies
0.14056946887766098063257 < C_term+eta_width
                       < 0.14056946887766098063392
PASS boundary floor failure for n=50000k+1; no eventual unchanged gate
PASS strict scaling: t=9999/10000, N=1106195; loss < 5e-11
PASS improved rational witness: both margins 1/100000, N=100000
PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers

python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
EXACT A-3w > 354539/1000000000 > 0
EXACT A-3w-4eta_0 > 154539/1000000000 > 0
EXACT a-w-eta_0 > 204539/3000000000 > 0
EXACT b-w-eta_0 > 520991513/1000000000 > 0
EXACT 3/2-M > 21016513/1000000000 > 0
PASS 16 corner partitions, 448 reflection moments, 48 branch probes,
6 sign/tie controls
EXACT 16-panel raw full-max increment
<= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
PASS bounded exact support; analytic proof supplies interval and cubic term
```

The displayed checker outputs retain the material results, with long lines
wrapped and ancillary lower-width diagnostic values omitted. Assertions
were enabled; optimized reruns in the earlier final packet remain earlier
evidence and are not claimed as additional runs here.

One scoped text search initially named a nonexistent
`results/optimum_n14.json` and exited 1 after reporting that missing path.
This was an inspection-path mistake, not a failed verifier. A subsequent
`rg --files results` identified the actual `results/n14/optimum.json` and
`results/frontiers/n14_frontier.json` locations. No file was created or
modified to accommodate the mistaken path.

## Handoff and limits

All initial theorem statements and quantitative claims are consistent with
the reviewed source hierarchy within the scope above. The three requested
corrections should be verified on the final TeX before the builder marks
the submission audit complete. Existing internal status is preserved;
there is no externally accepted-baseline update here.

Protected historical v1 TeX was read for the conjecture comparison but not
edited. Production code, the verifier, original finite certificates,
proof notes, thematic ledgers and all published v1 assets were untouched by
this subagent. No mathematical experiments beyond rerunning the existing
bounded checkers were introduced. The remaining task is the parent task's
final corrected-source/package validation, not a new research direction.

## Final corrected-source closeout

Read the entire final TeX diff against
`3beb8d70c5b3748d370a92855847bdf574e5a14f` and the changed passages in
their final context. Independently hashed the final source with PowerShell
`Get-FileHash -Algorithm SHA256`: it is exactly
`189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a`.
The final candidate has 581 source lines.

| Finding/change | Final TeX location | Fresh closeout |
|---|---|---|
| SCI-1, IMPORTANT | 37-41 | CORRECTED. The abstract explicitly requires total slab length strictly below `1-alpha` and defines `0<=alpha<1` as the shift parameter. It matches the theorem at 277-303. |
| SCI-2, IMPORTANT | 70-75 | CORRECTED. The envelope comparison now uses exactly `2(max_i x_i-min_i x_i)`. The direct shelf equivalence and scale are consistent. |
| SCI-3, IMPORTANT | 321-329 | CORRECTED. The literal g and normalized empirical sum G_m are explicitly defined with the correct low/high scaling, predecessor and `1/m` factor. |
| Numerical certificate scope | 494-506 | The added finite-error-guard qualification is accurate. Fresh inspection of `verify_frontier` confirms that it checks saved coverage summaries/prefix logs, top-excluded guards and retained orders; it does not enumerate every excluded order with directed intervals. No numerical certificate is promoted into an interval proof. |
| Immutable supplement | 510-518, 573-579 | The source supplement is pinned to the reviewed base commit, with explicit allowance for the already-cited earlier mathematical checkpoint. This adds provenance, not a new claim. |
| PDF title and date hygiene | 7, 21-23 | PDF title now matches the visible title; the transient unsubmitted-candidate subtitle is removed. Neither change alters mathematics. |
| Removal of transient no-submission sentence | 533-540 | Removing the initial 524 sentence makes the eventual submission source durable. The conclusion retains all scientific limitations and the distinction between internal assistance, author approval and external review. |

All three scientific findings are closed; no scientific BLOCKER or
uncorrected IMPORTANT finding remains in this review's scope. The changes
introduce **no new scientific conclusion**, no expanded certified finite
range and no stronger global/contact/countable-partition quantifier.

The root reviewer reported its own fresh full-verifier execution at all
twelve sizes, restoring 12 logs/9,649,682 bytes, and a clean stabilized
nine-page build. Those are root-run results to be recorded in the parent
evidence; they are not additional executions by this scientific subagent.

Final `git diff --check` exited 0. A separate Python UTF-8 read of this
untracked audit checked every line for trailing whitespace and its final
newline, printing `PASS scientific audit UTF-8, final newline and no trailing
whitespace`. The audit text was inspected in full during creation. No
source or protected file was edited by this subagent. Scientific closeout
does not independently decide arXiv environment compatibility, submission
metadata provenance, final PDF appearance or external acceptance.

An initial closeout append patch failed harmlessly because its context
line had different wrapping. The exact tail was read and the patch reapplied;
the failed attempt changed no file.

Command display convention: `<repository-root>` replaces only the local
`safe.directory` path, to avoid storing a machine-specific absolute path.
All other shown command arguments and results retain their recorded meaning.
