# Fixed second reflected block: full-root transfer and deletion

```text
status=PROVED
classification=exact fixed-order feasibility and limit theorem / separate global limsup corollary
domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; second block [1/3,103/300]; integers m>=2
uniform_root_error=explicit O(1/m), m>=2048
proved_on=2026-09-06
published_snapshot=arXiv v1 unchanged
```

## 1. Fixed inputs and the three conclusions

Keep exactly the implicit constants of the
[joint-prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md)
and the permutations of the
[second-block recovery theorem](PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md):

```text
alpha=alpha_hat, A=1+alpha, lambda=A*x_*, b=1-alpha, a=A/3,
u=1/3, epsilon=1/100, v=103/300,
AL=1093/10000 < alpha < AH=10931/100000,
XL=719/2500 < x_* < XH=2877/10000,
LL=(1+AL)*XL < lambda < LH=(1+AH)*XH.                 (1)
```

Neither a decimal minimizer nor a new block choice is used. The two
accepted one-variable minimization results remain imported inputs. Let
mu_2 be the precise recovered measure in the recovery note, equation (2),
and retain its full cost on D=[0,1] x [1,2]^2:

```text
g(t,x,y)=max(k(t,x,y),c(x,y)),
k(t,x,y)=sqrt(t)*(sqrt(x)+sqrt(y)), c(x,y)=sqrt(x*y),
I_2=integral g dmu_2.                                (2)
```

We establish, separately:

1. Every prescribed even order has an all-pairs feasible placement at
   its exact full root, for every m>=2 (Section 3).
2. Its normalized full root converges to C_2=I_2/(4*pi), with the
   explicit bound (15). Section 7 identifies this coefficient exactly.
3. Deleting radius 2m gives a feasible odd construction. A separate
   necessary-cell lower bound proves its fixed-order limit too; deletion
   alone would give only an upper bound (Section 8).

Only after these steps do we deduce the global limsup in Section 9.
Weak recovery is an input about empirical measures, never inferred from
geometric feasibility or merely from balanced marginals.

## 2. The finite order and every actual cyclic cell

For every m>=2, set

```text
s=floor(alpha*m), q=2*floor(lambda*m/2), r=m-s,
p=2*floor(m/6), d=2*floor(m/200), e=p+d,
H(j)=m+1+((j+s-1) mod m), 1<=j<=m,
J(i)=q+2-i                  if i<=q and i even,
     2*p+d+2-i              if p<i<=e and i even,
     i                      otherwise,
P_i=H(J(i)), P_0=P_m,
sigma_m=(1,P_1,2,P_2,...,m,P_m).                      (3)
```

