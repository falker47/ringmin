# Task Log

## 2026-09-11 — Exact preservation

- Mathematical checkpoint 13ddb41180b3911940f4fe5cf7d61c0545f9f834 committed
  and pushed normally; local origin/main matched and tree was clean.
- Read actual ignored progress logs and verifier's prefix-completion reader.
- Captured 12 original logs (9649682 bytes) as deterministic gzip evidence
  and manifest (710353 bytes total), with original and archive SHA-256.
- Initial new pytest invocation failed at fixture setup: default temp directory
  ownership denied access before tests ran. Existing cache also denied writes.
  Task-local base temp and disabled cache selected; no test weakened.
- Initial PowerShell glob passed literally to rg; corrected with rg's -g flag.
  No machine paths or credentials found in preserved log content.

## 2026-09-11 — Failure controls and clean reproduction

- Explicit temp retry first needed its parent directory created. The next
  attempt exposed recursive fixture copying (two fail, one pass); narrowed
  source to frontier_logs, removed the checked task-owned failed fixture,
  and obtained three passing tests. No check was weakened.
- Internal review independently found the copy problem and hardcoded capture
  runtime metadata; corrected both, preserving compressed log bytes. Refreshed
  the not-yet-committed manifest generator hash and repeated capture successfully.
- Reviewer found drive-qualified path aliasing. Added PureWindowsPath drive
  rejection and all three regression controls; parent and reviewer tests pass.
- Clean tracked-source export plus explicit delta started without ignored logs,
  restored archives, then passed 15 tests, smoke, full 3..14 and all six new
  checker normal/optimized invocations. Exact manifest and output preserved.
- Independent implementation review finalized INTERNALLY_VALIDATED. Canonical
  implementation/certification entries and reproduction README updated.
- Complete additions, original-byte/archive hashes and staged delta are checked
  before integration; external review remains a separate final-goal obligation.
