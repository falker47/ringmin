# Evidence

## Environment

```text
repository_head=c45162f7df1b1b482b9dbecea7b619ecdaa02227
platform=Windows; PowerShell
python=3.14.3
dependency_source=stdlib only; isolated Python -I -S
task_mode=STRICT
```

Base HEAD is identified as accepted by the user. No independent review of
that HEAD is inferred from its previous READY_FOR_REVIEW file state.

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Exact fourth-block complete-max identity, branch classification and cubic leading term with signed remainder | exact continuous theorem | research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md Sections 2-5 | analytic argument; external review pending | only the specified fixed-input direction |
| Negative interval and rational-width saving | exact continuous theorem / proved corollary | same proof, equations (4)-(6), (12) | bounded raw-max enclosure independently supports the witness | no finite Ringmin optimum/certificate |
| Domain and marginal preservation | exact continuous theorem | arbitrary-test involution and zero-mass seam proof | finite rational moments only support it | marginals alone do not establish recoverability |
| Checker outputs below | engineering fact / independently reproduced rational checks | stdlib checker, no production or previous-checker imports | local and separate from production | finite support does not prove continuum quantifiers |
| Later transfer obligations | conditional claim | proof Section 6 and existing full-cell criterion | not applied to four-block orders | transfer expressly deferred |

The sole stable thematic owner is knowledge/FIXED_ORDER_THEORY.md. The
compact index and global ledger need no changes: neither scope/navigation
nor the transferred global coefficient has changed.

## Commands and exact results

All commands below ran locally in the repository. None is hosted CI.
The two mathematical checks initially shared one PowerShell invocation;
they were then run separately to obtain an individual exit code for each.
The portable Git reads use the PowerShell prelude
`$taskGitRoot = (Get-Location).Path.Replace('\','/')`.

| Command | Exit/result | Property checked | Not checked |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | actual interpreter | dependencies beyond stdlib |
| `python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py` | 0; output below | exact gates and independent raw-max witness enclosure | analytic continuum proof or transfer |
| `python -O -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py` | 0; identical output | explicit checks and rejection controls survive disabled assertions | no additional mathematical claim |
| `python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py` | 0; two directed signs and all recorded implications reproduced | accepted Delta_* bracket's bounded arithmetic support | does not re-prove analytic stationarity/uniqueness |
| `python -I -S -` with the exact scope-audit stdin below | 0; 8 paths and 12 links/anchors pass | tracked and untracked paths, full-file whitespace and links | mathematical correctness |
| `git -c "safe.directory=$taskGitRoot" diff --check` | 0; no output | tracked whitespace | untracked additions checked explicitly above |
| `git -c "safe.directory=$taskGitRoot" diff` and direct `Get-Content` of additions | 0; complete content inspected | scope, proof/code text, protected-path preservation | independent mathematical acceptance |

The per-command safe.directory override uses the current repository path;
it changes no persistent Git configuration and is not an artifact input.

### New check output

```text
EXACT A-3w > 354539/1000000000 > 0
EXACT A-3w-4eta_0 > 154539/1000000000 > 0
EXACT a-w-eta_0 > 204539/3000000000 > 0
EXACT b-w-eta_0 > 520991513/1000000000 > 0
EXACT 3/2-M > 21016513/1000000000 > 0
PASS 16 corner partitions, 448 reflection moments, 48 branch probes, 6 sign/tie controls
EXACT 16-panel raw full-max increment <= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
PASS bounded exact support; analytic proof supplies interval and cubic term
NOTE no root solving, width scan, finite recovery, transfer or output files
```

The radicands are enclosed by rational roots on a fixed 10^-40 grid, with
every lower/upper square checked in integers. The output upper bound is
rounded UP to a 10^-24 grid. There are exactly 16 midpoint panels, 16
parameter-box corners, 7 high moments per block and 3 branch probes per
corner; no adaptive or unbounded computation and no random seed.
Concavity and monotonicity, proved in Section 6, make the raw-max result a
rigorous integral enclosure. The checker never evaluates the proof's
antiderivative, rationalized integrand or a decimal substitute for a minimum.

The dependency output includes the exact signed square differences

```text
-963745517404602389188679409068317/4734571866017504812540302482915910561 < 0
34763358497298510706339907/205268116362886684743388903969 > 0
stationary upper slack = 35511/800000000
diagonal cutoff slack = 354539/3000000000
inherited epsilon slack = 431/32000000
```

### Exact scope-audit stdin

Run the following as the stdin of `python -I -S -` from the repository
(PowerShell literal here-string; it writes no files). Only added lines of
the two large existing canonical documents are used for link traversal;
all eight task files are inspected in full for encoding and whitespace.

