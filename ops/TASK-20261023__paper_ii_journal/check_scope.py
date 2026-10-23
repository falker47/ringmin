"""Check the protected baseline and optionally the original checkout / staged bytes."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ALLOWED = {"CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md", ".github/workflows/ci.yml"}
PREFIXES = ("paper_assets/paper_ii_journal/", "ops/TASK-20261023__paper_ii_journal/")
ORIGINAL_HEAD = "6167e36cf6f80a6a7a7a6b41518a6b3f7155295d"
ZIP_PATH = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
ZIP_SHA = "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db"

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def git(*args, root=ROOT):
    return subprocess.check_output(["git", *args], cwd=root)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original-checkout", type=Path)
    parser.add_argument("--staged", action="store_true")
    args = parser.parse_args()
    saved = json.loads((HERE / "PROTECTED_INPUTS.json").read_text(encoding="utf-8"))
    tree = {}
    for row in git("ls-tree", "-rz", "--full-tree", saved["baseline"]).split(b"\0"):
        if row:
            metadata, name = row.split(b"\t", 1)
            tree[name.decode()] = metadata.split()[2].decode()
    require(set(saved["files"]) == set(tree) - ALLOWED, "protected inventory differs from baseline")
    for name, record in saved["files"].items():
        require(tree[name] == record["git_object"], "baseline object differs: " + name)
        require(sha256((ROOT/name).read_bytes()).hexdigest() == record["working_bytes_sha256"], "protected working bytes differ: " + name)
    changed = set(git("diff", "--name-only", saved["baseline"]).decode().splitlines())
    untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    require(all(p in ALLOWED or p.startswith(PREFIXES) for p in changed | untracked), "change outside task scope")
    print(f"PASS: {len(saved['files'])} protected baseline paths; only declared task paths differ")
    if args.staged:
        names = git("diff", "--cached", "--name-only").decode().splitlines()
        require(bool(names), "no staged candidate")
        for name in names:
            actual = (ROOT/name).read_bytes()
            staged = git("show", ":"+name)
            if name.startswith("paper_assets/paper_ii_journal/"):
                require(staged == actual, "staged package bytes differ: " + name)
            else:
                require(staged.replace(b"\r\n", b"\n") == actual.replace(b"\r\n", b"\n"), "staged task content differs: " + name)
        print(f"PASS: {len(names)} staged task paths; every package blob equals its manifested working bytes")
    if args.original_checkout:
        original = args.original_checkout.resolve()
        require(git("rev-parse", "HEAD", root=original).decode().strip() == ORIGINAL_HEAD, "original HEAD changed")
        require(git("status", "--short", root=original).decode().splitlines() == ["?? "+ZIP_PATH], "original checkout state changed")
        require(sha256((original/ZIP_PATH).read_bytes()).hexdigest() == ZIP_SHA, "original ZIP changed")
        print("PASS: original checkout HEAD/status and sole untracked ZIP preserved")

if __name__ == "__main__":
    main()
