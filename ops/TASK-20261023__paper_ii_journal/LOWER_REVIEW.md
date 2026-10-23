# Fresh Internal Review of the Reused Lower Supplement

## Outcome and Scope

**No substantive mathematical gap was identified in this targeted analytic
review.** The reused S1 proof supports the lower-endpoint statement and
proof outline in `paper_assets/paper_ii_journal/main.tex`, Proposition 7
(label `prop:lower`), with the scope and qualifications below.

This is a fresh internal critical reading on 2026-10-23 by the agent that
authored S2, not S1 or the main manuscript. It is independent of S1's
writing and of the prior internal-review conclusion. It is not external
scientific acceptance, a formal proof-assistant verification, or a new
research result. The review did not use a prior PASS as a proof premise.

The complete unchanged S1 source was read: L1 through L8, the rational
arithmetic exposition, and the included global-limit existence proof.
The review also read the candidate's lower section, `certificate.json`,
and the parameter/target-checking portion of S1 `verify.py` to establish
what the reported interval means. No checker or numerical experiment was
rerun in this review. Existing execution results remain separate evidence.

## Reviewed Identities

| File | SHA-256 at Review |
|---|---|
| `paper_assets/asymptotic_sequel/proposition7_supplement/supplement.tex` | `ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4` |
| `paper_assets/paper_ii_journal/main.tex` | `2e74ed7ca0385523d98d8573ce0a0b20b3fbe51a6e9c8adda29550b70df69b06` |
| `paper_assets/asymptotic_sequel/proposition7_supplement/certificate.json` | `d8cf058a5d31a2651e603e14b907b09445b2cf563b9142a71d20e47517a1de46` |
| `paper_assets/asymptotic_sequel/proposition7_supplement/verify.py` | `c98cb1978701c50c546f3061c0f4f246a157794bf2e22259904525c032eaa1f7` |

Only this review record was written. S1, its PDF, certificate, checkers,
manifest and all journal-package files were left unchanged by this review.

## Analytic Assessment

### L1: Chain Bounds Are Used in the Correct Direction

The two angular kernel forms and the sandwich
`S/pi - n <= R_chain <= S/pi` use only bounds valid for every positive R;
there is no assumed quadratic scale. Both directed arcs are required by
the geometric model. Deletion begins with a full feasible placement and
keeps original radii, so each surviving adjacent gap satisfies the pair
constraint and the induced chain root is at most the original R. The
argument never promotes a chain-feasible order to full feasibility.
At least three surviving radii are explicitly required, including when
an order's closing edge is counted.

### L2: The Terminal Parameter Is Exact and Sufficiently Isolated

`cos(tau)=tau` has a unique root in (0,1) by strict decrease. The change
of variables for the terminal integral, the derivative of its normalized
form, and the identification `J=pi*C_term` are consistent. The terminal
optimization is over that one integral, not over finite tours. Its
identity is all that L3-L8 require; there is no missing finite Supnick
optimality premise.

The rational root gates preserve the directions of the alternating
cosine/sine sums, the decreasing map from sine to q, and Machin's identity.
The latter includes an angle-branch argument. The stated q bounds supply
the finite-grid gate `alpha=floor(q*n)/n>1/6` for n>=102.

### L3: One Order and One Correctly Normalized Energy

The dual potential has equality on the reflection assignment. The
integrated derivative denominator lies in [4 alpha,4], so both signs of
`y-(s-x)` give the displayed quadratic lower and upper bounds. Degree two
and the reflection's exact permutation of the inclusive grid identify
its potential sum with J_n. Consequently `e=W0-J_n>=0` and `E<=8e`
apply to each genuine outer cyclic order.

The measure gives each oriented edge mass `1/(2n)` and reflects only the
second endpoint. Both marginals are exactly the same inclusive grid
measure; its mass `(n-k+1)/n` is deliberately not normalized to one.
This makes the energy equal to the original undirected sum and permits
exact primitive cancellation. The assignment reference may contain a
fixed point or two-cycles, but it is never asserted to be a realizable
cycle. The three restrictions retain the same original sigma, mu and E;
there is no substitution of independently optimized orders.

### L4: The Constants 43, 11 and 54 Include Runs and the Seam

The proof partitions deleted vertices into maximal cyclic runs after
rotating to a survivor. This accounts for the closing seam and all removed
and inserted edges. For isolated deletions the displayed Hessian bounds
imply an operator norm at most six and a Taylor error at most three times
the two squared defects. No incident edge is shared by two isolated
vertices, because adjacent deleted vertices would form a longer run.

For longer runs, `V_bad<=2*M_LL`; the cost discrepancy and the removed
first variation are bounded separately by `8*M_LL/n` and `2*M_LL/n`.
Every LL edge has defect magnitude greater than 1/2 under the cutoff
gate, giving `M_LL/n<=4E`. Together with the isolated contribution this
produces `3E+40E=43E` without dropping either incidence of an LL edge.
The run cost change bound uses a difference of nonnegative edge sums;
it does not incorrectly add their separate maxima.

For cancellation, |p|<1 and |p'|<11 hold on the full grid interval.
The continuous primitive of the cut-off p has a jump in its derivative,
not in its value. The smooth error is quadratic, the crossing error is
linear, and equal marginals remove the primitive exactly. Multiplication
by two yields `11E+2K`; adding the earlier bound gives `54E+2K`.
The midpoint cutoff excludes grid points on the discontinuity.

The floor bounds `5/n` and `19/(2n)` include the inclusive endpoint of
J_n and the lower-endpoint, parameter and upper-cutoff changes in D_n.
Their signs are used safely through a lower bound and the one-Lipschitz
positive-part map. The necessary gate `floor(beta*n)/n>q` is explicit.

