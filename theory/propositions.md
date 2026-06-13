# Propositions

## Proposition 1: Lost intervals do not invalidate future anchors

If:

```text
τ = K + U + R
```

and `K` and `R` are observed while `U` is uncertain, then `R` still contributes valid information about `τ`.

### Meaning

The uncertainty of `U` does not make `R` meaningless.

## Proposition 2: Uncertainty increases under no-anchor conditions

If:

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q > 0
Δt > 0
```

then:

```text
P_{t+Δt} > P_t
```

### Meaning

When uncertainty diffuses and no anchor is available, inaction is not neutral.

## Proposition 3: Informative low-cost actions can dominate inaction

If:

```text
V(a) = I(a) + B(a) - C(a) > 0
```

then action `a` is favorable under the model.

### Meaning

Small informative actions can be rational even after prior measurement failure.

## Proposition 4: Frequent small re-anchoring actions can constrain uncertainty diffusion

If a sequence of actions `a_1, a_2, ..., a_n` repeatedly provides positive informational value at low cost, then it can prevent uncertainty from growing unchecked.

### Meaning

The strategic advantage is not arbitrary hyperactivity. It is high-frequency low-cost re-anchoring.

## Proposition 5: Empty activity is unfavorable

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

### Meaning

The model does not justify action without informational or intervention value.

## Proposition 6: Timer re-anchoring can dilute relative uncertainty

In the timer model:

```text
τ = K + U + R
```

assume `K` and `R` are observed, while `U` has uncertainty.

Define relative uncertainty ratio:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

If the uncertainty scale `sqrt(Var(U))` grows more slowly than the expected elapsed time `E[τ]`, then increasing `R` decreases `ρ(R)`.

### Meaning

Timer re-anchoring does not necessarily reduce the absolute variance of the unknown interval `U`. Absolute uncertainty may remain or even increase. The key claim is that the relative influence of `U` can decrease when the known interval `R` expands the total reference scale faster than the uncertainty scale grows.

## Proposition 7: Fixed upper-bound non-arrival can tighten the unknown interval

If a fixed upper time bound `T` exists and the bound has not yet been reached, then:

```text
K + U + R < T
```

which implies:

```text
U < T - K - R
```

### Meaning

In fixed-bound cases, increasing `R` while the bound is still unreached can shrink the admissible range of `U`. This is stronger than relative dilution.
