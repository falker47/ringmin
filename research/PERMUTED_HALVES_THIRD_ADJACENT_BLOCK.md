# Third adjacent reflected block: strict continuous full-cost improvement

    status=PROVED
    classification=exact continuous theorem; explicit rational strict saving
    domain=alpha_hat; lambda=(1+alpha_hat)*x_*; epsilon_b; v=lambda+epsilon_b; delta=1/1000
    finite_recovery_and_geometric_transfer=not supplied
    proved_on=2026-09-08
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs and theorem

Import the exact definitions, existence, uniqueness and accepted brackets
of x_*, alpha_hat and epsilon_b from the
[boundary-minimum theorem](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md),
Sections 1 and 6. In particular x_* minimizes its full-max E on [0,1],
alpha_hat is the unique zero of K'(alpha)+(1+alpha)*E(x_*) on [0,1/2],
and epsilon_b is the unique zero of D_b' on (0,A/3-lambda).
These definitions are unchanged; no bracket midpoint defines a parameter.
Use exactly

    AL=1093/10000 < alpha=alpha_hat < AH=10931/100000,
    XL=719/2500 < x=x_* < XH=2877/10000,
    EL=43/1000 < e=epsilon_b < EH=11/250,
    A=1+alpha, lambda=A*x, v=lambda+e,
    a=A/3, b=1-alpha, delta=1/1000,
    B=A+v, M=B+delta/2.                                    (1)

Let mu_b be the exact boundary coupling in
[boundary recovery](PERMUTED_HALVES_BOUNDARY_RECOVERY.md), equation (4).
Only that measure definition is used, not its finite recovery theorem.
The normalization agrees with the current
[boundary full-root baseline](PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md),
equation (2): on D=[0,1] x [1,2]^2,

    k(t,X,Y)=sqrt(t)*(sqrt(X)+sqrt(Y)), c(X,Y)=sqrt(X*Y),
    g(t,X,Y)=max(k(t,X,Y),c(X,Y)),
    C(mu)=(1/(4*pi))*integral g dmu, C_b=C(mu_b).             (2)

**Theorem.** Replacing the diagonal slab [v,v+delta] of mu_b by its
own symmetric reflection, as defined below, gives a probability coupling
mu_3 with uniform t, X and Y marginals and equal (t,X)/(t,Y) marginals.
The second and third blocks touch only at a zero-mass endpoint in both
low and high coordinates. For C_3=C(mu_3),

    4*pi*(C_3-C_b)
      =-integral_(-delta/2)^(delta/2)
          z^2/[M+sqrt(M^2-z^2)] dz,

    -delta^3/(24*B) <= 4*pi*(C_3-C_b)
                     <= -delta^3/(24*M)
                     < -1/36000000000 < 0,

    C_b-C_3 > 1/(144000000000*pi)
            > 1/576000000000 > 0.                          (3)

This is the specified continuous discriminator. There is no new finite
permutation, R_full statement, global bound or parameter optimization.

## 2. Exact domain from only the accepted brackets

Put A_L=1+AL, A_H=1+AH and

    V_L=A_L*XL+EL=9050867/25000000 < v,
    v < V_H=A_H*XH+EH=363148487/1000000000.

All following lower and upper corners are directed using positivity.
In particular 1-3*XH>0. Exact rational arithmetic gives

    A-3*v-4*delta=A*(1-3*x)-3*e-4*delta
      > A_L*(1-3*XH)-3*EH-4*delta
      =1586317/100000000 > 0,                              (4)

    a-v-delta
      > A_L*(1/3-XH)-EH-delta
      =1686317/300000000 > 0,                              (5)

    b-v-delta > 1-AH-V_H-delta
      =526541513/1000000000 > 0,                           (6)

    M < A_H+V_H+delta/2=1472958487/1000000000 < 3/2,
    3/2-(A_H+V_H+delta/2)=27041513/1000000000 > 0.          (7)

