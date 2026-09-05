# A second disjoint reflected block: exact continuum variation

```text
status=PROVED
classification=exact continuum theorem / counterexample to balanced-coupling local minimality
domain=alpha_hat and lambda_hat fixed; lambda_hat<u<1-alpha_hat; epsilon down to zero at fixed u
width_first_derivative=zero everywhere; first nonzero term cubic negative except at the diagonal switch
finite_permutation_recovery=not established in this task
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Baseline, question and theorem

Use exactly the baseline minimizers and coupling from
[the joint reflected-prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md),
Sections 1, 3-6. Put

```text
alpha=alpha_hat, A=1+alpha, lambda=lambda_hat=A*x_*,
a=A/3, b=1-alpha,
AL=1093/10000<alpha<AH=10931/100000,
XL=719/2500<x_*<XH=2877/10000<1/3.                       (1)
```

These are imported exact brackets, not decimal definitions or newly
computed minima. In particular 0<lambda<a<b: the first inequality
lambda<a follows from x_*<1/3, and b-a=(2-4*alpha)/3>0.
Write mu_0 for the baseline coupling, and retain the full symmetric cost
and its continuum coefficient

```text
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)),
C(mu)=(1/(4*pi))*integral g dmu,   C(mu_0)=C_hat.        (2)
```

The normalization and necessary local balance are those of
[the three-marginal theorem](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Sections 3-4. The baseline is diagonal at (t,A+t,A+t) on (lambda,b).
Only this diagonal part will change; the first reflected prefix and the
wrapped tail are fixed.

**Theorem.** For every fixed u in the strictly disjoint pre-wrap domain

```text
U=(lambda,b),  0<epsilon<b-u,                           (3)
```

define the symmetric reflection on I=[u,u+epsilon] in Section 2 and let
Delta C(u,epsilon)=C(mu_(u,epsilon))-C_hat. It preserves the uniform low
marginal, each uniform high marginal separately, and the equality of
the two conditional high marginals. Its ordinary width first variation is

```text
V_1(u)=lim_(epsilon down to 0) Delta C(u,epsilon)/epsilon=0
for EVERY u in U.                                      (4)
```

The first nonzero terms of the FULL cost are

```text
Delta C(u,epsilon)
 =-epsilon^3/(96*pi*(A+u))+o(epsilon^3),      lambda<u<a;
 =+epsilon^2/(256*pi)+O(epsilon^3/a),         u=a;
 =-epsilon^3/(96*pi*sqrt(u*(A+u)))
    +o(epsilon^3),                          a<u<b.     (5)
```

Thus no u has a negative ordinary first derivative. Nevertheless every
fixed u except a strictly decreases the cost for all sufficiently small
positive widths, while u=a strictly increases it. Equality in (4) holds
for all u. The quadratic scaled limit is zero exactly for u!=a; at a
it is 1/(256*pi)>0. On each of the two remaining intervals the cubic
scaled limit in (5) is strictly negative and has no zero. At epsilon=0
the coupling and cost equal the baseline. These are all equality cases
for the stated local variation; arbitrary larger widths are not classified.

In particular the fixed rational block

```text
u_0=1/3, epsilon_0=1/100
```

is strictly admissible and gives the exact continuum counterexample

```text
C(mu_(u_0,epsilon_0)) < C_hat-1/(144000000*pi).          (6)
```

This disproves local minimality of mu_0 among balanced continuum couplings.
It does not contradict the baseline's unique minimum within its original
one-prefix family. No new finite-order or geometric upper bound follows
here: no recovery of this second block is supplied.

## 2. The specified perturbation and exact marginals

For t in I let R_I(t)=2*u+epsilon-t. Replace the diagonal conditional
atom by

```text
(1/2)*delta_(A+t,A+R_I(t))
 +(1/2)*delta_(A+R_I(t),A+t).                           (7)
```

Outside I keep mu_0 exactly. More explicitly, for any continuous test f,

```text
integral f dmu_(u,epsilon) - integral f dmu_0
 =(1/2)*integral_I [f(t,A+t,A+R_I(t))
                   +f(t,A+R_I(t),A+t)
                   -2*f(t,A+t,A+t)] dt.               (8)
