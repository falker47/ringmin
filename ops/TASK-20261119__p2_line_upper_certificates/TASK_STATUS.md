# Task status

```text
task=TASK-20261119__p2_line_upper_certificates
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-19
updated_at=2026-11-20
base=7d257221d9034ca5f895f062e45e782d8e77b6c2
branch=codex/p2-line-upper-certificates
```

## Objective, scope and result

Give a reproducible line witness and a rigorous structured upper endpoint for Paper II. For p=1 the n=3200 witness proves C* < 0.140958576058 by the published limit theorem. The fixed rational block cost lies in [0.14191330499527, 0.14191330499528]. For p=2 the same construction proves finite upper bounds and yields a conditional limiting ceiling of 0.088581212993. See the [note](../../paper_assets/line_upper/NOTE.md).

## Completion gates and protected paths

All twenty exact certificates, both block methods, the reference comparisons, the one-page three-pass preview, the full unit suite, the legacy exact-bracket verifier and byte replay passed locally. The changes are additions under the permitted paper subdirectory, test and dossier. Existing papers, publication assets, implementations, results, certificate verifiers and shared ledgers are protected.

## Blockers and handoff

The work has no remaining local verification blocker. Search optimality and the precise limiting constant remain open. The quadratic limiting statement depends on independent acceptance of the profile theorem. The local commit awaits independent mathematical review.
