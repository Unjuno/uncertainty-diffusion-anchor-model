# 10 Formal Refinement

This document records the next formal refinements required for UDAM.

## 1. Core uncertainty representation

The current core version uses variance or covariance-like belief uncertainty.

Scalar form:

```text
P_t = Var(S_t | D_t)
```

Vector form:

```text
P_t = Cov(S_t | D_t)
```

This is the representation used in the minimal theory.

## 2. Generalized uncertainty functional

A later version may replace or supplement `P_t` with a more general uncertainty functional:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

Possible choices:

- variance;
- covariance determinant;
- entropy;
- credible interval width;
- expected decision error;
- probability of being in a critical region;
- expected value loss from uncertainty.

This is a future extension, not the core representation.

## 3. Diffusion-rate conditions

UDAM should not assume positive diffusion merely because time passes.

The minimal diffusion equation is:

```text
P_{t+Δt} = P_t + QΔt
```

A positive diffusion rate is appropriate when unobserved time can make the agent's belief about the relevant state less reliable.

A practical decomposition is:

```text
Q_total = Q_state + Q_memory + Q_dependency + Q_context
```

where:

- `Q_state` comes from latent state change;
- `Q_memory` comes from memory or calibration decay;
- `Q_dependency` comes from unobserved dependency changes;
- `Q_context` comes from task or decision context loss.

Positive diffusion is assumed when:

```text
Q_total > 0
```

If:

```text
Q_total = 0
```

then the diffusion-prevention argument weakens. Re-anchoring may still be justified by direct information value, observability value, or intervention value.

## 4. Observation update after re-anchoring

A stricter Bayesian update can be written as:

```text
p(S_t | D_t, y_a)
```

where `y_a` is the observation returned by action `a`.

In variance form:

```text
P_t^+ = Var(S_t | D_t, y_a)
```

A strong re-anchor satisfies:

```text
P_t^+ < P_t^-
```

A weak re-anchor may only satisfy:

```text
P_t^+ < P_{no-action}
```

## 5. Timer-specific refinement: relative dilution

If:

```text
τ = K + U + R
```

and `K` and `R` are observed while `U` is uncertain, then adding `R` does not necessarily reduce:

```text
Var(U)
```

Absolute uncertainty may remain or increase.

Relative influence may still decrease if the reference scale grows faster than the uncertainty scale.

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

A fixed upper time bound provides an additional constraint:

```text
K + U + R < T
U < T - K - R
```

## 6. Fixed-target scope

The timer seed model assumes:

```text
fixed target, uncertain position
```

It does not model:

```text
uncertain target, uncertain position
```

A stochastic target-occurrence extension would require at least:

```text
P(target occurs)
P(position | target occurs)
```

and would change the action-value structure:

```text
V(a) = P(target occurs) · I_position(a) + B(a) - C(a)
```

This extension is deferred because it mixes occurrence uncertainty with position uncertainty.

## 7. Controllability boundary

UDAM is an action-oriented model.

The core theory should include only uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable external uncertainty should be treated as outside the core model, an external parameter, a separate extension, or an exception condition.

## 8. Observability value

Observation can be valuable even when it does not directly improve the state.

Its value comes from enabling better conditional action.

Without observation:

```text
V_no_obs = max_a E[V(a, S)]
```

With observation:

```text
V_obs = E_y[max_a E[V(a, S) | y]] - C(obs)
```

Define observability value:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

This formalizes why re-anchoring can reveal both hidden upside and hidden downside.

The value is not that observation makes the world better. The value is that it separates states and enables action conditional on the observed state.

## 9. Fixed-target disbelief

In the fixed-target core model, positional information has value:

```text
V_reanchor_core = I_position(a) + B(a) - C(a)
```

If the agent discounts the target with subjective relevance weight `pi_hat`, then perceived value becomes:

```text
V_reanchor_perceived = pi_hat * I_position(a) + B(a) - C(a)
```

A re-anchor can be favorable in the core model but skipped by the agent when:

```text
pi_hat * I_position(a) + B(a) <= C(a) < I_position(a) + B(a)
```

This is the formal region for fixed-target disbelief.

## 10. Diminishing information value

Repeated checking should be modeled with declining marginal information:

```text
I_1 >= I_2 >= ... >= I_n >= 0
```

Each repeated action is favorable only if:

```text
I_i + B_i - C_i > 0
```

The stopping condition is:

```text
I_i + B_i <= C_i
```

For observation-specific actions, define marginal observability value:

```text
MOV_i = E_y[max_a E[V(a,S) | y, D_i]] - max_a E[V(a,S) | D_i] - C(obs_i)
```

Repeated observation `i` is favorable only when:

```text
MOV_i > 0
```

Thus, UDAM favors repeated observation only while each additional observation changes belief, decision, or state enough to exceed cost.

This prevents the model from justifying checking loops.

## 11. State change versus belief change

UDAM currently focuses on belief uncertainty.

However, an unobserved interval may involve two processes:

```text
state dynamics: S_t changes
belief dynamics: uncertainty about S_t changes
```

## 12. Stronger state-space version

A more standard state-space form would be:

```text
S_{t+Δt} = F S_t + w_t
w_t ~ noise(Q)
y_t = H S_t + v_t
v_t ~ noise(R_obs)
```

UDAM does not need this form initially, but it connects the model to existing filtering theory.

## 13. Formal priority list

1. Keep timer model clean.
2. Use `P_t = Var(S_t | D_t)` or `Cov(S_t | D_t)` in the core model.
3. Reserve `𝓤_t = 𝓤(p(S_t | D_t))` for future extension.
4. Assume `Q > 0` only when unobserved time can reduce belief reliability.
5. Make all claims about re-anchoring comparative unless strong observation is assumed.
6. Distinguish absolute uncertainty from relative uncertainty dilution.
7. Keep fixed-target scope in the core timer model.
8. Keep uncontrollable external uncertainty outside the core action-value argument.
9. Treat observability value as conditional-action value, not automatic benefit.
10. Keep fixed-target disbelief as a subjective discounting error, not a change in the core target condition.
11. Treat repeated checking as favorable only while marginal information value remains positive.
12. Distinguish empty activity from informative action.
