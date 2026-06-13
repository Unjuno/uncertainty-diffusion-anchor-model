# Deterministic Event Scope

UDAM's timer seed model intentionally assumes a fixed or deterministic target event.

The model does **not** primarily ask:

```text
Will the event occur?
```

It asks:

```text
Where am I relative to an event assumed to occur at a fixed condition?
```

## Core distinction

There are two different uncertainties:

1. event occurrence uncertainty;
2. agent-position uncertainty.

UDAM's timer model focuses on the second.

## Fixed-event assumption

In the timer model, the target is treated as fixed:

```text
T = fixed upper time bound
```

The agent's uncertainty is about elapsed position:

```text
τ = K + U + R
```

not about whether `T` exists or whether the target condition will occur.

## Why this scope is intentional

If event occurrence itself becomes stochastic, the model must add another uncertainty layer:

```text
P(event occurs)
```

or a hazard function:

```text
h(t)
```

This would make the theory broader but weaker as a minimal timer-derived model.

UDAM intentionally avoids this expansion at the core level.

## Scope boundary

The core model assumes:

```text
event condition is fixed
agent position is uncertain
```

It does not assume:

```text
event occurrence is itself uncertain
```

## Relation to determinism

UDAM does not need to claim that all events in the universe are deterministic.

It only requires that, within the local model, the target condition is treated as fixed for analysis.

This is a modeling constraint, not a metaphysical claim.

## Correct reading

The correct timer interpretation is:

> Given that the target condition is fixed, how does losing and regaining an anchor affect the agent's uncertainty about current position?

The incorrect expanded interpretation is:

> What is the probability that the target event itself will occur?

That expansion is intentionally out of scope for the core theory.
