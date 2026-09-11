"""Independently inspect source inventories, actual TeX inputs and PDF objects."""
from pathlib import Path
import argparse
import importlib.util
import json
import re


ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    'prior_pdf_auditor', ROOT / 'ops/TASK-20260911__arxiv_submission_audit/check_bundle.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
require, sha = audit.require, audit.sha
DATA = {
    'sequel': ('asymptotic_sequel', 'ringmin_asymptotic', 8,
               'Minimum central circles: an effective characterization of the global asymptotic constant'),
    'correction': ('v1_correction', 'ringmin_finite_v2', 12,
                  'Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP and certified finite optima'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', choices=DATA)
    parser.add_argument('clean_directory', type=Path)
    args = parser.parse_args()
    dirname, stem, pages, title = DATA[args.candidate]
    candidate = ROOT / 'paper_assets' / dirname
    bundle = candidate / 'source_bundle'
    clean = args.clean_directory.resolve()
    manifest = json.loads((candidate / 'BUILD_MANIFEST.json').read_text())
    inputs = {row['name'] for row in manifest['source_files']}
    require(inputs == ({stem + '.tex'} if args.candidate == 'sequel' else
                       {stem + '.tex', 'appendix_tables.tex', 'figures/n14.png',
                        'figures/radii_vs_n.png'}), 'Manifest input mismatch')
    require({p.relative_to(bundle).as_posix() for p in bundle.rglob('*') if p.is_file()}
            == inputs, 'Extra bundle files')
    for name in inputs:
        require((candidate / name).read_bytes() == (bundle / name).read_bytes()
                == (clean / name).read_bytes(), 'Source/candidate/clean input drift')
    for row in manifest['source_files']:
        require(sha(bundle / row['name']) == row['sha256'], 'Manifest input hash drift')
    tex = '\n'.join((bundle / name).read_text(encoding='utf-8')
                    for name in sorted(inputs) if name.endswith('.tex'))
    forbidden = (r'(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|file://|'
                 r'API_KEY|SECRET_KEY|PRIVATE KEY|'
                 r'\\(?:write18|openout|read|directlua|pdfobj|pdfannot)\b|(?<!\\)%')
    require(re.search(forbidden, tex) is None, 'Source hygiene or active primitive')
    require(all(line == line.rstrip() for line in tex.splitlines()), 'Source whitespace')
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
    bib = re.findall(r'\\bibitem\{([^}]+)\}', tex)
    cites = [item.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', tex)
             for item in group.split(',')]
    require(len(labels) == len(set(labels)) and set(refs) <= set(labels), 'Source labels')
    require(len(bib) == len(set(bib)) and set(cites) <= set(bib), 'Source bibliography')
    dependencies = {}
    for line in (clean / (stem + '.fls')).read_text().splitlines():
        if not line.startswith('INPUT '):
            continue
        item = Path(line[6:])
        item = (item if item.is_absolute() else clean / item).resolve()
        if item.is_relative_to(clean):
            require(item.relative_to(clean).as_posix() in inputs | {stem + '.aux', stem + '.out'},
                    'Unexpected local TeX input')
        else:
            match = re.search(r'/(texmf-(?:dist|var|config))/', item.as_posix(), flags=re.I)
            if match:
                key = item.as_posix()[match.start() + 1:]
            else:
                require(item.name == 'texmf.cnf' and (item.parent / 'texmf-dist').is_dir(),
                        'Dependency outside bundle and TeX system')
                key = 'distribution-root/texmf.cnf'
            dependencies[key] = sha(item)
    final, report = audit.inspect_pdf(candidate / (stem + '.pdf'))
    other, comparison = audit.inspect_pdf(clean / (stem + '.pdf'))
    require(len(final.pages) == len(other.pages) == pages, 'Page count changed')
    require(report['metadata'] == comparison['metadata'], 'PDF metadata mismatch')
    require(report['metadata']['/Title'] == title and
            report['metadata']['/Author'] == 'Maurizio Falconi', 'Title/author mismatch')
    for one, two in zip(final.pages, other.pages):
        require(one.extract_text() == two.extract_text() and one.mediabox == two.mediabox
                and one.get_contents().get_data() == two.get_contents().get_data(),
                'Page text/painting/dimensions differ')
    require(report['embedded_fonts'] == comparison['embedded_fonts'], 'Fonts differ')
    source = (bundle / (stem + '.tex')).read_text(encoding='utf-8')
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1)
    abstract = re.sub(r'\s+', ' ', abstract).strip()
    for before, after in [(r'\Rstar', r'{R^\ast}'), (r'\CC', r'{C_\ast}'),
                          (r'\rm term', r'\mathrm{term}'),
                          (r'\rm width', r'\mathrm{width}')]:
        abstract = abstract.replace(before, after)
    abstract = abstract.replace(r'\cite{sequel}', '(see the cited standalone sequel)')
    require(set(re.findall(r'\\([A-Za-z]+)', abstract)) <=
            {'ast', 'ldots', 'dots', 'pi', 'mathrm', 'eta', 'le'},
            'Unexpanded or accidentally joined abstract macro')
    require(len(abstract) <= 1920 and abstract.isascii(), 'Abstract metadata length/encoding')
    pending = 'PENDING_STANDALONE_ARXIV_ID'
    require((pending in source) == (args.candidate == 'correction'), 'Identifier placeholder status')
    metadata = {'Status': manifest['status'], 'Title': title, 'Authors': 'Maurizio Falconi',
                'Abstract': abstract, 'Abstract characters': len(abstract), 'Pages': pages,
                'Processor': 'pdflatex', 'Main file': stem + '.tex',
                'Primary category proposed from existing record': 'cs.CG', 'Cross-lists': [],
                'Purpose': 'Review consistency record; not an upload authorization',
                'Comments proposal': (f'{pages} pages, no figures. Standalone asymptotic sequel to '
                    'arXiv:2607.28654; prior finite results and model are explicitly attributed. '
                    'Proof and code supplement: https://github.com/falker47/ringmin'
                    if args.candidate == 'sequel' else
                    'Deferred until a real standalone identifier exists; no copy-ready replacement metadata.')}
    (candidate / 'REVIEW_METADATA.json').write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    report.update(source_files=manifest['source_files'], tex_dependencies=dependencies,
                  labels=len(labels), bibliography_keys=len(bib),
                  independent_clean_pdf_sha256=comparison['sha256'],
                  exact_page_content_match=True, pending_identifier=args.candidate == 'correction')
    (Path(__file__).parent / (args.candidate.upper() + '_PACKAGE_CHECK.json')).write_text(
        json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'PASS {args.candidate}: {len(inputs)} inputs; {len(labels)} labels; {len(bib)} references; '
          f'{pages} exact pages; {len(report["embedded_fonts"])} embedded scalable fonts; '
          f'{len(dependencies)} system-only dependencies; no active content; metadata consistent')


if __name__ == '__main__':
    main()