### L5-L6: Crossings Spend the Shared Energy Once

The midpoint strip bound `nu(|x-B|<=h)<=4h` includes small h: below
`1/(2n)` the strip is empty, and above it the grid count supplies the
bound without an unrecorded O(1/n) remainder.

For multiple strictly crossed cutoffs, separation implies that the sum
of their widths is less than the point-pair distance. Each of those
crossings is therefore long, and their combined weighted contribution
is at most the single squared distance. A single long crossing has the
same bound; short crossings are paid by the strip masses. Thus
`sum h_i K_i <= 4 sum h_i^3 + E` spends the common E once, including a
pair crossing all three cutoffs. Equality at the short/long boundary and
cutoff endpoint conventions are covered.

The finite minimax retains W0 as well as the weighted mean of the inner
costs. Substituting `E<=8e` into the common bound yields
`L=8(54H+2)=16+432H`. The two scalar branches meet at `e=F_n/L` when
F_n>0; when F_n<=0 their infimum on e>=0 is zero. The scalar infimum is
not claimed realizable by a tour. Uniformity in the order permits the
finite minimum over sigma and the root sandwich. Taking the original
geometric infimum requires no attainment assumption. All cardinality
parities remain covered.

### L7: The KKT Identity Is a Global Certificate

The cubic expansion for N and the identity `G'=N''L=48(z-a-b)L<0`
are consistent on [0,a]. Opposite rational endpoint signs isolate the
unique root. At that root, `G=0` gives the required gradient relation
`g2=g1+g3`. Positive multipliers and positive coordinates of u are
explicit finite rational gates, not inferred from a numerical optimizer.

The exact cubic remainder is strictly negative whenever any coordinate
of h differs from u, since h_i>=0 and u_i>0. The linear normal terms
are nonpositive everywhere in the closed feasible polyhedron. This
establishes a global unique maximizer, including every face, vertex and
zero-width point; the argument does not presume the optimum lies on the
chosen two-active-constraint edge. The positive-part objective is handled
separately when F(h)<=0, using F(u)>0.

### L8: Boundary Widths Are Reached Only After the Size Limit

At each fixed positive strictly separated width vector, the finite
threshold pays both rounding loss and the cutoff gates for all later
integers n. At the optimizer u, the proof uses `h=t*u` for fixed
0<t<1. Its strict margins are `(1-t)a` and `(1-t)b`, and the given
N(t) suffices because b>a, beta1-q>a and 1/a>102.

The order is first n->infinity with t fixed, then t->1. The same
liminf is bounded for every t and M_n,4 itself does not depend on h.
No minimization/limit interchange or unjustified eventual separation
at u is used. The explicit sequence n=50000*j+1 correctly gives both
floor separations as their macroscopic values times `(n-1)/n`, explaining
why unchanged u fails both finite gates infinitely often.

### Included Existence Proof Uses Actual Labels and All Sizes

The longest-path placement on a fixed line order satisfies every earlier
pair constraint and is componentwise minimal. Minimization over finitely
many orders gives attainment. Deletion, decreasing marks and homogeneous
scaling preserve feasibility. Closing with one unit gap pays the
complementary directed arc for every pair, which yields the line/circle
sandwich and then the global geometric squeeze.

For arbitrary N, concatenation uses k=ceil(N/n) copies and unit joins.
After retaining the N smallest marks, their sorted values are
`ceil(i/k)/n`. Scaling by nk/N makes each at least i/N, so decreasing
marks assigns each actual label once and preserves all constraints.
Temporary marks greater than one are explicitly allowed at this line
stage. The normalized bound tends to `(b_n+1)/n` for every fixed n;
a subsequence attaining the liminf then forces convergence. This is an
all-N construction, not recovery only on a divisibility subsequence or
from marginal information alone.

## Endpoint Meaning and Consistency with Proposition 7

The interval
`0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392`
encloses the specified lower-bound coefficient. Its right endpoint is
**not** an upper bound for C*. The theorem separately says
`C* >= C_term+eta_width`. Main Proposition 7 keeps these quantities
separate and matches S1's exact parameters, three cutoffs, width region,
cubic objective, denominator, unique maximizing vector and ordered limit.
The statement C*>1/8 follows from this lower endpoint and invalidates the
stated v1 coefficient/deficit conjectures without claiming a sharp value.

The arithmetic exposition preserves interval direction in the binomial
integral tail, the q-parameter error, and division by positive pi and L.
Independent interval boxes may widen the enclosure but do not invalidate
it. The certificate explicitly declares closed internal enclosures and a
strict target interval. Reading `verify.py` confirms it compares computed
lower-coefficient bounds against the two literal target rationals, checks
positive KKT gates and signs, rejects optimized Python execution, and
returns certificate content for an equality check. This review did not
rerun that implementation or independently recompute its large fractions.

## Residual Limits and Handoff

The analytic closure is sufficient within the reviewed scope; no requested
mathematical correction or new proof dependency was found. Universal
quantifiers are supplied by the written estimates, not by the bounded
fixtures or their historical passing output. Exact endpoint numerics still
rely on the specified finite rational computations and their separately
recorded execution. This targeted review is not an exhaustive independent
implementation audit, new certificate replay, typography review, or
assessment of the whole package's hosted CI state.

Exactly one next atomic review action: assess the final committed journal
candidate and its immutable evidence as a complete package, without
interpreting this component review as external acceptance or advancing the
Review State Registry.
