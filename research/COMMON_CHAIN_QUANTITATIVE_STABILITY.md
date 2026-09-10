# Quantitative stability for one common pair of terminal chain tours

    status=PROVED
    classification=exact theorem / quantitative asymptotic stability / proved global corollary
    domain=all cyclic orders; all integers n>=10^14
    proved_on=2026-09-10
    published_snapshot=arXiv v1 remains unchanged

## 1. Statement and exact scope

Import only the terminal optimizer and its coefficient from
[the terminal-bound proof](INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md),
Sections 5-7. In this note q always denotes the terminal lower endpoint:

```text
tau=cos(tau), 0<tau<pi/2,
q=q_*=(1-sin(tau))/(1+sin(tau))=1/lambda_*,
C=C_term=tau/(pi*(1+sin(tau))),
pi*C=integral_q^1 sqrt(x*(1+q-x)) dx,
beta=23/100,
k=floor(q*n), ell=floor(beta*n),
T_q(n)={k,...,n}, T_beta(n)={ell,...,n}.
```

Restriction retains the original radii and joins cyclically successive
survivors. For every integer n>=10^14 and every cyclic order sigma of
T_q(n), the following implication holds:

```text
R_chain(sigma) <= (C+10^-12)*n^2
    implies
R_chain(sigma|T_beta(n)) >= (C+10^-5)*n^2.                 (1)
```

Thus the requested statement is **true**, with explicit
epsilon=10^-12 and delta=10^-5. The constants and sufficient cutoff are
not asserted sharp. No search at the cutoff is needed or proposed.

Sections 2-7 concern precisely these two chain costs. Section 8 transfers
their incompatibility to R_full and R*, with the same constants and cutoff.
It proves R*(n)>(C+10^-12)*n^2 and liminf R*(n)/n^2>=C+10^-12.
No minimizing common tour, optimized cutoff or general tradeoff, upper
construction, finite certification or public-paper revision is supplied.
Independent mathematical acceptance remains separate from this proof.

## 2. Uniform reduction to sqrt-product edge costs

For any cyclic order omega of at least three distinct radii in {1,...,n},
define

```text
S(omega)=sum_{cyclic edges (u,v)} sqrt(u*v),
W(omega)=S(omega)/n^2,
r(omega)=R_chain(omega)/n^2.
```

Every edge angle is continuous and strictly decreasing in R>0, tending
from pi to zero, so the closure sum has a unique positive 2*pi root.
The half-angle identity and elementary asin/atan inequalities give

```text
theta_R(u,v)=2 asin(sqrt(u*v)/sqrt((R+u)*(R+v)))
           =2 atan(sqrt(u*v)/sqrt(R*(R+u+v))),
2*sqrt(u*v)/(R+n) <= theta_R(u,v) <= 2*sqrt(u*v)/R.
```

Sum at the root, rearranging the two inequalities in their stated
directions. This proves the exact, order-uniform sandwich

```text
S(omega)/pi-n <= R_chain(omega) <= S(omega)/pi,
W(omega)/pi-1/n <= r(omega) <= W(omega)/pi.                (2)
```

It applies simultaneously to the outer and restricted cycles, including
every new closing edge. There is no assumed root scale, parity condition,
or hidden order-dependent error constant. In particular the hypothesis
of (1) implies W(sigma)<=pi*C+pi*epsilon+pi/n, while a lower bound on the
restricted W transfers with loss at most 1/n in its normalized root.

## 3. Anti-Monge exchange and a quantitative reflected-pair bound

For now let a=k/n, s=1+a, N=n-k+1, x_i=i/n for k<=i<=n,
and f(x,y)=sqrt(x*y) on [a,1]^2. Its anti-Monge exchange slack is exactly

```text
f(x,y)+f(x',y')-f(x,y')-f(x',y)
 = (sqrt(x')-sqrt(x))*(sqrt(y')-sqrt(y))>0
                                           (x<x', y<y').        (3)
```

The Supnick exchange structure pairs opposite ranks up to one mesh step.
To quantify that structure for every competing cycle, rather than infer
stability from finite uniqueness, put c=s/2 and define the dual potential

```text
h(x)=c/2 + (1/2)*integral_c^x sqrt((s-t)/t) dt.
```

Differentiation and evaluation at x=c give
h(x)+h(s-x)=f(x,s-x). For fixed x, set
H(x,y)=f(x,y)-h(x)-h(y). It vanishes at y=s-x, and

```text
partial_y H(x,y)
 = (x+y-s)/(2*sqrt(y)*(sqrt(x)+sqrt(s-y))).                 (4)
```

The denominator lies in [4*a,4]. Integrate from s-x to y, reversing
both the orientation and sign when y<s-x. In either case,

