# Alternating-halves fixed-order full asymptotics

```text
status=PROVED
classification=exact finite fixed-order characterization / exact asymptotic theorem / explicit feasible construction / proved global limsup corollary
domain=integer m>=2, n=2m, then m->infinity
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Statement and epistemic scope

For `R,a,b>0`, write

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))).             (1)
```

Let `n=2m`, and consider only the cyclic order

```text
sigma_{2m}=(1,m+1,2,m+2,...,m,2m).                    (2)
```

The low and high radii in its `i`-th cell are

```text
L_i=i,    H_i=m+i,    1<=i<=m,
H_0=H_m.
```

At a fixed `R`, define the two adjacent angles and the high-to-high chord
across the low valley `L_i` by

```text
A_i=theta_R(L_i,H_i),
B_i=theta_R(H_i,L_{i+1})       (1<=i<m),
B_m=theta_R(H_m,L_1),
C_i=theta_R(H_{i-1},H_i),

S_m(R)=sum_{i=1}^m max(A_i+B_{i-1},C_i),              (3)
```

where `B_0=B_m`. The first result is an exact finite characterization:

```text
R_full(sigma_{2m}) is the unique root of S_m(R)=2*pi.  (4)
```

Thus the only fixed-`R` constraints needed in the exact obstruction are,
cell by disjoint cell, the two adjacent constraints around a low radius and
the high-to-high constraint across that valley. Section 4 gives explicit
gaps and proves that these constraints imply every other pairwise constraint.

For the asymptotic constants, put

```text
J = integral_0^1 sqrt(t(t+1)) dt
  = 3sqrt(2)/4-log(3+2sqrt(2))/8,

K = J-1/12+log(3)/8
  = 3sqrt(2)/4-1/12
      +(log(3)-log(3+2sqrt(2)))/8.                    (5)
```

Then the chain and full fixed-order limits are

```text
R_chain(sigma_{2m})/(2m)^2 -> J/(2*pi)
  = 0.13374056850825863009...,

R_full(sigma_{2m})/(2m)^2 -> K/(2*pi)
  = 0.14233385361931275491....                         (6)
```

The decimals are diagnostic displays, not proof premises. The inequalities

```text
0<J<K<1                                                   (7)
```

are proved below. In particular, this family has a fixed-order full limit
strictly between its chain coefficient and `1/(2*pi)`.

Finally, deletion transfers only the justified global upper consequence:

```text
limsup_{n->infinity} R*(n)/n^2 <= K/(2*pi)<1/(2*pi).    (8)
```

Equation (8) does not assert equality, existence of the normalized global
limit, or global optimality of (2). No other order family is optimized here.

## 2. A thick-shell angular lemma

The sufficiency proof needs one exact fact about the high radii. It is not an
asymptotic approximation.

**Lemma 1 (thick-shell triangle).** If

```text
0<a<=b<=c<=2a,
```

then, at every `R>0`,

```text
theta_R(a,b)+theta_R(a,c)>=theta_R(b,c).               (9)
```

By monotonicity of (1) in each radius, the left side of (9) is at least
`2 theta_R(a,a)` and the right side is at most `theta_R(c,c)`. It is therefore
enough to prove

```text
2 theta_R(a,a)>=theta_R(c,c).                          (10)
```

Set `x=a/(R+a)` and `z=c/(R+c)`. Since `c<=2a`,

```text
z<=2a/(R+2a)=2x/(1+x).                                 (11)
```

If `x>=1/sqrt(2)`, then `2 asin(x)>=pi/2>=asin(z)`. If
`0<x<=1/sqrt(2)`, then

```text
(1+x)^2(1-x^2)-1
  =x(2-2x^2-x^3)>0,                                   (12)
```

because `2-2x^2-x^3` is decreasing and is still positive at
`x=1/sqrt(2)`. Hence

```text
2x/(1+x)<=2x sqrt(1-x^2)=sin(2 asin(x)).               (13)
```

Both angles in (13) lie in `[0,pi/2]`, so (11)-(13) give
`asin(z)<=2 asin(x)`, which is exactly (10).