Thus 0<lambda<v<v+delta<a<b<1: use x>0, e>0, (5), and
b-a=(2-4*alpha)/3>0. The new block is strictly pre-wrap and all
its highs lie in [A+v,A+v+delta] subset (1,2). The exact widths,
start and previously accepted parameters have not moved. These gates
actually hold throughout the given parameter bracket box; they use
neither stationarity nor a refined enclosure of any minimum.

## 3. Measure definition, endpoint contact and exact marginals

Write h_alpha(t)=1+{t+alpha}. For any continuous, possibly nonsymmetric,
test F on D, mu_b is

    integral F dmu_b
      =(1/2)*integral_0^lambda [F(t,A+t,A+lambda-t)
                                +F(t,A+lambda-t,A+t)] dt
       +(1/2)*integral_lambda^v [F(t,A+t,A+lambda+v-t)
                                 +F(t,A+lambda+v-t,A+t)] dt
       +integral_v^1 F(t,h_alpha(t),h_alpha(t)) dt.          (8)

For I=[v,v+delta] put R_I(t)=2*v+delta-t and replace only its
diagonal conditional mass with

    (1/2)*delta_(A+t,A+R_I(t))
      +(1/2)*delta_(A+R_I(t),A+t).                         (9)

In particular, the exact difference of measures is specified by

    integral F d(mu_3-mu_b)
      =(1/2)*integral_v^(v+delta) [F(t,A+t,A+R_I(t))
                                  +F(t,A+R_I(t),A+t)
                                  -2*F(t,A+t,A+t)] dt.    (10)

The baseline is diagonal almost everywhere on I by (6) and (8).
This removes and replaces exactly delta units of positive mass, so
mu_3 is positive with total mass 1 and unchanged low marginal dt.

The closed low intervals [lambda,v] and [v,v+delta] intersect in
{v}; their closed high ranges [A+lambda,A+v] and [A+v,A+v+delta]
intersect in {A+v}. The first block ends at lambda and does not reach
the third. The low marginal is Lebesgue measure and the affine high
maps have slopes +1 or -1, so these points have zero mass. Equivalently
assign half-open intervals in (8)-(10), with the last endpoint arbitrary.
No endpoint is counted twice with positive mass. The limiting conditional
pairs on the two sides of v need not agree: there is no atom or additional
cost term there. We keep THREE SEPARATE reflections; in particular the
second reflection t->lambda+v-t is not extended to the third interval.

R_I is a measure-preserving involution of the closed interval I.
For every continuous phi on [1,2], either high marginal of (9) satisfies

    (1/2)*integral_I [phi(A+t)+phi(A+R_I(t))] dt
      =integral_I phi(A+t) dt,                             (11)

by the substitution r=R_I(t), with reversed limits. Each high marginal
is therefore preserved separately. Explicitly, their unchanged/changed
ranges partition [1,2] modulo endpoints as

    [1,A], [A,A+lambda], [A+lambda,A+v],
    [A+v,A+v+delta], [A+v+delta,2].

The first range is the unchanged wrapped tail. All densities remain 1.
At each t in I the two high conditional distributions are equal by swap;
the same holds outside I in (8). Hence for every continuous f(t,X),

    integral [f(t,X)-f(t,Y)] dmu_3=0.                     (12)

This is exact local balance, or equality of the (t,X) and (t,Y) marginals.
Their common two-dimensional marginal need not equal that of mu_b.
No sufficiency of these constraints for finite recovery is assumed.

## 4. Full max and its branch domain, including both endpoints

Use s=t-v in [0,delta], X=B+s, Y=B+delta-s and t=v+s.
Symmetry of g in (10) yields, BEFORE any branch reduction,

    4*pi*(C_3-C_b)=integral_0^delta [
      max(sqrt(t)*(sqrt(X)+sqrt(Y)),sqrt(X*Y))
      -max(2*sqrt(t*X),X)] ds.                            (13)

The unchanged first and second blocks and wrapped tail cancel with their
full costs, including every old chain/chord switch. In particular this
does not treat the mixed second block as chord.

