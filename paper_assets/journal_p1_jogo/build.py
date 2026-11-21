"""Build the JOGO manuscript and optionally export its flat submission source."""

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
INPUTS = (
    "sn-jnl.cls", "sn-mathphys-num.bst", "references.bib",
    *(f"Fig{i}.pdf" for i in range(1, 7)),
)
UNRESOLVED = re.compile(
    r"(?:Reference|Citation)\s+[^\n]*undefined|undefined (?:references|citations)"
    r"|Rerun to get cross-references right|Citation\(s\) may have changed"
    r"|multiply.defined labels|File [^\n]*not found|using draft setting",
    re.IGNORECASE,
)
BOX = re.compile(r"^Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)", re.M)


def check_log(log):
    if warning := UNRESOLVED.search(log):
        raise ValueError(f"Unresolved final LaTeX log: {warning.group()}")
    boxes = list(BOX.finditer(log))
    if len(boxes) != len(re.findall(r"^Overfull ", log, re.M)):
        raise ValueError("Unrecognized overfull-box diagnostic in the final log")
    large = [log[m.start():].splitlines()[0] for m in boxes if float(m[1]) > 1]
    if large:
        raise ValueError("Final boxes above 1 pt:\n" + "\n".join(large))
    return max((float(m[1]) for m in boxes), default=0.0)


def run(command, work, env):
    result = subprocess.run(
        command, cwd=work, env=env, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        encoding="utf-8", errors="replace",
    )
    if result.returncode:
        raise RuntimeError(f"{command[0]} exited {result.returncode}:\n{result.stdout[-4000:]}")
    return result.stdout


def publish(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as folder:
        ready = Path(folder) / source.name
        shutil.copyfile(source, ready)
        ready.replace(destination)


def build(output, submission_zip=None):
    if submission_zip is not None and output.resolve() == submission_zip.resolve():
        raise ValueError("The PDF and submission ZIP need different destinations")
    with tempfile.TemporaryDirectory(prefix="ringmin-jogo-") as folder:
        work = Path(folder)
        for filename in INPUTS:
            shutil.copyfile(HERE / filename, work / filename)
        # Springer requests a single manuscript .tex. Keep numbers.tex editable
        # in the repository and compile exactly the source exported to the journal.
        source = (HERE / "main.tex").read_text(encoding="utf-8")
        marker = r"\input{numbers.tex}"
        if source.count(marker) != 1:
            raise ValueError("Expected one input of numbers.tex")
        numbers = (HERE / "numbers.tex").read_text(encoding="utf-8").rstrip()
        (work / "main.tex").write_text(source.replace(marker, numbers), encoding="utf-8", newline="\n")

        env = dict(os.environ, SOURCE_DATE_EPOCH="0", FORCE_SOURCE_DATE="1")
        latex = ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
                 "-halt-on-error", "-file-line-error", "main.tex"]
        run(latex, work, env)
        run(["bibtex", "main"], work, env)
        if "???" in (work / "main.bbl").read_text(encoding="utf-8"):
            raise ValueError("BibTeX inserted a placeholder for missing publication data")
        run(latex, work, env)
        run(latex, work, env)
        log = (work / "main.log").read_text(encoding="utf-8", errors="replace")
        maximum = check_log(log)
        info = run(["pdfinfo", "main.pdf"], work, env)
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
        publish(work / "main.pdf", output)
        if submission_zip is not None:
            archive = work / "submission.zip"
            with ZipFile(archive, "w") as package:
                for filename in ("main.tex", *INPUTS, "main.bbl", "main.pdf"):
                    entry = ZipInfo(filename, (1980, 1, 1, 0, 0, 0))
                    package.writestr(entry, (work / filename).read_bytes(), compress_type=ZIP_DEFLATED)
            publish(archive, submission_zip)
        print(f"PDF pages={pages} pdflatex_passes=3 bibtex_runs=1 unresolved=0 "
              f"max_overfull_pt={maximum:g} overfull_above_1pt=0")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "main.pdf")
    parser.add_argument("--submission-zip", type=Path, help="also write the flat upload package")
    args = parser.parse_args()
    build(args.output, args.submission_zip)
