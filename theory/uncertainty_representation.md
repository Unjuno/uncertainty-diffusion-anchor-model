# Uncertainty Representation

This file records the representation decision for uncertainty in UDAM.

## Decision

In the core model, UDAM treats uncertainty as variance or covariance-like belief uncertainty.

Scalar form:

```text
P_t = Var(S_t | D_t)
```

Vector form:

```text
P_t = Cov(S_t | D_t)
```

A more general uncertainty functional may be introduced later:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

but it is not part of the minimal core model.

## Why keep `P_t` in the core?

The current theory already uses:

```text
P_{t+Δt} = P_t + QΔt
```

and:

```text
P_t^+ < P_{no-action}
```

These are easiest to read when `P_t` is variance or covariance-like uncertainty.

Keeping `P_t` fixed preserves clarity in:

- the timer model;
- diffusion-rate conditions;
- observation updates;
- relative uncertainty discussion;
- state-belief separation.

## Why not generalize immediately?

A general uncertainty functional is more flexible, but it makes the theory harder to read.

If the core model used:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

from the beginning, every equation would need additional assumptions about how `𝓤` behaves under diffusion, observation, and action.

For the current theory note, that is unnecessary.

## Future extension

A later version may define:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

where `𝓤` could be:

- variance;
- covariance determinant;
- entropy;
- credible interval width;
- expected decision error;
- probability of critical-region error;
- posterior dispersion;
- expected value loss from uncertainty.

This extension should be introduced only after the variance/covariance version is stable.

## Relation to observability value

Observability value does not require replacing `P_t`.

`P_t` measures belief uncertainty.

`OV` measures decision value from observation:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Thus UDAM can keep both:

```text
P_t = Var(S_t | D_t)
```

and:

```text
OV > 0
```

without forcing all uncertainty into one scalar.

## Relation to action value

Action value remains:

```text
V(a) = I(a) + B(a) - C(a)
```

`P_t` may inform `I(a)`, but it is not identical to `I(a)`.

`I(a)` is a utility-valued informational term.

`P_t` is a belief-uncertainty term.

They should not be conflated.

## Correct statement

The precise repository-level decision is:

> Core UDAM uses variance/covariance-like belief uncertainty `P_t`. A general uncertainty functional `𝓤_t` is allowed as a future extension, not as the minimal representation.

## Consequence for v0.5

The v0.5 formal refinement decision is closed:

```text
core: P_t = Var(S_t | D_t) or Cov(S_t | D_t)
extension: 𝓤_t = 𝓤(p(S_t | D_t))
```
