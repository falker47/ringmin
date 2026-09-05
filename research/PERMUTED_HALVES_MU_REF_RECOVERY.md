# Deterministic permutation recovery of the reflected coupling

```text
status=PROVED
classification=exact recovery theorem / exact fixed-order asymptotic theorem / proved global upper-bound corollary
domain=the single coupling mu_ref; integer m>=2 and the full sequence m->infinity
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question, notation and result

This note resolves only the realizability of mu_ref from
[PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md](PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md),
Section 6. Let alpha=alpha_* be the exact shift minimizer defined in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Sections 5-6.
In particular 0<alpha<1/2. Put

```text
ell=1/4, A=1+alpha, h(t)=1+{t+alpha},
D=[0,1] x [1,2] x [1,2],
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)).
```

For every continuous F on D the requested coupling is

```text
integral F dmu_ref
 = (1/2) integral_0^ell
     [F(t,A+t,A+ell-t)+F(t,A+ell-t,A+t)] dt
   + integral_ell^1 F(t,h(t),h(t)) dt.                         (1)
```

We construct a deterministic high permutation P_m for EVERY m>=2 with

```text
mu_m^(P_m)=(1/m) sum_{i=1}^m delta_(i/m,P_{m,i-1}/m,P_{m,i}/m)
   -> mu_ref weakly,   P_{m,0}=P_{m,m}.                       (2)
```

For sigma_m=(1,P_{m,1},...,m,P_{m,m}) and rho_m=R_full(sigma_m),
the uniform full-radius theorem from the relaxation note, Section 4,
then gives the exact limit

```text
rho_m/(2m)^2 -> C_ref=(integral g dmu_ref)/(4*pi)
                    =C_shift-delta_alpha/(4*pi)
                    <C_shift-1/(9984*pi),                    (3)
```

where C_shift=K(alpha)/(2*pi) and delta_alpha is the exact positive
integral in Section 5 below. Thus the best shift coefficient is strictly
improved by actual permuted-halves orders. No optimization of alpha,
permutations or the relaxed measure is performed here. The proof uses only
0<alpha<1/2 in recovery; alpha remains the one fixed constant alpha_*.

## 2. Explicit finite sequence and exact occurrences

For m>=2 define

```text
s=s_m=floor(alpha*m), q=q_m=2*floor(m/8),
beta=s/m, lambda=q/m, r=m-s,
H_m(j)=m+1+((j+s-1) mod m),          1<=j<=m.
```

Here mod has values 0,...,m-1. Define the index map and the high order by

```text
J_m(i) = q+2-i,    if 1<=i<=q and i is even;
         i,       otherwise;
