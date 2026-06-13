# Proofs

This file contains initial proof sketches. These are intentionally minimal but dimensionally explicit.

## Proof of Proposition 1

Given:

```text
τ = K + U + R
```

Assume `K` and `R` are observed and `U` is uncertain.

The uncertainty of `τ` is induced by `U`:

```text
Var(τ | K, R) = Var(K + U + R | K, R)
```

Since `K` and `R` are observed constants under the conditioning:

```text
Var(K + U + R | K, R) = Var(U | K, R)
```

If `U` is independent of the measurement noise in `K` and `R`, or if `K` and `R` are treated as fixed observations, this reduces to:

```text
Var(τ | K, R) = Var(U)
```

Therefore, the uncertainty in `τ` is located in `U`, not in `R`.

Thus `R` remains valid information.

## Proof of Proposition 2

Given:

```text
P_{t+Δt} = P_t + QΔt
```

with:

```text
Q > 0
Δt > 0
```

Then:

```text
QΔt > 0
```

Therefore:

```text
P_{t+Δt} = P_t + QΔt > P_t
```

So uncertainty strictly increases under no-anchor conditions.

## Proof of Proposition 3

Given action value:

```text
V(a) = I(a) + B(a) - C(a)
```

If:

```text
V(a) > 0
```

then the net value of action `a` is positive under the model.

If inaction is normalized to:

```text
V(inaction) = 0
```

then:

```text
V(a) > V(inaction)
```

Therefore `a` is favorable compared with inaction under the model.

## Proof sketch of Proposition 4

Assume uncertainty grows without anchors by:

```text
P_{t+Δt} = P_t + QΔt
```

Now suppose a re-anchoring action occurs at discrete times:

```text
t_1, t_2, ..., t_n
```

and each action reduces uncertainty by an amount `r_i >= 0` after local diffusion.

A simple recurrence is:

```text
P_{i+1} = P_i + QΔt_i - r_i
```

where:

- `Δt_i` is the time since the previous anchor;
- `r_i` is uncertainty reduction from the next re-anchor.

If:

```text
r_i > 0
```

then the uncertainty after action is lower than it would have been under pure diffusion:

```text
P_i + QΔt_i - r_i < P_i + QΔt_i
```

Therefore repeated informative re-anchors constrain uncertainty relative to the no-action trajectory.

This does not prove that any frequency is optimal. It proves only comparative containment against unchecked diffusion, assuming positive uncertainty reduction and acceptable cost.

## Proof of Proposition 5

Assume:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

Then:

```text
V(a) = I(a) + B(a) - C(a)
     = 0 + 0 - C(a)
     = -C(a)
```

Since:

```text
C(a) > 0
```

we have:

```text
V(a) < 0
```

Therefore empty activity is unfavorable.

## Proof of Proposition 6

Given:

```text
τ = K + U + R
```

with `K` and `R` observed, and `U` uncertain.

Define:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

Since:

```text
E[τ] = K + E[U] + R
```

we get:

```text
ρ(R) = sqrt(Var(U)) / (K + E[U] + R)
```

### Special case: fixed absolute uncertainty

If `Var(U)` is fixed, let:

```text
A = sqrt(Var(U))
B = K + E[U]
```

Then:

```text
ρ(R) = A / (B + R)
```

For `A >= 0` and `B + R > 0`, the derivative is:

```text
dρ/dR = -A / (B + R)^2 <= 0
```

If `A > 0`, then:

```text
dρ/dR < 0
```

Therefore increasing `R` decreases relative uncertainty in the fixed-variance case.

### General case: increasing absolute uncertainty

Let the uncertainty scale be:

```text
A(R) = sqrt(Var(U_R))
```

and the total reference scale be:

```text
B(R) = E[τ] = K + E[U_R] + R
```

Then:

```text
ρ(R) = A(R) / B(R)
```

Relative dilution occurs when:

```text
dρ/dR < 0
```

Using the quotient rule:

```text
dρ/dR = (A'(R)B(R) - A(R)B'(R)) / B(R)^2
```

Since `B(R)^2 > 0`, relative dilution occurs when:

```text
A'(R)B(R) < A(R)B'(R)
```

Equivalently:

```text
A'(R)/A(R) < B'(R)/B(R)
```

when `A(R) > 0` and `B(R) > 0`.

Thus absolute uncertainty may increase, but relative influence decreases if the uncertainty scale grows more slowly, in proportional terms, than the total reference scale.

## Proof of Proposition 7

Assume a fixed upper time bound `T` and that the bound is not yet reached.

Then:

```text
τ < T
```

Using the timer decomposition:

```text
K + U + R < T
```

Subtracting `K + R` from both sides gives:

```text
U < T - K - R
```

Therefore, as `R` increases, the upper bound on admissible `U` decreases.

This gives an upper-bound tightening effect.

## Unit checks

For uncertainty diffusion:

```text
[QΔt] = (state unit^2 / s) · s = state unit^2
```

So:

```text
[P_{t+Δt}] = [P_t] = [QΔt]
```

For timer decomposition:

```text
[τ] = [K] = [U] = [R] = s
```

For relative uncertainty ratio:

```text
ρ = sqrt(Var(U)) / E[τ]
```

we have:

```text
[sqrt(Var(U))] = s
[E[τ]] = s
[ρ] = 1
```

For action value:

```text
[V(a)] = [I(a)] = [B(a)] = [C(a)] = utility unit
```

All core equations are dimensionally consistent under the stated definitions.

## Current proof status

These are proof sketches, not final formal proofs.

The next formal step is to specify whether `P_t` is always variance, covariance, entropy, or a more general uncertainty functional.
