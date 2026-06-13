# Controllability Boundary

UDAM should distinguish controllable or actionable uncertainty from uncontrollable exogenous uncertainty.

## Core principle

UDAM focuses on uncertainty that can be affected by re-anchoring actions.

A variable is inside the core model only if an action can do at least one of the following:

1. observe it more clearly;
2. constrain the belief state about it;
3. improve the state itself;
4. reveal the next viable action.

If none of these are possible, the variable should be treated as external or out of scope.

## Event occurrence as an external variable

In the timer seed model, event occurrence is treated as fixed.

If event occurrence is instead uncertain, then it becomes an external uncertainty layer:

```text
P(event occurs)
```

But this layer is not directly controlled by re-anchoring.

The agent can re-anchor their position relative to the target, but they may not control whether the target condition itself occurs.

## Why exclude it from the core model?

If uncontrollable occurrence uncertainty is included, it can dominate the action calculation.

For example:

```text
V_reanchor ≈ P(event occurs) · V_position_update - C(a)
```

If `P(event occurs)` is low or ambiguous, re-anchoring may appear unnecessary even when positional uncertainty is high.

This weakens the core argument.

## Correct boundary

UDAM core model:

```text
fixed target condition
uncertain agent position
action can re-anchor position
```

Out-of-scope or exception layer:

```text
uncertain target occurrence
agent cannot control occurrence
```

## Exception handling

Uncontrollable event uncertainty should be handled as one of the following:

1. excluded from the core model;
2. treated as an external parameter;
3. handled in a separate extension;
4. marked as an exception condition.

It should not be mixed into the core timer argument.

## Practical implication

The core question is not:

```text
Will the event occur?
```

The core question is:

```text
Given a fixed or externally determined target condition, what position am I in relative to it?
```

Re-anchoring is rational only where action can affect information, state, or decision quality.

## Relation to action value

The core action value remains:

```text
V(a) = I(a) + B(a) - C(a)
```

For uncontrollable external occurrence, a broader extension may introduce a parameter:

```text
π = P(event occurs)
```

and write:

```text
V(a) = π I_position(a) + B(a) - C(a)
```

But this is not part of the core UDAM model.
