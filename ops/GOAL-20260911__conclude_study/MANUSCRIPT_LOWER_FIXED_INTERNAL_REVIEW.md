# Manuscript review: explicit lower endpoint and fixed-order classification

Date: 2026-09-11. Mode: STRICT. Scope: the lower-endpoint section,
fixed-order paragraphs/table, their cross-references, related abstract and
scope statements, and the cited supplement in
`paper_assets/v2/ringmin_v2.tex`. This is a separate internal manuscript
consistency review, not external acceptance. No manuscript edits were made.

The first reviewed manuscript SHA256 was
`1a6997ad0b50037fa108bc1200390bd3c3aaadaf4d11d79aa470fe46ab712c93`.
The tracked HEAD was `13ddb41180b3911940f4fe5cf7d61c0545f9f834`.
The manuscript itself was a working draft being prepared by the parent goal.
Line numbers below identify that reviewed draft, not an immutable final PDF.

## Outcome

The mathematical statements, numerical enclosure and complete fixed-order
table agree with the separately completed dependency audits:

- `ops/GOAL-20260911__conclude_study/LOWER_INTERNAL_AUDIT.md`;
- `ops/GOAL-20260911__conclude_study/FIXED_ORDER_INTERNAL_AUDIT.md`.

No substantive theorem error was found. Three local corrections and one
wording clarification were sent to the parent immediately. The parent
implemented them, and the revised source was rechecked: **INTERNALLY
VALIDATED within this review's scope**. Their initial findings are retained
below for provenance. The publication packet citation remains a separate
packaging gate until the named packet exists.

## Initial corrections, subsequently resolved

1. **Integral differential, line 396.** The definition ends in `],dx`.
   Use the TeX thin-space command before dx, rather than a printed comma.
2. **Undefined optimizer symbols and conflicting denominator notation,
   lines 433-438.** The outline uses u, rho and `F-rho L`, but neither
   u nor rho was defined and the only previously defined L is a
   one-dimensional function L(z). Define, for example,
   `u=(a-z_*,z_*,b-z_*)`, `Q(h)=16+432 sum_i h_i`, and
   `rho=F(u)/Q(u)>0`; then refer to `F-rho Q` in the gradient/remainder
   argument. This leaves the correctly defined scalar `L(z)=Q(a-z,z,b-z)`
   and `G=N'L+432N` unchanged. Equivalent notation is acceptable, but the
   multidimensional denominator and positive rho must be defined.
3. **Explicit integer domain, line 452.** Begin the fixed-order statement
   with "For integers k>=1 and n>=k+2". The table currently communicates
   the intended cases, but the canonical cycle and root must be defined
   only on their proved domain. "Strictly increasing positive radii" in
   the preceding paragraph also matches the stated published theorem
   exactly.

Advised clarity: replace "Signed deletion at cutoff i is at most ..."
(lines 425-426) by "The absolute discrepancy between the actual deletion
cost and its reference D_(i,n) is at most ...". The proved bound is on
`|W_i-W_0-D_(i,n)|`, not on the raw deletion cost `W_i-W_0`.
The present outline can be understood correctly from the supplement,
but the intended object should be explicit in the manuscript.

The lower proof is expressly an outline, so it need not reproduce every
finite constant, midpoint measure or bridge table. It must nevertheless
define the symbols it actually uses.

The revised source fixes the differential, defines u and the separate
multidimensional denominator `mathcal L(h)`, defines `rho=F(u)/mathcal L(u)`,
uses `F-rho mathcal L` consistently, states the integer domain explicitly,
and names the absolute signed deletion discrepancy. All required corrections
are resolved. The optional adjective "strictly" was not added before
"increasing"; the existing conventional wording creates no substantive
scope error here, and the proof supplement states the precise distinct-radius
domain.

## Statement-by-statement consistency checks

| Manuscript item | Result of comparison |
| --- | --- |
| `tau` is the root of `cos(tau)=tau` in (0,1) | Correct unique defining interval; the elementary strict derivative supplies uniqueness |
| `q=(1-sin(tau))/(1+sin(tau))` and `C_term=tau(1+q)/(2pi)` | Exactly the audited cutoff and integral normalization; not the differently parameterized q in older terminal notes |
| Three cutoffs | Exact values `2091/10000`, `10907/50000`, `23/100` match the source |
| D_i integrand and endpoints | Correct mathematical expression and sign; only the differential typo needs correction |
| `F=sum h_i D_i-8 sum h_i^3` | Correct shared-strip numerator, with three coordinates |
| Width region and denominator | Exact `a=113/12500`, `b=593/50000`, nonnegative widths and both weak adjacent constraints; denominator `pi(16+432 sum h_i)` is correct |
| `eta_width=max F_+/(pi denominator)` | Correct positive-part quotient on the complete compact region; a maximum, not just a strict-domain supremum |
| `u=(a-z_*,z_*,b-z_*)`, `G=N'L+432N` | Correct stationary equation because `L'=-432`; z_* deliberately avoids the upper construction's x_* notation. Definition of u is required before the outline uses it |
| Global bound `C_*>=C_term+eta_width` | Follows from the audited liminf theorem together with the separately proved existence theorem in this draft. This manuscript review does not independently audit that existence proof |
| Directed enclosure | Both endpoints match the exact source character for character: `.14056946887766098063257` and `.14056946887766098063392`. Strictness and all digits are correct |
| Refutation of `1/8` and the stronger deficit claim | Correct: the exact lower endpoint exceeds 1/8. Historical v1 explicitly conjectured both `R*(n)~n^2/8` and `n^2/8-R*(n)=O(sqrt(n))`; this is not a back-projected claim |
| Shared-energy proof outline | Correct order of dependencies: same outer order, nested restrictions, `E<=8e`, signed discrepancy bound, one shared crossing energy, scalar minimax, uniform finite errors and full-feasible deletion |
| Width optimality outline | Correct monotone cubic/root gates and positive constraint multipliers; the exact cubic remainder proves uniqueness on the entire region, including zero coordinates/positive-part cases. Missing symbols are the only local defect |
| Fixed-t passage | Correct order: hold `0<t<1` fixed, take n to infinity, then t to one. The explicit warning that unchanged boundary widths fail finite floors infinitely often is accurate and necessary |
| Classical Supnick claim | Correct maximum-tour application to the negative anti-Monge angular matrix; "one" minimizing tour avoids an unsupported uniqueness assertion |
| Definition of the seam at the chain root | Correct endpoints n,k,n-1 and radius substitution. Add the explicit integer domain |
| Complete fixed-order table | All six rows and every endpoint match the audited theorem. Infeasibility concerns that same fixed order at its chain root, not every order or every larger radius |
| Iff criterion and outline | Correct: the seam is the minimum triangle defect; fan telescoping controls both arcs; closure forces every adjacent gap tight. The integer signs are strict, while the analytic criterion is weak `delta>=0` |
| Global/floating non-implications | Correct separation: the fixed-order classification does not determine the floating set or the global optimum after deleting selected radii |

