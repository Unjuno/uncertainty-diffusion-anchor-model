# Propositions

## Proposition 1: Lost intervals do not invalidate future anchors

If:

```text
τ = K + U + R
```

and `K` and `R` are observed while `U` is uncertain, then `R` still contributes valid information about `τ`.

### Meaning

The uncertainty of `U` does not make `R` meaningless.

## Proposition 2: Uncertainty increases under no-anchor conditions

If:

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q > 0
Δt > 0
```

then:

```text
P_{t+Δt} > P_t
```

### Meaning

When uncertainty diffuses and no anchor is available, inaction is not neutral.

## Proposition 3: Informative low-cost actions can dominate inaction

If:

```text
V(a) = I(a) + B(a) - C(a) > 0
```

then action `a` is favorable under the model.

### Meaning

Small informative actions can be rational even after prior measurement failure.

## Proposition 4: Frequent small re-anchoring actions can constrain uncertainty diffusion

If a sequence of actions `a_1, a_2, ..., a_n` repeatedly provides positive informational value at low cost, then it can prevent uncertainty from growing unchecked.

### Meaning

The strategic advantage is not arbitrary hyperactivity. It is high-frequency low-cost re-anchoring.

## Proposition 5: Empty activity is unfavorable

If:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

then:

```text
V(a) < 0
```

### Meaning

The model does not justify action without informational or intervention value.

## Proposition 6: Timer re-anchoring can dilute relative uncertainty

In the timer model:

```text
τ = K + U + R
```

assume `K` and `R` are observed, while `U` has uncertainty.

Define relative uncertainty ratio:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

If the uncertainty scale `sqrt(Var(U))` grows more slowly than the expected elapsed time `E[τ]`, then increasing `R` decreases `ρ(R)`.

### Meaning

Timer re-anchoring does not necessarily reduce the absolute variance of the unknown interval `U`. Absolute uncertainty may remain or even increase. The key claim is that the relative influence of `U` can decrease when the known interval `R` expands the total reference scale faster than the uncertainty scale grows.

## Proposition 7: Fixed upper-bound non-arrival can tighten the unknown interval

If a fixed upper time bound `T` exists and the bound has not yet been reached, then:

```text
K + U + R < T
```

which implies:

```text
U < T - K - R
```

### Meaning

In fixed-bound cases, increasing `R` while the bound is still unreached can shrink the admissible range of `U`. This is stronger than relative dilution.

## Proposition 8: Observation can have non-negative decision value under ideal conditions

Let `S` be a latent state and `y` an observation produced by a re-anchoring action.

Without observation:

```text
V_no_obs = max_a E[V(a, S)]
```

With observation:

```text
V_obs = E_y[max_a E[V(a, S) | y]] - C(obs)
```

If observation cost is zero and the agent uses the observation optimally, then:

```text
E_y[max_a E[V(a, S) | y]] >= max_a E[V(a, S)]
```

### Meaning

Observation can help because it enables conditional action. It can reveal both hidden upside and hidden downside.

## Proposition 9: Observation is favorable when observability value is positive

Define:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

If:

```text
OV > 0
```

then the observation or re-anchoring action is favorable.

### Meaning

Observation is not automatically good. It is good only when improved conditional action exceeds observation cost.

## Proposition 10: Fixed-target disbelief can suppress a favorable re-anchor

In the fixed-target core model, suppose the re-anchor value is:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

If the agent discounts the fixed target by a subjective relevance weight `π_hat < 1`, perceived value becomes:

```text
V_reanchor_perceived = π_hat · I_position(a) + B(a) - C(a)
```

The agent fails to re-anchor despite positive core value when:

```text
π_hat · I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

### Meaning

This captures fixed-target disbelief: the target is fixed in the model, but the agent discounts it, so a positive re-anchor becomes subjectively unattractive.

## Proposition 11: A valid re-anchor must be state-informative

Let `S` be the relevant hidden state and `y` the observation produced by action `a`.

A re-anchor is valid only if the observation is connected to the state:

```text
P(y | S) != P(y)
```

Equivalently, the observation can change the posterior:

```text
P(S | y) != P(S)
```

### Meaning

A small action is not enough. A valid re-anchor must return information about the state being estimated. The timer `R` is valid because it is part of the elapsed-position decomposition.

## Proposition 12: A useful observation can justify a conditional action switch

Let `a_0` be the action chosen before observation and `a(y)` the action chosen after observing `y`.

A useful observation can support a conditional switch when:

```text
a(y) != a_0
```

for at least one possible observation result.

The decision-theoretic value is captured by:

```text
OV > 0
```

### Meaning

This is the Monty-Hall-type structure inside UDAM: observation is valuable when it is state-informative and can rationally change the next action.

## Proposition 13: Expansion factor is constrained by adverse boundary risk

Let the current action or observation scope be:

```text
s_i
```

and the next scope be:

```text
s_{i+1} = r_i s_i
```

A larger expansion factor is favorable only if:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

### Meaning

Geometric expansion can reduce search energy, but the expansion factor is constrained by the probability and cost of crossing a relevant adverse boundary before the next observation.

A default doubling pattern can be useful:

```text
1 -> 2 -> 4 -> 8
```

but it is not universally optimal. The factor depends on observation cost, correction cost, state volatility, reversibility, and adverse boundary risk.
