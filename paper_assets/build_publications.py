"""Build the standalone submission candidate or pending finite correction.

The source bundles also compile directly with pdflatex, without this script.
No historical asset is modified. Matching bytes requires matching TeX inputs.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import uuid


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = {
    'sequel': ('asymptotic_sequel', 'ringmin_asymptotic', 'ARXIV_SUBMISSION_CANDIDATE'),
    'correction': ('v1_correction', 'ringmin_finite_v2',
                   'AWAITING_STANDALONE_ARXIV_ID'),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(key, engine):
    dirname, stem, status = CANDIDATES[key]
    candidate = ROOT / 'paper_assets' / dirname
    inputs = [stem + '.tex']
    if key == 'correction':
        inputs += ['appendix_tables.tex', 'figures/n14.png', 'figures/radii_vs_n.png']
    bundle = candidate / 'source_bundle'
    bundle.mkdir(exist_ok=True)
    existing = {p.relative_to(bundle).as_posix()
                for p in bundle.rglob('*') if p.is_file()}
    if existing - set(inputs):
        raise RuntimeError('Unexpected bundle inputs: ' + repr(existing - set(inputs)))
    work = ROOT / 'reproducibility' / '.work' / ('publication-' + key + '-' + uuid.uuid4().hex)
    work.mkdir(parents=True)
    for name in inputs:
        source = candidate / name
        for destination in (bundle / name, work / name):
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
    env = dict(os.environ, SOURCE_DATE_EPOCH='1789084800', FORCE_SOURCE_DATE='1',
               TEXINPUTS='.' + os.pathsep)
    args = [engine, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
            '-file-line-error', '-recorder', stem + '.tex']
    previous = None
    for passes in range(1, 6):
        proc = subprocess.run(args, cwd=work, env=env, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
        (work / f'pass-{passes}.txt').write_bytes(proc.stdout)
        if proc.returncode:
            raise RuntimeError(f'{key} pass {passes} exit={proc.returncode}; '
                               f'log {work.relative_to(ROOT).as_posix()}/pass-{passes}.txt')
        state = [sha(work / (stem + ext)) for ext in ('.aux', '.out')]
        if passes >= 3 and state == previous:
            break
        previous = state
    else:
        raise RuntimeError('References did not stabilize in five passes')
    log = (work / (stem + '.log')).read_text(errors='replace')
    warnings = [line for line in log.splitlines() if re.search(
        r'Overfull |Underfull |Missing character|undefined|multiply defined|'
        r'Rerun to get|Label\(s\) may have changed|Package .* Warning|'
        r'LaTeX Warning|destination with the same identifier', line)]
    if warnings:
        raise RuntimeError(f'{key} final log requires review: {warnings}; '
                           + work.relative_to(ROOT).as_posix())
    shutil.copyfile(work / (stem + '.pdf'), candidate / (stem + '.pdf'))
    manifest = {
        'status': status,
        'publication_action': ('author to create a NEW arXiv submission and inspect server PDF'
                               if key == 'sequel' else 'none; independent review pending'),
        'source_date_epoch': 1789084800,
        'command': f'python paper_assets/build_publications.py {key}',
        'direct_compile': ' '.join(['pdflatex'] + args[1:]),
        'engine': log.splitlines()[0].split('  ')[0],
        'passes': passes, 'warnings': warnings,
        'source_files': [{'name': name, 'bytes': (bundle / name).stat().st_size,
                          'sha256': sha(bundle / name)} for name in inputs],
        'pdf': {'name': stem + '.pdf', 'sha256': sha(candidate / (stem + '.pdf'))},
        'builder_sha256': sha(Path(__file__)),
        'scientific_supplement_commit': '3beb8d70c5b3748d370a92855847bdf574e5a14f',
        'publication_generation_commit': 'Containing commit; see git log for this manifest',
        'limits': 'Local TeX Live 2025 package snapshot is newer than arXiv 2025-08-03. '
                  'Byte reproducibility needs identical packages, fonts and input bytes. '
                  'Git line-ending conversion can change text hashes.',
    }
    if key == 'sequel':
        manifest.update(main_file=stem + '.tex', processor='pdflatex',
                        builder_bytes=Path(__file__).stat().st_size)
        manifest['pdf']['bytes'] = (candidate / (stem + '.pdf')).stat().st_size
        write_submission_metadata(candidate, stem, log)
    (candidate / 'BUILD_MANIFEST.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8',
        newline='\n' if key == 'sequel' else None)
    print(f'PASS {key}: {passes} clean passes; stable aux/out; zero warnings', flush=True)
    print('CLEAN_BUILD=' + work.relative_to(ROOT).as_posix(), flush=True)
    print('PDF_SHA256=' + manifest['pdf']['sha256'], flush=True)


def write_submission_metadata(candidate, stem, log):
    """Derive copy-ready fields from the exact manuscript outside the bundle."""
    source = (candidate / (stem + '.tex')).read_text(encoding='utf-8')
    title = re.search(r'pdftitle=\{([^}]+)\}', source).group(1)
    author = re.search(r'\\author\{([^}]+)\}', source).group(1)
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1)
    abstract = re.sub(r'\s+', ' ', abstract).strip()
    for before, after in [(r'\Rstar', r'{R^\ast}'), (r'\CC', r'{C_\ast}'),
                          (r'\rm term', r'\mathrm{term}'),
                          (r'\rm width', r'\mathrm{width}')]:
        abstract = abstract.replace(before, after)
    if (len(abstract) > 1920 or not abstract.isascii() or
            not set(re.findall(r'\\([A-Za-z]+)', abstract)) <=
            {'ast', 'ldots', 'pi', 'mathrm', 'eta', 'le'}):
        raise RuntimeError('Abstract needs an explicit metadata expansion')
    pages = int(re.search(r'Output written on .*?\((\d+) pages?', log, re.S).group(1))
    supplement = 'https://github.com/falker47/ringmin/tree/3beb8d70c5b3748d370a92855847bdf574e5a14f'
    comments = (f'{pages} pages, no figures. Asymptotic sequel to arXiv:2607.28654v1. '
                'Proves existence and an effective finite-program characterization of the '
                'global asymptotic constant. Proofs and code: ' + supplement)
    license_name = 'arXiv.org perpetual, non-exclusive license'
    license_url = 'https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html'
    metadata = {
        'Status': 'ARXIV_SUBMISSION_CANDIDATE', 'Title': title, 'Authors': author,
        'Abstract': abstract, 'Abstract characters': len(abstract), 'Pages': pages,
        'Comments': comments, 'Primary category': 'cs.CG',
        'Cross-lists recommended': ['math.MG'],
        'MSC2020': {'Primary': ['52C15'], 'Secondary': ['52C26', '90C05']},
        'License guidance': 'Preserve the author\'s choice displayed on arXiv:2607.28654v1: ' + license_name,
        'License URL': license_url, 'Processor': 'pdflatex', 'Main file': stem + '.tex',
        'Submission type': 'NEW', 'Scientific supplement': supplement,
    }
    (candidate / 'ARXIV_METADATA.json').write_text(
        json.dumps(metadata, indent=2) + '\n', encoding='utf-8', newline='\n')
    handoff = f'''# arXiv submission metadata

Copy the fields below for a **NEW** submission. Upload only the contents of
`source_bundle/`; the PDF, manifest and metadata stay outside that directory.
Inspect arXiv's compiled PDF before finalizing the submission.

## Title

{title}

## Authors

{author}

## Abstract

```text
{abstract}
```

## Comments

{comments}

## Classification

- Primary category: `cs.CG` (Computational Geometry).
- Recommended cross-list: `math.MG` (Metric Geometry), subject to arXiv classification.
- MSC2020: Primary `52C15`; Secondary `52C26`, `90C05`.

## License and source

- Preserve the prior paper's author-selected [{license_name}]({license_url}).
  The repository's MIT code license does not select a paper license.
- Processor: `pdflatex`.
- Main source: `{stem}.tex`.
- Leave journal reference, DOI and report number blank; none is assigned here.

The manuscript is {pages} pages. Exact source/PDF hashes are in
[BUILD_MANIFEST.json](BUILD_MANIFEST.json). The machine-readable copy is
[ARXIV_METADATA.json](ARXIV_METADATA.json). This is prepared metadata, not a
record of submission, moderation or external mathematical acceptance.
'''
    (candidate / 'ARXIV_METADATA.md').write_text(handoff, encoding='utf-8', newline='\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', choices=[*CANDIDATES, 'all'])
    parser.add_argument('--engine', default='pdflatex')
    args = parser.parse_args()
    engine = shutil.which(args.engine)
    if engine is None:
        parser.error('pdflatex is required')
    for key in CANDIDATES if args.candidate == 'all' else [args.candidate]:
        build(key, engine)


if __name__ == '__main__':
    main()
