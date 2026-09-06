# Second reflected block: positive start derivative on the chord-diagonal domain

```text
status=PROVED
classification=exact continuous theorem / proved boundary-infimum corollary
domain=alpha=alpha_hat; A=1+alpha_hat; lambda=A*x_*; lambda<u; 0<epsilon<A/3-u
result=D_u>0 throughout the domain, including the block-entry switch
boundary=continuous extension to u=lambda; joint infimum equals boundary infimum
boundary_width_optimization_and_finite_radius_transfer=outside this task
proved_on=2026-09-06
published_snapshot=arXiv v1 unchanged
```

## 1. Fixed inputs, full cost and exact statement

Keep the baseline measure mu_0 and exact minimizers from the
[joint prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md),
Section 1. Only its coarse exact brackets are needed:

```text
alpha=alpha_hat, A=1+alpha, lambda=A*x_*, a=A/3, b=1-alpha,
AL=1093/10000 < alpha < AH=10931/100000,
XL=719/2500 < x_* < XH=2877/10000 < 1/3.                 (1)
```

Thus 0<lambda<a<b. The minima and these brackets are imported, not
recomputed or replaced by rational midpoints. Neither alpha nor lambda
varies. This theorem extends the analytic start argument in the
[local start note](PERMUTED_HALVES_SECOND_BLOCK_START.md); it does not
use epsilon_*, width stationarity, the refined alpha bracket or a
numerical switch enclosure.

Use precisely the symmetric slab replacement in the
[second-block variation](PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md),
Sections 1-3. On I=[u,u+epsilon], replace the diagonal conditional atom
(A+t,A+t) by equal masses at (A+t,A+2*u+epsilon-t) and its high-coordinate
swap. Elsewhere keep mu_0. Write the result as mu_(u,epsilon), and retain

```text
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)),
C(mu)=(1/(4*pi))*integral g dmu,
D(u,epsilon)=4*pi*[C(mu_(u,epsilon))-C(mu_0)],
Omega={(u,epsilon): lambda<u, 0<epsilon<a-u},
Bdry={(lambda,epsilon): 0<epsilon<a-lambda}.             (2)
```

The low marginal, each uniform high marginal separately, and equality of
the two conditional high marginals are preserved by reflection and swap.
These are continuum measure identities. The boundary family in (2) is
defined rigorously in Section 5.

**Theorem.** D is C^1 on Omega, smooth inside each strict block regime,
and for every (u,epsilon) in Omega,

```text
D_u(u,epsilon) >= epsilon^3/[48*(A+u+epsilon)^2] > 0.    (3)
```

This includes the all-chord regime, the mixed regime, and the exact
entry tie at which the chain interval has zero length. D extends
continuously to

```text
K={(u,epsilon): lambda<=u<=a, 0<=epsilon<=a-u}.          (4)
```

At every positive-width point of Bdry the same derivative formula and
strict bound give its right u derivative. For fixed epsilon and
lambda<u<a-epsilon,

```text
D(lambda,epsilon)<D(u,epsilon),
inf_(Omega) D = inf_(0<epsilon<a-lambda) D(lambda,epsilon). (5)
```

No point of the open domain Omega minimizes D there. Equation (5) is
an equality of infima and strict dominance at fixed width. It does not
assert attainment, uniqueness or the width of a boundary minimum.
The identical statements hold for C after adding the fixed C(mu_0)
and dividing D by the positive constant 4*pi.

## 2. Exhaustive branch classification and every entry endpoint

Set s=t-u. For 0<=s<=epsilon put

```text
B=A+u, t=u+s, X=B+s, Y=B+epsilon-s,
c(s)=sqrt(X*Y), k(s)=sqrt(t)*(sqrt(X)+sqrt(Y)),
d(s)=max(X,2*sqrt(t*X)),
v(s)=k(s)/c(s)=sqrt(t/X)+sqrt(t/Y).                      (6)
```

The equal swapped costs cancel the factor 1/2 in the measure. The
unaltered prefix, other diagonal mass and wrapped tail cancel exactly:

```text
D=integral_0^epsilon [max(c(s),k(s))-d(s)] ds.           (7)
```

For every point of Omega, t<=u+epsilon<a, so 4*t<X and d(s)=X strictly
on the entire slab. This derives the chord-diagonal reduction from the
full max. At the upper edge epsilon=a-u the diagonal ties only at the
upper endpoint; the same integral reduction remains valid. It is not
valid throughout the larger pre-wrap domain beyond that edge.

