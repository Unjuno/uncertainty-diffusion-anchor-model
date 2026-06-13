# Examples

This directory contains structured applications of the Uncertainty-Diffusion Anchor Model.

Each example should distinguish **state change** from **belief uncertainty**.

## Example types

| File | Type | Purpose |
|---|---|---|
| `learning_reanchor.md` | application | learning after interruption |
| `work_interruption.md` | application | project recovery after context loss |
| `relationship_uncertainty.md` | application | social uncertainty and low-pressure contact |
| `health_tracking.md` | application | limited health-state tracking |
| `life_strategy.md` | application | re-anchoring after model collapse |
| `missed_reanchor_miscalculation.md` | miscalculation | cases where UDAM applies but the agent fails to use it |
| `happy_miscalculation.md` | upside example | cases where observation reveals the state is better than expected |

## Template

```markdown
# Example: <Name>

## Situation

What is happening?

## Lost anchor

What reference point was lost?

## State variable

What is the latent state `S_t`?

## Belief uncertainty

What is the agent uncertain about?

```text
P_{domain,t} = Var(S_t | D_t)
```

## Possible state dynamics

How might the state itself change?

## Belief dynamics

How might uncertainty about the state change?

## Re-anchoring action

What small action returns information?

## Informational value

What does the action reveal?

```text
I(a) > 0
```

## Intervention value

Does the action also improve the state?

```text
B(a) >= 0
```

## Failure case

When does this stop being a good re-anchor?
```

## Miscalculation examples

Some examples are not normal applications, but **missed applications**.

A missed application occurs when:

```text
UDAM applies, but the agent fails to use it
```

The common pattern is:

```text
partial uncertainty → total invalidation
```

UDAM's correction is:

```text
partial uncertainty → re-anchor if the next action has positive value
```

## Happy miscalculation examples

Some examples describe upside hidden inside uncertainty.

The common pattern is:

```text
uncertainty feels negative → observation reveals a better state than expected
```

This is not blind optimism.

It is an observability effect:

```text
uncertainty may hide upside
observation can reveal it
```

The action is still justified only when:

```text
V(a) > 0
```

## High-stakes examples

High-stakes examples can be useful when they clarify:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

However, examples in this repository should remain abstract, non-operational, and neutral.

Use neutral wording such as:

- high-stakes fixed-deadline example;
- safety-critical fixed-target example;
- constrained decision context;
- upper time bound.

The goal is to preserve the model structure, not vivid scenario detail.

## Core distinction

UDAM does not require the external state to worsen during inaction.

It requires only that the agent's uncertainty about the state may increase without anchors.

```text
state dynamics ≠ belief dynamics
```
