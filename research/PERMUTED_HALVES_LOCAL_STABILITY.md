# Uniform local stability of permuted alternating halves

```text
status=PROVED
classification=exact fixed-order theorem / proved asymptotic corollaries
domain=all integers m>=2, all high permutations, adjacent position swaps
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Objects, quantifiers and statements

Let P permute {m+1,...,2m}, with low radii kept in increasing order in
sigma_P=(1,P_1,2,P_2,...,m,P_m). At R>0 put

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_t(a,b;R)=max(theta_R(t,a)+theta_R(t,b),theta_R(a,b)),
S_P(R)=sum_{i=1}^m F_i(P_{i-1},P_i;R),  P_0=P_m.
```

The exact theorem in [PERMUTED_ALTERNATING_HALVES.md](PERMUTED_ALTERNATING_HALVES.md),
Sections 2-6, proves that S_P(R)<=2*pi is equivalent to full all-pairs
feasibility, and that its unique positive level-2*pi root is
rho_P=R_full(sigma_P). This is not the adjacent-chain root or R*(2m).

An adjacent transposition exchanges neighboring POSITIONS in the high
list, not necessarily consecutive numerical radii. The results hold even
if the cyclic pair of positions (m,1) is allowed, and hence also for the
usual linear adjacent transpositions. All low labels remain fixed.

**Uniform stability theorem.** Suppose a path from P to Q uses k adjacent
swaps, with high values x_h,y_h exchanged at step h. Define its weight
D=sum_{h=1}^k |x_h-y_h|. For m>=3 set

```text
L_m=max(1,(m+1)(csc(pi/m)-1)),
C_m=sqrt(2)/(2*pi) * (1+2m/L_m).
```

Then, for every such path,

```text
|rho_P-rho_Q| <= C_m D <= 2D <= 2k(m-1),              (1)
C_m = sqrt(2)/(2*pi) + O(1/m).
```

For m=2 all high permutations have identical S and rho. Consequently,
for every FIXED nonnegative integer K,

```text
sup_{d_adj(P,Q)<=K} |rho_P-rho_Q|/m^2
 <= 2K(m-1)/m^2 -> 0.                               (2)
```

The supremum includes all permutations and swap positions at each m.
There is no assumption of convergence, regularity, or an active-branch
pattern for either permutation. In particular the bound is O_K(m).
When D=O_K(1), as for boundedly many swaps of numerically consecutive
highs, it is O_K(1). More generally D=o(m^2), or k=o(m), suffices for (2).

The scale O(m) for ONE unrestricted adjacent swap is optimal in order:
Section 6 supplies explicit permutations with a radius difference >=c*m
for all m>=32, for an absolute c>0. Section 7 proves the stronger O(1/m)
bound for swapping the first two highs of any interior increasing shift.

## 2. Uniform root bounds

For every P and m>=3, each chord is at least theta_R(m+1,m+1). At rho_P,

```text
2*pi >= 2m asin((m+1)/(rho_P+m+1)).
```

Since pi/m<=pi/3<pi/2, monotonicity of sin on this interval gives
rho_P>=(m+1)(csc(pi/m)-1). This inference is not used at m=2.
Also rho_P>1 for m>=3: at R=1 every one of the 2m adjacent angles is
at least theta_1(1,m+1)>=theta_1(1,4)>pi/3, because its squared asin
argument is 2/5>1/4. Therefore S_P(1)>2*pi. Thus rho_P>=L_m.

A convenient coarser lower bound, for every m>=4, is

```text
rho_P > m^2/(4*pi).                                 (3)
```

Indeed csc(pi/m)>m/pi, and

```text
(m+1)(m/pi-1)-m^2/(4*pi)
 = [3m^2/4+(1-pi)m-pi]/pi > 0.
```

At m=4 the numerator is 16-5*pi>2/7 using pi<22/7;
its derivative in real m>=4 is 3m/2+1-pi>0.

For later use a uniform upper bound is rho_P<2m^2. Convexity of asin
gives asin(z)<=pi*z/2 on [0,1]. Hence theta_R(a,b)<pi*sqrt(ab)/R
<=2*pi*m/R for 1<=a,b<=2m. Each cell is less than 4*pi*m/R, so
S_P(2m^2)<2*pi. Strict decrease proves the upper bound.

