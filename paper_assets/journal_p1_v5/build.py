"""Compile the journal draft in an isolated directory and validate its PDF."""

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_build(destination):
    with tempfile.TemporaryDirectory(prefix="ringmin-journal-p1-") as name:
        work = Path(name)
        for source in HERE.glob("*.tex"):
            shutil.copyfile(source, work / source.name)
        shutil.copytree(HERE / "figures", work / "figures")
        env = dict(os.environ, SOURCE_DATE_EPOCH="0", FORCE_SOURCE_DATE="1")
        command = [
            "pdflatex",
            "-no-shell-escape",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            "main.tex",
        ]
        for index in range(1, 4):
            result = subprocess.run(
                command,
                cwd=work,
                env=env,
                stdin=subprocess.DEVNULL,
                capture_output=True,
            )
            if result.returncode:
                tail = result.stdout.decode("utf-8", "replace")[-4500:]
                raise RuntimeError(f"pdflatex pass {index} failed:\n{tail}")
        log = (work / "main.log").read_text(encoding="utf-8", errors="replace")
        bad = re.search(
            r"undefined (?:references|citations)|(?:Reference|Citation)\s+[^\n]*undefined"
            r"|Rerun to get cross-references right|File [^\n]* not found"
            r"|using draft setting|There were multiply-defined labels",
            log,
            re.IGNORECASE,
        )
        if bad:
            raise ValueError(f"unresolved final log: {bad.group()}")
        aux = (work / "main.aux").read_text(encoding="utf-8")
        label = re.search(r"\\newlabel\{app:seam\}\{\{[^{}]+\}\{(\d+)\}", aux)
        if not label:
            raise ValueError("appendix page is missing in the final auxiliary file")
        first_appendix = int(label[1])
        info = subprocess.run(
            ["pdfinfo", "main.pdf"],
            cwd=work,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdin=subprocess.DEVNULL,
            capture_output=True,
            check=True,
        ).stdout
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)[1])
        if not 2 <= first_appendix <= pages:
            raise ValueError("invalid appendix page")
        if not re.search(r"Page size:.*\(A4\)", info):
            raise ValueError("PDF does not have A4 pages")
        for warning in log.splitlines():
            if warning.startswith("Overfull "):
                print(warning)
        bad_boxes = log.count("Overfull \\")
        print(
            f"PDF pages={pages} before_appendices={first_appendix - 1} "
            f"appendix_starts={first_appendix} overfull_boxes={bad_boxes} "
            "pdflatex_passes=3 unresolved=0"
        )
        if first_appendix - 1 > 12:
            raise ValueError("main text including references exceeds twelve pages")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "main.pdf", destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "main.pdf")
    run_build(parser.parse_args().output.resolve())
