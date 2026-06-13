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

## 3. Why not generalize immediately?

The timer model is easiest to understand using variance-like uncertainty.

Premature generalization may make the theory harder to read.

Current recommendation:

> Keep `P_t` as variance/covariance in the main theory. Add `𝓤_t` later as an extension.

## 4. Observation update after re-anchoring

The current model uses the simple comparative idea:

```text
P_after_action < P_no_action_trajectory
```

A stricter Bayesian update could be written as:

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

The timer model requires a special distinction.

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

A representative ratio is:

```text
ρ(R) = sqrt(Var(U)) / E[τ]
```

because:

```text
E[τ] = K + E[U] + R
```

Thus timer re-anchoring should be described as **relative uncertainty dilution** unless there is an additional observation that tightens `U`.

A fixed upper time bound provides such an additional constraint:

```text
K + U + R < T
```

which implies:

```text
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

This extension is intentionally deferred because it weakens the minimal timer argument by mixing occurrence uncertainty with position uncertainty.

## 7. Controllability boundary

UDAM is an action-oriented model.

The core theory should include only uncertainty that action can affect through at least one of:

- observation;
- belief update;
- decision improvement;
- state intervention.

Uncontrollable external uncertainty should be treated as:

- outside the core model;
- an external parameter;
- a separate extension;
- or an exception condition.

This boundary prevents uncontrollable occurrence uncertainty from weakening the core re-anchoring argument.

## 8. Diminishing information value

Repeated checking should be modeled with declining marginal information:

```text
I(a_1) >= I(a_2) >= ... >= I(a_n)
```

If:

```text
I(a_n) + B(a_n) < C(a_n)
```

then repeated checking becomes unfavorable.

## 9. State change versus belief change

UDAM currently focuses on belief uncertainty.

However, an unobserved interval may involve two processes:

```text
state dynamics: S_t changes
belief dynamics: uncertainty about S_t changes
```

A later formal version should separate these.

## 10. Stronger state-space version

A more standard state-space form would be:

```text
S_{t+Δt} = F S_t + w_t
w_t ~ noise(Q)
y_t = H S_t + v_t
v_t ~ noise(R_obs)
```

UDAM does not need this form initially, but it connects the model to existing filtering theory.

## 11. Formal priority list

1. Keep timer model clean.
2. Preserve `P_t` as variance/covariance in the minimal theory.
3. Add optional `𝓤_t` generalization later.
4. Make all claims about re-anchoring comparative unless strong observation is assumed.
5. In the timer model, distinguish absolute uncertainty from relative uncertainty dilution.
6. Keep fixed-target scope in the core timer model.
7. Keep uncontrollable external uncertainty outside the core action-value argument.
8. Distinguish empty activity from informative action.
