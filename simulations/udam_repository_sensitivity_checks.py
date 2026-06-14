"""UDAM repository-facing toy sensitivity checks.

These simulations are demonstrations, not empirical validation.

This script adds one additional repository-facing sensitivity check:

1. Observation-cost threshold sensitivity: as signal accuracy improves, the
   maximum observation cost that can remain favorable should increase.

Run from repository root:

    python simulations/udam_repository_sensitivity_checks.py

Outputs are written to simulations/results/.
"""

from __future__ import annotations

import csv
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


def observation_cost_threshold_sensitivity() -> list[dict[str, object]]:
    """Toy threshold check for observation value.

    In the first-pass observation-value toy model:

        V_obs = accuracy * 10 + (1 - accuracy) * (-10) - cost

    With a symmetric prior, the no-observation baseline is 0. The strict
    favorable condition is:

        OV > 0

    So the break-even observation cost is:

        cost_threshold = 20 * accuracy - 10

    If the threshold is not positive, no non-negative observation cost is
    strictly favorable in this toy setup.
    """

    accuracies = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
    sample_costs = [0, 1, 2, 4, 6, 8, 10]

    rows: list[dict[str, object]] = []
    for accuracy in accuracies:
        threshold = 20 * accuracy - 10
        favorable_sample_costs = [cost for cost in sample_costs if threshold - cost > 0]
        rows.append(
            {
                "signal_accuracy": f"{accuracy:.2f}",
                "break_even_observation_cost": f"{threshold:.2f}",
                "strictly_favorable_nonnegative_cost_exists": str(threshold > 0).lower(),
                "favorable_sample_cost_count": len(favorable_sample_costs),
                "max_favorable_sample_cost": "" if not favorable_sample_costs else max(favorable_sample_costs),
            }
        )
    return rows


def write_report(rows: list[dict[str, object]]) -> None:
    report = RESULTS_DIR / "repository_sensitivity_check_report.md"
    report.write_text(
        "# UDAM repository-facing toy sensitivity checks\n\n"
        "These are toy demonstrations, not empirical validation.\n\n"
        "## 1. Observation-cost threshold sensitivity\n\n"
        "This check extends the observation-value toy model by varying signal accuracy "
        "and computing the break-even observation cost.\n\n"
        "Interpretation boundary: a higher threshold means a more accurate observation "
        "can tolerate a higher observation cost under this toy setup. It does not mean "
        "that more observation is always better.\n\n"
        + markdown_table(
            rows,
            [
                "signal_accuracy",
                "break_even_observation_cost",
                "strictly_favorable_nonnegative_cost_exists",
                "favorable_sample_cost_count",
                "max_favorable_sample_cost",
            ],
        )
        + "\n\n## Interpretation\n\n"
        "- At accuracy `0.50`, the signal has no positive break-even cost.\n"
        "- Higher signal accuracy raises the break-even observation cost in this toy setup.\n"
        "- This reinforces the existing guardrail: state-informative still must be favorable after cost.\n"
        "- This is a toy sensitivity check, not empirical validation.\n",
        encoding="utf-8",
    )


def main() -> None:
    rows = observation_cost_threshold_sensitivity()
    write_csv(
        RESULTS_DIR / "observation_cost_threshold_sensitivity.csv",
        rows,
        [
            "signal_accuracy",
            "break_even_observation_cost",
            "strictly_favorable_nonnegative_cost_exists",
            "favorable_sample_cost_count",
            "max_favorable_sample_cost",
        ],
    )
    write_report(rows)

    print("UDAM repository-facing sensitivity checks complete.")
    print(f"Results written to: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
