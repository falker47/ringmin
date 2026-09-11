# Three-block reflected construction: uniform full-feasibility transfer

    status=PROVED
    classification=exact fixed-order theorem; uniform quantitative limits; global limsup corollary
    domain=every real 0<=Delta<=h=A/3-v; every integer m>=2
    fixed_inputs=alpha_hat; x_*; lambda=(1+alpha_hat)*x_*; epsilon_b
    proved_on=2026-09-11
    published_snapshot=arXiv v1 unchanged

## 1. Statement and the geometric discriminator

Keep the exact inputs and definitions of the
[continuous width theorem](PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md), Sections
1-3, and [mixed-width theorem](PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md),
Sections 1-6. Write

    alpha=alpha_hat, A=1+alpha, lambda=A*x_*, epsilon=epsilon_b,
    v=lambda+epsilon, a=A/3, b=1-alpha, h=a-v,
    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    EL=43/1000 < epsilon < EH=11/250.                     (1)

These are exact implicitly defined parameters, not decimal replacements.
For every Delta in [0,h], put w=v+Delta and define mu_Delta on
D=[0,1] x [1,2]^2 by the three separate reflected slabs
(a_j,c_j)=(0,lambda),(lambda,v),(v,w):

    G_j^+(t)=(t,A+t,A+a_j+c_j-t),
    G_j^-(t)=(t,A+a_j+c_j-t,A+t),
    G_0(t)=(t,1+{t+alpha},1+{t+alpha}),
    integral F dmu_Delta
      =(1/2)*sum_j integral_(a_j)^(c_j) [F(G_j^+)+F(G_j^-)] dt
         +integral_w^1 F(G_0(t)) dt,
    g(t,X,Y)=max(sqrt(t)*(sqrt(X)+sqrt(Y)),sqrt(X*Y)),
    I(Delta)=integral g dmu_Delta, C_3(Delta)=I(Delta)/(4*pi). (2)

At Delta=0 the third integral vanishes and mu_0=mu_b. The continuous
sources prove the required marginals and domain through h; the zero-width
extension is immediate. Endpoint assignments have zero mass. Unqualified
C_3 in older notes still means C_3(1/1000).

**Uniform transfer theorem.** The deterministic orders sigma_(m,Delta)
defined in (6) are permutations for every integer m>=2 and EVERY real
Delta in [0,h]. Their unique full-cell roots rho_(m,Delta) are exactly
R_full(sigma_(m,Delta)) and admit all-pairs-feasible placements. For every
continuous, possibly nonsymmetric F on D, writing omega_F for its uniform
max-norm modulus of continuity and M_F=||F||_infinity,

    sup_(0<=Delta<=h) |integral F dmu_(m,Delta)-integral F dmu_Delta|
      <=omega_F(4/m)+omega_F(11/m)+38*M_F/m, m>=2,       (3)
    sup_(0<=Delta<=h) |rho_(m,Delta)/(2m)^2-C_3(Delta)|
      <=[1198/m+16384/(3*m^2)]/(4*pi), m>=2048.          (4)

Deleting only 2m defines odd orders sigma_(m,Delta)^-. Their actual
fixed-order full minima satisfy the uniform quantitative bound (15),
and converge after normalization to C_3(Delta). The quantitative cutoff
is sufficient, not minimal; even full feasibility and odd deletion
feasibility hold at every m>=2. The alternating-cell theorem excludes
m=1 because its two neighboring highs would be the same circle.

The exact geometric criterion is the full-cell inequality (11), using
the ACTUAL cyclic high neighbors in the shell [m+1,2m]. Its sufficiency
comes from the shell triangle inequality and high/low separation. It has
no chord-dominance or width hypothesis. The width-dependent work is to
recover (2), with finitely many genuine seams and vanishing error.
In particular the former gate A-3*v-4*Delta>0 controls a branch formula,
not full feasibility. The theorem covers the entire previously studied
continuous interval, including the mixed minimum Delta_*; it does not
claim [0,h] is the maximal possible transfer domain.

