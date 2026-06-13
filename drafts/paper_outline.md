# Paper Outline

## Working title

Uncertainty-Diffusion Anchor Model: Re-Anchoring Action Under Fixed Targets and Belief Uncertainty

## Alternative titles

- Uncertainty-Diffusion Anchor Model: Why Small Informative Actions Are Rational After Anchor Loss
- Fixed Target, Uncertain Position: A Timer-Derived Model of Re-Anchoring
- Partial Uncertainty Does Not Imply Total Invalidation

## Abstract draft

This paper introduces the Uncertainty-Diffusion Anchor Model (UDAM), a cognitive and decision-theoretic model of how agents recover after losing a reference point for their current state. The model begins from a timer seed case: after losing track of elapsed position relative to a fixed target condition, restarting the count does not recover the lost interval but does create a new anchor. The core decomposition is `τ = K + U + R`, where `K` is a known interval before anchor loss, `U` is the uncertain interval, and `R` is a re-anchored known interval.

UDAM distinguishes absolute uncertainty from relative influence. Absolute uncertainty in `U` may remain or increase, while the relative influence of `U` can decrease if the reference scale grows faster than the uncertainty scale. The model also distinguishes belief uncertainty from physical state change, and limits its core scope to actionable uncertainty: uncertainty that can be affected by observation, belief update, decision improvement, or state intervention. Event-occurrence uncertainty is excluded from the core timer model and treated as an external parameter, separate extension, or exception condition.

The paper argues that low-cost informative actions can be rational when `V(a)=I(a)+B(a)-C(a)>0`. It distinguishes re-anchoring from arbitrary activity, identifies missed re-anchor miscalculations, and lists boundary conditions such as misleading feedback, compulsive checking, high-cost action, non-actionable external uncertainty, and safety-critical delay.

## Core thesis

UDAM's core claim is:

> Losing an anchor creates local uncertainty; it does not invalidate all future anchors.

In practical form:

> When uncertainty diffuses and a low-cost action can return information, the action can be rational even before confidence is restored.

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
9. Propositions and proof sketches
10. Missed re-anchor miscalculations
11. Failure cases and boundary conditions
12. High-stakes examples as abstract fixed-target cases
13. Applications
14. Related work
15. Limitations and deferred extensions
16. Conclusion

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

### 9. Propositions and proof sketches

Include propositions on:

1. lost intervals do not invalidate future anchors;
2. uncertainty may diffuse without anchors;
3. informative low-cost actions can dominate inaction;
4. frequent small re-anchoring can constrain uncertainty growth;
5. empty activity is unfavorable;
6. timer re-anchoring can dilute relative influence;
7. fixed upper-bound conditions can constrain the unknown interval.

### 10. Missed re-anchor miscalculations

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

### 11. Failure cases and boundary conditions

Include:

- no information;
- high cost;
- misleading feedback;
- compulsive checking;
- relative dilution failure;
- missing upper-bound condition;
- uncontrollable occurrence uncertainty;
- state-belief conflation;
- safety-critical delay.

### 12. High-stakes examples as abstract fixed-target cases

High-stakes examples can clarify the structure:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

But public wording should remain neutral, non-operational, and abstract.

### 13. Applications

Applications:

- time perception;
- learning recovery;
- work interruption recovery;
- relationship uncertainty;
- health tracking;
- life strategy after failure.

### 14. Related work

Discuss overlap with:

- Bayesian filtering;
- Kalman filtering;
- POMDPs and belief states;
- active inference;
- value of information;
- behavioral activation;
- cognitive anchoring.

### 15. Limitations and deferred extensions

Deferred extensions:

- stochastic target occurrence;
- entropy or general uncertainty functional;
- nonlinear diffusion;
- empirical testing;
- rendered simulations or diagrams.

### 16. Conclusion

Conclude:

> Re-anchoring is not optimism or arbitrary activity. It is the creation of a new valid reference point after partial uncertainty.

## Core equations

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
ρ = sqrt(Var(U)) / E[τ]
V(a) = I(a) + B(a) - C(a)
```

## Main contribution

UDAM reframes small actions after disruption as information-producing re-anchors rather than mere effort or optimism.

Its distinctive contribution is the timer-derived structure:

```text
partial uncertainty does not imply total invalidation
```

combined with an action-value rule:

```text
act only when I(a) + B(a) > C(a)
```
