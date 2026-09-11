"""Portable log restoration and verifier failure behavior; no production import."""

import importlib.util
import json
from pathlib import Path
import shutil

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_portable_original_frontier_paths(tmp_path):
    logs = load(ROOT / "scripts" / "frontier_logs.py", "restore_logs")
    verifier = load(ROOT / "verify.py", "independent_verifier")
    shutil.copytree(ROOT / "reproducibility" / "frontier_logs",
                    tmp_path / "reproducibility" / "frontier_logs")
    logs.restore(tmp_path)
    logs.restore(tmp_path)  # Idempotent readback, without overwriting evidence.
    for n in range(3, 15):
        payload = json.loads((ROOT / "results" / "frontiers" / f"n{n:02d}_frontier.json").read_text())
        ok, messages = verifier.progress_log_has_prefixes(tmp_path, payload)
        assert ok, messages
        portable = dict(payload, progress_log=payload["progress_log"].replace("\\", "/"))
        assert verifier.progress_log_has_prefixes(tmp_path, portable) == (True, [])
    for name in ("../outside.log", "/outside.log",
                 "C:/results/checkpoints/progress_n03_lb3.log",
                 "C:results/checkpoints/progress_n03_lb3.log",
                 "C:\\results\\checkpoints\\progress_n03_lb3.log"):
        assert not verifier.progress_log_has_prefixes(tmp_path, {"progress_log": name})[0]


def test_corrupt_archive_and_existing_log_fail_before_restoration(tmp_path):
    logs = load(ROOT / "scripts" / "frontier_logs.py", "restore_logs_corrupt")
    shutil.copytree(ROOT / "reproducibility" / "frontier_logs",
                    tmp_path / "reproducibility" / "frontier_logs")
    archive = tmp_path / "reproducibility" / "frontier_logs" / "progress_n14_lb3.log.gz"
    data = archive.read_bytes()
    archive.write_bytes(data[:-1] + bytes([data[-1] ^ 1]))
    with pytest.raises(ValueError, match="archive hash mismatch"):
        logs.restore(tmp_path)
    assert not (tmp_path / "results").exists()
    archive.write_bytes(data)
    target = tmp_path / "results" / "checkpoints" / "progress_n14_lb3.log"
    target.parent.mkdir(parents=True)
    target.write_bytes(b"different existing evidence")
    with pytest.raises(ValueError, match="refusing to overwrite"):
        logs.restore(tmp_path)
    assert not target.with_name("progress_n03_lb3.log").exists()
    assert target.read_bytes() == b"different existing evidence"


def test_missing_prefix_completion_is_rejected(tmp_path):
    verifier = load(ROOT / "verify.py", "independent_verifier_missing")
    path = tmp_path / "results" / "checkpoints" / "sample.log"
    path.parent.mkdir(parents=True)
    path.write_text("stage=stage_a\tprefix=1\tdone=4\tchunk\n")
    payload = {"progress_log": "results\\checkpoints\\sample.log",
               "prefix_coverage": [{"prefix": 1, "count": 4}]}
    assert not verifier.progress_log_has_prefixes(tmp_path, payload)[0]
    path.write_text("stage=stage_a\tprefix=1\tdone=3\tprefix complete\n")
    assert not verifier.progress_log_has_prefixes(tmp_path, payload)[0]
    path.write_text("stage=stage_a\tprefix=1\tdone=4\tprefix complete\n")
    assert verifier.progress_log_has_prefixes(tmp_path, payload) == (True, [])
