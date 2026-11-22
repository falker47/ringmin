# Paper I in the Journal of Global Optimization format

~~~text
task=TASK-20261121__p1_jogo_format
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-21
updated_at=2026-11-21
branch=codex/p1-jogo-format
target=codex/p1-integrated-draft
base=040d301e600acc12430f76333ec3243268dd3d3e
~~~

## Objective and scope

Port the reviewed version of Paper I to Springer Nature's journal class and numbered mathematics style, with the three requested editorial changes. The deliverables are the [journal sources and PDF](../../paper_assets/journal_p1_jogo/), the [comparison test](../../tests/test_journal_p1_jogo.py) and this dossier. PR #12 supplies the reference text. The previous journal directory, certificate data, publication archives, shared ledgers, root README and CI configuration are protected.

## Outcome and evidence

The official package was obtained from Springer Nature and the two distributed style files preserve its original bytes. The 27-page PDF compiles in three LaTeX passes with one BibTeX run. All mathematical source comparisons and the local 99-test suite passed. Independently compiled manuscripts assign the same numbers to all 67 labeled objects. [Math comparison](../../paper_assets/journal_p1_jogo/MATH_DIFF.md) · [Build, provenance and review evidence](EVIDENCE.md)

## Author handoff

The date is September 19, 2026. The visible general-radii revision marker is awaiting the post-merge commit. The source comment requests the author's addition of Claude (Anthropic) to the AI disclosure. The existing condition concerning the public revision of Paper II applies before submission. The formatted manuscript is a draft for review.

**Proposed ledger text.** “The JOGO-format journal source at `paper_assets/journal_p1_jogo/` reproduces the mathematical body, figure sources and numbered references of integrated Paper I at `040d301`. See its MATH_DIFF and template provenance.” The existing scientific claims keep their current owners.

**Next atomic task.** Independently review the JOGO-format draft PR against its integrated parent.

The subsequent [referee audit](../../paper_assets/journal_p1_jogo/REFEREE_NOTES.md) covers clean-checkout reproduction, the source for Figure 5 and the two pre-submission dependencies above. The scientific body and certificate records retain their reviewed contents.
