# Permuted halves: a three-marginal relaxation cannot certify the shifts

```text
status=PROVED
classification=exact continuum theorem / explicit coupling / disproved relaxation certificate
domain=all high permutations at each m>=2; limits as m tends to infinity
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question, dependencies and conclusion

Keep the low radii increasing. For a permutation P of {m+1,...,2m}, put
sigma_P=(1,P_1,...,m,P_m), P_0=P_m, and rho_P=R_full(sigma_P).
The exact full criterion in
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, gives

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
d_i(R)=max(theta_R(i,P_{i-1})+theta_R(i,P_i),
           theta_R(P_{i-1},P_i)),
S_P(R)=sum_{i=1}^m d_i(R),
rho_P = the unique positive root of S_P(R)=2*pi.             (1)
```

This is the all-pairs full radius, not the adjacent-chain root. Every
high-high chord, including the low seam, remains in (1).

Write alpha_* for the exact unique shift minimizer proved in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md),
Sections 4-6. In particular, 0<alpha_*<1/2 and

```text
h_alpha(t)=1+{t+alpha},
K(alpha)=integral_0^1 max(sqrt(t*h_alpha(t)),h_alpha(t)/2) dt,
C_shift=K(alpha_*)/(2*pi).                                  (2)
```

The fractional part's endpoint values do not affect the measures below.
No decimal approximation or numerical optimizer defines alpha_*.

**Result.** On D=[0,1] x [1,2] x [1,2], define

```text
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)).             (3)
```

The leading full-cell cost is g/(2*c*m) at R=c*(2m)^2,
uniformly over every permutation. Every empirical limit has marginals
dt on [0,1] and dx,dy on [1,2]; it also satisfies equality of the (t,x)
and (t,y) marginals. Let L_3 be the infimum of integral g over measures
with the three stated uniform marginals. Adding that two-dimensional
balance condition does not change the infimum. An explicit balanced
coupling mu_ref below proves

```text
L_3 <= integral g dmu_ref < 4*pi*C_shift - 1/2496.            (4)
```

Thus this relaxation cannot certify the coefficient C_shift against all
high permutations. Equation (4) neither identifies L_3 nor constructs
a sequence of permutations realizing mu_ref. It gives no improved
geometric upper bound and no new lower bound for R*(n).

## 2. Uniform angular and full-cell scaling

Fix c_0>0 and c>=c_0, R=4*c*m^2. For any 1<=a,b<=2m, set

```text
v=sqrt(a*b)/R,  u=v/sqrt((1+a/R)*(1+b/R)).
```

Along the straight segment from (0,0) to (a/R,b/R), the absolute
directional derivative of ((1+s)*(1+t))^(-1/2) is at most
(a+b)/(2*R). Integration therefore gives

```text
0<=v-u<=v*(a+b)/(2*R)<=1/(4*c^2*m^2),
u<=v<=1/(2*c*m).                                           (5)
```

For m>=1/c_0, u<=1/2. If 0<=z<=1/2, then

```text
1/sqrt(1-z^2)-1
 =z^2/(sqrt(1-z^2)*(1+sqrt(1-z^2)))<=z^2,
```

because sqrt(1-z^2)>=3/4 and (3/4)*(7/4)>1. Integrating from 0 to u
yields 0<=asin(u)-u<=u^3/3. Consequently

```text
|theta_R(a,b)-2*sqrt(a*b)/R| <= e_m(c_0),
e_m(c_0)=1/(2*c_0^2*m^2)+1/(12*c_0^3*m^3).                 (6)
```

This estimate does not divide by a low radius or differentiate sqrt(t)
near zero. It covers a fixed low i, i=o(m), all seams and arbitrary high
jumps. The sole large-m restriction is explicit and uniform in P.

Use exactly t_i=i/m, x_i=P_{i-1}/m, y_i=P_i/m in each cell. Then

