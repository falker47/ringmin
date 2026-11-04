# ringmin

Ringmin is a computational-geometry research project studying the **minimum central circle problem**: given circles of radii $1,2,\ldots,n$, arrange them around a central circle so that every surrounding circle is externally tangent to the central one, no two surrounding circles overlap, and the central radius $R$ is as small as possible.

The project combines mathematical analysis, geometric optimization, computational certificates, and reproducible research code. Its two public arXiv preprints address complementary questions: **finite global optimization** and **asymptotic behavior as $n\to\infty$**.

The repository also contains a standalone exact-arithmetic verifier establishing rigorous global radius brackets for $3\le n\le14$. Those computer-certified results are distinct from theoretical results for arbitrary $n$, numerical reconstructions, and heuristic observations.

**Navigate:** [Publications](#publications) · [Mathematical scope](#mathematical-scope) · [Certified finite results](#certified-finite-results) · [Quick verification](#quick-verification) · [Full certification and regeneration](#full-certification-and-regeneration) · [How to cite](#how-to-cite) · [Repository layout](#repository-layout) · [Non-technical explainer (Italian)](SPIEGAMI.md)

## Publications

### Paper I — finite optimization and certified optima

**Maurizio Falconi**, *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima*.

[arXiv:2607.28654v2](https://arxiv.org/abs/2607.28654v2) · 2026 · Computational Geometry (cs.CG)

The finite paper establishes the Supnick/anti-Monge structure of the adjacent-chain ordering problem, develops an all-pairs geometric feasibility model, and reports computer-certified global optima for $3\le n\le14$.

Its central distinction is that **an optimal adjacent-chain order need not produce a feasible arrangement of all the circles**. Nonadjacent pairs impose additional constraints, and some smaller circles may become floating circles, touching only the central circle.

The public corrective v2 preserves the finite results while correcting the asymptotic conjectures made in v1. In particular, the former conjecture $R^\ast(n)\sim n^2/8$ was disproved by subsequent work.

Repository materials:

- [Corrective v2 manuscript and source](paper_assets/v1_correction/README.md)
- [Historical finite-paper source](paper_assets/ringmin_paper.tex)
- [Finite certification evidence](knowledge/CERTIFICATION.md)
- [Publication history](knowledge/PUBLICATION_HISTORY.md)

### Paper II — global asymptotic theory

**Maurizio Falconi**, *Minimum central circles: an effective characterization of the global asymptotic constant*.

[arXiv:2609.13630](https://arxiv.org/abs/2609.13630) · 2026 · Metric Geometry (math.MG), Computational Geometry (cs.CG)

The standalone sequel studies what happens as the number of surrounding circles grows. It establishes the quadratic-scale asymptotic relation

$$
R^\ast(n)=C_\ast n^2+o(n^2)
$$

and characterizes $C_\ast$ through finite balanced-word linear programs.

For $k$ mark types and words of length $r$, the construction provides rigorous upper and lower bounds whose gap is

$$
\frac{1/k+1/r}{\pi},
$$

before directed arithmetic error.

This gives an effective characterization of the constant to arbitrary prescribed precision in principle. It does not provide an elementary closed form or an established efficient high-precision evaluation algorithm.

The explicit bounds include

$$
C_{\mathrm{term}}+\eta_{\mathrm{width}}
\le C_\ast\le U_4,
$$

with

$$
C_{\mathrm{term}}+\eta_{\mathrm{width}}
>0.14056946887766098063257>\frac18.
$$

Neither endpoint is claimed to equal the true constant. The four-block upper construction includes genuine-permutation recovery and full geometric feasibility.

The theoretical arguments, their dependencies, and the internal adversarial reviews are documented in the repository. Internal verification is not a substitute for independent external peer review or journal acceptance.

Repository materials:

- [Standalone sequel, source and PDF](paper_assets/asymptotic_sequel/README.md)
- [Global asymptotic results and limitations](knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md)
- [Global variational-limit proof](research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md)
- [Four-block geometric recovery](research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md)

Both papers are publicly available as arXiv preprints. Journal preparation and any subsequent editorial review are separate from these public versions; this README does not claim journal acceptance.

> **Italian introduction:** [SPIEGAMI.md](SPIEGAMI.md) explains the geometric problem, the main results, and the distinction between finite certification and asymptotic theory without requiring specialist background.

## Mathematical scope

### The geometric model

For surrounding radii $a,b>0$ and central radius $R>0$, the minimum angular separation required to prevent overlap is

$$
\theta_R(a,b)
=2\arcsin\sqrt{\frac{ab}{(R+a)(R+b)}}.
$$

For a cyclic order $\sigma$, three quantities must be distinguished:

- $R_{\mathrm{chain}}(\sigma)$: the radius obtained by closing the chain of consecutive angular separations.
- $R_{\mathrm{full}}(\sigma)$: the minimum radius permitting a placement satisfying **all pairwise non-overlap constraints** in that fixed cyclic order.
- $R^\ast(n)=\min_\sigma R_{\mathrm{full}}(\sigma)$: the global minimum over all cyclic orders.

For every order,

$$
R_{\mathrm{chain}}(\sigma)
\le R_{\mathrm{full}}(\sigma).
$$

Consequently,

$$
\min_\sigma R_{\mathrm{chain}}(\sigma)
\le R^\ast(n).
$$

The Supnick/anti-Monge theorem identifies a minimizing order for the adjacent-chain relaxation. Its geometric realizability is a separate question. The full fixed-order feasibility problem is represented through pairwise angular constraints, equivalently a Simple Temporal Network (STN).

See [Definitions and Core Model](knowledge/DEFINITIONS.md) and [Fixed-Order Theory](knowledge/FIXED_ORDER_THEORY.md).

### Evidence and claim boundaries

The project distinguishes several forms of evidence:

| Claim type | Supported scope |
|---|---|
| Mathematical theorems | Results proved in the cited manuscripts and research notes, subject to their stated assumptions |
| Exact-arithmetic computer certification | Rigorous global intervals for $R^\ast(n)$, for $n=3,\ldots,14$, using finite combinatorial coverage and rational arithmetic |
| Historical numerical certification | The finite solver, frontier artifacts and independent 50-digit checks, subject to the documented numerical guards |
| High-precision reconstruction | Numerical values and reported geometric structures for saved candidate configurations |
| Heuristic optimization | Candidate arrangements and patterns beyond the certified finite range |
| Conjectures and open questions | Claims not established by the available proofs or certificates |

In particular, a feasible arrangement establishes an **upper bound**, not global optimality. Local optimality for one cyclic order is not global optimality over every order.

The finite results do not prove that a floating-circle pattern continues indefinitely, that a reported contact structure is unique, or that every global minimizer has the same geometry.

The authoritative classification of the project's stable claims is maintained in [PROJECT_KNOWLEDGE.md](PROJECT_KNOWLEDGE.md), with detailed evidence in its linked thematic ledgers.

## Certified finite results

### Exact global radius brackets

The repository contains a standalone exact-arithmetic verification route supporting, for every integer $n=3,\ldots,14$,

$$
\boxed{L_n<R^\ast(n)\le U_n,\qquad U_n-L_n=10^{-11}.}
$$

Here $L_n$ and $U_n$ are exact rational endpoints supplied by the preserved certificate. They are not assertions that $R^\ast(n)$ has a known exact decimal expansion.

The certificate combines:

1. Rigorous outward-checked angular intervals.
2. Complete canonical-order coverage, using integer dynamic programming, pruning and explicit insertion cases.
3. Strict lower-bound margins excluding feasible configurations at and immediately above $L_n$.
4. Exact rational Cartesian witnesses establishing feasible arrangements at $U_n$.
5. Input-integrity and provenance checks tied to the preserved certificate.

The complete verifier is [`verify_global_brackets.py`](verify_global_brackets.py). It uses the Python standard library only and does not rely on the production solver, historical floating-point frontier pruning, checkpoint files or an exhaustive-search replay.

The [global bracket proof note](research/GLOBAL_BRACKET_CERTIFICATE.md) documents the mathematical derivation, completeness argument, exact inequalities, witness verification and limitations. [Certification](knowledge/CERTIFICATION.md#independent-exact-arithmetic-global-brackets) records the separate review and acceptance history for this finite result.

**Scope limitation:** these brackets certify the global radius to the stated interval width. They do not, by themselves, establish an exact optimal cyclic order, uniqueness, a universally valid contact graph, or any result for $n>14$.

### Reported optimal configurations

The following 30-digit numerical reconstructions and representative configurations are recorded in [`results/highprec.csv`](results/highprec.csv) and the saved `results/nNN/optimum.json` artifacts.

The table retains the finite study's reported incumbent orders and floating sets. A floating circle is tangent to the central circle but need not touch any other surrounding circle in the reported placement.

| $n$ | Reported $R^\ast$ (numerical reconstruction) | Reported incumbent cycle | Floating circles |
|---:|---|---|---|
| 3 | 0.260869565217391304347826086957 | `[3, 1, 2]` | `{}` |
| 4 | 0.844453589560855604347528524674 | `[4, 1, 3, 2]` | `{}` |
| 5 | 1.69549408120271081351328017371 | `[5, 1, 4, 3, 2]` | `{}` |
| 6 | 2.79491951889692485617024406797 | `[6, 1, 5, 3, 4, 2]` | `{}` |
| 7 | 4.15318955374381246513863858202 | `[7, 1, 6, 3, 4, 5, 2]` | `{}` |
| 8 | 5.7677942845896143026361805725 | `[8, 1, 6, 4, 5, 3, 7, 2]` | `{1}` |
| 9 | 7.72672655261128921886246177604 | `[9, 2, 8, 1, 5, 6, 4, 7, 3]` | `{1}` |
| 10 | 9.97990738586347760966552641468 | `[10, 2, 9, 4, 7, 1, 6, 5, 8, 3]` | `{1}` |
| 11 | 12.4887204871876588517468786264 | `[11, 2, 10, 4, 8, 6, 7, 1, 5, 9, 3]` | `{1}` |
| 12 | 15.2588704304484933617250043503 | `[12, 2, 11, 4, 9, 6, 7, 8, 5, 1, 10, 3]` | `{1}` |
| 13 | 18.3175630472173206282821941532 | `[13, 3, 1, 12, 2, 10, 6, 8, 7, 9, 5, 11, 4]` | `{1}` |
| 14 | 21.6653951822145150956462891793 | `[14, 3, 13, 2, 9, 8, 7, 10, 6, 11, 5, 1, 12, 4]` | `{1,2}` |

The printed precision is numerical reconstruction precision, **not a claim of 30 certified decimal places**. The historical finite certification reports an absolute global-radius guard of $10^{-10}$, with local checks near $R^\ast\pm10^{-12}$ and 50-digit arithmetic. The later exact-arithmetic route establishes the separate $10^{-11}$-wide global brackets.

The reported orders and floating sets describe saved representative configurations. Their appearance in the table does not establish uniqueness or the same floating structure for every global optimum.

The reconstructed values are also reproduced in [`paper_assets/appendix_tables.tex`](paper_assets/appendix_tables.tex).

## Quick verification

Run the following commands from the repository root.

### Requirements

The Python project supports Python **3.11 or newer**. The recorded submission-gate environment uses Python 3.14.3 and the exact package versions in [`requirements.txt`](requirements.txt):

- `numpy==2.4.3`
- `scipy==1.17.1`
- `mpmath==1.3.0`
- `matplotlib==3.10.9`
- `pytest==9.0.2`

The package configuration in [`pyproject.toml`](pyproject.toml) intentionally leaves ordinary development dependencies unpinned. Use `requirements.txt` when reproducing the recorded submission environment.

Install the development and test dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
```

### Verify all exact global brackets

This is the recommended first check for the complete finite certified range:

```bash
python -I -S verify_global_brackets.py
```

It requires only Python 3.11+ and the tracked certificate files. Third-party packages and installation of `ringmin` are unnecessary for this standalone command.

The verifier checks all twelve cases, mathematical certificate content, and the pinned original-input identities. It has no partial-case or skipped-proof success mode.

Its optional `--mathematical-only` mode retains the complete mathematical checks but deliberately omits historical input-identity verification. See [the verifier documentation](reproducibility/global_brackets/README.md) before using that option.

For the exact mathematical argument and the limits of the preserved evidence, consult [`research/GLOBAL_BRACKET_CERTIFICATE.md`](research/GLOBAL_BRACKET_CERTIFICATE.md). Re-executing the verifier is a reproducibility check, not a new independent mathematical peer review.

### Run tests and the historical verifier smoke check

```bash
python -m pytest
python verify.py --start 3 --stop 8 --skip-frontier
```

The smoke command checks the selected incumbent configurations and local-radius behavior, but explicitly skips the historical frontier audit. It must not be presented as a complete global certificate.

### Continuous integration

[GitHub Actions CI](.github/workflows/ci.yml) runs on pushes and pull requests. The workflow currently installs the pinned dependencies with Python 3.14 and executes:

- The pytest suite.
- The historical verifier smoke test for $n=3,\ldots,8$, with frontier checks skipped.
- The complete standalone exact-arithmetic global bracket verifier for $n=3,\ldots,14$.

The workflow does not regenerate exhaustive searches or run the full historical frontier audit.

A successful CI run verifies the configured checks for its specific commit, not the correctness of every mathematical proof or unpublished conjecture.

## Full certification and regeneration

The following procedures serve different purposes. The exact global bracket verifier is self-contained; the historical frontier route and long-running search regeneration are separate.

### Historical high-precision and frontier verification

The historical verifier, [`verify.py`](verify.py), is implemented using the Python standard library and `mpmath`, independently of `src/ringmin`.

It checks three layers:

1. **Incumbent feasibility:** reads the saved `optimum.json` artifacts, reconstructs angular constraints at 50-digit precision, and examines witness positions, all-pairs non-overlap, essential pairs and floating circles.
2. **Local optimality:** checks feasibility at the reported radius plus a small tolerance and infeasibility at the reported radius minus that tolerance for the saved order.
3. **Historical global pruning evidence:** checks frontier hashes, canonical enumeration metadata, progress logs, saved lower bounds and numerical guards.

On a fresh clone, restore the exact archived historical progress logs before performing the complete historical verification:

```bash
python scripts/frontier_logs.py restore
python verify.py --start 3 --stop 14
```

The restoration checks archive hashes and original log bytes and refuses to overwrite differing evidence. It **restores the saved historical logs**; it does not regenerate the exhaustive search.

A recorded historical full-verifier run reports:

```text
n=03 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=1
n=04 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=3
n=05 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=12
n=06 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=60
n=07 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=360
n=08 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=2520
n=09 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=20160
n=10 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=4 total=181440
n=11 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=6 total=1814400
n=12 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=9 total=19958400
n=13 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=10 total=239500800
n=14 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=11 total=3113510400
```

These are recorded results, not a claim that the complete historical verifier runs on every CI commit.

The historical frontier method used floating-point lower bounds during Stage A and high-precision rechecking of saved frontier candidates. Its retained Top-K comparisons and frontier-completeness assumptions have documented limitations.

High-precision verification of retained orders does not independently prove every historical exclusion decision. The accepted exact-arithmetic global bracket route avoids that dependency for its stated finite claim.

See the [historical evidence restoration dossier](ops/TASK-20260911__portable_frontier_evidence/EVIDENCE.md), [Certification](knowledge/CERTIFICATION.md) and [Implementation](knowledge/IMPLEMENTATION.md).

### Regenerate exhaustive searches

These commands are intended for research-level regeneration, not ordinary installation or CI.

The recorded historical sweep used `K=20000` for $n\le13$ and `K=50000` for $n=14$.

```bash
python scripts/sweep_certified.py --start 3 --stop 13 --k 20000 --workers 8 --resume
```

For $n=14$, the sweep can be run directly:

```bash
python scripts/sweep_certified.py --start 14 --stop 14 --k 50000 --workers 8 --resume
```

A Windows detached execution wrapper is also provided:

```powershell
powershell -File scripts/start_detached_sweep.ps1 -Start 14 -Stop 14 -K 50000 -Workers 8 -Resume
```

These searches can be computationally expensive, especially for $n=13,14$. Checkpoint pickle files are not tracked by Git and cannot be reconstructed merely by restoring archived progress logs.

The saved $n=14$ historical frontier was extracted from the existing `K=50000` checkpoint heaps; the documented extraction did not require a new Stage-A sweep.

### Regenerate high-precision and frontier artifacts

After the required search evidence is available:

```bash
python scripts/highprec_verify.py --start 3 --stop 14 --digits 50
python scripts/extract_frontiers.py --start 3 --stop 14 --margin 2e-10
```

The frontier extraction requires the relevant original checkpoint artifacts. A clean clone containing only the tracked frontier JSON and archived progress logs is not, by itself, sufficient to regenerate those frontier files.

### Numerical calibration

Run the historical float64-versus-mpmath sampling procedure:

```bash
python scripts/calibrate_float64.py --start 8 --stop 14 --samples 100000 --workers 8 --batch-size 500
```

The recorded sampled maximum absolute deviation was approximately `1.75137506176142662e-14`, below the historical `1e-11` submission threshold.

This is an empirical calibration result for the tested samples, **not a rigorous universal error bound** for all excluded search orders.

### Regenerate tables, figures and reports

```bash
python scripts/refresh_heuristic_artifacts.py
python scripts/free_float_criterion.py
python scripts/patterns_table.py
python scripts/supnick_validity.py
python scripts/asymptotic_fit.py
python scripts/generate_figures.py
python scripts/build_report.py
python scripts/export_paper_assets.py
```

These scripts regenerate research and presentation artifacts from the available inputs. They do not extend the certified range.

### Rebuild the public manuscripts

With `pdflatex` and the required LaTeX packages installed, use the dedicated builders:

```bash
python paper_assets/build_publications.py correction
```

This rebuilds the finite corrective-v2 package.

```bash
python paper_assets/build_publications.py sequel
```

This rebuilds the standalone asymptotic sequel.

The source bundles can also be compiled directly with `pdflatex`, following the instructions in their respective directories.

The older root manuscript can be compiled separately as historical provenance:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

Rebuilding a manuscript does not submit, replace or update its arXiv record. Historical builder metadata may still describe the original pre-submission workflow.

Matching PDF bytes across different LaTeX installations requires compatible source files, packages, fonts and build settings. See the corresponding build manifests for the recorded environments and hashes.

## Provenance and data-generation records

The original M6 data artifacts record their generation commit in each `results/nNN/optimum.json` file:

```text
fea000523a1ec4193d8ba9c4637563fd65e86d1a
```

This is the historical data-generating commit, not the current `main` HEAD.

Historical long-run evidence includes:

- `results/checkpoints/progress_n13_lb3.log`
- `results/checkpoints/progress_n14_lb3.log`
- `results/logs/sweep_14_14_20260610_221502.out.log`
- `results/logs/sweep_14_14_20260610_221502.err.log`

The original progress logs can be restored from [`reproducibility/frontier_logs/`](reproducibility/frontier_logs/). Large checkpoint `.pkl` files are intentionally ignored by Git. The portable historical frontier JSON artifacts are tracked under [`results/frontiers/`](results/frontiers/).

The exact-arithmetic global bracket evidence is preserved separately under [`reproducibility/global_brackets/`](reproducibility/global_brackets/).

These evidence chains must not be conflated. Preserving original files and checking their hashes establishes input identity, while the mathematical certificate verification establishes the stated finite bounds.

## How to cite

Cite the paper corresponding to the result used:

- **Finite Supnick theory and certified optima:** Falconi, *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima*, arXiv:2607.28654v2 (2026).
- **Global asymptotic theory:** Falconi, *Minimum central circles: an effective characterization of the global asymptotic constant*, arXiv:2609.13630 (2026).

Cite both when discussing the research program across its finite and asymptotic scope.

The machine-readable [`CITATION.cff`](CITATION.cff) describes the software and finite-certificate companion, with Paper I as its preferred citation. It does not replace the separate citation of Paper II when asymptotic results are used.

The archived software companion has version DOI [10.5281/zenodo.22849826](https://doi.org/10.5281/zenodo.22849826), identifying release `v1.1.0-dcg-presubmission` at commit:

```text
80919666c3c54f8ce20cf66c456d413f6a2c075f
```

The deposit is a frozen versioned snapshot, not a citation of every subsequent repository change. Its provenance is documented in the [archive evidence dossier](ops/TASK-20260926__archive_evidence_integration/EVIDENCE.md).

## Research workflow and AI assistance

Ringmin was developed through an AI-assisted research workflow under the author's direction and review.

AI assistance supported mathematical exploration and argument development, software implementation, testing, verification tools, documentation, and research artifacts.

The project's mathematical and computational claims should be evaluated through their explicit proofs, assumptions, certificates and reproducibility evidence. AI assistance and internal adversarial review do not independently establish mathematical correctness or replace external scientific review.

Scientific responsibility and decisions concerning the public manuscripts remain with the author.

The repository separates durable mathematical knowledge, current research work, historical provenance and independent verification so that results can be examined without relying on an AI-generated summary or an unverified status label.

## Repository layout

- [`src/ringmin/`](src/ringmin/) — solver library, geometric evaluation, search, numerical methods and CLI.
- [`tests/`](tests/) — pytest coverage for geometry, search, numerical cross-checks, certificate verification and adversarial cases.
- [`verify.py`](verify.py) — standalone high-precision verifier for the historical finite certificate route.
- [`verify_global_brackets.py`](verify_global_brackets.py) — complete exact-arithmetic global bracket verifier.
- [`results/`](results/) — reported finite optima, saved frontier certificates, heuristic results, calibration data and recorded outputs.
- [`reproducibility/`](reproducibility/) — preserved exact certificate evidence, historical log archives and reproducibility material.
- [`scripts/`](scripts/) — search, calibration, analysis and artifact-generation utilities.
- [`knowledge/`](knowledge/) — thematic ledgers classifying established results, limitations, disproved claims and open questions.
- [`research/`](research/) — detailed mathematical arguments, constructions, proof notes and research directions.
- [`paper_assets/`](paper_assets/) — public manuscript sources and PDFs, supporting material, tables, figures and separate journal-preparation packages.
- [`paper_assets/figures/`](paper_assets/figures/) — tracked publication figures; additional output under root `figures/` is generated locally.
- [`ops/`](ops/) — dated task dossiers, review records, commands and historical evidence.
- [`PROJECT_KNOWLEDGE.md`](PROJECT_KNOWLEDGE.md) — index of durable mathematical knowledge and source authority.
- [`SPIEGAMI.md`](SPIEGAMI.md) — non-technical explanation in Italian.

## License

The repository includes the [MIT License](LICENSE) for its software.

The public manuscripts have their own publication records and applicable arXiv licensing terms. Consult those records when reusing manuscript content; the software license should not be assumed to determine every publication or third-party reuse right.
