# Logical Synthesis Review

This document reviews whether the current UDAM layers fit together without contradiction.

Status:

```text
No major internal contradiction found.
```

However, several distinctions must remain explicit to prevent misreading.

## 1. Core synthesis

The current model is logically organized around the timer seed structure:

```text
τ = K + U + R
```

This supports the core claim:

```text
partial uncertainty does not imply total invalidation
```

or:

```text
anchor loss does not imply future anchor invalidation
```

The later layers are consistent with this core if they are read as refinements, not replacements.

## 2. Current layer stack

The current UDAM stack is:

```text
1. timer seed model
2. belief uncertainty diffusion
3. action value
4. observability value
5. valid re-anchor condition
6. conditional action switch
7. repeated observation stopping rule
8. adaptive expansion factor
9. boundary-risk constraint
10. positioning as practical synthesis
```

Each layer answers a different question.

| Layer | Question |
|---|---|
| timer seed model | Does a lost interval invalidate later anchors? |
| uncertainty diffusion | Does uncertainty grow without anchors? |
| action value | Is the action worth taking? |
| observability value | Is observation worth making? |
| valid re-anchor condition | Is the observation state-informative? |
| conditional switch | Can observation change action? |
| repeated observation | Is another observation still useful? |
| expansion factor | How much should scope expand? |
| boundary-risk constraint | Can expansion happen before adverse boundary risk dominates? |
| positioning | Is UDAM a practical synthesis rather than a new foundation? |

This structure is coherent because no layer requires denying a previous layer.

## 3. No contradiction: fixed target versus observability

The timer seed model assumes:

```text
fixed target, uncertain position
```

The observability layer introduces hidden state `S` and observation `y`.

This does not contradict the fixed-target scope.

The target condition can remain fixed while the agent's position or state relative to it remains uncertain.

Correct reading:

```text
fixed target condition
uncertain agent state or position
state-informative observation
```

Incorrect reading:

```text
UDAM now models whether the target itself occurs
```

Target occurrence uncertainty remains outside the core model unless a separate event-occurrence layer is added.

## 4. No contradiction: re-anchor does not always reduce absolute uncertainty

A re-anchor can be useful even if it does not reduce absolute uncertainty immediately.

Safe comparative claim:

```text
P_after_action < P_no_action_trajectory
```

not necessarily:

```text
P_after_action < P_before_action
```

Timer-specific version:

```text
τ = K + U + R
```

`R` can be valid even if `Var(U)` remains or increases.

The claim is either:

```text
R remains valid information
```

or, under additional conditions:

```text
relative influence of U decreases
```

This is coherent with Propositions 1 and 6.

## 5. Important distinction: valid observation versus favorable observation

A valid re-anchor requires state-informativeness:

```text
P(y | S) != P(y)
```

This means the observation can update belief.

But validity alone does not imply favorable action.

A favorable observation additionally requires:

```text
OV > 0
```

Therefore:

```text
state-informative observation != automatically worth observing
```

The complete reading is:

```text
valid if state-informative
favorable if expected decision value exceeds cost
```

This distinction prevents a contradiction between Proposition 11 and Proposition 9.

## 6. Important distinction: I(a) versus OV

`I(a)` is a broad informational value term inside:

```text
V(a) = I(a) + B(a) - C(a)
```

`OV` is a more specific observability-value expression:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

They should not be added together unless the model explicitly decomposes them.

Correct reading:

```text
I(a) = broad informational value
OV = decision-theoretic refinement for observation-specific actions
```

Incorrect reading:

```text
V(a) = I(a) + OV + B(a) - C(a)
```

This would risk double-counting.

## 7. Important distinction: first observation versus repeated observation

The first valid observation can be valuable because it breaks observation rate zero.

But repeated observation requires marginal value:

```text
MOV_i > 0
```

Therefore:

```text
first observation may be justified
repeated checking is not automatically justified
```

This is coherent with the checking-loop failure cases.

