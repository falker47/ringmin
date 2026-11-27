# Independent proof check, November 2026

Machine checks that accompany [`docs/referee/proofcheck-2026-11.md`](../../docs/referee/proofcheck-2026-11.md).
They cover the statements that earlier verification passes had not examined:

* Paper I (`paper_assets/journal_p1_jogo/main.tex`): angular reformulation,
  anti-Monge structure and Supnick tour, fixed-order feasibility, seam
  criterion and the onsets `n = 8, 13, 17`, outward cosine arithmetic,
  coverage and strictness. Modules `p1_*.py`, identifiers `P1-…`.
* Paper II (`paper_assets/journal_p2_sidma/supplement.tex`): lemmas L1–L8 of
  the lower bound for consecutive radii. Modules `p2_*.py`, identifiers `P2-…`.

The Paper I modules live on `fable/proofcheck-p1`, the Paper II modules on
`fable/proofcheck-p2`. `__main__.py`, `fable_common.py`, `test_proofcheck.py`
and this file are byte-identical on both branches; the runner discovers
whichever modules are present, so the command below is the same everywhere.

## One command

```bash
python -m pip install python-flint==0.9.0 sympy
python -I -B independent_check/fable_proofcheck
```

Run it from the repository root with Python 3.11 or later. It prints one line
per check and per negative control and exits nonzero if any check fails or
any control is not rejected. Add identifier prefixes to run a subset, for
example `python -I -B independent_check/fable_proofcheck P1-B P1-E7`.

The same items are available to pytest:

```bash
python -m pytest independent_check/fable_proofcheck -q
```

Observed on Windows 11, Python 3.14.3, python-flint 0.9.0, sympy 1.14.0:
Paper I 40 checks and 6 controls in about 35 s; Paper II 20 checks and
8 controls in about 10 s.

## What a result means

Each check is labelled with the arithmetic that decides it.

| Label | Decided by | Reading |
|---|---|---|
| `exact` | Python integers and `fractions.Fraction` | The stated finite claim is proved for the stated range. |
| `interval` | Arb balls (python-flint) | Every comparison is certain for all points of the balls. An undecided comparison is a failure. |
| `symbolic` | sympy simplification to an exact zero | The printed formula equals the derivative computed from the definition. |

No float decides anything. Floats appear only in two places, both marked in
the code: the search heuristic that proposes adversarial orders in
`p2_energy.py` (the proposed orders are then audited with Arb), and the
display of ratios in result strings.

A passing finite check is evidence for a universally quantified statement,
never a proof of it. The report states for each manuscript claim whether it
was verified by machine, by hand, or not at all.

## Independence

The package imports nothing from `src/ringmin`, `verify.py`,
`verify_global_brackets.py`, `paper_assets/general_radii`, or the earlier
checker in `independent_check/p2`. Manuscript sources are opened only to read
the printed constants and table rows that are being checked. Certificates are
not read: `P1-V5` rebuilds the lower exclusion for `n = 3..14` from the
printed endpoints alone.

## Negative controls

Identifiers `P1-X…` and `P2-X…` assert deliberately false variants (a wrong
onset, a tampered table entry, a halved constant, exclusion at an upper
endpoint). Each must raise `AssertionError`. They show that the checking code
can fail.
