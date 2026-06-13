# Variables

This file fixes notation for the Uncertainty-Diffusion Anchor Model.

## Timer model variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `T` | fixed upper time bound | s | total duration, e.g. 60 s | `T > 0` | scalar |
| `K` | known counted interval | s | interval counted before losing the anchor | `K >= 0` | scalar |
| `U` | unknown interval | s | interval while the anchor was lost | `U >= 0` | random variable |
| `R` | re-anchored counted interval | s | interval counted after restarting | `R >= 0` | scalar or low-noise observation |
| `τ` | current elapsed time | s | `τ = K + U + R` | `τ >= 0` | random variable |
| `D` | observation history | context-dependent | remembered counts, records, observations | arbitrary | data |

## General state variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `t` | time | s | external time | `t >= 0` | scalar |
| `S_t` | true state | state unit | latent current state | directly unobserved | latent variable |
| `D_t` | observation history | context-dependent | observations up to time `t` | arbitrary | data |
| `P_t` | uncertainty at time `t` | state unit squared | `P_t = Var(S_t | D_t)` in the variance formulation | `P_t >= 0` | variance / covariance |
| `Q` | uncertainty diffusion rate | state unit squared / s | rate at which uncertainty grows per unit time without anchors | `Q >= 0` | scalar / matrix |
| `Q_total` | composite uncertainty diffusion rate | state unit squared / s | total positive diffusion rate from multiple sources | `Q_total >= 0` | scalar / matrix |
| `Q_state` | state-change diffusion component | state unit squared / s | uncertainty from latent state changes | `Q_state >= 0` | scalar / matrix |
| `Q_memory` | memory-decay diffusion component | state unit squared / s | uncertainty from memory or calibration decay | `Q_memory >= 0` | scalar / matrix |
| `Q_dependency` | dependency-change diffusion component | state unit squared / s | uncertainty from unobserved dependency changes | `Q_dependency >= 0` | scalar / matrix |
| `Q_context` | context-loss diffusion component | state unit squared / s | uncertainty from loss of task or decision context | `Q_context >= 0` | scalar / matrix |
| `Δt` | unanchored elapsed time | s | elapsed time without anchoring observation | `Δt >= 0` | scalar |

## Important distinction: `P_t` vs `Q`

`P_t` is the current amount of uncertainty.

`Q` is not the uncertainty itself. It is the coefficient or rate that determines how much uncertainty is added per unit time.

In the minimal diffusion equation:

```text
P_{t+Δt} = P_t + QΔt
```

- `P_t` is the current variance-like uncertainty.
- `QΔt` is the increase in uncertainty during the unanchored interval.
- `Q` has units of uncertainty per second.

So if `P_t` is measured in `state unit^2`, then `Q` is measured in `state unit^2 / s`.

In the timer case, if the state is elapsed time, then the state unit is seconds:

```text
[P_t] = s^2
[Q] = s^2 / s
[QΔt] = s^2
```

Because `s^2 / s` dimensionally simplifies to `s`, `Q` can look misleading in the timer case. Semantically, however, it should be read as:

```text
elapsed-time variance added per second
```

The model should be read as:

> uncertainty increases by `QΔt`, not that `Q` itself is the uncertainty.

## Diffusion-rate decomposition

A composite diffusion rate can be written as:

```text
Q_total = Q_state + Q_memory + Q_dependency + Q_context
```

A positive diffusion assumption is appropriate when:

```text
Q_total > 0
```

If all components are zero, then the diffusion argument weakens:

```text
Q_total = 0
```

## Action-value variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `a` | action | dimensionless | confirmation, measurement, work unit, message, test | chosen from available actions | decision variable |
| `I(a)` | informational value | utility unit | value from reducing uncertainty or enabling better conditional action | `I(a) >= 0` | scalar |
| `B(a)` | intervention value | utility unit | value from improving the state | real number | scalar |
| `C(a)` | action cost | utility unit | time, fatigue, money, risk, opportunity cost | `C(a) >= 0` | scalar |
| `V(a)` | total action value | utility unit | `V(a) = I(a) + B(a) - C(a)` | real number | scalar |
| `I_position(a)` | positional information value | utility unit | information value of re-anchoring position relative to a fixed target | `I_position(a) >= 0` | scalar |

## Observability variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `S` | latent state | state unit | current hidden state in observability model | finite or continuous | random variable |
| `G` | favorable state | state unit | state classified as favorable | member of state space | state label |
| `B_state` | unfavorable state | state unit | state classified as unfavorable | member of state space | state label |
| `y` | observation | observation unit | information returned by an observation or re-anchor | generated by observation process | random variable / data |
| `D_i` | information state before observation `i` | context-dependent | data available before repeated observation `i` | arbitrary | data |
| `C(obs)` | observation cost | utility unit | cost of making the state more observable | `C(obs) >= 0` | scalar |
| `C(obs_i)` | marginal observation cost | utility unit | cost of observation `i` | `C(obs_i) >= 0` | scalar |
| `OV` | observability value | utility unit | value from enabling better conditional action after observation | real number | scalar |
| `OV_i` | observability value after observation `i` | utility unit | value of observation sequence up to `i` | real number | scalar |
| `MOV_i` | marginal observability value | utility unit | additional value of observation `i` | real number | scalar |
| `I_i` | marginal informational value | utility unit | informational value of repeated action `i` | `I_i >= 0` | scalar |
| `B_i` | marginal intervention value | utility unit | intervention value of repeated action `i` | real number | scalar |
| `C_i` | marginal action cost | utility unit | cost of repeated action `i` | `C_i >= 0` | scalar |
| `pi_hat` | subjective target relevance weight | dimensionless | agent's subjective discount on fixed-target relevance | `0 <= pi_hat <= 1` | scalar |

## Observability equations

No-observation value:

```text
V_no_obs = max_a E[V(a, S)]
```

Observation-conditioned value:

```text
V_obs = E_y[max_a E[V(a, S) | y]] - C(obs)
```

Observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

Marginal observability value:

```text
MOV_i = E_y[max_a E[V(a,S) | y, D_i]] - max_a E[V(a,S) | D_i] - C(obs_i)
```

Repeated observation `i` is favorable only when:

```text
MOV_i > 0
```

Diminishing marginal information can be represented as:

```text
I_1 >= I_2 >= ... >= I_n >= 0
```

and repeated action `i` is unfavorable when:

```text
I_i + B_i <= C_i
```

Fixed-target discounting:

```text
V_reanchor_perceived = pi_hat * I_position(a) + B(a) - C(a)
```

Core fixed-target value:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

Error region:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

## Naming decision

The unknown interval is `U`, not `G`, to avoid collision with intervention value.

The favorable state is referred to as `G` only inside the observability model. If collision risk is high, use `S = favorable` instead.

The intervention value is `B(a)`, not `G(a)`, to avoid collision with the unknown interval.

The unfavorable state is written as `B_state`, not `B`, to avoid collision with intervention value `B(a)`.
