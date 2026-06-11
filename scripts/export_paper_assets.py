from __future__ import annotations

import csv
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import chain_radius, full_radius
from ringmin.patterns import supnick_min_tour
from ringmin.plots import draw_result

CERTIFIED_STOP = 14


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#")))


def latex_escape(value: object) -> str:
    return str(value).replace("_", r"\_")


def write_appendix(path: Path) -> None:
    highprec = read_csv(ROOT / "results" / "highprec.csv")
    patterns = read_csv(ROOT / "results" / "patterns_table.csv")
    lines = [
        r"\begin{table}",
        r"\centering",
        r"\begin{tabular}{rl}",
        r"\toprule",
        r"$n$ & $R^*$ \\",
        r"\midrule",
    ]
    for row in highprec:
        lines.append(f"{row['n']} & {row['R_mpmath_30']} \\\\")
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Certified optima, 30 significant digits.}",
        r"\end{table}",
        "",
        r"\begin{table}",
        r"\centering",
        r"\begin{tabular}{rlll}",
        r"\toprule",
        r"$n$ & Supnick min tour & $R_{\mathrm{chain}}$ & $R_{\mathrm{full}}$ \\",
        r"\midrule",
    ]
    for row in patterns:
        lines.append(
            f"{row['n']} & {latex_escape(row['worst_order'])} & "
            f"{row['worst_order_R_chain']} & {row['worst_order_R_full']} \\\\"
        )
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Worst-arrangement comparison; Supnick min tour values.}",
        r"\end{table}",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    assets = ROOT / "paper_assets"
    figures = assets / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    for n in range(3, CERTIFIED_STOP + 1):
        payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
        result = full_radius(tuple(payload["ordering"]), R_chain=payload["R_chain_float64"])
        draw_result(result, figures / f"n{n:02d}.png", dpi=300)

    heuristic_dir = ROOT / "results" / "heuristic"
    if heuristic_dir.exists():
        for path in sorted(heuristic_dir.glob("n*.json")):
            n = int(path.stem[1:])
            if n <= CERTIFIED_STOP:
                stale = figures / f"{path.stem}_heuristic.png"
                if stale.exists():
                    stale.unlink()
                continue
            payload = json.loads(path.read_text())
            result = full_radius(tuple(payload["ordering"]), R_chain=payload["R_chain"])
            draw_result(result, figures / f"{path.stem}_heuristic.png", dpi=300)

    import matplotlib.pyplot as plt

    ns: list[int] = []
    radii: list[float] = []
    labels: list[str] = []
    asymptote: list[float] = []
    worst: list[float] = []
    heuristic_rows: dict[int, dict[str, str]] = {}
    heuristic_path = ROOT / "results" / "heuristic_n14_18.csv"
    if heuristic_path.exists():
        for row in read_csv(heuristic_path):
            heuristic_rows[int(row["n"])] = row
    for n in range(3, 19):
        ns.append(n)
        if n <= CERTIFIED_STOP:
            payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text())
            radii.append(float(payload["R_float64"]))
            labels.append("certified")
        else:
            radii.append(float(heuristic_rows[n]["R_full"]))
            labels.append("heuristic")
        worst.append(chain_radius(supnick_min_tour(range(1, n + 1))))
        asymptote.append(n * n / 8.0)

    certified_points = [(n, radius) for n, radius, label in zip(ns, radii, labels, strict=True) if label == "certified"]
    heuristic_points = [(n, radius) for n, radius, label in zip(ns, radii, labels, strict=True) if label == "heuristic"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        [n for n, _ in certified_points],
        [radius for _, radius in certified_points],
        marker="o",
        label="certified R*",
    )
    ax.plot(
        [n for n, _ in heuristic_points],
        [radius for _, radius in heuristic_points],
        marker="o",
        linestyle="--",
        label="heuristic R",
    )
    ax.plot(ns, worst, marker="s", label="Supnick MIN R_chain")
    ax.plot(ns, asymptote, linestyle="--", color="gray", label="n^2 / 8")
    ax.set_xlabel("n")
    ax.set_ylabel("radius")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.savefig(figures / "radii_vs_n.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    for name in (
        "highprec.csv",
        "patterns_table.csv",
        "asymptotic_fit.csv",
        "heuristic_n14_18.csv",
        "heuristic_confidence_n16_18.csv",
        "free_float_criterion_n14_20.csv",
        "pocket_definition_audit_n14.json",
    ):
        source = ROOT / "results" / name
        if source.exists():
            shutil.copy2(source, assets / name)
    schema = ROOT / "results" / "heuristic" / "schema.json"
    if schema.exists():
        shutil.copy2(schema, assets / "heuristic_schema.json")
    write_appendix(assets / "appendix_tables.tex")
    print(f"wrote {assets}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
