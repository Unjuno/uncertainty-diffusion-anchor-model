# 05 Propositions

This document gives a readable overview of the core propositions of the Uncertainty-Diffusion Anchor Model.

For stricter formulation, see:

- `theory/propositions.md`
- `theory/proofs.md`
- `theory/observability_proofs.md`

## Proposition 1: Lost intervals do not invalidate future anchors

If an anchor is lost during an unknown interval, the unknown interval remains uncertain. However, observations made after re-anchoring are still valid.

Timer form:

```text
τ = K + U + R
```

`U` is uncertain, but `R` is still informative.

## Proposition 2: Uncertainty may diffuse without anchors

If there is no anchoring observation, uncertainty can increase over time.

```text
P_{t+Δt} = P_t + QΔt
```

When `Q > 0` and `Δt > 0`, uncertainty increases.

## Proposition 3: Informative small actions can be rational

An action has value:

```text
V(a) = I(a) + B(a) - C(a)
```

If:

```text
V(a) > 0
```

then the action is favorable under the model.

## Proposition 4: Re-anchoring is not arbitrary activity

Only actions that return information or improve the state count as re-anchoring.

Empty activity is excluded by:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

which implies:

```text
V(a) < 0
```

## Proposition 5: High-frequency small re-anchors can stabilize cognition

If uncertainty diffuses over time, repeated low-cost informative actions can prevent uncertainty from growing unchecked.

This is the precise version of the practical rule:

> When uncertain, do not freeze. Take a small action that returns information.

## Proposition 6: Timer re-anchoring can dilute relative uncertainty

In the timer model, re-anchoring does not necessarily erase or reduce the absolute uncertainty of the lost interval.

If:

```text
τ = K + U + R
```

and `U` remains uncertain while `R` grows as a known interval, then the relative influence of `U` can decrease.

One simple ratio is:

```text
ρ = sqrt(Var(U)) / E[τ]
```

If `sqrt(Var(U))` is fixed, then `ρ` decreases as `R` increases.

More generally, even if `Var(U)` increases, `ρ` can still decrease when the uncertainty scale grows more slowly than the total reference scale.

This is **relative uncertainty dilution**.

## Proposition 7: Fixed upper-bound non-arrival tightens the unknown interval

If there is a fixed upper time bound `T` and the bound is still unreached, then:

```text
K + U + R < T
```

so:

```text
U < T - K - R
```

Thus, in fixed-bound cases, increasing `R` can also shrink the admissible range of `U`.

## Proposition 8: Observation can have non-negative decision value under ideal conditions

Observation can be valuable because it allows the agent to choose an action after seeing more information.

Without observation:

```text
V_no_obs = max_a E[V(a, S)]
```

With observation:

```text
E_y[max_a E[V(a, S) | y]]
```

Under ideal use of information and zero observation cost:

```text
E_y[max_a E[V(a, S) | y]] >= max_a E[V(a, S)]
```

Readable meaning:

> Seeing the state before choosing can never be worse in the idealized model, because the agent can always ignore the observation and choose the same action as before.

## Proposition 9: Observation is favorable when observability value is positive

Define observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

Readable meaning:

> Observation is not automatically good. It is good only when the value of better conditional action exceeds the cost of observing.

This proposition explains both:

```text
hidden upside
hidden downside
```

The same observation can reveal that the state is better than expected or worse than expected.

## Proposition 10: Fixed-target disbelief can suppress a favorable re-anchor

In the fixed-target core model, the value of positional re-anchoring is:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

If the agent discounts the fixed target with subjective weight `pi_hat`, perceived value becomes:

```text
V_reanchor_perceived = pi_hat * I_position(a) + B(a) - C(a)
```

The agent may skip a re-anchor even though the core model favors it when:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

Readable meaning:

> The target is fixed in the model, but the agent discounts it. Because of that, a useful positional observation appears not worth doing.

This captures fixed-target disbelief and the false-comfort pattern.

## Proposition 11: A valid re-anchor must be state-informative

A re-anchor is not just any small action.

It must return information about the relevant hidden state.

Formal condition:

```text
P(y | S) != P(y)
```

Posterior-change form:

```text
P(S | y) != P(S)
```

Readable meaning:

> A future observation remains valid after anchor loss only if it is informative about the state being estimated.

This explains why the timer case works: `R` matters because it is part of the elapsed-position decomposition.

## Proposition 12: A useful observation can justify a conditional action switch

A useful observation can change the next action.

Let `a_0` be the action before observation and `a(y)` the action after observation.

Conditional switch condition:

```text
a(y) != a_0
```

Readable meaning:

> The point of observation is not observation itself. The point is that different results can justify different next actions.

This is the Monty-Hall-type structure in UDAM.
