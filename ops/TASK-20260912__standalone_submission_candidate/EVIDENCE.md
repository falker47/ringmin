# Evidence

## Environment and provenance

Starting HEAD: `87a163289be1326c9864b359ca8e12b3de08ec75`.
Windows PowerShell; STRICT publication task. Scientific supplement remains
`3beb8d70c5b3748d370a92855847bdf574e5a14f`. Publication source/PDF provenance is
the containing commit, recoverable with `git log -1 --` this dossier or manifest.
No mathematical source or certificate regeneration is authorized or performed.

## Claim classifications and limits

The exact theorems remain owned by the linked proof notes and
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`; no new theorem or duplicated ledger
entry is created. Bounded exact checkers give independently reproduced finite
arithmetic evidence, not all-n proofs. Package/PDF checks are local engineering
facts. Separate agent audits are internal validation, not external acceptance.

## Verification record

All results below were executed locally in this task. Historical dossiers remain untouched.


### Fresh mathematical checks

The separate internal scientific auditor used Python 3.14.3 and SciPy 1.17.1.
Every command exited **0**. They are independent of production Ringmin imports;
SciPy proposes LP solutions, while exact rational comparisons validate them.
The manuscript's analytic arguments, not these bounded enumerations, establish
the infinite quantifiers. This task did not rerun finite global searches or the
saved-frontier verifier because no finite claim/artifact or solver was changed.

| Exact command | Material result | Property checked |
| --- | --- | --- |
| `python -I -S ops/TASK-20260911__global_variational_limit/check_line_recovery.py` | PASS 1089 words, 13995 independent paths, 13941 pair/closure checks, 1089 concatenations, 94620 quantiles; 4 negative controls rejected | Independent recurrence, all pairs, closure and actual label recovery. |
| `python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py` | PASS (k,r)=(1,2),(1,5),(2,2),(2,3),(3,4),(4,5); 1119 word inequalities; 18 corrupt certificates rejected | Complete bounded rational primal/dual certificates. |
| `python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py` | PASS 30034 orders/580560 cells; 18 larger orders/1080000 cells; 342 directed max probes, 438 Lipschitz probes, 4 controls | Finite label/cell recovery and directed arithmetic. |
| `python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py` | PASS 16 corner partitions, 448 moments, 48 branch probes, 6 sign/tie controls; saving >1/4608000000000000; 3 invalid chord gates rejected | Retained literal fourth-block saving. |
| `python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | PASS polynomial/root/KKT/uniqueness and floor-failure/strict-scaling gates | Directed lower enclosure reproduced exactly: 0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392. |

No material defect was found in the direct main proof or the linked endpoint
and recovery dependencies. Finite certified scope stays 3<=n<=14; endpoint
sharpness, efficient evaluation, closed form and global floating structure
remain open. The supplementary minima are not promoted to global optimizers.

### Build, PDF and metadata checks

Environment: Python 3.14.3 with pypdf 6.14.2 for the package audit; installed
TinyTeX/TeX Live 2025, pdfTeX 1.40.28 (format dated 2026-02-13), Poppler.
Bundled Python 3.12.14/pypdf 6.10.0 was located but the package command used
the installed Python. The manifest and PACKAGE_CHECK.json record all input,
builder, font, page-painting and 108 TeX-system dependency hashes. Reproducible
PDF time is SOURCE_DATE_EPOCH=1789084800 and FORCE_SOURCE_DATE=1; TEXINPUTS
contains only the current directory plus default distribution search paths.
This fixed September 11 epoch is build provenance, not the displayed paper date.

| Exact command | Exit and material result | Boundary |
| --- | --- | --- |
| `python paper_assets/build_publications.py sequel` | 0; PASS sequel: 3 clean passes; stable aux/out; zero warnings | Isolated one-input build, metadata generation; source-coupled builder. |
| `& './ops/TASK-20260911__publication_architecture/clean_compile.ps1' -Candidate sequel` | 0; PASS independent sequel compile; 1 inputs; 3 passes; zero warnings | Separate direct orchestration, same installed TeX distribution. |
| `python -B ops/TASK-20260912__standalone_submission_candidate/check_submission.py reproducibility/.work/publication-sequel-a914d86e6999428295be8d082e7bd9e8 reproducibility/.work/independent-sequel-b9ff92cb22a04470a0d2fdbe1780da41` | 0; one source, 20 labels, 6 references, 273 unchanged math expressions; 8 exact numbered pages; 16 embedded scalable fonts; no active content; sizes/hashes/metadata pass; 10 tamper controls rejected | Independent package checker; shared read-only PDF-object helper; no theorem acceptance claim. |
| `pdfinfo paper_assets/asymptotic_sequel/ringmin_asymptotic.pdf` | 0; 8 pages, 612x792 pt, PDF 1.7, no encryption, form or JavaScript; exact title and author | PDF header/metadata corroboration. |
| `pdftoppm -r 115 -png paper_assets/asymptotic_sequel/ringmin_asymptotic.pdf reproducibility/.work/final-sequel-pages/page` | 0; 8 page images rendered and individually inspected by root | Visual review of final exact artifact; not text-only QA. |

