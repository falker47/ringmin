# Research sprint, November 2026

```text
branch=fable/research-sprint
base=main @ c26400b328c2f8fa338b588e61abb98266a265f9
run_on=2026-11-24
mode=STRICT (mathematical claims and certificates), unsupervised
state=READY_FOR_REVIEW
scope=new files under research/fable_sprint_2026-11/ only
```

Goal: one additional result that adds weight to Paper I or Paper II, whose
journal drafts live on `review/p1-square-radii` (@ `91ce1cb`) and
`review/p2-square-radius-project` (@ `51dfc1b`). No manuscript, ledger,
status file, result artifact or production code was changed.

## Results

1. **Explicit convergence rate (Paper II).**
   [NOTE_QUANTILE_RATE.md](NOTE_QUANTILE_RATE.md) proves, for every
   nondecreasing quantile template `Q:(0,1]->[0,M]` and every `n >= 2`,

   ```text
   -M <= b_n^Q - n E <= (5/2) M sqrt(n log2 n),
   ```

   hence `R_p^*(n) = C_p n^(p+1) + O(n^(p+1/2) sqrt(log n))` for every fixed
   `p > 0`, with explicit constants that do not depend on the law. For
   consecutive radii:
   `-(1+1/pi) n <= R^*(n) - C_* n^2 <= ((5/2) sqrt(n log2 n) + 1) n/pi`.
   A LaTeX version written against the SIDMA draft's labels is in
   [rate_theorem_section.tex](rate_theorem_section.tex); it compiles inside
   that draft (checked on a scratch copy, manuscript untouched).
2. **Seam-onset law, independent certificate (Paper I).**
   [NOTE_SEAM_ONSET_CERTIFICATE.md](NOTE_SEAM_ONSET_CERTIFICATE.md)
   certifies `s_1 = 8`, `s_k = 4k+5` (`2 <= k <= 5`), `s_k = 4k+6`
   (`6 <= k <= 5000`). The triage found that the all-`k` law is already
   proved in `research/` and only missing from the journal draft.

## Phase 0: triage

| # | Target | Editorial value | Chance in this sprint | Compute | Decision |
|---|---|---|---|---|---|
| 1 | Narrow `0.1405694688 < C_* < 0.140958576058` tenfold | high | low | high | not chosen |
| 2 | Tighten the bracket for `C_2` | high | low | high | not chosen |
| 3 | First seam failure for general `k` | medium to high | certain | minutes | **secondary** |
| 4 | Global certification at `n = 15` (16) | low to medium | medium (15), low (16) | days | not chosen |
| 5 | Explicit rate in the uniform case | high | high | seconds | **primary** |

Reasons.

- **1 and 2.** The lower endpoint for `C_*` exceeds the single
  terminal-subset value `C_term = 0.14056908...` by only `3.9e-7`, and the
  lower endpoint for `C_2` is the optimum of its induced-cycle family. The
  upper witnesses have span/(pi m) equal to `0.1408591` and `0.0884817`
  before the closing term `1/(3200 pi) = 9.9e-5`. *Heuristic reading:* if
  those templates are close to optimal, the true constants sit near the
  upper endpoints, and a tenfold narrowing has to raise the lower bounds by
  about `3e-4`. That needs a new all-pairs lower-bound mechanism or a dual
  certificate for a word program with `k^r` columns. Larger templates alone
  cannot reach a factor ten.
- **3.** Already solved in the repository at proof-note level
  (`research/SUPNICK_SEAM_SEQUENCES.md`, `status=PROVED`, 2026-09-04). The
  cheap missing piece was an independent certificate.
- **4.** `n = 15` has `14!/2 = 43,589,145,600` cyclic classes, 14 times
  `n = 14`, and the retained skeletons grew from 246 to 18,660 between
  `n = 13` and `n = 14`. One more table row would not answer a rejection
  for lack of interest.
- **5.** The SIDMA referee report (major issue 5, decision 3) asks for the
  scope of a finite-size rate, and the draft says the quantile-grid step
  has none. A rate that is uniform in the law strengthens the main theorem.

## Layout

```text
NOTE_QUANTILE_RATE.md            research note, target 5 (statement, proof, limits)
rate_theorem_section.tex         the same result as a LaTeX section draft
NOTE_SEAM_ONSET_CERTIFICATE.md   research note, target 3
rate/rounding_generate.py        generator: explicit instances of the rounding lemma
rate/rounding_certificates.json  18 instances (placements and selected pieces)
rate/rounding_verify.py          independent exact verifier (standard library)
rate/rate_bound_generate.py      generator: table of the explicit bound
rate/rate_bound_table.json       15 rows
rate/rate_bound_verify.py        independent exact verifier (standard library)
seam/seam_generate.py            float64 generator (numpy, scipy), untrusted
seam/seam_certificate.json       18,910 records, k <= 5000
seam/seam_verify.py              rigorous verifier (python-flint / Arb, 128 bits)
seam/seam_verify_stdlib.py       exact-rational cross-check, k <= 100 (standard library)
controls/tamper_controls.py      20 negative controls on the four verifiers
logs/                            outputs and timings of the recorded runs
```

## Reproduction

