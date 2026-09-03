# Task Status

```text
task=TASK-20260902__radius8_seam_diagnostic
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-02
updated_at=2026-09-02
```

## Objective

Run a bounded NUMERICAL DIAGNOSTIC for the formal radius-8 Supnick seam,
using every integer `33<=n<=46`, and locate the first stable sign change of
`D=R_{8,n}-T_{8,n}`. If adjacent endpoints exist, search for one common
rational separator with denominator at most `1000`.

## Scientific or engineering question

`R` is the adjacent-chain closure root on `{8,...,n}`; `T` is the physical
Descartes threshold in `research/FIXED_K_SUPNICK_SEAM.md`. No full-order or
global optimization is involved. A candidate onset remains a numerical
observation until a separate exact endpoint proof is completed.

## In scope

- This dossier, a standalone diagnostic script, and its numerical artifact.
- `CURRENT_STATUS.md` and the pertinent roadmap entry.
- Independent edge constructions and independent runs at 90/150 decimal digits.

## Out of scope

Exact endpoint proofs, scans outside `33..46`, other `k`, production changes,
certificate generation, paper revisions, and Git/GitHub writes.

## Expected delta

Five dossier files plus the two current-state/priority documents. Preserve
`PROJECT_KNOWLEDGE.md` byte for byte, including its exact claims.

## Protected paths potentially affected

`PROJECT_KNOWLEDGE.md`, all research proof notes, `AGENTS.md`, `src/`,
`tests/`, `scripts/`, `results/`, `verify.py`, `paper_assets/`, `README.md`,
`REPORT.md`, dependency files, and earlier dossiers. Verify no changes.

## Completion gates

- [x] Two reconstructions agree for every `n`; all vertices/edges audited.
- [x] Independent 90/150-digit runs cover exactly `33..46`.
- [x] Root residuals, local numerical brackets, threshold branch and stability checked.
- [x] First crossing and bounded separator search recorded without an exact onset claim.
- [x] Artifact source hashes and deterministic reproduction checked.
- [x] Current status and roadmap updated with exactly one next atomic task.
- [x] Complete tracked/untracked delta and whitespace inspected.
- [x] No protected or incidental generated changes; `READY_FOR_REVIEW`.

## Blockers

None. Git requires a per-command safe-directory override for the sandbox
account; no persistent configuration is modified.

## Handoff

NUMERICAL DIAGNOSTIC completed: first stable crossing `37/38`, numerical
candidate `38`, common separator `176/1`, minimum numerical separator
margin approximately `0.2242263045`. All 14 inputs were computed at both
90 and 150 digits; optimized recomputation is byte-identical. The largest
stored run difference is approximately `4.021905e-76`.

Five new dossier files and two tracked documentation updates are ready for
manual review. Both numerical paths share mpmath, and no endpoint
inequality or exact onset is proved here. See `EVIDENCE.md` for commands,
all values, reconstruction, guards, source hashes and limitations.

Suggested manual commit message:
`research: record bounded radius-8 seam numerical diagnostic`

Exactly one next atomic task: prove the exact endpoint bridge at `n=37,38`
with separator `176`, auditing both threshold signs and all 30/31 chain
edges before applying the existing fixed-`k` theorem. Do not start it here.