```text
(x+y-s)^2/8 <= H(x,y) <= (x+y-s)^2/(8*a).                  (5)
```

This is the quantitative anti-Monge estimate used below. It is derived
directly; no matrix perturbation theorem or finite uniqueness gap is a
premise. Define the reflected assignment reference

```text
J_n=(1/n)*sum_{i=k}^n f(x_i,s-x_i),
e=W(sigma)-J_n,
d_e=x+y-s for an outer edge with normalized endpoints x,y.
```

Here the subscript on d_e labels an edge; the standalone e is excess cost.
Reflection permutes this finite grid, so sum_i f(x_i,s-x_i)=2*sum_i h(x_i).
Each tour vertex has degree two. Summing (5) once per undirected cyclic
edge therefore yields

```text
e >= 0,
(1/n)*sum_edges d_e^2 <= 8*e,
A:=(1/n)*sum_edges |d_e| <= sqrt(8*e).                    (6)
```

The last inequality is Cauchy-Schwarz with N/n<=1. J_n is an assignment
lower bound, not in general the cost of a Hamiltonian cycle: reflection
may have two-cycles and, for odd N, a fixed middle vertex. This does not
affect the degree-two identity or (6).

For clarity, this reference is asymptotically the actual Supnick minimum.
The exact edges in [the fixed-k note](FIXED_K_SUPNICK_SEAM.md), Section 1,
have sums n+k-1, n+k, or n+k+1 in both parities, including the seam and
even-cardinality middle edge. Hence |d_e|<=1/n for that tour, and (5) gives

```text
0 <= W(Supnick(T_q(n)))-J_n <= 1/(8*a*n^2).               (7)
```

The published Supnick theorem identifies this as the minimizing tour;
alternatively (6)-(7) already give the needed asymptotic minimum without
importing its optimality. The middle reflection fixed point is permitted
only in the lower reference, not inserted into a tour.

## 4. Restriction is stable even with consecutive deleted vertices

Assume n>=102. The rational optimizer bracket proved in Section 6 gives

```text
1/6 < a <= q < 1/5,  q < b:=ell/n <= beta,
s-2*b >= 7/6-23/50 = 53/75 > 1/2.                       (8)
```

Both cycles have at least three vertices. Let L be the deleted vertices
k,...,ell-1. For x in their normalized range define

```text
t=s-x,
D_a(x)=t-2*sqrt(x*t),
D_n=(1/n)*sum_{i=k}^{ell-1} D_a(i/n).
```

We prove the uniform finite tradeoff

```text
|W(sigma|T_beta(n))-W(sigma)-D_n| <= 60*sqrt(e).           (9)
```

Partition the deleted vertices into maximal runs in the cyclic traversal.
Each run is flanked by survivors; if the run crosses a written starting
point, rotate the traversal to a survivor first. Distinct runs account
for all removed edges and all replacement edges exactly once.

For an isolated deleted vertex x with surviving neighbors y,z, the cost
change before the outer factor 1/n is

```text
g(x;y,z)=f(y,z)-f(x,y)-f(x,z).
```

At y=z=t it is D_a(x). On [a,1]^3 each of the two partial derivatives
of g in y,z has absolute value at most 1/sqrt(a)<3 (bound its two terms
separately). The line segments to (t,t) stay in that domain. Thus

```text
|g(x;y,z)-D_a(x)| <= 3*(|y-t|+|z-t|).
```

These absolute differences are the defects of the two edges incident
to x. An edge is counted at most once across isolated deletions.

For a nonisolated run of r>=2 deleted vertices, the exact cost change
is one replacement weight minus r+1 removed weights. All normalized
weights are between zero and one, so its absolute value is at most
r+1<=2*r. Also |D_a(x)|<=2, giving discrepancy at most 4*r from the
sum of its ideal changes. If E_LL is the number of original edges with
both endpoints deleted, the total number of vertices in such runs is
at most 2*E_LL, since r<=2*(r-1) in each run. Their discrepancy is
therefore at most 8*E_LL.

Every LL edge has x,y<b and, by (8), |x+y-s|>1/2. Hence
E_LL<=2*sum_edges |d_e|. Combining the isolated and nonisolated bounds,
and reinstating the common factor 1/n, gives

```text
|W(restriction)-W(sigma)-D_n|
 <= (3+16)*A <= 20*sqrt(8*e) <= 60*sqrt(e).
```

This proves (9). In particular it does not assume that competing tours
delete independent low vertices, nor that their induced edges follow the
prescribed Supnick traversal. Rotations, reversals and closing runs are
included by the same cyclic edge accounting.