## 2. Uniform floor gates and every actual seam

The directed bounds in (1) give

    0 < h_L=(1+AL)*(1/3-XH)-EH=1986317/300000000 < h
      < h_H=(1+AH)*(1/3-XL)-EL=1933111/250000000 < EL,
    EL-h_H=8816889/250000000>0,
    1/2-alpha-(v+Delta) >= 1/2-alpha-A/3
      > 1/2-AH-(1+AH)/3=523/25000>0.                    (5)

Thus 0<=Delta<=h<epsilon<lambda, w<=a<b, and all reflected highs lie
in [1,2]. This uniform half-wrap margin is independent of the full-max
branch. It remains strict at Delta=h. Also h_L-1/250>0; the imported
mixed theorem gives 1/250<tau_3<Delta_*<27/4000<h.

For each m>=2 set, with all floors interpreted exactly,

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), f=2*floor(Delta*m/2),
    e=q+d, z=e+f, r=m-s,
    H(j)=m+1+((j+s-1) mod m),
    J(i)=q+2-i,       if i<=q and i is even;
         2*q+d+2-i,   if q<i<=e and i is even;
         2*e+f+2-i,   if e<i<=z and i is even;
         i,          otherwise,
    P_i=H(J(i)), P_0=P_m,
    sigma_(m,Delta)=(1,P_1,2,P_2,...,m,P_m).             (6)

Starts are sums of rounded lengths, never independently rounded
endpoints. Floor monotonicity gives 0<=f<=d<=q; all lengths and starts
are even. Downward rounding and (5) give

    s+z <= m*(alpha+w)<m/2,
    r-z>m/2>=1, hence r>=z+2.                            (7)

Every block and exit lies before the wrap; m is outside the reversals,
P_r=2m and P_m=H(m). Each even-length block (a_0,a_0+l] reverses just
its even ranks by J(a_0+2j)=a_0+2*(l/2+1-j). The three disjoint
involutions and cyclic bijection H prove the permutation assertion.
No numerical decision of a floor of an implicit constant is a premise.

At Delta=0, f=0 for every m. For Delta>0 the exact cases are f=0 iff
m*Delta<2, f=2 iff 2<=m*Delta<4, and f>=4 iff m*Delta>=4.
More generally f=2k iff 2k<=m*Delta<2k+2, including ties at the left
endpoint. Lengths 0 and 2 are identity reversals; a positive length
2 modulo 4 has one fixed even rank, while a length 0 modulo 4 has none.
Both parities of m are allowed. The unchanged strict bounds
6*lambda<2<7*lambda and 9*alpha<1<10*alpha give q=0 precisely at
m=2..6 and s=0 precisely at m=2..9. Also d=0 at m<=45 and d>=2 at
m>=47; either coarse-bracket possibility at m=46 is harmless. Thus
positive blocks form an initial segment; d>0 implies s,q>0.

For each nonempty (a_0,l) in {(0,q),(q,d),(e,f)}, interior cells
a_0+2<=i<=a_0+l have ordered pairs

    even i: (m+s+i-1,m+s+2*a_0+l+2-i), count l/2;
    odd i:  (m+s+2*a_0+l+3-i,m+s+i),   count l/2-1.       (8)

The set of comparison exceptions is
X_m=({1,r,r+1} union {q+1:q>0} union {e+1:d>0}
union {z+1:f>0}) intersect {1,...,m}. Actual pairs are:

| Cell | Condition | (P_(i-1),P_i) |
|---|---|---|
| 1 | s=0 | (2m,m+1) |
| 1 | s>0 | (m+s,m+s+1) |
| q+1 | q>0 | (m+s+2,m+s+q+1) |
| e+1 | d>0 | (m+s+q+2,m+s+e+1) |
| z+1 | f>0 | (m+s+e+2,m+s+z+1) |
| r | always | (2m-1,2m) |
| r+1 | s>0 | (2m,m+1) |

