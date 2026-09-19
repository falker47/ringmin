# Task Status

```text
task=TASK-20260919__merge_global_bracket_verifier
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
```

## Objective

Merge the explicitly authorized remote main into local main without rewriting
either history; verify, push normally and inspect hosted CI for the exact merge.

## Scientific or engineering question

Engineering integration only. Preserve the existing finite claim
L_n < R*(n) <= U_n for n=3,...,14, its evidence and its independent-review
boundary. No new theorem, certificate, baseline acceptance or journal readiness.

## In scope and expected delta

- Merge parents: local `c0075cf9dbe902571748299b21e368a0433c784e` and remote
  `5c98063a9a38d6f7f76d7ec7a073f3cdf8d5717a`.
- Common base: `98d6a6e340e4008ce35e789c54333ae43466b49d`.
- Resolve only `CURRENT_STATUS.md`, preserving both compatible contexts.
- Add this task dossier and reproducible integration/preservation evidence.
- Preserve every other path exactly as selected by the nonconflicting union.

## Protected paths and exclusions

Production solver, historical verifier, numerical results, original evidence,
proofs, publication sources/PDFs, citation metadata, index, roadmap and review
protocol remain unchanged. Remote publication README/ledger changes are retained
exactly. The Review State Registry is external and receives no read/write call.
No baseline is promoted. The existing untracked publication ZIP remains
untouched and unstaged; its initial SHA-256 is
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.

## Completion gates

- [x] Fetch confirms the precise authorized divergence, two commits on each side.
- [x] Only the explicitly exempted ZIP was dirty before merge.
- [x] Merge stopped before commit; only CURRENT_STATUS.md conflicts.
- [x] Resolve status without changing scientific meaning.
- [x] Complete global verifier, STRICT adversarial regressions, full tests,
  historical full verifier, CI smoke command, lint and whitespace pass.
- [x] Source/archive hashes and both parent trees preserved; inspect staged diff.
- [ ] Commit with two intended parents and push normally.
- [ ] Verify actual remote SHA and its hosted CI.

## Blockers

None. Local verification and staged preservation audit passed. The last two
gates are performed after creating this merge commit and reported in the task
handoff for its exact SHA; they cannot be recorded as passed in their own SHA.

## Handoff

Local result: READY_FOR_REVIEW. Exactly one next atomic task: independent STRICT review of the resulting merge
commit and the global bracket integration. Acceptance remains the reviewer's
decision; local/hosted checks do not update the Registry.
