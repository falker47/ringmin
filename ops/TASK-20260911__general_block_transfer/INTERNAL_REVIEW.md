# Internal adversarial review: fourth block and general transfer

    classification=internal mathematical validation; bounded independent arithmetic checks
    reviewer=fresh reviewer subagent in the same authorized research goal
    external_acceptance=not performed or implied
    reviewed_on=2026-09-11
    starting_head=372f96c0a9f14d968e7ecb3b1a039e7867340005
    environment=Windows; CPython 3.14.3; stdlib only

This review was performed separately from the parent agent's construction of
the general-transfer proof. The reviewer first read the fourth-block proof
and its canonical definitions, then audited the general-transfer draft
read-only while the parent worked on its checker. The reviewer subsequently
persisted the independent finite audit as `check_general_blocks.py` in this
dossier. This is internal validation, not an independent external acceptance
review and not a modification of external Review State.

## 1. Fourth-block continuous audit

**Outcome: INTERNALLY VALIDATED, with imported dependencies identified.**
No error was found in
[`PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md`](../../research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md)
or its bounded checker at the starting HEAD.

The reviewer independently reconstructed the following from the measure
and literal complete maximum, rather than treating checker success as proof:

- Separate reflected slabs preserve each high marginal individually.
  Symmetrization preserves equality of the two low/high marginals. Their
  common two-coordinate marginal is not asserted unchanged. The third/fourth
  seam and high boundary have zero mass.
- The original blocks cancel with their full costs. The inherited rational
  margins imply strict chord dominance on the entire closed witness slab,
  including its endpoints; third-width stationarity is not used for this
  cancellation.
- The later branch description is correct: the ratio increases strictly in
  the cell coordinate, its midpoint remains chord, and the increasing
  endpoint ratio has exactly one root between the witness and cutoff.
- Centering and rationalization give the asserted integral and elementary
  antiderivative. The denominator bounds give the negative cubic coefficient,
  nonnegative remainder with the stated upper bound, and strict rational
  saving. The first nonzero variation is cubic, not linear.
- An independent expansion of the original expression, using `s=eta*t`,
  gives integrated coefficients `0, -1/24, 1/48` and therefore
  `F=-eta^3/(24*B)+eta^4/(48*B^2)+O(eta^5)`.
- The raw-max checker's directed square roots and concave midpoint enclosure
  have the correct direction. Its worst-B corner is justified by integrated
  pointwise monotonicity. It does not evaluate the proof's antiderivative or
  rationalized integrand. Corner/moment probes are diagnostics, not a
  substitute for the arbitrary-test or interval proof.

The exact minimizers' earlier existence/uniqueness proofs were imported,
not all independently re-audited here. The mixed-width proof's rational
localization and the relevant source definitions were read, and its bounded
checker was independently run. This continuous audit alone supplies neither
finite recovery nor a new global upper coefficient.

## 2. General finite and countable transfer audit

**Outcome: INTERNALLY VALIDATED.** No error was found in the reviewed draft
of [`PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md`](../../research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md).

The reviewer verified:

- Genuine permutations for arbitrary finite `k`, unordered nonnegative
  lengths, zero middle lengths, length-two identities, fixed even ranks,
  both parities and floor ties. Rounded starts are sums of rounded lengths.
- Exhaustive, disjoint classification of every cell: interiors, shared
  boundaries, initial cyclic predecessor, final exit, both high-wrap cells
  and ordinary tail. Zero blocks do not create missing or duplicate cells.
- Double-panel orientation and coordinate errors. The finite assignments
  give `omega_F(4/m)+2*(k+3)*B_F/m`; rounded endpoints and wrap give the
  coefficient `2*k^2+4*k+8` in the final recovery estimate.
- The literal maximum is globally 4-Lipschitz; its chain branch is inactive
  below `t=1/4`. The resulting coefficient is `6*k^2+28*k+36`.
- The imported arbitrary-high full-cell theorem was re-derived from its
  angular model and high-shell inequality. The proof covers each pair type
  and both directed paths, including `m=2` and arbitrary high permutations.
- Angular approximation, the prior root-scale squeeze, and substitution of
  the actual root are valid. The final coefficient is
  `6*k^2+28*k+1060`, giving `1268` at `k=4`.
- Deleting only the largest high gives the odd global upper bound without
  requiring equality with an odd fixed-order limiting minimum.
- Countable truncation changes a continuous test moment by at most twice
  its sup norm times the omitted length. The diagonal recovery sequence
  and root transfer are valid when the total length is strictly below
  `1-alpha`. No characterization of arbitrary marginal couplings follows.

The four-block corollary still imports the earlier exact parameter
definitions and localization. This review does not solve partition
optimization, the global asymptotic constant, or any finite optimum.

## 3. Persisted independent general-block checker

[`check_general_blocks.py`](check_general_blocks.py) builds integer
permutations by reversing explicit even-rank lists. It then compares all
cells with the independently written symbolic inventory and checks both
endpoints of every nonexceptional affine panel. This separates the builder
from the cell formulas being tested.

