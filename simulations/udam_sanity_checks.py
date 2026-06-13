"""UDAM first-pass sanity-check simulations.

These simulations are demonstrations, not empirical validation.

They test whether three minimal toy models reproduce expected qualitative UDAM behavior:

1. Timer re-anchor: increasing R reduces the relative influence of unknown U.
2. Observation value: state-informative does not automatically mean favorable.
3. Expansion boundary risk: larger expansion factors are not automatically better.

Run from repository root:

    python simulations/udam_sanity_checks.py

Outputs are written to simulations/results/.
"""

from __future__ import annotations

import csv
import math
import random
import statistics
from pathlib import Path
from typing import Iterable

RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
random.seed(SEED)


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


def timer_reanchor_simulation(n: int = 200_000) -> list[dict[str, object]]:
    """Simulate tau = K + U + R with U uncertain and R increasing."""
    k = 20.0
    u_values = [random.uniform(0.0, 15.0) for _ in range(n)]
    sd_u = statistics.stdev(u_values)
    r_values = [0.0, 5.0, 10.0, 20.0, 30.0, 40.0, 60.0]
    target_t = 60.0

    rows: list[dict[str, object]] = []
    for r in r_values:
        tau_values = [k + u + r for u in u_values]
        e_tau = statistics.mean(tau_values)
        rows.append(
            {
                "R": f"{r:.1f}",
                "E_tau": f"{e_tau:.6f}",
                "sd_U": f"{sd_u:.6f}",
                "relative_uncertainty_sdU_over_Etau": f"{sd_u / e_tau:.6f}",
                "P_tau_ge_T": f"{sum(tau >= target_t for tau in tau_values) / n:.5f}",
            }
        )
    return rows


def expected_value_without_observation(prior: float = 0.5) -> float:
    reward_correct = 10.0
    reward_wrong = -10.0
    v_action_1 = prior * reward_correct + (1 - prior) * reward_wrong
    v_action_0 = (1 - prior) * reward_correct + prior * reward_wrong
    return max(v_action_0, v_action_1)


def expected_value_with_observation(signal_accuracy: float, observation_cost: float) -> float:
    reward_correct = 10.0
    reward_wrong = -10.0
    decision_value = signal_accuracy * reward_correct + (1 - signal_accuracy) * reward_wrong
    return decision_value - observation_cost


def observation_value_simulation() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    base_value = expected_value_without_observation()
    accuracies = [0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.95]
    costs = [0, 1, 2, 4, 6, 8, 10]

    grid_rows: list[dict[str, object]] = []
    for acc in accuracies:
        for cost in costs:
            v_obs = expected_value_with_observation(acc, cost)
            ov = v_obs - base_value
            grid_rows.append(
                {
                    "signal_accuracy": f"{acc:.2f}",
                    "observation_cost": cost,
                    "V_no_obs": f"{base_value:.1f}",
                    "V_obs": f"{v_obs:.1f}",
                    "OV": f"{ov:.1f}",
                    "favorable": str(ov > 0).lower(),
                }
            )

    example_specs = [
        ("uninformative signal", 0.50, 0, "state-informative condition fails; no decision gain"),
        ("informative and cheap", 0.80, 2, "state-informative and favorable"),
        ("informative but too costly", 0.80, 8, "state-informative but not favorable enough"),
    ]
    example_rows: list[dict[str, object]] = []
    for name, acc, cost, interpretation in example_specs:
        ov = expected_value_with_observation(acc, cost) - base_value
        example_rows.append(
            {
                "case": name,
                "signal_accuracy": f"{acc:.2f}",
                "observation_cost": cost,
                "OV": f"{ov:.1f}",
                "interpretation": interpretation,
            }
        )
    return grid_rows, example_rows


