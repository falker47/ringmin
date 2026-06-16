# Submission Checklist

## Pre-Submission Repo Checks

- [ ] Confirm `python -m pytest` passes from a clean checkout.
- [ ] Confirm `python verify.py --start 3 --stop 8` passes as a quick verifier smoke test.
- [ ] Confirm `python verify.py --start 3 --stop 14` passes before submission if time permits.
- [ ] Confirm no certified artifacts under `results/nNN/`, `results/frontiers/`, or `paper_assets/*.csv` changed unintentionally.
- [ ] Confirm `README.md`, `ENDORSEMENT_SUMMARY.md`, and `SUBMISSION_CHECKLIST.md` agree on certified versus heuristic claims.
- [ ] Confirm `.github/workflows/ci.yml` is present and lightweight.

## Paper Checks

- [ ] Compile `paper_assets/ringmin_paper.tex` twice with `pdflatex`.
- [ ] Read the abstract and introduction for clear separation between proved results, certified computations, heuristic evidence, and conjectures.
- [ ] Check that theorem/proposition statements have not been weakened or inflated accidentally.
- [ ] Check that tables of numerical values match the saved artifacts.
- [ ] Check the AI-assistance acknowledgment is concise and professional.
- [ ] Bibliography TODO: decide whether the current references are sufficient for submission context. Do not add new entries unless metadata is verified from reliable sources.

## Reproducibility Checks

- [ ] Use `requirements.txt` for the exact submission-gate dependency versions.
- [ ] Confirm `pyproject.toml` remains suitable for editable installs.
- [ ] Confirm long-running commands are not represented as quick checks.
- [ ] Confirm `verify.py` still imports only the standard library and `mpmath`.
- [ ] Confirm regenerated paper assets are intentionally reviewed before committing.

## arXiv Category Decision

- [ ] Choose primary category: `math.MG`, `math.CO`, or `cs.CG`.
- [ ] `math.MG`: strongest for the circle-tangency problem statement and geometric feasibility.
- [ ] `math.CO`: strongest for the Supnick/anti-Monge TSP theorem and exhaustive ordering certificate.
- [ ] `cs.CG`: plausible if emphasizing computational geometry and certified search, but likely less natural as the primary category.
- [ ] Prepare a one-sentence category rationale for the endorsement email.

## GitHub-Facing Recommendations

- [ ] Repository description: `Certified computations and Supnick/anti-Monge TSP proof for arranging circles around a central circle.`
- [ ] Suggested topics: `circle-packing`, `discrete-geometry`, `computational-geometry`, `monge-arrays`, `traveling-salesman-problem`, `reproducible-research`, `certified-computation`.
- [ ] Suggested release tag: `v0.1-submission`.
- [ ] Optional after release: archive the release on Zenodo and add the DOI only after Zenodo issues it.

## Endorsement-Email Preparation

- [ ] Select recipients whose work is close to discrete geometry, Monge/Supnick TSPs, or computational geometry.
- [ ] Personalize the template in `endorsement/email_templates.md`.
- [ ] Include the paper PDF link, repository link, proposed category, and arXiv endorsement code/link.
- [ ] State that the author is an independent researcher.
- [ ] State that endorsement is not a request for peer review.

## Remaining Human-Only Steps

- [ ] Decide the final title/version/date shown in the paper.
- [ ] Choose the primary arXiv category and any cross-listing strategy.
- [ ] Generate or confirm the arXiv endorsement code/link.
- [ ] Send endorsement requests manually.
- [ ] Review arXiv source upload contents and remove stale build artifacts if needed.
- [ ] Make the submission release and optional Zenodo archive after final review.
