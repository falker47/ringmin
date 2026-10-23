# Upper Endpoint Dependency Closure

## Scope and Classification

`upper_supplement.tex` is a standalone analytic supplement titled
**Reflected Blocks, Implicit Parameters, and Full Geometric Recovery**.
It reorganizes existing exact theorems and proved corollaries. It proves
`limsup R*(n)/n^2 <= U4 = C4(1/20000)` and the strict fourth-block saving
`C3(Delta*) - U4 > 1/4608000000000000`.

All four baseline parameters retain their exact implicit definitions:

- `x*`: unique global minimizer of the complete-max `E` on `[0,1]`.
- `alpha_hat`: unique zero of `K'(alpha)+(1+alpha)E(x*)` on `[0,1/2]`.
- `epsilon_b`: unique mixed stationary minimum of the complete reflection
  cost starting at `lambda=(1+alpha_hat)x*`, on `[0,A/3-lambda]`.
- `Delta*`: unique mixed stationary minimum starting at `v=lambda+epsilon_b`,
  on `[0,A/3-v]`.

The displayed rational intervals isolate these values; no endpoint,
midpoint, decimal or fitted root replaces any of them. The common width
lemma consolidates the same analytic proof already present for the two
starts, with both applications' hypotheses checked explicitly. No new
research theorem or coefficient is claimed.

## Proof Map

The scientific source snapshot is
`3beb8d70c5b3748d370a92855847bdf574e5a14f`, the frozen snapshot referenced
by the public asymptotic manuscript. Repository baseline for this journal
packaging task is `75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae`.
All proof-source paths below are repository-root-relative provenance;
reading or executing them is not required to review the standalone proof.

| Supplement Section | Mathematical Obligation | Existing Source |
|---|---|---|
| 1 | Exact angular model and distinct chain/full/global quantities | `research/PERMUTED_ALTERNATING_HALVES.md`, Sections 1–2 |
| 2 | High-shell inequality, both arcs for every pair type, unique full root, closed feasible gaps, small cycles and cyclic seam | `research/PERMUTED_ALTERNATING_HALVES.md`, Sections 1–6 |
| 3 | Genuine even-rank involutions, complete seam inventory, arbitrary-test recovery, full-max error, root scale, both parities and countable slabs | `research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md`, Sections 1–5 |
| 4 | Exact E, clipped unsquared switch, middle derivative, tail concavity, unique global x* minimum | `research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md`, Sections 2–7 |
| 5 | Full K split, moving-wrap derivative, convexity, endpoint signs, exact alpha_hat and Taylor isolation | `research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md`, Sections 1–4 |
| 6 | Literal complete reflection integral, unique mixed switch, retained Q term in second derivative, entry/cutoff signs, unique width minima and distance from entry | `research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md`, Sections 1–4, 6; `research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md`, Sections 1–5 |
| 7 | Rational gates and their mathematical enclosure algorithms | The four implicit-parameter notes above, at their stated gate sections |
| 8 | Exact fourth-slab domain/marginals, strict closed-slab chord margins, cubic decrement with signed remainder, strict rational saving | `research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md`, Sections 1–6; general transfer, Section 5 |
| 9 | Reproduction scope | Checker implementations listed below |

The general transfer proof supplies the finite recovery that the historical
fourth-block and mixed-width notes deliberately deferred. The historical
notes' then-current scope statements are not carried forward as new
limitations on the combined theorem. The source's earlier shift optimizer
`alpha_*` is not needed for defining `x*` or `alpha_hat` here: the full
normalized E proof and the full K derivative are given directly.

## Included Checkers and Attribution

All five files are byte-for-byte copies of existing Ringmin checkers by
Maurizio Falconi, retaining their source documentation and implementations.
Only their filenames differ. They have no external input files, sibling
checker imports, production imports or repository discovery. A historical
path in a copied docstring is provenance, not a runtime dependency.

| Included File | Original Source | Used Proof Premises |
|---|---|---|
| `checks/upper_lambda.py` | `ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py` | Four Phi/E rational gates and arithmetic/sign safeguards |
| `checks/upper_alpha_minimum.py` | `ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py` | E(x0), Taylor e enclosure, two D/Fprime endpoint signs |
| `checks/upper_boundary.py` | `ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py` | Two second-width unsquared-sign equivalents with positive residuals |
| `checks/upper_mixed_width.py` | `ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py` | Inherited sharper epsilon bound, two third-width gates, cutoff and distance margins |
| `checks/upper_fourth_block.py` | `ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py` | Fourth closed-slab margins and independent 16-panel raw-cost upper enclosure |