The two clean directories are ignored intermediates, reproduced by rerunning
the commands, not bundle dependencies. Independent and builder PDFs are also
byte-identical to the final PDF. Final logs have no overfull/underfull boxes,
undefined citations/references, duplicate labels, missing glyphs or warnings.
The main TeX source is self-contained, has inline bibliography, and needs no
Python, graphics, metadata or repository files to compile.

### Every-page visual record

| Page | Inspected content and result |
| --- | --- |
| 1 | Exact title/author/date, abstract and introduction; no workflow text. |
| 2 | Angular formulas, line definition/recurrence, closing lemma and squeeze; aligned, legible displays. |
| 3 | Existence proof and quantization; all equations and page boundaries fit. |
| 4 | Balanced LP, boxed effective bound and rational-certificate discussion; no collision or clipping. |
| 5 | Full-cell cost, block theorem and recovery proof; long inequality fits. |
| 6 | Recovery continuation, parameter brackets, fourth saving and start of lower section; display fits. |
| 7 | Lower endpoint, directed enclosure, proof outline and reproducibility; all text legible. |
| 8 | Open scope, AI acknowledgment and all six bibliography entries; pinned URL fits, ample ending space. |

### Exact artifacts

- `paper_assets/asymptotic_sequel/source_bundle/` contains exactly
  `ringmin_asymptotic.tex`, 26863 bytes. Source and bundle are identical.
- Source SHA-256: `5248445a3a1b92c494466fdfe266555023bbc13606f93ffc07ec229538b886e6`.
- PDF: `paper_assets/asymptotic_sequel/ringmin_asymptotic.pdf`, 325473 bytes.
- PDF SHA-256: `1f3bb01a8088b7b345eea710c99653ee4f06fb27cc45c58642333510e2d96454`.
- Exact copy-ready title, author, 1231-character abstract, Comments, categories,
  MSC, previous non-exclusive license guidance and processor/main source are
  in generated `ARXIV_METADATA.md` and `ARXIV_METADATA.json` outside the bundle.
- Old review-only metadata is replaced, with the historical version preserved
  in Git and the untouched architecture dossier. No conflicting current
  standalone upload identity remains.

### Publication and reference checks

[REFERENCE_AUDIT.md](REFERENCE_AUDIT.md) records current primary-source checks,
the ten immutable supplement targets and the final overlap diagnostic. Raw
repository paths in bibliography labels became readable titles with direct
commit-pinned links; a full stable GitHub URL remains printed for offline
identification. No future arXiv ID, DOI or journal information was invented.

### Failed attempts and limits

The initial sandbox TeX invocation exited 1 before source parsing with
`fatal: Can't get long name` for the installed distribution's profile path.
The identical authorized command outside that restriction passed; no scientific
or layout failure was hidden. A multi-operation documentation patch failed
atomically and was reapplied safely. The plain-Git ownership restriction was
handled per command without global Git changes.

No mathematical acceptance, server compilation, new finite search or hosted
CI is claimed. Local TL2025 packages are newer than arXiv's recorded snapshot;
actual arXiv output must be inspected by the author. Moderation may require
consolidation/versioning. These limits do not change the local artifact's
ARXIV_SUBMISSION_CANDIDATE identity or the task's READY_FOR_REVIEW state.


## Final diff inspection and integration boundary

Root inspected the complete tracked text delta, both identical source copies,
the regenerated manifest, both metadata formats, the complete new checker,
task documents and reference report. The generated PACKAGE_CHECK.json was
fully parsed and its data checked by the independent auditor; all fields,
page/font/dependency inventories and limits were reviewed. Binary PDF changes
were checked by exact hashes, independent page painting and every-page images.
An explicit UTF-8/whitespace check covers every new text file, which ordinary
unstaged `git diff --check` would omit. The staged whitespace check then covers
all additions as well. A Windows-locale decoding artifact in two new log
headings was corrected; no manuscript encoding was affected.

Protected-path diff against starting HEAD exited 0 for the original paper and
assets, both other manuscript trees, citation metadata, mathematical proof
sources and ledgers, results, solver, verifier, dependencies, workflows and
prior audit dossiers. The only research-file change is current publication
routing in the roadmap. The compact index and AGENTS.md are unchanged. No
stable mathematical claim is duplicated or promoted by a publication-state
label. The source bundle remains exactly one TeX file.

The authorized integration stages only the inspected task paths, checks the
staged diff/whitespace and source/PDF blob hashes, commits with
`Finalize standalone asymptotic arXiv submission candidate`, normally pushes
existing `main` to `origin`, and compares HEAD with remote `refs/heads/main`.
Its actual command results and commit SHA are recorded by the final tool
outputs and user handoff; the committed manifest is identified by its
containing commit. READY_FOR_REVIEW is a pre-submission task state, not
external ACCEPTED. No force push, merge, rebase, tag, release or submission
is part of this task.


Final pre-stage command results: `git diff --check` exit 0; protected-path
`git diff --exit-code 87a163289be1326c9864b359ca8e12b3de08ec75 -- ...` exit 0;
explicit Python UTF-8/JSON/allowed-path checks exit 0 and full untracked
whitespace scan passes all nine additions. An initial overbroad scan included
pre-existing root README trailing whitespace and exited 1; no unrelated
cleanup was made. Modified-line whitespace is covered by Git's diff check.
The exact task path inventory contains twenty paths including the replaced
review-only JSON. The staged check below must retain precisely this scope.
