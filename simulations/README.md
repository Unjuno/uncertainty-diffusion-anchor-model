# Simulations

This directory contains small UDAM sanity-check simulations.

These simulations are toy demonstrations, not empirical validation.

They are intended to check whether minimal toy models reproduce the expected qualitative pattern encoded by the repository assumptions.

## Current simulation set

| File | Purpose |
|---|---|
| `udam_sanity_checks.py` | Reproducible script for the first three toy sanity checks |
| `udam_extended_sanity_checks.py` | Reproducible script for repeated-checking and boundary-risk sensitivity toy checks |
| `udam_repository_sensitivity_checks.py` | Reproducible script for repository-facing observation-cost threshold sensitivity |
| `plot_sanity_checks.py` | Reproducible SVG plot generator for repository-facing simulation plots |
| `results/timer_reanchor_summary.csv` | Timer re-anchor summary results |
| `results/observation_value_examples.csv` | Three illustrative observation-value cases |
| `results/observation_value_grid.csv` | Full observation-value grid over signal accuracy and observation cost |
| `results/expansion_boundary_risk_summary.csv` | Expansion boundary-risk summary results |
| `results/repeated_checking_mov_summary.csv` | Repeated-checking marginal observation value toy results |
| `results/boundary_risk_sensitivity_summary.csv` | Boundary-risk sensitivity toy results |
| `results/observation_cost_threshold_sensitivity.csv` | Observation-cost threshold sensitivity toy results |
| `results/udam_sanity_check_report.md` | Compact first-pass result report |
| `results/extended_sanity_check_report.md` | Compact extended result report |
| `results/repository_sensitivity_check_report.md` | Compact repository-facing sensitivity report |
| `plots/repeated_checking_mov.svg` | Repository-facing plot for repeated-checking MOV_i |
| `plots/boundary_risk_sensitivity.svg` | Repository-facing plot for boundary-risk sensitivity |
| `plots/observation_cost_threshold.svg` | Repository-facing plot for observation-cost threshold sensitivity |

## Six toy sanity checks

The current simulation layer checks:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
4. Repeated-checking MOV_i
5. Boundary-risk sensitivity
6. Observation-cost threshold sensitivity
```

## Interpretation boundary

A passing sanity check means:

```text
the toy model reproduces the expected qualitative pattern under the chosen toy assumptions
```

It does not mean:

```text
empirical validation of UDAM
general proof of UDAM
superiority over existing decision theory
```

## Current first-pass result

The first three checks passed qualitatively:

```text
Timer: increasing R reduced the relative influence of unknown U.
Observation: state-informative did not automatically imply favorable.
Expansion: larger r_i was not automatically better once boundary risk and correction cost were included.
```

See:

- [`results/udam_sanity_check_report.md`](results/udam_sanity_check_report.md)
- [`../docs/39_simulation_sanity_checks.md`](../docs/39_simulation_sanity_checks.md)

## Current extended result

The two extended checks passed qualitatively:

```text
Repeated checking: MOV_i became non-positive after repeated observation under the toy assumptions.
Boundary-risk sensitivity: harsher boundary-risk and correction-cost settings reduced or eliminated favorable expansion factors.
```

See:

- [`results/extended_sanity_check_report.md`](results/extended_sanity_check_report.md)
- [`../docs/49_extended_simulation_sanity_checks.md`](../docs/49_extended_simulation_sanity_checks.md)

## Current repository-facing sensitivity result

The additional repository-facing sensitivity check passed qualitatively:

```text
Observation-cost threshold sensitivity: higher signal accuracy raised the break-even observation cost in the toy observation-value setup.
```

Interpretation boundary:

```text
This does not mean that more observation is always better.
It only visualizes the cost threshold implied by the toy observation-value setup.
```

See:

- [`results/repository_sensitivity_check_report.md`](results/repository_sensitivity_check_report.md)
- [`results/observation_cost_threshold_sensitivity.csv`](results/observation_cost_threshold_sensitivity.csv)

## Repository-facing plots

Plots are stored under:

```text
simulations/plots/
```

Current plots:

- [`plots/repeated_checking_mov.svg`](plots/repeated_checking_mov.svg)
- [`plots/boundary_risk_sensitivity.svg`](plots/boundary_risk_sensitivity.svg)
- [`plots/observation_cost_threshold.svg`](plots/observation_cost_threshold.svg)

These plots are generated from CSV outputs and are explanatory only.

## Reproduction

Run the first-pass checks:

```bash
python simulations/udam_sanity_checks.py
```

Run the extended checks:

```bash
python simulations/udam_extended_sanity_checks.py
```

Run the repository-facing sensitivity check:

```bash
python simulations/udam_repository_sensitivity_checks.py
```

Generate repository-facing SVG plots:

```bash
python simulations/plot_sanity_checks.py
```

The scripts write CSV outputs to:

```text
simulations/results/
```

The plot script writes SVG outputs to:

```text
simulations/plots/
```

The scripts use deterministic toy parameters and a fixed random seed where randomness is used.

## CI

The GitHub Actions workflow `.github/workflows/simulation-plots.yml` regenerates toy outputs and uploads SVG plots as a workflow artifact.
