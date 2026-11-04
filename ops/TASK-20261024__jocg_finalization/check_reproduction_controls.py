"""Task-local portable build and negative controls; no delivered file is changed."""
from pathlib import Path
from hashlib import sha256
import runpy
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "paper_assets/paper_ii_journal"


def run(directory, script, *args, failure=None):
    result = subprocess.run([sys.executable, "-I", "-S", str(directory / script), *args],
                            cwd=directory, capture_output=True, text=True)
    output = result.stdout + result.stderr
    if failure:
        if result.returncode == 0 or failure not in output:
            raise RuntimeError("Negative control did not reject as expected: " + output)
        print("PASS rejected", failure, flush=True)
    else:
        if result.returncode:
            raise RuntimeError(output)
        print(output.strip(), flush=True)


def main():
    with tempfile.TemporaryDirectory(prefix="ringmin-jocg-audit-") as temporary:
        outer = Path(temporary)
        package = outer / "package"
        with zipfile.ZipFile(PACKAGE / "source_bundle.zip") as archive:
            archive.extractall(package)
        run(package, "verify_package.py")
        before = {p.relative_to(package): sha256(p.read_bytes()).hexdigest()
                  for p in package.rglob("*") if p.is_file()}
        run(package, "check_reproducibility.py", "--require-delivered")
        after = {p.relative_to(package): sha256(p.read_bytes()).hexdigest()
                 for p in package.rglob("*") if p.is_file()}
        if before != after:
            raise RuntimeError("Portable check changed delivered bytes")
        print("PASS extracted standalone package and non-mutating builds", flush=True)
        pdf = package / "main.pdf"
        original = pdf.read_bytes()
        pdf.write_bytes(original + b"\n% corruption control\n")
        run(package, "check_reproducibility.py", "--require-delivered",
            failure="Rebuild differs from delivered PDF: main")
        run(package, "verify_package.py", failure="hash mismatch: main.pdf")
        pdf.write_bytes(original)
        checker = package / "check_reproducibility.py"
        saved = checker.read_bytes()
        checker.unlink()
        run(package, "verify_package.py", failure="manifest file inventory mismatch")
        checker.write_bytes(saved)
        builder = runpy.run_path(str(package / "build.py"))
        source = outer / "probe.tex"
        for suffix in (".tex", ".aux", ".out", ".toc"):
            foreign = outer / ("foreign" + suffix)
            foreign.write_text("\\relax\n", encoding="utf-8")
            source.write_text(
                "\\documentclass{article}\n\\begin{document}\n" +
                "\\input{" + foreign.as_posix() + "}Hello.\n\\end{document}\n",
                encoding="utf-8")
            try:
                builder["compile_document"](source)
            except RuntimeError as error:
                if "Input outside isolated build" not in str(error):
                    raise
            else:
                raise RuntimeError("Accepted undeclared input " + suffix)
            print("PASS rejected undeclared external input", suffix, flush=True)
        run(package, "verify_package.py")
    print("PASS portable reproduction and seven negative controls; delivered package untouched")


if __name__ == "__main__":
    main()
