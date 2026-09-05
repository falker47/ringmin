# Exact alpha minimum of the reflected prefix at fixed x_*

```text
status=PROVED
classification=exact family-minimization, recovery and fixed-order full-radius theorem / proved global limsup corollary
domain=0<=alpha<=1/2; x=x_* fixed; lambda=(1+alpha)*x_* before the wrap
minimizer_bracket=1093/10000<alpha_hat<10931/100000
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Inputs, definitions and exact result

The accepted x_* is the SAME alpha-independent normalized minimizer from
[PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
Sections 2-7. Keep its definitions

```text
c(u,x)=sqrt((1+u)*(1+x-u)),
k(u,x)=sqrt(u)*(sqrt(1+u)+sqrt(1+x-u)),
d(u)=max(1+u,2*sqrt(u*(1+u))),
E(x)=integral_0^x [max(c(u,x),k(u,x))-d(u)] du,
sqrt(tau/(1+tau))+sqrt(tau)=1,
1/4<tau<x_*<1/3,  E'(x_*)=0,
XL=719/2500<x_*<XH=2877/10000.                           (1)
```

That theorem proves x_* is the unique minimum of E on its auxiliary
[0,1]. It does not define x_* through decimal data. Write e=E(x_*).
The shift function and its derivative are those of
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Sections 5-6:

```text
A=1+alpha, b=1-alpha, a=A/3,
h_alpha(t)=1+{t+alpha},
K(alpha)=integral_0^1 max(sqrt(t*h_alpha(t)),h_alpha(t)/2) dt,
D(alpha)=K'(alpha)
 =a/2+(1/2) integral_a^b sqrt(t/(t+A)) dt
      +(1/2) integral_b^1 sqrt(t/(t+alpha)) dt
      -(sqrt(2)-1)*sqrt(b).                             (2)
```

Endpoint values of h have no integral mass. In particular (2) includes
the moving-wrap jump term. The accepted neighborhood formula from
[PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md](PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md)
extends, as proved in Section 2 below, to the ENTIRE closed interval:

```text
C(alpha,x_*)=K(alpha)/(2*pi)+A^2*e/(4*pi),
F(alpha)=2*pi*C(alpha,x_*)=K(alpha)+A^2*e/2,
F'(alpha)=D(alpha)+A*e,
F''(alpha)=K''(alpha)+e.                                (3)
```

**Family theorem.** There is exactly one zero alpha_hat of F' on
[0,1/2], and

```text
1093/10000 < alpha_hat < 10931/100000.                   (4)
```

C(alpha,x_*) decreases strictly up to alpha_hat and increases strictly
after it. Thus alpha_hat is the unique minimum of THIS fixed-x_* family
on [0,1/2]. Define

```text
C_hat := C(alpha_hat,x_*).
```

The old C_107=C(107/1000,x_*) retains its accepted meaning. We prove

```text
C_hat < C_107-1/22000000,
C_hat < 14191364/100000000.                             (5)
```

Section 6 gives the fixed-order full-radius theorem for the recovered
orders, with actual all-pairs feasibility stated separately. Section 7
then derives the global limsup corollary. The family minimum does not
optimize general permutations, couplings, other alpha regimes or global
geometry. In particular no normalized global limit is asserted.

## 2. Closed-domain recovery and the full coefficient

For every fixed alpha in [0,1/2] put lambda=A*x_*. The rational domain
gates, including their endpoint behavior, are

```text
1/4<lambda<A/3<=b,
b-lambda >=1/2-(3/2)*x_* >1/2-(3/2)*XH
         =1369/20000>1/15.                              (6)
