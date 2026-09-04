# Ringmin Project Knowledge

## Scope and provenance

This is the canonical compact index for durable Ringmin knowledge after the
public arXiv-v1 snapshot. It routes readers to thematic ledgers; it is not a
second ledger and does not independently prove or re-certify their claims.

Bootstrap source snapshot:

```text
repository=falker47/ringmin
commit=9f67244b6226619df99a5eea2249f3fca8a32669
paper=arXiv:2607.28654
snapshot_date=2026-08-04
```

The commit records the post-arXiv-v1 repository update. Detailed published
proofs remain in `paper_assets/ringmin_paper.tex`. Finite certificate claims
require the optimum and frontier artifacts, their provenance, and
`verify.py`. The full frontier audit also reads local progress logs that are
intentionally ignored by Git; tracked files alone are not currently
sufficient to reproduce that audit in a fresh clone.

## Central definitions and guardrails

For surrounding radii `a,b > 0` and central radius `R > 0`, write

```text
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

For a cyclic order `sigma`, keep these objects distinct:

- `R_chain(sigma)`: the adjacent-chain closure radius;
- `R_full(sigma)`: the minimum all-pairs-feasible radius for that fixed
  cyclic order;
- `R*(n) = min_sigma R_full(sigma)`: the global optimum for radii
  `1,2,...,n`;
- `sigma*`: the chain-optimal Supnick order.

Always preserve

```text
R_chain(sigma) <= R_full(sigma)
min_sigma R_chain(sigma) <= R*(n) = min_sigma R_full(sigma)
R_chain(sigma*) <= R*(n)
```

These relations do not make the chain optimum a geometric optimum, fixed-order
feasibility a global optimum, a feasible construction an optimum, a finite
certificate an all-`n` theorem, or a heuristic result certified. Quantifiers,
tolerances, and the distinction between one recovered placement and every
optimal placement are part of each claim.

## Canonical thematic ledgers

Each stable claim has one canonical thematic owner. The short central
reminders above do not replace the full classified entry in its owner.

- [`knowledge/DEFINITIONS.md`](knowledge/DEFINITIONS.md) — angular kernel,
  core objects, stable relations, and exact model reformulation.
- [`knowledge/FIXED_ORDER_THEORY.md`](knowledge/FIXED_ORDER_THEORY.md) —
  Supnick chain theory, formal seam onsets, fixed-order feasibility, and the
  boundary between those theorems and the floating-cascade conjecture.
- [`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`](knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md)
  — induced-subset bounds, global asymptotic bounds, explicit constructions,
  heuristic larger-`n` observations, disproved claims, and open global
  questions.
- [`knowledge/CERTIFICATION.md`](knowledge/CERTIFICATION.md) — certified
  finite scope, finite regimes, evidence-chain requirements, and
  certification-specific limitations.
- [`knowledge/IMPLEMENTATION.md`](knowledge/IMPLEMENTATION.md) — production
  and independent-verifier architecture, test/CI scope, and portability
  limitations.
- [`knowledge/PUBLICATION_HISTORY.md`](knowledge/PUBLICATION_HISTORY.md) —
  public-snapshot provenance and the separation between historical arXiv-v1
  wording and active post-publication knowledge.

## Navigation and authority rules

1. Start here, then read only the thematic ledger or ledgers relevant to the
   task.
2. Within each ledger, use its explicit epistemic status and source links;
   follow a link only when the task needs the underlying detail.
   Source paths recorded in ledgers are repository-root-relative.
3. For mathematical detail, the linked proof note or published theorem
   controls over every compact ledger summary.
4. For a finite certification claim, the artifact, complete provenance, and
   independent verifier must agree; a ledger entry or Boolean field is not
   sufficient evidence.
5. The same stable claim must not be copied into multiple thematic ledgers.
   Use a cross-reference to its canonical owner instead.
6. Current task state belongs only in `CURRENT_STATUS.md`; ranked scientific
   priorities belong only in `research/NEXT_RESEARCH_STEPS.md`.
7. If a source and summary conflict, correct the summary in its owning ledger;
   do not silently revise the source, publication history, or another module.
