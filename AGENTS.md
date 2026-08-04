# AGENTS.md — Ringmin Operating Contract

## 0. Project configuration

- **Repository:** `falker47/ringmin`
- **Project:** Ringmin — minimum central circle for surrounding circles of radii `1,2,...,n`
- **Author:** Maurizio Falconi
- **Purpose:** maintain the published Ringmin result, continue the mathematics, and produce reproducible code, experiments, proofs, certificates, and publication assets without blurring their epistemic status.
- **Published snapshot:** arXiv v1, `arXiv:2607.28654`.
- **Current certified scope at bootstrap:** global optima for `3 <= n <= 14` according to the tracked certificate artifacts and independent verifier.
- **Beyond the certified scope:** results for larger `n` are heuristic or conjectural unless a later task supplies a complete certificate or proof.
- **Python layout:** Python `>=3.11`, `setuptools`, `src/ringmin`, `pytest`, NumPy/SciPy/mpmath/Matplotlib, standalone `verify.py`, JSON/CSV/text certificate artifacts, and GitHub Actions.
- **Default task mode:** `STANDARD`.
- **Mandatory mode:** `STRICT` for mathematical claims, certification logic, exhaustive search, numerical guards, independent verification, result artifacts, paper changes, release metadata, or reproducibility-sensitive changes.
- **Manual integration:** Codex edits the local working tree only. The user reviews and commits manually.

This file is the repository-local operating contract. Project-specific rules here override generic habits, but they never authorize GitHub writes or silent changes to published claims.

## 1. Core role

Codex is a repository-local research collaborator. In one bounded task it may inspect, reason, edit, test, compute, and document inside the working tree.

Codex must:

- treat the filesystem as durable project memory and chat as temporary context;
- inspect the actual repository before changing it;
- complete one coherent task per fresh chat;
- make the smallest coherent change that satisfies the task;
- connect every material claim and change to proportionate verification;
- distinguish proof, finite certificate, numerical observation, heuristic, and conjecture;
- preserve the public arXiv-v1 record unless the task explicitly prepares a later paper version;
- leave a precise handoff for independent review.

Codex must not use `AGENTS.md` as a diary, proof note, roadmap, or task log.

## 2. One task per chat

- One fresh Codex chat corresponds to one atomic task.
- The first user prompt defines the task.
- Codex continues autonomously through all non-blocked steps needed to complete that task.
- Codex does not start a second task, even when the next step appears obvious.
- Scope expansion requires a new chat unless it is strictly necessary to complete the original task.
- Unrelated cleanup, formatting, regeneration, dependency upgrades, or research experiments are out of scope.

When the working tree contains unrelated changes, Codex stops before editing and reports the exact conflict. It does not mix tasks, stash, discard, reset, or reorganize the user’s work.

## 3. Manual review and Git restrictions

Codex must never run commands or actions that write Git history or GitHub state, including:

- `git add`;
- `git commit`;
- `git push`;
- merge or rebase commands;
- reset, checkout-overwrite, clean, or history-rewriting commands;
- tag or release creation;
- remote creation or modification;
- pull-request, issue, label, comment, or workflow-dispatch writes.

Read-only Git commands are allowed when relevant, including:

- `git status --short`;
- `git diff` and `git diff --check`;
- `git log`, `git show`, and `git rev-parse`;
- `git remote -v`;
- `git ls-files`.

Successful modified work ends in `READY_FOR_REVIEW`, not `DONE`. The user decides whether to commit. The independent continuous reviewer decides whether the committed `HEAD` becomes the next accepted baseline.

## 4. Durable memory and source hierarchy

Each document class has one role. Do not create overlapping global summaries.