def expansion_boundary_risk_simulation() -> list[dict[str, object]]:
    r_values = [1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0]
    c_boundary = 20.0
    rows: list[dict[str, object]] = []

    for r in r_values:
        b_expand = 10 * math.log(r)
        i_expand = 4 * math.log(r)
        c_obs = 1.5 * r
        c_correct = 0.8 * (r ** 1.5)
        p_boundary = 1 - math.exp(-0.18 * max(r - 1, 0) ** 1.4)
        lhs = b_expand + i_expand
        rhs = c_obs + p_boundary * c_boundary + c_correct
        margin = lhs - rhs
        rows.append(
            {
                "r_i": f"{r:.1f}",
                "B_expand": f"{b_expand:.6f}",
                "I_expand": f"{i_expand:.6f}",
                "lhs_benefit_info": f"{lhs:.6f}",
                "C_obs": f"{c_obs:.6f}",
                "P_boundary": f"{p_boundary:.6f}",
                "P_boundary_x_C_boundary": f"{p_boundary * c_boundary:.6f}",
                "C_correct": f"{c_correct:.6f}",
                "rhs_cost_risk": f"{rhs:.6f}",
                "margin_lhs_minus_rhs": f"{margin:.6f}",
                "expand": str(margin > 0).lower(),
            }
        )
    return rows


def write_report(
    timer_rows: list[dict[str, object]],
    obs_examples: list[dict[str, object]],
    expansion_rows: list[dict[str, object]],
) -> None:
    report = RESULTS_DIR / "udam_sanity_check_report.md"
    expansion_compact = [
        {
            "r_i": row["r_i"],
            "lhs_benefit_info": row["lhs_benefit_info"],
            "rhs_cost_risk": row["rhs_cost_risk"],
            "margin_lhs_minus_rhs": row["margin_lhs_minus_rhs"],
            "expand": row["expand"],
        }
        for row in expansion_rows
    ]

    report.write_text(
        "# UDAM sanity-check simulations\n\n"
        "These are toy demonstrations, not empirical validation.\n\n"
        "## 1. Timer re-anchor\n\n"
        "Tested whether the unknown interval `U` remains uncertain while its relative influence declines as `R` grows.\n\n"
        + markdown_table(
            timer_rows,
            ["R", "E_tau", "sd_U", "relative_uncertainty_sdU_over_Etau", "P_tau_ge_T"],
        )
        + "\n\n## 2. Observation value\n\n"
        "Tested whether a state-informative signal can still fail to be favorable when observation cost is high.\n\n"
        + markdown_table(
            obs_examples,
            ["case", "signal_accuracy", "observation_cost", "OV", "interpretation"],
        )
        + "\n\n## 3. Expansion boundary risk\n\n"
        "Tested whether a larger expansion factor can become unfavorable once boundary risk and correction cost are included.\n\n"
        + markdown_table(
            expansion_compact,
            ["r_i", "lhs_benefit_info", "rhs_cost_risk", "margin_lhs_minus_rhs", "expand"],
        )
        + "\n\n## Interpretation\n\n"
        "- Timer: `R` does not erase `U`, but increasing `R` reduces `U`'s relative influence on `tau`.\n"
        "- Observation: state-informative does not automatically mean favorable.\n"
        "- Expansion: local success does not automatically justify large expansion.\n",
        encoding="utf-8",
    )


def main() -> None:
    timer_rows = timer_reanchor_simulation()
    obs_grid, obs_examples = observation_value_simulation()
    expansion_rows = expansion_boundary_risk_simulation()

    write_csv(
        RESULTS_DIR / "timer_reanchor_summary.csv",
        timer_rows,
        ["R", "E_tau", "sd_U", "relative_uncertainty_sdU_over_Etau", "P_tau_ge_T"],
    )
    write_csv(
        RESULTS_DIR / "observation_value_grid.csv",
        obs_grid,
        ["signal_accuracy", "observation_cost", "V_no_obs", "V_obs", "OV", "favorable"],
    )
    write_csv(
        RESULTS_DIR / "observation_value_examples.csv",
        obs_examples,
        ["case", "signal_accuracy", "observation_cost", "OV", "interpretation"],
    )
    write_csv(
        RESULTS_DIR / "expansion_boundary_risk_summary.csv",
        expansion_rows,
        [
            "r_i",
            "B_expand",
            "I_expand",
            "lhs_benefit_info",
            "C_obs",
            "P_boundary",
            "P_boundary_x_C_boundary",
            "C_correct",
            "rhs_cost_risk",
            "margin_lhs_minus_rhs",
            "expand",
        ],
    )
    write_report(timer_rows, obs_examples, expansion_rows)

    print("UDAM sanity-check simulations complete.")
    print(f"Results written to: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
