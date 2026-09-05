# Task Status

```text
task=TASK-20260905__reflected_prefix_lambda
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective

Optimize the proved reflected-prefix family over 1/4<=lambda<1-alpha_*,
with alpha=alpha_* fixed exactly. Characterize the complete variation,
prove or refute the proposed unique internal minimum with strict
monotonicity on both sides, rigorously bracket any claimed minimizer,
and improve C_30 by a separate feasible-construction global corollary.

## Scientific question

The exact block and tail formulas are imported from
research/PERMUTED_HALVES_REFLECTED_PREFIX.md. The complete variation now
proves the reviewer's minimizer bracket, but refutes whole-right-side
monotonicity: a later local maximum precedes a final descent. The minimum
remains globally unique. Rational gates give the strict coefficient saving
C_rp<C_30-1/100000, followed by a separate global upper-bound corollary.
The authoritative proof is research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md.

## In scope and expected delta

- New research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md.
- This dossier and a deterministic task-local independent checker.
- knowledge/FIXED_ORDER_THEORY.md as sole owner of the fixed-order result.
- knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md for the separate deletion corollary.
- CURRENT_STATUS.md and research/NEXT_RESEARCH_STEPS.md for the handoff.

## Out of scope and protected paths

Alpha is not varied as a design parameter. No general permutation/coupling
search or finite certification extension. Earlier proof notes and dossiers,
paper_assets/, results/, src/, tests/, scripts/, verify.py, publication
metadata, README, REPORT, other knowledge ledgers, PROJECT_KNOWLEDGE.md,
AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md remain protected. The user's
subsequent explicit instruction authorizes commit and push of this task
delta only. Inspect the final changed-path whitelist. Mathematical review
and acceptance remain separate from this Git integration authorization.

## Verification design

Analytic derivatives and curvature inequalities cover the complete domain
and both switches. The checker discharges only isolated exact gates:
two coarse and two narrow alpha signs, two normalized-minimizer signs,
Phi(4/5)<0, E(1)>0, coefficient enclosures at lambda=159/500 and 3/10,
and rational square gates for the curvature proof. It uses 10^50 integer
interval scaling, 64-term bounded series and 100 switch bisections.
The range/stopping rules were fixed in the source before execution.

An independent 70-digit mpmath diagnostic compares the original full-max
integrals to eleven derivative and curvature probes, both transition
continuity checks and exact slope/coefficient enclosures. It reports two
stationary points without using them in the exact gates. A later verification
addition audits nondegenerate interval boxes and the derived curvature
formula, without expanding the mathematical task. No random search,
unbounded enumeration, new dependency or production change.

## Completion gates

- [x] Complete analytic variation and rigorous monotonicity counterexample.
- [x] Exact rational brackets and strict coefficient improvement.
- [x] Independent local checker; diagnostics separated from exact gates.
- [x] Fixed-order theorem and global corollary kept distinct.
- [x] Durable owners, roadmap, current state and evidence updated.
- [x] Complete tracked/untracked diff and explicit whitespace audit.
- [x] Protected paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. Existing sources record external independent review as pending;
this task does not infer an acceptance decision from committed files.

## Handoff

The bounded question is resolved: the minimum is unique but the full
right branch is not increasing. External independent review remains
pending, including imported recovery, feasibility and uniform root transfer.
Exactly one next atomic task: independently review this lambda-variation
theorem and checker, recording acceptance or precise corrections without
alpha or general permutation/coupling optimization.

Suggested manual commit message:
`research: optimize reflected prefix lambda at fixed alpha`.
