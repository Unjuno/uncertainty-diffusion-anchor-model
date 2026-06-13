# Lemmas

## Lemma 1: Constants do not contribute conditional variance

If:

```text
τ = K + U + R
```

and `K` and `R` are observed constants, then:

```text
Var(τ | K, R) = Var(U)
```

### Use

This lemma supports Proposition 1: uncertainty in the lost interval does not invalidate the re-anchored interval.

## Lemma 2: Positive diffusion increases uncertainty

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

### Use

This lemma supports Proposition 2.

## Lemma 3: Empty activity has negative value

If:

```text
I(a) = 0
B(a) = 0
C(a) > 0
```

then:

```text
V(a) = I(a) + B(a) - C(a) < 0
```

### Use

This lemma excludes arbitrary activity from the model.

## Lemma 4: Positive action value favors action under normalized inaction

If inaction is normalized to zero value and:

```text
V(a) > 0
```

then action `a` is favorable relative to inaction under the model.

### Use

This lemma supports the practical rule that informative low-cost actions can be rational.
