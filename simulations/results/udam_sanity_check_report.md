# UDAM sanity-check simulations

These are toy demonstrations, not empirical validation.

## 1. Timer re-anchor

Tested whether the unknown interval `U` remains uncertain while its relative influence declines as `R` grows.

| R | E_tau | sd_U | relative_uncertainty_sdU_over_Etau | P_tau_ge_T |
|---|---|---|---|---|
| 0.0 | 27.499698 | 4.329971 | 0.157455 | 0.00000 |
| 5.0 | 32.499698 | 4.329971 | 0.133231 | 0.00000 |
| 10.0 | 37.499698 | 4.329971 | 0.115467 | 0.00000 |
| 20.0 | 47.499698 | 4.329971 | 0.091158 | 0.00000 |
| 30.0 | 57.499698 | 4.329971 | 0.075304 | 0.33276 |
| 40.0 | 67.499698 | 4.329971 | 0.064148 | 1.00000 |
| 60.0 | 87.499698 | 4.329971 | 0.049486 | 1.00000 |

## 2. Observation value

Tested whether a state-informative signal can still fail to be favorable when observation cost is high.

| case | signal_accuracy | observation_cost | OV | interpretation |
|---|---|---|---|---|
| uninformative signal | 0.50 | 0 | 0.0 | state-informative condition fails; no decision gain |
| informative and cheap | 0.80 | 2 | 4.0 | state-informative and favorable |
| informative but too costly | 0.80 | 8 | -2.0 | state-informative but not favorable enough |

## 3. Expansion boundary risk

Tested whether a larger expansion factor can become unfavorable once boundary risk and correction cost are included.

| r_i | lhs_benefit_info | rhs_cost_risk | margin_lhs_minus_rhs | expand |
|---|---|---|---|---|
| 1.0 | 0.000000 | 2.300000 | -2.300000 | false |
| 1.2 | 2.552502 | 3.226293 | -0.673792 | false |
| 1.5 | 5.676512 | 5.038356 | 0.638155 | true |
| 2.0 | 9.704061 | 8.557337 | 1.146723 | true |
| 3.0 | 15.380572 | 16.219505 | -0.838933 | false |
| 4.0 | 19.408121 | 23.748475 | -4.340353 | false |
| 6.0 | 25.084633 | 37.152111 | -12.067479 | false |
| 8.0 | 29.112182 | 48.815890 | -19.703709 | false |

## Interpretation

- Timer: `R` does not erase `U`, but increasing `R` reduces `U`'s relative influence on `tau`.
- Observation: state-informative does not automatically mean favorable.
- Expansion: local success does not automatically justify large expansion.

## Boundary

This report supports only a narrow claim:

```text
the three toy models reproduce the expected qualitative UDAM behavior under the chosen assumptions
```

It does not show:

```text
empirical validation
general proof
clinical safety
superiority over existing decision theory
```
