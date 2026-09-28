"""Build/check an exact DCG submission package; never modify accepted inputs."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = Path(__file__).resolve().parent
PACKAGE = ROOT / "paper_assets/dcg_submission"
SOURCE = ROOT / "paper_assets/journal_dcg"
WORK = ROOT / "reproducibility/.work/dcg_submission_package"
BASE = "6749d6b165f982136117481be322c8beaec223ce"
TEX = ("bracket_rows.tex", "coverage_rows.tex", "ringmin_dcg.tex", "seam_appendix.tex")
PAYLOAD = (*TEX, "ringmin_dcg.pdf", "ringmin_dcg_sources.zip",
           "cover_letter.txt", "UPLOAD_CHECKLIST.md", ".gitattributes")
ALL_FILES = {*PAYLOAD, "SUBMISSION_MANIFEST.json", "SHA256SUMS"}
EXEMPT = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
EXEMPT_HASH = "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db"
MUTABLE = {"CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md"}
NEW_PREFIXES = ("paper_assets/dcg_submission/", "ops/" + DOSSIER.name + "/")
GIT = ["git", "-c", "safe.directory=" + ROOT.as_posix()]
COMMAND = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
           "-file-line-error", "-no-shell-escape", "-recorder", "ringmin_dcg.tex"]


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8", newline="\n")


def accepted(name):
    return subprocess.check_output(GIT + ["show", BASE + ":paper_assets/journal_dcg/" + name])


def source_zip():
    result = io.BytesIO()
    with zipfile.ZipFile(result, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in TEX:
            entry = zipfile.ZipInfo(name, (2026, 9, 28, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (PACKAGE / name).read_bytes())
    return result.getvalue()


def compile_clean(index):
    # This fresh directory is outside the repository. Only the source ZIP's
    # four explicit entries enter it; inherited TeX input paths are discarded.
    with tempfile.TemporaryDirectory(prefix="ringmin_dcg_package_") as temporary:
        build = Path(temporary)
        need(not build.is_relative_to(ROOT), "build must be outside repository")
        with zipfile.ZipFile(PACKAGE / "ringmin_dcg_sources.zip") as archive:
            need(archive.namelist() == list(TEX), "source ZIP membership/order")
            for name in TEX:
                (build / name).write_bytes(archive.read(name))
        env = dict(os.environ, SOURCE_DATE_EPOCH="1789776000", FORCE_SOURCE_DATE="1")
        for key in ("TEXINPUTS", "TEXMFHOME", "TEXMFOUTPUT", "TEXMFLOCAL"):
            env.pop(key, None)
        env["TEXINPUTS"] = "." + os.pathsep
        env["TEXMFHOME"] = str(build / "empty-texmf-home")
        exits = []
        for run in (1, 2):
            result = subprocess.run(COMMAND, cwd=build, env=env, capture_output=True)
            (WORK / f"clean-{index}-pass-{run}.txt").write_bytes(result.stdout + result.stderr)
            exits.append(result.returncode)
            need(result.returncode == 0, f"clean build {index} pass {run} failed; see ignored log")
        log = (build / "ringmin_dcg.log").read_text(encoding="utf-8", errors="replace")
        unresolved = [line for line in log.splitlines() if any(s in line.lower() for s in
                      ("undefined", "rerun to get", "multiply defined", "rerunfilecheck warning"))]
        overfull = re.findall(r"Overfull \\[hv]box[^\n]*", log)
        need(not unresolved and not overfull, "final-pass references/layout")
        records = (build / "ringmin_dcg.fls").read_text(encoding="utf-8", errors="replace")
        local_inputs, system_inputs = set(), set()
        for line in records.splitlines():
            if not line.startswith("INPUT "):
                continue
            path = Path(line[6:])
            path = (build / path).resolve() if not path.is_absolute() else path.resolve()
            need(not path.is_relative_to(ROOT), "repository input leaked into clean build")
            if path.is_relative_to(build):
                local_inputs.add(path.relative_to(build).as_posix())
            else:
                system_inputs.add(path.name)
        need(set(TEX) <= local_inputs, "all packaged TeX inputs consumed")
        need(local_inputs <= {*TEX, "ringmin_dcg.aux", "ringmin_dcg.out"}, "unexpected local input")
        pdf_hash = sha((build / "ringmin_dcg.pdf").read_bytes())
        need(pdf_hash == sha(accepted("ringmin_dcg.pdf")), "compiled PDF differs from accepted PDF")
        (WORK / f"clean-{index}-final.log").write_text(log, encoding="utf-8")
        return {"build": index, "passes": 2, "exit_codes": exits,
                "directory": "fresh external temporary directory; removed after verification",
                "local_inputs": sorted(local_inputs), "system_input_basenames": sorted(system_inputs),
                "repository_inputs": [], "pdf_sha256": pdf_hash,
                "pages": int(re.search(r"Output written on .*?\((\d+) pages?", log, re.S)[1]),
                "unresolved_references": unresolved, "overfull_boxes": overfull}


def build_package():
    WORK.mkdir(parents=True, exist_ok=True)
    for name in (*TEX, "ringmin_dcg.pdf"):
        data = accepted(name)
        need((SOURCE / name).read_bytes() == data, "accepted input modified: " + name)
        (PACKAGE / name).write_bytes(data)
    (PACKAGE / "ringmin_dcg_sources.zip").write_bytes(source_zip())
    builds = [compile_clean(1), compile_clean(2)]
    compiler = subprocess.check_output(["pdflatex", "--version"]).decode().splitlines()[0]
    report = {"accepted_baseline": BASE, "compiler": compiler, "command": COMMAND,
              "builds": builds, "same_pdf_bytes": builds[0]["pdf_sha256"] == builds[1]["pdf_sha256"]}
    write_json(DOSSIER / "build_report.json", report)
    manifest = {
        "schema_version": 1, "artifact": "DCG submission package from unchanged accepted manuscript",
        "accepted_baseline": BASE, "prepared_on": "2026-09-28",
        "generation_commit": "The commit containing this manifest; inspect git log for this path",
        "archive_doi": "10.5281/zenodo.22849826",
        "archive_scope": "Frozen software/certificate snapshot, not this submission package",
        "source_directory_at_accepted_commit": "paper_assets/journal_dcg",
        "accepted_manuscript_sha256": {name: sha(accepted(name)) for name in (*TEX, "ringmin_dcg.pdf")},
        "payload": {name: {"bytes": (PACKAGE/name).stat().st_size,
                           "sha256": sha((PACKAGE/name).read_bytes())} for name in sorted(PAYLOAD)},
        "checksum_convention": "Raw bytes; manifest excludes itself and SHA256SUMS; SHA256SUMS hashes every other package file including this manifest",
        "source_zip": {"entries": list(TEX), "compression": "STORED", "entry_timestamp": "2026-09-28T00:00:00", "unix_mode": "100644"},
        "build": {"command": COMMAND, "compiler": compiler, "passes_per_clean_build": 2,
                  "clean_builds": 2, "SOURCE_DATE_EPOCH": "1789776000", "FORCE_SOURCE_DATE": "1",
                  "pages": 19, "overfull_boxes": 0, "unresolved_references": 0,
                  "repository_inputs": [], "matches_accepted_pdf_byte_for_byte": True},
        "standard_tex_dependencies": ["article", "fontenc (T1)", "lmodern", "geometry", "amsmath",
                                      "amssymb", "amsthm", "booktabs", "tabularx", "array", "hyperref"],
        "custom_styles_figures_bibliography_databases": [],
        "portability": "PDF byte identity verified on the recorded local toolchain; other TeX/font versions may differ",
        "scientific_supplementary_files": [],
    }
    write_json(PACKAGE / "SUBMISSION_MANIFEST.json", manifest)
    sums = "".join(sha((PACKAGE/name).read_bytes()) + "  " + name + "\n"
                   for name in sorted(ALL_FILES - {"SHA256SUMS"}))
    (PACKAGE / "SHA256SUMS").write_text(sums, encoding="utf-8", newline="\n")


def verify_package():
    need({p.name for p in PACKAGE.iterdir()} == ALL_FILES, "exact package inventory")
    manifest = json.loads((PACKAGE / "SUBMISSION_MANIFEST.json").read_text())
    need((PACKAGE / "SUBMISSION_MANIFEST.json").read_bytes() ==
         (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode(), "deterministic manifest serialization")
    need(manifest["accepted_baseline"] == BASE, "manifest baseline")
    need(set(manifest["payload"]) == set(PAYLOAD), "manifest inventory")
    for name, record in manifest["payload"].items():
        data = (PACKAGE/name).read_bytes()
        need(record == {"bytes": len(data), "sha256": sha(data)}, "payload hash/size: " + name)
    for name in (*TEX, "ringmin_dcg.pdf"):
        data = (PACKAGE/name).read_bytes()
        need(data == accepted(name) == (SOURCE/name).read_bytes(), "accepted source/PDF bytes: " + name)
        need(manifest["accepted_manuscript_sha256"][name] == sha(data), "source hash: " + name)
    need((PACKAGE/"ringmin_dcg_sources.zip").read_bytes() == source_zip(), "deterministic source ZIP")
    expected = "".join(sha((PACKAGE/name).read_bytes()) + "  " + name + "\n"
                       for name in sorted(ALL_FILES - {"SHA256SUMS"}))
    need((PACKAGE/"SHA256SUMS").read_text() == expected, "complete SHA256SUMS")
    report = json.loads((DOSSIER/"build_report.json").read_text())
    need(report["accepted_baseline"] == BASE and report["same_pdf_bytes"] and
         len(report["builds"]) == 2, "two-build report")
    for build in report["builds"]:
        need(build["exit_codes"] == [0, 0] and build["pages"] == 19 and
             build["pdf_sha256"] == sha(accepted("ringmin_dcg.pdf")) and
             build["repository_inputs"] == build["overfull_boxes"] == build["unresolved_references"] == [],
             "reported compilation gates")
    text = (PACKAGE/"ringmin_dcg.tex").read_text(encoding="utf-8")
    abstract = text.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
    keywords = text.split(r"\textbf{Keywords:}")[1].split(r"\medskip")[0]
    need(len(abstract.split()) == 184 and len(keywords.split(";")) == 6, "abstract and keywords")
    for token in ("52C26, 52C15, 05C85, 90C27", "Corresponding author:",
                  "Statements and Declarations", "Data and code availability.",
                  "10.5281/zenodo.22849826", "Use of artificial intelligence.",
                  "This assistance extended beyond copy editing."):
        need(token in text, "metadata: " + token)
    alltex = "\n".join((PACKAGE/name).read_text(encoding="utf-8") for name in TEX)
    need(set(re.findall(r"\\input\{([^}]+)\}", alltex)) == set(TEX)-{"ringmin_dcg.tex"}, "source closure")
    letter = (PACKAGE/"cover_letter.txt").read_text(encoding="utf-8")
    for stale in ("pre-submission", "working manuscript", "requires separate review", "b148080"):
        need(stale not in letter, "stale cover letter: " + stale)
    for token in ("Supnick", "seam", "3 <= n <= 14", "10.5281/zenodo.22849826",
                  "arXiv:2607.28654v2", "arXiv:2609.13630"):
        need(token in letter, "cover letter substance: " + token)
    snapshot = json.loads((WORK/"preflight_sha256.json").read_text())
    protected = {p: h for p, h in snapshot.items() if p not in MUTABLE}
    for path, digest in protected.items():
        need(sha((ROOT/path).read_bytes()) == digest, "protected bytes: " + path)
    need(sha((ROOT/EXEMPT).read_bytes()) == EXEMPT_HASH, "exempt ZIP bytes")
    tracked_changes = subprocess.check_output(GIT+["diff", BASE, "--name-only"], text=True).splitlines()
    untracked = subprocess.check_output(GIT+["ls-files", "--others", "--exclude-standard"], text=True).splitlines()
    need(all(p in MUTABLE or p.startswith(NEW_PREFIXES) for p in tracked_changes), "tracked scope")
    need(all(p == EXEMPT or p.startswith(NEW_PREFIXES) for p in untracked), "untracked scope")
    staged = subprocess.check_output(GIT+["diff", "--cached", "--name-only"], text=True).splitlines()
    need(EXEMPT not in staged, "exempt ZIP staged")
    additions = [p for prefix in NEW_PREFIXES for p in (ROOT/prefix).rglob("*") if p.is_file()]
    for path in additions + [ROOT/p for p in MUTABLE]:
        if path.suffix in (".pdf", ".zip"):
            continue
        value = path.read_text(encoding="utf-8")
        need(value.endswith("\n") and all(line == line.rstrip() for line in value.splitlines()),
             "text/whitespace: " + path.relative_to(ROOT).as_posix())
    result = {"status": "PASS_PACKAGE", "accepted_baseline": BASE,
              "package_files": len(ALL_FILES), "checksums_verified": len(ALL_FILES)-1,
              "accepted_manuscript_files_byte_identical": 5,
              "protected_files_byte_identical": len(protected), "exempt_zip_sha256": EXEMPT_HASH,
              "abstract_whitespace_words": 184, "keywords": 6,
              "msc": ["52C26", "52C15", "05C85", "90C27"],
              "manifest_sha256": sha((PACKAGE/"SUBMISSION_MANIFEST.json").read_bytes()),
              "sha256sums_sha256": sha((PACKAGE/"SHA256SUMS").read_bytes()),
              "limitations": "Packaging/transcription checks, not fresh mathematical verification or independent review"}
    write_json(DOSSIER/"verification_report.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="copy accepted inputs and run two clean two-pass builds")
    args = parser.parse_args()
    if args.build:
        build_package()
    verify_package()
