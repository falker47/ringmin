# Evidence

## Environment

```text
repository_head=1636bf23cfadac46fb785bf6b1afda7e2787a466
platform=Windows-11-10.0.26200-SP0
python=3.14.3 (MSC v.1944 64 bit, AMD64)
mpmath=1.3.0
dependency_source=existing environment; no installs
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| All 32 labeled orders at m=2,3,4 evaluated | engineering fact / independently reproduced finite result | roots.json and independent enumeration/set equality | no symmetry quotient or pruning; m=5..8 not run |
| Root values and numerical minimizers | numerical observation / independently reproduced finite result | 80-digit asin and 110-digit atan scorers | common exact criterion and mpmath library; different formula, cycle indexing and enumeration; not rigorous decimal intervals |
| Cyclic shifts need not minimize rho_P | disproved claim | rational separator R=577/100 | exact Fraction/isqrt/series; no numerical value enters the certificate |
| m=4 is least, with unique arbitrary/shift minimizers there and unique m=3 shift winner | computer-certified finite result | three separators, exhaustive rational scoring, m=2 exact cell invariance | within this prescribed family; no R*(8) claim |
| Four short root brackets and negative mixed/chain root swap | computer-certified finite result | rational endpoint tests, exact branch gates, monotonic R-band enclosure | longer decimal roots remain diagnostic |
| Full placement at R=577/100 | proved fixed-order consequence; independently reproduced numerical witness | imported criterion plus exact S<2*pi; separate 110-digit paths/Cartesian reconstruction | no independent re-proof of the criterion or global optimality |

Detailed mathematical authority: research/PERMUTED_HALVES_ROOT_SEARCH.md.
The sole thematic owner is knowledge/FIXED_ORDER_THEORY.md; neither another
ledger nor the compact index acquired a duplicate claim.

## Commands and checks

All commands below ran locally from the repository root, in the existing
environment above. No hosted CI or external reviewer result is asserted.
Read-only Git used `git -c safe.directory=<repository-root>`; the actual
root is the current checkout, not a required machine-specific project input.
The initial clean status exited 0, no path entries, with two warnings that
the user's global ignore file was unreadable. No Git config/state was written.

### Exhaustive numerical search

```text
python ops/TASK-20260905__permuted_halves_root_search/search_roots.py
exit=0
m=2 permutations=2 best=0.84445358956085560434752852467389 shift=0.84445358956085560434752852467389 gap=0.0
  best_orders= [[3, 4], [4, 3]] best_shift_orders= [[3, 4], [4, 3]]
m=3 permutations=6 best=2.7949195188969248561702440679659 shift=2.7949195188969248561702440679659 gap=0.0
  best_orders= [[6, 4, 5]] best_shift_orders= [[6, 4, 5]]
m=4 permutations=24 best=5.7677942845896143026361805724956 shift=5.783560085857001475667965181196 gap=0.0157658012674
  best_orders= [[8, 7, 5, 6]] best_shift_orders= [[7, 8, 5, 6]]
