# An explicit convergence rate for quantile-sampled radius profiles

```text
status=PROVED in this note; one internal adversarial read, no external review
domain=nondecreasing Q:(0,1]->[0,M], M>0, integers n>=2
written_on=2026-11-24
target=Paper II (paper_assets/journal_p2_sidma, branch review/p2-square-radius-project @ 51dfc1b)
manuscripts=unchanged
```

Labels such as `lem:closing` are the LaTeX labels of the SIDMA draft at the
commit above. Nothing here revises a published or submitted claim.

## 1. Statements

For a finite list `a` of marks in `[0,M]`, `b(a)` is the least span of points
on a line with `|x_i - x_j| >= sqrt(a_i a_j)` for all `i != j`
(`def:line`). For a nondecreasing `Q:(0,1]->[0,M]` write

```text
b_n^Q = b(Q(1/n), Q(2/n), ..., Q(1)),      E = E(Q) = lim_m b_m^Q / m .
```

The limit exists and equals `inf_{n>=2} (b_n^Q + M)/n` (`lem:profile-copy`).
When `Q = Q_mu` is the quantile function of a law `mu` on `[0,M]`, this is
the constant `E(mu)` of the radius-profile limit theorem
(`thm:profile-law`).

**Theorem 1 (two-parameter bound; exact theorem).** Let `n >= 2`, let
`0 <= kappa <= rho` be integers, and put `k = 2^kappa`, `r = 2^rho`,

```text
T = ceil( ceil(n/k) / (r/k) ).
```

Then

```text
n E - M  <=  b_n^Q  <=  T r (E + M/k) + (T + (k-1) rho - 1) M.          (1.1)
```

Since `T r <= n + r - 1`, the right side of (1.1) is at most

```text
n E + (r-1) E + ( (n + r - 1)/k + (n - 1)/r + (k-1) rho ) M.            (1.2)
```

**Corollary 2 (rate; exact theorem for `n >= 2^11`, computer-certified
finite result for `2 <= n < 2^11`).** For every `n >= 2`,

```text
- M  <=  b_n^Q - n E  <=  (5/2) M sqrt(n log2 n).                       (1.3)
```

**Corollary 3 (ring radius; proved corollary).** Let `n >= 3`, `N_n > 0`,
and let `R_n` be the infimum central radius for the outer radii
`N_n Q(i/n)`, `1 <= i <= n`. Then

```text
- (1 + 1/pi) M/n  <=  R_n/(N_n n) - E/pi
                  <=  ((5/2) sqrt(n log2 n) + 1) M/(pi n).              (1.4)
```

**Corollary 4 (consecutive and power radii; proved corollary).** For every
real `p > 0` and every `n >= 3`, the infimum `R_p^*(n)` for the outer radii
`1^p, ..., n^p` satisfies, with `C_p = E(law(U^p))/pi`,

```text
- (1 + 1/pi) n^p  <=  R_p^*(n) - C_p n^(p+1)
                  <=  ((5/2) sqrt(n log2 n) + 1) n^p / pi.              (1.5)
```

The constants do not depend on `p`. For `p = 1` this reads

```text
- (1 + 1/pi) n  <=  R^*(n) - C_* n^2  <=  ((5/2) sqrt(n log2 n) + 1) n / pi,
```

so `R^*(n) = C_* n^2 + O(n^(3/2) sqrt(log n))`, with a linear error on the
lower side. For `p = 2` it gives
`R_2^*(n) = C_2 n^3 + O(n^(5/2) sqrt(log n))`.

**Corollary 5 (arbitrary arrays; three separated error terms; proved
corollary).** Let `a = (a_1,...,a_n)` be any marks in `[0,M]`, with sorted
values `a_(1) <= ... <= a_(n)`, let `mu` be any law on `[0,M]` and put

```text
W_n = (1/n) sum_i | sqrt(a_(i)) - sqrt(Q_mu(i/n)) | .
```

Then, for `n >= 2`,

```text
| b(a)/n - E(mu) |  <=  2 sqrt(M) W_n + (5/2) M sqrt(log2(n)/n).         (1.6)
```

If moreover `n >= 3`, `N_n > 0` and `R_n` is the infimum central radius for
the outer radii `N_n a_i`, then

```text
- 2 sqrt(M) W_n/pi - (1 + 1/pi) M/n
     <=  R_n/(N_n n) - E(mu)/pi
     <=  2 sqrt(M) W_n/pi + ((5/2) sqrt(n log2 n) + 1) M/(pi n).        (1.7)
```

