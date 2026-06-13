# Assumptions

This file lists the assumptions of UDAM.

## A0. Partial observability

The agent does not directly know the full current state.

There exists a latent state `S_t` and an observation history `D_t`.

```text
P_t = Var(S_t | D_t)
```

## A1. Belief-state focus

UDAM primarily models uncertainty in the agent's belief state, not necessarily direct deterioration of the external state.

The model distinguishes:

```text
state dynamics: S_t changes
belief dynamics: P_t changes
```

The core uncertainty equation concerns `P_t`.

## A2. Fixed target condition in the timer seed model

The timer seed model assumes a fixed target condition.

It does not model uncertainty about whether the target condition exists or will occur.

The core timer question is:

```text
Given a fixed target condition, where is the agent relative to it?
```

not:

```text
What is the probability that the target condition itself occurs?
```

This is a local modeling assumption, not a metaphysical claim that all events are deterministic.

## A3. Controllability boundary

UDAM is an action-oriented model.

The core theory includes only uncertainty that can be affected by action through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable event-occurrence uncertainty is excluded from the core timer model or treated as an exception layer.

## A4. Anchor dependence

The agent uses anchors to constrain uncertainty about the current state.

An anchor may be:

- a count;
- a record;
- a measurement;
- a visible state;
- a feedback signal;
- a completed small action;
- an external confirmation.

## A5. Anchor loss

When an anchor is lost, part of the state becomes uncertain.

In the timer model:

```text
τ = K + U + R
```

`U` represents the interval that became uncertain after anchor loss.

## A6. Uncertainty diffusion

In the absence of anchoring observations, belief uncertainty may increase over time.

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q >= 0
```

This is a belief-uncertainty assumption, not a claim that the world necessarily worsens.

## A7. Timer relative influence

In the timer model, re-anchoring does not necessarily reduce absolute uncertainty in `U`.

Absolute uncertainty may remain or increase:

```text
Var(U_{t+Δt}) >= Var(U_t)
```

However, the relative influence of `U` may decrease when the total reference scale grows faster than the uncertainty scale.

One relative measure is:

```text
ρ = sqrt(Var(U)) / E[τ]
```

## A8. Upper-bound constraint

If there is a fixed upper time bound `T` and the current elapsed time is known to be below it, then:

```text
K + U + R < T
```

which implies:

```text
U < T - K - R
```

This is an additional constraint, not part of the basic timer decomposition.

## A9. Informative action

Some actions return information about the state.

Such actions have informational value:

```text
I(a) > 0
```

## A10. Intervention value

Some actions improve or degrade the state itself.

This is represented by:

```text
B(a)
```

where `B(a)` can be positive, zero, or negative.

## A11. Cost

All actions may carry cost:

```text
C(a) >= 0
```

## A12. Rational action condition

An action is favorable under the model when:

```text
V(a) = I(a) + B(a) - C(a) > 0
```

## A13. No arbitrary action principle

UDAM does not claim that action is always better than inaction.

It claims only that low-cost informative actions can be favorable under uncertainty diffusion.
