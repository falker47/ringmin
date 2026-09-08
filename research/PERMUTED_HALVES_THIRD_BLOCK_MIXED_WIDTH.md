# Third adjacent reflection: the unique continuous mixed-width minimum

    status=PROVED
    classification=exact continuous theorem; two rational endpoint sign gates
    accepted_input_head=b21c2dff20ca7419db56545c67386b369b8d24ac
    domain=tau_3<Delta<=h=A/3-v; v=lambda+epsilon_b fixed
    fixed_inputs=alpha_hat; x_*; lambda=(1+alpha_hat)*x_*; epsilon_b
    stationary_width=unique mixed root Delta_* of 4*pi*C_3'(Delta)=0
    rational_bracket=29/5000<Delta_*<27/4000<h
    scope=continuous only; no finite recovery or geometric/global transfer
    proved_on=2026-09-08
    published_snapshot=arXiv v1 unchanged

## 1. Inputs and statement

Start with the accepted [third-width theorem](PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md),
Sections 1-3. Its exact definitions and brackets are premises, not parameters
to be fitted or reoptimized. In particular, x_* is the unique minimizer of
the complete-max E, alpha_hat is the unique zero of K'(alpha)+(1+alpha)*E(x_*),
and epsilon_b is the unique mixed zero of the boundary derivative D_b'.
The defining functions, existence and uniqueness are in the accepted
[boundary minimum](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md), Section 1.
Keep all four inputs fixed and write

    alpha=alpha_hat, A=1+alpha, lambda=A*x_*, e=epsilon_b,
    v=lambda+e, a=A/3, b=1-alpha, B=A+v, h=a-v.

Here B denotes A+v, not the boundary note's A+lambda. The accepted brackets
give A/4<v<a<b, hence B>5*A/4, 0<h<A/12 and h/B<1/15.
The measure mu_3(Delta) is exactly the third-width theorem's separate
symmetric reflection on [v,v+Delta] of the diagonal mass of mu_b.
Its Section 2 already proves the domain, uniform low marginal, each high
marginal separately, and equal (t,X)/(t,Y) marginals for 0<Delta<=h.
At h the diagonal cutoff is reached only at the upper endpoint; there is
no high wrap or additional positive-mass branch. All three reflections
remain separate, meeting only at endpoints of zero mass.

For the same complete cost and normalization,

    g(t,X,Y)=max(k,c),
    k=sqrt(t)*(sqrt(X)+sqrt(Y)), c=sqrt(X*Y),
    C(mu)=(integral g dmu)/(4*pi), C_b=C(mu_b),
    C_3(Delta)=C(mu_3(Delta)), F(Delta)=4*pi*[C_3(Delta)-C_b],
    Psi(Delta)=F'(Delta)=4*pi*C_3'(Delta).                 (1)

The old unqualified C_3 and mu_3 in finite/geometric results continue to
mean width d_0=1/1000. Also put d_1=1/250 and
D_g=1986317/400000000, as in the starting theorem.

**Theorem.** The exact mixed derivative is (5) below, with the unique
interior full-max switch retained. On the entire mixed interval,

    Psi'(Delta)>131/120>1,       tau_3<Delta<=h,           (2)

where the derivative at h is from the left. Nevertheless Psi is negative
at entry and positive at h. There is exactly one stationary width Delta_*
in (tau_3,h). The cost strictly decreases on (tau_3,Delta_*) and strictly
increases on (Delta_*,h]; thus it is neither nonincreasing nor nondecreasing
on the requested interval. Its sole minimum there is attained at Delta_*.
Combined with the accepted chord theorem, it is also the unique minimum
on [0,h], where C_3(0)=C_b. Quantitatively,

    29/5000 < tau_3 < Delta_* < tau_3+tau_3^2/(8*B)
       < 27/4000 < h,
    C_3(Delta_*) < C_3(tau_3) < C_3(D_g)
       < C_3(d_1) < C_3(d_0) < C_b,
    C_3(d_1)-C_3(Delta_*) > 12389/72000000000000 > 0.      (3)

Section 6 also gives a rational bracket for C_3(Delta_*)-C_b. These are
continuous costs, with no new assertion about R_full or R*(n).

## 2. Full maximum, moving switch and exact derivative

