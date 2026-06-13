# Conditional Action Switch

This file records a key information-action structure in UDAM.

The useful pattern is:

```text
uncertain state -> informative observation -> conditional action switch
```

## State-informative observation

Let:

- `S` be the hidden state;
- `y` be the observation;
- `a_0` be the action before observation;
- `a(y)` be the action after observation.

An observation is useful when it is connected to the hidden state:

```text
P(y | S) != P(y)
```

Then the posterior can change:

```text
P(S | y) != P(S)
```

The action may also change:

```text
a(y) != a_0
```

## UDAM interpretation

UDAM should not say:

```text
observe anything
```

It should say:

```text
observe something that can change belief or action
```

## Timer seed model

In the timer model:

```text
tau = K + U + R
```

`R` is useful because it is connected to the elapsed-position estimate.

It is not arbitrary activity.

It is a valid re-anchor.

## Decision value

The observation-specific value is:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

## Practical test

Before observing, ask:

```text
What result would change my next action?
```

If no result changes belief or action, the observation is weak.

If different results lead to different actions, the observation is likely useful.

## Boundary

This separates valid re-anchoring from empty checking.

```text
valid re-anchor = state-informative observation
```

```text
weak check = observation that does not change belief or action
```
