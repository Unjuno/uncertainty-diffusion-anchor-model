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
| `state_belief_separation.md` | distinction between state dynamics and belief uncertainty dynamics |
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

The safer interpretation is layered:

1. `Var(U)` may remain unchanged or increase.
2. relative uncertainty can still be diluted if the reference scale grows faster than the uncertainty scale.
3. an upper bound can constrain the admissible range of `U`.

A compact version:

```text
absolute uncertainty may increase
relative influence may decrease
```

## State-belief caution

UDAM is primarily about belief uncertainty.

It should not be read as claiming that the external world always worsens during inaction.

The minimal model concerns:

```text
P_t = Var(S_t | D_t)
```

not necessarily direct deterioration of `S_t`.

## Current formal status

The theory is currently formulated in variance/covariance terms.

A future extension may use a general uncertainty functional:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```
