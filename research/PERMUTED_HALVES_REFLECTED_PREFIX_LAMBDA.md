# Exact lambda variation of the reflected prefix at fixed alpha_*

```text
status=PROVED
classification=exact family-minimization and fixed-order coefficient theorem / proved global upper-bound corollary
domain=alpha=alpha_* fixed exactly; 1/4<=lambda<1-alpha_*
minimizer_bracket=159/500<lambda_*<319/1000
monotonicity=decrease, increase, decrease; whole-right-side increase is disproved
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question, dependencies and result

Throughout, alpha is the SAME exact alpha_* defined by D(alpha)=0 in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Section 6.
Its defining function and uniqueness theorem are imported, not optimized
again. Put A=1+alpha and b=1-alpha. We start from the exact full-max block
and tail formulas (8)-(9) of
[PERMUTED_HALVES_REFLECTED_PREFIX.md](PERMUTED_HALVES_REFLECTED_PREFIX.md).
That note supplies genuine permutations P_m(lambda) for every integer
m>=2 and every fixed 1/4<=lambda<b, their continuous-test recovery, and
the full-radius limit C_ref(lambda). Its C_ref=C_ref(1/4) and
C_30=C_ref(3/10) retain their meanings.

**Fixed-family variation theorem.** There are exactly two stationary
points in this domain: lambda_* and lambda_dagger, with

```text
159/500 < lambda_* < 319/1000,
A/3 < lambda_dagger < 4*A/5 < b.
```

C_ref is strictly decreasing on [1/4,lambda_*], strictly increasing on
[lambda_*,lambda_dagger], and strictly decreasing on [lambda_dagger,b).
The first point is the unique GLOBAL minimizer of this one-parameter
family; the second is a strict local maximum. Define

```text
C_rp := C_ref(lambda_*).
```

In particular the reviewer's predicted minimizer bracket is confirmed,
but global strict increase to its right is FALSE. A rational counterexample
is

```text
C_ref(891/1000) < C_ref(89/100),
lambda_* < 89/100 < 891/1000 < b.                         (1)
```

An explicit rational witness also proves

```text
C_rp < C_ref(159/500) < C_30 - 1/100000,
C_rp < 14191369/100000000.                               (2)
```

**Fixed-order coefficient theorem.** For the already constructed orders
sigma_m(lambda_*)=(1,P_{m,1}(lambda_*),...,m,P_{m,m}(lambda_*)),

```text
R_full(sigma_m(lambda_*))/(2m)^2 -> C_rp.                 (3)
```

This is a full all-pairs fixed-order coefficient. Section 8 separately
derives the global limsup upper bound by feasibility and deletion. Neither
statement optimizes alpha, general high permutations, the continuum
relaxation or the global geometry.

## 2. Scale reduction and the two exact switches

Set x=lambda/A, u=t/A and U=b/A<1. Define the auxiliary functions on
0<=x<=1 by

```text
c(u,x)=sqrt((1+u)*(1+x-u)),
k(u,x)=sqrt(u)*(sqrt(1+u)+sqrt(1+x-u)),
d(u)=max(1+u,2*sqrt(u*(1+u))),
E(x)=integral_0^x [max(c(u,x),k(u,x))-d(u)] du.            (4)
```

The exact scaling of the imported integrals, with both alpha and its
wrapped tail fixed, gives

```text
C_ref(lambda)=C_shift + A^2*E(lambda/A)/(4*pi),
C_shift=K(alpha_*)/(2*pi).                               (5)
```

Only x<U represents the stated construction. The auxiliary extension
E on [U,1] will be used for an inequality, not as a permutation formula
crossing the high wrap.

Write

```text
v(u,x)=sqrt(u/(1+u))+sqrt(u/(1+x-u)).
```

For fixed x, v strictly increases in u on [0,x], and c>=k exactly when
v<=1. The unique block-entry parameter tau satisfies

```text
sqrt(tau/(1+tau))+sqrt(tau)=1,
1/4 < tau < 1/3.                                        (6)
```

Indeed v(x,x) strictly increases, its value at 1/4 is
1/sqrt(5)+1/2<1 and at 1/3 it is 1/2+1/sqrt(3)>1.
For x<=tau set z(x)=x. For x>tau, z(x) is the unique solution
v(z,x)=1 in (0,x). Hence the block is chord on [0,z] and chain on [z,x].
The second switch is the diagonal one: d(u)=1+u for u<=1/3 and
d(u)=2*sqrt(u*(1+u)) for u>=1/3. The two switches do not coincide.

On x>tau the implicit function is smooth, and, with y=1+x-z and
r=sqrt(z/(1+z)),

```text
z'(x)=z/((y/(1+z))^(3/2)+1+x)
     =(1-r)^2/(2-r+2*r^2)>0.                             (7)