STOP: first robust numerical counterexample at m= 4
```

Checks the root objective with the exact full criterion, not the chain
relaxation or a generic fixed-R comparison. Every order has its own root;
the retained bracket signs use numerical arithmetic. Domain, iteration
counts and guards were declared before the run in TASK_STATUS.md.

### Independent scorer, exact certificate and targeted rejection checks

```text
python ops/TASK-20260905__permuted_halves_root_search/check_roots.py
exit=0
PASS independent atan: m=2, orders=2, best=[(3, 4), (4, 3)], shifts=[(3, 4), (4, 3)]
PASS independent atan: m=3, orders=6, best=[(6, 4, 5)], shifts=[(6, 4, 5)]
PASS independent atan: m=4, orders=24, best=[(8, 7, 5, 6)], shifts=[(7, 8, 5, 6)]
PASS numerical roots=32; maximum midpoint error=1.79291546936e-71
PASS rejection checks: omitted/duplicate order, invalid bracket, incomplete shift ties, source hash
PASS 110-digit witness at R=577/100: 28 Cartesian pairs, 56 directed paths; guard=1e-100
PASS exact m=2: both permutations are cyclic shifts; cells invariant
PASS exact m=3 domain=all R=559/200: winner S-2pi in ['-19046129/200000000000', '-23807661/250000000000']; others > 6338731857/1000000000000
PASS exact m=4 domain=all R=577/100: winner S-2pi in ['-1419924193/1000000000000', '-44372631/31250000000']; others > 1143073557/125000000000
PASS exact m=4 domain=shifts R=723/125: winner S-2pi in ['-74049311/250000000000', '-296197243/1000000000000']; others > 24416871879/1000000000000
PASS rational root bracket m=2 P=(3, 4): 1688907179/2000000000 < rho < 1055566987/1250000000
PASS rational root bracket m=3 P=(6, 4, 5): 6987298797/2500000000 < rho < 2794919519/1000000000
PASS rational root bracket m=4 P=(8, 7, 5, 6): 11535588569/2000000000 < rho < 28838971423/5000000000
PASS rational root bracket m=4 P=(7, 8, 5, 6): 28917800429/5000000000 < rho < 57835600859/10000000000
PASS exact local swap j=1: mixed/chain increments; Delta at shift root in ['-2026856843/200000000000', '-2533571043/250000000000']
```

The first run passed all numerical roots and rational separators/brackets,
then failed an erroneous all-chain local diagnostic (exit 1). After its
correction, the checker exited 0. The final run above adds five tampering
tests and the independent all-pairs reconstruction, and also exited 0.
No failed attempt is erased from TASK_LOG.md.

The exact part does not consume roots.json or its labels to establish
the certificate: it uses explicit rational inputs and exhaustive recursive
enumeration. Asin enclosure uses 240 positive-series terms, coefficient
tail <=q^240/(1-q), integer square-root endpoints on a 10^-40 grid, and
an asserted angular width <10^-30. Pi uses the Machin identity and
80-term alternating atan intervals. All arithmetic deciding signs is exact.
The fixed-order interpretation imports the preceding proof; the finite
certificate does not rerun the production global-pruning verifier.

### Other commands and skipped layers

The inline `python -` diagnostics sorted the saved root table and checked
the exact four branch corners at four rational radii (both exit 0). A
separate inline stdlib query converted certificate fractions to exact
terminating decimals and calculated SHA256 (exit 0). These are presentation
and diagnostic checks, not independent new mathematical premises.

Production pytest, `verify.py --start 3 --stop 14`, its smoke mode, the
paper build and hosted CI were not run. Their implementations, artifacts
and publication content are protected and unchanged; they do not verify
this task-local permutation conjecture. No dependencies were installed.

## Artifact and provenance checks

Generation provenance is base HEAD plus the uncommitted source bytes
identified below; the base commit does not contain these new scripts.
All inputs are fixed in the scripts. There is no random seed, resume state,
parallel reduction or nondeterministic ordering. Run search_roots.py before
check_roots.py; each writes only its own dossier JSON output.

| Artifact | Schema | Source / independent checking |
|---|---|---|
| roots.json | ringmin.permuted-halves-roots.v1 | search_roots.py; all 32 roots independently recomputed by check_roots.py |
| certificate.json | ringmin.permuted-halves-root-certificate.v1 | check_roots.py exact arithmetic; explicit per-order enclosures and root brackets; proof of the method in the new note |

SHA256 of final source/artifact bytes, calculated with Python hashlib:

```text
search_roots.py
d62016fbbee95670d62b33575b47cf808a7aff4a601232ac1c70a3abe01492b5
check_roots.py
9ebb8f6e3b8afd51f7496f3547924561c4f3b666e5ce11e86230ae6561db769b
roots.json
83f22900c482c12c77ba89303f89d5ae4a9c129b692110dd3c03a5b1c827cf0d
certificate.json
59ac600177aeaef4564ddac1de35f50dff1fa6d201cbd671a06cb9681af98b9d
```

Paths above are relative to this dossier. The certificate generator is
independent of the numerical search but is not a second independent exact
implementation of its own rational bound method; human review is pending.
No production/publication artifacts were regenerated.

## Failed checks and negative evidence

The all-m finite-root shift conjecture is refuted at m=4. The local
all-chain diagnostic failed because the left increment crosses from chain
to chord. This failure and the exact mixed/chain repair are retained in
TASK_LOG.md and the proof note; no universal all-chain sign is inferred.

## Final diff inspection

The complete tracked diff was read with
`git -c safe.directory=<repository-root> diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md`.
Every new file (both scripts, both JSON artifacts, the proof and all three
dossier documents) was read in full with `Get-Content -Encoding UTF8`.
The final handoff edits were inspected separately after those full reads.

An inline local stdlib audit (`python -`, exit 0) obtains Git's changed
and untracked path sets, requires exact equality with the 11-file whitelist,
checks an empty staged diff, reads every file as UTF-8 and checks final
newline, trailing whitespace and conflict markers. It also inspects both
script import ASTs, checks every recorded SHA256 and both embedded source
hashes, and invokes `git diff --check`. Material output:

```text
PASS whitelist: 3 tracked modifications, 8 untracked additions; staged diff empty
PASS UTF-8/newline/whitespace/conflict audit: all 11 files; independent script imports
PASS recorded SHA256: search_roots.py
PASS recorded SHA256: check_roots.py
PASS recorded SHA256: roots.json
PASS recorded SHA256: certificate.json
PASS artifact/source provenance; every other tracked path protected
PASS git diff --check: exit 0, no output
```

Final inventory:

```text
 M CURRENT_STATUS.md
 M knowledge/FIXED_ORDER_THEORY.md
 M research/NEXT_RESEARCH_STEPS.md
?? ops/TASK-20260905__permuted_halves_root_search/EVIDENCE.md
?? ops/TASK-20260905__permuted_halves_root_search/TASK_LOG.md
?? ops/TASK-20260905__permuted_halves_root_search/TASK_STATUS.md
?? ops/TASK-20260905__permuted_halves_root_search/certificate.json
?? ops/TASK-20260905__permuted_halves_root_search/check_roots.py
?? ops/TASK-20260905__permuted_halves_root_search/roots.json
?? ops/TASK-20260905__permuted_halves_root_search/search_roots.py
?? research/PERMUTED_HALVES_ROOT_SEARCH.md
```

All other tracked paths were checked by the exact changed-path whitelist,
including the two preceding proof notes, prior dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, publication metadata, README,
REPORT, other ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and the review
protocol. Only the two intended task-local JSON outputs were generated.
No stable claim was duplicated in another thematic module. No Git or
GitHub write, external review decision or hosted CI result is asserted.

## Residual uncertainty

High-precision root approximations alone do not certify their displayed
digits; rigorous short brackets and strict comparisons are separate.
The fixed-order geometric interpretation imports the preceding theorem;
this task does not independently re-prove it or certify global R*(2m).
m=5..8 remain untested under the authorized early stop. No all-m optimizer,
general permutation asymptotic functional, improved asymptotic coefficient,
contact/floater classification or external acceptance is claimed.
