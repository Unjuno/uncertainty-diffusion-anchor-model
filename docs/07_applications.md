# 07 Applications

UDAM can be applied wherever an agent loses an anchor and uncertainty about the current state grows over time.

However, applications must distinguish **state dynamics** from **belief dynamics**.

UDAM does not require the external state to worsen during inaction. It requires only that the agent's uncertainty about the state may increase without anchors.

## Application structure

Each application should be written in the same structure:

1. Situation
2. Lost anchor
3. State variable
4. Belief uncertainty
5. Possible state dynamics
6. Belief dynamics
7. Re-anchoring action
8. Informational value
9. Intervention value
10. Failure case
11. Observation cadence
12. Expansion factor and boundary risk

## Application domains

| Domain | State variable | Lost anchor | Re-anchor |
|---|---|---|---|
| time perception | elapsed time | counted position | restart counting |
| learning | skill state | skill calibration | solve one problem |
| work | project state | task/context map | inspect task list or working tree |
| relationships | social state | current social signal | send one clear message |
| health | health state | body-state trajectory | record one variable |
| life strategy | self-state after failure | model of remaining options | take one small reality-contacting action |

## Observability application layer

The observability layer asks whether a small action makes the current state visible enough to support better conditional action.

Core condition:

```text
OV > 0
```

where:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

This layer explains three application patterns:

1. missed re-anchor miscalculation;
2. happy miscalculation;
3. false comfort miscalculation, including fixed-target disbelief.

## Adaptive expansion application layer

After a small valid observation, the agent may expand the next action or observation scope.

```text
s_{i+1} = r_i s_i
```

A common pattern is:

```text
1 -> 2 -> 4 -> 8
```

But application examples must not treat doubling as automatically correct.

Expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Readable meaning:

> Expand when favorable observations support expansion, but reduce the expansion factor when the next observation may come too late relative to a relevant adverse boundary.

## Missed application cases

Some examples should describe cases where the model applies but the agent fails to use it.

These are not failure cases of UDAM.

They are miscalculations by the agent.

The general pattern is:

```text
partial uncertainty → total invalidation
```

Examples:

- stopping measurement because one interval was missed;
- avoiding study because current skill is unclear;
- avoiding a project because the project state is unclear;
- avoiding low-pressure contact because the social state is unclear;
- waiting for certainty before taking any diagnostic action.

The UDAM correction is:

```text
partial uncertainty → choose a low-cost informative action if V(a) > 0
```

where:

```text
V(a) = I(a) + B(a) - C(a)
```

See:

- `examples/missed_reanchor_miscalculation.md`

## Happy miscalculation cases

Some examples should describe cases where uncertainty hides upside.

These are not claims that uncertainty is good.

They are cases where increased observability reveals that the current state is better than expected.

The general pattern is:

```text
uncertainty feels negative → observation reveals a better state than expected
```

Examples:

- a learner expects total forgetting, but one problem reveals retained skill;
- a project feels chaotic, but opening the task list reveals a small next step;
- a social state feels negative, but a low-pressure message reveals neutrality or receptiveness;
- a tracked variable is feared to be worsening, but one record shows stability.

The UDAM correction is:

```text
uncertainty may hide upside → observe if the observation is low-cost and actionable
```

See:

- `examples/happy_miscalculation.md`

## False comfort miscalculation cases

Some examples should describe cases where uncertainty hides downside while the agent feels safe or in control.

These are not arguments for compulsive checking.

They are cases where observation would reveal a worse-than-expected state early enough to respond.

The general pattern is:

```text
uncertainty feels manageable → no observation → hidden downside appears later
```

Examples:

- a learner assumes they understand, but a small test reveals a gap;
- a project seems fine, but opening the task list reveals a blocker;
- a social state seems fine, but a low-pressure check reveals unresolved tension;
- a tracked variable seems stable, but one record reveals drift.

The UDAM correction is:

```text
uncertainty may hide downside → observe if the observation is low-cost and actionable
```

See:

- `examples/false_comfort_miscalculation.md`

## Fixed-target disbelief

Fixed-target disbelief is a special false-comfort pattern.

The agent discounts a fixed target condition and therefore fails to re-anchor their position relative to it.

Formal pattern:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

Readable meaning:

> The core model favors re-anchoring, but the agent's discounted model does not.

This case should be handled abstractly, especially in high-stakes examples.

## Practical principle

The first action after anchor loss should usually be small, concrete, and diagnostic.

It should answer:

> What state am I actually in now?

More precisely, it should update:

```text
p(S_t | D_t)
```

or reduce uncertainty in:

```text
P_t = Var(S_t | D_t)
```

For observability-specific cases, it should also increase the ability to choose conditionally:

```text
observe y → choose a(y)
```

After favorable results, the next scope may expand:

```text
small probe -> favorable response -> larger probe
```

but only when boundary-risk-constrained expansion value is positive.

## Bad application pattern

Do not use UDAM to justify:

- blind optimism;
- compulsive action;
- vague productivity;
- high-risk action under uncertainty;
- ignoring safety or professional support;
- assuming the world always worsens during inaction;
- treating observation as useful when it does not change any decision;
- expanding scope just because the previous small probe succeeded.

## Good application pattern

Use UDAM to select actions that:

- update belief about the current state;
- reveal the next action;
- create feedback;
- improve the state slightly;
- preserve future option value;
- reveal hidden upside when the current state is better than expected;
- reveal hidden downside early when the current state is worse than expected;
- make action conditional on observation;
- expand scope only when the response and boundary-risk terms justify it.

## Key distinction

An action may have:

```text
I(a) > 0
```

because it updates belief.

It may also have:

```text
B(a) > 0
```

because it improves the state.

An observation-specific action may also be justified by:

```text
OV > 0
```

because it enables better conditional action.

A scope expansion may be justified by:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

because the expansion benefit and information value exceed observation, correction, and boundary-risk costs.

These should not be conflated or double-counted.
