# 11 Timer Three-Layer Model

This document refines the timer model into distinct layers.

The goal is to avoid the incorrect claim that re-anchoring always reduces absolute uncertainty.

## Base equation

```text
τ = K + U + R
```

where:

- `K` is the known interval before anchor loss;
- `U` is the unknown interval;
- `R` is the re-anchored known interval;
- `τ` is the current elapsed time.

## Layer 1: Absolute uncertainty

If `K` and `R` are known and `U` is still uncertain, then:

```text
Var(τ | K, R) = Var(U)
```

This means that re-anchoring does not necessarily reduce the absolute uncertainty of the unknown interval.

The unknown interval remains unknown.

## Layer 1b: Absolute uncertainty may still increase

In a more realistic timer model, the unknown interval may continue to accumulate uncertainty until it is bounded or inferred.

For example, if the unknown component has its own diffusion process:

```text
Var(U_{t+Δt}) = Var(U_t) + Q_U Δt
```

then absolute uncertainty increases when:

```text
Q_U > 0
Δt > 0
```

So the refined claim is not:

> absolute uncertainty must stay fixed.

It is:

> absolute uncertainty may stay fixed or even increase, while its relative influence can still decrease if the known interval grows faster or the total reference scale expands.

## Layer 2: Relative uncertainty dilution

Even if `Var(U)` does not decrease, and even if it increases slowly, the relative influence of `U` can decrease as `R` grows.

Define:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

Since:

```text
E[τ] = K + E[U] + R
```

we have:

```text
ρ(R) = sqrt(Var(U)) / (K + E[U] + R)
```

If the numerator grows more slowly than the denominator, then:

```text
ρ(R) decreases as R increases
```

This is **relative uncertainty dilution**.

## Layer 3: Upper-bound tightening

If there is a fixed upper time bound `T`, and the current elapsed time is known to be below it, then:

```text
K + U + R < T
```

which implies:

```text
U < T - K - R
```

In this special case, increasing `R` reduces the upper bound of `U`.

This is stronger than relative dilution because it constrains the possible range of the unknown interval.

## Three-layer summary

| Layer | Claim | Formula | Strength |
|---|---|---|---|
| Absolute uncertainty | `U` may remain uncertain or even grow | `Var(U_{t+Δt}) = Var(U_t) + Q_U Δt` | base |
| Relative dilution | `U` can matter less relative to total elapsed time | `ρ(R) = sqrt(Var(U)) / E[τ]` | comparative |
| Upper-bound tightening | possible range of `U` shrinks under an upper bound | `U < T - K - R` | strongest |

## Corrected timer claim

The timer model should not claim:

> Re-anchoring always reduces absolute uncertainty.

It should claim:

> Re-anchoring preserves a new known interval. Absolute uncertainty in the unknown interval may remain or even increase, but the unknown interval's relative influence can decrease as the known interval grows. Under an upper-bound condition, the admissible range of the unknown interval can also tighten.

## General implication

This refinement matters because the timer model is the seed of UDAM.

If the seed case is precise, later applications are less likely to overclaim.
