"""Inspect actual clean-build dependencies, source hygiene and PDF objects."""
from pathlib import Path
import argparse
import hashlib
import json
import re

from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_pdf(path):
    reader = PdfReader(path, strict=True)
    require(not reader.is_encrypted, 'Encrypted PDF')
    seen = set()
    fonts = {}
    uris = set()
    active = {'/JavaScript', '/JS', '/AA', '/EmbeddedFiles', '/Launch',
              '/RichMedia', '/XFA', '/AcroForm'}

    def walk(obj):
        if isinstance(obj, IndirectObject):
            identity = (obj.idnum, obj.generation)
            if identity in seen:
                return
            seen.add(identity)
            obj = obj.get_object()
        if isinstance(obj, DictionaryObject):
            require(not (active & set(obj)), 'Active content or attachment found')
            if '/S' in obj:
                require(str(obj['/S']) not in {'/JavaScript', '/Launch', '/GoToR',
                        '/SubmitForm', '/ImportData', '/Rendition', '/Movie', '/Sound'},
                        'Disallowed action found')
            if '/URI' in obj:
                uri = str(obj['/URI'])
                require(uri.startswith('https://'), 'Non-HTTPS external link')
                uris.add(uri)
            if obj.get('/Type') == '/Font' and '/BaseFont' in obj:
                require(obj.get('/Subtype') != '/Type3', 'Bitmap Type 3 font')
                descriptor = obj.get('/FontDescriptor')
                if descriptor is not None:
                    descriptor = descriptor.get_object()
                    streams = [key for key in ('/FontFile', '/FontFile2', '/FontFile3')
                               if key in descriptor]
                    require(streams, 'Unembedded font')
                    fonts[str(obj['/BaseFont'])] = {
                        'subtype': str(obj['/Subtype']),
                        'embedding': streams[0],
                        'stream_sha256': hashlib.sha256(
                            descriptor[streams[0]].get_data()).hexdigest(),
                    }
                else:
                    require('/DescendantFonts' in obj, 'Font has no embedding descriptor')
            for value in obj.values():
                walk(value)
        elif isinstance(obj, ArrayObject):
            for value in obj:
                walk(value)

    walk(reader.trailer['/Root'])
    require(fonts, 'No fonts inspected')
    return reader, {'pages': len(reader.pages), 'metadata': dict(reader.metadata),
                    'embedded_fonts': fonts, 'external_uris': sorted(uris),
                    'active_content': False, 'sha256': sha(path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('clean_directory', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    clean = args.clean_directory.resolve()
    bundle = root / 'paper_assets/v2/arxiv_submission'
    candidate = root / 'paper_assets/v2'
    require(sorted(p.name for p in bundle.iterdir()) == ['ringmin_v2.tex'],
            'Unexpected public bundle file')
    source = bundle / 'ringmin_v2.tex'
    require(source.read_bytes() == (candidate / source.name).read_bytes()
            == (clean / source.name).read_bytes(), 'TeX copies differ')
    tex = source.read_text(encoding='utf-8')
    forbidden = (r'\\(?:input|include|includegraphics|bibliography|write18|openout|'
                 r'read|directlua|pdfobj|pdfannot)\b|(?<![A-Za-z])[A-Za-z]:[\\/]|'
                 r'/Users/|/home/|file://|(?:API_KEY|SECRET_KEY|PRIVATE KEY)|'
                 r'(?<!\\)%')
    require(re.search(forbidden, tex) is None,
            'External source input, machine path, active primitive, secret or comment')
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    require(len(labels) == len(set(labels)), 'Duplicate TeX labels')
    refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
    require(set(refs) <= set(labels), 'Unresolved source cross-reference')
    bib = re.findall(r'\\bibitem\{([^}]+)\}', tex)
    require(len(bib) == len(set(bib)), 'Duplicate bibliography keys')
    cites = [key for group in re.findall(r'\\cite\{([^}]+)\}', tex)
             for key in group.split(',')]
    require(set(cites) <= set(bib), 'Unresolved source citation')
    dependencies = {}
    for line in (clean / 'ringmin_v2.fls').read_text().splitlines():
        if not line.startswith('INPUT '):
            continue
        raw = line[6:]
        item = Path(raw)
        if not item.is_absolute():
            item = clean / item
        item = item.resolve()
        if item.is_relative_to(clean):
            require(item.name in {'ringmin_v2.tex', 'ringmin_v2.aux', 'ringmin_v2.out'},
                    'Unexpected local compilation input')
            continue
        portable = item.as_posix()
        match = re.search(r'/(texmf-(?:dist|var|config))/', portable, flags=re.I)
        if match is not None:
            key = portable[match.start() + 1:]
        else:
            require(item.name == 'texmf.cnf' and (item.parent / 'texmf-dist').is_dir(),
                    'Compilation input outside bundle and TeX trees')
            key = 'distribution-root/texmf.cnf'
        dependencies[key] = sha(item)
    final, report = inspect_pdf(clean / 'ringmin_v2.pdf')
    approved, candidate_report = inspect_pdf(candidate / 'ringmin_v2.pdf')
    require(len(final.pages) == len(approved.pages) == 9, 'Unexpected page count')
    require(report['metadata'] == candidate_report['metadata'], 'PDF metadata differs')
    for index, (one, two) in enumerate(zip(final.pages, approved.pages), 1):
        require(one.extract_text() == two.extract_text(), f'Page {index} text differs')
        require(one.get_contents().get_data() == two.get_contents().get_data(),
                f'Page {index} painting instructions differ')
        require(one.mediabox == two.mediabox, f'Page {index} size differs')
    require(report['embedded_fonts'] == candidate_report['embedded_fonts'], 'Fonts differ')
    require(report['external_uris'] == candidate_report['external_uris'], 'Links differ')
    expected_title = ('Minimum central circles: certified finite optima and '
                      'an effective global asymptotic constant')
    require(report['metadata']['/Title'] == expected_title, 'PDF title mismatch')
    require(report['metadata']['/Author'] == 'Maurizio Falconi', 'PDF author mismatch')
    report.update(source_sha256=sha(source), candidate_pdf_sha256=candidate_report['sha256'],
                  source_files=['ringmin_v2.tex'], tex_dependencies=dependencies,
                  labels=len(labels), citation_keys=len(bib),
                  exact_page_content_match=True, pdf_metadata_match=True,
                  local_environment='pdfTeX 1.40.28 / TinyTeX TeX Live 2025; packages updated after arXiv snapshot')
    output = Path(__file__).with_name('BUNDLE_CHECK.json')
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'PASS one source; {len(labels)} unique labels; {len(bib)} bibliography keys; '
          f'{len(dependencies)} TeX-system inputs only')
    print(f'PASS 9 pages identical in text, painting instructions, dimensions and metadata; '
          f'{len(report["embedded_fonts"])} embedded scalable fonts; no active content')
    print('PASS source hygiene; exact HTTPS link inventory; evidence BUNDLE_CHECK.json')


if __name__ == '__main__':
    main()
