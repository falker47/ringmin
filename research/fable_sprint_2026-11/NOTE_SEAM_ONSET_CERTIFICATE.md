# The first seam failure for general k: independent certificate

```text
status=COMPUTER-CERTIFIED for 1 <= k <= 5000 (this note); all-k law imported
domain=canonical Supnick cycle on radii k,...,n at its chain root
written_on=2026-11-24
target=Paper I (paper_assets/journal_p1_jogo, branch review/p1-square-radii @ 91ce1cb)
manuscripts=unchanged
```

## 1. Triage finding

The JOGO draft states the first seam failures only for `k = 1, 2, 3`
(`n = 8, 13, 17`) and says that its proof gives no formula for `k >= 4`.
The repository already contains the complete law, as proof notes dated
2026-08-30 to 2026-09-04 that are not used by the draft:

```text
s_1 = 8,   s_k = 4k + 5  (2 <= k <= 5),   s_k = 4k + 6  (k >= 6).        (1.1)
```

Sources: `research/RADIUS1_SEAM_OBSTRUCTION.md` to
`research/RADIUS6_SEAM_ONSET.md` for `k <= 6`,
`research/SUPNICK_SEAM_SEQUENCES.md` (monotonicity of the two sequences, all
`k >= 6`), and `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` (an independent
analytic proof for `k >= 4325`). All carry `status=PROVED`; the owning
ledger entry is `knowledge/FIXED_ORDER_THEORY.md`, "Exact sequence
monotonicity and complete formal seam onsets". So the target "a law for
general `k`" is a porting task for Paper I, not an open problem. This sprint
did not re-read those proofs. It adds an independent machine check.

## 2. Statement

Notation of the JOGO draft, Sections 3 and 5: `sigma_{k,n}` is the canonical
Supnick cycle on `k,...,n`, `R_{k,n}` its chain root, and

```text
Delta_{k,n} = theta(n,k) + theta(k,n-1) - theta(n,n-1)   at R = R_{k,n},
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

**Proposition A (computer-certified finite result).** For every integer
`1 <= k <= 5000`, with `m_k = 8` for `k = 1`, `m_k = 4k+5` for
`2 <= k <= 5` and `m_k = 4k+6` for `k >= 6`,

```text
Delta_{k, m_k - 1} > 0 > Delta_{k, m_k}.                                (2.1)
```

For every `1 <= k <= 60` and every `k+2 <= n <= 4k+60`, `Delta_{k,n} > 0`
if `n < m_k` and `Delta_{k,n} < 0` if `n >= m_k`.

**Corollary B (proved corollary, conditional on `thm:seam`).** By part 2 of
the seam theorem of the JOGO draft (`thm:seam`, Appendix A), the deficit is
positive for `k+2 <= n < s_k` up to a possible zero at `s_k - 1`, and
negative for `n >= s_k`. With (2.1) this gives `s_k = m_k` for every
`1 <= k <= 5000`, with no equality case. By part 1 of the same theorem, the
canonical order on `k,...,n` is feasible at its chain root exactly for
`n < m_k`.

**Corollary C (second route to the all-k law; imported tail).** The note
`research/EVENTUAL_SUPNICK_SEAM_ONSET.md` proves `s_k = 4k+6` for
`k >= 4325`. Proposition A covers `k <= 5000`. Together with `thm:seam`
they give (1.1) for all `k >= 1` without using the monotonicity note. The
two routes overlap on `4325 <= k <= 5000`.

## 3. Certificate and verification

`seam/seam_certificate.json` holds 18,910 records
`(k, n, lo, hi, sign)`: the two onset records of every `k <= 5000` and the
full window `k+2 <= n <= 4k+60` for `k <= 60`. `lo < hi` are decimal
rationals proposed by a float64 generator (`seam/seam_generate.py`, numpy
and Brent's method). The generator is not trusted.

`seam/seam_verify.py` (python-flint 0.9.0, Arb balls at 128 bits) proves for
each record:

- **S1** the cycle rebuilt from the rank rule is a cyclic arrangement of
  `k,...,n`, the neighbours of `k` are `n-1` and `n`, and its edge set
  equals the printed list (A.5) of the draft's Appendix A;
- **S2** `C(lo) > 2 pi > C(hi)` for the angle sum `C` of the cycle, so the
  root of the strictly decreasing `C` lies in `(lo, hi)`;
- **S3** the ball for the deficit evaluated on the whole interval
  `[lo, hi]` has a strict sign.

It then extracts the unique sign change of each `k` and compares it with
`m_k`. The smallest certified `|Delta|` is `2.37e-9`, at
`(k, n) = (5000, 20006)`; the working radius of the balls is many orders
smaller.

`seam/seam_verify_stdlib.py` is a second verifier for the onset records of
`k <= 100`. It uses only `fractions.Fraction`: `cos(theta) = 1 - 2q` is
rational, each angle is enclosed by proving
`cos(l) > 1 - 2q > cos(u)` with Taylor partial sums, `pi` is enclosed by
Machin's formula, and the deficit on `[lo, hi]` is bounded through the
monotonicity of `theta_R` in `R`. It reads the cycle from the edge list
(A.5), not from the rank rule, so the two verifiers also differ in how they
read the definition.

`controls/tamper_controls.py` checks that both verifiers reject a flipped
sign, a shifted bracket, a bracket too wide to decide the sign, and a
missing record.

## 4. What is not shown

- Nothing beyond `k = 5000` is checked here. The all-`k` statement rests on
  the repository's proof notes, which this sprint did not review.
- Outside the windows, the sign of `Delta_{k,n}` for `n` away from the
  onset is taken from `thm:seam`, not recomputed.
- The result concerns one fixed cyclic order at its chain root. It says
  nothing about `R^*(n)`, about global optimal orders, or about floating
  disks; `s_k` is not the size at which a global optimum changes regime.
- The certificate depends on Arb for `k > 100`. The exact-rational
  cross-check covers `k <= 100` only.

## 5. Suggested use in Paper I (not applied)

The abstract and Theorem `thm:seam` could replace "the first failures for
`k = 1,2,3` occur at `n = 8,13,17`" by the full law (1.1), with the proof
taken from the existing notes and this certificate cited as an independent
check for `k <= 5000`. Table `tab:onsets` would gain the rows
`k = 4, 5` (`s_k = 21, 25`) and `k >= 6` (`s_k = 4k+6`). The sentence in
Appendix A, "The proof does not assert the absence of equality for every
`k >= 4`, nor give an explicit formula for their onsets", would then be
superseded.
