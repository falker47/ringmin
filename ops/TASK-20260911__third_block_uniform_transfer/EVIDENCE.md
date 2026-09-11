# Evidence

## Environment and provenance

    repository_head=2c32a099b775afc98a464fdece75b807efddb079
    platform=Windows; PowerShell; local Codex workspace
    python=3.14.3
    dependency_source=standard library only; isolated Python with site disabled
    task_mode=STRICT

No result artifact, production code, verifier or publication asset is
generated or modified. The executable audit below is kept in this dossier
to respect the task's Markdown-only scope. No approximate input minimizer,
external data, third-party library, production or prior-checker import is
used by this audit. Existing dependency checkers are run separately.

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| Uniform [0,h] floor gates and recovery | Exact theorem | New proof Sections 2-3 | Analytic all-m/all-width argument; finite integer checks only supplement it |
| Full-cell root equals full minimum | Exact fixed-order theorem | New proof Section 4; arbitrary-high theorem | Uses a separately proved geometric dependency; not external review |
| Uniform even/odd radius errors | Exact theorem / proved corollary | New proof Section 5 | Width-free angular bound, separately bracketed odd lower root |
| C_3(Delta_*) global limsup bound | Proved upper corollary | New proof Section 6; existing mixed minimum | Feasible constructions, not global optimality or a finite certificate |
| Executable audit outputs | Independently reproduced finite arithmetic facts | Code below | Independent of production; not an all-m proof or hosted CI |

## Precise bounded discriminator

Conjecture tested: the ordered-cell and panel formulas depend on the
pre-wrap floor gates, not on the third slab being chord. In particular
they remain correct at Delta=h, where the old chord gate is strictly
false. The analytic proof supplies every interval quantifier.

Use only the two structural endpoint widths 0 and h at the eight CLOSED
input bracket corners; these are enlarged-domain controls, not substituted
definitions of the implicit inputs. At each corner use the seven specified
small/boundary sizes, m=2048 and the three sizes surrounding each of the
first three third-floor transitions at h. At m=1000 separately test the
three exact floor ties 2/m,4/m,6/m. These are floor controls; no cost scan,
numerical root, optimization, random seed or width mesh is used. The
fixed-size audit terminates after these cases. A failure invalidates the
proposed seam/recovery argument until corrected; success only supports it.

The independent list rotation and even-slot reversals are checked against
the displayed rank formula, actual cyclic pairs, parity panels, counts and
deletion incidence. Rational residual-box endpoints check the constants
13 and 11, and exact endpoint identities exhibit chain dominance at h.

## Executable focused audit