```

This is replacement of a positive slab of mass epsilon, so the result is
a probability measure, with the same low marginal. The two high values
lie in A+I subset (A+lambda,2), disjoint from the first block's high range.
Reflection is an involution preserving Lebesgue measure on I. Therefore,
for any continuous phi, either new high marginal on that slab integrates

```text
(1/2)*integral_I [phi(A+t)+phi(A+R_I(t))] dt
 =integral_I phi(A+t) dt.                              (9)
```

Both full high marginals remain uniform on [1,2], separately. At every
t in I their conditional distributions are identical by the swap in (7).
Outside I they already agree. Consequently for every continuous f(t,x),
integral[f(t,x)-f(t,y)] dmu_(u,epsilon)=0: local balance is exact, although
the individual (t,x) marginal need not remain equal to the baseline's.

Equation (8) also gives |integral f d(mu_(u,epsilon)-mu_0)|<=2*epsilon
when ||f||_infinity<=1. The strictly cheaper couplings with u=u_0 and
epsilon down to zero thus approach mu_0 even in total variation.
These measure facts do not assert permutation realizability.

## 3. Exact full-max formula, including every switch

Write s=t-u, B=A+u, and for 0<=s<=epsilon define

```text
c_e(s)=sqrt((B+s)*(B+epsilon-s)),
k_e(s)=sqrt(u+s)*(sqrt(B+s)+sqrt(B+epsilon-s)),
d(s)=max(B+s,2*sqrt((u+s)*(B+s))),
v_e(s)=sqrt((u+s)/(B+s))+sqrt((u+s)/(B+epsilon-s)).
```

The high-high chord is c_e and the low-high chain sum is k_e. Symmetry
of g cancels the factor 1/2 in (8), giving the exact difference

```text
4*pi*Delta C=integral_0^epsilon [max(c_e(s),k_e(s))-d(s)] ds.
                                                               (10)
```

Both summands of v_e strictly increase in s: the derivatives of their
squares are A/(B+s)^2>0 and (B+epsilon+u)/(B+epsilon-s)^2>0. Since c_e>0,
k_e/c_e=v_e, so the chord wins precisely when v_e<=1. Set

```text
z_e=epsilon,  if v_e(epsilon)<=1;
z_e=0,        if v_e(0)>=1;
z_e=the unique unsquared root v_e(z_e)=1 otherwise;
w_e=min(epsilon,max(0,a-u)).
```

Endpoint ties have zero-length intervals. The diagonal chord wins
precisely for s<=a-u, by 4*(u+s)<=B+s. Hence (10) is exactly

```text
 integral_0^z_e c_e(s) ds + integral_z_e^epsilon k_e(s) ds
 -integral_0^w_e (B+s) ds
 -2*integral_w_e^epsilon sqrt((u+s)*(B+s)) ds.           (11)
```

This formula applies to every admissible positive width, including a
mixed reflected block, a mixed diagonal slab and all endpoint ties.
No branch is dropped, and no squared equation selects a spurious root.
The unchanged prefix, its own switch and the wrapped tail cancel exactly.

## 4. Chord regime: exact negative identity and cubic term

Fix lambda<u<a. For

```text
0<epsilon<min(b-u,(A-3*u)/4),                           (12)
```

both perturbed high values are >=B and u+s<=u+epsilon. Thus
v_e(s)<=2*sqrt((u+epsilon)/B)<1 by the positive rational gate
4*(u+epsilon)<B. The entire perturbed block is chord. This same width
is smaller than a-u=(A-3*u)/3, so the diagonal slab is chord too.

Center the interval with z=s-epsilon/2 and M=B+epsilon/2. The linear
diagonal integrates to epsilon*M, and rationalization yields

```text
4*pi*Delta C
 =-integral_(-epsilon/2)^(epsilon/2)
       z^2/[M+sqrt(M^2-z^2)] dz <0.                    (13)
```

The radicand is >=B*(B+epsilon)>0. The denominator lies between 2*B
and 2*M, and integral z^2 dz=epsilon^3/12. Consequently

```text
-epsilon^3/(24*B) <= 4*pi*Delta C
                  <=-epsilon^3/(24*M)<0.              (14)
