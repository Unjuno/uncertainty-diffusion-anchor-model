# 02 Uncertainty Diffusion

## Core idea

Without an anchor, uncertainty about the current state does not merely remain fixed. It can grow over time.

This is the diffusion assumption.

## Variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `t` | time | s | external time | `t >= 0` | scalar |
| `S_t` | true state | state unit | latent current state | not directly observed | latent variable |
| `D_t` | observation history | context-dependent | observations up to time `t` | arbitrary | data |
| `P_t` | uncertainty | state unit squared | `P_t = Var(S_t | D_t)` | `P_t >= 0` | variance / covariance |
| `Q` | uncertainty diffusion rate | state unit squared / s | rate of uncertainty growth without anchors | `Q >= 0` | scalar / matrix |
| `Δt` | elapsed unanchored time | s | time without anchoring observation | `Δt >= 0` | scalar |

## Minimal diffusion equation

```text
P_{t+Δt} = P_t + QΔt
```

If:

```text
Q > 0
Δt > 0
```

then:

```text
P_{t+Δt} > P_t
```

## Unit check

```text
[QΔt] = (state unit^2 / s) · s = state unit^2
```

So `P_t` and `QΔt` have the same unit. The equation is dimensionally valid.

## Interpretation

The model does not claim that every state diffuses equally. It says:

> In domains where the agent lacks anchoring observations, uncertainty about the current state may increase with time.

## Examples of diffusion

| Domain | State | Why uncertainty grows |
|---|---|---|
| timer | elapsed time | uncounted intervals accumulate |
| learning | skill level | forgetting and unknown retention |
| work | project status | dependencies change while unattended |
| relationship | other person's attitude | unobserved reactions accumulate |
| health | body state | symptoms and recovery vary over time |

## Important distinction

Uncertainty diffusion is not always physical deterioration.

It may mean:

- the world changed;
- the agent's memory degraded;
- the agent lost track of dependencies;
- the state remained stable but the agent no longer knows it precisely.

## Failure condition

If `Q = 0`, uncertainty does not grow under inaction.

In that case, the urgency of re-anchoring is lower.
