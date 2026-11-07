"""Task-scoped wrapper: compile only main manuscripts; preserve supplements."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import tempfile
import zipfile

BASE = "4303fe4d937c5f2c7915070a0aaffa67f9b448ca"
TASK = "ops/TASK-20261107__two_paper_approved_refinements"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8", newline="\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("build", "export", "verify"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    dossier = root / TASK
    work = root / "reproducibility/.work/approved_refinements_20261107"
    package = root / "paper_assets/paper_ii_journal"
    builder = runpy.run_path(str(package / "build.py"))
    verifier = runpy.run_path(str(package / "verify_package.py"))
    before = json.loads((dossier / "BUILD_REPORT.before.json").read_text())
    compiler = subprocess.check_output(["pdflatex", "--version"], text=True).splitlines()[0]

    def supplements_unchanged():
        pins = json.loads((dossier / "SUPPLEMENTS.before.json").read_text())["sha256"]
        assert all(sha((root / name).read_bytes()) == digest for name, digest in pins.items())
        report = json.loads((package / "BUILD_REPORT.json").read_text())
        for name in ("lower", "upper_supplement"):
            assert report["documents"][name] == before["documents"][name], name
        return len(pins)

    if args.mode == "build":
        supplements_unchanged()
        # Reuse the previously audited isolated Paper I builder unchanged.
        previous = runpy.run_path(str(root / "ops/TASK-20261107__two_paper_editorial_review/editorial_build.py"))
        compile_i = previous["compile_one"]
        compile_i.__globals__.update(BASE=BASE, DOSSIER=dossier, WORK=work)
        records_i = [compile_i("paper_i", phase) for phase in ("revised", "repeat")]
        assert not any(r["warnings"] for r in records_i)
        assert records_i[0]["pdf_sha256"] == records_i[1]["pdf_sha256"]
        assert records_i[0]["system_inputs"] == records_i[1]["system_inputs"]
        results_ii = []
        # Capture final logs before the unchanged compile_document removes its temp dir.
        original_temp = tempfile.TemporaryDirectory
        for phase in ("revised", "repeat"):
            destination = work / phase / "paper_ii"
            destination.mkdir(parents=True, exist_ok=True)

            class CapturedTemporaryDirectory(original_temp):
                def __exit__(self, *exc):
                    for suffix in (".log", ".fls", ".pdf", ".aux"):
                        item = Path(self.name) / ("main" + suffix)
                        if item.exists():
                            shutil.copyfile(item, destination / item.name)
                    return super().__exit__(*exc)

            tempfile.TemporaryDirectory = CapturedTemporaryDirectory
            try:
                # Explicitly required main-only entry point; never call build().
                pdf, record = builder["compile_document"](package / "main.tex")
            finally:
                tempfile.TemporaryDirectory = original_temp
            log = (destination / "main.log").read_text(errors="replace")
            warnings = [line.strip() for line in log.splitlines() if re.search(
                r"^(?:LaTeX|Package .+|Class .+|pdfTeX)(?: Font)? Warning:|^Overfull|^Underfull|^Missing character|^!|undefined references|multiply defined labels|Rerun to get",
                line, re.I)]
            assert not warnings, warnings
            write_json(dossier / f"build_{phase}_paper_ii.json", record)
            results_ii.append((pdf, record))
            print(f"{phase} paper_ii: {record['pages']} pages; zero final-log warnings; SHA256 {sha(pdf)}", flush=True)
        assert results_ii[0] == results_ii[1], "Repeated main PDF/record mismatch"
        # Deliver only after both independent fresh-directory repeats pass.
        folder_i = root / "paper_assets/journal_dcg"
        shutil.copyfile(work / "revised/paper_i/ringmin_dcg.pdf", folder_i / "ringmin_dcg.pdf")
        record_i = records_i[0]
        manifest_i = json.loads((folder_i / "BUILD_MANIFEST.json").read_text())
        manifest_i.update({
            "artifact": "Approved editorial refinements of the finite manuscript; no submission",
            "revision_baseline_commit": BASE,
            "command_from_repository_root": f"python {TASK}/approved_build.py build",
            "compiler": compiler, "passes": 3, "pages": record_i["pages"],
            "unresolved_references": [], "overfull_boxes": [],
            "output_sha256": {"paper_assets/journal_dcg/ringmin_dcg.pdf": record_i["pdf_sha256"]},
            "editorial_build_evidence": f"{TASK}/build_revised_paper_i.json",
        })
        for rel in manifest_i["inputs_sha256"]:
            manifest_i["inputs_sha256"][rel] = sha((root / rel).read_bytes())
        write_json(folder_i / "BUILD_MANIFEST.json", manifest_i)
        report = copy.deepcopy(before)
        report["documents"]["main"] = results_ii[0][1]
        historical = {key: before[key] for key in
                      ("compiler", "command", "SOURCE_DATE_EPOCH", "FORCE_SOURCE_DATE")}
        current = dict(historical, compiler=compiler, SOURCE_DATE_EPOCH=builder["EPOCH"])
        current.update(status="recompiled", observed_on="2026-11-07",
                       invocation=f"python {TASK}/approved_build.py build; direct runpy compile_document(main.tex)")
        report["build_context_by_document"] = {"main": current}
        for name in ("lower", "upper_supplement"):
            report["build_context_by_document"][name] = dict(
                historical, status="inherited_not_recompiled", inherited_from_commit=BASE,
                scope="Original context of the unchanged supplement build record; not a current execution.")
        report["document_provenance"] = {
            "main": "Recompiled twice on 2026-11-07 using direct compile_document(main.tex); identical PDF bytes and build records.",
            "lower": f"Entire record and delivered files inherited unchanged from {BASE}; no S1 compilation.",
            "upper_supplement": f"Entire record and delivered files inherited unchanged from {BASE}; no S2 compilation.",
        }
        report["top_level_environment_scope"] = (
            "Historical environment of the inherited lower/upper_supplement records only. "
            "Use build_context_by_document for each document; main was recompiled with its own current compiler. "
            "S1 delivered PDF remains preserved-baseline, distinct from its historical check-build PDF.")
        (package / "main.pdf").write_bytes(results_ii[0][0])
        write_json(package / "BUILD_REPORT.json", report)
        count = supplements_unchanged()
        verifier["validate_build_report"](package, builder["lower_dir"]())
        write_json(dossier / "REPEAT_BUILD_CHECK.json", {
            "paper_i_pdf_identical": True, "paper_i_system_inputs_identical": True,
            "paper_ii_pdf_and_record_identical": True, "final_log_warnings": [],
            "supplement_files_byte_identical": count, "supplement_records_unchanged": True,
            "validate_build_report": "PASS", "compiler": compiler,
        })
        print("PASS main-only delivery, repeated builds and validate_build_report", flush=True)

    elif args.mode == "export":
        supplements_unchanged()
        verifier["validate_build_report"](package, builder["lower_dir"]())
        export = builder["export"]
        original_manifest = export.__globals__["manifest"]
        report = json.loads((package / "BUILD_REPORT.json").read_text())

        def current_manifest(files):
            value = original_manifest(files)
            value.update({
                "date": "2026-11-07", "editorial_base_commit": BASE,
                "generation": f"python {TASK}/approved_build.py export (temporary wrapper copy outside package; unchanged build.py export)",
                "scope": "Approved prose refinements: main recompiled; S1/S2 reused byte-identically. No submission, push or scientific baseline promotion.",
                "build_context_by_document": report["build_context_by_document"],
            })
            return value

        export.__globals__["manifest"] = current_manifest
        try:
            export()
        finally:
            export.__globals__["manifest"] = original_manifest
        supplements_unchanged()

    else:
        count = supplements_unchanged()
        verifier["validate_build_report"](package, builder["lower_dir"]())
        with zipfile.ZipFile(package / "source_bundle.zip") as archive:
            inner = json.loads(archive.read("MANIFEST.json"))
        outer = json.loads((package / "MANIFEST.json").read_text())
        for key in ("date", "generation", "scope", "editorial_base_commit", "build_context_by_document"):
            assert inner[key] == outer[key], key
        assert inner["date"] == "2026-11-07"
        assert "main recompiled; S1/S2 reused" in inner["scope"]
        print(f"PASS preserved {count} supplement files, full inherited records, and paired manifest context")


if __name__ == "__main__":
    main()
