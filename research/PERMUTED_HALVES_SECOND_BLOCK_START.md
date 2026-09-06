# Second reflected block: exact positive start derivative at the width minimum

```text
status=PROVED
classification=exact continuous theorem with a rational interval gate
domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon=epsilon_* fixed; u near 1/3
result=partial_u Delta C(1/3,epsilon_*)>0
finite_recovery_and_radius_transfer=outside this task
proved_on=2026-09-06
published_snapshot=arXiv v1 unchanged
```

## 1. Exact inputs, two-parameter family and theorem

Keep the exact baseline alpha=alpha_hat, A=1+alpha and lambda=A*x_*
from the [joint prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md).
Import the exact unique width minimum epsilon_* at u0=1/3 from the
[width theorem](PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md), Sections 1, 4 and 7:

```text
alpha_L=10930369/10^8 < alpha_hat < alpha_H=10930371/10^8,
EL=31248/10^6 < epsilon_* < EH=1/32,
719/2500 < x_* < XH=2877/10000,
A_L=1+alpha_L, A_H=1+alpha_H, a=A/3, b=1-alpha.
                                                               (1)
```

The refined alpha bracket is equation (25) of that proof. These brackets
enclose the same exact minimizers; no decimal is a defining parameter,
and neither alpha nor lambda is varied here.

For lambda<u<u+epsilon<b, use precisely the slab replacement in
[the second-block variation](PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md),
Sections 1-3. On [u,u+epsilon], replace the baseline diagonal by equal
masses at (t,A+t,A+2*u+epsilon-t) and its high-coordinate swap. Keep
the rest of the baseline mu_0 fixed. Reflection preserves each uniform
high marginal, the swap preserves conditional high-marginal equality,
and the low marginal is unchanged. These identities remain valid as u
moves within the strictly disjoint pre-wrap domain.

Write mu_(u,epsilon) for this measure and retain the full cost:

```text
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)),
C(mu)=(1/(4*pi))*integral g dmu,
Delta C(u,epsilon)=C(mu_(u,epsilon))-C(mu_0),
D(u,epsilon)=4*pi*Delta C(u,epsilon).                 (2)
```

**Theorem.** D is smooth in a neighborhood of (u0,epsilon_*), and

```text
partial_epsilon D(u0,epsilon_*)=0,
partial_u D(u0,epsilon_*)
 =2*B+epsilon_*-sqrt(B*(B+epsilon_*))
  -sqrt(u0+epsilon_*)*(sqrt(B)+sqrt(B+epsilon_*)),
B=A+u0,
66955912/10^12 <= partial_u D(u0,epsilon_*)
                <= 74512461/10^12.                   (3)
```

In particular 1/20000<partial_u D<1/10000, so the requested derivative
partial_u Delta C is strictly positive, not zero. There is also a direct
analytic sign proof before imposing width stationarity (Section 4).

Consequently (u0,epsilon_*) is not a stationary point or a local minimum
of the continuous family in (u,epsilon). Moving u slightly to the left
with this exact epsilon_* fixed strictly lowers C. This is compatible
with unique global minimization on the one-dimensional slice u=u0.

## 2. Full max, diagonal cutoff and a uniform local branch certificate

Put s=t-u and, for 0<=s<=epsilon, define

```text
B=A+u, t=u+s, X=B+s=A+t, Y=B+epsilon-s,
c(s)=sqrt(X*Y), k(s)=sqrt(t)*(sqrt(X)+sqrt(Y)),
d(s)=max(X,2*sqrt(t*X)),
v(s)=k(s)/c(s)=sqrt(t/X)+sqrt(t/Y).                    (4)
```

The equal swapped costs remove the factor 1/2 in the measure definition.
The exact full-max difference is

```text
D=integral_0^epsilon [max(c(s),k(s))-d(s)] ds.          (5)
```

The prefix, its own switch, the other diagonal mass and the wrapped
tail cancel exactly. In particular there is no differentiation of the
baseline alpha/lambda parameters or of a finite-size floor.

