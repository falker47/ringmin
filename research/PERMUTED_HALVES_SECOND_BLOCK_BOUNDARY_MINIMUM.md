# Second reflected block: exact minimum of the continuous boundary family

    status=PROVED
    classification=exact continuous theorem; two rational endpoint sign gates
    domain=alpha=alpha_hat; A=1+alpha_hat; lambda=A*x_*; u=lambda; 0<epsilon<A/3-lambda
    minimizer=unique interior mixed-branch root epsilon_b of D_b'=0
    minimizer_bracket=43/1000<epsilon_b<11/250
    finite_recovery_and_radius_transfer=not supplied
    proved_on=2026-09-06
    published_snapshot=arXiv v1 unchanged

## 1. Exact baseline, boundary measure and statement

Use the exact definitions from the
[normalized prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
Sections 2-7, and the
[alpha minimum theorem](PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md),
Sections 1, 3-4:

    E(x)=integral_0^x [
      max(sqrt((1+r)*(1+x-r)),
          sqrt(r)*(sqrt(1+r)+sqrt(1+x-r)))
      -max(1+r,2*sqrt(r*(1+r)))] dr,
    x_* = the unique global minimizer of E on [0,1],

    h_alpha(t)=1+{t+alpha},
    K(alpha)=integral_0^1 max(sqrt(t*h_alpha(t)),h_alpha(t)/2) dt,
    alpha_hat = the unique zero of
                K'(alpha)+(1+alpha)*E(x_*) on [0,1/2].       (1)

The existence, uniqueness and coarse exact brackets in those theorems
are imported. Neither a decimal nor a bracket midpoint defines a parameter:

    AL=1093/10000 < alpha_hat < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    1/4 < x_* < 1/3,
    A=1+alpha_hat, u=lambda=A*x_*, a=A/3, b=1-alpha_hat,
    B=A+u, h=a-u.                                           (2)

In particular A>1, A/4<u<A/3, B>5*A/4, 0<h<A/12,
h/B<1/15, and a<b. The baseline mu_0 is precisely the coupling of the
[joint prefix theorem](PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md),
Section 3: symmetric reflection on [0,lambda], diagonal shifted mass
after lambda, and the original wrapped tail.

For 0<=epsilon<=h use the boundary coupling in Section 5 of the
[start-domain theorem](PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md).
On [lambda,lambda+epsilon], replace the diagonal high pair (A+t,A+t)
by equal masses at (A+t,A+2*lambda+epsilon-t) and its swap. All other
mass stays fixed. The two low blocks and the two high ranges touch
only at zero-mass endpoints. They keep their TWO SEPARATE reflections;
this is not reflection of their union. The replacement preserves the
low marginal, each high marginal separately, and conditional swap
symmetry. The measure and cost extend continuously to epsilon=0,h.

Retain the complete cost and its original normalization:

    g(t,X,Y)=max(sqrt(t)*(sqrt(X)+sqrt(Y)),sqrt(X*Y)),
    C(mu)=(1/(4*pi))*integral g dmu,
    D_b(epsilon)=D(lambda,epsilon)
                =4*pi*[C(mu_(lambda,epsilon))-C(mu_0)],
    Psi_b(epsilon)=D_b'(epsilon).                          (3)

**Theorem.** There is exactly one stationary point epsilon_b in (0,h).
It lies in the strict mixed regime and is the unique global minimum
both on the requested open interval and on its continuous extension
[0,h]. More precisely,

    43/1000 < tau_b < 87/2000,
    tau_b < epsilon_b < tau_b+tau_b^2/(8*B) < 11/250,        (4)

where tau_b is the exact block-entry width defined below. D_b strictly
decreases on (0,epsilon_b) and strictly increases on (epsilon_b,h).
Its endpoint and minimum signs satisfy

    D_b(0)=Psi_b(0)=0,
    D_b(epsilon_b)<D_b(tau_b)<0,
    D_b(h)>11*h^2/1440>0,  Psi_b(h)>11*h/280>0.             (5)

There is exactly one positive-width cost zero epsilon_0 in
(epsilon_b,h). On the closed extension h is the unique global maximum;
on the open interval the supremum is D_b(h) and is not attained.
The excluded zero endpoint is a strict one-sided local maximum.

D_b is C^1 on [0,h], using one-sided endpoint derivatives, and analytic
in each strict regime. It is not C^2 at tau_b: its left curvature is
negative, while its right curvature exceeds 1. This is a theorem about
the specified continuous family, with no finite permutation or new
R_full or R*(n) consequence.

## 2. Full max and exhaustive branch and endpoint classification

For 0<=s<=epsilon put

    t=u+s, X=B+s, Y=B+epsilon-s,
    c(s,epsilon)=sqrt(X*Y),
    k(s,epsilon)=sqrt(t)*(sqrt(X)+sqrt(Y)),
    d(s)=max(X,2*sqrt(t*X)),
    v(s,epsilon)=k/c=sqrt(t/X)+sqrt(t/Y).                   (6)

The swapped costs coincide; all unchanged mass cancels. Therefore,
before making any branch reduction,

    D_b(epsilon)=integral_0^epsilon [max(c,k)-d] ds.         (7)

Since t<=u+epsilon<=a, 4*t<=A+t=X, with equality only at
epsilon=s=h. Thus the removed diagonal is chord throughout, except
for that single upper-endpoint tie, and its integral is
B*epsilon+epsilon^2/2. This is a consequence of the full max.

At fixed epsilon both summands of v strictly increase with s:

    v_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0.
    v(0,epsilon)<2*sqrt(u/B)<1,
    v(epsilon/2,epsilon)
      =2*sqrt((u+epsilon/2)/(A+u+epsilon/2))<1              (8)

for every epsilon>0, including h. The endpoint function

    V_end(epsilon)=v(epsilon,epsilon)
       =sqrt((u+epsilon)/(B+epsilon))+sqrt((u+epsilon)/B)   (9)

strictly increases, V_end(0)<1 and V_end(h)=1/2+sqrt(a/B)>1.
Consequently tau_b is the unique UNSQUARED solution V_end(tau_b)=1
in (0,h). Define the clipped switch

    z(epsilon)=epsilon,                                epsilon<=tau_b;
    v(z(epsilon),epsilon)=1, z in (epsilon/2,epsilon),   epsilon>tau_b.
                                                                    (10)

The all-chain regime, a switch at s=0, and a positive-width midpoint
switch are impossible.

| Width | Reflected block | Removed diagonal |
|---|---|---|
| epsilon=0 | Empty interval | Empty interval |
| 0<epsilon<tau_b | Strictly chord everywhere | Strictly chord |
| epsilon=tau_b | Chord; k=c only at s=epsilon | Strictly chord |
| tau_b<epsilon<h | Chord on [0,z), tie at z, chain on (z,epsilon] | Strictly chord |
| epsilon=h | Same mixed partition, h/2<z<h | Chord; tie only at s=h |

In particular no second diagonal regime or high-wrap crossing occurs
inside the requested domain. The entry tie has a zero-length chain
interval, not a positive-length chain contribution.

## 3. Exact cost and derivative, with moving boundaries retained

The exact split expression, valid also at all endpoints, is

    D_b=integral_0^z c ds+integral_z^epsilon k ds
        -B*epsilon-epsilon^2/2.                          (11)

For a closed expression without quadrature, define

    F(t,A)=[(2*t+A)*sqrt(t*(t+A))
            -A^2*log((sqrt(t)+sqrt(t+A))/sqrt(A))]/4,
    J(v,M)=[v*sqrt(M^2-v^2)+M^2*asin(v/M)]/2,
    H(T,t)=T*asin(sqrt(t/T))-sqrt(t*(T-t)),
    M=B+epsilon/2, T=B+u+epsilon.

Their derivatives in t,v,t, respectively, are
sqrt(t*(t+A)), sqrt(M^2-v^2), and sqrt(t/(T-t)).
All radicands and log arguments are positive at the uses below;
the inverse sine is its principal real branch. Then

    D_b=J(z-epsilon/2,M)-J(-epsilon/2,M)
        +F(u+epsilon,A)-F(u+z,A)
        +J(u+epsilon-T/2,T/2)-J(u+z-T/2,T/2)
        -B*epsilon-epsilon^2/2,                           (12)

    I1=H(2*B+epsilon,B+z)-H(2*B+epsilon,B),
    I2=H(T,u+epsilon)-H(T,u+z),
    c0=sqrt(B*(B+epsilon)),
    p=sqrt(u+epsilon)*(sqrt(B+epsilon)+sqrt(B)),
    P=max(c0,p),
    Psi_b=P-(B+epsilon)+(I1+I2)/2.                        (13)

Here I1=integral_0^z sqrt(X/Y) ds and
I2=integral_z^epsilon sqrt(t/Y) ds. Zero-length terms vanish exactly.

To derive (13), differentiate (11) at fixed u. The upper slab endpoint
contributes P, the removed diagonal contributes -(B+epsilon), and the
two partial-epsilon integrals contribute (I1+I2)/2. The interior term
is [c(z)-k(z)]*z', which vanishes in the mixed branch by COST equality.
On the all-chord branch differentiate its single integral; one must not
drop a nonzero switch term from a fictitious mixed-branch representation.
At entry the two endpoint costs agree and the chain interval shrinks to
zero, so the two derivative expressions match.

More explicitly, on the all-chord branch put
w=epsilon/B and phi(w)=sqrt(1+w)+(1+w/2)*asin(w/(2+w))-(1+w).
Then

    D_b=epsilon*c0/2+M^2*asin(epsilon/(2*B+epsilon))
        -B*epsilon-epsilon^2/2,
    Psi_b=B*phi(epsilon/B).                               (14)

In the mixed branch, evaluate t,X,Y at s=z. Implicit differentiation
of the unsquared switch gives

    z'=t/[A*(Y/X)^(3/2)+Y+t],  0<z'<1/2.                 (15)

The clipped derivative is instead z'=1 on the all-chord branch.
In (15), Y-t=A+epsilon-2*z>A-epsilon>0, so the denominator
exceeds 2*t and gives the stated strict upper bound on z'.
At entry z is continuous but these one-sided derivatives differ.
The cost derivative remains continuous by the cancellation just proved.

For rigor at the tie itself, set s=epsilon*r in (7), r in [0,1].
Locally the radicands stay positive and the branch derivatives are
bounded. The max has a uniformly bounded difference quotient; the
tie set consists of at most one r and has zero measure. Dominated
differentiation proves differentiability at entry, and the same bound
proves continuity of its integrated derivative. The argument and formulas
also give the one-sided derivative at h. Formula (14) gives the zero
endpoint and

    D_b(epsilon)=-epsilon^3/(24*B)+O(epsilon^4/B^2),
    Psi_b(epsilon)=-epsilon^2/(8*B)+O(epsilon^3/B^2).       (16)

## 4. Analytic derivative signs and a quantitative distance from entry

Direct differentiation gives

    phi(0)=phi'(0)=0,
    -1/4<phi''(w)=-1/[2*(2+w)*(1+w)^(3/2)]<0,  w>0.
                                                                    (17)

Consequently Psi_b<0 throughout (0,tau_b], and the all-chord curvature
Psi_b'=phi'(epsilon/B) is negative. Double integration also gives

    -tau_b^2/(8*B)<Psi_b(tau_b)<0.                         (18)

On the mixed branch define positive quantities

    J1=integral_0^z sqrt(B+s)/(B+epsilon-s)^(3/2) ds
       +integral_z^epsilon sqrt(u+s)/(B+epsilon-s)^(3/2) ds,
    Q1=z'*(sqrt(B+z)-sqrt(u+z))/(2*sqrt(B+epsilon-z))>0,
    q=u+epsilon.

Differentiation of (13), retaining the moving boundary of I1+I2, gives

    Psi_b'=p'-1+sqrt(q/B)/2-J1/4+Q1,
    p'=(A+2*q)/(2*sqrt(q*(A+q)))+sqrt(B)/(2*sqrt(q)).        (19)

The first term of p' decreases with q and equals 5/4 at q=A/3.
Since q<a, B>5*A/4 and sqrt(15)>7/2,

    p'>5/4+sqrt(15)/4>17/8,
    0<J1<=epsilon*sqrt(B+epsilon)/B^(3/2)<2/15,
    Psi_b'>9/8-1/30=131/120>1.                           (20)

The J1 bound uses u+s<B+s, epsilon/B<h/B<1/15 and
sqrt(1+epsilon/B)<2. No numerical subdivision is involved.
The same bounds hold in the mixed one-sided limits at tau_b and h.
Thus the negative all-chord curvature and positive mixed curvature
prove the asserted failure of C^2 matching, while preserving C^1.

At h, B=4*a-h and u=a-h>3*a/4. Formula (13) gives

    Psi_b(h)=sqrt(a*B)-2*a+(I1+I2)/2,
    2*a-sqrt(a*B)=h/(2+sqrt(B/a))<2*h/7.                  (21)

For this endpoint, sqrt(X/Y)>sqrt(15/16)>9/10 on the chord
part and sqrt(t/Y)>sqrt(3/16)>2/5 on the chain part. Since z>h/2,

    (I1+I2)/2 > [9*z/10+2*(h-z)/5]/2 >13*h/40,
    Psi_b(h)>(13/40-2/7)*h=11*h/280>0.                   (22)

Continuity, (18), and strict increase of Psi_b on (tau_b,h) prove
existence and uniqueness of epsilon_b there. There are no other
stationary points because the all-chord derivative is strictly negative.
The resulting decrease/increase proves the unique attained global
minimum, including comparison with both excluded endpoints.

Finally, integrate (20) from tau_b to epsilon_b:

    epsilon_b-tau_b < -Psi_b(tau_b) < tau_b^2/(8*B).        (23)

This proves that the minimum occurs shortly after entry without solving
a transcendental stationarity equation in a checker.

## 5. Upper endpoint cost and the complete zero classification

The endpoint cost sign can also be proved analytically. At epsilon=h,
X+Y=2*B+h and integral_0^h (X+Y)/2 ds=integral_0^h X ds.
The hypothetical all-chord difference therefore obeys

    D_ch(h)=integral_0^h [c-(X+Y)/2] ds,
    c-(X+Y)/2=-(h-2*s)^2/[2*(sqrt(X)+sqrt(Y))^2],
    D_ch(h)>=-h^3/(24*B)>-h^2/360.                       (24)

The full max adds integral_0^h (k-c)_+ ds. Put r(s)=k-c for this
paragraph only. Its endpoint value and derivative satisfy

    r(h)=2*a-sqrt(a*B)>h/4,
    r_s=(sqrt(X)+sqrt(Y))/(2*sqrt(t))
        +sqrt(t)/(2*sqrt(X))-sqrt(t)/(2*sqrt(Y))
        +(X-Y)/(2*sqrt(X*Y))
       <4/sqrt(3)+1/sqrt(15)+1/30
       <12/5+1/3+1/30<3.                                 (25)

Here 3*a/4<t<=a, 15*a/4<X,Y<=4*a and h/(2*B)<1/30.
All comparisons have positive quantities before squaring the elementary
constants. Thus r(s)>h/4-3*(h-s) on the last h/12 of the slab, and

    integral_0^h (k-c)_+ ds
      >integral_0^(h/12) (h/4-3*delta) ddelta=h^2/96,
    D_b(h)>h^2*(1/96-1/360)=11*h^2/1440>0.               (26)

Together with strict decrease/increase, D_b(0)=0 and the negative
minimum, this proves the unique positive-width zero and every endpoint
value comparison in Section 1. No value quadrature is a proof gate.

## 6. Only two rational gates for the physical-width location

The entire branch, regularity, sign, attainment and uniqueness argument
above uses analytic inequalities and the imported domain (2). To locate
the minimum in the proposed physical epsilon bracket, put

    EL=43/1000, ET=87/2000, EH=11/250.
    V_end(epsilon)=f(x_*,epsilon/A),
    f(x,w)=sqrt((x+w)/(1+x+w))+sqrt((x+w)/(1+x)).

The function f strictly increases in w, and in x when w<1. The latter
claim follows by differentiating the squared summands: their x
derivatives are 1/(1+x+w)^2 and (1-w)/(1+x)^2, both positive.
Our widths have w<1/3-x<1. Hence the directed corners are

    V_end(EL)<f(XH,EL/(1+AL))<1,
    V_end(ET)>f(XL,ET/(1+AH))>1.                          (27)

Only the final sign in each line needs a rational gate. Write
p=(x+w)/(1+x+w), q=(x+w)/(1+x), R=1-p-q. At both corners p,q,R>0.
Then sign(sqrt(p)+sqrt(q)-1)=sign(4*p*q-R^2), with all pre-square
signs retained. The exact signed square differences are

    lower:
    -342531413518344092144807428477/
      441789962670730640526171361763841 <0,
    upper:
     51974394530491111127115563/
     253438432681061908372345318521 >0.                   (28)

The [standalone Fraction checker](../ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py)
checks these two comparisons and their positive residuals, plus simple
rational bracket ordering. In particular EH<h and B>1. Equations
(23), (27) give

    EL<tau_b<epsilon_b<tau_b+tau_b^2/(8*B)
       <ET+ET^2/8<EH,
    EH-ET-ET^2/8=8431/32000000>0.                         (29)

This proves 0.043<epsilon_b<0.044 exactly and, more quantitatively,
0<epsilon_b-tau_b<7569/32000000. There is no root enclosure, integral
enclosure, interval mesh, optimization scan or refined alpha bracket
in this checker. The exact parameters remain those defined in (1).

## 7. Evidence, continuous consequences and limits of transfer

The two rational comparisons are a bounded exact arithmetic check.
All remaining new mathematical claims are proved analytically above;
the imported baseline minimization theorems are not re-proved.

Separate [70-digit diagnostics](../ops/TASK-20260906__second_block_boundary_minimum/diagnose_boundary.py)
recompute x_* and alpha_hat numerically from their defining equations,
then check the literal full max against (12), central differences,
the entry tie, mixed curvature, endpoint bounds and the cubic limit.
They give the NONCERTIFIED observations

    tau_b       approximately 0.04338587279773466854,
    epsilon_b   approximately 0.04349174800601259590,
    epsilon_b-tau_b approximately 0.00010587520827792736,
    D_b(epsilon_b) approximately -0.00000235526264033607323,
    D_b(h)      approximately 0.00003712032157406775.

These digits are not exact definitions or certified enclosures.
The prior prediction is confirmed by (29), not by the numerical root.

Combining the present theorem with the previously proved start-domain
infimum equality gives the continuous corollary

    inf_{lambda<u, 0<epsilon<a-u} D(u,epsilon)
      =D_b(epsilon_b).

The open two-parameter domain still has no minimizing point. On its
closed triangle lambda<=u<=a, 0<=epsilon<=a-u, the sole minimizer is
(lambda,epsilon_b): positive-width points with u>lambda have strictly
larger same-width cost by the start derivative (and its upper-edge
continuous limit); zero-width costs are zero. This is only a continuous
corollary. For the coefficient functional add the fixed C(mu_0) and
divide by 4*pi.

No finite recovery of the touching-block optimizer, all-pairs radius
limit at this new width, or improved R*(n) bound is established here.
The earlier fixed second-block recovery and transfer retain their
original parameters. No general coupling optimum or result outside
the chord-diagonal subdomain follows. Published arXiv-v1 assets,
finite certificates and production code remain unchanged.

Commands, exact outputs, limitations and source audit are recorded in
the [task evidence](../ops/TASK-20260906__second_block_boundary_minimum/EVIDENCE.md).
The sole stable claim owner is knowledge/FIXED_ORDER_THEORY.md.
Independent external mathematical acceptance and hosted CI are separate.