The following cyclic consequence will control the seam.

**Lemma 2 (increasing thick-shell cycle).** Let
`a_1<=...<=a_m<=2a_1`. Suppose a cyclic set of nonnegative high-to-high
path lengths `d_i`, with `a_{m+1}=a_1`, satisfies

```text
d_i>=theta_R(a_i,a_{i+1})    for every i.              (14)
```

Then both cyclic path lengths between every pair `a_i,a_j` are at least
`theta_R(a_i,a_j)`.

For `i<j`, the forward path contains `d_{j-1}`, and

```text
d_{j-1}>=theta_R(a_{j-1},a_j)>=theta_R(a_i,a_j).       (15)
```

If `j<m`, the complementary path contains `d_j`, which gives the same
conclusion by monotonicity. If `j=m,i=1`, it contains the closing edge `d_m`,
whose lower bound is exactly the required one. Finally, if `j=m,1<i<m`, it
contains `d_m+d_{i-1}`. Monotonicity and Lemma 1 give

```text
d_m+d_{i-1}
 >=theta_R(a_m,a_1)+theta_R(a_{i-1},a_i)
 >=theta_R(a_m,a_1)+theta_R(a_1,a_i)
 >=theta_R(a_i,a_m).                                  (16)
```

This proves both directions, including the increasing-order seam.

## 3. The exact cellwise lower obstruction

Consider any feasible angular gaps in the order (2). Around `L_i`, the two
adjacent gaps are the gap from `H_{i-1}` to `L_i` and the gap from `L_i` to
`H_i`. Their individual adjacent constraints make their sum at least
`B_{i-1}+A_i`. The pair `(H_{i-1},H_i)` also uses this two-edge path, so the
same sum is at least `C_i`. Therefore the cell contributes at least

```text
max(A_i+B_{i-1},C_i).                                  (17)
```

The `m` cells partition all `2m` cyclic gaps. Summing (17) gives the exact
necessary condition

```text
2*pi>=S_m(R).                                          (18)
```

This is the matching leading obstruction requested in the problem, but it is
stronger: it is an exact finite fixed-`R` obstruction. The next section proves
that it is also sufficient; no unlisted long pair can strengthen (18).

## 4. Explicit gaps and the all-pairs proof

Assume `S_m(R)<=2*pi`, and put

```text
e_i=[C_i-A_i-B_{i-1}]_+.
```

Give the cyclic gaps the explicit values

```text
g(L_i,H_i)=A_i+e_i,
g(H_i,L_{i+1})=B_i,                                   (19)
```

where `L_{m+1}=L_1`. The two gaps through valley `L_i` then have total

```text
B_{i-1}+A_i+e_i=max(A_i+B_{i-1},C_i).                 (20)
```

Thus the gaps in (19) have total `S_m(R)`. Add the remaining angle

```text
E=2*pi-S_m(R)>=0                                       (21)
```

to any one gap, for example the seam gap `g(H_m,L_1)`. This is an explicit
closed placement once all pairwise lower bounds are verified.

First contract each two-edge valley path
`H_{i-1}->L_i->H_i` to a high-to-high edge. Equation (20) says its length is
at least `C_i`. The high radii satisfy

```text
H_1=m+1<...<H_m=2m<2H_1.                              (22)
```

Lemma 2 therefore proves both directed constraints for every high-high pair,
including all paths that use the `H_m,H_1` seam.

Now take a low-high pair `(L_i,H_j)`. One cyclic path leaves `L_i` through
`H_i`; the other leaves it through `H_{i-1}`. If that neighboring high radius
is the endpoint, its adjacent gap already gives (1). Otherwise the contracted
high path has length at least its direct high-high angle, which is at least
`theta_R(L_i,H_j)` because both `H_i` and `H_{i-1}` exceed `L_i`. Hence both
cyclic paths satisfy the low-high constraint.

For a low-low pair, each cyclic path either contains a contracted high path
between high radii at least as large as the two low endpoints, or the lows are
consecutive and the path contains their common high neighbor. In the first
case monotonicity makes that high-high angle at least the required low-low
angle. In the consecutive case one of the adjacent high-low gaps alone is at
least the required low-low angle. The same argument applies in the opposite
cyclic direction. Thus every low-low pair is also safe.

