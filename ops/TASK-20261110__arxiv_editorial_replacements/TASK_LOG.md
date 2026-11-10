# Task log

## 2026-11-10 — Baseline and scope

- STRICT, editorial replacements of the two existing arXiv records. The existing
  main checkout contains the pre-existing untracked finite-v2 ZIP. Left it in
  place (SHA-256 `e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`).
- The clean dedicated worktree started at editorial commit
  `4b3721df8061f1992cfd242df69b1a0643216d8f`. Normal branch creation; no
  merge from main or draft PR #4 (head `7d257221d9034ca5f895f062e45e782d8e77b6c2`).
  Live main: `c26400b328c2f8fa338b588e61abb98266a265f9`.
- The web cache missed the versioned records. Direct official HTTPS served
  the public TeX archives, PDFs and abstract records. Compared the November 9
  preparation packages and the November 10 unsubmitted Paper II candidate.
  The large ZIPs exceeded a local transfer helper's size limit; comparing
  archive members directly avoided requiring that transfer.
- Before the editorial changes the authenticated arXiv account showed both
  owned articles and no pending submission. Last public versions: I v3,
  II v2. The weekly replacement guidance applies to submission timing.

## 2026-11-10 — Build, verification and handoff

- Built Paper I and Paper II twice each from fresh extractions; inspected the
  rendered pages. Final previews: 18 and 9 pages. The revised Paper I
  declarations and provenance no longer repeat the bibliographic and
  archival identifiers. Paper II preserves the four supplement payloads.
- Rebuilt both ZIPs and PDFs once more by independent replay; all four
  compared byte for byte. Replayed the Paper I verifier from the full
  pinned commit after identifying a missing manifest in a partial export.
  Exercised both printed Paper II commands in the frozen companion.
- Inspected every changed public-source hunk and verified all conserved
  members. Draft PR #4, main, the existing journal packages and the
  scientific baseline are outside the integration.
- Candidate state: READY_FOR_REVIEW. Submission of both versions remains
  a separate step at the weekly checkpoint; see TASK_STATUS.md.
