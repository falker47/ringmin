# Numerical Certification Upgrade Plan

Date: 2026-09-16

## Executive conclusion

The existing finite-result evidence is strong, reproducible and internally
consistent, but its current numerical rigor is not identical to a full interval-
arithmetic proof of every historical pruning decision.

The audit separates **two different numerical boundaries** that should not be
conflated:

1. **Top-K heap coverage (orders excluded during Stage A).** This boundary is
   comparatively easy to harden. For `n <= 9` no order is excluded by the
   per-prefix heap. For `n = 10,...,14`, the saved `top_excluded_guard` values
   sit far above the final incumbent. The smallest observed gap occurs at
   `n=14` and is approximately `8.56e-2`, many orders of magnitude larger than
   the historical `1e-10` global guard.
2. **Retained-candidate / high-precision frontier boundary.** This is the real
   formal bottleneck. `extract_frontiers.py` selected retained candidates using
   the float64 condition `lower_bound < bestR_f64 + 2e-10`. The independent
   verifier recomputes every saved frontier order at 50 digits, but the full
   retained Stage-A heaps are not committed. Therefore the current repository
   cannot directly prove that a retained candidate omitted from the saved
   frontier did not have a true high-precision lower bound below the optimum
   unless one supplies a uniform worst-case bound for the historical float64
   lower-bound computation at roughly this `2e-10` scale.

This is substantially narrower than saying that the whole search must be rerun.

## What the current evidence proves operationally

The repository currently provides:

- exhaustive canonical enumeration counts from the historical Stage-A runs;
- per-prefix top-excluded guards and saved frontier metadata;
- independently recomputed 50-digit incumbent radii;
- independently recomputed 50-digit lower bounds for every saved frontier
  order;
- local-neighborhood checks around the incumbent;
- a verifier that reports `incumbent=PASS`, `local=PASS`, `frontier=PASS` for
  every certified `n = 3,...,14`;
- regression tests and task evidence tying the public finite tables to the
  saved artifacts.

What it does **not** currently provide is a directed-rounding or interval replay
of every historical Stage-A comparison.

## Why the heap-exclusion side is not the main problem

The Stage-A search keeps the `K=20000` smallest float64 lower bounds for each
prefix. The saved frontier JSON records the first excluded lower bound when a
prefix actually overflows the heap.

- For `n <= 9`, every canonical order is retained in the per-prefix heaps, so
  there is no top-K exclusion boundary to justify.
- For `n=10,...,14`, the observed gap between the weakest saved heap-exclusion
  guard and the final incumbent remains macroscopic. The minimum is about
  `0.0856` at `n=14`.

Consequently, a future formal treatment of Stage-A heap membership only needs a
very conservative worst-case numerical-error envelope smaller than this gap; it
does not require proving `1e-10`-level accuracy for every excluded order.

## Why the frontier boundary is harder

`extract_frontiers.py` loads the Stage-A checkpoint heaps and retains orders
whose float64 lower bound is within `2e-10` of the incumbent. `verify.py` then
recomputes the resulting finite frontier at 50 digits.

The committed repository deliberately ignores:

- `results/checkpoints/`;
- `*.pkl`;
- progress logs.

Thus the original `stage_a_n*_lb3.pkl` heaps are absent from Git history. The
repository knows the high-precision values of the saved frontier orders, but it
cannot widen that frontier retrospectively because the omitted retained orders
are no longer available here.

This means the current formal gap is specifically:

> Could an order retained by Stage A, but omitted by the `bestR + 2e-10`
> float64 frontier filter, have a true lower bound below the incumbent because
> the historical float64 lower bound overestimated it by more than the filter
> margin?

The random float64-vs-mpmath calibration gives strong empirical evidence that
this did not happen, but random calibration is not a worst-case proof.

## Preferred upgrade path — recover the historical Stage-A checkpoints

Before considering an expensive rerun, search the original machine/backups for
files such as:

```text
results/checkpoints/stage_a_n03_lb3.pkl
...
results/checkpoints/stage_a_n14_lb3.pkl
```

and any associated Stage-A progress logs.

If these checkpoints still exist, the most expensive combinatorial enumeration
need not automatically be repeated. A stronger certificate can be built by:

1. loading every retained top-K-per-prefix candidate from the historical heaps;
2. recomputing retained candidates with high precision or rigorous interval
   arithmetic, at least for a deliberately wide neighborhood above the
   incumbent;
3. recording the minimum rigorous lower bound among all retained candidates
   outside the incumbent/frontier set;
4. combining that result with the much wider saved heap-exclusion gaps;
5. replacing the empirical `2e-10` frontier-completeness assumption with a
   directly checked finite statement over the recovered heaps.

A checkpoint-based upgrade is therefore the first thing to attempt.

## If the checkpoints cannot be recovered

There are two defensible journal routes.

### Route A — rerun Stage A with a rigorous filter

Re-enumerate the canonical orders while ensuring that every pruning/filtering
comparison has a mathematically valid lower enclosure. Possible implementation
strategies include directed interval evaluation or an analytically certified
lower bound used as a coarse prefilter, with expensive high-precision work only
near the cutoff.

This need not rerun the expensive all-pairs Stage-B optimization for every
order; the principal requirement is to rebuild a rigorously complete candidate
frontier.

### Route B — narrow the journal claim

If a rigorous Stage-A rerun is disproportionate, keep the existing exhaustive
combinatorial search and independent high-precision validation, but describe the
finite results as reproducible numerical/exhaustive certification under the
stated float64 guard rather than implying a fully interval-certified
computer-assisted proof.

The manuscript must then state the numerical assumption and calibration
boundary explicitly.

## Stage-B stopping rule

The historical Stage-B search stops when the next retained float64 lower bound
satisfies

```text
lower_bound >= incumbent.R_full - 1e-9
```

This approximate stopping rule is not itself the strongest evidence in the
current package. The saved-frontier extraction plus 50-digit verification can
serve as the post-hoc certificate — **provided frontier completeness is made
rigorous**. Thus the same retained/frontier boundary, not the Stage-B stopping
constant alone, is the decisive issue.

## Recommendation for the journal paper

Do not weaken the finite mathematical result prematurely, and do not claim that
an interval proof already exists.

Recommended sequence:

1. search for the historical Stage-A `.pkl` checkpoints/backups;
2. if found, build a widened high-precision/interval post-hoc certificate from
   them;
3. if not found, estimate the cost of a rigorous Stage-A-only rerun;
4. only then freeze the theorem wording for the DCG manuscript;
5. use narrower certification terminology only if a rigorous upgrade is judged
   not worth the computational/engineering cost.

## Immediate decision gate

The next practical question is therefore **checkpoint recovery**, not journal
formatting. The public arXiv v2 remains valid as the corrective preprint; this
plan concerns the stronger evidentiary standard desirable for journal review.
