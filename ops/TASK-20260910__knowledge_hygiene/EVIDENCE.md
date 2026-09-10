# Evidence

## Environment

```text
repository_head=ab6f663200f8d9eae95d30c6c96eb6c052aed881
platform=Windows / PowerShell
python=3.14.3
dependency_source=Python standard library and local Git; no installs
task_mode=STRICT
```

The user supplies the current HEAD as accepted input. The clean startup tree
was on `main`, tracking `origin/main` at the same SHA. Mathematical acceptance
is not independently inferred from the previous dossier or current status.
All checks in this dossier are local; hosted CI is not claimed.

## Exact file inventory

Modified:

1. `AGENTS.md` — section retrieval and cold dossier access only.
2. `PROJECT_KNOWLEDGE.md` — navigation rules only; definitions/index unchanged.
3. `CURRENT_STATUS.md` — this task, verification and one next atomic review.
4. `research/NEXT_RESEARCH_STEPS.md` — compact current roadmap.
5. `docs/post_arxiv_tasks.md` — historical authority notice only.
6. `SUBMISSION_CHECKLIST.md` — historical navigation notice only.
7. `SUBMISSION_REVIEW_REPORT.md` — historical navigation notice only.

Added:

8. `docs/archive/RESEARCH_ROADMAP_20260910.md` — full historical payload.
9. `ops/TASK-20260910__knowledge_hygiene/TASK_STATUS.md`.
10. `ops/TASK-20260910__knowledge_hygiene/TASK_LOG.md`.
11. `ops/TASK-20260910__knowledge_hygiene/EVIDENCE.md`.
12. `ops/TASK-20260910__knowledge_hygiene/check_hygiene.py`.

## Claim ledger and semantic crosswalk

All restructuring/preservation conclusions are **engineering facts**. The
mathematical classifications below are inherited summaries, not new claims.
Manual comparison used the baseline roadmap and only the relevant ledger
sections/source statements; the checker guards notation and exact preserved
passages but does not automate semantic judgment or prove mathematics.

| Item | Baseline meaning and current treatment | Controlling source / limitation |
|---|---|---|
| Finite scope | Computer-certified global optima for `3 <= n <= 14`; retained unchanged | `knowledge/CERTIFICATION.md`, Computer-certified finite results; artifacts and full verifier remain required |
| Formal seam and fixed-order feasibility | Resolved exact theory; summarized with link, never promoted to global floating behavior | `knowledge/FIXED_ORDER_THEORY.md`, Complete exact Supnick fixed-order feasibility classification; proof unchanged |
| Strongest lower endpoint | `C_term+eta_60`, non-strict liminf; retained in the same interval `[C_term+eta_60,C_3]` | Global-bounds ledger, Quantitative stability entry; `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md` Sections 8–9 |
| Lower constants/finite scope | `eta_60=D^2/(3600*pi)`, original exact integral and brackets, `n>=102` finite error and `n>=10^14` strict rational endpoint unchanged | Owning ledger and proof are protected; compact roadmap links them rather than copying constants/proof into another ledger |
| Strongest upper endpoint | Unqualified `C_3` remains exactly `C_3(1/1000)`; proved global limsup corollary | Global-bounds ledger, Three-block full-root transfer entry; `research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md` Section 7 |
| Earlier upper chain/diagnostic decimals | Still true at their original status, preserved in full archive and original owners; omitted from current orientation | No constants or older theorems modified; only strongest endpoint needed to choose work |
| Leading asymptotics | `R*(n)=Theta(n^2)`; normalized limit and endpoint sharpness unresolved; `1/8` disproved, floating set `o(n)` unproved | Baseline asymptotic-direction paragraph retained verbatim; global ledger Asymptotics/Primary open problems unchanged |
| Lower-method discriminators | Single-subset/one-level leading improvement closed; macroscopic/common-chain direction remains live | Relevant global-ledger sections; detailed resolved roadmap entries archived verbatim |
| Deletion estimate | Actual-tour square-root sharpness ruled out; improved exponent not asserted optimal; no new minimax/global coefficient | Common-chain Section 11 and sole global-ledger owner unchanged |
| Continuous widths | Mixed minimum below `C_3(1/250)` below `C_3(1/1000)`; no finite recovery/transfer at larger widths | Fixed-order ledger, Unique continuous mixed-width minimum; does not change global endpoint |
| First scientific priority | Section 11 independent review, identical audit scope/stopping rules | Verbatim paragraph except label `Exactly one next atomic task:` becomes `First scientific priority:` to avoid competing with CURRENT_STATUS |
| Broader direction | Review then refine two-level deletion before deciding on more coupling; further upper refinement deferred | Former Deferred priority 8 body retained verbatim; obsolete heading number removed |
| Deferred reviews | All scopes preserved; no acceptance/completion inferred, no new priority ranking | Compact dependency paragraph routes to specific archive scope, then existing source/ledger/dossier |
| Certification/extensions | Precise discriminator and feasibility estimate before n=15; extensions remain lower priority | Former Deferred priority 9 body retained verbatim with obsolete heading number removed; Lower-priority extensions section unchanged |