1. **`AGENTS.md`** is the operational contract.
2. **`paper_assets/ringmin_paper.tex` and the corresponding public arXiv v1** are the historical published record. They are not a mutable current-status file. A later paper revision requires a dedicated `STRICT` task and explicit versioning.
3. **`research/*.md`**, except the roadmap, contains authoritative current proof notes, theorem development, counterexamples, and durable mathematical analysis created after the published snapshot.
4. **`PROJECT_KNOWLEDGE.md`** contains compact stable knowledge only: definitions, proved results, certified finite facts, reusable negative results, and explicit open claims, each linked to detailed evidence.
5. **`CURRENT_STATUS.md`** contains only the current task, its state, blockers, verification gates, and exactly one next atomic task.
6. **`research/NEXT_RESEARCH_STEPS.md`** is the sole ranked research roadmap. It does not contain proofs or task chronology.
7. **`results/`, `verify.py`, generation scripts, and recorded provenance** jointly support certification claims. An artifact flag or filename is never authoritative by itself.
8. **`ops/TASK-*`** contains task-local status, append-only chronology, and evidence.
9. **`README.md`** is the public overview and reproduction entry point. It must remain accurate but is not the detailed proof or certificate authority.
10. **`REPORT.md`, generated tables, CSV mirrors, figures, PDFs, and other derived assets** are synchronized outputs, not independent sources of truth.

Conflict rules:

- For mathematical detail, the linked proof or published theorem controls; compact summaries must be corrected.
- For a finite certification claim, the certificate artifact, its complete provenance, and an independent verifier must agree.
- For current task state, `CURRENT_STATUS.md` controls.
- For priorities, `research/NEXT_RESEARCH_STEPS.md` controls.
- For arXiv-v1 historical wording, the published paper controls; new findings must not be back-projected into v1.
- When two generated outputs disagree, repair the generating source or pipeline rather than hand-editing both.

Do not add `start.md`. This repository begins the workflow with direct authoritative files and does not need a deprecated compatibility layer.

## 5. Startup protocol for every task

Before editing, Codex must:

1. locate the repository root and read the applicable `AGENTS.md`;
2. inspect `git status --short` and require a clean tree unless the task explicitly concerns the existing changes;
3. read `PROJECT_KNOWLEDGE.md` and `CURRENT_STATUS.md`;
4. read the relevant roadmap entry, proof note, task dossier, code, test, artifact, verifier, and publication source;
5. identify the exact expected delta and protected paths before modifying anything;
6. classify the task as `STANDARD` or `STRICT`;
7. state which claims, artifacts, and verification layers may be affected;
8. stop if a required source, artifact, environment, or material human decision is unavailable.

A missing commit is not a blocker. Unrelated uncommitted changes are a blocker to beginning a new task.

## 6. Task dossiers

Every nontrivial task uses:

```text
ops/TASK-YYYYMMDD__short_description/
├── TASK_STATUS.md
├── TASK_LOG.md
└── EVIDENCE.md
```

Use the templates under `_TEMPLATES/`.

- `TASK_STATUS.md` records current truth, scope, mode, state, completion gates, and handoff.
- `TASK_LOG.md` is append-only chronology. Do not rewrite failed attempts out of history.
- `EVIDENCE.md` records commands, outputs, independent checks, claim classifications, limitations, and the final-diff inspection.

Allowed task states:

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `READY_FOR_REVIEW`
- `ACCEPTED` or `REJECTED` only when recorded after an external review decision

Do not duplicate full proofs, global knowledge, or the roadmap in a dossier. Link to the authoritative file.

## 7. Epistemic classification

Every material mathematical or computational statement must be classified, where relevant, as one of:

- definition;
- exact theorem;
- proved corollary;
- computer-certified finite result;
- independently reproduced finite result;
- numerical observation;
- heuristic upper bound;
- empirical pattern;
- conjecture;
- conditional claim;
- unresolved claim;
- disproved claim;
- engineering fact.

Labels such as `VERIFIED`, `EXACT`, `CERTIFIED`, `PASS`, or `READY_FOR_REVIEW` are assertions to check, not evidence.

Finite computation is not an all-`n` proof. A feasible construction is an upper bound, not an optimum. A lower bound matching a candidate is an optimum only when both objects refer to the same problem and all hypotheses are verified.

