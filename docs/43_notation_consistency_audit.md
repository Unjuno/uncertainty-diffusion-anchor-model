# 43 Notation Consistency Audit

This document records a first-pass notation consistency audit for UDAM.

The purpose is not to add new theory.

The purpose is to keep the existing timer, uncertainty, action-value, observation-value, marginal-observation, and expansion layers readable and internally consistent before any later paper draft cleanup.

## Audit status

Status:

```text
first-pass complete
```

Scope:

```text
README.md
docs/00_overview.md
docs/01_timer_model.md
docs/02_uncertainty_diffusion.md
docs/03_reanchoring.md
docs/04_action_value.md
docs/05_propositions.md
docs/10_formal_refinement.md
docs/16_adaptive_observation_cadence.md
docs/18_adaptive_expansion_factor.md
docs/21_failure_decision_tree.md
theory/variables.md
theory/propositions.md
theory/proofs.md
theory/logical_synthesis_review.md
```

This audit is a routing and consistency note. It does not supersede `theory/variables.md`, `theory/propositions.md`, or `theory/proofs.md`.

## 1. Timer notation

Canonical timer expression:

```text
τ = K + U + R
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `τ` | current elapsed time or current position in the timer seed model | stable |
| `K` | known interval before anchor loss | stable |
| `U` | unknown interval during anchor loss | stable |
| `R` | re-anchored interval after restart | stable |

Consistency decision:

```text
Keep tau/τ as the timer seed symbol only.
Do not reuse τ for unrelated stopping time or threshold notation without explicit local definition.
```

Guardrail:

```text
U remains uncertain; R remains meaningful.
```

Avoid:

```text
R eliminates U.
R proves the whole timeline.
```

## 2. Uncertainty diffusion notation

Canonical expression:

```text
P_{t+Δt} = P_t + QΔt
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `P_t` | uncertainty measure at time `t`, usually variance/covariance-like in the current core | stable with scope note |
| `Q` | diffusion or uncertainty-growth rate | stable with scope note |
| `Δt` | elapsed time increment | stable |

Consistency decision:

```text
Use P_t for the core variance/covariance-like uncertainty layer.
Use any generalized uncertainty functional only when the local document defines it explicitly.
```

Guardrail:

```text
P_t describes belief uncertainty, not necessarily physical state change.
```

Avoid:

```text
P_t always means entropy.
P_t always means scalar variance.
Q > 0 in every domain.
```

## 3. Re-anchor validity notation

Canonical local informativeness checks:

```text
P(y | S) != P(y)
```

and equivalently:

```text
P(S | y) != P(S)
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `S` | relevant hidden state | stable |
| `y` | observation result | stable |
| `P(y | S)` | observation distribution conditional on state | stable |
| `P(y)` | marginal observation distribution | stable |
| `P(S | y)` | posterior belief after observation | stable |
| `P(S)` | prior belief before observation | stable |

Consistency decision:

```text
Use these as local state-informativeness conditions, not as the full Blackwell order.
```

Guardrail:

```text
state-informative != favorable
```

Avoid:

```text
P(y | S) != P(y) proves the action is useful.
P(y | S) != P(y) proves Blackwell superiority.
```

## 4. Action-value notation

Canonical expression:

```text
V(a) = I(a) + B(a) - C(a)
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `a` | action | stable |
| `V(a)` | net action value | stable |
| `I(a)` | information value of action | stable with caution |
| `B(a)` | non-informational benefit of action | stable |
| `C(a)` | action cost | stable |

Consistency decision:

```text
Use V(a) for action value.
Do not use V(a) as the observation-value expression when conditional observation is central.
```

Guardrail:

```text
I(a) is not automatically expected free energy.
I(a) contributes to value only through the current UDAM action-value decomposition unless a formal mapping is provided.
```

Avoid:

```text
I(a) > 0 implies V(a) > 0.
Information-seeking action is automatically favorable.
```

## 5. Observation-value notation

Canonical expression:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `OV` | observation value after observation cost | stable |
| `E_y[...]` | expectation over possible observation results | stable |
| `S` | hidden state relevant to the decision | stable |
| `V(a, S)` | state-dependent value of action `a` | stable with local definition |
| `C(obs)` | cost of observing | stable |

Consistency decision:

```text
Use OV when the point is whether observing before acting is worthwhile.
Use V(a) when the point is whether a specific action is worthwhile.
```