Both summands of v increase strictly in s. Define z=epsilon if
v(epsilon)<=1, z=0 if v(0)>=1, and otherwise let z be the unique
unsquared root v(z)=1 in (0,epsilon). The removed diagonal is chord
exactly when t<=a. With w=min(epsilon,max(0,a-u)), formula (5) is

```text
D=integral_0^z c ds+integral_z^epsilon k ds
  -integral_0^w (B+s) ds
  -2*integral_w^epsilon sqrt((u+s)*(B+s)) ds.           (6)
```

This full formula retains both max branches and both switches, including
zero-length intervals. The branch reduction used below is proved next.
For delta=1/10^6, set u_-=u0-delta and u_+=u0+delta. Throughout the
closed parameter rectangle

```text
alpha_L<=alpha<=alpha_H,
u_-<=u<=u_+, EL<=epsilon<=EH,                          (7)
```

the exact gates are

```text
A_H*XH<u_-, u_++EH<1-alpha_H,
3*(u_++EH)<A_L, A_L>EH,
sqrt((u_-+EL)/(A_H+u_-+EL))
 +sqrt((u_-+EL)/(A_H+u_-))>1.                         (8)
```

Thus the slab stays strictly disjoint, pre-wrap and wholly below a;
the removed diagonal is chord everywhere, with w=epsilon. Also
v(0)<2*sqrt(u/(A+u))<1. At the other endpoint v(epsilon) increases
with u and epsilon and decreases with A: for its second squared term
the u derivative is (A-epsilon)/(A+u)^2>0; the other derivatives have
immediate positive or negative signs. The last gate in (8) therefore
proves v(epsilon)>1 on (7). The reflected block is strictly mixed,
with 0<z<epsilon, on the whole rectangle. All inequalities are strict,
so the same branch pattern holds on an open neighborhood of every
point of (7). No diagonal-chain contribution is silently suppressed.

## 3. Implicit switch and both moving physical endpoints

At the switch put t=u+z, X=A+t and Y=B+epsilon-z. Differentiation
of the unsquared v, first with s held fixed, gives

```text
v_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0,
v_u=[A/X^(3/2)+(Y-t)/Y^(3/2)]/(2*sqrt(t)),
v_epsilon=-sqrt(t)/(2*Y^(3/2)),
N=A*(Y/X)^(3/2)+Y+t,
z_u=-[A*(Y/X)^(3/2)+Y-t]/N,
z_epsilon=t/N,
1+z_u=2*z_epsilon.                                   (9)
```

Here Y-t=A+epsilon-2*z>A-epsilon>0, hence -1<z_u<0 and
0<z_epsilon<1/2. The implicit function theorem makes z smooth in
(u,epsilon) on the local regime. The physical switch is xi=u+z;
its start velocity is xi_u=1+z_u, not z_u. The integral formulas
with smooth integrands and endpoints now give the asserted smoothness
of D. In particular differentiating a nonsmooth pointwise max needs no
unjustified exchange of limits.

To retain the moving slab endpoints explicitly, use physical t and set

```text
q=u+epsilon, xi=u+z,
c_tilde(t,u)=sqrt((A+t)*(A+2*u+epsilon-t)),
k_tilde(t,u)=sqrt(t)*(sqrt(A+t)+sqrt(A+2*u+epsilon-t)),
d0(t)=max(A+t,2*sqrt(t*(A+t))).
```

Then D=integral_u^xi c_tilde+integral_xi^q k_tilde-integral_u^q d0.
Holding epsilon and A fixed, the COMPLETE Leibniz formula is

```text
D_u=k_tilde(q,u)-d0(q)-[c_tilde(u,u)-d0(u)]
    +[c_tilde(xi,u)-k_tilde(xi,u)]*(1+z_u)
    +integral_u^xi sqrt((A+t)/(A+2*u+epsilon-t)) dt
    +integral_xi^q sqrt(t/(A+2*u+epsilon-t)) dt.        (10)
```

