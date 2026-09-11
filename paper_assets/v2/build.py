"""Build the explicitly versioned candidate; never touch historical v1 assets."""
from pathlib import Path
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine', default='pdflatex')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    build = root / 'reproducibility' / '.work' / 'paper-v2'
    build.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    epoch = int(datetime(2026, 9, 11, tzinfo=timezone.utc).timestamp())
    env.update(SOURCE_DATE_EPOCH=str(epoch), FORCE_SOURCE_DATE='1')
    engine = shutil.which(args.engine)
    if engine is None:
        raise SystemExit('pdflatex is required; use --engine to name an installed executable')
    command = [engine, '-interaction=nonstopmode', '-halt-on-error',
               '-output-directory='+build.as_posix(),
               'paper_assets/v2/ringmin_v2.tex']
    for _ in range(2):
        result = subprocess.run(command, cwd=root, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(result.stdout)
        if result.returncode:
            raise SystemExit(result.returncode)
    log = (build/'ringmin_v2.log').read_text(errors='replace')
    for failure in ('Overfull ', 'undefined references', 'Citation ',
                    'There were undefined', 'Rerun to get cross-references right'):
        if failure in log:
            raise SystemExit('Build requires review: '+failure)
    data = (build/'ringmin_v2.pdf').read_bytes()
    (here/'ringmin_v2.pdf').write_bytes(data)
    metadata = {
        'status':'Versioned v2 / journal candidate; not submitted',
        'source_date_epoch':epoch,
        'command':'python paper_assets/v2/build.py',
        'engine':log.splitlines()[0].split('  ')[0],
        'passes':2,
        'files':{name:hashlib.sha256((here/name).read_bytes()).hexdigest()
                 for name in ('ringmin_v2.tex','build.py','ringmin_v2.pdf')},
        'supplement_math_checkpoint':'13ddb41180b3911940f4fe5cf7d61c0545f9f834',
        'limits':'PDF reproducibility additionally requires the same TeX packages/fonts. '
                 'Complete final source and review evidence are identified by the containing Git commit.'}
    (here/'BUILD_MANIFEST.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf-8')
    print('PASS versioned PDF built; source/PDF/build hashes recorded')


if __name__ == '__main__':
    main()
