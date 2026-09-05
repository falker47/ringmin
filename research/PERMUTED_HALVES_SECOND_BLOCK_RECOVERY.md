# Deterministic recovery of the fixed second reflected block

```text
status=PROVED
classification=exact finite construction / exact weak-recovery theorem
domain=alpha=alpha_hat; lambda=(1+alpha_hat)*x_*; second block [1/3,103/300]; every integer m>=2
quantitative_recovery=every continuous test; estimate (12) for m>=200
full_root_transfer=not applied in this task
proved_on=2026-09-06
published_snapshot=arXiv v1 unchanged
```

## 1. Fixed inputs, target and result

Import exactly the constants and baseline coupling from
[the joint-prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md),
Sections 1-3, and the fixed witness from
[the continuum second-block theorem](PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md),
Sections 2 and 7. Define

```text
alpha=alpha_hat, A=1+alpha, lambda=A*x_*, b=1-alpha,
u=1/3, epsilon=1/100, v=u+epsilon=103/300,
h(t)=1+{t+alpha}, D=[0,1] x [1,2]^2,
AL=1093/10000 < alpha < AH=10931/100000,
XL=719/2500 < x_* < XH=2877/10000,
LL=(1+AL)*XL < lambda < LH=(1+AH)*XH.                 (1)
```

These are exact implicit constants and imported strict rational brackets,
not decimal definitions. No parameter is selected or optimized here.
For a continuous test F on D write

```text
f_1^+(t)=F(t,A+t,A+lambda-t),
f_1^-(t)=F(t,A+lambda-t,A+t),
f_2^+(t)=F(t,A+t,A+u+v-t),
f_2^-(t)=F(t,A+u+v-t,A+t),
f_0(t)=F(t,h(t),h(t)).
```

The required probability measure mu_2 is precisely

```text
integral F dmu_2
 = (1/2)*integral_0^lambda (f_1^+ + f_1^-) dt
   +integral_lambda^u f_0 dt
   +(1/2)*integral_u^v (f_2^+ + f_2^-) dt
   +integral_v^1 f_0 dt.                              (2)
```

Endpoint values in these integrals have zero mass. This retains the
baseline prefix and every other diagonal slab, including the wrapped
tail. It is exactly mu_(1/3,1/100) of the continuum note. Its marginal
and balance properties are already proved there; they are not premises
for the finite construction below.

**Recovery theorem.** For every integer m>=2, formula (4) gives a
deterministic permutation P^(2)=(P^(2)_1,...,P^(2)_m) of {m+1,...,2m}.
We suppress m in the component subscripts. With the actual cyclic
predecessor P^(2)_0=P^(2)_m,

```text
mu_m^(2)=(1/m)*sum_(i=1)^m delta_(i/m,P^(2)_(i-1)/m,P^(2)_i/m)
   -> mu_2 weakly along all integers m->infinity.       (3)
```

Equation (12) bounds the error for every continuous F. This is a
recovery theorem for one specified coupling. No general sufficiency
theorem for marginals/local balance, finite radius comparison or new
geometric bound is inferred.

## 2. Finite floors and the two disjoint parity reversals

For every integer m>=2 set

```text
s=floor(alpha*m), q=2*floor(lambda*m/2), r=m-s,
p=2*floor(m/6), d=2*floor(m/200), e=p+d,
beta=s/m, L=q/m, U=p/m, W=d/m, V=e/m,
H(j)=m+1+((j+s-1) mod m), 1<=j<=m.

J(i)=q+2-i,       if 1<=i<=q and i even;
     2*p+d+2-i,   if p<i<=e and i even;
     i,          otherwise.

P^(2)_i=H(J(i)), 1<=i<=m,    P^(2)_0=P^(2)_m.          (4)
```

Mod takes values 0,...,m-1. Empty blocks have no active case. In
particular d=0 for m<200. This defines the family without random
choices, subsequences, permutation search or decimal rounding of a
minimizer. Floor has its usual value also at an exact integer tie.

Put

```text
delta_alpha=alpha-beta, delta_lambda=lambda-L,
delta_u=u-U, delta_w=epsilon-W.
0<=delta_alpha<1/m,
0<=delta_lambda,delta_u,delta_w<2/m,
v-V=delta_u+delta_w,
(u+v)-(2*U+W)=2*delta_u+delta_w<6/m.                  (5)
```