## 5. Explicit floor estimates

Write F_a(x)=sqrt(x*(1+a-x)) and

```text
J=integral_q^1 F_q(x) dx=pi*C,
D=integral_q^beta D_q(x) dx.
```

For n>=102, all factors in the following comparisons lie in [1/6,1].
On their domains, direct derivatives give the convenient bounds

```text
|partial_x F_a(x)|<=3,       |partial_a F_a(x)|<=3/2,
|F_a(x)|<=1,
|partial_x D_a(x)|<=7,       |partial_a D_a(x)|<=2,
|D_a(x)|<=2.                                                   (10)
```

For example, each coordinate derivative of sqrt(x*t) is at most
sqrt(6)/2<3/2; D_a(x)=1+a-x-2*F_a(x) gives the x bound, while
partial_a D_a=1-sqrt(x/(1+a-x)) gives the stated a bound.

The inclusive sum J_n differs from integral_a^1 F_a by at most
(3/2+1)/n: use left rectangles of width 1/n and then the extra endpoint
term F_a(1)/n. Moving a to q removes an interval of length less than 1/n
at cost at most 1/n and changes the integrand on [q,1] by at most
(3/2)/n. Thus

```text
|J_n-pi*C| <= 5/n <= 6/n.                                  (11)
```

D_n is exactly the left sum on [a,b]. Its rectangle error is at most
7/(2*n). Remove [a,q], compare parameter a with q on [q,b], and add
[b,beta]; the three costs are at most 2/n, 2/n and 2/n respectively.
Here b>q by (8). Consequently

```text
|D_n-D| <= 19/(2*n) <= 10/n.                               (12)
```

No floor of the transcendental number q is evaluated numerically. Only
0<=q-a<1/n and 0<=beta-b<1/n are used. Neither estimate selects a
cardinality parity. The assignment identity, run counts and root
sandwich likewise hold for both outer and restricted parities.

## 6. Exact positive margin at beta=23/100

The rational Taylor gates in
[the macroscopic discriminator](MACROSCOPIC_TERMINAL_DISCRIMINATOR.md),
Section 5, prove 3/17<q<1/5. For reproducibility their premises are
P_6(73/100)>73/100, P_4(3/4)<3/4,
Q_7(73/100)>2/3, Q_5(3/4)<7/10, where P and Q are the alternating
cosine and sine Taylor polynomials of those degrees. Monotonicity of
cos(t)-t and sine gives 2/3<sin(tau)<7/10, then the stated q bracket.
All four gates are exact rational inequalities; the checker repeats them.

For q<=x<=beta set t=1+q-x. Then t<=1 and
t-4*x=1+q-5*x>20/17-23/20=9/340>0. Therefore D_q(x)>0
on that whole interval. On its subinterval [1/5,23/100], also
t>=20/17-23/100=1609/1700>9/10. Rationalization gives

```text
D_q(x)=t-2*sqrt(x*t)
      = t*(t-4*x)/(t+2*sqrt(x*t))
      > (9/10)*(9/340)/3 = 27/3400.
```

The denominator is at most 3 since x,t<=1. Integrating only over
that subinterval, retaining positivity on the omitted part, proves

```text
D > (3/100)*(27/3400)=81/340000 > 1/5000=:m.                (13)
```

This is a quantitative version of the prescribed-order excess. By (9),
it persists uniformly whenever the outer excess e is sufficiently small.

## 7. Constants and completion of the implication

Suppose r(sigma)<=C+epsilon. From (2), (6) and (11), using pi<4,

```text
0<=e<=pi*epsilon+(pi+6)/n <= 4*epsilon+10/n.                (14)
```

Combining (9), (11)-(13) first at the edge-cost level gives

```text
W(sigma|T_beta(n))
 >= pi*C+m-16/n-60*sqrt(4*epsilon+10/n).                   (15)
```

Finally (2) gives the order-uniform root tradeoff

```text
r(sigma|T_beta(n))
 >= C + [m-20/n-60*sqrt(4*epsilon+10/n)]/pi.               (16)
```

Take epsilon=10^-12 and n>=10^14. Then

```text
4*epsilon+10/n <= 5*10^-12 < ((5/2)*10^-6)^2,
60*sqrt(4*epsilon+10/n) <= 3/20000,
m-3/20000-20/10^14 = 1/20000-20/10^14 > 4/100000.
```

Since pi<4, (16) is strictly greater than C+1/100000, proving (1)
with the requested non-strict conclusion. All hypotheses used above
already hold at n>=102, so the stated larger cutoff also covers them.
This completes the proof through all integer sizes and all cyclic orders.

## 8. Global corollary by deletion from a full feasible configuration

