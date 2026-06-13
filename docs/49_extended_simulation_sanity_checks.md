# 49 Extended Simulation Sanity Checks

This document records the first extended UDAM toy-simulation sanity checks.

These simulations are toy demonstrations, not empirical validation.

They do not prove UDAM in general.

They extend the first-pass simulation layer from `docs/39_simulation_sanity_checks.md`.

## Location

Reproducible script:

```text
simulations/udam_extended_sanity_checks.py
```

Result files:

```text
simulations/results/repeated_checking_mov_summary.csv
simulations/results/boundary_risk_sensitivity_summary.csv
simulations/results/extended_sanity_check_report.md
```

## Why these two checks

The first simulation set covered:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
```

This extension adds:

```text
4. Repeated-checking MOV_i
5. Boundary-risk sensitivity
```

Together, these check two additional guardrails:

```text
first useful observation does not justify indefinite repeated checking
boundary-risk parameters can shrink or eliminate favorable expansion factors
```

## Check 4: Repeated-checking MOV_i

Model:

```text
MOV_i = expected_information_gain_i - observation_cost_i
```

Toy setting:

```text
expected information gain decays geometrically
observation cost rises mildly with repeated checking
```

Observed result:

```text
i = 1 through 4: MOV_i > 0
i >= 5: MOV_i <= 0
```

This supports the toy-demonstration version of:

```text
Repeated checking should continue only while marginal observation value remains positive.
```

It does not show that every possible future observation is worthless after `MOV_i <= 0`.

The safe interpretation is:

```text
MOV_i <= 0 means stop or change the current observation mode.
```

## Check 5: Boundary-risk sensitivity

Model:

```text
B_expand(r_i) + I_expand(r_i)
>
C_obs(r_i) + P_boundary(i) C_boundary + C_correct(r_i)
```

Toy setting:

```text
boundary-risk steepness varies
correction-cost multiplier varies
r_i in {1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0}
```

Observed result:

```text
lower-risk settings allow larger favorable expansion factors
higher-risk settings shrink the favorable expansion region
some harsh settings make every tested expansion factor unfavorable
```

This supports the toy-demonstration version of:

```text
local success does not automatically justify large expansion
```

and:

```text
r_i is selected under boundary risk, not automatically doubled
```

## Interpretation boundary

A passing extended sanity check means:

```text
the toy model reproduces the expected UDAM qualitative behavior under chosen assumptions
```

It does not mean:

```text
UDAM is empirically validated
UDAM is proven in general
UDAM is safe for high-stakes use
UDAM gives an optimal expansion factor
```

## Current result

The two extended sanity checks pass qualitatively.

Safe wording:

```text
UDAM's expected qualitative behavior appears in these two additional toy models under the chosen assumptions.
```

Avoid wording:

```text
UDAM is confirmed by simulation.
UDAM has empirical support.
UDAM's checking and expansion rules are validated.
```

## Remaining simulation work

Possible later work:

```text
stochastic diffusion-and-reanchor time series
sensitivity analysis over observation-value parameters
plots or rendered figures if the simulation layer becomes public-facing
```
