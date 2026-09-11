# Internal manuscript review: global asymptotic theorem

    reviewed_on=2026-09-11
    mode=STRICT
    review_kind=bounded fresh internal mathematical manuscript review
    review_state=INTERNALLY_VALIDATED
    external_acceptance=not performed or implied

## Scope and sources

The reviewer independently compared Sections 2--4 of
[`ringmin_v2.tex`](../../paper_assets/v2/ringmin_v2.tex) with the self-contained
canonical proof
[`GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md`](../../research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md).
The relevant theorem claims are the global normalized limit, genuine-label
recovery, finite-type quantization, the balanced-word LP and arbitrary-precision
computability. This is a mathematical source review, not a PDF layout review,
a literature-priority adjudication or external acceptance.

No substantive proof gap was found in transferring the canonical argument
to these manuscript sections. The two small definition clarifications below
were incorporated and independently checked in the revised text.

## Independent reconstruction and source correspondence

| Manuscript statement | Canonical source | Review conclusion |
| --- | --- | --- |
| Pair-angle identity and both directed arcs | Section 2, equations (5)--(6) | The atan denominator, angle scale and both inequality directions agree with the exact cosine-law model. |
| Ordered line recurrence and closing lemma | Sections 1--2, equations (1)--(4) | Every pair is enforced; longest-path minimality and the unit closing gap are retained. The corrected infimum definition covers degenerate mark sets. |
| Geometric squeeze | Section 2, equation (6) | Both factors of pi and n are correct, and the geometric assertion is restricted to n>=3. |
| Genuine-label concatenation and limit | Section 3, equation (7), then equation (3) | The manuscript's q is the canonical proof's copy count k. Ceilings, the scale nq/N, actual label assignment and all-size limsup argument agree. |
| Finite-type approximation | Section 4, equations (8)--(10) | Subadditivity, zero marks, top-type join cost and the 1/k error agree. The revised manuscript explicitly displays the correct per-point normalization. |
| Balanced-word LP and both bounds | Section 5, equations (11)--(14) | The objective's 1/r and the r/k count constraints agree. The lower empirical limit and rational integer-batch upper recovery are complete. |
| Directed costs and exact checking | Section 6, equation (15) | The endpoint error is (r-1)epsilon/r. Rational endpoint LPs, rather than algebraic equality by endless interval refinement, support effective computation. |

The geometric squeeze applies to every feasible original order. The upper
recovery closes every pair arc, so it is not merely chain feasibility. In the
existence proof, labels are assigned to particular retained points and only
decreased; the construction does not assume that a limiting marginal is
recoverable. Scaling outside the original mark interval is explicitly handled
by homogeneity before returning to the genuine uniform labels.

For the LP lower bound, the number of leftover vertices is less than the
fixed word length. The sum of within-block spans is bounded by the total
span, and discarded type-count discrepancies vanish after normalization.
For the upper bound, compactness gives an optimum at a rational polytope
vertex despite the algebraic objective. A common denominator supplies exact
integer counts of each word and each type. The additional span per word is
one, hence the per-point correction is 1/r. Combining this with quantization
gives the displayed joint-limit bracket without an unproved compatibility
or continuum-to-finite transfer step.

The manuscript correctly distinguishes its effective characterization from
an elementary closed form, practical high-precision computation, optimal
microscopic structure or a finite global-optimum certificate. Its description
of SciPy candidate discovery followed by exact Fraction checking agrees with
the independently reviewed bounded implementation; see the
[earlier checker audit](../TASK-20260911__global_variational_limit/INTERNAL_REVIEW.md).
Those computations corroborate arithmetic cores and are not used as proofs
of the infinite quantifiers.

## Definition clarifications requested and verified

1. The initial closing lemma called B(a) a minimum circumference for arbitrary allowed
   marks, including multisets with fewer than two positive marks. If only
   positive circumference circles are admitted, those cases have infimum zero
   without an attained minimum. The reviewer requested an infimum definition
   or an explicit degenerate zero-circumference object. The infimum wording is sufficient
   because the proof constructs an actual circle of circumference b(a)+1.
   The same initial wording occurred in the canonical source. This correction
   has no effect on the global squeeze for the positive uniform
   arrays with n>=3. The revised manuscript and canonical source both now
   use "infimum circumference"; the reviewer inspected both changes.
2. The reviewer requested that Section 4.1 explicitly display
   `e_k=lim_q b(A_{k,q})/(kq)` and
   `e^-_k=lim_q b(A^-_{k,q})/(kq)`. The initial phrase "limiting mean spans"
   suggested the correct normalization, but the subsequent subadditivity
   argument first uses division by q. The displayed definitions make the
   factor k unambiguous and match canonical equation (8). Both explicit
   definitions are now present and were independently checked.

A further clarification makes positivity independent of the later
explicit lower-bound proof chain: the roughly n/2 marks at least 1/2 have
successive line separations at least 1/2, giving E>=1/4 and C_*>=1/(4*pi)>0.
This elementary observation is not needed for the correctness of the stated
limit and LP identities. The builder added it to the existence proof; the
reviewer rechecked the successive-selected-mark separation argument and its
limiting factor 1/4. The computation paragraph's endpoint LPs have rational
data and admit rational certificate coefficients, as required for the stated
finite checking scheme.

No unresolved correction remains within this bounded review scope.

## Verification and limitations

The reviewer read the complete canonical proof and manuscript Sections 2--4,
rederived their scale factors, recovery assignments, bin errors and LP
normalizations, and checked the described exact-computation boundary. No new
numerical experiment was needed or used to certify this manuscript
transcription. The prior independent line and LP checker runs remain recorded
in their owning dossier and were not relabeled as new runs in this review.

The review does not validate Sections 5 onward, their separate endpoint
dependency chains, bibliography metadata, rendering or publication actions.
The historical arXiv-v1 paper was not edited. This reviewer changed only this
review record for the manuscript subtask.
