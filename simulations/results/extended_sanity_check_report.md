# UDAM extended toy sanity-check simulations

These are toy demonstrations, not empirical validation.

They extend the first-pass sanity-check layer with repeated-checking and boundary-risk sensitivity checks.

## 1. Repeated-checking MOV_i

Tested whether repeated observation stops being favorable when marginal information value decays below observation cost.

| i | expected_information_gain | observation_cost | MOV_i | continue_observing |
|---|---|---|---|---|
| 1 | 6.000000 | 0.800000 | 5.200000 | true |
| 2 | 3.720000 | 0.980000 | 2.740000 | true |
| 3 | 2.306400 | 1.160000 | 1.146400 | true |
| 4 | 1.429968 | 1.340000 | 0.089968 | true |
| 5 | 0.886580 | 1.520000 | -0.633420 | false |
| 6 | 0.549680 | 1.700000 | -1.150320 | false |
| 7 | 0.340801 | 1.880000 | -1.539199 | false |
| 8 | 0.211297 | 2.060000 | -1.848703 | false |
| 9 | 0.131004 | 2.240000 | -2.108996 | false |
| 10 | 0.081223 | 2.420000 | -2.338777 | false |
| 11 | 0.050358 | 2.600000 | -2.549642 | false |
| 12 | 0.031222 | 2.780000 | -2.748778 | false |

Interpretation:

- The first four repeated checks remain favorable under this toy parameterization.
- From `i = 5`, `MOV_i <= 0`, so the current observation mode should stop or change.
- This does not prove that every future observation is worthless.

## 2. Boundary-risk sensitivity

Tested whether favorable expansion factors shrink or disappear as boundary-risk steepness and correction-cost multiplier increase.

| boundary_alpha | correction_multiplier | max_favorable_r | best_margin_r | best_margin | any_favorable |
|---|---|---|---|---|---|
| 0.08 | 0.4 | 4.0 | 3.0 | 4.995629 | true |
| 0.08 | 0.8 | 4.0 | 3.0 | 2.917168 | true |
| 0.08 | 1.2 | 3.0 | 2.0 | 1.772275 | true |
| 0.12 | 0.4 | 4.0 | 3.0 | 3.373361 | true |
| 0.12 | 0.8 | 3.0 | 2.0 | 2.179728 | true |
| 0.12 | 1.2 | 2.0 | 2.0 | 1.048357 | true |
| 0.18 | 0.4 | 3.0 | 2.0 | 2.278094 | true |
| 0.18 | 0.8 | 2.0 | 2.0 | 1.146723 | true |
| 0.18 | 1.2 | 2.0 | 2.0 | 0.015352 | true |
| 0.25 | 0.4 | 2.0 | 2.0 | 1.148705 | true |
| 0.25 | 0.8 | 2.0 | 1.5 | 0.149146 | true |
| 0.25 | 1.2 |  | 1.5 | -0.585701 | false |
| 0.35 | 0.4 | 1.5 | 1.5 | 0.207530 | true |
| 0.35 | 0.8 |  | 1.5 | -0.527317 | false |
| 0.35 | 1.2 |  | 1.5 | -1.262164 | false |

Interpretation:

- Lower-risk settings allow larger favorable expansion factors.
- Higher boundary-risk or correction-cost settings shrink the favorable expansion region.
- Some harsh settings make every tested expansion factor unfavorable.
- This is still a toy sensitivity check, not empirical validation.
