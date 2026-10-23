"""Audit this editorial delta against its immutable baseline; stdlib only."""
from pathlib import Path
from hashlib import sha256
import argparse
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = "fa32c99e9da0d639dca5735864c7c341d2e60059"
PACKAGE = "paper_assets/paper_ii_journal/"
ALLOWED = {
    ".github/workflows/ci.yml", ".github/workflows/paper-ii-latex.yml",
    "CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md",
    *(PACKAGE + name for name in (
        "main.tex", "main.pdf", "upper_supplement.tex", "upper_supplement.pdf",
        "README.md", "READINESS.md", "EDITORIAL_REQUIREMENTS.md", "PRIOR_ART.md",
        "build.py", "BUILD_REPORT.json", "verify_package.py", "MANIFEST.json",
        "source_bundle.zip", "check_reproducibility.py")),
}
DOSSIER = "ops/TASK-20261024__jocg_finalization/"


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
    changed.update(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    require(all(n in ALLOWED or n.startswith(DOSSIER) for n in changed),
            "Unexpected paths: " + str(changed - ALLOWED))
    substitutions = {
        "main": (
            (r"\date{23 October 2026\\\small Journal candidate for independent review}",
             r"\date{24 October 2026}"),
            ("This separate journal candidate supplies", "This separate journal manuscript supplies"),
            ("precise candidate revision", "precise manuscript revision"),
            ("Accompanies this candidate", "Accompanies this manuscript"),
            (r"\url{https://arxiv.org/abs/2607.28654v1}.",
             r"\url{https://arxiv.org/abs/2607.28654v1}." + "\n" +
             r"DOI: \href{https://doi.org/10.48550/arXiv.2607.28654}{10.48550/arXiv.2607.28654}."),
        ),
        "upper_supplement": (
            (r"\date{Journal Candidate, 23 October 2026}", r"\date{24 October 2026}"),
            (r"\usepackage[hidelinks]{hyperref}", r"\usepackage[hidelinks]{hyperref}" + "\n" +
             r"\hypersetup{pdftitle={Reflected Blocks, Implicit Parameters, and Full Geometric Recovery}," +
             "\n" + r" pdfauthor={Maurizio Falconi}}"),
        ),
    }
    for name, replacements in substitutions.items():
        path = PACKAGE + name + ".tex"
        old = git("show", BASE + ":" + path).decode()
        actual = (ROOT / path).read_text(encoding="utf-8")
        abstract = lambda s: re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", s, re.S)[1]
        require(abstract(old) == abstract(actual), "Abstract changed: " + name)
        print("PASS unchanged abstract", name, sha256(abstract(actual).encode()).hexdigest())
        for before, after in replacements:
            require(before in old, "Missing baseline editorial fragment: " + before)
            old = old.replace(before, after)
        require(old == actual, "Non-editorial TeX change: " + name)
    print("PASS complete main/S2 source equality apart from enumerated editorial substitutions")
    if args.staged:
        for name in git("diff", "--cached", "--name-only").decode().splitlines():
            staged = git("show", ":" + name)
            actual = (ROOT / name).read_bytes()
            if name.startswith(PACKAGE):
                require(staged == actual, "Manifested bytes changed on staging: " + name)
            else:
                require(staged.replace(b"\r\n", b"\n") == actual.replace(b"\r\n", b"\n"),
                        "Staged content differs: " + name)
        print("PASS staged content; every package blob matches manifested bytes")
    print("PASS declared scope; protected baseline files have no Git delta")


if __name__ == "__main__":
    main()