```

Indeed b-A*x_* decreases with alpha. At alpha=1/2, a=b but lambda<a;
at alpha=0, b=1 and the wrapped tail has zero length. The reflected
block stays strictly before the wrap everywhere in this closed domain.
This statement does not identify the maximal possible pre-wrap domain.

For every integer m>=2 use the existing construction, now with this alpha:

```text
s=floor(alpha*m), q=2*floor(lambda*m/2), r=m-s,
beta=s/m, L=q/m,
H(j)=m+1+((j+s-1) mod m), 1<=j<=m,
J(i)=q+2-i if i<=q is even, and J(i)=i otherwise,
P_i=H(J(i)), P_0=P_m, sigma_m(alpha)=(1,P_1,...,m,P_m).   (7)
```

The floor errors are 0<=alpha-beta<1/m and 0<=lambda-L<2/m.
Since s+q< m, r>=q+1 and q<m. The odd block ranks remain fixed,
the even ranks q,q-2,...,2 occur once, and every tail rank stays fixed.
Thus J is an involution and H a bijection; P is a genuine high
permutation. This includes q=0,2, when J is the identity.

The earlier neighborhood assertion r>=q+2 need NOT hold for small m
here. Use the SET of exceptions

```text
X_m={1,q+1,r,r+1} intersect {1,...,m} if q>=2,
X_m={1,r,r+1} intersect {1,...,m} if q=0.                 (8)
```

It has at most four members, with coincident cells counted only once.
The actual cyclic and junction pairs are retained exactly:

- i=1: (P_m,P_1)=(m+s,m+s+1) if s>0, or (2m,m+1) if s=0;
- i=q+1, q>=2: (m+s+2,m+s+q+1), even when q+1=r;
- i=r+1, s>0: (2m,m+1);
- i=r: P_r/m=2, whereas h_alpha(r/m) takes its lower branch.

At m=2,alpha=1/2 one has q=0,r=1: the wrap endpoint also coincides
with the low seam, and (8) still contains both cells. At alpha=0 the
high wrap is the low cyclic seam. No exceptional cell is removed from P.

For q>=2 the q-1 interior block cells, disjoint from X_m, have the
following exact predecessor/current pairs divided by m, with t=i/m:

| Cells | Predecessor | Current |
|---|---|---|
| even i=2,...,q | 1+beta+t-1/m | 1+beta+L-t+2/m |
| odd i=3,...,q-1 | 1+beta+L-t+3/m | 1+beta+t |

Outside X_m, tail pairs are (1+beta+t-1/m,1+beta+t) for i<r,
and (beta+t-1/m,beta+t) for i>r+1. The ordinary tail has
m-(q-1)-|X_m| cells when q>=2, and m-|X_m| when q=0. These
partitions include every cell also when exceptions coincide.

Compare the actual triples to (t,A+t,A+lambda-t) on even block cells,
their high-coordinate reversal on odd block cells, and
(t,h_alpha(t),h_alpha(t)) on the tail. These comparison triples lie
in [0,1] x [1,2]^2 by (6). Outside X_m their coordinate errors are
at most 3/m. The branch comparison is exact: i<r implies i/m<b,
while i>r+1 implies i/m>b. The problematic endpoint i=r is in X_m.

For a continuous test f on this compact box, with M=||f||_infinity
and modulus of continuity omega_f, the actual and comparison empirical
averages therefore differ by at most omega_f(3/m)+8*M/m. The parity
Riemann sums each have mesh 2/m and weight 1/m. The tail has only
one possible jump, at b. Moving q/m to lambda costs O(M/m). Hence

```text
mu_m=(1/m) sum_i delta_(i/m,P_{i-1}/m,P_i/m) -> mu_alpha,
integral f dmu_alpha
 =(1/2) integral_0^lambda
    [f(t,A+t,A+lambda-t)+f(t,A+lambda-t,A+t)] dt
   +integral_lambda^1 f(t,h_alpha(t),h_alpha(t)) dt.       (9)
```

This holds for every fixed alpha, along all integers m. No derivative
of a finite floor or interchange of derivative and m-limit is used.
For m>=15 the uniform gap (6) gives r-q>m/15>=1, hence r>=q+2;
also q>=2. Small coincidences do not obstruct the limit.

Retain the full cost g(t,u,v)=max(sqrt(t)*(sqrt(u)+sqrt(v)),sqrt(u*v)).
Its block switch is z_alpha=A*z(x_*), where z solves
sqrt(z/(1+z))+sqrt(z/(1+x_*-z))=1. The chord and chain values agree
at this switch, and x_*>tau ensures a nonempty chain segment.
The tail is exactly

```text
integral_lambda^a (A+t) dt
 +2 integral_a^b sqrt(t*(A+t)) dt
 +2 integral_b^1 sqrt(t*(alpha+t)) dt.                  (10)