In (1.7) the term `M/n` is the geometric error of `lem:profile-squeeze`,
`W_n` is the sampling error of the given array against the proposed law, and
the square-root term is the template error bounded by Corollary 2. No
convergence hypothesis is used: (1.6)-(1.7) are finite inequalities.

For `34 <= n < 2^11`, Corollaries 3-5 inherit the computer-checked range of
Corollary 2. For `n <= 33` the upper bound in (1.3) already follows from
`b_n^Q <= (n-1) M`.

## 2. Imported facts

The proof of Theorem 1 and Corollary 2 uses only the following statements of
the SIDMA draft.

- **(F1)** Deleting marks or decreasing marks cannot increase `b`
  (text after `eq:recurrence`). `b` does not depend on the order of the list.
- **(F2)** A gap of length `M` suffices to join two feasible line placements
  (`lem:closing`): every cross pair needs separation at most `M`.
- **(F3)** `lim_m b_m^Q/m = inf_{n>=2} (b_n^Q + M)/n` (`lem:profile-copy`).
- **(F4)** `b(a_n)/(pi n) - M/n <= R_n/(N_n n) <= (b(a_n) + M)/(pi n)` for
  `n >= 3` (`lem:profile-squeeze`).
- **(F5)** `|b(a) - b(c)| <= 2 sqrt(M) sum_i |sqrt(a_i) - sqrt(c_i)|` for two
  matched lists in `[0,M]` (`eq:profile-change`).

Corollaries 3-5 use (F4) and (F5), and Corollary 4 uses the identification
of `C_p` in `cor:profile-powers` (`thm:existence` for `p = 1`). Sections 5.2
and 5.3 also import the certified endpoints `prop:cert-upper` and
`prop:lower`, and the finite inequality `b_m^Q <= q (b_n^Q + M) - M` of
`lem:profile-copy`.

## 3. Proof of Theorem 1

The lower bound in (1.1) is (F3): `(b_n^Q + M)/n >= E`. The upper bound has
six steps. Fix `n, kappa, rho, k, r, T` as in the statement and put
`v_j = Q(j/k)` for `1 <= j <= k`. A *type* is an index `j`; two types stay
distinct even when their marks coincide.

### 3.1 Type lists

For an integer `q >= 1` let `U_q` be the list with `q` points of each type,
`k q` marks in all. Then

```text
b(U_q) <= b_{kq}^Q + q M.                                               (3.1)
```

*Proof.* Put `N = k q` and `Q(0) = 0`. Let `Lambda_q` contain `q` copies of
`Q((j-1)/k)` for `1 <= j <= k`. For `(j-1) q < i <= j q` we have
`(j-1)/k < i/N`, hence `Q((j-1)/k) <= Q(i/N)`: the sorted list `Lambda_q` is
termwise at most the sorted grid, and `b(Lambda_q) <= b_N^Q` by (F1).
`U_q` is `Lambda_q` with the `q` zero marks of type `j = 1` removed and `q`
copies of `v_k <= M` added. Take a minimal placement of `Lambda_q`, delete
those `q` zero marks, and append the `q` new points to the right at
successive spacing `M`, the first of them at distance `M` from the rightmost
retained point (if `k = 1` nothing is retained and the span is `(q-1) M`).
Every new pair is separated by at least `M`. The span grows by at most
`q M`.

### 3.2 Blocks and extents

Assume `(r/k) | q`, so that `r | kq`. Fix any feasible placement `P` of
`U_q` and list its points from left to right (ties in any order). A *block*
is a set of consecutive points in this list; its *extent* `ext(B)` is the
difference of its last and first coordinates, and its *count vector*
`c(B) in Z^k` records how many of its points have each type. Then:

- (i) the points of a block, at their coordinates in `P`, form a feasible
  placement of their own marks, of span `ext(B)`;
- (ii) if `B` is cut into a left part `B'` and a right part `B''`, then
  `ext(B') + ext(B'') <= ext(B)` and `c(B') + c(B'') = c(B)`;
- (iii) the `kq/r` *windows* (consecutive blocks of `r` points) have total
  extent at most `span(P)`, and their count vectors add up to `q (1,...,1)`.

