# Ringmin: arXiv editorial replacements, 10 November 2026

| Existing record | Candidate preview | Source ZIP to upload | Portal fields and editorial comparison |
| --- | --- | --- | --- |
| [Paper I, public v3](https://arxiv.org/abs/2607.28654v3) | [18 pages](paper_i/paper_i.pdf) | [Paper I ZIP](paper_i/paper_i_source.zip) | [Paper I metadata and checks](paper_i/metadata.md) |
| [Paper II, public v2](https://arxiv.org/abs/2609.13630v2) | [9 pages](paper_ii/paper_ii.pdf) | [Paper II ZIP](paper_ii/paper_ii_source.zip) | [Paper II metadata and checks](paper_ii/metadata.md) |

These are candidates for the next versions of the existing records. The
manuscripts, title/abstract fields and source layouts come from the public
arXiv distributions. Each ZIP contains the files shown under its `src/`
directory. The PDF is the local preview. [SHA-256 manifest](SHA256SUMS)
covers the sources, uploads, previews and field sheets; from this directory
run `sha256sum -c SHA256SUMS` to check a copy. The [package replay](../../ops/TASK-20261110__arxiv_editorial_replacements/replay_packages.py)
reconstructs the ZIPs and compares fresh local PDF builds. The DOI for the frozen Paper I
certificate release and the Paper II companion ZIP refer to their original
editions; neither identifies the bytes of these editorial replacements.

Before submitting, check for pending replacements on the [author page](https://arxiv.org/user).
Use the existing draft if one exists, otherwise **Replace** on the
corresponding owned article. For Paper II, keep all seven source members,
including both supplementary TeX files; only `main.tex` should compile.
Check the portal PDF, the section 7 link and the absence of line numbers.
Review each candidate's Comments and page count, submit, and retain its ID
and confirmation. A submission receipt precedes public announcement.

On 10 November the authenticated account showed neither replacement pending.
To observe [arXiv's requested weekly cadence](https://info.arxiv.org/help/replace.html),
the joint submission checkpoint is 16 November 2026 at 14:05 Europe/Rome,
after both previous submission timestamps plus seven days. This is a
recommended interval for these version numbers. Portal processing and
publication of these candidates are unverified.
