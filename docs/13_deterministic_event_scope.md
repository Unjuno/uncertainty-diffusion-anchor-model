# 13 Deterministic Event Scope

UDAM's timer model deliberately assumes that the target condition is fixed.

This keeps the seed model narrow and strong.

## What the model does not ask

The timer model does not primarily ask:

```text
Will the event occur?
```

That would introduce event-occurrence uncertainty.

## What the model asks

The model asks:

```text
Given a fixed target condition, where is the agent relative to it?
```

The uncertainty is about position, not about whether the target exists.

## Minimal timer form

```text
τ = K + U + R
```

where:

- `K` is known;
- `U` is uncertain;
- `R` is known after re-anchoring;
- `τ` is current elapsed position.

The target condition is treated as fixed:

```text
T = fixed upper time bound
```

## Why not add stochastic event occurrence?

If the event itself is uncertain, then the model needs another layer:

```text
P(event occurs)
```

or:

```text
h(t)
```

This may be useful in another theory, but it weakens the minimal timer argument by mixing two uncertainties:

1. uncertainty about event occurrence;
2. uncertainty about agent position.

UDAM's core timer argument intentionally keeps only the second.

## Local determinism, not metaphysical determinism

The model does not need to claim that all reality is deterministic.

It only assumes local determinism or fixedness of the target condition inside the model.

In other words:

```text
fixed target, uncertain position
```

not:

```text
uncertain target, uncertain position
```

## Correct scope

The strongest version of the timer model is:

> The target condition is fixed. The agent loses track of position. Re-anchoring does not change the target, but it changes the agent's positional uncertainty relative to that target.

This scope should not be broadened unless the theory explicitly adds a separate event-occurrence layer.
