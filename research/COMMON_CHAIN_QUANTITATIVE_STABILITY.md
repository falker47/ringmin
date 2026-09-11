# Quantitative stability for one common pair of terminal chain tours

    status=PROVED
    classification=exact theorem / asymptotic minimax lower bound / proved global corollary
    domain=all cyclic orders; finite stability n>=10^14; minimax estimate n>=102
    proved_on=2026-09-10
    midpoint_split_optimized_on=2026-09-11
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

Sections 2-7 retain this finite theorem. Section 8 retains its original
global transfer with the same constants and cutoff. Section 9 optimizes
the asymptotic consequence of the stated deletion estimate (9), using
the actual integral D rather than its coarse lower bound m. Define

```text
B_n=min_{sigma cyclic on T_q(n)}
          max{R_chain(sigma), R_chain(sigma|T_beta(n))},
eta_60=D^2/(3600*pi),
D=integral_q^(23/100) [1+q-x-2*sqrt(x*(1+q-x))] dx.
```

The new exact theorem and full-feasible-deletion corollary are

```text
R*(n) >= B_n,
B_n/n^2 >= C+eta_60-3/n                         (n>=102),
liminf B_n/n^2 >= C+eta_60,
liminf R*(n)/n^2 >= C+eta_60,
5.1529885884211781970537738e-10 < eta_60
                              < 5.1529885884211781970537739e-10.
```

In particular R*(n)>=B_n>(C+5.152e-10)*n^2 for n>=10^14.
The coefficient eta_60 is sharp for the scalar information in (2),
e>=0, (9), (11)-(12), not asserted sharp for tours or for refinements
of the deletion proof. No minimizing common tour, optimized cutoff,
upper construction, finite certification or public-paper revision is supplied.
Independent mathematical acceptance remains separate from this proof.

Section 12 refines this lower bound using Section 11, with additive
coefficient eta_split determined by a monotone cubic after the exact
midpoint-split optimization. The preceding coefficient eta_new remains
a valid weaker bound with its original provenance. Sections 2-10 and
the family proofs in Sections 11.5-11.6 retain their statements; the
strongest current finite and asymptotic consequences are (42)-(48) below.

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
A_n=(C+10^-12)*n^2 and U_n=(C+10^-5)*n^2, so U_n>A_n.
If R_full(omega)<=A_n, (18) implies R_chain(sigma)<=A_n.
The all-order theorem (1) then gives

```text
U_n <= R_chain(sigma|T_beta(n)) <= R_full(omega) <= A_n,
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

## 9. Asymptotic two-level minimax with the actual deletion integral

**Status: exact analytic lower-bound theorem / proved global corollary.**
Throughout this section q=q_* and beta=23/100 are fixed. The minimax B_n
is defined in Section 1; both restrictions use the original radii and
the ambient normalization n^2. No order enumeration is involved.

### 9.1 Preserve the outer excess on both branches

For any outer tour write W=W(sigma), W'=W(sigma|T_beta(n)) and
e=W-J_n>=0. Equations (2) and (9) imply, uniformly in the order,

```text
max{r(sigma),r(sigma|T_beta(n))}
 >= [J_n+max{e,e+D_n-60*sqrt(e)}]/pi-1/n.                 (19)
```

The positive e in the second branch matters: replacing W by J_n before
optimizing would lose information. One must minimize the maximum over a
single common e, not minimize the two roots independently.

Here is the exact scalar optimization, for any K>0 and 0<d<K^2/2:

```text
min_{e>=0} max{e,e+d-K*sqrt(e)} = d^2/K^2.               (20)
```

Set t=sqrt(e), t_0=d/K. If t>=t_0, the first branch is at least
t_0^2. If 0<=t<=t_0, the second branch dominates and

```text
t^2+d-K*t-t_0^2 = (t_0-t)*(K-t_0-t) >= 0.
```

The second factor is positive because 2*t_0<K. Equality in the
minimax occurs at t=t_0, where both branches equal t_0^2.
This is a global argument on e>=0, including arbitrarily large excess,
and does not presume that a minimizing sequence has e near zero.

For n>=102, Section 4 gives a>1/6 and x<b<=23/100 for every deleted
vertex. Thus 1+a-5*x>7/6-23/20=1/60>0, so D_a(x)>0. The deleted
set is nonempty and |D_a(x)|<=2; consequently 0<D_n<2<1800.
Use (20) with K=60,d=D_n in (19) and take the finite minimum over
outer tours. This proves the exact finite bound

```text
B_n/n^2 >= J_n/pi + D_n^2/(3600*pi)-1/n.                 (21)
```

Since J_n->pi*C and D_n->D>0, it already follows that

```text
liminf B_n/n^2 >= C+eta_60,    eta_60=D^2/(3600*pi)>0.    (22)
```

No interchange of a limit and an order-dependent minimum is needed:
(21) is uniform and holds before the limit. In the limit, the equivalent
root-excess envelope is

```text
max{u, u+D/pi-(60/sqrt(pi))*sqrt(u)},       u>=0.
```

Its crossing is u=eta_60. At that point both branches equal eta_60;
their maximum cannot be strictly above it on the whole scalar domain.
The formal scalar data e=D^2/3600 and W'=W=pi*C+e obey the limiting
deletion estimate with equality. Thus (22) is the strongest coefficient
forced by these aggregate scalar inequalities. Such scalar data are
not a construction of tours or configurations. This ceiling applies
to the stated 60*sqrt(e) estimate (9); it does not limit a sharper
deletion estimate, including reworking the unrounded run estimates in
Section 4, nor does it upper-bound B_n or R*(n).

### 9.2 Exact enclosure of the actual integral

All terminating decimals in this subsection denote exact rationals.
The following strict brackets are verified by rational Taylor gates:

```text
0.7390851332151606416553120876738734040134 < tau
  < 0.7390851332151606416553120876738734040135,
0.1950200913506069300798071259134151019366 < q
  < 0.1950200913506069300798071259134151019367,
3.1415926535897932384626433832795028841971 < pi
  < 3.1415926535897932384626433832795028841972.            (23)
