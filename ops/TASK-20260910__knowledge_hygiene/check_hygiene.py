"""Bounded, standard-library documentation audit; does not verify mathematics."""

from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = "ab6f663200f8d9eae95d30c6c96eb6c052aed881"
TASK = "ops/TASK-20260910__knowledge_hygiene"
ROADMAP = "research/NEXT_RESEARCH_STEPS.md"
ARCHIVE = "docs/archive/RESEARCH_ROADMAP_20260910.md"
MODIFIED = {
    "AGENTS.md", "PROJECT_KNOWLEDGE.md", "CURRENT_STATUS.md", ROADMAP,
    "docs/post_arxiv_tasks.md", "SUBMISSION_CHECKLIST.md",
    "SUBMISSION_REVIEW_REPORT.md",
}
ADDED = {ARCHIVE} | {
    f"{TASK}/{name}" for name in
    ("TASK_STATUS.md", "TASK_LOG.md", "EVIDENCE.md", "check_hygiene.py")
}


def git(*args, data=None):
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}",
         "-c", "core.excludesFile=", *args], cwd=ROOT, input=data
    )


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def baseline(path):
    return git("show", f"{BASE}:{path}")


def section(text, heading):
    start = text.index(heading)
    end = text.find("\n## ", start + 1)
    return text[start:] if end < 0 else text[start:end + 1]


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


old_bytes = baseline(ROADMAP)
old = old_bytes.decode("utf-8")
new = read(ROADMAP)
begin = b"<!-- BEGIN VERBATIM ROADMAP SNAPSHOT -->\n````markdown\n"
end = b"````\n<!-- END VERBATIM ROADMAP SNAPSHOT -->\n"
# Normalize checkout CRLF; the original Git payload is LF.
archive_bytes = (ROOT / ARCHIVE).read_bytes().replace(b"\r\n", b"\n")
payload = archive_bytes.split(begin, 1)[1].rsplit(end, 1)[0]
require(payload == old_bytes, "archive payload differs from baseline blob")
require(sha256(payload).hexdigest() in read(ARCHIVE), "missing payload hash")
require(BASE in read(ARCHIVE), "missing archive baseline")
headings = re.findall(r"^## .+$", old, flags=re.M)
require(all(section(old, h) in payload.decode() for h in headings),
        "missing original section")
print(f"PASS archive: {len(payload)} bytes, {len(old.splitlines())} lines, "
      f"{len(headings)} sections; SHA-256={sha256(payload).hexdigest()}")

priority = "## Priority 1 — Independent review of the deletion exponent improvement"
require(section(new, priority) == section(old, priority).replace(
    "Exactly one next atomic task:", "First scientific priority:"),
    "scientific review scope changed")
for heading in (
    "## Deferred priority 8 — Determine the true leading asymptotics",
    "## Deferred priority 9 — Certification architecture beyond `n=14`",
    "## Lower-priority extensions",
):
    current_heading = re.sub(r"Deferred priority [89]", "Deferred direction", heading)
    require(section(new, current_heading) == section(old, heading).replace(
        heading, current_heading, 1), heading)
require("## Resolved" not in new, "resolved history remains in current roadmap")
require(len(new.encode()) < len(old_bytes) / 5, "insufficient roadmap reduction")
print("PASS priorities: review and deferred bodies (labels only), asymptotic direction, "
      "certification prerequisite and extensions preserved")

# These are notation/scope guards, not a proof of semantic equivalence.
# EVIDENCE.md records the manual crosswalk to unchanged controlling sources.
for phrase in (
    "C_term+eta_60", "C_3(1/1000)", "[C_term+eta_60,C_3]",
    "`3 <= n <= 14`", "R*(n)=Theta(n^2)", "not asserted optimal",
    "Neither endpoint is established as sharp", "no normalized global limit",
    "Neither\n  larger width has finite recovery or geometric transfer",
):
    require(phrase in new, f"missing current bound/scope: {phrase}")
print("PASS bound/scope markers; mathematical authority is preserved sources")