```python
from fractions import Fraction as Q
from itertools import product
from math import ceil, floor

if not __debug__:
    raise SystemExit("ERROR: assertions must be enabled")

AL, AH = Q(1093, 10000), Q(10931, 100000)
XL, XH = Q(719, 2500), Q(2877, 10000)
EL, EH = Q(43, 1000), Q(11, 250)
hL = (1+AL)*(Q(1, 3)-XH)-EH
hH = (1+AH)*(Q(1, 3)-XL)-EL
margin = Q(1, 2)-AH-(1+AH)/3
assert hL == Q(1986317, 300000000) > Q(1, 250)
assert hH == Q(1933111, 250000000) < EL
assert EL-hH == Q(8816889, 250000000)
assert margin == Q(523, 25000) > 0

def construct(m, s, q, d, f):
    assert m >= 2 and 0 <= s < m
    assert 0 <= f <= d <= q and all(k % 2 == 0 for k in (q, d, f))
    assert 2*(s+q+d+f) < m
    highs = list(range(m+1, 2*m+1))
    p = highs[s:]+highs[:s]
    for a, length in ((0, q), (q, d), (q+d, f)):
        p[a+1:a+length:2] = p[a+1:a+length:2][::-1]
    return p

def audit(m, s, q, d, f, p):
    e, z, r = q+d, q+d+f, m-s
    assert sorted(p) == list(range(m+1, 2*m+1))
    assert r >= z+2 and p[r-1] == 2*m
    ranks = []
    for i in range(1, m+1):
        j = i
        if i % 2 == 0:
            if i <= q:
                j = q+2-i
            elif i <= e:
                j = q+e+2-i
            elif i <= z:
                j = e+z+2-i
        ranks.append(j)
    assert sorted(ranks) == list(range(1, m+1))
    assert all(ranks[j-1] == i for i, j in enumerate(ranks, 1))
    assert p == [m+1+(j+s-1) % m for j in ranks]
    ex = {1: (m+s, m+s+1) if s else (2*m, m+1),
          r: (2*m-1, 2*m)}
    if s:
        ex[r+1] = (2*m, m+1)
    if q:
        ex[q+1] = (m+s+2, m+s+q+1)
    if d:
        ex[e+1] = (m+s+q+2, m+s+e+1)
    if f:
        ex[z+1] = (m+s+e+2, m+s+z+1)
    interior = {}
    for a, length in ((0, q), (q, d), (e, f)):
        for i in range(a+2, a+length+1):
            assert i not in interior and i not in ex
            interior[i] = (a, length)
        fixed = sum(ranks[i-1] == i for i in range(a+2, a+length+1, 2))
        assert fixed == int(length % 4 == 2)
    for i in range(1, m+1):
        pair = p[i-2], p[i-1]
        if i in ex:
            assert pair == ex[i]
        elif i in interior:
            a, length = interior[i]
            if i % 2 == 0:
                expected = m+s+i-1, m+s+2*a+length+2-i
                panel, bound = (i-2, i), 2
            else:
                expected = m+s+2*a+length+3-i, m+s+i
                panel, bound = (i-1, i+1), 4
            assert pair == expected
            for u in panel:
                target = m+s+u, m+s+2*a+length-u
                if i % 2:
                    target = target[::-1]
                assert max(abs(i-u), *(abs(x-y) for x, y in zip(pair, target))) <= bound
        else:
            base = m+s if i < r else s
            assert pair == (base+i-1, base+i)
            for u in (i-1, i):
                assert max(abs(i-u), *(abs(x-base-u) for x in pair)) <= 1
    counts = len(interior), len(ex), m-len(interior)-len(ex)
    expected = ((0, 2, m-2) if q == 0 else
                (q-1, 3, m-q-2) if s == 0 else
                (q-1, 4, m-q-3) if d == 0 else
                (q+d-2, 5, m-q-d-3) if f == 0 else
                (q+d+f-3, 6, m-q-d-f-3))
    assert counts == expected and min(counts) >= 0 and sum(counts) == m
    cycle = [k for i, high in enumerate(p, 1) for k in (i, high)]
    odd = [k for k in cycle if k != 2*m]
    pos = {k: j for j, k in enumerate(odd)}
    used = set()
    removed = {r, r % m+1}
    for i in range(1, m+1):
        if i in removed:
            continue
        u, v = p[i-2], p[i-1]
        edges = {pos[u], pos[i]}
        assert (pos[u]+1) % len(odd) == pos[i]
        assert (pos[i]+1) % len(odd) == pos[v]
        assert not used & edges
        used |= edges
    assert len(used) == 2*m-4 and len(odd)-len(used) == 3
    return len(ex)

cases = cells = seams = endpoint_controls = ties = 0
seen_f = set()
for alpha, x, eps in product((AL, AH), (XL, XH), (EL, EH)):
    A, lam = 1+alpha, (1+alpha)*x
    v = lam+eps
    h, B = A/3-v, A+v
    assert hL <= h <= hH and 0 < h < eps < lam
    assert Q(1, 2)-alpha-(v+h) >= margin
    # At s=Delta=h the diagonal ties, while the reflection is chain:
    # W(h)=1/2+sqrt((A/3)/B)>1 because 4*(A/3)>B>0.
    assert A+v+h == 4*(v+h) and 4*(A/3) > B > 0
    assert A-3*v-4*h == -h < 0
    endpoint_controls += 1
    sizes = {2, 3, 6, 7, 9, 10, 46, 2048}
    for threshold in (2, 4, 6):
        onset = ceil(Q(threshold)/h)
        sizes.update((onset-1, onset, onset+1))
    probes = [(m, Delta) for m in sorted(sizes) for Delta in (Q(0), h)]
    probes += [(1000, Q(k, 1000)) for k in (2, 4, 6)]
    for m, Delta in probes:
        s, q, d = floor(alpha*m), 2*floor(lam*m/2), 2*floor(eps*m/2)
        f = 2*floor(Delta*m/2)
        assert 0 <= m*Delta-f < 2 and f <= d <= q
        if m == 1000:
            assert f == m*Delta
            ties += 1
        p = construct(m, s, q, d, f)
        seams += audit(m, s, q, d, f, p)
        cases += 1
        cells += m
        seen_f.add(f)

# Closed residual corners overcover all strict floor residuals, scaled by m.
for ra, rl, re, rd in product((0, 1), (0, 2), (0, 2), (0, 2)):
    assert ra+3*rl+2*re+rd <= 13
    assert ra+rl <= 3 and ra+2*rl+re <= 7
    assert ra+2*rl+2*re+rd <= 11
assert {0, 2, 4, 6} <= seen_f
m = 2048
E = Q(1024, m)+Q(16384, 3*m*m)
Berr = Q(96, m)+Q(2048, m*m)+Q(32768, 3*m**3)
assert 0 < E < 1 and 0 < Berr < 1
assert 16-E-Berr > 14 > Q(44, 7)
assert 3+E < 4 < 6
assert 4*4+4*11+38*3 == 174 and 174+1024 == 1198

def reject(action):
    try:
        action()
    except AssertionError:
        return 1
    raise AssertionError("negative control accepted")

m, s, q, d, f = 1000, 109, 318, 42, 6
p = construct(m, s, q, d, f)
duplicate = p.copy()
duplicate[0] = duplicate[1]
negatives = reject(lambda: audit(m, s, q, d, f, duplicate))
merged = construct(m, s, q, d+f, 0)
negatives += reject(lambda: audit(m, s, q, d, f, merged))
false_seam = p.copy()
false_seam[q+d-1], false_seam[q+d] = false_seam[q+d], false_seam[q+d-1]
negatives += reject(lambda: audit(m, s, q, d, f, false_seam))
negatives += reject(lambda: construct(1, 0, 0, 0, 0))
print("EXACT h brackets =", hL, hH)
print("EXACT uniform half-wrap margin =", margin)
print(f"EXACT endpoint chain/failed-chord-gate controls = {endpoint_controls}")
print(f"EXACT floors/cells/panels/deletion: cases={cases} cells={cells} seams={seams} ties={ties}")
print("EXACT residual constants = 13,11; score/root constants = 174,1198; gate m=2048")
print(f"EXACT negative controls rejected = {negatives}")
print("PASS bounded arithmetic support; interval and all-m claims require the analytic proof")
```

