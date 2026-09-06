# Second reflected block: complete continuous width minimum

```text
status=PROVED
classification=exact continuous theorem with rational interval gates
domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; u=1/3; 0<epsilon<1-alpha_hat-u
minimizer_bracket=31248/10^6<epsilon_*<1/32
finite_recovery_and_radius_transfer=outside this task
proved_on=2026-09-06
published_snapshot=arXiv v1 unchanged
```

## 1. Exact inputs, functional and theorem

Keep precisely the baseline from the
[joint reflected-prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md).
The meanings and uniqueness of x_* and alpha_hat are imported from the
[lambda theorem](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md), Sections 2-7,
and the [alpha theorem](PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md),
Sections 1, 3-4. Neither parameter is re-optimized here. Write

```text
alpha=alpha_hat, A=1+alpha, lambda=A*x_*, u=1/3,
B=A+u, a=A/3, b=1-alpha,
h=a-u=alpha/3, L=b-u=2/3-alpha,
AL=1093/10000<alpha<AH=10931/100000,
719/2500<x_*<2877/10000.                                (1)
```

In particular lambda<(1+AH)*2877/10000<u<a<b. The new family is exactly
the reflection of the diagonal slab I=[u,u+epsilon] in
[the second-block variation note](PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md),
Sections 1-3, for every 0<epsilon<L. On I replace the atom at
(A+t,A+t) by equal masses at (A+t,A+2*u+epsilon-t) and its swap;
elsewhere keep the baseline measure mu_0. Call the result mu_epsilon.
Reflection preserves both uniform high marginals separately; the swap
preserves equality of the two conditional high marginals. The uniform
low marginal is unchanged. These are measure identities, not a recovery
criterion for finite permutations.

Retain the full symmetric cost and its normalization:

```text
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)),
C(mu)=(1/(4*pi))*integral g dmu,
Delta C(epsilon)=C(mu_epsilon)-C(mu_0), C(mu_0)=C_hat,
D(epsilon)=4*pi*Delta C(epsilon), Psi(epsilon)=D'(epsilon). (2)
```

The symbol D in this note means the scaled width difference (2). The
imported shift derivative K' is denoted D_shift below to avoid ambiguity.

**Theorem (continuous, fixed-baseline width family).** D extends
continuously to [0,L], is C^1 there with one-sided endpoint derivatives,
and has exactly two stationary points in (0,L):

```text
31248/10^6 < epsilon_* < 1/32,
1/3 < epsilon_dagger < 2/5 < L.                         (3)
```

It decreases strictly on (0,epsilon_*), increases strictly on
(epsilon_*,epsilon_dagger), and decreases strictly on
(epsilon_dagger,L). The first point is the unique GLOBAL minimum on
(0,L), and also on the continuous extension [0,L]. The second is a
strict local maximum. Thus increase everywhere to the right of the
minimum is false.

Moreover D(0)=0, D(epsilon_*)<0, D(h)>0 and D(L)>0. There is exactly
one positive-width zero epsilon_0, with

```text
epsilon_*<epsilon_0<h,
Delta C(epsilon)<0 for 0<epsilon<epsilon_0,
Delta C(epsilon)>0 for epsilon_0<epsilon<L.              (4)
```

The equality cases are exactly epsilon=0 and epsilon=epsilon_0 for the
cost difference, and the two points (3) for its derivative in (0,L).
The unique minimum statement is only within this one-dimensional
continuous family. No new R_full or global geometric bound is deduced.

## 2. Every block/diagonal branch, including their crossing

For 0<=s<=epsilon put

```text
c(s,epsilon)=sqrt((B+s)*(B+epsilon-s)),
k(s,epsilon)=sqrt(u+s)*(sqrt(B+s)+sqrt(B+epsilon-s)),
d(s)=max(B+s,2*sqrt((u+s)*(B+s))),
v(s,epsilon)=sqrt((u+s)/(B+s))+sqrt((u+s)/(B+epsilon-s)). (5)
```

The ratio k/c equals v. For fixed epsilon, v strictly increases in s:
the derivatives of the squared summands are A/(B+s)^2 and
(B+epsilon+u)/(B+epsilon-s)^2, both positive. At s=0,
v(0,epsilon)<2*sqrt(u/B)<1 since B>4*u. Hence a wholly chain block
never occurs at any admissible width.

The endpoint v(epsilon,epsilon) strictly increases with epsilon. Its
value at zero is less than 1, and at epsilon=h its first summand is
1/2 while its second is sqrt(a/B)>1/2, since B<4*a. Thus there is
exactly one block-entry width tau in (0,h), defined without squaring by