for path, marker in (
    ("docs/post_arxiv_tasks.md", "The paper is public as arXiv v1:"),
    ("SUBMISSION_CHECKLIST.md", "## Pre-Submission Repo Checks"),
    ("SUBMISSION_REVIEW_REPORT.md", "Date: 2026-06-16"),
):
    before = baseline(path).decode().replace("\r\n", "\n")
    after = read(path)
    require(after[after.index(marker):] == before[before.index(marker):],
            f"historical body changed: {path}")
    require("historical" in after[:after.index(marker)].lower(), path)
print("PASS historical bodies: 3 unchanged; only authority/navigation wrappers edited")

# Hash cold evidence without using its contents for orientation.
entries = {}
for record in git("ls-tree", "-r", "-z", BASE).split(b"\0"):
    if record:
        meta, path = record.split(b"\t", 1)
        mode, kind, oid = meta.split()
        require(kind == b"blob", "unexpected non-blob baseline entry")
        entries[path.decode()] = oid.decode()
protected = sorted(set(entries) - MODIFIED)
hashes = git("hash-object", "--stdin-paths",
             data=("\n".join(protected) + "\n").encode()).decode().splitlines()
require(len(hashes) == len(protected), "incomplete protected-file hash inventory")
require(all(oid == entries[path] for path, oid in zip(protected, hashes)),
        "protected tracked file changed")
changed = set(git("diff", "--name-only", BASE).decode().splitlines())
untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
require(changed | untracked == MODIFIED | ADDED, "unexpected or missing task path")
print(f"PASS inventory: {len(MODIFIED)} modified + {len(ADDED)} added; "
      f"{len(protected)} protected baseline blobs unchanged")
for path in sorted(MODIFIED | ADDED):
    print(("M " if path in MODIFIED else "A ") + path)


def slugs(text):
    return {
        re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")
        for h in re.findall(r"^#{1,6} (.+)$", text, flags=re.M)
    }


links = 0
for path in sorted(MODIFIED | {ARCHIVE}):
    content = read(path).split("<!-- BEGIN VERBATIM ROADMAP SNAPSHOT -->")[0]
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
        if "://" in target or target.startswith("mailto:"):
            continue
        name, _, anchor = target.partition("#")
        dest = ((ROOT / path).parent / name).resolve() if name else ROOT / path
        require(dest.is_relative_to(ROOT) and dest.is_file(), f"broken link: {target}")
        if anchor:
            require(anchor in slugs(dest.read_text(encoding="utf-8")),
                    f"broken anchor: {target}")
        links += 1
require("sole ranked current research roadmap" in new, "roadmap authority")
require(read("CURRENT_STATUS.md").count("## Exactly one next atomic task") == 1,
        "current-status next task")
require("cold audit/provenance storage" in read("AGENTS.md"), "contract cold policy")
require("Never scan dossiers broadly" in read("PROJECT_KNOWLEDGE.md"), "index cold policy")
require("non-authoritative" in read(ARCHIVE).split(begin.decode())[0], "archive authority")
print(f"PASS navigation: {links} local links/anchors and authority policy markers")

# New files require explicit checks; ordinary unstaged diff omits additions.
for path in sorted(ADDED | {ROADMAP, "CURRENT_STATUS.md"}):
    text = read(path)
    require(all(line == line.rstrip() for line in text.splitlines()),
            f"trailing whitespace: {path}")
    require(text.endswith("\n") and not text.endswith("\n\n"),
            f"final newline: {path}")
git("diff", "--check")
git("diff", "--cached", "--check")
print("PASS whitespace: explicit additions/rewrites plus unstaged and staged Git checks")
old_lines, new_lines = len(old.splitlines()), len(new.splitlines())
print(f"ROADMAP {old_lines}->{new_lines} lines; {len(old_bytes)}->{len(new.encode())} bytes; "
      f"line reduction={100 * (1 - new_lines / old_lines):.2f}%")
hot = ("AGENTS.md", "PROJECT_KNOWLEDGE.md", "CURRENT_STATUS.md", ROADMAP)
before = sum(len(baseline(p).decode().splitlines()) for p in hot)
after = sum(len(read(p).splitlines()) for p in hot)
print(f"ORIENTATION {before}->{after} lines; reduction={100 * (1 - after / before):.2f}%")
