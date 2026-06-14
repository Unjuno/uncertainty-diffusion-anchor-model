# Simulation plots

This directory contains repository-facing SVG plots generated from toy simulation CSV outputs.

These plots are explanatory artifacts only.

They are not empirical validation.

## Current plots

| Plot | Source data | Meaning |
|---|---|---|
| `repeated_checking_mov.svg` | `simulations/results/repeated_checking_mov_summary.csv` | Visualizes where repeated-checking `MOV_i` becomes non-positive |
| `boundary_risk_sensitivity.svg` | `simulations/results/boundary_risk_sensitivity_summary.csv` | Visualizes how harsher boundary/correction settings reduce favorable expansion |
| `observation_cost_threshold.svg` | `simulations/results/observation_cost_threshold_sensitivity.csv` | Visualizes how signal accuracy changes the break-even observation cost |

## Regeneration

Run from repository root:

```bash
python simulations/udam_sanity_checks.py
python simulations/udam_extended_sanity_checks.py
python simulations/udam_repository_sensitivity_checks.py
python simulations/plot_sanity_checks.py
```

The GitHub Actions workflow `.github/workflows/simulation-plots.yml` runs the same commands and uploads the generated plot directory as an artifact.

## Interpretation boundary

A plot passing visual sanity inspection means only:

```text
the selected toy assumptions produced the expected qualitative shape
```

It does not mean:

```text
UDAM is empirically validated
UDAM is proven in general
more observation is always better
larger expansion is always better
```
