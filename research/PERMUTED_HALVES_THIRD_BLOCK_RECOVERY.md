# Deterministic finite weak recovery of the third adjacent reflection

    status=PROVED
    classification=exact finite construction / exact quantitative weak-recovery theorem
    domain=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon_b; delta=1/1000; every integer m>=2
    quantitative_error=omega_F(4/m)+omega_F(11/m)+38*||F||_infinity/m
    geometric_transfer=not applied
    proved_on=2026-09-08
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs, target and theorem

Start from repository HEAD `6f86fd1a98e9eb56cfbc78bc6444d8f816167879`.
Import the exact definitions, existence, uniqueness and rational brackets
of x_*, alpha_hat and epsilon_b from the
[boundary minimum](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md),
Sections 1 and 6, as restated in
[boundary recovery](PERMUTED_HALVES_BOUNDARY_RECOVERY.md), equations (1)-(3).
Thus x_* is the unique minimizer of that full-max E on [0,1], alpha_hat
is the unique zero of K'(alpha)+(1+alpha)*E(x_*) on [0,1/2], and
epsilon_b is the unique zero of D_b' on (0,(1+alpha_hat)/3-lambda).
Those functions, including both maxima, are unchanged. Set exactly

    alpha=alpha_hat, A=1+alpha, lambda=A*x_*, epsilon=epsilon_b,
    v=lambda+epsilon, delta=1/1000, w=v+delta, b=1-alpha,
    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    LL=(1+AL)*XL < lambda < LH=(1+AH)*XH,
    EL=43/1000 < epsilon < EH=11/250.                       (1)

No midpoint, decimal root or surrogate parameter defines this sequence.
Only exact floors of these constants are used below, including at ties.
The target is precisely mu_3 of the
[third-block continuous theorem](PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md),
equations (8)-(10). Its domain gates give 0<lambda<v<w<A/3<b<1.
For D=[0,1] x [1,2]^2 put h_alpha(t)=1+{t+alpha}, and define

    (a_1,c_1)=(0,lambda), (a_2,c_2)=(lambda,v),
    (a_3,c_3)=(v,w),
    G_j^+(t)=(t,A+t,A+a_j+c_j-t),
    G_j^-(t)=G_j^+(t) with its last two coordinates swapped,
    G_0(t)=(t,h_alpha(t),h_alpha(t)).

For every continuous real F on D, including nonsymmetric F,

    integral F dmu_3
      =(1/2)*sum_(j=1)^3 integral_(a_j)^(c_j)
           [F(G_j^+(t))+F(G_j^-(t))] dt
        +integral_w^1 F(G_0(t)) dt.                        (2)

These are three SEPARATE adjacent reflections. In particular the third
reflection is t->2*v+delta-t, while the second is t->lambda+v-t.
The shared endpoints in low and high ranges carry no mass. The source
proves that (2) is a probability coupling with uniform marginals and
local balance; no general sufficiency of those conditions is used here.

**Theorem.** For every integer m>=2, equation (3) constructs a permutation
P of the high radii {m+1,...,2m}. With its actual cyclic predecessor
P_0=P_m, define

    mu_m=(1/m)*sum_(i=1)^m delta_(i/m,P_(i-1)/m,P_i/m).