P_{m,i}=H_m(J_m(i)),               1<=i<=m.                 (4)
```

This is a formula using integers and the previously defined exact alpha;
there are no random choices, subsequence selections or fitted parameters.
When m<8, q=0 and (4) is simply the original high shift.

Write q=2k. For i=2j-1 in the block, 1<=j<=k, J_m(i)=2j-1;
these are exactly the k odd ranks 1,3,...,q-1. For i=2j,

```text
J_m(2j)=2(k+1-j),       j=1,...,k,                          (5)
```

which lists the k even ranks q,q-2,...,2 exactly once. The remaining
ranks q+1,...,m are fixed. These three disjoint images partition
{1,...,m}; indeed J_m is an involution. H_m is a cyclic shift and hence
a bijection onto {m+1,...,2m}. Thus every high radius occurs in P_m
exactly once, including for q=0 and q=2. This is exact finite bookkeeping,
not a limiting marginal argument.

The block does not wrap: s<m/2 and q<=m/4 imply s+q<m. Consequently

```text
P_{m,i}=m+s+i,          i<=q odd;
P_{m,i}=m+s+q+2-i,      i<=q even;
P_{m,i}=H_m(i),         i>q.                                (6)
```

For example q=8 changes the first eight ranks to
(1,8,3,6,5,4,7,2), retaining all eight exactly once. No finite example
is used to prove (5).

## 3. Interior triples and all seam/wrap cells

For the convergence proof take m>=8, so q>=2. Write t_i=i/m and
A_m=1+beta. Using the actual predecessor from (6), every block cell
except i=1 has the EXACT normalized coordinates

| Cell | P_{m,i-1}/m | P_{m,i}/m | Number of cells |
|---|---|---|---|
| i even, 2<=i<=q | A_m+t_i-1/m | A_m+lambda-t_i+2/m | q/2 |
| i odd, 3<=i<=q-1 | A_m+lambda-t_i+3/m | A_m+t_i | q/2-1 |

In particular the even cells tend to the first orientation in (1), and
the odd cells tend to the second. Distinct finite high radii can approach
the same limiting value at t=ell/2; this introduces no duplicate radius.

Here is the complete exceptional bookkeeping, with r=m-s:

- The cyclic low seam is i=1 and uses P_{m,0}=P_{m,m}. Since q<m,
  P_{m,m}=m+s if s>0, and P_{m,m}=2m if s=0; P_{m,1}=m+s+1.
- The block-to-tail cell is i=q+1, with actual highs
  (P_{m,q},P_{m,q+1})=(m+s+2,m+s+q+1).
- If s>0, the high-wrap cell is i=r+1, with actual highs (2m,m+1).
  If s=0, this wrap is the cyclic cell i=1 already listed.
- The cell i=r is additionally set aside when comparing the shifted
  grid with h_alpha: P_{m,r}/m=2 whereas h_alpha(r/m) lies on the lower
  branch (also when alpha*m is an integer). This is an endpoint comparison
  issue, not an additional geometric seam.

Define exactly

```text
X_m={1,q+1,r,r+1} intersect {1,...,m}.                      (7)
```

Since r>m/2 and q<=m/4, r>q+1 for m>=8. Thus X_m has four cells if
s>0 and three if s=0. These are disjoint from 2,...,q. The numbers of
remaining tail cells are respectively m-q-3 and m-q-2. Adding the
q-1 interior block cells and X_m gives exactly m cells in both cases.
No triple is omitted from the empirical measure or from its full cost.
The exceptional empirical mass is exactly |X_m|/m<=4/m.

For every remaining tail cell q+2<=i<=m, i not in X_m, consecutive highs
are on the same unwrapped branch. More explicitly their normalized pair is

```text
(1+beta+t_i-1/m, 1+beta+t_i),    i<r;
(beta+t_i-1/m, beta+t_i),        i>r+1.                    (8)
```

The inequalities

```text
0<=alpha-beta<1/m,      0<=ell-lambda<2/m                  (9)
```

imply that h_alpha(t_i)=1+alpha+t_i for i<r and
h_alpha(t_i)=alpha+t_i for i>r. Thus each coordinate in (8) differs
from h_alpha(t_i) by at most 2/m. The extra exclusion of r makes this
uniform even at exact rational grid alignments.

## 4. Weak convergence on the entire sequence

For each m>=8 introduce a comparison probability measure nu_m with exactly
m equally weighted atoms. For i<=q use

```text
(t_i,A+t_i,A+ell-t_i),      i even;
(t_i,A+ell-t_i,A+t_i),      i odd;
```

and for i>q use (t_i,h(t_i),h(t_i)). Every atom belongs to D. For
i not in X_m, (6)-(9) show that the actual empirical atom is at distance
at most 3/m from its comparison atom in the max norm. For example the
odd-cell reflected coordinate error is

```text
(beta-alpha)+(lambda-ell)+3/m,
```

which lies in (0,3/m]; the other errors are no larger in absolute value.
The t coordinate agrees exactly. On X_m both actual and comparison atoms
are retained with weight 1/m, without a small-coordinate-error assertion.

Let M_F=||F||_infinity and omega_F be the modulus of continuity on D
in that norm. It follows that

```text
|integral F dmu_m^(P_m)-integral F dnu_m|
 <=omega_F(3/m)+2*M_F*|X_m|/m
 <=omega_F(3/m)+8*M_F/m ->0.                              (10)
```

There are exactly q/2 even and q/2 odd comparison block atoms. Each
parity grid has mesh 2/m and atom weight 1/m, hence half the usual
Riemann-sum weight. Since q/m->ell, their sums converge respectively to
the two half-weight integrals on [0,ell] in (1). The odd sum includes
i=1; (10) has explicitly paid for replacing its cyclic predecessor.

The comparison tail is the ordinary 1/m-mesh Riemann sum of
F(t,h(t),h(t)) starting at (q+1)/m. This bounded function is continuous
except possibly at t=1-alpha, so it is Riemann integrable. Moving the
lower endpoint q/m to ell costs at most M_F*(ell-q/m) in the integral,
which tends to zero. Endpoint conventions at the wrap affect at most
one sample and no integral. Therefore the tail tends to the last
integral in (1). Combining these three Riemann sums with (10) proves
(2) for every continuous F, along all integers m, not only multiples
of eight. The finitely many m<8 cannot change this limit.

For an optional quantitative audit, if F is L-Lipschitz in the max norm,
the same proof gives the convenient, deliberately loose bound

```text
|integral F dmu_m^(P_m)-integral F dmu_ref|
 <= (6*L+16*M_F)/m,                     m>=8.             (11)
