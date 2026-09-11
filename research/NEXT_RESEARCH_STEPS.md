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
  `C_term+eta_new`; the strongest current upper coefficient is `C_3`, still
  exactly `C_3(1/1000)`. Thus the current coefficient interval is
  `[C_term+eta_new,C_3]`, and `R*(n)=Theta(n^2)`.
  The [common-chain entry](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#quantitative-stability-for-the-fixed-macroscopic-common-chain-pair)
  owns the lower endpoint, its exact integral definition and finite bounds;
  the [three-block global entry](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#three-block-full-root-transfer-improved-global-upper-bound)
  owns the upper corollary. The source statements are
  [common-chain Section 12](COMMON_CHAIN_QUANTITATIVE_STABILITY.md#12-refined-two-level-minimax-from-the-proved-deletion-envelope)
  and [three-block Section 7](PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md#7-identification-strict-saving-and-global-consequence).
  Neither endpoint is established as sharp; no normalized global limit is proved.
- **Resolved lower-bound discriminators:** a single induced-subset chain
  envelope and one-level terminal coupling cannot improve the leading
  coefficient. Macroscopic prescribed-order excess is resolved, and the
  common-chain stability/global/minimax results supply the current lower
  improvement. See the corresponding sections of the [global-bounds ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
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
  Section 12 resolves the scalar minimax
  consequence and transfers the refined lower bound through full-feasible
  deletion. External acceptance of these proofs remains separate.
- **Continuous-only upper improvement:** a unique mixed third-block width
  minimum lies below `C_3(1/250)`, which lies below `C_3(1/1000)`. Neither
  larger width has finite recovery or geometric transfer. See the
  [mixed-width entry](../knowledge/FIXED_ORDER_THEORY.md#unique-continuous-mixed-width-minimum-of-the-third-reflection);
  these continuous costs do not replace the current global upper bound.

## Priority 1 — Independent review of signed discrepancy sharpness

Independently review Section 11.6 of
`research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md` at committed HEAD.
Audit the exact seam/interior/shifted-block radical formula, isolated
deletions and induced replacement edges, signed cancellations, one-sided
grid expansion and uniform Taylor remainder. Check the actual floor and
both parities, including the Section 11.5 family/E formula as dependencies;
reproduce the new bounded independent checker. Verify the positive limit
and its stronger-exponent/little-o consequences. Record acceptance or
precise corrections without inferring geometry or a new global coefficient.
Stop before constant optimization, new coupling methods or tour enumeration.

## Deferred direction — Determine the true leading asymptotics

Determine the true normalized liminf and limsup within
`[C_term+eta_new,C_3]`, and whether they agree. Prioritize stronger valid lower
bounds beyond the current coupled-pair corollary, which already improves
the resolved single-subset envelope. The optimized scalar consequence is
small in absolute size; Section 12 now incorporates Section 11's stronger
deletion information. Review the refined bound before choosing further
deletion estimates or additional coupled information. Scalar sharpness of
the stated envelope does not limit the broader method. The crossing and
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

Earlier dependency-review scopes remain deferred, without implying completion
or changing acceptance status. Retrieve only the relevant scope from the
[historical snapshot](../docs/archive/RESEARCH_ROADMAP_20260910.md), then its
owning ledger, proof and specifically linked dossier. This includes the
lower-bound dependencies, fixed-order classification, and the continuous
upper/recovery/full-root chain. Their detailed audit instructions are cold
history, not a second queue of current priorities. Revisit a dependency when
it materially affects the chosen task; success remains acceptance or precise
corrections within that dependency's stated scope.

The previously prioritized Section 12 review is deferred; this task does
not record its completion. Its scope remains to
audit its scalar minimum, rational cubic/integral enclosures, finite error
directions and full-feasible-deletion transfer, together with the Section 11
dependency and their bounded checkers. Neither sharpness result accepts
or revises that lower bound. The prior standalone Section 11.5 crossing
review has also not been recorded as completed; retrieve that scope through
its proof and linked dossier when auditing the current dependency.

## Deferred direction — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
