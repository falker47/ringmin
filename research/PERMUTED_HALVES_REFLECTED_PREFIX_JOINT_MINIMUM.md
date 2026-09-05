# Exact joint minimum of the two-parameter reflected-prefix family

```text
status=PROVED
classification=exact recovery, fixed-order full-radius and family-minimization theorem / separate proved global limsup corollary
domain=0<=alpha<=1/2; 1/4<=lambda<1-alpha; every fixed pair; all integers m>=2
minimizer=(alpha_hat,(1+alpha_hat)*x_*) uniquely
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question, accepted inputs and notation

Let D be the parameter domain in the header. For (alpha,lambda) in D set

```text
A=1+alpha, b=1-alpha, a=A/3, x=lambda/A,
h_alpha(t)=1+{t+alpha},
K(alpha)=integral_0^1 max(sqrt(t*h_alpha(t)),h_alpha(t)/2) dt.
                                                               (1)
```

Fractional-part values at the wrap and endpoints are retained in finite
comparisons below; they have zero mass in these integrals. The split
formula for K on the closed alpha interval is in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Section 5.

Keep exactly the alpha-independent functions from
[PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
Sections 2-6:

```text
c(u,x)=sqrt((1+u)*(1+x-u)),
k(u,x)=sqrt(u)*(sqrt(1+u)+sqrt(1+x-u)),
d(u)=max(1+u,2*sqrt(u*(1+u))),
E(x)=integral_0^x [max(c(u,x),k(u,x))-d(u)] du, 0<=x<=1.
                                                               (2)
```

The user supplies the following two accepted exact theorems as inputs:

1. E is continuous on [0,1] and has its unique global minimum at x_*,
   with 1/4<tau<x_*<1/3 and
   XL=719/2500<x_*<XH=2877/10000. Here tau is the unique solution of
   sqrt(tau/(1+tau))+sqrt(tau)=1. The source above includes the
   descending final segment of E; global convexity is not a premise.
2. With e=E(x_*), the function K(alpha)/(2*pi)+A^2*e/(4*pi) has its
   unique minimum on [0,1/2] at alpha_hat, where
   1093/10000<alpha_hat<10931/100000. This is the theorem in
   [PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md](PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md),
   Sections 1, 3-5. Its minimum is the existing C_hat.

To avoid confusing the second coordinate, write

```text
C_tilde(alpha,x)=K(alpha)/(2*pi)+A^2*E(x)/(4*pi).
```

The earlier alpha note's C(alpha,x_*) means C_tilde(alpha,x_*).
Here C(alpha,lambda) will be the full-radius coefficient of the actual
two-parameter construction. Sections 2-5 first prove, for every fixed
(alpha,lambda) in D, recovery and

```text
R_full(sigma_m(alpha,lambda))/(2m)^2 -> C(alpha,lambda)
 = C_tilde(alpha,lambda/A)
 = K(alpha)/(2*pi)+A^2*E(lambda/A)/(4*pi).                (3)
