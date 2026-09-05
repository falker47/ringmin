# Improving the reflected prefix by increasing alpha at fixed x_*

```text
status=PROVED
classification=exact recovery, fixed-order coefficient and first-variation theorem / proved global upper-bound corollary
domain=alpha in I=[53/500,107/1000]; x=x_* fixed; lambda=(1+alpha)*x_*
explicit_witness=alpha=107/1000
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Exact question, dependencies and result

Keep the SAME alpha_* characterized by D(alpha_*)=K'(alpha_*)=0 in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Section 6,
and the SAME normalized minimizer x_* from
[PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
Sections 2-7. In particular that theorem supplies

```text
1/4 < tau < x_* < 1/3,
719/2500 < x_* < 2877/10000,
E'(x_*)=0,    lambda_*=(1+alpha_*)*x_*,
C_rp=C_ref(lambda_*) < 14191369/100000000.                 (1)
```

The definitions of E, tau and x_* contain NO alpha. The old lambda_* and
C_rp retain their meanings at alpha_*. This task varies only alpha along
lambda(alpha)=(1+alpha)*x_*. It does not minimize over alpha or over both
parameters, and does not search other permutations or couplings.

**Neighborhood theorem.** On the explicit closed neighborhood

```text
I=[53/500,107/1000],    53/500<alpha_*<267/2500<107/1000,
```

the parity-reflection recovery extends along every integer m>=2. Its
fixed-order full radius has coefficient

```text
C(alpha,x_*)=K(alpha)/(2*pi)+(1+alpha)^2*E(x_*)/(4*pi),
R_full(sigma_m(alpha))/(2m)^2 -> C(alpha,x_*).             (2)
```

The dependence in (2) is continuously differentiable in the interior of
I, with the corresponding one-sided endpoint derivatives, and

```text
partial_alpha C(alpha,x_*)
  =[D(alpha)+(1+alpha)*E(x_*)]/(2*pi) < -1/12000 on I,
partial_alpha C(alpha_*,x_*)
  =(1+alpha_*)*E(x_*)/(2*pi) < 0.                         (3)