All q,p,d,e are even. Since lambda<u, monotonicity of floor gives
q<=p, so the rank intervals {1,...,q} and {p+1,...,e} are disjoint
for EVERY m. Also e<=v*m and q<=lambda*m, hence s+e<m and s+q<m:
neither block wraps under H. The following convenient rational gates
follow directly from (1):

```text
u-LH>1/100,   1-AH-v>1/2,   1-AH-LH>1/2,
6*LH<2<7*LL, 12*LH<4<13*LL, 9*AH<1<10*AL.           (6)
```

When d>0, m>=200 and

```text
p-q > m*(u-lambda)-2 > m/100-2 >=0,
r-e >= m*(b-v)>m/2,
U>u-2/m>=u-1/100>lambda,
V>u, since W>=2/m>delta_u.                            (7)
```

Thus p>=q+2 and r>=e+2 whenever the second block is active. These
strict inequalities rule out coincident block junctions or a second
block meeting the finite wrap. They are proved, not assumed from an
asymptotic picture. For q>0, (6) gives m>=7 and r-q>m/2, so the
prefix exit cannot coincide with r either.

For the first block write q=2k. Its odd ranks stay 1,3,...,q-1;
at i=2j, j=1,...,k, the images are 2(k+1-j), listing every even
rank exactly once in reverse order. For the second block write d=2h.
At i=p+2j-1 the image is p+2j-1; at i=p+2j it is

```text
J(p+2j)=p+2(h+1-j), j=1,...,h.                        (8)
```

These list its h odd ranks increasingly and its h even ranks
decreasingly, each once. All other ranks are fixed. The disjoint
images partition {1,...,m}, and J(J(i))=i. Since H is bijective,
each high radius occurs exactly once in P^(2), and exactly once in
its cyclic predecessor list. A fixed even rank at a reflection
midpoint is one occurrence, not two. Blocks of length 0 or 2 have
identity rank map, including d=2 for 200<=m<=399.

The construction covers odd and even m. The p-floor has period 6
in its residual, the d-floor period 200; neither imposes divisibility
on m. It first changes the baseline high order at m=400, when d=4.

## 3. Exact predecessors, junctions, wrap and complete counts

Write t=i/m and A_m=1+beta. In a nonempty block with start a and
even length l, where (a,l) is (0,q) or (p,d), the interior cells
a+2<=i<=a+l have the exact normalized pairs

| Cells | P^(2)_(i-1)/m | P^(2)_i/m | Count |
|---|---|---|---|
| even i | A_m+t-1/m | A_m+(2*a+l)/m-t+2/m | l/2 |
| odd i | A_m+(2*a+l)/m-t+3/m | A_m+t | l/2-1 |

These follow from the preceding position's parity in (4), not from
an independently assigned pair. There is no assumption that the
two orientations are equal for a nonsymmetric test F.

Use the set of exceptional comparison cells

```text
X_m=({1,r,r+1}
     union {q+1 : q>0}
     union {p+1,e+1 : d>0}) intersect {1,...,m}.        (9)
```

The notation includes or excludes the displayed sets according to
the condition. In particular a zero-length second block creates no
ghost junction. These actual pairs are always retained:

| Cell and condition | Actual ordered pair (P^(2)_(i-1),P^(2)_i) |
|---|---|
| i=1, s=0 | (2m,m+1) |
| i=1, s>0 | (m+s,m+s+1) |
| i=q+1, q>0 | (m+s+2,m+s+q+1) |
| i=p+1, d>0 | (m+s+p,m+s+p+1) |
| i=e+1, d>0 | (m+s+p+2,m+s+e+1) |
| i=r | (2m-1,2m) |
| i=r+1, s>0 | (2m,m+1) |

The cyclic predecessor at i=1 is P^(2)_m, never a missing or
linearly extrapolated value. For s=0 the high wrap is that same
cyclic cell, while r+1=m+1 is out of range. At i=r the actual current
high is 2m, but h(r/m)=alpha+r/m lies on the lower branch, even
if alpha*m is an integer. This extra comparison exception is not
another high jump. At d=2 the second entry/exit are ordinary shift
pairs; retaining them in X_m is deliberate and harmless.