```

The first-branch diagonal switch is a; the wrapped branch is always
chain because t>=b>=1/2>alpha/3. The middle integral vanishes when
alpha=1/2; the last vanishes when alpha=0. The diagonal cost before
lambda is A+t because lambda<a. Replacing that diagonal prefix by
the reflected full block, and setting t=A*u in the difference, gives

```text
integral g dmu_alpha=2*K(alpha)+A^2*e.                   (11)
```

Both the block integrand and dt supply one factor A. All moving-tail
dependence remains in K, including the jump in (2). The split integrals
give C^2 dependence within [0,1/2], with derivatives taken from inside
the domain at its endpoints; their t arguments stay away from any
singularity in the differentiated tail. This proves (3) as a coefficient
formula; the full-radius identification is deferred to Section 6.

## 3. Exact curvature and the two regime endpoint signs

First obtain a coarse TWO-SIDED analytic bound on e. For 0<x<1/3
write M=1+x/2 and v=u-x/2. The full block is at least its chord, so

```text
E(x)>=integral_(-x/2)^(x/2) [sqrt(M^2-v^2)-M] dv
    >=-integral_(-x/2)^(x/2) v^2/M dv
     =-x^3/(12*M)>-1/324.                              (12)
```

Here sqrt(1-y)>=1-y for 0<=y<=1 proves the second inequality; the
diagonal integral equals M*x. For the upper bound, x=1/4<tau makes
the block all chord. Its saving, rationalized, is

```text
-E(1/4)=integral_(-1/8)^(1/8) v^2/[9/8+sqrt((9/8)^2-v^2)] dv
       >1/1728.
```

Strictness holds away from v=0 on positive measure. The accepted strict
minimum property in (1) now gives

```text
-1/324<e<E(1/4)<-1/1728<0.                             (13)
```

The differentiated formula (2), including both moving endpoints, is

```text
K''=1/12+(1-1/sqrt(2))*sqrt(b)/2
          +(sqrt(2)-1)/(2*sqrt(b))-T/4,
T=integral_a^b sqrt(t)/(t+A)^(3/2) dt
  +integral_b^1 sqrt(t)/(t+alpha)^(3/2) dt.              (14)
