# Fixed third width 1/250: integer recovery and full-root transfer

    status=PROVED
    classification=exact fixed-order theorem; quantitative even/odd limits; global limsup corollary
    domain=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon_b; Delta=1/250; every integer m>=2
    quantitative_root_gate=m>=2048
    proved_on=2026-09-11
    published_snapshot=arXiv v1 unchanged

## 1. Inputs, target and statement

Keep the EXACT alpha=alpha_hat, x=x_*, lambda=(1+alpha)*x and
epsilon=epsilon_b of the [previous full-root theorem](PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md),
Section 1, with their defining minima and imported strict brackets:

    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x < XH=2877/10000,
    LL=(1+AL)*XL < lambda < LH=(1+AH)*XH,
    EL=43/1000 < epsilon < EH=11/250.
    A=1+alpha, v=lambda+epsilon, Delta=1/250, w=v+Delta,
    b=1-alpha, B=A+v, M=B+Delta/2.                         (1)

No numerical approximation defines an input or chooses an ambiguous floor.
The target is exactly mu_3(Delta) of the
[continuous width theorem](PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md), Sections 1-3.
On D=[0,1] x [1,2]^2, let (a_j,c_j) be (0,lambda), (lambda,v),
(v,w), and put

    G_j^+(t)=(t,A+t,A+a_j+c_j-t),
    G_j^-(t)=(t,A+a_j+c_j-t,A+t),
    G_0(t)=(t,1+{t+alpha},1+{t+alpha}).
    integral F dmu_3(Delta)
      =(1/2)*sum_j integral_(a_j)^(c_j) [F(G_j^+)+F(G_j^-)] dt
        +integral_w^1 F(G_0(t)) dt.
    g(t,X,Y)=max(sqrt(t)*(sqrt(X)+sqrt(Y)),sqrt(X*Y)),
    I=integral g dmu_3(Delta), C=I/(4*pi)=C_3(1/250).      (2)

Unqualified C_3 in earlier sources continues to mean C_3(1/1000).
The continuous theorem already proves

    C_3(1/1000)-C > 1/(2304000000*pi) > 1/9216000000.     (3)

**Theorem.** The orders sigma_m in (4) have R_full(sigma_m)=rho_m,
where rho_m is their unique full-cell root, for EVERY integer m>=2.
They are all-pairs feasible at that root. Moreover

    |rho_m/(2m)^2-C| <= [1198/m+16384/(3*m^2)]/(4*pi),
                                                        m>=2048.

Deleting only 2m gives odd orders sigma_m^- with
R_full(sigma_m^-)/(2m-1)^2 -> C, with the explicit error (12).
Thus limsup R*(n)/n^2 <= C < C_3(1/1000). These are fixed-order
equalities/limits and a global upper bound, not global optimality.

## 2. New floors, gates and every actual seam

For m>=2 define

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), f=2*floor(m/500),
    e=q+d, z=e+f, r=m-s,
    H(j)=m+1+((j+s-1) mod m),
    J(i)=q+2-i,       if i<=q and i is even;
         2*q+d+2-i,   if q<i<=e and i is even;
         2*e+f+2-i,   if e<i<=z and i is even;
         i,          otherwise,
    P_i=H(J(i)), P_0=P_m,
    sigma_m=(1,P_1,2,P_2,...,m,P_m).                     (4)

The range of i is 1,...,m; mod has values 0,...,m-1. Starts e and z
are sums of the rounded lengths, not independently rounded endpoints.
The new denominator is 500 because f=2*floor(Delta*m/2).

Here are the exact gates that replace every width-dependent gate in the
old recovery/transfer:

    0<Delta<EL<EH<LL<LH,
    1/2-AH-LH-EH-Delta=23541513/1000000000>0,
    L=(1+AL)*(1-3*XH)-3*EH=1986317/100000000,
    A-3*v-4*Delta > L-4*Delta=386317/100000000>0,
    A/3-v-Delta > L/3-Delta=786317/300000000>0,
    M < 1+AH+LH+EH+Delta/2=1474458487/1000000000<3/2.     (5)

