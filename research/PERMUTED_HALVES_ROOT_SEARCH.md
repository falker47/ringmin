# Permuted alternating halves: a minimal root-level shift counterexample

```text
status=REFUTED root-level cyclic-shift conjecture
classification=disproved claim / computer-certified finite result
domain=all high permutations for m=2,3,4; stopped before m=5
checked_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Exact question and result

For integer m>=2, let P permute {m+1,...,2m}, retain the low labels in
increasing order, and write sigma_P=(1,P_1,...,m,P_m), P_0=P_m. Define

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_i(a,b)=max(theta_R(i,a)+theta_R(i,b),theta_R(a,b)),
S_P(R)=sum_{i=1}^m F_i(P_{i-1},P_i),
rho_P = the unique positive root of S_P(R)=2*pi.
```

The exact theorem in `research/PERMUTED_ALTERNATING_HALVES.md` proves
continuity, strict decrease and R_full(sigma_P)=rho_P. The tested
conjecture was precisely

```text
for every integer m>=2,
min_{P a permutation of {m+1,...,2m}} rho_P
 = min_{0<=s<m} rho_{P(s)},  P(s)_i=m+1+((i+s-1) mod m).    (1)
```

**Finite certified refutation.** The least counterexample size is m=4.
At that size the unique minimizing high permutation is A=(8,7,5,6),
whereas the unique best shift is B=(7,8,5,6), with

```text
rho_A < 577/100 < rho_B,
0.0157658012 < rho_B-rho_A < 0.0157658014.                 (2)
```

Uniqueness here is among the displayed labeled permutations, with lows
fixed in increasing order. It does not classify every geometric order or
placement. In particular neither root is claimed to be R*(8).

## 2. Exhaustive finite experiment and stopping rule

The predeclared domain was m=2..8, ascending, stopping only after all
permutations at the first counterexample size had been evaluated. No
symmetry reduction, pruning, candidate cap, seed or multiprocessing was
used. The search enumerated exactly 2!+3!+4!=32 permutations, then
stopped; **m=5,6,7,8 were not run**.

The first scorer used 80-decimal mpmath asin, 240 bisections per root on
[1/100,4m^2], checking both endpoint signs, and a 10^-60 comparison guard.
It retained every root bracket and every near tie. These computed brackets
are numerical observations, not outward-rounded intervals.

A separate scorer traversed an explicit alternating cycle and used

```text
theta_R(a,b)=2 atan2(sqrt(ab),sqrt(R(R+a+b)))
```

at 110 digits, 320 bisections on [1/128,1024], and independently recursive
enumeration. It reproduced every root inside its saved numerical bracket;
the largest midpoint discrepancy was 1.79291546936e-71. Its minimizer
comparison guard was 10^-90. Neither script imports production code,
verify.py, the other script, or a preceding task checker. Both score the
same exact criterion; this is not an independent re-proof of that theorem.

| m | Permutations / shifts | Minimizing P | Best shift P | Minimum rho_P, diagnostic | Best shift root, diagnostic |
|---|---|---|---|---|---|
| 2 | 2 / 2 | (3,4), (4,3) | both | 0.844453589560856 | 0.844453589560856 |
| 3 | 6 / 3 | (6,4,5) | (6,4,5) | 2.794919518896925 | 2.794919518896925 |
| 4 | 24 / 4 | (8,7,5,6) | (7,8,5,6) | 5.767794284589614 | 5.783560085857001 |

The root diagnostics discovered the witness. The rational checks below,
not these decimals or the comparison guards, establish (2), minimal m,
and the finite uniqueness assertions.

## 3. Rigorous fixed-radius separators and minimality

At the exact rational radius T=577/100, rigorous enclosures give:

| P | Enclosure of S_P(T)-2*pi (terminating decimals are exact rationals) |
|---|---|
| A=(8,7,5,6) | [-0.001419924193, -0.001419924192] |
| shift (5,6,7,8) | [0.051865656884, 0.051865656885] |
| shift (6,7,8,5) | [0.055147475169, 0.055147475170] |
| shift B=(7,8,5,6) | [0.009144588456, 0.009144588457] |
| shift (8,5,6,7) | [0.033418291688, 0.033418291689] |

Moreover **every other one of the 23 permutations** has
S_P(T)-2*pi >= 0.009144588456 > 0. By strict decrease,
rho_A<T<rho_P for each P!=A. Thus A is the unique minimizer among all
24, and beats every shift. This single-radius test proves root dominance;
comparing S_A and S_B without the intervening 2*pi would not suffice.

To identify B independently as the best shift, use U=723/125=5.784.
The enclosure for S_B(U)-2*pi is
[-0.000296197244,-0.000296197243], while every other shift has residual
at least 0.024416871879>0. Hence rho_B<U<rho_P for each other shift.

For m=3 use V=559/200=2.795. The enclosure for P=(6,4,5) is
[-0.000095230645,-0.000095230644]; each of the other five residuals is
at least 0.006338731857>0. Thus this shift is the unique root minimizer.
For m=2 both permutations are shifts; in addition, each cell has the same
unordered high pair before and after their swap, so their entire score
functions coincide, as in the local-swap theorem. There is consequently
no smaller counterexample anywhere in the stipulated domain m>=2.

The following additional rational endpoint sign checks certify short
root brackets, separately from the high-precision search:

| m, P | Strict lower bound | Strict upper bound |
|---|---|---|
| 2, (3,4) and (4,3) | 0.8444535895 | 0.8444535896 |
| 3, (6,4,5) | 2.7949195188 | 2.7949195190 |
| 4, A | 5.7677942845 | 5.7677942846 |
| 4, B | 5.7835600858 | 5.7835600859 |

