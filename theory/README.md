# Theory Index

This directory contains the formal components of the Uncertainty-Diffusion Anchor Model.

## Files

| File | Role |
|---|---|
| `definitions.md` | core definitions |
| `variables.md` | notation and units |
| `assumptions.md` | assumptions of the model |
| `axioms.md` | axiomatic core |
| `lemmas.md` | supporting lemmas |
| `propositions.md` | main propositions |
| `proofs.md` | proof sketches |
| `counterexamples.md` | failure cases and boundary conditions |
| `timer_three_layer_model.md` | formal timer-specific refinement |
| `consistency_review.md` | known corrections and open consistency issues |

## Core equations

Timer model:

```text
τ = K + U + R
```

Uncertainty diffusion:

```text
P_{t+Δt} = P_t + QΔt
```

Action value:

```text
V(a) = I(a) + B(a) - C(a)
```

## Timer-specific caution

In the timer model, re-anchoring does not necessarily reduce absolute uncertainty in `U`.

The safer interpretation is three-layered:

1. `Var(U)` may remain unchanged.
2. relative uncertainty can be diluted as `R` grows.
3. an upper bound can constrain the admissible range of `U`.

## Current formal status

The theory is currently formulated in variance/covariance terms.

A future extension may use a general uncertainty functional:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```