Both summands of v strictly increase in s. Explicitly, with A and the
parameters fixed,

```text
v_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0,
v(0)<2*sqrt(u/(A+u))<1,
v(epsilon/2)=2*sqrt((u+epsilon/2)/(A+u+epsilon/2))<1.    (8)
```

Thus an all-chain regime or a switch at s=0 is impossible, and the
entire first half of every positive-width slab is strictly chord.

For each fixed 0<u<a write h(u)=a-u and

```text
F(u,e)=sqrt((u+e)/(A+u+e))+sqrt((u+e)/(A+u)).           (9)
```

F(u,0)<1 and F is strictly increasing in e. At e=h(u),
F=1/2+sqrt(a/(A+u))>1. The intermediate value theorem and strict
monotonicity give exactly one tau(u) in (0,h(u)), defined by the
UNSQUARED equation F(u,tau(u))=1. In particular neither endpoint e=0
nor e=h(u) is an entry tie. Define the clipped switch by

```text
z(u,epsilon)=epsilon,                      epsilon<=tau(u);
z(u,epsilon)=the unique root v(z)=1 in (0,epsilon),
                                           epsilon>tau(u).     (10)
```

Then z>epsilon/2 for every positive width, and

```text
D=integral_0^z c ds + integral_z^epsilon k ds
  -B*epsilon-epsilon^2/2.                              (11)
```

| Width | Reflected block | Removed diagonal |
|---|---|---|
| 0<epsilon<tau(u) | Strictly chord everywhere | Strictly chord |
| epsilon=tau(u) | Chord, with k=c only at s=epsilon | Strictly chord |
| tau(u)<epsilon<h(u) | Chord to z, chain after z | Strictly chord |
| epsilon=h(u)>0, continuous upper edge | Mixed, epsilon/2<z<epsilon | Chord, with a tie only at s=epsilon |
| epsilon=0, continuous lower edge | Empty interval | Empty interval |

Every row also applies at u=lambda where its width is admissible.
At (u,epsilon)=(a,0) only the empty row applies. The first-half argument
excludes a switch at the midpoint for any positive width in K. There
are no additional block/diagonal crossings in the stated domain.

## 3. Moving endpoints, clipped-switch regularity and C^1 matching

The following calculations hold more generally for A>0 and
0<u<u+epsilon<a, independently of the lower cutoff lambda. In the
mixed regime, evaluate t,X,Y at s=z and set

```text
N=A*(Y/X)^(3/2)+Y+t,
z_u=-[A*(Y/X)^(3/2)+Y-t]/N,
z_epsilon=t/N,
1+z_u=2*z_epsilon.                                    (12)
```

These follow by implicit differentiation of v(z)=1 using (8),
v_u=[A/X^(3/2)+(Y-t)/Y^(3/2)]/(2*sqrt(t)), and
v_epsilon=-sqrt(t)/(2*Y^(3/2)). Since
Y-t=A+epsilon-2*z>=A-epsilon>0, we have -1<z_u<0 and
0<z_epsilon<1/2. The physical switch xi=u+z has velocity 1+z_u.
In the all-chord regime the clipped switch is instead z=epsilon,
with z_u=0 and z_epsilon=1. One must not assign a common switch
derivative across the entry curve.

For completeness, F_e>0 and F_u>0 on 0<e<h(u). The second summand's
u derivative is (A-e)/(2*sqrt(u+e)*(A+u)^(3/2))>0; the first is also
positive. Thus tau is smooth and tau'(u)=-F_u/F_e<0. At its entry
curve the local unconstrained switch root is smooth, by v_s>0,
and tends to epsilon from the mixed side. The clipped z is continuous.

Hold epsilon fixed and use physical t, q=u+epsilon, xi=u+z:

```text
c_tilde(t,u)=sqrt((A+t)*(A+2*u+epsilon-t)),
k_tilde(t,u)=sqrt(t)*(sqrt(A+t)+sqrt(A+2*u+epsilon-t)),
c0=sqrt(B*(B+epsilon)),
p=sqrt(u+epsilon)*(sqrt(B+epsilon)+sqrt(B)),
P=max(c0,p),
I=integral_0^z sqrt((B+s)/(B+epsilon-s)) ds
  +integral_z^epsilon sqrt((u+s)/(B+epsilon-s)) ds.       (13)
```

In the mixed regime the complete physical Leibniz formula is

