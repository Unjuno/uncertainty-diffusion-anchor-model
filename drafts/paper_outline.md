# Paper Outline

> Draft status: this is a downstream paper-facing presentation of UDAM, not a source-of-truth document. Formal claims route to `theory/`; literature claims route to `docs/17_literature_support_map.md` and `notes/literature_verification.md`; simulation claims route to `docs/39_simulation_sanity_checks.md` and `simulations/`. This outline should not introduce claims stronger than those sources support.

## Working title

Uncertainty-Diffusion Anchor Model: Re-Anchoring Action Under Fixed Targets, Belief Uncertainty, and Observability Value

## Alternative titles

- Uncertainty-Diffusion Anchor Model: Why Small Informative Actions Can Be Rational After Anchor Loss
- Fixed Target, Uncertain Position: A Timer-Derived Model of Re-Anchoring
- Partial Uncertainty Does Not Imply Total Invalidation
- Observability After Anchor Loss: A Decision-Theoretic Reading of Re-Anchoring

## Abstract draft

This paper outlines the Uncertainty-Diffusion Anchor Model (UDAM), a cognitive and decision-theoretic practical synthesis for describing how agents may recover local decision structure after losing a reference point for their current state. The model begins from a timer seed case: after losing track of elapsed position relative to a fixed target condition, restarting the count does not recover the lost interval but can create a new anchor. The core decomposition is `τ = K + U + R`, where `K` is a known interval before anchor loss, `U` is the uncertain interval, and `R` is a re-anchored known interval.

UDAM distinguishes absolute uncertainty from relative influence. Absolute uncertainty in `U` may remain or increase, while the relative influence of `U` can decrease if the reference scale grows faster than the uncertainty scale. The model also distinguishes belief uncertainty from physical state change, and limits its core scope to actionable uncertainty: uncertainty that can be affected by observation, belief update, decision improvement, or state intervention. Event-occurrence uncertainty is excluded from the core timer model and treated as an external parameter, separate extension, or exception condition.

The outline further formalizes observability value: the value of an observation comes from enabling better conditional action after the state is observed. This explains both happy miscalculation, where observation reveals hidden upside, and false comfort miscalculation, where skipped observation leaves hidden downside unmanaged. Fixed-target disbelief is modeled as subjective discounting of positional information value.

The outline also presents adaptive observation cadence and adaptive expansion factor. After an initial valid observation, an agent may expand action or observation scope geometrically, but the expansion factor is constrained by adverse-boundary risk: the probability and cost of crossing a relevant boundary before the next observation.

The safe paper claim is conditional: low-cost informative actions can be rational when `V(a)=I(a)+B(a)-C(a)>0`, when observation-specific value `OV>0`, or when expansion value exceeds observation, correction, and boundary-risk costs. The outline distinguishes re-anchoring from arbitrary activity and identifies boundary conditions such as misleading feedback, compulsive checking, high-cost action, non-actionable external uncertainty, and safety-critical delay.

## Core thesis

UDAM's core claim is:

> Losing an anchor creates local uncertainty; it does not invalidate all future anchors.

In practical form:

> When uncertainty diffuses and a low-cost action can return information, the action can be rational before full confidence is restored.

Observability refinement:

> Observation is valuable when it separates latent states and enables better conditional action.

Expansion refinement:

> Scope may expand after favorable observations, but expansion should be constrained by the risk of crossing a relevant adverse boundary before the next observation.

## Scope statement

UDAM core assumes:

```text
fixed target, uncertain position
```

It does not model:

```text
uncertain target, uncertain position
```

The fixed-target assumption is a local modeling constraint, not a metaphysical claim that all events are deterministic.

## Controllability boundary

UDAM is action-oriented.

The core model includes uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable event-occurrence uncertainty is outside the core model.

## Sections

1. Introduction
2. The timer seed model
3. Fixed-target scope
4. Absolute uncertainty versus relative influence
5. Belief uncertainty versus state change
6. Uncertainty diffusion
7. Re-anchoring actions
8. Action value
9. Observability value
10. Adaptive observation cadence and expansion factor
11. Propositions and proof sketches
12. Missed re-anchor miscalculations
13. Happy miscalculation and false comfort
14. Failure cases and boundary conditions
15. High-stakes examples as abstract fixed-target cases
16. Applications
17. Related work
18. Limitations and deferred extensions
19. Conclusion

## Section notes

### 1. Introduction

Introduce anchor loss as a common cognitive and decision-theoretic problem.

The central error is all-or-nothing invalidation:

```text
partial uncertainty → total invalidation
```

UDAM's correction is:

```text
partial uncertainty → re-anchor if V(a) > 0
```

### 2. The timer seed model

Define:

```text
τ = K + U + R
```

Explain:

- `K`: known interval before anchor loss;
- `U`: uncertain interval;
- `R`: known interval after re-anchoring;
- `τ`: current position.

Core point:

```text
U is uncertain, but R remains informative
```

### 3. Fixed-target scope

Define the seed scope:

```text
fixed target, uncertain position
```

Exclude:

```text
P(target occurs)
```

from the core model.

Reason:

```text
V(a) = P(target occurs) · I_position(a) + B(a) - C(a)
```

would mix event-occurrence uncertainty with position uncertainty.

### 4. Absolute uncertainty versus relative influence

Absolute uncertainty may remain or increase:

```text
Var(U_{t+Δt}) >= Var(U_t)
```

Relative influence may decrease:

```text
ρ = sqrt(Var(U)) / E[τ]
```

