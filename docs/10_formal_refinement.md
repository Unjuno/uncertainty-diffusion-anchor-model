# 10 Formal Refinement

This document records the next formal refinements required for UDAM.

## 1. Minimal version

The current minimal version uses variance or covariance:

```text
P_t = Var(S_t | D_t)
```

and diffusion:

```text
P_{t+Δt} = P_t + QΔt
```

This is sufficient for the timer-derived model.

## 2. Generalized uncertainty functional

A later version may replace `P_t` with a more general uncertainty functional:

```text
𝓤_t = 𝓤(p(S_t | D_t))
```

Possible choices:

- variance;
- covariance determinant;
- entropy;
- credible interval width;
- expected decision error;
- probability of being in a critical region.

## 3. Observation update after re-anchoring

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

## 4. Timer-specific refinement: relative dilution

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

## 5. Fixed-target scope

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

## 6. Controllability boundary

UDAM is an action-oriented model.

The core theory should include only uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable external uncertainty should be treated as outside the core model, an external parameter, a separate extension, or an exception condition.

## 7. Observability value

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

## 8. Fixed-target disbelief

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

## 9. Diminishing information value

Repeated checking should be modeled with declining marginal information:

```text
I(a_1) >= I(a_2) >= ... >= I(a_n)
```

If:

```text
I(a_n) + B(a_n) < C(a_n)
```

then repeated checking becomes unfavorable.

## 10. State change versus belief change

UDAM currently focuses on belief uncertainty.

However, an unobserved interval may involve two processes:

```text
state dynamics: S_t changes
belief dynamics: uncertainty about S_t changes
```

## 11. Stronger state-space version

A more standard state-space form would be:

```text
S_{t+Δt} = F S_t + w_t
w_t ~ noise(Q)
y_t = H S_t + v_t
v_t ~ noise(R_obs)
```

UDAM does not need this form initially, but it connects the model to existing filtering theory.

## 12. Formal priority list

1. Keep timer model clean.
2. Preserve `P_t` as variance/covariance in the minimal theory.
3. Add optional `𝓤_t` generalization later.
4. Make all claims about re-anchoring comparative unless strong observation is assumed.
5. Distinguish absolute uncertainty from relative uncertainty dilution.
6. Keep fixed-target scope in the core timer model.
7. Keep uncontrollable external uncertainty outside the core action-value argument.
8. Treat observability value as conditional-action value, not automatic benefit.
9. Keep fixed-target disbelief as a subjective discounting error, not a change in the core target condition.
10. Distinguish empty activity from informative action.
