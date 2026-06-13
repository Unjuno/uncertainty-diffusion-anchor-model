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

## C5. Non-diffusing state

If:

```text
Q = 0
```

then uncertainty does not increase without anchors.

In this case, urgent re-anchoring may be unnecessary.

## C6. Safety-critical delay

If measurement delays necessary safety behavior, then action cost may dominate.

Example:

- counting risk while evacuation is possible;
- over-analyzing during immediate danger;
- seeking information when action is already clearly required.

## C7. Noise-producing activity

Some actions create additional ambiguity rather than resolving it.

Examples:

- vague searching;
- excessive planning;
- symbolic productivity;
- social media refreshing;
- changing tools instead of contacting the state.

These actions may increase subjective activity while failing to reduce `P_t`.

## C8. Wrong anchor

An action may anchor the wrong variable.

Example:

- organizing notes when the true uncertainty is whether one can solve problems;
- tracking mood when the relevant variable is sleep;
- rewriting plans when the project blocker is external approval.

## Boundary statement

UDAM favors only actions that satisfy:

```text
I(a) + B(a) > C(a)
```

It does not favor activity as such.
