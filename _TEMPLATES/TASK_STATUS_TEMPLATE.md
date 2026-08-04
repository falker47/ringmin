# Task Status

```text
task=TASK-YYYYMMDD__short_description
mode=STANDARD|STRICT
state=NOT_STARTED|IN_PROGRESS|BLOCKED|READY_FOR_REVIEW|ACCEPTED|REJECTED
started_at=YYYY-MM-DD
updated_at=YYYY-MM-DD
```

## Objective

One bounded outcome, stated so that completion or failure is decidable.

## Scientific or engineering question

State the exact question, domain, quantifiers, and current epistemic status.

## In scope

- path/component;
- path/component;
- required proof, implementation, artifact, or documentation delta.

## Out of scope

List only concrete nearby risks of scope mixing.

## Expected delta

Describe the smallest coherent file-level change expected before editing.

## Protected paths potentially affected

- path;
- reason;
- required verification.

## Completion gates

- [ ] implementation/proof complete within stated scope;
- [ ] claims classified correctly;
- [ ] relevant tests run;
- [ ] relevant independent verification run;
- [ ] artifacts/provenance checked when applicable;
- [ ] durable memory updated;
- [ ] `git status --short` inspected;
- [ ] complete `git diff` inspected;
- [ ] `git diff --check` passed;
- [ ] no incidental generated/protected-file changes;
- [ ] state set to `READY_FOR_REVIEW`.

## Blockers

None, or one exact unresolved dependency/decision/resource.

## Handoff

Summarize the completed outcome, residual uncertainty, and exactly one next atomic task.
