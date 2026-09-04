# Definitions and Core Model

This thematic ledger owns the stable mathematical definitions and the exact
angular reformulation. It is a compact summary only; the linked publication
source remains authoritative for proof detail.

## Core definitions

For surrounding radii `a,b > 0` and central radius `R > 0`, the minimum angular separation is

```text
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

For a cyclic order `sigma`:

- `R_chain(sigma)` is the unique radius at which the sum of consecutive `theta_R` values is `2*pi`.
- `R_full(sigma)` is the minimum radius for which all pairwise angular non-overlap constraints are feasible in that fixed cyclic order.
- `R*(n) = min_sigma R_full(sigma)` is the global optimum for radii `1,2,...,n`.

Stable relations:

```text
R_chain(sigma) <= R_full(sigma)
min_sigma R_chain(sigma) <= R*(n) = min_sigma R_full(sigma)
R_chain(sigma*) <= R*(n)
```

Here `sigma*` denotes the chain-optimal Supnick order. These inequalities do not imply that `sigma*` is fully realizable.

## Stable model result

### Exact angular reformulation

**Status:** exact theorem.

Pairwise non-overlap for circles tangent to the central circle is equivalent to the angular-separation inequality defined above. The angle is symmetric, lies in `(0,pi)`, decreases strictly with `R`, and increases with each surrounding radius.

**Source:** `paper_assets/ringmin_paper.tex`, model section.