The interiors in the preceding table are disjoint from X_m. Every
remaining cell is ordinary diagonal, with pair

```text
(A_m+t-1/m,A_m+t), if i<r;
(beta+t-1/m,beta+t), if i>r+1.                         (10)
```

The bounds (6)-(7) and the empty-block convention give this complete
finite count, including the smallest cases:

| m | s and active blocks | Interior cells | Exceptional cells | Ordinary cells |
|---|---|---:|---:|---:|
| 2..6 | s=0, q=d=0 | 0 | 2 | m-2 |
| 7..9 | s=0, q>=2, d=0 | q-1 | 3 | m-q-2 |
| 10..199 | s>0, q>=2, d=0 | q-1 | 4 | m-q-3 |
| >=200 | s>0, q,d>=2 | q+d-2 | 6 | m-q-d-4 |

In every row the three counts sum to m. Also q=2 for 7<=m<=12;
the corresponding odd interior count is zero. The formula treats
s=0 and the wrap/seam coincidence through m=9, both parities, all
floor ties, and both length-2 identity blocks. No cell is deleted
from the measure; its exceptional mass is exactly |X_m|/m<=6/m.

For a concrete finite example the strict brackets alone give at m=600

```text
(s,q,p,d,e,r)=(65,190,200,6,206,535).
J(201),...,J(206)=(201,206,203,204,205,202).
P^(2)_201,...,P^(2)_206=(866,871,868,869,870,867).
```

The second entry is (865,866), the second exit is (867,872), and
the separate high wrap is (1200,601) at i=536. All are genuine
cyclic-list pairs; no assertion concerns their geometric radius.

## 4. Quantitative recovery for arbitrary continuous tests

Let M=||F||_infinity and let omega_F(delta) be the uniform modulus of
continuity on D in the max norm. Fix any m>=200. For each i introduce
one comparison atom at t_i=i/m:

- in 1<=i<=q use the triple defining f_1^+ for even i and f_1^-
  for odd i;
- in p<i<=e use the triple defining f_2^+ for even i and f_2^-
  for odd i;
- elsewhere use (t_i,h(t_i),h(t_i)).

Their equally weighted probability measure is nu_m. On the second
finite interval [U,V] these formulas slightly extend the target
reflection left of u. They still lie in D: U>lambda, V<=v<b,
the reflected high is at least A+u, and at most A+v+delta_u<2
by (5)-(7). The prefix and diagonal atoms also lie in D.

Outside X_m the actual triple has the same t coordinate. The prefix
errors are <=3/m as is also seen directly in its predecessor table.
The second reflected-coordinate errors are precisely

```text
-delta_alpha-2*delta_u-delta_w+2/m, if i even;
-delta_alpha-2*delta_u-delta_w+3/m, if i odd.
```

They belong respectively to (-5/m,2/m] and (-4/m,3/m]. Its other
high-coordinate errors are <=2/m. On ordinary cells, i<r implies
t_i<=1-(s+1)/m<b, and i>r+1 implies t_i>b. Thus the branches of
h match (10) with errors <2/m. At i=r and the actual wrap no such
approximation is used. Consequently

```text
|integral F dmu_m^(2)-integral F dnu_m|
 <=omega_F(5/m)+12*M/m.                               (11)
```

To bound the Riemann error, compare nu_m with the integral having
the same f_1^+/- on [0,L], f_2^+/- on [U,V], and f_0 on the
complement. The continuous block maps use the TRUE lambda,u,v,A;
only their integration endpoints have temporarily moved.

In each block the even grid samples are right endpoints of panels
of length 2/m, and odd samples are their midpoints. This holds in
the second block because p is even. Each sample has weight 1/m,
so each orientation approximates half the block integral. All three
coordinates of each affine triple have slopes of absolute value 1.
Their combined Riemann error is at most (L+W)*omega_F(2/m).
The comparison sums include each block's initial odd sample, whose
actual predecessor has already been paid for in (11).

Every complementary diagonal interval has endpoints on the 1/m grid.
Set aside the at most two grid panels whose closures contain the
single wrap b; their total error is <=4*M/m, even when b is exactly
a grid point. The remaining diagonal error is at most
(1-L-W)*omega_F(1/m). Thus the total Riemann error is bounded by
omega_F(2/m)+4*M/m.

