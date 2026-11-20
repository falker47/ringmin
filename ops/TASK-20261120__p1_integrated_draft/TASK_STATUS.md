# Paper I integrated journal draft

~~~text
task=TASK-20261120__p1_integrated_draft
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-20
updated_at=2026-11-20
branch=codex/p1-integrated-draft
base=56a9b999925ab61a0217273adf8f61a9b176c5e4
second_parent=d93fca92714fc9e59e69ed036fab734c9c5edb2d
merge=a437cc86ad6393c6c2f9b2f86ffa81ef96637aeb
target=main
~~~

## Objective and scope

Prepare one Journal of Global Optimization draft for the exact certification of prescribed lists of at least three distinct positive integer radii. The reported families are the linear and quadratic radii for each size from 3 through 14. Keep the original structural statements, declarations and publication record. Integrate PR #7 with PR #9 by an ordinary merge on the dedicated branch, then open a draft PR into main.

The editorial changes belong to `paper_assets/journal_p1_v5/`, its journal test and this dossier. The parent branches, shared status and knowledge, publication archives, generators and certificate inputs are protected. The author requested proposed ledger text in this dossier.

## Verified draft

The [manuscript](../../paper_assets/journal_p1_v5/main.pdf) has 21 A4 pages, including 12 pages before the appendices. Section 9, Table 5 and Figure 5 share page 10. Appendix C proves the general coverage and strictness arguments. The [claim map](../../paper_assets/journal_p1_v5/CLAIMS_DIFF.md) distinguishes finite certificates, the chain and seam theorems, and the limiting bounds attributed to revised Paper II.

On the merged branch both isolated verifiers passed, including all 24 general-radii certificates, and all 93 tests passed. Independent builds reproduced all six figures and the complete manuscript byte for byte. The [evidence](EVIDENCE.md) records the checks on the integrated tree and the earlier source-specific runs.

## Review handoff

Following the author's direct authorization, the ordinary merge joined the two source revisions without conflicts. The merge tree preserves all 25 changes from PR #7 and all 36 from PR #9. The integration branch supersedes those two PRs for review. The draft PR and its head revision identify the submission for independent review.

Before journal submission, check that the revised Paper II containing the quoted limits is publicly available on arXiv. This is a separate publication dependency.

**Next atomic action.** Conduct an independent STRICT mathematical and editorial review of the integrated draft PR at its recorded head revision.

## Proposed knowledge ledger text

For the certification owner, after independent review: “For each size from 3 through 14, the general-radii verifier reproduces the twelve original linear endpoint pairs with fresh rational witnesses and complete lower coverage. For square radii it verifies twelve finite global brackets of width 10⁻¹¹, open below and closed above. The coverage proof treats deletion of the smallest d ranks with at least three ranks retained. See the [method](../../paper_assets/general_radii/METHOD_NOTE.md), [certificates](../../paper_assets/general_radii/certificates/) and [independent verifier](../../paper_assets/general_radii/verify_radii_certificate.py).”
