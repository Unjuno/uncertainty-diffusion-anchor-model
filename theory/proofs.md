# Proofs

This file contains initial proof sketches. These are intentionally minimal.

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
Var(K + U + R | K, R) = Var(U)
```

Therefore, the uncertainty in `τ` is exactly the uncertainty in `U`, not in `R`.

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

Therefore `a` is favorable compared with inaction normalized to zero value.

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

For action value:

```text
[V(a)] = [I(a)] = [B(a)] = [C(a)] = utility unit
```

All core equations are dimensionally consistent under the stated definitions.
