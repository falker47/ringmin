# Task Status

```text
task=TASK-20260911__four_level_width_optimum
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
base_head=4e1aaef297d7946e9afe7f348a39ba607d985288
```

## Objective

Solve the closed width-only variational problem at the three unchanged
Section 11 cutoffs, classify the accepted widths, and rigorously bound the
largest gain. The user identifies the base HEAD as accepted.

## Scientific question

For every nonnegative h with h_1+h_2<=113/12500 and
h_2+h_3<=593/50000, maximize the exact positive-part quotient in
Section 9. Separate its weak-boundary optimum from finite floor gates.

## In scope and expected delta

- Append Section 12 to `research/THREE_LEVEL_COMMON_CHAIN.md`.
- Extend the existing four-level owner in
  `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`; update its endpoint cross-reference.
- Update `research/NEXT_RESEARCH_STEPS.md` and `CURRENT_STATUS.md`.
- Add this focused dossier and an independent standard-library checker.

## Out of scope and protected paths

No new cutoffs, broader parameter search, production or verifier edits,
finite certificate generation, paper revision, or upper construction.
Protect proof Sections 1-11, other ledgers, `PROJECT_KNOWLEDGE.md`,
`AGENTS.md`, `src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`,
`README.md`, `REPORT.md`, metadata, workflows and all earlier dossiers.
Compare the final changed-path list and the old proof prefix with base HEAD.

## Completion gates

- [x] Exact global proof, uniqueness and accepted-width classification.
- [x] Rational root, multiplier, value and gain certificates.
- [x] Weak versus strict finite-gate distinction, including a negative control.
- [x] Fresh standalone and dependency checks; optimization-disable control.
- [x] Classified single-owner memory, roadmap and current status.
- [x] Complete tracked/untracked review, whitespace/link/scope checks.
- [x] READY_FOR_REVIEW handoff, independent acceptance separate.

Integration follows this precommit snapshot: stage only inspected paths,
inspect/check the staged diff, commit and normally push under the standing
authorization, then verify remote HEAD and the clean tree. The final task
response records the integration result without a self-referential commit hash.

## Blockers

None. Git needs a per-command safe.directory setting under the sandbox
identity; no persistent Git configuration is changed.

## Handoff

Section 12 resolves the width-only question with an exact global remainder
certificate, a unique isolated cubic root and rational gain bounds. The
accepted widths are strictly locally improvable. The boundary optimum is
an unattained strict-domain supremum and fails finite floor gates infinitely
often; strict scaling and a rational improved witness have explicit gates.
No production, certificate or publication changes. See EVIDENCE.md for
local verification and limits.

Exactly one next atomic task: independently review the fixed-cutoff width
optimum and its arithmetic/transfer at committed HEAD.