In particular s+z<m/2, r-z>m/2>=1, hence r>=z+2. The blocks
and their exits precede the wrap; P_r=2m lies outside them. Also
w<A/3<b and their continuum highs lie in [1,2]. Each even-length
block (a,a+l] reverses exactly its even ranks by
J(a+2j)=a+2*(l/2+1-j). The three disjoint reversals are involutions,
so J and H are bijections and P contains all highs exactly once.
The shell is [m+1,2m], all lows are smaller, and 2m<2(m+1).

The unchanged gates 6*LH<2<7*LL, 9*AH<1<10*AL and
45*EH<2<47*EL give q=0 exactly at m=2..6, s=0 exactly at
m=2..9, and d=0 for m<=45, d>=2 for m>=47. At m=46 both
d=0 and d=2 are covered. Floor monotonicity gives f<=d<=q.
The NEW exact onsets are f=0 at m<500, f=2 at 500<=m<1000,
and f>=4 at m>=1000. Lengths 0 and 2 are identity reversals.
Positive length 2 modulo 4 has one fixed even midpoint; length 0
modulo 4 has none. Both parities of m and all floor ties are included.

For each active (a,l) in {(0,q),(q,d),(e,f)}, interior cells
a+2<=i<=a+l have actual ORDERED pairs

    even i: (m+s+i-1, m+s+2*a+l+2-i), count l/2;
    odd i:  (m+s+2*a+l+3-i, m+s+i),   count l/2-1.

The comparison-exception set is
X_m=({1,r,r+1} union {q+1:q>0} union {e+1:d>0}
union {z+1:f>0}) intersect {1,...,m}. Its actual pairs are:

| Cell | Condition | (P_(i-1),P_i) |
|---|---|---|
| 1 | s=0 | (2m,m+1) |
| 1 | s>0 | (m+s,m+s+1) |
| q+1 | q>0 | (m+s+2,m+s+q+1) |
| e+1 | d>0 | (m+s+q+2,m+s+e+1) |
| z+1 | f>0 | (m+s+e+2,m+s+z+1) |
| r | always | (2m-1,2m) |
| r+1 | s>0 | (2m,m+1) |

Shared exit/entry e+1 is ONE cell, with predecessor P_e=H(q+2),
including when f=2. If f=0 there is no extra z+1 exception; if
s=0 the wrap is at 1, and r+1 is outside the list. For ordinary
cells the pair is (m+s+i-1,m+s+i) before r and (s+i-1,s+i)
after r+1. The disjoint (interior,exception,ordinary) counts are

    q=0:          (0,2,m-2);
    q>0,s=0:      (q-1,3,m-q-2);
    s>0,d=0:      (q-1,4,m-q-3);
    d>0,f=0:      (q+d-2,5,m-q-d-3);
    f>0:          (q+d+f-3,6,m-q-d-f-3).

They sum to m, and no actual exception is removed from the score.
At m=500 the strict brackets determine (s,q,d,f)=(54,158,20,2),
(e,z,r)=(178,180,446): seam e+1=179 has pair (714,733), exit
181 has (734,735). At m=1000 they determine
(s,q,d,f)=(109,318,42,4), (e,z,r)=(360,364,891): seam 361
has pair (1429,1470), exit 365 has (1471,1474). In both cases the
strict upper epsilon bracket excludes the next even floor.

## 3. Quantitative recovery without a branch substitution

This section audits why the proof of the
[old recovery](PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md), Sections 4-5,
survives this particular change of width. Define the actual empirical
measure mu_m=(1/m)*sum_i delta_(i/m,P_(i-1)/m,P_i/m). For a continuous
F on D, omega_F(h) is its uniform max-norm modulus of continuity, and
||F||_infinity is its supremum absolute value on D. Set beta=s/m, L_m=q/m,
W_m=d/m, Z_m=f/m, V_m=L_m+W_m, U_m=V_m+Z_m. All four
residuals alpha-beta, lambda-L_m, epsilon-W_m, Delta-Z_m are
nonnegative, respectively <1/m,<2/m,<2/m,<2/m. The last vanishes
exactly when 500 divides m. Let bar_mu_m be (2) with
(alpha,lambda,epsilon,Delta) replaced by (beta,L_m,W_m,Z_m).
Gate (5) makes it a measure on the same compact domain D.

