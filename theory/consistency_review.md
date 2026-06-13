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

Status: Watch.

Potential problem:

Some wording says re-anchoring reduces uncertainty.

More precise statement:

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

## Current conclusion

The main structure remains coherent:

```text
τ = K + U + R
P_{t+Δt} = P_t + QΔt
V(a) = I(a) + B(a) - C(a)
```

The main correction made during review was the timer-specific unit error for `QΔt`.

The main unresolved theoretical decision is whether `P_t` remains variance/covariance or becomes a more general uncertainty functional.
