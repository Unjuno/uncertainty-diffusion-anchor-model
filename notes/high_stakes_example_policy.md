# High-Stakes Example Policy

Some origin examples used high-stakes or intense scenarios to make the timer seed model intuitive.

These examples can be meaningful because they expose the structure of the model clearly:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

However, the repository should handle them carefully.

## Why high-stakes examples can be useful

High-stakes examples make the following features visible:

1. the target condition is fixed inside the model;
2. the agent's position is uncertain;
3. ignoring uncertainty can be costly;
4. restarting measurement can still be meaningful;
5. partial uncertainty does not invalidate future anchors.

This can help readers understand why the model matters.

## What should be preserved

The useful structure is:

```text
fixed target, uncertain position
```

and:

```text
partial uncertainty does not imply total invalidation
```

The model does not need vivid or harmful details to preserve that structure.

## What should be avoided

The repository should avoid operational, graphic, or harmful descriptions.

Do not include details that could be read as instructions, encouragement, or scenario design.

Use neutral language such as:

- fixed target condition;
- upper time bound;
- high-stakes deadline;
- safety-critical setting;
- constrained decision context.

## Safe rewrite pattern

Instead of preserving a vivid scenario, rewrite it as:

```text
An agent faces a fixed upper time bound, loses track of position, and then re-anchors by taking a valid observation.
```

This keeps the mathematical structure while removing unnecessary harmful detail.

## Why this matters for readers

For some readers, a high-stakes framing can make the practical implication clear:

> Even after losing track, restarting from the current point can still improve orientation.

That can be constructive when framed as cognition, measurement, and recovery rather than harm.

## Boundary

High-stakes examples in UDAM are not advice about dangerous situations.

They are abstract illustrations of:

```text
position uncertainty under a fixed target condition
```

and should remain non-operational.

## Recommended public wording

Use:

> high-stakes fixed-deadline example

or:

> safety-critical fixed-target example

Avoid vivid scenario details unless strictly necessary for theoretical clarity.