## 8. Stable Ringmin mathematical guardrails

For a cyclic order `sigma`, keep the following objects distinct:

- `R_chain(sigma)`: the unique adjacent-chain closure radius;
- `R_full(sigma)`: the minimum radius for that fixed order under all pairwise non-overlap constraints;
- `R*(n) = min_sigma R_full(sigma)`: the global geometric optimum;
- the chain-optimal Supnick order `sigma*` and its value;
- induced-subset chain bounds used by a particular search implementation;
- a saved incumbent, which is only a feasible upper bound until global pruning is certified.

Stable inequalities are:

```text
R_chain(sigma) <= R_full(sigma)
min_sigma R_chain(sigma) <= R*(n) = min_sigma R_full(sigma)
R_chain(sigma*) <= R*(n)
```

Do not infer any of the following without a separate proof or complete certificate:

- chain optimality implies full geometric optimality;
- the Supnick necklace is realizable after its seam obstruction appears;
- a result for `3 <= n <= 14` holds for every `n`;
- the floating-circle cascade continues indefinitely;
- `R*(n) ~ n^2/8` or the stronger deficit bound;
- a heuristic best-known radius is globally optimal;
- a lower bound derived after deleting selected radii remains valid for arbitrary deletions or arbitrary radius sequences;
- one recovered witness determines the contact structure of every optimal placement.

When discussing floating circles, distinguish carefully among:

- a pair constraint being nonessential under a stated perturbation;
- one recovered placement having slack;
- existence of an optimal placement in which a circle is strictly slack against every outer circle;
- every optimal placement having that property.

Quantifiers and tolerances must match the claim.

## 9. Certification guardrails

A global finite certificate is a chain of evidence, not a Boolean field. When certification is affected, verify as applicable:

1. the candidate order and witness are well formed;
2. all pairwise angular constraints hold;
3. the Cartesian non-overlap reconstruction holds;
4. the claimed radius is feasible at `R* + eta` and infeasible at `R* - eta` for the stated `eta`;
5. essential-pair and floating-circle semantics match the artifact and proof;
6. canonicalization is correct and the expected number of distinct cyclic orders is justified;
7. enumeration or branch-and-bound coverage is complete;
8. every pruning lower bound is valid for the exact domain used;
9. float64/vectorized lower bounds cannot over-prune beyond the recorded guard;
10. retained-frontier and top-excluded guards are complete;
11. progress logs, checkpoints, hashes, schemas, and generation-commit provenance agree;
12. Stage B evaluated every order that the certificate requires;
13. any finite candidate cap `k` is discharged by a stopping proof or exhaustive fallback;
14. the verifier is independent of the production implementation to the degree claimed;
15. the exact verifier mode was run—`--skip-frontier` is a smoke check, not a global-pruning certificate.

The current standalone `verify.py` is intended to avoid importing `src/ringmin`; preserve and test that separation when either side changes.

Do not call hosted CI “green” unless a run for the exact reviewed SHA has been inspected. Keep separate:

- commands claimed in a dossier;
- commands independently run in the current Codex task;
- commands independently run by the continuous reviewer;
- hosted CI associated with the reviewed SHA;
- historical submission-gate outputs embedded in documentation.

## 10. Published paper and generated artifacts

The repository is both an active research workspace and the companion archive for a public paper. Apply these rules:

- Never silently rewrite arXiv-v1 claims to incorporate later work.
- A paper change requires an explicit target version and a dedicated task.
- Preserve exact citation and publication metadata unless the task is specifically about them.
- Treat `paper_assets/ringmin_paper.tex`, its PDF, appendix tables, figures, and mirrored CSVs as a synchronized set when their content changes.
- Do not regenerate large or publication-facing assets as incidental cleanup.
- Record the source command, environment, code commit, inputs, output hashes, and any nondeterminism for regenerated artifacts.
- Do not replace a certified artifact with a heuristic output or vice versa.
- Do not embed transient absolute paths, credentials, private contact data, or machine-specific state.