```

Thus the prediction is true. Define the new coefficient only by

```text
C_107 := C(107/1000,x_*).
```

The rational witness satisfies the exact strict comparisons

```text
C_107 < C_rp-1/60000000,
C_107 < 14191368/100000000.                              (4)
```

Section 5 establishes the fixed-order full-radius limit and actual
all-pairs feasibility; Section 6 then derives the separate global
limsup corollary by deletion. Neither (2) nor (4) asserts global optimality.

## 2. Recovery in the explicit neighborhood

For each FIXED alpha in I put A=1+alpha, b=1-alpha,
lambda=A*x_* and h_alpha(t)=1+{t+alpha}. The domain gates are

```text
0<alpha<1/2,    1/4<lambda<A/3<b,
b-lambda > 893/1000-1107/3000 = 131/250 > 1/2.             (5)
```

Here lambda>1/4 follows from A>1 and x_*>1/4; lambda<A/3
follows from (1). For every m>=2 define

```text
s=floor(alpha*m), q=2*floor(lambda*m/2), r=m-s,
beta=s/m, L=q/m,
H(j)=m+1+((j+s-1) mod m), 1<=j<=m,
J(i)=q+2-i if i<=q is even, and J(i)=i otherwise,
P_i=H(J(i)), P_0=P_m, sigma_m(alpha)=(1,P_1,...,m,P_m).   (6)
```

The floor bounds are 0<=alpha-beta<1/m and 0<=lambda-L<2/m.
Since s+q< m, every block rank is before the wrap of H. More precisely,
r-q=m-s-q>m/2>=1 by (5), so r>=q+2. The potentially coincident
junction/wrap endpoint r=q+1 from the older, larger lambda domain cannot
occur here. No exceptional cell is discarded from the actual order.

The odd block ranks 1,3,...,q-1 stay fixed; the even ranks q,q-2,...,2
occur once each; ranks q+1,...,m stay fixed. Hence J is an involution
and H is a bijection onto {m+1,...,2m}. This proves exact occurrence
for every m, including q=0 and q=2, when J is the identity.

The proof of recovery in
[PERMUTED_HALVES_REFLECTED_PREFIX.md](PERMUTED_HALVES_REFLECTED_PREFIX.md),
Sections 2-3, used only these floor bounds, 0<alpha<1/2 and lambda<b,
not D(alpha)=0. To make this extension explicit, with t=i/m the interior
predecessor/current pairs divided by m are exactly

| Cells | Predecessor | Current | Count |
|---|---|---|---|
| even i=2,...,q | 1+beta+t-1/m | 1+beta+L-t+2/m | q/2 |
| odd i=3,...,q-1 | 1+beta+L-t+3/m | 1+beta+t | q/2-1 |

For q>=2, the exceptional set is X_m={1,q+1,r,r+1} intersect {1,...,m}.
It has four cells if s>0 and three if s=0, since r>=q+2. Their pairs
are retained exactly:

- i=1: (P_m,P_1)=(m+s,m+s+1) for s>0, and (2m,m+1) for s=0;
- i=q+1: (m+s+2,m+s+q+1);
- i=r+1, if s>0: (2m,m+1), the high wrap;
- i=r: the endpoint P_r/m=2, whereas h_alpha(r/m) takes its lower branch.

The interior count q-1, ordinary tail count m-q+1-|X_m| and |X_m|
sum to m. For q=0 omit the junction and use X_m={1,r,r+1} intersect
{1,...,m}; its size is three for s>0 and two for s=0. This includes
m=2,3. Outside X_m the tail pairs are (1+beta+t-1/m,1+beta+t) for
i<r, and (beta+t-1/m,beta+t) for i>r+1. The matching branches of
h_alpha have coordinate errors at most 2/m. The endpoint i=r is set
aside even if alpha*m is an integer. For m>=8, (5) guarantees q>=2.

Define the empirical measure with the ACTUAL cyclic predecessor by

```text
mu_m=(1/m) sum_i delta_(i/m,P_{i-1}/m,P_i/m).
```

Compare with (t,A+t,A+lambda-t) on even block indices,
(t,A+lambda-t,A+t) on odd block indices, and (t,h_alpha(t),h_alpha(t))
on the tail. These comparison atoms lie in [0,1] x [1,2]^2. Outside
X_m every coordinate error is at most 3/m. For an arbitrary continuous
test F on that compact box, writing M=||F||_infinity and omega_F for
its modulus of continuity, the integral error is at most

```text
omega_F(3/m)+8*M/m -> 0.                                (7)
```

The two parity sums have mesh 2/m and weight 1/m, so each tends to one
half of its block integral. The tail is a Riemann sum with only the jump
at b; moving q/m to lambda costs O(M/m). Consequently, along ALL integers,

```text
integral F dmu_(alpha,x_*)
 = (1/2) integral_0^lambda
     [F(t,A+t,A+lambda-t)+F(t,A+lambda-t,A+t)] dt
   + integral_lambda^1 F(t,h_alpha(t),h_alpha(t)) dt,
mu_m -> mu_(alpha,x_*).                                 (8)
```

Either high marginal of the block is Lebesgue measure on [A,A+lambda],
the same mass removed from the shift, and symmetry preserves conditional
high balance. Thus no marginal or wrap mass changes have been concealed.
Convergence for each fixed alpha suffices here. We do not differentiate
the finite floors, or interchange an alpha derivative with an m limit.

## 3. Full cost, moving tail and correct differentiation

Write g(t,u,v)=max(sqrt(t)*(sqrt(u)+sqrt(v)),sqrt(u*v)). Retain
the FULL max. Its reflected block has the switch z_alpha=A*z(x_*),
where z(x_*) is the unique solution in (0,x_*) of

```text
sqrt(z/(1+z))+sqrt(z/(1+x_*-z))=1.
```

Indeed, substitution t=A*u reduces the unsquared switch equation to
this equation, independently of alpha. Since x_*>tau, a nonempty chain
part follows the chord part; replacing the entire block by a chord
would be incorrect. The block and tail integrals are exactly

```text
B = integral_0^z_alpha sqrt((A+t)*(A+lambda-t)) dt
    + integral_z_alpha^lambda
        sqrt(t)*(sqrt(A+t)+sqrt(A+lambda-t)) dt,
T = integral_lambda^(A/3) (A+t) dt
    + 2 integral_(A/3)^b sqrt(t*(A+t)) dt
    + 2 integral_b^1 sqrt(t*(alpha+t)) dt.                (9)
```

The wrapped tail is always on the chain branch: t>=b>alpha/3.
The moving first switch is A/3; (5) places it between lambda and b.
The original diagonal shift has total full cost 2*K(alpha). Therefore

```text
B+T=2*K(alpha)+B-integral_0^lambda (A+t) dt
   =2*K(alpha)+A^2*E(x_*),                               (10)
