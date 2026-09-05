# A longer reflected prefix at the fixed shift minimizer

```text
status=PROVED
classification=exact recovery and full-radius theorem / proved global upper-bound corollary
domain=alpha=alpha_* fixed; 1/4<=lambda<1-alpha; every integer m>=2
explicit_improving_witness=lambda=3/10
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question, dependencies and result

This generalizes the deterministic construction in
[PERMUTED_HALVES_MU_REF_RECOVERY.md](PERMUTED_HALVES_MU_REF_RECOVERY.md).
Throughout, alpha is EXACTLY the unique shift minimizer alpha_* defined by
D(alpha)=0 in [SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md),
Section 6; it is never optimized again. That theorem gives 0<alpha<1/2.
Write A=1+alpha, b=1-alpha, h(t)=1+{t+alpha}, and

```text
D_box=[0,1] x [1,2] x [1,2],
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)).
```

For a fixed 1/4<=lambda<b, define the reflected coupling by

```text
integral F dmu_lambda
 = (1/2) integral_0^lambda
     [F(t,A+t,A+lambda-t)+F(t,A+lambda-t,A+t)] dt
   + integral_lambda^1 F(t,h(t),h(t)) dt.                 (1)
```

The restriction lambda<b keeps the reflected block before the high wrap.
It suffices for the requested witness and is the domain of this extension;
no formula for a block crossing that wrap is asserted. The substitution
t->lambda-t shows that either high marginal on the block is Lebesgue
measure on [A,A+lambda], exactly the mass removed from the shift. Thus
both high marginals remain uniform on [1,2], the low marginal is uniform
on [0,1], and the two conditional high marginals agree by symmetry.

We construct genuine high permutations P_m(lambda) on the full integer
sequence with empirical measures tending weakly to (1). For their cyclic
orders sigma_m=(1,P_{m,1},...,m,P_{m,m}) the imported uniform full-radius
theorem then gives

```text
R_full(sigma_m)/(2m)^2 -> C_ref(lambda)
                       := (integral g dmu_lambda)/(4*pi).  (2)