## Commands and checks

The source extraction command below executes exactly the Python fence above
without writing another file. It was run locally and exited 0:

```powershell
$auditText = Get-Content -Raw ops/TASK-20260911__third_block_uniform_transfer/EVIDENCE.md
$auditCode = [regex]::Match($auditText, '(?s)```python\r?\n(.*?)```').Groups[1].Value
$auditCode | python -I -S -
```

Material output, reproduced verbatim:

```text
EXACT h brackets = 1986317/300000000 1933111/250000000
EXACT uniform half-wrap margin = 523/25000
EXACT endpoint chain/failed-chord-gate controls = 8
EXACT floors/cells/panels/deletion: cases=296 cells=138844 seams=1344 ties=24
EXACT residual constants = 13,11; score/root constants = 174,1198; gate m=2048
EXACT negative controls rejected = 4
PASS bounded arithmetic support; interval and all-m claims require the analytic proof
```

| Exact command | Exit and material result | Property and limit |
|---|---|---|
| Same extraction, then `$auditCode \| python -I -S -O -` | Expected exit 1: `ERROR: assertions must be enabled` | Disabled-assertion negative control; no mathematical check claimed |
| `python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py` | Exit 0; two rational signs, root/cost implications pass; saving `>12389/72000000000000` | Reproduces imported finite sign gates; analytic source supplies uniqueness and all-width statements |
| `python -I -S ops/TASK-20260911__third_block_250_transfer/check_transfer.py` | Exit 0; 614 cases, 208182 cells, 3063 seams; 17 even and 15 retained-odd rational root brackets; 28999561 unordered pairs with both paths checked; 6 negative controls rejected | Independently reproduces old fixed-width geometry dependency evidence; does not computationally certify a new width or replace the uniform proof |
| `$gitTaskRoot = (Get-Location).Path.Replace('\','/'); git -c "safe.directory=$gitTaskRoot" diff --check` | Exit 0, no output | Portable command-local ownership exception and tracked whitespace check; untracked additions checked separately |