Every radicand is positive: t>=v>0, X,Y>=B>1. For the reflected block,

    k/c=sqrt(t/X)+sqrt(t/Y)
        <=2*sqrt((v+delta)/B)<1,                          (14)

because B-4*(v+delta)=A-3*v-4*delta>0 by (4). All quantities
are positive before the square comparison. This proves strict chord
dominance on the ENTIRE CLOSED slab, including s=0,delta; there is no
hidden switch or endpoint tie. For the removed diagonal,

    X-4*t=A-3*v-3*s
      >=A-3*v-3*delta
      >1686317/100000000>0.                              (15)

Thus its full maximum is also strictly chord everywhere. Equations
(4)-(6), (14)-(15) verify both the geometric coordinate domain of the
coupling and the full-max branch domain using only the accepted brackets.
Only after these checks can (13) become

    4*pi*(C_3-C_b)
      =integral_0^delta [sqrt((B+s)*(B+delta-s))-(B+s)] ds.
                                                               (16)

## 5. Exact identity and explicit rational saving

Set z=s-delta/2. Then X*Y=M^2-z^2 and
integral_0^delta (B+s) ds=delta*M. Consequently

    4*pi*(C_3-C_b)
      =integral_(-delta/2)^(delta/2) [sqrt(M^2-z^2)-M] dz
      =-integral_(-delta/2)^(delta/2)
          z^2/[M+sqrt(M^2-z^2)] dz.                       (17)

Here M^2-z^2>=B*(B+delta)>0; the rationalization has a strictly
positive denominator. Moreover

    2*B <= M+sqrt(M^2-z^2) <= 2*M,
    integral_(-delta/2)^(delta/2) z^2 dz=delta^3/12.       (18)

The nonnegative numerator vanishes only at z=0, so the integral in
(17) is strictly positive before the minus sign. Bounding its denominator
in the correct direction proves the two-sided bound in (3).
By (7), -delta^3/(24*M)<-delta^3/36=-1/36000000000.
Dividing by 4*pi>0 gives its first cost bound. Finally

    0<pi=4*integral_0^1 1/(1+r^2) dr<4

gives the fully rational separation in (3), with no new transcendental
bracket. This argument is a finite-width identity, not a truncated cubic
expansion or a negative first-derivative claim.

## 6. Verification and precise limits

The [standalone stdlib checker](../ops/TASK-20260908__third_adjacent_block/check_third_block.py)
recomputes every rational domain/denominator margin. An independent
eight-panel concave midpoint upper enclosure evaluates the literal full
max with directed rational square-root bounds at the worst B corner.
It confirms the strict bound 4*pi*(C_3-C_b)<-1/36000000000 without
integrating (17). Monotonicity in B is checked analytically: the derivative
of the integrand in (16) is (2*B+delta)/(2*sqrt(X*Y))-1>=0 since
(2*B+delta)^2-4*X*Y=(delta-2*s)^2. Concavity follows from
d^2/ds^2 sqrt(M^2-z^2)=-M^2/(M^2-z^2)^(3/2)<0.
The raw max is concave here because (14) already proves its active branch.

Finite rational moment checks at bracket corners test the three separate
reflections and endpoint partition; they do not replace the arbitrary-test
proof (11)-(12). All checker evidence is local, independent of production
and prior-checker imports, and writes no files. The accepted minimum
definitions/brackets are imported, not re-proved or refined. Exact commands,
results and protection checks belong to the
[task evidence](../ops/TASK-20260908__third_adjacent_block/EVIDENCE.md).

The sole stable claim owner is knowledge/FIXED_ORDER_THEORY.md. This proves
only C_3<C_b for the specified continuous coupling. There is no construction
of a finite recovery, transfer to R_full, new global bound, finite-n
comparison, new minimizing width/start or optimality claim for mu_3.
The current global coefficient stays C_b. All earlier proof notes,
certificates, production code and arXiv-v1 assets remain unchanged.
Independent external mathematical review remains separate.
