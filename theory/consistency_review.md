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

Status: Fixed as representation decision.

Core formulation:

```text
P_t = Var(S_t | D_t)
```

or, for vector states:

```text
P_t = Cov(S_t | D_t)
```

Future extension:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

Decision:

Core UDAM uses variance/covariance-like belief uncertainty. A general uncertainty functional is allowed as a future extension, but it is not part of the minimal model.

See:

- `theory/uncertainty_representation.md`

## Issue 5: Constant `Q` is a simplification

Status: Refined.

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

Current decomposition:

```text
Q_total = Q_state + Q_memory + Q_dependency + Q_context
```

`Q > 0` should be assumed only when unobserved time can reduce the reliability of belief about the relevant state.

See:

- `theory/diffusion_rate_conditions.md`

## Issue 6: Action value uses utility units

Status: Watch.

The equation:

```text
V(a) = I(a) + B(a) - C(a)
```

requires all terms to be on a shared utility scale.

This is acceptable as a decision-theoretic abstraction, but not a direct physical equation.

## Issue 7: Cognitive uncertainty versus physical state change

Status: Refined.

Uncertainty diffusion may mean either:

1. the world physically changed; or
2. the agent's knowledge became less reliable; or
3. both.

The model distinguishes:

```text
state dynamics
belief uncertainty dynamics
```

Current formulation intentionally focuses on belief uncertainty while allowing state-dynamics components through `Q_state`.

## Issue 8: Novelty claim

Status: Watch.

UDAM should not claim full mathematical originality.

Safe claim:

> UDAM is a timer-derived cognitive and decision-theoretic formulation that integrates uncertainty diffusion, re-anchoring, state-informative observation, adaptive expansion, and boundary-risk-constrained small informative actions into a practical theory of recovery after anchor loss.

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

Status: Refined.

Observation is not automatically valuable.

The condition is:

```text
OV > 0
```

For repeated observation, the marginal condition is:

```text
MOV_i > 0
```

If observation is repetitive, noisy, expensive, or non-actionable, then UDAM does not favor it.

See:

- `theory/diminishing_information_value.md`

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

## Issue 14: Valid re-anchor condition

Status: Fixed as refinement.

Potential problem:

UDAM can be misread as saying that any small action is useful.

Correction:

A valid re-anchor must be state-informative.

Formal condition:

```text
P(y | S) != P(y)
```

Posterior-change form:

```text
P(S | y) != P(S)
```

Practical reading:

```text
small action is not enough
small state-informative observation is required
```

The timer seed model satisfies this because `R` is part of the elapsed-position decomposition:

```text
τ = K + U + R
```

See:

- `theory/valid_reanchor_condition.md`

## Issue 15: Conditional action switch and Monty Hall analogy

Status: Fixed as refinement.

The Monty Hall analogy should not be read as a claim that UDAM is the Monty Hall problem.

The useful relation is structural:

```text
hidden state -> state-informative observation -> conditional action switch
```

In UDAM notation:

```text
a(y) != a_0
```

for at least one possible observation result.

The observation has decision value when it can rationally change the next action and when cost is justified:

```text
OV > 0
```

This prevents the practical protocol from becoming vague checking.

See:

- `theory/conditional_action_switch.md`
- `docs/08_related_work.md`

## Issue 16: Adaptive expansion factor can be misread as always-expand

Status: Fixed as refinement.

Potential problem:

The expansion pattern:

```text
1 -> 2 -> 4 -> 8
```

can be misread as a universal rule.

Correction:

Expansion is favorable only when expansion value exceeds observation, correction, and boundary-risk costs:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

The boundary term is essential:

```text
P_boundary(i) * C_boundary
```

Practical reading:

```text
doubling is a possible default, not a universal optimum
```

and:

```text
expand only as far as adverse-boundary risk allows
```

See:

- `docs/18_adaptive_expansion_factor.md`
- `theory/propositions.md` Proposition 13

## Current conclusion

The main structure remains coherent:

```text
τ = K + U + R
P_t = Var(S_t | D_t)
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
MOV_i > 0
P(y | S) != P(y)
P(S | y) != P(S)
a(y) != a_0
s_{i+1} = r_i s_i
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

The main correction made during review was the timer-specific unit error for `QΔt`.

The main conceptual refinement is now six-layered:

1. timer re-anchoring can produce decreasing relative influence even when absolute uncertainty remains or increases;
2. observation can produce value by enabling better conditional action;
3. repeated observation is useful only while marginal value remains positive;
4. a valid re-anchor must be state-informative;
5. useful observation can justify conditional action switching;
6. geometric expansion is useful only when boundary-risk-constrained expansion value is positive.

The core representation decision is closed:

```text
core: P_t = Var(S_t | D_t) or Cov(S_t | D_t)
extension: 𝓤_t = 𝓤(p(S_t | D_t))
```
