"""Matplotlib drawings for solved configurations."""

from __future__ import annotations

from pathlib import Path
import math

from ringmin.evaluator import FullResult


def draw_result(result: FullResult, path: str | Path, dpi: int = 180) -> None:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 8))
    central = plt.Circle((0, 0), result.R_full, fill=False, color="black", linewidth=2)
    ax.add_patch(central)
    floating = set(result.floating_radii)
    for radius, phi in zip(result.order, result.positions, strict=True):
        center_radius = result.R_full + radius
        x = center_radius * math.cos(phi)
        y = center_radius * math.sin(phi)
        color = "tab:orange" if radius in floating else "tab:blue"
        circle = plt.Circle((x, y), radius, fill=False, color=color, linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, f"{int(radius)}", ha="center", va="center", fontsize=10)
    limit = result.R_full + max(result.order) * 2.2
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")
    ax.axis("off")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