```

Both denominators' bases are at least 1, and t<=1; hence T<=1-a<=2/3.
Since 1/2<=b<=1 and sqrt(2)>7/5, discarding the first strictly positive
term in (14) gives K''>(sqrt(2)-1)/2-1/12>7/60. Thus

```text
F''=K''+e>7/60-1/324=46/405>1/9>0                      (15)
```

throughout the domain (one-sided at the endpoints). This bound concerns
alpha variation only; it makes no convexity assertion across other
active regimes of K or across the switches of E.

For completeness the regime endpoint signs use only elementary exact
inequalities. Formula (2) at zero evaluates to

```text
D(0)=5/6-sqrt(2)/2-(1/2)*log((1+sqrt(2))/sqrt(3)).
```

For z>1, log(z)>2*(z-1)/(z+1), by differentiating the difference
from z=1. Since sqrt(2)>7/5 and sqrt(3)<7/4, the log argument is
greater than 48/35. Therefore

```text
F'(0)=D(0)+e<D(0)<5/6-7/10-13/83=-29/1245<0.            (16)
```

At alpha=1/2 one has a=b=1/2. The remaining integrand in (2) is
at least 1/sqrt(2), so D(1/2)>=5/(4*sqrt(2))-3/4>1/8,
using sqrt(2)<10/7. Equation (13) gives the other sign:

```text
F'(1/2)>1/8-(3/2)/324=13/108>0.                         (17)
```

All radical comparisons above follow by positive rational squares.
Continuity and (15)-(17) prove a unique zero in (0,1/2), strict decrease
before it, strict increase after it, and the unique family minimum.

## 4. Exact isolation in the requested rational bracket

The next gates locate this already unique zero; no numerical root is
used as a premise. It suffices to enclose e and the two values of D.
To avoid evaluating at an uncertified irrational argument, set

```text
x0=(XL+XH)/2=5753/20000, |x0-x_*|<1/20000.               (18)
```

The lower endpoint XL is above tau: the square-root enclosure of
sqrt(XL/(1+XL))+sqrt(XL) is strictly above 1. On the entire interval
(tau,1/3), the accepted lambda differentiation formula reads

```text
E''(x)=p'(x)-1+sqrt(x)/2-J(x)/4+Q(x),
p'(x)=(1+2*x)/(2*sqrt(x*(1+x)))+1/(2*sqrt(x)),
J(x)>=0,
Q(x)=z'(x)*(sqrt(1+z)-sqrt(z))/(2*sqrt(1+x-z)),
z'(x)=z/(( (1+x-z)/(1+z) )^(3/2)+1+x).                 (19)
```

Since x>1/4, p'<5/3+1=8/3. Since 0<z<x<1/3,
z'<x/(1+x)<1/4, sqrt(1+z)-sqrt(z)<1, and 1+x-z>1,
so Q<1/8; also sqrt(x)/2<1/3. Dropping -J/4 yields
E''<8/3-1+1/3+1/8=17/8<3. Taylor's formula about the stationary
minimum x_*, together with its minimum property, proves

```text
E(x0)-3/800000000 < e <= E(x0).                         (20)
```

Only a single rational-argument E integral is now needed. The independent
[check_alpha_minimum.py](../ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py)
uses the following finite rational enclosure algorithm:

1. For y=p/q>=0 take k=isqrt(floor(p*10^48/q)). Enclose sqrt(y)
   by k/10^24 and (k+1)/10^24, with a singleton for an exact square.
   Every returned endpoint is checked by rational squaring.
2. Isolate z(x0) in [zl,zh] by 64 dyadic bisections of [0,x0]. At each
   step test the UNSQUARED sum sqrt(t/(1+t))+sqrt(t/(1+x0-t))-1;
   a non-separated sign aborts. Monotonicity in t fixes the root and
   zh-zl=x0/2^64. Both final endpoint signs are checked.
3. On [0,zl] integrate c(u,x0); on [zh,x0] integrate k(u,x0).
   Each is concave: c''=-M^2/c^3, while the two summands of k have
   second derivatives -1/(4*(u*(1+u))^(3/2)) and
   -(1+x0)^2/(4*(u*(1+x0-u))^(3/2)). Thus the composite trapezoid
   is a lower bound and the composite midpoint an upper bound.
   Use exactly 2048 equal panels per interval. The omitted switch
   interval contributes between 0 and 4*(zh-zl). Subtract x0+x0^2/2
   and apply (20). This retains the chain part of the full max.
4. For D at each alpha endpoint, use 256 equal panels in each of its
   two integrals in (2). For f_c(t)=sqrt(t/(t+c)),
   f_c''=-c*(4*t+c)/(4*t^(3/2)*(t+c)^(5/2))<0, so the same
   trapezoid/midpoint enclosure applies. Multiply the two positive
   radical factors of the negative wrap term in the correct direction.

All sums and products use Fraction; there is no floating-point rounding
assumption or estimated quadrature error. The following are outward
RATIONAL display intervals with common denominator 10^12:

| Quantity | Lower numerator | Upper numerator |
|---|---:|---:|
| E(x0) | -844268665 | -844268070 |
| e=E(x_*) | -844272415 | -844268070 |
| D(1093/10000) | 935124205 | 935201790 |
| F'(1093/10000) | -1427184 | -1344781 |
| D(10931/100000) | 938842182 | 938919761 |
| F'(10931/100000) | 2282349 | 2364747 |

In particular the two strict sign gates are

```text
-3/2000000<F'(1093/10000)<-1/1000000<0,
0<2/1000000<F'(10931/100000)<5/2000000.                  (21)
```

Together with (15), these prove exactly the bracket (4) requested in
the question. The full-domain uniqueness proof is analytic; the checker
supplies only these isolated constant gates and rational implications.

## 5. Rigorous improvement over C_107

Put alpha0=107/1000 and L=1093/10000. Since alpha0<L<alpha_hat,
integrating F''>1/9 back from F'(alpha_hat)=0 gives

```text
F(alpha0)-F(alpha_hat)>(alpha_hat-alpha0)^2/18
                         >(L-alpha0)^2/18.
```

Dividing by 2*pi, and using the exact bound pi<22/7 established by
the positive integral in the accepted alpha note, Section 4, yields

```text
C_107-C_hat >529/(3600000000*pi)
             >3703/79200000000>1/22000000.               (22)
```

The accepted rational coefficient bound C_107<14191368/100000000
then gives

```text
C_hat<14191368/100000000-1/22000000
     <14191364/100000000,                               (23)
