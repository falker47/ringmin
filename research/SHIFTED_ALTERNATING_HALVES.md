# Shifted alternating-halves: exact full feasibility and optimal shift

```text
status=PROVED
classification=exact finite fixed-order theorem / exact asymptotic and family-minimization theorem / proved global limsup corollary
domain=integer m>=2, 0<=s<m; sequences s/m->alpha in [0,1]
proved_on=2026-09-05
published_snapshot=arXiv v1 remains unchanged
```

## 1. Statement and definitions

Write

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
L_i=i,  P_i=m+1+((i+s-1) mod m),  1<=i<=m,
sigma_{m,s}=(L_1,P_1,...,L_m,P_m).
```

All subscripts on L and P are cyclic. At fixed R>0 put

```text
A_i=theta_R(L_i,P_i),  B_i=theta_R(P_i,L_{i+1}),
C_i=theta_R(P_{i-1},P_i),
Q_{m,s}(R)=sum_i (A_i+B_{i-1}),
S_{m,s}(R)=sum_i max(A_i+B_{i-1},C_i).                (1)
```

The maximum compares the SUM of the two adjacency requirements with the
high-high chord. For every m>=2 and every shift, full feasibility at R is
equivalent to S_{m,s}(R)<=2*pi. Thus R_chain(sigma_{m,s}) and
R_full(sigma_{m,s}) are respectively the unique roots of Q=2*pi and S=2*pi.
Sections 2-3 prove this without importing the unshifted all-pairs argument.

For 0<=alpha<1 let h_alpha(t)=1+{t+alpha}, where braces mean fractional part;
values at its single jump do not affect integrals. Put h_1=h_0 and define

```text
J(alpha)=integral_0^1 sqrt(t h_alpha(t)) dt,
K(alpha)=integral_0^1 max(sqrt(t h_alpha(t)),h_alpha(t)/2) dt.    (2)
```

For EVERY sequence of integer shifts s_m/m->alpha in [0,1],

```text
R_chain(sigma_{m,s_m})/(2m)^2 -> J(alpha)/(2*pi),
R_full(sigma_{m,s_m})/(2m)^2 -> K(alpha)/(2*pi).        (3)
```

K has a unique minimizer alpha_* on [0,1], lying in (0,1/2), characterized
by the explicit derivative equation (11) below. In particular

```text
K(alpha_*)<K(0)=3sqrt(2)/4-1/12
                    +(log(3)-log(3+2sqrt(2)))/8.
```

Deletion from the even constructions proves only the global corollary

```text
limsup_{n->infinity} R*(n)/n^2 <= C_shift=K(alpha_*)/(2*pi)<C_alt.
                                                               (4)
```

Here C_alt=K(0)/(2*pi) is the preceding alternating-halves upper coefficient.
The minimization theorem is within this shift family, not over all orders.
Neither global optimality, sharpness of (4), nor existence of a normalized
global limit follows. Decimal evaluations in Section 8 are diagnostic only.

## 2. Thick shell and both high-high paths

We reprove a slightly stronger shell lemma to remove any dependence on where
the increasing high sequence wraps. Fix 0<u<=v<=2u. Then

```text
2 theta_R(u,u)>=theta_R(v,v).                         (5)
```

Indeed, x=u/(R+u) lies in (0,1), and z=v/(R+v)<=2x/(1+x).
If x>=1/sqrt(2), then 2 asin(x)>=pi/2>asin(z). Otherwise

```text
(1+x)^2(1-x^2)-1=x(2-2x^2-x^3)>0,
```

since the decreasing last factor is at least 1-1/(2sqrt(2))>0 on
0<x<=1/sqrt(2). Hence z<=2x sqrt(1-x^2)=sin(2 asin(x)); both
asin(z) and 2 asin(x) are in [0,pi/2]. This proves (5).

Consequently, for ANY three radii a,b,c in [u,v], with any middle radius b,

```text
theta_R(a,b)+theta_R(b,c)
 >=2 theta_R(u,u)>=theta_R(v,v)>=theta_R(a,c).         (6)
