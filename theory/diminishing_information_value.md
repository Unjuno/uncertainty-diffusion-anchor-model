# Diminishing Information Value

UDAM supports informative action, but it does not support unlimited checking.

This file formalizes when repeated observation stops being useful.

## Core idea

The first observation after anchor loss can have high value because it restores contact with the state.

Repeated observations often have lower marginal value.

Let repeated observation actions be:

```text
a_1, a_2, ..., a_n
```

Let their marginal informational values be:

```text
I_1, I_2, ..., I_n
```

A simple diminishing-value assumption is:

```text
I_1 >= I_2 >= ... >= I_n >= 0
```

## Action-value condition

Each repeated action is favorable only if:

```text
V(a_i) = I_i + B_i - C_i > 0
```

where:

- `I_i` is marginal informational value;
- `B_i` is marginal intervention value;
- `C_i` is marginal cost.

The stopping condition is:

```text
I_i + B_i <= C_i
```

When this holds, the next check is not favored.

## Observation-specific form

For observation actions, define marginal observability value:

```text
MOV_i = OV_i - OV_{i-1}
```

or more directly:

```text
MOV_i = E_y[max_a E[V(a,S) | y, D_i]] - max_a E[V(a,S) | D_i] - C(obs_i)
```

where `D_i` is the information state before observation `i`.

Observation `i` is favorable only when:

```text
MOV_i > 0
```

## Repeated checking boundary

Repeated checking becomes unfavorable when:

```text
MOV_i <= 0
```

or in the simpler action-value form:

```text
I_i + B_i <= C_i
```

This boundary prevents UDAM from becoming a justification for compulsive checking.

## Difference between re-anchoring and checking loops

A re-anchor creates a useful reference point.

A checking loop repeats observation without improving action selection.

Re-anchor:

```text
observation changes belief or next action
```

Checking loop:

```text
observation does not change belief or next action enough to exceed cost
```

## Practical interpretation

Ask:

```text
Will this next observation change what I do?
```

If yes, observation may have positive value.

If no, observation may be empty activity.

## Relation to observability value

The observability layer says:

```text
OV > 0
```

for a useful observation.

The diminishing information layer says:

```text
MOV_i > 0
```

for each additional observation.

Thus, UDAM favors repeated observation only while each additional observation has positive marginal value.

## Correct statement

The precise claim is:

> Low-cost informative actions are useful while their marginal information or observability value exceeds their cost.

Not:

> More checking is always better.