Guardrail:

```text
OV > 0 means the observation is favorable under the stated model and cost.
It does not mean every possible observation sequence remains favorable.
```

Avoid:

```text
state-informative observation always has positive OV.
more information is always better.
```

## 6. Conditional action notation

Canonical expression:

```text
a(y) != a_0
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `a(y)` | action selected after observing result `y` | stable |
| `a_0` | default action without observation | stable |

Consistency decision:

```text
Use a(y) != a_0 as a decision-relevance condition.
Do not use it as a sufficient condition for positive value.
```

Guardrail:

```text
action-changing != favorable
```

Avoid:

```text
Any observation that changes action is worth taking.
```

## 7. Marginal observation notation

Canonical expression:

```text
MOV_i > 0
```

Failure boundary:

```text
MOV_i <= 0
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `MOV_i` | marginal observation value at observation step `i` | stable enough for practical layer |
| `i` | observation or expansion step index, locally defined | stable with local scope note |

Consistency decision:

```text
Use MOV_i for repeated-observation decisions.
Use OV for the first or general observation-value decision.
```

Guardrail:

```text
MOV_i <= 0 means stop or change the current observation mode.
It does not prove that every possible future observation is worthless.
```

Avoid:

```text
The first useful check justifies indefinite checking.
MOV_i is Wald's stopping rule.
```

## 8. Expansion notation

Canonical expressions:

```text
s_{i+1} = r_i s_i
```

and:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Recommended meanings:

| Symbol | Meaning | Status |
|---|---|---|
| `s_i` | current action or observation scope at step `i` | stable |
| `r_i` | expansion factor from `s_i` to `s_{i+1}` | stable |
| `B_expand(r_i)` | expected benefit from expansion factor `r_i` | stable |
| `I_expand(r_i)` | expected information gain from expansion factor `r_i` | stable |
| `C_obs(r_i)` | observation cost under expansion factor `r_i` | stable |
| `P_boundary(i)` | probability of crossing or hitting an adverse boundary at step `i` | stable with modeling caution |
| `C_boundary` | cost of adverse boundary crossing | stable |
| `C_correct(r_i)` | correction or reversal cost after expansion | stable |

Consistency decision:

```text
Use r_i as a selected expansion factor.
Do not silently equate r_i with 2.
```

Guardrail:

```text
local success != global expansion permission
```

Avoid:

```text
Double after success.
A favorable local probe justifies global expansion.
```

## 9. Indexing convention

Current convention:

```text
i indexes local observation, checking, or expansion steps depending on the document.
```

Consistency decision:

```text
When a document uses i, define whether i indexes observations, expansion steps, or both.
Avoid mixing observation index and expansion index in the same paragraph unless explicitly stated.
```

This is the main notation weakness found in this first-pass audit.

Recommended future cleanup:

```text
If a paper draft requires tighter notation, consider using j for observation count and i for expansion step.
Do not change repository-wide notation yet unless the maintainer requests a formal notation refactor.
```

## 10. Current risk register

| Risk | Severity | Correction |
|---|---:|---|
| `i` can index both observation and expansion steps | medium | define local index role in each document |
| `P_t` can be overread as entropy or scalar variance | medium | preserve variance/covariance-like scope note |
| `I(a)` can be overread as active-inference expected free energy | medium | require formal mapping before equating them |
| `OV` can be confused with `V(a)` | medium | use OV for observe-before-act decisions and V for direct action value |
| `r_i` can be misread as automatic doubling | high | state that `r_i` is selected and boundary-risk constrained |
| `MOV_i <= 0` can be overread as all future observation worthless | medium | specify current observation mode only |

## 11. Result

First-pass notation audit result:

```text
No notation conflict currently breaks the model.
```

But the following cleanup should be done before a paper-style draft:

```text
1. Define index roles locally when using i.
2. Keep P_t scoped to the core uncertainty layer.
3. Keep I(a), OV, and MOV_i distinct.
4. Keep r_i as selected expansion factor, not automatic doubling.
5. Route formal notation changes through theory/ first.
```

## 12. Repository status update

This audit supports the existing v1.0 roadmap item:

```text
audit notation consistency across timer, action-value, observability, and expansion layers
```

Status after this document:

```text
notation consistency audit: first-pass complete
formal notation refactor: not performed
paper-level notation tightening: still optional / future work
```
