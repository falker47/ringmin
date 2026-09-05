# Task Log

## 2026-09-05 01:45 - Startup and experiment design

- Base HEAD: 1636bf23cfadac46fb785bf6b1afda7e2787a466.
- Clean tree, including untracked inventory, before editing. Read the
  contract, index, current status, pertinent fixed-order ledger, roadmap,
  two requested notes, preceding swap evidence/checker, task templates,
  dependency manifests and angular definitions in paper/verifier.
- Mode STRICT; expected delta and finite discriminator are in TASK_STATUS.
- Initial plain Git status failed dubious ownership. Per-command
  safe.directory resolved it; the global ignore file remains unreadable.
  An attempted core.excludesFile=NUL was rejected by Git (exit 128 for
  that Git call); this option was abandoned, with no state changed.
- A targeted read named nonexistent src/ringmin/geometry.py; only that
  read failed. Production code is protected and is not an experiment input.
- No computation about roots has yet been launched in this task.

## 2026-09-05 01:51 - Bounded search completed

- Correction to the startup entry: src/ringmin/geometry.py does exist;
  the rg command had no matches there, not a missing file. The combined
  command's exit 1 was a no-match status. No required source is missing.
- Ran python ops/TASK-20260905__permuted_halves_root_search/search_roots.py,
  exit 0, all 32 permutations at m=2,3,4. At m=4 the unique numerical
  minimizer (8,7,5,6) improves the best shift (7,8,5,6) by about
  0.0157658012674. Stopped before m=5 as predeclared.
- m=2 ties exactly by symmetry; m=3 numerical winner (6,4,5) is a shift.
  Exact minimum-size exclusion and separator verification are next.

## 2026-09-05 01:58 - Independent run and local branch correction

- check_roots.py reproduced all 32 roots using independent 110-digit
  atan scoring/recursive enumeration, maximum midpoint discrepancy
  1.79291546936e-71. All three rational separator checks and four root
  brackets passed. The run then exited 1 on an incorrect added assertion
  that the left swap increment was entirely chain-active.
- Exact branch diagnostics show F_1(6,7) is chain and F_1(6,8) chord;
  the left increment is mixed, while the right increment is chain.
  The discarded chain-only explanation is not a theorem or evidence.
- Corrected the local audit to use the mixed/chain formula from the
  preceding note and a rigorous R-band enclosure at the shift root.
  Neither the exhaustive experiment nor its witness/root comparisons
  changed. Rerun required before completion.

## 2026-09-05 - Final verification and handoff

- Timing correction: the earlier 01:51 and 01:58 headings were unmeasured
  estimates, not clock evidence. A subsequent measured Get-Date returned
  2026-09-05 01:52:13 after both successful checker runs. The append order
  records the actual event order; no runtime claim uses those headings.
- Corrected check_roots.py exited 0. Added the five artifact-corruption
  rejection checks and a separate 110-digit all-pairs witness check,
  then reran the final checker: exit 0, all checks passed. Full material
  outputs and verification limits are in EVIDENCE.md.
- Created the proof note and updated only the owning fixed-order ledger,
  roadmap and current status. No larger m or asymptotic work was started.
- Inspected the complete tracked diff and all eight untracked files in
  full. Inline whitelist/text/import/provenance audit exited 0; exactly
  3 tracked modifications, 8 additions, empty staged diff, correct hashes
  and no protected changes. git diff --check exited 0, no output.
- State READY_FOR_REVIEW, pending independent human review. Exact finite
  certificates are distinguished from numerical root decimals and the
  imported fixed-order theorem. No production/global certificate or paper
  build was run, because those protected layers are unchanged.
- Manual commit suggestion: research: certify minimal cyclic-shift root counterexample
- Exactly one next atomic task: independently review the minimal root
  counterexample, including all 32 roots, rational separators, enumeration
  and smaller-size exclusion, the mixed/chain root swap and its fixed-order
  dependency; record acceptance or corrections without starting general
  permutation or asymptotic optimization.
