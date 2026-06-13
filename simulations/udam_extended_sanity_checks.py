"""UDAM extended toy sanity-check simulations.

These simulations are demonstrations, not empirical validation.

They extend the first-pass sanity-check layer with two additional toy checks:

1. Repeated-checking MOV_i: repeated observation should stop when marginal
   observation value becomes non-positive.
2. Boundary-risk sensitivity: favorable expansion factors should shrink or
   disappear as boundary-risk and correction-cost parameters increase.

Run from repository root:

    python simulations/udam_extended_sanity_checks.py

Outputs are written to simulations/results/.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable

RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: Iterable[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(fieldnames))
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    sep = "|" + "|".join(["---" for _ in columns]) + "|"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row[col]) for col in columns) + " |")
    return "\n".join([header, sep, *body])


def repeated_checking_mov_simulation() -> list[dict[str, object]]:
    """Toy diminishing-MOV_i check for repeated observation.

    The model intentionally uses simple deterministic parameters:
    expected information gain decays geometrically while observation cost
    rises mildly with each repeated check.

    This is a sanity check for the qualitative boundary:

        continue observing only while MOV_i > 0
    """

    base_information_gain = 6.0
    information_decay = 0.62
    base_observation_cost = 0.8
    cost_growth_per_check = 0.18

    rows: list[dict[str, object]] = []
    for i in range(1, 13):
        expected_information_gain = base_information_gain * (information_decay ** (i - 1))
        observation_cost = base_observation_cost + cost_growth_per_check * (i - 1)
        mov_i = expected_information_gain - observation_cost
        rows.append(
            {
                "i": i,
                "expected_information_gain": f"{expected_information_gain:.6f}",
                "observation_cost": f"{observation_cost:.6f}",
                "MOV_i": f"{mov_i:.6f}",
                "continue_observing": str(mov_i > 0).lower(),
            }
        )
    return rows


def boundary_risk_sensitivity_simulation() -> list[dict[str, object]]:
    """Toy sensitivity check for boundary-risk-constrained expansion.

    This varies two parameters in the existing expansion-boundary toy model:
    boundary-risk steepness and correction-cost multiplier.

    It checks whether favorable expansion factors shrink or disappear as the
    risk/correction regime becomes harsher.
    """

    r_values = [1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0]
    boundary_alpha_values = [0.08, 0.12, 0.18, 0.25, 0.35]
    correction_multipliers = [0.4, 0.8, 1.2]
    c_boundary = 20.0

    rows: list[dict[str, object]] = []
    for boundary_alpha in boundary_alpha_values:
        for correction_multiplier in correction_multipliers:
            favorable_r: list[float] = []
            margins: list[tuple[float, float]] = []
            for r in r_values:
                b_expand = 10 * math.log(r)
                i_expand = 4 * math.log(r)
                c_obs = 1.5 * r
                c_correct = correction_multiplier * (r**1.5)
                p_boundary = 1 - math.exp(-boundary_alpha * max(r - 1, 0) ** 1.4)
                lhs = b_expand + i_expand
                rhs = c_obs + p_boundary * c_boundary + c_correct
                margin = lhs - rhs
                margins.append((r, margin))
                if margin > 0:
                    favorable_r.append(r)

            best_margin_r, best_margin = max(margins, key=lambda item: item[1])
            rows.append(
                {
                    "boundary_alpha": f"{boundary_alpha:.2f}",
                    "correction_multiplier": f"{correction_multiplier:.1f}",
                    "max_favorable_r": "" if not favorable_r else f"{max(favorable_r):.1f}",
                    "best_margin_r": f"{best_margin_r:.1f}",
                    "best_margin": f"{best_margin:.6f}",
                    "any_favorable": str(bool(favorable_r)).lower(),
                }
            )
    return rows


def write_report(
    mov_rows: list[dict[str, object]],
    sensitivity_rows: list[dict[str, object]],
) -> None:
    report = RESULTS_DIR / "extended_sanity_check_report.md"

    report.write_text(
        "# UDAM extended toy sanity-check simulations\n\n"
        "These are toy demonstrations, not empirical validation.\n\n"
        "They extend the first-pass sanity-check layer with repeated-checking "
        "and boundary-risk sensitivity checks.\n\n"
        "## 1. Repeated-checking MOV_i\n\n"
        "Tested whether repeated observation stops being favorable when marginal "
        "information value decays below observation cost.\n\n"
        + markdown_table(
            mov_rows,
            ["i", "expected_information_gain", "observation_cost", "MOV_i", "continue_observing"],
        )
        + "\n\nInterpretation:\n\n"
        "- The first four repeated checks remain favorable under this toy parameterization.\n"
        "- From `i = 5`, `MOV_i <= 0`, so the current observation mode should stop or change.\n"
        "- This does not prove that every future observation is worthless.\n\n"
        "## 2. Boundary-risk sensitivity\n\n"
        "Tested whether favorable expansion factors shrink or disappear as boundary-risk "
        "steepness and correction-cost multiplier increase.\n\n"
        + markdown_table(
            sensitivity_rows,
            [
                "boundary_alpha",
                "correction_multiplier",
                "max_favorable_r",
                "best_margin_r",
                "best_margin",
                "any_favorable",
            ],
        )
        + "\n\nInterpretation:\n\n"
        "- Lower-risk settings allow larger favorable expansion factors.\n"
        "- Higher boundary-risk or correction-cost settings shrink the favorable expansion region.\n"
        "- Some harsh settings make every tested expansion factor unfavorable.\n"
        "- This is still a toy sensitivity check, not empirical validation.\n",
        encoding="utf-8",
    )


def main() -> None:
    mov_rows = repeated_checking_mov_simulation()
    sensitivity_rows = boundary_risk_sensitivity_simulation()

    write_csv(
        RESULTS_DIR / "repeated_checking_mov_summary.csv",
        mov_rows,
        ["i", "expected_information_gain", "observation_cost", "MOV_i", "continue_observing"],
    )
    write_csv(
        RESULTS_DIR / "boundary_risk_sensitivity_summary.csv",
        sensitivity_rows,
        [
            "boundary_alpha",
            "correction_multiplier",
            "max_favorable_r",
            "best_margin_r",
            "best_margin",
            "any_favorable",
        ],
    )
    write_report(mov_rows, sensitivity_rows)

    print("UDAM extended toy sanity-check simulations complete.")
    print(f"Results written to: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