For `0 <= l <= rho` let `F_l` be the family of dyadic sub-blocks of size
`r 2^-l` of the windows (`F_0` is the family of windows; each block of
`F_{l-1}` is the union of its two halves in `F_l`).

### 3.3 Lemma 3 (dyadic rounding)

*Let `d in Z^k` have nonnegative entries with `r | (d_1 + ... + d_k)`, and
let `g >= 0` be real weights on `F_0` with `sum_B g_B c(B) = d`. Then there
are nonnegative integers `m_B`, `B in F_0 u ... u F_rho`, such that*

```text
(a)  sum_B m_B c(B) = d;
(b)  sum_B m_B ext(B) <= sum_{B in F_0} g_B ext(B);
(c)  sum_{B in F_0} m_B <= (d_1+...+d_k)/r,
     sum_{B in F_l} m_B <= 2 (k-1)   for 1 <= l <= rho,   and
     sum_{all B} m_B <= (d_1+...+d_k)/r + (k-1) rho.
```

*Proof.* **Support reduction.** Let `h >= 0` be weights on some `F_l` with
`sum_B h_B c(B) = d'`. If the count vectors of the blocks in the support of
`h` are linearly dependent, choose `z != 0` supported there with
`sum_B z_B c(B) = 0`. Summing the `k` coordinates gives
`r 2^-l sum_B z_B = 0`, so `z` has entries of both signs. Replace `z` by
`-z` if necessary so that `sum_B z_B ext(B) <= 0`, and move from `h` to
`h + t z` with the largest `t > 0` that keeps all weights nonnegative. The
combination `d'` and the total weight are unchanged, the cost
`sum_B h_B ext(B)` does not increase, and the support loses a block.
Repeating, we may assume that the support has linearly independent count
vectors, hence at most `k` blocks.

**One level.** Suppose `d^(l) in Z^k` is nonnegative with total divisible by
`r 2^-l`, and `g^(l) >= 0` on `F_l` satisfies
`sum_B g^(l)_B c(B) = d^(l)`. Reduce the support of `g^(l)` to obtain `h`.
Put `m_B = floor(h_B)` for `B in F_l`, and let `f_B = h_B - m_B` be the
fractional parts. Summing coordinates, the total weight
`H_l = sum_B h_B = |d^(l)| / (r 2^-l)` is an integer, so
`Phi_l = sum_B f_B` is an integer; it is smaller than the size of the
support, hence

```text
Phi_l <= k - 1.                                                         (3.2)
```

The remainder `d^(l+1) = d^(l) - sum_B m_B c(B) = sum_B f_B c(B)` is a
nonnegative integer vector whose total `r 2^-l Phi_l` is divisible by
`r 2^-(l+1)`. If `l < rho`, give each half `B', B''` of a support block the
weight `f_B`; by (ii) this defines `g^(l+1)` on `F_{l+1}` with
`sum g^(l+1) c = d^(l+1)`, total weight `H_{l+1} = 2 Phi_l`, and

```text
sum_{B in F_l} m_B ext(B) + sum_{B in F_{l+1}} g^(l+1)_B ext(B)
      <= sum_{B in F_l} h_B ext(B) <= sum_{B in F_l} g^(l)_B ext(B).    (3.3)
```

**Last level.** At `l = rho` the blocks are single points and their count
vectors are unit vectors. Linear independence forces at most one support
block per type, so `h_B = d^(rho)_j` is an integer and `Phi_rho = 0`.

Start with `d^(0) = d`, `g^(0) = g` and iterate. Property (a) holds because
the final remainder is zero, and (b) follows by adding (3.3) over the
levels. Level `l` contributes `H_l - Phi_l` pieces, with `H_0 = |d|/r` and
`H_l = 2 Phi_{l-1} <= 2(k-1)` for `l >= 1`; this gives the first two lines
of (c). Adding over the levels, the sum telescopes:

```text
sum_l (H_l - Phi_l) = H_0 + (Phi_0 + ... + Phi_{rho-1}) - Phi_rho
                    <= |d|/r + (k-1) rho.
```

### 3.4 Assembly: the finite inequality

Apply Lemma 3 to `d = (T r/k)(1,...,1)`, an integer vector with total `T r`
because `k | r`, and to the constant weights `g_B = T r/(k q)` on the
windows; by (iii), `sum_B g_B c(B) = d` and
`sum_B g_B ext(B) <= (T r/(kq)) span(P)`. Lay out `m_B` translated copies
of each selected block from left to right, leaving a gap `M` between the
last point of one copy and the first point of the next. By (i) and (F2) this
is a feasible placement of the list `V_T` with `T r/k` points of each type.
There are at most `T + (k-1) rho` copies. Therefore, for every feasible
placement `P` of `U_q`,

