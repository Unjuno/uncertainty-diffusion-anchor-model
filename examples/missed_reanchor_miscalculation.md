# Example: Missed Re-Anchor Miscalculation

This document describes cases where UDAM applies, but the agent fails to use it.

These are not failures of the model.

They are miscalculations by the agent.

## Core pattern

The agent assumes:

```text
previous anchor failed → whole process is invalid
```

But UDAM says:

```text
previous anchor failed → lost interval is uncertain
future anchors can still be valid
```

In timer form:

```text
τ = K + U + R
```

The agent incorrectly treats `U` as invalidating `R`.

The correct interpretation is that `U` remains uncertain, while `R` can still provide valid positional information.

## Miscalculation 1: All-or-nothing measurement

### Situation

A person tracks a process, misses part of it, and concludes that all later tracking is worthless.

### Mistake

They treat partial measurement failure as total measurement failure.

```text
U is uncertain → K and R are meaningless
```

### UDAM correction

```text
U is uncertain
K and R remain informative
```

### Re-anchor

Restart measurement from the current point.

### Why this matters

The agent cannot recover the lost interval perfectly, but they can prevent all future time from being added to the same unknown region.

## Miscalculation 2: Stopping after a study break

### Situation

A learner stops studying for a while and concludes that restarting is pointless because they no longer know their current ability.

### Mistake

They confuse lack of calibration with lack of ability.

### UDAM correction

Solving one problem can re-anchor the current skill estimate.

```text
I(a) > 0
```

The action may also improve skill slightly.

```text
B(a) >= 0
```

## Miscalculation 3: Avoiding work because the project state is unclear

### Situation

A project is interrupted. The agent avoids opening it because they do not know what state it is in.

### Mistake

They treat unclear project state as evidence that useful action is impossible.

### UDAM correction

The first action does not need to solve the project.

It only needs to contact the state.

Examples:

- inspect the task list;
- read the last commit;
- open the current working tree;
- write one note about current blockers.

These actions have informational value:

```text
I(a) > 0
```

## Miscalculation 4: Not sending a low-pressure message

### Situation

A social state becomes uncertain. The agent avoids sending a small message because the relationship feels too unclear.

### Mistake

They treat uncertainty as a reason to avoid all contact, even when one low-cost contact could update the belief state.

### UDAM correction

A small, non-compulsive message may re-anchor social uncertainty.

This does not guarantee repair.

It only updates:

```text
p(S_t | D_t)
```

## Miscalculation 5: Waiting for full confidence before acting

### Situation

The agent waits until they feel certain before taking any action.

### Mistake

They assume action requires certainty.

### UDAM correction

Some actions are valuable precisely because they reduce uncertainty.

The correct condition is not:

```text
certainty first, action second
```

but:

```text
action can produce information
```

## General form

The miscalculation is:

```text
P_t is high → do nothing
```

The UDAM correction is:

```text
P_t is high → choose a low-cost informative action if V(a) > 0
```

where:

```text
V(a) = I(a) + B(a) - C(a)
```

## Boundary

This document does not say that action is always correct.

If the action has no information value, no intervention value, or excessive cost, then it is not favored.

```text
I(a) + B(a) <= C(a)
```

In that case, the agent should not act merely for the sake of acting.

## Practical summary

When UDAM applies, the common mistake is to treat partial uncertainty as total invalidation.

The correction is:

> Do not ask whether the whole process is already clean. Ask whether the next small action can create a valid new anchor.