## 8. Important distinction: expansion versus automatic doubling

Adaptive expansion uses:

```text
s_{i+1} = r_i s_i
```

with:

```text
r_i >= 1
```

A common pattern is:

```text
1 -> 2 -> 4 -> 8
```

But this is not a universal rule.

Expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Watch item:

The phrase "reduce `r_i`" should mean:

```text
choose a smaller expansion factor, closer to 1
```

not necessarily:

```text
shrink the current scope
```

If future versions need actual contraction, introduce a separate shrinkage rule or allow:

```text
0 < r_i < 1
```

Currently, the model treats contraction as:

```text
keep scope small or switch probe
```

not as part of the expansion equation.

## 9. Important distinction: local observation versus global conclusion

UDAM favors local observations after anchor loss.

But local observations should update local beliefs.

Failure pattern:

```text
one local result -> total self/world/project judgment
```

Correct reading:

```text
local observation updates local posterior
global judgment requires broader evidence
```

This does not contradict the practical protocol. It constrains its scope.

## 10. Important distinction: Q = 0 does not mean no action is useful

If:

```text
Q = 0
```

then the diffusion-based urgency weakens.

But action can still be justified by:

```text
I(a) + B(a) - C(a) > 0
```

or:

```text
OV > 0
```

Therefore:

```text
no uncertainty diffusion != no action value
```

This keeps the diffusion layer and action-value layer consistent.

## 11. Important distinction: state dynamics versus belief dynamics

UDAM is primarily about belief uncertainty:

```text
P_t = Var(S_t | D_t)
```

It does not claim:

```text
inaction always worsens S_t
```

The correct claim is:

```text
lack of anchors may increase uncertainty about S_t
```

State change can be included as a component of diffusion:

```text
Q_state
```

but it is not the whole model.

## 12. Logical dependency map

A clean dependency structure is:

```text
τ = K + U + R
    -> lost interval does not invalidate future anchor

P_t = Var(S_t | D_t)
P_{t+Δt} = P_t + QΔt
    -> belief uncertainty can diffuse without anchors

V(a) = I(a) + B(a) - C(a)
    -> action is favorable if value is positive

P(y | S) != P(y)
    -> observation is state-informative

a(y) != a_0
OV > 0
    -> observation can justify conditional action

MOV_i > 0
    -> repeated observation remains useful

s_{i+1} = r_i s_i
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
    -> expansion is favorable under boundary-risk constraint
```

No step requires the stronger claim that all action is good, all observation is good, or all expansion is good.

## 13. Watch items

The following are not contradictions, but should remain marked as watch items.

### 13.1 `I(a)` and `OV`

Do not double-count informational value.

### 13.2 `state-informative` and `favorable`

State-informative means belief-relevant. Favorable means cost-justified.

### 13.3 `doubling` and `optimal expansion`

Doubling is a possible heuristic, not a theorem.

### 13.4 `fixed target` and `π_hat`

The target is fixed in the core model. `π_hat` is subjective discounting by the agent, not target stochasticity.

### 13.5 `R` as known

The minimal timer model treats `R` as known or low-noise. A stricter model may split:

```text
R_true
R_observed
```

### 13.6 local versus global inference

Local observation should not be overextended into global conclusion.

## 14. Overall verdict

Current status:

```text
logically coherent with explicit boundary conditions
```

The model is strongest when stated as:

```text
UDAM is a timer-derived practical synthesis.
```

It should avoid claiming:

```text
all action is useful
all observation is useful
all uncertainty is bad
all expansion should be geometric
UDAM is a new mathematical foundation
```

The current repository already contains safeguards against these misreadings.

## 15. Next logical cleanup tasks

Recommended next cleanup items:

1. Link this review from `theory/README.md` and `README.md`.
2. Add a short Japanese counterpart later if needed.
3. If contraction becomes important, define a separate shrinkage rule instead of overloading `r_i`.
4. Continue treating literature references as verification candidates until checked.
