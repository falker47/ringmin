# Finite dominance for arbitrary induced subsets

```text
status=PROVED
classification=exact finite theorem / exact asymptotic corollary
domain=all subsets S of {1,...,n} with cardinality at least 3; arbitrary subset sequences
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Results and exact scope

For `R>0` and positive radii `a,b`, write

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))).
```

Let `Supnick(S)` denote the canonical chain-minimizing Supnick cycle on a
finite set `S` of distinct positive radii, indexed by the increasing ranks
of the radii. The published arbitrary-radii Supnick theorem implies that its
rank-edge multiset depends only on `N=|S|`, not on the radius values.

**Finite terminal-dominance theorem.** For every integer `n`, every
`3<=N<=n`, and every

```text
S={r_1<...<r_N} subset {1,...,n},
T_{n,N}={n-N+1,...,n},
```

one has exactly

```text
R_chain(Supnick(S)) <= R_chain(Supnick(T_{n,N})).       (1)
```

Equality holds if and only if `S=T_{n,N}`. Thus, at every finite `n` and
fixed cardinality, the terminal subset is the unique maximizer of the
single-subset Supnick chain bound.

The finite theorem removes every regularity hypothesis from the subset:
there is no interval, finite-union, endpoint, component-count, or limiting
shape assumption.

To state the sharp sequence consequence, define for `0<=L<=1`

```text
G(L)=(2/pi) integral_0^(L/2)
                    sqrt((1-L+t)(1-t)) dt.             (2)
```

Its boundary values are

```text
G(0)=0,                 G(1)=1/8.                       (3)
```

Let `tau` be the unique root of `tau=cos(tau)` in `(0,pi/2)`, and put

```text
lambda_*=(1+sin(tau))/(1-sin(tau)),
L_*=1-1/lambda_*=2 sin(tau)/(1+sin(tau)),
C_term=tau/(pi(1+sin(tau))).                            (4)
```

The accepted terminal-subset optimization is equivalently

```text
max_{0<=L<=1} G(L)=G(L_*)=C_term,                       (5)
```

with the maximum unique.

**Arbitrary-sequence corollary.** For any sequence

```text
S_n subset {1,...,n},       3<=N_n=|S_n|<=n,
B_n=R_chain(Supnick(S_n)),
```

if `N_n/n->L`, then

```text
limsup_{n->infinity} B_n/n^2 <= G(L).                  (6)
```

Without any limit assumption on the cardinalities,

```text
limsup_{n->infinity} B_n/n^2 <= C_term.                (7)
```

Moreover, every subsequence along which `B_n/n^2->C_term` must satisfy
`N_n/n->L_*`. This is only a cardinality condition: finite strictness does
not provide a uniform normalized gap, so no asymptotic uniqueness of the
subset shape is asserted.

This is sharp. If

```text
M_n=max_{S subset {1,...,n}, |S|>=3}
                     R_chain(Supnick(S)),
```

then

```text
M_n=max_{1<=k<=n-2} R_chain(Supnick({k,...,n})),
M_n/n^2 -> C_term.                                     (8)
```

Consequently no choice of one induced subset at each `n`, however irregular
or adaptive, can improve the leading coefficient `C_term` supplied by a
single induced-subset chain bound. A pointwise maximum of any collection of
such individual bounds is also bounded by the same finite envelope `M_n`.
This does not cover a genuinely coupled method which combines constraints
from several subsets, and it makes no claim about `R_full`, a geometric
upper bound, or the true leading coefficient of `R*(n)`.

## 2. The common rank-edge multiset

For reference, the canonical Supnick rank edges are recorded explicitly.
If `N=2h`, they are

```text
(j,N-j),       1<=j<=h-1,
(j,N+2-j),     2<=j<=h,
(1,N), (h,h+1).                                        (9)
```

If `N=2h+1`, they are

```text
(j,N-j),       1<=j<=h,
(j,N+2-j),     2<=j<=h+1,
(1,N).                                                 (10)
```

An edge `(i,j)` joins the radii of increasing ranks `i,j`. The counts are
`(h-1)+(h-1)+2=N` in (9) and `h+h+1=N` in (10). In
particular these are Hamiltonian-cycle edge multisets: every rank has degree
two. Equations (9)-(10) are the same parity formulas used in the continuum
functional, but the proof of (1) needs only that a common rank-edge multiset
is used for `S` and `T_{n,N}`.

