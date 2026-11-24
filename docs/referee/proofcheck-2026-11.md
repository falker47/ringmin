# Proof check of Paper I and of the L1–L8 chain of Paper II

**November 2026 · independent referee-style verification · internal document**

## Verdict

No ERROR and no GAP was found in the statements examined. Every proof in
scope was reconstructed before reading the author's argument and then
compared with it step by step; every step that a machine can check was
checked with new code. The findings are four imprecisions and five remarks
on style. The check itself changed no manuscript text. The author then
approved the wording for the four imprecisions, which was applied in
separate commits; see [Follow-up](#follow-up-wording-applied).

| Class | Paper I | Paper II (S1, L1–L8) |
|---|---|---|
| ERROR (false statement or irreparable proof) | 0 | 0 |
| GAP (incomplete but repairable proof) | 0 | 0 |
| IMPRECISION | 3 | 1 |
| STYLE | 3 | 2 |

## Scope and sources

| Paper | Source | Branch head examined |
|---|---|---|
| I, *Exact global bounds for minimum central circles with prescribed integer radii* | `paper_assets/journal_p1_jogo/main.tex` | `review/p1-square-radii` at `91ce1cbf42543b6bcaea8ac94688c34d29066087` (Draft PR #21) |
| II, supplement S1 | `paper_assets/journal_p2_sidma/supplement.tex` | `review/p2-square-radius-project` at `51dfc1b8c9ba02faa665cb20f60ce2d87f761c00` (Draft PR #22) |

Paper I: Sections 2–6, Theorem 7.1 as far as it follows from them, and
Appendices A–C. Paper II: Sections SM1–SM11 of S1, which are the lemmas
L1–L8 and the limit-existence argument. Numbering follows the compiled PDFs.

Outside the scope, and not verified here: the certificate files and their
verifiers, the upper witnesses for `n >= 8`, the square-radius brackets of
Paper I (Table 5), the square-radius lower bound of S1 (Section SM13), the
upper bounds of Paper II, and every bibliographic source.

## How to read the evidence column

* **H** — verified by hand: I rebuilt the proof from the statement, then
  compared it with the manuscript line by line.
* **M** — verified by machine. The identifier names a check in
  [`independent_check/fable_proofcheck`](../../independent_check/fable_proofcheck/README.md).
  Its label says what decides it: *exact* (integers and rationals),
  *interval* (Arb balls, certain comparisons only) or *symbolic* (sympy).
* **N** — not verified in this review.

A machine check of finitely many cases supports a statement about all `n`;
it does not prove it. Where a universal statement is marked verified, the
proof is the hand argument and the machine checks are corroboration and a
search for counterexamples. One command reproduces all machine checks:

```bash
python -I -B independent_check/fable_proofcheck
```

The Paper I checks (`P1-…`) are on branch `fable/proofcheck-p1`, the Paper II
checks (`P2-…`) on `fable/proofcheck-p2`.

## Paper I: statement, verdict, evidence

| Statement | Verdict | Evidence |
|---|---|---|
| Eq. (2), Lemma 2.1: both directed arcs; symmetry and monotonicity of the kernel | Verified | H. M: `P1-K1` (distance identities, exact), `P1-K2` (2,187 rational directions), `P1-K3` |
| §2: `C_sigma` strictly decreasing with limits `N pi` and `0`; unique chain radius; hierarchy (4); finiteness | Verified | H. M: every root bracket in `P1-E3` uses the strict decrease |
| Lemma 3.1 and Eq. (6): mixed partial derivative, strict anti-Monge inequality on and across the diagonal | Verified | H (derivative recomputed from the arctangent form). M: `P1-K4` (symbolic), `P1-K5` (3,136 quadruples) |
| §3: the rank rule defines a cycle through every rank once; examples `sigma*_4`, `sigma*_7` | Verified | H (parity count of low and high entries). M: `P1-S1` (`N <= 600`) |
| §3: Supnick's theorem makes `sigma*_N` a minimum-angle tour | Verified without the citation | H: cut-count proof below. M: `P1-S2` (equals the zigzag tour, `N <= 600`), `P1-S3` (attains every cut bound, `N <= 160`), `P1-S4` (all 23,116 tours, `N <= 9`, unique maximizer), `P1-S5` (60 random Monge matrices). The wording of the cited source: N |
| Theorem 3.2 (chain optimization) | Verified | H. M: `P1-S6` (45 cases with arbitrary rational radii, all tours), `P1-S7` |
| §4: difference constraints (7), negative-cycle criterion, monotone feasibility in `R`, forced gaps at the chain root | Verified | H. The complexity remark on Floyd–Warshall: N |
| Eq. (A.5): explicit edge lists in both parities; the neighbours of `k` are `n-1`, `n` | Verified | H. M: `P1-E1` (1,548 pairs `(k,n)`) |
| Lemma A.1 and (A.6): `R_{k,n+1} > R_{k,n}`, `R_{k,n} -> infinity` | Verified | H. M: `P1-E2` (edge matching, 1,188 steps), `P1-E3` (166 roots) |
| Lemma A.2: least triangle defect and its equality case | Verified | H. M: `P1-E4` (16,236 ordered triples, strict except the stated case) |
| Eq. (A.10): fan identity, bound `(m-1) delta_R`, equality discussion | Verified | H. M: `P1-E5` |
| Theorem 5.1(1) / Appendix A.4: feasible at the chain root iff `Delta_{k,n} >= 0`; then `R_full = R_{k,n}` | Verified | H. M: `P1-E6` (118 cycles, every nonadjacent pair, both arcs; the seam is the unique least slack) |
| (A.12)–(A.17): pocket identity, sign of `delta_R`, threshold `T_{k,n}`, its domain `n >= 4k+1` and its decrease | Verified | H. M: `P1-E8` (polynomial identities), `P1-E9`, `P1-E10` (`k <= 399`), `P1-E11` |
| Theorem 5.1(2): finite `s_k >= 4k+1`, persistence, at most one equality at `s_k - 1` | Verified | H. M: `P1-E11` (`k <= 5`) |
| (A.18)–(A.21), Tables 6–8: the six rational bridges | Verified | M exact: `P1-B1`–`P1-B5` (every printed rational recomputed from the source). M interval: `P1-B6` (the six inequalities directly). H for (A.20), (A.21) |
| Theorem 5.1(3), Table 1: onsets `8, 13, 17`, no integer equality | Verified | H (completion of ranges). M: `P1-E7` (signs for all `n <= 70`) |
| Corollary 5.2 | Verified | H. M: `P1-E12` (`L_n < R_{1,n} < U_n` for `n = 3..7`; chain root below `L_n` for `n = 8..14`) |
| §6.1, Eq. (9): induced-cycle inequality | Verified | H. Used by `P1-V5` |
| §6.2, Eq. (10): outward enclosures, circumference bounds `T_-`, `T_+` | Verified | H. M: `P1-A2` (printed `T_-`, `T_+` by the paper's own sign test), `P1-A3` (all 908 intervals) |
| Appendix B: integer recurrence, alternating remainder, cutoff 112 | Verified | H. M: `P1-A1` (induction invariants, exact), `P1-A4` |
| §6.3, Eqs. (11)–(13): class counts, skeleton–gap bijection, DP, exact pruning, partition identities | Verified | H. M: `P1-V1`, `P1-V2` (DP and pruned set against brute force) |
| §6.4: derivative bound, buffer `eps_n`, strict lower endpoint | Verified | H. M: `P1-K4`, `P1-V4`, `P1-V5` (every order excluded again at `L_n + eps_n`) |
| §6.5, Eq. (14): logic of the rational witnesses | Verified | H. The witnesses themselves: N |
| Theorem 7.1, lower side `L_n < R*(n)`, `n = 3..14`; Table 3 | Verified independently | M: `P1-V5`, a fresh exclusion from the printed endpoints alone; reproduces Table 3 exactly (246 and 18,660 retained skeletons; 268,648 explicit and 3,374,988,556 covered classes) |
| Theorem 7.1, upper side `R*(n) <= U_n` | Verified for `n <= 7`; N for `n = 8..14` | `n <= 7`: Corollary 5.2 with `P1-E12`. `n >= 8` rests on the certificate witnesses |
| §§6.2, 6.5, 10: reported totals 908, 47, 540, 3,004, 6,008 | Verified | M: `P1-V6` |
| Appendix C: lifting count `I_{n,k}`, partition, difference-constraint test, buffer `eps` | Verified | H. M: `P1-V3`, `P1-V4` |
| Table 5 (square radii) | N | Outside the scope |

### Supnick's maximum tour by cut counting

The paper imports the tour theorem. The following argument makes
Theorem 3.2 independent of the citation. Let `c` be a symmetric `N x N`
matrix whose second differences
`D[p][q] = c[p][q] + c[p+1][q+1] - c[p][q+1] - c[p+1][q]` are nonpositive
for `1 <= p, q <= N-1`. This is the Monge property; it involves the diagonal
entries. Then `c[i][j] = c[i][1] + c[1][j] - c[1][1] + sum_{p<i, q<j} D[p][q]`.
In a tour every vertex has degree two, so the first three terms contribute
the same constant to every tour. For `p <= q` let `X(p,q)` be the number of
tour edges joining `{1..p}` to `{q+1..N}`. Counting degrees in `{q+1..N}`,

```text
cost = const + sum_{p<q} D[p][q] (2(N-q) - X(p,q)) + sum_p D[p][p] (N-p - X(p,p)/2).
```

Since `D <= 0`, the cost is nondecreasing in every `X(p,q)`. Degrees give
`X(p,q) <= 2p` and `X(p,q) <= 2(N-q)`. For `p < q` the crossing edges lie on
fewer than `N` vertices, so they form a forest and `X(p,q) <= p + N - q - 1`.

By (A.5) every edge `{i,j}` of `sigma*_N` has `i + j` in `{N, N+1, N+2}`,
and `{p, N-p}` is an edge for every `1 <= p < N/2`. If `p + q < N`, both
neighbours of each `i <= p` are at least `N - p > q`, so `X = 2p`. If
`p + q > N`, both neighbours of each `j > q` are at most `N + 1 - q <= p`,
so `X = 2(N-q)`. If `p + q = N` and `p < q`, the only neighbour not above
`q` is `q = N - p`, reached once from `p`, so `X = 2p - 1`. If
`p = q = N/2`, the central edge replaces the impossible neighbour, and
`X = N`. Every bound is attained at once. Hence `sigma*_N` has maximum cost
for every symmetric Monge matrix, and minimum angle sum for `c = -theta_R`.

`P1-S3` confirms the attained bounds for `N <= 160` and `P1-S5` the cost
formula exactly. `P1-S4` confirms the bounds over all tours for `N <= 9`
and shows that no other tour attains all of them.

## Paper II, supplement S1: statement, verdict, evidence

| Statement | Verdict | Evidence |
|---|---|---|
| L1. Eq. (SM2.1), Lemma SM2.1 (root sandwich) | Verified | H. M: `P2-L1a`, `P2-L1b` (126 cycles, both sides strict) |
| L1. Lemma SM2.2 (deletion from full geometry) | Verified | H. M: `P2-L1c` (60 fully feasible configurations) |
| L2. Lemma SM3.1: `tau` unique, `3/17 < q < 1/5 < beta_1`, `J = pi C_term`, unique maximum at `r = q` | Verified | H (substitution redone). M: `P2-L2a` (printed 40-digit gates, exact; Machin branch), `P2-L2b` (rigorous quadrature and closed form), `P2-L2c` |
| L3. Grid gate (SM4.1); Lemma SM4.1 (assignment dual); `e >= 0`, `E <= 8e` | Verified | H (integral form of `H` recomputed). M: `P2-L3a` (3,750 grid pairs), `P2-L3b` (40 genuine orders) |
| L3. Measure (SM4.4), marginals and energy (SM4.5) | Verified | H. M: `P2-L3b` (exact) |
| L4. Lemma SM5.1 (midpoint strip mass) | Verified | H. M: `P2-L4a` (exact; the constant 4 is attained at `h = 1/(2n)`) |
| L4. Lemma SM5.2: `Lambda = 2 int P (x-z) d mu`, `|Delta - Lambda| <= 43E` | Verified | H (isolated deletions `3E`; runs `10 M_LL / n <= 40E`). M: `P2-L4b` (Hessian, constants), `P2-L4c` (244 cases; largest ratio to the bound 0.003) |
| L4. Lemma SM5.3: `|Lambda| <= 11E + 2K`, `|W_beta - W_0 - D_n| <= 54E + 2K` | Verified | H. M: `P2-L4b`, `P2-L4c` (largest ratios 0.096 and 0.031) |
| L4. Lemma SM5.4 (floor estimates `5/n`, `19/(2n)`) | Verified | H. M: `P2-L4d` (258 sizes up to `n = 50001`; observed constants 0.44 and 0.15) |
| L5. Lemma SM6.1 (shared crossing budget) | Verified | H. M: `P2-L5` (400 exact instances, including couplings off the grid) |
| L6. Proposition SM7.1: `R*(n) >= M_{n,4}` and (SM7.3) | Verified | H (weighted mean with weights `h_i / L` rederived). M: `P2-L6a` (scalar minimax, exact), `P2-L6b` (8 orders at `n = 222, 301, 1107`, down to the chain roots) |
| L7. §SM8: `N`, `G`, `G' = N''L`, unique `z_*`; Lemma SM8.1 (cubic certificate, global maximizer) | Verified | H. M: `P2-L7a` (polynomial identities, exact), `P2-L7b`, `P2-L7c` (1,339 points of the polyhedron) |
| L7. §SM9: series enclosures of `D_i`, signs of `G`, multipliers, enclosure (SM1.4) | Verified | M: `P2-L7b`. `D_i` by an arcsine primitive and by rigorous quadrature; the paper's series formulas transcribed and found to enclose the same values; `C_term + eta_width = 0.14056946887766098063324…` |
| L8. §SM10: ordered limits with `h = t u`, threshold `N(t)` | Verified | H. M: `P2-L8` (32,000 sizes, exact; failure at `n = 50000j+1` for `t = 1`) |
| §SM11: line comparison (SM11.2), squeeze (SM11.3), Lemma SM11.1 | Verified | H. M: `P2-L8b` (`b_2..b_7` by enumeration; concatenation bound; squeeze against `R*(n)`, `n <= 7`) |
| Theorem SM1.1 and Proposition 7.1 of the article | Verified | Assembled from the rows above. `P2-L7b` checks that the article and S1 print the same two endpoints and that `0.1405694688` rounds the lower one down |
| §SM13 (square radii) | N | Outside the scope |

Two tests could have falsified the lower bound and did not. `P2-L8b`
compares `(b_n + 1)/n`, whose infimum is `pi C_*`, with
`pi (C_term + eta_width) = 0.44161…`: the exact values for `n <= 7` and
heuristic spans up to `n = 150` all exceed it (least value 0.46424).
`P2-L6b` evaluates the inequality of Proposition SM7.1 on genuine orders.

## Findings

Line numbers refer to the heads examined, before the follow-up commits.

### ERROR

None.

### GAP

None.

### IMPRECISION

1. **Paper I, §5, `main.tex` lines 282–283.** “A fan decomposition bounds
   every triangle defect below by `delta_R`.” The roles are reversed.
   Lemma A.2 bounds each triangle defect, by monotonicity from the positive
   mixed derivative. The fan identity (A.10) then writes a path slack as a
   sum of `m-1` triangle defects. Suggested wording: “Lemma A.2 bounds every
   triangle defect below by `delta_R`, and a fan decomposition writes each
   path slack as a sum of such defects.”
2. **Paper I, Theorem 3.2, lines 208–223.** The theorem concerns arbitrary
   distinct radii but does not state `N >= 3`. Its proof invokes (4), which
   is displayed “in the linear family” with `R*(n)`. The general statement
   is the sentence before (4), so the argument is complete. Stating `N >= 3`
   and the hierarchy for an arbitrary list would match the theorem.
3. **Paper I, §3, lines 202–206.** Supnick's theorem is cited through “the
   maximum-tour discussion” of the survey, without a theorem number. Its
   hypothesis includes Monge inequalities that involve diagonal entries.
   Lemma 3.1 supplies them through the analytic diagonal values, but the
   text does not say that this is the matrix to which the theorem is
   applied. The cut-count argument above could replace the citation in a
   short appendix.
4. **Paper II, S1, Lemma SM5.1, `supplement.tex` lines 288–292.** “No grid
   point is within `1/(2n)` of `B`.” The two nearest grid points are at
   distance exactly `1/(2n)`; none is strictly closer. The proof needs only
   the strict statement, and the bound `4h` is attained at `h = 1/(2n)`
   (`P2-L4a`). Suggested wording: “No grid point is at distance less than
   `1/(2n)` from `B`.”

### STYLE

1. Paper I, line 147: `C_sigma` “decreases continuously from `N pi > 2 pi`
   to zero”. These are limits as `R -> 0+` and `R -> infinity`.
2. Paper I, lines 334–335: `0 < l <= u < 3S`. The strict test (10) forces
   `l < u`.
3. Paper I, Appendix A.6.2: (A.20) and (A.21) are applied to the rational
   upper bounds `q_e`. The step `arcsin z_e < arcsin q_e` is left implicit.
4. Paper II, S1, Lemma SM5.2, line 341: the bound `|D_alpha(x)| <= 2` is
   used before Lemma SM5.4 states it. It holds because
   `D_alpha(x) = (sqrt(s-x) - sqrt(x))^2 <= 1`.
5. Paper II, S1: the constants 43, 54, 5 and 19/2 are far from tight on
   every instance tested (ratios at most 0.1). This is an observation, with
   no consequence for the proof.

## Follow-up: wording applied

On 2026-11-24 the author approved the wording for the four imprecisions.
Each is a separate commit on the proof-check branch of its paper.

| Finding | Change | Branch |
|---|---|---|
| 1 | Paper I, §5: the lemma bounds the triangle defects, and the fan decomposition sums them along a path | `fable/proofcheck-p1` |
| 2 | Paper I, Theorem 3.2: `N >= 3` is stated, and the proof derives the lower bound from the general remark before (4) | `fable/proofcheck-p1` |
| 3 | Paper I, §3: the matrix is named, with its diagonal given by the kernel formula, and (5) is cited for its Monge property | `fable/proofcheck-p1` |
| 4 | Paper II, S1, proof of Lemma SM5.1: “at distance less than `1/(2n)`” | `fable/proofcheck-p2` |

Each commit also updates the regression test of its paper, which lists the
replacement explicitly, the file `MATH_DIFF.md`, and the rebuilt PDF. Paper I
still has 27 pages and S1 still has 15. The article PDF of Paper II is
byte-identical to the one examined.

Two things were deliberately left alone. The survey citation in finding 3
still has no theorem number, because no source was consulted. The frozen S1
source, `s1_support.zip` and the standalone Proposition 7 supplement keep the
original sentence of Lemma SM5.1; only the SIDMA draft is reworded, and its
comparison test applies that one replacement to the frozen text.

The five style remarks were not applied. After the commits, the Paper I
checks (`46 items, 0 failures`) and the Paper II checks
(`28 items, 0 failures`) pass unchanged.

## Not verified

* The text of every cited source, including the survey statement of
  Supnick's theorem. No external source was consulted.
* The certificate files, their verifiers and the upper witnesses. For
  `n >= 8` the inequality `R*(n) <= U_n` rests on them.
* The square-radius results of both papers.
* The complexity remarks (Floyd–Warshall, `O(n 2^n)` states).
* Hosted CI. No workflow was added or run for the new checks.

## Decisions taken without supervision

* The heads were taken from the remote at start. The local remote-tracking
  ref of the Paper II branch was stale (`8730b6f`) and was not used.
* The report is identical on both proof-check branches, so that the two
  lines merge without conflict. The runner, its shared helper and the test
  entry point are identical for the same reason.
* The checks depend on `python-flint==0.9.0`, already used by
  `independent_check/p2`, and on `sympy` for four symbolic identities.
* A new dependency was not added to `requirements.txt` and no CI workflow
  was changed.