```text
theta_R(i,P_{i-1})+theta_R(i,P_i)
 =sqrt(t_i)*(sqrt(x_i)+sqrt(y_i))/(2*c*m) + error <=2*e_m,
theta_R(P_{i-1},P_i)=sqrt(x_i*y_i)/(2*c*m) + error <=e_m,
|d_i(R)-g(t_i,x_i,y_i)/(2*c*m)|<=2*e_m.                      (7)
```

Here and below an error bound is an absolute bound. The last line uses
|max(a,b)-max(A,B)|<=max(|a-A|,|b-B|), valid also at branch ties.
No ordinary-cell approximation x_i=y_i has been used.

Define the empirical probability measure and its cost

```text
mu_m^P=(1/m) sum_{i=1}^m delta_(i/m,P_{i-1}/m,P_i/m),
A_m(P)=integral g dmu_m^P.
```

Summing (7), including all m cells, gives

```text
|S_P(c*(2m)^2)-A_m(P)/(2*c)| <= E_m(c_0),
E_m(c_0)=1/(c_0^2*m)+1/(6*c_0^3*m^2).                      (8)
```

In particular the error is O(1/m), uniformly over P and c in any compact
positive interval (indeed for every c>=c_0).

## 3. Empirical limits and which marginals are necessary

All empirical measures lie in the fixed compact box D, so every sequence
has a weakly convergent subsequence. Let mu be any such limit. The exact
one-dimensional empirical marginals are

```text
(pi_t)#mu_m^P=(1/m) sum_{i=1}^m delta_(i/m),
(pi_x)#mu_m^P=(pi_y)#mu_m^P
             =(1/m) sum_{j=1}^m delta_(1+j/m).              (9)
```

The second identity uses the permutation property and its cyclic shift,
not randomness. These are Riemann sums. Taking weak limits in (9) proves

```text
(pi_t)#mu=Lebesgue|_[0,1],
(pi_x)#mu=(pi_y)#mu=Lebesgue|_[1,2].                        (10)
```

Each interval has length one, so these are already probability measures.
In particular x and y each have their own full uniform marginal; merely
fixing the sum of their distributions would discard a necessary condition.

There is also a necessary local balance relation. For any continuous
f on [0,1] x [1,2], let omega_f(delta) be its uniform modulus in the first
variable and M_f=||f||_infinity. Cyclic reindexing gives

```text
integral [f(t,x)-f(t,y)] dmu_m^P
 =(1/m) sum_{j=1}^{m-1}
       [f((j+1)/m,P_j/m)-f(j/m,P_j/m)]
   +(1/m)[f(1/m,P_m/m)-f(1,P_m/m)].
```

Its absolute value is at most omega_f(1/m)+2*M_f/m, which tends to zero.
The last term explicitly treats the low-index seam. Hence

```text
(pi_(t,x))#mu=(pi_(t,y))#mu.                                (11)
```

Equivalently, conditional on almost every t, the two high distributions
agree. Those conditional distributions need not be uniform; only their
average over t is uniform. Neither the (t,x) marginal nor the (x,y)
marginal is required to be a product measure. Shift limits, for example,
are supported on x=y=h_alpha(t), and already contradict such an
independence requirement. The finite fact P_{i-1}!=P_i does not forbid
diagonal support in a weak limit. Reflection symmetry of mu is not a
necessary assertion either; (11) alone was proved here.

We do not claim that (10)-(11) are sufficient for realization by a single
permutation at each m. Such a recovery theorem is outside this task.

Since g is continuous and bounded on D (also at t=0), weak convergence
implies A_m(P_m)->integral g dmu. Equation (8) thus proves the full-score
limit S_(P_m)(c*(2m)^2)->(integral g dmu)/(2*c), uniformly in c on compact
positive intervals along the same subsequence.

## 4. Uniform transfer to roots and the separate optimization levels

On D, 1<=g<=2*sqrt(2), so 1<=A_m<=2*sqrt(2). Put
c_-=1/(8*pi) and c_+=1/pi. At these two fixed test radii the limiting
comparison quantities A_m/(2*c) satisfy, for every P,

```text
A_m/(2*c_-)>=4*pi>2*pi,
A_m/(2*c_+)<=sqrt(2)*pi<2*pi.
```

