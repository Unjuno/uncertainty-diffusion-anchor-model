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
| `false_comfort_miscalculation.md` | downside example | cases where lack of observation hides a worse-than-expected state |
| `failure_state_uninformative_observation.md` | failure example | action feels like checking but is not informative about the relevant state |
| `failure_checking_loop.md` | failure example | repeated observation loses marginal decision value |
| `failure_over_expansion.md` | failure example | favorable small probe is overextended into an excessive scope |
| `failure_local_to_global_judgment.md` | failure example | local observation is misused as a global conclusion |
| `concrete_learning_reanchor.md` | concrete daily case | one representative problem as learning re-anchor |
| `concrete_work_reanchor.md` | concrete daily case | task list inspection as project re-anchor |
| `concrete_relationship_reanchor.md` | concrete daily case | low-pressure message as social re-anchor |
| `concrete_budget_reanchor.md` | concrete daily case | minimum budget numbers as planning re-anchor |
| `application_playbook_template.md` | template | required structure for future concrete applications |

## Concrete daily cases

The concrete daily cases are meant to make UDAM usable, not merely abstract.

They follow the pattern:

```text
unclear state -> state-informative observation -> mapped next action
```

The action is justified only when:

```text
V(a) > 0
```

or:

```text
OV > 0
```

The concrete cases should show:

- the exact unclear state;
- the common mistaken inference;
- the small state-informative observation;
- the immediate action steps;
- the possible observation results;
- the next action map.

## Required practical sections

Every concrete application should include these sections:

```text
If you are in this situation, do this now
Observation result
Next action map
Boundary
```

The most important section is:

```text
Next action map
```

because UDAM becomes practical only when observation changes action.

```text
a(y) != a_0
```

## Application playbook template

For new applications, use:

- `application_playbook_template.md`

Minimal shape:

```text
unclear state
-> state-informative observation
-> classify result
-> choose mapped next action
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

## False comfort miscalculation examples

Some examples describe downside hidden inside apparent safety.

The common pattern is:

```text
uncertainty feels manageable → no observation → hidden downside appears later
```

This is not pessimism.

It is the same observability logic in the other direction:

```text
uncertainty may hide downside
observation can reveal it early
```

The action is still justified only when:

```text
V(a) > 0
```

## Failure examples

Failure examples show where UDAM weakens or is misused.

They are different from missed-application examples.

A missed application says:

```text
UDAM would apply, but the agent fails to use it
```

A failure example says:

```text
UDAM does not apply cleanly, or the agent applies it to the wrong object
```

Common failure conditions:

```text
P(y | S) = P(y)
a(y) = a_0
MOV_i <= 0
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
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

- safety-critical fixed-reference example;
- constrained decision context;
- upper time bound.

The goal is to preserve the model structure, not operational detail.

## Core distinction

UDAM does not require the external state to worsen during inaction.

It requires only that the agent's uncertainty about the state may increase without anchors.

```text
state dynamics ≠ belief dynamics
```
