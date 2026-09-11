"""Preserve/check/restore exact historical frontier logs, without regeneration.

The archive is evidence copied from the original checkout. Hashes establish
byte identity, not search correctness; run the independent full verifier too.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import platform


REPO = Path(__file__).resolve().parents[1]
NUMBERS = tuple(range(3, 15))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def archive_name(n: int) -> str:
    return f"progress_n{n:02d}_lb3.log.gz"


def log_name(n: int) -> str:
    return f"progress_n{n:02d}_lb3.log"


def read_bundle(root: Path) -> list[tuple[Path, bytes]]:
    bundle = root / "reproducibility" / "frontier_logs"
    manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != 1 or [row.get("n") for row in manifest["logs"]] != list(NUMBERS):
        raise ValueError("unexpected frontier-log manifest schema or coverage")
    decoded = []
    for row in manifest["logs"]:
        n = row["n"]
        if row.get("archive") != archive_name(n) or row.get("target") != f"results/checkpoints/{log_name(n)}":
            raise ValueError("unexpected frontier-log path")
        compressed = (bundle / archive_name(n)).read_bytes()
        if digest(compressed) != row["archive_sha256"]:
            raise ValueError(f"archive hash mismatch n={n}")
        data = gzip.decompress(compressed)
        if len(data) != row["bytes"] or digest(data) != row["sha256"]:
            raise ValueError(f"restored log hash mismatch n={n}")
        target = root / "results" / "checkpoints" / log_name(n)
        if not target.resolve().is_relative_to(root.resolve()):
            raise ValueError("log target escapes root")
        decoded.append((target, data))
    return decoded


def restore(root: Path, check_only: bool = False) -> None:
    decoded = read_bundle(root)
    # Validate every existing target before writing any missing target.
    for target, data in decoded:
        if target.exists() and target.read_bytes() != data:
            raise ValueError(f"refusing to overwrite different existing log: {target.name}")
    if not check_only:
        for target, data in decoded:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                with target.open("xb") as stream:
                    stream.write(data)
            if target.read_bytes() != data:
                raise ValueError(f"restored readback mismatch: {target.name}")
    print(f"PASS {len(decoded)} exact log archives; {sum(len(data) for _, data in decoded)} original bytes; "
          + ("check only" if check_only else "restored/existing readback identical"))


def capture(root: Path, source_commit: str) -> None:
    if len(source_commit) != 40 or any(c not in "0123456789abcdef" for c in source_commit):
        raise ValueError("capture requires a full lowercase source commit SHA")
    bundle = root / "reproducibility" / "frontier_logs"
    rows, outputs = [], []
    for n in NUMBERS:
        data = (root / "results" / "checkpoints" / log_name(n)).read_bytes()
        compressed = gzip.compress(data, compresslevel=9, mtime=0)
        rows.append({"n": n, "archive": archive_name(n),
                     "target": f"results/checkpoints/{log_name(n)}",
                     "bytes": len(data), "sha256": digest(data),
                     "archive_sha256": digest(compressed)})
        outputs.append((bundle / archive_name(n), compressed))
    manifest = {"schema": 1, "source_checkout_commit": source_commit,
                "generator_sha256": digest(Path(__file__).read_bytes()),
                "provenance": "Exact locally preserved historical logs; not regenerated searches.",
                "compression": f"gzip level 9; mtime=0; {platform.python_implementation()} {platform.python_version()}",
                "logs": rows}
    outputs.append((bundle / "manifest.json", (json.dumps(manifest, indent=2)+"\n").encode()))
    for path, data in outputs:
        if path.exists() and path.read_bytes() != data:
            raise ValueError(f"refusing to replace existing archive evidence: {path.name}")
    bundle.mkdir(parents=True, exist_ok=True)
    for path, data in outputs:
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(data)
    print(f"PASS captured {len(rows)} original logs; {sum(len(data) for _, data in outputs)} archive bytes")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("restore", "check", "capture"))
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--source-commit", default="")
    args = parser.parse_args()
    if args.mode == "capture":
        capture(args.root.resolve(), args.source_commit)
    else:
        restore(args.root.resolve(), check_only=args.mode == "check")


if __name__ == "__main__":
    main()
