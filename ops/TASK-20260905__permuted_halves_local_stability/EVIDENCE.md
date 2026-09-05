# Evidence

## Environment

```text
repository_head=460d705ff349340975feb51ea886d7a0f1aab08c
platform=Windows AMD64, PowerShell
python=3.14.3 (MSC v.1944 64 bit)
mpmath=1.3.0
sympy=1.14.0
dependency_source=existing environment; no installation or upgrade
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Weighted root bound and uniform O_K(m) | Exact fixed-order theorem | Proof Sections 2-4 | Analytic; imports the exact full criterion, never substitutes chain closure |
| Linear one-swap scale cannot be o(m) | Proved corollary / explicit exact construction | Sections 5-6 | Upper radial rate is proved separately; no fitted coefficient or root limit used |
| First interior shift swap has a strict O(1/m) improvement | Proved fixed-order corollary | Sections 5 and 7 | Uniform chord gate m>=32; excludes shifts 0,m-2,m-1 from this refinement |
| Bounded neighborhoods preserve the leading coefficient | Proved asymptotic corollary | Sections 7-8 | Imports the shift limit only for conclusions involving C_shift |
| Strict m=4 gap | Rechecked computer-certified finite result | Four rational endpoint signs | Reuses prior exact scorer; does not independently recertify minimality or all 32 orders |
| Sampled swap/root/contraction comparisons | Numerical observation | New 70-digit alternate-angle scorer | Independent of production, previous scorers and symbolic formulas; coupled to the full cell criterion |

The authoritative proof is research/PERMUTED_HALVES_LOCAL_STABILITY.md.
No stable claim is added to another thematic ledger. The global ledger and
PROJECT_KNOWLEDGE.md need no change: neither coefficient nor navigation
has changed. Prior proof notes retain their historical task scope.

## Commands and checks

Startup reads and environment inspection succeeded. The environment command
was `python -c "import sys, mpmath, sympy; print(sys.version); print('mpmath='+mpmath.__version__); print('sympy='+sympy.__version__)"`,
exit 0, with the versions above. No dependency installation was performed.
Read-only Git commands use a transient safe.directory option for the
workspace; see TASK_LOG.md for the initial ownership and NUL-exclude failures.

Executed locally, from the repository root:

```text
python -B ops/TASK-20260905__permuted_halves_local_stability/check_stability.py
exit=0
Python 3.14.3; mpmath 1.3.0; sympy 1.14.0
PASS symbolic: high, cross and radial derivative identities
PASS rational: lower-root polynomial coefficients=[3/4, 27/7, 2/7]; m=32 chord gate=11/64<1/3; rate/sharpness constant gates
PASS reused rational scorer: two m=4 root brackets, four signs; 0.0157658012 < rho_B-rho_A < 0.0157658014
PASS numerical size m=2: prescribed orders and cyclic boundary swaps
PASS numerical size m=3: prescribed orders and cyclic boundary swaps
PASS numerical size m=4: prescribed orders and cyclic boundary swaps
PASS numerical size m=8: prescribed orders and cyclic boundary swaps
PASS numerical size m=16: prescribed orders and cyclic boundary swaps
PASS numerical size m=32: prescribed orders and cyclic boundary swaps
PASS numerical size m=48: prescribed orders and cyclic boundary swaps
PASS numerical size m=64: prescribed orders and cyclic boundary swaps
PASS numerical: swaps=67, score/contraction probes=201, max root-change / bound=0.262304857463
PASS numerical m=32: shift drop=0.0057976130754343, O(1/m) bound=0.012916133776904; sharp-family drop/m=0.039849588065334
PASS numerical m=48: shift drop=0.0041280072879173, O(1/m) bound=0.0074231105028131; sharp-family drop/m=0.04425192490046
PASS numerical m=64: shift drop=0.0031485837095273, O(1/m) bound=0.0051151140713514; sharp-family drop/m=0.046642797256278
PASS bounded audit: distinct roots=90; 70 digits, 240 bisections, guard=1e-55; no enumeration
```

The diagnostic domain has no seed or nondeterminism: ascending, descending
and half-shift orders at m=2,3,4,8,16,32,48,64; positions 1,m-1,m
(deduplicated); plus two specified first-swap families at m=32,48,64.
At fixed m this is a bounded number of orders, each score requiring O(m)
cells. This does not enumerate m!, optimize a shift, or extend any global
certificate. Numerical bisection brackets are not outward-rounded intervals.

Manual analytic review checks: m=2 degeneracy; m=3 coincident exterior
highs; both cyclic wrap swaps; max ties under a common contraction factor;
comparison at the smaller FULL root; positivity before reciprocal/sine
inversions; the separate upper rate for sharpness; the m>=32 uniform
branch rectangle; and the distinction between m=4's exceptional shift
and eventual interior best shifts. No all-m sign is inferred from m=4.

Production pytest, verify.py (both smoke and frontier modes), paper build,
and hosted CI were not run: their inputs/implementation are unchanged.
The new mathematics is supported by its proof, with proportionate local
algebraic and diagnostic checks. No hosted-CI success is asserted.

## Artifact and provenance checks

No result/certificate/publication artifact is generated or changed; the
task-local output above is retained in this evidence file, not mirrored
into results/. No generated result file or JSON schema is introduced.

The checked implementation is the new uncommitted working-tree delta on
the base HEAD above; that HEAD alone does not contain this checker.
SHA256 values, inspected with Get-FileHash -Algorithm SHA256:

```text
ops/TASK-20260905__permuted_halves_local_stability/check_stability.py
b530603e7a32261cafbd82460a789dc4fb9d71357adf488d47f8055581ac14db
ops/TASK-20260905__permuted_halves_root_search/check_roots.py
9ebb8f6e3b8afd51f7496f3547924561c4f3b666e5ce11e86230ae6561db769b
```

The latter is loaded for its rational functions only, via runpy with a
non-main name. Its root enumeration, main entry point and artifact writers
are not called; -B prevents bytecode output. The new numerical scorer
does not call those functions. SymPy is available in the existing local
environment but is not added to production requirements.

## Failed checks and negative evidence

All mathematical checks passed on their first run. Initial Git access
failures are recorded in TASK_LOG.md and did not affect repository files.
The explicit sharpness construction rules out the stronger uniform o(m)
one-swap claim. The stronger shift O(1/m) estimate is deliberately not
applied to the finite mixed/chain m=4 configuration.

## Final diff inspection

- `git status --short`: exactly 3 tracked modifications (CURRENT_STATUS,
  fixed-order ledger, roadmap) and 5 new files (proof note and this
  dossier's four files). Full tracked diff and every untracked file read.
- `git diff --cached --name-only`: exit 0, no staged paths.
- `git diff --check`: exit 0, empty stdout. Commands used the successful
  transient per-command safe.directory override; the convenience
  PowerShell interpolation failure is retained in TASK_LOG.md.
- Explicit inline Python audit: exit 0, eight allowed files checked for
  whitespace, final newline, conflict markers and UTF-8; four relative
  Markdown links exist; both checker hashes match the checked sources;
  exact changed-path whitelist and empty staged diff confirmed.
- All protected tracked paths are unchanged, including prior proof notes
  and dossiers, paper_assets/, results/, src/, tests/, scripts/, verify.py,
  metadata, public overview/report, other ledgers, index and contracts.
  No generated assets changed or incidental new files were found.

The audit was executed as a PowerShell here-string piped to `python -B -`.
Its read-only source is retained for exact reproduction:

```powershell
@'
from pathlib import Path
import hashlib
import re
import subprocess
root = Path.cwd()
git = ['git', '-c', 'safe.directory=' + root.as_posix()]
def read_git(*args):
    return subprocess.check_output(git + list(args), text=True, stderr=subprocess.PIPE)
