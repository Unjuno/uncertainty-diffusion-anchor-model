# Observability Value

This file formalizes the value of making a state more observable.

It covers both:

```text
happy miscalculation
false comfort miscalculation
```

and explains fixed-target disbelief as an underweighting of re-anchoring value.

## 1. Latent state

Let the current latent state be:

```text
S ∈ {G, B}
```

where:

- `G` = favorable state;
- `B` = unfavorable state.

The agent has prior belief:

```text
p = P(S = G)
1 - p = P(S = B)
```

## 2. Action without observation

If the agent does not observe, they choose one action under the prior:

```text
a_0 ∈ A
```

The best no-observation value is:

```text
V_no_obs = max_a E[V(a, S)]
```

where:

```text
E[V(a, S)] = p V(a, G) + (1 - p) V(a, B)
```

## 3. Observation and posterior update

A re-anchoring action produces an observation:

```text
y
```

The observation updates the belief state:

```text
p_y = P(S = G | y)
```

After observing `y`, the agent can choose a state-conditioned action:

```text
a(y) ∈ A
```

The observation-conditioned value is:

```text
V_obs = E_y[max_a E[V(a, S) | y]] - C(obs)
```

The observation is favorable when:

```text
V_obs > V_no_obs
```

Equivalently:

```text
E_y[max_a E[V(a, S) | y]] - C(obs) > max_a E[V(a, S)]
```

## 4. Value of observability

Define observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Then observation is favorable when:

```text
OV > 0
```

Without observation cost and with ideal use of information:

```text
E_y[max_a E[V(a, S) | y]] >= max_a E[V(a, S)]
```

This is the basic reason observation has non-negative decision value under ideal assumptions.

## 5. Happy miscalculation

Happy miscalculation occurs when the agent's prior is pessimistic:

```text
p is low
```

but the observation reveals a favorable state:

```text
p_y > p
```

or, more strongly:

```text
p_y ≈ 1
```

The agent expected a poor state, but re-anchoring reveals upside.

Pattern:

```text
uncertainty feels negative → observation reveals upside
```

## 6. False comfort miscalculation

False comfort occurs when the agent's prior is overconfident:

```text
p is high
```

but the observation would reveal an unfavorable state:

```text
p_y < p
```

or, more strongly:

```text
p_y ≈ 0
```

The agent assumes the state is safe or favorable, skips observation, and leaves downside unmanaged.

Pattern:

```text
uncertainty feels manageable → no observation → hidden downside appears later
```

## 7. Fixed-target disbelief as value discounting

UDAM's timer seed model assumes a fixed target condition.

Inside the core model:

```text
π = 1
```

where `π` is the modeled occurrence or relevance weight of the target condition.

If the agent incorrectly treats the fixed target as unlikely or irrelevant, they may use:

```text
π_hat < 1
```

The perceived value of re-anchoring becomes:

```text
V_reanchor_perceived = π_hat · I_position(a) + B(a) - C(a)
```

while the model-relevant value is:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

If:

```text
V_reanchor_core > 0
```

but:

```text
V_reanchor_perceived <= 0
```

then the agent fails to re-anchor even though re-anchoring is favorable under the fixed-target model.

This is fixed-target disbelief.

## 8. Reverse action condition

The action is skipped when the agent uses the discounted value:

```text
π_hat · I_position(a) + B(a) <= C(a)
```

But the action would have been favored under the core model if:

```text
I_position(a) + B(a) > C(a)
```

Thus the error region is:

```text
π_hat · I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

This inequality captures the reverse effect:

> The target is fixed in the model, but the agent discounts it, so a positive re-anchor becomes subjectively unattractive.

## 9. Relation to UDAM

UDAM's basic action rule is:

```text
V(a) = I(a) + B(a) - C(a)
```

Observability value refines `I(a)`.

The information value of action is not merely uncertainty reduction.

It is the value of enabling better conditional action:

```text
I(a) ≈ E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)]
```

This explains why observation can help in both directions:

```text
upside revealed
hidden downside revealed
```

## 10. Boundary

This does not justify checking everything.

Observation is favorable only when:

```text
OV > 0
```

or equivalently when the value of improved conditional action exceeds observation cost.

If observation is expensive, misleading, repetitive, or non-actionable, it may not be justified.
