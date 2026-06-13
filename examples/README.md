# Examples

This directory contains structured applications of the Uncertainty-Diffusion Anchor Model.

Each example should distinguish **state change** from **belief uncertainty**.

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

## Core distinction

UDAM does not require the external state to worsen during inaction.

It requires only that the agent's uncertainty about the state may increase without anchors.

```text
state dynamics ≠ belief dynamics
```