```text
sqrt((u+tau)/(B+tau))+sqrt((u+tau)/B)=1.                 (6)
```

Set z(epsilon)=epsilon for epsilon<=tau. Otherwise z is the unique
unsquared root v(z,epsilon)=1 in (0,epsilon). The block uses chord on
[0,z] and chain on [z,epsilon]. The removed diagonal uses chord up to
s=h and chain afterwards. Set w(epsilon)=min(epsilon,h). The exact
complete formula, including all endpoint ties, is

```text
D(epsilon)
 = integral_0^z c(s,epsilon) ds
   +integral_z^epsilon k(s,epsilon) ds
   -B*w-w^2/2
   -2*integral_w^epsilon sqrt((u+s)*(B+s)) ds.           (7)
```

It follows directly from the symmetric cost: the two half-weighted
high-coordinate swaps have the same g. The fixed prefix, its switch,
the rest of the diagonal and the wrapped tail cancel exactly.

There is also a spatial crossing of the two switches at epsilon=2*h.
Indeed, for epsilon>=h,

```text
v(h,epsilon)=1/2+sqrt(a/(4*a+epsilon-2*h)).              (8)
```

Thus z<h when h<epsilon<2*h, z=h at 2*h, and z>h after it. The
following table specifies every open spatial interval; a label pair
means (reflected block, removed diagonal).

| Width | Intervals and active branches |
|---|---|
| 0<epsilon<=tau | (0,epsilon): (chord,chord) |
| tau<epsilon<=h | (0,z): (chord,chord); (z,epsilon): (chain,chord) |
| h<epsilon<2*h | (0,z): (chord,chord); (z,h): (chain,chord); (h,epsilon): (chain,chain) |
| epsilon=2*h | (0,h): (chord,chord); (h,epsilon): (chain,chain) |
| 2*h<epsilon<L | (0,h): (chord,chord); (h,z): (chord,chain); (z,epsilon): (chain,chain) |

All costs agree at their own tie points, which have zero integral mass.
The rational gates below give tau<h<2*h<L. The crossing at 2*h changes
this spatial ordering but creates no additional piece in the analytic
formula (7), nor any new loss of differentiability.

For a closed expression without quadrature define

```text
F(t,c)=[(2*t+c)*sqrt(t*(t+c))
        -c^2*log((sqrt(t)+sqrt(t+c))/sqrt(c))]/4,
J(v,R)=[v*sqrt(R^2-v^2)+R^2*atan(v/sqrt(R^2-v^2))]/2,
M=B+epsilon/2, T=B+u+epsilon.
```

Here partial_t F=sqrt(t*(t+c)) and partial_v J=sqrt(R^2-v^2);
atan is the principal real branch. All arguments below have positive
radicands and positive logarithm arguments. Formula (7) becomes

```text
D(epsilon)
 = J(z-epsilon/2,M)-J(-epsilon/2,M)
   +F(u+epsilon,A)-F(u+z,A)
   +J(u+epsilon-T/2,T/2)-J(u+z-T/2,T/2)
   -B*w-w^2/2-2*[F(u+epsilon,A)-F(u+w,A)].              (9)
```

An interval of zero length contributes zero. This also gives the
continuous endpoint values at 0 and L. At L this is the left-limit
extension of the integral, not a construction crossing the high wrap.

## 3. Complete first variation and switch regularity

In the all-chord regime,

```text
Psi(epsilon)=sqrt(B*(B+epsilon))
 +(B+epsilon/2)*asin(epsilon/(2*B+epsilon))-(B+epsilon).
                                                               (10)
```

For epsilon>tau put

```text
I1=integral_0^z sqrt((B+s)/(B+epsilon-s)) ds,
I2=integral_z^epsilon sqrt((u+s)/(B+epsilon-s)) ds,
p(epsilon)=sqrt(u+epsilon)*(sqrt(B+epsilon)+sqrt(B)).
```

Then

```text
Psi(epsilon)=p(epsilon)-d(epsilon)+(I1+I2)/2.            (11)
```

The moving z terms cancel when differentiating (7), because c(z)=k(z).
At tau the emerging chain interval has zero length and the endpoint
costs agree. At h the two diagonal costs agree. Thus (10)-(11) join
continuously, proving the C^1 assertion for D. D is real analytic on
each of (0,tau), (tau,h) and (h,L); second derivatives need not agree
at tau or h. In particular curvature must not be extrapolated across h.

For exact evaluation use

