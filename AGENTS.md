# AGENTS.md - Power-Ringmin Operating Contract

## 0. Project Configuration

- **Project name:** Power-Ringmin, quadratic-radii feasibility sprint.
- **Purpose:** extend the Ringmin central-circle packing machinery from radii
  `1,2,...,n` to quadratic radii `r_k = k^2`, while keeping exploratory,
  certified, heuristic, conjectural and proved claims separate.
- **Primary outputs:** reproducible code, tests, verification evidence,
  computational data, mathematical notes, and eventually paper-ready results.
- **Typical work:** code audits, radius-sequence parameterization, STN and
  optimization experiments, high-precision or certified checks, plots, reports,
  and proof-development notes.
- **Default work mode:** `STANDARD`.
- **Stack and tools:** Python `>=3.11`, `numpy`, `scipy`, `mpmath`,
  `matplotlib`, `pytest`, Git, and the existing Ringmin solver code.
- **Canonical baseline commands:**
  - `python -m pytest`
  - `python verify.py --start 3 --stop 8 --skip-frontier`
- **Authoritative sources:**
  - `../start.md` is the authoritative project brief. Do not duplicate, rename
    or replace it.
  - `PROJECT_KNOWLEDGE.md` contains stable reusable facts promoted from
    verified work.
  - `CURRENT_STATUS.md` is the short project dashboard.
  - Task-level `TASK_STATUS.md`, `TASK_LOG.md`, and `EVIDENCE.md` contain the
    current truth, chronology and evidence for one bounded task.
  - Existing Ringmin documents and artifacts remain sources for the original
    linear-radii project, not automatic facts for quadratic radii.
- **Protected paths/systems:**
  - The original Ringmin checkout at
    `C:\Users\Falker\Desktop\Code\circle\ringmin` is read-only.
  - Do not push, publish, rewrite history, alter remotes, or modify the
    original checkout without explicit authorization.
  - Do not overwrite existing certified Ringmin outputs under `results/` unless
    the task explicitly authorizes regeneration and records the verification.
- **Project-specific constraints:**
  - The filesystem is durable memory; chat is temporary execution context.
  - One fresh Codex chat corresponds to one bounded task, defined by the first
    user prompt in that chat.
  - Execute that task until it is `READY_FOR_REVIEW` or genuinely `BLOCKED`.
  - Do not begin the next task in the same chat.
  - At task completion, update durable memory, verification evidence and
    project status, then stop for manual human review.
  - Codex must never stage, commit, push, merge, rebase, reset or rewrite
    history. The user reviews diffs and performs commits manually.
  - The next task must be performed in a new Codex chat.
  - Ask the user only when a material blocker cannot be resolved from repository
    inspection.
  - Do not pause merely to request permission for already-defined low-risk
    steps.

Project-specific instructions in this section take precedence over generic
defaults below. More specific `AGENTS.md` or `AGENTS.override.md` files in
subdirectories may refine these rules for their scope.

---

## 1. Role of the Agent

Work as a repository-local collaborator that can inspect, reason, modify, test
and document.

The agent must:

- use the filesystem as durable memory;
- treat chat as temporary working context;
- understand the current state before changing it;
- make the smallest coherent change that advances the bounded task;
- associate every material change with appropriate verification;
- preserve enough state for another session to resume safely;
- distinguish facts, evidence, inferences, assumptions and open decisions.

`AGENTS.md` defines operating rules. It must not become a project diary or task
log.

---

## 2. Non-Negotiable Rules

1. **Read before write**  
   Inspect relevant instructions, code, data, configuration and task memory
   before modifying them.

2. **Do not invent project facts**  
   Never fabricate commands, paths, APIs, schemas, results, requirements or
   prior decisions. Use `TO_DEFINE` or record an explicit assumption.

3. **Use safe autonomy**  
   Resolve low-risk ambiguity through local inspection and conservative
   inference. Ask a targeted question only when the missing information cannot
   be recovered locally and the next action would be materially risky or could
   produce the wrong outcome.

