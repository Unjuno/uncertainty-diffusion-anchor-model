# Axioms

## Axiom 1: Partial Observability

The agent does not directly know the full current state.

There exists a latent state `S_t` and an observation history `D_t`.

In the minimal variance formulation:

```text
P_t = Var(S_t | D_t)
```

## Axiom 2: Fixed Target Condition

In the timer seed model, the target condition is treated as fixed.

The model does not assign probability to whether the target condition itself occurs.

It asks only where the agent is relative to the fixed target condition.

Compact form:

```text
fixed target, uncertain position
```

not:

```text
uncertain target, uncertain position
```

## Axiom 3: Controllability Boundary

UDAM's core action-value argument applies to uncertainty that can be affected by action.

An uncertainty source belongs inside the core model only if action can affect at least one of:

1. information about the state;
2. belief uncertainty;
3. decision quality;
4. the state itself.

Uncontrollable external occurrence uncertainty is excluded from the core timer model or treated as an exception layer.

## Axiom 4: Anchor Loss

When an agent loses an anchor, part of the state becomes uncertain.

Timer form:

```text
τ = K + U + R
```

`U` is the uncertain part created by anchor loss.

## Axiom 5: Belief Uncertainty Diffusion

Without anchoring observations, belief uncertainty increases or remains unchanged over time.

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q >= 0
Δt >= 0
```

If `Q > 0` and `Δt > 0`, then uncertainty strictly increases.

This is an axiom about belief uncertainty, not necessarily about direct deterioration of the external state.

## Axiom 6: Timer Relative Influence

In the timer model, re-anchoring does not necessarily reduce absolute uncertainty in the unknown interval.

Absolute uncertainty may remain or increase.

However, relative influence can decrease if the total reference scale grows faster than the uncertainty scale.

A representative ratio is:

```text
ρ = sqrt(Var(U)) / E[τ]
```

## Axiom 7: Re-Anchoring

An action that returns information about the current state can re-anchor the agent's belief state.

A minimal condition is:

```text
I(a) > 0
```

## Axiom 8: Action Value

An action has total value:

```text
V(a) = I(a) + B(a) - C(a)
```

An action is favorable under the model if:

```text
V(a) > 0
```

## Axiom 9: No Arbitrary Activity

Activity without information value or intervention value is not re-anchoring.

If:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

then:

```text
V(a) < 0
```

The model therefore rejects empty busyness.