Subtracting the last two strict brackets gives the gap bounds in (2).

## 4. Exact enclosure arithmetic and finite coverage

The retained `check_roots.py` uses Python integers and Fraction throughout
the sign certificate. For each rational R,a,b>0 put
q=ab/((R+a)(R+b)) in (0,1), D=10^40 and

```text
k=isqrt(floor(q D^2)),  l=k/D,  u=(k+1)/D;
l^2 <= q < u^2.
```

From the positive convergent arcsine series,

```text
asin(sqrt(q))=sqrt(q) sum_{j>=0} c_j q^j,
c_0=1,  c_{j+1}/c_j=(2j+1)^2/[2(j+1)(2j+3)] < 1,
T_N=sum_{j=0}^{N-1} c_j q^j,
2 l T_N <= theta_R(a,b) <= 2 u (T_N+q^N/(1-q)).          (3)
```

Here N=240. Every coefficient lies in (0,1], so the stated geometric
tail bound is valid without floating-point estimates. The checker asserts
that each resulting angular enclosure has width below 10^-30 on all
certificate inputs, including the m=2 root bracket. Sums, differences
and cell maxima use outward interval arithmetic: max([a,b],[c,d]) is
enclosed by [max(a,c),max(b,d)]. No branch decision is required for (3).

For 2*pi the checker uses the exact Machin identity

```text
2*pi=32 atan(1/5)-8 atan(1/239).
```

Indeed tan(4 atan(1/5))=120/119 and the tangent subtraction formula gives
tan(4 atan(1/5)-atan(1/239))=1; the angle is in (0,pi/2), fixing pi/4.
Each atan is enclosed by its 80-term alternating Taylor sum and that sum
plus its signed next term. This is a rigorous rational enclosure; no
stored decimal pi or mpmath value enters the exact comparisons.

Enumeration completeness is elementary: the independent recursion picks
each available first value once and recursively permutes the remaining
values. Induction gives each labeled permutation exactly once, m! in
total. The numerical audit also compares the complete order sets with
the independent enumeration, rejecting duplicates and omissions. The
certificate enumerates all six orders at m=3, all 24 at m=4, and all
four shifts separately; every enclosure and separator is retained in
`certificate.json`. The displayed bounds round outward to a 10^-12
rational grid. They are derived outputs; the rational algorithm and
reproducible sign checks are the evidence, not the artifact's status field.

## 5. Local-swap explanation at the actual shift root

Use `research/PERMUTED_HALVES_ADJACENT_SWAP.md` with B=(7,8,5,6), swapping
j=1 to obtain A. Its notation is

```text
u=6, x=7, y=8, v=5, l=1, r=3,
Delta(R)=S_A(R)-S_B(R)
        =F_1(6,8)-F_1(6,7)+F_3(7,5)-F_3(8,5).           (4)
```

Cells 2 and 4 are unchanged. On the entire band
[577/100,723/125] containing rho_B, exact branch tests give

```text
F_1(6,7)=theta_R(1,6)+theta_R(1,7),
F_1(6,8)=theta_R(6,8),
F_3(5,b)=theta_R(3,5)+theta_R(3,b), b=7,8.
```

To check the signs, set A_R=1/R, c=1/a, d=1/b and
e=1/t-A_R-c-d. If e<=0 the chain branch is strict; otherwise its sign
relative to the chord is sign(4(A_R c+A_R d+cd)-e^2). All are rational
tests with the pre-square gate retained. K_R(a,b) from the local note
decreases in R and b, so the checked rectangle corners certify the whole
R-band. The moving-high threshold for the left increment lies strictly
between 7 and 8; the right increment is chain throughout [7,8].

This is a **mixed/chain** exchange, not an all-chain exchange. Its exact
specialization of the clipped-threshold formula is

```text
Delta(R)=theta_R(6,8)-theta_R(1,6)-theta_R(1,7)
                          +theta_R(3,7)-theta_R(3,8).   (5)
```

For the rational bracket [L,H]=[5.7835600858,5.7835600859] of rho_B,
bound each positive angle in (5) above at L and below at H, and each
subtracted angle in the reverse direction. Monotonicity and (3) give

```text
-0.010134284215 <= Delta(rho_B) <= -0.010134284172 < 0.    (6)
```

This checks the local root-improvement implication at its required radius.
The mixed contribution cannot be assigned the universal chain-only sign;
the sufficient coordinate conditions in the earlier note do not apply
here because u>v while l<r. The direct rigorous evaluation resolves this
specific exchange without asserting any general rearrangement principle.

## 6. Authority and limitations

The root conjecture (1) is disproved, and m=4 minimality and the stated
finite minimizers are computer-certified finite results. The numerical
root table is independently reproduced finite numerical evidence; its
extra digits are not claimed as rigorous root intervals. A separate
110-digit construction at T checks 56 directed angular paths and all
28 Cartesian pairs for sigma_A, with a 10^-100 numerical guard; exact
feasibility follows from the imported fixed-order theorem and Section 3.

No claim is made for the optimum at m=5..8, an all-m minimizing structure,
the global optimum R*(2m), or contacts/floating circles. General permutation
asymptotics were not begun; no asymptotic coefficient, production code,
global finite certificate or arXiv-v1 wording changed. Independent human
proof review remains pending.

The single thematic owner is `knowledge/FIXED_ORDER_THEORY.md`.
Commands, exact outputs, failed local-branch attempt, source hashes,
artifact provenance and verification limits are in
`ops/TASK-20260905__permuted_halves_root_search/`.