It remains to restore the target intervals. Since L<=lambda<U and
U<=u<V<=v by (7), the prefix change costs at most
2*M*(lambda-L)<4*M/m. The symmetric difference of [U,V] and [u,v]
has length

```text
(u-U)+(v-V)=2*delta_u+delta_w<6/m.
```

On its complement the second-block integrands agree exactly, not
just approximately; the boundary change therefore costs <12*M/m.
All other parts, including the wrapped tail, are identical. Combining
the three errors proves the explicit estimate

```text
|integral F dmu_m^(2)-integral F dmu_2|
 <=omega_F(5/m)+omega_F(2/m)+32*||F||_infinity/m,
                                                     m>=200. (12)
```

Since F is continuous on compact D, both moduli tend to zero.
This proves (3) along the entire integer sequence. The finitely many
2<=m<200 are already genuine permutations with the complete counts
in Section 3; the trivial error bound there is 2*M. In particular
no subsequence divisible by 6, 200 or 600 is being substituted.
For an L_F-Lipschitz test, (12) gives the convenient bound
(7*L_F+32*M)/m. Lipschitz regularity is not required for recovery.

## 5. Simultaneous preservation of the baseline and scope of the result

Let P^(0) be the exact baseline finite order at the same m, obtained from (4)
by omitting only the second reversal. For m<200 the two orders
coincide; they also coincide for 200<=m<=399 because d=2. When
d>0, they differ only at even positions inside {p+1,...,e}.
Thus their empirical triples can differ only at cells p+2,...,e+1;
the second entry p+1 is identical. The first prefix, its exit,
the low cyclic seam, and the high wrap are untouched. This is a
finite preservation statement, in addition to the simultaneous
recovery of ALL parts of (2).

The imported baseline recovery then also gives the signed limit

```text
integral F d(mu_m^(2)-mu_m^(0))
 -> (1/2)*integral_u^v [f_2^+(t)+f_2^-(t)-2*f_0(t)] dt.
```

The positive result is therefore constructive; no realizability
obstruction arises for this specified block. It does not assert
that every balanced coupling can be recovered or that arbitrary
collections of reflected blocks can be combined without further
floor/predecessor analysis.

For g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)), continuity
on D permits F=g in (12). Hence the empirical g integrals converge
to the already proved continuum cost of mu_2. Its strict continuum
saving remains the theorem in the earlier note. This statement
about integrals is not a statement about R_chain, R_full or R*(n).

The separate full-root transfer is in
[the three-marginal note](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Sections 2 and 4, using
[the all-pairs fixed-order criterion](PERMUTED_ALTERNATING_HALVES.md).
This task does not apply it. A subsequent atomic transfer must
explicitly match the constructed alternating order, true cyclic
predecessors and every cell to that criterion, retain both max
branches, verify the uniform root-scale/error hypotheses, and
justify all-pairs feasibility and any odd-n deletion separately.
No new full-radius limit, finite-m improvement or geometric global
upper bound is recorded here; the owning global ledger keeps C_hat.

## 6. Verification and authority

Sections 2-4 are the exact finite construction and analytic recovery
proof. The [bounded independent checker](../ops/TASK-20260905__second_block_recovery/check_recovery.py)
audits the specified formula against a separate rotation/list-reversal
implementation, scores predecessors directly from that list, and
overcovers every possible alpha/lambda floor pair using (1). Its
bounded range m=2..1201 includes two complete periods of m modulo
600, both identity-block thresholds, wrap cases and endpoint ties.
This is a scan of rounding cases for ONE construction, not an
enumeration or optimization of high permutations.

Exact interval checks of polynomial tests enclose the integrals at
the SAME implicit alpha/lambda; no surrogate decimal minimizer is
used to decide a floor. Finite checks audit bookkeeping, not the
all-m theorem. Independent external review of this proof and of its
imported dependencies remains separate. Exact commands, limitations
and provenance are in [the task evidence](../ops/TASK-20260905__second_block_recovery/EVIDENCE.md).
The sole thematic owner is knowledge/FIXED_ORDER_THEORY.md. Previous
proof notes/dossiers, the public paper, certificates and production
implementation remain unchanged.
