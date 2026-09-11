"""One recorded local gate: tracked base plus explicitly listed task delta."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tarfile

root = Path(__file__).resolve().parents[2]
target = root / 'reproducibility/.work/clean-repro'
if target.exists():
    raise SystemExit('fresh target required')
target.mkdir()
base = '13ddb41180b3911940f4fe5cf7d61c0545f9f834'
archive = root / 'reproducibility/.work/clean-base.tar'
subprocess.run(['git', '-c', 'safe.directory='+root.as_posix(), 'archive',
                '--format=tar', '--output='+str(archive), base], check=True, cwd=root)
with tarfile.open(archive) as stream:
    stream.extractall(target, filter='data')
paths = ['.gitignore', 'verify.py', 'scripts/frontier_logs.py',
         'tests/test_frontier_reproduction.py',
         'research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md']
paths += [p.relative_to(root).as_posix() for p in
          sorted((root/'reproducibility/frontier_logs').iterdir())]
for name in paths:
    out = target/name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(root/name, out)
manifest = {p.relative_to(target).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(target.rglob('*')) if p.is_file()}
assert not (target/'results/checkpoints').exists()
dossier = root/'ops/TASK-20260911__portable_frontier_evidence'
(dossier/'CLEAN_SOURCE_MANIFEST.json').write_text(json.dumps({
    'base_commit':base, 'overlaid_paths':paths, 'files':manifest},indent=2)+'\n')
commands = [
    ['scripts/frontier_logs.py','restore'],
    ['-m','pytest','-p','no:cacheprovider','--basetemp=tmp-tests'],
    ['verify.py','--start','3','--stop','8','--skip-frontier'],
    ['verify.py','--start','3','--stop','14'],
    ['-I','-S','ops/TASK-20260911__general_block_transfer/check_general_blocks.py'],
    ['-I','-S','-O','ops/TASK-20260911__general_block_transfer/check_general_blocks.py'],
    ['-I','-S','ops/TASK-20260911__global_variational_limit/check_line_recovery.py'],
    ['-I','-S','-O','ops/TASK-20260911__global_variational_limit/check_line_recovery.py'],
    ['-I','ops/TASK-20260911__global_variational_limit/check_word_lp.py'],
    ['-I','-O','ops/TASK-20260911__global_variational_limit/check_word_lp.py'],
]
with (dossier/'CLEAN_RUN.txt').open('w', encoding='utf-8') as out:
    out.write('Clean tracked-source export plus explicit delta; original ignored logs absent.\n')
    out.write('Same installed CPython 3.14.3 and pinned dependencies; no package reinstall.\n')
    for args in commands:
        label='python '+' '.join(args)
        print('RUN '+label,flush=True)
        result=subprocess.run([sys.executable,*args],cwd=target,text=True,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        out.write('\n$ '+label+'\n'+result.stdout+'\nEXIT '+str(result.returncode)+'\n')
        out.flush()
        print(result.stdout,flush=True)
        if result.returncode:
            raise SystemExit(result.returncode)
print('PASS clean-source gate',flush=True)
