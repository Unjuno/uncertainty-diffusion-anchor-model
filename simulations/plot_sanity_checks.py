"""Generate repository-facing SVG plots for UDAM toy sanity checks.

These plots visualize toy demonstrations only. They are not empirical validation.

Run from repository root:

    python simulations/plot_sanity_checks.py

Outputs are written to simulations/plots/.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"
PLOTS_DIR = ROOT / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def scale(value: float, low: float, high: float, start: float, end: float) -> float:
    if high == low:
        return (start + end) / 2
    return start + (value - low) / (high - low) * (end - start)


def write_line_svg(
    path: Path,
    title: str,
    subtitle: str,
    x_label: str,
    y_label: str,
    points: list[tuple[float, float]],
    zero_line: bool = True,
) -> None:
    width, height = 900, 520
    left, right, top, bottom = 90, 40, 70, 80
    plot_w = width - left - right
    plot_h = height - top - bottom
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    if zero_line:
        y_min = min(y_min, 0)
        y_max = max(y_max, 0)
    pad = (y_max - y_min) * 0.08 if y_max > y_min else 1.0
    y_min -= pad
    y_max += pad

    def sx(x: float) -> float:
        return scale(x, x_min, x_max, left, left + plot_w)

    def sy(y: float) -> float:
        return scale(y, y_min, y_max, top + plot_h, top)

    point_text = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in points)
    circles = "\n".join(
        f'<circle cx="{sx(x):.2f}" cy="{sy(y):.2f}" r="4"><title>{x_label}: {x:g}, {y_label}: {y:g}</title></circle>'
        for x, y in points
    )
    y_ticks = []
    for i in range(6):
        y = y_min + (y_max - y_min) * i / 5
        py = sy(y)
        y_ticks.append(
            f'<line x1="{left - 5}" y1="{py:.2f}" x2="{width - right}" y2="{py:.2f}" class="grid"/>'
            f'<text x="{left - 10}" y="{py + 4:.2f}" class="tick" text-anchor="end">{y:.1f}</text>'
        )
    x_ticks = "\n".join(
        f'<text x="{sx(x):.2f}" y="{height - bottom + 25}" class="tick" text-anchor="middle">{x:g}</text>'
        for x in xs
    )
    zero = ""
    if zero_line and y_min < 0 < y_max:
        zy = sy(0)
        zero = f'<line x1="{left}" y1="{zy:.2f}" x2="{width - right}" y2="{zy:.2f}" class="zero"/>'

    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title>
<desc id="desc">{subtitle}</desc>
<style>
  text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #1f2937; }}
  .title {{ font-size: 24px; font-weight: 700; }}
  .subtitle {{ font-size: 14px; fill: #4b5563; }}
  .axis {{ stroke: #111827; stroke-width: 1.4; }}
  .grid {{ stroke: #e5e7eb; stroke-width: 1; }}
  .zero {{ stroke: #6b7280; stroke-width: 1.5; stroke-dasharray: 5 5; }}
  .series {{ fill: none; stroke: #2563eb; stroke-width: 3; }}
  circle {{ fill: #2563eb; }}
  .tick {{ font-size: 12px; fill: #4b5563; }}
  .label {{ font-size: 14px; font-weight: 600; fill: #374151; }}
</style>
<rect width="100%" height="100%" fill="#ffffff"/>
<text x="{left}" y="35" class="title">{title}</text>
<text x="{left}" y="56" class="subtitle">{subtitle}</text>
{''.join(y_ticks)}
<line x1="{left}" y1="{top}" x2="{left}" y2="{height - bottom}" class="axis"/>
<line x1="{left}" y1="{height - bottom}" x2="{width - right}" y2="{height - bottom}" class="axis"/>
{zero}
<polyline points="{point_text}" class="series"/>
{circles}
{x_ticks}
<text x="{left + plot_w / 2}" y="{height - 25}" class="label" text-anchor="middle">{x_label}</text>
<text x="24" y="{top + plot_h / 2}" class="label" transform="rotate(-90 24 {top + plot_h / 2})" text-anchor="middle">{y_label}</text>
</svg>
''',
        encoding="utf-8",
    )


def write_bar_svg(path: Path, title: str, subtitle: str, rows: list[tuple[str, float]]) -> None:
    width, height = 1000, 620
    left, right, top, bottom = 100, 40, 80, 130
    plot_w = width - left - right
    plot_h = height - top - bottom
    y_max = max(max(value for _, value in rows), 1.0) * 1.12
    gap = 6
    bar_w = max(6, (plot_w - gap * (len(rows) - 1)) / len(rows))

    def sy(y: float) -> float:
        return scale(y, 0, y_max, top + plot_h, top)

    y_ticks = []
    for i in range(6):
        y = y_max * i / 5
        py = sy(y)
        y_ticks.append(
            f'<line x1="{left - 5}" y1="{py:.2f}" x2="{width - right}" y2="{py:.2f}" class="grid"/>'
            f'<text x="{left - 10}" y="{py + 4:.2f}" class="tick" text-anchor="end">{y:.1f}</text>'
        )

    bars = []
    for i, (label, value) in enumerate(rows):
        x = left + i * (bar_w + gap)
        y = sy(value)
        h = height - bottom - y
        bars.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{bar_w:.2f}" height="{h:.2f}" rx="3"><title>{label}: {value:g}</title></rect>'
        )
        bars.append(
            f'<text x="{x + bar_w / 2:.2f}" y="{height - bottom + 18}" class="tick" text-anchor="end" transform="rotate(-55 {x + bar_w / 2:.2f} {height - bottom + 18})">{label}</text>'
        )

    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title>
<desc id="desc">{subtitle}</desc>
<style>
  text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #1f2937; }}
  .title {{ font-size: 24px; font-weight: 700; }}
  .subtitle {{ font-size: 14px; fill: #4b5563; }}
  .axis {{ stroke: #111827; stroke-width: 1.4; }}
  .grid {{ stroke: #e5e7eb; stroke-width: 1; }}
  rect {{ fill: #2563eb; }}
  .tick {{ font-size: 11px; fill: #4b5563; }}
  .label {{ font-size: 14px; font-weight: 600; fill: #374151; }}
</style>
<rect width="100%" height="100%" fill="#ffffff"/>
<text x="{left}" y="38" class="title">{title}</text>
<text x="{left}" y="60" class="subtitle">{subtitle}</text>
{''.join(y_ticks)}
<line x1="{left}" y1="{top}" x2="{left}" y2="{height - bottom}" class="axis"/>
<line x1="{left}" y1="{height - bottom}" x2="{width - right}" y2="{height - bottom}" class="axis"/>
{''.join(bars)}
<text x="{left + plot_w / 2}" y="{height - 25}" class="label" text-anchor="middle">Boundary alpha / correction multiplier</text>
<text x="28" y="{top + plot_h / 2}" class="label" transform="rotate(-90 28 {top + plot_h / 2})" text-anchor="middle">Max favorable r_i</text>
</svg>
''',
        encoding="utf-8",
    )


def main() -> None:
    mov_rows = read_csv(RESULTS_DIR / "repeated_checking_mov_summary.csv")
    boundary_rows = read_csv(RESULTS_DIR / "boundary_risk_sensitivity_summary.csv")
    threshold_rows = read_csv(RESULTS_DIR / "observation_cost_threshold_sensitivity.csv")

    write_line_svg(
        PLOTS_DIR / "repeated_checking_mov.svg",
        "Repeated-checking MOV_i",
        "Toy check: marginal observation value turns non-positive after repeated checks.",
        "Check index i",
        "MOV_i",
        [(float(row["i"]), float(row["MOV_i"])) for row in mov_rows],
    )
    write_bar_svg(
        PLOTS_DIR / "boundary_risk_sensitivity.svg",
        "Boundary-risk sensitivity",
        "Toy check: harsher boundary/correction settings shrink favorable expansion.",
        [
            (
                f"a{row['boundary_alpha']} / c{row['correction_multiplier']}",
                0.0 if row["max_favorable_r"] == "" else float(row["max_favorable_r"]),
            )
            for row in boundary_rows
        ],
    )
    write_line_svg(
        PLOTS_DIR / "observation_cost_threshold.svg",
        "Observation-cost threshold sensitivity",
        "Toy check: more accurate signals tolerate higher observation cost before OV stops being favorable.",
        "Signal accuracy",
        "Break-even observation cost",
        [
            (float(row["signal_accuracy"]), float(row["break_even_observation_cost"]))
            for row in threshold_rows
        ],
        zero_line=True,
    )

    print("UDAM plot generation complete.")
    print(f"Plots written to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
