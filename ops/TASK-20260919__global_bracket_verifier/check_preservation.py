"""Read-only preservation, scope and whitespace audit for this integration."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
TASK = Path(__file__).resolve().parent
ARCHIVE = ROOT / "reproducibility/global_brackets/originals"
BASE = "98d6a6e340e4008ce35e789c54333ae43466b49d"
EXEMPT = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
OWNED = {
    ".gitattributes",
    ".github/workflows/ci.yml",
    "CURRENT_STATUS.md",
    "knowledge/CERTIFICATION.md",
    "research/GLOBAL_BRACKET_CERTIFICATE.md",
    "verify_global_brackets.py",
    "tests/test_global_brackets.py",
}


def git(*args):
    return subprocess.check_output(
        ["git", "-c", "safe.directory=" + ROOT.as_posix(), *args],
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
    )


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--staged", action="store_true")
    args = ap.parse_args()
    before = json.loads((TASK / "SOURCE_HASHES.json").read_bytes())
    after = {
        p.relative_to(args.source).as_posix(): sha(p.read_bytes())
        for p in args.source.rglob("*")
        if p.is_file()
    }
    assert before == after, "external source changed"
    manifest = json.loads((ARCHIVE.parent / "manifest.json").read_bytes())
    for rec in manifest["files"]:
        p = ARCHIVE / rec["path"]
        data = p.read_bytes()
        assert data == (args.source / rec["path"]).read_bytes(), rec["path"]
        assert len(data) == rec["bytes"] and sha(data) == rec["sha256"]
        if args.staged:
            assert git("cat-file", "blob", ":" + p.relative_to(ROOT).as_posix()) == data
    status = (
        git("status", "--porcelain=v1", "--untracked-files=all").decode().splitlines()
    )
    paths = []
    for line in status:
        state, path = line[:2], line[3:]
        if path == EXEMPT:
            assert state == "??", "exempt ZIP must remain untracked"
            continue
        assert path in OWNED or path.startswith(
            (
                "reproducibility/global_brackets/",
                "ops/TASK-20260919__global_bracket_verifier/",
            )
        ), "unrelated dirty path: " + path
        paths.append(path)
    protected = git(
        "diff",
        "--name-only",
        BASE,
        "--",
        "src/ringmin",
        "verify.py",
        "results",
        "paper_assets",
        "README.md",
        "REPORT.md",
        "CITATION.cff",
        "PROJECT_KNOWLEDGE.md",
        "research/NEXT_RESEARCH_STEPS.md",
        "AGENTS.md",
        "RINGMIN_REVIEW_PROTOCOL.md",
    )
    assert not protected, "protected tracked path changed"
    inherited = []
    for path in paths:
        data = (ROOT / path).read_bytes()
        text = data.decode("utf-8")
        if path.endswith(".json"):
            json.loads(text)
        lines = text.splitlines()
        assert all(line == line.rstrip(" \t") for line in lines), (
            "trailing space: " + path
        )
        if lines and not lines[-1]:
            assert (
                path == "reproducibility/global_brackets/originals/STRICT_REVIEW_IT.md"
            ), "blank EOF: " + path
            inherited.append(path)
    print(
        json.dumps(
            {
                "status": "PASS_PRESERVATION_AND_SCOPE",
                "external_files_unchanged": len(after),
                "selected_originals_identical": len(manifest["files"]),
                "staged_archive_bytes_checked": args.staged,
                "complete_added_or_modified_files_read": len(paths),
                "protected_tracked_paths_unchanged": True,
                "exempt_zip_untracked": True,
                "inherited_blank_eof_preserved": inherited,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