By (8), for all sufficiently large m, independently of P, the actual
score has the same strict signs relative to 2*pi. Strict decrease in
(1) gives c_-<c_P:=rho_P/(2m)^2<c_+. Apply (8) at this c_P to obtain

```text
|c_P-A_m(P)/(4*pi)|
 <=c_P*E_m(c_-)/(2*pi)<=E_m(c_-)/(2*pi^2)=O(1/m).            (12)
```

Thus every weak empirical limit yields
rho_(P_m)/(2m)^2->(integral g dmu)/(4*pi). The scale of the root was
proved before applying a compact-in-c expansion at it.

For clarity define the actual family optimum at each m, without computing it,

```text
B_m=min_{P permutation of {m+1,...,2m}} rho_P/(2m)^2.         (13)
```

The minimum exists because the set is finite; this definition does not
launch an enumeration. The relaxed value in the next section satisfies

```text
L_3/(4*pi) <= liminf B_m <= limsup B_m <= C_shift.            (14)
```

For the first inequality choose minimizing permutations along a
subsequence realizing liminf, extract a weak limit and use (10),(12).
For the last, use the known asymptotically minimizing shifts. At each m
the geometric global optimum instead satisfies

```text
R*(2m)/(2m)^2 <= B_m.                                      (15)
```

Accordingly a relaxed lower bound on B_m is NOT a lower bound on R*(2m).
A strictly cheaper relaxed coupling is NOT an upper bound on B_m. We
neither assert convergence of B_m nor equality with L_3/(4*pi).

## 5. Relaxation, optional balance and the obstruction to a dual certificate

Let Pi_3 be the Borel probability measures on D satisfying (10), and set

```text
Pi_bal={mu in Pi_3 : (pi_(t,x))#mu=(pi_(t,y))#mu},
L_3=min_{mu in Pi_3} integral g dmu,
L_bal=min_{mu in Pi_bal} integral g dmu.                    (16)
```