```

For explicit reproduction, let P_j,Q_j be the degree-j cosine and sine
Taylor polynomials at zero and let tau_-,tau_+ denote the displayed
endpoints. Alternating remainders on (0,1) give

```text
P_82(tau_-)>tau_-,        P_80(tau_+)<tau_+,
Q_83(tau_-)<sin(tau)<Q_81(tau_+).
```

Strict decrease of cos(t)-t proves the tau bracket. Apply the decreasing
map v -> (1-v)/(1+v) to the two sine bounds and compare rationally with
the displayed q endpoints. For pi use Machin's identity
pi=16*atan(1/5)-4*atan(1/239). Its angle identity follows from
tan(4*atan(1/5))=120/119 and
(120/119-1/239)/(1+120/(119*239))=1, on the branch (0,pi/2).
The alternating atan sums through indices 40 and 41 enclose each atan;
subtract in the outward directions and compare with (23).

To enclose D without floating quadrature, set q_0 to the lower rational
endpoint for q in (23), s_0=1+q_0, z_q=(1-q_0)/s_0 and
z_b=(s_0-2*beta)/s_0. Then 0<z_b<z_q<1 and

```text
D(q_0,beta)=s_0*(beta-q_0)-(beta^2-q_0^2)/2-2*I,
I=(s_0^2/4)*integral_(z_b)^(z_q) sqrt(1-z^2) dz.
```

Use the convergent expansion with positive decreasing coefficients

```text
sqrt(1-z^2)=1-sum_{j>=1} c_j*z^(2*j),
c_1=1/2,       c_(j+1)=c_j*(2*j-1)/(2*(j+1)).
```

With M=80, termwise integration and a geometric majorant of the tail give

```text
I_+=(s_0^2/4)*[z_q-z_b
       -sum_{j=1}^M c_j*(z_q^(2*j+1)-z_b^(2*j+1))/(2*j+1)],
T=(s_0^2/4)*(z_q-z_b)*c_(M+1)*z_q^(2*M+2)/(1-z_q^2),
I_+-T <= I <= I_+.
```

Every expression is rational. To restore the true q, differentiate the
integral with its moving lower endpoint:

```text
partial_q D(q,beta)=-D_q(q)
     + integral_q^beta [1-sqrt(x/(1+q-x))] dx.
```

The bounds |D_q(q)|<=2 and |partial_q D_q(x)|<=2 from (10) give
|partial_q D(q,beta)|<=4 throughout the tiny q bracket. Thus add an
outward error 4*(q_+-q_-)=4*10^-40 to the rational integral enclosure.
The exact calculations yield

```text
0.00241410289623904895465331017 < D
  < 0.00241410289623904895465331018.                       (24)
```

Squaring the positive endpoints of the internal (unrounded) enclosure
and dividing by 3600 times the opposite pi endpoint gives

```text
5.1529885884211781970537738e-10 < eta_60
  < 5.1529885884211781970537739e-10.                       (25)
```

The [standalone exact checker](../ops/TASK-20260910__two_level_minimax_bound/check_minimax.py)
implements precisely these rational sums and comparisons with fixed term
counts. No numerical solver or floating evaluation is a premise of
(23)-(25). The optional independent 80/120-dps quadrature and elementary
antiderivative checks are only numerical corroboration.

### 9.3 Finite error, strictness and transfer to the full problem

Equations (11)-(12) hold for every n>=102. By (24), D<1/100, while
0<D_n<2. Therefore

```text
|D_n^2-D^2| <= (10/n)*(D_n+D) < 21/n,
B_n/n^2 >= C+eta_60-[1+(6+21/3600)/pi]/n
         >= C+eta_60-3/n.                                (26)
