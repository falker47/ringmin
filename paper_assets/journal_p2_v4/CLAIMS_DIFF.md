# Paper II claim map

The comparison text is the official TeX source of arXiv:2609.13630v3,
SHA-256 `792473ac5b2f0b39bcf9bb3e0d0d576c70aa42bc55c941bc914e4eb8354e98e4`.
PR #10 supplied the journal presentation of the uniform case. Section and
statement numbers below refer to the integrated manuscript.

## Published statements

| v3 | Journal draft | Disposition |
|---|---|---|
| Definition 1 | Definition 1 (`def:line`) | Kept. Least span for all pair separations of marks in [0,1], including zeros. |
| Lemma 2 | Lemma 2 (`lem:closing`) | Kept. Cutting and adding the unit gap bound both arcs. |
| Lemma 3 | Lemma 3 (`lem:squeeze`) | Kept. Both bounds on the normalized ring radius hold for every n ≥ 3. |
| Theorem 4 | Theorem 4 (`thm:existence`) | Kept. The uniform line limit is the infimum over genuine finite templates and equals π times the leading ring coefficient. |
| Theorem 5 | Theorem 5 (`thm:lp`) | Kept. Same balanced-word program, joint limit and error terms for the uniform profile. |
| Theorem 6 | Remark 13 | Removed from the submission. The finite and countable reflected-block transfer proofs, recovery errors, parameter isolations and implicit four-block endpoint remain in v3 and S2. The finite line certificate supplies the journal upper endpoint. |
| Proposition 7 | Proposition 14 (`prop:lower`) | Moved after the profile and certificate sections. The cutoffs, maximization, strict directed enclosure, rejected coefficient and stronger rejected deficit estimate are preserved. S1 is the complete proof and retains its original numbering. |

| v3 equations | Journal draft | Disposition |
|---|---|---|
| (1)–(3) | (1)–(3), `eq:theta`, `eq:line`, `eq:recurrence` | Kept. Angular kernel, all-pairs line model, and fixed-word recurrence. |
| (4)–(6) | (4)–(6), `eq:squeeze`, `eq:limit`, `eq:copies` | Kept. Geometric comparison, uniform limit and copy estimate. |
| (7)–(9) | (7)–(9), `eq:types`, `eq:lp`, `eq:effective` | Kept. Uniform quantization, word balance and both error terms. |
| (10)–(11) | Historical reference in Remark 13 | Removed with the explicit block construction. These equations define its cost and the strict decrement for the implicit parameter choice. |

The regression test compares the six surviving original statement formulas,
all nine surviving numbered equations and the seven further displays in
their sections against digests from v3. It also checks the original
acknowledgment. [Published version](https://arxiv.org/abs/2609.13630v3) · [Journal base, PR #10](https://github.com/falker47/ringmin/pull/10)

## Added results and their sources

| Journal location | Classification and scope | Source |
|---|---|---|
| Lemmas 6–7 | Exact geometric squeeze for uniformly bounded nonnegative marks and arbitrary positive scales. For a nondecreasing quantile template, replication and sorted reassignment give the finite-template infimum. | [PR #8, proof §§1–2](../../research/PROFILE_GENERALIZATION.md#2-replication-with-genuine-labels) |
| Theorem 8 and (11) | Exact limit under weak convergence of the empirical laws. The square-root matching estimate gives stability. Bounded Riemann-integrable grid profiles supply one class of examples. | [PR #8, proof §3](../../research/PROFILE_GENERALIZATION.md#3-distributional-stability) |
| Theorem 9 | Exact finite-word bracket for the ring coefficient, of width M(1/k+1/r)/π before evaluation of the quantile costs. Indexed types allow equal marks. | [PR #8, proof §4](../../research/PROFILE_GENERALIZATION.md#4-finite-words-for-any-limit-law) |
| Corollaries 10–11 | Proved reverse-quantile adjacent-pair lower bound and power-profile limit for every fixed real p > 0. Square radii give cubic growth and the lower bound 1/(6π). | [PR #8, proof §5](../../research/PROFILE_GENERALIZATION.md#5-power-radii-and-an-adjacent-pair-lower-bound) |
| Proposition 12 | Strict upper bounds on the two limiting coefficients. Exact finite line witnesses combine with Theorem 4 for the linear profile and Lemma 7 and Corollary 11 for the quadratic profile. | [PR #6, certificates and verifier](../line_upper/) · [PR #8, profile proof](../../research/PROFILE_GENERALIZATION.md) |
| Remark 13 | Certified cost enclosure for the four specified rational slab parameters and shift. The implicit v3 endpoint has different parameters. | [PR #6, cost evaluation](../line_upper/NOTE.md#two-evaluations-of-the-four-block-cost) |

The abstract's lower decimal rounds down Proposition 14. The two upper
decimals are strict ceilings from Proposition 12. The finite-bracket plot
uses the twelve Paper I intervals already present in PR #10. Pages, labels
and figure numbering belong to this version. [PR #6](https://github.com/falker47/ringmin/pull/6) · [PR #8](https://github.com/falker47/ringmin/pull/8)
