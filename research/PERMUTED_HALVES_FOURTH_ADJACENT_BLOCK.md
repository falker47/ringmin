# Fourth independent reflection after the exact third-width minimum

    status=PROVED
    classification=exact continuous theorem; rational width witness
    accepted_input_head=c45162f7df1b1b482b9dbecea7b619ecdaa02227
    fixed_inputs=alpha_hat; x_*; epsilon_b; Delta_*
    variable=eta; fourth slab [w,w+eta], w=lambda+epsilon_b+Delta_*
    guaranteed_interval=0<eta<=1/20000
    finite_recovery_and_full_feasibility_transfer=not performed
    proved_on=2026-09-11
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs and statement

Import the exact definitions, existence and uniqueness of x_*, alpha_hat
and epsilon_b from the [boundary-minimum proof](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md),
Section 1, and of Delta_* from the [mixed third-width proof](PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md),
Sections 1-5. Thus x_* minimizes its complete-max E, alpha_hat is the
specified zero of K'(alpha)+(1+alpha)*E(x_*), epsilon_b is the unique
mixed boundary stationary width, and Delta_* is the unique mixed zero
of Psi(Delta)=4*pi*C_3'(Delta). All four parameters stay EXACT and fixed.
In particular Delta_* is not replaced by a rational bracket endpoint.

Write

    alpha=alpha_hat, A=1+alpha, lambda=A*x_*, v=lambda+epsilon_b,
    w=v+Delta_*, a=A/3, b=1-alpha, B_4=A+w, h_4=a-w,
    k(t,X,Y)=sqrt(t)*(sqrt(X)+sqrt(Y)), c(X,Y)=sqrt(X*Y),
    g=max(k,c), C(mu)=(integral g dmu)/(4*pi).