```

The old constant retains its meaning: C_ref=C_ref(1/4). The explicit
witness C_30:=C_ref(3/10) satisfies the exact strict inequality

```text
C_30 < C_ref - 37/(1830400*pi) < C_ref.                   (3)
```

The full max, including its possible switches for other lambda, is derived
in Section 4. Section 5 proves that this particular witness has no switch
inside the reflected block and proves (3) with rational inequalities.
Neither alpha, lambda, permutations nor couplings are optimized here.

## 2. Finite permutation, predecessors and exceptional cells

For every m>=2 set

```text
s=floor(alpha*m), q=2*floor(lambda*m/2),
beta=s/m, L=q/m, r=m-s,
H(j)=m+1+((j+s-1) mod m),  1<=j<=m,
J(i)=q+2-i if i<=q is even, and J(i)=i otherwise,
P_{m,i}=H(J(i)),  P_{m,0}=P_{m,m}.                        (4)
```

Here mod takes values 0,...,m-1. The floor errors obey
0<=alpha-beta<1/m and 0<=lambda-L<2/m. Also
s+q< m, since alpha+lambda<1; thus q<m and the entire block is unwrapped.
For q=2k, the odd block ranks are 1,3,...,q-1 and the even ranks are
q,q-2,...,2, each once. All ranks q+1,...,m are fixed. These disjoint
images partition {1,...,m}, and J is an involution. H is a bijection
onto {m+1,...,2m}, proving exact occurrence of every high radius once.
This includes q=0 and q=2, where J is the identity.

For q>=2, the actual highs are

```text
P_{m,i}=m+s+i                 (i<=q odd),
P_{m,i}=m+s+q+2-i             (i<=q even),
P_{m,i}=H(i)                 (i>q).
```

With t=i/m and A_m=1+beta, the interior pairs are EXACTLY

| Cells | Predecessor divided by m | Current high divided by m | Count |
|---|---|---|---|
| even i=2,...,q | A_m+t-1/m | A_m+L-t+2/m | q/2 |
| odd i=3,...,q-1 | A_m+L-t+3/m | A_m+t | q/2-1 |

All seams and exceptional comparisons are retained:

- At the low cyclic seam i=1, P_m=m+s for s>0 and P_m=2m for s=0;
  P_1=m+s+1 in both cases. The predecessor is never replaced by P_1.
- At i=q+1 (q>=2), the pair is (m+s+2,m+s+q+1).
- At i=r+1 when s>0, the high wrap is exactly (2m,m+1).
  For s=0 the wrap is the cyclic seam already counted.
- At i=r, P_r/m=2 but h(r/m)=alpha+r/m is on its lower branch,
  even when alpha*m is an integer. This comparison endpoint is set aside.

For q>=2 put X_m={1,q+1,r,r+1} intersect {1,...,m}.
Since r>=q+1, this set never meets the interior block. It has the
following exact counts, including coincident junction/endpoint cells:

| Condition | s>0 | s=0 |
|---|---|---|
| r>=q+2 | 4 | 3 |
| r=q+1 | 3 | 2 |

There are q-1 interior cells and m-q+1-|X_m| ordinary tail cells;
together with X_m they count exactly m. In the coincident case i=q+1=r,
the junction pair ends at 2m, and the next cell (if present) is the wrap.
For q=0 there is no block or junction: use X_m={1,r,r+1} intersect
{1,...,m}, of size 3 for s>0 and 2 for s=0, and m-|X_m| ordinary cells.
Here r>m/2>=1. These conventions cover every finite m, including m=2,3.

Outside X_m, each tail pair is

```text
(1+beta+t-1/m,1+beta+t)       for i<r,
(beta+t-1/m,beta+t)           for i>r+1.                  (5)
```

For q>=2 these cells also satisfy i>=q+2. The matching branch of h(t)
is respectively 1+alpha+t or alpha+t, so both coordinate errors are
at most 2/m. For every fixed lambda<b, eventually q>=2 and r>=q+2:
it suffices that lambda*m>=2 and (b-lambda)*m>1. In particular for
lambda=3/10, both hold for m>=7 using b>1/2.

## 3. Weak convergence for every continuous test

Define the empirical probability measure, with the actual cyclic predecessor,

```text
mu_m=(1/m) sum_{i=1}^m delta_(i/m,P_{m,i-1}/m,P_{m,i}/m).
```

Compare the m equally weighted actual triples with the following m atoms:

```text
(i/m,A+i/m,A+lambda-i/m)       if i<=q is even,
(i/m,A+lambda-i/m,A+i/m)       if i<=q is odd,
(i/m,h(i/m),h(i/m))           if i>q.
```

They all belong to D_box since q/m<=lambda<b. For sufficiently large m
as specified above, the coordinate error outside X_m is at most 3/m in
the max norm. In the odd reflected coordinate, for example, the error is
(beta-alpha)+(L-lambda)+3/m, lying in (0,3/m]; the other coordinates
follow from the same two floor bounds. The low coordinates agree exactly.

For F continuous on D_box, write M_F=||F||_infinity and omega_F for its
uniform modulus of continuity. If nu_m is the comparison measure, then

```text
|integral F dmu_m - integral F dnu_m|
 <= omega_F(3/m)+2*M_F*|X_m|/m
 <= omega_F(3/m)+8*M_F/m ->0.                            (6)
```

The q/2 atoms of each parity have mesh 2/m and weight 1/m, giving one
half of each Riemann integral on [0,lambda]. This includes the comparison
atom at i=1; its actual cyclic predecessor has already been paid for in
(6). The tail is a 1/m-mesh Riemann sum of F(t,h(t),h(t)); it is bounded
and continuous except possibly at b. Moving its lower endpoint from
q/m to lambda changes the integral by at most 2*M_F/m. The single wrap
and endpoint conventions have zero limiting mass. Therefore nu_m tends
to (1), and (6) proves mu_m -> mu_lambda for every continuous F along ALL
integers m. No polynomial-density assumption or Lipschitz assumption on
g near t=0 is needed.

For a bounded L_F-Lipschitz test, the same accounting gives the convenient
audit bound, once q>=2 and r>=q+2,

```text
|integral F dmu_m - integral F dmu_lambda|
 <= (6*L_F+16*M_F)/m.                                    (7)
