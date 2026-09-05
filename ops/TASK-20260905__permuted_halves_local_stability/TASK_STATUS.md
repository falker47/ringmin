# Task Status

```text
task=TASK-20260905__permuted_halves_local_stability
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective and scientific question

Prove uniformly over high permutations that at most K adjacent position
swaps change the exact full-radius root by o(m^2), for each fixed K.
Seek an explicit stronger bound and apply it to the first-two-high swap
behind the m=4 counterexample, preserving the distinction between finite
improvement and a changed leading coefficient.

## In scope and expected delta

- research/PERMUTED_HALVES_LOCAL_STABILITY.md;
- knowledge/FIXED_ORDER_THEORY.md (sole stable claim owner);
- research/NEXT_RESEARCH_STEPS.md and CURRENT_STATUS.md;
- this dossier, including a bounded independent diagnostic/algebra checker.

## Out of scope and protected paths

All other paths, especially preceding proof notes and dossiers,
paper_assets/, results/, src/, tests/, scripts/, verify.py, publication
metadata, README.md, REPORT.md, other knowledge ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md and RINGMIN_REVIEW_PROTOCOL.md.
No permutation optimization, factorial enumeration, global certification,
published-paper changes or Git/GitHub writes.

## Verification design

The proof uses the exact full cell criterion, the two-cell swap identity,
an angular high derivative bound, and a branch-safe radial contraction.
Check derivatives independently with symbolic algebra and all scalar
constant/sign gates exactly. The deterministic diagnostic used only
m in {2,3,4,8,16,32,48,64}, three prescribed permutations per size and
at most three cyclic swap positions per permutation; plus the two explicit
first-swap refinement/sharpness families at m=32,48,64. No permutation search.
The alternate atan formula used 70 digits, 240 bisections and guard 1e-55.
It checked the weighted O(m), O(1/m) and linear-sharpness bounds; these
finite observations are not proof premises. Only the two m=4 brackets
were rechecked with rational intervals from the existing checker,
without invoking its enumeration or writing its assets.

## Completion gates

- [x] analytic proof, boundary cases and coefficient quantifiers;
- [x] symbolic/rational checks and bounded independent numerical checks;
- [x] claims, dependencies and verification limitations recorded;
- [x] owning ledger, roadmap, current status and dossier synchronized;
- [x] complete tracked/untracked content and whitespace review;
- [x] changed-path whitelist and protected/generated-file audit;
- [x] READY_FOR_REVIEW handoff.

## Blockers

None. The clean tree was checked at HEAD
460d705ff349340975feb51ea886d7a0f1aab08c with a per-command
safe.directory option. No persistent Git configuration was changed.

## Handoff

The exact weighted bound resolves the requested uniform o(m^2) theorem,
with O_K(m), an explicit linear-sharpness family, and the sharper O(1/m)
first-swap corollary for interior shifts. The best-shift continuation of
m=4 retains C_shift. Symbolic/rational and all bounded numerical checks
passed locally; all eight changed files passed the final file audit.
Independent human review of the proof and imported dependencies remains
pending; no general permutation optimizer or global certificate is claimed.

Suggested manual commit: research: prove uniform local stability of permuted halves

Exactly one next atomic task: independently review this uniform stability
theorem, its sharpness and shift refinement, reproduce the bounded checker
and audit the imported fixed-order/shift-limit dependencies; record
acceptance or precise corrections.
