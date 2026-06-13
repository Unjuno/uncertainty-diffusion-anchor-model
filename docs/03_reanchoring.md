# 03 Re-Anchoring

## Definition

A **re-anchoring action** is an action that returns information about the current state after the agent has lost an anchor.

Japanese: **再アンカー行動**

## Core claim

Re-anchoring does not fully recover the lost interval. It creates a new point of reference from the present onward.

More precisely, re-anchoring constrains the belief state relative to continued non-observation. It may reduce uncertainty absolutely, but the safer claim is comparative:

```text
P_after_action < P_no_action_trajectory
```

not always:

```text
P_after_action < P_before_action
```

## In the timer model

```text
τ = K + U + R
```

`R` is the re-anchored interval.

It does not eliminate uncertainty about `U`, but it prevents all future time from being folded into the unknown interval.

## General structure

```text
known state + unknown state + re-anchored observation
```

A re-anchor is useful when it satisfies at least one of the following:

1. It reduces uncertainty about the state absolutely.
2. It constrains uncertainty relative to the no-action trajectory.
3. It reveals the next viable action.
4. It constrains the range of possible states.
5. It creates feedback from the environment.
6. It records the present state for later use.

## What re-anchoring is not

Re-anchoring is not arbitrary motion.

The following are usually not re-anchors unless they return meaningful state information:

- compulsive checking;
- refreshing social media;
- vague planning without output;
- busywork that hides the actual state;
- high-cost action with no feedback.

## Minimal criterion

An action `a` is a re-anchor only if:

```text
I(a) > 0
```

or:

```text
B(a) > 0
```

where:

- `I(a)` is informational value;
- `B(a)` is intervention value.

## Examples

| Situation | Lost anchor | Re-anchor |
|---|---|---|
| lost time count | elapsed time | restart counting |
| stopped studying | actual skill level | solve one problem |
| project interruption | project state | inspect task list for 10 minutes |
| uncertain relationship | other person's state | send one clear message |
| unclear health | body state | record one symptom or metric |

## Practical principle

When uncertain, do not immediately choose a large irreversible action.

First choose a small action that returns information.