Both physical endpoints have velocity 1. The moving-switch term
vanishes because the two COSTS agree at xi, not because its velocity
vanishes or because their derivatives agree. The diagonal d0 has no
u dependence at fixed t, since A is fixed. Its two endpoint terms give
d0(u)-d0(q)=-epsilon on (7). If its cutoff were interior, it would
be the fixed physical point a; equivalently, in (6) the apparent moving
cutoff w=a-u has coefficient -[(B+w)-2*sqrt((u+w)*(B+w))]=0.

Define

```text
c0=sqrt(B*(B+epsilon)),
p=sqrt(u+epsilon)*(sqrt(B+epsilon)+sqrt(B)),
I=integral_0^z sqrt((B+s)/(B+epsilon-s)) ds
  +integral_z^epsilon sqrt((u+s)/(B+epsilon-s)) ds.
```

The lower reflected endpoint is chord, the upper one is chain, and
the diagonal endpoints are both chord. Equation (10) is exactly

```text
D_u=p-c0-epsilon+I.                                  (11)
```

The two slab-endpoint differences generally do not cancel each other.
Omitting either one, or treating A+2*u+epsilon-t as independent of u,
would give a different derivative.

## 4. Translated formula and direct strict sign

At fixed s in (4), all three variables t,X,Y have u derivative 1.
Differentiate (6), keeping its boundary terms until the costs cancel:

```text
D_u=integral_0^z c_u ds+integral_z^epsilon k_u ds
    -w-integral_w^epsilon (A+2*(u+s))/sqrt((u+s)*(B+s)) ds
    +[c(z)-k(z)]*z_u
    -[(B+w)-2*sqrt((u+w)*(B+w))]*w_u.                 (12)
```

This expression applies within each smooth cutoff regime. In our
neighborhood w=epsilon and w_u=0. The switch coefficient is zero,
so the same complete derivative is

```text
D_u=integral_0^z [(X+Y)/(2*sqrt(X*Y))-1] ds
    +integral_z^epsilon [
        (sqrt(X)+sqrt(Y))/(2*sqrt(t))
        +sqrt(t)*(1/sqrt(X)+1/sqrt(Y))/2-1] ds.        (13)
```

One can also obtain (13) from (10) by translating t=u+s: the integral
of each spatial derivative supplies exactly the endpoint terms in
(10), and the internal switch costs cancel once. Thus (11) and (13)
include the same moving-domain contributions.

The first integrand in (13) equals

```text
(sqrt(X)-sqrt(Y))^2/(2*sqrt(X*Y))>=0,                  (14)
```

with equality only at s=epsilon/2. The second is

```text
(sqrt(X/t)+sqrt(t/X)+sqrt(Y/t)+sqrt(t/Y))/2-1>1.       (15)
```

Indeed each reciprocal pair is at least 2, and the X pair is strictly
greater than 2 because X=A+t>t. All quantities are positive before
this comparison. Since the chain interval has positive length,

```text
D_u>epsilon-z>0                                     (16)
```

throughout (7), without using width stationarity, quadrature or a
numerical enclosure of z. This already proves the requested sign and
excludes a stationary point anywhere in this local rectangle.

## 5. Elimination at the exact width root and the only value gate

For completeness differentiate the same full integral with respect to
epsilon, with u fixed. The physical lower endpoint now has velocity 0,
the upper one has velocity 1, and the internal term
[c_tilde(xi)-k_tilde(xi)]*z_epsilon again vanishes. The result is

```text
D_epsilon=p-(B+epsilon)+I/2.                         (17)
```

Combining (11) and (17), BEFORE imposing stationarity, gives

```text
D_u=2*D_epsilon+2*B+epsilon-p-c0.                     (18)
```

At (u0,epsilon_*) the imported width theorem gives D_epsilon=0.
This proves the exact radical formula in (3). It does not set epsilon
to a rational proxy or differentiate epsilon_* as a function of u.

