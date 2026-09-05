# Task Status

```text
task=TASK-20260905__permuted_halves_root_search
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective

Test whether the best increasing cyclic high shift minimizes the unique
root rho_P of S_P(R)=2*pi among all high permutations, for m=2..8 only,
stopping after completing the first counterexample size.

## Scientific question

For each visited integer m, compare min_{P in Sym({m+1,...,2m})} rho_P
with min_{0<=s<m} rho_{P(s)}, P(s)_i=m+1+((i+s-1) mod m).
The all-m root conjecture is unresolved at startup; fixed-R small-R
counterexamples do not decide it. Use the exact full criterion and local
swap theory in the two preceding research notes.

## In scope and expected delta

A new research/PERMUTED_HALVES_ROOT_SEARCH.md, this dossier (scripts,
finite outputs, evidence), knowledge/FIXED_ORDER_THEORY.md,
research/NEXT_RESEARCH_STEPS.md and CURRENT_STATUS.md.

## Out of scope and protected paths

General asymptotic optimization, orders outside this family, production
certification and published claims. All other paths are protected,
especially the preceding two proof notes, prior dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, publication metadata,
README.md, REPORT.md, other ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md
and RINGMIN_REVIEW_PROTOCOL.md. Check the full changed-path whitelist.

## Predeclared experiment

- Ascending m=2..8, every m! labeled high permutation, no symmetry
  reduction, candidate cap, pruning, random seed or multiprocessing.
- 80-decimal mpmath direct asin cell scorer; 240 bisections per root,
  positive bracket [1/100,4*m*m], bracket signs checked; comparison guard
  1e-60, preserving every near tie for later checking.
- Finish all permutations at a size, then stop if arbitrary minimum
  improves on every shift by more than the guard. Never run above m=8.
- Separate scorer with alternate half-angle atan formula and independent
  enumeration at 110 digits; exact rational angular/pi enclosures for a
  fixed-R root separator and the smaller-size exclusion if needed.
- JSON schema: provenance/precision/domain, per-size counts, every order
  and numerical root bracket, all numerical minimizers, shift minima,
  root gap and explicit stop reason. Numerical brackets alone are not
  rigorous intervals. Source hashes accompany retained artifacts.
- If refuted, record the least m with certified root separation and
  retain local swap explanation; if not, retain only finite evidence.
  Either outcome updates the roadmap to a bounded independent review,
  without starting the general asymptotic problem.

## Completion gates

- [x] bounded enumeration and independent numerical comparison;
- [x] rigorous counterexample/minimality checks if a witness is found;
- [x] proof/evidence classification and provenance;
- [x] owning ledger, roadmap and current status updated;
- [x] complete tracked/untracked diff, whitespace and protected paths;
- [x] READY_FOR_REVIEW handoff.

## Blockers

None. Git ownership requires only a per-command safe.directory option;
no persistent configuration or Git state changes are needed.

## Handoff

The root-level shift conjecture is refuted at the least m=4; all 32 orders
at m=2,3,4 were independently rescored and exact rational separators certify
the finite minimizers and strict root comparison. m=5..8 were not run.
All 11 allowed files passed content, whitespace and provenance checks;
every other tracked path is protected and unchanged. No blocker; human
review of the proof and imported fixed-order dependency remains pending.

Suggested manual commit: research: certify minimal cyclic-shift root counterexample

Exactly one next atomic task: independently review the minimal root
counterexample, reproduce the 32 roots and rational separators, audit
coverage/minimality and the mixed/chain root swap with its fixed-order
dependency, and record acceptance or precise corrections. Do not start
general permutation or asymptotic optimization.
