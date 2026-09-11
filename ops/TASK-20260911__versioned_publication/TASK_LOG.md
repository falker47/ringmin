# Task Log

## 2026-09-11 — Versioned publication and surviving dependencies

- Core theorem/general transfer integrated as 13ddb411; reproduction gate
  integrated and pushed as df9c4f8. Complete final lower, upper and fixed-order
  source chains independently audited internally with exact controls.
- Created a new v2 manuscript. Separate reviewers inspected the global,
  upper and lower/fixed sections and reported local definition/wording fixes.
- Corrected B from minimum/least to infimum circumference for degenerate
  marks in both new proof and manuscript; explicitly defined type normalization,
  lower optimizer symbols and domain, C3/C4 and exact endpoint/exit wording.
  No theorem scope or coefficient changed. Reviewers rechecked all corrections.
- Initial sandboxed TinyTeX invocation failed to read its runtime outside the
  workspace. Authorized escalation allowed the build. A direct relative
  output argument was parsed incorrectly; the explicit subprocess argument
  list and absolute build path solved it without modifying the installation.
- Initial two-pass PDF exposed an overlong bibliography path. The builder
  rejected that output, wrapped source paths, selected scalable Latin Modern
  fonts, then rebuilt with no overflow or unresolved-reference warning.
- Rendered all nine pages with Poppler at 110 dpi and visually inspected every
  page, including displayed equations, threshold table and source references.
- Added final claim matrix, exact command index and one external review packet;
  no external state write, publication, tag, release or unrelated search.

## 2026-09-11 — Final publication gate

- Added PDF title/author metadata and AI-assistance disclosure. Final two-pass
  build and one unchanged repeat both produced the identical SHA-256 recorded
  in EVIDENCE.md. Re-rendered all pages; pages1-7 were byte-identical to the
  inspected images, and final pages8-9 were inspected again.
- The raw-Git comparison of the clean-export manifest initially failed on
  Git's Windows line-ending conversion; explicitly normalized text only and
  verified all546 hashes, with522 CRLF/LF-only text differences. No source
  content difference was found.
- Final source manifest, link/whitespace/protected-path checks and exact staged
  comparison complete the packet before the authorized final commit/push.
