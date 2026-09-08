# Three adjacent reflections: exact full-root transfer and quantitative limit

    status=PROVED
    classification=exact fixed-order theorem and quantitative limit; separate global limsup corollary
    domain=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon_b; delta=1/1000; every integer m>=2
    uniform_root_error=explicit O(1/m), m>=2048
    proved_on=2026-09-08
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs and statement

Import exactly the parameters, floors, permutation and measure mu_3 from
the [finite recovery theorem](PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md),
equations (1)-(3). In particular alpha=alpha_hat and x=x_* are the exact
minimizers defined there, lambda=(1+alpha)*x, epsilon=epsilon_b is the
exact boundary minimum, and delta=1/1000. Their definitions, existence,
uniqueness and brackets remain imported theorems. Set

    A=1+alpha, v=lambda+epsilon, w=v+delta, b=1-alpha,
    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x < XH=2877/10000,
    LL=(1+AL)*XL < lambda < LH=(1+AH)*XH,
    EL=43/1000 < epsilon < EH=11/250.                       (1)

No approximate minimizer or bracket midpoint defines a parameter. On
D=[0,1] x [1,2]^2 use the complete cost

    k(t,X,Y)=sqrt(t)*(sqrt(X)+sqrt(Y)), c(X,Y)=sqrt(X*Y),
    g=max(k,c), I_3=integral g dmu_3, C_3=I_3/(4*pi).       (2)

This is precisely C_3 of the
[continuous third-block theorem](PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md),
not a newly optimized cost. C_b keeps its definition in the
[boundary full-root comparison](PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md).

For sigma_m=(1,P_1,...,m,P_m) from the recovery, let rho_m be the root
of its full-cell score defined below. We prove

    R_full(sigma_m)=rho_m, for every integer m>=2,
    |rho_m/(2m)^2-C_3|
      <=[1198/m+16384/(3*m^2)]/(4*pi), m>=2048.             (3)

Let sigma_m^- delete only 2m. A separate necessary-cell lower squeeze
proves R_full(sigma_m^-)/(2m-1)^2 -> C_3, with the explicit bound (19).
Only after that squeeze we conclude

    limsup_(n->infinity) R*(n)/n^2 <= C_3 < C_b,
    C_b-C_3 > 1/576000000000.                              (4)

The first equality concerns a fixed order; the last line is an upper
bound, with no claim of global optimality or a global normalized limit.

## 2. Every criterion hypothesis and the actual three-block cells

Restate the exact finite construction to make the audit unambiguous:

    s=floor(alpha*m), q=2*floor(lambda*m/2),
    d=2*floor(epsilon*m/2), f=2*floor(m/2000),
    e=q+d, z=e+f, r=m-s,
    H(j)=m+1+((j+s-1) mod m),
    J(i)=q+2-i,       if 1<=i<=q and i is even;
         2*q+d+2-i,   if q<i<=e and i is even;
         2*e+f+2-i,   if e<i<=z and i is even;
         i,          otherwise,
    P_i=H(J(i)), 1<=i<=m, P_0=P_m.                         (5)

Mod has values 0,...,m-1. The three disjoint blocks have even
(start,length) pairs (0,q),(q,d),(e,f). Each reverses its even ranks
separately, fixing its odd ranks; hence J is an involutive bijection.
H is a cyclic bijection onto {m+1,...,2m}. Thus every high is distinct,
every low i is smaller than every high, and sigma_m contains exactly
1,...,2m once. The shell endpoints obey 2m<2(m+1).

