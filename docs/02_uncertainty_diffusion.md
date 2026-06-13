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
| `P_t` | uncertainty at time `t` | state unit squared | `P_t = Var(S_t | D_t)` in the variance formulation | `P_t >= 0` | variance / covariance |
| `Q` | uncertainty diffusion rate | state unit squared / s | rate at which uncertainty grows per unit time without anchors | `Q >= 0` | scalar / matrix |
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

## What is variance here?

In the minimal version, `P_t` is the variance-like quantity.

It means:

```text
P_t = Var(S_t | D_t)
```

So `P_t` is the amount of uncertainty the agent currently has about the state.

`Q` is different. `Q` is not the current uncertainty. It is the diffusion coefficient, or the growth rate of uncertainty over time.

The term:

```text
QΔt
```

is the added uncertainty during the unanchored interval.

So the model says:

```text
new uncertainty = old uncertainty + added uncertainty
```

or:

```text
P_{t+Δt} = P_t + QΔt
```

## Unit check

```text
[QΔt] = (state unit^2 / s) · s = state unit^2
```

So `P_t` and `QΔt` have the same unit. The equation is dimensionally valid.

## Timer-specific interpretation

If the state is elapsed time, then the state unit is seconds.

Therefore:

```text
[P_t] = s^2
[Q] = s^2 / s
[QΔt] = s^2
```

That means `P_t` is not elapsed time itself. It is uncertainty about elapsed time.

Example:

- estimated elapsed time: 40 s
- uncertainty variance: 25 s²
- standard deviation: 5 s

In this case, the agent's current estimate might be read as roughly:

```text
40 s ± 5 s
```

where `5 s` is the standard deviation, not the variance.

## Diffusion versus dilution

The timer model now has a separate three-layer interpretation:

```text
τ = K + U + R
```

In that timer-specific setting, adding `R` does not necessarily reduce the absolute variance of `U`.

Instead, it can dilute the relative influence of `U`:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

This is different from uncertainty diffusion.

- **Diffusion**: uncertainty grows during unanchored time.
- **Dilution**: a known interval grows around an already-localized unknown interval.

The two can coexist, but they are not the same claim.

## Interpretation

The model does not claim that every state diffuses equally. It says:

> In domains where the agent lacks anchoring observations, uncertainty about the current state may increase with time.

The diffusion equation is a minimal abstraction, not a universal law. Some domains may have nonlinear, bounded, or state-dependent uncertainty growth.

## Examples of diffusion

| Domain | State | Why uncertainty grows |
|---|---|---|
| timer | elapsed time | uncounted intervals accumulate before re-anchoring |
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