## 3. Exact finite proof

The order statistics of an `N`-element subset of `{1,...,n}` obey

```text
r_i <= n-N+i=:t_i,                 1<=i<=N.             (11)
```

Indeed, there must be `N-i` distinct integers larger than `r_i`, so
`r_i+(N-i)<=n`. Equality in every coordinate of (11) is equivalent to
`S=T_{n,N}`.

For fixed `R>0`, `theta_R(a,b)` is strictly increasing in each positive
radius. Let `E_N` be the common rank-edge multiset and define the two closure
sums

```text
F_S(R)=sum_{(i,j) in E_N} theta_R(r_i,r_j),
F_T(R)=sum_{(i,j) in E_N} theta_R(t_i,t_j).             (12)
```

Coordinatewise monotonicity and (11) give

```text
F_S(R)<=F_T(R)                     for every R>0.       (13)
```

If `S!=T_{n,N}`, at least one inequality in (11) is strict. That rank has
degree two in the Supnick cycle, so at least its incident comparisons in
(13) are strict. Hence

```text
F_S(R)<F_T(R)                      for every R>0        (14)
```

in the nonterminal case.

Each closure sum is continuous and strictly decreasing from `N*pi>2*pi`
as `R->0+` to `0` as `R->infinity`. Let its unique `2*pi` root be `R_S` or
`R_T`. At `R=R_T`, (13) gives `F_S(R_T)<=2*pi`; strict decrease then gives
`R_S<=R_T`. Under (14), `F_S(R_T)<2*pi`, so `R_S<R_T`. This proves (1) and
its equality condition. Notice that the direction is transferred at the
roots only after the fixed-`R` closure sums have been compared.

## 4. Terminal roots for every cardinality regime

Put

```text
T_{k,n}={k,...,n},       N=n-k+1,
R_{k,n}=R_chain(Supnick(T_{k,n})).
```

The following triangular-array limit includes moving endpoints and both
boundary cardinality regimes.

**Terminal-array lemma.** If `n_j->infinity`, `1<=k_j<=n_j-2`, and

```text
k_j/n_j -> q in [0,1],
```

then

```text
R_{k_j,n_j}/n_j^2 -> Phi(q),                            (15)

Phi(q)=(2/pi) integral_q^((1+q)/2)
                         sqrt(x(1+q-x)) dx.             (16)
```

At `q=1`, the integral in (16) is zero.

To prove the lemma, let `E_{k,n}` be the terminal Supnick edges and set

```text
W_{k,n}=(1/n^2) sum_{(a,b) in E_{k,n}} sqrt(ab).        (17)
```

For `N=2h`, substituting the actual radii into (9) gives the two long
families

```text
(k+j-1,n-j),       1<=j<=h-1,
(k+j-1,n+2-j),     2<=j<=h,                            (18)
```

and the exceptional edges `(k,n)` and `(k+h-1,k+h)`. For `N=2h+1`, (10)
gives the same long-family formulas with their corresponding ranges and
only `(k,n)` exceptional. After division by `n`, both long families are
mesh-`1/n` Riemann sums on the interval from `k/n` to
`(1+k/n)/2`, with paired-coordinate sums respectively
`1+k/n-1/n` and `1+k/n+1/n`. Continuity of the square-root integrand,
including at `q=0`, and the `O(1/n)` contribution of the at most two
exceptional edges give, for every `q<1`,

```text
W_{k_j,n_j} -> J(q)
  :=2 integral_q^((1+q)/2) sqrt(x(1+q-x)) dx.          (19)
```

If `q=1`, then `N_j/n_j->0` and the elementary bound
`sqrt(ab)<=n_j` gives `0<=W_{k_j,n_j}<=N_j/n_j->0`, so (19) still holds
with `J(1)=0`.

It remains to transfer (19) to the implicit roots uniformly. Fix `r>0`,
set `R=rn^2`, and for one edge put

```text
v=sqrt(ab)/R,
u=sqrt(ab/((R+a)(R+b))).                              (20)
```

Since `1<=a,b<=n`, rationalizing the two denominator factors gives
`0<=v-u=O_r(n^-2)` uniformly in the edge. Also `u<=v<=1/(rn)`, and the
standard bound `0<=asin(u)-u<=u^3/3` applies for all sufficiently large
`n`. Summing over `N<=n` edges yields the uniform fixed-`r` closure estimate