```

The last comparison is an exact rational consequence of the lower pi
endpoint in (23). In particular, for every fixed 0<eta'<eta_60 and
every integer n>=102 with n>3/(eta_60-eta'),

```text
B_n > (C+eta')*n^2.                                      (27)
```

This is finite strictness at a smaller coefficient, not at eta_60.
Equation (25) gives the convenient explicit instance

```text
B_n > (C+5.152e-10)*n^2                for every n>=10^14. (28)
```

For the global transfer, take any full feasible order omega at radius R
and apply Section 8's directed-gap argument separately to T_q(n) and
T_beta(n). Both induced chain roots are at most R, including their
new closing edges, and the smaller restriction belongs to the same
sigma=omega|T_q(n). For each fixed omega, taking the infimum over its
full feasible configurations gives, exactly as in (18),

```text
R_full(omega) >= max{R_chain(sigma),R_chain(sigma|T_beta(n))}
             >= B_n.
```

Now minimize over the finitely many full orders to conclude

```text
R*(n) >= B_n                         (n>=102),
liminf R*(n)/n^2 >= C+eta_60.                              (29)
```

Combining with (28) gives R*(n)>(C+5.152e-10)*n^2 for n>=10^14.
This uses actual full-feasible deletion only; deletion from a chain at
its root was never asserted feasible. No attainment assumption is needed.

Both (22) and (29) have a non-strict comparison at C+eta_60. Since
eta_60 is strictly greater than the rational lower endpoint in (25),
they also give strict liminf comparisons with that smaller endpoint
added to C. Neither fact implies liminf>C+eta_60, eventual finite
strictness at C+eta_60, equality, convergence, or geometric optimality.
The explicit improvement is more than 515 times 10^-12, but less than
5.153e-10 in absolute coefficient. This quantifies the limited output
of (9), without claiming a ceiling on the broader two-level method.

## 10. Evidence and ownership

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

Section 9's [task evidence](../ops/TASK-20260910__two_level_minimax_bound/EVIDENCE.md)
records the exact integral and coefficient enclosures, scalar minimax,
finite-error gates, optional independent symbolic/high-precision checks,
and the scope of the scalar ceiling. The prior finite theorem and its
checker remain unchanged. These are analytic bounds with exact-arithmetic
support, not finite Ringmin optimum certificates.

The sole stable owner is the common-chain-stability entry in
[the global ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
The earlier prescribed-order proof and its historical limited scope remain
unchanged; this note supplies the additional uniform argument.

## 11. The square-root loss is not sharp for actual cyclic tours

**Status: exact theorem / proved uniform little-o corollary, after arXiv v1.**
Keep exactly q=q_*, beta=23/100, k, ell, a, s, W, J_n and D_n from
Sections 1-4. For every integer n>=102 and every genuine cyclic order
sigma on {k,...,n}, put

```text
e=W(sigma)-J_n,
Delta=W(sigma|T_beta(n))-W(sigma)-D_n.
```

Then the following uniform improvement holds:

```text
|Delta| <= 24*e^(2/3)+432*e.                              (30)
```

In particular, for every 0<e<=epsilon the quotient satisfies

```text
|Delta|/sqrt(e) <= 24*epsilon^(1/6)+432*sqrt(epsilon) -> 0
                                                   as epsilon -> 0. (31)
```

The supremum implicit here ranges over all n>=102 and all their cyclic
orders with 0<e<=epsilon. Thus no deterministic or other family of actual
tours with e->0 can have |Delta|>=c*sqrt(e) for a fixed c>0. The bound
alone does not assert that exponent 2/3 is sharp for the signed Delta.
Section 11.5 proves sharpness for the nonnegative crossing term K;
Section 11.6 proves it for signed Delta using that same cyclic family.
The optimized midpoint split below replaces the original coefficient 40
by 24 without changing any structural premise. Section 12 propagates
this coefficient through the scalar minimax and global lower bound.
Neither 60, beta, q nor the other deletion estimates are optimized here.

### 11.1 Exact finite measure and a midpoint cutoff

Let V={k/n,...,1}, r(x)=s-x and

```text
E=(1/n)*sum_{undirected cyclic edges {x,y}} (x+y-s)^2.
```

Here, as in Section 3, an undirected edge is counted once in the cycle.
Equation (6) gives E<=8*e. Replace each cyclic edge by its two orientations
(x,y) and (y,x), and define the finite measure

```text
mu=(1/(2*n))*sum_{oriented edges (x,y)} delta_(x,r(y)),
nu=(1/n)*sum_{x in V} delta_x.
```

Both marginals of mu equal nu exactly: each vertex occurs twice as a
first endpoint, twice as a second endpoint, and r permutes V. Consequently
for every function F on V,

```text
integral [F(x)-F(z)] dmu(x,z)=0,
integral (x-z)^2 dmu(x,z)=E.                              (32)
```

These are finite identities, not a continuum approximation. A reflection
fixed point when n-k+1 is odd changes neither identity; it is a coordinate
in the measure, not a loop added to the tour. The measure's total mass is
(n-k+1)/n, with the normalization above unchanged.

Place the cutoff at

```text
B=(ell-1/2)/n.
```

For x in V, x<B is exactly the condition that x is deleted. No grid
point equals B, and each grid point has distance at least 1/(2*n) from B.
For every real h>0 the following exact bound holds:

```text
nu({x: |x-B|<=h}) <= 4*h.                                (33)
```

Indeed the set is empty if h<1/(2*n). Otherwise its grid-point count
is at most 2*n*h+1, whose mass is at most 2*h+1/n<=4*h.
Truncation at k/n or 1 only decreases that count. This midpoint choice
removes a possible mesh error even when h is smaller than a grid step.

### 11.2 Deletion equals a signed first variation up to O(E)

For x in [a,1] define

```text
p(x)=(1-sqrt(x/(s-x)))/2,
P(x)=p(x)*1_{x<B},
L=(1/n)*sum_{deleted vertices x} p(x)*sum_{y adjacent to x}(x+y-s)
 =2*integral P(x)*(x-z) dmu(x,z).                         (34)
```

All adjacent vertices in the sums refer to the original cyclic tour.
In particular L includes both endpoints of any LL edge. The factor 2
in (34) follows from the mass 1/(2*n) for each oriented edge.

Consider an isolated deleted vertex x with surviving neighbors y,z and
t=s-x. Use g(x;y,z) from Section 4. Its two first derivatives at (t,t)
are both p(x), and g(x;t,t)=D_a(x). Its Hessian in (y,z) has entries

```text
g_yy=(sqrt(x)-sqrt(z))/(4*y^(3/2)),
g_zz=(sqrt(x)-sqrt(y))/(4*z^(3/2)),
g_yz=1/(4*sqrt(y*z)).
```

Throughout [a,1]^3, with a>1/6, the absolute diagonal entries are less
than 4 and the off-diagonal entries are less than 2. For example,
1/(4*a^(3/2))<3*sqrt(6)/2<4. The symmetric Hessian has operator norm
at most 6, so Taylor's theorem along the segment from (t,t) to (y,z)
gives

```text
|g(x;y,z)-D_a(x)-p(x)*[(y-t)+(z-t)]|
 <= 3*[(y-t)^2+(z-t)^2].                                 (35)
```

The segment stays in [a,1]^2. Summed over isolated deleted vertices,
each incident edge occurs at most once; after division by n their total
Taylor error is at most 3*E.

For all nonisolated maximal deleted runs, let M_LL be the number of
original edges with both endpoints deleted and V_bad their total number
of deleted vertices. Section 4's exact cyclic accounting gives

```text
V_bad<=2*M_LL,
|total discrepancy of these runs|<=8*M_LL/n.
```

For completeness, a run of length m>=2 replaces m+1 edges by one edge.
Each weight lies in [0,1], so its cost change has absolute value at most
m+1<=2*m. Subtracting its m ideal changes, each of absolute value at
most 2, costs at most 4*m. Also m<=2*(m-1); summing proves these bounds.
For every deleted x, 0<p(x)<1/2 because x<B<b<s/2. Since every defect
has absolute value at most 1-a<1, the part of L incident to the bad
vertices has absolute value at most V_bad/n<=2*M_LL/n.
Every LL edge has |x+y-s|>1/2 by (8); hence M_LL/n<=4*E. Combining
the isolated and nonisolated contributions proves

```text
|Delta-L| <= 3*E+10*M_LL/n <= 43*E.                       (36)
```

Runs partition removed and replacement edges even when a run crosses the
written start: rotate to a survivor first. The surviving set has at least
three vertices, so this operation always exists and produces exactly its
cyclic restriction, including the final replacement edge. No adjacency
pattern or independence assumption about the deleted vertices was used.

### 11.3 Marginal cancellation leaves only threshold crossings

On the whole interval [a,1], the smooth function p satisfies

```text
|p(x)|<1,
p'(x)=-s/(4*sqrt(x)*(s-x)^(3/2)),
|p'(x)| <= s/(4*a^2) < 54/5 < 11.                        (37)
```

Here s=1+a<6/5 and a>1/6. The square-root ratio is less than sqrt(6)<3,
which proves the first bound. Define the continuous, piecewise smooth
primitive F(u)=integral_a^u P(v) dv on [a,1]. For grid points x,z,
integrating P(x)-P(v) along the segment gives

```text
|P(x)*(x-z)-[F(x)-F(z)]|
 <= (11/2)*(x-z)^2
      + |x-z|*1_{(x-B)*(z-B)<0}.                         (38)
```

One direct justification is
P(x)-P(v)=1_{x<B}*[p(x)-p(v)]+p(v)*[1_{x<B}-1_{v<B}].
The first term integrates to at most (11/2)*(x-z)^2. The second is
zero unless the segment crosses B and otherwise integrates to at most
|x-z|. This argument covers both directions of the segment; endpoints
never equal B. Values at the single integration point B do not matter.

Let

```text
K=integral |x-z|*1_{(x-B)*(z-B)<0} dmu(x,z).
```

Integrating (38), using the exact cancellation (32) and (34), gives
|L|<=11*E+2*K. For any h>0 split K by |x-z|<=h and |x-z|>h.
On a short crossing, |x-B|<=h; use the first marginal and (33).
On a long crossing, |x-z|<=(x-z)^2/h. Therefore

```text
K <= h*nu({x: |x-B|<=h})+E/h <= 4*h^2+E/h.              (39)
```

For E>0, set u=2*h/E^(1/3)>0. The objective in (39) is
E^(2/3)*(u^2+2/u), and the exact identity

```text
u^2+2/u-3 = (u-1)^2*(u+2)/u >= 0
```

has equality only at u=1. Thus the unique minimizing choice is
h=E^(1/3)/2=(E/8)^(1/3), and

```text
inf_{h>0} (4*h^2+E/h) = 3*E^(2/3),
K <= 3*E^(2/3).                                         (39opt)
```

There is no restriction on h relative to 1/n or the interval endpoints:
(33) and (39) hold for every h>0, including below the mesh spacing.
The value 3 is optimal for this scalar split objective. It does not prove
that a tour saturates the strip/long-crossing bounds, or that 3 is the
best crossing constant for tours. Equations (36)-(39opt) now give

```text
|Delta| <= 54*E+6*E^(2/3)
        <= 432*e+24*e^(2/3),
```

proving (30), since E<=8*e and 8^(2/3)=4. Keeping all other estimates
fixed, this is the best coefficient supplied by optimization of (39);
no claim of an optimal tour-deletion constant is made. For E=0 the
split infimum is zero as h decreases to zero and is not attained at any
h>0. Independently (32) concentrates mu on x=z, so K=L=0 and (36)
gives Delta=0 directly. In fact a genuine cycle here has E>0: a zero
defect would give every vertex only its unique reflected neighbor,
inconsistent with two distinct neighbors in a cycle of at least three
vertices. Thus e>0 for the actual tours, and division in (31) is valid.

The accepted rational gates give (8) for every n>=102. No other
information about floor(q*n) or floor(beta*n) was used. The exact grid
reflection, midpoint mass bound, degrees and maximal-run accounting are
independent of both outer and restricted cardinality parities. In
particular there is no additive O(1/n) error to obstruct the little-o
statement along extremely small-excess sequences. The near-minimizing
regime is nonempty: (7) gives actual Supnick tours with e=O(n^-2).

### 11.4 Precise implication for the two-level method

The square-root barrier is an artifact of the absolute-value step in
Section 4. Actual tour degrees enforce the signed cancellation (32),
which its scalar relaxation omits. The fixed two-level method should
therefore be refined using this cancellation; this discriminator gives
no reason to abandon it in favor of additional coupled information.
For example the available edge-cost envelope can now use

```text
max{e, e+D_n-24*e^(2/3)-432*e}
```

with the same exact e, J_n, D_n and root sandwich. Section 12 now optimizes
this envelope and propagates its finite errors and global corollary.
Section 9 remains the sharp scalar consequence of its explicitly stated
old information. Its coefficients and the previous Section 12 coefficient
remain valid weaker bounds. Sections 11.5-11.6 separately settle the
deletion exponent; they do not establish the best multiplicative constant.
No geometric realization or sharpness of the broader common-tour minimax
follows from this split optimization.

The [task evidence](../ops/TASK-20260910__deletion_exponent_sharpness/EVIDENCE.md)
and [bounded checker](../ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py)
record exact finite accounting, symbolic identities and deterministic
prescribed-tour diagnostics for the original coefficient 40. The new
optimization and enclosures have separate evidence linked in Section 12.
These checks do not enumerate general tours or
serve as proof of the all-order theorem. Sole stable ownership remains
the existing common-chain entry in the global-bounds ledger.

### 11.5 The crossing exponent 2/3 is sharp for genuine cyclic tours

**Status: exact counterexample family / proved sharp exponent for K,
after arXiv v1.** The definitions of mu, E, B and K in Sections 11.1-11.3
are unchanged. There is no finite constant C_0 and exponent alpha>2/3 for which
K<=C_0*E^alpha holds uniformly over all n>=102 and their genuine cyclic
tours, even if the inequality is required only for sufficiently small E.
There is also no uniform K=o(E^(2/3)) as E->0. Together with (39), this
settles the exponent for K exactly; in particular K=O(E) is false.

Here is an explicit infinite family. For every multiple m of 10 with
m>=40, set

```text
n=m^2,  k=floor(q*n),  ell=23*n/100,
S=n+k,  N=n-k+1,
c_N=1 if N is odd, and c_N=2 if N is even.
```

Use the canonical shifted Supnick cyclic order sigma*_{k,n}, explicitly
given by its two rank lists in
[the fixed-k note, Section 1](FIXED_K_SUPNICK_SEAM.md#1-canonical-shifted-supnick-order).
Define a permutation of the vertex labels by

```text
phi(i)=i+m   for ell-m <= i <= ell-1,
phi(i)=i-m   for ell   <= i <= ell+m-1,
phi(i)=i     otherwise,
sigma_m=(phi(i) : i occurs in sigma*_{k,n}), cyclically.
```

This is one cycle through exactly {k,...,n}: a bijective relabeling of
one cycle cannot split it, introduce a loop or repeat a vertex. In
particular its reflected-edge measure has the exact marginals (32),
as well as all the undirected-edge symmetry and degree restrictions.
It is not a doubly stochastic relaxation or a union of short cycles.

The two exchanged blocks lie strictly inside the low-label portion of
the Supnick tour. Indeed q<1/5 gives
ell-m-k>3*m^2/100-m>=8, and
ell+m=23*m^2/100+m<=51*m^2/200<n/2. Thus each exchanged label i has
exactly the two original neighbors

```text
j_-=S-1-i,  j_+=S+1-i.
```

This follows directly from the fixed-k edge formulas in both parities;
neither the seam nor the middle edge meets the blocks. Both neighbors
are above n/2 and hence are fixed by phi. The affected edges are
therefore exactly 4m distinct edges, with one exchanged endpoint each.
For an exchanged i put t_i=phi(i)-i in {m,-m}. Their new integer defects
phi(i)+j-S are t_i-1 and t_i+1.

In the base tour, all integer defects are +1 or -1 except for exactly
c_N zero defects (the seam, and also the middle edge when N is even).
Its sum of squared integer defects is N-c_N. At each exchanged vertex,
the new pair of squares totals
(t_i-1)^2+(t_i+1)^2=2*m^2+2, replacing 2. Summing over the 2m vertices,
and retaining exactly the normalization in E, proves

```text
E(sigma_m) = (4*m^3+N-c_N)/n^3.                         (39a)
```

For K, orient each affected edge first from its relabeled low endpoint.
In integer coordinates the two measure pairs are

```text
(phi(i), S-j_-)=(phi(i),i+1),
(phi(i), S-j_+)=(phi(i),i-1).
```

The cutoff is ell-1/2 in these coordinates. All 4m such pairs cross it,
except (i, S-j)=(ell-1,ell) before relabeling and
(i, S-j)=(ell,ell-1) before relabeling. Those two pairs end on the same
side after relabeling and have absolute integer defect m-1. For every
exchanged vertex the two absolute defects sum to (m-1)+(m+1)=2m.
The sum of crossing absolute integer defects is consequently
4*m^2-2*(m-1).

The reverse orientations contribute zero to K: both their coordinates
are above n/2. No unaffected edge contributes either. In the base tour
|x-z| is at most one mesh step, so its only crossing pairs have integer
coordinates (ell-1,ell) or (ell,ell-1), and both belong to the affected
edges just accounted for. This also checks every closing edge. Each
oriented atom has mass 1/(2*n), and a normalized defect is its integer
defect divided by n. Hence

```text
K(sigma_m) = (2*m^2-m+1)/n^2.                           (39b)
```

These identities are exact for the actual floor k and either parity of
N. Since 0<N-c_N<=n=m^2, they give

```text
E(sigma_m)=4/m^3+O(m^-4) -> 0,
K(sigma_m)=2/m^2-1/m^3+1/m^4,
K(sigma_m)/E(sigma_m)^(2/3) -> 2^(-1/3),
K(sigma_m)/E(sigma_m)^alpha
  ~ (2/4^alpha)*m^(3*alpha-2) -> infinity   (alpha>2/3).
```

For an explicit nonasymptotic obstruction, E<=5/m^3 and K>=1/m^2
imply K>=5^(-2/3)*E^(2/3) throughout the family. Equation (39), with
h=E^(1/3), gives the matching uniform exponent K<=5*E^(2/3) for every
tour. No claim of optimality of either multiplicative constant is made.
The degree identity and (5) also give E/8<=e<=E/(8*a), so the family has
e->0 and likewise obstructs K=O(e^alpha) for alpha>2/3.

This resolves the crossing-term discriminator using the exact cyclic
structure. The upper estimate |L|<=11*E+2*K alone cannot turn a lower
bound on K into one on the signed L or Delta. Section 11.6 separately
computes Delta for this family. The Section 12 minimax and global coefficients
remain unchanged. No geometric feasibility or optimality of sigma_m
at its chain root is asserted, and no new coupling method is started.

The [bounded checker](../ops/TASK-20260911__midpoint_crossing_sharpness/check_crossing.py)
scores fixed prescribed tours directly in integer arithmetic, including
both orientations, rotations and reversals, against (39a)-(39b).
Its [evidence](../ops/TASK-20260911__midpoint_crossing_sharpness/EVIDENCE.md)
is finite corroboration, not the proof of the infinite family or external
mathematical acceptance. The common-chain ledger entry is the sole
thematic owner.

### 11.6 Signed discrepancy of the same explicit cyclic family

**Status: exact formula / rigorous asymptotic theorem / proved sharp
exponent for signed Delta, after arXiv v1.** Use precisely sigma_m from
Section 11.5, with m in 10N, m>=40, n=m^2, k=floor(q*n),
ell=23*n/100, S=n+k and N=n-k+1. No tour is changed or optimized here.
Put

```text
a=k/n,  t_beta=1+q-beta,  beta=23/100,
A_q=1-sqrt(beta/t_beta)>0,
C_q=1/(4*sqrt(beta*t_beta)).
```

Then, along all these m without a parity restriction,

```text
Delta < 0,
Delta = -A_q/m^2-C_q/m^3+O(m^-4),                       (39c)
|Delta|/E^(2/3) -> A_q/4^(2/3) > 0.                     (39d)
```

The remainder is uniform in the actual floor and both parities. In
particular this is a signed-discrepancy sharpness family, not merely a
crossing-term obstruction. We first give an exact finite formula so that
no mesh, seam or replacement contribution is hidden in (39c).

**Exact deletion accounting.** Every deleted vertex is isolated and all
its neighbors survive. The label k retains neighbors n-1,n, including
the written closing edge (n,k). Every other deleted label j has neighbors

```text
S-j-1,   S-j+1       for k+1 <= j <= ell-m-1,
S-j-m-1, S-j-m+1     for ell-m <= j <= ell-1.             (39e)
```

Indeed the second interval consists of the images of the original labels
j+m in the upper exchanged block. The original lower exchanged block now
survives. Section 11.5 places both blocks inside the low-label portion;
the fixed-k edge lists also give the first line of (39e) in both parities.
All these neighbors exceed n/2. The parity-dependent middle edges have
only surviving endpoints and cancel between the two costs. No deleted
run has length two. Deleting an isolated vertex removes its two incident
edges and adds the edge joining exactly those two neighbors. These local
changes partition the removed and replacement edges of the induced cycle,
including its wrap: rotating to any survivor makes this explicit. There
are at least three survivors, so there is no degenerate two-vertex cycle.

For integer j,d occurring below, set T=S-j and define the radical expression

```text
H(j,d)=sqrt((T-d)^2-1)
       -sqrt(j*(T-d-1))-sqrt(j*(T-d+1))
       -T+2*sqrt(j*T),
H_seam=(sqrt(n)-sqrt(k))*(sqrt(n-1)-sqrt(n)).
```

The first radical of H is the induced replacement weight; the next two
are the removed weights; -T+2*sqrt(j*T) subtracts that label's ideal
deletion contribution in D_n. The seam analog simplifies to H_seam.
With the ambient n^2 normalization of W and D_n, the exact formula is

```text
Delta = [H_seam
         + sum_{j=k+1}^{ell-m-1} H(j,0)
         + sum_{j=ell-m}^{ell-1} H(j,m)]/n^2.             (39f)
```

Thus the actual integer k appears everywhere it is required; there is no
replacement of floor(q*n) by q*n in this identity. It accounts for all
original and induced edges, independently of the parity of N or of the
surviving cardinality.

It also proves the strict sign for every stated m. H_seam<0. For H(j,0),
write U=sqrt(T-1)+sqrt(T+1)<2*sqrt(T). Then

```text
H(j,0)=(U-2*sqrt(T))*[(U+2*sqrt(T))/2-sqrt(j)]<0,
```

because T>j. For H(j,m), both new neighbors are strictly below T and
strictly above j. The function
G(j;y,z)=sqrt(y*z)-sqrt(j*y)-sqrt(j*z) is strictly increasing in each
neighbor whenever y,z>j, as its partial derivatives are
(sqrt(z)-sqrt(j))/(2*sqrt(y)) and its symmetric counterpart. Hence
G(j;T-m-1,T-m+1)<G(j;T,T), proving H(j,m)<0.

**Signed first variations.** This independently identifies which terms
can have leading size. With p=p_a from (34), the exact sum of the two
integer defects at a deleted vertex is -1 at k, zero on the first
interval of (39e), and -2m on the second. Therefore

```text
L = -[p_a(a)+2*m*sum_{j=ell-m}^{ell-1} p_a(j/n)]/n^2.    (39g)
```

The interior +1/-1 mesh defects cancel before any absolute value is taken.
Both defects of each newly deleted label have negative sum. The labels
exchanged upwards survive and supply no positive deleted-vertex term in
L. Their cost changes are already accounted for in the exact difference
(39f). Also M_LL=0, so (35) gives |Delta-L|<=3*E. This explains why the
crossing contribution need not cancel, but the sharper expansion below
comes directly from (39f), retaining the quadratic terms as well.

**Uniform Taylor expansion.** To avoid confusing a mesh step with the
block width, write h=1/m and epsilon=1/n=h^2. Normalize j to x=j/n,
t=1+a-x and define smooth functions

```text
A_a(x)=1-sqrt(x/(1+a-x)),
Q_a(x)=sqrt(x)/(4*(1+a-x)^(3/2)).
```

For the shifted block, the normalized neighbors are t-h-epsilon and
t-h+epsilon. On this block x=beta-r*epsilon, 1<=r<=m. The bound
3/17<q<1/5 and m>=40 place a>1/6, h<=1/40 and all the relevant x and
neighbor arguments in a fixed compact subset of (0,infinity), bounded
above by 1. For example x>=beta-1/40>1/6 and
t-h-epsilon>1+1/6-beta-1/40-1/1600>9/10.
All derivatives used here consequently have common finite bounds, with
no dependence on k or a parity choice.

The symmetry of the two neighbor offsets eliminates their linear mesh
term. Taylor's theorem first in epsilon and then in h gives, uniformly,

```text
H(j,m)/n
 = g(x;t-h-epsilon,t-h+epsilon)-D_a(x)
 = -h-2*sqrt(x)*(sqrt(t-h)-sqrt(t))+O(epsilon^2)
 = -h*A_a(x)+h^2*Q_a(x)+O(h^3+epsilon^2).               (39h)
```

Here g is exactly Section 4's normalized replacement-minus-removal cost;
no formal infinite series is assumed. Bounded second derivatives control
the symmetric mesh error and bounded third derivatives control the h
remainder on the same compact set. Since W uses an additional factor
1/n=epsilon, summing the m shifted labels makes the remainder in (39h)
O(epsilon*m*h^3)=O(h^4), with the mesh part even smaller, O(h^5).

The actual one-sided grid ends at beta-epsilon, not beta. Taylor in x
and the exact sums of r and r^2 yield

```text
sum_{r=1}^m A_a(beta-r*epsilon)
 = m*A_a(beta)-epsilon*m*(m+1)*A_a'(beta)/2
   +O(epsilon^2*m^3),
sum_{r=1}^m Q_a(beta-r*epsilon)
 = m*Q_a(beta)+O(epsilon*m^2).
```

Substitution into epsilon times (39h) gives the shifted contribution

```text
-h^2*A_a(beta)+h^3*[A_a'(beta)/2+Q_a(beta)]+O(h^4).
```

The two signed terms in the second coefficient simplify exactly:

```text
A_a'(x)=-(1+a)/(2*sqrt(x)*(1+a-x)^(3/2)),
A_a'(beta)/2+Q_a(beta)=-1/(4*sqrt(beta*(1+a-beta))).
```

For the unshifted interior, (35) with defects +/-epsilon bounds each
normalized H(j,0)/n by 6*epsilon^2. There are fewer than n such labels,
so their total normalized contribution is O(epsilon^2)=O(h^4).
The exact H_seam is bounded in absolute value by
sqrt(n)/(sqrt(n)+sqrt(n-1))<1, hence its contribution is also O(h^4).
These statements include the closing replacement edge, rather than
discarding a boundary term of unexamined size. We have proved

```text
Delta=-A_a(beta)/m^2
      -1/(4*sqrt(beta*(1+a-beta))*m^3)+O(m^-4).
```

Finally 0<=q-a<1/n=h^2. Bounded a-derivatives change the leading term
by O(h^4) and the next term by O(h^5), proving (39c) with the actual
floor. There is no premise about fractional parts or equidistribution.
The exact formula (39f) retains the finite floor dependence that this
remainder absorbs.

**Sharpness and scope.** From (39a),
E=4/m^3+O(m^-4), with 0<N-c_N<=m^2 for either parity. Combining with
(39c), and noting t_beta>beta, proves (39d). More generally,

```text
|Delta|/E^alpha ~ (A_q/4^alpha)*m^(3*alpha-2).
```

Consequently no finite uniform |Delta|<=C_0*E^alpha with alpha>2/3,
and no uniform |Delta|=o(E^(2/3)), can hold for genuine tours even at
arbitrarily small E. Section 11.3 supplies the matching uniform upper
exponent, without asserting an optimal multiplicative constant. The
comparison E/8<=e<=E/(8*a), with a>1/6, proves the same obstruction to
stronger exponents and to little-o(e^(2/3)) for e; it does not identify
a limit for |Delta|/e^(2/3). This settles the exponent for the signed
discrepancy, not the optimal scalar envelope, common-tour minimax or a
geometric coefficient. No geometric feasibility of sigma_m, new global
bound, certification or publication change follows.

The [bounded independent checker](../ops/TASK-20260911__signed_discrepancy_family/check_signed_discrepancy.py)
constructs and filters the cyclic rank lists, compares the full signed
edge sums to (39f) as exact formal radical expressions, and checks the
defect sums in (39g), both parities, rotations and reversals. Exact square
root enclosures provide only finite asymptotic corroboration; the uniform
Taylor argument above is the proof. Its
[evidence](../ops/TASK-20260911__signed_discrepancy_family/EVIDENCE.md)
records the bounded domain and limits. The existing common-chain entry
in the global-bounds ledger remains the sole thematic owner.

## 12. Refined two-level minimax from the proved deletion envelope

**Status: exact scalar theorem / analytic minimax lower bound / proved
global corollary, after arXiv v1.** Keep exactly q=q_*, beta=23/100,
the original radii, ambient normalization n^2 and B_n from Section 1.
For every integer n>=102, (2), e=W-J_n>=0 and the proved (30) imply

```text
max{r(sigma),r(sigma|T_beta(n))}
 >= [J_n+max{e,e+D_n-24*e^(2/3)-432*e}]/pi-1/n.          (40)
```

The positive outer excess is retained on both branches. All optimization
below is over one scalar excess shared by the two restrictions. The
all-tour premise is Section 11, not a sampled family or a new claim about
the best possible deletion exponent.

### 12.1 Exact global scalar minimum

For d>0 define t(d) as the unique positive root and m(d) by

```text
P(t)=432*t^3+24*t^2,
P(t(d))=d,                 m(d)=t(d)^3.
```

Existence and uniqueness follow because P is continuous, strictly
increasing on [0,infinity), starts at zero and is unbounded. This root
characterization is an exact algebraic definition, with no numerical
root selection. Also set t(0)=m(0)=0 and m(d)=0 for d<0. For every real d,

```text
min_{e>=0} max{e,e+d-24*e^(2/3)-432*e} = m(d).           (41)
```

For d<=0 the value at e=0 is zero and the first branch is nonnegative.
For d>0 set t=e^(1/3), r=t(d). The second branch becomes
g(t)=d-24*t^2-431*t^3, strictly decreasing for t>=0, whereas t^3 is
strictly increasing. Their difference is d-P(t), so they meet only
at t=r. For 0<=t<=r, the dominating second branch obeys the identity

```text
g(t)-r^3=(r-t)*[24*(r+t)+431*(r^2+r*t+t^2)] >= 0.
```

For t>=r, the first branch satisfies
t^3-r^3=(t-r)*(t^2+t*r+r^2)>=0. Equality holds only at t=r.
Thus the unique minimizer is e=m(d), with value m(d). The proof covers
zero, the crossing and arbitrarily large excess; it makes no small-e
assumption or exchange of optimization and limits.

Section 9.1 already proves 0<D_n<2 for all n>=102, including both
cardinality parities. Taking the finite minimum over common tours in (40)
therefore proves the exact finite lower bound

```text
B_n/n^2 >= [J_n+m(D_n)]/pi-1/n.                          (42)
```

For precision about scalar sharpness, the formal data
e=m(d), W=J+e, W'=W have Delta=-d and saturate
|Delta|<=24*e^(2/3)+432*e. They realize the scalar minimum; they do
not assert the existence of any corresponding tour or configuration.
Even retaining the old scalar inequality |Delta|<=60*sqrt(e) does not
raise this minimum for 0<d<2: P(1/6)=8/3>2 implies r<1/6 and

```text
d^2/m(d)=r*(24+432*r)^2
         < (1/6)*96^2=1536 < 3600.
```

Hence d<60*sqrt(m(d)) at the new crossing. This also proves
m(d)>d^2/3600 on that domain. The scalar ceiling applies only to these
aggregate inequalities, with e>=0; it does not upper-bound B_n or R*(n),
limit sharper deletion constants or additional information about tours,
or establish optimality of exponent 2/3.

### 12.2 Asymptotic coefficient and exact rational enclosures

Write t_*=t(D), eta_split=m(D)/pi, with the same actual integral D>0
from Sections 5 and 9. Since J_n->pi*C, D_n->D and m is continuous,
the uniform finite inequality (42) gives

```text
liminf B_n/n^2 >= C+eta_split,
432*t_*^3+24*t_*^2=D,          eta_split=t_*^3/pi.         (43)
```

Every displayed terminating decimal below is an exact rational. The
bounded checker proves strict enclosures

```text
0.0092836183568361125168565556 < t_*
  < 0.0092836183568361125168565557,
2.546841764900829732093748e-7 < eta_split
  < 2.546841764900829732093749e-7,
0.1405693355294332566284894404 < C+eta_split
  < 0.1405693355294332566284894405.                      (44)
```

Here is a reproducible rational derivation independent of floating
quadrature. Recheck the Section 9.2 Taylor gates for tau,q,pi and use its
endpoint substitution z=(1+q_0-2*x)/(1+q_0), q_0=q_-. Integrate the first
80 terms of the positive-coefficient expansion of sqrt(1-z^2) with the
explicit geometric tail given there, and include 4*(q_+-q_-) for the
moving-endpoint error. The new standalone checker implements these
rational sums directly; it imports neither the Section 9 checker nor the
previous Section 12 midpoint-integration checker. Call its unrounded
rational bounds d_-<D<d_+. They reproduce (24) and prove

```text
P(t_-)<d_-<D<d_+<P(t_+),
t_-^3/pi_+ < eta_split < t_+^3/pi_-.
```

Strict monotonicity of P proves the root enclosure, and exact rational
comparisons prove the eta_split bracket in (44). Finally
C=tau*(1+q)/(2*pi), so the separate positive parameter bounds give
outward rational bounds for C; add them to those for eta_split to prove
the total coefficient bracket. No independence of these parameters is
assumed by interval arithmetic.

For comparison only, denote the preceding coefficient by
eta_new=t_40^3/pi, where 432*t_40^3+40*t_40^2=D. It is the value proved
before the midpoint optimization, with its original checker and dossier
linked below. More generally let t_40(d)>0 solve
P_40(t_40(d))=d for d>0. Since P_40(t)=P(t)+16*t^2>P(t) at positive t,
t(d)>t_40(d) and m(d)>t_40(d)^3. The strongest finite bound (42) and
asymptotic gain therefore strictly improve the preceding lower formulas.
Fresh rational root gates for P_40, with the same d_-,d_+, give

```text
1.917 < eta_split/eta_new < 1.918.
```

This compares lower-bound gains, not the total global coefficients and
not the unknown geometric optimum. The old 40-envelope is weaker at
every e>0 and is nonbinding at the new scalar minimum.

### 12.3 Propagating the existing finite errors

For d>0 implicit differentiation, with t=t(d), gives

```text
m'(d)=3*t/(48+1296*t),             0<m'(d)<1/432,
d/dt [3*t/(48+1296*t)]=144/(48+1296*t)^2>0.
```

Thus m is increasing and convex on [0,infinity), with right derivative
zero at zero. Retain the tighter already-proved versions of (11)-(12):
|J_n-pi*C|<=5/n and |D_n-D|<=19/(2*n). For x_+=max{x,0}, monotonicity
in (42) first gives the explicit bound, without linearizing m,

```text
B_n/n^2 >= C+[m((D-19/(2*n))_+)-5/n]/pi-1/n.            (45)
```

This retains the nonlinear finite error for every integer n>=102,
including the range where D-19/(2*n)<=0. It is stronger than the
following convenient linear consequence. Set

```text
mu=m'(D)=3*t_* /(48+1296*t_*),
A=1+[5+(19/2)*mu]/pi.
```

For every delta>=0, integrate the increasing derivative on
[(D-delta)_+,D] to obtain

```text
0<=m(D)-m((D-delta)_+)<=mu*min{delta,D}<=mu*delta.
```

This also covers delta>=D; no positivity of D-delta is silently
assumed. Applying delta=19/(2*n) in (45) gives

```text
B_n/n^2 >= C+eta_split-A/n
         >= C+eta_split-2.592953/n,                    n>=102,
2.592952349827745447477519 < A
  < 2.592952349827745447477520 < 2.592953.                (46)
```

The displayed strict rational bounds follow by substituting t_-,t_+
in the increasing function 3*t/(48+1296*t) and using opposite pi
endpoints. For an algebraic check of the error direction, for 0<=t<=r
the secant inequality follows from

```text
3*r*[24*(r+t)+432*(r^2+r*t+t^2)]
 -(48+1296*r)*(r^2+r*t+t^2)=24*(r-t)*(r+2*t)>=0.
```

The checker verifies this coefficient identity independently. All finite
statements use the same floor estimates, parities and common normalization
as the input proof. No numerical evaluation of floor(q*n) is needed.

### 12.4 Transfer through full-feasible deletion and stopping scope

Take any full feasible configuration on {1,...,n} at radius R with
order omega. Keeping either terminal subset preserves all its original
radii, central tangencies and surviving pairwise distance constraints.
For consecutive surviving radii a,b, let g be their positive directed
gap, including the closing gap. Full feasibility gives
min{g,2*pi-g}>=theta_R(a,b), hence g>=theta_R(a,b).
Summing the surviving directed gaps gives 2*pi, so strict monotonicity
of the chain closure sum implies R_chain(omega|T)<=R for each subset.
This is valid for gaps above pi, consecutive deletions and cyclic wrap.

The restrictions share sigma=omega|T_q(n), and restricting sigma again
to T_beta(n) equals omega|T_beta(n). Their two chain roots are fixed
numbers for fixed omega. Taking the infimum over full feasible
configurations of that order, and then minimizing over full orders, gives

```text
R_full(omega)>=max{R_chain(sigma),R_chain(sigma|T_beta(n))}>=B_n,
R*(n)>=B_n.                                               (47)
```

No attainment assumption, chain-only deletion or reconstruction at a
chain root is used. In particular the strongest finite formula (42),
its explicit finite-error form (45) and (46) all transfer to R*(n).
Equations (43)-(47) prove

```text
liminf R*(n)/n^2 >= C+eta_split,
R*(n)>=B_n>(C+2.5468e-7)*n^2                 for n>=10^12. (48)
```

The finite instance is the exact rational gate
eta_- - 2.592953/10^12 > 2.5468e-7; it also has n>=102.
More generally a fixed 0<eta'<eta_split gives strict finite bounds
at C+eta' whenever n>=102 and n>A/(eta_split-eta'). Neither cutoff is
claimed minimal. Liminf comparisons at C+eta_split are non-strict;
the lower rational endpoint in (44) gives a strict comparison at that
smaller total coefficient. Finite strictness at a smaller coefficient
does not prove strictness at C+eta_split, equality, or a normalized limit.

The [new bounded independent checker](../ops/TASK-20260911__optimized_midpoint_split/check_split.py)
uses only standard-library exact arithmetic: polynomial coefficient
identities, fixed rational Taylor gates, 80 endpoint integral terms with
a proved tail, and rational cubic/enclosure/finite-cutoff inequalities.
It checks the split identity, E-to-e constants, scalar crossing,
inverse derivative and secant identity, and new coefficient enclosures.
It imports neither production code, earlier checkers nor saved results,
and does not sample tours or use floating quadrature. The
[new task evidence](../ops/TASK-20260911__optimized_midpoint_split/EVIDENCE.md)
records exact outputs and the analytic propagation/full-deletion audit.
The [previous checker](../ops/TASK-20260910__refined_two_level_minimax/check_refined_minimax.py)
and [its evidence](../ops/TASK-20260910__refined_two_level_minimax/EVIDENCE.md)
retain the historical 40-envelope and eta_new provenance unchanged.
These bounded checks support the new identities and enclosures; they
do not replace the analytic all-tour theorem or independently review its
entire dependency chain. External mathematical acceptance remains separate.

The midpoint optimization propagates without an obstruction and stops
here. The constant 3 is sharp for the objective in (39), and m(d) is sharp
for the stated aggregate scalar envelope. Neither assertion proves tour
realizability or the best constant for tours. The separate exponent
sharpness proofs in Sections 11.5-11.6 remain unchanged. No sharp global
geometric coefficient, minimizing common tour, normalized limit, upper
construction, finite optimum certificate or arXiv-v1 revision follows.
Sole stable ownership remains the common-chain entry in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`.