In particular e+1 is ONE shared exit/entry cell and P_e=H(q+2),
including when f=2. At f=0 there is no extra z+1 exception. At s=0
the cyclic seam is the wrap, and r+1 is outside the list. Ordinary
pairs are (m+s+i-1,m+s+i) before r and (s+i-1,s+i) after r+1.
The disjoint (interior,exception,ordinary) counts are

    q=0:          (0,2,m-2);
    q>0,s=0:      (q-1,3,m-q-2);
    s>0,d=0:      (q-1,4,m-q-3);
    d>0,f=0:      (q+d-2,5,m-q-d-3);
    f>0:          (q+d+f-3,6,m-q-d-f-3).

They follow from (7)-(8), are nonnegative, and sum to m. No exception
is discarded from the empirical measure or geometric score. This is
the old seam inventory with its width-dependent hypotheses now proved
uniformly, rather than assumed from the case Delta=1/250.

## 3. Uniform recovery of the full cost, across the mixed switch

Let mu_(m,Delta)=(1/m)*sum_i delta_(i/m,P_(i-1)/m,P_i/m).
Put beta=s/m, L=q/m, W=d/m, Z=f/m, V=L+W and U=V+Z.
All residuals alpha-beta, lambda-L, epsilon-W and Delta-Z are
nonnegative and respectively <1/m,<2/m,<2/m,<2/m, uniformly in Delta.
Let bar_mu_(m,Delta) be (2) with these four rounded parameters.
Gate (7) puts it on the same compact D, even if some slabs vanish.

For a block (a_0,a_0+l], assign half of the plus integral on
[(a_0+2j-2)/m,(a_0+2j)/m] to its even cell a_0+2j, and half of
the minus integral to its odd cell a_0+2j-1. Each assignment has mass
1/m. Ordinary cells receive the diagonal unit panel. From (8), the
coordinate errors are at most 2/m for even interiors, 4/m for odd
interiors and 1/m for ordinary cells. At most six exceptional assignments
each cost 2*M_F/m. Hence the empirical-to-rounded error is at most
omega_F(4/m)+12*M_F/m, without a symmetry assumption on F.

The rounded-to-target bad set is

    [L,lambda] union [V,v] union [U,w] union [b,1-beta].

