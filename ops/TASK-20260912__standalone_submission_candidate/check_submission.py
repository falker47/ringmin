"""Independently audit the final standalone source bundle and two clean PDFs.

Read-only apart from this dossier's PACKAGE_CHECK.json. This checker never
invokes a builder or a historical auditor's main function. It checks package
engineering and unchanged mathematical notation, not theorem correctness,
external peer review, visual layout, or arXiv's actual compilation.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
STARTING_COMMIT = '87a163289be1326c9864b359ca8e12b3de08ec75'
SUPPLEMENT_COMMIT = '3beb8d70c5b3748d370a92855847bdf574e5a14f'
STEM = 'ringmin_asymptotic'
SOURCE_NAME = STEM + '.tex'
CANDIDATE = ROOT / 'paper_assets/asymptotic_sequel'
STATUS = 'ARXIV_SUBMISSION_CANDIDATE'
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    'historical_pdf_objects', ROOT / 'ops/TASK-20260911__arxiv_submission_audit/check_bundle.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
require, sha = audit.require, audit.sha

WORKFLOW = re.compile(
    r'\b(?:draft|candidate|review copy|not submitted|ready for review|'
    r'pending submission|unsubmitted|placeholder|TODO|FIXME)\b|'
    r'READY_FOR_REVIEW|ARXIV_SUBMISSION_CANDIDATE|PENDING_STANDALONE|'
    r'AWAITING_STANDALONE|EDITORIALLY_SUPERSEDED|TASK-\d{8}', re.I)
MACHINE_PATH = re.compile(r'(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|file://')
WARNING = re.compile(
    r'Overfull |Underfull |Missing character|undefined|multiply defined|'
    r'Rerun to get|Label\(s\) may have changed|Package .* Warning|'
    r'LaTeX Warning|destination with the same identifier')
MATH = re.compile(
    r'(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$|'
    r'\\\[.*?\\\]|\\\(.*?\\\)|'
    r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}'
    r'.*?\\end\{\1\}', re.S)


def scientific_tokens(tex):
    """Exclude editorial bibliography; retain ordered, whitespace-normalized math."""
    scientific = tex.split(r'\begin{thebibliography}', 1)[0]
    return [re.sub(r'\s+', '', match.group(0)) for match in MATH.finditer(scientific)]


def math_declarations(tex):
    return [line.strip() for line in tex.splitlines()
            if line.startswith((r'\newcommand', r'\DeclareMathOperator'))]


def source_checks(tex):
    require(WORKFLOW.search(tex) is None, 'Manuscript contains a workflow marker')
    require(MACHINE_PATH.search(tex) is None, 'Manuscript contains a machine path')
    require(re.search(r'\\(?:input|include|includegraphics|bibliography|write18|'
                      r'openout|read|directlua|pdfobj|pdfannot)\b|'
                      r'API_KEY|SECRET_KEY|PRIVATE KEY|(?<!\\)%', tex) is None,
            'Source dependency, active primitive, secret or comment')
    require(all(line == line.rstrip() for line in tex.splitlines()), 'Source whitespace')
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
    bibliography = re.findall(r'\\bibitem\{([^}]+)\}', tex)
    citations = [key.strip()
                 for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', tex)
                 for key in group.split(',')]
    require(len(labels) == len(set(labels)), 'Duplicate TeX labels')
    require(set(refs) <= set(labels), 'Unresolved TeX reference')
    require(len(bibliography) == len(set(bibliography)), 'Duplicate bibliography keys')
    require(set(citations) <= set(bibliography), 'Unresolved citation')
    require(set(bibliography) == set(citations), 'Unused bibliography entry')
    require('https://arxiv.org/abs/2607.28654v1' in tex, 'Missing historical v1 citation')
    github_links = re.findall(r'https://github\.com/[^}\s]+', tex)
    require(github_links and all(SUPPLEMENT_COMMIT in url for url in github_links),
            'Supplement citation is not pinned to the selected immutable commit')
    return {'labels': len(labels), 'bibliography_keys': len(bibliography),
            'github_links': github_links}


def metadata_checks(tex, metadata):
    title = re.search(r'\\title\{([^}]+)\}', tex).group(1)
    title = re.sub(r'\s+', ' ', title.replace(r'\\', ' ')).strip()
    author = re.search(r'\\author\{([^}]+)\}', tex).group(1).strip()
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex, re.S).group(1)
    abstract = re.sub(r'\s+', ' ', abstract).strip()
    for before, after in [(r'\Rstar', r'{R^\ast}'), (r'\CC', r'{C_\ast}'),
                          (r'\rm term', r'\mathrm{term}'),
                          (r'\rm width', r'\mathrm{width}')]:
        abstract = abstract.replace(before, after)
    require(set(re.findall(r'\\([A-Za-z]+)', abstract)) <=
            {'ast', 'ldots', 'dots', 'pi', 'mathrm', 'eta', 'le'},
            'Abstract contains unexpanded or accidentally joined macro')
    require(abstract.isascii() and len(abstract) <= 1920, 'Abstract encoding/length')
    require(metadata['Title'] == title and metadata['Authors'] == author,
            'Source title/author disagrees with submission metadata')
    require(metadata['Abstract'] == abstract, 'Source abstract disagrees with metadata')
    require(metadata['Status'] == STATUS and metadata['Processor'] == 'pdflatex'
            and metadata['Main file'] == SOURCE_NAME, 'Submission identity mismatch')
    require(isinstance(metadata['Pages'], int) and metadata['Pages'] > 0, 'Invalid page count')
    return {'title': title, 'author': author, 'abstract_characters': len(abstract)}


def check_math(baseline, tex):
    before = 'The integer gate keeps the final'
    after = 'The lower bound on $m$ keeps the final'
    require(baseline.count(before) == tex.count(after) == 1,
            'Expected reviewed editorial clarification missing or duplicated')
    original, current = scientific_tokens(baseline), scientific_tokens(tex.replace(after, before))
    require(original == current, 'Scientific mathematical expressions changed')
    require(math_declarations(baseline) == math_declarations(tex), 'Math macro definition changed')
    return {'starting_commit': STARTING_COMMIT, 'expressions': len(current),
            'current_expression_count': len(scientific_tokens(tex)),
            'reviewed_editorial_addition': {'before': before, 'after': after,
                                           'added_math_token': '$m$'},
            'macro_declarations': len(math_declarations(tex)),
            'ordered_math_sha256': hashlib.sha256('\n'.join(current).encode()).hexdigest(),
            'bibliography_excluded': True, 'whitespace_normalized': True}


def file_record(path, record):
    require(path.stat().st_size == record['bytes'], 'Manifest byte-size drift: ' + path.name)
    require(sha(path) == record['sha256'], 'Manifest SHA-256 drift: ' + path.name)


def dependencies_and_log(clean, manifest):
    dependencies = {}
    for line in (clean / (STEM + '.fls')).read_text().splitlines():
        if not line.startswith('INPUT '):
            continue
        item = Path(line[6:])
        item = (item if item.is_absolute() else clean / item).resolve()
        if item.is_relative_to(clean):
            require(item.relative_to(clean).as_posix() in
                    {SOURCE_NAME, STEM + '.aux', STEM + '.out'}, 'Unexpected local TeX input')
        else:
            match = re.search(r'/(texmf-(?:dist|var|config))/', item.as_posix(), re.I)
            if match:
                key = item.as_posix()[match.start() + 1:]
            else:
                require(item.name == 'texmf.cnf' and (item.parent / 'texmf-dist').is_dir(),
                        'Input outside the bundle and TeX distribution')
                key = 'distribution-root/texmf.cnf'
            value = sha(item)
            require(key not in dependencies or dependencies[key] == value,
                    'Ambiguous TeX dependency key')
            dependencies[key] = value
    require(dependencies, 'No system dependencies recorded')
    log = (clean / (STEM + '.log')).read_text(errors='replace')
    require(not any(WARNING.search(line) for line in log.splitlines()),
            'Clean compilation contains unresolved warnings')
    require(log.splitlines()[0].split('  ')[0] == manifest['engine'], 'TeX engine mismatch')
    require('Output written on ' + STEM + '.pdf' in log, 'No completed PDF in clean log')
    return dependencies


def pdf_pair(approved, clean, metadata):
    other, comparison = audit.inspect_pdf(clean / (STEM + '.pdf'))
    final, report = approved
    pages = metadata['Pages']
    require(len(final.pages) == len(other.pages) == pages, 'PDF page-count mismatch')
    require(final.page_labels == other.page_labels == [str(i) for i in range(1, pages + 1)],
            'PDF page labels are not consecutive')
    require(report['metadata'] == comparison['metadata'], 'PDF metadata differs')
    require(report['metadata']['/Title'] == metadata['Title'] and
            report['metadata']['/Author'] == metadata['Authors'], 'PDF title/author mismatch')
    page_records = []
    for index, (one, two) in enumerate(zip(final.pages, other.pages), 1):
        first, second = one.extract_text(), two.extract_text()
        require(first == second, f'Page {index} text differs')
        require(len(first.strip()) > 80, f'Page {index} blank or malformed')
        require(first.rstrip().splitlines()[-1].strip() == str(index),
                f'Page {index} printed number mismatch')
        require(WORKFLOW.search(first) is None and MACHINE_PATH.search(first) is None,
                f'Page {index} contains workflow text or a machine path')
        require(one.mediabox == two.mediabox and one.cropbox == two.cropbox,
                f'Page {index} dimensions differ')
        content = one.get_contents().get_data()
        require(content == two.get_contents().get_data(), f'Page {index} painting differs')
        page_records.append({'page': index, 'text_sha256': hashlib.sha256(first.encode()).hexdigest(),
                             'painting_sha256': hashlib.sha256(content).hexdigest()})
    require(report['embedded_fonts'] == comparison['embedded_fonts'], 'Embedded fonts differ')
    require(report['external_uris'] == comparison['external_uris'], 'External links differ')
    return {'sha256': comparison['sha256'], 'exact_page_content_match': True,
            'consecutive_printed_page_numbers': True, 'pages': page_records}


def tamper_controls(tex, metadata, baseline, record):
    """In-memory negative controls exercise independent rejection mechanisms."""
    cases = {
        'workflow_marker': lambda: source_checks(tex + '\nReview copy\n'),
        'duplicate_label': lambda: source_checks(tex + '\\label{sec:line}'),
        'undefined_citation': lambda: source_checks(tex + '\\cite{missing-control}'),
        'external_source_input': lambda: source_checks(tex + '\\input{extra.tex}'),
        'wrong_title': lambda: metadata_checks(tex, dict(metadata, Title='Wrong title')),
        'wrong_abstract': lambda: metadata_checks(tex, dict(metadata, Abstract='Wrong abstract')),
        'changed_formula': lambda: check_math(baseline, tex.replace('$1/8$', '$1/9$', 1)),
        'changed_macro': lambda: check_math(baseline, tex.replace(r'{R^\ast}', r'{R^2}', 1)),
        'wrong_source_hash': lambda: file_record(CANDIDATE / SOURCE_NAME,
                                                dict(record, sha256='0' * 64)),
        'wrong_source_size': lambda: file_record(CANDIDATE / SOURCE_NAME,
                                                dict(record, bytes=record['bytes'] + 1)),
    }
    for name, operation in cases.items():
        try:
            operation()
        except RuntimeError:
            continue
        raise RuntimeError('Tamper control was not rejected: ' + name)
    return list(cases)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('builder_clean_directory', type=Path)
    parser.add_argument('independent_clean_directory', type=Path)
    args = parser.parse_args()
    clean_dirs = [args.builder_clean_directory.resolve(), args.independent_clean_directory.resolve()]
    require(clean_dirs[0] != clean_dirs[1], 'Two distinct clean compilations required')
    source = CANDIDATE / SOURCE_NAME
    bundle = CANDIDATE / 'source_bundle'
    require(sorted(p.relative_to(bundle).as_posix() for p in bundle.rglob('*')) == [SOURCE_NAME],
            'Source-only bundle must contain exactly one TeX source and no directories')
    require(all(source.read_bytes() == (directory / SOURCE_NAME).read_bytes()
                for directory in [bundle, *clean_dirs]), 'Source/bundle/clean byte mismatch')
    tex = source.read_text(encoding='utf-8')
    manifest = json.loads((CANDIDATE / 'BUILD_MANIFEST.json').read_text())
    metadata = json.loads((CANDIDATE / 'ARXIV_METADATA.json').read_text())
    require(manifest['status'] == STATUS, 'Manifest is not the submission candidate')
    require(manifest['main_file'] == SOURCE_NAME and manifest['processor'] == 'pdflatex',
            'Manifest main source/processor mismatch')
    require(manifest['passes'] >= 3 and manifest['warnings'] == [], 'Build gates not recorded')
    require(manifest['scientific_supplement_commit'] == SUPPLEMENT_COMMIT, 'Supplement drift')
    require(len(manifest['source_files']) == 1 and
            manifest['source_files'][0]['name'] == SOURCE_NAME, 'Manifest source inventory mismatch')
    record = manifest['source_files'][0]
    file_record(source, record)
    require(manifest['pdf']['name'] == STEM + '.pdf', 'Manifest PDF name mismatch')
    file_record(CANDIDATE / (STEM + '.pdf'), manifest['pdf'])
    file_record(ROOT / 'paper_assets/build_publications.py',
                {'bytes': manifest['builder_bytes'], 'sha256': manifest['builder_sha256']})
    report = source_checks(tex)
    report.update(metadata_checks(tex, metadata))
    baseline = subprocess.run(
        ['git', '-c', 'safe.directory=' + ROOT.as_posix(), 'show',
         STARTING_COMMIT + ':paper_assets/asymptotic_sequel/' + SOURCE_NAME],
        cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    report['unchanged_scientific_notation'] = check_math(baseline, tex)
    approved = audit.inspect_pdf(CANDIDATE / (STEM + '.pdf'))
    report['pdf'] = approved[1]
    report['clean_builds'] = {}
    for kind, directory in zip(('builder', 'independent'), clean_dirs):
        result = pdf_pair(approved, directory, metadata)
        result['tex_dependencies'] = dependencies_and_log(directory, manifest)
        report['clean_builds'][kind] = result
    require(report['clean_builds']['builder']['tex_dependencies'] ==
            report['clean_builds']['independent']['tex_dependencies'], 'TeX dependency snapshots differ')
    report['tamper_controls_rejected'] = tamper_controls(tex, metadata, baseline, record)
    report.update(status='PASS', classification='engineering fact; local internal validation',
                  source_files=manifest['source_files'], source_sha256=sha(source),
                  builder_sha256=manifest['builder_sha256'], python_version=sys.version.split()[0],
                  checker_sha256=sha(Path(__file__)),
                  limitations=['Does not prove mathematical statements or certify finite optima.',
                               'Math comparison excludes bibliography and normalizes whitespace; prose requires review.',
                               'Uses historical PDF object inspection as a read-only helper; no builder imports.',
                               'Visual inspection and actual arXiv compilation are separate gates.',
                               'No hosted CI or external acceptance is inferred.'])
    Path(__file__).with_name('PACKAGE_CHECK.json').write_text(
        json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'PASS one source; {report["labels"]} labels; {report["bibliography_keys"]} references; '
          f'{report["unchanged_scientific_notation"]["expressions"]} unchanged mathematical expressions')
    print(f'PASS two clean builds; {metadata["Pages"]} exact pages with consecutive numbers; '
          f'{len(report["pdf"]["embedded_fonts"])} embedded scalable fonts; no active content')
    print(f'PASS source/PDF/builder hashes and sizes; metadata; '
          f'{len(report["tamper_controls_rejected"])} rejected tamper controls; PACKAGE_CHECK.json')


if __name__ == '__main__':
    main()