```

An induction now shows that the sum of angular edge requirements along every
nonempty high path is at least the direct requirement of its endpoints.
This does not require the path to be increasing. In this task every P_i lies
in [m+1,2m], a shell of ratio strictly less than 2. Contract each valley
P_{i-1}->L_i->P_i into an edge whose length is at least C_i. Apply (6)
independently to each of the two cyclic high paths between any distinct high
endpoints. Both paths obey the required direct angle.

For m=2 these are the two distinct one-cell paths between the same two high
vertices; each already has its own bound C_i. No three-vertex argument or
long-complement assumption is needed in this smallest case.

## 3. Fixed-R necessity, construction and every endpoint type

In any feasible placement, each of the two gaps of valley i is at least its
adjacent angle, and their sum is at least the P_{i-1},P_i pair angle along
that path. The cells partition all gaps. Summation gives S<=2*pi, proving
necessity without discarding the complementary pair constraints.

For sufficiency, set e_i=[C_i-A_i-B_{i-1}]_+ and choose

```text
g(L_i,P_i)=A_i+e_i,
g(P_i,L_{i+1})=B_i.                                  (7)
```

Each cell has length max(A_i+B_{i-1},C_i); all these gaps are positive and
sum to S. First check every path with these base gaps, before closing to 2*pi:

- High-high endpoints: each direction consists of a nonempty chain of whole
  valley cells. Section 2 bounds each chain by its endpoint angle.
- Low-high endpoints L_i,P_j: each direction first reaches one of L_i's two
  neighboring highs. If that high is P_j, the adjacent gap already suffices.
  Otherwise the rest is a nonempty contracted high path, whose length is at
  least theta_R(P_neighbor,P_j)>=theta_R(L_i,P_j). The first gap is
  nonnegative. This applies independently to both directions, including the
  complement of an adjacent low-high pair.
- Distinct low-low endpoints L_i,L_j: in either direction the path starts
  by reaching a high U and ends by leaving a high V. If U!=V, the intervening
  whole-cell high path has length at least theta_R(U,V)>=theta_R(L_i,L_j),
  since every high exceeds every low. If U=V, this is the two-edge path
  through their common high; its first gap alone is at least
  theta_R(L_i,U)>=theta_R(L_i,L_j). This includes cyclically consecutive
  lows, and both complementary common-high paths when m=2.

Add E=2*pi-S>=0 to any one gap, for instance g(P_m,L_1). For each pair
this increases one path and leaves the other unchanged; both already satisfy
their lower constraints. Their new sum is 2*pi, so the exact angular model
gives Cartesian non-overlap and a closed placement in the prescribed order.

There are two index discontinuities to keep distinct. The LOW seam is the
cell i=1 through L_1, preceded by P_m. The HIGH wrap is the cell with
P_{i-1}=2m and P_i=m+1: it is i=m-s+1 if s>0, and i=1 if s=0.
For nonzero shifts these are different cells. Equation (7) handles either
chord exactly; (6) handles every path crossing either or both seams. No seam
has been removed or replaced by an asymptotic estimate in this proof.

Every term in Q and S is continuous and strictly decreasing in R (the max
of these strictly decreasing functions is also strictly decreasing).
Both sums tend to 2*pi*m as R decreases to zero and to zero as R tends to
infinity. Since m>=2, each has a unique root at level 2*pi. Necessity and
sufficiency identify the full root, including equality. This completes (1).

## 4. Uniform scaling, moving wrap and the two different limits

Let n=2m, R=rn^2 with r in any compact positive interval. Uniformly over
1<=a,b<=n,

```text
theta_{rn^2}(a,b)=2sqrt(ab)/(rn^2)+O(n^-2).            (8)
```

For completeness, with v=sqrt(ab)/R and
u=sqrt(ab/((R+a)(R+b))), denominator rationalization gives
0<=v-u<=v(a+b)/(2R)=O(n^-2), while asin(u)-u=O(n^-3).
This is uniform even for a fixed low radius or one that is o(n).

Put t_i=i/m and beta_m=s_m/m. Except at the single high-wrap cell, consecutive
highs differ by 1, and P_i/m is t_i+1+beta_m before the wrap and t_i+beta_m
after it. Square roots on the high shell have uniformly bounded derivative.
Thus each ordinary cell has, with h=P_i/m,

```text
A_i+B_{i-1}=sqrt(t_i h)/(r m)+O(m^-2),
C_i=h/(2r m)+O(m^-2).                                (9)
```

The exceptional high-wrap cell is O(1/m) in either sum by (8). The low seam
does not disturb (9) when it is not also the high wrap: both adjacent angles
in (1) use the SAME low L_i, so there is no hidden replacement of L_m by L_1.
One may alternatively discard both seam cells; their total is still O(1/m).
Lipschitz continuity of max transfers the errors in (9) to S.

These are triangular Riemann sums with a moving jump. If beta_m->alpha,
outside a small interval about t=1-alpha they converge uniformly to the
two continuous branches in (2); the integrands are uniformly bounded by
sqrt(2) (chain) and sqrt(2) (full). The omitted interval and cells have mass
bounded by a constant times its length plus O(1/m). First let m tend to
infinity, then shrink the interval. This also works when alpha=0 or 1:
the short wrapping or nonwrapping interval tends to an endpoint and has
vanishing mass. The endpoint choice h_1=h_0 is correct almost everywhere.
It follows that Q(rn^2)->J(alpha)/r and S(rn^2)->K(alpha)/r.

Both constants are positive. For any epsilon strictly between zero and the
corresponding coefficient, evaluate these sums at (coefficient +/- epsilon)
times n^2. Their limits lie strictly on opposite sides of 2*pi. Monotonicity
brackets the unique roots, proving (3) without assuming their scale.
Moreover K(alpha)>J(alpha) for every alpha: a positive initial interval has
h_alpha(t)>4t (and the same holds for h_1=h_0). This fixed-order chain/full
distinction persists at leading order.

## 5. Explicit functional and active-cell regimes

Write b=1-alpha, a=(1+alpha)/3, and d=log(3)/8-1/12. For c>0 define

```text
F_c(t)=(2t+c)sqrt(t(t+c))/4
       -c^2/8 log((2t+c+2sqrt(t(t+c)))/c),