```text
F_{k,n}(rn^2)=(2/r)W_{k,n}+O_r(1/n).                  (21)
```

For `q<1`, `J(q)>0`. Evaluating (21) at fixed radii immediately below and
above `J(q)/pi` brackets the unique decreasing closure root and proves
(15)-(16). For `q=1`, (19)-(21) show for every fixed `epsilon>0` that
`F_{k_j,n_j}(epsilon n_j^2)<2*pi` eventually. Hence
`0<=R_{k_j,n_j}/n_j^2<epsilon` eventually, proving the zero limit.

At the other boundary, symmetry of `sqrt(x(1-x))` and the beta integral
give

```text
Phi(0)=(2/pi) integral_0^(1/2) sqrt(x(1-x)) dx=1/8,
Phi(1)=0.                                               (22)
```

For `0<q<1`, substitute `x=qy` and put `lambda=1/q`. With the notation of
the optimized terminal-subset theorem this gives

```text
Phi(q)=c(1/q).                                         (23)
```

Thus `Phi` is continuous on `[0,1]`, its boundary values are strictly below
`C_term`, and the accepted exact optimization of `c` proves that its unique
maximum is at `q_*=1/lambda_*`, with value `C_term`. Since
`k/n=1-(N-1)/n`, equations (2) and (16) agree under `q=1-L`.

## 5. Proof of the arbitrary-sequence and envelope statements

Given `S_n` and `N_n`, put `k_n=n-N_n+1`. The finite theorem gives for every
`n`

```text
B_n<=R_{k_n,n}.                                        (24)
```

If `N_n/n->L`, then `k_n/n->1-L`; the terminal-array lemma turns (24) into
(6). In particular:

- if `N_n/n->0`, including bounded or unbounded sublinear cardinality, then
  `B_n/n^2->0`;
- if `N_n/n->L in (0,1)`, then
  `limsup B_n/n^2<=G(L)`, strictly below `C_term` unless `L=L_*`;
- if `N_n/n->1`, including `n-N_n` bounded or `o(n)`, then
  `limsup B_n/n^2<=1/8<C_term`.

If the cardinality ratio has no limit, choose a subsequence realizing the
limsup in (7), then a further subsequence on which `N_n/n` converges in the
compact interval `[0,1]`. Equation (6) on that further subsequence and (5)
prove (7).

If instead a subsequence has `B_n/n^2->C_term`, every convergent further
subsequence of its cardinality ratios has a limit `L` satisfying
`C_term<=G(L)<=C_term`. Uniqueness in (5) forces `L=L_*`. Compactness then
forces the whole cardinality-ratio subsequence to converge to `L_*`. This
argument gives no normalized shape rigidity for the radii inside the subset.

At fixed `n,N`, the strict equality statement in the finite theorem proves
the first identity in (8). For the lower limit in the second identity,
choose `k_n=floor(n/lambda_*)`; then `k_n/n->1/lambda_*` and (15) gives
`M_n/n^2>=R_{k_n,n}/n^2->C_term`. For the upper limit, choose a maximizing
`k_n` in (8). Every subsequence has a further subsequence with
`k_n/n->q`; (15) and the global maximum of `Phi` give an upper limit at
most `C_term`. This proves (8).

Finally, deletion from an actual feasible configuration and the
arbitrary-radii Supnick theorem give, for every selected `S_n`,

```text
R*(n)>=R*(S_n)>=R_chain(Supnick(S_n))=B_n.             (25)
```

Equations (7)-(8) therefore close the best possible leading coefficient of
this one-subset chain mechanism, not the value of the full geometric
problem.

## 6. Independent corroboration and epistemic limits

The task-local checker constructs (9)-(10) without importing `src/ringmin`,
enumerates all subsets for `3<=n<=11`, verifies their rank bounds and every
fixed-cardinality strict/equality case, and compares independently bisected
closure roots. It also checks that the largest enumerated bound is attained
by a terminal subset.

That enumeration is corroborative only. The exact result is the
rank-coordinate inequality, coordinatewise angular monotonicity, decreasing
root transfer, terminal triangular-array lemma, and compactness argument
above. The proof imports the published arbitrary-radii Supnick theorem and
the already proved exact optimization of `c(lambda)`. It does not use or
alter the production search, finite certificates, independent certificate
verifier, result artifacts, or historical arXiv-v1 paper.