```

Dividing by epsilon^3 and letting epsilon decrease to zero proves the
first line of (5), without numerical integration. Strictness follows
because z^2>0 except at one point in a positive-length interval.

## 5. Chain regime: exact rearrangement identity and cubic term

Fix a<u<b. For

```text
0<epsilon<min(b-u,3*u-A),                              (15)
```

both high values are <=B+epsilon and u+s>=u. Hence
v_e(s)>=2*sqrt(u/(B+epsilon))>1, because 4*u>B+epsilon.
The diagonal is also entirely chain. Put f(s)=sqrt(u+s), h(s)=sqrt(B+s).
The exact chain difference I_e is

```text
I_e=integral_0^epsilon f(s)*[h(epsilon-s)-h(s)] ds
 =-(1/2)*integral_0^epsilon
       [f(s)-f(epsilon-s)]*[h(s)-h(epsilon-s)] ds
 =-(1/2)*integral_0^epsilon (2*s-epsilon)^2 /
       [(sqrt(u+s)+sqrt(u+epsilon-s))
        *(sqrt(B+s)+sqrt(B+epsilon-s))] ds <0.          (16)
```

The middle equality uses the substitution s->epsilon-s in the same
integral. Both functions strictly increase, and all denominators are
positive. Formula (16) is valid as an identity for the chain difference
even when the full max uses another branch. In the present regime
4*pi*Delta C=I_e. Since integral(2*s-epsilon)^2 ds=epsilon^3/3,

```text
-epsilon^3/(24*sqrt(u*B)) <= I_e
 <=-epsilon^3/(24*sqrt((u+epsilon)*(B+epsilon)))<0.       (17)
```

The bounds follow by bounding each sum of square roots between twice
its smallest and largest endpoint roots. They prove the third line
of (5) and strict cost decrease for every width in (15).

## 6. The diagonal switch: positive quadratic term and explicit remainder

At u=a one has B=4*a. The diagonal is chain for s>0, with a tie at s=0.
The reflected block is mixed for EVERY positive admissible width:

```text
v_e(0)=1/2+sqrt(a/(4*a+epsilon))<1,
v_e(epsilon)=sqrt((a+epsilon)/(4*a+epsilon))
              +sqrt((a+epsilon)/(4*a))>1.
```

Retaining that chord interval, with [q]_+=max(q,0), gives

```text
4*pi*Delta C(a,epsilon)=I_e+integral_0^epsilon [c_e(s)-k_e(s)]_+ ds.
                                                               (18)
```

Use r=s/epsilon in [0,1] and delta=epsilon/a. The two scaled costs are

```text
C(delta,r)=c_e(epsilon*r)/a
          =sqrt(4+delta*r)*sqrt(4+delta*(1-r)),
K(delta,r)=k_e(epsilon*r)/a
          =sqrt(1+delta*r)
             *(sqrt(4+delta*r)+sqrt(4+delta*(1-r))).
```

At delta=0 their values are both 4 and their first derivatives are
1/2 and 2*r+1/4 respectively. Thus uniformly in r,

```text
c_e(epsilon*r)-k_e(epsilon*r)
 =epsilon*(1/4-2*r)+O(epsilon^2/a).                    (19)
```

In particular z_e/epsilon->1/8. The positive-part function is
1-Lipschitz, so the new chord contribution has leading term

```text
epsilon^2*integral_0^1 [1/4-2*r]_+ dr
 =epsilon^2*integral_0^(1/8) (1/4-2*r) dr
 =epsilon^2/64.                                       (20)
```

The chain saving I_e is O(epsilon^3/a) by (17), which proves the
middle line of (5). Keeping only the chain branch would incorrectly
predict a decrease at this point.

Here is an explicit analytic error bound, so the positive sign need
not rely on an unquantified remainder. For 0<=delta<=1 the high roots
lie in [2,sqrt(5)] subset [2,3], and the low root in [1,sqrt(2)] subset
[1,2]. Differentiating products twice, with respect to delta, gives

```text
|C''| <= (3/32)*(r^2+(1-r)^2)+r*(1-r)/8 <=1/8,
|K''| <= (3/2)*r^2+r/4+(r^2+(1-r)^2)/16 <=29/16.
```

Thus |(C-K)''|<=31/16<2. Taylor's theorem with its integral remainder
proves that the absolute error in (19) is <=epsilon^2/a. Apply the
positive-part Lipschitz bound and (17), whose denominator here has
sqrt(u*B)=2*a, to obtain

```text
|4*pi*Delta C(a,epsilon)-epsilon^2/64|
 <=(49/48)*epsilon^3/a,  0<epsilon<=a, epsilon<b-a.     (21)
