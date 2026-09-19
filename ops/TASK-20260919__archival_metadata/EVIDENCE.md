# Evidence

## Environment

```text
repository_head=2a1118b1236a8c8f9e356a5e01bd2afb4f689276
platform=Windows / PowerShell
python=3.14.3
dependency_source=isolated CFF tooling under ignored reproducibility/.work/archival_metadata/
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Current CFF describes software and recommends the public finite v2 paper | Engineering fact | CFF schema and rendering checks below | Independent of solver | Not mathematical verification |
| Exact finite bracket scope in the abstract | Inherited computer-certified finite result | [Owning ledger](../../knowledge/CERTIFICATION.md#independent-exact-arithmetic-global-brackets), user-supplied accepted baseline | Prior accepted evidence | No new verifier run or scope extension claimed |
| CFF alone supplies the needed archive metadata | Documented integration behavior | Current official Zenodo documentation below | External primary source | Actual record still requires inspection after archiving |

## Metadata sources checked on 2026-09-19

- [Zenodo CFF support](https://help.zenodo.org/docs/github/describe-software/citation-file/):
  supported fields include title, version, license, type, abstract, authors and keywords.
- [Zenodo JSON guidance](https://help.zenodo.org/docs/github/describe-software/zenodo-json/):
  CFF alone suffices without Zenodo-specific fields; JSON would override it.
- [GitHub citation documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files):
  `preferred-citation` overrides the citation suggestion; `article` renders as
  BibTeX `@article`; GitHub offers APA and BibTeX using `ruby-cff`.
- [cffconvert](https://github.com/citation-file-format/cffconvert): schema validator
  and converters; its conversions do not implement `preferred-citation`, so
  its top-level APA output must not be mistaken for GitHub's preferred citation.

## Expected Zenodo metadata

These are expectations from documented CFF support, not an observed deposit.

| CFF source | Expected archive metadata |
|---|---|
| `type: software` | Software resource |
| `title` | Ringmin: minimum central circle software and exact finite certificates |
| `version` | `1.1.0-dcg-presubmission` |
| `authors` | Sole creator: Maurizio Falconi; no ORCID or affiliation |
| `abstract` | The CFF software/finite-companion description, including certificate scope and pre-submission status |
| `license: MIT` | MIT license |
| `keywords` | The seven current CFF keywords |

The top-level `url` and `repository-code` both identify
`https://github.com/falker47/ringmin`; GitHub release linkage should be supplied
by the integration. Zenodo's documented subset does not promise a structured
publication relation from `preferred-citation` or direct import of every CFF
URL field. Do not assume such a relation was deposited: verify the actual
record next time. The description explicitly names `arXiv:2607.28654v2`.
GitHub should recommend that paper while Zenodo describes the software archive.
No publication date, DOI, grants, communities or journal acceptance is asserted.

## Archival snapshot contents

Archive the complete tracked repository tree at the independently accepted
metadata SHA selected for the candidate tag in [TASK_STATUS.md](TASK_STATUS.md).
Do not substitute the earlier manuscript-only source bundle. In particular retain:

- `CITATION.cff`, `LICENSE`, `README.md`, `pyproject.toml`, `requirements.txt`;
- `src/`, `scripts/`, `tests/`, `.github/` and both standalone verifiers
  `verify_global_brackets.py` and historical `verify.py`;
- `reproducibility/global_brackets/manifest.json`, its README and all preserved
  `originals/` (including explicitly invalid test fixtures in their test role),
  plus tracked `results/` and other reproducibility inputs;
- all of `paper_assets/journal_dcg/`: manuscript and seam sources, both table
  inputs, PDF, build manifest, build/export scripts, README and source map;
- `research/` proof notes (including `GLOBAL_BRACKET_CERTIFICATE.md`), `knowledge/`,
  the index/current-status files and tracked `ops/` audit provenance;
- all other tracked files, including historical public-arXiv sources and the
  separate asymptotic sequel. Their presence preserves repository history and
  context; it does not expand this finite companion's accepted claim scope.