Environment of the recorded runs: Windows 11, AMD64 (16 logical cores),
Python 3.14.3, python-flint 0.9.0, numpy 2.4.3, scipy 1.17.1. The
generators are deterministic: regenerating both `rate/` JSON files gave
byte-identical output.

Run from `research/fable_sprint_2026-11/`.

| Command | Checks | Time |
|---|---|---|
| `cd rate && python -I rounding_generate.py --out rounding_certificates.json` | generator | 21 s |
| `cd rate && python -I -S rounding_verify.py rounding_certificates.json` | V1-V7, 3,602,455 exact pair checks | 11 s |
| `cd rate && python -I rate_bound_generate.py --out rate_bound_table.json` | generator | < 1 s |
| `cd rate && python -I -S rate_bound_verify.py rate_bound_table.json` | R1-R4, `2 <= n <= 32768` | 3 s |
| `cd seam && python -I seam_generate.py --kmax 5000 --out seam_certificate.json` | generator | 69 s |
| `cd seam && python -I seam_verify.py seam_certificate.json --jobs 12` | S1-S3, onsets, windows | 57 s |
| `cd seam && python -I seam_verify.py seam_certificate.json` | same, one core | 5 min 52 s |
| `cd seam && python -I -S seam_verify_stdlib.py seam_certificate.json 100` | exact rationals, `k <= 100` | 45 s |
| `python -I controls/tamper_controls.py` | 20 negative controls | 32 s |

No computation exceeds a few minutes, so there is no saved state to resume.
To extend the seam certificate, rerun the generator with a larger `--kmax`;
the verifier cost grows like `kmax^2`.

SHA-256 of the tracked certificates (LF line endings, as committed):

```text
f8a0f789da8613f79f930cee8b9fe89e52cf87193249b479602f6fb701a5b340  rate/rounding_certificates.json
c6cc6598e3b9bd8e8b724ce73948cb5924921c825bd97af1842236af1769fa1e  rate/rate_bound_table.json
3ee15c515038d437ba3ef67f1efc74f7936c83eb2d82683be3369dd27572ac84  seam/seam_certificate.json
```

The generator logs in `logs/` come from the determinism rerun, which wrote
to `*.regen.json` and compared the bytes with the tracked files.

## Claim classification

| Claim | Class | Evidence |
|---|---|---|
| Theorem 1 of the rate note | exact theorem, author-internal | written proof, Section 3 of the note |
| Corollary 2, range `n >= 2^11` | exact theorem | written proof, threshold constant checked (R4) |
| Corollary 2, range `2 <= n < 2^11` | computer-certified finite result | `rate_bound_verify.py`, check R3 (run up to `2^15`) |
| Corollaries 3-5 | proved corollaries; for `34 <= n < 2^11` they inherit the computer-checked range of Corollary 2 | Section 4 of the note |
| Finite inequality (3.4) on 18 instances | independently reproduced finite check; a test of the proof, not a premise | `rounding_verify.py` |
| Optimised constant between 1.6 and 2.2 | numerical observation | table, Section 5.1 of the note |
| Examples with `b_n^Q - nE > 0`; uniform law negative for `n <= 10` | exact small examples / numerical observation | Section 7 of the note |
| All-`n` bracket of Section 5.3 | proved corollary of imported certified bounds | SIDMA draft, not re-verified here |
| Seam onsets for `1 <= k <= 5000` | computer-certified finite result, conditional on `thm:seam` of the JOGO draft for the definition of `s_k` | `seam_verify.py`; cross-check for `k <= 100` |
| Seam law for all `k` | exact theorem in existing repository notes, not reviewed in this sprint | `research/SUPNICK_SEAM_SEQUENCES.md` |

Nothing here is a conjecture presented as a theorem. The rate note states
which questions stay open (sharpness, boundedness of `b_n^Q - nE`).

## Assumptions and deviations

- The task asked for everything under this directory and for new files
  only. The dossier required by `AGENTS.md` Section 6 is therefore folded
  into this README and the two notes, and `CURRENT_STATUS.md`, the
  knowledge ledgers and the roadmap were left untouched. Promoting either
  result to a ledger is a separate reviewed task.
- The manuscripts were read from the two review branches at the commits
  above. Lemmas of the SIDMA draft are imported as stated (list (F1)-(F5)
  in the rate note); their proofs were read but not independently
  re-derived.
- `E_UP = 0.4428345` uses the draft's certified bound
  `C_* < 0.140958576058`. Only the uniform-law column of the table depends
  on it.
- The seam certificate trusts Arb for `k > 100`.
- Hosted CI was not run for this branch. All commands above were run
  locally in this sprint.

## Internal review

A separate agent refereed the rate note adversarially before the commit,
with its own brute-force and randomised exact scripts. It found no error in
the chain of Theorem 1 and its corollaries. It found one false sentence in
the sharpness discussion and a sharper count in the rounding lemma. Both are
incorporated: the bound now carries `(k-1) rho` instead of `2(k-1) rho`, and
the constant of Corollary 2 went from `3` to `5/2`. This is not an
independent review in the sense of `RINGMIN_REVIEW_PROTOCOL.md`.

## Verification not performed

- No external or independent human review of the proof of Theorem 1.
- No re-verification of the repository's seam proof notes or of the SIDMA
  draft's certified endpoints.
- `python -m pytest` and `verify.py` were not run: no tracked source,
  test or artifact outside this directory changed.
