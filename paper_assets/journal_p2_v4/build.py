"""Build the Paper II journal draft in isolation and check its final log."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def build(destination):
    with tempfile.TemporaryDirectory(prefix="ringmin-p2-v4-") as temp:
        staging = Path(temp)
        for filename in ("main.tex","numbers.tex"):
            shutil.copyfile(HERE/filename, staging/filename)
        (staging/"figures").mkdir()
        source = (staging/"main.tex").read_text(encoding="utf-8")
        for figure in re.findall(r"\\includegraphics(?:\[.*?\])?\{(figures/[^}]+\.pdf)\}", source):
            shutil.copyfile(HERE/figure, staging/figure)
        for index in range(1,4):
            result = subprocess.run(
                ["pdflatex","-interaction=nonstopmode","-halt-on-error","main.tex"],
                cwd=staging,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                env={**os.environ,"SOURCE_DATE_EPOCH":"1793664000","FORCE_SOURCE_DATE":"1"})
            if result.returncode:
                raise RuntimeError(result.stdout.decode("utf-8","replace")[-4500:])
        log = (staging/"main.log").read_text(encoding="latin1")
        problems = re.findall(r"(?:Citation|Reference) [^\n]* undefined|undefined (?:references|citations)|"
                              r"Label\(s\) may have changed|multiply[- ]defined|"
                              r"(?:File|file) [^\n]*(?:not found|does not exist)", log,re.I)
        if problems:
            raise RuntimeError("unresolved final TeX log: "+"; ".join(problems))
        pdf = staging/"main.pdf"
        info = subprocess.check_output(["pdfinfo",str(pdf)],text=True,encoding="utf-8",errors="replace")
        count = int(re.search(r"(?m)^Pages:\s+(\d+)",info)[1])
        # The last scientific paragraph precedes data availability and acknowledgments.
        aux = (staging/"main.aux").read_text(encoding="utf-8")
        marker = re.search(r"\\newlabel\{page:main-end\}\{\{[^}]*\}\{(\d+)\}", aux)
        if marker is None:
            raise RuntimeError("missing end-of-main-text page label")
        main_pages = int(marker[1])
        if not 1 <= main_pages <= count or main_pages > 14:
            raise RuntimeError(f"draft has {main_pages} main-text pages out of {count} total")
        destination.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=destination.parent,suffix=".pdf",delete=False) as f:
            tmp=Path(f.name)
        try:
            shutil.copyfile(pdf,tmp)
            os.replace(tmp,destination)
        finally:
            tmp.unlink(missing_ok=True)
        print(f"BUILD_PASS pages={count} main_pages={main_pages} passes=3 unresolved=0 overfull={log.count('Overfull')}")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=HERE/"main.pdf")
    build(parser.parse_args().output.resolve())
