# Final verification command index

All results here are local. Builder runs, separate internal reviewer runs,
historical evidence and external acceptance are distinguished. The full raw
clean-source output is [CLEAN_RUN.txt](../TASK-20260911__portable_frontier_evidence/CLEAN_RUN.txt).
The input file list and hashes are in [CLEAN_SOURCE_MANIFEST.json](../TASK-20260911__portable_frontier_evidence/CLEAN_SOURCE_MANIFEST.json).

## Documented environment and fresh-clone procedure

CPython 3.14.3, NumPy 2.4.3, SciPy 1.17.1, mpmath 1.3.0, Matplotlib 3.10.9,
pytest 9.0.2, Windows PowerShell. Legacy symbolic checks additionally used
SymPy 1.14.0. The versions in requirements.txt were already installed;
installation commands below are instructions, not claimed fresh installs:

```text
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
python -m pip install sympy==1.14.0
```

From a fresh checkout at the final review commit:

```text
python scripts/frontier_logs.py restore
python -m pytest -p no:cacheprovider --basetemp=tmp-tests
python verify.py --start 3 --stop 8 --skip-frontier
python verify.py --start 3 --stop 14
python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py
python -I -S -O ops/TASK-20260911__general_block_transfer/check_general_blocks.py
python -I -S ops/TASK-20260911__global_variational_limit/check_line_recovery.py
python -I -S -O ops/TASK-20260911__global_variational_limit/check_line_recovery.py
python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py
python -I -O ops/TASK-20260911__global_variational_limit/check_word_lp.py
```

The builder ran every command above in a clean tracked-source export plus
explicit inspected delta, initially without results/checkpoints. All exited 0:
12 logs/9649682 bytes restored; 15 tests passed in 41.19s; all six smoke sizes
incumbent/local PASS with frontier SKIP; all twelve full sizes incumbent/local/
frontier PASS. General checker: 30034 small orders/580560 cells, 18 larger
rational-surrogate orders/1080000 cells, 342 full-max and 438 panel probes,
four controls. Line checker: 1089 words, 13995 independent paths, 13941 pair/
closure checks, 1089 concatenations, 94620 quantiles, four controls. LP checker:
1119 complete inequalities and 18 rejected corrupt certificates. Optimized
outputs match normal outputs. No bound for all n rests on these finite scans.

This gate used the existing pinned environment rather than an isolated
dependency reinstall. The tests explicitly load the exported src tree; the
verifier and new checkers do not import production Ringmin. The source manifest
records actual exported bytes: 522 tracked text files have Git's Windows line
endings, with otherwise identical content to their base blobs. All 546 source
hashes were checked. These assumptions are explicit; POSIX execution was not
available. No input required by the successful commands remains untracked.

## Exact endpoint and fixed-order dependencies

The separate internal reviewers freshly executed the following commands in
this goal. Their full output, proof scope, additional inline independent
certificates and negative controls are preserved in the linked audit files.
They are not being relabeled as additional builder clean-export runs.

Upper and fourth-block commands (all exit 0):

```text
python -I -S ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only
python -I -S ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py --exact-only
python -I -S ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py
python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py
python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
python -I -S -O ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py
```

Exact results: all parameter isolation, derivative, branch, signed remainder,
rational saving and control gates pass. See [UPPER_INTERNAL_AUDIT.md](UPPER_INTERNAL_AUDIT.md)
and [general/fourth review](../TASK-20260911__general_block_transfer/INTERNAL_REVIEW.md).

Lower dependency commands (exit 0 unless explicitly identified):

```text
python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py
python -I -S ops/TASK-20260911__four_level_rational_witness/check_four_level.py
python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py
python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py
python ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py
python -I -S -O ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py
```

The final command intentionally exits 1 with
`RuntimeError: This checker requires enabled assertions; omit -O.`
That is a successful fail-closed negative test, not a passing ordinary run.
Normal width gates certify the stated rational enclosure; common-crossing
checker covers 48 prescribed measures and 16 tour/cutoff cases, and the
three-level checker 12 prescribed couplings. The sharpness diagnostic mixes
exact floors/identities and separately classified 70/100-dps observations.
The reviewer also supplies 120 fresh direct-cost diagnostics and false-root
controls in [LOWER_INTERNAL_AUDIT.md](LOWER_INTERNAL_AUDIT.md). These do not
replace its analytic rederivation of the minimal all-order proof.

Fixed-order commands (all exit 0):

```text
python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py
python -I -O ops/TASK-20260904__supnick_feasibility_classification/check_exact.py
python -I ops/TASK-20260904__supnick_feasibility_classification/diagnose.py
python -I -S ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py
python -I -S -O ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py
python -I ops/TASK-20260904__seam_sequence_monotonicity/check_symbolic.py
python -I -S ops/TASK-20260804__radius3_seam_onset/check_seam.py --order-stop 17
python -I -S ops/TASK-20260804__radius4_seam_onset/check_seam.py --order-stop 21
python -I -S ops/TASK-20260804__radius5_seam_onset/check_seam.py --order-stop 25
python -I -S ops/TASK-20260805__radius6_seam_onset/check_seam.py --order-stop 30
```

Results include 1482 pairs/2964 directed paths and 82 rejection gates;
ten exact positive-polynomial certificates and six controls; separate symbolic
derivatives; all rational onset bridges. The numerical diagnose command found
no counterexample in 106 cases/445470 triangles, with its 80-dps tolerance
explicitly distinguished from interval proof. The exact k=1,2 function calls
and a complete separate stdlib rational sqrt/atan certificate for all twelve
bridges are embedded, executable and freshly rerun in
[FIXED_ORDER_INTERNAL_AUDIT.md](FIXED_ORDER_INTERNAL_AUDIT.md).

## Publication and repository gates

```text
python paper_assets/v2/build.py
git diff --check
git diff --cached --check
```

The actual build supplied `--engine` for the installed pdflatex executable.
Two-pass build, repeat hash comparison, Poppler rendering and nine-page visual
inspection are recorded in the [publication evidence](../TASK-20260911__versioned_publication/EVIDENCE.md).
Explicit UTF-8/whitespace and full-content reviews cover additions omitted by
ordinary git diff. Staged blob comparisons check the exact inspected files.
Protected paths are compared with the starting commit. No hosted CI run is
claimed for any goal SHA, and no exhaustive search regeneration is claimed.

Earlier local setup failures, the corrected recursive fixture, the Windows
drive-path finding and build-layout corrections are retained in their dossiers;
they are not erased from the evidence. The final external reviewer must
independently inspect the full accepted-baseline delta, including mathematical
proofs and provenance, under RINGMIN_REVIEW_PROTOCOL.md.