Together with m>=2 and R>0, these are ALL the hypotheses of the
[arbitrary-high all-pairs criterion](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6. It requires no positive gap between blocks, monotonicity
of highs, restriction on jumps, large radius, or chain/chord agreement.
The recovery's probability-coupling properties are not being used as a
substitute for this geometric criterion.

The exact positive margin

    1/2-AH-LH-EH-delta=26541513/1000000000>0               (6)

gives s+z<m/2 and r-z>m/2>=1, hence r>=z+2. Every reflection and exit
is before the high wrap, and P_r=2m is outside all blocks. Floor
monotonicity gives f<=d<=q. Empty/short cases from the recovery are:
q=0 precisely at m=2..6; s=0 precisely at m=2..9; d=0 for m<=45,
d>=2 for m>=47, with d=0 or 2 covered at m=46. Exactly f=0 for
m<2000, f=2 for 2000<=m<4000 and f>=4 for m>=4000. Lengths 0
and 2 are identity reversals; a length congruent to 2 modulo 4 has
one fixed even midpoint. None of these creates a duplicate high.
There is no parity restriction on m.

For each nonempty block (a,l), its interior a+2<=i<=a+l has pairs
(m+s+i-1,m+s+2*a+l+2-i) for even i, and
(m+s+2*a+l+3-i,m+s+i) for odd i. Counts are l/2 and l/2-1.
The actual exceptional ordered pairs are:

| Cell | Condition | (P_(i-1),P_i) |
|---|---|---|
| 1 | s=0 | (2m,m+1) |
| 1 | s>0 | (m+s,m+s+1) |
| q+1 | q>0 | (m+s+2,m+s+q+1) |
| e+1 | d>0 | (m+s+q+2,m+s+e+1) |
| z+1 | f>0 | (m+s+e+2,m+s+z+1) |
| r | always | (2m-1,2m) |
| r+1 | s>0 | (2m,m+1) |

When d>0, q+1 is one shared first-exit/second-entry cell. When f>0,
e+1 is one shared second-exit/third-entry cell: P_e=H(q+2), not H(e)
or H(e+2). At f=0, z=e and no extra z+1 cell is added. If d=0,
also f=0; if q=0 all three blocks vanish. At s=0 the actual wrap is
cell 1, r=m and r+1 is outside the list. Cell r is a continuum
comparison exception only, and its actual high pair stays in the score.

The disjoint complete partition is:

| Case | Block interiors | Exceptions | Ordinary |
|---|---:|---:|---:|
| 2<=m<=6 | 0 | 2 | m-2 |
| 7<=m<=9 | q-1 | 3 | m-q-2 |
| m>=10, d=0 | q-1 | 4 | m-q-3 |
| d>0, f=0 | q+d-2 | 5 | m-q-d-3 |
| f>0 | q+d+f-3 | 6 | m-q-d-f-3 |

Ordinary cells have consecutive highs before r or after r+1. The
recovery proves these formulas directly from preceding positions,
including exact floor ties. At m=2000 the brackets uniquely give
(s,q,d,f,e,z,r)=(218,638,86,2,724,726,1782); the e+1 seam is
(2858,2943), even though the third reversal is identity. At m=2 the
two different cells join the same two highs in opposite directions;
both chord constraints are retained. Nothing in this partition is
discarded from geometry or from the full maximum.

## 3. Exact root, necessity and both directed paths for every pair

For R>0 put

    theta_R(h,k)=2 asin sqrt(h*k/((R+h)*(R+k))),
    a_i=theta_R(P_(i-1),i), b_i=theta_R(i,P_i),
    c_i=theta_R(P_(i-1),P_i),
    d_i(R)=max(a_i+b_i,c_i), S_m(R)=sum_(i=1)^m d_i(R).   (7)

Each branch is positive, continuous and strictly decreasing. For
R_1<R_2 select a maximizing branch at R_2; its strict decrease proves
d_i(R_1)>d_i(R_2) even if the maximizing branch changes. As R->0+,
a_i+b_i->2*pi and c_i->pi, so S_m->2*pi*m>2*pi. As R->infinity
S_m->0. There is exactly one positive rho_m with S_m(rho_m)=2*pi.

In any full placement let x_i,y_i be the gaps P_(i-1)->i->P_i.
Both directed separations for every pair must be at least its theta.
Thus x_i>=a_i, y_i>=b_i and x_i+y_i>=c_i. These cells partition all
gaps, proving necessity S_m(R)<=2*pi and R>=rho_m. At rho_m choose

    x_i=a_i, y_i=b_i+max(0,c_i-a_i-b_i).                   (8)

They are positive, sum to 2*pi and satisfy x_i+y_i=d_i. For clarity,
the criterion's full path argument specializes as follows, separately
for EACH of the two simple directed paths of every unordered pair.

- High-high paths concatenate whole actual cells. In the high shell
  [m+1,2m], theta_R satisfies the strict triangle inequality at every
  R>0. Contracting the actual high sequence therefore bounds each
  path below by its endpoint chord. For m=2 each path is one cell.
- A low-high path either is its adjacent gap, or reaches a first high
  U different from its target high V and then traverses a nonempty
  whole-cell high path. That part alone is at least theta_R(U,V),
  strictly greater than the requested theta_R(i,V) since U>i.
- A low-low path first reaches high U and last leaves high V. If U=V,
  simplicity makes it a two-gap path and its first gap alone suffices
  by U>j. Otherwise its nonempty whole-cell middle path is at least
  theta_R(U,V)>theta_R(i,j), since both highs exceed both lows.

The shell lemma has no branch omission: for u<=v<=2u put
xi=u/(R+u), eta=v/(R+v)<=2*xi/(1+xi). At xi>=1/sqrt(2),
2 asin(xi)>=pi/2>asin(eta). Below that point,
(1+xi)^2*(1-xi^2)-1=xi*(2-2*xi^2-xi^3)>0, using
2-2*xi^2-xi^3>5/8. Positivity and the angle range then give
2 asin(xi)>asin(eta), hence 2 theta_R(u,u)>theta_R(v,v).
Monotonicity in each radius gives the stated triangle inequality.

A path crossing q+1, e+1, z+1, the cyclic seam or high wrap uses its
whole actual cell; a path ending at that low uses its partial gap.
The preceding exhaustive pair cases cover multiple seams simultaneously.
Both separations are at least theta and sum to 2*pi. Cumulative angles
in sigma_m, with outgoing gaps y_i from i and x_(i+1) from P_i, give
centers (rho_m+h)*(cos(phi_h),sin(phi_h)). The cosine law proves all
Cartesian non-overlap and central tangency. This proves the first line
of (3). For larger R one may add 2*pi-S_m(R) to a single gap; one
path increases and its complement is unchanged. No chain-root or
global-optimum identification is made.

## 4. Uniform recovery for the complete maximum

Use every empirical triple, including all six possible exceptions:

    G_m=(1/m)*sum_i g(i/m,P_(i-1)/m,P_i/m).

On t<=1/4, k/c=sqrt(t/X)+sqrt(t/Y)<=2*sqrt(t)<=1, so g=c.
On t>=1/4 the sum of the absolute partial derivatives of k is at
most 2*sqrt(2)+1<4; for c it is at most sqrt(2)<2. Thus their max
is 4-Lipschitz in the max norm on that slab. Below it g=c; splitting
a straight segment at t=1/4 proves the global bound across the tie,
including t=0. Also 1<=g<=2*sqrt(2)<3. The recovery's arbitrary-test
estimate therefore gives for EVERY m>=2

    |G_m-I_3| <= [4*4+11*4+38*3]/m = 174/m.              (9)

No derivative of sqrt(t) at zero is used. This pays for all moving
boundaries, parities, seams and wrap through the recovery theorem.

## 5. Uniform angular error and a root bracket before substitution

Recheck the comparison method for ALL 1<=h,k<=2m. At R=4*c*m^2,
c>=c0>0, put u=sqrt(h*k)/R and
u'=u/sqrt((1+h/R)*(1+k/R)). Differentiating the inverse square-root
factor along the positive segment gives

    0<=u-u'<=u*(h+k)/(2*R)<=1/(4*c^2*m^2),
    0<u'<=u<=1/(2*c*m).

For m>=1/c0 this is at most 1/2. On [0,1/2], rationalization of
1/sqrt(1-t^2)-1 bounds it above by t^2: its denominator is at least
(3/4)*(7/4)>1. Integrating gives asin(t)-t<=t^3/3. Hence

    |theta_R(h,k)-2*sqrt(h*k)/R|<=a_m(c0),
    a_m(c0)=1/(2*c0^2*m^2)+1/(12*c0^3*m^3).              (10)

The chain error is <=2*a_m and the chord error <=a_m. Since the
scalar max is 1-Lipschitz in its two entries, with NO branch agreement
assumption between finite and limiting cells,

    |d_i(4*c*m^2)-g(i/m,P_(i-1)/m,P_i/m)/(2*c*m)|<=2*a_m,
    |S_m(4*c*m^2)-G_m/(2*c)|<=E_m(c0),
    E_m(c0)=1/(c0^2*m)+1/(6*c0^3*m^2).                   (11)

Set c0=1/32, c1=1/2 and

    E_m=1024/m+16384/(3*m^2).

For m>=32, (9)-(11) also give the uniform full-score comparison

    |S_m(4*c*m^2)-I_3/(2*c)|
      <=3808/m+16384/(3*m^2), c>=1/32.                   (12)

Before substituting the unknown root, take m>=2048. Then E_m<1,
and 1<=G_m<3 proves

    S_m(4*c0*m^2)>=16-E_m>15>2*pi,
    S_m(4*c1*m^2)<3+E_m<4<2*pi,                         (13)

using 3<pi<22/7. Monotonicity now places
c_m=rho_m/(2m)^2 in (1/32,1/2). Evaluate (11) there and multiply
by c_m/(2*pi)<=1/(4*pi) to obtain

    |c_m-G_m/(4*pi)|<=E_m/(4*pi).

Together with (9), this proves (3) and the quantitative limit along
all integers m, with no floor subsequence. The cutoff and constants
are sufficient, not optimized. Exact full feasibility still holds at
every smaller m>=2 by Section 3.

## 6. Odd deletion with a genuine lower squeeze

Write rho_m^-=R_full(sigma_m^-). Delete 2m from the placement (8);
merge its two positive incident gaps. All other central tangencies and
pair separations survive. Thus rho_m^-<=rho_m for every m>=2.
This is only the upper half of the squeeze; the odd order has adjacent
lows and cannot be passed to the alternating criterion.

By (6), 2m=P_r, including r=m when s=0. Set j=1+(r mod m).
Exactly the original cells r and j contain that high. All other
triples remain consecutive in the odd cycle, and their two-gap arcs
are disjoint. They count 2m-4 gaps, leaving exactly three odd gaps
uncounted, including the new low-low gap r->j. Necessity for any
feasible odd placement at R gives

    T_m(R)=sum_(i not in {r,j}) d_i(R)<=2*pi.              (14)

For m>=4, T_m is continuous, strictly decreasing, tends to
2*pi*(m-2)>2*pi at zero and to zero at infinity. Its unique positive
root tau_m is therefore a genuine lower bound:

    tau_m<=rho_m^-<=rho_m.                               (15)

No sufficiency of the retained-cell condition is claimed. These
inequalities also hold if R_full is initially defined as an infimum.
In fact the finite odd minimum is attained: it has a positive lower
bound from its adjacent-chain score (at least three vertices), a
finite feasible upper bound by deletion, and a closed angle-constraint
set on a compact angle simplex over any such positive radius interval.

For c>=1/32 and m>=32 each omitted cell is at most
3/(2*c*m)+2*a_m(1/32). Consequently

    0<=S_m(4*c*m^2)-T_m(4*c*m^2)<=B_m,
    B_m=96/m+2048/m^2+32768/(3*m^3).                     (16)

For m>=2048 both E_m<1 and B_m<1. Thus T_m at c0 is at least
16-E_m-B_m>14>2*pi, while at c1 it is <=S_m<4<2*pi. This
separately brackets t_m=tau_m/(2m)^2 in (1/32,1/2). Only now
evaluate (9), (11), (16) at t_m to get

    |t_m-C_3|<=H_m,
    H_m=[174/m+E_m+B_m]/(4*pi).                          (17)

The even endpoint in (15) has the smaller error (3). Therefore

    |rho_m^-/(2m)^2-C_3|<=H_m.                           (18)

With F_m=(2m/(2m-1))^2 and 1<=I_3<3, changing normalization gives

    |rho_m^-/(2m-1)^2-C_3|
      <=F_m*H_m+(F_m-1)*3/(4*pi), m>=2048.               (19)

Both terms vanish. For m=2,3 deletion already gives feasible odd
placements; a positive tau_m is neither needed nor asserted there.
This proves the odd fixed-order limit with its own lower squeeze,
without identifying finite odd and even roots.

## 7. Identification, strict saving and global consequence

The continuous mu_3 in (2) is exactly the recovery target: three
separate reflections on [0,lambda], [lambda,v], [v,w], followed
by the shifted diagonal. Hence no identification gap remains between
the geometric coefficient and the continuous third-block coefficient.

For completeness, the continuous theorem compares full maxima first.
On the changed third slab let t=v+s, X=B+s, Y=B+delta-s,
B=A+v and M=B+delta/2. Its accepted rational gates give

    A-3*v-4*delta>1586317/100000000>0,
    M<1472958487/1000000000<3/2.

Thus X,Y>=B>4*(v+delta)>=4*t and both new and removed full
maxima are strictly chord throughout that closed continuum slab.
Only there may the max be reduced. The unchanged prefix, mixed second
block and tails cancel with their full costs. Finite seam cells are
still evaluated by (7), regardless of continuum branch labels.
The centered identity is

    4*pi*(C_3-C_b)
      =-integral_(-delta/2)^(delta/2)
          u^2/[M+sqrt(M^2-u^2)] du
      <=-delta^3/(24*M)<-1/36000000000.                  (20)

The radicands and denominator are positive; the integral numerator
is positive except at one point. With pi<4 this yields the strict
saving in (4). This imports no all-chord claim on the second block
and requires no numerical subtraction of nearby costs.

The actual even and deleted odd placements give
R*(2m)<=rho_m and R*(2m-1)<=rho_m^-. The limits (3) and (19)
now imply (4) over both parities. No all-pairs, deletion or squeeze
obstruction remains for these exact orders. There is no new finite-n
comparison cutoff, optimization of a third parameter, sharp coefficient,
global normalized limit, expanded finite certification or floating claim.

## 8. Evidence and canonical ownership

The analytic arguments above supply the all-m quantifiers. The
[exact bounded checker](../ops/TASK-20260908__third_block_full_root/check_full_root.py)
adapts the boundary checker's method to three blocks without importing
it: bracket-compatible floor overcovers, independent list construction,
actual seams, all-cell branch signs, disjoint odd incidence and exact
arctangent enclosures. It also checks the new constants and negative
controls. This is independent of production and verify.py, but shares
analytic algebra with the proof; it is not an independent proof review.
The [numerical diagnostic](../ops/TASK-20260908__third_block_full_root/diagnose_full_root.py)
independently checks both angular paths and Cartesian distances, and
an all-pairs difference-constraint solver tests both sides of small
even full roots and the separate odd squeeze. Bracket-floor cases
are overcovered, not used to redefine implicit parameters. Threshold
third-block seams receive exact checks, without quadratic or factorial
search at those sizes. Numerical roots are observations, not certificates.

The fixed-order ledger alone owns (2), (3), (19) and the already proved
strict coefficient comparison. The global ledger alone owns the R*(n)
corollary, referring to that coefficient. Exact local commands, outputs,
provenance and limitations are in the
[STRICT evidence](../ops/TASK-20260908__third_block_full_root/EVIDENCE.md).
Earlier notes remain scoped records of their own results. No historical
paper, certificate or production code changes; external review is separate.