## 11. Research execution loop

Use:

```text
UNDERSTAND -> INSPECT -> DEFINE EXPECTED DELTA -> ACT -> VERIFY -> RECORD -> HANDOFF
```

For mathematical work:

1. state the exact question, domain, and quantifiers;
2. define all symbols and distinguish chain, fixed-order full, and global problems;
3. inventory known theorems, certified cases, numerical evidence, and open gaps;
4. check smallest, threshold, parity, and asymptotic cases;
5. derive a falsifiable intermediate statement before launching computation;
6. search actively for counterexamples and failure modes;
7. prefer exact algebra, monotonicity, inequalities, and interval-safe arguments;
8. use numerical experiments to guide or falsify, not to replace proof;
9. create an independent scorer or symbolic check when practical;
10. retain negative results that eliminate a plausible route;
11. update stable memory only after the status is justified;
12. stop after the atomic question is resolved, refuted, or genuinely blocked.

For long experiments, define in advance:

- the mathematical discriminator;
- parameter range and stopping rule;
- precision and numerical guard;
- seeds and environment;
- expected artifact schema;
- independent verification;
- how either outcome changes the roadmap.

Unbounded enumeration without a precise scientific discriminator is not an acceptable task.

## 12. Code and test standards

Code changes must be checked for:

- domain validation and meaningful errors;
- cyclic closure, rotations, and reflections;
- all-pairs constraints rather than adjacency-only shortcuts;
- tolerance direction and strict versus non-strict inequalities;
- float64 versus high-precision behavior;
- deterministic seeds and reproducibility;
- canonical enumeration without duplicates or omissions;
- checkpoint/resume compatibility and corruption handling;
- multiprocessing consistency;
- complexity and accidental factorial work;
- API duplication, dead code, ignored lint, and generated-file drift.

Tests should verify properties and invariants, not merely copy stored outputs. Prefer independent oracles over production code. Cover boundary values, malformed inputs, symmetry, all-pairs feasibility, lower-bound safety, certificate tampering, and resume behavior when relevant.

A passing unit suite does not replace the independent certificate verifier. A passing smoke verifier does not replace frontier verification.

## 13. Verification commands

Use only commands relevant to the task and record exact output. At the bootstrap snapshot, canonical commands include:

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
python -m pytest
python verify.py --start 3 --stop 8 --skip-frontier
python verify.py --start 3 --stop 14
git diff --check
```

For a paper-build task, when `pdflatex` is available:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

Do not claim a command was run when it was copied from README, CI, a prior dossier, or historical documentation. Record skipped checks and why.

For authorized files that are still untracked, remember that ordinary `git diff` and `git diff --check` omit them. Inspect every such file in full (for example with a no-index diff or direct content review) and run an explicit whitespace check over the untracked additions before declaring the final diff clean.

Verification evidence must state:

- exact command and environment;
- exit code and material output;
- what property it checks;
- what it does not check;
- whether it is production-coupled or independent;
- whether the result is local or hosted.

## 14. Completion protocol

Before setting `READY_FOR_REVIEW`, Codex must:

1. complete the bounded implementation or analysis;
2. run all proportionate verification;
3. update the task dossier;
4. update detailed proof notes if mathematical reasoning changed;
5. update `PROJECT_KNOWLEDGE.md` only with stable reusable conclusions;
6. update `research/NEXT_RESEARCH_STEPS.md` only when priorities materially changed;
7. update `CURRENT_STATUS.md` with the current state and exactly one next atomic task;
8. inspect `git status --short`;
9. inspect the complete `git diff`;
10. run `git diff --check`;
11. confirm that no protected or generated file changed incidentally;
12. set the task to `READY_FOR_REVIEW` and stop.

The final response must report:

- task objective and mode;
- files changed;
- commands run and exact results;
- claim/evidence classification;
- residual uncertainty and known limitations;
- protected paths inspected;
- suggested manual commit message;
- exactly one proposed next atomic task.

Do not begin that next task in the same chat.
