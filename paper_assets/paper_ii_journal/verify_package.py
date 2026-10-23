"""Check candidate payload and reused lower-supplement hashes; no mathematical proof claim."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import json
import zipfile

HERE=Path(__file__).resolve().parent
def require(ok,message):
    if not ok:
        raise ValueError(message)
def digest(data):
    return sha256(data).hexdigest()
REQUIRED = {
    "main.tex", "main.pdf", "upper_supplement.tex", "upper_supplement.pdf",
    "BUILD_REPORT.json", "README.md", "READINESS.md", "CLAIM_PROOF_MAP.md",
    "PRIOR_ART.md", "EDITORIAL_REQUIREMENTS.md", "UPPER_DEPENDENCIES.md",
    "build.py", "verify_package.py", "check_reproducibility.py", ".gitattributes",
    "checks/check_line_recovery.py", "checks/check_word_lp.py", "verify_math.py",
    "checks/upper_lambda.py", "checks/upper_alpha_minimum.py", "checks/upper_boundary.py",
    "checks/upper_mixed_width.py", "checks/upper_fourth_block.py",
}
def validate_build_report(here, lower):
    require(all((here/name).is_file() for name in REQUIRED), "required candidate payload missing")
    report=json.loads((here/"BUILD_REPORT.json").read_text())
    require(set(report["documents"])=={"main","upper_supplement","lower"}, "incomplete build report")
    for name, record in report["documents"].items():
        source=lower/"supplement.tex" if name=="lower" else here/(name+".tex")
        pdf=lower/"supplement.pdf" if name=="lower" else here/(name+".pdf")
        require(digest(source.read_bytes())==record["source_sha256"], "stale build source: "+name)
        require(digest(pdf.read_bytes())==record["pdf_sha256"], "stale build PDF: "+name)
        require(record["passes"]>=3 and record["pages"]>0, "incomplete build: "+name)
        require(not record["unresolved_or_box_warnings"], "build warnings: "+name)
    lower_manifest=json.loads((lower/"MANIFEST.json").read_text())
    for name, expected in lower_manifest["outputs"].items():
        require(digest((lower/name).read_bytes())==expected,"lower payload hash: "+name)
def check_mapping(manifest, files):
    require(manifest["schema"]=="ringmin-paper-ii-journal-v1","schema")
    expected=manifest["outputs"]
    require(REQUIRED <= set(expected), "required manifest payload missing")
    require(set(expected)==set(files),"manifest file inventory mismatch")
    for name, data in files.items():
        path=PurePosixPath(name)
        require(not path.is_absolute() and ".." not in path.parts and "\\" not in name,"unsafe path")
        require(digest(data)==expected[name],"hash mismatch: "+name)
    return len(files)
def main():
    manifest=json.loads((HERE/"MANIFEST.json").read_text())
    files={p.relative_to(HERE).as_posix():p.read_bytes()
           for p in HERE.rglob("*") if p.is_file()
           and "__pycache__" not in p.parts and p.relative_to(HERE).as_posix()!="MANIFEST.json"}
    count=check_mapping(manifest,files)
    lower=HERE/"lower_supplement"
    if not lower.is_dir():
        lower=HERE.parent/"asymptotic_sequel/proposition7_supplement"
    require(digest((lower/"MANIFEST.json").read_bytes())==manifest["lower_supplement"]["manifest_sha256"],
            "reused lower supplement differs")
    validate_build_report(HERE, lower)
    archive=HERE/"source_bundle.zip"
    if archive.exists():
        with zipfile.ZipFile(archive) as source:
            require(len(source.namelist())==len(set(source.namelist())),"duplicate archive names")
            archived={name:source.read(name) for name in source.namelist()}
        inner=json.loads(archived.pop("MANIFEST.json"))
        check_mapping(inner,archived)
        expected_archive=set(files)-{"source_bundle.zip"}
        if not (HERE/"lower_supplement").is_dir():
            expected_archive |= {"lower_supplement/"+p.name for p in lower.iterdir() if p.is_file()}
        require(set(archived)==expected_archive, "archive inventory differs from complete current package")
        for name,data in archived.items():
            if not name.startswith("lower_supplement/"):
                require(files.get(name)==data,"archive/current mismatch: "+name)
            else:
                require((lower/name.removeprefix("lower_supplement/")).read_bytes()==data,"lower archive mismatch")
        print(f"PASS archive: {len(archived)} payload hashes; current-source and reused-supplement identity")
    print(f"PASS candidate manifest: {count} payload hashes; lower-supplement provenance")
if __name__=="__main__":
    main()
