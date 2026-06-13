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
| `observability_proofs.md` | proof sketches for observability value and fixed-target discounting |
| `counterexamples.md` | failure cases and boundary conditions |
| `logical_synthesis_review.md` | review of logical coherence across model layers |
| `timer_three_layer_model.md` | formal timer-specific refinement |
| `deterministic_event_scope.md` | fixed-target scope of the timer seed model |
| `controllability_boundary.md` | boundary between actionable uncertainty and uncontrollable external uncertainty |
| `valid_reanchor_condition.md` | condition that a re-anchor must be state-informative |
| `conditional_action_switch.md` | information-action structure where observation changes the next action |
| `diffusion_rate_conditions.md` | conditions under which positive uncertainty diffusion is appropriate |
| `uncertainty_representation.md` | decision to keep `P_t` as variance/covariance in core and reserve `𝓤_t` for extension |
| `observability_value.md` | formal value of observation, upside/downside uncertainty, and fixed-target disbelief |
| `diminishing_information_value.md` | declining marginal value of repeated observation and checking boundaries |
| `upside_uncertainty.md` | favorable-state discovery through re-anchoring |
| `downside_uncertainty.md` | hidden downside and false comfort miscalculation |
| `state_belief_separation.md` | distinction between state dynamics and belief uncertainty dynamics |
| `consistency_review.md` | known corrections and open consistency issues |

## Current synthesis status

The current layer stack is logically coherent when each condition is kept explicit.

The most important synthesis review is:

- `logical_synthesis_review.md`

Core verdict:

```text
No major internal contradiction found.
```

Main watch items:

```text
I(a) versus OV
state-informative versus favorable
first observation versus repeated observation
expansion versus automatic doubling
local observation versus global conclusion
```

## Core equations

Timer model:

```text
τ = K + U + R
```

Core uncertainty representation:

```text
P_t = Var(S_t | D_t)
```

or, for vector states:

```text
P_t = Cov(S_t | D_t)
```

Future uncertainty-functional extension:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

Valid re-anchor condition:

```text
P(y | S) != P(y)
```

Posterior-change condition:

```text
P(S | y) != P(S)
```

Conditional action switch:

```text
a(y) != a_0
```

Uncertainty diffusion:

```text
P_{t+Δt} = P_t + QΔt
```

Composite diffusion rate:

```text
Q_total = Q_state + Q_memory + Q_dependency + Q_context
```

Action value:

```text
V(a) = I(a) + B(a) - C(a)
```

Observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Marginal observability value:

```text
MOV_i = E_y[max_a E[V(a,S) | y, D_i]] - max_a E[V(a,S) | D_i] - C(obs_i)
```

Fixed-target discounting error region:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

Expansion scope update:

```text
s_{i+1} = r_i s_i
```

Boundary-risk-constrained expansion:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
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

## Valid re-anchor caution

UDAM should not say:

```text
any small action is useful
```

It should say:

```text
small state-informative observation can be useful
```

The timer `R` is valid because it is part of the elapsed-position decomposition:

```text
τ = K + U + R
```

## Diffusion-rate caution

UDAM should not assume `Q > 0` merely because time passes.

A positive diffusion rate is appropriate when unobserved time can make the agent's belief about the relevant state less reliable through state change, memory decay, dependency change, context loss, or increased sensitivity to position error.

If these do not hold, `Q` may be zero.

## Uncertainty-representation caution

Core UDAM uses variance/covariance-like belief uncertainty:

```text
P_t = Var(S_t | D_t)
```

or:

```text
P_t = Cov(S_t | D_t)
```

A general uncertainty functional is permitted as a later extension:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

but it is not required for the minimal theory.

## Fixed-target and controllability caution

The timer seed model assumes:

```text
fixed target, uncertain position
```

It excludes:

```text
uncertain target, uncertain position
```

The reason is not only mathematical simplicity. Event-occurrence uncertainty is often uncontrollable by the agent, so it should be treated as external, exceptional, or deferred to an extension.

## Observability caution

Observation has value when it enables better conditional action.

It can reveal:

```text
hidden upside
hidden downside
```

But observation is not automatically valuable. It must exceed cost and be actionable.

Repeated observation must satisfy:

```text
MOV_i > 0
```

or it becomes checking without sufficient marginal value.

## Expansion caution

Geometric expansion can be useful, but only under the expansion-value condition.

```text
s_{i+1} = r_i s_i
```

A larger expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Doubling is a possible heuristic, not a universal optimum.

## State-belief caution

UDAM is primarily about belief uncertainty.

It should not be read as claiming that the external world always worsens during inaction.

The minimal model concerns:

```text
P_t = Var(S_t | D_t)
```

not necessarily direct deterioration of `S_t`.

## Current formal status

The theory is currently formulated in variance/covariance and expected-value terms.

The v0.5 representation decision is:

```text
core: P_t = Var(S_t | D_t) or Cov(S_t | D_t)
extension: 𝓤_t = 𝓤(p(S_t | D_t))
```
