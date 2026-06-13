# 06 Failure Cases

UDAM is useful only if its boundary conditions are explicit.

This document summarizes the main failure cases. For stricter details, see:

- `theory/counterexamples.md`

## 1. No information

If an action does not return information and does not improve the state, it is not a re-anchor.

```text
I(a) = 0
B(a) = 0
```

If it has cost:

```text
C(a) > 0
```

then:

```text
V(a) < 0
```

Plain reading:

```text
activity without information or intervention value is not re-anchoring
```

## 2. State-uninformative observation

A small observation is not enough.

It must be connected to the relevant state.

A valid re-anchor requires:

```text
P(y | S) != P(y)
```

Failure case:

```text
P(y | S) = P(y)
```

Plain reading:

```text
the observation result tells the agent nothing about the state being estimated
```

Example:

```text
checking an unrelated metric while the actual uncertainty concerns task ability
```

## 3. Observation with no possible action change

Observation has decision value when it can support conditional action.

Useful-observation structure:

```text
a(y) != a_0
```

for at least one possible result `y`.

Failure case:

```text
a(y) = a_0
```

for all possible results.

Plain reading:

```text
if the agent will do the same thing regardless of the observation, the observation has little or no decision value
```

## 4. High cost

An informative action can still be bad if its cost is too high.

```text
C(a) > I(a) + B(a)
```

For observation-specific actions:

```text
OV <= 0
```

Plain reading:

```text
information is useful only if its expected decision value exceeds its cost
```

## 5. Misleading feedback

A measurement can reduce apparent uncertainty while increasing actual error if the feedback is biased, false, or systematically misread.

Failure pattern:

```text
apparent clarity -> wrong posterior -> worse action
```

This is not a failure of re-anchoring itself. It is a failure of signal reliability.

## 6. Repeated checking loop

Repeated checking may have diminishing informational value.

The repeated-observation condition is:

```text
MOV_i > 0
```

Failure case:

```text
MOV_i <= 0
```

Plain reading:

```text
the next check no longer changes belief or action enough to justify its cost
```

This prevents UDAM from becoming a justification for checking loops.

## 7. Wrong anchor

An action may anchor the wrong state variable.

Example:

```text
organizing notes when the actual uncertainty is whether one can solve problems
```

Failure pattern:

```text
valid observation of the wrong state -> false sense of re-anchoring
```

## 8. Non-diffusing belief uncertainty

If belief uncertainty does not grow without action, then urgent re-anchoring may not be necessary.

```text
Q = 0
```

This is not the same as saying that the external state cannot change.

It means that the relevant belief uncertainty is not currently diffusing in the modeled sense.

## 9. Relative dilution failure

In the timer model, absolute uncertainty may increase while relative influence decreases only under a growth-rate condition.

Let:

```text
ρ(R) = A(R) / B(R)
```

where:

```text
A(R) = sqrt(Var(U_R))
B(R) = E[τ]
```

Relative dilution can fail if `A(R)` grows as fast as or faster than `B(R)`.

In plain terms:

> If the unknown part grows in influence faster than the known reference scale expands, re-anchoring may not dilute the uncertainty enough.

## 10. Missing upper-bound condition

The upper-bound tightening result requires an actual upper bound.

Without:

```text
K + U + R < T
```

one cannot infer:

```text
U < T - K - R
```

Plain reading:

```text
fixed-bound conclusions require a fixed bound
```

## 11. Uncontrollable occurrence uncertainty

If the uncertainty concerns whether the target condition itself occurs, and that occurrence is not controllable by the agent, then it should not be mixed into the core timer model.

It should be treated as:

- outside the core model;
- an external parameter;
- a separate extension;
- or an exception condition.

Otherwise, the value of re-anchoring becomes diluted by occurrence uncertainty:

```text
V_reanchor ≈ P(event occurs) · V_position_update - C(a)
```

## 12. State-belief conflation

UDAM should not be read as saying:

> inaction always worsens the world.

The safer claim is:

> lack of anchors may increase uncertainty about the current state.

A correct application separates:

```text
state dynamics
belief dynamics
```

## 13. Excessive expansion factor

After a favorable probe, expansion can be useful:

```text
s_{i+1} = r_i s_i
```

But expansion fails when:

```text
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Plain reading:

```text
the expanded scope costs more than its benefit and information value justify
```

This includes the case where doubling is treated as automatic.

```text
1 -> 2 -> 4 -> 8
```

is a possible pattern, not a universal rule.

## 14. Boundary-risk underestimation

A major expansion error is underestimating:

```text
P_boundary(i) * C_boundary
```

Failure pattern:

```text
previous scope was safe -> next scope is assumed safe -> boundary risk is ignored
```

Correct reading:

```text
no boundary crossing in the previous scope is evidence, not proof of safety in the next scope
```

## 15. Irreversible action with large expansion

When an action is hard to reverse, the expansion factor should usually be smaller.

Failure pattern:

```text
low reversibility + large expansion + weak observation
```

This is especially important when correction cost is high:

```text
C_correct(r_i) >> 0
```

## 16. Local observation used as global conclusion

UDAM favors local observations.

But a local observation should not be turned into a global conclusion too quickly.

Failure pattern:

```text
one local result -> total self/world/project judgment
```

Examples:

```text
one failed problem -> I cannot learn this at all
one awkward response -> the whole relationship is over
one blocked task -> the whole project is impossible
```

Correct reading:

```text
local observation updates local belief; global conclusions require broader evidence
```

## 17. Safety-critical delay

In urgent safety-critical contexts, measurement can be inferior to immediate action.

UDAM does not justify delaying protective behavior for more information.

The relevant failure pattern is:

```text
more measurement -> delayed necessary action
```

## Boundary rule

The model supports only actions satisfying:

```text
I(a) + B(a) > C(a)
```

Observation-specific actions should satisfy:

```text
OV > 0
```

Repeated observations should satisfy:

```text
MOV_i > 0
```

Expansion should satisfy:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

It does not support activity, checking, observation, or expansion as such.
