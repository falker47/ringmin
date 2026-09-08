# One-level terminal coupling: a uniform linear bound and eventual equality

    status=PROVED
    classification=exact theorem / proved asymptotic corollaries
    domain=integers k>=1, n>=k+3; M=n-k+1, N=n-k
    proved_on=2026-09-09
    published_snapshot=arXiv v1 remains unchanged

## 1. Definitions and result

Use the definitions of [coupled terminal subsets](COUPLED_TERMINAL_SUBSETS.md):

```text
T_M={k,...,n},                    T_N={k+1,...,n},
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_sigma(R)=sum_{cyclic edges (a,b) of sigma} theta_R(a,b),
A_M=R_chain(Supnick(T_M)),        A_N=R_chain(Supnick(T_N)),
B_{M,N}=min_{sigma on T_M} max{R_chain(sigma),R_chain(sigma|T_N)},
G_{k,n}=B_{M,N}-max{A_M,A_N}.
```

Restriction deletes vertices and joins consecutive survivors, including
the cyclic closing edge. Each cycle has at least three vertices; thus its
continuous strictly decreasing closure sum has a unique positive 2 pi
root. The cardinalities M,N vary with n and k. Supnick denotes the
chain-minimizing cycle, not the opposite extremal tour.

**Theorem.** For every integer k>=1 and n>=k+3,

```text
0 <= G_{k,n} <= n/2.                                      (1)
```

There is also exact eventual equality, with an explicit sufficient cutoff:

```text
n >= n_k := 48 k(k+1)^2
    implies A_M < A_N, B_{M,N}=A_N, and G_{k,n}=0.          (2)
```

Consequently G_{k,n}=o(n^2) for every fixed k. In fact (1) is uniform in
k, so even a moving one-level choice k=k(n), 1<=k(n)<=n-3, cannot create
a positive leading quadratic gain over its separate minima. The cutoff
in (2) is sufficient, not claimed minimal. Neither the scale n/2 nor its
constant is claimed sharp.

These are chain-minimax statements. Actual deletion still gives the lower
bound R*(n)>=B_{M,N}; no comparison tour here is asserted all-pairs
feasible, and no value of R_full or R*(n) is computed.

## 2. Imported facts and the two constructive tours

The only tour optimality premise is the published arbitrary-positive-radii
[Supnick chain theorem](../paper_assets/ringmin_paper.tex), Theorem A.
The explicit rank construction and both parity edge formulas in
[the fixed-k note](FIXED_K_SUPNICK_SEAM.md), Section 1, show that the
smallest radius of a terminal Supnick cycle has its two largest radii
as neighbors. In particular, put

```text
S=Supnick({k,...,n}),             I=S|{k+1,...,n},
T=Supnick({k+1,...,n}).
```

Deleting k from S replaces (n-1,k),(k,n) by (n-1,n), so exactly

```text
F_I(R)=F_S(R)+D_{k,n}(R),
D_{k,n}(R)=theta_R(n-1,n)-theta_R(n-1,k)-theta_R(k,n).     (3)
```

This holds for M=4,N=3 too. It has the opposite sign to the previously
defined larger-Supnick seam defect. A positive D is the cost of retaining
the larger optimizer when its smallest radius is deleted.

For the second construction, T contains (k+1,n). Subdivide that edge
by inserting k and call the resulting cycle H. Then H is a Hamiltonian
cycle on T_M, H|T_N=T, and

```text
F_H(R)=F_T(R)+J_{k,n}(R),
J_{k,n}(R)=theta_R(k,k+1)+theta_R(k,n)-theta_R(k+1,n).     (4)
```

Both are explicit linear-size constructions; there is no search over
tours or gaps. Rotations or reversals give the same edge identities. The
two defects concern different triples and must not be identified.

## 3. Angular and closure derivative bounds at every positive radius

Let u=sqrt(ab/((R+a)(R+b))). Direct differentiation gives

```text
-partial_R theta_R(a,b)
  = u/sqrt(1-u^2) * (1/(R+a)+1/(R+b)).                   (5)
```

For 0<=u<1, u/sqrt(1-u^2)>=asin(u): the difference vanishes at zero
and has derivative u^2/(1-u^2)^(3/2)>=0. If 0<a,b<=n, (5) therefore
implies

```text
-partial_R theta_R(a,b) >= theta_R(a,b)/(R+n).
```

For the closure sum of any fixed cycle with radii at most n this yields

```text
-F'(R)>=F(R)/(R+n),
d/dR [(R+n)F(R)]<=0,
F(R+d)<=F(R)*(R+n)/(R+n+d),           d>=0.              (6)
```

This integrated derivative estimate does not assume beforehand that R
or the unknown root has quadratic size. Its direction is the one needed
for an upper bound on a closure root.

Two upper bounds and one lower bound will also be used. The increasing
radius factors give u<=n/(R+n), and convexity of asin on [0,1] gives
asin(u)<=pi*u/2. The exact alternative formula and atan(x)<x give

```text
theta_R(a,b) <= pi*n/(R+n),                  0<a,b<=n,  (7)
theta_R(a,b) = 2 atan sqrt(ab/(R(R+a+b)))
             < 2 sqrt(ab)/R,                 a,b,R>0,  (8)
theta_R(a,b) >= 2 sqrt(ab/((R+a)(R+b))).                (9)
```

The alternative formula follows because both half-angles are in (0,pi/2)
and tan(asin(u))=u/sqrt(1-u^2).

## 4. The uniform n/2 gain bound

Evaluate (3) at A=A_M. By (7),

```text
F_I(A)=2 pi+D_{k,n}(A) <= 2 pi+pi*n/(A+n).
```

Apply (6) to I, from A to A+n/2:

