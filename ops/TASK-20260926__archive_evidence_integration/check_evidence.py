"""Documentary integrity checks only: never import/run solver or verifier.

python -B ops/TASK-20260926__archive_evidence_integration/check_evidence.py
Add --staged to check index blobs; --durable PATH also checks local originals,
Windows preservation-snapshot bytes and the private, untracked ZIP.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REL = HERE.relative_to(ROOT).as_posix()
BASE = "7201f788b586ae059078dde6221d58b0ce8f79a1"
ACCEPTED = "80919666c3c54f8ce20cf66c456d413f6a2c075f"
ZIP = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
ZIP_HASH = "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db"
ALLOWED = {"README.md", "CITATION.cff", "CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md"}


def git(*args):
    return subprocess.check_output(["git", "-c", "safe.directory=" + ROOT.as_posix(),
                                    *args], cwd=ROOT)


def digest(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--durable", type=Path)
    args = parser.parse_args()

    def read(path):
        return git("show", ":" + path) if args.staged else (ROOT / path).read_bytes()

    def evidence(name):
        return read(REL + "/evidence/" + name)

    def obj(name):
        return json.loads(evidence(name))

    manifest = json.loads(read(REL + "/EVIDENCE_MANIFEST.json"))
    assert manifest["release_commit"] == ACCEPTED
    entries = manifest["files"]
    assert len(entries) == len({x["public_path"] for x in entries}) == 28
    assert {p.name for p in (HERE / "evidence").iterdir()} == {
        x["source_relative_path"] for x in entries}
    for entry in entries:
        path = entry["public_path"]
        assert not PurePosixPath(path).is_absolute() and ".." not in PurePosixPath(path).parts
        data = read(REL + "/" + path)
        assert digest(data) == entry["public"], path
        assert entry["source_before_copy"] == entry["durable_after_copy"], path
        same = entry["public"] == entry["source_before_copy"]
        assert same == (entry["classification"] == "BYTE_IDENTICAL"), path
        if path.endswith(".json"):
            json.loads(data)
        text = data.decode("utf-8")
        # Known private roots/URLs, credential shapes and authenticated URLs.
        for pattern in [r"(?i)[A-Z]:[/\\]+Users[/\\]", r"docs\.google\.com|drive\.google\.com",
                        r"(?i)bearer\s+[a-z0-9._-]+|gh[pousr]_[a-z0-9]+|github_pat_[a-z0-9_]+",
                        r"sk-[a-zA-Z0-9]{20,}|-----BEGIN .*PRIVATE KEY",
                        r"https?://[^\s/]+:[^\s/]+@|[?&](?:access_token|token|signature|sig)="]:
            assert not re.search(pattern, text), (path, "privacy scan")
    e = obj("EVIDENCE.json")
    c = obj("archive_comparison.json")
    v = obj("verifier_execution.json")
    rows = list(csv.DictReader(io.StringIO(evidence("ARCHIVE_INVENTORY.csv").decode())))
    assert e["result"] == "PASS" and e["archive"]["comparison"] == c
    assert c["git_commit"] == e["release"]["resolved_commit"] == e["accepted_review_baseline"] == ACCEPTED
    assert c["tracked_files"] == c["archive_files"] == len(rows) == len({x["path"] for x in rows}) == 701
    assert not c["mismatches"] and c["all_directory_members_expected"]
    for row in rows:
        assert row["result"] == "MATCH" and row["git_sha256"] == row["archive_sha256"]
        assert row["git_bytes"] == row["archive_bytes"] and int(row["git_bytes"]) >= 0
        assert re.fullmatch("[a-f0-9]{64}", row["git_sha256"])
        assert re.fullmatch("[a-f0-9]{40}", row["git_blob"])
        assert row["git_mode"] == "100644"
        assert not PurePosixPath(row["path"]).is_absolute() and ".." not in PurePosixPath(row["path"]).parts
    by = {x["path"]: x for x in rows}
    originals = obj("originals_check.json")
    assert len(originals) == 13
    for row in originals:
        assert row["result"] == "MATCH"
        assert row["sha256"] == by[row["path"]]["archive_sha256"]
        assert row["bytes"] == int(by[row["path"]]["archive_bytes"])
    assert e["verifier_execution"] == v and v["execution_count"] == 1 and v["exit_code"] == 0
    assert evidence("verifier.stdout.txt") == v["stdout"].encode("utf-8")
    assert evidence("verifier.stderr.txt") == v["stderr"].encode("utf-8") == b""
    result = json.loads(v["stdout"])
    assert result == e["verifier_result"]
    assert result["status"] == "PASS_GLOBAL_BRACKETS" and result["pinned_input_verification"] == "PASS"
    assert by["verify_global_brackets.py"]["git_sha256"] == result["verifier_sha256"]
    logs = [json.loads(line) for line in evidence("commands.jsonl").splitlines()]
    assert len(logs) == 24
    assert [x for x in logs if x.get("command") == v["command"]] == [v]
    assert obj("github_tag.json")["object"]["sha"] == ACCEPTED
    z = obj("zenodo_record.json")
    assert z["doi"] == e["zenodo"]["version_doi"] == manifest["version_doi"] == "10.5281/zenodo.22849826"
    assert z["metadata"]["version"] == e["release"]["tag"] == "v1.1.0-dcg-presubmission"
    assert z["status"] == "published" and z["state"] == "done" and z["submitted"] is True
    assert obj("metadata_comparison.json") == e["zenodo"]["metadata_comparison"]
    for name in ["github_release.json", "github_tag.json", "zenodo_record.json"]:
        meta = obj(name + ".http.json")
        assert digest(evidence(name)) == {k: meta[k] for k in ("bytes", "sha256")}
        assert meta["http_status"] == 200
    doi = obj("doi_resolution.html.http.json")
    assert doi["http_status"] == 200 and doi["resolved_url"] == "https://zenodo.org/records/22849826"
    assert obj("zenodo_archive.zip.http.json") == e["archive"]["acquisition"]
    before, after = obj("repository_before.json"), obj("repository_after.json")
    assert before["files"] == after["files"] and before["git_metadata"] == after["git_metadata"]
    assert len(before["files"]) == 702
    assert before["files"][ZIP]["sha256"] == ZIP_HASH
    build = obj("build_manifest_hash_check.json")
    assert len(build) == 13 and all(x["result"] == "PASS" and x["expected"] == x["actual"] for x in build)
    registry = obj("registry_state.json")["structuredContent"]["values"]
    assert len(registry) == 2 and registry[1][:3] == ["ringmin", "falker47/ringmin", ACCEPTED]
    cff = read("CITATION.cff")
    old_cff = git("show", BASE + ":CITATION.cff")
    assert cff.split(b"preferred-citation:", 1)[1].replace(b"\r\n", b"\n") == old_cff.split(b"preferred-citation:", 1)[1].replace(b"\r\n", b"\n")
    assert b'doi: "10.5281/zenodo.22849826"' in cff
    changed = git("diff", "--name-only", BASE).decode().splitlines()
    assert all(p in ALLOWED or p.startswith(REL + "/") for p in changed), changed
    assert ZIP not in git("ls-files").decode().splitlines()
    # Local Markdown links in authored documents; archived report links retain historical context.
    authored = ["README.md", "CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md"]
    authored += [REL + "/" + name for name in ["TASK_STATUS.md", "TASK_LOG.md", "EVIDENCE.md"]]
    for path in authored:
        for target in re.findall(r"\]\(([^)]+)\)", read(path).decode()):
            if "://" not in target and not target.startswith("#"):
                assert ((ROOT / path).parent / target.split("#")[0]).exists(), (path, target)
    if args.durable:
        for path, recorded in after["files"].items():
            if path not in ALLOWED:
                assert digest((ROOT / path).read_bytes()) == recorded, path
        assert hashlib.sha256((ROOT / ZIP).read_bytes()).hexdigest() == ZIP_HASH
        copy_data = (args.durable / "COPY_MANIFEST.json").read_bytes()
        assert digest(copy_data) == manifest["private_copy_manifest"]
        copy = json.loads(copy_data)
        assert len(copy["files"]) == manifest["local_copy_file_count"] == 68
        for row in copy["files"]:
            assert digest(Path(row["source"]).read_bytes()) == row["before"]
            assert digest(Path(row["copy"]).read_bytes()) == row["after"] == row["before"]
    print("PASS: 28 evidence hashes; JSON/CSV and 24 log records; 701 inventory rows; 13 recorded originals; one historical verifier record")
    print("PASS: historical identity/log bindings; DOI/CFF preferred citation; local links; scoped protected paths; ZIP excluded from Git; privacy patterns")
    if args.staged:
        print("PASS: all 28 staged evidence blobs match declared SHA-256 and sizes")
    if args.durable:
        print("PASS: 697 protected tracked files and exempt ZIP also match historical preservation-snapshot bytes")
        print("PASS: 68 durable original copies and their source files match before/after hashes and sizes")
    print("NO scientific verification executed; documentary self-check only")


if __name__ == "__main__":
    main()
