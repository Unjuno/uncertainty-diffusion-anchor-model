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

## Why stochastic occurrence weakens the advantage

If the target may not occur, the value of re-anchoring can be discounted by event occurrence uncertainty.

A simplified form is:

```text
V_reanchor ≈ P(event occurs) · V_position_update - C(a)
```

If `P(event occurs)` is low or undefined, then the advantage of positional re-anchoring becomes ambiguous.

This can produce a weak practical conclusion:

```text
maybe nothing needs to be done because maybe the target never occurs
```

The core timer model avoids this by assuming:

```text
fixed target, uncertain position
```

## Controllability boundary

There is a second reason to exclude event-occurrence uncertainty from the core model: controllability.

UDAM evaluates actions. Therefore, its core variables should be variables that action can affect through:

- observation;
- belief update;
- decision improvement;
- state intervention.

If the target condition's occurrence is external and uncontrollable, then including it inside the core action-value equation weakens the model.

The correct treatment is to classify it as:

- outside the core model;
- an external parameter;
- a separate extension;
- or an exception condition.

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

## Deferred extension

A stochastic occurrence extension is possible but deferred.

It would require at least:

```text
P(event occurs)
P(position | event occurs)
```

and the action value would become something like:

```text
V(a) = P(event occurs) · I_position(a) + B(a) - C(a)
```

This is outside the core model because it changes the source of the advantage and may introduce uncontrollable external uncertainty into an action-oriented model.

## Correct scope

The strongest version of the timer model is:

> The target condition is fixed. The agent loses track of position. Re-anchoring does not change the target, but it changes the agent's positional uncertainty relative to that target.

This scope should not be broadened unless the theory explicitly adds a separate event-occurrence layer.