```

Indeed the coordinate/exception errors give (3L_F+8M_F)/m; the two
parity sums give 2L_F/m; the tail gives (L_F+4M_F)/m after removing
at most two grid intervals meeting b; changing from reflection to
diagonal on [q/m,lambda] costs at most 4M_F/m.

## 4. Correct continuous full cost and possible switches

Set x=A+t, y=A+lambda-t and

```text
v_lambda(t)=sqrt(t/(A+t))+sqrt(t/(A+lambda-t)).
```

Both terms are strictly increasing in t>=0 on [0,lambda] (their
squared arguments have positive derivatives). Thus v_lambda(0)=0,
and the chord wins exactly when v_lambda(t)<=1. If v_lambda(lambda)<=1,
put z_lambda=lambda. Otherwise there is a unique z_lambda in (0,lambda)
with v_lambda(z_lambda)=1. This handles equality at the endpoint as well
as an actual branch change; no unsafe squaring is used to select a root.
The block cost is exactly

```text
B(lambda)=integral_0^z_lambda sqrt((A+t)*(A+lambda-t)) dt
 + integral_z_lambda^lambda
      sqrt(t)*(sqrt(A+t)+sqrt(A+lambda-t)) dt.             (8)
```

On the diagonal first branch h=A+t, the full switch is a=A/3; the chord
wins below a. The imported 0<alpha<1/2 implies a<b. On the wrapped
branch t>=b, h=alpha+t and t>alpha/3, so the chain sum always wins.
Hence the full tail, with every possible relative position of lambda
and a, is

```text
T(lambda)=integral_lambda^a (A+t) dt
           +2 integral_a^b sqrt(t*(A+t)) dt
           +2 integral_b^1 sqrt(t*(alpha+t)) dt,  lambda<=a;

T(lambda)=2 integral_lambda^b sqrt(t*(A+t)) dt
           +2 integral_b^1 sqrt(t*(alpha+t)) dt,  lambda>=a.

C_ref(lambda)=(B(lambda)+T(lambda))/(4*pi).                (9)
```

The formulas agree at lambda=a. Equivalently B is the integral of the
full max, and T is its diagonal integral. In general B CANNOT be replaced
by its chord integral beyond z_lambda. Equations (8)-(9) are exact
integral expressions, with no numerical root or quadrature premise.

## 5. Exact branch certificate and improvement at lambda=3/10

First obtain the coarse bound alpha_*>1/12 from the existing strictly
increasing D=K' on [0,1/2]. At alpha_0=1/12, its integration endpoints
are a_0=13/36 and b_0=11/12. The function
f_c(t)=sqrt(t/(t+c)) is concave for c>0,t>0 since

```text
f_c''(t)=-c*(4*t+c)/(4*t^(3/2)*(t+c)^(5/2))<0.
```

Upper-bound the first integral in D by midpoint rectangles on
[13/36,23/36] and [23/36,11/12], each of width 5/18 and with midpoints
1/2 and 7/9. Use one midpoint rectangle on [11/12,1], midpoint 23/24.
The three midpoint values are sqrt(6/19), sqrt(28/67), sqrt(23/25).
All signs in these exact rational square gates are positive:

```text
(281/500)^2-6/19=259/4750000>0,
(647/1000)^2-28/67=46803/67000000>0,
(24/25)^2-23/25=1/625>0,
2-(707/500)^2=151/250000>0,
11/12-(957/1000)^2=2453/3000000>0.
```

Inserting the upper bounds for the three midpoint values and lower
bounds for sqrt(2)-1 and sqrt(b_0) in the exact formula for D gives

```text
D(1/12)
 < 13/72+(5/36)*(281/500+647/1000)+(1/24)*(24/25)
       -(207/500)*(957/1000)
 = -17383/2250000 <0.
```

Strict increase and D(alpha_*)=0 prove

```text
13/12 < A < 3/2.                                         (10)
```

For lambda_0=3/10, v_lambda is increasing in t and decreasing in A.
At its worst comparison endpoint use x_0=13/12, y_0=83/60. The
inequality v_lambda(lambda)<1 is equivalent to
lambda*(x+y+2sqrt(x*y))<x*y. Both squaring gates are explicit:

```text
H=x_0*y_0-lambda_0*(x_0+y_0)=2731/3600>0,
H^2-4*lambda_0^2*x_0*y_0=466441/12960000>0.                (11)
```

Thus lambda_0*(x_0+y_0+2sqrt(x_0*y_0))<x_0*y_0, and by (10) the
reflected block at the actual A uses the chord strictly throughout.
Also lambda_0<13/36<A/3, so the removed diagonal block uses the chord.
At ell=1/4 both chord statements follow already from t<=1/4,x,y>=1.

For either ell in {1/4,3/10}, put M_ell=A+ell/2 and define

```text
delta(ell)=integral_(-ell/2)^(ell/2)
                  [M_ell-sqrt(M_ell^2-u^2)] du.
