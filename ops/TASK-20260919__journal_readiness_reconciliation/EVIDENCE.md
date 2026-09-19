# Evidence

## Environment

```text
repository_head=f6f22e95af495a4b0385322a5b6add5966cd7296
branch=main
platform=Windows
powershell=7.6.5
python=3.14.3
dependency_source=existing environment; documentation checks use stdlib only
task_mode=STRICT
```

Git commands in the sandbox use command-local
`-c safe.directory=<repository-root>`; no Git configuration is modified.

## Accepted review provenance

The task's user supplied the completed independent STRICT review and stated
that the Review State Registry accepted baseline is
`f6f22e95af495a4b0385322a5b6add5966cd7296`. This is the authority received for
recording acceptance, not an inference from an artifact label, task status or
CI success. No Registry read/write or new independent mathematical review was
performed by this reconciliation. The new commit is READY_FOR_REVIEW, not an
automatic replacement of that accepted baseline.

The supplied review accepted exclusively `n=3,...,14`,
`L_n < R*(n) <= U_n`, exact `U_n - L_n = 10^-11`. It reported independent
checks of all 908 angular intervals with cosine and rational/integer arithmetic;
coverage of 3,374,988,556 canonical classes; a backward DP distinct from the
integrated forward DP; strict `>` pruning and rejection of a `>=` mutant;
reinsertion of radius 1 into every gap, including the final gap; 47 upper
witnesses, 540 central tangencies and 3,004 exact Cartesian pair checks.

It also reported P1 closed by a per-n witness requirement and rejection of the
false n=4 bracket with 47 redistributed witnesses; P2 closed for
`dp_table_sha256`, `pruning_and_skeleton_stream_sha256` and `input_cases_sha256`;
generator/candidate/Windows/CASES binding checked; all twelve declared CASES
`frontier_blob` values matched actual reference-commit Git blobs; both merge
parents and protected solver/results/verifier/publication bytes were preserved.
Those independent review checks are supplied evidence, not local reruns here.

The review did not accept the fixed-order seam theorem as a self-contained
journal component, general optimizer structure, universal contact/floating
classification, n>14 results, asymptotics, peer review or overall journal
readiness. The unchanged [proof note](../../research/GLOBAL_BRACKET_CERTIFICATE.md)
owns the proof and the integrated verifier's own narrower provenance checks.

## Exact closure wording

> The former numerical-certification journal blocker is closed for this finite
> claim through the accepted exact global-bracket route: the historical
> Stage-A/Top-K/frontier float64 path is no longer a necessary dependency of its
> proof. This does not retroactively certify historical float64 pruning.

Here "this finite claim" is exactly the twelve brackets above. The old
Stage-A/Top-K/frontier route retains its numerical limitations and historical
provenance. No worst-case float64 proof, checkpoint recovery or replay is implied.

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| Accepted twelve exact global brackets | computer-certified finite result, independently reviewed | supplied review at the named baseline; unchanged certificate/proof/verifier | acceptance received from user; not re-reviewed here |
| Numerical journal blocker closed for that claim | scientific/editorial reconciliation | accepted route has its own complete global lower/upper proof | no retro-certification of historical pruning |
| Seam self-containedness remains a journal gate | unresolved publication claim | historical mock report and user's review boundary | no new seam proof or manuscript |
| Protected paths and ZIP preserved | engineering fact | current-task diff/hash checks below | preservation does not itself prove mathematics |

## Commands and checks

Startup local reads:

- `git rev-parse HEAD`: exit 0, full baseline SHA above.
- `git branch --show-current`: exit 0, `main`.
- `git status --short`: exit 0, only `?? paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip`.
- `git log --oneline f6f22e95af495a4b0385322a5b6add5966cd7296..HEAD`:
  exit 0, empty output.
- `python --version`: exit 0, `Python 3.14.3`.
- `Test-Path -LiteralPath paper_assets/journal_dcg`: `False`; targeted file
  listing found no journal/DCG manuscript.
- `Get-FileHash -LiteralPath paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip -Algorithm SHA256`:
  hash `e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`,
  unchanged from the merge dossier; size 316076 bytes.

