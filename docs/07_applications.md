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

## Application domains

| Domain | State variable | Lost anchor | Re-anchor |
|---|---|---|---|
| time perception | elapsed time | counted position | restart counting |
| learning | skill state | skill calibration | solve one problem |
| work | project state | task/context map | inspect task list or working tree |
| relationships | social state | current social signal | send one clear message |
| health | health state | body-state trajectory | record one variable |
| life strategy | self-state after failure | model of remaining options | take one small reality-contacting action |

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

## Bad application pattern

Do not use UDAM to justify:

- blind optimism;
- compulsive action;
- vague productivity;
- high-risk action under uncertainty;
- ignoring safety or professional support;
- assuming the world always worsens during inaction.

## Good application pattern

Use UDAM to select actions that:

- update belief about the current state;
- reveal the next action;
- create feedback;
- improve the state slightly;
- preserve future option value.

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

These are different and should not be conflated.
