# Timer Three-Layer Model

This file gives the formal version of the timer-specific refinement.

## Setup

Let:

```text
τ = K + U + R
```

where:

- `K` is observed;
- `R` is observed;
- `U` is uncertain.

Assume initially that `K` and `R` are exact or low-noise observations.

## Layer 1: Absolute uncertainty

Under the conditioning on observed `K` and `R`:

```text
Var(τ | K, R) = Var(K + U + R | K, R)
```

Since `K` and `R` are constants under the conditioning:

```text
Var(τ | K, R) = Var(U | K, R)
```

If `U` is independent of measurement noise in `K` and `R`, or if `K` and `R` are treated as fixed:

```text
Var(τ | K, R) = Var(U)
```

Therefore, re-anchoring does not necessarily reduce the absolute variance of the unknown interval.

## Layer 2: Relative uncertainty dilution

Define relative uncertainty ratio:

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

Let:

```text
A = sqrt(Var(U))
B = K + E[U]
```

Then:

```text
ρ(R) = A / (B + R)
```

For `B + R > 0`:

```text
dρ/dR = -A / (B + R)^2
```

If `A > 0`, then:

```text
dρ/dR < 0
```

Therefore, as `R` increases, the relative uncertainty ratio decreases.

## Layer 3: Upper-bound tightening

Suppose there is a fixed upper time bound `T` and the current elapsed time is known to be below it:

```text
τ < T
```

Using:

```text
τ = K + U + R
```

we get:

```text
K + U + R < T
```

Therefore:

```text
U < T - K - R
```

As `R` increases, the upper bound on `U` decreases.

## Interpretation

Timer re-anchoring has three different effects depending on what is being measured:

1. It may leave absolute uncertainty unchanged.
2. It can reduce relative uncertainty.
3. Under an upper-bound condition, it can reduce the possible range of the unknown interval.

These should not be conflated.

## Importance

This file prevents an overclaim in the core seed model.

The correct statement is not:

```text
re-anchoring always lowers Var(U)
```

but:

```text
re-anchoring adds observed interval R, which can dilute the relative effect of U and may constrain U under additional bounds
```