Read-only GitHub connector calls in this task:

- `github_fetch` of `https://api.github.com/repos/falker47/ringmin/branches/main`:
  main SHA equals the baseline.
- `github_fetch` of `https://api.github.com/repos/falker47/ringmin/actions/runs/35450959211`:
  `head_sha` equals baseline; `status=completed`, `conclusion=success`.
- `github_fetch_workflow_run_jobs(repo_full_name="falker47/ringmin", run_id=35450959211)`:
  job 105917907440 and all test/smoke/global-bracket steps completed successfully.
- `github_fetch_workflow_job_logs(repo_full_name="falker47/ringmin", job_id=105917907440)`:
  `59 passed in 25.05s`, `PASS_GLOBAL_BRACKETS`, `pinned_input_verification: PASS`.

This is inspected [hosted baseline CI](https://github.com/falker47/ringmin/actions/runs/35450959211),
not hosted CI for the new documentation commit. No local pytest, verifier,
Stage A, generator replay, checkpoint recovery or large enumeration is needed
or claimed for this text-only delta.

## Artifact and provenance checks

No artifact generation is applicable. `src/`, `results/`, both verifiers,
certificate tests, original evidence, paper sources/PDFs and `CITATION.cff`
are protected. The original certificate and proof remain controlling; this
task changes only their current acceptance/status references. The 2026-09-16
journal documents are consulted as dated historical evidence, not rewritten.

## Failed checks and negative evidence

Initial Git reads failed with dubious ownership; command-local safe.directory
resolved that without configuration changes. The unrelated ZIP initially
blocked editing until the user's explicit exception. The sandbox reports an
inaccessible global Git ignore file; tracked-file diffs and explicit ZIP checks
are used. A CODEX_HOME lookup found no variable and was not needed further.

## Reproducible document and preservation check

The following stdlib-only check reads the eight task documents, Git paths,
original manifest and endpoint metadata. It does not execute a solver or prove
the certificate; semantic claim boundaries are inspected in the complete diff.

```python
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import subprocess

root = Path.cwd()
base = "f6f22e95af495a4b0385322a5b6add5966cd7296"
dossier = "ops/TASK-20260919__journal_readiness_reconciliation"
canonical = ["CURRENT_STATUS.md", "PROJECT_KNOWLEDGE.md",
             "knowledge/CERTIFICATION.md", "knowledge/PUBLICATION_HISTORY.md",
             "research/NEXT_RESEARCH_STEPS.md"]
files = canonical + [f"{dossier}/{name}.md"
                     for name in ("TASK_STATUS", "TASK_LOG", "EVIDENCE")]
zip_path = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
def git(*args):
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={root.as_posix()}", *args],
        text=True, encoding="utf-8").strip()
assert git("branch", "--show-current") == "main"
git("merge-base", "--is-ancestor", base, "HEAD")
changed = set(git("diff", "--name-only", base).splitlines())
untracked = set(git("ls-files", "--others", "--exclude-standard").splitlines())
assert changed | (untracked - {zip_path}) == set(files)
assert zip_path in untracked
assert not git("ls-files", "--", zip_path)
assert hashlib.sha256(Path(zip_path).read_bytes()).hexdigest() == (
    "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db")
links = 0
shas = set()
for name in files:
    path = Path(name)
    text = path.read_text(encoding="utf-8")
    assert text.endswith("\n") and not text.endswith("\n\n"), name
    assert all(line == line.rstrip() for line in text.splitlines()), name
    shas.update(re.findall(r"\b[0-9a-f]{40}\b", text))
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if "://" in target:
            continue
        target_path, _, anchor = target.partition("#")
        dest = path.parent / target_path if target_path else path
        assert dest.is_file(), (name, target)
        if anchor:
            headings = re.findall(r"^#{1,6} (.+)$",
                                  dest.read_text(encoding="utf-8"), re.M)
            slugs = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")
                     for h in headings}
            assert anchor in slugs, (name, target)
        links += 1
for sha in shas:
    git("cat-file", "-e", sha + "^{commit}")
status = Path("CURRENT_STATUS.md").read_text(encoding="utf-8")
assert status.count("## Exactly one next atomic task") == 1
next_task = status.split("## Exactly one next atomic task\n", 1)[1]
assert "fixed-order seam theorem / self-containedness" in next_task
assert "\n## " not in next_task and not re.search(r"^\d+\.", next_task, re.M)
assert f"accepted_baseline={base}" in status
assert not Path("paper_assets/journal_dcg").exists()
evidence = Path("reproducibility/global_brackets")
manifest = json.loads((evidence / "manifest.json").read_text())["files"]
for item in manifest:
    data = (evidence / "originals" / item["path"]).read_bytes()
    assert len(data) == item["bytes"]
    assert hashlib.sha256(data).hexdigest() == item["sha256"]
candidate = evidence / "originals/source/ringmin_global_interval_candidate.json"
cases = json.loads(candidate.read_text())["certificate"]["cases"]
assert [row["n"] for row in cases] == list(range(3, 15))
assert all(Fraction(row["U"]) - Fraction(row["L"]) == Fraction(1, 10**11)
           for row in cases)
print(f"PASS_DOC_SCOPE: {len(files)} Markdown files; {links} local links/anchors; "
      f"{len(shas)} commit references; one next task")
print(f"PASS_PRESERVATION: all other tracked paths unchanged; "
      f"{len(manifest)} original files hash-match; ZIP untouched/untracked")
print("PASS_ENDPOINT_METADATA: 12 cases, n=3..14, exact width=1/100000000000")
```

## Final diff inspection

The embedded check was executed locally with this exact PowerShell command:

```powershell
python -c 'from pathlib import Path; s=Path("ops/TASK-20260919__journal_readiness_reconciliation/EVIDENCE.md").read_text(encoding="utf-8"); marker=chr(96)*3; exec(s.split(marker+"python\n",1)[1].split(marker,1)[0])'
```

Exit 0, material output:

```text
PASS_DOC_SCOPE: 8 Markdown files; 52 local links/anchors; 3 commit references; one next task
PASS_PRESERVATION: all other tracked paths unchanged; 13 original files hash-match; ZIP untouched/untracked
PASS_ENDPOINT_METADATA: 12 cases, n=3..14, exact width=1/100000000000
```

`git diff --check`: exit 0, no output. The full five-file canonical diff and
all three new dossier files were read; the embedded check explicitly reads
every new file and checks trailing whitespace and blank EOF, including files
that ordinary `git diff --check` omits while untracked. Only those eight
Markdown files differ from baseline. All protected paths, historical dossiers
and generated assets remain unchanged. The exempt ZIP remains untracked with
its initial hash and is never selected for staging.

Semantic inspection confirms the exact finite quantifier/inequality/width,
closure through a separate exact route, preservation of historical float64
limitations, and no new n>14, universal contact/floating, peer-review or overall
journal-readiness claim. No stable theorem was copied into another thematic
ledger; the publication ledger and compact index cross-reference the owner.
CURRENT_STATUS has exactly one next atomic task, the fixed-order seam treatment.

`rg -n --glob '*.md' 'journal-readiness-phase-2026-09-16|priority-1--one-independent-external-review|subsequent-scientific-questions' .`:
exit 1, no matches; no inbound links use the three changed old section anchors.

Staged exactly the eight named Markdown paths using the standing authorization
and tool escalation for index access. Inspected `git diff --cached`;
`git diff --cached --check` and `git diff --exit-code` both exited 0, with no
whitespace errors or unstaged tracked changes. The staged audit is repeated
after this evidence entry. The normal push, resulting SHA and actual remote
state are checked afterward and reported at handoff; no post-commit success
is inferred in advance.

## Residual uncertainty

The seam publication gate remains unresolved. Acceptance of the baseline's
finite brackets does not imply peer review, journal readiness or acceptance of
this new reconciliation commit. Historical float64 limitations remain. No new
Registry access is claimed. The final SHA, normal push and any exact-SHA hosted
outcome will be reported after commit; they cannot be embedded in that same SHA.
