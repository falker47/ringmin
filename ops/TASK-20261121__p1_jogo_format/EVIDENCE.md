# Evidence for the Springer Nature port

## Publisher requirements and upstream inputs

Read on 21 November 2026. JOGO requests the editable source, figures and compiled PDF, with no submission subdirectories. It specifies numeric square-bracket citations, consecutively numbered entries and DOI links where available. It calls for a 150–250-word abstract, four to six keywords, corresponding-author details and relevant declarations. The draft has a 158-word abstract, six keywords, the four original MSC codes and the original author disclosures. [Journal guidelines](https://link.springer.com/journal/10898/submission-guidelines)

The journal links to the Springer Nature author support page. Its ZIP identifies the article template as version 3.1, December 2024. The manual and example select `sn-mathphys-num` for numbered mathematics and physical sciences references. The table records SHA-256 over the original bytes. [Springer Nature LaTeX author support](https://www.springernature.com/gp/authors/campaigns/latex-author-support) · [Publisher ZIP, CMS revision v12](https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12)

| Download or ZIP member | Version or role | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| ZIP archive | Template 3.1, December 2024, HTTP 200, CRC check passed | 901814 | `812e76dcaa9c28dc1bff1fb6065d51729b67d4ea140552a05088317414a3ecae` |
| sn-article-template/sn-jnl.cls | Class declares 2019/11/18 v0.1 | 55857 | `36d0c3273a59d48dc6a9c7b080dfa1ec50dc10229d8751568d1f2e490ffa5ecc` |
| sn-article-template/bst/sn-mathphys-num.bst | Style declares 2024/07/19 v1.1, compatible with BibTeX 0.99d | 64164 | `b3a7c7fbcc1e7f9619de634fcea2f5bb7a245818a5942bc576e40ea001633332` |
| sn-article-template/sn-article.tex | Publisher example identifying version and class option | 34686 | `71777936dca4952ac34aef4b98f5ce543fe50597efb2c1798cbb7a97767b70a9` |
| sn-article-template/user-manual.pdf | Publisher's style table and single-source instructions | 418495 | `4bb5d025c3ec64825cb3f4e1590d7ecc73b51c3c7c53e06711f59d2e840ed9e9` |

The class and bibliography style are distributed as downloaded with their original license headers. The directory's two Git attributes preserve their byte representation, including CR-only line endings in the class and the legacy-encoded bibliography style. The regression checks their original hashes on every platform. The manuscript's bibliography adds publisher locations required by the style for two chapters and one book. [Szabó et al., Springer](https://link.springer.com/chapter/10.1007/978-1-4613-0295-7_14) · [Graph Drawing and Network Visualization, Springer](https://link.springer.com/book/10.1007/978-3-319-27261-0) · [Tucker, Princeton University Press](https://press.princeton.edu/books/hardcover/9780691147819/validated-numerics)

## Environment

Local Windows 11, CPython 3.14.3, pytest 9.0.2, pypdf 6.14.2, pdfTeX 1.40.28 and BibTeX 0.99d (TeX Live 2025), Poppler 26.07.0. The base is PR #12 at `040d301e600acc12430f76333ec3243268dd3d3e`. All six vector figures come from that revision. The PDF build fixes the source date and removes variable PDF metadata. It uses the unmodified publisher class and bibliography style.

The existing TinyTeX installation lacked four runtime packages. Installed them with `tlmgr --repository https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2025/tlnet-final install sttools threeparttable appendix wrapfig` (exit 0). The configured repository was left at its existing setting. The four standard TeX dependencies are environment prerequisites.

## Checks on the formatted manuscript

| Command or check | Result and scope |
| --- | --- |
| `python paper_assets/journal_p1_jogo/build.py` | Exit 0. `PDF pages=27 pdflatex_passes=3 bibtex_runs=1 unresolved=0 max_overfull_pt=0 overfull_above_1pt=0`. The final log is checked for citation, cross-reference, figure and box diagnostics. The builder rejects missing publication data emitted as question marks by BibTeX. |
| `python -m pytest` | Exit 0, `99 passed in 62.34s` with the final export. For this process, set `PYTHONPATH` to the checkout's `src` directory and verified the imported package path before running. Includes the paper-specific comparison and upload-package build tests. |
| `python -m ruff check paper_assets/journal_p1_jogo/build.py tests/test_journal_p1_jogo.py --no-cache` | Exit 0, `All checks passed!`. |
| `python paper_assets/journal_p1_jogo/build.py --output <tmp>/second.pdf --submission-zip <tmp>/handoff.zip` | Exit 0. The second PDF matched the delivered PDF byte for byte. The 12-member flat archive contains one expanded manuscript TeX file, six figures, the original class and style, the BibTeX database, generated bibliography and PDF. Compiling its extracted contents again produced the same PDF. |
| Independent TeX numbering check | Compiled the reviewed article and extracted flat port in separate temporary directories and compared the numeric fields in their final auxiliary files, parsing nested braces. All 67 cross-reference keys and their printed numbers matched. Page numbers vary with typesetting. |
| Independent PDF inspection | pypdf found the original author details, date and MSCs, all 48 printed endpoints from the 24 rational certificate files, all three Paper II constants, and all 16 source DOI targets. The requested commit placeholder is visible once. The source-only author note is absent from the PDF. Zero unresolved markers. |
| Visual inspection | Rendered the 27-page layout with Poppler and examined the final quadratic table and availability/declarations page at higher resolution. The complete table is on page 12, Figure 5 on page 13, declarations on page 14, references on pages 15–16, and Appendix A begins on page 17. |

The delivered PDF is 596176 bytes, SHA-256 `fb39aafa831569f5b4036e066ca280e6847293ecae7c483815834f1db5a63ee0`. The final flat ZIP has SHA-256 `8d02cb6be9b001ddd16fcc1657cc2becd77128d6bfca6d27baeec39d63e3ebd1`. Two separate builds from explicitly LF and CRLF copies of the BibTeX database produced identical archives and PDFs. Binary identity applies to the recorded toolchain and fonts.

## Claim status and final scope

The change is editorial and typographical. The source equality and binary matches are engineering facts. Finite certificates, existing exact theorems, numerical reconstruction observations and claims attributed to revised Paper II retain the integrated draft's respective classifications. [Normalized comparison and figure hashes](../../paper_assets/journal_p1_jogo/MATH_DIFF.md) · [Reviewed claim map](../../paper_assets/journal_p1_v5/CLAIMS_DIFF.md)

The three permitted path groups contain the complete change. For a source checkout, build from the repository root using the command above. For an upload, the optional ZIP uses the same flat inputs as the local PDF build. Actual Editorial Manager execution and journal acceptance are outside this draft review.

Before staging, `git status --short --untracked-files=all` and an independent path-set comparison identified exactly 19 additions, comprising 15 journal assets, one test and three dossier files. All ten authored text files passed direct checks for trailing whitespace and final newlines. The other nine files were seven PDFs and the two hash-pinned publisher inputs. The complete diff outside the three authorized groups was empty and `git diff --check` exited 0. The source ZIP used for extraction and the temporary page-review images were removed after verification.

Reviewed the full staged diff and compared all 19 index blobs with their inspected working files. All matched, the unstaged diff was empty and `git diff --cached --check` exited 0.

## Windows test-launch replay

The standalone build passed at the initial port commit `85954f2`. A full pytest repeat there returned `1 failed, 98 passed in 57.46s`. The new test's Python child failed to start because Windows could not duplicate its inherited standard-input handle (WinError 6). Its subprocess now receives `subprocess.DEVNULL`. In a separate Python process, setting the Windows standard-input handle to an invalid value reproduced that same error with the old launch arguments. With the handle still invalid, the corrected test built the PDF and checked the 12-member upload package, exit 0. The entire suite then returned `99 passed in 63.28s` and Ruff again returned `All checks passed!`. The PDF retained the digest reported above.
