# Complete global bracket certificate for n=3,...,14

## Scope and evidence status

**Classification:** computer-certified finite brackets, independently
reimplemented relative to the production solver and original generator.
The current integration adapts the supplied reviewer's implementation; running
it again is not a new independent review. Acceptance of the exact integration
commit remains separate. No paper or Review State is changed by this note.

For every integer n in {3,...,14}, in the model of outer circles of radii
1,...,n externally tangent to a central circle with pairwise disjoint interiors,
the preserved certificate supports

    L_n < R*(n) <= U_n,       U_n - L_n = 1/100000000000.

The exact rational endpoints and witnesses are in the preserved
[candidate](../reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json).
Every decimal denotes a rational input, not an exact value of R*(n).
The single complete command is

```bash
python -I -S verify_global_brackets.py
```

It imports only the Python standard library and reads the selected evidence.
It does not import or run the original generator, production solver or old
`verify.py`; no pickle, historical log, frontier, Top-K or candidate cap enters
the proof. The existing historical certificate route remains distinct.

## Model and necessary induced-cycle inequalities

**Exact identities and necessary conditions.** For central radius R>0 and
outer radii a,b>0, set q=ab/((R+a)(R+b)) and
phi_ab(R)=2 asin(sqrt(q)), using the principal branch in (0,pi).
For directed angular separation delta in [0,2*pi],

    distance^2 = (a-b)^2 + 4(R+a)(R+b) sin^2(delta/2).

Non-overlap is therefore equivalent to
phi_ab(R) <= delta <= 2*pi-phi_ab(R). The directed gaps of any cyclically
ordered subset of a feasible placement sum to 2*pi. Its edge-angle sum must
be at most 2*pi, even if some directed gap exceeds pi.

The lower proof tests the full cyclic order, the order induced by deleting 1,
and the order induced by deleting {1,2}, only when at least three vertices
remain. A strict violation of any one of these necessary conditions excludes
that full order. No sufficiency assertion or optimality of a Supnick order is
used. In the project's notation these are bounds on R_full and hence on
R*(n)=min_sigma R_full(sigma); they do not identify R_chain with R_full.

## Independent outward interval checks

**Exact arithmetic derivation.** The data use S=2^128. The verifier validates
each saved interval [lo/S,hi/S] rather than assuming its generator's accuracy.
It checks 0<q<9/10 and 0<lo<=hi<3S with width at most two grid units.
Since cos(phi)=1-2q and cos decreases on (0,3), it is enough to prove

    cos(lo/S) > 1-2q > cos(hi/S).

Use cos(x)=sum((-1)^k x^(2k)/(2k)!) on 0<=x<=4. On the internal grid
B=2^224, floor and ceiling enclose each positive term, starting with B.
For x^2=a/d the next term is obtained by multiplying by
a/[d(2k+1)(2k+2)], again rounding each bound outwards. Signed accumulation
uses the upper bound for subtraction in the lower sum and conversely.
After 112 terms, the absolute tail terms decrease: their ratios are at most
x^2/[(2N+1)(2N+2)]<1 for N=112 and decrease thereafter. The first omitted
absolute term bounds the alternating remainder with its correct sign. Early
terms need not decrease, and the implementation does not assume they do.

For the circumference, check 6S<T_-<T_+<7S and opposite strict cosine signs
at T_-/(4S), T_+/(4S). On (1.5,1.75) the unique cosine zero is pi/2
(using the elementary bounds 3<pi<4). Thus T_-/S<2*pi<T_+/S.
This check neither uses the generator's arcsin series nor its Machin formula.
All 908 pair intervals at L and U and the circumference interval are checked.

## Complete lower coverage

**Finite combinatorial proof.** For n<=9, fix the largest radius first and
retain one of each pair of reflected permutations. Distinct labels give
exactly (n-1)!/2 cyclic-order classes. Every retained order is tested for a
strict induced-cycle violation, using the lower integer edge weights w and
the upper circumference T_+.

For n>=10, delete the distinguished radius 1. Each full order determines a
skeleton on {2,...,n}, and insertion of 1 in each of the n-1 cyclic gaps
reconstructs the full orders. The gap from the last vertex to anchor n is
included. Deletion is the inverse, so the correspondence is bijective up to
rotation/reflection. At least three distinct skeleton vertices ensure that
reflection has no fixed class of oriented representatives.

The independent DP is forward. For vertices V={2,...,n-1} and anchor n,

    D[{j},j] = w[n,j]
    D[M,j] = min_{k in M\{j}} (D[M\{j},k] + w[k,j]).

Induction on |M| identifies the minimum Hamiltonian path from n through M
ending at j. The root cycle cost is min_j D[V,j]+w[j,n]. Symmetry of the
integer weight matrix is checked; path reversal then gives the exact minimum
completion cost from current j through unvisited M back to n as
D[M union {j},j]. Adding the prefix cost is a lower bound for every true
angular completion. The verifier prunes only when this sum is **strictly
greater** than T_+. Equality remains explicit.

The stack visits all remaining choices without a cap. A pruned prefix with
k unvisited vertices covers k! oriented completions. Let P count these
completions and K count retained skeletons after reflection. The verifier
checks P+2K=(n-2)!, P even, exactly K reversed leaves, exactly K(n-1)
insertions, and

    P(n-1)/2 + K(n-1) = (n-1)!/2.

