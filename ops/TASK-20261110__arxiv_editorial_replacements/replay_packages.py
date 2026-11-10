"""Compare both upload ZIPs and their PDFs to clean builds; run from any cwd.

PDF byte comparison is a reproduction check for the recorded TeX Live 2025
build environment, not an arXiv processing test or mathematical verifier.
"""
import hashlib
import io
import os
from pathlib import Path
import subprocess
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[2] / "paper_assets" / "arxiv_replacements"


def check(name, main):
    doc = ROOT / name
    sources = doc / "src"
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as z:
        files = (p for p in sources.rglob("*") if p.is_file())
        for path in sorted(files, key=lambda p: p.relative_to(sources).as_posix().lower()):
            info = zipfile.ZipInfo(path.relative_to(sources).as_posix(), (2026, 11, 10, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    upload = doc / (name + "_source.zip")
    if output.getvalue() != upload.read_bytes():
        raise ValueError(f"{upload.name}: ZIP bytes differ from rebuilt archive")
    env = os.environ.copy()
    if name == "paper_i":
        env.update(SOURCE_DATE_EPOCH="1794268800", FORCE_SOURCE_DATE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix=name + "-replay-") as tmp:
        with zipfile.ZipFile(upload) as z:
            z.extractall(tmp)
        for _ in range(3):
            subprocess.run(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
                            "-halt-on-error", "-file-line-error", main + ".tex"],
                           cwd=tmp, env=env, stdout=subprocess.DEVNULL, check=True)
        data = (Path(tmp) / (main + ".pdf")).read_bytes()
    if data != (doc / (name + ".pdf")).read_bytes():
        raise ValueError(f"{name}: compiled PDF differs (verify TeX/font environment)")
    print(f"{name}: ZIP and compiled PDF match; PDF sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    check("paper_i", "ringmin_dcg")
    check("paper_ii", "main")