The first two scripts additionally print historical comparisons involving
`alpha_*`, `C_30`, `C_107` or earlier coefficients. Those outputs are not
premises of this supplement; in particular their older assumed comparison
bounds are not represented as freshly reproved global theorems. The alpha
script's 120 recovery cases and fourth script's corner/moment probes are
bounded bookkeeping checks, not universal proofs. The rational checkers
are independent of production geometry; they do not certify a finite
Ringmin optimum or independently establish analytic uniqueness.

## Exact Commands and Local Results

Run from this directory with Python >=3.11, standard library only:

```text
python -I -S checks/upper_lambda.py --exact-only
python -I -S checks/upper_alpha_minimum.py --exact-only
python -I -S checks/upper_boundary.py
python -I -S checks/upper_mixed_width.py
python -I -S checks/upper_fourth_block.py
```

All five commands were run locally on 2026-10-23 under Python 3.14.3 and exited 0. The first
reproduced 2,835 point and 297 interval-box Fraction oracle checks and the
four required Phi/E gates. The second reproduced the complete six-row
outward interval table in Section 7.2 plus 120 bounded recovery cases.
The next two reproduced the literal signed fractions in Section 7.3 and
positive pre-square residuals. The fourth-block raw unnormalized cost
upper bound was exactly `-701561353/200000000000000000000000`, strictly
below `-1/288000000000000`; normalization with pi<4 gives the stated
saving. All five are bounded exact arithmetic checks. No optional mpmath
diagnostics, global finite verifier or optimization search was run for
this subtask. These are local results, not hosted CI or external acceptance.

Use assertions enabled: the first four scripts contain bare assertions.
Do not invoke these copies with `-O` or `-OO`; the parent package's runner
must reject optimized execution. The fifth uses explicit checks that
survive optimized execution, but is run under the same normal policy.

## Standalone Reading and Limits

The proof does not require any `ops` chronology, earlier proof note, code
module, generated result artifact, external image, or external TeX input.
The optional code and the finite gate derivations are included here. The
main article's global-limit theorem is needed only to replace the proved
limsup by its name `C*`. The supplement proves both parities directly.

No substantive mathematical dependency gap was found while assembling
this closure. Independent adversarial review and final all-page visual inspection are
separate gates owned by the journal-candidate task. After removing unused
mathtools/microtype dependencies and breaking three long formulas, the command
`python paper_assets/paper_ii_journal/build.py --document upper_supplement`
passed an isolated three-pass build: 13 pages, zero reference/box warnings,
PDF SHA-256 `bb6b2704151ced2464e76cf6272072d1185258ff2655b7baea5ed468285ba56b`.
No protected original was changed.

## Source Identity

The SHA-256 values below identify the inspected source bytes and unchanged checker copies. Git blob identities were also checked against the frozen scientific snapshot for all twelve sources. This proves provenance identity; it does not independently prove their mathematics.

| Source or Included Copy | SHA-256 |
|---|---|
| research/PERMUTED_ALTERNATING_HALVES.md | `f270ecbfb1cd093293ec1d61f9a08e47307bad0208c2ee9872be8bc506c2b448` |
| research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md | `906944d60dfdea24573e42d89050e25b1b04541897aac0ca6cbb3ba1b59936b9` |
| research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md | `4c7e0070a08108ebe54b70c93e0d3bd79b581936bb02f85c7608957630a0924e` |
| research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md | `578003adb187a8549d8f95c3279dc405c9e90f94a3a7090873f9aa9725e56da7` |
| research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md | `8800e3f720ff850052235136824882d416173bf436f4cff40e7d80c6c3642d23` |
| research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md | `45cd57a28c4e50de459d5933fbd217b8db39a7c558e36f6fc386b9c8427c2388` |
| research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md | `4d8bf80b684b1591d5f16ed8a894e59380427b4c88bebb33298c3b7edd74a956` |
| checks/upper_alpha_minimum.py | `16668fb3bafb4d8cf8186710c72e39365fc723b4ac99540d9a4e763d87ba63b4` |
| checks/upper_lambda.py | `e4172acd17d8a9d2658c72e0ce260496be428e0e750af48b5fc6dcf551bedacf` |
| checks/upper_boundary.py | `b57a90b4e1d826f739316f32b771dd17aae62d0fce35a2f6d599745ecd958bc2` |
| checks/upper_mixed_width.py | `bc16372c27be8ee82b8248b891b1474c2c29172b765c6cb54e587e43cac340b6` |
| checks/upper_fourth_block.py | `4b0f5d627fdcd800cb9402ea53de362962234a888faefd72b7f8d8be7b008935` |
