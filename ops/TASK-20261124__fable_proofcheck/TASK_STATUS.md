# Task Status

```text
task=TASK-20261124__fable_proofcheck
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-24
updated_at=2026-11-24
```

This dossier is identical on `fable/proofcheck-p1` and `fable/proofcheck-p2`.

## Objective

Independent, referee-style verification of the mathematics that earlier
passes had not examined: Paper I from the angular reformulation to the seam
criterion and its appendices, and lemmas L1–L8 of the lower bound for
consecutive radii in supplement S1 of Paper II. Deliver a report, isolated
checking code with one documented command, and corrections for errors or
gaps only.

## Scientific or engineering question

For each statement in scope: are the hypotheses sufficient and is the
printed proof correct and complete? Each answer is classified as verified by
machine, verified by hand, or not verified. Finite machine checks support,
and never replace, a proof of a statement quantified over all `n`.

## In scope

- `paper_assets/journal_p1_jogo/main.tex` at `91ce1cbf42543b6bcaea8ac94688c34d29066087`, Sections 2–6, Theorem 7.1 as far as it follows from them, Appendices A–C (read only);
- `paper_assets/journal_p2_sidma/supplement.tex` at `51dfc1b8c9ba02faa665cb20f60ce2d87f761c00`, Sections SM1–SM11 (read only);
- new files `docs/referee/proofcheck-2026-11.md`, `independent_check/fable_proofcheck/`, this dossier;
- `CURRENT_STATUS.md`.

## Out of scope

- certificate files, their verifiers and the upper witnesses for `n >= 8`;
- square-radius results of both papers;
- the upper bounds and the law theorem of Paper II;
- style of the manuscripts;
- CI workflows and `requirements.txt`.

## Expected delta

New files, plus `CURRENT_STATUS.md`. The check changed no manuscript: a
manuscript would change only for an ERROR or a GAP, and none was found.
After the author's approval on 2026-11-24, four wording changes were applied
in separate commits, each with its regression test, `MATH_DIFF.md` and
rebuilt PDF.

## Protected paths potentially affected

- `paper_assets/journal_p1_jogo/{main.tex,main.pdf,MATH_DIFF.md}` and `tests/test_journal_p1_jogo.py`: changed only by the three approved wording commits;
- `paper_assets/journal_p2_sidma/{supplement.tex,supplement.pdf,MATH_DIFF.md}` and `tests/test_journal_p2_sidma.py`: changed only by the one approved wording commit;
- every other file under `paper_assets/`, including the frozen S1 bundle, `s1_support.zip` and the Paper II article: unchanged;
- `results/**`, `verify.py`, `verify_global_brackets.py`, `src/**`: not read by the checks, unchanged.

## Completion gates

- [x] analysis complete within the stated scope;
- [x] claims classified (machine / hand / not verified) in the report;
- [x] new checks run: Paper I 40 checks and 6 controls, Paper II 20 checks and 8 controls, all passing;
- [x] existing repository test suite run on both branches (see EVIDENCE);
- [x] artifacts and provenance: the two rebuilt PDFs are recorded in EVIDENCE with command, environment and hashes;
- [x] durable memory: report added; `PROJECT_KNOWLEDGE.md` and `knowledge/*.md` unchanged because no stable claim changed;
- [x] `git status --short` inspected;
- [x] complete diff of the new files inspected;
- [x] whitespace check passed;
- [x] no incidental generated or protected-file change;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

No error and no gap in the statements examined. The four imprecisions were
reworded after the author's approval, in separate commits; the five style
remarks were not applied. Residual uncertainty: the cited sources, the certificates and
the upper witnesses for `n >= 8` were not re-verified here.

Exactly one next atomic task: the author reviews the four wording commits in
Draft PRs #23 and #24 and decides whether to merge them into the review
branches.