Here is a transparent interval enclosure that uses only (1). For
rational A,e>0 at u=u0, put

```text
R(A,e)=sqrt((A+u0)*(A+u0+e))
       +sqrt(u0+e)*(sqrt(A+u0)+sqrt(A+u0+e)).
```

Every positive summand increases separately in A and e. Enclose
R(A_L,EL) from below by R_L and R(A_H,EH) from above by R_H. Then

```text
2*(A_L+u0)+EL-R_H <= D_u(u0,epsilon_*)
                  <=2*(A_H+u0)+EH-R_L.               (19)
```

The independent choices of endpoints lose correlation and widen the
interval; they cannot exclude the true value. The
[stdlib checker](../ops/TASK-20260906__second_block_start/check_start.py)
encloses each rational square root on the grid 1/S, S=10^30. For x=n/d
it computes j=isqrt(floor(n*S^2/d)); the enclosure is
[j/S,(j+1)/S], with an exact upper endpoint j/S when j^2*d=n*S^2.
It checks the rational squared inequalities on every call. Positive
products and sums preserve the stated lower/upper directions.

The final outward display of (19) is exactly the interval in (3).
The checker also verifies its containment in (1/20000,1/10000).
No transcendental evaluation, switch root search, subdivision, optimizer
or parameter scan enters this gate. For the radical-sum gate in (8),
set r=1-p-q for its two rational radicands p,q. If r<0 the sum of roots
exceeds 1; otherwise its sign relative to 1 is exactly the sign of
4*p*q-r^2. Both sides are nonnegative before squaring, and ties are kept.

These domain/switch gates and the single terminal value enclosure are
the checker's only mathematical tasks. The analytic derivative identities
and strict sign are proved above. The exact baseline/width minima are
imported, not independently re-proved by this checker.

## 6. Precise stationarity consequence and limits

For the CONTINUOUS two-parameter family here, the variables are
(u,epsilon); alpha and lambda stay fixed. At the interior point
(u0,epsilon_*),

```text
grad Delta C=(D_u/(4*pi),0), with D_u>0.               (20)
```

Thus the directional derivative in direction (-1,0) is negative.
For every sufficiently small h>0, the slab remains admissible and
C(mu_(u0-h,epsilon_*))<C(mu_(u0,epsilon_*)). This disproves local
minimality in the two-parameter family, and therefore also excludes
global minimization there. It supplies no location or existence theorem
for a joint minimizer elsewhere.

The width theorem also gives D_epsilon_epsilon(u0,epsilon_*)>77/160.
Smoothness and the implicit function theorem therefore give a unique
local smooth branch epsilon_loc(u), through epsilon_*, of strict local
width minima. Define V(u)=C(mu_(u,epsilon_loc(u))). Then
V'(u0)=D_u/(4*pi)>0, since the term D_epsilon*epsilon_loc'(u) vanishes
there. This local statement does
not assert that epsilon_loc(u) is a global width minimizer for other u,
or continue that branch to a parameter boundary. Re-optimizing width
locally cannot make the original point stationary in u.

Independent 70-digit diagnostics, recomputing the implicit baseline and
width roots, give D_u approximately 0.00007192229619488977356. This is
consistent with the user's falsifiable prediction 7.19222961949e-5.
The extra digits are numerical observations only; the proof and (3)
do not depend on them. The raw-full-max differences and the two derivative
formulas were compared separately, as recorded in the
[task evidence](../ops/TASK-20260906__second_block_start/EVIDENCE.md).

There is no finite permutation construction, R_full transfer, new
geometric/global bound or finite-limit/derivative interchange. The
existing recovery and full-root results at width 1/100 keep exactly
their original scope. Published arXiv-v1 assets, certificates and
production code are unchanged. The sole stable owner is
knowledge/FIXED_ORDER_THEORY.md; external independent review remains
separate from local proof/checker completion.
