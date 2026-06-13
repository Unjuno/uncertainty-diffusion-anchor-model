# Diffusion Rate Conditions

This file defines when UDAM should assume a positive uncertainty diffusion rate.

The minimal diffusion equation is:

```text
P_{t+Δt} = P_t + QΔt
```

The key question is when:

```text
Q > 0
```

## Core interpretation

`Q` is the rate at which belief uncertainty increases when no anchor is available.

It is not a claim that the external world always worsens.

It is a claim that the agent's uncertainty about the relevant state can increase under non-observation.

## Minimal condition

A positive diffusion rate is appropriate when at least one of the following holds during an unanchored interval:

1. the state may change;
2. memory of the previous state may decay;
3. unobserved external dependencies may change;
4. the agent's internal model may become less calibrated;
5. the decision context may become less recoverable;
6. the cost of wrong action may become more sensitive to position error.

If none of these hold, then `Q` may be zero.

## Formal sufficient condition

Let `S_t` be the latent state and `D_t` the agent's observation history.

Uncertainty is:

```text
P_t = Var(S_t | D_t)
```

During an unanchored interval, `Q > 0` is appropriate when:

```text
Var(S_{t+Δt} | D_t) > Var(S_t | D_t)
```

or, more generally:

```text
U(p(S_{t+Δt} | D_t)) > U(p(S_t | D_t))
```

where `U` is an uncertainty functional.

## State-change component

If the state evolves as:

```text
S_{t+Δt} = S_t + w_t
```

with process noise:

```text
Var(w_t) = Q_state Δt
```

then uncertainty increases when:

```text
Q_state > 0
```

This is the standard state-dynamics source of diffusion.

## Memory-decay component

Even if the external state is stable, the agent's memory or calibration may degrade.

Let `M_t` be memory reliability.

If:

```text
M_{t+Δt} < M_t
```

then belief uncertainty may increase.

A simple form is:

```text
Q_memory > 0
```

## Dependency-change component

A project, relationship, health state, or environment may have hidden dependencies.

If unobserved dependencies can change during `Δt`, then:

```text
Q_dependency > 0
```

## Composite diffusion rate

A practical decomposition is:

```text
Q_total = Q_state + Q_memory + Q_dependency + Q_context
```

where:

- `Q_state` is uncertainty from latent state change;
- `Q_memory` is uncertainty from memory or calibration decay;
- `Q_dependency` is uncertainty from unobserved external dependencies;
- `Q_context` is uncertainty from loss of task or decision context.

The model assumes positive diffusion when:

```text
Q_total > 0
```

## Zero-diffusion case

`Q = 0` is appropriate when:

```text
state is stable
memory is stable
context is recoverable
external dependencies are fixed
position error does not become more costly
```

In such a case, the urgency of re-anchoring weakens.

UDAM may still support an action if it has intervention value, but the diffusion argument itself is weaker.

## Negative diffusion case

A negative effective diffusion rate may occur if uncertainty decreases without action.

For example:

```text
Q_effective < 0
```

when external information arrives automatically, the environment stabilizes, or uncertainty resolves without the agent's intervention.

This is outside the minimal diffusion assumption but should be treated as a boundary case.

## Relation to action value

When `Q > 0`, delay can increase the value of re-anchoring because the no-action trajectory becomes worse in belief-space.

A comparative condition is:

```text
P_after_action < P_no_action_trajectory
```

If `Q = 0`, re-anchoring must be justified by direct information value, observability value, or intervention value, rather than diffusion prevention.

## Correct statement

The precise claim is:

> UDAM assumes positive uncertainty diffusion only when unobserved time can make the agent's belief about the relevant state less reliable.

Not:

> Uncertainty always increases whenever time passes.
