# 12 State Versus Belief

UDAM is primarily a model of **belief uncertainty**, not necessarily physical deterioration.

This distinction is important.

## Two processes

There are two different processes that can occur during an unanchored interval.

### 1. State dynamics

The world or target state may change.

```text
S_t changes over time
```

Examples:

- a project receives new dependencies;
- health state changes;
- another person's attitude changes;
- memory decays;
- external conditions shift.

### 2. Belief dynamics

The agent's uncertainty about the state may change.

```text
P_t = Var(S_t | D_t)
```

Even if the physical state is stable, the agent may become less certain about it because their anchor is missing.

## Four cases

| Case | State changes? | Belief uncertainty changes? | Example |
|---|---:|---:|---|
| A | no | no | stable state, retained anchor |
| B | no | yes | state stable, but agent forgets or loses track |
| C | yes | no | state changes but agent has continuous observation |
| D | yes | yes | state changes while agent lacks an anchor |

UDAM mainly concerns cases B and D.

## Minimal belief uncertainty equation

```text
P_{t+Δt} = P_t + QΔt
```

This equation is about belief uncertainty, not necessarily physical deterioration.

## Why this matters

If this distinction is not made, the model can be misread as saying:

> The world always gets worse when I do nothing.

That is not the claim.

The claim is:

> Without anchors, the agent's uncertainty about the current state may increase.

## Relation to action

A re-anchoring action may do either or both of the following:

1. update belief about the state;
2. change the state itself.

This maps to the action-value terms:

```text
V(a) = I(a) + B(a) - C(a)
```

where:

- `I(a)` is belief-update value;
- `B(a)` is state-intervention value;
- `C(a)` is action cost.

## Correct interpretation

UDAM is strongest when it says:

> Small informative actions can be rational because they reconnect the agent's belief state with the current state.

It is weaker when interpreted as:

> Any action improves the world.

That interpretation is rejected.
