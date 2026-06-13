# Assumptions

This file lists the assumptions of UDAM.

## A0. Partial observability

The agent does not directly know the full current state.

There exists a latent state `S_t` and an observation history `D_t`.

```text
P_t = Var(S_t | D_t)
```

## A1. Anchor dependence

The agent uses anchors to constrain uncertainty about the current state.

An anchor may be:

- a count;
- a record;
- a measurement;
- a visible state;
- a feedback signal;
- a completed small action;
- an external confirmation.

## A2. Anchor loss

When an anchor is lost, part of the state becomes uncertain.

In the timer model:

```text
τ = K + U + R
```

`U` represents the interval that became uncertain after anchor loss.

## A3. Uncertainty diffusion

In the absence of anchoring observations, uncertainty may increase over time.

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q >= 0
```

## A4. Informative action

Some actions return information about the state.

Such actions have informational value:

```text
I(a) > 0
```

## A5. Intervention value

Some actions improve or degrade the state itself.

This is represented by:

```text
B(a)
```

where `B(a)` can be positive, zero, or negative.

## A6. Cost

All actions may carry cost:

```text
C(a) >= 0
```

## A7. Rational action condition

An action is favorable under the model when:

```text
V(a) = I(a) + B(a) - C(a) > 0
```

## A8. No arbitrary action principle

UDAM does not claim that action is always better than inaction.

It claims only that low-cost informative actions can be favorable under uncertainty diffusion.