**Status: proved corollary, after arXiv v1.** With exactly the constants
of (1), for every integer n>=10^14,

```text
R*(n) > (C_term+10^-12)*n^2,
liminf_{n->infinity} R*(n)/n^2 >= C_term+10^-12.           (17)
```

Here R_full(omega) is the minimum all-pairs-feasible radius for a fixed
cyclic order omega of {1,...,n}, and R*(n)=min_omega R_full(omega).
The proof also works with fixed-order infima, without assuming their
attainment. R_chain remains the closure root of the adjacent-angle sum;
it is not identified with either geometric optimum.

**Deletion at the same geometric radius.** By (8),
1<=k<ell<=n-2, so T_beta(n) is contained in T_q(n) and both sets have
at least three radii, for either cardinality parity. Take any full
feasible configuration of {1,...,n} at R>0, with cyclic order omega.
Its centers have the form

```text
p_a=(R+a)*(cos(phi_a),sin(phi_a)),
|p_a-p_b|>=a+b                 for all distinct a,b.
```

For either retained set T, keep the same R, radii and centers. Every
central tangency and every surviving pairwise distance inequality is
unchanged. Let g_i be the positive directed gaps between consecutive
survivors in omega|T, including the closing gap; their sum is 2*pi.
For such an edge (a,b), the smaller angular separation is
Delta_i=min(g_i,2*pi-g_i). The
[published angular reformulation](../paper_assets/ringmin_paper.tex) gives

```text
Delta_i>=theta_R(a,b),
theta_R(a,b)<=g_i<=2*pi-theta_R(a,b),
sum_{edges of omega|T} theta_R(a,b)<=2*pi.
```

This covers gaps larger than pi, arbitrary consecutive deletions and
the wrap edge. The new adjacency uses an existing full pairwise
constraint; no triangle inequality for deleted chain edges is assumed.
Strict decrease of the closure sum and its unique root now imply
R_chain(omega|T)<=R. Deletion need not make the surviving circles
mutually tangent, or make their chain root fully feasible.

Put sigma=omega|T_q(n). Since restriction only removes entries,
sigma|T_beta(n)=omega|T_beta(n), as cyclic orders. Thus both chain roots
belong to the same common tour and satisfy, simultaneously,

```text
max{R_chain(sigma),R_chain(sigma|T_beta(n))} <= R.
```

Neither retained set is translated or rescaled; n^2 always refers to
the original largest radius n. For fixed omega the two roots are fixed
numbers, independent of the positions and of R. Taking the infimum over
all feasible configurations in that order therefore gives

```text
max{R_chain(sigma),R_chain(sigma|T_beta(n))}
    <= R_full(omega).                                  (18)
```

**Strict bound before global minimization.** Write
A_n=(C+10^-12)*n^2 and B_n=(C+10^-5)*n^2, so B_n>A_n.
If R_full(omega)<=A_n, (18) implies R_chain(sigma)<=A_n.
The all-order theorem (1) then gives

```text
B_n <= R_chain(sigma|T_beta(n)) <= R_full(omega) <= A_n,
```

a contradiction. Hence R_full(omega)>A_n for every omega. For each fixed
n there are only finitely many cyclic orders, so their minimum is also
strictly greater than A_n. This proves the first part of (17), without
inferring a strict infimum bound merely from R>A_n for feasible radii.

Dividing by n^2 and taking the liminf proves the second part of (17).
Strictness at each finite n does not assert a strict liminf above
C+10^-12, or a lower coefficient C+10^-5. No constants from Sections 1-7
were changed or optimized. This is an analytic global lower bound, not
a finite optimum certificate, a sharp coefficient or a convergence theorem.

## 9. Evidence and ownership

The all-order inequalities, floor estimates and limiting scope are analytic.
The [bounded standalone checker](../ops/TASK-20260910__common_chain_stability/check_stability.py)
audits rational gates, symbolic identities, exact cyclic run accounting,
small prescribed edge-cost examples and numerical root sandwiches. It
imports no production implementation or saved result, does no tour search,
and is not a finite global certificate. Numerical checks are observations,
not premises of (1). Its exact ranges and outputs are in the dossier.

The global transfer in Section 8 is analytic. Its
[task evidence](../ops/TASK-20260910__common_chain_global_corollary/EVIDENCE.md)
records the directed-gap, nested-order, fixed-order-infimum and finite-minimum
checks, together with exact algebra and the unchanged rational constants.
No new enumeration or numerical experiment is used for this corollary.

The sole stable owner is the common-chain-stability entry in
[the global ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
The earlier prescribed-order proof and its historical limited scope remain
unchanged; this note supplies the additional uniform argument.