On every block (a,a+l], the panel [(a+2j-2)/m,(a+2j)/m]
assigns half its plus integral to even cell a+2j and half its minus
integral to odd cell a+2j-1, each of mass 1/m. Ordinary cells receive
their diagonal unit panel. The actual pair table bounds coordinate
errors by 2/m for even interiors, 4/m for odd interiors and 1/m
for ordinary cells. Each of the at most six exception assignments costs
at most 2*||F||_infinity/m. Thus the empirical-to-rounded error is
at most omega_F(4/m)+12*||F||_infinity/m.

The rounded-to-target bad intervals are [L_m,lambda], [V_m,v],
[U_m,w], [b,1-beta]. Their union has length <13/m even if intervals
overlap or rounded blocks disappear. Off that union the same block and
orientation apply; reflected-coordinate errors are <3/m,<7/m,<11/m
on the three respective blocks. Diagonal error is <1/m. This gives

    |integral F dmu_m-integral F dmu_3(Delta)|
      <=omega_F(4/m)+omega_F(11/m)+38*||F||_infinity/m,   (6)

for every continuous, possibly nonsymmetric F on D and every m>=2.
This proves weak convergence along all integers. It does not substitute
probability marginals for geometry.

For the COMPLETE g in (2), 1<=g<3 and g is globally 4-Lipschitz
in max norm: below t=1/4 the chord dominates, and above that level
the absolute partial derivatives sum to <4 on each branch. Split a
segment at t=1/4 to cross the boundary. Therefore

    G_m=(1/m)*sum_i g(i/m,P_(i-1)/m,P_i/m),
    |G_m-I|<=174/m.                                     (7)

There is no all-chord assumption on finite cells or on the mixed second
block. The new continuum third slab is chord by (5), but even there
finite branch agreement is unnecessary.

## 4. Full feasibility at the exact even fixed-order root

Use theta_R(h,k)=2*asin(sqrt(h*k/((R+h)*(R+k)))) and set

    a_i=theta_R(P_(i-1),i), b_i=theta_R(i,P_i),
    c_i=theta_R(P_(i-1),P_i), d_i=max(a_i+b_i,c_i),
    S_m(R)=sum_i d_i(R), S_m(rho_m)=2*pi.                (8)

The maximum of these positive continuous strictly decreasing branches
is strictly decreasing. The score goes from 2*pi*m to zero, giving a
unique positive root. Necessity follows by summing the disjoint actual
cell constraints. At rho_m choose x_i=a_i and y_i=d_i-a_i; these
positive gaps close at 2*pi and meet every cell constraint.

Section 2 checks ALL hypotheses of the
[arbitrary-high criterion](PERMUTED_ALTERNATING_HALVES.md), Sections 1-6:
m>=2, positive R, a high permutation in [m+1,2m], and smaller lows.
For completeness, its all-pairs argument applies separately to BOTH
simple directed paths. A high-high path contracts whole actual cells;
the shell triangle inequality bounds it by its endpoint chord. A low-high
path is adjacent, or contains a whole high path with a strictly larger
first endpoint than its low. A low-low path either shares a single high
(one incident gap already suffices), or contains a nonempty whole high
path with both endpoints larger than the lows. These cases cover all
seams, both wrap directions, and m=2, where each high-high path is one
cell. No discarded or idealized seam enters this argument.

Both angular separations are at least theta_R. With radial coordinates
R+h, the cosine law gives Cartesian non-overlap and central tangency.
Hence R_full(sigma_m)=rho_m for all m>=2, with NO eventual-size gate
for feasibility. Increasing R permits adding the nonnegative closure
slack to one gap; both path lower bounds remain valid.

## 5. Uniform root convergence and the exact sufficient gate

The [previous angular error proof](PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md),
Section 5, uses only 1<=h,k<=2m, not the old width. Explicitly, for
R=4*c*m^2, c>=c0=1/32 and m>=32,

    |theta_R(h,k)-2*sqrt(h*k)/R|<=a_m,
    a_m=512/m^2+8192/(3*m^3),
    |S_m(4*c*m^2)-G_m/(2*c)|<=E_m,
    E_m=1024/m+16384/(3*m^2).                            (9)

Indeed denominator linearization costs <=1/(2*c0^2*m^2), and
asin(t)-t<=t^3/3 for t<=1/2 costs <=1/(12*c0^3*m^3).
The chain has twice the single-angle error; the chord has at most that
error, and max is 1-Lipschitz in its two entries. This retains every
finite branch even at ties or disagreement with the limiting branch.

