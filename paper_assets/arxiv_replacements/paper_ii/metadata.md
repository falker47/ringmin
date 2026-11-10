# Paper II | arXiv replacement candidate

**Record.** [arXiv:2609.13630v2](https://arxiv.org/abs/2609.13630v2). Prepared 10 November 2026 for replacement of this record. Upload `paper_ii_source.zip`. The corresponding locally compiled preview is `paper_ii.pdf`.

| arXiv field | Value |
| --- | --- |
| Title | Minimum central circles: an effective characterization of the global asymptotic constant |
| Authors | Maurizio Falconi |
| Primary / cross-list | Metric Geometry (math.MG) / Computational Geometry (cs.CG) |
| MSC (2020) | 52C15, 52C26, 90C05 |
| License | arXiv.org perpetual, non-exclusive license (1.0) |
| Journal reference, report number, journal DOI | No additions. The existing arXiv record has its own DOI, 10.48550/arXiv.2609.13630. |
| Compilation | pdfLaTeX, TeX Live 2025, `main.tex` as the single top-level document. Retain all seven files, including both supplement TeX sources. |
| Manuscript keywords | circle packing; geometric optimization; asymptotic limits; linear programming; rigorous computation |

**Comments (copy into the form)**

```text
9 pages. Updated the reference to Paper I and added a direct link and verification commands for the frozen companion archive in section 7. Mathematical results unchanged. Standalone proof supplements S1 (14 pages) and S2 (13 pages) are supplied as ancillary PDFs, with their TeX sources included.
```

**Abstract (from the existing public record)**

```text
Let $R^\ast(n)$ be the minimum radius of a central circle externally tangent to nonoverlapping circles of radii $1,\ldots,n$. We prove that $R^\ast(n)=C_\ast n^2+o(n^2)$ and give finite linear programs that enclose $C_\ast$ with prescribed error. An exact angular comparison reduces the problem to marked points on a line with separation at least the geometric mean of each pair of marks. Concatenation with bounded joining cost and reassignment to the prescribed normalized radii prove existence of the limit. Balanced finite-word programs give a bracket of width $(1/k+1/r)/\pi$, before directed arithmetic error, using $k$ types and words of length $r$. We also obtain explicit geometric bounds. For the upper bound, we recover finite and countable reflected-block constructions by actual permutations, retaining all pair constraints. A coupled terminal-subset argument gives an explicit lower bound strictly above $1/8$. Together these give $C_{\rm term}+\eta_{\rm width}\le C_\ast\le U_4$. The lower endpoint comes from the terminal-subset argument, and the upper endpoint from the four-block construction; neither is asserted sharp. The finite-word scheme establishes computability; efficient high-precision evaluation and the structure of global optimizers remain open.
```

## Editorial comparison and provenance

The starting point was the [official v2 source distribution](https://arxiv.org/src/2609.13630v2) (SHA-256 `359ded0dddbf7c632423d9a84e87d77319ab286c5caf7707b205a3d8c8306c7f`). The [public PDF](https://arxiv.org/pdf/2609.13630v2) has 9 pages (SHA-256 `5950e70e5560821a53a36337a50ae50332aa0a1c4bd31fcbed8d698209777caa`). The repository source edition was frozen at `4b3721df8061f1992cfd242df69b1a0643216d8f`. The published v2 keeps the arXiv context, historical v1 self-citation, corrected line break and disabled line numbers. Its `main.tex` matches the 9 November no-line-numbers package. arXiv normalized the build configuration for the published source tar. This candidate preserves the published configuration.

Compared with v2, the introduction and bibliography now cite [Paper I v3](https://arxiv.org/abs/2607.28654v3) for the finite results, v1 for the conjecture and v2 for its correction. Section 7 integrates the direct archive link and the two working-directory-specific commands from the 10 November §7 candidate (ZIP SHA-256 `605e3ec957c7251ea5dbf327a273b718f1a375c68601f107821dbb53c31fc323`). The text identifies the earlier source edition described by the archive manifest. The ancillary README describes the updated citation and instructions. The diff against v2 touches only `main.tex` and `anc/README.txt`.

The acknowledgment retains the four uses already disclosed for Paper II (proof exploration, software, drafting and adversarial checks) and the author's responsibility. The title, abstract, manuscript dateline, keywords and MSC codes remain those of the public source. Both supplement PDFs and both TeX sources are byte-identical to the public v2 and the frozen companion.

| Preserved member | SHA-256 |
| --- | --- |
| `anc/lower_supplement/supplement.pdf` | `a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568` |
| `lower_supplement/supplement.tex` | `ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4` |
| `anc/upper_supplement.pdf` | `3e63ad0132d9a328c7f35f3af100f20c6473e74624ef5220278ca88cca91e11a` |
| `upper_supplement.tex` | `941d6ae995a7f7f23ab80f7db73d1a73c1c2d9ed97d160cd35e95bcfd2c6cb42` |

## Candidate verification

- On Windows with pdfTeX 1.40.28 (TeX Live 2025), extracted the upload ZIP into two fresh directories. In each ran `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error main.tex` three times. All six commands exited 0. The two final PDFs were byte-identical. Both final logs had zero missing characters, undefined references, LaTeX/package warnings, or overfull/underfull boxes. A preliminary version had a 19.65637 pt overfull line in §7. The shorter final prose and unbroken commands resolved it.
- ZIP readback checked CRC and exact equality with all seven files in `src/`. Compared against v2, all 268 delimited math expressions, 19 matched formal environments, the abstract and acknowledgment, and the entire 19,027-byte source of §§2–6 are identical. Diff inspection also covered prose outside those environments. No certificate or solver was edited.
- Checked all 28 internal PDF link destinations and enumerated 11 external annotations. The companion URL occurs once, on page 8. Page 9 links to the correct v3, v2 and v1 of Paper I. Rendered all nine pages with Poppler. Inspected the layout as a whole and reviewed pages 1, 8 and 9 individually for margins, commands, references and line numbers.
- Fetched the [companion ZIP](https://github.com/falker47/ringmin/raw/4b3721df8061f1992cfd242df69b1a0643216d8f/paper_assets/paper_ii_journal/source_bundle.zip) pointed to by the PDF. Its SHA-256 was `81923e4e76aaaed8180e3d3059d87adbe07022c0782b901ce24dba68f97bde50`, matching the archive at the pinned commit. Ran both printed commands with Python 3.14.3 against that download after extraction. From `lower_supplement/`, `python -I -S verify.py` exited 0 with `PASS supplement checks; analytic proof supplies universal quantifiers`. From its root, `python -I -S verify_math.py` exited 0 with `PASS bounded arithmetic replay; universal quantifiers require the written proofs`. The optional SciPy LP pass and global finite-optimum certification were outside these two replay commands. The proofs retain responsibility for all universal and limiting assertions.

| Deliverable | Bytes | SHA-256 |
| --- | ---: | --- |
| `paper_ii.pdf` | 336286 | `07a3733734ac828ab0a84670c9197f7c15178e86330396e889b310514395e1e5` |
| `paper_ii_source.zip` | 789129 | `97661b611e27100921c948ff50a002c598a778741b360fde8c358342a997bb38` |