```

Section 6 then proves unique joint minimization at
(alpha_hat,lambda_hat), lambda_hat=(1+alpha_hat)*x_*.
Actual finite full feasibility and the resulting global limsup inequality
are separate statements in Sections 7-8. No assertion concerns a finite-m
family optimizer, arbitrary high permutations or couplings, or a geometric
global optimum. The accepted one-variable theorems are not re-proved here.

## 2. All finite floors, predecessors and coincident cells

For every fixed admissible pair and every integer m>=2 define

```text
s=floor(alpha*m), q=2*floor(lambda*m/2), r=m-s,
beta=s/m, L=q/m,
H(j)=m+1+((j+s-1) mod m), 1<=j<=m,
J(i)=q+2-i if i<=q is even, and J(i)=i otherwise,
P_i=H(J(i)), P_0=P_m,
sigma_m(alpha,lambda)=(1,P_1,2,P_2,...,m,P_m).            (4)
```

Mod takes values 0,...,m-1. The exact bounds are

```text
0<=alpha-beta<1/m, 0<=lambda-L<2/m,
0<=s<=floor(m/2), 0<=q, q even,
s+q <= (alpha+lambda)*m < m,
r-q >= m*(b-lambda)>0, hence r>=q+1 and q<m.             (5)
```

Thus the block lies before the finite high wrap even when b-lambda
is arbitrarily small. No claim r>=q+2 is made at finite m. The odd
block ranks stay fixed, the even ranks become q,q-2,...,2, and every
tail rank stays fixed. These images partition {1,...,m}; J is an
involution and H is a bijection. Consequently P is a true permutation
of {m+1,...,2m}. For q=0 and q=2, J is the identity.

For q>=2 the q-1 interior block cells have these exact pairs, with t=i/m:

| Cells | P_(i-1)/m | P_i/m | Count |
|---|---|---|---|
| even i=2,...,q | 1+beta+t-1/m | 1+beta+L-t+2/m | q/2 |
| odd i=3,...,q-1 | 1+beta+L-t+3/m | 1+beta+t | q/2-1 |

Use a SET of exceptional comparison cells:

```text
X_m={1,q+1,r,r+1} intersect {1,...,m}, if q>=2;
X_m={1,r,r+1} intersect {1,...,m},     if q=0.           (6)
```

The actual pairs at its seams are always retained:

- At i=1, (P_m,P_1)=(m+s,m+s+1) for s>0, and (2m,m+1)
  for s=0. The finite low seam uses the actual cyclic predecessor.
- At i=q+1, q>=2, the junction pair is (m+s+2,m+s+q+1).
  When q+1=r it ends at 2m; this is one cell with two roles.
- At i=r+1, s>0, the high wrap is exactly (2m,m+1).
  For s=0 it occurs at i=1 instead; r+1 is outside the index range.
- At i=r, P_r/m=2, while h_alpha(r/m)=alpha+r/m is on its lower
  branch: r/m>=b, including equality. This endpoint is exceptional
  even if alpha*m is an integer.

For q>=2 the interior block is disjoint from X_m, and the exact sizes are

| Condition | s>0 | s=0 |
|---|---:|---:|
| r>=q+2 | 4 | 3 |
| r=q+1 | 3 | 2 |

For q=0 the size is 2 when s=0; it is 3 when s>0,r>1; and it is 2
when s>0,r=1. The last case is precisely m=2,s=1,alpha=1/2: the
low seam and wrap endpoint coincide, and X_m={1,2}. This is why the
q=0 count from an open alpha interval cannot be used unchanged here.

Every remaining ordinary tail pair is exactly

```text
(1+beta+t-1/m,1+beta+t),  if i<r;
(beta+t-1/m,beta+t),      if i>r+1.                      (7)
```

For q>=2 there are m-(q-1)-|X_m| such ordinary cells; for q=0 there
are m-|X_m|. These partitions count all m cells, including q=0,2,
coincident junction/wrap endpoints and m=2,3. At alpha=0, s=0,r=m
and the high wrap coincides with the low seam. At alpha=1/2 both
parities of m satisfy (5)-(7). No exceptional cell is deleted from
the permutation, empirical measure or exact full-radius score.

## 3. Recovery without a common positive pre-wrap gap

On D_box=[0,1] x [1,2]^2 form the empirical measure with its actual predecessor:

```text
mu_m=(1/m) sum_i delta_(i/m,P_(i-1)/m,P_i/m).
```

Define the candidate recovered probability measure by, for continuous f,

```text
integral f dmu_(alpha,lambda)
 =(1/2) integral_0^lambda
    [f(t,A+t,A+lambda-t)+f(t,A+lambda-t,A+t)] dt
  +integral_lambda^1 f(t,h_alpha(t),h_alpha(t)) dt.       (8)
```

All these triples are in D_box since A+lambda<2. Either high marginal
of the reflected block is Lebesgue measure on [A,A+lambda], by the
substitution t->lambda-t. This is exactly the part replaced in the
diagonal shift. The low marginal is uniform on [0,1], each high marginal
is uniform on [1,2], and the two conditional high marginals agree by
symmetry. Realization, rather than these marginal properties alone,
is proved next.

Compare each actual atom with (t,A+t,A+lambda-t) for even i<=q,
with (t,A+lambda-t,A+t) for odd i<=q, and with the diagonal triple
for i>q. Call the equally weighted comparison measure nu_m.
Outside X_m the max-norm coordinate error is at most 3/m. In the
odd reflected predecessor it is
(beta-alpha)+(L-lambda)+3/m in (0,3/m]; the other block errors have
absolute value at most 2/m. Tail errors have absolute value less than
2/m. Their branch match is exact: i<r gives
i/m<=1-(s+1)/m<b, while i>r+1 gives i/m>b. The excluded comparison
endpoint i=r and actual wrap i=r+1 need no such approximation.

For M=||f||_infinity and the uniform max-norm modulus omega_f,

```text
|integral f dmu_m-integral f dnu_m|
 <= omega_f(3/m)+2*M*|X_m|/m
 <= omega_f(3/m)+8*M/m.                                 (9)