Finally C_m<2: at m=3, L_m>=1 gives C_m<=7sqrt(2)/(2*pi)<7/4<2,
using sqrt(2)<3/2 and pi>3. At m>=4, the derivation of (3) also gives
L_m>m^2/(4*pi), hence

```text
C_m < sqrt(2)/(2*pi) * (1+8*pi/m)
 <= sqrt(2)+sqrt(2)/(2*pi) < 7/4 < 2.
```

The standard limit sin(z)/z->1 gives L_m~m^2/pi and the stated
C_m=sqrt(2)/(2*pi)+O(1/m); for this O estimate it also suffices to use
(3), which bounds the nonconstant term by 4sqrt(2)/m.

## 3. Radial contraction through every max-branch change

Let z=sqrt(ab/((R+a)(R+b))) and w=asin(z)=theta_R(a,b)/2.
Direct differentiation gives

```text
-partial_R theta_R(a,b)
 = tan(w) * (1/(R+a)+1/(R+b))
 >= theta_R(a,b)/(R+2m),                            (4)
```

for a,b<=2m. Here 0<w<pi/2 and tan(w)>=w. Integrating the logarithmic
derivative between 0<r<=s proves

```text
theta_s(a,b) <= (r+2m)/(s+2m) * theta_r(a,b).
```

The SAME positive factor bounds both branches of every F, so it also
bounds their maximum and sum:

```text
S_P(s) <= (r+2m)/(s+2m) * S_P(r).                   (5)
```

No differentiability of F or S at a branch tie is assumed. If r is the
smaller of two full roots and s is the larger, and the score of the
larger-root order at r exceeds 2*pi by at most epsilon, (5) gives

```text
s-r <= (r+2m)*epsilon/(2*pi).                       (6)
```

Both roots must be those of the full criterion. A fixed-R score change
without the level-2*pi comparison would not establish (6).

## 4. A high-value-weighted bound for one swap

For a<=2m and b in [m+1,2m], direct differentiation gives

```text
h_R(a;b)=partial_b theta_R(a,b)
 = sqrt(R*a)/(sqrt(b)(R+b)sqrt(R+a+b))
 <= sqrt(a/b)/R <= sqrt(2)/R.                       (7)
```

Thus, for x<y in the high shell and t<=m<a, BOTH branches defining
F_t(a,b;R) are increasing and Lipschitz in b with the same constant.
Taking their maximum preserves both properties, including a branch
crossing. In particular

```text
0 <= F_t(a,y;R)-F_t(a,x;R) <= sqrt(2)*(y-x)/R.       (8)
```

For a swap at positions j,j+1 with m>=3, write cyclically
u=P_{j-1}, x=P_j, y=P_{j+1}, v=P_{j+2}, l=j, r0=[j+2]_m.
The two-cell identity from
[PERMUTED_HALVES_ADJACENT_SWAP.md](PERMUTED_HALVES_ADJACENT_SWAP.md), Section 1, is

```text
S_Q-S_P = F_l(u,y)-F_l(u,x) - [F_r0(v,y)-F_r0(v,x)]. (9)
```

The middle cell [j+1]_m is invariant by symmetry. If x<y, the two
bracketed increments belong to the SAME interval in (8); their difference
has absolute value at most the interval's length, not twice its length.
If x>y reverse the increments. Hence, at every R>0,

```text
|S_Q(R)-S_P(R)| <= sqrt(2)*|x-y|/R.                 (10)
```

Apply (6) at r=min(rho_P,rho_Q), with epsilon given by (10). This gives

```text
|rho_Q-rho_P|
 <= sqrt(2)/(2*pi) * (1+2m/r) * |x-y|
 <= C_m |x-y|.                                     (11)
```

At m=3 the exterior highs coincide, u=v, but the two exterior cells are
distinct and (9)-(11) remain valid. At j=m-1 and j=m the low labels are
(m-1,1) and (m,2); (7)-(8) require no order between them. At m=2 each
cell retains its unordered high pair, so S_Q=S_P exactly; (9) must not
double-count the coincident exterior cell. The criterion excludes m=1.
Telescoping (11) along any path proves (1)-(2), including K=0 and ties.

## 5. A chord rectangle bound for the first two positions

For every m>=32, every high permutation, and every
R>=m^2/(4*pi), the exterior cells of the j=1 swap (lows 1 and 3)
are strictly chord-active, including all real high values in [m+1,2m].
To see this use the exact branch criterion from the adjacent-swap note:

