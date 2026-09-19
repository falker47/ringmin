"""Read-only audit of the authorized merge's staged union and preserved inputs."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
TASK = Path(__file__).resolve().parent
TASK_PATH = TASK.relative_to(ROOT).as_posix() + "/"
LOCAL = "c0075cf9dbe902571748299b21e368a0433c784e"
REMOTE = "5c98063a9a38d6f7f76d7ec7a073f3cdf8d5717a"
BASE = "98d6a6e340e4008ce35e789c54333ae43466b49d"
ZIP = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
ZIP_SHA = "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db"


def git(*args):
    return subprocess.check_output(
        ["git", "-c", "safe.directory=" + ROOT.as_posix(), *args],
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
    )


def sha(data):
    return hashlib.sha256(data).hexdigest()


def tree(ref):
    entries = {}
    for record in git("ls-tree", "-rz", ref).split(b"\0"):
        if record:
            meta, path = record.split(b"\t", 1)
            mode, kind, oid = meta.decode().split()
            assert kind == "blob", (kind, path)
            entries[path.decode()] = (mode, oid)
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    assert git("merge-base", LOCAL, REMOTE).decode().strip() == BASE
    base, local, remote = (tree(ref) for ref in (BASE, LOCAL, REMOTE))
    expected, conflicts = {}, []
    for path in sorted(base.keys() | local.keys() | remote.keys()):
        b, left, right = base.get(path), local.get(path), remote.get(path)
        if left == right or right == b:
            value = left
        elif left == b:
            value = right
        else:
            conflicts.append(path)
            continue
        if value is not None:
            expected[path] = value
    assert conflicts == ["CURRENT_STATUS.md"], conflicts
    staged = {}
    for record in git("ls-files", "--stage", "-z").split(b"\0"):
        if record:
            meta, path = record.split(b"\t", 1)
            mode, oid, stage = meta.decode().split()
            assert stage == "0", (path, stage)
            staged[path.decode()] = (mode, oid)
    actual_union = {
        path: value
        for path, value in staged.items()
        if path != "CURRENT_STATUS.md" and not path.startswith(TASK_PATH)
    }
    assert actual_union == expected, "staged tree differs from both-parent union"
    assert "CURRENT_STATUS.md" in staged
    git("diff", "--exit-code")  # No worktree change may escape index inspection.
    untracked = git("ls-files", "--others", "--exclude-standard", "-z")
    assert untracked.decode().split("\0") == [ZIP, ""], untracked
    assert ZIP not in staged and sha((ROOT / ZIP).read_bytes()) == ZIP_SHA

    remote_status = git("show", REMOTE + ":CURRENT_STATUS.md").decode()
    retained = remote_status.split("The standalone asymptotic sequel is public as", 1)[
        1
    ]
    retained = retained.split("## Exactly one next atomic task", 1)[0]
    current = (ROOT / "CURRENT_STATUS.md").read_text(encoding="utf-8")
    assert retained in current, "remote publication/review context was lost"
    assert current.count("## Exactly one next atomic task") == 1
    assert all(marker not in current for marker in ("<<<<<<<", "=======", ">>>>>>>"))

    old_task = ROOT / "ops/TASK-20260919__global_bracket_verifier"
    before = json.loads((old_task / "SOURCE_HASHES.json").read_bytes())
    after = {
        p.relative_to(args.source).as_posix(): sha(p.read_bytes())
        for p in args.source.rglob("*")
        if p.is_file()
    }
    assert before == after, "external source changed"
    archive = ROOT / "reproducibility/global_brackets/originals"
    manifest = json.loads((archive.parent / "manifest.json").read_bytes())
    for rec in manifest["files"]:
        path = archive / rec["path"]
        data = path.read_bytes()
        assert data == (args.source / rec["path"]).read_bytes(), rec["path"]
        assert len(data) == rec["bytes"] and sha(data) == rec["sha256"]
        assert git("cat-file", "blob", ":" + path.relative_to(ROOT).as_posix()) == data

    additions = sorted(p for p in staged if p.startswith(TASK_PATH))
    for path in ["CURRENT_STATUS.md", *additions]:
        content = (ROOT / path).read_text(encoding="utf-8")
        if path.endswith(".json"):
            json.loads(content)
        lines = content.splitlines()
        assert all(line == line.rstrip(" \t") for line in lines), path
        assert not lines or lines[-1], "blank EOF: " + path
    git("diff", "--cached", "--check")
    print(
        json.dumps(
            {
                "status": "PASS_MERGE_UNION_AND_PRESERVATION",
                "local_parent": LOCAL,
                "remote_parent": REMOTE,
                "unchanged_union_paths": len(expected),
                "resolved_conflicts": conflicts,
                "new_dossier_paths_read_in_full": len(additions),
                "remote_status_context_retained_verbatim": True,
                "external_files_unchanged": len(after),
                "original_files_source_worktree_index_identical": len(
                    manifest["files"]
                ),
                "zip_untracked_and_sha256_unchanged": ZIP_SHA,
                "no_unstaged_changes": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