The mixed-width checker's two signed-square results were
`-963745517404602389188679409068317/4734571866017504812540302482915910561`
and `34763358497298510706339907/205268116362886684743388903969`.
It reproduced the cost bracket
`(-2187/2048000000000,-24389/72000000000000)` relative to C_b.
Its final historical note says no geometric transfer; that describes its
own continuous-only scope, not the new theorem.

The fixed-width dependency checker's rational root brackets all have width
at most 1/100000. It reported 56088 detailed angle checks with outward
integer interval scale 10^32 and 64 terms; the remaining pairs use its
proved interval shortcut. For example m=1000, floors (109,318,42), f=4
has bracket [566736017443/1000000,283368008723/500000]. These are
finite exact enclosures, not feasibility claims at a rounded root.

All computations are local and independent of production imports. The
production pytest suite, certificate/frontier verifier and paper build
were not run: this Markdown-only theorem changes none of those sources or
artifacts. No hosted run for this task's eventual SHA has been inspected.

## Failed checks and negative evidence

Initial git status without command-local safe.directory failed ownership
validation. No working file or Git configuration was changed by that attempt.
The old chord gate is analytically negative at h; this is a deliberate
negative control on the abandoned necessity claim, not a failed transfer.
A combined documentation patch was rejected because it targeted current
status with both delete and add operations in one patch. No changes from
that patch applied; the corrected patch and literal status rewrite succeeded.
The first inline final-diff audit used a Windows-backslash safe.directory
value and failed Git repository recognition before any file checks ran.
Normalizing that command-local value with Path.as_posix() fixed the audit;
the successful rerun below is the verification evidence. No global setting
or working file was altered by either failed read-only attempt.

## Final diff inspection

- `git status --short` and complete tracked diff inspected. Four tracked
  edits: CURRENT_STATUS.md, the fixed-order and global ledgers, and roadmap.
- All four untracked additions inspected in full: the new proof and the
  three dossier Markdown files. No code artifact is added.
- Inline `python -I -S -` path/link/whitespace audit: exit 0. It derives
  the changed paths from `git diff --name-only` plus `git ls-files --others
  --exclude-standard`, asserts the exact eight-path allowlist, decodes
  every file as UTF-8, rejects BOM/NUL/trailing whitespace/missing final
  newline, and verifies every Markdown local link and heading anchor.
- Exact output: `PASS exact scope: 8 Markdown paths; 4 tracked edits and
  4 untracked additions`; `PASS UTF-8/no BOM/newline/explicit whitespace
  checks on all 8 paths`; `PASS local links/anchors: 34`;
  `PASS protected paths and prior proof dependencies unchanged`;
  `PASS git diff --check`.
- The audit runs `git diff --quiet HEAD --` on AGENTS.md,
  PROJECT_KNOWLEDGE.md, src/, tests/, verify.py, results/, paper_assets/,
  README.md, REPORT.md and all six directly used previous proof notes;
  exit 0. The exact changed-path allowlist additionally excludes all other
  prior dossiers/proofs, generated outputs and release metadata.
- Stable ownership inspected: uniform recovery/full radii in fixed-order
  theory; global upper corollary in global bounds; continuous minimizer
  and saving in their unchanged owning entry. No new knowledge module or
  duplicate cross-module claim is created. The compact index is unchanged.
- Authorized staging and its full diff/whitespace inspection, commit and
  normal push follow this precommit record. Their final SHA and result are
  reported in the task response; independent review remains separate.

## Residual uncertainty

The new theorem and imported proof chain await independent mathematical
review. No maximal transfer interval beyond h, best geometric coefficient,
global normalized limit, finite-n comparison cutoff or expanded finite
certification is asserted. No hosted CI result is claimed. Historical
dependency-checker labels retain their old task scope.