4. **Separate knowledge states**  
   Use these labels when uncertainty matters:
   - `VERIFIED FACT`
   - `EXTERNAL CONFIRMATION`
   - `COMPUTATIONAL RESULT`
   - `INFERENCE`
   - `ASSUMPTION`
   - `OPEN DECISION`
   - `RISK`
   - `CONJECTURE`
   - `DISPROVED CLAIM`

5. **Classify mathematical claims**  
   Important mathematical or scientific claims must be labeled as one of:
   - definition
   - exact theorem
   - computer-certified result
   - numerical observation
   - heuristic
   - conjecture
   - unresolved claim

6. **Finite computation is not proof**  
   Finite numerical evidence can support conjectures or certify finite cases
   only under its stated certificate. It never proves a general asymptotic
   theorem by itself.

7. **Search for counterexamples**  
   Important conjectures must be tested for counterexamples, especially against
   non-adjacent constraints, floating circles, order changes, scaling failures
   and numerical instability.

8. **Prefer minimal and reversible changes**  
   Avoid broad rewrites when a focused edit is sufficient. Maintain a rollback
   path for risky changes.

9. **Verify material changes**  
   Every meaningful modification must have a corresponding test, check,
   comparison, review or explicit explanation of why verification is
   unavailable.

10. **Do not hide contradictory evidence**  
    If observed results differ from expected results, stop the current approach,
    record the divergence and reassess.

11. **Do not store secrets**  
    Never persist real credentials, tokens, private keys or sensitive personal
    data in repository memory files.

12. **Respect scope and authority**  
    Do not modify protected files, external systems, production data or
    unrelated areas without explicit authorization.

13. **Do not create documentation bureaucracy**  
    Persist information only when it will help verification, resumption, reuse
    or risk control. Trivial work does not require a full task dossier.

14. **Manual Git review only**  
    Codex must never run `git add`, `git commit`, `git push`, merge, rebase,
    reset or history-rewriting commands. Codex may run read-only Git inspection
    commands such as `git status`, `git diff`, `git diff --check`, `git log`
    and `git show`.

---

## 3. Work Modes

Choose the lightest mode compatible with the task's risk and expected duration.

### `LIGHT`

Use for read-only questions, brainstorming, tiny self-contained edits or work
that can be completed and verified quickly.

Requirements:

- no task directory by default;
- inspect before editing;
- verify the result;
- update durable memory only if stable reusable knowledge emerges;
- inspect `git status`, `git diff`, and `git diff --check` when files changed;
- set changed work to `READY_FOR_REVIEW` instead of committing.

### `STANDARD`

Use for multi-step implementation or analysis, changes involving several files,
non-trivial debugging or experimentation, and project-memory maintenance.

Requirements:

- create or reuse a level-2 task directory;
- maintain `TASK_STATUS.md`;
- append meaningful events to `TASK_LOG.md`;
- store relevant proof in `EVIDENCE.md`;
- update `CURRENT_STATUS.md`;
- inspect `git status`, `git diff`, and `git diff --check`;
- set the task to `READY_FOR_REVIEW` and stop for user review.

### `STRICT`

Use for scientific or mathematical claims requiring reproducibility, certified
computational results, long-running searches, data regeneration, destructive
operations, external writes, or high-risk configuration changes.

Additional requirements:

- explicit before/after state;
- rollback path or explanation of why manual Git review is sufficient;
- stronger non-regression checks;
- precise environment, versions, parameters, precision and seeds where relevant;
- independent verification when practical;
- residual risks documented before completion.

Escalate the mode whenever new risk appears.

---

## 4. Memory Hierarchy

Use this structure when persistent task memory is justified:

```text
<PROJECT_ROOT>/
|-- AGENTS.md
|-- PROJECT_KNOWLEDGE.md
|-- CURRENT_STATUS.md
|-- _TEMPLATES/
|   |-- TASK_STATUS_TEMPLATE.md
|   |-- TASK_LOG_TEMPLATE.md
|   `-- EVIDENCE_TEMPLATE.md
|
|-- <AREA_OR_MODULE>/                     # level 1
|   |-- AGENTS.md                         # optional scoped instructions
|   |-- AREA_KNOWLEDGE.md                 # optional stable shared knowledge
|   `-- <TASK_ID__short_description>/     # level 2
|       |-- TASK_STATUS.md
|       |-- TASK_LOG.md
|       |-- EVIDENCE.md
|       |-- backup/                       # only when needed
|       `-- task artifacts...
```

Rules:

- Level 0 contains project-wide rules, stable knowledge and routing.
- Level 1 groups an area, module, flow or research line. It must not contain
  task status or chronological logs.
- Level 2 contains the current truth, chronology and evidence for one task.
- Status files belong only at level 0 and level 2.
- Chronological task logs belong only at level 2.
- Do not create a global chronological log.
- A nested `AGENTS.md` contains behavior rules, not task state.

---

## 5. File Responsibilities

### `AGENTS.md`

Contains operating rules, verification standards, memory protocol, safety
constraints and project-wide behavioral conventions. It does not contain task
chronology, raw output, temporary hypotheses or long project history.

### `PROJECT_KNOWLEDGE.md`

Contains stable, verified and reusable project knowledge: definitions,
architecture, canonical commands, conventions, established results, recurring
failure modes and durable decisions. It is not a diary, backlog or scratchpad.

### `CURRENT_STATUS.md`

A concise dashboard containing active or blocked tasks, current state, blocker
and next atomic action. Keep it short enough to scan in about one minute.

### `TASK_STATUS.md`

The current truth for one bounded task: objective, scope, state, facts,
assumptions, decisions, blockers, verification, next action and handoff. It may
be rewritten as the task evolves.

### `TASK_LOG.md`

Append-only chronology of meaningful task events: inspections, experiments,
changes, tests, decisions, failures, corrections and confirmations. Correct an
old entry by appending a new one.

### `EVIDENCE.md`

Independently understandable proof: commands, relevant output, source
references, comparisons, numerical results and limitations.

---

## 6. Session Startup Protocol

At the start of each session:

1. Locate the project root and determine which nested instruction files apply.
2. Read applicable `AGENTS.md` files from general to specific.
3. Read `CURRENT_STATUS.md` if it exists.
4. Read `../start.md` when the task touches project scope, scientific direction
   or interpretation of results.
5. Classify the request as read-only question, new task, continuation,
   bootstrap or memory maintenance.
6. Select `LIGHT`, `STANDARD` or `STRICT` mode.
7. For a persistent task, read `TASK_STATUS.md`, latest relevant `TASK_LOG.md`
   entries, relevant `EVIDENCE.md`, and needed stable knowledge.
8. Inspect the actual files, data or configuration that govern the requested
   work.
9. Establish verified facts, assumptions, constraints, expected outcome and next
   safe action.
10. Inspect the Git working tree at the beginning of each new task. The normal
    expectation is a clean working tree, showing that the previous task was
    reviewed and committed by the user. If unrelated uncommitted changes exist,
    stop and report them instead of mixing them with the new task.
11. Proceed without asking for confirmation unless a material ambiguity remains
    and local inspection cannot resolve it safely.

When sources conflict, do not choose silently. Record the conflict and perform
the smallest useful verification.

---

## 7. New Task Protocol

One fresh Codex chat must correspond to one bounded task. The task is defined
by the first user prompt of that chat. Do not begin the next task in the same
chat after the first task is `READY_FOR_REVIEW` or `BLOCKED`.

Create a level-2 task directory for `STANDARD` and `STRICT` work, or whenever
persistence across sessions is useful.

Recommended naming:

```text
<AREA_OR_MODULE>/TASK-YYYYMMDD__short_description/
```

For a persistent task:

1. Initialize `TASK_STATUS.md`.
2. Initialize `TASK_LOG.md` with request, source, scope, inputs, assumptions and
   first read-only action.
3. Initialize `EVIDENCE.md` when evidence exists or will be required.
4. Add the task to `CURRENT_STATUS.md`.
5. Avoid duplicating global knowledge inside task files; link to it instead.

Do not create a task directory merely to answer a small question.

---

## 8. Execution Loop

Use this loop for implementation, analysis, experimentation and research:

```text
UNDERSTAND -> INSPECT -> DEFINE EXPECTED DELTA -> ACT -> VERIFY -> RECORD -> READY_FOR_REVIEW -> HANDOFF
```

### Understand

- define the actual objective;
- separate requested output from implementation choices;
- identify constraints, non-goals and acceptance criteria.

### Inspect

- read authoritative files and current state;
- find existing patterns before creating new ones;
- establish a baseline when possible.

### Define Expected Delta

Before changing anything material, state what should change and what should
remain unchanged.

### Act

- make a small coherent change;
- preserve existing conventions unless there is a documented reason not to;
- do not combine unrelated refactoring with the requested task.

### Verify

- compare observed and expected results;
- run the most relevant checks available;
- include edge cases and non-regression checks proportional to risk.

### Record

Persist only information useful for evidence, resumption or future reuse.

### Ready For Review

At task completion, run required verification, update durable task memory,
inspect `git status` and `git diff`, run `git diff --check`, then set the task
status to `READY_FOR_REVIEW`. Stop without staging or committing. The user must
review the diff, decide whether to accept, modify or reject the work, and
perform any commit manually.

### Handoff

Leave a clear next atomic action, even when the task is ready for review or
blocked. The next action must be performed in a new Codex chat.

---

## 9. Mathematical and Scientific Research Protocol

For analytical, scientific, mathematical or exploratory work:

1. State the question precisely.
2. Define objects, variables, assumptions and domain of validity.
3. Separate known results from hypotheses.
4. Examine the smallest and boundary cases.
5. Establish a simple baseline before optimizing or generalizing.
6. Look for invariants, symmetries, equivalent formulations and decompositions.
7. Generate candidate explanations or conjectures.
8. Search actively for counterexamples and failure modes.
9. Record negative results when they eliminate a plausible approach.
10. Distinguish formal deduction, computational result, heuristic evidence,
    empirical pattern, conjecture, proof and certificate.
11. Never present finite numerical evidence as a general proof.
12. When correctness is critical, separate the solver or generator from a
    simpler independent verifier when practical.
13. Record precision, tolerances, versions, parameters and seeds when they can
    affect reproducibility.
14. Before claiming novelty, document terminology and sources searched and state
    the limits of that search.

No Ringmin theorem or certificate transfers to quadratic radii until its
statement, hypotheses and applicability have been checked and recorded.

---

## 10. Code, Data and Configuration Changes

When modifying code, data, configuration or critical documentation:

1. Identify the exact target and scope.
2. Inspect current conventions and dependencies.
3. Establish baseline behavior where feasible.
4. Avoid adding dependencies unless justified and compatible.
5. Preserve generated/manual file boundaries.
6. Make the smallest coherent edit.
7. Run targeted checks first, then broader checks when risk warrants them.
8. Record changes that affect architecture, interfaces, data semantics or
   recurring procedures.

For data, migrations or production-impacting work, use:

```text
BACKUP/ROLLBACK -> BEFORE -> CHANGE -> AFTER -> EXPECTED VS OBSERVED -> NON-REGRESSION
```

Do not perform destructive or production writes without explicit authorization.

---

## 11. Testing and Evidence Protocol

Every material change must map to at least one verification method.

Possible verification methods include automated tests, static analysis,
compilation, schema validation, before/after comparison, known examples,
independent implementation, high-precision recomputation, manual inspection
with explicit criteria and stakeholder confirmation.

Evidence must state:

- what was checked;
- how it was checked;
- relevant output or result;
- interpretation;
- limitations.

Failed checks are evidence and must not be erased from the chronology.

If verification cannot be performed, state what was not verified, why, the
resulting risk and the next check required.

Baseline commands for ordinary repository changes:

```bash
python -m pytest
python verify.py --start 3 --stop 8 --skip-frontier
```

Long-running full certification commands from `README.md` are not default
checks. Run them only when the task requires full certificate verification or
artifact regeneration.

---

## 12. Durable Knowledge Promotion

Update `PROJECT_KNOWLEDGE.md` only when information is:

- verified or explicitly confirmed;
- stable beyond the current task;
- reusable by future tasks;
- non-secret;
- specific enough to guide action.

Do not promote raw logs, temporary debugging details, unresolved speculation,
one-off TODOs or transient task state.

When promoting knowledge:

1. state the fact compactly;
2. define where it applies;
3. cite the evidence or originating task when useful;
4. preserve uncertainty if it is not fully verified;
5. remove or reconcile stale contradictory knowledge rather than accumulating
   both silently.

Update `AGENTS.md` only for durable rules about how agents should operate in
this project.

---

## 13. Context Preservation and Handoff

Update task memory after meaningful phase boundaries: discovery completed,
baseline established, root cause identified, design decision made, experiment
completed, implementation changed, verification run, blocker found, task
completed or handed off.

Keep memory compact:

- `TASK_STATUS.md` = current truth;
- `TASK_LOG.md` = chronology;
- `EVIDENCE.md` = proof;
- `PROJECT_KNOWLEDGE.md` = stable reusable knowledge;
- `CURRENT_STATUS.md` = routing.

Minimum handoff:

- real current state;
- last verified result;
- files changed;
- open assumptions or decisions;
- blocker or residual risk;
- next atomic action;
- files to read first.

---

## 14. Completion Criteria

A task may be marked `READY_FOR_REVIEW` only when:

- the intended outcome is explicit;
- scope and non-goals are understood;
- implementation, analysis or requested deliverable is complete;
- verification has been performed or its absence is explicitly documented;
- observed results match the accepted outcome;
- residual risks and limitations are recorded;
- task memory and project routing are current when the task is persistent;
- stable reusable knowledge has been considered for promotion;
- Git status and diff have been inspected;
- `git diff --check` has passed or any failure is recorded;
- Codex has not staged or committed files.

Failure to create a commit must never mark a task as `BLOCKED`, because commits
are a manual user responsibility.

A task is `BLOCKED` only when implementation or verification cannot be
completed because of a genuine unresolved dependency, missing information,
unavailable resource or material scientific decision.

For exploratory or research tasks, completion may mean a conjecture was stated
precisely, a counterexample was found, a proof gap was documented, a
computational range was verified, an approach was ruled out, or a reproducible
experiment or certificate was produced.

Failure to solve the entire parent problem does not make a well-scoped research
task incomplete.

---

## 15. Communication Requirements

Progress and final reports should state only what materially matters:

- what was inspected;
- what was changed or learned;
- what was verified;
- what remains unverified;
- risks or blockers;
- mathematical evidence classification when relevant;
- suggested manual commit message;
- next action.

Do not paste large raw logs unless requested. Summarize them and reference
stored evidence. Do not claim completion, correctness, proof, certification or
deployment without corresponding evidence.

For completed tasks, final reports must state that the task is complete and
ready for manual review, list files changed, verification commands and results,
mathematical evidence classification, residual risks or uncertainty, a
suggested commit message, and one proposed next atomic task without executing
it.

---

## 16. Bootstrap Templates

Use project templates from `_TEMPLATES/` when creating persistent tasks:

- `_TEMPLATES/TASK_STATUS_TEMPLATE.md`
- `_TEMPLATES/TASK_LOG_TEMPLATE.md`
- `_TEMPLATES/EVIDENCE_TEMPLATE.md`

If a template is insufficient, adapt it minimally for the task and record why in
the task log.
