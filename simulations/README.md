# Simulations

This directory contains small UDAM sanity-check simulations.

These simulations are demonstrations, not empirical validation.

They are intended to check whether minimal toy models reproduce the expected qualitative behavior of UDAM.

## Current simulation set

| File | Purpose |
|---|---|
| `udam_sanity_checks.py` | Reproducible script for the first three toy sanity checks |
| `udam_extended_sanity_checks.py` | Reproducible script for repeated-checking and boundary-risk sensitivity toy checks |
| `results/timer_reanchor_summary.csv` | Timer re-anchor summary results |
| `results/observation_value_examples.csv` | Three illustrative observation-value cases |
| `results/observation_value_grid.csv` | Full observation-value grid over signal accuracy and observation cost |
| `results/expansion_boundary_risk_summary.csv` | Expansion boundary-risk summary results |
| `results/repeated_checking_mov_summary.csv` | Repeated-checking marginal observation value toy results |
| `results/boundary_risk_sensitivity_summary.csv` | Boundary-risk sensitivity toy results |
| `results/udam_sanity_check_report.md` | Compact first-pass result report |
| `results/extended_sanity_check_report.md` | Compact extended result report |

## Five toy sanity checks

The current simulation layer checks:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
4. Repeated-checking MOV_i
5. Boundary-risk sensitivity
```

## Interpretation boundary

A passing sanity check means:

```text
the toy model reproduces the expected UDAM behavior under the chosen assumptions
```

It does not mean:

```text
UDAM is empirically validated
UDAM is proven in general
UDAM is superior to existing decision theory
UDAM is safe for high-stakes use
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

## Reproduction

Run the first-pass checks:

```bash
python simulations/udam_sanity_checks.py
```

Run the extended checks:

```bash
python simulations/udam_extended_sanity_checks.py
```

The scripts write CSV outputs to:

```text
simulations/results/
```

The scripts use deterministic toy parameters and a fixed random seed where randomness is used.