Exclude `.git/`, untracked/ignored working files, caches, rendering/build
intermediates, local checkpoints and the user-exempted untracked
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip`.
The archive is a source-tree snapshot, not a Git-history backup. Verify its
actual member list and hashes against the tagged tree during the release task.

## Commands and checks

All checks below are local unless explicitly marked as hosted UI. Git commands
in the sandbox used a command-scoped `safe.directory` for the repository root;
no persistent Git configuration changed. Each successful command exited 0.

| Command/check | Exact result or material output | What it checks / does not check |
|---|---|---|
| `python -m pip install --target reproducibility/.work/archival_metadata/cff-tools cffconvert==2.0.0 --disable-pip-version-check --no-warn-script-location --retries 0` | Exit 0; `Successfully installed ... cffconvert-2.0.0 ...` | Isolated tooling, not a project dependency change |
| `python -c 'from cffconvert.cli.cli import cli; cli()' --version` | `2.0.0` | Actual validator version |
| `python -c 'from cffconvert.cli.cli import cli; cli()' --validate` | `Citation metadata are valid according to schema version 1.2.0.` | Full CFF schema including preferred citation; independent of production code |
| `python -c 'from cffconvert.cli.cli import cli; cli()' --format zenodo` | Creator `Falconi, Maurizio`, software title, full abstract, all seven keywords, MIT and `1.1.0-dcg-presubmission` | Local conversion preview; not a deposit or full GitHub integration simulation |
| `git diff --exit-code 2a1118b1236a8c8f9e356a5e01bd2afb4f689276 -- . ':(exclude)CITATION.cff' ':(exclude)CURRENT_STATUS.md' ':(exclude)research/NEXT_RESEARCH_STEPS.md'` | No diff, exit 0 | All 695 other baseline tracked paths unchanged, including every protected mathematical/publication input |
| `git tag --list v1.1.0-dcg-presubmission` | No output | Candidate tag absent locally |
| `git ls-remote origin refs/heads/main refs/tags/v1.1.0-dcg-presubmission` | Only `2a1118b1236a8c8f9e356a5e01bd2afb4f689276 refs/heads/main` | Remote baseline matches; candidate tag absent on origin |
| `git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'` | `origin/main` | Existing intended upstream |
| `Get-FileHash paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip -Algorithm SHA256` | SHA-256 below, unchanged | Exempted ZIP preservation |
| `git diff --check` | No output, exit 0 | Tracked-change whitespace; new dossier checked separately |

For the CFF CLI commands, the task-local process environment was set with:

```powershell
$env:PYTHONPATH = (Resolve-Path 'reproducibility/.work/archival_metadata/cff-tools').Path
```

The validator used `jsonschema 3.2.0` and `ruamel.yaml 0.19.1`. Installation
warned about the ambient `chromadb` requirement for newer jsonschema; only the
ignored `--target` directory was populated, and the override was limited to
validator processes. Project dependency files and the ambient installation
were not changed. The final CFF was validated again after its comment edit.

This additional semantic check was executed (exit 0):

```powershell
python -c "from pathlib import Path; import yaml; c=yaml.safe_load(Path('CITATION.cff').read_text(encoding='utf-8')); assert c['authors']==c['preferred-citation']['authors']==[{'family-names':'Falconi','given-names':'Maurizio'}]; assert c['type']=='software' and c['license']=='MIT'; assert c['version']=='1.1.0-dcg-presubmission'; assert c['repository-code']==c['url']=='https://github.com/falker47/ringmin'; assert c['preferred-citation']['url']=='https://arxiv.org/abs/2607.28654v2'; assert not any(k in c for k in ['doi','date-released']); assert not Path('.zenodo.json').exists(); print('PASS: CFF author, type, license, version, URLs and absence checks')"
```