```

For completeness, the Riemann estimate also works for every finite m.
On [0,L], even comparison atoms are right endpoints of intervals of
length 2/m; odd comparison atoms are their midpoints. Weight 1/m
gives one half of each integral. Along either affine triple, f has
modulus at most omega_f, so their total error is <=L*omega_f(2/m).
If q=0 this interval and both sums are empty.

On [L,1], remove from the Riemann estimate the at most two grid
intervals whose closures contain b. Their total error is <=4*M/m,
including b=1 at alpha=0. On all other intervals the diagonal triple
is affine with slopes 1,1,1, giving error <=(1-L)*omega_f(1/m).
Finally replace the diagonal interval [L,lambda] by its reflected
integrand. This costs at most 2*M*(lambda-L)<=4*M/m. Thus

```text
|integral f dmu_m-integral f dmu_(alpha,lambda)|
 <= omega_f(3/m)+omega_f(2/m)+16*M/m ->0.                (10)
```

In particular mu_m converges weakly to (8) along all integers m for
every fixed admissible pair. The bound contains no reciprocal of
b-lambda and requires neither distinct exception indices nor an
eventual separation threshold. It covers parameters arbitrarily close
to the upper boundary. Since lambda>=1/4, q>=2 for m>=8, but even
that eventual observation is unnecessary for (10). Finite floors are
never computed from decimal approximations of implicit minimizers.

## 4. The full cost, including every branch and alpha endpoint

Keep the continuous symmetric full cost

```text
g(t,u,v)=max(sqrt(t)*(sqrt(u)+sqrt(v)),sqrt(u*v)).
```

Symmetry makes its recovered cost B(alpha,lambda)+T(alpha,lambda),
the full reflected-block integral plus the diagonal tail integral.
For the block set z_lambda=lambda when

```text
v_lambda(lambda)<=1,
v_lambda(t)=sqrt(t/(A+t))+sqrt(t/(A+lambda-t)).
```

Otherwise z_lambda is the unique point in (0,lambda) where v_lambda=1.
Both summands strictly increase in t, so this exhausts the cases and
handles a tie at the endpoint. Dividing by the positive chord shows
that the chord wins exactly up to z_lambda. Hence

```text
B(alpha,lambda)
 =integral_0^z_lambda sqrt((A+t)*(A+lambda-t)) dt
  +integral_z_lambda^lambda
       sqrt(t)*(sqrt(A+t)+sqrt(A+lambda-t)) dt.          (11)
```

In normalized variables z_lambda=A*z(x), with z(x)=x for x<=tau;
for x>tau it is the unsquared switch root from the accepted E theorem.
The zero-length chain interval at x=tau is included.

For the diagonal first branch, comparison of the two nonnegative
values A+t and 2*sqrt(t*(A+t)) puts the switch at a=A/3.
Throughout the closed alpha interval,

```text
b-a=(2-4*alpha)/3>=0,
b-alpha/3=1-4*alpha/3>=1/3>0.                           (12)
```

Thus the wrapped branch is always chain. The exact tail is

```text
T(alpha,lambda)
 =integral_lambda^a (A+t) dt
  +2*integral_a^b sqrt(t*(A+t)) dt
  +2*integral_b^1 sqrt(t*(alpha+t)) dt,   lambda<=a;

T(alpha,lambda)
 =2*integral_lambda^b sqrt(t*(A+t)) dt
  +2*integral_b^1 sqrt(t*(alpha+t)) dt,   lambda>=a.      (13)
