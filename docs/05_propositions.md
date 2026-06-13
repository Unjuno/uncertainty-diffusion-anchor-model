# 05 Propositions

This document gives a readable overview of the core propositions of the Uncertainty-Diffusion Anchor Model.

For stricter formulation, see:

- `theory/propositions.md`
- `theory/proofs.md`

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