These minima exist: the sets are nonempty, weakly closed subsets of the
weakly compact probability measures on D, and the cost is continuous.
Nonemptiness follows even from a diagonal shift measure. This is the
usual prescribed-marginal Kantorovich formulation; see the background
survey [Brendan Pass, Multi-marginal optimal transport: theory and
applications](https://arxiv.org/abs/1406.0026). No theorem concerning
optimal plans or strong duality from that survey is used below.

For any mu in Pi_3 let T(t,x,y)=(t,y,x) and
mu_sym=(mu+T#mu)/2. Its high marginals remain uniform, and its (t,x)
and (t,y) marginals are the same average of the originals. The symmetry
of g preserves its cost. Therefore

```text
L_3=L_bal.                                                (17)
```

So retaining the necessary balance relation does not repair this
particular relaxation. No symmetry or balance is being inferred for
finite permutation measures from this symmetrization argument.

For integrable potentials phi,psi,chi with pointwise inequality

```text
phi(t)+psi(x)+chi(y)<=g(t,x,y),
```

integration over every admissible coupling bounds their marginal objective
by L_3. For Pi_bal the same is true if the left side also contains
f(t,x)-f(t,y), with f continuous, since that term integrates to zero.
These are direct weak-duality statements, requiring no strong-duality
theorem. The strictly cheaper coupling now rules out a sound analytical
or interval-safe certificate reaching 4*pi*C_shift in either formulation.

## 6. Explicit balanced coupling strictly below the best shift

In fact the construction applies to every alpha in (0,1/2). Fix such an
alpha and put

```text
ell=1/4,  A=1+alpha,  M=A+ell/2,
h=h_alpha.
```

On [0,ell] the shift has not wrapped: h(t)=A+t, since
1-alpha>1/2>ell. Define a probability measure by its action on any
bounded Borel test function F:

```text
integral F dmu_ref,alpha
 = (1/2) integral_0^ell
       [F(t,A+t,A+ell-t)+F(t,A+ell-t,A+t)] dt
   + integral_ell^1 F(t,h(t),h(t)) dt.                     (18)
```

This is an explicit sum of three pushforwards of restricted Lebesgue
measure. Its only parameter is alpha; setting alpha=alpha_* uses the
previously defined exact constant, not an estimated root or an unknown
optimal coupling.

**Marginals.** Both choices in the first integral lie in D and have
total mass ell; the second has mass 1-ell. The t marginal is dt. In
either high coordinate, the first block has distribution

```text
(1/2) integral_0^ell [delta_(A+t)+delta_(A+ell-t)] dt
 = integral_0^ell delta_(A+t) dt,
```

by t->ell-t. This is precisely the high mass removed from the original
diagonal shift. That shift sends dt to the uniform measure on [1,2]
(split at its wrap), so both new high marginals remain uniform. Moreover
(18) is symmetric under x<->y at each t. Thus it satisfies (11) exactly,
not only in the limit, and belongs to Pi_bal.

**Branch safety.** For every t<=1/4 and x,y>=1,

```text
sqrt(t)*(1/sqrt(x)+1/sqrt(y))<=2*sqrt(t)<=1.
```

Multiplying by sqrt(x*y)>0 proves that g(t,x,y)=sqrt(x*y)
throughout this entire slab. All altered cells therefore use the chord
branch, including endpoints; there is no branch crossing omitted in (18).

**Strict cost improvement.** The original diagonal shift has cost

```text
integral_0^1 g(t,h(t),h(t)) dt=2*K(alpha).
```

Its cost on the first block is integral_0^ell (A+t)dt=ell*M.
The reflected coupling's cost there is

```text
integral_0^ell sqrt((A+t)*(A+ell-t)) dt
 = integral_(-ell/2)^(ell/2) sqrt(M^2-u^2) du.
```

All other cells are unchanged. The exact saved cost is therefore

```text
delta_alpha=integral_(-ell/2)^(ell/2)
                   [M-sqrt(M^2-u^2)] du,
integral g dmu_ref,alpha=2*K(alpha)-delta_alpha.             (19)
```

For u!=0, exact rationalization and M>ell/2 give

```text
M-sqrt(M^2-u^2)=u^2/(M+sqrt(M^2-u^2))>u^2/(2*M).
```

The omitted u=0 has measure zero. Since M<13/8,

```text
delta_alpha>ell^3/(24*M)> (1/4)^3/(24*(13/8))=1/2496.        (20)
```

There is no numerical premise in this bound. With alpha=alpha_* and
mu_ref=mu_ref,alpha_*, (2),(19),(20) prove (4), and in coefficient units

```text
L_3/(4*pi) <= (integral g dmu_ref)/(4*pi)
            < C_shift - 1/(9984*pi) < C_shift.              (21)
```

As a useful interpretation, the shift's diagonal high pairing is already
strictly improvable inside a block where the low variable has no effect
on the active cost. The relaxation permits this reflected pairing and
the strict geometric-mean saving. Equality of the two conditional high
distributions does not remove it.

## 7. Verification, negative result and remaining scope

Sections 2-6 are the proof; (1) and the exact alpha_* definition/minimum
are imported mathematical dependencies. The construction does not need
LP discovery. No permutation enumeration, finite optimization or
production/global certificate calculation is part of this task.

The independent task-local checker and its exact outputs are recorded in
[the task evidence](../ops/TASK-20260905__three_marginal_relaxation/EVIDENCE.md).
Its exact gates audit the rational/algebraic identities, positivity and
marginal substitutions. Separate finite 70-digit atan calculations probe
the uniform cell/score bounds, cyclic balance and root transfer on a
predeclared bounded list; integral diagnostics quantify one witness but
do not prove the universal statements or give the value L_3.

The falsified proposition is specifically L_3>=4*pi*C_shift, even when
the balance constraint (11) is added. Optimality or nonoptimality of
shifts among all asymptotic permuted-halves configurations remains
unresolved here, as does the exact relaxation value. No recovery of
(18) as a permutation sequence is asserted. R*(n), the known global
bounds, finite certified scope and the arXiv-v1 publication are unchanged.
The sole stable claim owner is knowledge/FIXED_ORDER_THEORY.md.