## Commands and checks

Run from repository root unless indicated. Git commands use command-local
`safe.directory` derived from the repository root (the exact invocation is
in `check_hygiene.py`); final checks also use `-c core.excludesFile=` to avoid
an unreadable user-global ignore file. No persistent configuration changed.

| Command/check | Exit/result | Property / limitation |
|---|---|---|
| `git status --short`, `git rev-parse HEAD`, `git log -6 --oneline`, `git remote -v`, `git branch -vv` with the safe-directory override | 0; clean, SHA above, `main` tracking `origin/main`, origin `https://github.com/falker47/ringmin.git` | Local baseline/branch only; not a hosted review decision |
| `python --version` | 0; `Python 3.14.3` | Actual local runtime |
| `python ops/TASK-20260910__knowledge_hygiene/check_hygiene.py` | 0; output excerpt below | Standalone text/blob/link audit; no production imports or mathematical checking |
| `git diff --check` and `git diff --cached --check` with command-local overrides | 0; no output, including populated 12-path index | Changed tracked/staged whitespace; script separately checks additions |
| `git diff --cached --stat`, `git status --short` | 0; exactly the 12 listed task paths staged | Integration scope; no unrelated file staged |
| Python comparison of `git show :path` against each inspected working file for all paths from `git diff --cached --name-only`; complete `git diff --cached --no-ext-diff --no-textconv --no-renames` read | 0; all 12 staged blobs identical to inspected files; 12 diff entries | Staged-file/content coverage; original roadmap/archive covered by the separate exact payload check |

Material local checker output (the exact 12-path listing is the inventory above):

```text
PASS archive: 62810 bytes, 1339 lines, 86 sections; SHA-256=c1eb563ab3d6ea871ed61f01ed68c66b003634a7f1a92ed2badd5e979d595802
PASS priorities: review and deferred bodies (labels only), asymptotic direction, certification prerequisite and extensions preserved
PASS bound/scope markers; mathematical authority is preserved sources
PASS historical bodies: 3 unchanged; only authority/navigation wrappers edited
PASS inventory: 7 modified + 5 added; 450 protected baseline blobs unchanged
PASS navigation: 33 local links/anchors and authority policy markers
PASS whitespace: explicit additions/rewrites plus unstaged and staged Git checks
ROADMAP 1339->102 lines; 62810->6690 bytes; line reduction=92.38%
```

