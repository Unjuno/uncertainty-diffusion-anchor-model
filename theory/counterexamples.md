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

## C2. High cost

If:

```text
C(a) > I(a) + B(a)
```

then:

```text
V(a) < 0
```

The action is unfavorable even if it returns some information.

## C3. Misleading feedback

If an action returns systematically false information, it can reduce apparent uncertainty while increasing actual error.

Example:

- unreliable measurement;
- biased feedback;
- deceptive social signal;
- self-serving interpretation.

## C4. Compulsive checking

Repeated checking may have rapidly diminishing informational value.

If:

```text
I(a_n) → 0
```

while:

```text
C(a_n) > 0
```

then repeated checking becomes unfavorable.

## C5. Non-diffusing belief uncertainty

If:

```text
Q = 0
```

then belief uncertainty does not increase without anchors.

In this case, urgent re-anchoring may be unnecessary.

This is a belief-state condition, not necessarily a claim that the external state is fixed.

## C6. Relative influence does not decrease

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

## C7. No upper-bound condition

The upper-bound tightening result requires an additional condition:

```text
K + U + R < T
```

Without such an upper bound, one cannot infer:

```text
U < T - K - R
```

Therefore, upper-bound tightening is not part of the basic timer decomposition.

## C8. Stochastic occurrence dilution

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

## C9. Safety-critical delay

If measurement delays necessary safety behavior, then action cost may dominate.

Example:

- over-analyzing during immediate danger;
- seeking information when action is already clearly required.

## C10. Noise-producing activity

Some actions create additional ambiguity rather than resolving it.

Examples:

- vague searching;
- excessive planning;
- symbolic productivity;
- social media refreshing;
- changing tools instead of contacting the state.

These actions may increase subjective activity while failing to reduce `P_t`.

## C11. Wrong anchor

An action may anchor the wrong variable.

Example:

- organizing notes when the true uncertainty is whether one can solve problems;
- tracking mood when the relevant variable is sleep;
- rewriting plans when the project blocker is external approval.

## C12. State-belief conflation

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

It does not favor activity as such.