Exact output: `PASS: CFF author, type, license, version, URLs and absence checks`.
A separate `python -` assertion pass also compared the preferred article's
type, title, authors and year against the accepted baseline, inspected tracked
`.gitattributes` for archive exclusions, checked absence of submodules and
compared the ZIP hash. Exact output:

```text
PASS: metadata semantics and preferred-publication identity; no DOI/date/Zenodo JSON; candidate tag absent
PASS: 695 protected tracked paths unchanged; no submodules/export-ignore; exempt ZIP hash unchanged
```

No solver unit suite, exhaustive search, certificate verifier or manuscript
build was run: no code, certificate or publication input changed, and the
all-protected-path diff establishes preservation of the accepted baseline.
These are metadata/preservation checks, not independent mathematical review.

## GitHub citation rendering inspection

Read-only hosted UI inspection of `https://github.com/falker47/ringmin` at
baseline `2a1118b` opened **Cite this repository** and inspected both formats.
It actually displayed the preferred paper, not the stale software version:
APA began `Falconi, M. (2026). Arranging circles...`; BibTeX used
`@article{Falconi_Arranging_circles_of_2026,...}` with author, title, URL and
year. The old URL was `https://arxiv.org/abs/2607.28654` in both formats.

The paper's type/title/author/year are preserved; the updated version-specific
URL is the intended rendering delta. From that live inspection and GitHub's
documented preferred-citation behavior, the expected updated displays are:

```text
Falconi, M. (2026). Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima. https://arxiv.org/abs/2607.28654v2
```

```bibtex
@article{Falconi_Arranging_circles_of_2026,
  author = {Falconi, Maurizio},
  title = {{Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima}},
  url = {https://arxiv.org/abs/2607.28654v2},
  year = {2026}
}
```

Formatting above expands GitHub's compact BibTeX for readability. The arXiv
identifier is retained in CFF; the observed renderer uses the URL rather than
adding an `eprint` field. No fictitious journal or DOI is introduced. A final
live check after the authorized push belongs to the terminal/chat handoff;
this pre-commit record does not claim that the draft is already hosted.

## Artifact and provenance checks

No manuscript, certificate, result, figure or PDF is generated or changed.
Final working-file `CITATION.cff` SHA-256:
`649c075980c6174a45e0ec827c6d48169878e6a5088daa7b475c7c53dab6eb23`.
The exempted ZIP's initial SHA-256 is
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.
The forthcoming tag, GitHub release, Zenodo deposit and DOI do not yet exist
for this candidate; no creation or registration operation is run here.

## Failed checks and negative evidence

Initial unscoped Git calls failed on sandbox ownership, resolved with a
command-scoped safe-directory option. Initial validator download failed on
sandbox network access (exit 1), before an approved network retry. Neither
failure is a CFF validation result.
The attempted `python -m cffconvert` invocation failed (exit 1) because this
package has no `__main__`; inspection of its console entry point identified
`cffconvert.cli.cli:cli`, used successfully above. The approved installation's
files were inaccessible to the sandbox account, so validator inspection and
execution used approved elevated calls. A combined patch was rejected for
targeting `CURRENT_STATUS.md` twice; it made no changes and was reapplied with
one operation per path.

## Final diff inspection

Complete working diff and all three untracked dossier files were read in full.
Only CFF, current status and the finite roadmap entry modify baseline files;
only this dossier adds tracked files. No stable mathematical claim is duplicated
in a new ledger. All protected and generated baseline paths are unchanged.
The remaining untracked ZIP is explicitly exempted and must not be staged.

The final integration pass runs direct whitespace checks on all six task files,
`git diff --check`, stages exactly those six paths, inspects `git diff --cached`
and runs `git diff --cached --check` before committing. The committed file list,
final SHA, normal push result, fresh `git ls-remote` and final `git status --short`
are recorded in the terminal/chat handoff rather than embedding the containing
commit's own hash. No tag/release/deposit/DOI creation is part of that pass.

## Residual uncertainty

Independent review, live Zenodo ingestion and DOI verification remain future
gates. No hosted-CI result or new mathematical verification is claimed.