```python
from pathlib import Path
import re
import subprocess
root = Path.cwd()
git = ['git', '-c', 'safe.directory='+root.as_posix()]
def output(*args):
    return subprocess.check_output(git+list(args), text=True, encoding='utf-8')
dossier = 'ops/TASK-20260911__fourth_adjacent_block/'
expected = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md',
            'research/NEXT_RESEARCH_STEPS.md',
            'research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md'}
expected |= {dossier+n for n in ('TASK_STATUS.md', 'TASK_LOG.md',
                               'EVIDENCE.md', 'check_fourth_block.py')}
changed = set(output('diff', '--name-only', 'HEAD').splitlines())
changed |= set(output('ls-files', '--others', '--exclude-standard').splitlines())
if changed != expected:
    raise RuntimeError(('unexpected paths', changed ^ expected))
links = 0
for name in sorted(expected):
    path = root/name
    raw = path.read_bytes()
    content = raw.decode('utf-8')
    if content.startswith('\ufeff') or not content.endswith('\n'):
        raise RuntimeError(('encoding/final newline', name))
    for line, text in enumerate(content.splitlines(), 1):
        if text.rstrip() != text or '\t' in text:
            raise RuntimeError(('whitespace', name, line))
    if name in ('knowledge/FIXED_ORDER_THEORY.md', 'research/NEXT_RESEARCH_STEPS.md'):
        diff = output('diff', '--unified=0', 'HEAD', '--', name)
        content = '\n'.join(x[1:] for x in diff.splitlines()
                            if x.startswith('+') and not x.startswith('+++'))
    for target in re.findall(r'\[[^\]]+\]\(([^\s()]+)\)', content):
        if '://' in target:
            continue
        file, _, anchor = target.partition('#')
        dest = (path.parent/file).resolve() if file else path
        if not dest.is_file():
            raise RuntimeError(('missing link', name, target))
        if anchor:
            headings = re.findall(r'^#{1,6} (.+)$', dest.read_text(encoding='utf-8'), re.M)
            slugs = {re.sub(r'[^\w -]', '', h.lower()).replace(' ', '-') for h in headings}
            if anchor not in slugs:
                raise RuntimeError(('missing anchor', name, target))
        links += 1
print('PASS exact 8-path scope; UTF-8, final newlines and full-file whitespace')
print('PASS', links, 'task-local Markdown links/anchors')
print('PASS protected tracked paths unchanged; no generated/untracked extras')
```

This is a precommit audit: after committing, compare the task commit with
its parent instead of HEAD to reproduce the changed-path part.

## Failed checks and negative evidence

- Initial plain Git reads failed on sandbox dubious ownership. A per-command
  safe.directory override recovered them without editing configuration.
- Attempted `core.excludesFile=NUL` for a read failed with exit 128; Git
  rejects this device as an exclude file. It was abandoned without changes.
  Optional global-ignore permission warnings remain harmless to these checks.
- One multi-file patch was rejected because it attempted both delete and add
  for CURRENT_STATUS.md in the same patch. No portion applied; the corrected
  update was subsequently applied and inspected.
- A portability check with raw `$PWD` as safe.directory failed to recognize
  the repository. Repeating both reads with forward-slash normalization in
  the prelude above returned exit 0. No persistent configuration changed.
- At the later diagonal cutoff the inserted endpoint is strictly chain and
  the removed endpoint ties. Directed root bounds detect positive chain
  excess, so extrapolating the chord-only formula there is invalid.
- Zero/negative widths and a whole-slab chord claim at that cutoff are
  rejected. These are expected controls, not failed proof gates.

## Artifacts, provenance and final diff

No result artifact, generated output, finite permutation, certificate or
publication asset is created or regenerated. The checker writes no files.
Its input provenance is the exact accepted definitions/brackets at base HEAD,
not a new numeric solve. Source and evidence are committed together.

Complete tracked diff and every untracked addition were read in full.
The scope/whitespace/link audit covers all eight paths, including additions
omitted by ordinary git diff --check. No stable claim was added to a second
knowledge module. All previous proof notes, PROJECT_KNOWLEDGE.md, AGENTS.md,
other ledgers, src/, tests/, verify.py, results/, paper_assets/, README.md,
REPORT.md, generated assets, publication metadata and CI files are unchanged.
Final staged diff and its whitespace check follow this precommit record;
the final response reports the commit SHA, normal push result and tree state.

## Residual uncertainty and skipped checks

Independent mathematical review is still required. The proven negative
interval is sufficient, not maximal; no fourth-width optimization, minimum
redefinition, finite/full-feasibility transfer, new global coefficient or
expanded finite certification is asserted. The continuous result by itself
is not an upper bound for R*(n). The later transfer obligations distinguish
an odd upper bound from an odd fixed-order equality.

Production pytest, verify.py/frontier audits and paper builds were not run:
no corresponding code, certificate or publication input changed. No hosted
CI run for the eventual commit was inspected or described as green.