```text
D_u=[k_tilde(q,u)-(A+q)]-[c_tilde(u,u)-(A+u)]
    +[c_tilde(xi,u)-k_tilde(xi,u)]*(1+z_u)+I
   =P-c0-epsilon+I.                                   (14)
```

Both slab endpoints have velocity 1. The switch term vanishes by
equality of the COSTS at xi, not by a zero switch velocity or equality
of derivatives. The two diagonal endpoint terms sum to -epsilon.
In the all-chord regime, differentiate the single integral from u to q:
the upper reflected cost is c_tilde(q,u)=c0, so the same formula holds
with P=c0 and the second integral in I empty. At the entry tie p=c0,
the two formulas match exactly.

In translated coordinates both endpoints 0,epsilon are fixed under
u differentiation. Differentiating (11) within each strict regime gives

```text
D_u=integral_0^z (c_u-1) ds
    +integral_z^epsilon (k_u-1) ds
    +[c(z)-k(z)]*z_u.                                 (15)
```

The last term is zero in the mixed regime; in the all-chord regime
z_u=0, even when c(z)!=k(z). Translating (14) gives exactly (15),
since the integrated spatial derivatives provide both physical endpoint
terms. At the entry tie either one-sided formula has the same limit.
For the other partial derivative the analogous endpoint calculation is

```text
D_epsilon=P-(B+epsilon)+I/2.                          (16)
```

This formula is only a regularity identity here; no width equation is
solved. Both (14) and (16) are continuous at entry, where z=epsilon
and p=c0.

Here is a direct justification that these matching limits really are
partial derivatives at the entry curve. Substitute s=epsilon*r in (7),
with r in the fixed interval [0,1]. On any compact neighborhood with
u>0, epsilon>0 and u+epsilon<a, the positive radicands are bounded
away from zero, and the smooth branch values and their first partials
are uniformly bounded. The max is locally Lipschitz in the parameters,
with the corresponding uniform difference-quotient bound. At a fixed
parameter pair it has only one possible tie value of r, because v_s>0.
Thus the difference quotients converge for almost every r and are
dominated by an integrable constant. Differentiation under the integral
is valid even when the tie is at r=1. For parameter convergence the
active derivative converges at every r outside the limiting tie set;
the same domination proves continuity of both integrated derivatives.
This proves C^1 across every entry point. Smoothness holds in the two
strict regimes; global C^2 or smoothness of the clipped switch is not
assumed.

## 4. Exact strict sign, including the all-chord and entry-tie cases

For the translated derivatives in (15), all of t,X,Y have u derivative
1. Their integrands are exactly

```text
c_u-1=(X+Y)/(2*sqrt(X*Y))-1
     =(sqrt(X)-sqrt(Y))^2/(2*sqrt(X*Y))
     =(epsilon-2*s)^2/[2*sqrt(X*Y)*(sqrt(X)+sqrt(Y))^2]>=0,

k_u-1=[sqrt(X/t)+sqrt(t/X)+sqrt(Y/t)+sqrt(t/Y)]/2-1>1.  (17)
```

For the last inequality, each reciprocal pair is at least 2; the X
pair is strictly greater than 2 because X=A+t>t. All quantities are
positive before using this exact algebra. The chord integrand vanishes
only at s=epsilon/2.

By (8), [0,epsilon/2] lies entirely in the chord region, for every
positive width in the domain, whether the chain interval exists or not.
On this half interval X,Y<=B+epsilon. Consequently

```text
2*sqrt(X*Y)*(sqrt(X)+sqrt(Y))^2 <= 8*(B+epsilon)^2,
integral_0^(epsilon/2) (epsilon-2*s)^2 ds=epsilon^3/6.
```

All remaining contributions in (15) are nonnegative. These two
identities prove (3) directly. In particular entry at z=epsilon does
not destroy strictness: a positive-length chord interval already
supplies it. No switch root, quadrature, subdivision, finite scan,
stationarity equation or floating-point sign enters the proof.

There is no exception for positive epsilon in Omega. On the excluded
zero-width edge D(u,0)=0 identically and its u derivative is zero.
The bound (3) tends to zero with epsilon, so no uniform positive lower
bound independent of width is asserted. No start sign is claimed
outside the chord-diagonal domain.

## 5. Touching blocks, boundary continuity and exact infimum reduction

At u=lambda the two low intervals [0,lambda] and [lambda,lambda+epsilon]
touch at a single point; their high intervals [A,A+lambda] and
[A+lambda,A+lambda+epsilon] also touch at a single point. These points
have zero marginal mass. Assign either endpoint convention there.
The first prefix keeps its own reflection t->lambda-t; the second
uses t->2*lambda+epsilon-t on its own interval. They remain two
distinct reflections, not a reflection of the combined interval.