If M=||F||_infinity and omega_F(h) is the uniform max-norm modulus of
continuity of F on D, namely

    omega_F(h)=sup{|F(p)-F(p')|: p,p' in D, ||p-p'||_infinity<=h},

then, for every m>=2,

    |integral F dmu_m - integral F dmu_3|
      <=omega_F(4/m)+omega_F(11/m)+38*M/m.                  (T)

Consequently mu_m converges weakly to mu_3 along ALL integers. For an
L_F-Lipschitz test this is at most (15*L_F+38*M)/m. No Lipschitz
assumption is needed for weak convergence. If m=1 is desired, use the
same construction P_1=P_0=2; (T) holds trivially by 2*M<=38*M.
The detailed cell inventory below concerns m>=2.

## 2. Exact floors, finite domain and bijectivity

For m>=2 put

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), f=2*floor(delta*m/2)=2*floor(m/2000),
    e=q+d, z=e+f, r=m-s,
    beta=s/m, L=q/m, W=d/m, Z=f/m,
    V=L+W, U=V+Z, A_m=1+beta,
    H(j)=m+1+((j+s-1) mod m), 1<=j<=m,

    J(i)=q+2-i,       if 1<=i<=q and i is even;
         2*q+d+2-i,   if q<i<=e and i is even;
         2*e+f+2-i,   if e<i<=z and i is even;
         i,          otherwise,
    P_i=H(J(i)), 1<=i<=m, P_0=P_m.                         (3)

Mod has values 0,...,m-1. The disjoint integer blocks are (0,q],
(q,e], (e,z]; an empty interval activates no case. Each next start is
the preceding finite endpoint. In particular e is NOT independently
rounded from v*m, and z is NOT independently rounded from w*m.
The finite low slabs [0,L], [L,V], [V,U] meet at endpoints;
their high slabs meet at A_m+L and A_m+V. Boundary ranks belong only
to the preceding integer block. Formula (3) reduces exactly to the
boundary recovery when f=0.

The exact nonnegative residuals satisfy

    rho_a=alpha-beta in [0,1/m),
    rho_l=lambda-L, rho_e=epsilon-W, rho_d=delta-Z in [0,2/m),
    v-V=rho_l+rho_e, w-U=rho_l+rho_e+rho_d.                 (4)

This includes every floor tie without an irrationality assumption.
The known rational delta gives rho_d=0 whenever 2000 divides m.
The formulas are exact mathematical definitions. The finite checker
overcovers the floors allowed by (1); it does not claim to decide an
ambiguous implicit-constant floor from a decimal approximation.

The following rational gates suffice for all finite-domain and onset
claims (the checker recomputes their margins):

    0<delta<EL<EH<LL<LH, 0<AL<AH,
    AH+LH+EH+delta<1/2,
    6*LH<2<7*LL, 9*AH<1<10*AL,
    45*EH<2<47*EL.                                       (5)

Because all floors are downward,

    s+z<=m*(alpha+w)<m/2,
    r-z>=m*(1-alpha-w)>m/2>=1, hence r>=z+2.               (6)

Every reflected rank and every exit is strictly before the high wrap;
also m is outside the reflections. Monotonicity of floor gives
f<=d<=q. Thus positive blocks form an initial segment of the three.
Gates (5) give q=0 exactly for 2<=m<=6 and s=0 exactly for
2<=m<=9. Also d=0 for m<=45, d>=2 for m>=47, with both d=0
and d=2 permitted by the coarse bracket at m=46. Exactly f=0 for
m<2000, f=2 for 2000<=m<4000, and f>=4 for m>=4000.
In particular d>0 implies s,q>0 and f>0 implies s,q,d>0.

For each (a,l) in {(0,q),(q,d),(e,f)}, write l=2k. Odd ranks
are fixed and the even ranks obey

    J(a+2j)=a+2*(k+1-j), j=1,...,k.                       (7)

This reverses exactly that block's even ranks. Therefore each block
maps bijectively to itself, J is an involution of {1,...,m}, and H is
a cyclic bijection onto the high radii. Hence P is a permutation.
Every high appears once in both the current and predecessor lists.
Every low i appears once as well; the alternating order
(P_m,1,P_1,2,P_2,...,m-1,P_(m-1),m) is a permutation of 1,...,2m.
This is an order statement only, with no geometric feasibility assertion.

Lengths 0 and 2 give identity maps. For positive l congruent to 2
modulo 4 there is exactly one fixed even rank; for l divisible by 4
there is none. All odd ranks are fixed. These are single occurrences,
including when a reflection fixes its middle even rank. No parity
condition on m itself is required.

## 3. Exact predecessor and exceptional-cell inventory

For a nonempty block (a,l), put C=(2*a+l)/m and t=i/m.
Direct evaluation of (3) at the PRECEDING POSITION gives:

| Interior a+2<=i<=a+l | P_(i-1)/m | P_i/m | Count |
|---|---|---|---:|
| even i | A_m+t-1/m | A_m+C-t+2/m | l/2 |
| odd i | A_m+C-t+3/m | A_m+t | l/2-1 |

The initial odd cell a+1 of each nonempty block is excluded from
this table. Its predecessor comes from the preceding block or the
cyclic tail, not from a fictitious reflection within its own block.
Use the SET of comparison exceptions

    X_m=({1,r,r+1}
         union {q+1:q>0}
         union {e+1:d>0}
         union {z+1:f>0}) intersect {1,...,m}.             (8)

All its actual, unnormalized, ORDERED pairs are:

| Cell and condition | (P_(i-1),P_i) |
|---|---|
| 1, s=0 | (2m,m+1) |
| 1, s>0 | (m+s,m+s+1) |
| q+1, q>0 | (m+s+2,m+s+q+1) |
| e+1, d>0 | (m+s+q+2,m+s+e+1) |
| z+1, f>0 | (m+s+e+2,m+s+z+1) |
| r | (2m-1,2m) |
| r+1, s>0 | (2m,m+1) |

When d>0, q+1 is one shared first-exit/second-entry cell. When
f>0, e+1 is one shared second-exit/third-entry cell. Its predecessor
is P_e=H(q+2), NOT H(e) and NOT H(e+2). There is exactly one
atom of mass 1/m at this seam. Assigning independent exit and entry
exceptions would double count it; omitting the second exit because a
third block starts there would lose it. These distinctions persist
when f=2 is the identity; when d=2 some pair values coincide with
diagonal formulas, without changing the designated partition.

If f=0 and d>0, e=z and e+1 is only the last exit, with no ghost
third seam. If d=0, also f=0 and e=z=q; only q+1 is added when
q>0. If q=0 all three vanish, and no block seam is added at 1.
The conditional set (8) handles all shared endpoints once.

Since m is outside the reversals, the true cyclic predecessor is
P_m=H(m): m+s if s>0 and 2m if s=0. For s=0 the high jump is
the cyclic seam, and r+1=m+1 is outside the list. For s>0 the
actual high jump is at r+1. Cell r is a COMPARISON exception, not
a second jump: P_r/m=2, but h_alpha(r/m)=1+rho_a, on the lower
branch even if alpha*m is an integer. The actual pair at r stays
(2m-1,2m) because r-1>=z+1 by (6).

All other cells are ordinary diagonal, with normalized pairs

    (A_m+t-1/m,A_m+t), if i<r;
    (beta+t-1/m,beta+t), if i>r+1.                         (9)

The block interiors, exceptions and ordinary cells are disjoint and
exhaust {1,...,m}. Their complete counts are:

| Case | Block interiors | Exceptions | Ordinary |
|---|---:|---:|---:|
| 2<=m<=6 | 0 | 2 | m-2 |
| 7<=m<=9 | q-1 | 3 | m-q-2 |
| m>=10, d=0 | q-1 | 4 | m-q-3 |
| d>0, f=0 | q+d-2 | 5 | m-q-d-3 |
| f>0 | q+d+f-3 | 6 | m-q-d-f-3 |

For each active block its interior parity counts are those in the first
table, including zero odd interiors at length 2. The exceptions are
distinct in each row by (6) and the positive even lengths. The table
sums to m; nonnegativity of the ordinary count also follows from (6)
and the disjoint partition. Thus |X_m|<=6 for every m>=2.
The exceptional mass is bounded for comparison, never deleted.

For a concrete case, the strict rational brackets alone determine at
m=2000 (the exact third-block onset)

    (s,q,d,f,e,z,r)=(218,638,86,2,724,726,1782).

The second-third seam is cell 725 with pair (2858,2943), the third
exit is cell 727 with pair (2944,2945), the high jump is cell 1783
with pair (4000,2001), and the cyclic seam is cell 1 with pair
(2218,2219). These are the actual floors of (1), not a representative
choice among ambiguous floors. Although the third map has length 2
and is identity, its entry still inherits the reflected second exit.

## 4. Exact panel allocation to a rounded coupling

Let bar_mu_m be (2) with (alpha,lambda,epsilon,delta) replaced by
(beta,L,W,Z). Its slabs are [0,L], [L,V], [V,U] and [U,1].
It has three separate reflections, omitting zero-width slabs, and
diagonal h_beta after U. It is a probability measure on D even for
small m: by (6), beta+U<1/2, so every block is pre-wrap.

For each block (a,l) and j=1,...,l/2, take the two-cell panel

    I_j=[(a+2*j-2)/m,(a+2*j)/m].

Assign half of the bar_G^+ integral on I_j to even cell a+2*j,
and half of the bar_G^- integral to odd cell a+2*j-1. Each
assignment has mass 1/m. Outside the blocks, assign the bar_G_0
integral on [(i-1)/m,i/m] to cell i, also mass 1/m. These
assignments sum EXACTLY to integral F dbar_mu_m. Endpoints have
zero integral mass; no parity averaging assumption on F is made.

For an even interior cell, the panel parameter is in [t_i-2/m,t_i];
using its predecessor table gives max-coordinate error <=2/m.
For an odd interior cell it lies in [t_i-1/m,t_i+1/m], so the
reflected predecessor offset 3/m gives error <=4/m. For an ordinary
diagonal cell (9), the error is <=1/m; its panel uses one branch
of h_beta apart from null endpoints at the wrap r/m.

The remaining assignments are exactly X_m. They include each active
block's first odd cell and the last exit, with each shared seam
assigned once, and the wrap/cyclic comparison cells. Each costs at
most 2*M/m. All assigned triples and atoms lie in D. Hence

    |integral F dmu_m - integral F dbar_mu_m|
      <=omega_F(4/m)+2*M*|X_m|/m
      <=omega_F(4/m)+12*M/m.                              (10)

This is a direct integral comparison, with no additional Riemann error
and no discarded cell.

## 5. Moving all three boundaries and the wrap

Set b_m=1-beta=r/m. Compare the two couplings at the SAME t,
excluding the union

    T_m=[L,lambda] union [V,v] union [U,w] union [b,b_m].

The intervals may overlap, including when a rounded block disappears.
Only the union bound is needed. By (4),

    |T_m|<=rho_l+(rho_l+rho_e)+(rho_l+rho_e+rho_d)+rho_a
           =rho_a+3*rho_l+2*rho_e+rho_d <13/m.             (11)

Outside this set and null endpoints, t has crossed exactly the same
subset of ordered block boundaries in both measures. Their block
labels and diagonal wrap branches therefore agree even for empty
rounded blocks. Couple equal orientations within that common block.
The unreflected coordinate differs by rho_a, and the reflected
coordinate errors on blocks 1, 2, 3 respectively are

    rho_a+rho_l <3/m,
    rho_a+2*rho_l+rho_e <7/m,
    rho_a+2*rho_l+2*rho_e+rho_d <11/m.                    (12)

On a common diagonal branch the error is rho_a<1/m. The compared
triples lie in D because each reflection is used only on its own
slab. On T_m the conditional F averages differ by at most 2*M.
Consequently

    |integral F dbar_mu_m - integral F dmu_3|
      <=omega_F(11/m)+26*M/m.                             (13)

Adding (10) and (13) proves (T). Uniform continuity on compact D
makes its right side tend to zero, for every continuous test, along
all integers. No full-radius or geometric theorem is needed.

## 6. Bounded exact checker and scope

The [standalone checker](../ops/TASK-20260908__third_block_recovery/check_recovery.py)
uses only stdlib integers and Fraction (python -S), with no production,
verifier, old-checker or numerical-root imports and no output files.
Its predeclared range is m=2..512 plus m in
{1998,1999,2000,2001,2002,3998,3999,4000,4001,5999,6000,6001,8000}.
It covers EVERY floor triple allowed by the strict brackets (1),
ignoring correlations only to add cases, and computes f exactly by
integer division. The set covers third-block emptiness, exact onset,
identity, both midpoint parities and odd/even m. Closed clipped
floor-box corners also audit limiting ties, not substitute parameters.

An independent list rotation followed by three even-slot slice reversals
is compared with (3). Predecessors are read from that actual cyclic list.
Every cell, exception pair, parity/count, bijection, short block and
affine panel bound is checked. Residual and bad-interval constants are
checked on exact box corners. Negative controls reject duplicate highs,
each adjacent union-reflection, a lost/duplicated second-third seam,
an incorrect second-third predecessor preserving its marginal multiset,
and a false cyclic predecessor. Malformed inputs and exact floor ties
are checked as well. At m=1 the extension is checked separately.

These are finite exact arithmetic/engineering checks, not a finite scan
standing in for the all-m proof in Sections 2-5. They do not re-prove
the imported minima, select ambiguous exact floors, or sample test
functions to assert weak convergence. The formulas preserve the exact
constants regardless of which compatible floor occurs.

The sole stable owner is knowledge/FIXED_ORDER_THEORY.md; commands,
outputs and limitations belong to the [task evidence](../ops/TASK-20260908__third_block_recovery/EVIDENCE.md).
This task ends at finite recovery. It supplies no R_full statement,
full-root convergence, deletion, new global bound, finite-n optimality,
or optimization of the third start/width. The current global coefficient
remains C_b. Earlier proofs/dossiers, certificates, production code and
arXiv-v1 assets are unchanged. Independent external review is separate.