Before adding `E`, both paths between every pair already obey their angular
lower bound. Adding `E` increases one path and leaves its complement
unchanged, so all lower bounds remain true; afterward the two path lengths sum
to `2*pi`. By the exact angular reformulation, (19)-(21) are an all-pairs
feasible placement.

Together with (18), this proves the exact equivalence

```text
sigma_{2m} is fully feasible at R  iff  S_m(R)<=2*pi.  (23)
```

Every angle in (3) is continuous and strictly decreasing in `R`, so `S_m` is
continuous and strictly decreasing. As `R` decreases to zero, every angle
tends to `pi`, whence `S_m(R)->2*pi*m>2*pi`; as `R->infinity`, `S_m(R)->0`.
The unique root in (4) follows.

This also treats the alternating valleys and seam exactly. The seam valley is
`H_m->L_1->H_1`; if its chord dominates, (19) puts the needed excess into
`g(L_1,H_1)`, while `g(H_m,L_1)` retains its adjacent lower bound. Lemma 2,
not an asymptotic appeal to a long complementary path, verifies the remaining
seam-crossing pairs.

## 5. Uniform angular scaling

Fix `r_0>0`, let `R=r n^2` with `r>=r_0`, and take any `1<=a,b<=n`. Uniformly
in these radii,

```text
theta_{r n^2}(a,b)=2sqrt(ab)/(r n^2)+O(n^-2).          (24)
```

Indeed, if

```text
u=sqrt(ab/((R+a)(R+b))),    v=sqrt(ab)/R,
```

then `u,v=O(1/n)` and

```text
0<=v-u<=v(a+b)/(2R)=O(n^-2).                           (25)
```

The Taylor remainder `asin(u)-u=O(u^3)=O(n^-3)` is uniform as well. This
proves (24). In particular,

```text
max_{a,b<=n} theta_{r n^2}(a,b)
 =theta_{r n^2}(n,n)=O(1/n).                          (26)
```

All limits below are uniform when `r` stays in a compact subinterval of
`(0,infinity)`.

## 6. The chain coefficient

Let `Q_m(R)` be the adjacent closure sum for (2):

```text
Q_m(R)=sum_{i=1}^m A_i+sum_{i=1}^m B_i.               (27)
```

Put `x_i=i/n`, so `H_i/n=x_i+1/2`. The non-seam terms in (24) form two
Riemann sums, while the single seam term `B_m` is `O(n^-3/2)`. Hence, for
every fixed `r>0`,

```text
Q_m(r n^2)
 ->(1/r) integral_0^(1/2) 4sqrt(x(x+1/2)) dx
 =J/r.                                                (28)
```

The substitution `t=2x` gives the integral in (5). To locate the root without
assuming its scale, fix `0<epsilon<J/(2*pi)`. Equation (28) gives

```text
Q_m((J/(2*pi)-epsilon)n^2)>2*pi,
Q_m((J/(2*pi)+epsilon)n^2)<2*pi                       (29)
```

for all sufficiently large even `n`. The closure sum is continuous and
strictly decreasing, so its unique root is bracketed by (29). This proves the
first limit in (6).

## 7. The full coefficient and the active valleys

The seam cell `i=1` in (3) is `O(1/n)` by (26), so it has no leading mass.
For `2<=i<=m`, (24) and the definitions give, uniformly with
`x_i=i/n`,

```text
A_i+B_{i-1}
 =(1/(r n))(4sqrt(x_i(x_i+1/2))+o(1)),

C_i=(1/(r n))(2(x_i+1/2)+o(1)).                       (30)
```

The maximum is Lipschitz in its two arguments, so the triangular Riemann sum
in (3) yields

```text
S_m(r n^2)->K/r,                                      (31)

K=integral_0^(1/6) 2(x+1/2) dx
  +integral_(1/6)^(1/2) 4sqrt(x(x+1/2)) dx.           (32)
```

The switch is analytic:

```text
2(x+1/2)>=4sqrt(x(x+1/2))  iff  0<=x<=1/6.            (33)
```