The fixed-order paragraph would also be mathematically sound if it spelled
out that the iff refers both to the cumulative-angle placement and to
existence of any placement in that same order at the root. The present
table/context already identify that scope; the cited complete proof
explicitly establishes both formulations.

## Supplement delegation and scope

The lower citation names `research/THREE_LEVEL_COMMON_CHAIN.md` Sections
7, 9, 11-12 and the lower audit. Those files contain the exact definition,
finite minimax, weak-boundary passage, rational arithmetic and the minimal
dependency graph. The graph in turn identifies the dual-potential and
signed-deletion sections of
`research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md`. No important ingredient
of the outline is delegated to an unchecked conjecture. Both named lower
files are present at the cited mathematical checkpoint 13ddb41180b3911940f4fe5cf7d61c0545f9f834.

The fixed-order citation names `research/SUPNICK_FULL_FEASIBILITY.md`,
`research/SUPNICK_SEAM_SEQUENCES.md` and the complete internal audit.
Their linked minimal chain includes `research/FIXED_K_SUPNICK_SEAM.md`
and the initial endpoint bridges. The internal audit independently
reconstructs all twelve required bridge inequalities; the source table
does not rely on separate unreviewed k=7,...,10 or effective-cutoff proofs.
The fixed-order audit is a later goal addition and is not represented
by this bibliography item as existing at the earlier mathematical checkpoint.

The printed Supnick/survey citation agrees with the classical import
already checked during the fixed-order audit. No new external theorem is
introduced by the two manuscript sections reviewed here.

The general citation to
`ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md` was unresolved
at first inspection because the parent had not created that file yet.
That is an outstanding final packaging check, not a mathematical gap in
these sections. The final supplement must supply the cited file and a
reviewed source manifest before it is described as a complete packet.

The adjacent finite-certification paragraph, the new global-limit proof,
the linear programs, upper constructions, PDF rendering and compilation
are outside this review's assigned scope. They must rely on their own
verification, not inherit a pass from this document. In particular the
claim that a full finite verifier run passes is not independently rerun
by this manuscript review.

## Fresh verification and exact results

Local environment: PowerShell; Python 3.14.3. No source was changed and
no network request was needed for this consistency pass. The complete
earlier source audits already record their own fresh checker executions;
those executions are not falsely relabeled as rerun here.

- Scoped TeX reads and searches inspected the complete lower and fixed-order
  sections plus their abstract, scope, bibliography and original v1
  asymptotic-conjecture context.
- An inline standard-library Python check found both exact 23-place lower
  endpoints in the draft and the canonical proof and verified that all
  seven essential source/audit files exist. Exit 0, output:
  `PASS both 23-place lower endpoints exactly match source; seven minimal supplement/audit files exist`.
- Read-only `git ls-tree --name-only 13ddb41180b3911940f4fe5cf7d61c0545f9f834`
  with the two lower source/audit paths returned both paths. Thus the
  lower bibliography's checkpoint claim was checked, not assumed.
- Initial reads of the prospective v2 README, final packet and claim matrix
  reported missing files. No proof conclusion was based on those files;
  only the packet is actually cited by this draft. Their absence was
  treated as ongoing parent packaging work rather than a mathematical
  blocker.
- A second inline standard-library check on the revised manuscript verified
  all corrected definitions/phrases and confirmed the exact lower enclosure
  and all six table rows were preserved. Exit 0, output:
  `PASS revised definitions, differential, domain and discrepancy; exact lower enclosure and all six classification rows preserved`.
  The revised complete TeX SHA256 at that check was
  `39ab28b60ef73cf5999465f59c769f753a4864d59f8e5734c8c7d30d988aecb4`.

## Handoff

Mathematical consistency and the revised definitions pass within the stated
scope. No manuscript correction remains from this review. Verify final
packet availability and the rendered equations as part of the parent's
remaining publication gate. All acceptance here is internal; external
independent acceptance remains outstanding.