```

Indeed (10) contributes (3L+8M_F)/m. The two parity Riemann sums on
[0,q/m] together contribute at most 2L/m. The diagonal sum on [q/m,1]
contributes at most L/m+4M_F/m: set aside the at most two mesh cells
whose closed intervals meet the single wrap; on every other cell the
map t->(t,h(t),h(t)) is 1-Lipschitz. Finally changing from reflection
to diagonal on the interval [q/m,ell], of length less than 2/m, costs
at most 4M_F/m. These bounds give (11). Lipschitz regularity is not
required in (2), and is not being assumed for g near t=0.

## 5. Full-radius coefficient and its strict saving

The exact all-pairs criterion in
[PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 1-6, applies to (4) at every m>=2, since it is a genuine
high permutation. It identifies rho_m as the unique root of

```text
sum_{i=1}^m max(theta_R(i,P_{m,i-1})+theta_R(i,P_{m,i}),
               theta_R(P_{m,i-1},P_{m,i}))=2*pi.             (12)
```

All exceptional cells of (7), including the cyclic chord, remain in (12).
The uniform theorem already proved in the relaxation note, Sections 2-4,
applies without a bound on high jumps or their number and gives

```text
rho_m/(2m)^2=(integral g dmu_m^(P_m))/(4*pi)+O(1/m).         (13)
```

Its root scale was justified there before the expansion, and its constant
is uniform over permutations. Since g is continuous and bounded on D,
(2) implies convergence of its integrals. Equation (13) now proves
the first equality in (3). This step concerns R_full, not R_chain.

For completeness the exact cost from the coupling note can be written
with M=A+ell/2 as

```text
delta_alpha=integral_(-ell/2)^(ell/2) [M-sqrt(M^2-u^2)] du,
integral g dmu_ref=2*K(alpha)-delta_alpha.                  (14)
```

On t<=ell=1/4 the cost is the chord sqrt(x*y), because
sqrt(t)*(1/sqrt(x)+1/sqrt(y))<=1 for x,y>=1. Substituting u=t-ell/2
in the reflected block gives (14); the diagonal tail is unchanged.
For u!=0,

```text
M-sqrt(M^2-u^2)=u^2/(M+sqrt(M^2-u^2))>u^2/(2*M).
```

Since M=9/8+alpha<13/8, integration proves

```text
delta_alpha>ell^3/(24*M)>1/2496,
C_ref=C_shift-delta_alpha/(4*pi)<C_shift-1/(9984*pi).       (15)
```

These are exact inequalities; no decimal value of alpha or quadrature
is a premise. In particular the actual sequence eventually has
rho_m/(2m)^2<C_shift. This does not determine the best coefficient over
all high permutations or the minimum cost in the relaxation.

## 6. Immediate geometric corollary and limits of the result

The full criterion supplies an actual feasible placement at rho_m, so
R*(2m)<=rho_m. Deleting only radius 2m from that placement leaves
{1,...,2m-1}, preserves central tangency and all pairwise non-overlap,
and gives R*(2m-1)<=rho_m. Therefore

```text
limsup_{n->infinity} R*(n)/n^2 <= C_ref < C_shift,           (16)
```

since (2m)^2/(2m-1)^2->1. This is solely an upper bound derived from
this coupling's explicit sequence, without an optimization problem or
new global lower bound. It combines with the existing C_term lower bound,
but neither endpoint is asserted to be sharp and no global normalized
limit is proved. There is no general recovery theorem for balanced
couplings, no determination of L_3, no finite global optimality claim,
and no contact/floating-circle conclusion.

The fixed-order recovery/coefficient has its sole stable owner in
knowledge/FIXED_ORDER_THEORY.md; the distinct global corollary (16) is
owned by knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md with a cross-reference.
Previous proof notes and dossiers retain their original task scope;
their earlier lack of a recovery assertion is resolved here. The public
paper, certified artifacts and production verifier remain unchanged.

## 7. Verification and authority

Sections 2-4 are the exact recovery proof; Sections 5-6 use the imported
uniform full-radius and feasibility theorems. The bounded exact checker in
[the task dossier](../ops/TASK-20260905__mu_ref_recovery/EVIDENCE.md)
audits the parity map with a separate list-reversal implementation,
every empirical predecessor including the seam, exceptional-cell counts,
coordinate estimates and rational polynomial test integrals. Its bounded
diagnostics do not replace the all-m proof and do not constitute a global
certificate. Independent external review of this proof and its imported
dependencies remains pending.