F_0(t)=t^2/2.
```

Direct differentiation gives F_c'(t)=sqrt(t(t+c)), F_c(0)=0. Thus

```text
J(alpha)=F_{1+alpha}(b)+F_alpha(1)-F_alpha(b).
```

On a branch h=t+c, the high-high chord wins exactly when t<=c/3, by
nonnegative squaring. On the first branch 0<=t<b the switch is a; it is
inside that branch iff alpha<=1/2. On the second branch b<=t<=1 the switch
is alpha/3; it enters that branch iff alpha>=3/4. Since
F_c(c/3)=c^2(5/18-log(3)/8), integration gives

```text
K(alpha) =
  F_{1+alpha}(b)+F_alpha(1)-F_alpha(b)+d(1+alpha)^2,
                                         0<=alpha<=1/2;
  b^2/4+(1+alpha)b/2+F_alpha(1)-F_alpha(b),
                                         1/2<=alpha<=3/4;
  b/2+F_alpha(1)+d alpha^2,                3/4<=alpha<=1.       (10)
```

The formulas agree at both internal endpoints, where an active interval
has zero length. K(1)=K(0), recovering exactly the earlier unshifted
coefficient. This identifies all leading active cells, including the
regime in which the shifted high wrap passes through an active switch.

## 6. Rigorous unique minimum; the diagnostic is not a premise

For 0<=alpha<=1/2, differentiation under the split integrals gives

```text
D(alpha)=K'(alpha)
 =a/2 + (1/2) integral_a^b sqrt(t/(t+1+alpha)) dt
      + (1/2) integral_b^1 sqrt(t/(t+alpha)) dt
      -(sqrt(2)-1)sqrt(b).                            (11)
```

The moving interior switch cancels because the two values agree there.
The last term is the jump contribution at the moving high wrap: the left
value is sqrt(2b), the right value sqrt(b), and b'=-1. Omitting this term
would give the wrong variation.

Let

```text
T=integral_a^b sqrt(t)/(t+1+alpha)^(3/2) dt
  +integral_b^1 sqrt(t)/(t+alpha)^(3/2) dt.
```

Another differentiation, retaining all endpoints, gives

```text
K''(alpha)=1/12+(1-1/sqrt(2))sqrt(b)/2
                 +(sqrt(2)-1)/(2sqrt(b))-T/4.          (12)
```

Both high branches are >=1 and t<=1, so each integrand in T is <=1.
Their total interval length is 1-a<=2/3. Since 1/2<=b<=1, (12) implies

```text
K''(alpha)>(sqrt(2)-1)/2-1/12>0,
```

where the final sign follows already from sqrt(2)>7/6. Therefore D is
strictly increasing on this interval.

The right derivative at zero is exactly

```text
D(0)=5/6-sqrt(2)/2-(1/2)log((1+sqrt(2))/sqrt(3))<0.    (13)
```

Here is a rational sign proof. For z>1,
log(z)>2(z-1)/(z+1), as follows by differentiating their difference from
z=1. The square gates sqrt(2)>7/5 and sqrt(3)<7/4 give
z=(1+sqrt(2))/sqrt(3)>48/35. Hence

```text
D(0)<5/6-7/10-13/83=-29/1245<0.
```

At alpha=1/2, a=b=1/2 and the remaining integral's integrand is at least
1/sqrt(2), so

```text
D(1/2)>=5/(4sqrt(2))-3/4>0.                           (14)
```

Thus a unique alpha_* in (0,1/2) solves D(alpha_*)=0. Strict convexity
makes it the unique minimum on [0,1/2], strictly below K(0).

To exclude the other regimes, on 1/2<alpha<3/4 (10) gives

```text
K'(alpha)=b/2-1+sqrt(b)
                 +(1/2) integral_b^1 sqrt(t/(t+alpha)) dt,