```

For the completely explicit interval

```text
0<epsilon<=min(a/128,(b-a)/2),
```

the rational gate 1/64-49/(48*128)=47/6144>0 yields

```text
Delta C(a,epsilon)>=47*epsilon^2/(24576*pi)>0.          (22)
```

Equations (14), (17) and (21) also directly prove (4), with the
quadratic/cubic equality cases stated in Section 1.

## 7. One exact rational counterexample, without optimization

Choose only u_0=1/3 and 0<epsilon<=epsilon_0=1/100. The imported brackets
give the following strictly rational gates:

```text
lambda < (1+AH)*XH < 1/3=u_0,
u_0+epsilon_0 < 1-AH < b,
4*epsilon_0 < AL < alpha=A-3*u_0,
A+u_0+epsilon/2 < (1+AH)+1/3+1/200 < 3/2.              (23)
```

They establish disjointness, the strict pre-wrap margin, the all-chord
condition (12), and M<3/2, respectively. All squarings used in (12)
have nonnegative sides. Equation (14), divided by 4*pi, now proves

```text
Delta C(u_0,epsilon)
 <=-epsilon^3/(96*pi*M)<-epsilon^3/(144*pi)<0.           (24)
```

Taking epsilon=1/100 gives (6). No floating approximation to alpha_hat
or x_*, quadrature, parameter scan, or stationary-point search enters
this witness. The width first derivative is still zero: the improvement
is cubic. For a fixed such width, linear interpolation of measures
(1-eta)*mu_0+eta*mu_(u_0,epsilon) is also balanced and has strictly
negative derivative Delta C(u_0,epsilon) with respect to eta. This is
a different derivative from shrinking the interval in (4).

## 8. Quantifiers, evidence and limits

The new theorem concerns the continuum functional (2), at the fixed exact
baseline and fixed u. The explicit ranges (12), (15), (22) resolve the
sign for every fixed u in U. They shrink as u approaches a or the wrap;
no uniform expansion is asserted for moving u=u(epsilon), an interval
crossing the wrap, touching/overlapping the first block, or arbitrary
larger widths. The endpoints u=lambda and u=b are excluded by (3);
u=b admits no positive pre-wrap width. No parameter family is optimized.

The previous recovery theorem realizes one reflected PREFIX. It is not
a recovery theorem for (7). Exact high marginals and local balance alone
are necessary conditions and have not been proved sufficient here. No
permutation sequence, finite floor/seam analysis or all-pairs placements
for the second block are constructed in this task. Consequently (6)
is a strict continuum cost bound only; it does not improve the recorded
bound limsup R*(n)/n^2<=C_hat, prove any finite-m improvement, or identify
a continuum/permutation/geometric global optimum. No limits in m and
epsilon are interchanged.

The [bounded exact checker](../ops/TASK-20260905__second_reflected_block/check_second_block.py)
audits rational gates, sign-safe radical comparison including ties,
reflection moments, independent formal Taylor algebra, and the switch
remainder constants using stdlib integers/Fraction only. An independent
eight-panel midpoint upper enclosure also checks the raw witness cost
with rational square-root bounds. This is rigorous because the chord
c_e is concave. It suffices to check A=1+AH: for fixed epsilon, (13)
increases with B, since its denominator increases with M. It does not
re-prove the imported minima, replace the analytic arguments, use a
numerical diagnostic as sign evidence, or import production/checker code.
[Task evidence](../ops/TASK-20260905__second_reflected_block/EVIDENCE.md)
records commands and provenance. The sole thematic owner of this
continuum result is knowledge/FIXED_ORDER_THEORY.md. Global claims,
finite certificates, production code and historical paper assets are
unchanged. Independent external review remains separate.
