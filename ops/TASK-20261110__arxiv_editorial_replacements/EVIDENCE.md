# Evidence — editorial replacements

## Baseline and provenance

Local Windows worktree; dedicated branch from editorial Git revision
`4b3721df8061f1992cfd242df69b1a0643216d8f`. The live public
[Paper I v2](https://arxiv.org/abs/2607.28654v2),
[Paper I v3](https://arxiv.org/abs/2607.28654v3) and
[Paper II v2](https://arxiv.org/abs/2609.13630v2) records were downloaded
on 2026-11-10. Public sources are the editorial base; the journal
manuscripts remain the historical source edition. All digests are SHA-256.

| Record | Public source tar.gz | Public PDF | Pages |
| --- | --- | --- | ---: |
| I v2 | `34e99300acc11a1a490321328e65ad57906f1c73dad5d1f48093569e246d5cd0` | `211cd007a176426acc7514ec31add92615383a5a293cee45593feffebddde727` | 12 |
| I v3 | `92cadeacb469db6947f4b5b74d2ab3bf8e4313927496ac98b350cd46b1288bf7` | `9fcf9fbd7e0c890d4362503925ce6732a19d2eeaf4b7785aa806ea4124914302` | 18 |
| II v2 | `359ded0dddbf7c632423d9a84e87d77319ab286c5caf7707b205a3d8c8306c7f` | `5950e70e5560821a53a36337a50ae50332aa0a1c4bd31fcbed8d698209777caa` | 9 |

November 9 upload ZIPs: I `9e8006f486d69b6f2e9f3c9c5b67be4ee226bd38bca4af34c051f3710dec9475`,
II `db3d81c107f06b69f59066043ddec19a3117392faa14d19050b1eb289c896d7b`.
Member comparisons with the corresponding public tar: all four Paper I and
all six Paper II non-configuration files agree byte for byte. arXiv rewrote
both `00README.json` files: retain the published configurations and the
single top-level manuscript in each case. In the November 10 Paper II ZIP
(`605e3ec957c7251ea5dbf327a273b718f1a375c68601f107821dbb53c31fc323`),
only `main.tex` differs from the November 9 ZIP; this is evidence for the
requested instructions, not a published or independently accepted version.

Local checks below are editorial/integrity checks. The existing exact finite
certificate route is distinct from the historical float64 route. No new
mathematical result or scientific baseline promotion is claimed.

## Local verification and its limits

Windows, Python 3.14.3, pdfTeX 1.40.28 (TeX Live 2025), Poppler and pypdf.
The [Paper I field sheet](../../paper_assets/arxiv_replacements/paper_i/metadata.md)
and [Paper II field sheet](../../paper_assets/arxiv_replacements/paper_ii/metadata.md)
record the exact build invocations, sizes, hashes, visual checks and relevant
public changes. These are claims about the candidate files, not the portal.

| Check actually run | Result | Scope |
| --- | --- | --- |
| `git ls-remote --heads origin` with the relevant ref filters and GitHub PR #4 inspection | Base refs match the brief; PR still open, draft and unmerged | Checkout/concurrency, not acceptance |
| Direct archive read and unified diff of every changed member against versioned arXiv sources | Only I `ringmin_dcg.tex` (§10/declarations), II `main.tex` and `anc/README.txt` changed; complete ZIP inventories preserved | Editorial and source integrity |
| Compare new files against historical Git source and public arXiv editions | Public-specific historical links, Paper II publication context, line break and disabled line numbers preserved; both public configs retained | Distinguishes published sources from journal editions |
| Two independent clean extractions per ZIP, three pdfLaTeX passes each | Exit 0; identical repeat PDFs for each paper, no final warnings; 18 and 9 pages | Build and local preview |
| `python -I -S ops/TASK-20261110__arxiv_editorial_replacements/replay_packages.py` | Exit 0; ZIP and compiled PDF byte-identical for each paper | Separate byte reconstruction from the checked source directories and another fresh build; environment-sensitive |
| SHA-256 recomputation for every entry in `paper_assets/arxiv_replacements/SHA256SUMS` | 18/18 match | Sources, PDFs, ZIPs and field sheets |
| From a full export of `6c16af422d1cb38641c62d43b6e0e547921b9ba9`, `python -I -S verify_global_brackets.py` | Exit 0; `PASS_GLOBAL_BRACKETS`, pinned input verification PASS. 908 intervals, 47 witnesses, 540 central tangencies, 3,004 outer pairs, 6,008 angular inequalities. | Reproduction of the existing exact finite verification for 3–14. No newly designed certificate, historical float64 audit, or independent peer acceptance |
| Download frozen companion linked in II §7; from `lower_supplement/`, `python -I -S verify.py`; from its root, `python -I -S verify_math.py` | Both exit 0; supplement checks and bounded arithmetic replay pass | Frozen edition, S1/S2 and bounded cases; universal claims depend on the proofs |
| PDF annotations and rendered pages | All internal destinations resolve. Paper II: all 10 distinct external URLs (11 annotations) returned HTTP 200; printed commands and link checked in PDF. Paper I: see field sheet for two publisher/community direct-access limits. | Local PDFs and cited sources; network responses can vary by method and client |

A preliminary Paper I typeset paragraph and the first Paper II §7 draft had
overfull lines; both were shortened and the final logs rechecked. A Paper II
diagnostic initially could not print a glyph on the Windows console; the
underlying check was rerun without that console dependency. A first attempt
to replay Paper I from a subset of the pinned repository omitted
`reproducibility/global_brackets/manifest.json` and failed explicitly. A
full export of the same commit supplied the missing manifest and passed.
A separate HTTP GET for the Zenodo DOI returned 403 with one client; it
was reachable in the field-sheet link check. These network checks do not
establish byte identity of a DOI landing page.

## Protected scope, submission and review

The only pre-existing tracked file intended to change is `CURRENT_STATUS.md`.
All new paper assets are under `paper_assets/arxiv_replacements/`. The
original `src/ringmin/`, `results/`, certificate/verifier inputs, research
notes, v1/v2 sources, both journal directories (including the companion and
S1/S2), prior dossiers, roadmap, and workflows are outside this delta.
No stable scientific claim changes and no Registry write is proposed.

Latest public submissions: Paper I 9 November 11:24:08 UTC; Paper II
9 November 13:04:19 UTC. Both records were visible in the authenticated
account, with an empty submission queue on 10 November. No new draft,
upload, portal PDF, receipt or new public version is claimed. For these
versions arXiv requests a weekly interval; it is not the hard cap used
after version 5. The [replacement instructions](https://info.arxiv.org/help/replace.html)
and [package guide](../../paper_assets/arxiv_replacements/README.md) give
the appropriate next action. No journal was selected or contacted.

The full historical frontier audit and local project-wide pytest were not
run for this source-only editorial delta. The push CI is independent of
the above local records; its eventual result must be checked on the exact
commit. The separate journal LaTeX workflow is path-filtered outside these
new paths. No external editorial or scientific acceptance is claimed.

## Final diff and delivery

The pre-stage scope check found 25 additions, one existing tracked file
changed, and 20 text files (including status) with no trailing whitespace
or missing final newline. Both normal and staged `git diff --check` exited
0. All 26 staged blobs were compared to the inspected working files; no
protected paths changed. Each of the two PDF/ZIP/metadata triplets was
also read back after delivery to the author's private editorial folder: all
six SHA-256 values and sizes matched the local manifest. No access changes.
