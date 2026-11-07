"""Task-local editorial invariants, not a mathematical proof or certification audit.

Run from any directory with Python >=3.11:
    python ops/TASK-20261107__two_paper_editorial_review/check_scope.py

The exact base Git blobs control manuscript checks. startup_hashes.json binds
the checked-out bytes of other tracked files, including binary supplements.
The parser targets the environments and math delimiters actually used here;
a human semantic diff review remains necessary for prose outside them.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
BASE = "7d257221d9034ca5f895f062e45e782d8e77b6c2"
TASK = DOSSIER.relative_to(ROOT).as_posix()
MANUSCRIPTS = (
    "paper_assets/journal_dcg/ringmin_dcg.tex",
    "paper_assets/paper_ii_journal/main.tex",
)
ALLOWED_TRACKED = {
    "CURRENT_STATUS.md",
    "paper_assets/journal_dcg/ringmin_dcg.tex",
    "paper_assets/journal_dcg/ringmin_dcg.pdf",
    "paper_assets/journal_dcg/BUILD_MANIFEST.json",
    "paper_assets/journal_dcg/README.md",
    "paper_assets/paper_ii_journal/main.tex",
    "paper_assets/paper_ii_journal/main.pdf",
    "paper_assets/paper_ii_journal/BUILD_REPORT.json",
    "paper_assets/paper_ii_journal/MANIFEST.json",
    "paper_assets/paper_ii_journal/source_bundle.zip",
    "paper_assets/paper_ii_journal/README.md",
    "paper_assets/paper_ii_journal/READINESS.md",
    "paper_assets/paper_ii_journal/EDITORIAL_CHECKLIST.md",
}
PROTECTED_ENVS = {
    "theorem", "lemma", "proposition", "corollary", "definition", "remark",
    "proof", "table", "table*", "tabular", "tabularx", "longtable",
    "thebibliography", "verbatim",
}
MATH_ENVS = {
    "equation", "equation*", "align", "align*", "gather", "gather*",
    "multline", "multline*", "displaymath", "math",
}
TOKEN = re.compile(r"\\(begin|end)\{([^}]+)\}")
MATH_INLINE = re.compile(r"(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$|(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\\\(.*?(?<!\\)\\\)", re.S)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def normalize(data):
    return data.decode("utf-8").replace("\r\n", "\n")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def base_bytes(path):
    return git("show", f"{BASE}:{path}")


def environments(text, names):
    stack = []
    result = []
    for match in TOKEN.finditer(text):
        action, name = match.groups()
        if action == "begin":
            stack.append((name, match.start()))
        else:
            require(bool(stack) and stack[-1][0] == name,
                    "Unbalanced environment: " + name)
            _, start = stack.pop()
            if name in names:
                result.append((start, name, text[start:match.end()]))
    require(not stack, "Unclosed LaTeX environment")
    return [(name, block) for _, name, block in sorted(result)]


def math_blocks(text):
    # Remove comments only for detecting formula delimiters, not block identity.
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    blocks = [("inline_or_delimited", m.group()) for m in MATH_INLINE.finditer(text)]
    return blocks, environments(text, MATH_ENVS)


def between(text, start, end):
    require(text.count(start) == 1, "Expected unique marker: " + start)
    return text.split(start, 1)[1].split(end, 1)[0]


def invariants(text, paper):
    preamble = text.split(r"\begin{document}", 1)[0]
    protected = environments(text, PROTECTED_ENVS)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    # Prose can be regrouped; preserve all reference occurrences as a multiset.
    references = Counter(re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text))
    citations = Counter(re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", text))
    inputs = re.findall(r"\\(?:input|include)\{([^}]+)\}", text)
    if paper == 1:
        declarations = between(text, r"\section*{Statements and Declarations}", r"\appendix")
        extra = text.split(r"\appendix", 1)[1]
    else:
        declarations = between(text, r"\section*{Acknowledgment}", r"\begin{thebibliography}")
        extra = between(text, r"\section{An Explicit Global Lower Endpoint}",
                        r"\section{Reproducibility and Open Questions}")
    return {
        "preamble": preamble,
        "protected_environments": protected,
        "math": math_blocks(text),
        "labels": labels,
        "references": references,
        "citations": citations,
        "inputs": inputs,
        "disclosures": declarations,
        "protected_appendix_or_lower_section": extra,
    }


def check_manuscript(path, paper):
    before = normalize(base_bytes(path))
    after = normalize((ROOT / path).read_bytes())
    expected, actual = invariants(before, paper), invariants(after, paper)
    for key, value in expected.items():
        require(actual[key] == value, f"{path}: changed {key}")
    # Negative controls are in-memory mutations of the baseline, never file edits.
    for name, mutant in (
        ("formula", before.replace(r"\pi", r"\tau", 1)),
        ("proof", before.replace(r"\begin{proof}", r"\begin{proof}Altered.", 1)),
        ("disclosure", before.replace("Responsibility", "No responsibility", 1)
         if paper == 2 else before.replace("The author retains responsibility", "Nobody retains responsibility", 1)),
    ):
        require(mutant != before, "Negative control did not mutate: " + name)
        require(invariants(mutant, paper) != expected,
                "Negative control not detected: " + name)
    protected_count = len(actual["protected_environments"])
    inline_count = len(actual["math"][0])
    display_count = len(actual["math"][1])
    print(f"PASS Paper {paper}: {protected_count} protected environments; "
          f"{inline_count} delimited formulas; {display_count} math environments; "
          "preamble, labels, references, citations, disclosures and protected section unchanged")
    print(f"PASS Paper {paper}: formula/proof/disclosure negative controls detected")


def main():
    snapshot = json.loads((DOSSIER / "startup_hashes.json").read_text(encoding="utf-8"))
    require(snapshot["base"] == BASE, "Startup snapshot base mismatch")
    baseline_paths = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
    require(set(snapshot["tracked_files"]) == baseline_paths,
            "Startup snapshot does not cover exact baseline tracked inventory")
    count = 0
    for path, expected in snapshot["tracked_files"].items():
        if path in ALLOWED_TRACKED:
            continue
        file = ROOT / path
        require(file.is_file(), "Protected tracked file missing: " + path)
        require(sha256(file.read_bytes()).hexdigest() == expected,
                "Protected tracked bytes changed: " + path)
        count += 1
    changed = set(git("diff", "--name-only", BASE, "--").decode().splitlines())
    new_files = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    unauthorized = {p for p in changed | new_files
                    if p not in ALLOWED_TRACKED and not p.startswith(TASK + "/")}
    require(not unauthorized, "Unexpected changed/additional paths: " + repr(sorted(unauthorized)))
    for paper, path in enumerate(MANUSCRIPTS, 1):
        check_manuscript(path, paper)
    print(f"PASS protected inventory: {count} tracked files byte-identical to startup")
    print("PASS scope: every changed/additional path is an explicit editorial output or this dossier")
    print("LIMIT: text invariants and scoped byte preservation; not semantic equivalence, proof validity, or hosted CI")


if __name__ == "__main__":
    main()
