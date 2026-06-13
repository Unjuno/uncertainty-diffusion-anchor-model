# Short Manifesto

Uncertainty does not wait.

When an anchor is lost, the unknown part can spread across the agent's belief about the current state.

The mistake is to think:

> I lost track once, so everything after that is meaningless.

The correction is:

> I lost one interval. I can still create a new anchor.

UDAM begins from a fixed-target timer structure:

```text
fixed target, uncertain position
```

The target is treated as fixed inside the model. The uncertainty is about position.

In timer form:

```text
τ = K + U + R
```

`U` remains uncertain.

`R` can still be valid.

A small informative action is not merely effort. It is measurement. It contacts the state again.

But not every action is good.

The rule is:

```text
V(a) = I(a) + B(a) - C(a)
```

Act only when:

```text
V(a) > 0
```

UDAM does not favor empty activity.

It favors low-cost actions that return information, improve the state, or clarify the next decision.

It also excludes uncertainty that action cannot affect. If a variable is external and uncontrollable, it belongs outside the core model or in a separate extension.

The practical error is:

```text
partial uncertainty → total invalidation
```

The practical correction is:

```text
partial uncertainty → re-anchor if the next action has positive value
```

First re-anchor.

Then optimize.
