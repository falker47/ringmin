# Task Log

Append-only chronology.

## 2026-09-08 — Startup and discovery

- Read the operating contract, index, status, pertinent definitions and
  lower-bound/chain ledgers, finite subset proof, roadmap and templates.
- Clean main at 3c415b36ade354cfd9beff637ec98bb5cc6b7d0a; origin/main agrees.
  Initial unqualified Git status/log hit dubious ownership. Command-local
  safe.directory resolved it without configuration changes; Git also warns
  that the sandbox cannot read the user's global ignore file.
- Mode STRICT; eight-path expected delta and protected paths in TASK_STATUS.
- Falsifiable discriminator: a larger chain minimizer may restrict to a
  nonminimal smaller cycle, but strict minimax separation additionally needs
  that restriction to exceed the larger of the two independent minima.
- Bounded discovery: standalone Python math/bisection, n=4..9, only the
  two Supnick cycles and deletion of the minimum; seven insertion checks
  at n=8. No permutation enumeration, seeds or production imports.
  Candidate: n=M=8,N=7; roots approximately 5.756031086142491 (larger),
  5.726997793763834 (smaller), 5.7982214430237615 (induced larger tour).
  These floats discover the candidate and are not proof premises.
- Read the exact radius-1 seam and general Supnick triangle/path proofs.
  Verified the matrix-level Supnick max-tour premise in the cited survey,
  Section 2.2.3, p.507, and Proposition 2.13, p.508 (publisher pagination),
  via https://pure.tue.nl/ws/files/2373438/Metis148543.pdf.
- Proof plan: quantitative strict anti-Monge perturbation excludes every
  different larger tour at once; a rational gate excludes its own induced
  cycle. Smaller n will be excluded analytically using triangle defects.

## 2026-09-08 — Exact arithmetic implementation

- First checker run exited 1: the draft aggregate interval for the first
  closure sum was incorrect. No mathematical gate was accepted from it.
- Evaluated the four fixed rational polynomial expressions to set their
  displayed outward bounds, then corrected all four draft table rows.
  This is arithmetic evaluation at fixed endpoints, not a radius search.

## 2026-09-08 — Proper-outer-subset interpretation

- The user's subset symbol may require T_M to be proper in {1,...,n}.
  Cover this interpretation within the same compatibility question.
- One additional fixed candidate, n=13,M=12,N=11, was checked by the
  same standalone math bisection: larger root 18.277543500174055,
  smaller root 18.204735279026984, restricted root 18.39876464468486.
  These are discovery diagnostics only. The same analytic perturbation
  will give separation >1/5000; four further rational gates suffice.
- The fixed-k note's radius-2 corollary and its linked exact endpoint
  proof exclude all smaller n under the proper-outer-set convention.
- A documentation patch was rejected before writing because it used
  both Delete and Add for CURRENT_STATUS in one patch. No partial changes
  resulted; the same intended scoped edits were then applied correctly.

## 2026-09-09 — Verification and handoff preparation

- Exact checker exits 0 for eight fixed rational gates via two formulas,
  pi, rank edges, cyclic deletion and both explicit separation constants.
- Fresh radius-1/radius-2 check_exact_bridges calls each pass; no numeric
  scan. Independent SymPy mixed and radial derivative identities pass.
- Read-only guessed dependency filename/wildcard failed; actual paths
  were discovered and read. No source changes resulted.
- Completed analytic all-tour proof and minimality under both outer-set
  conventions. Read the new proof/checker fully and the entire tracked
  diff; checked all source links and owning ledger.
- Source/protected-path audit exits 0: exactly eight allowed paths,
  explicit tracked/untracked whitespace, all eight table transcriptions,
  sole ledger owner and eight imported texts equal baseline. Every other
  tracked path is unchanged. git diff --check exits 0 with no output.
- Current status and roadmap move the scientific direction to coupled
  lower bounds. Third-block refinement/transfer remains deferred.
- Final state for integration: READY_FOR_REVIEW; independent acceptance
  remains separate. Exactly one next atomic task: independent review of
  this theorem, including both inclusion conventions and rational gates.
  Authorized stage/commit/normal push follows the final staged inspection;
  actual SHA, push and tree result will be given in the handoff.

## 2026-09-09 — Staged verification

- Sandbox git add could not create .git/index.lock (exit 1). The same
  explicit eight-path staging command succeeded with authorized tool
  escalation (exit 0); automatic approval review did not reject it.
- Complete staged diff inspected, including the separately read middle
  section after output truncation. git diff --cached --check and
  git diff --exit-code each exit 0. The staged change has eight paths.
- This final log/evidence update is inspected and restaged before commit;
  proof/checker hashes and mathematical claims are unchanged.
