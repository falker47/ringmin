# Task Status

```text
task=TASK-20260905__reflected_prefix_alpha
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
task_base_head=ae2b7ab2de614b798950fc2192437880078b5b3a
```

## Objective and scientific question

Decide whether the lambda-optimized reflected prefix improves by increasing
alpha from the exact shift minimizer alpha_*, keeping the exact normalized
minimizer x_* fixed and lambda=(1+alpha)*x_*. The completed proof extends
recovery only to I=[53/500,107/1000], verifies the full coefficient formula,
and proves a uniformly negative derivative there. The rational witness
alpha=107/1000 improves C_rp by more than 1/60000000. Its full-radius
theorem, actual feasibility and global deletion corollary are separate.
Authoritative source: research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md.

## In scope and expected delta

- New research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md.
- This dossier and its deterministic check_alpha.py.
- knowledge/FIXED_ORDER_THEORY.md: sole owner of recovery, variation,
  coefficient definitions and comparisons.
- knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md: separate global deletion corollary.
- CURRENT_STATUS.md and research/NEXT_RESEARCH_STEPS.md: state and priority.

## Out of scope and protected paths

No joint global alpha/lambda optimization, general permutation/coupling
search, finite certification extension or publication revision. Earlier
proof notes and dossiers, paper_assets/, results/, src/, tests/, scripts/,
verify.py, publication metadata, README.md, REPORT.md, other knowledge
ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md are
protected. Check the complete changed-path whitelist before handoff.
The user's subsequent explicit request authorizes commit and push of
exactly this nine-file task delta. Mathematical review and acceptance
remain separate from this Git integration authorization.

## Verification design

The analytic proof must check finite floors, both cyclic seams, the moving
wrap contribution to K', the normalization A^2/(4*pi), and constant x_*.
Use only isolated rational gates: square-root enclosures on a 10^-20 grid,
128-panel trapezoid/midpoint bounds for the concave integrands in D=K',
at alpha=53/500,267/2500,107/1000. Verify the rational domain, saving and
slope comparisons. No random seed or unbounded experiment is needed.

Bounded combinatorial checks cover m=2..128 and three rational alpha
probes, with x at the two accepted bracket endpoints and their midpoint.
They test the construction, not an optimization. Separate canonical mpmath
diagnostics at 70 digits use the original unnormalized full-max cost,
three alpha derivative probes, and all-pairs angular/Cartesian checks at
selected small and growing m for the witness. For all eight tested sizes,
the accepted rational x_* bracket determines the same integer floor at
both endpoints; the finite orders therefore use no decimal floor premise.

## Completion gates

- [x] Analytic neighborhood recovery, correct coefficient and derivative.
- [x] Explicit rational witness and exact strict coefficient comparison.
- [x] Local exact checker and independent full-max/geometry diagnostics.
- [x] Fixed-order, feasibility and global statements distinguished.
- [x] Durable owners, roadmap and task evidence updated.
- [x] Complete tracked/untracked diff and explicit whitespace audit.
- [x] Protected paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. The user identifies the HEAD lambda theorem as accepted; the existing
notes retain their historical review wording. No external review of the
present extension is asserted.

## Handoff

The bounded mathematical question is resolved affirmatively. New exact
gates, the imported lambda exact checker, independent full-max/geometry
diagnostics and the source/path audit exit 0. The new extension awaits
external independent review; imported exact theorems remain dependencies.
No parameter optimum, finite global certificate or normalized global limit
is established. Final file/provenance/whitespace inspection passes and the
task is READY_FOR_REVIEW. The user subsequently requested commit and push;
the authorized integration does not change the mathematical review state.

Exactly one next atomic task: independently review this alpha extension,
its rational gates and witness, recovery, full-root and separate deletion
steps, recording acceptance or precise corrections without further research.

Suggested manual commit message:
`research: improve reflected prefix by increasing alpha at fixed x`.
