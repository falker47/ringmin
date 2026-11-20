# Task Status

```text
task=TASK-20261119__p1_general_radii_certification
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-19
updated_at=2026-11-20
base=c26400b328c2f8fa338b588e61abb98266a265f9
working_branch=codex/p1-general-radii-certification
```

## Objective and scope

Generalize Paper I's exact finite certification to any list of at least three distinct positive integer radii. Certify the linear regression through fourteen and quadratic radii at least through ten when feasible. Deliver source, standalone verifier, certified data, mathematical argument, tests, and a proposed shared update. The dossier contains local evidence for independent review.

## Expected delta and protected paths

The change adds only `paper_assets/general_radii/`, `tests/test_general_radii.py`, and this dossier. The published manuscript, original generator, original certificates and both existing verifiers are evidence inputs. They remain protected, as do shared ledgers, the roadmap, repository status, packaging, production code and CI.

## Completion gates

The generator and independent verifier support arbitrary distinct positive integer radii and every deletion depth from zero through $n-3$. The [method note](../../paper_assets/general_radii/METHOD_NOTE.md) proves coverage and strictness. The 24 verified brackets cover both families for $n=3,\ldots,14$. The [evidence](EVIDENCE.md) records independent replay, comparison to the earlier interval results, byte-identical regeneration, controls and the full local suite. Proposed ledger/status text is confined to this dossier.

## Blockers and handoff

All requested finite gates passed locally. The worked examples establish finite brackets and leave exact optimal orders, contact classification, larger instances and asymptotic conclusions open. The two-minute per-rung generation limit did not bind within the selected range. The independent reviewer can replay this branch from its committed snapshot. No external submission or push was requested.

## Exactly one next atomic task

Independently review the generalized coverage proof and replay the committed quadratic and linear certificates.
