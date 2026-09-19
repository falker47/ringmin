"""Build the journal PDF twice in an ignored work directory; record provenance.

Run from any directory. Requires Python >=3.11 and pdflatex on PATH.
No protected paper, solver, result, certificate or verifier is modified.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WORK = ROOT / "reproducibility/.work/journal_dcg"
BASELINE = "6c16af422d1cb38641c62d43b6e0e547921b9ba9"
EPOCH = str(int(datetime.datetime(2026, 9, 19, tzinfo=datetime.timezone.utc).timestamp()))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def protected_digest(path):
    data = path.read_bytes()
    if "originals" not in path.parts:
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()

def main():
    WORK.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH=EPOCH, FORCE_SOURCE_DATE="1")
    command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-no-shell-escape",
               "-output-directory=" + os.path.relpath(WORK, HERE), "ringmin_dcg.tex"]
    for run in (1, 2):
        result = subprocess.run(command, cwd=HERE, env=env, capture_output=True)
        (WORK / f"build-pass-{run}.txt").write_bytes(result.stdout + result.stderr)
        if result.returncode:
            print((result.stdout + result.stderr).decode("utf-8", errors="replace")[-6500:])
            raise SystemExit(result.returncode)
    log = (WORK / "ringmin_dcg.log").read_text(encoding="utf-8", errors="replace")
    unresolved = [s for s in log.splitlines() if "undefined" in s.lower()
                  or "Rerun to get" in s or "multiply defined" in s.lower()]
    if unresolved:
        raise RuntimeError("Unresolved references: " + repr(unresolved))
    overfull = re.findall(r"Overfull \\[hv]box[^\n]*", log)
    if overfull:
        print("LAYOUT WARNINGS:", *overfull, sep="\n")
    pdf = HERE / "ringmin_dcg.pdf"
    shutil.copyfile(WORK / pdf.name, pdf)
    inputs = sorted(HERE.glob("*.tex")) + [HERE / "build.py", HERE / "export_tables.py", HERE / ".gitattributes"]
    protected = [
        "paper_assets/v1_correction/ringmin_finite_v2.tex",
        "research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md",
        "research/GLOBAL_BRACKET_CERTIFICATE.md", "verify_global_brackets.py",
        "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json",
    ]
    version = subprocess.check_output(["pdflatex", "--version"], env=env).decode().splitlines()[0]
    manifest = {
        "artifact": "First complete standalone finite DCG working manuscript",
        "mathematical_source_commit": BASELINE,
        "manuscript_generation_commit": "The task commit containing this manifest; see git log -- paper_assets/journal_dcg/BUILD_MANIFEST.json",
        "command_from_repository_root": "python paper_assets/journal_dcg/build.py",
        "compiler": version, "passes": 2, "SOURCE_DATE_EPOCH": EPOCH,
        "FORCE_SOURCE_DATE": "1", "shell_escape": False,
        "pdf_dates_and_path_identifiers": "suppressed in source",
        "inputs_sha256": {p.relative_to(ROOT).as_posix(): digest(p) for p in inputs},
        "protected_input_hash_convention": "CRLF normalized to LF for tracked text sources; preserved originals hashed byte for byte",
        "protected_mathematical_inputs_sha256": {p: protected_digest(ROOT/p) for p in protected},
        "output_sha256": {pdf.relative_to(ROOT).as_posix(): digest(pdf)},
        "pages": int(re.search(r"Output written on .*?\((\d+) pages?", log, re.S)[1]),
        "unresolved_references": unresolved, "overfull_boxes": overfull,
        "portability": "Byte identity tested only with the recorded local TeX toolchain; other TeX/font versions may differ.",
    }
    (HERE / "BUILD_MANIFEST.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(f"Built {pdf.name}: {manifest['pages']} pages; {len(overfull)} overfull boxes; no unresolved references.")
    print("PDF SHA256:", digest(pdf))

if __name__ == "__main__":
    main()
