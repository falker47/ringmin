# Task Log

## 2026-09-05 00:44 — Startup and predeclared experiment

- HEAD: 6bc4ac31b96ffcccb8fcfacf7478ae148a82bb2e; working tree clean.
- Read applicable AGENTS.md, index/status, definitions, fixed-order entries,
  shifted and unshifted proofs, prior shifted dossier/checker, roadmap,
  relevant global lower-bound/disproved-claim entries, angular model in
  the paper, geometry/evaluator and independent verifier model sections,
  environment declarations and task templates.
- Google Drive read of Review State Registry reports the same SHA for
  ringmin, baseline_status=accepted, updated_at_utc=2026-09-04T22:40:04Z.
  No registry mutation or external review decision is part of this task.
- Plain Git reads initially failed ownership checks. Command-local
  safe.directory resolved them; empty core.excludesFile avoids unreadable
  user ignore-file warnings. No configuration was written.
- Mode STRICT. Delta and protected paths are in TASK_STATUS.md.
- Before any new proof, fixed the finite experiment, discriminator, bounds,
  tolerances, stopping rule and no-RNG policy in TASK_STATUS.md and the
  checker. New proof and ledger integration await its outcome.

## 2026-09-05 00:48 — Pre-proof falsification outcome

- Ran python -u ops/TASK-20260905__permuted_alternating_halves/check_falsification.py.
- Exit 0: 872 permutations, 6104 independent LP probes, no discrepancy.
  The minimum absolute cell margin was 2.27313241e-05, outside the
  predeclared 1e-7 band. Complete stdout is preserved in EVIDENCE.md.
- Only after this run, proceed to the proof. Inspection of the shifted
  argument identifies its permutation-free shell triangle lemma as the
  candidate mechanism; no counterexample is inferred from floating noise.
- Additional post-proof verification is bounded in advance: exact shell
  polynomial/sign gates; 70-digit roots with 180 bisections for all
  permutations at m=2..5 and five specified m=6 orders; every directed
  angular path and independent Cartesian distances, three cell splits at
  the root, unclosed base paths at root/10, positive extra slack at 2*root,
  and rotations/reflections. Guards and exact case list are in the retained
  checker. These tests corroborate the proof, without enlarging its scope.

## 2026-09-05 00:54 — Proof, verification and durable integration

- Completed the exact proof with a strict shell triangle lemma valid for
  arbitrary high paths. Both directions for HH/LH/LL, all six m=2 pairs,
  m=3, arbitrary descents/jumps and the low seam are explicit.
- The stronger local description follows from the same proof: all feasible
  gaps satisfy exactly the cell constraints plus closure. Derived only the
  unique root, optimal gap parametrization and chain/full equality test.
- check_witness.py exited 0: exact shell gates; 107388 finite directed
  path decompositions; 157 high-precision roots, 1303 path audits and
  1146 Cartesian audits. Both residual minima exceed the -1e-55 guard.
- Integrated the theorem in its sole fixed-order ledger. Updated roadmap
  priority and explicitly stated that 1/8 is disproved, linking the global
  owner. CURRENT_STATUS.md now refers to this task. Protected global ledger,
  index, previous proofs, paper and code remain untouched.
- Inspected the full tracked diff: exactly the expected three files.
  Recorded both checker hashes. Full untracked review and final scope/
  whitespace audit follow; no asymptotic optimization has been started.

## 2026-09-05 — Final review and handoff

- Read the proof, both checkers and all dossier additions in full. Reviewed
  the complete tracked diff. No missing pair direction, low seam, arbitrary
  high jump or small-cycle case was found. No shift-specific asymptotic
  premise was imported into the theorem.
- Scope/whitespace audit exited 0: exactly 3 tracked and 6 new authorized
  files; no staged/protected/generated changes; explicit UTF-8, final
  newline and trailing-whitespace checks over all 9 files. git diff --check
  exited 0 with no output. The same audit is repeated after these final
  dossier/status edits, which are also read back.
- Changed the diagnostic summary to say three tested splits, matching the
  finite check; the exact theorem still covers all allowed split choices.
- State READY_FOR_REVIEW; suggested manual commit is recorded in status.
  No Git history or GitHub/registry state was written.
- Residual limitation: independent human proof review; finite numerical
  corroboration is not an interval or global certificate. Existing global
  bounds and certified scope remain unchanged.
- Exactly one next atomic task: independently review the arbitrary-P
  fixed-order criterion, both paths and wraps, small cases and immediate
  corollaries, reproduce its bounded checks and record acceptance or precise
  corrections. Permutation asymptotics are not started in this task.
