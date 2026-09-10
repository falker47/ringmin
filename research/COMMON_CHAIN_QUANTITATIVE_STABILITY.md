# Quantitative stability for one common pair of terminal chain tours

    status=PROVED
    classification=exact theorem / asymptotic minimax lower bound / proved global corollary
    domain=all cyclic orders; finite stability n>=10^14; minimax estimate n>=102
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
|Delta| <= 40*e^(2/3)+432*e.                              (30)
```

In particular, for every 0<e<=epsilon the quotient satisfies

```text
|Delta|/sqrt(e) <= 40*epsilon^(1/6)+432*sqrt(epsilon) -> 0
                                                   as epsilon -> 0. (31)
```

The supremum implicit here ranges over all n>=102 and all their cyclic
orders with 0<e<=epsilon. Thus no deterministic or other family of actual
tours with e->0 can have |Delta|>=c*sqrt(e) for a fixed c>0. The bound
does not assert that exponent 2/3 is itself sharp. No new optimization of
60, beta, q, the scalar minimax or a geometric coefficient is undertaken.

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

If E>0 choose h=E^(1/3). There is no restriction on h relative to 1/n
or to the interval endpoints. Equations (36)-(39) give

```text
|Delta| <= 54*E+10*E^(2/3)
        <= 432*e+40*e^(2/3),
```

proving (30). If E=0, (32) concentrates mu on x=z, so L=0 and (36)
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
max{e, e+D_n-40*e^(2/3)-432*e}
```

with the same exact e, J_n, D_n and root sandwich. Optimizing that
envelope, improving its constants, determining the best deletion
exponent, or deciding how much more coupling is ultimately needed are
not part of this result. Section 9 remains the sharp scalar consequence
of its explicitly stated old information; (30) supplies new information
about actual tours and does not alter that historical statement or its
accepted global coefficients. No geometric realization or sharpness of
the broader common-tour minimax follows.

The [task evidence](../ops/TASK-20260910__deletion_exponent_sharpness/EVIDENCE.md)
and [bounded checker](../ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py)
record exact finite accounting, symbolic identities and deterministic
prescribed-tour diagnostics. They do not enumerate general tours or
serve as proof of the all-order theorem. Sole stable ownership remains
the existing common-chain entry in the global-bounds ledger.
