from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import full_radius
from ringmin.patterns import supnick_min_tour
from ringmin.plots import draw_result
from ringmin.evaluator import chain_radius


def main() -> int:
    figures = ROOT / "figures"
    figures.mkdir(parents=True, exist_ok=True)

    ns: list[int] = []
    opt: list[float] = []
    worst: list[float] = []
    asymptote: list[float] = []
    certified_stop = 14
    for n in range(3, certified_stop + 1):
        payload = json.loads((ROOT / "results" / f"n{n:02d}" / "optimum.json").read_text(encoding="utf-8"))
        result = full_radius(tuple(payload["ordering"]), R_chain=payload["R_chain_float64"])
        draw_result(result, figures / f"n{n:02d}.png")
        ns.append(n)
        opt.append(float(payload["R_float64"]))
        worst.append(chain_radius(supnick_min_tour(range(1, n + 1))))
        asymptote.append(n * n / 8.0)
        print(f"wrote {figures / f'n{n:02d}.png'}")

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ns, opt, marker="o", label="certified R*")
    ax.plot(ns, worst, marker="s", label="Supnick MIN R_chain")
    ax.plot(ns, asymptote, linestyle="--", color="gray", label="n^2 / 8")
    ax.set_xlabel("n")
    ax.set_ylabel("radius")
    ax.set_title("Minimum central circle radius")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.savefig(figures / "radii_vs_n.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {figures / 'radii_vs_n.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