For 0<=s<=Delta<=h set

    t=v+s, X=B+s, Y=B+Delta-s,
    V(s,Delta)=k/c=sqrt(t/X)+sqrt(t/Y),
    W(Delta)=V(Delta,Delta)
      =sqrt((v+Delta)/(B+Delta))+sqrt((v+Delta)/B).

The removed diagonal is chord since X-4*t=A-3*(v+s)>=0, with its only
tie at Delta=s=h. Unchanged costs, including the mixed second block,
cancel with their complete maxima. The starting theorem proves W strictly
increasing with its unique UNSQUARED root W(tau_3)=1 in (D_g,h). It also
proves V_s>0, V(Delta/2,Delta)<1 and, for tau_3<Delta<=h, the unique switch

    z=z(Delta) in (Delta/2,Delta), V(z,Delta)=1.

In particular this retains the full-max equality, not a squared equation
with unspecified roots. The exact full cost is

    F=integral_0^z c ds+integral_z^Delta k ds-B*Delta-Delta^2/2
     =F_ch(Delta)+integral_z^Delta (k-c) ds,
    F_ch=integral_0^Delta [c-X] ds,
    integral_z^Delta (k-c) ds>0.                          (4)

F_ch is only the chord contribution in this regime, not the full cost.
At the switch, implicit differentiation gives

    V_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0,
    V_Delta=-sqrt(t)/(2*Y^(3/2)),
    z'=t/[A*(Y/X)^(3/2)+Y+t],  0<z'<1/2.

The strict upper bound uses Y-t=A+Delta-2*z>A-Delta>0. All radicands
are positive, so the implicit function theorem applies throughout the
mixed interval and to its one-sided endpoints.

Write

    q=v+Delta,
    p=sqrt(q)*(sqrt(B+Delta)+sqrt(B)),
    I_c=integral_0^z sqrt((B+s)/(B+Delta-s)) ds,
    I_k=integral_z^Delta sqrt((v+s)/(B+Delta-s)) ds.

Leibniz differentiation of (4) at fixed A,v,B gives the exact derivative

    Psi=p-(B+Delta)+(I_c+I_k)/2.                         (5)

The endpoint contributes k(Delta,Delta)=p. The switch term is
[c(z,Delta)-k(z,Delta)]*z'=0 by COST equality. The partial-Delta
integrands are c_Delta=sqrt(X/Y)/2 and k_Delta=sqrt(t/Y)/2.
Thus (5) includes both width dependences and the endpoint contribution;
neither the positive chain integral nor its derivative is discarded.

If desired (5) has the following exact elementary form, without numerical
quadrature. Define, for 0<r<T,

    H(T,r)=T*asin(sqrt(r/T))-sqrt(r*(T-r)),
    partial_r H(T,r)=sqrt(r/(T-r)).

Then with the principal real inverse sine,

    I_c=H(2*B+Delta,B+z)-H(2*B+Delta,B),
    I_k=H(B+v+Delta,v+Delta)-H(B+v+Delta,v+z).             (6)

Every argument lies strictly between 0 and its T. This is an exact
formula with z specified uniquely above, not an approximation to it.

At entry z tends to tau_3 and the chain interval shrinks to zero;
p tends to sqrt(B*(B+tau_3)). Formula (5) therefore matches the accepted
chord derivative. Differentiability at the tie can also be seen directly
by substituting s=Delta*r in the literal full-max integral, 0<=r<=1:
locally positive radicands bound difference quotients, and the tie set has
measure zero. Dominated differentiation gives the same derivative and
continuity. At h the same argument gives the left derivative; the removed
diagonal's endpoint tie changes no integral on the stated domain.

## 3. Analytic strict increase of the mixed derivative

Differentiate (5), still keeping the moving switch. Define

    J=integral_0^z sqrt(B+s)/(B+Delta-s)^(3/2) ds
       +integral_z^Delta sqrt(v+s)/(B+Delta-s)^(3/2) ds,
    Q=z'*(sqrt(B+z)-sqrt(v+z))/(2*sqrt(B+Delta-z))>0.

The boundary term of I_c+I_k is now NONZERO: their integrands do not
agree at the cost switch. The exact second derivative is

    Psi'=p'-1+sqrt(q/B)/2-J/4+Q,
    p'=(A+2*q)/(2*sqrt(q*(A+q)))+sqrt(B)/(2*sqrt(q)).       (7)