```

The two expressions agree at lambda=a. At alpha=1/2 one has a=b,
lambda<a, and the middle interval in the first expression is empty.
At alpha=0 the wrapped integral is empty; the endpoint h_0(1)=1
has already been treated in (6)-(10). The lower boundary lambda=1/4
requires no change to (11)-(13). A reflected block may be entirely
chord or have a chain part, independently of the tail switch; neither
max branch is suppressed.

The full diagonal integral over [0,1] is 2*K(alpha). Because
lambda<b, its prefix integrand on [0,lambda] is
max(A+t,2*sqrt(t*(A+t))). Replacing precisely that prefix by (11)
and setting t=A*u gives

```text
integral g dmu_(alpha,lambda)
 =2*K(alpha)
  +integral_0^lambda [g(t,A+t,A+lambda-t)-g(t,A+t,A+t)] dt
 =2*K(alpha)+A^2*E(lambda/A).                           (14)
```

One factor A comes from the integrand and one from dt. This is an
identity of the full maxima even when x crosses tau or 1/3. All
wrapped-tail dependence remains in K. There is no differentiation
of finite floors, discarded moving-wrap term or chain-only substitution.

## 5. Fixed-order full-radius identification for each pair

The exact arbitrary-high-permutation theorem in
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, applies to every permutation in (4), including m=2.
It identifies rho_m=R_full(sigma_m(alpha,lambda)) as the unique
positive root of

```text
S_m(R)=sum_i max(theta_R(i,P_(i-1))+theta_R(i,P_i),
                theta_R(P_(i-1),P_i))=2*pi,
theta_R(u,v)=2*asin(sqrt(u*v/((R+u)*(R+v)))).            (15)
```

All m cells, including the exceptions in (6), remain in this sum.
Necessity and sufficiency
refer to both directed paths for every pair, not only adjacency.
The imported uniform-root theorem in
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Sections 2-4, first brackets rho_m/(2m)^2 between fixed positive
constants, and only then proves

```text
rho_m/(2m)^2=(integral g dmu_m)/(4*pi)+O(1/m),           (16)
```

uniformly over all high permutations. Its angular error includes
arbitrary high jumps, low radii near zero and branch ties. As g is
continuous on D_box, (10), (14) and (16) prove exactly (3) for every
fixed admissible pair. This is the minimum full radius for that order;
it is not the adjacent-chain closure coefficient or an optimization
over finite-m orders.

## 6. Exact admissibility and unique joint minimum

For any alpha in [0,1/2], the admissible normalized interval is

```text
1/(4*A)<=x<b/A, with 1/(4*A)<=1/4< x_* <1/3<=b/A<=1.
                                                               (17)
```

The right inequality 1/3<=b/A is exactly 4*alpha<=2, and A>0.
Thus lambda_*(alpha)=A*x_* is strictly admissible at EVERY alpha,
including both endpoints. If desired the accepted rational x bracket
gives explicit uniform margins:

```text
lambda_*(alpha)-1/4 > XL-1/4=47/1250,
b-lambda_*(alpha) >=1/2-(3/2)*x_*
                  >1/2-(3/2)*XH=1369/20000>0.          (18)
```

At alpha=0, lambda_*=x_* is between 1/4 and 1/3; at alpha=1/2,
it is between 3/8 and 1/2, strictly below the wrap. These are exact
admissibility statements, independent of decimal values.

Now take ANY (alpha,lambda) in D and use (3). Since x=lambda/A
belongs to [0,1], the two accepted minima yield the identity

```text
C(alpha,lambda)-C_hat
 = A^2/(4*pi) * [E(x)-E(x_*)]
   +[C_tilde(alpha,x_*)-C_tilde(alpha_hat,x_*)] >=0.     (19)
```

Both terms are nonnegative, and A^2/(4*pi)>0. Equality in the first
term holds exactly when x=x_*; equality in the second holds exactly
when alpha=alpha_hat. By (17), the first comparison uses an actual
admissible construction for this same alpha, including alpha=0,1/2.
Therefore equality in (19) holds if and only if

```text
(alpha,lambda)=(alpha_hat,(1+alpha_hat)*x_*).            (20)
```

This point is admissible, so it is the unique global minimizer of the
entire stated two-parameter coefficient family. Neither alpha endpoint
is minimizing, by the accepted strict alpha minimum. At lambda=1/4,
x<=1/4<x_*, so the first term is strictly positive. No assumption
of joint convexity or global monotonicity to the right of x_* is used.

The open upper boundary creates no competing infimum. For each fixed
alpha, continuity gives

```text
lim_(lambda up to b) C(alpha,lambda)
 =K(alpha)/(2*pi)+A^2*E(b/A)/(4*pi)
 >C_tilde(alpha,x_*)>=C_hat,                            (21)