The four routine orientation files (`AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
`CURRENT_STATUS.md`, roadmap) fell from 1,888 to 637 lines (66.26% reduction).
Their final size is also printed by the checker;
the archival payload and dossier are deliberately outside this working set.

## Archive provenance and completeness

- Source: Git blob `ab6f663200f8d9eae95d30c6c96eb6c052aed881:research/NEXT_RESEARCH_STEPS.md`.
- Payload: 62,810 bytes, 1,339 lines; no excerpts were discarded.
- SHA-256: `c1eb563ab3d6ea871ed61f01ed68c66b003634a7f1a92ed2badd5e979d595802`.
- Creation: Python `subprocess.check_output` of `git show` above, prepended
  historical navigation/source/hash notice, enclosed the original bytes in a
  four-backtick Markdown fence between explicit BEGIN/END markers. No external
  input, computation, randomness, publication asset or certificate generation.
- Independent preservation check: `check_hygiene.py` re-reads the source Git
  blob and extracts the marked payload, requires exact equality and every
  original level-two section, including current passages retained in both.
  Checkout CRLF normalization is explicit. Original path references inside
  the inert payload remain repository-root-relative.
- The payload's old authority wording/review requests are quoted historical
  text; the wrapper expressly denies current priority/status authority.

## Navigation inventory and authority audit

Inspected root/docs names, headings and navigation wording. Only
`research/NEXT_RESEARCH_STEPS.md` ranks current scientific priorities;
`CURRENT_STATUS.md` alone owns current task state. The roadmap calls its
review a scientific priority; the current-status next task is the independent
review of this documentation change. The index routes to thematic owners.

| Record | Decision |
|---|---|
| `docs/post_arxiv_tasks.md` | Add historical notice; preserve entire original body and publication details |
| `SUBMISSION_CHECKLIST.md` | Already archived; replace its misleading current-follow-up pointer in the notice only |
| `SUBMISSION_REVIEW_REPORT.md` | Historical notice now also covers later post-arXiv update, removing its misleading current-status pointer |
| `docs/release_notes_arxiv_v1.md` | Already explicitly records arXiv-v1 repository state; unchanged |
| `docs/math_stackexchange_answer_draft.md` | Explicit draft, no current roadmap/status claim; unchanged |
| `ENDORSEMENT_SUMMARY.md`, `endorsement/email_templates.md` | Already archived pre-publication records; unchanged |
| `README.md` | Public reproduction overview already points to compact index for current post-v1 knowledge; unchanged |
| `REPORT.md` | Derived certified-result report, not roadmap/status; protected and unchanged |
| `SPIEGAMI.md` | Explanatory paper guide, not current task list; unchanged |
| `RINGMIN_REVIEW_PROTOCOL.md` | Existing review procedure, not a current status/roadmap. Specific changed/latest dossier review remains compatible with cold access; unchanged |

Detailed history is available by deliberate archive/source retrieval. No new
global summary or thematic ledger is created. `ops/TASK-*` remain audit
records; filename/hash enumeration for preservation is not content loading
for orientation. Link validation is local, including new heading anchors;
historical literal payload paths and external URLs are not reinterpreted.

## Ledger growth concern (unranked)

No ledger is split or edited. At startup the two large ledgers contain
1,812 lines (`FIXED_ORDER_THEORY.md`, 80,936 checkout bytes) and 915 lines
(`GLOBAL_BOUNDS_ASYMPTOTICS.md`, 39,056 checkout bytes). The other ledgers
contain 27–40 lines. This is a future retrieval-maintenance concern if
section-level lookup becomes insufficient, not another task begun here.
Size is measured mechanically, without loading full ledgers for orientation.

## Failed checks and negative evidence

- Plain Git startup commands: exit 128 per Git command due to sandbox
  ownership; resolved by command-local safe-directory override.
- Template reads with missing `_TEMPLATE` suffix: paths absent; corrected to
  actual tracked template names before dossier creation.
- Optional `gh` executable discovery: not installed; not needed for this task.
- An initial combined read was truncated; relevant ranges were read in
  bounded follow-ups. No missing source became a premise.
- A patch combining deletion and addition of CURRENT_STATUS in one operation
  was rejected before applying; retried as a direct rewrite and a separate
  patch. No partial changes from the rejected operation.
- Initial checker: exit 1, `scientific review scope changed`. Comparison
  exposed one extra blank separator after retained sections, not a changed
  review instruction. Removed the extra separators; exact body check passes.
- `git status --short` with `core.excludesFile=NUL` failed with `fatal: cannot
  use NUL as an exclude file`. An empty command-local `core.excludesFile=`
  value fixes status and is used by the final checker; no global ignore
  configuration was edited.
- Initial `git add` in the filesystem sandbox failed with `index.lock:
  Permission denied`. The same exact 12-path staging command succeeded with
  tool-enforced escalation under the user's standing integration authorization.

## Final diff inspection

Complete working diff inspected: all seven modified documents and all new
dossier/checker text read; archive wrapper read directly and the entire
payload compared exactly to its original Git blob. Explicit whitespace
checking includes all five additions. No protected/generated file changed.
`git status --short` lists exactly the seven modifications and two new
directories whose five files are enumerated by the checker. The populated
index contains only those 12 paths. Full staged diff/content inspection and
`git diff --cached --check` passed; the checker passed again against that
index. Final dossier-record edits receive the same staged equality and
whitespace checks before commit. Final handoff reports commit/push results.

Protected-source comparisons cover
every baseline tracked file outside the seven allowed modifications, including
all mathematical/proof/certification/production/publication sources and prior
dossiers/checkers. The three edited historical bodies are checked separately.
The entire archive payload is inspected by exact equality to the original;
its new wrapper and all new dossier/checker text receive direct review.

## Residual uncertainty

This task checks preservation and navigation, not the truth of inherited
mathematics. No pytest, certificate verifier, numerical experiment, paper
build, external URL check or hosted CI inspection is needed/run for this
documentation-only delta. External independent review remains separate.
Ignored local progress logs and other untracked historical evidence are not
regenerated, moved or deleted; the tracked-source audit does not recertify them.
