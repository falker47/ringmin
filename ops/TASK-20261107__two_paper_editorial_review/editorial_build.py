"""Task-local prose-review build provenance; never rebuild S1 or S2."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, re, shutil, subprocess, sys, tempfile, zipfile
ROOT = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
BASE = "7d257221d9034ca5f895f062e45e782d8e77b6c2"
WORK = ROOT / "reproducibility/.work/editorial_20261107"
SPECS = {
    "paper_i": ("paper_assets/journal_dcg", "ringmin_dcg", "1789776000",
                ["ringmin_dcg.tex", "seam_appendix.tex", "bracket_rows.tex", "coverage_rows.tex"]),
    "paper_ii": ("paper_assets/paper_ii_journal", "main", "1792713600", ["main.tex"]),
}
def sha(data):
    return hashlib.sha256(data).hexdigest()
def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n", encoding="utf-8", newline="\n")
def git_bytes(path):
    return subprocess.check_output(["git", "show", BASE+":"+path], cwd=ROOT)
def compile_one(paper, phase):
    folder, stem, epoch, names = SPECS[paper]
    dest = WORK / phase / paper
    dest.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH=epoch, FORCE_SOURCE_DATE="1")
    command = ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
               "-halt-on-error", "-file-line-error", "-recorder", stem+".tex"]
    roots = []
    for key in ("TEXMFROOT", "TEXMFDIST", "TEXMFLOCAL", "TEXMFVAR", "TEXMFCONFIG", "TEXMFSYSVAR", "TEXMFSYSCONFIG"):
        value = subprocess.check_output(["kpsewhich", "-var-value="+key], text=True).strip()
        if value and "{" not in value:
            roots.append(Path(value).resolve())
    expanded = subprocess.check_output(["kpsewhich", "-expand-path=$TEXMF"], text=True).strip()
    for value in expanded.split(os.pathsep):
        value = value.removeprefix("!!").rstrip("/")
        if value and "{" not in value and Path(value).is_absolute():
            roots.append(Path(value).resolve())
    with tempfile.TemporaryDirectory(prefix="ringmin-editorial-") as tmp:
        work = Path(tmp)
        inputs = {}
        for name in names:
            rel = folder+"/"+name
            data = git_bytes(rel) if phase == "baseline" else (ROOT/rel).read_bytes()
            (work/name).write_bytes(data)
            inputs[rel] = sha(data)
        for run in range(1, 4):
            result = subprocess.run(command, cwd=work, env=env, capture_output=True)
            (dest/f"pass-{run}.txt").write_bytes(result.stdout+result.stderr)
            if result.returncode:
                raise RuntimeError(f"{paper} {phase} pass {run}: "+
                    (result.stdout+result.stderr).decode(errors="replace")[-5000:])
        log = (work/(stem+".log")).read_text(errors="replace")
        warnings = [line.strip() for line in log.splitlines() if re.search(
            r"^(?:LaTeX|Package .+|Class .+|pdfTeX)(?: Font)? Warning:|^Overfull|^Underfull|^Missing character|^!|undefined references|multiply defined labels|Rerun to get", line, re.I)]
        systems = {}
        local_inputs = set()
        for line in (work/(stem+".fls")).read_text(errors="replace").splitlines():
            if not line.startswith("INPUT "):
                continue
            item = Path(line[6:])
            if not item.is_absolute():
                item = work/item
            if not item.exists():
                continue
            item = item.resolve()
            if item.is_relative_to(work.resolve()):
                if item.name not in set(names)|{stem+s for s in (".aux", ".out", ".toc")}:
                    raise RuntimeError("Undeclared local input: "+item.name)
                if item.name in names:
                    local_inputs.add(item.name)
            else:
                if not any(item.is_relative_to(root) for root in roots):
                    raise RuntimeError("Undeclared external input: "+item.name)
                digest = sha(item.read_bytes())
                systems[item.name+":"+digest[:16]] = digest
        if local_inputs != set(names):
            raise RuntimeError("Missing declared inputs")
        for ext in (".pdf", ".log", ".aux", ".fls"):
            shutil.copyfile(work/(stem+ext), dest/(stem+ext))
        pdf = (dest/(stem+".pdf")).read_bytes()
        record = {
            "phase": phase, "source_base_commit": BASE, "inputs_sha256": inputs,
            "source_sha256": inputs[folder+"/"+stem+".tex"], "pdf_sha256": sha(pdf),
            "pages": int(re.search(r"Output written on .*?\((\d+) pages?", log, re.S)[1]),
            "passes": 3, "warnings": warnings, "unresolved_or_box_warnings": warnings,
            "compiler": subprocess.check_output(["pdflatex","--version"], text=True).splitlines()[0],
            "command": command, "SOURCE_DATE_EPOCH": epoch, "FORCE_SOURCE_DATE": "1",
            "system_inputs": dict(sorted(systems.items())),
            "source_commit": "The local task commit containing these source and output hashes" if phase != "baseline" else BASE,
        }
        write_json(DOSSIER/f"build_{phase}_{paper}.json", record)
        print(f"{phase} {paper}: {record['pages']} pages; {len(warnings)} final-log warnings; SHA256 {sha(pdf)}", flush=True)
        return record
def deliver():
    for paper, (folder, stem, epoch, names) in SPECS.items():
        record = json.loads((DOSSIER/f"build_revised_{paper}.json").read_text())
        pdf = WORK/"revised"/paper/(stem+".pdf")
        if sha(pdf.read_bytes()) != record["pdf_sha256"]:
            raise RuntimeError("Stale revised PDF")
        for name in names:
            rel=folder+"/"+name
            if sha((ROOT/rel).read_bytes()) != record["inputs_sha256"][rel]:
                raise RuntimeError("Stale revised source")
        if record["warnings"]:
            raise RuntimeError("Unresolved build warning")
        shutil.copyfile(pdf, ROOT/folder/(stem+".pdf"))
        if paper == "paper_i":
            old = json.loads(git_bytes(folder+"/BUILD_MANIFEST.json"))
            old.update({
                "artifact": "Local editorial revision of the finite manuscript; no submission",
                "revision_baseline_commit": BASE,
                "command_from_repository_root": "python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py revised; python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py deliver",
                "compiler": record["compiler"], "passes": 3,
                "pages": record["pages"], "unresolved_references": [], "overfull_boxes": [],
                "output_sha256": {folder+"/"+stem+".pdf": record["pdf_sha256"]},
                "editorial_build_evidence": "ops/TASK-20261107__two_paper_editorial_review/build_revised_paper_i.json",
            })
            for rel in old["inputs_sha256"]:
                old["inputs_sha256"][rel] = sha((ROOT/rel).read_bytes())
            write_json(ROOT/folder/"BUILD_MANIFEST.json", old)
        else:
            old = json.loads(git_bytes(folder+"/BUILD_REPORT.json"))
            old["documents"]["main"] = record
            old["document_provenance"] = {
                "main": "Fresh 2026-11-07 local build; compiler and system-input hashes in this document record.",
                "upper_supplement": "Inherited unchanged from "+BASE+"; not compiled or edited in this task.",
                "lower": "Inherited unchanged from "+BASE+"; not compiled or edited in this task.",
            }
            old["top_level_environment_scope"] = "Historical environment of unchanged S1/S2 records. The main record carries its own current environment."
            write_json(ROOT/folder/"BUILD_REPORT.json", old)
    print("Delivered only the two main PDFs and synchronized their build provenance.")
def export():
    folder = ROOT/"paper_assets/paper_ii_journal"
    spec = importlib.util.spec_from_file_location("paper_ii_build", folder/"build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    import runpy
    verifier = runpy.run_path(str(folder/"verify_package.py"))
    verifier["validate_build_report"](folder, module.lower_dir())
    def manifest(files):
        record = module.manifest(files)
        record.update({"date":"2026-11-07", "editorial_base_commit":BASE,
                       "generation":"python ops/TASK-20261107__two_paper_editorial_review/editorial_build.py export",
                       "scope":"Local prose revision; S1/S2 retained byte for byte; no submission or push."})
        return record
    files = module.payload()
    for path in sorted(module.lower_dir().iterdir()):
        if path.is_file():
            files["lower_supplement/"+path.name] = path.read_bytes()
    files["MANIFEST.json"] = module.json_bytes(manifest(files))
    archive = folder/"source_bundle.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for name,data in sorted(files.items()):
            info=zipfile.ZipInfo(name,(2026,11,7,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            out.writestr(info,data)
    outer=module.payload()
    outer["source_bundle.zip"]=archive.read_bytes()
    (folder/"MANIFEST.json").write_bytes(module.json_bytes(manifest(outer)))
    print("Exported local review bundle with preserved supplement bytes:",len(files),"members;",sha(archive.read_bytes()))
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("baseline","revised","repeat","deliver","export"))
    args=parser.parse_args()
    if args.mode in ("baseline","revised","repeat"):
        for paper in SPECS:
            compile_one(paper,args.mode)
    elif args.mode=="deliver":
        deliver()
    else:
        export()
if __name__=="__main__":
    main()
