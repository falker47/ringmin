"""Create the disclosed public derivatives; never run audit/science programs.

Usage: python -B prepare_public_evidence.py DURABLE_ROOT OUTPUT_DIRECTORY
OUTPUT_DIRECTORY must not exist. Originals and COPY_MANIFEST.json are read-only.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

NAMES = """AUDIT.md EVIDENCE.json ARCHIVE_INVENTORY.csv CHECKPOINT.md
COMMAND_LOG.md commands.jsonl archive_comparison.json originals_check.json
metadata_comparison.json build_manifest_hash_check.json repository_preservation.json
repository_before.json repository_after.json extracted_after_verifier.json
verifier_execution.json verifier.stdout.txt verifier.stderr.txt python_environment.json
github_release.json github_release.json.http.json github_tag.json github_tag.json.http.json
zenodo_record.json zenodo_record.json.http.json zenodo_archive.zip.http.json
doi_resolution.html.http.json CITATION.tag.cff registry_state.json""".split()


def digest(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def prepare(durable, output):
    originals = durable / "originals"
    copy_bytes = (durable / "COPY_MANIFEST.json").read_bytes()
    copy = json.loads(copy_bytes)
    mapping = {r["relative_path"]: r for r in copy["files"]}
    source_evidence = json.loads((originals / "EVIDENCE.json").read_bytes())
    aliases = {
        source_evidence["evidence_directory"]: "AUDIT_ORIGINALS",
        source_evidence["local_root"]: "REPOSITORY_ROOT",
    }
    registry = source_evidence["baseline_source"]["url"]

    def scrub(value):
        if isinstance(value, list):
            return [scrub(x) for x in value]
        if isinstance(value, dict):
            return {scrub(k): scrub(v) for k, v in value.items()}
        if not isinstance(value, str):
            return value
        value = value.replace("[Registry](" + registry + ")",
                              "Registry (private source; see registry_state.json)")
        value = value.replace(registry, "REVIEW_STATE_REGISTRY")
        for root, alias in aliases.items():
            value = value.replace(root, alias).replace(root.replace("\\", "/"), alias)
        value = re.sub(r"[A-Za-z]:[/\\]Users[/\\][^/\\\s\"<>]+", "USER_HOME", value)
        return value

    output.mkdir(parents=True, exist_ok=False)
    evidence = output / "evidence"
    evidence.mkdir()
    entries = []
    for name in NAMES:
        raw = (originals / name).read_bytes()
        row = mapping[name]
        assert digest(raw) == row["before"] == row["after"], name
        transformations = []
        published = raw
        if name == "registry_state.json":
            obj = json.loads(raw)
            values = obj["structuredContent"]["values"]
            obj["structuredContent"]["values"] = [values[0]] + [
                r for r in values[1:] if r and r[0] == "ringmin"]
            assert len(obj["structuredContent"]["values"]) == 2
            transformations.append("Omit unrelated project rows; retain original queried-range label.")
            published = (json.dumps(scrub(obj), ensure_ascii=False, indent=2) + "\n").encode()
        elif name.endswith(".json"):
            obj = json.loads(raw)
            clean = scrub(obj)
            if clean != obj:
                published = (json.dumps(clean, ensure_ascii=False, indent=2) + "\n").encode()
                transformations.append("Replace local path roots/private Registry URL; JSON reserialized as UTF-8/LF.")
        elif name.endswith(".jsonl"):
            objs = [json.loads(line) for line in raw.decode().splitlines()]
            clean = scrub(objs)
            if clean != objs:
                published = ("\n".join(json.dumps(x, ensure_ascii=False) for x in clean) + "\n").encode()
                transformations.append("Replace local path roots/private Registry URL; JSONL reserialized as UTF-8/LF.")
        elif name.endswith(".md"):
            clean = scrub(raw.decode())
            banner = "> DERIVED public copy of the historical audit; see ../EVIDENCE_MANIFEST.json and ../EVIDENCE.md.\n\n"
            published = (banner + clean.replace("\r\n", "\n")).encode()
            transformations.append("Add DERIVED banner; replace local path roots/private Registry URL; use UTF-8/LF.")
        (evidence / name).write_bytes(published)
        entries.append({"source_relative_path": name, "durable_relative_path": "originals/" + name,
                        "public_path": "evidence/" + name,
                        "classification": "DERIVED" if published != raw else "BYTE_IDENTICAL",
                        "source_before_copy": row["before"], "durable_after_copy": row["after"],
                        "public": digest(published), "transformations": transformations})
    manifest = {
        "schema": "ringmin-archive-evidence-integration-v1",
        "historical_task": source_evidence["task"],
        "release_commit": source_evidence["release"]["resolved_commit"],
        "version_doi": source_evidence["zenodo"]["version_doi"],
        "durable_directory_name": durable.name,
        "private_copy_manifest": digest(copy_bytes),
        "local_copy_file_count": len(copy["files"]),
        "scope": "Public selection from preserved original audit outputs; no new audit or verifier execution.",
        "aliases": {"AUDIT_ORIGINALS": "Original audit directory; full origin/copy mapping is local only.",
                    "REPOSITORY_ROOT": "Local repository root.",
                    "USER_HOME": "Local account home directory.",
                    "REVIEW_STATE_REGISTRY": "Private Review State Registry; ringmin row preserved."},
        "files": entries,
    }
    (output / "EVIDENCE_MANIFEST.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode())
    print(json.dumps({"result": "PASS", "public_files": len(entries),
                      "derived": sum(x["classification"] == "DERIVED" for x in entries),
                      "byte_identical": sum(x["classification"] == "BYTE_IDENTICAL" for x in entries)}))


if __name__ == "__main__":
    prepare(Path(sys.argv[1]), Path(sys.argv[2]))
