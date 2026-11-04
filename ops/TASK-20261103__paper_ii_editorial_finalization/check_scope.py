"""Bind the minimal editorial delta and protected bytes to d925f85; stdlib only."""
from pathlib import Path
from hashlib import sha256
import argparse
import re
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[2]
BASE = "d925f85c8aee2b26bca460bf33618eb65fb996b8"
PACKAGE = "paper_assets/paper_ii_journal/"
DOSSIER = "ops/TASK-20261103__paper_ii_editorial_finalization/"
ALLOWED = {
    "CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md",
    "tests/test_paper_ii_package.py",
    *(PACKAGE + name for name in (
        "main.tex", "main.pdf", "upper_supplement.tex", "upper_supplement.pdf",
        "README.md", "READINESS.md", "EDITORIAL_REQUIREMENTS.md", "PRIOR_ART.md",
        "REVIEW_COVERAGE.md", "EDITORIAL_CHECKLIST.md", "build.py",
        "BUILD_REPORT.json", "verify_package.py", "MANIFEST.json", "source_bundle.zip")),
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true")
    args = parser.parse_args()
    changed = set(git("diff", "--name-only", BASE).decode().splitlines())
    added = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    changed.update(added)
    unexpected = {p for p in changed if p not in ALLOWED and not p.startswith(DOSSIER)}
    require(not unexpected, "Unexpected paths: " + str(unexpected))
    substitutions = {
        "main": (
            (r"\date{24 October 2026}", r"\date{3 November 2026}"),
            ("Let $s=\\lfloor\\alpha m\\rfloor$, $l_j=2\\lfloor\\ell_jm/2\\rfloor$ and\n"
             "$a_j=\\sum_{h\\le j}l_h$. Reverse only the even ranks within each\n"
             "$(a_{j-1},a_j]$, fixing odd ranks, to obtain a permutation $J$.",
             "Let $s=\\lfloor\\alpha m\\rfloor$, $l_j=2\\lfloor\\ell_jm/2\\rfloor$,\n"
             "$a_0=0$ and $a_j=\\sum_{h\\le j}l_h$. Reverse only the even ranks within\n"
             "each $(a_{j-1},a_j]$ to obtain a permutation $J$ of $\\{1,\\ldots,m\\}$.\n"
             "Set $J(i)=i$ on odd ranks and on every index outside these blocks."),
        ),
        "upper_supplement": (
            (r"\date{24 October 2026}", r"\date{3 November 2026}"),
            ("and $H(u)=m+1+((u+s-1)\\bmod m)$. On the block $(a_{j-1},a_j]$ put\n"
             "$J(i)=2a_{j-1}+l_j+2-i$ when $i$ is even, and $J(i)=i$ otherwise.",
             "and $H(u)=m+1+((u+s-1)\\bmod m)$. For every $i\\in\\{1,\\ldots,m\\}$,\n"
             "put $J(i)=2a_{j-1}+l_j+2-i$ if $i$ is even and belongs to a block\n"
             "$(a_{j-1},a_j]$, and put $J(i)=i$ otherwise. In particular, $J$ fixes\n"
             "every index outside the inversion blocks."),
        ),
    }
    for name, replacements in substitutions.items():
        path = PACKAGE + name + ".tex"
        old = git("show", BASE + ":" + path).decode()
        actual = (ROOT / path).read_text(encoding="utf-8")
        abstract = lambda s: re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", s, re.S)[1]
        require(abstract(old) == abstract(actual), "Abstract changed: " + name)
        for before, after in replacements:
            require(old.count(before) == 1, "Missing or ambiguous baseline fragment: " + name)
            old = old.replace(before, after)
        require(old == actual, "Unexpected TeX change: " + name)
        print("PASS exact editorial source substitutions and unchanged abstract:", name)

    protected = 0
    with subprocess.Popen(["git", "archive", BASE], cwd=ROOT, stdout=subprocess.PIPE) as process:
        with tarfile.open(fileobj=process.stdout, mode="r|") as archive:
            for entry in archive:
                if entry.isfile() and entry.name not in ALLOWED:
                    baseline = archive.extractfile(entry).read()
                    current = ROOT / entry.name
                    require(current.is_file() and sha256(current.read_bytes()).digest() == sha256(baseline).digest(),
                            "Protected bytes changed: " + entry.name)
                    protected += 1
        require(process.wait() == 0, "git archive failed")
    print("PASS", protected, "protected baseline files byte-identical, including all S1 and earlier dossiers")

    for path in changed:
        p = ROOT / path
        # Generated stdout logs retain their original terminal padding.
        if p.suffix in {".md", ".py", ".json", ".txt"}:
            for number, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                require(line == line.rstrip(" \t"), f"Trailing whitespace: {path}:{number}")
    print("PASS explicit whitespace check for tracked and untracked task text")

    if args.staged:
        for path in git("diff", "--cached", "--name-only").decode().splitlines():
            require(git("show", ":" + path) == (ROOT / path).read_bytes(), "Staged bytes differ: " + path)
        print("PASS every staged blob equals inspected working-tree bytes")
    print("PASS declared task scope; unchanged science and public records")


if __name__ == "__main__":
    main()
