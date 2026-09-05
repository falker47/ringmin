# Task Status

```text
task=TASK-20260905__reflected_prefix
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective

At alpha=alpha_* fixed, prove that one explicit lambda>1/4 extends the
deterministic recovery construction to genuine high permutations and
strictly improves its full-radius coefficient over C_ref(1/4).

## Scientific question and result

The all-integer construction with q=2*floor(lambda*m/2) works for every
fixed 1/4<=lambda<1-alpha_*. The exact continuous full max admits at most
one reflected-block switch. Rational gates prove that lambda=3/10 stays
on the chord branch and improves the coefficient strictly. This is an
exact theorem, with an imported uniform full-root transfer and a proved
global upper-bound corollary. See the authoritative proof, not this dossier,
for all mathematical details.

## In scope and expected delta

- New research/PERMUTED_HALVES_REFLECTED_PREFIX.md.
- A task-local checker and this three-document dossier.
- The single fixed-order claim owner, distinct global upper-bound owner,
  ranked roadmap and current status, updated only after the proof closed.

## Out of scope and protected paths

No optimization of alpha or lambda and no general permutation/coupling
search. Previous proofs (including the original recovery note) and their
dossiers, paper_assets/, results/, src/, tests/, scripts/, verify.py,
README, REPORT, metadata, other knowledge ledgers, PROJECT_KNOWLEDGE.md,
AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md are protected. Final path-whitelist
inspection is required. No Git history or GitHub writes are authorized.

## Bounded verification design

The discriminator is the exact branch-safe strict saving at lambda=3/10,
not a numerical minimum. The checker domain was fixed in its source before
execution: all legal (m,s,q) for m=2..64; rational coordinate representatives
for m=2..48 and lambda in {1/4,3/10,1/2,3/4,7/8}; eight polynomial tests
at alpha=1/10, three prefix lengths and nine listed sizes; continuous cost
tests at four lengths and one switch boundary; nine specified root sizes.
The extra lengths exercise branch formulas and seam cases, without
searching for another witness. No randomness or unbounded loop is used.
Exact gates use Fraction; diagnostics use canonical mpmath at 60 digits
(120 digits only to cross-check bounded alpha floor choices). The output
is labeled stdout retained in EVIDENCE.md; no result artifact is replaced.

## Completion gates

- [x] Bounded proof complete; mathematical and numerical claims classified.
- [x] Rational occurrence, predecessor, seam, moment and saving gates pass.
- [x] Independent full-score/root and all-pairs diagnostics pass.
- [x] Canonical dependencies only; no SymPy dependency carried forward.
- [x] Durable owner/upper-bound/roadmap/current-state updates prepared.
- [x] Complete tracked and untracked diff, whitespace and source audit.
- [x] No incidental protected/generated changes; READY_FOR_REVIEW handoff.

## Blockers

None. External independent review of this proof and imported dependencies
remains pending; it is not being claimed by the local checker.

## Handoff

The exact witness is lambda=3/10. Neither a best parameter nor a global
optimum is determined. Exactly one next atomic task: independent review
of this longer-prefix proof, its imported root/deletion steps and bounded
checker, recording acceptance or precise corrections without optimization.

Suggested manual commit message:
`research: improve reflected-prefix upper bound at fixed alpha`.