```

because b/A in [1/3,1] excludes x_*. This is a limit of coefficients
from within D, not a claim of recovery at lambda=b. It also remains
separated if alpha varies: let eta=(1/3-XH)/2=1369/60000>0.
If 0<b-lambda<=eta, then

```text
x=b/A-(b-lambda)/A >=1/3-eta=18631/60000>XH>x_*.
```

By continuity and uniqueness, the exact constant
gamma=min_{18631/60000<=y<=1}(E(y)-E(x_*)) is positive.
Equation (19) then gives C(alpha,lambda)>=C_hat+gamma/(4*pi).
No numerical evaluation of gamma or search near the boundary is needed.

## 7. Actual all-pairs feasibility at every finite full root

For each fixed pair and each m>=2, evaluate at the exact root rho_m
from (15)

```text
a_i=theta_(rho_m)(P_(i-1),i), b_i=theta_(rho_m)(i,P_i),
c_i=theta_(rho_m)(P_(i-1),P_i),
u_i=a_i, v_i=b_i+max(0,c_i-a_i-b_i).                    (22)
```

These positive gaps for P_(i-1)->i->P_i have total 2*pi. The
imported theorem proves both directed pair paths satisfy their angular
lower bounds, for all endpoint types, every seam and m=2. Cumulative
angles with radius-j centers at distance rho_m+j therefore give
Cartesian pairwise non-overlap and tangency to the central circle.
This supplies actual feasible placements, separately from the limiting
coefficient calculation and its joint minimization. Their radii are
minimal in their fixed orders, without a claim of global minimality.

## 8. Separate global limsup construction and scope

For any fixed admissible pair, feasibility gives R*(2m)<=rho_m.
Deleting only radius 2m retains exactly {1,...,2m-1}, all remaining
central tangencies and every remaining pairwise non-overlap. Thus
R*(2m-1)<=rho_m. Since (2m/(2m-1))^2 tends to 1, (3) proves

```text
limsup_(n->infinity) R*(n)/n^2 <= C(alpha,lambda).
```

In particular at (20),

```text
limsup_(n->infinity) R*(n)/n^2 <= C_hat.                 (23)
```

This is the existing upper coefficient, now proved optimal within the
stated two-parameter family. It is not a new numerical improvement.
The accepted C_hat comparisons retain their original meanings. No
matching global lower bound, normalized global limit, general
permutation/coupling minimum, finite global certificate extension,
or contact/floating-circle classification follows. The family theorem
concerns leading coefficients for fixed parameters; it identifies no
minimizer of the finite-m floor-dependent radii. Other alpha regimes
and reflection at or across the upper boundary are outside this theorem.

## 9. Verification and ownership

The [bounded exact checker](../ops/TASK-20260905__reflected_prefix_joint_minimum/check_joint_minimum.py)
tests only new rational admissibility/branch gates and finite occurrence,
partition, seam and coordinate bookkeeping. It uses integers/Fraction,
compares the formula with an independent list construction, and includes
exact floor boundaries, interior floor states and near-wrap probes.
It performs no permutation search, numerical quadrature, optimization,
or import from production code, verify.py or previous checkers. Those
finite checks support bookkeeping; Sections 2-6 are the all-domain proof.
The [task evidence](../ops/TASK-20260905__reflected_prefix_joint_minimum/EVIDENCE.md)
records exact commands, outputs, budgets, hashes and limitations.

The user-accepted E and alpha minima and the exact full-feasibility and
uniform-root theorems remain explicit dependencies. This task does not
record independent external acceptance of those sources or of this new
extension. The single owner of recovery, coefficient definitions and
family/fixed-order results is knowledge/FIXED_ORDER_THEORY.md; only the
global limsup consequence belongs to knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md.
Earlier notes keep their historical task scopes. Published arXiv-v1
assets, finite certificates and production implementations are unchanged.