```

The second identity follows from sqrt(z/y)=1-r, so
y=z/(1-r)^2 and z=r^2/(1-r^2). All denominators are positive.
No polynomial root from an unsafe squaring step is substituted for v=1.

## 3. Analytic first variation on the complete domain

Let Phi=E'. Since the two block values agree at z, their moving-boundary
terms cancel. At x=tau the chain interval has zero length and its endpoint
value equals the chord value. At x=1/3 the two diagonal values agree.
Consequently E is C^1, including both switches, and is analytic inside
each of the three open regimes.

On the all-chord regime, centering the circular integral gives

```text
Phi(x)=sqrt(1+x)+(1+x/2)*asin(x/(2+x))-(1+x),  0<=x<=tau.
                                                               (8)
```

On x>tau, put

```text
I_1(x)=integral_0^z sqrt((1+u)/(1+x-u)) du,
I_2(x)=integral_z^x sqrt(u/(1+x-u)) du.
```

The exact derivative is

```text
Phi(x)=sqrt(x)*(sqrt(1+x)+1)-d(x)+(I_1(x)+I_2(x))/2.       (9)
C_ref'(lambda)=A*Phi(lambda/A)/(4*pi).                    (10)
```

These formulas retain the endpoint change from chord to chain as well
as the moving interior boundary; dropping the chain branch would give
the wrong derivative already near the minimizer.

For explicit evaluation without quadrature, define, for 0<w<c,

```text
H(c,w)=c*atan(sqrt(w/(c-w)))-sqrt(w*(c-w)).
```

Its w derivative is sqrt(w/(c-w)), so

```text
I_1=H(2+x,1+z)-H(2+x,1),
I_2=H(1+x,x)-H(1+x,z).                                  (11)
```

## 4. All-chord decrease and strictly increasing middle derivative

From (8),

```text
Phi(0)=Phi'(0)=0,
Phi''(x)=-1/(2*(2+x)*(1+x)^(3/2))<0.
```

Thus Phi'<0 on (0,tau), and Phi<0 for every 0<x<=tau, by continuity
at tau. In particular E decreases strictly there, and E(tau)<E(0)=0.

On the switched block put

```text
J(x)=integral_0^z sqrt(1+u)/(1+x-u)^(3/2) du
     +integral_z^x sqrt(u)/(1+x-u)^(3/2) du,
Q(x)=z'(x)*(sqrt(1+z)-sqrt(z))/(2*sqrt(1+x-z))>0,
p(x)=sqrt(x)*(sqrt(1+x)+1).
```

Differentiating (9), with the moving integration boundary retained,
gives

```text
Phi'(x)=p'(x)-d'(x)+sqrt(x)/2-J(x)/4+Q(x).                (12)
```

For tau<x<1/3, d'=1, 1+x-u>=1, and

```text
J<=x*sqrt(1+x)<7/18,
p'=(1+2*x)/(2*sqrt(x*(1+x)))+1/(2*sqrt(x))
   >1/sqrt(x)>=sqrt(3)>5/3.
