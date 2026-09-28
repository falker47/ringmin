# Task Log

## 2026-09-28 — Startup and explicit exception

- Local HEAD, cached origin/main, live remote HEAD/main and Registry
  State!A1:F2 all resolve to `6749d6b165f982136117481be322c8beaec223ce`.
  Registry status accepted, updated 2026-09-28T09:15:13Z; no Registry write.
- Initial Git reads required the per-command safe.directory option. The first
  live remote read failed in the network sandbox; authorized retry succeeded.
- Stopped before editing on the sole untracked arXiv ZIP. The user explicitly
  authorized preserving and excluding exactly that file for this task.
  Its SHA-256 matched the previous task's recorded bytes.
- Read AGENTS.md, PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, relevant publication
  ledger/roadmap sections, accepted manuscript/build sources, prior audit,
  source map, and task templates. Mode STRICT; scope recorded in TASK_STATUS.
- Existing submission-compliance checker exited 0 before any task changes.
  Its report-binding check reads inherited mathematical verification evidence;
  it does not execute a fresh global certificate verification.
- Captured raw-byte hashes of all tracked files plus the exempt ZIP before
  protected-path edits, under ignored reproducibility/.work/.

## 2026-09-28 — Live instructions and package preparation

- Rechecked live DCG guidelines: existing LaTeX template remains permitted.
  The editorial-board page additionally lists Csaba D. Tóth. The retrieved
  Editorial Manager landing page displays a development warning; preserved
  as a human-upload condition, without claiming a policy change.
- A Windows rg wildcard form failed; the directory plus `-g '*.tex'` retry
  found exactly three local inputs. A web click with an unresolved reference
  failed; retry from the fetched guideline page reached the journal portal.
- Sandboxed pdflatex --version failed on the host profile path; authorized
  retry returned pdfTeX 1.40.28, TeX Live 2025. No source change was needed.
- Prepared the cover letter and checklist without private portal-only data.
  The manuscript's accepted provenance language is preserved verbatim.

## 2026-09-28 — Compilation, integrity and visual verification

- The PDF skill's artifact-operation marker completed successfully once.
- `python ops/TASK-20260928__dcg_submission_package/package_submission.py --build`
  exited 0 with PASS_PACKAGE. Two fresh external temporary directories each
  received only the four TeX ZIP entries and ran two TeX passes. All four
  exit codes were 0. Both final PDFs equal the accepted PDF byte for byte:
  19 pages, zero unresolved references/overfull boxes, no repository input.
- `pdfinfo` confirmed 19 A4 pages, 402481 bytes, PDF 1.7. `pdftoppm -r 60`
  rendered all 19 pages; all five contact sheets were visually inspected.
  Tables, declarations, mathematical displays and references showed no clipping
  or overlap. The PDF skill was used for rendering and visual verification.
- Re-ran the packaging checker after strengthening report/serialization checks:
  PASS_PACKAGE; all 10 checksum entries, 5 accepted manuscript files and
  740 protected files verified, including the exempt ZIP.
- Full no-index comparisons of all four copied TeX files and the PDF against
  accepted working sources each exited 0 with no diff. Complete status/roadmap
  diff and authored package/dossier files were inspected. `git diff --check`
  exited 0. Direct UTF-8/whitespace validation includes untracked additions.
- One combined patch was rejected for targeting CURRENT_STATUS.md twice;
  no change from that rejected patch applied. Corrected scoped edits succeeded.
- Final Registry reread still returned the same accepted baseline, status and
  update time. No Registry mutation was performed.

## 2026-09-28 — Review handoff

- Local state READY_FOR_REVIEW. Only the new package, task dossier, current
  status and finite-submission roadmap priority are in scope for staging.
- No mathematical source, certificate, scientific code, original journal input,
  publication artifact, protected ZIP, thematic ledger or canonical index changed.
- Scoped staged inspection, commit, push and remote verification follow the
  local gates; their exact commit/result are reported in the final response.
- Staged exactly the 21 inspected files. All staged blobs matched their
  reviewed working-file bytes; no unstaged tracked delta remained. Staged
  whitespace checks passed and the exempt ZIP was absent from the index.
  Git's automatic PDF text converter emitted missing-tool warnings while
  producing a diff; raw blob checks remained valid, and final diff inspection
  uses `--no-textconv --no-ext-diff` to bypass that display-only converter.
- Exactly one next atomic task: independent review of the exact committed
  submission package; if accepted, human upload through Editorial Manager.