```

where the exact normalized E is the same function as in the lambda note:

```text
E(x)=integral_0^x [max(sqrt((1+u)*(1+x-u)),
                     sqrt(u)*(sqrt(1+u)+sqrt(1+x-u)))
                  -max(1+u,2*sqrt(u*(1+u)))] du.
```

On [0,x_*], the subtracted diagonal maximum is 1+u. Each block
integrand contributes a factor A, and dt contributes another A; this
proves the factor A^2 in (10). The tail is not held fixed: its entire
alpha dependence remains in K(alpha), including the moving wrap b.
In particular, for a=A/3 the imported differentiable formula is

```text
D(alpha)=K'(alpha)
 =a/2+(1/2) integral_a^b sqrt(t/(t+1+alpha)) dt
      +(1/2) integral_b^1 sqrt(t/(t+alpha)) dt
      -(sqrt(2)-1)*sqrt(b).                             (11)
```

The last term is the jump contribution at b, and is essential. Equations
(10)-(11) give (3)'s derivative formula by ordinary differentiation at
fixed x_*. Although lambda'(alpha)=x_*, x_* itself is constant.
For comparison, differentiation at fixed lambda would add
-A*x*E'(x)/(4*pi), with x=lambda/A. That extra term vanishes at x=x_*,
but the present path keeps x_* fixed for the ENTIRE comparison interval.
No assumption that K(alpha) stays equal to K(alpha_*) is made.

## 4. Exact sign and rational improving witness

First bound E(x_*) analytically. The accepted minimization theorem gives
E(x_*)<E(1/4). At x=1/4<tau both block and diagonal are chords. Center
the block integral and put M=1+x/2=9/8. Its saving is

```text
-E(1/4)=integral_(-x/2)^(x/2) [M-sqrt(M^2-v^2)] dv
       =integral_(-x/2)^(x/2) v^2/[M+sqrt(M^2-v^2)] dv
       >x^3/(24*M)=1/1728.                             (12)
```

The denominator is strictly below 2*M away from v=0; strictness holds
on a set of positive measure. Thus E(x_*)<-1/1728<0. Combining
D(alpha_*)=0 with (10) already proves the requested strict sign at alpha_*.

For an explicit finite increase, the fresh rational gates are

| Quantity | Strict lower bound | Strict upper bound |
|---|---:|---:|
| D(53/500) | -3/10000 | -1/5000 |
| D(267/2500) | 0 | 1/100000 |
| D(107/1000) | 7/100000 | 9/100000 |

These are enclosed independently of the earlier checker by
[check_alpha.py](../ops/TASK-20260905__reflected_prefix_alpha/check_alpha.py).
Here is the complete enclosure algorithm. For f_c(t)=sqrt(t/(t+c)),

```text
f_c''(t)=-c*(4*t+c)/(4*t^(3/2)*(t+c)^(5/2))<0, c,t>0.
```

On each of the two integration intervals in (11), divide into N=128
equal panels. Concavity makes the composite trapezoid a lower bound and
the composite midpoint sum an upper bound. For every nonnegative rational
y=p/q, set k=isqrt(floor(p*10^40/q)). Its square root lies in
[k/10^20,(k+1)/10^20], with an exact singleton if the square is exact.
All sums and products use Fraction. Enclose the negative last term of
(11) by multiplying its positive square-root factors in the correct
direction. No quadrature-error estimate or floating-point sign is used.
The square of each returned endpoint is checked against y.

Strict increase of D on [0,1/2], imported from the shift theorem, now gives
the claimed alpha_* bracket and D(alpha)<=D(107/1000)<9/100000 on I.
Together with A>=553/500 and (12),

```text
D(alpha)+A*E(x_*)
 < 9/100000-553/864000
 < -11/21000=-(2*(22/7))/12000.                          (13)
```

The rational gap in the second strict comparison is 3967/151200000.
For completeness, pi<22/7 follows from the positive integral

```text
integral_0^1 t^4*(1-t)^4/(1+t^2) dt = 22/7-pi > 0:
t^4*(1-t)^4/(1+t^2)
  =t^6-4*t^5+5*t^4-4*t^2+4-4/(1+t^2).
