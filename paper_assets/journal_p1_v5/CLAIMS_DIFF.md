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
| Table 5, exact threshold comparisons | Appendix A, `tab:seam2` | Identical rational margins and conclusions. Finite exact arithmetic in the written proof. |
| Table 6, rational edge bounds | Appendix A, `tab:seam3` | Identical rational edge bounds. Finite exact arithmetic in the written proof. |
| Table 7, exact chain comparisons | Appendix A, `tab:seam4` | Identical six endpoint checks. Finite exact arithmetic in the written proof. |

| v4 equations | Draft labels in original order | Disposition |
| --- | --- | --- |
| (1)–(4) | `eq:mainclaim`, `eq:kernel`, `eq:arcs`, `eq:hierarchy` | Identical numbered environments. |
| (5)–(8) | `eq:antimonge`, `eq:mixed`, `eq:difference`, `eq:seam-main` | Identical numbered environments. |
| (9)–(11) | `eq:induced`, `eq:coscheck`, `eq:dp` | Identical numbered environments, including the DP base case. |
| (12)–(14) | `eq:prune`, `eq:coverage`, `eq:stereo` | Identical numbered environments. |
| (A.1)–(A.21) | `eq:seam1` through `eq:seam21`, one-to-one | All 21 manually tagged displays are in the byte-identical v4 appendix. |
| Appendix B | `app:arithmetic` | The outward integer recurrence, alternating-series remainder, scaled circumference endpoints and comparison rules are retained. |

The three copied TeX inputs are byte-identical to the verified arXiv archive in this worktree. The tests also bind their text after newline normalization for fresh Windows checkouts. Separate source digests bind the formal environments, equations, literal main-table bodies and the complete declaration block. The companion paper's lower bound is inherited from arXiv:2609.13630v3, Theorem `thm:existence` and Proposition `prop:lower`. Its displayed decimal rounds the rigorous lower endpoint downward. The new geometry and seam plots are illustrations. Their floating coordinates carry no additional certification claim.