```text
b(V_T) <= (T r/(k q)) span(P) + (T + (k-1) rho - 1) M.                  (3.4)
```

Inequality (3.4) is finite and checkable on explicit instances; see
Section 6.

### 3.5 The limit in q

Take `P` minimal in (3.4) and use (3.1):

```text
b(V_T) <= T r ( b_{kq}^Q/(k q) + M/k ) + (T + (k-1) rho - 1) M.
```

Let `q` tend to infinity along multiples of `r/k`. By (F3) the first
quotient tends to `E`, so

```text
b(V_T) <= T r (E + M/k) + (T + (k-1) rho - 1) M.                        (3.5)
```

### 3.6 Counting

For `1 <= i <= n` put `j(i) = ceil(i k/n)`. Then `i/n <= j(i)/k`, so
`Q(i/n) <= v_{j(i)}`, and each type `j` is used by
`floor(j n/k) - floor((j-1) n/k) <= ceil(n/k)` indices. By the choice of
`T`, `T r/k >= ceil(n/k)`. Thus the grid list `(Q(i/n))_i` is obtained from
`V_T` by deleting points and decreasing marks, and (F1) gives

```text
b_n^Q <= b(V_T).                                                        (3.6)
```

(3.5) and (3.6) prove (1.1). Finally `T` is the least integer with
`T (r/k) >= ceil(n/k)`, so `T r/k <= ceil(n/k) + r/k - 1` and
`n <= T r <= k ceil(n/k) + r - k <= n + r - 1`; substituting
`T r <= n + r - 1` and `T <= (n + r - 1)/r` in (1.1) gives (1.2).

## 4. Proof of Corollaries 2-5

**Corollary 2.** Divide by `M` and write `e = E/M`; `0 <= e <= 1` because
`0 <= b_n^Q <= (n-1) M`. Since `T r >= n`, the right side of (1.1) minus
`n E` is at most `M B(n,kappa,rho)` with

```text
B(n,kappa,rho) = T r (1 + 1/k) + T + (k-1) rho - 1 - n
              <  r + n/r + n/k + k rho + r/k                            (4.1)
```

by (1.2). Put `L = log2 n`.

*Large n.* Let `n >= 2^11`. Take `rho = ceil(L/2)`, so
`sqrt(n) <= r < 2 sqrt(n)` and `2 rho < L + 2`. Put
`c = sqrt(2n/(L+2))` and let `k = 2^kappa` be the power of two with
`c/sqrt(2) < k <= c sqrt(2)`; then `1 <= k < sqrt(n) <= r`, so
`kappa <= rho`. Now `r + n/r <= (5/2) sqrt(n)` because `x + n/x` increases
on `[sqrt(n), 2 sqrt(n)]`;
`n/k + k rho < n/k + k (L+2)/2 = sqrt(n(L+2)/2) (c/k + k/c)
<= (3/2) sqrt(n(L+2))`, since `t + 1/t <= 3/sqrt(2)` on
`[1/sqrt(2), sqrt(2)]`; and `r/k < 2 sqrt(L+2)`. Hence

```text
B / sqrt(n L) < (3/2) sqrt(1 + 2/L) + (5/2)/sqrt(L)
                + 2 sqrt(1 + 2/L) / 2^(L/2).
```

Each term decreases in `L`. At `L = 11` the sum is `2.4325`, and check R4
of `rate/rate_bound_verify.py` proves that it is below `5/2` with rational
bounds for the square roots. (At `L = 10` the same sum is `2.5022`, so this
argument needs the threshold.)

*Small n.* For `2 <= n <= 2^15`, check R3 of the same verifier evaluates
`min_{kappa <= rho} B(n,kappa,rho)` in exact integer arithmetic and confirms
`4 B^2 <= 25 n L'` with a rational `L' <= log2 n`. The two ranges overlap.

**Corollary 3.** Insert (1.3) in (F4):
`R_n/(N_n n) >= (nE - M)/(pi n) - M/n` and
`R_n/(N_n n) <= (nE + (5/2) M sqrt(n log2 n) + M)/(pi n)`.