```text
H(c,t)=c*atan(sqrt(t/(c-t)))-sqrt(t*(c-t)),
I1=H(2*B+epsilon,B+z)-H(2*B+epsilon,B),
I2=H(B+u+epsilon,u+epsilon)-H(B+u+epsilon,u+z).           (12)
```

The derivative of H with respect to t is sqrt(t/(c-t)). Root selection
retains the unsquared relation v=1; every squared sign comparison in
the checker retains its preceding positivity gate.

For later differentiation write t=u+z, y=B+epsilon-z and
r=sqrt(t/(A+t)). The switch relation gives sqrt(t/y)=1-r. Implicit
differentiation and substitution of t=A*r^2/(1-r^2) give

```text
z'=t/[A*(y/(A+t))^(3/2)+A+2*u+epsilon]
   =(1-r)^2/(2-r+2*r^2),  0<z'<1,
d z'/dr=-3*(1-r^2)/(2-r+2*r^2)^2<0.                    (13)
```

In particular z increases, r increases, and z' decreases. For the
interval checker only, the switch also increases separately with A:
v decreases with A and with epsilon at fixed s. Together with the
clipped all-chord part this justifies rectangular endpoint enclosures
of z; it does not vary the fixed design parameter in the theorem.

## 4. Strict decrease followed by one minimum before h

Let

```text
phi(x)=sqrt(1+x)+(1+x/2)*asin(x/(2+x))-(1+x).
```

Equation (10) is Psi(epsilon)=B*phi(epsilon/B). Direct differentiation
gives phi(0)=phi'(0)=0 and

```text
phi''(x)=-1/[2*(2+x)*(1+x)^(3/2)]<0.
```

Hence Psi<0 for 0<epsilon<=tau. In particular D(tau)<D(0)=0.
The earlier local identity is retained:

```text
Delta C(epsilon)=-epsilon^3/(96*pi*B)+o(epsilon^3).
```

On the mixed block define the positive quantities

```text
J1=integral_0^z sqrt(B+s)/(B+epsilon-s)^(3/2) ds
   +integral_z^epsilon sqrt(u+s)/(B+epsilon-s)^(3/2) ds,
Q1=z'*(sqrt(B+z)-sqrt(u+z))/(2*sqrt(y)).
```

Differentiating (11), including its moving boundary, yields

```text
Psi'=p'-d'+sqrt((u+epsilon)/B)/2-J1/4+Q1.               (14)
```

For tau<epsilon<h put q=u+epsilon<a. Since A>0 and q<B,

```text
p'=(A+2*q)/(2*sqrt(q*(A+q)))+sqrt(B)/(2*sqrt(q))>3/2.
```

The first term exceeds 1 by the positive square difference A^2; the
second exceeds 1/2. Also d'=1, B>1, epsilon<h<1/20 and
B+epsilon<B+h=4*A/3<3/2, so

```text
0<J1<=epsilon*sqrt(B+epsilon)/B^(3/2)<3/40,
Psi'>1/2-3/160=77/160>0.                               (15)
```

Section 7 proves, with outward rational arithmetic,

```text
tau < EL=31248/10^6 < EH=1/32 < h,
Psi(EL)<0<Psi(EH).                                    (16)
```

The intermediate value theorem and (15) give exactly one zero
epsilon_* in (tau,h), located as in (3). Together with the all-chord
sign, Psi is strictly negative before epsilon_* and strictly positive
from epsilon_* through h. D(epsilon_*)<0 follows without quadrature.

## 5. The whole tail: strict concavity of Psi, not of D

For h<epsilon<L the diagonal endpoint is chain. Set q=u+epsilon and

```text
M1(q)=(A+2*q)/(2*sqrt(q*(A+q)))
      -(B+q)/(2*sqrt(B*q)).
```

Equation (14) simplifies exactly to

```text
Psi'=-M1(q)-J1/4+Q1.                                  (17)
```

We prove that EACH of these three contributions strictly decreases
with epsilon on the entire tail. No mesh of sampled curvatures is used.

First,

```text
M1'(q)=[(B-q)/sqrt(B)-A^2/(A+q)^(3/2)]/(4*q^(3/2)).    (18)
```

For a<=q<=b, B-q>0. The function
W(q)=(B-q)*(A+q)^(3/2) has derivative
sqrt(A+q)*(3*B-2*A-5*q)/2. Its only possible turning point is a
maximum, so its minimum on [a,b] is at an endpoint. The two exact
square gates

```text
(B-a)^2*(A+a)^3>A^4*B,
(B-b)^2*(A+b)^3=8*(B-b)^2>A^4*B                       (19)
```

