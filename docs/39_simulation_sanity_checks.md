# 39 Simulation Sanity Checks

This document records the first UDAM toy-simulation sanity checks.

These simulations are demonstrations, not empirical validation.

They do not prove UDAM in general.

They only check whether minimal numerical models reproduce three expected qualitative behaviors.

## Location

Reproducible script:

```text
simulations/udam_sanity_checks.py
```

Result files:

```text
simulations/results/
```

Main result report:

```text
simulations/results/udam_sanity_check_report.md
```

## Why these three checks

The first simulation set covers three central UDAM boundaries:

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
```

Together, they check:

```text
partial uncertainty does not imply total invalidation
state-informative does not automatically mean favorable
local success does not automatically justify expansion
```

## Check 1: Timer re-anchor

Model:

```text
tau = K + U + R
```

Toy setting:

```text
K = 20
U ~ Uniform(0, 15)
R in {0, 5, 10, 20, 30, 40, 60}
```

Observed result:

```text
R increases -> sd(U) / E[tau] decreases
```

This supports the toy-demonstration version of:

```text
U remains uncertain, but R is still meaningful.
```

It does not show that absolute uncertainty in `U` disappears.

## Check 2: Observation value

Model:

```text
OV = V_obs - V_no_obs
```

Toy setting:

```text
binary hidden state S
binary observation y
correct action = +10
wrong action = -10
observation cost varies
```

Observed result:

```text
uninformative signal -> OV = 0
informative and cheap signal -> OV > 0
informative but costly signal -> OV < 0
```

This supports the toy-demonstration version of:

```text
state-informative != favorable
```

## Check 3: Expansion boundary risk

Model:

```text
B_expand(r_i) + I_expand(r_i)
>
C_obs(r_i) + P_boundary(i) C_boundary + C_correct(r_i)
```

Toy setting:

```text
r_i in {1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0}
benefit and information grow sublinearly
cost, correction cost, and boundary risk rise with scale
```

Observed result:

```text
r_i = 1.5 and r_i = 2.0 were favorable
larger r_i values became unfavorable
```

This supports the toy-demonstration version of:

```text
larger expansion is not automatically better
```

and:

```text
local success does not imply global expansion permission
```

## First-pass result

The first three sanity checks pass qualitatively.

Safe wording:

```text
UDAM's expected qualitative behavior appears in these three toy models under the chosen assumptions.
```

Avoid wording:

```text
UDAM is empirically validated.
UDAM is proven by simulation.
UDAM works generally.
UDAM is safe for high-stakes decisions.
```

## Repository role

These simulations belong to the demonstration layer.

They are below formal proof and below empirical validation.

They are useful for:

```text
checking intuition
catching obvious model inconsistencies
explaining expected behavior
creating later simulation baselines
```

They are not sufficient for:

```text
scientific validation
clinical application
policy application
financial decision support
```

## Next possible simulation work

Possible later work:

```text
add repeated-checking MOV_i simulation
add stochastic diffusion-and-reanchor time series
add sensitivity analysis for boundary-risk parameters
add plots or rendered figures if the simulation layer becomes public-facing
```