```

The strict bound on p' also follows by separating the derivative of
sqrt(x)*sqrt(1+x) into two positive terms. Discarding the positive
sqrt(x)/2 and Q terms from (12) yields the uniform estimate

```text
Phi'(x)>5/3-1-7/72=41/72>0,  tau<x<1/3.                 (13)
```

It remains to show that Phi becomes positive before the diagonal switch.
At x=1/3, v(2/7,x)=sqrt(2/9)+sqrt(3/11)<1, with explicit square gates

```text
1-2/9-3/11=50/99>0,
(50/99)^2-4*(2/9)*(3/11)=124/9801>0.
```

Thus z(1/3)>2/7. Since I_1>=z/sqrt(1+x) and I_2>=0, (9) gives

```text
Phi(1/3)>1/sqrt(3)-2/3+sqrt(3)/14
          =17*sqrt(3)/42-2/3>0,                         (14)
```

where 17^2*3>28^2 proves the last sign. By continuity, (13),
Phi(tau)<0 and (14), there is exactly one zero x_* in (tau,1/3),
with Phi<0 before it and Phi>0 from it through 1/3.

## 5. Strictly decreasing tail derivative and the missed local maximum

For 1/3<x<=1, (12) simplifies to

```text
Phi'(x)=-M(x)-J(x)/4+Q(x),
M(x)=[1+2*x-(1+x)^(3/2)]/[2*sqrt(x*(1+x))].              (15)
```

Here are analytic bounds valid on this ENTIRE interval.

First, z is increasing and z(1/3)>2/7, so
r=sqrt(z/(1+z))>sqrt(2/9)>8/17. The last square gap is 2/2601.
The polynomial 5-13*r+5*r^2 decreases for 0<r<1 and equals
-3/289 at r=8/17. Formula (7) therefore gives z'<1/7. Also

```text
sqrt(1+z)-sqrt(z)=1/(sqrt(1+z)+sqrt(z))<2/3,
sqrt(1+x-z)>=1,
0<Q<1/21.                                               (16)
```

For the first strict bound it suffices that z>1/4.

Next set w=sqrt(1+x), so 2/sqrt(3)<=w<=sqrt(2), and factor

```text
M(x)=sqrt((w-1)/(w+1))*(1+w-w^2)/(2*w).
```

The first factor increases with w; the second equals
(1/w+1-w)/2, is positive here and strictly decreases. If w<=4/3,
the first factor is >1/4 because w>=2/sqrt(3)>17/15; the second is
>=5/24. Hence M>5/96>1/20. If w>=4/3, the first factor is
>=1/sqrt(7)>3/8, while the second is
>=(2-sqrt(2))/4>1/7, using sqrt(2)<10/7. Hence M>3/56>1/20.
Together with J>=0 and (16), this proves

```text
Phi'(x)<-1/20+1/21=-1/420<0,  1/3<x<1.                  (17)
```

The rational evaluation in Section 7 gives

```text
-1/500 < Phi(4/5) < -1/1000.                            (18)
```

By (14), (17) and (18), there is exactly one zero x_dagger in
(1/3,4/5). Phi is positive between x_* and x_dagger and negative
on (x_dagger,1]. Thus the whole-right-side monotonicity fails: the
tail is strictly concave, not an extension of the middle convex regime.
Assuming convexity across the diagonal switch is precisely the invalid
step that would conceal this second stationary point.

Section 7 also proves 53/500<alpha_*<107/1000<1/9. Therefore
4/5<U<1 and both stationary points lie in the construction's domain.
In particular lambda_dagger=A*x_dagger, while lambda_*=A*x_*.
For every lambda in [89/100,891/1000], the exact inequalities

```text
(4/5)*(1+107/1000)<89/100,
891/1000<1-107/1000
```

put lambda/A strictly above 4/5 and lambda strictly below b. Equations
(10), (17)-(18) show C_ref'<0 throughout this rational interval, proving
the explicit counterexample (1).

## 6. Unique global minimum despite the descending final segment

The minimum E(x_*) is strictly negative by Section 4. Also
E(1/3)>E(x_*) because Phi>0 between x_* and 1/3. Section 7 proves

```text
3/250 < E(1) < 13/1000.                                 (19)
```

Strict concavity (17) implies that on [1/3,1], E is at least the chord
joining its two endpoint values. Both endpoints are strictly greater
than E(x_*), so EVERY value in this interval is strictly greater too.
On [0,1/3], the already proved signs of Phi make x_* the unique minimum.
Consequently x_* is the unique global minimizer on the auxiliary [0,1]
and, in particular, on [1/(4*A),U). The comparison at x=1 uses only the
auxiliary function (4); no wrap-crossing construction has been assumed.

The rational derivative gates in Section 7 sharpen its location to

```text
719/2500 < x_* < 2877/10000.
```

Indeed both endpoints are in the switched middle branch and have
opposite derivative signs. Combining this with the coarse exact alpha
bracket proves

```text
159/500 < (1+53/500)*(719/2500) < lambda_*
        < (1+107/1000)*(2877/10000) < 319/1000.            (20)
