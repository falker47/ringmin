# Stage-A Checkpoint Recovery Audit

Date: 2026-09-16

## Why this matters

The journal-readiness audit narrowed the strongest remaining numerical-rigor question to the completeness of the high-precision frontier extracted from historical Stage-A heaps. Recovering the original `stage_a_n*_lb3.pkl` checkpoints would allow a substantially stronger post-hoc certificate without automatically rerunning the full canonical enumeration.

## GitHub-side recovery audit

The current repository deliberately ignores `results/checkpoints/`, `*.pkl` and progress logs. A code/history search does not find committed Stage-A checkpoint files.

The historical GitHub Actions CI workflow does not upload artifacts. It only checks out the repository, installs dependencies, runs `pytest`, and runs a small verifier smoke test (`n=3..8`, frontier skipped). An inspected successful historical workflow run contains zero artifacts.

No useful Stage-A checkpoint was found in the repository release history during this audit.

**Conclusion:** GitHub is exhausted as a known recovery source for the original Stage-A pickle heaps. The next recovery source is the machine or backup where the exhaustive sweep was run.

## Files to look for locally

Primary targets:

```text
stage_a_n03_lb3.pkl
stage_a_n04_lb3.pkl
...
stage_a_n14_lb3.pkl
```

Likely repository-relative location if the original working tree still exists:

```text
results/checkpoints/
```

Also preserve any matching progress/log files if found; they are useful provenance even though the pickle heaps are the critical asset.

## Safe local search commands

### Windows PowerShell

From the most likely parent directory first:

```powershell
Get-ChildItem -Path $HOME -Filter "stage_a_n*_lb3.pkl" -File -Recurse -ErrorAction SilentlyContinue |
    Select-Object FullName, Length, LastWriteTime
```

If that returns nothing and the sweep may have lived elsewhere, repeat on the relevant data/work drive rather than scanning every mounted drive blindly.

To search for the expected checkpoint folder itself:

```powershell
Get-ChildItem -Path $HOME -Directory -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match 'ringmin.*results[\\/]checkpoints$' } |
    Select-Object FullName, LastWriteTime
```

### Bash / WSL / Linux

```bash
find ~ -type f -name 'stage_a_n*_lb3.pkl' -printf '%p\t%s bytes\t%TY-%Tm-%Td %TH:%TM:%TS\n' 2>/dev/null
```

and, if useful:

```bash
find ~ -type d -path '*/ringmin/results/checkpoints' -print 2>/dev/null
```

## If files are recovered

Do **not** commit the pickle files directly to `main` yet. First:

1. copy them to a preserved working location;
2. compute SHA-256 hashes and record file sizes/timestamps;
3. confirm that the pickle schema can still be loaded by the current `search.py`/frontier tooling without mutating them;
4. reconstruct a much wider candidate band from every retained per-prefix heap;
5. recompute that band with high precision or interval arithmetic;
6. create a compact, text/JSON certificate suitable for version control and independent verification;
7. only then decide whether the original pickle files should be archived externally as research data.

## If files are not recovered

The next engineering decision is whether to rerun Stage A with a rigorously safe lower-bound/filtering path. Because the saved top-K exclusion margins are macroscopic, the rerun need not necessarily use expensive interval arithmetic on every operation; a conservative analytically justified enclosure can be used as a coarse filter, with high precision reserved for the narrow region near the incumbent.

If that engineering cost is judged disproportionate, the alternative remains to narrow the journal's terminology so that the numerical assumptions of the historical certification are explicit.

## Current decision gate

Before starting a DCG journal manuscript, answer one concrete question:

> Can the original `stage_a_n*_lb3.pkl` heaps be recovered from the machine/backups used for the exhaustive sweep?

Everything else in the journal-readiness plan can proceed after that answer without altering the already-public arXiv v2.