The recovery proof establishes, with exact floor conventions, that J is
an involution of {1,...,m}: the two disjoint sets of even ranks are
reversed separately, and every other rank is fixed. H is bijective.
Thus sigma_m contains each radius 1,...,2m exactly once, with increasing
lows L_i=i and distinct cyclic neighbors P_(i-1),P_i in [m+1,2m].
In particular the shell endpoints obey 2m<2(m+1), and every high exceeds
every low. These are precisely the hypotheses of the arbitrary-high-
permutation [all-pairs criterion](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6; it assumes no high monotonicity or single-wrap structure.

For clarity, here is the entire actual pair partition used in the full
score. In a reflected block of start j and even length l, where
(j,l)=(0,q) or (p,d), its interior j+2<=i<=j+l has

| Cell | P_(i-1) | P_i |
|---|---|---|
| even i | m+s+i-1 | m+s+2*j+l+2-i |
| odd i | m+s+2*j+l+3-i | m+s+i |

There are l/2 even and l/2-1 odd interior cells when l>0, and none
when l=0. Each formula is obtained from consecutive entries of (3).
The exceptional comparison set is

```text
X_m=({1,r,r+1} union {q+1:q>0} union {p+1,e+1:d>0})
    intersect {1,...,m}.                              (4)
```

| Cell and condition | Actual ordered pair (P_(i-1),P_i) |
|---|---|
| 1, s=0 | (2m,m+1) |
| 1, s>0 | (m+s,m+s+1) |
| q+1, q>0 | (m+s+2,m+s+q+1) |
| p+1, d>0 | (m+s+p,m+s+p+1) |
| e+1, d>0 | (m+s+p+2,m+s+e+1) |
| r | (2m-1,2m) |
| r+1, s>0 | (2m,m+1) |

All other cells have pairs (m+s+i-1,m+s+i) before r, or
(s+i-1,s+i) after r+1. The cell r is a comparison exception because
h(r/m)=1+{alpha+r/m} is on its lower branch, whereas P_r/m=2.
It is not a second high jump. The true jump is r+1 when s>0 and
the low cyclic seam 1 when s=0. No extrapolated P_0 is permitted.

The strict rational gates u-LH>1/100 and 1-AH-v>1/2 imply q<=p,
s+e<m and s+q<m for all m. When d>0, m>=200 and p>=q+2,
r>=e+2. Thus neither second-block junction meets the prefix or wrap.
The recovery proof's complete counts are

| m | Reflected interiors | Exceptions | Ordinary cells |
|---|---:|---:|---:|
| 2..6 | 0 | 2 | m-2 |
| 7..9 | q-1 | 3 | m-q-2 |
| 10..199 | q-1 | 4 | m-q-3 |
| >=200 | q+d-2 | 6 | m-q-d-4 |

They sum to m. Empty blocks and length-2 identity reversals are retained;
d=0 through m=199 and d=2 through m=399. Both parities of m, every
floor tie and the small s=0 wrap/seam coincidence are included. Being
exceptional in a Riemann comparison never removes a cell from geometry.

## 3. Exact full root and actual all-pairs feasibility

Using every pair above, at every R>0 put

```text
theta_R(h,k)=2 asin sqrt(h*k/((R+h)*(R+k))),
a_i=theta_R(P_(i-1),i), b_i=theta_R(i,P_i),
c_i=theta_R(P_(i-1),P_i),
d_i=max(a_i+b_i,c_i), S_m(R)=sum_(i=1)^m d_i.          (5)
```

Both branches are strictly decreasing and continuous in R, hence so is
their maximum. As R decreases to zero, d_i tends to 2*pi, including
m=2 and every seam; as R tends to infinity it tends to zero. Therefore
S_m has a unique positive root rho_m at 2*pi. Necessity of all-pairs
feasibility gives x_i>=a_i, y_i>=b_i, x_i+y_i>=c_i for the actual
cell P_(i-1)->i->P_i; summing gives S_m(R)<=2*pi.

At rho_m define positive gaps

```text
x_i=a_i, y_i=b_i+max(0,c_i-a_i-b_i).                   (6)
```

Their sum is exactly 2*pi and each cell total is d_i. The criterion's
sufficiency checks BOTH simple cyclic paths, independently, for each
endpoint type. Its argument specializes to (3) as follows:

- High-high paths consist of whole cells, bounded below by their
  actual chords c_i. In the shell [m+1,2m],
  theta(H,U)+theta(U,K)>theta(H,K); induction contracts any such
  path. At m=2 each of the two paths is one whole cell, so both
  identical numerical chord bounds must still be imposed.
- For a low-high path, its first high is either the target (the
  adjacent gap supplies the bound), or the remaining whole-cell path
  has length at least theta(U,target)>theta(low,target), since
  U>low. The opposite direction uses the other first high.
- A low-low path either uses a single common high, when its first
  gap alone exceeds the required low-low angle, or it contains a
  whole-cell high path whose endpoint radii both exceed the lows.
  The same dichotomy holds separately for the other direction.

The imported shell lemma holds for all R>0. Its small-angle sign gate is
2-2*z^2-z^3>5/8 for 0<z<1/sqrt(2); for z>=1/sqrt(2) the inverse-sine
branch is treated directly. No continuum inequality replaces this lemma.
Every seam-crossing path is covered: whole cells include their actual
chords, and a path ending at low 1, q+1, p+1, e+1, r or r+1 uses its
actual partial first/last gap. Crossing multiple jumps changes no bound.

Both directed separations therefore lie between theta_R and
2*pi-theta_R. Cumulative angles with radius-j center at distance rho_m+j
give Cartesian non-overlap by the cosine law, and central tangency.
This proves, for every m>=2,

```text
R_full(sigma_m)=rho_m, and (6) is feasible at rho_m.    (7)
```

Feasibility has been proved at the full root, not at R_chain. The
asymptotic and global statements have not been used in this argument.

## 4. Uniform control of empirical full costs, including both branches

Use the actual empirical measure and cost

```text
mu_m=(1/m)*sum_i delta_(i/m,P_(i-1)/m,P_i/m),
G_m=integral g dmu_m.                                 (8)
```

The recovery theorem, established for arbitrary continuous tests, gives
an error at most omega_F(5/m)+omega_F(2/m)+32*||F||/m for m>=200.
It can be made O(1/m) for THIS full cost without differentiating sqrt(t)
at zero. Indeed for t<=1/4,

```text
k/c=sqrt(t/x)+sqrt(t/y)<=2*sqrt(t)<=1,
```

so g=c there. On t>=1/4, the sum of absolute first derivatives of k
is at most 2*sqrt(2)+1<4; for c it is at most sqrt(2)<2. Each branch
and their maximum are therefore 4-Lipschitz in the max norm on that
half-box. On t<=1/4 only c is active. Split a straight segment at
t=1/4 to obtain the same bound across the two half-boxes. At the
boundary the values agree with the continuous full max. Thus

```text
g is globally 4-Lipschitz on D; 1<=g<=2*sqrt(2)<3,
|G_m-I_2| <= (7*4+32*3)/m = 124/m, m>=200.            (9)
```

This retains the branch switch, including ties. The six exceptions
have already been paid for in the recovery estimate. No new measure
recovery is deduced from (6), and no diagonal approximation replaces
the true high-high costs in (8).

For completeness, recheck the uniform angular hypotheses used in the
[full-root theorem](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md), Sections
2 and 4. At R=4*c*m^2, c>=c0>0, 1<=h,k<=2m, set
w=sqrt(h*k)/R and z=w/sqrt((1+h/R)*(1+k/R)). Rationalization (or
integration of the denominator's derivative) gives

```text
0<=w-z<=1/(4*c^2*m^2), z<=w<=1/(2*c*m).
```

For m>=1/c0, z<=1/2, and integration of
1/sqrt(1-z^2)-1<=z^2 gives 0<=asin(z)-z<=z^3/3. Hence

```text
|theta_R(h,k)-2*sqrt(h*k)/R| <= e_m(c0),
e_m(c0)=1/(2*c0^2*m^2)+1/(12*c0^3*m^3).               (10)
```

The chain sum has error <=2*e_m and the chord error <=e_m. The maximum
is 1-Lipschitz in its two scalar arguments, even at a tie. Summing ALL
m cells, including the exceptions, gives

```text
|S_m(4*c*m^2)-G_m/(2*c)| <= E_m(c0),
E_m(c0)=1/(c0^2*m)+1/(6*c0^3*m^2).                    (11)
```

There is no small-low denominator, bound on consecutive-high differences,
or requirement that a finite branch agree with its continuum branch.
For c>=1/32 and m>=200, (9)-(11) imply the explicit uniform score limit

```text
|S_m(4*c*m^2)-I_2/(2*c)|
 <=3008/m+16384/(3*m^2).                              (12)
```

## 5. A compact root bracket before evaluation at the root

Take c0=1/32, c1=1/2 and m>=2048. In this section write
E_m=1024/m+16384/(3*m^2)<1. Since 1<=G_m<3, (11) gives

```text
S_m(4*c0*m^2)>=16-E_m>15>2*pi,
S_m(4*c1*m^2)<3+E_m<4<2*pi,                          (13)
```

using 3<pi<22/7. Strict decrease therefore proves
c0<c_m=rho_m/(2m)^2<c1, uniformly for these orders (indeed for any
high permutation). We have verified the compact root-scale hypothesis
before substituting an unknown root into the error bound.

At c=c_m, equation (11), multiplied by c_m/(2*pi), gives

```text
|c_m-G_m/(4*pi)| <= E_m/(4*pi).                        (14)
```

Combining with the independent recovery estimate (9),

```text
C_2 := I_2/(4*pi),
|R_full(sigma_m)/(2m)^2-C_2|
 <= (1148/m+16384/(3*m^2))/(4*pi), m>=2048.            (15)
```

This proves the full-root limit along all integers m, not just a
divisibility subsequence. The cutoff and error constant are convenient
bounds, not optimal values. The finitely many smaller m are covered by
the exact feasibility/root theorem (7).

## 6. Branch and seam inequalities: continuum and finite versions

First classify the continuum cost used to identify C_2. From (1),

```text
lambda<u<v<a<b,
(A+u)-4*v=alpha-4*epsilon>693/10000>0.                 (16)
```

The second reflected pair and the replaced diagonal slab are thus
entirely chord: both high values are >=A+u and t<=v, so k/c<1.
This is a strict rational branch gate, not a numerical observation.
The prefix has a unique switch z1=A*z(x_*) in (0,lambda), defined by

```text
sqrt(z1/(A+z1))+sqrt(z1/(A+lambda-z1))=1.              (17)
```

Both squared summands increase strictly in t. The ratio is zero at
0 and exceeds 1 at lambda, because x_*>tau as in the accepted prefix
theorem. The independent checker also verifies the unsquared endpoint
sign using XL. The prefix therefore has a nonempty chord part AND a
nonempty chain part. The unreflected pre-wrap tail switches at a,
and the wrapped tail t>=b is always chain since 3*t>alpha.
In particular the complete cost is

```text
I_2 = integral_0^z1 sqrt((A+t)*(A+lambda-t)) dt
    + integral_z1^lambda sqrt(t)*(sqrt(A+t)+sqrt(A+lambda-t)) dt
    + integral_lambda^u (A+t) dt
    + integral_u^v sqrt((A+t)*(A+u+v-t)) dt
    + integral_v^a (A+t) dt
    + 2*integral_a^b sqrt(t*(A+t)) dt
    + 2*integral_b^1 sqrt(t*(alpha+t)) dt.             (18)
```

Endpoint ties have zero measure; the wrapped integrand has its correct
one-sided values. Finite cells near (17), a or b must still use (5).

Here are additional exact controls of the actual finite seams, independent
of ignoring their mass. Write t=i/m, x=P_(i-1)/m, y=P_i/m and
v_i=k/c=sqrt(t/x)+sqrt(t/y). For m>=200:

- Low seam 1: v_i<=2/sqrt(m)<1/2.
- Second block INCLUDING entry p+1 and exit e+1:
  t<=v+1/m and min(x,y)>A+u-3/m. The rational gate
  4*(v+1/200)/(1+AL+u-3/200)<(99/100)^2 proves v_i<99/100.
- Endpoint r: v_i>=2*sqrt((1-AH)/2)>5/4.
- True high wrap r+1: v_i>=sqrt((1-AH)/2)
  +sqrt((1-AH)/(1+1/200))>3/2.

At the prefix exit q+1, the correct pair is very different from a
diagonal pair. For m>=100000 its ratio satisfies

```text
v_i > sqrt((LL-1/100000)/(1+AH+2/100000))
      +sqrt((LL-1/100000)/(1+AH+LH+1/100000))
    > 201/200.                                       (19)
```

Every bound gets stronger with increasing m. Positive-side radical
comparisons certify (19) and the wrap inequality exactly. Since c(x,y)>=1,
these ratio margins are also lower bounds for |k-c|. By (10), the error
in the difference of the two angular branches, after multiplication by
2*c_m*m, is at most

```text
3/(c_m*m)+1/(2*c_m^2*m^2)
 <=96/m+512/m^2 < 1/200, m>=100000.                   (20)
```

Thus at the ACTUAL full root, for every m>=100000, seam 1 and the
entire second block with its two junctions are chord, while prefix
exit q+1, endpoint r and high wrap r+1 are chain. This cutoff is only
a sufficient sign bound. For smaller m, or near interior switches,
neither branch is discarded. In particular no continuum branch claim
is asserted uniformly down to R=0, where every cell is chain.

For exact finite checking at ANY rational R>0, set

```text
U=i*h/((R+i)*(R+h)), V=i*k/((R+i)*(R+k)),
W=h*k/((R+h)*(R+k)), h=P_(i-1), k=P_i.
```

If U+V>=1, asin(sqrt(U))+asin(sqrt(V))>=pi/2>asin(sqrt(W)),
so the chain wins. Otherwise the sum lies below pi/2; compare its sine
sqrt(U*(1-V))+sqrt(V*(1-U)) with sqrt(W). Put
A0=U*(1-V), B0=V*(1-U), H0=W-A0-B0. If H0<=0 the chain wins strictly;
if H0>0 the exact sign is that of 4*A0*B0-H0^2, with zero a genuine
tie. All sides squared are nonnegative, and the inverse-sine branch was
settled first. This oracle covers actual cyclic pairs, small m, seams,
and both branches without evaluating a numerical angle or root.

## 7. Exact coefficient of the fixed family and its strict saving

In (18), only the second slab differs from the accepted baseline cost
4*pi*C_hat. By its chord gate (16), with

```text
M=A+u+epsilon/2, h=epsilon/2=1/200,
J=integral_(-h)^h z^2/(M+sqrt(M^2-z^2)) dz,
```

rationalizing the chord-minus-diagonal integral gives the exact answer

```text
C_2 = C_hat-J/(4*pi)
    = C_hat + [h*sqrt(M^2-h^2)+M^2*asin(h/M)-2*h*M]/(4*pi).
                                                               (21)
```

Here C_hat=K(alpha_hat)/(2*pi)+(1+alpha_hat)^2*E(x_*)/(4*pi),
with precisely the imported K,E,x_* and alpha_hat. Formula (21), or
the full-max formula (18), defines C_2; a decimal does not define it.
It is now a full-radius coefficient by (15), as well as a continuum cost.

The radicand is >=(A+u)*(A+v)>0 and M<3/2. Since
integral_(-h)^h z^2 dz=epsilon^3/12 and the denominator is <2*M off zero,

```text
J>epsilon^3/(24*M),
C_hat-C_2>1/(144000000*pi)>2/10^9.                    (22)
```

The last comparison uses pi<22/7. It is also the earlier
[continuum second-block saving](PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md),
now legitimately transferred to the finite full-root family.
Combining (22) with the imported C_hat<14191364/10^8 yields

```text
C_2 < C_hat-1/(144000000*pi),
C_2 < 141913638/10^9.                                 (23)
```

An independent rational enclosure of (21)'s saving, obtained from its
positive integral rather than subtracting nearly equal chords, is

```text
2290431561/10^18 < C_hat-C_2 < 2290454215/10^18.         (24)
```

To reproduce it, put ML=1+AL+u+h, MH=1+AH+u+h. Lower-bound J by
epsilon^3/(24*MH) and upper-bound it by
epsilon^3/[12*(ML+sqrt(ML^2-h^2))]. Bound pi by Machin's identity with
alternating-series remainders and the radical by rational squares.
The endpoints in (24) are outward rounded rational displays. This is
an exact enclosure, not floating quadrature or a claim of optimality
within a larger block family.

## 8. Odd n: deletion, necessity and the fixed-order limit

Let sigma_m^- be the cyclic order obtained by deleting just radius 2m
from sigma_m, and let rho_m^-=R_full(sigma_m^-). Removing that circle
from (6) preserves every remaining central tangency and pair constraint.
The adjacent gaps across its position merge into their positive sum.
Thus, for every m>=2, sigma_m^- is a full-feasible order on
{1,...,2m-1} at rho_m, and

```text
rho_m^- <= rho_m.                                    (25)
```

This alone transfers an upper bound. To prove the normalized odd
fixed-order LIMIT, use a separate necessary condition, without applying
the alternating criterion to the now nonalternating odd cycle.
For m>=10, s>0 and the unique deleted high is P_r=2m. Only cells r
and r+1 contain it. All other high-low-high triples survive consecutively
in sigma_m^-. Their two-edge arcs are disjoint, so every feasible odd
placement at R satisfies

```text
T_m(R):=sum_(i not in {r,r+1}) d_i(R) <= 2*pi.         (26)
```

There are m-2 retained cells and three uncounted odd-cycle gaps. The
low at r, the low at r+1 and their new joining gap need not satisfy an
alternating-cell sufficiency theorem; (26) is only necessity.

T_m is continuous and strictly decreasing, with limit 2*pi*(m-2)>2*pi
at zero and zero at infinity. Let tau_m be its unique root at 2*pi.
Then necessity and (25) imply tau_m<=rho_m^-<=rho_m. Uniformly for
c>=c0=1/32, (10) and g<3 bound the two omitted cells by

```text
0<=S_m(4*c*m^2)-T_m(4*c*m^2) <= B_m,
B_m=96/m+2048/m^2+32768/(3*m^3).                      (27)
```

Indeed each d_i<=3/(2*c*m)+2*e_m(c0). For m>=2048, E_m<1 and B_m<1,
so the endpoint signs used in (13) also bracket tau_m/(2m)^2 in
(1/32,1/2). Equations (9), (11) and (27), evaluated at tau_m after
this bracket, give

```text
|tau_m/(2m)^2-C_2| <= (E_m+B_m+124/m)/(4*pi) -> 0.
```

Squeezing between tau_m and rho_m now proves

```text
R_full(sigma_m^-)/(2m-1)^2 -> C_2,                    (28)
```

because (2m/(2m-1))^2 tends to one. In particular the limit holds for
the family on all n, using sigma_m at n=2m and sigma_m^- at n=2m-1.
No equality of finite even and odd roots, and no general deletion
invariance of a fixed-order coefficient, has been assumed.

## 9. Separate global corollary and exact scope

The feasible even and deleted odd placements prove, respectively,
R*(2m)<=rho_m and R*(2m-1)<=rho_m. The normalized limits already
proved above therefore give

```text
limsup_(n->infinity) R*(n)/n^2 <= C_2
 < C_hat-1/(144000000*pi),
limsup_(n->infinity) R*(n)/n^2 < 141913638/10^9.         (29)
```

The new constant is strictly below the best coefficient of the original
one-prefix family. The second block has remained fixed. The global lower
bound C_term and finite certified scope remain unchanged. There is no
claim that C_2 is sharp, that a global normalized limit exists, that these
orders are globally optimal, or that any particular finite m beats the
old order; the limits imply eventual improvement but no comparison
cutoff is certified here. No contact or floating-circle conclusion is made.

## 10. Verification and authority

The [independent exact checker](../ops/TASK-20260906__second_block_full_root/check_full_root.py)
audits rational domain, branch and seam margins; the Lipschitz/root/deletion
constants; actual cyclic pairs at a bounded list of floor-sensitive sizes;
both angular branches with the sign-safe oracle; independent half-angle
arctangent interval comparisons of signs and angular/full-max errors;
deletion incidence; and the saving (24).
It treats every floor pair compatible with (1), never substituting
decimal floors. This is a prescribed construction audit, not permutation
enumeration. Synthetic exact ties test the oracle's non-strict boundary.
The earlier recovery checker is rerun separately; its arbitrary-test
theorem remains the source of recovery, not the new finite branch checks.

The proof above supplies the all-m quantifiers. Local exact checks are
not an external proof acceptance or a certificate of finite global optima.
Commands, scope, independence and source provenance are recorded in
[the STRICT evidence](../ops/TASK-20260906__second_block_full_root/EVIDENCE.md).
The sole owner of (7), (15), (21)-(24) and (28) is
knowledge/FIXED_ORDER_THEORY.md. The sole owner of (29) is
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md. Prior notes retain their historical
task scope; the public paper, certificates and production code are unchanged.