are proved for the whole coarse alpha interval in (1) by Section 7.
Both unsquared sides are positive. Thus W>A^2*sqrt(B) throughout
[a,b], proving M1'>0 in (18).

Next, J1'>0. With

```text
J2=integral_0^z sqrt(B+s)/(B+epsilon-s)^(5/2) ds
   +integral_z^epsilon sqrt(u+s)/(B+epsilon-s)^(5/2) ds,
```

the retained moving-boundary formula is

```text
J1'=sqrt(q)/B^(3/2)-(3/2)*J2
     +z'*(sqrt(B+z)-sqrt(u+z))/y^(3/2),
J2<=epsilon*sqrt(B+epsilon)/B^(5/2).                   (20)
```

All terms in the last boundary contribution are positive. It suffices
that 4*B^2*q>9*epsilon^2*(B+epsilon), with positive sides before
squaring. The function epsilon^2*(B+epsilon)/(u+epsilon) increases:
epsilon^2/(u+epsilon) has derivative
epsilon*(2*u+epsilon)/(u+epsilon)^2>0. At epsilon=L, q=b and
B+L=2. Thus the single exact gate

```text
4*B^2*b>18*L^2                                       (21)
```

proves J1'>0 on the entire tail (indeed wherever the block is mixed).

Finally Q1 strictly decreases. Formula (13) makes z' strictly decrease.
The positive factor sqrt(A+t)-sqrt(t) strictly decreases with t=u+z,
and sqrt(y) strictly increases since y'=1-z'>0. The product/quotient
of these positive factors has strictly negative derivative.

Equations (17)-(21) prove

```text
Psi''<0 for every h<epsilon<L.                         (22)
```

This is strict concavity of the FIRST derivative Psi=D'. It does not
assert D''<0 throughout this interval.
The finite gates in Section 7 give

```text
Psi(1/3)>0>Psi(2/5),  h<1/3<2/5<L.                    (23)
```

Since Psi(h)>0 by Section 4, a strictly concave Psi has exactly one
tail zero epsilon_dagger, with the bracket (3). Explicitly, before
that zero strict concavity places Psi above the chord from h to the
zero; after it the secant slope from h is negative and concavity
forces Psi to stay negative. This proves all derivative signs claimed
in Section 1, including the final strict descent.

## 6. Global comparison and every sign of the cost

The two critical full-max evaluations in Section 7 prove

```text
D(h)>0, D(L)>0.                                      (24)
```

Between h and epsilon_dagger the function D increases, and between
epsilon_dagger and L it decreases. Consequently every value on [h,L]
is at least min(D(h),D(L))>0. On [0,h], Section 4 already proves a
unique minimum at epsilon_* with negative value. This proves global
uniqueness on [0,L] and hence on the requested open interval.

Strict increase on (epsilon_*,h), together with D(epsilon_*)<0<D(h),
gives exactly one zero epsilon_0 there. All earlier positive widths
have negative cost difference, and all later ones have positive cost
difference by the tail comparison. This proves (4) and exhausts the
equality cases. In particular the known width 1/100 is admissible and
smaller than epsilon_*, so its continuous cost is strictly higher than
the new continuous minimum. That comparison is not a radius transfer.

## 7. Only the critical exact gates

The [bounded checker](../ops/TASK-20260906__second_block_width/check_width.py)
uses no production code, previous checker imports, floating arithmetic,
quadrature, parameter optimizer or permutations. The analytical arguments
above cover intervals; the checker supplies only the isolated inequalities
they require. Its constants and budgets are fixed before the final run.

The coarse alpha enclosure (1) suffices for (19), (21), disjointness
and all switch/curvature domains. To separate the narrow minimizer
bracket, first refine the SAME alpha_hat using the imported enclosure
from the alpha theorem, Section 4:

```text
-844272415/10^12 <= e_star=E(x_*) <= -844268070/10^12,
F_alpha'(alpha)=D_shift(alpha)+(1+alpha)*e_star,
F_alpha' strictly increasing and F_alpha'(alpha_hat)=0.
```

Here F_alpha is precisely F of that theorem, not the primitive F in
(9). D_shift is K' given by its equation (2), including its moving-wrap
term. Evaluate its two integrals with the primitive

```text
P(t,c)=sqrt(t*(t+c))-c*log((sqrt(t)+sqrt(t+c))/sqrt(c)),
partial_t P=sqrt(t/(t+c)).
```

Two strict sign gates prove

```text
10930369/10^8 < alpha_hat < 10930371/10^8.               (25)
```

