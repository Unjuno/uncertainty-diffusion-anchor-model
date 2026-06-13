# Counterexamples and Failure Cases

UDAM is not a universal justification for action.

This file lists conditions under which the model weakens or fails.

## C1. No information

If an action returns no state information:

```text
I(a) = 0
```

and does not improve the state:

```text
B(a) = 0
```

then the action is not a re-anchor.

If cost is positive:

```text
C(a) > 0
```

then:

```text
V(a) < 0
```

## C2. State-uninformative observation

A valid re-anchor must be state-informative.

Required condition:

```text
P(y | S) != P(y)
```

Counterexample condition:

```text
P(y | S) = P(y)
```

Then:

```text
P(S | y) = P(S)
```

So the observation does not update the belief about the relevant state.

This fails Proposition 11.

## C3. Observation with no conditional action change

Observation has decision value when it can support a different action under at least one possible observation result.

Useful condition:

```text
a(y) != a_0
```

Counterexample condition:

```text
a(y) = a_0
```

for all possible `y`.

In that case, the observation may still have psychological value, but its decision value is weak or zero inside the UDAM observability layer.

This weakens Proposition 12.

## C4. High cost

If:

```text
C(a) > I(a) + B(a)
```

then:

```text
V(a) < 0
```

The action is unfavorable even if it returns some information.

For observation-specific actions, the equivalent failure condition is:

```text
OV <= 0
```

## C5. Misleading feedback

If an action returns systematically false information, it can reduce apparent uncertainty while increasing actual error.

Example:

- unreliable measurement;
- biased feedback;
- deceptive social signal;
- self-serving interpretation.

Failure pattern:

```text
signal looks informative -> posterior moves in the wrong direction -> action worsens
```

UDAM requires signal relevance and sufficient reliability. State-informativeness alone is not enough if the signal is systematically distorted.

## C6. Repeated checking loop

Repeated checking may have rapidly diminishing informational value.

The repeated-observation condition is:

```text
MOV_i > 0
```

Counterexample condition:

```text
MOV_i <= 0
```

If repeated checking has no marginal decision value while cost remains positive, it becomes unfavorable.

A weaker but common representation is:

```text
I(a_n) -> 0
C(a_n) > 0
```

Then repeated checking becomes unfavorable.

## C7. Non-diffusing belief uncertainty

If:

```text
Q = 0
```

then belief uncertainty does not increase without anchors.

In this case, urgent re-anchoring may be unnecessary.

This is a belief-state condition, not necessarily a claim that the external state is fixed.

## C8. Relative influence does not decrease

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

Relative dilution requires:

```text
A'(R)/A(R) < B'(R)/B(R)
```

when `A(R) > 0` and `B(R) > 0`.

If the uncertainty scale grows as fast as or faster than the reference scale, then relative dilution may fail.

This weakens Proposition 6.

## C9. No upper-bound condition

The upper-bound tightening result requires an additional condition:

```text
K + U + R < T
```

Without such an upper bound, one cannot infer:

```text
U < T - K - R
```

Therefore, upper-bound tightening is not part of the basic timer decomposition.

This limits Proposition 7.

## C10. Stochastic occurrence dilution

UDAM's timer seed model assumes a fixed target condition.

If event occurrence itself is treated as uncertain, then the value of re-anchoring may be diluted by occurrence probability:

```text
V_reanchor ≈ P(event occurs) · V_position_update - C(a)
```

When `P(event occurs)` is low or undefined, the advantage of re-anchoring becomes ambiguous.

This can weaken the model into:

```text
maybe no action is needed because maybe the target never occurs
```

Therefore, stochastic event occurrence is not a counterexample inside the core model. It is an out-of-scope extension that requires a separate event-occurrence layer.

## C11. Safety-critical delay

If measurement delays necessary protective behavior, then action cost may dominate.

Failure pattern:

```text
more measurement -> delayed necessary action
```

UDAM does not justify delaying clearly necessary action for additional measurement.

## C12. Noise-producing activity

Some actions create additional ambiguity rather than resolving it.

Examples:

- vague searching;
- excessive planning;
- symbolic productivity;
- social media refreshing;
- changing tools instead of contacting the state.

These actions may increase subjective activity while failing to reduce `P_t`.

## C13. Wrong anchor

An action may anchor the wrong variable.

Example:

- organizing notes when the true uncertainty is whether one can solve problems;
- tracking mood when the relevant variable is sleep;
- rewriting plans when the project blocker is external approval.

Formal reading:

```text
observation y is informative about S_wrong, not S_relevant
```

This can create false confidence.

## C14. Excessive expansion factor

Adaptive expansion uses:

```text
s_{i+1} = r_i s_i
```

Expansion is favorable only when:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Counterexample condition:

```text
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

Then expansion is unfavorable.

This limits Proposition 13.

## C15. Boundary-risk underestimation

A previous safe scope is evidence, not proof of safety in a larger scope.

Failure pattern:

```text
no boundary crossing at s_i -> assume no boundary crossing at s_{i+1}
```

But:

```text
s_{i+1} = r_i s_i
```

may substantially change:

```text
P_boundary(i)
```

If boundary probability or boundary cost is underestimated, expansion can become unfavorable even after a favorable probe.

## C16. Irreversible action with large expansion

If an action is hard to reverse, correction cost can dominate:

```text
C_correct(r_i) >> 0
```

Failure pattern:

```text
low reversibility + large r_i + weak evidence
```

The model favors smaller probes when correction cost is high.

## C17. Local observation misused as global conclusion

A local observation updates local belief.

It does not automatically justify a global conclusion.

Failure pattern:

```text
one local result -> total self/world/project judgment
```

Examples:

- one failed problem -> I cannot learn this at all;
- one awkward response -> the entire relationship is over;
- one blocked task -> the whole project is impossible.

Correct reading:

```text
local observation updates local posterior; global judgment needs broader evidence
```

## C18. State-belief conflation

UDAM weakens if state dynamics and belief dynamics are conflated.

The model does not claim:

```text
inaction always worsens S_t
```

It claims:

```text
lack of anchors may increase uncertainty about S_t
```

A proper application should distinguish:

```text
state dynamics: S_t changes
belief dynamics: P_t changes
```

## Boundary statement

UDAM favors only actions that satisfy:

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

It does not favor activity, checking, observation, or expansion as such.