K''(alpha)=-1/2-1/(2sqrt(b))+sqrt(b)/2
                 -(1/4) integral_b^1 sqrt(t)/(t+alpha)^(3/2) dt<0.
```

This branch is strictly concave, so its minimum is at an endpoint.
On 3/4<alpha<1,

```text
K'(alpha)=-1/2+2d alpha
                 +(1/2) integral_0^1 sqrt(t/(t+alpha)) dt<0.    (15)
```

For the sign, log(3)<4/3 by the strict trapezoid upper bound for the
convex function 1/t on [1,3], so d<1/12 (and d>0 since log(3)>2/3).
The function t->sqrt(t/(t+alpha)) is concave; explicitly its second
derivative is

```text
-alpha(4t+alpha)/(4 t^(3/2)(t+alpha)^(5/2))<0  (t>0).
```

Jensen's inequality therefore bounds half its integral by
1/(2sqrt(1+2alpha))<=1/sqrt(10)<1/3. Together with 2d alpha<1/6,
this proves (15). Consequently K(3/4)>K(1)=K(0)>K(alpha_*).
Also K(1/2)>K(alpha_*); concavity excludes every middle-branch point.
The decreasing last branch has minimum K(1)>K(alpha_*). This proves unique
global minimization of K on [0,1], entirely analytically.

One can also allow arbitrary shift sequences without a limiting ratio.
Compactness of [0,1] and the every-sequence version of (3) imply that the
minimum of R_full(sigma_{m,s})/(2m)^2 over 0<=s<m converges to C_shift.
Every asymptotically minimizing sequence has s/m->alpha_*. This is still
only a statement about this family, not all cyclic orders.

## 7. Deletion and the precise global consequence

Choose s_m=floor(alpha_* m). These are legal shifts and s_m/m->alpha_*.
For even n=2m, (7) at the full root is an actual feasible configuration, so
R*(2m)<=R_full(sigma_{m,s_m}). For odd n=2m-1 delete just the outer circle
of radius 2m from that same configuration. All surviving central tangencies
and pairwise non-overlap constraints persist, and the surviving radii are
exactly 1,...,2m-1. Therefore

```text
R*(2m-1)<=R_full(sigma_{m,s_m}).
```

The ratio (2m/(2m-1))^2 tends to one; (3) gives (4) on both parity
subsequences. No identification of the odd induced order as a shifted
alternating-halves order is needed. The unchanged lower theorem still gives

```text
C_term <= liminf R*(n)/n^2 <= limsup R*(n)/n^2 <= C_shift < C_alt.
```

The owning global ledger defines C_term and links its independent proof.
This task does not change that lower theorem or close the coefficient gap.

## 8. Independent checks and limitations

Task-local sources and exact commands are recorded in
`ops/TASK-20260905__shifted_alternating_halves/EVIDENCE.md`. Analytic proof
is Sections 2-7; the numerical search is never its premise. Independent
high-precision evaluation gives the numerical observations

```text
alpha_*                  =0.1067847601999001993458136785...,
K(alpha_*)/(2*pi)         =0.1419959781277142849792181240...,
K(107/1000)/(2*pi)        =0.1419959794984599508468255895...,
K(0)/(2*pi)              =0.1423338536193127549063856822....
```

Thus the exploratory signal near 0.107 and 0.141996 is reproduced, with the
distinction between the rational witness 107/1000 and the exact implicit
minimizer retained. The exact arithmetic checker separately encloses
K(107/1000)/(2*pi) in (0.14199597949,0.14199597951); together with the
proved minimum it yields, if a rational bound is preferred,

```text
limsup R*(n)/n^2 < 0.14199597951 < C_alt.
```

This enclosure uses directed rational sqrt/log/pi bounds, not floating
rounding or an optimizer. The checker brackets each square root using an
integer square root on a 10^-35 grid. It reduces logarithms to y in [1,2]
using powers of 2, then uses z=(y-1)/(y+1) and the first 80 terms of
2 sum_{j>=0} z^(2j+1)/(2j+1), with tail between zero and
2 z^161/(161(1-z^2)). For pi it uses the Machin identity
pi=16 atan(1/5)-4 atan(1/239), the 80-term alternating sums and the next-term
error; rational tangent addition verifies the identity with the angle in
(0,pi/2). Interval operations retain their direction through F and division
by 2*pi. Thus the displayed rational separators are exact finite arithmetic
inequalities. The exact constant in (4) is stronger.
Finite all-pairs checks at selected shifts and sizes corroborate the exact
construction, including angular and Cartesian constraints and a separate
all-pairs feasibility formulation near the cell root. They do not certify
global optima, prove the asymptotic theorem, or determine subleading terms.
Independent human proof review remains pending; the paper, production code,
standalone verifier and finite certificates are unchanged.