C_ref(ell)=C_shift-delta(ell)/(4*pi).                     (12)
```

This follows by centering the reflected chord integral: the removed
diagonal integral is ell*M_ell. For u!=0 its saving integrand is

```text
u^2/(M_ell+sqrt(M_ell^2-u^2)).
```

Its denominator is strictly below 2*M_ell away from zero and strictly
above 2*A everywhere, since sqrt(M_ell^2-u^2)>=sqrt(A*(A+ell))>A.
Integration, using integral u^2 du=ell^3/12, proves

```text
ell^3/(24*M_ell) < delta(ell) < ell^3/(24*A).
```

By (10), M_(3/10)<33/20 and A>13/12. Therefore

```text
delta(3/10)>3/4400,
delta(1/4)<1/1664,
delta(3/10)-delta(1/4)>3/4400-1/1664=37/457600>0.           (13)
```

Equations (12)-(13) prove (3). This is an analytic exact inequality;
the bounded checker only audits the displayed rational arithmetic.
Numerically, as observations rather than premises,

```text
C_ref(1/4) = 0.1419538534197848532950...,
C_30       = 0.1419245920564058523022...,
C_ref-C_30 = 0.00002926136337900099285....
```

## 6. Uniform transfer to the full root and global consequence

The bijection in Section 2 permits the exact all-pairs criterion of
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md), Sections 1-6:

```text
S_m(R)=sum_i max(theta_R(i,P_{m,i-1})+theta_R(i,P_{m,i}),
                 theta_R(P_{m,i-1},P_{m,i})),
R_full(sigma_m)=the unique root of S_m(R)=2*pi.             (14)
```

No exceptional cell is deleted from (14). Section 4 of
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md)
proves, uniformly over all high permutations,

```text
R_full(sigma_m)/(2m)^2 = (integral g dmu_m)/(4*pi)+O(1/m).
```

That theorem brackets the root on a compact positive scale BEFORE using
the expansion at the root. It permits arbitrarily many high jumps and
retains the max at ties. Section 3 and continuity of g on D_box give
convergence of its integrals, proving (2) without a chain-root shortcut.

At lambda=3/10, the full criterion gives feasible even configurations at
rho_m=R_full(sigma_m). Hence R*(2m)<=rho_m. Deleting only radius 2m
preserves every central tangency and pairwise non-overlap and leaves
exactly {1,...,2m-1}, so R*(2m-1)<=rho_m. Since (2m/(2m-1))^2->1,

```text
limsup_{n->infinity} R*(n)/n^2 <= C_30
 < C_ref - 37/(1830400*pi) < C_ref < C_shift.              (15)
```

This is only a global upper bound. The existing C_term lower bound is
unchanged; no endpoint sharpness, normalized global limit, finite global
optimum, or contact/floating conclusion follows.

## 7. Verification and ownership

The [task evidence](../ops/TASK-20260905__reflected_prefix/EVIDENCE.md)
records bounded exact occurrence/predecessor/seam audits, including
q=0,2 and r=q+1, exact polynomial moments against independently expanded
integrals, rational sign gates, and separate high-precision full-cost and
root diagnostics. The checker uses only the standard library and canonical
mpmath; it imports neither production code, verify.py nor older checkers.
Numerics select and corroborate the single witness; Sections 2-6 prove it.

Recovery, branch formulas and the fixed-order coefficient have the sole
claim owner knowledge/FIXED_ORDER_THEORY.md. Only the global deletion
corollary is owned by knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md. Earlier notes
and dossiers preserve their scope. Independent external review of this
proof and its imported dependencies remains pending. General recovery,
best lambda, reoptimization of alpha, and general permutation/coupling
optimization remain outside the result.
