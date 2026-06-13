# Observability Proof Sketches

This file contains proof sketches for the observability-value propositions.

It supports:

- Proposition 8: observation can have non-negative decision value under ideal conditions;
- Proposition 9: observation is favorable when observability value is positive;
- Proposition 10: subjective target discounting can suppress a favorable re-anchor.

## Proof of Proposition 8

Let `Y` be the possible observation produced by a re-anchoring action.

Without observation, the best available expected value is:

```text
V_no_obs = max_a E[V(a, S)]
```

With observation, the agent first observes `Y = y`, updates the belief about `S`, and then chooses the best action conditional on `y`:

```text
E_y[max_a E[V(a, S) | y]]
```

Let `a*` be an action that maximizes the no-observation value:

```text
a* ∈ argmax_a E[V(a, S)]
```

For every observation `y`, the observation-conditioned policy can always choose `a*`.

Therefore:

```text
max_a E[V(a, S) | y] >= E[V(a*, S) | y]
```

Taking expectation over `y`:

```text
E_y[max_a E[V(a, S) | y]] >= E_y[E[V(a*, S) | y]]
```

By the law of total expectation:

```text
E_y[E[V(a*, S) | y]] = E[V(a*, S)]
```

Since `a*` maximizes no-observation value:

```text
E[V(a*, S)] = max_a E[V(a, S)]
```

Thus:

```text
E_y[max_a E[V(a, S) | y]] >= max_a E[V(a, S)]
```

This proves that observation has non-negative decision value under ideal use of information and zero observation cost.

## Proof of Proposition 9

Define observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable exactly when its net value exceeds the no-observation baseline:

```text
V_obs > V_no_obs
```

Substitute:

```text
E_y[max_a E[V(a, S) | y]] - C(obs) > max_a E[V(a, S)]
```

Rearrange:

```text
E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs) > 0
```

Therefore:

```text
OV > 0
```

Positive observability value is the condition under which observation is favorable.

## Proof of Proposition 10

In the core fixed-target model, the re-anchor value is:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

The action is favorable when:

```text
I_position(a) + B(a) > C(a)
```

If the agent discounts the fixed target with subjective weight `pi_hat < 1`, perceived value becomes:

```text
V_reanchor_perceived = pi_hat * I_position(a) + B(a) - C(a)
```

The agent skips the action when:

```text
pi_hat * I_position(a) + B(a) <= C(a)
```

Both conditions hold simultaneously when:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

This interval is non-empty when:

```text
pi_hat * I_position(a) + B(a) < I_position(a) + B(a)
```

which holds whenever:

```text
pi_hat < 1
I_position(a) > 0
```

Thus subjective discounting can make a favorable re-anchor appear unfavorable to the agent.

## Unit checks

For action value and observability value:

```text
[V(a)] = [I(a)] = [B(a)] = [C(a)] = [OV] = utility unit
```

For subjective relevance weight:

```text
[pi_hat] = 1
```

The observability equations are dimensionally consistent.
