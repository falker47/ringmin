# Ringmin — Next Research Steps

## Role and retrieval

This is the sole ranked current research roadmap: scientific direction and
success criteria only. Current task state belongs to
[CURRENT_STATUS.md](../CURRENT_STATUS.md). Start with the
[compact index](../PROJECT_KNOWLEDGE.md), then read relevant ledger sections
and linked proof notes. The ledgers retain thematic claim ownership; this
roadmap does not independently prove or re-certify their summaries.

The complete prior roadmap, including resolved work and deferred review
scopes, is preserved in the
[historical snapshot](../docs/archive/RESEARCH_ROADMAP_20260910.md).
That archive is non-authoritative and is read only for a specific history or
provenance question, not routine orientation.

## Current scientific state and strongest results

- **Computer-certified finite results:** global optima for `3 <= n <= 14`;
  no expanded certification. See the [certification ledger](../knowledge/CERTIFICATION.md#computer-certified-finite-results)
  for the artifact/provenance/verifier requirements and limitations.
- **Exact fixed-order theory:** all formal Supnick seam onsets and the
  complete fixed-order full-feasibility classification are resolved. These
  do not establish global floating behavior. See the [classification entry](../knowledge/FIXED_ORDER_THEORY.md#complete-exact-supnick-fixed-order-feasibility-classification).
- **Proved global bounds:** the strongest current lower endpoint is
  `C_term+eta_4`; the strongest current upper coefficient is
  `C_3(1/250)`. Thus the current coefficient interval is
  `[C_term+eta_4,C_3(1/250)]`, and `R*(n)=Theta(n^2)`.
  The [four-level entry](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#four-level-improvement-at-a-fixed-rational-witness)
  owns the lower endpoint, its exact integral definition and finite bounds;
  the [fixed 1/250 global entry](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#fixed-third-width-1250-improved-global-upper-bound)
  owns the upper corollary. The source statements are
  [four-level Section 11](THREE_LEVEL_COMMON_CHAIN.md#11-a-fixed-four-level-rational-improvement)
  and [fixed 1/250 Section 7](PERMUTED_HALVES_THIRD_BLOCK_250_TRANSFER.md#7-consequence-bounded-checker-and-scope).
  Neither endpoint is established as sharp; no normalized global limit is proved.
- **Resolved lower-bound discriminators:** a single induced-subset chain
  envelope and one-level terminal coupling cannot improve the leading
  coefficient. Macroscopic prescribed-order excess is resolved, and the
  common-chain stability/global/minimax results and shared crossing budgets
  supply successive lower improvements. The fixed rational three-cutoff
  witness now proves eta_4>eta_3+1e-7 with all finite gates discharged.
  See the corresponding sections of the [global-bounds ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
  The [arbitrary-finite-cutoff extension](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#arbitrarily-many-finite-cutoffs-with-one-shared-crossing-energy)
  now supplies the general shared-energy lemma and finite minimax corollary,
  with a precise pointwise sharpness scope. The user reports that extension
  accepted; its fixed four-level application awaits independent review.
- **Exact deletion-exponent theorem:** [Section 11](COMMON_CHAIN_QUANTITATIVE_STABILITY.md#11-the-square-root-loss-is-not-sharp-for-actual-cyclic-tours)
  rules out square-root sharpness uniformly over actual tours.
  [Section 11.5](COMMON_CHAIN_QUANTITATIVE_STABILITY.md#115-the-crossing-exponent-23-is-sharp-for-genuine-cyclic-tours)
  resolves the crossing-term discriminator: an explicit infinite family of
  genuine cycles makes exponent 2/3 sharp for K.
  [Section 11.6](COMMON_CHAIN_QUANTITATIVE_STABILITY.md#116-signed-discrepancy-of-the-same-explicit-cyclic-family)
  now resolves signed deletion for the same family by exact edge accounting
  and a rigorous expansion: its normalized absolute discrepancy has a
  positive limit at exponent 2/3. Seeking a uniform stronger exponent or
  little-o at that scale for K or signed Delta is therefore closed.
  Sections 11.3-12 now optimize the existing midpoint split and propagate
  its improved constant through the scalar minimax, finite errors and
  full-feasible deletion. This closes optimization of that particular
  split, without identifying the best tour constant or a minimizing tour.
  External acceptance of these proofs remains separate.
- **Continuous-only upper improvement:** a unique mixed third-block width
  minimum lies below `C_3(1/250)`, whose fixed-width geometric transfer is
  now proved. The mixed-width minimum still has no geometric transfer. See the
  [mixed-width entry](../knowledge/FIXED_ORDER_THEORY.md#unique-continuous-mixed-width-minimum-of-the-third-reflection);
  these continuous costs do not replace the current global upper bound.

## Priority 1 — Independent review of the fixed four-level witness

Independently review `THREE_LEVEL_COMMON_CHAIN.md`, Section 11, at committed
HEAD. Reproduce the fixed-witness arithmetic checker and audit the rational
integral tails, moving-q errors, old eta_3 comparison, all-n floor/stability
gates and finite/global transfer through the accepted corollary. Confirm
the three supplied cutoffs and widths are unchanged. Record acceptance or
precise corrections; stop before parameter search or further research.

## Deferred direction — Determine the true leading asymptotics

Determine the true normalized liminf and limsup within
`[C_term+eta_4,C_3(1/250)]`, and whether they agree. The concrete four-level
discriminator is resolved positively at the supplied rational witness.
Review that application before selecting further lower-bound work.
Neither the fixed witnesses nor scalar sharpness of the preceding
two-level envelope establish a ceiling on common-order methods. The crossing and
signed-discrepancy obstructions close improvements that require a uniform
exponent above 2/3, or little-o at that scale, for K or |Delta| over tours.
They do not establish an optimal envelope constant or minimax tour.
Further three-block refinement is deferred.
Success must address full feasibility or genuinely coupled constraints. Neither known endpoint
is established as sharp. The coefficient `1/8` is already disproved by
`liminf R*(n)/n^2>=C_term>1/8`, as recorded in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`; it is not an open candidate.
The claim that the floating set is `o(n)` remains unproved.

## Deferred dependency reviews

The previously prioritized fixed 1/250 transfer review remains deferred,
not completed: audit `PERMUTED_HALVES_THIRD_BLOCK_250_TRANSFER.md`, its exact
f=2*floor(m/500) construction, shared seams, width-dependent gates, full-root
all-pairs criterion, quantitative recovery and separate odd lower squeeze.
Reproduce its checker including rational root signs and both-path witnesses;
check the global limsup propagation and preservation of the old C_3 meaning.

Earlier dependency-review scopes remain deferred, without implying completion
or changing acceptance status. Retrieve only the relevant scope from the
[historical snapshot](../docs/archive/RESEARCH_ROADMAP_20260910.md), then its
owning ledger, proof and specifically linked dossier. This includes the
lower-bound dependencies, fixed-order classification, and the continuous
upper/recovery/full-root chain. Their detailed audit instructions are cold
history, not a second queue of current priorities. Revisit a dependency when
it materially affects the chosen task; success remains acceptance or precise
corrections within that dependency's stated scope.

The Section 12 optimized-split review is deferred; no independent acceptance
is implied. Its scope remains Sections 11.3-11.4 and the Section 12
propagation: h>0 and E=0, scalar minimum, coefficient transfer, rational
enclosures, finite error directions, nested full-feasible deletion and the
linked bounded checker. The previously
prioritized Section 11.6 signed-discrepancy review is deferred, not
completed: its scope is the exact radical formula, isolated deletions,
signed cancellations, one-sided expansion, uniform remainder, actual
floor and both parities, with the Section 11.5 family as dependency and
the linked bounded checker. The standalone Section 11.5 crossing review
also remains unrecorded. Neither family is a premise for the optimized
all-tour envelope or its global transfer; retrieve their specific proofs
and dossiers when those reviews become the chosen task.

## Deferred direction — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
