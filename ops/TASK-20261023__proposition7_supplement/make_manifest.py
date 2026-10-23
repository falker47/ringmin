"""Authoring-only manifest generation from immutable Git inputs.

Run from any directory with python -I -S; writes only the new package's manifest.
The verifier does not require this script or a Git checkout.
"""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'paper_assets/asymptotic_sequel/proposition7_supplement'
BASE='6167e36cf6f80a6a7a7a6b41518a6b3f7155295d'
SCIENCE='3beb8d70c5b3748d370a92855847bdf574e5a14f'
paths=[
    ('research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md',SCIENCE,'2-5, 11.1-11.3'),
    ('research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md',SCIENCE,'5-7'),
    ('research/THREE_LEVEL_COMMON_CHAIN.md',SCIENCE,'7, 9, 11-12'),
    ('research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md',SCIENCE,'1-3'),
    ('ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py',SCIENCE,'entire checker'),
    ('ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py',SCIENCE,'entire checker'),
    ('paper_assets/asymptotic_sequel/ringmin_asymptotic.tex',BASE,'Proposition 7 and definitions'),
]
inputs=[]
for path,commit,sections in paths:
    blob=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=ROOT)
    checkout=(ROOT/path).read_bytes()
    assert checkout.replace(b'\r\n',b'\n') == blob.replace(b'\r\n',b'\n'),path
    inputs.append({'path':path,'commit':commit,'sections':sections,
                   'git_blob_sha256':sha256(blob).hexdigest(),
                   'working_tree_sha256':sha256(checkout).hexdigest(),
                   'lf_normalized_sha256':sha256(blob.replace(b'\r\n',b'\n')).hexdigest()})
    if path.endswith('.py'):
        assert (P/Path(path).name).read_bytes() == blob
outputs={p.name:sha256(p.read_bytes()).hexdigest()
         for p in sorted(P.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}
manifest={'schema':'ringmin-proposition7-manifest-v1',
          'repository':'falker47/ringmin','authoring_base_commit':BASE,
          'scientific_commit':SCIENCE,'date':'2026-10-23',
          'generation_context':'New supplement sources over authoring_base_commit; output hashes pin every new generating source. The Git commit containing this manifest is the package revision.',
          'excluded_from_self_hash':['MANIFEST.json'],'inputs':inputs,'outputs':outputs,
          'generation_commands':[
              'python -I -S verify.py --write-certificate --skip-manifest',
              'pdflatex -interaction=nonstopmode -halt-on-error -recorder -output-directory=build supplement.tex (three passes from a fresh directory)',
              'python -I -S ops/TASK-20261023__proposition7_supplement/make_manifest.py'],
          'nondeterminism':'Arithmetic certificate is deterministic. PDF timestamps, trailer ID and optional PTEX metadata are suppressed; same-engine isolated rebuild reproduced the delivered PDF. Other TeX versions may differ.'}
(P/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
print(f'MANIFEST: {len(inputs)} immutable inputs, {len(outputs)} output hashes')