For either second-block high coordinate, the identity

```text
(1/2)*integral_lambda^(lambda+epsilon)
  [phi(A+t)+phi(A+2*lambda+epsilon-t)] dt
=integral_lambda^(lambda+epsilon) phi(A+t) dt           (18)
```

preserves its marginal, exactly as for u>lambda. Swap preserves
conditional high-marginal equality, and the low marginal is unchanged.
The baseline is diagonal almost everywhere on this second interval.
Thus this is a well-defined probability coupling with cost (7), even
at contact with the prefix. The positive gap a<b keeps the entire
closed triangle K pre-wrap.

For any continuous test f on the compact coordinate box, the measure
difference is

```text
(epsilon/2)*integral_0^1 [
 f(u+epsilon*r,A+u+epsilon*r,A+u+epsilon*(1-r))
+f(u+epsilon*r,A+u+epsilon*(1-r),A+u+epsilon*r)
-2*f(u+epsilon*r,A+u+epsilon*r,A+u+epsilon*r)] dr.        (19)
```

The integrand is continuous and uniformly bounded on K times [0,1].
This proves weak continuity of the actual couplings, including u=lambda,
epsilon=0 and epsilon=a-u. Taking f=g gives continuity of D on K;
D(u,0)=0. No total-variation convergence under start motion is needed
or asserted. For positive width the switch formulas and derivative
integrals also have continuous limits from the interior up to K;
at the top edge the sole diagonal tie has zero integration mass.

At each point of Bdry, lambda>0 and lambda+epsilon<a. The C^1 scalar
integral proof of Section 3 applies on an open neighborhood in the
larger mathematical domain 0<u<u+epsilon<a. Therefore its derivative
at u=lambda equals the actual right derivative of the boundary family
and satisfies (3). Extending this scalar expression left of lambda is
only a regularity argument; it does not replace overlapping baseline
mass or define an admissible two-block coupling there.

Fix 0<epsilon<a-lambda. For lambda<=v<u<a-epsilon, the fundamental
theorem of calculus and (3) give

```text
D(u,epsilon)-D(v,epsilon)
 >= (epsilon^3/48)*[1/(A+v+epsilon)-1/(A+u+epsilon)]>0.  (20)
```

In particular taking v=lambda proves strict boundary dominance. Since
every interior pair has an admissible boundary pair at the SAME width,
inf_Bdry D<=inf_Omega D. Conversely for any fixed boundary width choose

```text
u_j=lambda+(a-lambda-epsilon)/(j+1), j=1,2,... .        (21)
```

These starts lie in Omega and tend to lambda. Continuity implies
inf_Omega D<=D(lambda,epsilon). Taking the infimum over all those
widths proves the reverse inequality and hence (5). Both infima are
finite by continuity on K. Every interior point can also move strictly
left within Omega and lower its cost, so none is a local minimum there.

This finishes the reduction of the joint infimum on the requested
subdomain to the one-parameter boundary family. The open width endpoints
are retained in (5). No claim locates a minimizing width, proves its
attainment in that open interval, or continues the old epsilon_* branch.

## 6. Verification, ownership and scope

The sign and regularity proof is analytic and holds for every A>0 and
0<u<u+epsilon<A/3. Specialization to the exact baseline requires only
the rational ordering in (1). The
[minimal stdlib checker](../ops/TASK-20260906__second_block_start_domain/check_domain.py)
audits those imported bracket orderings and the positive margins
lambda>0, a-lambda>0 and b-a>0. There are no irreducible radical sign
or root-enclosure gates in this extension. The checker does not prove
the imported minima, substitute rational parameters for them, or
sample the continuum sign. The prior local value gate and complete
width theorem are unnecessary for the new proof.

Separate bounded raw-full-max diagnostics and exact commands are in the
[task evidence](../ops/TASK-20260906__second_block_start_domain/EVIDENCE.md).
They test the derivations and switch limits without serving as proof
premises. The sole stable owner is knowledge/FIXED_ORDER_THEORY.md;
independent external mathematical review remains separate.

This is a theorem about continuous couplings and their cost. No finite
permutation is constructed, no R_full limit or R*(n) bound is deduced,
and no boundary width is optimized. Earlier fixed-width recovery and
full-root results retain their original scopes. Existing proof notes,
published arXiv-v1 assets, certificates and production code are unchanged.
