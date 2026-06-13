# Variables

This file fixes notation for the Uncertainty-Diffusion Anchor Model.

## Timer model variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `T` | fixed deadline | s | total duration, e.g. 60 s | `T > 0` | scalar |
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

## Action-value variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `a` | action | dimensionless | confirmation, measurement, work unit, message, test | chosen from available actions | decision variable |
| `I(a)` | informational value | utility unit | value from reducing uncertainty | `I(a) >= 0` | scalar |
| `B(a)` | intervention value | utility unit | value from improving the state | real number | scalar |
| `C(a)` | action cost | utility unit | time, fatigue, money, danger, opportunity cost | `C(a) >= 0` | scalar |
| `V(a)` | total action value | utility unit | `V(a) = I(a) + B(a) - C(a)` | real number | scalar |

## Naming decision

The unknown interval is `U`, not `G`, to avoid collision with intervention value.

The intervention value is `B(a)`, not `G(a)`, to avoid collision with the unknown interval.