This also follows by differentiating the positive correction in (4);
using cost equality a second time to drop Q would be incorrect.

For f(q)=(A+2*q)/(2*sqrt(q*(A+q))),

    f'(q)=-A^2/[4*(q*(A+q))^(3/2)]<0,
    f(a)=5/4.

As q<=a and B>5*A/4,

    p'>5/4+sqrt(15)/4>17/8.

The positive integral is bounded uniformly, with no subdivision:

    0<J<=Delta*sqrt(B+Delta)/B^(3/2)
       =(Delta/B)*sqrt(1+Delta/B)<2/15.

Here v+s<B+s, Y>=B, and Delta/B<=h/B<1/15; also
sqrt(1+Delta/B)<2. Dropping the two strictly positive terms in (7),

    Psi'>17/8-1-(2/15)/4=131/120>1.

The same bounds hold in the right limit at tau_3 and the left limit at h.
This proves (2) on the full continuum. No sign mesh or width probes enter.

## 4. Endpoint signs, existence, uniqueness and distance from entry

For the entry derivative use the accepted chord formula only on its valid
branch, including its endpoint tau_3. Put

    phi(w)=sqrt(1+w)+(1+w/2)*asin(w/(2+w))-(1+w).

Then Psi(tau_3)=B*phi(tau_3/B) and direct differentiation gives

    phi(0)=phi'(0)=0,
    phi'(w)=1/sqrt(1+w)+asin(w/(2+w))/2-1,
    -1/4<phi''(w)=-1/[2*(2+w)*(1+w)^(3/2)]<0, w>0.

Double integration yields the strict entry bounds

    -tau_3^2/(8*B)<Psi(tau_3)<0.                         (8)

At Delta=h one has q=a, B=4*a-h, and v=a-h>3*a/4. Equation (5) becomes

    Psi(h)=sqrt(a*B)-2*a+(I_c+I_k)/2,
    2*a-sqrt(a*B)=h/(2+sqrt(B/a))<2*h/7.

On the endpoint slab, 15*a/4<X,Y<=4*a and 3*a/4<t<=a. Consequently
sqrt(X/Y)>sqrt(15/16)>9/10 and sqrt(t/Y)>sqrt(3/16)>2/5.
Together with z(h)>h/2 this implies

    (I_c+I_k)/2>[9*z/10+2*(h-z)/5]/2>13*h/40,
    Psi(h)>(13/40-2/7)*h=11*h/280>0.                    (9)

All sides compared before squaring the elementary constants are positive.
Continuity, (8), (9), and strict increase from Section 3 prove exactly one
zero Delta_* in (tau_3,h), with the stated strict decrease/increase of F
and C_3. This refutes monotonicity in either direction on (tau_3,h].
There are no earlier positive-width stationary points by the accepted
chord theorem. The continuous extension at zero has C_3(0)=C_b, strictly
larger than the positive-width minimum.

Finally integrate Psi'>1 from tau_3 to Delta_*:

    0<Delta_*-tau_3<-Psi(tau_3)<tau_3^2/(8*B).            (10)

This is the quantitative location discriminator. It requires no root
solver for either z or the stationary point. The derivation parallels
Sections 3-4 of the accepted boundary-minimum proof, with all inequalities
checked above for the third start v rather than assumed from its name.

## 5. Exact rational bracket: only two finite sign gates

Keep the original strict input bounds

    AL=1093/10000 < alpha < AH=10931/100000,
    XL=719/2500 < x_* < XH=2877/10000,
    EL=43/1000 < e < 11/250.

The already accepted boundary theorem, (29), additionally implies
e<ET+ET^2/8 with ET=87/2000. Use its rational weakening

    e<EU=7/160, EU-ET-ET^2/8=431/32000000>0.

This is an inherited inequality, not a new solve or reoptimization of e.
Define independent enclosing corners

    A_L=1+AL, A_H=1+AH,
    V_L=A_L*XL+EL=9050867/25000000,
    V_U=A_H*XH+EU=362898487/1000000000,
    T_L=29/5000, T_U=67/10000, D_U=27/4000.

