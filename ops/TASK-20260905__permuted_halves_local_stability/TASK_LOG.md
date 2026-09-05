# Task Log

Append entries; do not erase failed attempts or contradictory evidence.

## 2026-09-05 — Startup and analytic discriminator

- HEAD: 460d705ff349340975feb51ea886d7a0f1aab08c; clean working tree.
- Read AGENTS.md, PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, the pertinent
  fixed-order ledger, the shifted global coefficient entry, roadmap,
  the exact permuted criterion, adjacent-swap and root-counterexample
  notes, the shifted asymptotic proof, prior root dossier/checker,
  task templates, environment declarations, angular publication source
  and verifier interface. The open review protocol describes a different
  read-only review workflow; this user request is a local theorem task.
- Mode STRICT. Allowed and protected paths are in TASK_STATUS.md.
- Initial plain git status failed with dubious ownership. The transient
  safe.directory option restored read-only access. A trial
  core.excludesFile=NUL failed because Git rejects NUL as an exclude file;
  it was abandoned. Default status succeeds with permission warnings for
  the user's global ignore file. No configuration or Git state was written.
- Analytic candidate: each swap changes two monotone cell increments with
  opposite signs, giving a high-value-weighted score bound. Radial
  contraction transfers it to roots without differentiating a maximum.
- A further chord rectangle estimate suggests O(1/m) for the first swap
  of an interior shift, and O(m) is potentially sharp for arbitrary highs.
  The predeclared small diagnostic in TASK_STATUS.md will falsify these
  candidates if it finds a violation; no factorial enumeration is allowed.

## 2026-09-05 — Proof and local verification

- Added the analytic proof, including the weighted bound, a branch-safe
  radial contraction, uniform root brackets, cyclic and small-size cases.
- The separate upper radial rate and explicit high rectangle prove O(m)
  sharpness; a uniform m>=32 chord gate yields the O(1/m) interior-shift
  refinement. The best finite shift sequence gives a precise continuation
  of m=4, using the previously proved unique limit shift ratio.
- Ran `python -B ops/TASK-20260905__permuted_halves_local_stability/check_stability.py`:
  exit 0, all symbolic/rational gates passed, two prior m=4 brackets
  rechecked, 67 swaps and 201 score/contraction probes passed, 90 distinct
  diagnostic roots. The two special first-swap families at m=32,48,64
  passed the predeclared refinement and sharpness checks. Exact output
  and independence limits are retained in EVIDENCE.md.
- No factorial enumeration, prior certificate regeneration, production
  package import or Git/GitHub write occurred. No mathematical check failed.
- Updated the sole owning fixed-order ledger, current status and roadmap;
  the earlier counterexample/dependency reviews remain pending. Global
  bounds, published metadata, prior proof notes and certificates are intact.

## 2026-09-05 — Final file review

- A convenience attempt using PowerShell-interpolated safe.directory
  failed with Git's not-a-repository/usage output (exit 1 for the batch).
  Returned to the already working explicit per-command path; git diff
  then succeeded. No Git configuration or repository state was written.
- Read the complete tracked diff and every new file directly. Clarified
  explicitly that the lower-root derivation also bounds L_m itself.
- The inline Python file audit passed: 3 tracked and 5 untracked allowed
  files, explicit whitespace/EOF/conflict checks on all eight, 4 local
  Markdown links, both checker hashes and an empty staged diff. It invokes
  read-only Git with the root derived from Path.cwd(); git diff --check
  exited 0 with empty stdout. No protected or generated path changed.

## 2026-09-05 — Handoff

- State READY_FOR_REVIEW. Changed files: the new proof note, fixed-order
  ledger, roadmap, CURRENT_STATUS.md, and this dossier's status, log,
  evidence and checker. No protected/generated change; no Git writes.
- Residual limitation: independent human review, including imported
  mathematical dependencies, is pending. The diagnostics remain finite
  numerical observations; no global coefficient improvement is claimed.
- Exactly one next atomic task: independently review the uniform
  stability proof, linear sharpness and shift refinement, reproduce the
  bounded checker and audit the imported fixed-order/shift-limit results.