The baseline mu_3(Delta_*) is the three separate reflections on
[0,lambda], [lambda,v], [v,w], followed by the shifted diagonal and
wrapped tail in [uniform transfer (2)](PERMUTED_HALVES_THIRD_BLOCK_UNIFORM_TRANSFER.md#1-statement-and-the-geometric-discriminator).
Only that measure definition is used here. Let mu_4(eta) replace its
diagonal slab [w,w+eta] by its own symmetric reflection as in Section 3.
Define the NORMALIZED complete-max cost increment by

    C_4(eta)=C(mu_4(eta)),
    J_4(eta)=C_4(eta)-C_3(Delta_*), F_4(eta)=4*pi*J_4(eta).       (1)

**Theorem.** On 0<eta<=eta_0=1/20000 the removed and inserted full
maxima are strictly chord everywhere, including both endpoints. Put
M=B_4+eta/2 and q=eta/(2*B_4+eta). Then exactly

    F_4(eta)=-integral_(-eta/2)^(eta/2)
               z^2/[M+sqrt(M^2-z^2)] dz
      =(eta/2)*sqrt(B_4*(B_4+eta))+M^2*asin(q)-eta*M.           (2)

The principal real inverse sine is intended. The first nonzero unilateral
term, with a signed remainder valid on this whole interval, is

    J_4(eta)=-eta^3/(96*pi*B_4)+R_4(eta),
    0<=R_4(eta)<=eta^4/(192*pi*B_4^2).                         (3)

In particular the constant, linear and quadratic terms vanish, and
lim_(eta->0+) J_4(eta)/eta^3=-1/(96*pi*B_4)<-1/576<0.
The exact finite-width bound is stronger than a formal expansion:

    -eta^3/(96*pi*B_4)<=J_4(eta)
       <=-eta^3/(96*pi*M)<-eta^3/576<0.                       (4)

The rational witness is the new WIDTH eta_0; the old parameters and its
start w remain exact. Its rigorous saving is

    C_3(Delta_*)-C_4(1/20000)
       >1/4608000000000000>0.                                (5)

This disproves local optimality of the three-block coupling against the
specified independent fourth-block direction. It does not contradict the
unique minimum of C_3 in its own third-width family. No new global upper
coefficient or finite/full-feasibility transfer is concluded here.

## 2. Exact domain and branch margins from inherited brackets

Use precisely the accepted strict bounds and their rational weakening
from mixed-width Section 5:

    AL=1093/10000<alpha<AH=10931/100000,
    XL=719/2500<x_*<XH=2877/10000,
    EL=43/1000<epsilon_b<EU=7/160,
    DL=29/5000<Delta_*<DU=27/4000,
    A_L=1+AL, A_H=1+AH,
    V_L=A_L*XL+EL=9050867/25000000,
    V_U=A_H*XH+EU=362898487/1000000000,
    W_L=V_L+DL<w<W_U=V_U+DU=369648487/1000000000.

The sharper epsilon_b<EU already follows from the accepted boundary
distance estimate; it is not a new parameter solve. Independent enclosing
corners suffice, without assuming any correlations between the minima:

    A-3*w>A_L-3*W_U=354539/1000000000,
    A-3*w-4*eta>154539/1000000000,                  0<eta<=eta_0,
    a-w-eta>204539/3000000000,
    b-w-eta>520991513/1000000000,
    3/2-(B_4+eta/2)>21016513/1000000000.                       (6)

These inequalities are strict even at eta_0. The last three margins use,
respectively, A_L/3-W_U-eta_0, 1-AH-W_U-eta_0 and
3/2-A_H-W_U-eta_0/2. Since a<b by alpha<1/2, we have

    0<lambda<v<w<w+eta<a<b<1, 1<B_4<=X,Y<=B_4+eta<2.

In particular h_4>eta_0 and M<3/2. The same measure construction is
well-defined through eta=h_4; there is no high wrap in that larger domain.

## 3. Only the fourth slab changes; exact marginals and zero-mass seams

For I=[w,w+eta] and R_I(t)=2*w+eta-t, specify the change by every
continuous, possibly nonsymmetric test T on D=[0,1] x [1,2]^2:

    integral T d(mu_4(eta)-mu_3(Delta_*))
      =(1/2)*integral_I [T(t,A+t,A+R_I(t))
                         +T(t,A+R_I(t),A+t)-2*T(t,A+t,A+t)] dt. (7)

The removed conditional measure is diagonal almost everywhere on I.
Replacing it by two positive masses of weight 1/2 preserves positivity,
total mass and the uniform low marginal. Since R_I preserves Lebesgue
measure and is an involution of I, for each continuous phi,

    (1/2)*integral_I [phi(A+t)+phi(A+R_I(t))] dt
      =integral_I phi(A+t) dt.

Thus EACH high marginal is preserved separately. Conditional swap symmetry
also preserves equality of the (t,X) and (t,Y) marginals. Their common
two-variable distribution is not asserted to stay unchanged.

The low intervals of blocks 3 and 4 meet only at w and their high ranges
only at B_4. These points have zero mass: the low marginal is Lebesgue
and all high maps have slopes +/-1. The six high ranges

    [1,A], [A,A+lambda], [A+lambda,A+v], [A+v,B_4],
    [B_4,B_4+eta], [B_4+eta,2]

partition [1,2] modulo endpoints. Half-open assignments give the same
measure. The previous third reflection remains t->v+w-t and the new
one is t->2*w+eta-t. They are not merged. The conditional pair can jump
at w, with no atom or extra continuum seam cost. In particular the
chain-active end of the third block has no influence on the diagonal
mass immediately to its right. All of these facts hold also for eta<=h_4.
At eta=0 the replacement vanishes and J_4(0)=0.

## 4. Literal full max and all branch switches in the stated cost domain

Let 0<=s<=eta<=h_4 and put t=w+s, X=B_4+s, Y=B_4+eta-s.
Before selecting either branch, symmetry in (7) gives

    F_4(eta)=integral_0^eta [max(k(t,X,Y),c(X,Y))
                            -max(2*sqrt(t*X),X)] ds.           (8)

Every old block and switch cancels with its FULL cost, because the first
three parameters, their endpoints and their conditional measures are
unchanged. In particular differentiating eta does not move the old mixed
switch z(Delta_*); no stationarity cancellation is being assumed.

For eta<=eta_0, the explicit margins (6) give

    k/c=sqrt(t/X)+sqrt(t/Y)
       <=2*sqrt((w+eta)/B_4)<1,
    X-4*t=A-3*w-3*s>=A-3*w-3*eta>0.                          (9)

All quantities are positive before squaring. These uniform bounds cover
the closed slab, so no new branch switch or endpoint tie occurs in the
one-sided expansion interval. This justifies reducing (8) to

    F_ch(eta)=integral_0^eta [sqrt((B_4+s)*(B_4+eta-s))-(B_4+s)] ds.
                                                                    (10)

For clarity, the first later switch can also be specified exactly,
without solving or optimizing it. On 0<eta<=h_4 the removed diagonal
remains chord; its sole tie is s=eta=h_4. Define

    V(s,eta)=sqrt(t/X)+sqrt(t/Y),
    V_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0,
    W(eta)=V(eta,eta)
          =sqrt((w+eta)/(B_4+eta))+sqrt((w+eta)/B_4).

V(0,eta)<1, and V(eta/2,eta)<1 because w+eta/2<a.
W is strictly increasing: its squared summands have positive derivatives
A/(B_4+eta)^2 and 1/B_4. Its endpoint values obey

    W(0)=2*sqrt(w/B_4)<1,
    W(h_4)=1/2+sqrt(a/B_4)>1, since B_4<4*a.

There is therefore exactly one UNSQUARED root tau_4 in (eta_0,h_4)
of W(tau_4)=1. For eta<tau_4 all inserted costs are strictly chord.
At tau_4 only s=eta ties, with zero mass, and (10) is still exact.
For tau_4<eta<=h_4 there is exactly one switch z_4(eta) in
(eta/2,eta), defined by V(z_4(eta),eta)=1, and the full increment is

    F_4(eta)=F_ch(eta)+integral_(z_4(eta))^eta [k-c] ds,
    integral_(z_4(eta))^eta [k-c] ds>0.                         (11)

Formula (2) computes F_ch; past tau_4 it must include (11)'s correction.
Equality of costs cancels the moving-switch boundary term in a first
derivative of (11), but does not justify discarding the chain integral.
No sign or optimization claim beyond the guaranteed interval is needed.
No claim is made beyond h_4, where the diagonal itself changes branch.

## 5. Exact increment, rigorous unilateral expansion and rational saving

For eta<=tau_4 center z=s-eta/2 and M=B_4+eta/2. Then
X*Y=M^2-z^2>=B_4*(B_4+eta)>0 and the removed cost integrates to eta*M.
Rationalizing the centered difference proves (2); elementary integration
of sqrt(M^2-z^2) gives its displayed closed form. Uniformly in z,

    2*B_4<=M+sqrt(M^2-z^2)<=2*M,
    integral_(-eta/2)^(eta/2) z^2 dz=eta^3/12.

The numerator is positive off z=0 and the denominator is positive.
Consequently

    -eta^3/(24*B_4)<=F_4(eta)<=-eta^3/(24*M)<0,
    0<=F_4(eta)+eta^3/(24*B_4)
       <=eta^3*(1/B_4-1/M)/24
        =eta^4/(48*B_4*M)<=eta^4/(48*B_4^2).                 (12)

Dividing by 4*pi proves (3) with an explicit uniform remainder, hence
the asserted FIRST nonzero unilateral term. The scaled integral with
z=eta*r has positive radicands for small eta and a fixed compact r
interval, also giving an analytic extension near zero. Thus, if phrased
as derivatives, J_4'(0+)=J_4''(0+)=0 and
J_4'''(0+)=-1/(16*pi*B_4). A negative first variation is not claimed.

For every 0<eta<=eta_0, (6) gives M<3/2. Using
0<pi=4*integral_0^1 (1+r^2)^(-1) dr<4,

    -J_4(eta)>=eta^3/(96*pi*M)>eta^3/576.

This proves the exact interval margin (4) and, at the rational width
eta_0, (5). The remainder is not used to guess the finite-width sign.
Only w<a and the indicated coordinate/denominator bounds are needed for
this argument; no additional optimality equations for the old inputs
are assumed. Delta_*'s stationarity identifies the requested baseline.

## 6. Bounded independent support and later transfer obligations

The [standalone checker](../ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py)
uses stdlib rational arithmetic and directed square roots. Its fixed
discriminator is the inherited rational gates plus a 16-panel concave
midpoint upper enclosure of the literal new full max at eta_0, subtracting
the exact diagonal integral. It uses neither (2)'s antiderivative nor
its rationalized integrand. It encloses the worst B_4 corner because
the integrand (10) is nondecreasing in B_4:

    partial_(B_4) [sqrt(X*Y)-X]=(2*B_4+eta)/(2*sqrt(X*Y))-1>=0,
    (2*B_4+eta)^2-4*X*Y=(eta-2*s)^2>=0.

The raw maximum is concave in s on this certified branch, since
partial_s^2 sqrt(M^2-(s-eta/2)^2)=-M^2/[M^2-(s-eta/2)^2]^(3/2)<0.
Thus the midpoint enclosure is an integral upper bound, not a sign mesh.
Finite corner/moment and branch/tie probes are additional diagnostics;
the arbitrary-test and continuum statements are proved above. The checker
does not import production or previous checkers, solve any minimum, scan
widths or generate outputs. A separate dependency run reproduces the
accepted third-width rational sign gates. Commands and limitations belong
to the [task evidence](../ops/TASK-20260911__fourth_adjacent_block/EVIDENCE.md).

For a LATER transfer at a fixed positive witness, the following are the
only new construction obligations of the existing alternating-halves route:

1. Supply genuine permutations P^(m) of {m+1,...,2m} for all sufficiently
   large integers m, with actual cyclic predecessor P_0=P_m. Account for
   every real cell, including the new shared third/fourth seam, exit, short
   rounded blocks, floor ties and wrap; a formal continuum reflection or
   correct separate marginals alone does not supply these permutations.
2. Prove convergence of the ACTUAL complete cost moments
   (1/m)*sum_i g(i/m,P_(i-1)/m,P_i/m) to integral g dmu_4(eta).
   Arbitrary-test weak recovery is sufficient but stronger than needed for
   the radius limit. The complete maximum must be retained through finite
   branch mismatches; any seam error must vanish in this average.

The [existing arbitrary-high full-cell criterion](PERMUTED_ALTERNATING_HALVES.md)
then supplies the relevant geometry under its exact hypotheses m>=2,
distinct highs in that shell and lows 1,...,m. Its score is
sum_i max(theta_R(P_(i-1),i)+theta_R(i,P_i),theta_R(P_(i-1),P_i));
one must use its root and its all-pairs placement, with both cyclic paths.
There is no extra continuum chord-dominance, switch separation, seam
smoothness, stationarity or global-optimality hypothesis. The uniform
angular expansion and root-scale bounds in [uniform transfer Sections 4-5](PERMUTED_HALVES_THIRD_BLOCK_UNIFORM_TRANSFER.md#4-the-exact-all-pairs-criterion-has-no-width-threshold-here)
are the existing analytic tools to be checked and applied to those actual
orders. No new four-block orders or root limits are established in this task.

For a global limsup upper bound over both parities, deleting the single
largest high from each even feasible placement would suffice for the odd
upper bound. Equality with the limiting odd FIXED-ORDER full minimum would
add a surviving-cell lower squeeze; it is not needed merely for the global
upper bound. No assertion of a smaller finite-n optimum follows from (5).
In particular the currently transferred global coefficient remains
C_3(Delta_*). The stable continuous claim has exactly one owner,
knowledge/FIXED_ORDER_THEORY.md. Independent mathematical review is separate.