```

proving (5). This is a conservative exact improvement bound; it is not
the definition or an asserted tight enclosure of C_hat.

For orientation only, independent 70-digit original full-max quadrature
produces the following **numerical observations**, not premises:

```text
alpha_hat   =0.10930369632641477424523225745801230942...,
C_hat       =0.14191349134456084326890229893638278332...,
C_107-C_hat =0.00000015666216002543621573418467909454536....
```

## 6. Fixed-order full-radius theorem and separate feasibility

For every fixed alpha in [0,1/2], (7) is a true high permutation for
every m>=2. The exact arbitrary-permutation theorem in
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, identifies rho_m(alpha)=R_full(sigma_m(alpha)) as the
unique positive root

```text
sum_i max(theta_R(i,P_{i-1})+theta_R(i,P_i),
          theta_R(P_{i-1},P_i))=2*pi,
theta_R(u,v)=2*asin(sqrt(u*v/((R+u)*(R+v)))).             (24)
```

The uniform root-transfer theorem in
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Section 4, first brackets these roots at a compact positive quadratic
scale, and then gives, uniformly over high permutations,

```text
rho_m(alpha)/(2m)^2=(integral g dmu_m)/(4*pi)+O(1/m).
```

Continuity of g, recovery (9) and the full cost (11) prove

```text
R_full(sigma_m(alpha))/(2m)^2 -> C(alpha,x_*),
R_full(sigma_m(alpha_hat))/(2m)^2 -> C_hat.              (25)
```

These are limits for each fixed parameter and the prescribed orders.
They do not identify minimizers among the finite m orders or assert a
uniform-in-alpha minimum/limit interchange. The floors at the implicit
alpha_hat and x_* in (7) are exact definitions, never decimal floors.

**Actual feasibility, separately.** At the exact root rho_m define
a_i=theta_(rho_m)(P_{i-1},i), b_i=theta_(rho_m)(i,P_i), and
c_i=theta_(rho_m)(P_{i-1},P_i). Assign valley gaps

```text
u_i=a_i, v_i=b_i+max(0,c_i-a_i-b_i).                     (26)
```

They are positive and sum to 2*pi. The imported arbitrary-permutation
theorem checks both directed paths for every endpoint type, including
all seams and m=2. Thus (26) satisfies every pairwise angular constraint.
Cumulative angles with radius-j centers at distance rho_m+j give
Cartesian non-overlap and central tangency for every outer circle.
This constructs full-feasible placements at each fixed-order root; no
adjacent-chain radius has been substituted for R_full.

## 7. Global limsup corollary by feasibility and deletion

Only now fix alpha=alpha_hat and take the placements in (26). For every
m>=2, their feasibility gives R*(2m)<=rho_m(alpha_hat). Delete just
the circle of radius 2m; the remaining radii are exactly {1,...,2m-1},
and every remaining central tangency and pairwise non-overlap persists.
Hence R*(2m-1)<=rho_m(alpha_hat). The normalization factor
(2m/(2m-1))^2 tends to one, so (25) proves

```text
limsup_(n->infinity) R*(n)/n^2 <= C_hat
 < C_107-1/22000000,
limsup_(n->infinity) R*(n)/n^2 < 14191364/100000000.       (27)
```

The lower theorem for C_term and the finite certified scope are unchanged.
The family minimum in Section 3, the fixed-order theorem (25), feasibility
(26), and global bound (27) have different quantifiers. They imply no
general permutation or coupling optimum, geometric global equality,
normalized global limit, or contact/floating-circle assertion.

## 8. Verification, ownership and limitations

The [STRICT evidence](../ops/TASK-20260905__reflected_prefix_alpha_minimum/EVIDENCE.md)
records the fresh exact gates and a separate 70-digit quadrature cross-check
of the original full-max integrals, including alpha=0 and alpha=1/2.
The checker also audits only 120 small rational recovery cases, m=2..16,
covering the new endpoint and coincident-seam cases. These cases support
the bookkeeping and are not the proof of all-m occurrence or convergence.
No geometry scan, optimization search, production scorer, old checker or
standalone verifier is imported. Numerical diagnostics are not certificates.

The accepted x_* bracket/minimum, the differentiated shift and lambda
formulas, the arbitrary-permutation criterion and uniform root transfer
are explicit proof dependencies. This task does not independently
re-prove or re-certify their complete contents. External review of this
new extension remains pending. Prior notes and dossiers keep their
historical task scope and the published arXiv-v1 assets are unchanged.

The sole owner of definitions, recovery, family minimization, coefficient
comparisons and (25)-(26) is knowledge/FIXED_ORDER_THEORY.md. The sole
owner of the global corollary (27) is knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md.