Thus, away from the transition window, the controlling pairwise families are
exactly:

- the high-high chords across low valleys with `i/n<1/6`, equivalently
  `i/m<1/3`;
- the two adjacent chain constraints around each low valley with `i/n>1/6`;
- the equality transition at `i/n=1/6`, which affects no leading integral;
- the cyclic seam valley, whose chord dominates asymptotically but contributes
  only `O(1/n)` to the closure sum and is nevertheless handled exactly by
  (19) and Lemma 2.

No longer pairwise family changes (31), because the exact construction in
Section 4 already satisfies every such constraint at the cellwise lower
obstruction.

For the evaluation of (32),

```text
integral_0^(1/6) 2(x+1/2) dx=7/36,

integral_0^(1/6) 4sqrt(x(x+1/2)) dx
 =integral_0^(1/3) sqrt(t(t+1)) dt
 =5/18-log(3)/8.                                      (34)
```

Subtracting the second line of (34) from `J` and adding the first gives the
formula for `K` in (5).

Now use the exact feasibility equivalence (23). For every fixed `r<K/(2*pi)`,
(31) gives `S_m(rn^2)>2*pi` eventually, so the order is infeasible. For every
fixed `r>K/(2*pi)`, it gives `S_m(rn^2)<2*pi` eventually, and (19)-(21) give
an explicit all-pairs placement. Bracketing the unique root proves the second
limit in (6). The same cell family supplies both the lower obstruction and
the constructive upper bound.

Finally,

```text
K-J=-1/12+log(3)/8=(3log(3)-2)/24>0,                  (35)
```

because `log(3)=integral_1^3 dt/t>2/3`. Also
`log(3)-log(3+2sqrt(2))<0`, while `sqrt(2)<13/9`; hence

```text
K<3sqrt(2)/4-1/12<13/12-1/12=1.                      (36)
```

This proves (7), and therefore the strict comparison with `1/(2*pi)` without
using a decimal approximation.

## 8. Deletion and the all-integer global limsup

For even sizes, the constructed fixed order is merely one admissible order,
so

```text
R*(2m)<=R_full(sigma_{2m}).                            (37)
```

If a feasible configuration for radii `1,...,N` is given, deleting the circle
of radius `N` leaves a feasible configuration for `1,...,N-1` around the same
central circle: central tangency of every retained circle and all retained
pairwise non-overlap inequalities are unchanged. Therefore

```text
R*(N-1)<=R*(N).                                       (38)
```

For odd `n=2m-1`, apply (38) to the explicit even construction:

```text
R*(2m-1)<=R*(2m)<=R_full(sigma_{2m}).                  (39)
```

Divide (37) by `(2m)^2`, divide (39) by `(2m-1)^2`, and use
`(2m/(2m-1))^2->1`. The fixed-order limit (6) gives (8) on both parity
subsequences. Thus deletion does transfer the same upper coefficient to the
global all-integer limsup. It does not transfer a matching lower bound, make
the odd induced order a member of the family (2), or prove that the global
limsup equals this coefficient.

## 9. Independent finite diagnostic and limitations

The task-local checker independently implements (1), the chain closure, the
cellwise root (4), the explicit gaps (19), and a direct audit of both cyclic
paths for every pair; it does not import `src/ringmin`. At 70 decimal digits it
gives the following numerical observations:

```text
n=160  R_full(sigma_n)/n^2 = 0.139557268125223375...
n=320  R_full(sigma_n)/n^2 = 0.140940266075415282...
n=640  R_full(sigma_n)/n^2 = 0.141635631882792259...
```

These reproduce the independently supplied reviewer values and approach the
proved constant `0.142333853619312754...`; they are corroboration only. The
analytic proof is Sections 2-8.

The result does not determine a sharp subleading expansion, the exact finite
index of every valley switch, any global lower coefficient beyond previously
proved bounds, the value or existence of `lim R*(n)/n^2`, or the asymptotics
of a broader family of orders. The public arXiv-v1 paper, production code,
finite certificates, verifier, and result artifacts remain unchanged.
