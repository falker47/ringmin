#!/usr/bin/env python3
"""Negative controls for the four verifiers of this sprint.

Each control copies a tracked certificate, applies one deliberate defect and
runs the corresponding verifier in a subprocess.  A control passes only if
the verifier exits with a nonzero status and prints the expected reason.
The unmodified inputs must be accepted.  Nothing is written inside the
repository: all tampered files live in a temporary directory.

Usage (from research/fable_sprint_2026-11/):
    python -I controls/tamper_controls.py
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEAM_KMAX = 80


def run(script: Path, path: Path, *extra: str) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, "-I", str(script), str(path), *extra],
        capture_output=True,
        text=True,
        cwd=str(script.parent),
    )
    lines = [ln for ln in proc.stdout.strip().splitlines() if ln.strip()]
    return proc.returncode, (lines[-1] if lines else proc.stderr.strip()[-200:])


def main() -> None:
    failures = 0
    rows = []

    def expect(name, script, doc, needle, *extra, accept=False):
        nonlocal failures
        path = tmp / f"{name}.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        code, last = run(script, path, *extra)
        ok = (code == 0) if accept else (code != 0 and needle in last)
        failures += 0 if ok else 1
        rows.append((("ok  " if ok else "BAD "), name, script.name, code, last[:100]))

    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)

        # ---- seam certificate (restricted to k <= SEAM_KMAX) ----
        seam_full = json.loads((ROOT / "seam" / "seam_certificate.json").read_text(encoding="utf-8"))
        seam = dict(seam_full, kmax=SEAM_KMAX)
        seam["records"] = [r for r in seam_full["records"] if r[0] <= SEAM_KMAX]
        arb = ROOT / "seam" / "seam_verify.py"
        std = ROOT / "seam" / "seam_verify_stdlib.py"

        def find(doc, k, n):
            return next(r for r in doc["records"] if r[0] == k and r[1] == n)

        expect("seam_unmodified_arb", arb, seam, "", accept=True)
        expect("seam_unmodified_stdlib", std, seam, "", "12", accept=True)

        d = copy.deepcopy(seam)
        find(d, 7, 34)[4] = 1
        expect("seam_flip_sign", arb, d, "recorded sign is wrong")

        d = copy.deepcopy(seam)
        rec = find(d, 9, 41)
        lo = float(rec[2])
        rec[2], rec[3] = f"{lo * 1.001:.15e}", f"{lo * 1.002:.15e}"
        expect("seam_shift_bracket_arb", arb, d, "root not bracketed")
        expect("seam_shift_bracket_stdlib", std, d, "not proved", "12")

        d = copy.deepcopy(seam)
        rec = find(d, 5, 24)
        lo = float(rec[2])
        rec[2], rec[3] = f"{lo * 0.9:.15e}", f"{lo * 1.1:.15e}"
        expect("seam_wide_bracket_arb", arb, d, "not decided")
        expect("seam_wide_bracket_stdlib", std, d, "not proved", "12")

        d = copy.deepcopy(seam)
        d["records"] = [r for r in d["records"] if not (r[0] == 70 and r[1] == 286)]
        expect("seam_drop_onset_record", arb, d, "no unique certified sign change")

        d = copy.deepcopy(seam)
        d["records"] = [r for r in d["records"] if not (r[0] == 20 and r[1] == 120)]
        expect("seam_drop_window_record", arb, d, "window sign pattern broken")

        # ---- rounding certificates (first six instances) ----
        rnd_full = json.loads((ROOT / "rate" / "rounding_certificates.json").read_text(encoding="utf-8"))
        rnd = dict(rnd_full, instances=rnd_full["instances"][:6])
        rv = ROOT / "rate" / "rounding_verify.py"
        expect("rounding_unmodified", rv, rnd, "", accept=True)

        d = copy.deepcopy(rnd)
        coords = d["instances"][2]["coordinates"]
        for c in coords:  # shrink the placement by 1 percent
            c[0] *= 99
            c[1] *= 100
        expect("rounding_shrunk_placement", rv, d, "V1 placement P is infeasible")

        d = copy.deepcopy(rnd)
        d["instances"][4]["pieces"][0][2] += 1
        expect("rounding_extra_copy", rv, d, "V3 composition mismatch")

        d = copy.deepcopy(rnd)
        d["instances"][3]["pieces"][0][0] += 1
        expect("rounding_shifted_piece", rv, d, "V2 piece is not a dyadic sub-block")

        d = copy.deepcopy(rnd)
        inst = d["instances"][1]
        k = 2 ** inst["kappa"]
        # replace the selection by single points: right composition, too many pieces
        need = inst["T"] * 2 ** inst["rho"] // k
        first = {t: inst["sequence"].index(t) for t in range(1, k + 1)}
        inst["pieces"] = [[first[t], 1, need] for t in range(1, k + 1)]
        expect("rounding_single_points_only", rv, d, "V4 too many pieces")

        d = copy.deepcopy(rnd)
        seq = d["instances"][5]["sequence"]
        # relabel one small-type point as the largest type: P stays too tight
        idx = min(range(len(seq)), key=lambda i: seq[i])
        seq[idx] = max(seq)
        expect("rounding_relabelled_point", rv, d, "FAIL")

        # ---- rate table ----
        tab = json.loads((ROOT / "rate" / "rate_bound_table.json").read_text(encoding="utf-8"))
        tv = ROOT / "rate" / "rate_bound_verify.py"
        expect("rate_table_unmodified", tv, tab, "", "64", accept=True)

        d = copy.deepcopy(tab)
        d["rows"][3]["law_free"]["B"] = "1/1"
        expect("rate_table_lower_B", tv, d, "B mismatch", "64")

        d = copy.deepcopy(tab)
        d["rows"][5]["law_free"]["ratio_ceiling"] = "1.0000"
        expect("rate_table_low_ratio", tv, d, "ratio ceiling invalid", "64")

        d = copy.deepcopy(tab)
        d["rows"][2]["uniform"]["ring_error_ceiling"] = "0.001000000"
        expect("rate_table_low_ring_error", tv, d, "ring error ceiling invalid", "64")

        d = copy.deepcopy(tab)
        d["e_up"] = "44283/100000"
        expect("rate_table_e_up_too_small", tv, d, "E_UP does not exceed", "64")

    for row in rows:
        print(*row)
    if failures:
        print(f"CONTROLS FAILED: {failures}")
        sys.exit(1)
    print(f"ALL {len(rows)} CONTROLS BEHAVE AS EXPECTED")


if __name__ == "__main__":
    main()
