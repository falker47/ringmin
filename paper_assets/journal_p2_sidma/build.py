"""Build the two SIDMA review PDFs with reciprocal references and SIAM BibTeX."""
import argparse
from hashlib import sha256
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile


HERE = Path(__file__).resolve().parent
DOCUMENTS = ("main", "supplement")
MACROS = "siamart_251216.zip"
MACROS_SHA256 = "9883890f66dbf64ff57bd94a207b51c5991fc8751d39b40ef6bf3484b3ea8b8f"
FIGURES = ("line_geometry.pdf", "finite_brackets.pdf")
UNRESOLVED = re.compile(
    r"undefined (?:references|citations)|(?:citation|reference) [^\n]*undefined"
    r"|multiply[- ]defined|label\(s\) may have changed|rerun to get"
    r"|no file [^\n]*\.(?:aux|bbl)|no file [^\n]*not imported"
    r"|package xr(?:-hyper)? warning",
    re.IGNORECASE,
)
OVERFULL = re.compile(r"Overfull \\[hv]box \(([\d.]+)pt [^\n]*")


def run(command, cwd):
    env = {**os.environ, "SOURCE_DATE_EPOCH": "1793664000", "FORCE_SOURCE_DATE": "1"}
    result = subprocess.run(command, cwd=cwd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    output = result.stdout.decode("utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(f"{' '.join(command)} exited {result.returncode}\n{output[-4500:]}")
    return output


def check_log(name, log):
    problems = [line for line in log.splitlines() if UNRESOLVED.search(line)]
    problems.extend(match[0] for match in OVERFULL.finditer(log) if float(match[1]) > 1)
    if problems:
        raise RuntimeError(f"{name}.log\n" + "\n".join(problems))
    pages = re.search(rf"Output written on {name}\.pdf \((\d+) pages?,", log)
    if not pages:
        raise RuntimeError(f"Missing PDF page count in {name}.log")
    return int(pages[1])


def build(output_dir):
    archive = HERE / MACROS
    if sha256(archive.read_bytes()).hexdigest() != MACROS_SHA256:
        raise ValueError(f"Unexpected SIAM distribution digest for {archive.name}")
    with tempfile.TemporaryDirectory(prefix="ringmin-sidma-") as directory:
        stage = Path(directory)
        with ZipFile(archive) as distribution:
            for name in ("siamart251216.cls", "siamplain.bst"):
                (stage / name).write_bytes(distribution.read(name))
        for name in ("main.tex", "supplement.tex", "shared.tex", "numbers.tex",
                     "references.bib", "supplement-references.bib"):
            shutil.copyfile(HERE / name, stage / name)
        shutil.copytree(HERE / "sections", stage / "sections")
        (stage / "figures").mkdir()
        for name in FIGURES:
            shutil.copyfile(HERE / "figures" / name, stage / "figures" / name)

        # Both first-pass aux files must exist before either document is finalized.
        for round_number in range(1, 4):
            for name in DOCUMENTS:
                run(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
                     "-halt-on-error", f"{name}.tex"], stage)
            if round_number == 1:
                for name in DOCUMENTS:
                    run(["bibtex", name], stage)
        pages = {name: check_log(name, (stage / f"{name}.log").read_text(encoding="latin1"))
                 for name in DOCUMENTS}
        output_dir.mkdir(parents=True, exist_ok=True)
        for name, count in pages.items():
            shutil.copyfile(stage / f"{name}.pdf", output_dir / f"{name}.pdf")
            print(f"{name}.pdf: {count} pages; 3 passes; final log clean (overfull limit 1 pt)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE)
    build(parser.parse_args().output_dir)