The original bounded domain is exhaustive: `2<=m<=24`, every `0<=s<m`,
`1<=k<=4`, each integer length in `{0,2,4,6}`, retaining exactly the cases
with `m-s-sum(lengths)>=2`. It has 30,034 orders and 580,560 cells.

Large-size diagnostics use three strict interior rational surrogates of
each inherited coarse bracket, at weights `1/4,1/2,3/4`. The first length
is `(1+alpha)*x`; the others are the rational epsilon and Delta surrogates,
and exactly `eta=1/20000`. Sizes are
`39999,40000,40001,79999,80000,80001`, so the rounded fourth length is
respectively `0,2,2,2,4,4`. The second triplet checks the first nonidentity
fourth reflection, as length two is an identity.

**These are rational-surrogate diagnostics, not computations of the
floors of the implicitly defined exact minimizers.** They add 18 genuine
orders and 1,080,000 cells. Their branch outcomes are never substituted
for exact-parameter or all-size statements.

At selected actual cells and assigned panel endpoints, directed rational
square-root intervals evaluate the literal full maximum. They verify its
range and the 4-Lipschitz panel bound. These are bounded probes, not a
computer proof of the global Lipschitz theorem. No angular or root
numerics are used. Negative controls must reject a repeated high label,
wrong cyclic predecessor, reversed panel orientation, and negative
radicand, with the expected reason. No Python `assert` statement is used.

## 4. Commands independently executed and exact output

All commands below were run locally from the repository root under
CPython 3.14.3. Every command exited **0**. No hosted CI was inspected.
No production module, prior checker, or generated certificate is imported
by the new checker.

```text
python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py
python -I -S -O ops/TASK-20260911__general_block_transfer/check_general_blocks.py
```

Both runs produced identical output:

```text
PASS exact small domain: 30034 orders; 580560 cells; 173010 reflected and 254543 ordinary panel assignments
PASS rational-surrogate diagnostics: 18 orders; 1080000 cells; fourth lengths 0,2,2,2,4,4
PASS directed literal full max: 342 probes; 438 panel Lipschitz probes
PASS 4 negative controls: duplicate high, cyclic predecessor, reversed panel orientation, negative radical
NOTE finite arithmetic and rational-surrogate diagnostics only;
analytic proof supplies arbitrary parameters/k/m, full geometry and limits
```

```text
python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
python -I -S -O ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
```

Both runs produced identical output:

```text
EXACT A-3w > 354539/1000000000 > 0
EXACT A-3w-4eta_0 > 154539/1000000000 > 0
EXACT a-w-eta_0 > 204539/3000000000 > 0
EXACT b-w-eta_0 > 520991513/1000000000 > 0
EXACT 3/2-M > 21016513/1000000000 > 0
PASS 16 corner partitions, 448 reflection moments, 48 branch probes, 6 sign/tie controls
EXACT 16-panel raw full-max increment <= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
PASS bounded exact support; analytic proof supplies interval and cubic term
NOTE no root solving, width scan, finite recovery, transfer or output files
```

```text
python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py
```

```text
EXACT inherited epsilon slack = 431/32000000
EXACT lower residual = 1088173975683910831/2175907136349689169
EXACT lower signed square = -963745517404602389188679409068317/4734571866017504812540302482915910561 < 0
EXACT upper residual = 226493965596937/453065245150063
EXACT upper signed square = 34763358497298510706339907/205268116362886684743388903969 > 0
EXACT stationary upper slack = 35511/800000000
EXACT diagonal cutoff slack = 354539/3000000000
EXACT cost denominator slack = 24416513/1000000000
EXACT cost difference bracket = -2187/2048000000000 , -24389/72000000000000
EXACT saving over 1/250 > 12389/72000000000000
PASS two directed rational sign gates and positive pre-square residuals
PASS inherited bounds and analytic location/cost implications
NOTE: continuous proof supplies uniqueness; no finite recovery or geometric transfer
```

## 5. Source identity and handoff

SHA-256 values recorded after the above audits and runs:

```text
research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md
9ac8090eb00e85dcc155d875892e121f9459c28eb349109bc10a01a93950cb3b
research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md
2743de701d51d5fb57d84ffeff604ba5885a6a1c52340c96ca0dc98ceacfd4f5
ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
9f8abc019145df643f3e4b609fce3de137363ac884ac3e0d57153e979651df4c
ops/TASK-20260911__general_block_transfer/check_general_blocks.py
efa342274dd338d7331cfb12a4f3f4cf4c8f7b47ca4742fd409f0e5abb1cdec2
```

The general-transfer hash identifies the reviewed draft, including its draft
status marker; later editorial/status changes do not retroactively alter
this record. A material mathematical revision requires another audit of
the changed argument.

Only this review file and the new checker were written by the reviewer.
The proof, canonical ledgers, source certificates, production code,
historical paper and external review state were not edited by the reviewer.
Parent-agent integration, final-diff checks, checkpoint commit/push and
independent external acceptance remain separate steps.
