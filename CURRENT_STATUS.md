# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=3eb1ec321e2f5a334826ee70c2258f82b9703f66
observed_on=2026-09-02
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260902__radius8_seam_diagnostic
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and diagnostic outcome

Complete the bounded two-precision diagnostic for the formal radius-8
Supnick seam at every integer `33<=n<=46`.

**Classification: NUMERICAL DIAGNOSTIC / numerical observation.**

Independent rank-tour and parity-formula edge reconstructions agree for all
14 inputs. Separate calculations at 90 and 150 decimal digits find
`R_{8,n}-T_{8,n}<0` for `33..37` and `>0` for `38..46`. The first
stable crossing in the prescribed range is therefore `37/38`, nominating
`38` as a numerical candidate for `s_8`.

The selected rational separator is `176=176/1`. Numerically,

```text
R_{8,37} = 175.77577369548936913057 < 176
         < T_{8,37} = 184.04862734243861147206,

T_{8,38} = 152.91545396828178471093 < 176
         < R_{8,38} = 185.96986168932715306600.
```

The smallest numerical separator margin is approximately
`0.22422630451063086943`; the diagnostic guard is `1e-55`.
No exact endpoint inequality or exact value of `s_8` is established here.

### Allowed delta

- `ops/TASK-20260902__radius8_seam_diagnostic/`: three dossier documents,
  standalone `diagnose.py`, and `diagnostic.json`.
- The radius-8 entry in `research/NEXT_RESEARCH_STEPS.md`.
- This file.

### Verification gates

- 14 complete edge sets, 26 through 39 distinct edges, including cyclic
  closure, both seam edges, degree two, all rotations and reflections.
- 28 fresh root/threshold calculations: rank/asin/bisection/direct
  Descartes at 90 digits; parity/atan/Ridder/rationalized Descartes at 150.
- Positive thresholds, physical Descartes residuals, root residuals and
  local numerical brackets all pass; numerical sign and monotonicity checks
  pass throughout the fixed range.
- Largest difference between serialized run values is approximately
  `4.021905e-76`, below the `1e-55` guard.
- Normal generation and optimized recomputation both exit `0`;
  recomputation reports `reproduction=BYTE_IDENTICAL`.
- Separate Decimal/source audit exits `0`: all 14 rows checked, two
  out-of-range inputs and three malformed edge/tour cases rejected.
- Complete tracked/untracked delta inspected; the seven-file format/scope
  audit exits `0`, with five dossier files, no cache and zero protected
  changes. `git diff --check` exits `0`, no output. Commands and evidence
  are recorded in the dossier.

### Blockers and limitations

No blocker. Both computational paths share mpmath; the checks use no
directed rounding and are not exact endpoint certificates. A stored zero
residual is a rounded numerical zero. The range was not expanded.

`PROJECT_KNOWLEDGE.md` and all exact proof notes remain unchanged. No
full-feasibility, global-optimum, contact-graph, or floating-circle claim is
made. Production code, finite certificates, the standalone global verifier
and the arXiv-v1 publication assets are outside this diagnostic task.

## Exactly one next atomic task after acceptance

Prove the radius-8 endpoint bridge at `n=37,38` using `176`: establish
the four strict inequalities above with exact rational threshold and
complete chain-sum bounds, then apply the existing fixed-`k` theorem only
if every exact gate closes. This dedicated STRICT endpoint-proof task has
not begun.
