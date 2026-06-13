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
| `P_t` | uncertainty | state unit squared | `P_t = Var(S_t | D_t)` | `P_t >= 0` | variance / covariance |
| `Q` | uncertainty diffusion rate | state unit squared / s | uncertainty growth rate without anchors | `Q >= 0` | scalar / matrix |
| `Δt` | unanchored elapsed time | s | elapsed time without anchoring observation | `Δt >= 0` | scalar |

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