```text
F_t(a,b;R)=theta_R(a,b) strictly if
kappa=1/R+1/a+1/b+2sqrt(1/(Ra)+1/(Rb)+1/(ab)) < 1/t.
```

With pi<4 and m>=32,

```text
kappa < 16/m^2 + [2+2sqrt(1+32/m)]/m
      < 16/m^2+5/m <= 11/64 < 1/3 <= 1/t.           (12)
```

This is a uniform exact sign bound, not a sampled branch observation.
It applies on the whole interval between the two roots by (3).

Another direct derivative identity is

```text
theta_ab(R;a,b)
 = sqrt(R)/(2sqrt(ab)(R+a+b)^(3/2))
 = 1/[2sqrt(ab)R] * (1+(a+b)/R)^(-3/2) > 0.        (13)
```

Consequently, where these two cells are chords, (9) equals the oriented
rectangle integral

```text
Delta(R)=S_Q(R)-S_P(R)
 = - integral_u^v integral_x^y theta_ab(R;a,b) db da. (14)
```

Signed integrals allow either ordering of u,v or x,y. Since the integrand
is <=1/[2(m+1)R], (6) at the smaller root r gives

```text
|rho_Q-rho_P|
 <= |u-v|*|x-y|/[4*pi*(m+1)] * (1+2m/r)             (15)
 <= |u-v|*|x-y|/[4*pi*(m+1)] * (1+8*pi/m).
```

If u<v and x<y, (14) is strictly negative at rho_P, so rho_Q<rho_P.
Other orientations have the corresponding opposite or equal sign.
Equation (15) is specific to the proved chord regime, unlike (11).

## 6. Why a uniform o(m) bound for arbitrary single swaps is false

For every m>=32 take

```text
P=(m+2, 2m, 2m-1, m+3, m+4, ..., 2m-2, m+1),
Q=the swap of P_1 and P_2.
```

Each integer high occurs once. Here u=m+1<v=2m-1 and x=m+2<y=2m,
so r=rho_Q<s=rho_P. At R=s, (3) and pi<4 give s>m^2/16>=2m.
On the rectangle in (14), sqrt(ab)<=2m and 1+(a+b)/s<=3. Therefore
3^(3/2)<6 and (13) yield

```text
epsilon=2*pi-S_Q(s)
 >= (m-2)^2/(24*m*s).                              (16)
```

We also need an UPPER radial rate, rather than reversing (4).
At every R in [r,s], R>2m, so z<=2m/(R+2m)<=1/2. Since asin(z)>=z,

```text
(-partial_R theta)/theta
 <= 1/[R sqrt(1-z^2)] <= 2/(sqrt(3)R) < 2/R.
```

Each angle, each chain sum, and hence each maximum satisfies the
integrated lower contraction with factor (R_1/R_2)^2. The finite maxima
are locally Lipschitz; alternatively differentiating almost everywhere
gives -S_Q'(R)<=2S_Q(R)/R. On [r,s], S_Q(R)<=2*pi, so

```text
epsilon <= 4*pi*(s-r)/r.
```

From Section 2, r>m^2/16 and s<2m^2, hence r/s>1/32. Combining with
(16) gives the explicit, deliberately loose lower bound

```text
rho_P-rho_Q > (m-2)^2/(3072*pi*m) >= m/(12288*pi).   (17)
```

This proves linear sharpness of the unrestricted one-swap scale without
an asymptotic limit for P, numerical fitting, or permutation enumeration.

## 7. The m=4 counterexample and its large-m continuation

At m=4, the earlier rational certificate proves, for
B=(7,8,5,6), A=(8,7,5,6),

```text
0.0157658012 < rho_B-rho_A < 0.0157658014.
```

This is a computer-certified finite result imported from
[PERMUTED_HALVES_ROOT_SEARCH.md](PERMUTED_HALVES_ROOT_SEARCH.md), Sections 3-5.
Here |x-y|=1; (11) applies directly and gives |rho_A-rho_B|<=C_4<2.
It does not predict the sign. The prior negative sign is a mixed/chain
exchange at rho_B. The large-m chord argument (12) is not applicable
at m=4, and must not be used to reclassify those branches.

