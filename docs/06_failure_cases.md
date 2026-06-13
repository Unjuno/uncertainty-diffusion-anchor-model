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

## 2. High cost

An informative action can still be bad if its cost is too high.

```text
C(a) > I(a) + B(a)
```

## 3. Misleading feedback

A measurement can reduce apparent uncertainty while increasing actual error if the feedback is biased or false.

## 4. Compulsive checking

Repeated checking may have diminishing informational value.

If the marginal information value approaches zero while cost remains positive, the behavior becomes unfavorable.

## 5. Wrong anchor

An action may anchor the wrong state variable.

Example: organizing notes when the actual uncertainty is whether one can solve problems.

## 6. Non-diffusing state

If uncertainty does not grow without action, then urgent re-anchoring may not be necessary.

```text
Q = 0
```

## 7. Safety-critical delay

In emergencies, measurement can be inferior to immediate action.

UDAM does not justify delaying safety behavior for more information.

## Boundary rule

The model supports only actions satisfying:

```text
I(a) + B(a) > C(a)
```

It does not support activity as such.
