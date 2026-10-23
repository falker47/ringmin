"""Isolated, deterministic journal build/export. Python >=3.11; pdfLaTeX on PATH."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import runpy
import shutil
import subprocess
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
BASE = "75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae"
EPOCH = "1792713600"  # 2026-10-23 00:00:00 UTC; no local-time dependency.
EXCLUDED = {"MANIFEST.json", "source_bundle.zip"}
def sha(data):
    return hashlib.sha256(data).hexdigest()
def lower_dir():
    local = HERE / "lower_supplement"
    return local if local.is_dir() else HERE.parent / "asymptotic_sequel/proposition7_supplement"
def payload():
    return {p.relative_to(HERE).as_posix(): p.read_bytes()
            for p in sorted(HERE.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts
            and p.relative_to(HERE).as_posix() not in EXCLUDED}
def manifest(files):
    return {
        "schema": "ringmin-paper-ii-journal-v1",
        "repository": "falker47/ringmin", "baseline_commit": BASE,
        "scientific_source_commit": "3beb8d70c5b3748d370a92855847bdf574e5a14f",
        "candidate_revision": "The Git commit containing this manifest; output hashes bind its source files.",
        "date": "2026-10-23", "excluded_from_self_hash": ["MANIFEST.json"],
        "outputs": {name: sha(data) for name, data in sorted(files.items())},
        "lower_supplement": {"baseline_commit": BASE,
            "manifest_sha256": sha((lower_dir() / "MANIFEST.json").read_bytes()),
            "repository_path": "paper_assets/asymptotic_sequel/proposition7_supplement"},
        "generation": "python build.py; python build.py --export",
        "limitations": "Hashes bind files, not truth. Identical PDF bytes require the recorded TeX/font environment. Universal mathematical claims depend on written proofs."
    }
def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
def compile_document(source):
    env = dict(os.environ, SOURCE_DATE_EPOCH=EPOCH, FORCE_SOURCE_DATE="1")
    system_roots = []
    for key in ("TEXMFROOT", "TEXMFDIST", "TEXMFLOCAL", "TEXMFVAR", "TEXMFCONFIG", "TEXMFSYSVAR", "TEXMFSYSCONFIG"):
        value = subprocess.check_output(["kpsewhich", "-var-value="+key], text=True).strip()
        if value and "{" not in value:
            system_roots.append(Path(value).resolve())
    with tempfile.TemporaryDirectory(prefix="ringmin-paper-ii-") as temp:
        work = Path(temp)
        shutil.copyfile(source, work/source.name)
        command = ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
                   "-halt-on-error", "-file-line-error", "-recorder", source.name]
        for run in range(3):
            result = subprocess.run(command, cwd=work, env=env, capture_output=True)
            if result.returncode:
                raise RuntimeError(result.stdout.decode(errors="replace")[-8000:])
        log = (work/source.with_suffix(".log").name).read_text(errors="replace")
        problems = [line for line in log.splitlines()
                    if any(token in line.lower() for token in
                           ("undefined", "multiply defined", "rerun to get",
                            "overfull", "underfull", "missing character"))]
        if problems:
            raise RuntimeError("\n".join(problems))
        # Recorder closure: a source outside this isolated directory is forbidden.
        system_inputs = {}
        for line in (work/source.with_suffix(".fls").name).read_text(errors="replace").splitlines():
            if line.startswith("INPUT "):
                item = Path(line[6:])
                if not item.is_absolute():
                    item = work/item
                if item.exists():
                    resolved = item.resolve()
                    if resolved.is_relative_to(work.resolve()):
                        generated = {(work/source.with_suffix(suffix).name).resolve()
                                     for suffix in (".aux", ".out", ".toc")}
                        if resolved != (work/source.name).resolve() and resolved not in generated:
                            raise RuntimeError("Undeclared local build input: "+item.name)
                    else:
                        if not any(resolved.is_relative_to(base) for base in system_roots):
                            raise RuntimeError("Input outside isolated build and declared TeX roots: "+item.name)
                        key = item.name + ":" + sha(item.read_bytes())[:16]
                        system_inputs[key] = sha(item.read_bytes())
        pdf = (work/source.with_suffix(".pdf").name).read_bytes()
        record = {"pages": int(re.search(r"Output written on .*?\((\d+) pages?", log, re.S)[1]),
                  "source_sha256": sha(source.read_bytes()), "pdf_sha256": sha(pdf),
                  "passes": 3, "unresolved_or_box_warnings": problems,
                  "system_inputs": dict(sorted(system_inputs.items()))}
        return pdf, record
def build(names):
    records = {}
    for name in names:
        source = lower_dir()/"supplement.tex" if name == "lower" else HERE/(name+".tex")
        pdf, record = compile_document(source)
        if name == "lower":
            record["matches_preserved_pdf"] = sha(pdf) == sha((lower_dir()/"supplement.pdf").read_bytes())
        else:
            (HERE/(name+".pdf")).write_bytes(pdf)
        records[name] = record
        print(f"PASS isolated build {name}: {record['pages']} pages; zero reference/box warnings; {record['pdf_sha256']}")
    report = {"compiler": subprocess.check_output(["pdflatex","--version"]).decode().splitlines()[0],
              "SOURCE_DATE_EPOCH": EPOCH, "FORCE_SOURCE_DATE": "1",
              "command": "pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder <source> (three passes in a new external temporary directory)",
              "documents": records}
    (HERE/"BUILD_REPORT.json").write_bytes(json_bytes(report))
def export():
    verifier = runpy.run_path(str(HERE/"verify_package.py"))
    verifier["validate_build_report"](HERE, lower_dir())
    files = payload()
    # Copy the already completed lower supplement without changing any byte.
    if not (HERE/"lower_supplement").is_dir():
        for p in sorted(lower_dir().iterdir()):
            if p.is_file():
                files["lower_supplement/"+p.name] = p.read_bytes()
    files["MANIFEST.json"] = json_bytes(manifest(files))
    target = HERE/"source_bundle.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026,10,23,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            out.writestr(info, data)
    outer = payload()
    outer["source_bundle.zip"] = target.read_bytes()
    (HERE/"MANIFEST.json").write_bytes(json_bytes(manifest(outer)))
    print(f"PASS export: {len(files)} archive files; archive SHA256 {sha(target.read_bytes())}")
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export",action="store_true",help="Export current verified outputs; does not compile")
    parser.add_argument("--document",choices=("main","upper_supplement","lower"))
    args=parser.parse_args()
    if args.export:
        export()
    else:
        build([args.document] if args.document else ["main","upper_supplement","lower"])
if __name__=="__main__":
    main()
