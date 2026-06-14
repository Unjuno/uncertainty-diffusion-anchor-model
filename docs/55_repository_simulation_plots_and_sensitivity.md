# 55 Repository Simulation Plots and Sensitivity

This document records the repository-facing simulation plot and additional toy sensitivity pass.

This document does not add new UDAM theory.

The simulation layer remains:

```text
toy demonstration / sanity check only
```

It is not empirical validation.

## Additions

Added files:

```text
simulations/udam_repository_sensitivity_checks.py
simulations/plot_sanity_checks.py
simulations/results/observation_cost_threshold_sensitivity.csv
simulations/results/repository_sensitivity_check_report.md
simulations/plots/README.md
simulations/plots/repeated_checking_mov.svg
simulations/plots/boundary_risk_sensitivity.svg
simulations/plots/observation_cost_threshold.svg
.github/workflows/simulation-plots.yml
```

Updated files:

```text
simulations/README.md
docs/ja/README.md
docs/ja/06_repository_status_and_simulations.md
```

## New toy sensitivity check

The added sensitivity check is:

```text
Observation-cost threshold sensitivity
```

Question:

```text
As signal accuracy improves, does the break-even observation cost increase in the toy observation-value setup?
```

Toy result:

```text
Higher signal accuracy raises the break-even observation cost.
```

Interpretation boundary:

```text
This does not mean that more observation is always better.
It means only that, in this toy setup, a more accurate signal can tolerate a higher observation cost before OV stops being favorable.
```

## Repository-facing plots

Current plots:

| Plot | Source data | Intended reading |
|---|---|---|
| `simulations/plots/repeated_checking_mov.svg` | `simulations/results/repeated_checking_mov_summary.csv` | `MOV_i` becomes non-positive after repeated checks under toy assumptions |
| `simulations/plots/boundary_risk_sensitivity.svg` | `simulations/results/boundary_risk_sensitivity_summary.csv` | harsher risk/correction settings shrink favorable expansion |
| `simulations/plots/observation_cost_threshold.svg` | `simulations/results/observation_cost_threshold_sensitivity.csv` | more accurate signals raise the break-even observation-cost threshold |

## CI

The workflow:

```text
.github/workflows/simulation-plots.yml
```

runs:

```bash
python simulations/udam_sanity_checks.py
python simulations/udam_extended_sanity_checks.py
python simulations/udam_repository_sensitivity_checks.py
python simulations/plot_sanity_checks.py
```

and uploads the generated SVG plots as an artifact.

## Current simulation layer

The current simulation layer now contains six toy checks:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
4. Repeated-checking MOV_i
5. Boundary-risk sensitivity
6. Observation-cost threshold sensitivity
```

## Guardrails

Do not write:

```text
simulation validates UDAM
simulation proves UDAM
more observation is always better
larger expansion is always better
```

Use:

```text
selected toy assumptions reproduce the expected qualitative shape
repository-facing plot
sanity check
toy demonstration
not empirical validation
```

## Result

Result:

```text
repository-facing simulation plot pass: complete
additional toy sensitivity check: complete
CI plot generation workflow: added
```
