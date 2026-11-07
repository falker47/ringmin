"""Editorial preservation checks for the exact author-approved source hashes.

No mathematical certification claim. Reuses the previous read-only LaTeX
invariant extractor, with only the two explicitly authorized exceptions.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
BASE = "4303fe4d937c5f2c7915070a0aaffa67f9b448ca"
TASK = DOSSIER.relative_to(ROOT).as_posix()
PINS = {
    "paper_assets/journal_dcg/ringmin_dcg.tex": (
        "5595e34e5c95274fa68bc0368c8c5d7b4e41249d",
        "9bd9a8d605c207fb8e81d1abd024d8d536ac839a9eadbf18d63dc3c23e559d90"),
    "paper_assets/paper_ii_journal/main.tex": (
        "f0adc31b5ac6f1bcdd8782ba69e4c8a9253c3b8f",
        "11aef17bba8e0b0eb264553fb5e06d83fea361b22fe5eaf7a91d464151f5366d"),
}
ALLOWED = set(PINS) | {
    "CURRENT_STATUS.md", "paper_assets/journal_dcg/ringmin_dcg.pdf",
    "paper_assets/journal_dcg/README.md",
    "paper_assets/paper_ii_journal/README.md",
    "paper_assets/paper_ii_journal/READINESS.md",
    "paper_assets/journal_dcg/BUILD_MANIFEST.json",
    "paper_assets/paper_ii_journal/main.pdf",
    "paper_assets/paper_ii_journal/BUILD_REPORT.json",
    "paper_assets/paper_ii_journal/MANIFEST.json",
    "paper_assets/paper_ii_journal/source_bundle.zip",
}
OLD_AVAILABILITY = r"""Section~\ref{sec:repro} distinguishes the computational source pin, the
archived release commit and the later accepted repository baseline; the
DOI identifies only the archived snapshot. The proof of the selected"""
NEW_AVAILABILITY = r"""Section~\ref{sec:repro} distinguishes the computational source pin from
the archived release commit; the DOI identifies only the archived snapshot.
The proof of the selected"""


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def norm(data):
    return data.decode("utf-8").replace("\r\n", "\n")


def main():
    previous = runpy.run_path(str(ROOT / "ops/TASK-20261107__two_paper_editorial_review/check_scope.py"))
    extract = previous["invariants"]
    for paper, (path, (blob, expected_hash)) in enumerate(PINS.items(), 1):
        require(git("rev-parse", BASE + ":" + path).decode().strip() == blob, "Source blob pin mismatch")
        before = norm(git("show", blob))
        data = (ROOT / path).read_bytes()
        after = norm(data)
        require(sha256(after.encode()).hexdigest() == expected_hash, "Approved source hash mismatch: " + path)
        expected, actual = extract(before, paper), extract(after, paper)
        if paper == 1:
            require(expected["disclosures"].count(OLD_AVAILABILITY) == 1, "Unique authorized availability passage")
            expected["disclosures"] = expected["disclosures"].replace(OLD_AVAILABILITY, NEW_AVAILABILITY)
            start = before.index("This archival identity is distinct")
            end_marker = r"to Discrete \& Computational Geometry."
            end = before.index(end_marker, start) + len(end_marker)
            historical = before[start:end]
            provenance = (DOSSIER / "PAPER_I_PROVENANCE.md").read_text(encoding="utf-8")
            require("```tex\n" + historical + "\n```" in provenance, "Historical paragraph not preserved verbatim")
        else:
            expected["references"] = Counter(expected["references"])
            expected["references"]["thm:lp"] += 1
        for key, value in expected.items():
            require(actual[key] == value, f"Paper {paper}: changed {key}")
        for label, mutant in (
            ("formula", after.replace(r"\pi", r"\tau", 1)),
            ("proof", after.replace(r"\begin{proof}", r"\begin{proof}Altered.", 1)),
            ("disclosure", after.replace("The author retains responsibility", "Nobody retains responsibility", 1)
             if paper == 1 else after.replace("Responsibility", "No responsibility", 1)),
        ):
            require(mutant != after and extract(mutant, paper) != actual, "Undetected negative control: " + label)
        print(f"PASS Paper {paper}: approved SHA256; {len(actual['protected_environments'])} protected environments; "
              f"{len(actual['math'][0])} delimited formulas; {len(actual['math'][1])} math environments; "
              "citations, dates/preamble, AI disclosure preserved; negative controls detected")
    snapshot = json.loads((DOSSIER / "INITIAL_TRACKED_SHA256.json").read_text())
    require(snapshot["base_head"] == BASE, "Snapshot base mismatch")
    inventory = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
    require(set(snapshot["sha256"]) == inventory, "Incomplete baseline inventory")
    protected = {p: h for p, h in snapshot["sha256"].items() if p not in ALLOWED}
    for path, expected in protected.items():
        require(sha256((ROOT / path).read_bytes()).hexdigest() == expected, "Protected bytes changed: " + path)
    changed = set(git("diff", "--name-only", BASE, "--").decode().splitlines())
    added = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    require(all(p in ALLOWED or p.startswith(TASK + "/") for p in changed | added), "Out-of-scope changes")
    saved = (DOSSIER / "BUILD_REPORT.before.json").read_bytes()
    require(norm(saved) == norm(git("show", BASE + ":paper_assets/paper_ii_journal/BUILD_REPORT.json")), "Saved report differs from base")
    before_report = json.loads(saved)
    report = json.loads((ROOT / "paper_assets/paper_ii_journal/BUILD_REPORT.json").read_text())
    for name in ("lower", "upper_supplement"):
        require(report["documents"][name] == before_report["documents"][name], "Supplement record changed")
        context = report["build_context_by_document"][name]
        for field in ("compiler", "command", "SOURCE_DATE_EPOCH", "FORCE_SOURCE_DATE"):
            require(context[field] == before_report[field], "Wrong inherited context: " + field)
    print(f"PASS protected inventory: {len(protected)} tracked files byte-identical; exact baseline inventory {len(inventory)} files")
    print("PASS scope, historical paragraph, saved original report, full supplement records and inherited context")
    print("LIMIT: engineering/editorial preservation; no mathematical recertification, external acceptance or hosted CI")


if __name__ == "__main__":
    main()
