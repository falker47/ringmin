# Task Status

```text
task=TASK-20260830__effective_supnick_seam_cutoff
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-30
updated_at=2026-09-02
```

## Objective

Make the eventual formal-seam theorem effective by proving one explicit
integer cutoff `K_eff` such that

```text
s_k = 4k+6                         for every integer k>=K_eff.
```

Test `K_eff=4325` with the prescribed comparison scales `13/5` at `c=5`
and `11/5` at `c=6`; increase it without optimization only if an exact gate
fails.

## Scientific question

Do the quantitative closure estimate (17), the exact threshold estimate
(28), and rational separators for `rho` prove, without a finite scan,

```text
R_{k,4k+5} < (13/5)k^2 < T_{k,4k+5},
T_{k,4k+6} < (11/5)k^2 < R_{k,4k+6}
```

for every integer `k>=4325`, so that the imported fixed-`k` sign and
persistence theorem gives the claimed onset?

## In scope

- effective sharpening of `research/EVENTUAL_SUPNICK_SEAM_ONSET.md`;
- exact rational denominator, arcsine-remainder, `rho`, `kappa`, and
  reciprocal gates using only the estimates already present in that note;
- one task-local stdlib/`Fraction` checker with in-memory constant-mutation
  rejection and no scan over `k` or `n`;
- a new four-file dossier;
- durable knowledge, status, and roadmap synchronization only after all
  exact gates pass.

## Out of scope

- minimizing `K_eff` or classifying any individual onset below it;
- using a finite scan as proof;
- full fixed-order feasibility, `R*(n)`, global optima, contact graphs, or
  global floating-circle claims;
- solver, test, certificate, `verify.py`, paper, or generated-asset changes.

## Expected delta

- update the existing eventual-onset proof note with the effective bridge;
- add this dossier and `check_effective_cutoff.py`;
- update `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the ranked roadmap
  only after the checker and adversarial reviews pass.

## Protected paths potentially affected

- `research/FIXED_K_SUPNICK_SEAM.md`: read-only imported sign/persistence
  theorem;
- `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md`: read-only prior theorem;
- prior proof notes and `ops/TASK-*` dossiers: read-only historical evidence;
- `src/`, `tests/`, `scripts/`, `results/`, `verify.py`: no production or
  certificate delta;
- `paper_assets/`, `README.md`, `REPORT.md`: historical/public/generated
  assets remain unchanged.

## Completion gates

- [x] exact effective proof derived within the formal-seam scope;
- [x] `K_eff=4325` closes with exact positive margins;
- [x] three independent read-only derivations found no defect;
- [x] exact checker passes in normal and optimized/no-site modes;
- [x] in-memory constant-mutation audit rejects every alteration;
- [x] checker source/AST audit passes;
- [x] repository regression tests pass;
- [x] durable memory is synchronized;
- [x] `git status --short` and complete diff are inspected;
- [x] tracked and untracked whitespace checks pass;
- [x] protected paths remain unchanged;
- [x] the external-review documentation rejection is corrected;
- [x] the authoritative-source coherence audit passes;
- [x] the duplicate resolved roadmap section is consolidated without changing
  the active priority;
- [x] the post-review regression suite passes;
- [x] state is set to `READY_FOR_REVIEW`.

## Blockers

None.

## External review correction

The independent review of commit
`1db59857413b66b36b14e03af9281a956951fd40` accepted the mathematics and
checker but returned `REJECT` because `PROJECT_KNOWLEDGE.md` still listed
effectivizing the eventual identity as a primary open problem. That stale
claim is removed: the open seam-onset work now concerns only the unresolved
finite range `8<=k<4325`, beginning with a future diagnostic for `s_8`.

The two substantially duplicate resolved roadmap sections were consolidated
into one. `CURRENT_STATUS.md` was checked and required no change. The proof
note, checker, `K_eff=4325`, solver, tests, certificates, verifier, paper, and
publication assets remain untouched.

## Handoff

`K_eff=4325` is proved valid for the formal seam, with `156` exact checker
gates, `15` rejected constant mutations, three independent final reviews,
and `12` passing regression tests. The cutoff is not claimed minimal; exact
onsets in `8<=k<4325` remain open, and no full-feasibility, `R*(n)`,
contact-graph, or global-floating conclusion is made.

Exactly one next atomic task after acceptance: run the bounded two-precision
radius-8 diagnostic on `33<=n<=46`, reporting only a numerical onset
candidate and any rational separator of denominator at most `1000`.