```

Dividing (13) by 2*pi proves the uniform derivative bound in (3),
with its direction preserved for a negative numerator. Finally

```text
107/1000-alpha_* > 107/1000-267/2500=1/5000,
C_rp-C_107 > (107/1000-alpha_*)/12000 > 1/60000000.       (14)
```

This proves the first part of (4). Its second part follows separately
from the imported rational bound in (1) and the exact comparison
14191369/100000000-1/60000000<14191368/100000000.
The witness was selected in advance; no alpha minimization enters (14).

For orientation, independent 70-digit integration of the ORIGINAL
unnormalized full max gives these **numerical observations**, not premises:

```text
partial_alpha C(alpha_*,x_*) = -0.0001487181275456426051857963485674...,
lambda(107/1000)             =  0.3184072987667258900081758139487276...,
C_107                       =  0.1419136480067208687051180331210619...,
C_rp-C_107                  =  0.0000000306424269251625155676902797....
```

## 5. Fixed-order radius and exact full feasibility

For every fixed alpha in I and m>=2, (6) is a true high permutation.
The exact arbitrary-permutation theorem in
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, therefore identifies the full radius rho_m as the unique root

```text
S_m(R)=sum_i max(theta_R(i,P_{i-1})+theta_R(i,P_i),
                 theta_R(P_{i-1},P_i))=2*pi.              (15)
```

The uniform full-root transfer in
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Section 4, first brackets rho_m/(2m)^2 in a fixed compact positive
interval and then proves, uniformly over high permutations,

```text
rho_m/(2m)^2=(integral g dmu_m)/(4*pi)+O(1/m).
```

Continuity of g, (8) and (10) prove (2), including its specialization
to C_107. This is a theorem about R_full; no adjacent-chain radius has
been substituted and no limiting coupling alone is treated as a placement.

**Feasibility, separately.** At each exact rho_m in (15) put
a_i=theta_(rho_m)(P_{i-1},i), b_i=theta_(rho_m)(i,P_i),
c_i=theta_(rho_m)(P_{i-1},P_i). The incoming/outgoing valley gaps

```text
u_i=a_i,    v_i=b_i+max(0,c_i-a_i-b_i)
```

are positive and sum to 2*pi. The imported theorem checks both directed
paths for every endpoint type, including the low seam and every high
jump, so these gaps give all-pairs angular feasibility. Cumulative angles
with each radius-j center at distance rho_m+j give Cartesian non-overlap and every
central tangency. This construction works for every m>=2, including the
small identity-prefix cases. It establishes feasible radii for these
orders, not finite geometric global optima. No explicit asymptotic cutoff
for a prescribed finite coefficient tolerance is asserted.

## 6. Separate global deletion corollary

Now specialize to alpha=107/1000 and take the placements just proved
feasible. At even sizes R*(2m)<=rho_m. Deleting only the outer circle of
radius 2m preserves all remaining central tangencies and all pairwise
non-overlaps, and leaves exactly {1,...,2m-1}. Thus R*(2m-1)<=rho_m.
The normalization ratio (2m/(2m-1))^2 tends to one. From (2) and (4),

```text
limsup_(n->infinity) R*(n)/n^2 <= C_107
 < C_rp-1/60000000 < C_rp,
limsup_(n->infinity) R*(n)/n^2 < 14191368/100000000.        (16)
```

The lower coefficient C_term and the certified finite scope are unchanged.
No joint parameter optimum, general permutation/coupling optimum, global
geometric optimum, normalized global limit, contact or floating assertion
follows. The sole owner of (16) is knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md;
recovery, full-cost variation, definitions and comparisons (1)-(15) are
owned by knowledge/FIXED_ORDER_THEORY.md.

## 7. Verification and limitations

The [task evidence](../ops/TASK-20260905__reflected_prefix_alpha/EVIDENCE.md)
records fresh exact stdlib checks, a rerun of the imported lambda gates,
1143 rational finite recovery audits, and independent original full-max
quadrature/alpha derivatives. Numerical geometry diagnostics check eight
sizes and 11062 pairs, with finite floors determined from the accepted
rational x_* bracket. They are not global certificates or the proof of
continuous-test convergence. The checker imports no production code,
standalone verifier or older checker. The analytic argument and isolated
rational gates have been kept separate from the displayed decimals.

This extension needs the imported exact minimizer, feasibility and uniform
root theorems; its local checks do not independently re-prove those complete
dependencies. Independent external review of this new proof remains pending.
Earlier notes, dossiers and the arXiv-v1 record are unchanged.