```text
F_I(A+n/2)
 <= [2 pi+pi*n/(A+n)]*(A+n)/(A+3n/2)
 = 2 pi.                                                 (10)
```

Thus R_chain(I)<=A_M+n/2. Choosing sigma=S in the minimax gives
B_{M,N}<=A_M+n/2, while its defining independent minima give
B_{M,N}>=max{A_M,A_N}. Subtraction proves (1). A slightly more
informative version of the same argument is

```text
G_{k,n} <= (A_M+n)*max{D_{k,n}(A_M),0}/(2 pi) <= n/2.   (11)
```

If D<=0, the chosen larger tour already attains the independent maximum;
no derivative division or sign assumption on the seam was used. If D>0,
insert d=(A_M+n)D/(2 pi) in (6) to prove (11).

## 5. The insertion defect is eventually negative

We first obtain the modest root lower bound A_N>n in a completely
explicit range. Suppose n>=max{4k,40}, let q=floor(n/4), and consider
any cycle on {k+1,...,n}. There are L=q-k low vertices (radius <=q)
and H_c=n-q high vertices (radius >q). If e_HH and e_HL count high-high
and high-low edges, the degree identities give

```text
2 H_c=2 e_HH+e_HL,       e_HL<=2L,
e_HH>=H_c-L=n-2q+k>=n/2.
```

Both endpoints of every high-high edge exceed n/4. At R=n its angle
is strictly greater than 2 asin(1/5)>2/5. Consequently its whole
closure sum is >n/5>=8>2 pi, using pi<4. The decreasing-root criterion
gives A_N>n, in particular for all n>=n_k=48k(k+1)^2: n_k>=192,
and n_k>=4k. This degree count does not enumerate any tours.

Next, direct differentiation of the angle in its first radius gives

```text
partial_a theta_R(a,b)
 = sqrt(R*b)/((R+a)*sqrt(a)*sqrt(R+a+b)).                 (12)
```

For R>=n, k<=a<=k+1<=n, the inequalities R+a<=2R and
R+a+n<=3R imply

```text
partial_a theta_R(a,n)
 >= sqrt(n)/(2 sqrt(3)*R*sqrt(k+1)).
```

Integrate over the unit interval [k,k+1], then use (8) on (k,k+1):

```text
theta_R(k+1,n)-theta_R(k,n)
 >= sqrt(n)/(2 sqrt(3)*R*sqrt(k+1)),
theta_R(k,k+1) < 2 sqrt(k(k+1))/R.                       (13)
```

If n>=48k(k+1)^2, the first right side is at least the second
right side, as follows by squaring positive quantities. The strict
inequality in the second line therefore proves J_{k,n}(R)<0 for
every R>=n in this range, including the cutoff itself.

Apply this at R=A_N>n. The explicit H of (4) has
F_H(A_N)<F_T(A_N)=2 pi, hence

```text
A_M <= R_chain(H) < A_N,
R_chain(H|T_N)=A_N.
```

It follows that B_{M,N}<=A_N=max{A_M,A_N}. The reverse inequality
is definitional, proving (2). This tour need not minimize the larger
chain problem: simultaneous optimality is unnecessary for minimax equality.

## 6. Radius 1, radius 2, parity, and the quadratic coefficient

For k=1, M=n and N=n-1. Equation (1) holds for every n>=4, and

```text
n>=192  implies  B_{n,n-1}=A_{n-1} and G_{1,n}=0.        (14)
```

The earlier exact G_{1,8}>1/6000 remains unchanged. For k=2 the outer
subset is proper, M=n-1,N=n-2. Equation (1) holds for every n>=5, and

```text
n>=864  implies  B_{n-1,n-2}=A_{n-2} and G_{2,n}=0.      (15)
```

The earlier exact G_{2,13}>1/5000 also remains unchanged. These sufficient
cutoffs do not classify the intermediate sizes or the first return to
equality. Neither statement presumes that finite strict gain persists.
The cited rank construction covers both cardinality parities; the proof
otherwise needs only the two seam edges. The smallest admissible N=3 is
covered by (3), (4), and (6); smaller cardinalities are outside the model.

The terminal-array limit in
[finite subset dominance](FINITE_INDUCED_SUBSET_DOMINANCE.md), Section 4,
already proves A_M/n^2->1/8 and A_N/n^2->1/8 for each fixed k.
Combining it with (1) (or (2)) gives the proved corollary

```text
B_{n-k+1,n-k}/n^2 -> 1/8,                 fixed k>=1.   (16)
```

More generally, for any moving admissible k(n), (1) shows that the
normalized coupled bound and the normalized independent maximum differ
by at most 1/(2n). The already proved single-subset envelope therefore
bounds its limsup by C_term. Thus this one-level mechanism cannot improve
the leading lower-bound coefficient, even with a moving lower endpoint.
This is a corollary of a uniform bound, not a new subset optimization.

Multiple simultaneously coupled levels or two sets separated by a growing
number of deleted radii require a separate argument. Nothing here closes
the global coefficient gap, proves a normalized limit for R*(n), provides
an all-pairs construction, determines a floating set, or expands finite
certification. The old positive finite gaps and seam obstructions remain
valid; the constructive comparison is allowed to change the larger tour.

## 7. Evidence and authority

The proofs above are analytic and contain no numerical premise. The
[task-local checker](../ops/TASK-20260909__coupled_terminal_scale/check_scale.py)
checks bounded exact cyclic identities and rational cutoff implications;
an explicitly optional diagnostic evaluates only prescribed comparison
tours. Symbolic derivative checks and the unchanged finite counterexample
checker are separately recorded in the dossier. No factorial enumeration,
production import, new certificate or historical-paper revision is used.
Independent mathematical acceptance remains a separate review step.

The sole stable owner is the one-level entry in
[knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