In W(A,v,d)=sqrt((v+d)/(A+v+d))+sqrt((v+d)/(A+v)), both
squared summands decrease in A. Their v derivatives are respectively
A/(A+v+d)^2 and (A-d)/(A+v)^2, strictly positive for d<A.
The two proposed widths are in that domain. Thus the directed gates are

    W(A,v,T_L)<W(A_L,V_U,T_L)<1,
    W(A,v,T_U)>W(A_H,V_L,T_U)>1.                         (11)

For either rational corner put p=(v+d)/(A+v+d), q=(v+d)/(A+v)
and r=1-p-q. The checker verifies p,q,r>0. Since
(sqrt(p)+sqrt(q))^2-1=2*sqrt(p*q)-r, positivity before the
second squaring gives

    sign(W-1)=sign(4*p*q-r^2).

The exact signed square differences in (11), in that order, are

    -963745517404602389188679409068317/
      4734571866017504812540302482915910561 <0,
     34763358497298510706339907/
      205268116362886684743388903969 >0.                  (12)

Therefore T_L<tau_3<T_U. The remaining implications are rational:

    B>1,
    D_U-T_U-T_U^2/8=35511/800000000>0,
    A_L/3-V_U-D_U=354539/3000000000>0.

Equations (10)-(12) prove T_L<tau_3<Delta_*<D_U<h, wholly within the
requested domain. The upper corner used in the lower gate is already
admissible even at D_U by the last displayed margin; the other corner
has still larger h. No evaluation beyond h is needed.

The [standalone checker](../ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py)
uses only Fraction arithmetic. Its entire computational discriminator is
the two signed square comparisons (12); other checks are their rational
domain, location and cost implications. It has no width loop, radicals,
root solver, quadrature, interval mesh, production or previous-checker
import, input refinement or generated output file. The analytic proof
supplies every statement about the whole interval.

## 6. Cost comparison with the current widths

The accepted centered rationalization gives, for all 0<Delta<=h,

    F_ch(Delta)>=-Delta^3/(24*B).

This remains a bound on F_ch after entry, never an equality with F.
At Delta_* the positive correction in (4), B>1 and Delta_*<D_U give

    F(Delta_*)>-D_U^3/24=-6561/512000000000.              (13)

At the explicit width T_L<tau_3, the literal full cost is still chord.
Its centered denominator is at most 2*(B+T_L/2), and the accepted-box
margin

    3/2-A_H-V_U-D_U/2=24416513/1000000000>0

ensures B+T_L/2<3/2. Strict decrease to Delta_* therefore gives

    F(Delta_*)<F(T_L)<-T_L^3/36=-24389/4500000000000.      (14)

Dividing (13)-(14) by 4*pi with 3<pi<4, respecting the negative signs,
provides the rational cost bracket

    -2187/2048000000000 < C_3(Delta_*)-C_b
       < -24389/72000000000000.                         (15)

The current widths satisfy 0<d_0<d_1<D_g<T_L<tau_3<Delta_*.
The accepted strict chord decrease and the new strict decrease up to
Delta_* prove all of (3)'s cost ordering. For an explicit new saving,
F(d_1)>-d_1^3/24 by B>1, so

    F(d_1)-F(Delta_*)>T_L^3/36-d_1^3/24
       =12389/4500000000000>0,
    C_3(d_1)-C_3(Delta_*)>12389/72000000000000>0.          (16)

The same lower saving holds relative to d_0, whose cost is larger.
The value C_3(h) is strictly larger than the minimum by Section 4.
No decimal stationary width or approximate value defines any claim.

## 7. Scope and evidence

The exact continuous theorem is the analytic sign/uniqueness argument plus
the two bounded rational gates. It is not a finite Ringmin certificate.
The sole stable claim owner is knowledge/FIXED_ORDER_THEORY.md.
The [task evidence](../ops/TASK-20260908__third_block_mixed_width/EVIDENCE.md)
records exact commands, outputs, source protection and limitations.

No finite recovery at Delta_*, R_full transfer, global limsup coefficient,
fixed-input reoptimization, general coupling optimum, finite certification
or paper revision is supplied. Existing unqualified C_3 and all associated
finite/global statements retain d_0=1/1000. The accepted older proof is
preserved; this note resolves its explicitly open mixed-regime question.
Independent external mathematical acceptance remains separate.