**Corollary 4.** Take `Q(t) = t^p`, `M = 1`, `N_n = n^p` in Corollary 3
(`cor:profile-powers` identifies `C_p`), and multiply by `n^(p+1)`.

**Corollary 5.** `b` is symmetric, so (F5) applies to the sorted marks and
the grid `Q_mu(i/n)`. Then use (1.3) with `Q = Q_mu`, noting
`M/n <= (5/2) M sqrt(log2(n)/n)`; (1.7) follows from (F4).

## 5. Explicit values

### 5.1 Optimised two-parameter bound

`Delta_1(n) = min_{kappa<=rho} B(n,kappa,rho)` is the law-free excess in
units of `M`; the column `ratio` is a certified decimal upper bound for
`Delta_1(n)/sqrt(n log2 n)`. For the uniform law, `e <= E_UP` (Section 5.2)
gives a slightly smaller excess `Delta_U(n)`; the last column is a certified
decimal upper bound for `(Delta_U(n) + 1)/(pi n)`, which bounds
`R^*(n)/n^2 - C_*` from above. The triple `(k, r, T)` is the minimiser for
`Delta_1(n)`; `Delta_U(n)` can use a different pair. Source:
`rate/rate_bound_table.json`.

| `n` | `(k, r, T)` | `Delta_1(n)` | ratio `<=` | `R^*(n)/n^2 - C_* <=` |
|---:|:---|---:|---:|---:|
| `10^2` | `(8, 8, 13)` | 50 | 1.9403 | 0.155243991 |
| `10^3` | `(16, 16, 63)` | 193 | 1.9346 | 0.057495688 |
| `3200` | `(16, 128, 25)` | 329 | 1.7047 | 0.032825708 |
| `10^4` | `(32, 64, 157)` | 704 | 1.9318 | 0.021059302 |
| `10^5` | `(128, 256, 391)` | 2284 | 1.7723 | 0.007103124 |
| `10^6` | `(256, 1024, 977)` | 7882 | 1.7660 | 0.002429784 |
| `10^7` | `(1024, 2048, 4883)` | 26285 | 1.7239 | 0.000807393 |
| `10^8` | `(2048, 32768, 3052)` | 90524 | 1.7565 | 0.000274076 |
| `10^9` | `(8192, 65536, 15259)` | 282210 | 1.6324 | 0.000087379 |
| `10^10` | `(32768, 262144, 38147)` | 940296 | 1.6315 | 0.000029804 |
| `10^12` | `(262144, 1048576, 953675)` | 10728034 | 1.6993 | 0.000003288 |

On `2 <= n <= 2^15` the largest value of `Delta_1(n)^2/(n L')` is `5.3333`,
at `n = 3`. *Numerical observation:* on `4 <= n <= 2^16` the optimised ratio
is at most `2.163` (at `n = 13`), and in the table it lies between `1.63`
and `1.95`; only the constant `5/2` of Corollary 2 is proved for all `n`.

### 5.2 Imported constant

`E_UP = 0.4428345` satisfies `E_UP > pi_up * 0.140958576058`, where
`pi_up` is a Machin-series upper bound for `pi` (check R1) and
`C_* < 0.140958576058` is `prop:cert-upper` of the SIDMA draft. That
proposition is imported, not re-verified in this sprint. The law-free
columns do not use it.

### 5.3 Remark: an explicit all-n bracket from the existing certificates

This remark uses only imported results and no part of Theorem 1. Let
`C_L = 0.1405694688` and `C_U = 0.140958576058` be the certified endpoints
of the SIDMA draft (`prop:lower`, `prop:cert-upper`). For `n >= 3`, (F3) and
(F4) give `R^*(n) >= n (n pi C_* - 1)/pi - n`. For `n >= 3200`,
`lem:profile-copy` with the certified template of size `3200` gives
`b_n + 1 <= ceil(n/3200) (b_3200 + 1)` and
`(b_3200 + 1)/(3200 pi) < C_U`. Hence, for every `n >= 3200`,

```text
C_L n^2 - (1 + 1/pi) n  <  R^*(n)  <  C_U n (n + 3199).
```

The same argument with the square-radius template gives
`R_2^*(n) < 0.088581212993 n^2 (n + 3199)` for `n >= 3200`. Classification:
proved corollary of imported computer-certified bounds.

## 6. Evidence

All commands, outputs and timings are in [README.md](README.md).