Its length is <13/m by the four residual bounds, even when intervals
overlap or a rounded block vanishes. Off it, block labels and orientations
agree. Reflected-coordinate errors are <3/m,<7/m,<11/m on blocks
1,2,3, respectively, and diagonal errors are <1/m. The bad set costs
at most 26*M_F/m. Adding errors proves (3). This repeats the exact panel
argument of [recovery Sections 4-5](PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md#4-exact-panel-allocation-to-a-rounded-coupling)
under the now uniform gates; it requires neither w<a strictly nor
A-3*v-4*Delta>0.

On all D, 1<=g<=2*sqrt(2)<3 and g is 4-Lipschitz in max norm.
Indeed below t=1/4 the chord dominates. Above t=1/4 the sums of absolute
partial derivatives are bounded by 2*sqrt(2)+1<4 for the chain and
sqrt(2)<2 for the chord. Their maximum is Lipschitz; split a segment
at t=1/4 to cover t=0 as well. Thus, uniformly in Delta,

    G_(m,Delta)=(1/m)*sum_i g(i/m,P_(i-1)/m,P_i/m),
    |G_(m,Delta)-I(Delta)|<=174/m.                        (9)

Every maximum is retained, including all seams, the mixed second block,
and the third block's mixed region. Finite and continuum branches may
disagree or tie; no branch-identification estimate is used.

For completeness this is uniform also for varying widths. If Delta and
Delta' are in [0,h], their common third slab changes one high coordinate
by |Delta-Delta'| and their extra slab has that length. Therefore

    |integral F dmu_Delta-integral F dmu_Delta'|
      <=omega_F(|Delta-Delta'|)+2*M_F*|Delta-Delta'|,
    |C_3(Delta)-C_3(Delta')|<=10*|Delta-Delta'|/(4*pi).    (10)

Consequently any prescribed sequence Delta_m in [0,h] tending to Delta
recovers mu_Delta and the normalized radii tend to C_3(Delta). The
radius bound is (4) plus the second term in (10); no rate of width
convergence is assumed and no new width is optimized.

## 4. The exact all-pairs criterion has no width threshold here

Use the angular kernel theta_R(u,v)=2*asin(sqrt(u*v/((R+u)*(R+v))))
and the actual P of (6). For R>0 set

    a_i=theta_R(P_(i-1),i), b_i=theta_R(i,P_i),
    c_i=theta_R(P_(i-1),P_i), D_i(R)=max(a_i+b_i,c_i),
    S_(m,Delta)(R)=sum_i D_i(R).
    Full feasibility <=> S_(m,Delta)(R)<=2*pi.           (11)

This is the [arbitrary-high criterion](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6. Its hypotheses are now checked for all m,Delta: m>=2,
P is a permutation of [m+1,2m], every high exceeds every low, and
2m<2(m+1). The score is strictly decreasing and continuous from
2*pi*m to zero. Thus it has a unique positive root rho_(m,Delta).

Here is the structural reason for sufficiency. In this shell the angular
kernel satisfies the triangle inequality along ANY high path, since
2*theta_R(m+1,m+1)>theta_R(2m,2m) for every R>0. At the root choose
x_i=a_i and y_i=D_i-a_i. These positive gaps close at 2*pi. Each of
the two simple paths for a high-high pair concatenates whole cells,
whose chord bounds contract to its endpoint chord. A low-high path is
its adjacent gap or contains a nonempty high path with first high larger
than its low. A low-low path either shares one high (one incident gap
already suffices) or contains a nonempty high path with both endpoints
larger than the lows. These exhaustive cases work separately in BOTH
directions, also across any number of seams and at m=2. The cosine law
then yields Cartesian non-overlap and central tangency.

Necessity follows by summing the disjoint local cell constraints of any
feasible placement. This proves R_full(sigma_(m,Delta))=rho_(m,Delta).
For a larger radius add the nonnegative closure slack to one gap.
All pair lower bounds survive. No chain-root equality is asserted.

In particular at tau_3 the continuum third cell changes its maximizing
branch. Past it, the positive chain correction is already present in
(9) and (11). It is NOT a new all-pairs constraint outside the full-cell
score. A seam contributes at most one actual cell and is handled exactly
in geometry, with O(1/m) mass only in the recovery comparison.

## 5. Uniform normalized root estimate and odd lower squeeze

The width-free angular error from
[full-root Section 5](PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md#5-uniform-angular-error-and-a-root-bracket-before-substitution)
applies to every 1<=u,v<=2m. For R=4*c*m^2, c>=c0=1/32, m>=32,

    |theta_R(u,v)-2*sqrt(u*v)/R|<=a_m,
    a_m=512/m^2+8192/(3*m^3),
    |S_(m,Delta)(4*c*m^2)-G_(m,Delta)/(2*c)|<=E_m,
    E_m=1024/m+16384/(3*m^2).                            (12)

To recall its error directions, linearizing the denominator costs at
most 1/(2*c0^2*m^2); the inverse-sine remainder costs at most
1/(12*c0^3*m^3), using asin(t)-t<=t^3/3 for t<=1/2.
The chain has twice the single-angle error; the scalar max is
1-Lipschitz in its entries. The argument does not require branch agreement.

At m>=2048, E_m<1 and 1<=G_(m,Delta)<3. At c0 the score is
>=16-E_m>15>2*pi, while at c1=1/2 it is <3+E_m<4<2*pi.
Thus rho_(m,Delta)/(2m)^2 lies in (1/32,1/2) uniformly BEFORE
substitution in (12). Multiplying the root error by c/(2*pi)<=1/(4*pi)
and using (9) proves (4).

Delete only P_r=2m and merge its incident gaps. This supplies an odd
feasible placement at rho=rho_(m,Delta); denote the actual odd minimum
by rho^-=R_full(sigma_(m,Delta)^-). Let j=1+(r mod m). For every
feasible odd placement the surviving m-2 disjoint cells imply

    T_(m,Delta)(R)=sum_(i not in {r,j}) D_i(R)<=2*pi.      (13)

They cover 2m-4 of the 2m-1 gaps, leaving exactly three, including
the merged gap r->j. For m>=4, T decreases from 2*pi*(m-2)>2*pi
to zero, giving its unique positive root tau_(m,Delta) and the separate
squeeze tau_(m,Delta)<=rho^-<=rho. For m=2,3 use only deletion
feasibility; no positive retained-score root is asserted. The odd minimum
exists by the positive adjacent-chain lower bound, the finite deletion
upper bound, and closed constraints on the compact angle simplex.

The same full-cell bound (12) controls the two removed cells:

    0<=S_(m,Delta)(4*c*m^2)-T_(m,Delta)(4*c*m^2)<=B_m,
    B_m=96/m+2048/m^2+32768/(3*m^3), c>=1/32.             (14)

At m>=2048, B_m<1. Bracket T independently by 16-E_m-B_m>14>2*pi
at c0 and T<=S<4<2*pi at c1. Substitution gives
|tau_(m,Delta)/(2m)^2-C_3(Delta)|<=H_m, where
H_m=[174/m+E_m+B_m]/(4*pi). With F_m=(2m/(2m-1))^2, the squeeze
and C_3(Delta)<3/(4*pi) prove

    sup_(0<=Delta<=h) |rho^-/(2m-1)^2-C_3(Delta)|
      <=F_m*H_m+(F_m-1)*3/(4*pi), m>=2048.              (15)

Both terms vanish uniformly. This identifies the limit of the actual
odd full minimum, not just that of a deleted feasible placement; it does
not identify the finite odd minimum with either bounding root.

## 6. Transfer of the already proved mixed minimum and scope

The full interval [0,h] is transferable. In particular the existing
mixed theorem, without any new optimization, supplies its unique
minimizer Delta_* in (tau_3,h) and

    R*(2m)<=rho_(m,Delta_*),
    R*(2m-1)<=R_full(sigma_(m,Delta_*)^-),
    limsup_(n->infinity) R*(n)/n^2 <= C_3(Delta_*),
    C_3(1/250)-C_3(Delta_*)>12389/72000000000000>0.       (16)

The last strict saving is imported from
[mixed-width Section 6](PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md#6-cost-comparison-with-the-current-widths),
not estimated from a new numerical parameter. Thus the whole previously
continuous improvement to Delta_* is geometrically realizable. There is
no unavoidable seam or all-pairs obstruction before that minimum.
Continuing the chord-only formula after tau_3 WOULD be incorrect, but
its failure is a cost-branch obstruction already resolved by the full max.

This resolves the requested structural discriminator and stops. The endpoint
h is the existing continuous cost-analysis boundary, not a proved geometric
failure threshold. No result for wider slabs, further blocks, a global
normalized limit, sharpness, global optimality, expanded finite certification
or revised arXiv-v1 claim follows. The lower endpoint is unchanged.

The new proof and its imported theorems remain subject to independent
mathematical review. The fixed-order ledger owns (3)-(15); the global ledger
owns only the new upper corollary (16). The mixed-width ledger entry retains
ownership of the continuous minimum and saving. Bounded exact arithmetic
checks target only the proposed branch-independent gates, floor transitions,
actual cells and panel errors; they do not prove an all-width or all-m
statement. Their precise discriminator, executable snippet, outputs and
limitations are in the [task evidence](../ops/TASK-20260911__third_block_uniform_transfer/EVIDENCE.md).
