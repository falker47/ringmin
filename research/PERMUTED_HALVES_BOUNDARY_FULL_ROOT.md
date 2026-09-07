# Adjacent reflected blocks: full-root transfer at the exact boundary minimum

    status=PROVED
    classification=exact fixed-order theorem and quantitative limit; separate global limsup corollary
    domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon=epsilon_b; every integer m>=2
    uniform_root_error=explicit O(1/m), m>=2048
    proved_on=2026-09-07
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs and statement

Keep precisely the definitions of x_*, alpha_hat and epsilon_b in the
[boundary recovery](PERMUTED_HALVES_BOUNDARY_RECOVERY.md), equations (1)-(3).
The [boundary-minimum theorem](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md)
proves existence and uniqueness of epsilon_b, the mixed-branch zero of
D_b', and its global minimality on [0,A/3-lambda]. Write

    alpha=alpha_hat, A=1+alpha, lambda=A*x_*, epsilon=epsilon_b,
    v=lambda+epsilon, a=A/3, b=1-alpha, B=A+lambda,
    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    LL=(1+AL)*XL < lambda < LH=(1+AH)*XH,
    EL=43/1000 < epsilon < EH=11/250.                       (1)

These are imported exact parameters. Bracket endpoints, numerical roots
and rational test points never replace them. No parameter is optimized
here. Let mu_b be exactly the two-adjacent-reflection measure of recovery
equation (4). On D=[0,1] x [1,2]^2 define

    k(t,x,y)=sqrt(t)*(sqrt(x)+sqrt(y)), c(x,y)=sqrt(x*y),
    g=max(k,c), I_b=integral g dmu_b, C_b=I_b/(4*pi).       (2)

For the recovered sigma_m=(1,P_1,...,m,P_m), we prove that its full-cell
root rho_m equals R_full(sigma_m), with a closed all-pairs placement at
rho_m for EVERY m>=2. We prove the uniform estimate

    |rho_m/(2m)^2-C_b|
      <=[1140/m+16384/(3*m^2)]/(4*pi), m>=2048.             (3)

Deleting only 2m supplies a feasible odd placement for every m>=2.
A separate lower squeeze proves R_full(sigma_m^-)/(2m-1)^2 -> C_b.
Finally we identify

    C_b=C_hat+D_b(epsilon_b)/(4*pi),
    limsup_(n->infinity) R*(n)/n^2 <= C_b < C_2.            (4)

C_hat is the exact prefix coefficient
K(alpha_hat)/(2*pi)+A^2*E(x_*)/(4*pi) from the recovery's defining
functions. C_2 retains its earlier parameters u_0=1/3, epsilon_0=1/100
from the [fixed second-block transfer](PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md).
Its full-root method is a comparison source; its separated seams and
all-chord second-block reduction are not hypotheses of this proof.

## 2. Finite domain, actual seams and all criterion hypotheses

For every m>=2 use the recovery's exact floors and map, without alteration:

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), e=q+d, r=m-s,
    H(j)=m+1+((j+s-1) mod m),
    J(i)=q+2-i             if 1<=i<=q and i even;
         2*q+d+2-i        if q<i<=e and i even;
         i                otherwise,
    P_i=H(J(i)), 1<=i<=m, P_0=P_m.                       (5)

Mod takes values 0,...,m-1. Each block reverses only its even ranks,
separately. The (start,length) pairs are (0,q) and (q,d), with even
lengths, including zero. They are disjoint in positions, so J is an involutive
bijection; H is a bijection onto {m+1,...,2m}. In particular all highs
are distinct, every low is smaller than every high, and

    2m<2(m+1), m>=2.                                    (6)

