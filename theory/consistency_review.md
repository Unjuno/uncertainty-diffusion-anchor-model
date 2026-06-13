# Consistency Review

This document tracks internal consistency issues in UDAM.

## Status legend

- Fixed: corrected in repository files.
- Open: unresolved or intentionally deferred.
- Watch: not wrong, but easy to misread.

## Issue 1: `P_t` versus `Q`

Status: Fixed.

Problem:

`P_t` and `Q` can be confused.

Clarification:

- `P_t` is current uncertainty.
- `Q` is the diffusion rate of uncertainty.
- `QΔt` is added uncertainty over unanchored time.

Minimal equation:

```text
P_{t+Δt} = P_t + QΔt
```

Timer-specific unit correction:

```text
[P_t] = s^2
[Q] = s^2 / s
[QΔt] = s^2
```

The previous note that `[QΔt] = s` was wrong and has been corrected.

## Issue 2: Does re-anchoring always reduce uncertainty?

Status: Refined.

Potential problem:

Some wording says re-anchoring reduces uncertainty.

More precise general statement:

> Re-anchoring constrains or updates the belief state relative to continued non-observation. It may reduce uncertainty absolutely, but the safer claim is that it reduces uncertainty relative to the no-anchor trajectory.

Formal comparative form:

```text
P_{after action} < P_{no action trajectory}
```

not necessarily:

```text
P_{after action} < P_{before action}
```

The latter may hold for strong observations, but it should not be assumed universally.

## Issue 2a: Timer-specific dilution even under increasing absolute uncertainty

Status: Fixed as refinement.

In the timer model:

```text
τ = K + U + R
```

If `K` and `R` are known and `U` remains unchanged, then:

```text
Var(τ | K, R) = Var(U)
```

Therefore, restarting the count does not necessarily reduce absolute variance.

A stricter version also allows absolute uncertainty to increase:

```text
Var(U_{t+Δt}) = Var(U_t) + Q_U Δt
```

when:

```text
Q_U > 0
Δt > 0
```

So the most precise timer-specific claim is:

> Absolute uncertainty in `U` may remain or increase, while the relative influence of `U` can still decrease if the total reference scale grows faster than the uncertainty scale.

A relative uncertainty ratio can be defined as:

```text
ρ = sqrt(Var(U)) / E[τ]
```

Since:

```text
E[τ] = K + E[U] + R
```

`ρ` can decrease as `R` increases when `sqrt(Var(U))` grows more slowly than `E[τ]`.

Fixed-bound case:

If a fixed upper time bound `T` exists and the bound has not been reached, then:

```text
K + U + R < T
```

so:

```text
U < T - K - R
```

In that case, increasing `R` also tightens the upper bound on `U`.

## Issue 3: Is `R` perfectly known?

Status: Watch.

In the timer model:

```text
τ = K + U + R
```

`R` is often treated as observed.

However, real counting may be noisy. The strict version should distinguish:

```text
R_true
R_observed
```

or introduce measurement noise.

Current repository status:

The minimal model treats `K` and `R` as known or low-noise observations. This is acceptable for the initial theory, but the assumption should stay explicit.

## Issue 4: Is `P_t` variance, covariance, entropy, or a general uncertainty functional?

Status: Open.

Current formulation:

```text
P_t = Var(S_t | D_t)
```

This works for scalar or vector states under a variance/covariance interpretation.

However, if the model is generalized, uncertainty could also be represented by:

- entropy;
- credible interval width;
- expected decision error;
- posterior dispersion;
- general uncertainty functional.

Current recommendation:

Keep the minimal version as variance/covariance. Add a later generalization using `U_t` or `𝓤_t` as an uncertainty functional if needed.

## Issue 5: Constant `Q` is a simplification

Status: Watch.

The equation:

```text
P_{t+Δt} = P_t + QΔt
```

assumes a simple linear diffusion rate.

In real domains, `Q` may depend on:

- task complexity;
- environmental volatility;
- memory decay;
- emotional load;
- external dependencies;
- prior uncertainty.

Possible future generalization:

```text
P_{t+Δt} = P_t + ∫ Q(s) ds
```

or:

```text
P_{t+Δt} = f(P_t, Q, Δt)
```

## Issue 6: Action value uses utility units

Status: Watch.

The equation:

```text
V(a) = I(a) + B(a) - C(a)
```

requires all terms to be on a shared utility scale.

This is acceptable as a decision-theoretic abstraction, but not a direct physical equation.

## Issue 7: Cognitive uncertainty versus physical state change

Status: Open.

Uncertainty diffusion may mean either:

1. the world physically changed; or
2. the agent's knowledge became less reliable; or
3. both.

The model should eventually distinguish:

```text
state dynamics
belief uncertainty dynamics
```

Current formulation intentionally focuses on belief uncertainty.

## Issue 8: Novelty claim

Status: Watch.

UDAM should not claim full mathematical originality.

Safe claim:

> UDAM is a timer-derived cognitive and decision-theoretic formulation that integrates uncertainty diffusion, re-anchoring, and small informative action into a practical theory of recovery after anchor loss.

Unsafe claim:

> UDAM is an entirely new mathematical theory of uncertainty.

## Issue 9: Medical or crisis interpretation

Status: Watch.

Health and life-strategy examples can be misread as self-treatment advice.

Boundary:

UDAM can describe small information actions, but it does not replace professional care, crisis support, or safety behavior.

## Issue 10: `I(a)` versus `OV`

Status: Watch.

`I(a)` was initially used as a general informational value term.

The observability layer refines this by defining a more specific quantity:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Recommended reading:

- `I(a)` is the broad informational value term in the action-value equation.
- `OV` is a decision-theoretic refinement of informational value for observation-specific actions.

Do not double-count them in the same equation unless the model explicitly decomposes `I(a)`.

## Issue 11: Observability value versus compulsive checking

Status: Watch.

Observation is not automatically valuable.

The condition is:

```text
OV > 0
```

This means the value of improved conditional action must exceed observation cost.

If observation is repetitive, noisy, expensive, or non-actionable, then:

```text
OV <= 0
```

and UDAM does not favor it.

## Issue 12: `G`, `B(a)`, and `B_state` notation collision

Status: Fixed as naming caution.

The model uses:

```text
B(a)
```

for intervention value.

The observability layer may classify latent states as favorable or unfavorable. To avoid collision:

- use `G` only as a local label for favorable state;
- use `B_state` for unfavorable state;
- avoid writing `B` alone for a state label.

## Issue 13: `pi_hat` versus fixed-target assumption

Status: Watch.

The core timer model assumes:

```text
fixed target, uncertain position
```

In that core model, target relevance is effectively treated as fixed.

`pi_hat` is not a change to the core target condition. It is the agent's subjective discounting of the target's relevance.

Correct distinction:

```text
core model: fixed target
agent belief: pi_hat may be too low
```

The error region is:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

This means the core model favors re-anchoring, but the agent's discounted model does not.

## Current conclusion

The main structure remains coherent:

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

The main correction made during review was the timer-specific unit error for `QΔt`.

The main conceptual refinement is now two-layered:

1. timer re-anchoring can produce decreasing relative influence even when absolute uncertainty remains or increases;
2. observation can produce value by enabling better conditional action.

The main unresolved theoretical decision is whether `P_t` remains variance/covariance or becomes a more general uncertainty functional.