For m>=2048, E_m<1. Since 1<=G_m<3, the score at c0 is
>=16-E_m>15>2*pi, while at c1=1/2 it is <3+E_m<4<2*pi.
Thus c_m=rho_m/(2m)^2 is in (1/32,1/2) BEFORE substituting it
in (9). Multiplication by c_m/(2*pi)<=1/(4*pi) and (7) give

    |c_m-C|<=[174/m+E_m]/(4*pi).                         (10)

This is the asserted all-integer limit. The cutoff is sufficient, not
minimal, and is unrelated to the exact onset 500 or nonidentity onset 1000.

## 6. Odd deletion and its separate necessary lower squeeze

Delete only 2m=P_r and merge its two incident gaps. The remaining
placement is full-feasible at rho_m, so rho_m^-=R_full(sigma_m^-)
is <=rho_m. Do not apply the alternating criterion to this odd order.
Let j=1+(r mod m). Exactly cells r and j contain the removed high.
The other m-2 cells remain consecutive with disjoint two-gap arcs;
they cover 2m-4 odd gaps, leaving exactly three, including r->j.
For EVERY feasible odd placement, therefore,

    T_m(R)=sum_(i not in {r,j}) d_i(R)<=2*pi.

For m>=4, T_m decreases from 2*pi*(m-2)>2*pi to zero, so its
unique root tau_m satisfies tau_m<=rho_m^-<=rho_m. Small m=2,3
need only the deletion upper bound; no positive T_m root is asserted.
The odd minimum exists: the adjacent-chain necessary radius is positive,
deletion supplies a finite upper bound, and the angle constraints are
closed on the compact angle simplex within that radius interval.

Each omitted cell is <=3/(2*c*m)+2*a_m in (9), whence

    0<=S_m(4*c*m^2)-T_m(4*c*m^2)<=B_m,
    B_m=96/m+2048/m^2+32768/(3*m^3).                     (11)

At m>=2048 both B_m<1 and E_m<1. Independently bracket the T_m
root by 16-E_m-B_m>14>2*pi at c0, and T_m<=S_m<4<2*pi
at c1. Substitution now yields
|tau_m/(2m)^2-C|<=H_m=[174/m+E_m+B_m]/(4*pi).
Combine with (10) and the squeeze. For F_m=(2m/(2m-1))^2,

    |rho_m^-/(2m-1)^2-C|
      <=F_m*H_m+(F_m-1)*3/(4*pi), m>=2048.              (12)

Both terms vanish. This proves convergence of the actual odd fixed-order
minimum, as well as of the feasible deleted construction's radius. It
does not identify the finite odd minimum with either bounding root.

## 7. Consequence, bounded checker and scope

Equation (2) identifies the recovered limit with precisely C_3(1/250).
The continuous strict comparison (3) can now be transferred to geometry:

    R*(2m)<=rho_m, R*(2m-1)<=rho_m^-,
    limsup_(n->infinity) R*(n)/n^2 <= C_3(1/250) < C_3(1/1000). (13)

Only this upper corollary is propagated to the global ledger. There is
no finite-n comparison cutoff between the two families, no new lower
bound, no optimization of Delta or other parameters, no tour enumeration,
no global normalized limit or sharpness, and no expanded certification.

The [standalone bounded checker](../ops/TASK-20260911__third_block_250_transfer/check_transfer.py)
uses only the standard library under isolated Python with site disabled.
It independently constructs highs by list rotation and even-slot reversal,
overcovers strict bracket-compatible floors, checks all actual cells,
panel corners, deletion incidence, rational gates and negative controls.
Its declared sizes cover emptiness, identity, nonidentity and both midpoint
parities. For selected sizes including 500 and 1000, float bisection
only proposes rational root brackets: integer outward-rounded square-root
and arctangent enclosures then certify both score signs. Direct both-path
checks certify all pairs at the upper rational radius, for even and deleted
odd placements. This finite evidence does not replace the all-m proof or
claim feasibility at a numerically rounded root. It imports no production
module, verifier, previous checker, result, or approximate input minimizer.

The fixed-order ledger owns this recovery and limit; the global ledger
owns only (13). Earlier proof notes retain their original width and scope.
Commands, evidence classes, limitations and source protection are in the
[task evidence](../ops/TASK-20260911__third_block_250_transfer/EVIDENCE.md).
Independent mathematical acceptance remains separate.
