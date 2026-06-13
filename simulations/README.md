# Simulations

This directory contains small UDAM sanity-check simulations.

These simulations are demonstrations, not empirical validation.

They are intended to check whether minimal toy models reproduce the expected qualitative behavior of UDAM.

## Current simulation set

| File | Purpose |
|---|---|
| `udam_sanity_checks.py` | Reproducible script for the first three toy sanity checks |
| `results/timer_reanchor_summary.csv` | Timer re-anchor summary results |
| `results/observation_value_examples.csv` | Three illustrative observation-value cases |
| `results/observation_value_grid.csv` | Full observation-value grid over signal accuracy and observation cost |
| `results/expansion_boundary_risk_summary.csv` | Expansion boundary-risk summary results |
| `results/udam_sanity_check_report.md` | Compact result report |

## Three first-pass sanity checks

The first simulation set checks:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
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

## Reproduction

Run:

```bash
python simulations/udam_sanity_checks.py
```

The script writes CSV outputs to:

```text
simulations/results/
```

The script uses deterministic toy parameters and a fixed random seed where randomness is used.