This is enclosure refinement, not a new optimum or a decimal definition.
The checker imports the documented exact e_star enclosure as a theorem
dependency; it does not claim to independently re-prove it.

Every interval has integer endpoints divided by S=10^40. Addition and
subtraction are exact on that grid. Products and quotients use the extrema
of all endpoint combinations, rounded outward by integer floor/ceiling.
Division by an interval containing zero is rejected. Square roots use
isqrt(endpoint*S), with the upper endpoint raised one unit unless exact.
No machine floating-point rounding mode is assumed.

For atan, apply its half-angle identity twice, giving atan(x)=4*atan(q).
Enclose the first 64 terms of the alternating odd-power series and widen
by |q|_max^129/129 before multiplying by 4. For log(x), take two square
roots and set q=(x^(1/4)-1)/(x^(1/4)+1). Enclose twice the first 64
terms of the odd-power series, widen by
2*|q|_max^129/[129*(1-|q|_max^2)], and multiply by 4. The program checks
|q|_max<1 on every call; every series operation is itself enclosed.
These are analytic remainder bounds, not estimated quadrature errors.

For rational A,epsilon, the mixed switch uses at most 80 dyadic
bisections with EXACT rational signs. For p,q>=0, set r0=1-p-q.
If r0<0, sqrt(p)+sqrt(q)>1; otherwise its sign relative to 1 is the
sign of 4*p*q-r0^2. Equality is retained, and no negative side is
squared. Monotonicity in s proves root isolation. Monotonicity in A
and epsilon from Section 3 encloses a whole parameter box by its two
opposite corner roots. Formulae (9), (11), (12) then enclose the full
critical costs and slopes. At epsilon=h or L the formulas are evaluated
over a rectangle containing their exact parameter relation; this only
widens the bounds and does not assume that relation is independent.

The following OUTWARD RATIONAL intervals all have denominator 10^12:

| Critical quantity | Lower numerator | Upper numerator |
|---|---:|---:|
| F_alpha'(10930369/10^8) | -6646 | -1825 |
| F_alpha'(10930371/10^8) | 774 | 5594 |
| (B-a)^2*(A+a)^3-A^4*B, coarse alpha box | 1539769696812 | 1540056908541 |
| 8*(B-b)^2-A^4*B, coarse alpha box | 252449493925 | 252720030240 |
| 4*B^2*b-18*L^2, coarse alpha box | 1822946993601 | 1823333688076 |
| Psi(31248/10^6), refined alpha box | -601358 | -371047 |
| Psi(1/32), refined alpha box | 2452125 | 2682436 |
| Psi(1/3), refined alpha box | 1100874055 | 1101089693 |
| Psi(2/5), refined alpha box | -2864872963 | -2864658070 |
| D(h), refined alpha box | 19529281 | 19708132 |
| D(L), refined alpha box | 473194165 | 473693306 |

In addition, exact rational endpoint signs give

```text
3119/10^5 < tau < 312/10^4 < EL < EH < h < 1/20,
2*h<L, 2/5<L.                                        (26)
```

No endpoint in the requested bracket is stationary. The numerical
prediction epsilon_* approximately 0.0312483174 is consistent with
(3), but those extra digits are only a numerical observation; (3) is
the rigorously proved enclosure.

## 8. Limits, ownership and next discriminator

All quantified conclusions concern the continuous full-max functional
at exactly alpha_hat, lambda=A*x_* and u=1/3, with the width as the
sole variable. No movement of the start u, overlap with the first block,
crossing of the wrap, further block, joint re-optimization or general
balanced-coupling optimum is covered. The baseline minimum dependencies
are imported; independent external review of this proof is separate.

This task constructs no finite permutations, checks no finite floors or
cyclic cells, transfers no new full-radius limit and derives no new
geometric/global upper bound. The earlier finite recovery and full-root
result at width 1/100 retain exactly their existing scope. The continuous
minimum at epsilon_* is not silently substituted into those theorems.
There is no interchange of a finite-size limit with a width derivative.
Published assets and certified finite results are unchanged.

The sole thematic owner is knowledge/FIXED_ORDER_THEORY.md. Exact
commands, independent diagnostic limitations and the final source audit
are in the [task evidence](../ops/TASK-20260906__second_block_width/EVIDENCE.md).

**Exactly one next atomic discriminator:** with the baseline still fixed,
test the continuous start derivative partial_u Delta C(u,epsilon_*) at
u=1/3, keeping this exact width fixed. Prove it is zero or isolate its
strict sign with moving endpoints and the full max retained. This tests
whether the width minimum is stationary when the block start is freed;
it has not been carried out in this task.