if the reference scale grows faster than the uncertainty scale.

### 5. Belief uncertainty versus state change

Define:

```text
state dynamics: S_t changes
belief dynamics: P_t changes
```

UDAM primarily models belief uncertainty:

```text
P_t = Var(S_t | D_t)
```

### 6. Uncertainty diffusion

Minimal diffusion equation:

```text
P_{t+Δt} = P_t + QΔt
```

Clarify:

- `P_t` is uncertainty;
- `Q` is uncertainty diffusion rate;
- `QΔt` is added uncertainty.

### 7. Re-anchoring actions

A re-anchor is an action that returns information about the current state.

Observation update form:

```text
p(S_t | D_t, y_a)
```

where `y_a` is the observation produced by action `a`.

### 8. Action value

Core action value:

```text
V(a) = I(a) + B(a) - C(a)
```

An action is favorable when:

```text
V(a) > 0
```

### 9. Observability value

Without observation:

```text
V_no_obs = max_a E[V(a, S)]
```

With observation:

```text
V_obs = E_y[max_a E[V(a, S) | y]] - C(obs)
```

Define:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

This chapter explains why observation can reveal hidden upside or hidden downside.

### 10. Adaptive observation cadence and expansion factor

First observation and later observations should be separated.

If observation has been zero, the first valid observation often has high value.

After that, repeated observation is justified only when:

```text
MOV_i > 0
```

If a response supports expansion, the next scope can be modeled as:

```text
s_{i+1} = r_i s_i
```

A default geometric pattern is:

```text
1 -> 2 -> 4 -> 8
```

However, expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

This chapter distinguishes search-energy efficiency from adverse-boundary risk.

### 11. Propositions and proof sketches

Include propositions on:

1. lost intervals do not invalidate future anchors;
2. uncertainty may diffuse without anchors;
3. informative low-cost actions can dominate inaction under positive value conditions;
4. frequent small re-anchoring can constrain uncertainty growth under stated assumptions;
5. empty activity is unfavorable;
6. timer re-anchoring can dilute relative influence;
7. fixed upper-bound conditions can constrain the unknown interval;
8. observation can have non-negative decision value under ideal conditions;
9. observation is favorable when `OV > 0`;
10. fixed-target disbelief can suppress a favorable re-anchor;
11. valid re-anchor must be state-informative;
12. useful observation can justify a conditional action switch;
13. expansion factor is constrained by adverse boundary risk.

### 12. Missed re-anchor miscalculations

Define the agent-side error:

```text
UDAM applies, but the agent fails to use it
```

Core pattern:

```text
partial uncertainty → total invalidation
```

Examples:

- stopping measurement after missing one interval;
- refusing to restart study after a break;
- avoiding a project because the project state is unclear;
- waiting for full confidence before diagnostic action.

### 13. Happy miscalculation and false comfort

Happy miscalculation:

```text
uncertainty feels negative → observation reveals upside
```

False comfort:

```text
uncertainty feels manageable → no observation → hidden downside appears later
```

Fixed-target disbelief:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

All three are explained by observability and conditional action.

### 14. Failure cases and boundary conditions

Include:

- no information;
- high cost;
- misleading feedback;
- compulsive checking;
- relative dilution failure;
- missing upper-bound condition;
- uncontrollable occurrence uncertainty;
- state-belief conflation;
- safety-critical delay;
- observation with no actionable consequence;
- excessive observation cost;
- expansion too large for boundary risk.

### 15. High-stakes examples as abstract fixed-target cases

High-stakes examples can clarify the structure:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

But public wording should remain neutral, non-operational, and abstract.

### 16. Applications

Applications:

- time perception;
- learning recovery;
- work interruption recovery;
- relationship uncertainty;
- health tracking;
- life strategy after failure;
- adaptive observation cadence;
- adaptive expansion factor;
- happy miscalculation;
- false comfort miscalculation.

### 17. Related work

Discuss overlap with:

- Bayesian filtering;
- Kalman filtering;
- POMDPs and belief states;
- active inference;
- value of information;
- behavioral activation;
- cognitive anchoring;
- exponential search and doubling strategies;
- online algorithms and robust sequential decision rules.

Literature claims should be phrased as component-level support unless `docs/17_literature_support_map.md` and `notes/literature_verification.md` support stronger wording.

### 18. Limitations and deferred extensions

Deferred extensions:

- stochastic target occurrence;
- entropy or general uncertainty functional;
- nonlinear diffusion;
- empirical testing;
- rendered simulations or diagrams;
- optimal expansion factor under specific loss functions.

### 19. Conclusion

Conclude:

> Re-anchoring is not optimism or arbitrary activity. It is the creation of a new valid reference point after partial uncertainty.

Add:

> Observation is valuable when it makes action conditional on the actual state.

Add:

> Expansion is useful when a favorable observation supports a larger scope, but the expansion factor must be constrained by adverse-boundary risk.

## Core equations

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
ρ = sqrt(Var(U)) / E[τ]
V(a) = I(a) + B(a) - C(a)
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
s_{i+1} = r_i s_i
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

## Main contribution

UDAM reframes small actions after disruption as information-producing re-anchors rather than mere effort or optimism.

Its distinctive contribution is the timer-derived structure:

```text
partial uncertainty does not imply total invalidation
```

combined with action-value, observability, and expansion rules:

```text
act only when I(a) + B(a) > C(a)
observe only when OV > 0
expand only when expansion value exceeds observation, correction, and boundary-risk costs
```
