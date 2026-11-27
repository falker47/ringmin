# Task Log

Append entries; do not erase failed attempts or contradictory evidence.

## 2026-11-24 — Startup

- repository HEAD: `main` at `c26400b`, clean tree.
- heads examined: `review/p1-square-radii` at `91ce1cb` (Draft PR #21); `review/p2-square-radius-project` at `51dfc1b` (Draft PR #22), confirmed with `git ls-remote`.
- observation: the checkout fetches only `main` (`remote.origin.fetch`), so the local ref `origin/review/p2-square-radius-project` was stale at `8730b6f`, a commit replaced by a force-push. Both review branches were fetched explicitly. No remote configuration was changed.
- working trees: two linked worktrees under the ignored directory `reproducibility/.work/`, on new branches `fable/proofcheck-p1` and `fable/proofcheck-p2`.
- files read: `AGENTS.md`, `CURRENT_STATUS.md`, both manuscripts in full, the earlier referee report `docs/referee/p2-sidma-referee-2026-11.md` (Paper II branch) for context.
- task mode: STRICT (mathematical claims).
- expected delta: new report, new checking code, this dossier, `CURRENT_STATUS.md`.
- known risks: a finite check mistaken for a proof; a checker that cannot fail.

## 2026-11-24 — Paper I, analysis by hand

- action: each statement was read without its proof, a proof was reconstructed, and the two were compared.
- result: Lemma 2.1, Lemma 3.1, Theorem 3.2, Theorem 5.1 with Appendix A, Sections 6.1–6.5, Appendices B and C agree with the reconstructions.
- result: the imported tour theorem was re-proved by cut counting, so Theorem 3.2 no longer depends on the citation.
- result: growth of the chain root also follows from deleting the largest label and Theorem 3.2; the paper's Lemma A.1 avoids that premise and is correct as printed.
- claim status: no error, no gap; three imprecisions and three style remarks.

## 2026-11-24 — Paper I, machine checks

- action: wrote `p1_*.py` (kernel, Supnick tour, seam, bridges, cosine arithmetic, coverage, controls).
- result: 40 checks and 6 negative controls pass.
- result: a fresh lower exclusion from the printed endpoints reproduces Table 3 exactly and excludes every order again at `L_n + eps_n`.

## 2026-11-24 — Paper II, analysis by hand

- action: same method on Sections SM1–SM11 of S1.
- result: L1–L8 and the limit-existence argument agree with the reconstructions; the constants 43, 54, 5, 19/2, 16 and 432 were rederived.
- claim status: no error, no gap; one imprecision and two style remarks.

## 2026-11-24 — Paper II, machine checks

- action: wrote `p2_*.py` (geometry and terminal parameters, energy and deletion, minimax and width optimum, controls).
- result: 20 checks and 8 negative controls pass.
- failed attempts, all defects of the new checker and not of the manuscript:
  - `need()` rejected a sympy relational (`sympy.true` is not Python `True`); fixed with `bool()`.
  - two sympy identities were not simplified because `s - x > 0` was unknown to sympy; fixed by substituting `s = x + w` with `w > 0`.
  - `arb ** int` returns NaN at an exact zero base, which made `G(a)` NaN; fixed with explicit products.
  - an index error in the generator of crossing instances.
  - my own tolerance `1e-37` on the width of the series enclosure was too strict; the 80-term tail bound is about `1e-33`, consistent with the 30-place rounding stated in Section SM9.2.
- interpretation: none of these touched a manuscript claim. After the fixes every affected check passes.

## 2026-11-24 — Verification

- command: `python -I -B independent_check/fable_proofcheck` on `fable/proofcheck-p1`: `46 items, 0 failures`, exit 0.
- command: `python -I -B independent_check/fable_proofcheck` on `fable/proofcheck-p2`: `28 items, 0 failures`, exit 0.
- command: `python -m pytest independent_check/fable_proofcheck -q` on both branches: all passed.
- command: `python -m pytest` (existing suite) on both branches: see EVIDENCE.
- limitation: local runs only; no hosted CI is asserted.

## 2026-11-24 — Verification after the commits

- command: the existing suite on the committed state of both branches, several full runs.
- result: `fable/proofcheck-p1` `101 passed`. `fable/proofcheck-p2` `110 passed, 1 skipped` in six runs, and 13 and 12 transient `OSError` failures in `tests/test_line_upper.py` in two runs.
- interpretation: intermittent, not reproduced on demand, in tests that do not touch the new files. Recorded in EVIDENCE with its limits; cause not established.
- command: `python -I -B independent_check/fable_proofcheck` on the committed state: `46 items, 0 failures` and `28 items, 0 failures`.

## 2026-11-24 — Handoff

- final state: READY_FOR_REVIEW.
- files changed: new files under `docs/referee/`, `independent_check/fable_proofcheck/`, `ops/TASK-20261124__fable_proofcheck/`; `CURRENT_STATUS.md`.
- unresolved items: none blocking; the not-verified list is in the report.
- exactly one next atomic task: the author decides whether to apply the suggested wording for the four imprecisions.

## 2026-11-24 — Wording applied after the author's approval

- decision: the author answered “Sì, applicale” to the question whether to apply the four suggested rewordings in separate commits.
- preflight: in this environment `build.py` reproduced the three tracked PDFs byte for byte before any edit (Paper I `main.pdf`; Paper II `main.pdf` and `supplement.pdf`).
- action, Paper I: three commits, one per finding. Each changes `main.tex`, adds the replacement to `EDITORIAL` in `tests/test_journal_p1_jogo.py`, updates the character count, digest and table in `MATH_DIFF.md`, and rebuilds `main.pdf`.
- action, Paper II: one commit. It changes one sentence of the proof of Lemma SM5.1 in `supplement.tex`, adds that replacement to `tests/test_journal_p2_sidma.py`, notes it in `MATH_DIFF.md`, and rebuilds `supplement.pdf`. The article PDF came out byte-identical and is not part of the commit.
- not done: no theorem number was added to the survey citation, since no source was consulted. The frozen S1 bundle, `s1_support.zip` and `paper_assets/asymptotic_sequel/proposition7_supplement/` were not touched. The five style remarks were not applied.
- claim status: wording only. Theorem 3.2 now states the hypothesis `N >= 3`, which the definition of the chain radius already required.

## 2026-11-24 — Verification after the wording commits

- `python -m pytest tests/test_journal_p1_jogo.py`: `7 passed` after each of the three commits; `python -m pytest tests/test_journal_p2_sidma.py`: `7 passed`.
- `python -I -B independent_check/p2` (pre-existing checker, Paper II branch): `130 passed, 0 failed`.
- `python -I -B independent_check/fable_proofcheck`: `46 items, 0 failures` (Paper I) and `28 items, 0 failures` (Paper II).
- full existing suite: Paper I branch `two runs: 1 failed, 100 passed (the intermittent generator test again), then 101 passed`; Paper II branch `110 passed, 1 skipped`.

## 2026-11-24 — Second handoff

- final state: READY_FOR_REVIEW.
- exactly one next atomic task: the author reviews the four wording commits in Draft PRs #23 and #24.

## 2026-11-27 — Precision made local to each check

- trigger: while PRs #24 and #27 were merged, `P2-L3a` and `P2-L2b` failed when `tests/test_line_upper.py` and this package ran in one pytest process. `fable_common.py` set `ctx.prec = 256` once, at import; `paper_assets/line_upper/block_antiderivatives.py` later sets 192 bits, and an undecided Arb comparison counts as a failure. Alone, and with the documented command, every check passed.
- decision: the author answered “Sì, correggila” to the question whether to fix it.
- action: `fable_common.py` no longer sets the global precision. `working_precision()` gives 256 bits inside a context and restores the caller's value on exit. Every registered check and control runs inside it, and both loaders (`__main__.py`, `test_proofcheck.py`) import the check modules inside it, which covers the module-level constants of `p2_base.py`. The new test `test_check_ignores_caller_precision` runs every check with the caller's precision at 53 bits and requires that precision unchanged afterwards. The three shared files remain identical on both lines.
- not changed: no check module, manuscript, certificate, result artifact or production code.
- claim status: unchanged. Every check and control is evaluated at 256 bits, as before.
- verification: see “Commands after the precision fix” in EVIDENCE.