- `rate/rounding_generate.py` builds explicit instances of Sections 3.2-3.4
  (18 parameter sets, power profiles `p = 1,2,3`, `k <= 32`, `r <= 64`, up
  to 1024 points) in exact rational arithmetic.
- `rate/rounding_verify.py` (standard library, no shared code) re-proves the
  finite inequality (3.4) for each instance from the certificate alone:
  feasibility of `P`, dyadic pieces, exact type counts, the per-level and
  total piece counts of Lemma 3(c), the extent budget of Lemma 3(b), and all
  pairs of the assembled placement. It also checks the counting step 3.6
  exhaustively for `k <= 64`, `r <= 256`, `n <= 600`.
- `rate/rate_bound_verify.py` (standard library) recomputes the table of
  Section 5.1, the finite part of Corollary 2, and the threshold constant.
- A separate agent refereed Sections 1-5 adversarially, with its own
  brute-force and randomised exact scripts (about 2,900 random instances of
  Lemma 3, brute-force spans for `n <= 11`). It found no error in the chain
  of Theorem 1 and its corollaries. Its two findings are incorporated: the
  telescoped count `(k-1) rho` in Lemma 3(c), which halved the rounding
  term, and the corrected sharpness statement of Section 7.

The instance checks test the proof on examples. They are not part of the
logical chain of Theorem 1, which is the argument of Section 3. The only
computer-assisted step of the stated results is the range
`2 <= n < 2^11` of Corollary 2.

## 7. What is not proved

- **Sharpness of the upper side.** The lower bound `-M` in (1.3) is
  attained for every `n` by a single atom (`Q = M`: `b_n = (n-1) M`,
  `E = M`). The difference `b_n^Q - nE` can be positive. For `Q = 0` on
  `(0,1/2)`, `Q = M/4` on `[1/2,1)` and `Q(1) = M` it equals `M/4` for every
  even `n`; for `Q = M/16` on `(0,1)` and `Q(1) = M` it equals `M/8` for
  every `n >= 2` (both checked by brute force for small `n`). A genuine
  two-atom law with a light top atom, `0.999 delta_{0.05} + 0.001 delta_1`,
  also gives a positive difference for moderate `n`. Whether
  `sup_n (b_n^Q - nE)` is finite for every `Q` is open, and the exponent
  `1/2` and the logarithm in (1.3) are properties of the method.
  *Numerical observation:* for the uniform law a floating-point brute force
  over all orders gives `b_n - nE < -0.17` for `2 <= n <= 10`, using the
  imported bound `E > pi * 0.1405694688`.
- **The constant.** `5/2` is not optimised; the values in Section 5.1 show
  what the two-parameter bound gives.
- **The coefficients.** The result does not move either endpoint of
  `0.1405694688 < C_* < 0.140958576058` or of the bracket for `C_2`.
- **Arbitrary arrays.** For marks that are not a quantile grid, the rate is
  governed by `W_n` in Corollary 5, which weak convergence alone does not
  control (the SIDMA draft's example `a_{n,i} = eps_n` still applies).
- **Small n.** The bound (1.3) exceeds the trivial `b_n^Q <= (n-1) M` for
  `n <= 33`, and the optimised bound of Section 5.1 does not beat it for
  several `n <= 21`. Nothing useful follows for the certified range
  `3 <= n <= 14`.
- **Optimisers.** Nothing is asserted about optimal orders, contact graphs
  or floating disks at finite `n`.
- **Review.** There has been no external review, and the imported facts
  (F1)-(F5) were used as stated in the draft.

*Heuristic remark (not a claim).* Any argument that selects pieces of one
large placement meets an obstruction of order `sqrt(n)`: for the sorted
placement, `J` contiguous pieces miss some threshold count by about `n/J`,
and each piece costs a join. A better exponent would need structural
information about near-optimal placements.

## 8. Suggested use in Paper II (not applied)

A LaTeX version of the statement and proof, written against the labels of
the SIDMA draft, is in
[rate_theorem_section.tex](rate_theorem_section.tex). It compiles inside
that draft when inserted after `sections/law.tex` (checked on a scratch
copy). It could follow `thm:profile-law`, and the paragraph "Three sources
of error" could then quote (1.7) instead of stating that the quantile-grid
step has no rate. The referee report
(`docs/referee/p2-sidma-referee-2026-11.md`, major issue 5 and decision 3)
asks for exactly this separation and for the scope of any finite-size rate.
