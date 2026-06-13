# 11 Timer Three-Layer Model

This document refines the timer model into three distinct layers.

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

## Layer 2: Relative uncertainty dilution

Even if `Var(U)` does not decrease, the relative influence of `U` can decrease as `R` grows.

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

As `R` increases, the denominator increases while the numerator remains fixed.

Therefore:

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
| Absolute uncertainty | `U` remains uncertain | `Var(τ | K, R) = Var(U)` | weakest |
| Relative dilution | `U` matters less relative to total elapsed time | `ρ(R) = sqrt(Var(U)) / E[τ]` | medium |
| Upper-bound tightening | possible range of `U` shrinks under an upper bound | `U < T - K - R` | strongest |

## Corrected timer claim

The timer model should not claim:

> Re-anchoring always reduces absolute uncertainty.

It should claim:

> Re-anchoring preserves a new known interval. This can dilute the relative influence of the unknown interval, and under an upper-bound condition can also tighten the admissible range of the unknown interval.

## General implication

This refinement matters because the timer model is the seed of UDAM.

If the seed case is precise, later applications are less likely to overclaim.
