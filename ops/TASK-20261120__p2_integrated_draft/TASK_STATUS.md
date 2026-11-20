# Task status

~~~text
task=TASK-20261120__p2_integrated_draft
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-20
updated_at=2026-11-20
branch=codex/p2-integrated-draft
base=3a5c3c91fb9d744d90ca6776f41bb7704fd1a2c7
pr_target=codex/paper-ii-journal-candidate
~~~

## Objective and scope

Integrate the reviewed profile proof and finite upper witnesses into a
single journal manuscript. PR #10 is the base. Two normal merges supply
PR #6 and PR #8. All subsequent editorial changes belong to the journal
package, its test and this dossier.

## Completion gates

The journal PDF has nine main-text pages and ten pages in total. The
three-pass build resolves all references and citations, with zero
overfull boxes. Both n = 3200 line certificates pass the isolated
all-pairs checker. S1 and the independent global brackets pass. The
full source replay passes all 104 tests plus four subtests. The PDF and
both figures were reproduced byte for byte. See the commands, hashes,
claim classifications and scope audit in [EVIDENCE.md](EVIDENCE.md)
and the [v3 claim map](../../paper_assets/journal_p2_v4/CLAIMS_DIFF.md).

## Proposed shared ledger text

Proposed for the normalized-limit section of
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md` after independent review:

> Exact theorem with a written proof. For uniformly bounded marks with
> weakly convergent empirical laws, the optimal radius divided by the
> count and the common radius scale tends to E(μ)/π. The indexed quantile
> word program has ring-coefficient bracket width M(1/k+1/r)/π. For
> fixed p > 0 this gives a leading coefficient for radii iᵖ. The
> adjacent-pair bound gives C₂ ≥ 1/(6π). Proved corollaries of the
> finite-template infima and exact all-pairs witnesses give
> 0.1405694688 < C* < 0.140958576058 and C₂ < 0.088581212993.
> The profile theorem awaits external human mathematical review.

The owning proof and witness sources are
[PROFILE_GENERALIZATION.md](../../research/PROFILE_GENERALIZATION.md) and the
[line-certificate package](../../paper_assets/line_upper/).

## Handoff and next atomic task

The external mathematical reviewer should review the integrated profile
theorem and its quadratic specialization in the draft PR. The exact
asymptotic coefficients and witness optimality remain open.
