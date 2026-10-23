"""Reproducible standalone and tampering checks. Standard library only."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

if not __debug__:
    raise RuntimeError('Enabled assertions are required; omit -O.')

here=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='ringmin-prop7-') as temp:
    dest=Path(temp)/'standalone'
    dest.mkdir()
    for path in here.iterdir():
        if path.is_file():
            shutil.copyfile(path,dest/path.name)

    def run(*flags):
        return subprocess.run([sys.executable,'-I','-S',*flags,'verify.py'],
                              cwd=dest,capture_output=True,text=True)

    valid=run()
    assert valid.returncode == 0, valid.stderr
    assert '0 repository input hashes' in valid.stdout
    print('PASS standalone copy: full verifier exit 0 with no repository inputs')
    certificate=dest/'certificate.json'
    saved=certificate.read_bytes()
    data=json.loads(saved)
    data['strict_target'][0]='0'
    certificate.write_text(json.dumps(data),encoding='utf-8')
    corrupt=run()
    assert corrupt.returncode != 0 and 'AssertionError' in corrupt.stderr
    certificate.write_bytes(saved)
    print('PASS altered certificate rejected by fresh recomputation')
    readme=dest/'README.md'
    saved=readme.read_bytes()
    readme.write_bytes(saved+b'\nTampering negative control.\n')
    corrupt=run()
    assert corrupt.returncode != 0 and 'README.md' in corrupt.stderr
    readme.write_bytes(saved)
    print('PASS altered packaged document rejected by manifest')
    optimized=run('-O')
    assert optimized.returncode != 0 and 'Enabled assertions' in optimized.stderr
    print('PASS Python -O rejected explicitly')
print('PASS package integrity controls; no delivered file modified')
