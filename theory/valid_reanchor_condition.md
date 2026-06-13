# Valid Re-Anchor Condition

This file defines when an action counts as a valid re-anchor in UDAM.

## Core point

A re-anchor is not arbitrary action.

An action is a valid re-anchor only when the observation it produces is informative about the relevant state.

## Timer seed model

In the timer model:

```text
tau = K + U + R
```

`R` is valid because it is part of the elapsed-position decomposition.

The lost interval `U` remains uncertain, but the restarted interval `R` is still informative.

So the timer case is not saying:

```text
any action after anchor loss is useful
```

It is saying:

```text
a later observation can remain valid if it is connected to the state being estimated
```

## State-informative observation

Let `S` be the relevant hidden state.

Let `y` be the observation returned by action `a`.

The observation is state-informative when:

```text
P(y | S) != P(y)
```

Equivalently, after observing `y`, the belief changes:

```text
P(S | y) != P(S)
```

In practical terms:

```text
the observation changes either belief or the next action
```

## Decision-informative observation

Even if the belief changes slightly, the observation is useful only when it can affect action choice enough to matter.

A practical test is:

```text
a(y) != a_0
```

where:

- `a_0` is the action chosen before observation;
- `a(y)` is the action chosen after observation.

Observation has decision value when it enables a better conditional action.

This is captured by:

```text
OV > 0
```

## Relation to Monty-Hall-type structure

The relevant similarity is not the surface story.

The shared structure is:

```text
uncertain state
informative observation
action switch after observation
```

An observation matters only if it is generated in a way that carries information about the hidden state.

If the observation is independent of the state, it should not change the action.

## Invalid re-anchor cases

An action is not a valid re-anchor when:

```text
P(y | S) = P(y)
```

or when:

```text
a(y) = a_0
```

and the observation has no other useful effect.

Examples of invalid or weak re-anchors:

- activity that does not reveal the state;
- repeated checking after the next action is already clear;
- observation that is too noisy to change belief;
- observation that is too costly relative to its value;
- observation that returns information unrelated to the current decision.

## Practical test

Before choosing a re-anchor, ask:

```text
What state is this observation connected to?
```

Then ask:

```text
What result would change my next action?
```

If no possible result changes belief or action, the observation is not a strong re-anchor.

## Correct statement

The precise statement is:

> Anchor loss does not invalidate future observations, provided that the future observations are informative about the relevant state.

For practical use:

```text
small action is not enough
small state-informative observation is required
```
