# v4-to-draft claim mapping

The baseline is the published source of arXiv:2607.28654v4. The journal draft preserves all six formal theorem-family environments, all fourteen numbered main equations and their labels, and all seven original tables. The new figures have a separate counter. The main theorem numbers and the appendix's manual equation tags retain their published numbers.

| v4 | Draft location | Disposition and epistemic class |
| --- | --- | --- |
| Lemma 2.1, both directed arcs | §2, `lem:angular` | Verbatim statement. Exact theorem on the necessary and sufficient separation of a single pair. |
| Lemma 3.1, anti-Monge inequality | §3, unlabelled lemma preceding (6) | Verbatim statement. Exact theorem for every positive central radius. |
| Theorem 3.2, chain optimization | §3, `thm:chain` | Verbatim statement, including arbitrary distinct positive radii and the all-pairs hypothesis for attaining the lower bound. Exact theorem. |
| Theorem 5.1, seam criterion and persistence | §5, `thm:seam` | Verbatim statement, including the possible equality at the final feasible index for general fixed k. Exact theorem. |
| Corollary 5.2 | §5, `cor:small` | Verbatim statement. Proved corollary for the displayed necklace through 7 and its chain-root failure from 8. |
| Theorem 7.1, finite global brackets | §7, `thm:brackets` | Verbatim statement. Computer-certified finite result for 3 through 14. |
| Appendix A, three-part restatement | §A.1, same `seam_appendix.tex` | Identical proof input, including the strict onsets for k = 1, 2, 3 and the complete parity argument. Exact theorem. |
| Table 1, onsets | §5, `tab:onsets` | Values identical. Shortened caption ties each sign to the fixed chain root. Exact theorem. |
| Table 2, endpoints | §7, `tab:brackets` | Same `bracket_rows.tex` and all 12 rows. The caption retains the open lower and closed upper endpoint and counts of upper witnesses. Computer-certified finite result. |
| Table 3, coverage | §7, `tab:coverage` | Same `coverage_rows.tex`, class counts and zero-explicit cases. Computer-certified finite result. |
| Table 4, floating regimes | §8, `tab:regimes` | Original table and caption. Row 1 describes the exhibited optimum. Rows 2–5 are numerical observations about historical reconstructions. |
| Table 5, exact threshold comparisons | Appendix A, Table 6, `tab:seam2` | Identical rational margins and conclusions. Finite exact arithmetic in the written proof. |
| Table 6, rational edge bounds | Appendix A, Table 7, `tab:seam3` | Identical rational edge bounds. Finite exact arithmetic in the written proof. |
| Table 7, exact chain comparisons | Appendix A, Table 8, `tab:seam4` | Identical six endpoint checks. Finite exact arithmetic in the written proof. |

| v4 equations | Draft labels in original order | Disposition |
| --- | --- | --- |
| (1)–(4) | `eq:mainclaim`, `eq:kernel`, `eq:arcs`, `eq:hierarchy` | Identical numbered environments. |
| (5)–(8) | `eq:antimonge`, `eq:mixed`, `eq:difference`, `eq:seam-main` | Identical numbered environments. |
| (9)–(11) | `eq:induced`, `eq:coscheck`, `eq:dp` | Identical numbered environments, including the DP base case. |
| (12)–(14) | `eq:prune`, `eq:coverage`, `eq:stereo` | Identical numbered environments. |
| (A.1)–(A.21) | `eq:seam1` through `eq:seam21`, one-to-one | All 21 manually tagged displays are in the byte-identical v4 appendix. |
| Appendix B | `app:arithmetic` | The outward integer recurrence, alternating-series remainder, scaled circumference endpoints and comparison rules are retained. |

PR #7 recorded byte equality with the v4 archive for the linear bracket rows, coverage rows and seam appendix. The tests bind their text after newline normalization for Windows checkouts. Separate source digests bind the formal environments, equations, literal main-table bodies and complete declaration block. The companion paper's lower bound is inherited from arXiv:2609.13630v3, Theorem `thm:existence` and Proposition `prop:lower`. Its displayed decimal rounds the rigorous lower endpoint downward. The geometry and seam plots are numerical illustrations.

## Additions since v4

The source for the new finite results is [PR #9 at d93fca9](https://github.com/falker47/ringmin/tree/d93fca92714fc9e59e69ed036fab734c9c5edb2d/paper_assets/general_radii).

| Draft location | Claim and classification | Source |
| --- | --- | --- |
| Abstract, §§1 and 6 | The exact certificate method accepts finite lists of at least three distinct positive integer radii. The anti-Monge and chain theorems retain their positive-real domain, and the seam theorem retains its consecutive-integer domain. | [PR #9 method](../general_radii/METHOD_NOTE.md), v4 Theorems 3.2 and 5.1 |
| §6 | Independently reproduced finite result. The general implementation checks the twelve original linear endpoint pairs using recomputed lower partitions and fresh rational placements. It takes the published endpoints and one candidate order per size as inputs. | [PR #9 results](../general_radii/RESULTS.md) and the original [linear certificate](../../reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json) |
| §9, Table 5 | Computer-certified finite result. For square radii and each size from 3 to 14, the open lower and closed upper endpoints differ by exactly 10⁻¹¹. Each row has one rational upper witness. | [PR #9 table](../general_radii/quadratic_brackets.tex) and [certificate files](../general_radii/certificates/) |
| Appendix C | Exact coverage argument. Deleting the smallest d radii leaves at least three labels. The insertion bijection and the strict DP comparison partition all cyclic classes. The derivative estimate gives a positive rational strictness buffer after a successful lower audit. | [PR #9 proof](../general_radii/METHOD_NOTE.md) and [standalone verifier](../general_radii/verify_radii_certificate.py) |
| §1 and Figure 5 | Results attributed to revised Paper II. The linear asymptotic constant lies strictly between 0.1405694688 and 0.140958576058. For square radii the normalized limit exists and is strictly below 0.088581212993. Figure 5 plots finite certificate intervals and marks these asymptotic bounds. | [Companion preprint](https://arxiv.org/abs/2609.13630) and [revision sources and submission dependency](CHANGES.md) |
