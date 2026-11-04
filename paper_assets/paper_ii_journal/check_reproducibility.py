"""Rebuild each PDF twice without changing the delivered package (stdlib only)."""
from pathlib import Path
import argparse
import runpy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-delivered", action="store_true",
        help="Also require delivered bytes; needs the recorded TeX/font environment",
    )
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    builder = runpy.run_path(str(here / "build.py"))
    lower = builder["lower_dir"]()
    for name, source in (
        ("main", here / "main.tex"),
        ("upper_supplement", here / "upper_supplement.tex"),
        ("lower", lower / "supplement.tex"),
    ):
        first, record = builder["compile_document"](source)
        second, repeated = builder["compile_document"](source)
        if first != second or record != repeated:
            raise RuntimeError("Non-reproducible isolated build: " + name)
        matches = first == source.with_suffix(".pdf").read_bytes()
        if args.require_delivered and not matches:
            raise RuntimeError("Rebuild differs from delivered PDF: " + name)
        print(f"PASS reproducible {name}: {record['pages']} pages; "
              f"SHA256 {record['pdf_sha256']}; delivered_match={matches}", flush=True)
    print("PASS two isolated builds per document; delivered files unchanged")


if __name__ == "__main__":
    main()
