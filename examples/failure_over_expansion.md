# Failure Example: Over-Expansion

## Pattern

A small probe succeeds, but the agent expands too far without accounting for observation cost, correction cost, or boundary risk.

Scope update:

```text
s_{i+1} = r_i s_i
```

Expansion failure condition:

```text
B_expand(r_i) + I_expand(r_i) <= C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

## Situation

The agent is rebuilding a work routine.

A small probe works:

```text
work for 10 minutes -> task state becomes clearer
```

The agent interprets this as evidence that a much larger scope is safe:

```text
10 minutes -> 4 hours
```

## Why this fails

The small probe was valid.

But the expansion factor was too large.

The larger scope changes several terms:

```text
C_obs(r_i)
C_correct(r_i)
P_boundary(i)
```

The agent treats the previous safe scope as proof that the next scope is safe.

That is too strong.

Correct interpretation:

```text
previous safe scope is evidence, not proof of safety in a larger scope
```

## UDAM correction

Use a smaller expansion factor.

Example:

```text
10 minutes -> 20 minutes -> 40 minutes
```

or use an earlier observation point:

```text
10 minutes -> 30 minutes -> check task state
```

## Practical rule

```text
Expand when evidence supports expansion.
Do not confuse successful small scope with unlimited scope.
```