These check all order, distinctness, shell and size hypotheses of the
[arbitrary-permutation all-pairs criterion](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6. It requires neither a positive interblock gap nor monotone
highs, bounded high jumps, or agreement of chain and chord branches.

The rational gate

    1/2-AH-LH-EH=27541513/10^9>0                         (7)

gives s+e<m/2 and r-e>m/2, hence r>=e+2. Both blocks and their exits
are before the high wrap. Since epsilon<lambda, d<=q. The imported
floor gates give q=0 exactly for m=2..6, s=0 exactly for m=2..9,
d=0 for m<=45, d>=2 for m>=47, and either d=0 or d=2 at m=46.
Lengths 0 and 2 are identity reversals. Odd m is permitted in (5).

For completeness, every comparison exception has its ACTUAL ordered pair:

| Cell | Condition | (P_(i-1),P_i) |
|---|---|---|
| 1 | s=0 | (2m,m+1) |
| 1 | s>0 | (m+s,m+s+1) |
| q+1 | q>0 | (m+s+2,m+s+q+1) |
| e+1 | d>0 | (m+s+q+2,m+s+e+1) |
| r | always | (2m-1,2m) |
| r+1 | s>0 | (2m,m+1) |

When d>0, q+1 is ONE shared exit/entry cell. Its predecessor is not
m+s+q. When d=0 there is no extra second-block seam. When s=0 the
wrap occurs at cell 1 and r+1 is outside the index range. Cell r is
only a comparison exception: the discrete value P_r/m=2 meets the
lower branch of the continuum wrap. It remains in every full score.

In an active block (j,l)=(0,q) or (q,d), interior j+2<=i<=j+l has
pairs (m+s+i-1,m+s+2*j+l+2-i) for even i, and
(m+s+2*j+l+3-i,m+s+i) for odd i. The counts are l/2 and l/2-1.
The other cells have consecutive highs before r or after r+1, as in
recovery equation (11). Thus the complete counts are

| Case | Reflected interiors | Exceptions | Ordinary |
|---|---:|---:|---:|
| m=2..6 | 0 | 2 | m-2 |
| m=7..9 | q-1 | 3 | m-q-2 |
| m>=10, d=0 | q-1 | 4 | m-q-3 |
| d>0 | q+d-2 | 5 | m-q-d-3 |

They include every cell once. In particular m=2 has two distinct
high-low-high arcs, even though their chord values coincide. None of
the exceptions is discarded from geometry or from the maximum.

## 3. Exact full root and an all-pairs feasible construction

For R>0, with theta_R(h,k)=2 asin sqrt(h*k/((R+h)*(R+k))), put

    a_i=theta_R(P_(i-1),i), b_i=theta_R(i,P_i),
    c_i=theta_R(P_(i-1),P_i),
    d_i(R)=max(a_i+b_i,c_i), S_m(R)=sum_(i=1)^m d_i(R).  (8)

Each branch is continuous and strictly decreasing in R. To see strict
decrease of their maximum, select a maximizing branch at the larger R
and compare that same branch at the smaller R. Also d_i -> 2*pi as
R -> 0+, and d_i -> 0 as R -> infinity. Thus S_m has a unique positive
root rho_m at 2*pi, since m>=2.

In any fully feasible placement, the actual cell P_(i-1)->i->P_i has
gaps x_i>=a_i, y_i>=b_i and x_i+y_i>=c_i. Their disjoint union is
the cycle, so S_m(R)<=2*pi is necessary. At rho_m choose

    x_i=a_i, y_i=b_i+max(0,c_i-a_i-b_i).                  (9)

They are positive, sum to 2*pi, and have x_i+y_i=d_i. The verified
criterion proves sufficiency. Here is its path argument specialized to
these orders, retaining each of the two directed simple paths:

- High-high paths concatenate whole cells. Their lengths dominate the
  corresponding actual high chords. The shell [m+1,2m] obeys the strict
  triangle inequality for theta_R at every R>0, by (6) and the criterion's
  shell lemma. Successive contraction bounds each path by its endpoint
  chord. For m=2 each direction has one cell and its own chord bound.
- A path from a low to a high either consists of the adjacent gap, or
  after the first high contains a nonempty whole-cell high path. That
  path's bound alone exceeds the requested low-high angle by strict
  monotonicity in the first radius. Apply this separately in each direction.
- For a low-low path the first and last high either coincide, giving
  two gaps whose first alone suffices, or differ, giving a nonempty
  whole-cell high path whose endpoint radii both exceed the lows.
  The opposite direction satisfies the same exhaustive dichotomy.

The shell lemma includes both inverse-sine branches: for its variable
z<1/sqrt(2), its polynomial factor 2-2*z^2-z^3>5/8; for larger z
the angle comparison is direct. It has no large-R assumption. A path
crossing any seam uses its whole actual cell; a path ending at the seam's
low uses its actual partial gap. Multiple jumps introduce no new case.

Both separations of every pair are therefore >=theta_R and have sum
2*pi. Put phi_1=0 and form cumulative angles in sigma_m using outgoing
gaps y_i from i and x_(i+1) from P_i, with cyclic subscripts. Centers
(rho_m+j)*(cos(phi_j),sin(phi_j)) give central tangency and Cartesian
non-overlap by the cosine law. Consequently

    R_full(sigma_m)=rho_m, for every m>=2.                (10)

For R>rho_m, adding 2*pi-S_m(R) to one gap also preserves both path
lower bounds. The proof does not assert feasibility at R_chain.

## 4. Quantitative recovery of the full maximum

Use every empirical triple, including the shared seam:

    mu_m=(1/m)*sum_i delta_(i/m,P_(i-1)/m,P_i/m),
    G_m=integral g dmu_m.                                (11)

On t<=1/4, k/c=sqrt(t/x)+sqrt(t/y)<=2*sqrt(t)<=1, so g=c.
On t>=1/4 the sum of absolute first derivatives of k is at most
2*sqrt(2)+1<4; that of c is at most sqrt(2)<2. Each branch, and
their maximum, is 4-Lipschitz in the max norm there. Below 1/4 only c
is active. Split a straight segment at t=1/4, using continuity of the
max, to obtain the global bound on D, including t=0 and every tie:

    Lip_infinity(g)<=4, 1<=g<=2*sqrt(2)<3.                (12)

The recovery's all-continuous-test estimate therefore gives, for ALL m>=2,

    |G_m-I_b|<=(4*4+7*4+24*3)/m=116/m.                  (13)

In particular no derivative of sqrt(t) at zero is invoked. The maximum
is never replaced by a single branch on the second block. The at most
five exceptional atoms and the moving shared boundary are already paid
for by the recovery; there is no additional uncounted seam error.

## 5. Uniform angular approximation, compact root bracket and limit

Recheck the angular estimate of the earlier full-root argument for
ALL radii 1<=h,k<=2m. At R=4*c*m^2 with c>=c0>0, put
w=sqrt(h*k)/R and z=w/sqrt((1+h/R)*(1+k/R)). Differentiating the
inverse square-root factor along the positive segment gives

    0<=w-z<=w*(h+k)/(2*R)<=1/(4*c^2*m^2),
    z<=w<=1/(2*c*m).

For m>=1/c0, z<=1/2. On [0,1/2],
1/sqrt(1-z^2)-1<=z^2: rationalization bounds its denominator below
(3/4)*(7/4)>1. Integration gives asin(z)-z<=z^3/3. Hence

    |theta_R(h,k)-2*sqrt(h*k)/R|<=e_m(c0),
    e_m(c0)=1/(2*c0^2*m^2)+1/(12*c0^3*m^3).              (14)

The chain branch has absolute error <=2*e_m and the chord <=e_m.
Since the scalar max is 1-Lipschitz in its two arguments,

    |d_i(4*c*m^2)-g(i/m,P_(i-1)/m,P_i/m)/(2*c*m)|<=2*e_m,
    |S_m(4*c*m^2)-G_m/(2*c)|<=E_m(c0),
    E_m(c0)=1/(c0^2*m)+1/(6*c0^3*m^2).                   (15)

This is uniform at every cell, for every permutation and c>=c0;
finite and continuum branch choices may disagree. At c0=1/32,
(13)-(15) imply

    |S_m(4*c*m^2)-I_b/(2*c)|
      <=2880/m+16384/(3*m^2), c>=1/32, m>=32.            (16)

Before evaluating any estimate at an unknown root, set c1=1/2 and
m>=2048. Write E_m=1024/m+16384/(3*m^2)<1. From 1<=G_m<3,

    S_m(4*c0*m^2)>=16-E_m>15>2*pi,
    S_m(4*c1*m^2)<3+E_m<4<2*pi,                         (17)

using 3<pi<22/7. Thus c_m=rho_m/(2m)^2 lies in (1/32,1/2).
At c_m, (15), multiplied by c_m/(2*pi), gives

    |c_m-G_m/(4*pi)|<=E_m/(4*pi).

Combining with (13) proves (3), along all integers m, with no floor
subsequence. The constants and cutoff are sufficient, not optimized.
For smaller m, the exact root and feasibility result (10) still applies.

## 6. Mixed second block and exact identification of C_b

The rational gates LH+EH<(1+AL)/3 and (1+AH)/3<1-AH imply
v<a<b. Thus the removed diagonal on the second block is strictly
chord, but its reflected replacement is mixed. Indeed, in coordinates
t=lambda+s, X=B+s, Y=B+epsilon-s, its ratio is

    V(s)=sqrt((lambda+s)/(B+s))
         +sqrt((lambda+s)/(B+epsilon-s)).

Both summands strictly increase in s. By the boundary theorem,
epsilon>tau_b, so V(0)<1<V(epsilon); also V(epsilon/2)<1.
There is a unique z_b in (epsilon/2,epsilon) with V(z_b)=1.
There are positive-length chord AND chain intervals. The old gate
min(X,Y)>4*t for the whole reflected block would contradict this
strict endpoint sign and cannot be imported.

For the prefix let z_1 in (0,lambda) be the unique solution
sqrt(z_1/(A+z_1))+sqrt(z_1/(A+lambda-z_1))=1. Its endpoint
sign follows already from sqrt(XL/(1+XL))+sqrt(XL)>1, with positive
pre-square residual. The diagonal pre-wrap tail switches at a;
the wrapped tail is chain because 3*b>alpha, following from 4*AH<3.
The complete integral is therefore

    I_b=integral_0^z_1 sqrt((A+t)*(A+lambda-t)) dt
       +integral_z_1^lambda sqrt(t)*(sqrt(A+t)+sqrt(A+lambda-t)) dt
       +integral_0^z_b sqrt((B+s)*(B+epsilon-s)) ds
       +integral_z_b^epsilon sqrt(lambda+s)*(sqrt(B+s)+sqrt(B+epsilon-s)) ds
       +integral_v^a (A+t) dt
       +2*integral_a^b sqrt(t*(A+t)) dt
       +2*integral_b^1 sqrt(t*(alpha+t)) dt.               (18)

The two reflections meet only at a zero-mass endpoint; there is no
diagonal interval between them. The two switch ties and high-wrap endpoint
values have zero measure. Finite seam or switch cells must always use
(8), even if their limiting position lies in a strict continuum branch.

Subtracting the unchanged prefix and tail from the baseline integral
4*pi*C_hat leaves EXACTLY the full-max slab replacement that defines
D_b(epsilon_b). This proves C_b=C_hat+D_b(epsilon_b)/(4*pi), with
D_b as defined in the boundary theorem, including its chain integral.

## 7. Strict comparison with the old C_2 using exact gates

Put u_0=1/3 and epsilon_0=1/100, solely to compare with the old family.
The rational positive margins

    u_0-LH=42554539/3000000000>0,
    (1+AL)/3-u_0-epsilon_0=793/30000>0,
    (1+AL)/3-LH-EH=19854539/3000000000>0                 (19)

place (u_0,epsilon_0) in the OPEN start-domain Omega and place both
epsilon_0 and epsilon_b inside the boundary width domain. In particular
the entire same-width segment lambda<=u<=u_0 lies within that domain.
The [start-domain theorem](PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md)
therefore gives

    D(u_0,epsilon_0)-D_b(epsilon_0)
      >=epsilon_0^3/48 *
        [1/(A+lambda+epsilon_0)-1/(A+u_0+epsilon_0)]
      >gamma,
    gamma=epsilon_0^3*(u_0-LH)/[48*(1+AH+u_0+epsilon_0)^2]>0. (20)

The last strict inequality also follows by bounding the integrated
derivative's denominator from above and the segment length from below.
All these are rational gates on imported enclosing intervals.
The boundary-minimum theorem gives D_b(epsilon_b)<=D_b(epsilon_0).
(In fact it is strict, since epsilon_0<EL<epsilon_b.) The old coefficient
has exactly C_2=C_hat+D(u_0,epsilon_0)/(4*pi), by its full-cost theorem.
Consequently

    gamma=42554539/303864862158400000,
    C_2-C_b>gamma/(4*pi)>7*gamma/88
           =297881773/26740107869939200000>0.             (21)

This comparison uses the boundary and start theorems, with their hypotheses
checked, and no difference of decimal costs or quadrature sign. It does
not require a new enclosure of epsilon_b or optimization of another width.

## 8. Odd n: deletion upper bound and separate necessary-cell squeeze

Let sigma_m^- be sigma_m with just 2m removed and set
rho_m^-=R_full(sigma_m^-). Deleting that circle from (9) preserves
all remaining tangencies and pair constraints. The two incident gaps
merge into their positive sum. Thus for EVERY m>=2,

    rho_m^-<=rho_m.                                     (22)

This statement alone is an upper bound and does not prove an odd
fixed-order limit. The odd cycle has adjacent lows at the deletion and
does not satisfy the alternating criterion's hypotheses.

By r>=e+2, the unique high 2m is P_r, including r=m when s=0.
Let j=1+(r mod m), the next low index. Only cells r and j contain 2m.
Every other original triple survives consecutively in the odd order;
its two gaps are disjoint from those of other retained triples. There
are m-2 retained cells, 2m-4 counted gaps and exactly three uncounted
odd gaps. Therefore every feasible odd placement at R must obey

    T_m(R)=sum_(i not in {r,j}) d_i(R)<=2*pi.              (23)

For m>=4 this decreasing continuous score has a unique positive root
tau_m: its zero-radius limit is 2*pi*(m-2)>2*pi. Necessity and deletion
give tau_m<=rho_m^-<=rho_m. No sufficiency of (23) is asserted.

For c>=1/32 and m>=32, (12) and (14) bound the two omitted cells:

    0<=S_m(4*c*m^2)-T_m(4*c*m^2)<=B_m,
    B_m=96/m+2048/m^2+32768/(3*m^3).                     (24)

Indeed each cell is <=3/(2*c*m)+2*e_m(1/32). For m>=2048,
E_m<1 and B_m<1, so T_m at c0 is >=16-E_m-B_m>14>2*pi,
and T_m at c1 is <=S_m<4<2*pi. This separately brackets
t_m=tau_m/(2m)^2 in (1/32,1/2) before evaluating the errors there.
Equations (13), (15), (24) now give

    |t_m-C_b|<=H_m,
    H_m=[116/m+E_m+B_m]/(4*pi).                          (25)

The even endpoint has the smaller error (3); squeezing shows
|rho_m^-/(2m)^2-C_b|<=H_m. With f_m=(2m/(2m-1))^2 and
1<=I_b<3 we also have the explicit odd estimate

    |rho_m^-/(2m-1)^2-C_b|
      <=f_m*H_m+(f_m-1)*3/(4*pi), m>=2048.               (26)

Both terms tend to zero. The small m=2,3 need no tau_m; deletion (22)
already supplies their feasible odd constructions. This proves the
fixed-order limit for both parities without equating finite odd/even roots.

## 9. Global consequence, verification and ownership

The actual placements give R*(2m)<=rho_m and R*(2m-1)<=rho_m.
Using the even limit and f_m -> 1 proves the global limsup in (4);
this corollary only needs the deletion upper bound. The stronger odd
fixed-order limit has its own proof in Section 8. Combining with (21)
gives the requested strict improvement C_b<C_2.

The [exact bounded checker](../ops/TASK-20260907__boundary_full_root/check_full_root.py)
audits rational gates, actual seams and deletion incidence, both branches
with sign-safe algebra, independent arctangent angle enclosures and uniform
constants. The earlier recovery, boundary and start-domain checkers are
rerun separately. The
[numerical diagnostics](../ops/TASK-20260907__boundary_full_root/diagnose_full_root.py)
use the full maximum, alternate angular formula, both directed paths,
Cartesian distances and an independent all-pairs difference-constraint
solver for small even and odd orders. Their roots and quadratures are
numerical observations, not exact definitions or certificates.

The analytic proof supplies all-m quantifiers. The fixed-order ledger
alone owns (3), (10), (21), (26) and the definition of C_b. The global
ledger alone owns the R*(n) corollary, referring to that coefficient.
Exact commands, bounded ranges, output, independence and limitations are
in the [STRICT evidence](../ops/TASK-20260907__boundary_full_root/EVIDENCE.md).
No global optimality, sharp coefficient, global normalized limit, finite
improvement cutoff or floating-circle assertion follows. Prior proofs,
arXiv-v1 assets, finite certificates and production code retain their scope.
