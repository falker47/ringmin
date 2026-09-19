# Task Status

```text
task=TASK-20260919__global_bracket_verifier
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
```

## Objective

Integrate a complete independent verifier of the supplied twelve global
brackets, reject the reproduced P1 false positives, and bind the pinned
payload to its preserved input evidence. No historical Stage A replay.

## Scientific or engineering question

For each integer n=3,...,14, does the supplied finite certificate establish
L_n < R*(n) <= U_n? The result is a computer-certified finite bracket,
subject to separate review of the exact integration commit.

## In scope and expected delta

- `verify_global_brackets.py`: stdlib-only complete verifier adapted from the
  preserved independent reviewer implementation, with explicit schema and
  mathematical versus pinned-evidence contracts.
- `tests/test_global_brackets.py`, `.github/workflows/ci.yml`: falsification,
  small independent oracles, complete certificate gate.
- `reproducibility/global_brackets/`, `.gitattributes`: selected unchanged
  originals and byte-preservation checks, not the entire external directory.
- `research/GLOBAL_BRACKET_CERTIFICATE.md`, `knowledge/CERTIFICATION.md`,
  `CURRENT_STATUS.md`, and this dossier: proof, scope, provenance and handoff.

## Protected paths potentially affected

`src/ringmin/`, `verify.py`, `results/`, `paper_assets/`, public result tables,
publication metadata, roadmap and Review State Registry are outside the delta.
The user explicitly permits the existing untracked
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip` and
requires it to remain untouched and unstaged. No other unrelated dirty path
is authorized. The external supplied directory is read-only.

## Completion gates

- [x] complete original-payload verification and input binding;
- [x] adversarial, DP, insertion and interval oracles: 44 new tests passed;
- [x] proportionate full tests: 59 passed; complete CI command added;
- [x] proof and evidence classifications recorded;
- [x] original bytes and protected paths checked;
- Final integration gate: inspect staged diff and whitespace, commit, normal
  push, inspect exact-SHA hosted status and report at handoff.
- [x] READY_FOR_REVIEW, without accepting a baseline.

## Blockers

None after the user supplied the original package and the specific ZIP exception.

## Handoff

Implementation and local verification are complete; see EVIDENCE.md and
VERIFICATION_FINAL.json. The verifier is independent of production and the
generator, but derives from supplied reviewer code; another execution is not
another independent review. Exactly one next atomic task: independent review
of the integration commit.