Every inserted full order must have a strict induced-cycle violation; its
normalized class is checked for uniqueness. Insertions in the last gap can
produce representatives that fail the old second<last convention; normalization
still recovers the same unique cyclic-order class. The proof is the complete
partition plus valid pruning, not the factorial identity alone.

The verifier recomputes and compares **all** lower-proof fields, including
the DP stream, pruning/skeleton stream and explicit-witness digests, skeleton
vertex list, margins, counts and method. The forward DP is converted into the
original completion-state serialization only for digest comparison; the cost
calculation is independently implemented.

## Strictness for the global infimum

**Proved implication of finite margins.** Infeasibility at L alone need not
give L<R*. Here every covered order has a strict necessary angular violation.
Let m>0 be the smallest integer margin among explicit witnesses and pruning
bounds. Each covered order has a selected cycle whose true excess over 2*pi
at L is at least m/S.

For R>=L,

    |phi'_ab(R)| = sqrt(q_R/(1-q_R)) [1/(R+a)+1/(R+b)]
                <= max(1,q_L/(1-q_L)) [1/(L+a)+1/(L+b)] = d_ab.

Indeed q_R decreases and sqrt(z)<=max(1,z) for z>=0. Set
D_n=n max_ab d_ab and epsilon=m/(2 S D_n). Every relevant cycle uses at most
n edges, so its strict violation persists throughout [L,L+epsilon], with
remaining margin at least m/(2S). At smaller positive radii the angles are
larger. Thus no feasible radius lies at or below L+epsilon, and
R*(n)>=L+epsilon>L. Attainment of the infimum is not needed.
The verifier constructs this positive rational epsilon for each row and checks
epsilon<U-L. Exact buffers are recorded in its result JSON.

## Existential upper bound, including the P1 repair

**Exact rational geometric witnesses.** Each row must contain at least one
witness. Every listed order is a permutation of 1,...,n, without repeated
cyclic-order classes. Saved angular positions are checked for strict ordering
and every directed/wrap pair inequality with positive padding ceil(S/10^16).
This padding strengthens construction; it is not a negative error tolerance.

For each supplied rational stereographic parameter t_r define

    C_r=(U+r)((1-t_r^2)/(1+t_r^2), 2t_r/(1+t_r^2)).

Fraction arithmetic checks ||C_r||^2=(U+r)^2 and
||C_a-C_b||^2>(a+b)^2 for **every** outer pair. Polar order is checked by
half-planes and cross products, with anchor (1,0) and distinct directions.
The recorded minimum distance gap must equal the exact recomputed minimum.
These rational coordinates alone prove existence of a placement at U. The
angular and Cartesian witnesses need not have exactly identical angles.

Checking every member of an empty list proves no existence. A missing witness
therefore fails before numerical work, including when another row is padded
to preserve the global total 47. Exact reproduction additionally binds all
orders and their per-row cardinalities to CASES, rather than checking that
total alone. Feasibility at U does not prove those orders attain the infimum.

## Identity, provenance, tests and limitations

The default entrypoint performs both mathematical verification and pinned
input verification. It parses CASES from the preserved, hash-identified
generator through AST and a literal JSON value, without executing it. It checks
its full digest, row endpoints/orders/counts, declared script digest, the
canonical certificate digest, the original Windows file hash, equality of
Windows/candidate payloads, and the selected archive's bytes.

`--mathematical-only` performs the same complete twelve-case mathematical and
DP/pruning-metadata verification without requiring historical input or payload
identity. It explicitly reports those bindings as unchecked. This permits
rehashed falsification tests to reach actual arithmetic and geometry checks.
Historical execution timestamps, platform claims, regression PASS labels,
CASES frontier-blob provenance and source execution authenticity are not
verified in either mode. A declared source hash is not execution attestation.

The [tests](../tests/test_global_brackets.py) cover the saved false n=4 brackets
(including 47 redistributed witnesses), the false one-grid-unit angular
endpoint with recomputed lower evidence, collapsed directions, malformed
schema/coverage, altered DP/pruning digests, and input binding. Exact small
path enumeration checks every populated forward DP state, with symmetric and
asymmetric matrices. Direct full-cycle set enumeration checks pruning and all
insertion gaps. In-memory `>=` and omitted-final-gap mutants must fail those
oracles. An exact Fraction cosine series checks both parity cutoffs of the
fixed-point kernel. Tests complement the proof and full certificate command;
they do not prove correctness on all possible inputs.

The [STRICT review](../reproducibility/global_brackets/originals/STRICT_REVIEW_IT.md)
and original reviewer programs/reports are immutable historical evidence. The
original proof's pending-Windows wording is historical: the already received
Windows JSON is verified here; no new generator replay was run. This adapted
implementation shares the reviewer's algorithms, so its new local run is
reproduction of that implementation lineage, not another independent design.

No exact decimal optimum, classification of all minimizing orders, universal
floating/contact claim, n>14 result, historical float64 pruning validation,
proof-assistant verification or journal-readiness is asserted. The fixed-order
seam theorem remains a separate question. See the
[integration dossier](../ops/TASK-20260919__global_bracket_verifier/EVIDENCE.md)
for actual local commands and the boundary to exact-SHA hosted CI and external
review.