To state an asymptotic consequence, specify a sequence, not just this
one finite pair. Let B_m be the increasing cyclic high shift with index
s_m, and A_m its first-two-high swap. If

```text
1 <= s_m <= m-3,
```

then (u,x,y,v)=(m+s_m,m+s_m+1,m+s_m+2,m+s_m+3).
For m>=32 equations (14)-(15) prove uniformly over these shifts

```text
0 < rho_{B_m}-rho_{A_m}
 <= 3/[4*pi*(m+1)] * (1+8*pi/m) = O(1/m).           (18)
```

The first two highs and their exterior neighbors do not cross the high
wrap in this range. No assertion (18) is made for s=0,m-2,m-1: near
the wrap the exterior difference can be O(m), and the swapped values
can themselves differ by m-1. The unconditional bound (11) still applies.
In particular the m=4 best shift has s=2=m-2, outside (18)'s range.

One precise continuation of the counterexample is to choose B_m as ANY
finite root-minimizing shift at each m, and then perform this first swap.
The already proved shift theorem in
[SHIFTED_ALTERNATING_HALVES.md](SHIFTED_ALTERNATING_HALVES.md), Sections 4-6,
gives s_m/m->alpha_* in (0,1/2). This follows also by compactness:
any subsequential shift-ratio limit must minimize its continuous limit
functional, whose minimizer is unique. Thus eventually 1<=s_m<=m-3;
(18) applies. At m=4 this definition chooses exactly B and A above.
No finite search for B_m is required for this existential corollary.

To avoid confusing the swap budget K with the previous note's functional,
call that functional script-K here:

```text
script-K(alpha)=integral_0^1
  max(sqrt(t*(1+{t+alpha})), (1+{t+alpha})/2) dt,
C_shift=script-K(alpha_*)/(2*pi).
```

Its endpoint convention at alpha=1 agrees almost everywhere with alpha=0.
For this continuation, the precise conclusion is

```text
rho_{A_m}/(2m)^2 -> C_shift,
rho_{B_m}/(2m)^2 -> C_shift,
0 < [rho_{B_m}-rho_{A_m}]/(2m)^2 = O(m^-3)
  for all sufficiently large m.                    (19)
```

Thus even strict eventual improvement over the best finite shift can
coexist with exactly the same leading quadratic coefficient. Equation
(18) controls the difference only; it does not give an O(1/m) remainder
for either individual radius relative to 4*C_shift*m^2.

## 8. What the stability theorem does and does not decide

For arbitrary sequences P_m,Q_m at bounded adjacent distance, (2) says
their normalized difference tends to zero. They have identical liminf
and limsup, and if either has a normalized limit, both have that limit.
This does not assert that arbitrary permutation sequences converge.

More uniformly, let U_{m,K} be the union of the distance-K balls about
all increasing shifts, with K fixed. It contains the shifts themselves,
and (1) gives

```text
0 <= min_shift rho - min_{P in U_{m,K}} rho_P <= 2K(m-1).
```

Therefore the minimum over this entire enlarged family, divided by
(2m)^2, still tends to C_shift. The same conclusion holds for K=o(m).
A sequence with a strictly smaller leading coefficient than C_shift
must have adjacent distance at least of order m from the shift family;
this is only a necessary condition, not a sufficient construction.

A bounded local modification can change finite roots, their rankings,
and subleading behavior, as the m=4 certificate and (17)-(18) demonstrate.
It cannot change an existing quadratic leading coefficient. This does
not settle optimization over all high permutations, give an all-order
limit for R*(n), improve the existing global upper coefficient, establish
global optimality at m=4, or classify contacts or floating circles.

## 9. Verification and authority

The proof is the analytic argument above, using the imported exact full
criterion and the separately proved shifted-family limit only where
explicitly cited. Symbolic identities, exact scalar gates, a targeted
rational recheck of the two m=4 brackets, and small deterministic
alternate-angle diagnostics are recorded in
ops/TASK-20260905__permuted_halves_local_stability/.
No factorial enumeration or production-code import is involved.

High-precision diagnostics are finite numerical observations, not interval
certificates of the uniform theorem. The reused m=4 rational checker is
coupled to the earlier finite evidence and is identified as such in the
dossier. Independent human review remains pending. The sole stable
thematic owner is knowledge/FIXED_ORDER_THEORY.md. Published assets,
global certificates and the production verifier are unchanged.
