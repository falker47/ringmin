# Deterministic weak recovery of the adjacent-block boundary optimizer

    status=PROVED
    classification=exact finite construction / exact quantitative weak-recovery theorem
    domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; u=lambda; epsilon=epsilon_b; every integer m>=2
    quantitative_error=omega_F(4/m)+omega_F(7/m)+24*||F||_infinity/m
    full_root_transfer=not applied
    proved_on=2026-09-06
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs and the target measure

The input baseline is the user-accepted commit
`7b43946dffa40b96a72b15924ea987fbcd9d3b9d`. Import the existence,
uniqueness and strict rational brackets from the
[normalized prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
[alpha minimum theorem](PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md),
and [boundary minimum theorem](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md).
For specificity, their exact definitions are

    E(x)=integral_0^x [
      max(sqrt((1+t)*(1+x-t)),
          sqrt(t)*(sqrt(1+t)+sqrt(1+x-t)))
      -max(1+t,2*sqrt(t*(1+t)))] dt,
    x_* = the unique global minimizer of E on [0,1],
    h_alpha(t)=1+{t+alpha},
    K(alpha)=integral_0^1 max(sqrt(t*h_alpha(t)),h_alpha(t)/2) dt,
    alpha_hat = the unique zero of K'(alpha)+(1+alpha)*E(x_*)
                on [0,1/2].                                      (1)

Fix alpha=alpha_hat, A=1+alpha, lambda=A*x_*, u=lambda,
B=A+lambda, h=A/3-lambda and b=1-alpha. Define exactly

    D_b(epsilon)=integral_0^epsilon [
      max(sqrt((B+s)*(B+epsilon-s)),
          sqrt(lambda+s)*(sqrt(B+s)+sqrt(B+epsilon-s)))
      -max(B+s,2*sqrt((lambda+s)*(B+s)))] ds,
    epsilon_b = the unique zero of D_b' in (0,h),
    epsilon=epsilon_b, v=lambda+epsilon.                          (2)

The boundary theorem proves that this zero exists, is in the strict
mixed branch, and is the unique minimum on [0,h]. Thus (2) is an
unambiguous exact definition, retaining both maxima; no decimal, rounded
root, bracket midpoint or rational surrogate defines a parameter here.
Its optimality is within that specified continuous family only.

The imported brackets and their products are

    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    LL=(1+AL)*XL < lambda < LH=(1+AH)*XH,
    EL=43/1000 < epsilon < EH=11/250,
    0<epsilon<h, 0<lambda<v<A/3<b.                               (3)

Let D=[0,1] x [1,2]^2. For every continuous, possibly nonsymmetric,
real-valued F on D put

    G_1^+(t)=(t,A+t,A+lambda-t),
    G_2^+(t)=(t,A+t,A+2*lambda+epsilon-t),
    G_j^-(t)=G_j^+(t) with its last two coordinates swapped,
    G_0(t)=(t,h_alpha(t),h_alpha(t)).

The desired probability measure mu_b is exactly

    integral F dmu_b
      = (1/2)*integral_0^lambda [F(G_1^+)+F(G_1^-)] dt
        +(1/2)*integral_lambda^v [F(G_2^+)+F(G_2^-)] dt
        +integral_v^1 F(G_0) dt.                                (4)

The low blocks [0,lambda] and [lambda,v] are adjacent, as are the
high ranges [A,A+lambda] and [A+lambda,A+v]. They have two separate
reflections, not reflection of their union. Endpoint assignments have
zero mass. Each reflected coordinate preserves Lebesgue measure on its
own high interval. Together with the diagonal intervals [A+v,2] and
the wrapped [1,A], this gives each high marginal uniform on [1,2]. The
low marginal is uniform on [0,1]; conditional swap symmetry is explicit.

**Recovery theorem.** For every integer m>=2, (5) below is a genuine
permutation of {m+1,...,2m}. With its actual cyclic predecessor P_0=P_m,

    mu_m=(1/m)*sum_(i=1)^m delta_(i/m,P_(i-1)/m,P_i/m)
      -> mu_b weakly along all integers m -> infinity.

For M=||F||_infinity define the uniform max-norm modulus on D by

    omega_F(delta)=sup{|F(z)-F(z')| : z,z' in D, ||z-z'||_infinity<=delta}.

The stronger bound, valid for EVERY m>=2, is

    |integral F dmu_m - integral F dmu_b|
      <=omega_F(4/m)+omega_F(7/m)+24*M/m
      <=2*omega_F(7/m)+24*M/m.

Sections 2-5 prove these statements without a geometric transfer.

## 2. Floors, parity and bijectivity with a shared finite endpoint

For every integer m>=2 define

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), e=q+d, r=m-s,
    beta=s/m, L=q/m, W=d/m, V=e/m, A_m=1+beta,
    H(j)=m+1+((j+s-1) mod m), 1<=j<=m,

    J(i)=q+2-i,       if 1<=i<=q and i is even;
         2*q+d+2-i,   if q<i<=e and i is even;
         i,          otherwise,
    P_i=H(J(i)), 1<=i<=m, P_0=P_m.                              (5)

Mod takes values 0,...,m-1. A block of length zero has no active case.
The second block starts at q itself, not at a separately rounded start
strictly to its right. No positive intervening gap is present or needed.
The [older fixed second-block recovery](PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md)
is a reference for the parity reversal only; none of its separation
inequalities, exceptional-cell counts or weak estimates is imported.

Write the exact nonnegative floor residuals as

    delta_alpha=alpha-beta, delta_lambda=lambda-L,
    delta_epsilon=epsilon-W,
    0<=delta_alpha<1/m,
    0<=delta_lambda,delta_epsilon<2/m,
    v-V=delta_lambda+delta_epsilon,
    (2*lambda+epsilon)-(2*L+W)=2*delta_lambda+delta_epsilon.
                                                                  (6)

These hold also at integer ties. No irrationality assumption, floor
decision from decimal digits, or restriction to a subsequence is used.
The formulas are mathematical definitions at the exact constants; the
bounded checker below overcovers floor choices rather than computing
the implicitly defined constants to decide them.

Only the following elementary rational gates are used for the finite
domain and the small-case classification:

    0<AL<AH, 0<EL<EH<LL<LH,
    AH+LH+EH<1/2,
    6*LH<2<7*LL, 9*AH<1<10*AL,
    45*EH<2<47*EL.                                               (7)

In particular b-v>1/2. Thus

    s+e< m/2, r-e>=m*(b-v)>m/2>=1, hence r>=e+2.                (8)

Both finite blocks and their exits are strictly before the high wrap.
The two reflected high ranges themselves stay below 2m. Since
epsilon<lambda, d<=q, so d>0 implies q>0. Gates (7) give q=0
exactly for 2<=m<=6, and s=0 exactly for 2<=m<=9. Also d=0 for
m<=45, d>=2 for m>=47, and d is either 0 or 2 at m=46.
No refinement of epsilon_b is required to select an onset for the proof:
its exact floor specifies it, and both m=46 alternatives are covered.
In particular d>0 always implies s>0 and q>0.

For a block with even start a and even length l=2k, where (a,l)
is (0,q) or (q,d), its odd positions are fixed and

    J(a+2j)=a+2*(k+1-j), j=1,...,k.                            (9)

These are its even ranks in reverse order, each once. The two rank
intervals are disjoint even though their endpoints are adjacent.
Each maps to itself, and the complement is fixed. Therefore J is a
bijection and J(J(i))=i; H is a cyclic shift and a bijection onto the
high radii. Every high radius appears once in P and once in its
cyclic predecessor list. All low radii i=1,...,m appear once as well.

Lengths 0 and 2 give identity block maps. For positive l congruent to
2 modulo 4 there is exactly one fixed even rank at the reflection
midpoint; for l divisible by 4 there is none. All odd ranks stay fixed
in either case. These are single occurrences, not duplicates. This
argument handles both odd and even m; only q and d must be even.

## 3. Every actual predecessor, seam and exceptional cell

For a nonempty block (a,l)=(0,q) or (q,d), write t=i/m and
C=(2*a+l)/m. For its interior a+2<=i<=a+l, direct evaluation of
the preceding POSITION in (5) gives

| Interior cells | P_(i-1)/m | P_i/m | Count |
|---|---|---|---:|
| even i | A_m+t-1/m | A_m+C-t+2/m | l/2 |
| odd i | A_m+C-t+3/m | A_m+t | l/2-1 |

The orientation alternation is not an independent pairing prescription.
In particular the second block begins at the odd position q+1, whose
predecessor belongs to the first block and is handled separately.

Use the SET of exceptional comparison cells

    X_m=({1,r,r+1}
         union {q+1 : q>0}
         union {e+1 : d>0}) intersect {1,...,m}.                 (10)

All their actual unnormalized ordered pairs are

| Cell and condition | (P_(i-1),P_i) |
|---|---|
| i=1, s=0 | (2m,m+1) |
| i=1, s>0 | (m+s,m+s+1) |
| i=q+1, q>0 | (m+s+2,m+s+q+1) |
| i=e+1, d>0 | (m+s+q+2,m+s+e+1) |
| i=r | (2m-1,2m) |
| i=r+1, s>0 | (2m,m+1) |

When d>0, q+1 is BOTH the first-block exit and second-block entry.
There is one cell with one pair and mass 1/m. Replacing its predecessor
by m+s+q, as for an isolated diagonal entry, is wrong when q>2.
When d=0 there is just the prefix exit, with no ghost second seam.
When q=0, also d=0; no prefix exit is added at i=1.

The true cyclic predecessor at i=1 is P_m=H(m): (8) leaves m
outside both reversals. For s=0 the high wrap coincides with this
cyclic seam and r+1=m+1 is outside the range. For s>0 the actual
high jump is at r+1. The cell r is an additional COMPARISON exception:
P_r/m=2, whereas h_alpha(r/m)=1+delta_alpha is on the lower branch,
also when alpha*m is an integer. It is not a second high jump.

By (8), neither block interior nor block seam meets r or r+1. Every
remaining cell is ordinary diagonal, with normalized pair

    (A_m+t-1/m,A_m+t), if i<r;
    (beta+t-1/m,beta+t), if i>r+1.                           (11)

These tables partition ALL m cells. The complete counts are

| Case | Block interiors | Exceptional | Ordinary |
|---|---:|---:|---:|
| 2<=m<=6: s=q=d=0 | 0 | 2 | m-2 |
| 7<=m<=9: s=d=0, q>0 | q-1 | 3 | m-q-2 |
| m>=10, d=0: s,q>0 | q-1 | 4 | m-q-3 |
| d>0: s,q>0 | q+d-2 | 5 | m-q-d-3 |

In each row the sum is m, and the ordinary count is nonnegative by
the disjoint partition. The table includes m=2 (only the two exceptions),
the first q=2 blocks (zero odd interior count), both d=0 and d=2 at
m=46, and every later length-2 or midpoint case. Identity blocks may
have ordinary-looking seam pairs; retaining their designated cells in
X_m is intentional. No atom is discarded: |X_m|/m<=5/m is only the
mass on which approximation will use a crude bound.

For example, the coarse rational brackets alone give at m=100

    (s,q,d,e,r)=(10,30,4,34,90),
    (J(31),...,J(34))=(31,34,33,32),
    (P_31,...,P_34)=(141,144,143,142).

The shared seam at 31 is (112,141), the second exit at 35 is
(142,145), the high wrap at 91 is (200,101), and the cyclic seam
at 1 is (110,111). No optimization or geometric assertion is attached
to this example.

## 4. Direct panel comparison with the rounded coupling

Define bar_mu_m by (4) with (alpha,lambda,epsilon) replaced by
(beta,L,W), retaining TWO adjacent reflections and the diagonal
h_beta(t)=1+{t+beta} on [V,1]. This is a probability measure on D
even when either block is empty: 1+beta+V<2 by (8). Denote its
affine triple maps by bar_G_j^+/- and bar_G_0.

There is an exact allocation of its integral to the m finite cells.
In a block (a,l), for j=1,...,l/2 use the panel

    I_j=[(a+2*j-2)/m,(a+2*j)/m].

Assign (1/2)*integral_(I_j) F(bar_G^+) to its even cell a+2*j,
and (1/2)*integral_(I_j) F(bar_G^-) to its odd cell a+2*j-1.
Each assignment has total mass 1/m. Assign integral_((i-1)/m)^(i/m)
F(bar_G_0) to every cell outside the blocks, again mass 1/m.
These assignments sum EXACTLY to integral F dbar_mu_m; orientations
need not give equal values for a nonsymmetric F.

For an even interior cell, comparison with every t in its panel
has max-coordinate error <=2/m: t lies between t_i-2/m and t_i,
and the two high offsets in the interior table are -1/m and 2/m.
For an odd interior cell the panel has t between t_i-1/m and
t_i+1/m; the reflected-coordinate offset is 3/m, so the error is
<=4/m. This accounts for the shifted predecessor, not only the
current high. For an ordinary diagonal cell (11), the error on
its unit panel is <=1/m. That panel is on one branch of h_beta
apart from irrelevant endpoints, since its wrap is exactly r/m.

The remaining assignments are precisely the cells X_m and cost at
most 2*M/m each. This includes the initial odd cell of each active
block, the shared seam once, the exits, and both wrap comparison
cells. It follows for every m>=2 that

    |integral F dmu_m - integral F dbar_mu_m|
      <=omega_F(4/m)+2*M*|X_m|/m
      <=omega_F(4/m)+10*M/m.                               (12)

No extra Riemann error or omitted endpoint atom is concealed here:
the panel allocation is exact and all m atoms are scored.

## 5. Moving the shared endpoint and both remaining boundaries

Set b_m=1-beta=r/m. To compare bar_mu_m with the true mu_b at
the SAME t, set aside the union of intervals

    T_m=[L,lambda] union [V,v] union [b,b_m].

By (6), its Lebesgue measure satisfies

    |T_m|<=delta_lambda+(delta_lambda+delta_epsilon)+delta_alpha
           <7/m.                                           (13)

The intervals may overlap: in particular V may lie below lambda
for small m. A union bound, rather than an ordering or positive-gap
assumption, is all that is used. Outside this union (up to null
endpoints) the two measures use the same block or diagonal slab,
and the diagonal wrap branches agree. Couple equal orientations
at each such t. On the first block, coordinate errors are bounded
by delta_alpha+delta_lambda<3/m. On the second block the largest
error is

    delta_alpha+2*delta_lambda+delta_epsilon<7/m,             (14)

coming from the reflected coordinate. On the diagonal it is
delta_alpha<1/m. All compared triples are in D because each
uses its own valid slab. There is no extension of a reflection
outside its domain. On T_m the difference of conditional F
averages is bounded by 2*M. Therefore

    |integral F dbar_mu_m - integral F dmu_b|
      <=omega_F(7/m)+14*M/m.                               (15)

Combining (12) and (15) proves the announced bound. Uniform
continuity on compact D gives weak convergence along all integers.
For an L_F-Lipschitz test the bound is (11*L_F+24*M)/m; no
Lipschitz hypothesis is required. For the smallest m the bound
may be crude but is still valid (the trivial bound is 2*M).

The first block, the second block, their shared endpoint, the tail
and high wrap have thus been recovered simultaneously. Since both
finite high-coordinate marginals are the exact uniform high grid,
there is also no missing marginal mass at any finite m.

## 6. Bounded exact checker, authority and scope

The [standalone checker](../ops/TASK-20260906__boundary_recovery/check_recovery.py)
uses integers and Fraction only, with no production, verifier, prior
checker or numerical-root imports. Its fixed range is m=2..512.
It covers every floor triple compatible with the strict rational
alpha/lambda/epsilon brackets, including both choices when a bracket
crosses an integer floor boundary. Ignoring their correlations only
adds cases. Closed clipped boxes also audit limiting floor ties.

It checks the elementary gates (7), compares the formula with a
separate rotation and even-slot list reversal, and reads predecessors
directly from that list. Every cell, parity count, shared seam, high
wrap, bijection, identity block, and panel-coordinate bound is checked.
Affine residual bounds are checked on exact box corners. Deliberate
duplicate, union-reflection, false shared-seam and cyclic-predecessor
mutations must be rejected. This is a bounded bookkeeping audit of
one construction, not enumeration or optimization of high permutations.

The proof in Sections 2-5 supplies the all-m statement. The checker
does not certify the input minima, decide their exact floors by
approximation, or prove weak convergence by finite sampling. No
new root enclosure, refined epsilon bracket, quadrature, moment
mesh or numerical diagnostic is needed; predecessor numerical
diagnostics remain separate and are not used as evidence here.

The sole stable owner is knowledge/FIXED_ORDER_THEORY.md; commands,
outputs and limitations are in the [task evidence](../ops/TASK-20260906__boundary_recovery/EVIDENCE.md).
The task ends with weak recovery. In particular it supplies no
full-root transfer, new R_full or R*(n) statement, finite-m optimality,
or general coupling optimality. The earlier fixed-width geometric
results retain their parameters. Prior proofs, production code,
certificates and the historical arXiv-v1 assets are unchanged.