dossier = 'ops/TASK-20260905__permuted_halves_local_stability/'
allowed = {'CURRENT_STATUS.md', 'knowledge/FIXED_ORDER_THEORY.md', 'research/NEXT_RESEARCH_STEPS.md', 'research/PERMUTED_HALVES_LOCAL_STABILITY.md'} | {dossier + name for name in ('TASK_STATUS.md', 'TASK_LOG.md', 'EVIDENCE.md', 'check_stability.py')}
tracked = set(read_git('diff', '--name-only').splitlines())
untracked = set(read_git('ls-files', '--others', '--exclude-standard').splitlines())
assert tracked | untracked == allowed, (tracked, untracked)
assert not read_git('diff', '--cached', '--name-only').strip()
links = 0
for name in sorted(allowed):
    data = Path(name).read_bytes()
    text = data.decode('utf-8')
    assert data.endswith(b'\n') and not data.endswith(b'\n\n'), name
    assert all(line == line.rstrip(' \t') for line in text.splitlines()), name
    assert '\x00' not in text and not re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M), name
    if name.endswith('.md'):
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' not in target:
                assert (Path(name).parent / target).exists(), (name, target)
                links += 1
assert hashlib.sha256(Path(dossier + 'check_stability.py').read_bytes()).hexdigest() == 'b530603e7a32261cafbd82460a789dc4fb9d71357adf488d47f8055581ac14db'
assert hashlib.sha256(Path('ops/TASK-20260905__permuted_halves_root_search/check_roots.py').read_bytes()).hexdigest() == '9ebb8f6e3b8afd51f7496f3547924561c4f3b666e5ce11e86230ae6561db769b'
check = subprocess.run(git + ['diff', '--check'], capture_output=True, text=True)
assert check.returncode == 0 and not check.stdout, check
print(f'PASS final file audit: {len(tracked)} tracked + {len(untracked)} untracked = {len(allowed)} allowed files; whitespace/EOF/conflict gates; {links} local Markdown links; two hashes; empty staged diff; protected paths unchanged')
print('git diff --check: exit 0, stdout empty')
'@ | python -B -
```

Output:

```text
PASS final file audit: 3 tracked + 5 untracked = 8 allowed files; whitespace/EOF/conflict gates; 4 local Markdown links; two hashes; empty staged diff; protected paths unchanged
git diff --check: exit 0, stdout empty
```

## Residual uncertainty

Independent human proof review is pending. This task does not re-prove the
imported full-feasibility criterion or certify a global optimum. Production
tests, global frontier verification and hosted CI are outside this delta.