```

This brackets the exact minimizer; the numerical prediction was not a
premise. Strict decrease before lambda_* implies
C_rp<C_ref(159/500). The coefficient enclosures below give the further
strict improvements (2).

## 7. Reproducible rational endpoint gates

The finite evaluations in this section use integer arithmetic with
outward rational enclosures, not floating-point quadrature. Their source
is [check_lambda.py](../ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py);
commands, complete output, independent diagnostics and provenance are
in the [task evidence](../ops/TASK-20260905__reflected_prefix_lambda/EVIDENCE.md).
The all-domain sign and uniqueness arguments are Sections 2-6; the
checker supplies only the explicitly isolated constant/sign gates.

The rational enclosure algorithm is as follows. Represent an interval
by integer endpoints divided by S=10^50. Round each product and quotient
outward using integer floor/ceiling; addition and subtraction are exact
on this grid. For a nonnegative grid endpoint n/S, the lower square-root
endpoint is isqrt(n*S)/S; add one grid unit for the upper endpoint unless
the square is exact. Division by an interval containing zero is rejected.

To evaluate atan(y), apply twice

```text
atan(y)=2*atan(y/(1+sqrt(1+y^2))).
```

For the resulting interval q, sum the first N=64 terms of
sum_{k>=0} (-1)^k*q^(2k+1)/(2k+1), and widen by
|q|_max^(2*N+1)/(2*N+1); then multiply by 4. All arguments have
|q|_max<1, explicitly checked. To evaluate log(y)>-infinity for y>0,
take two square roots, put q=(y^(1/4)-1)/(y^(1/4)+1), and use

```text
log(y)=4*[2*sum_{k>=0} q^(2k+1)/(2*k+1)].
```

Widen the bracketed 64-term sum by
2*|q|_max^(129)/(129*(1-|q|_max^2)), then multiply by 4. These are
the alternating-series and geometric-tail bounds, with every arithmetic
operation itself enclosed. Root isolation of z at rational x uses 100
dyadic bisections of [0,x], testing the unsquared v-1. A step whose sign
is not separated is rejected. For a parameter interval, monotonicity (7)
allows the hull of its two endpoint isolations. The all-chord case is
retained when v(x,x)<1.

For the coefficient and E evaluations, use the exact primitives

```text
F(t,c)=[(2*t+c)*sqrt(t*(t+c))
        -c^2*log((sqrt(t)+sqrt(t+c))/sqrt(c))]/4,
J_circ(v,R)=[v*sqrt(R^2-v^2)
             +R^2*atan(v/sqrt(R^2-v^2))]/2.
```

Their derivatives are respectively sqrt(t*(t+c)) and sqrt(R^2-v^2).
The normalized block is

```text
J_circ(z-x/2,1+x/2)-J_circ(-x/2,1+x/2)
 +F(x,1)-F(z,1)
 +J_circ(x-(1+x)/2,(1+x)/2)
 -J_circ(z-(1+x)/2,(1+x)/2),                             (21)
```

with the last four terms omitted in the all-chord regime. Subtract
x+x^2/2 if x<=1/3, or 7/18+2*(F(x,1)-F(1/3,1)) otherwise, to obtain E.
For K and D use the exact formulas in the shift note: the derivative
integrals have primitive sqrt(t*(t+c))-c*log((sqrt(t)+sqrt(t+c))/sqrt(c)).
Thus all gates reduce to the specified finite rational operations.

| Quantity | Strict lower bound | Strict upper bound |
|---|---:|---:|
| D(53/500) | -3/10000 | -1/5000 |
| D(107/1000) | 7/100000 | 9/100000 |
| Phi(719/2500) | -1/20000 | -1/25000 |
| Phi(2877/10000) | 1/10000 | 11/100000 |
| Phi(4/5) | -1/500 | -1/1000 |
| E(1) | 3/250 | 13/1000 |

Strict increase of the imported D gives the coarse alpha bracket used
above. For tighter coefficient enclosures, the same exact D evaluation
has negative and positive signs, respectively, at

```text
alpha_lo=10678476019/100000000000,
alpha_hi=10678476021/100000000000.
```

This isolates the SAME fixed alpha_* and does not vary it as a design
parameter. Evaluate (5) for this whole alpha box. Pi is enclosed using
pi=16*atan(1/5)-4*atan(1/239): the tangent of
4*atan(1/5)-atan(1/239) is exactly 1 and the angle is in (0,pi/2),
fixing the branch at pi/4. The resulting rigorous enclosures are

```text
14191368/100000000 < C_ref(159/500) < 14191369/100000000,
14192459/100000000 < C_30           < 14192460/100000000.
```

The separated rational endpoints give

```text
C_30-C_ref(159/500) > 1090/100000000 > 1/100000,
```

proving (2). These constant enclosures are exact rational computations
inside the proof, not geometric finite certificates.

For orientation only, independent 70-digit quadrature gives the following
**numerical observations**, which are not premises:

```text
lambda_*      = 0.31834538917021562118799984238752004...,
lambda_dagger = 0.87275088111738991353888985739456419...,
C_rp          = 0.1419136786491477938676336008113416....
```

## 8. Fixed-order transfer first, global corollary second

**Proof of (3).** Equation (20) puts the exact, fixed lambda_* in the
domain of the existing reflected-prefix recovery theorem. In its
construction keep

```text
s_m=floor(alpha_* m), q_m=2*floor(lambda_* m/2),
```

and the same parity involution and cyclic high shift as before. No
finite floor is inferred from a decimal. The imported bijection and
continuous-test convergence hold for this fixed real parameter along
all integers m. The exact arbitrary-high-permutation all-pairs criterion
of [PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, retains every valley and cyclic seam. The uniform full-root
transfer from
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Section 4, therefore gives (3). Its root bracket precedes its asymptotic
expansion; there is no substitution of the adjacent-chain radius.

**Separate global upper-bound corollary.** At even size 2m, the exact full
criterion supplies a feasible placement at rho_m=R_full(sigma_m(lambda_*)).
Thus R*(2m)<=rho_m. Deleting just the circle of radius 2m preserves all
remaining central tangencies and all pairwise non-overlaps, leaving
exactly {1,...,2m-1}. Hence R*(2m-1)<=rho_m. Since
(2m/(2m-1))^2 tends to 1, (3) proves

```text
limsup_{n->infinity} R*(n)/n^2 <= C_rp
 < C_30-1/100000,
limsup_{n->infinity} R*(n)/n^2 < 14191369/100000000.        (22)
```

The fixed-order theorem and the feasibility/deletion corollary have
different quantifiers and different ledger owners. C_term and the finite
certified scope are unchanged. No global optimality, matching lower
bound, normalized global limit, contact or floating-circle assertion
follows from the unique minimizer within this family.

## 9. Verification, ownership and limitations

The exact gates run with the standard library only. A separate mpmath
diagnostic evaluates the original unnormalized full-max integrals and
their derivatives at eleven fixed probes, including both sides of both
switches and the final descent, and compares independent quadrature to
the interval enclosures. It imports neither production code, verify.py
nor older checkers. It does not independently re-prove imported recovery
or geometric feasibility, nor does it extend any finite certificate.

The sole owner of variation, minimization, coefficient definitions and
comparisons is knowledge/FIXED_ORDER_THEORY.md. Only (22) belongs to
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md. Earlier proof notes retain their
historical task scope; alpha optimization, reflection across the high
wrap and general permutation/coupling optimization remain outside this
result. Independent external review of this proof and its dependencies
remains pending.
