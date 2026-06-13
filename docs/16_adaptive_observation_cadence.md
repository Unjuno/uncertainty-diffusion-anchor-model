# 16 Adaptive Observation Cadence

This document explains how often to observe after the first re-anchor.

The core problem is:

```text
observation rate = 0 -> uncertainty can grow unchecked
```

But the solution is not:

```text
observe everything constantly
```

The better rule is:

```text
observe when the next observation can change belief or action
```

## 1. First observation has special value

When observation has been zero for a while, the first valid observation often has high value.

Reason:

```text
D_t has not been updated
```

so the agent may be acting from an old or collapsed belief state.

If uncertainty diffuses:

```text
P_t+dt = P_t + Q dt
```

then the first state-informative observation can be valuable because it reconnects belief with the current state.

Practical version:

```text
if you have not looked at the state at all, take one small valid observation
```

## 2. Later observations need a marginal test

After the first observation, the question changes.

The question is no longer:

```text
Should I observe at least once?
```

It becomes:

```text
Would another observation change the next action?
```

Use:

```text
MOV_i > 0
```

In plain language:

```text
the next observation is useful only if it can change belief or action enough to justify its cost
```

## 3. Observation cadence is adaptive, not fixed

UDAM does not give one universal observation interval.

The cadence depends on the object being observed.

A useful observation schedule depends on:

```text
state volatility
cost of observation
cost of being wrong
action reversibility
information decay
whether the next action can change
```

Therefore:

```text
same interval for every domain is wrong
```

## 4. Possible cadence patterns

Different domains may use different patterns.

### One-shot observation

Use when one observation is enough to choose the next action.

```text
observe once -> act
```

### Periodic observation

Use when the state changes at a roughly predictable rhythm.

```text
observe every fixed interval -> update plan
```

### Event-triggered observation

Use when a new signal or threshold appears.

```text
if relevant change occurs -> observe again
```

### Shrinking observation interval

Use when the target approaches, uncertainty is increasing, or cost of error rises.

```text
far from decision -> observe sparsely
near decision -> observe more often
```

### Expanding observation interval

Use when the state stabilizes and repeated checks stop changing action.

```text
if repeated observations do not change action -> observe less often
```

## 5. Why this prevents miscalculation

Two errors occur when observation cadence is wrong.

### Hidden downside error

The agent feels safe, does not observe, and misses a worsening state.

```text
false comfort -> no observation -> hidden downside appears later
```

### Hidden upside error

The agent feels defeated, does not observe, and misses a better-than-expected state.

```text
pessimistic belief -> no observation -> hidden upside remains unused
```

Both errors come from treating a stale belief as if it were a current observation.

## 6. Practical rule

Use this rule:

```text
observe sooner when the state can change fast, the cost of being wrong is high, or the next action may change
```

Observe later when:

```text
the state is stable, observation is costly, or the next action would not change
```

Stop observing when:

```text
MOV_i <= 0
```

## 7. Minimal decision card

```text
1. Has this state been observed recently?
2. Can the state change before the next action?
3. Would a new observation change what I do?
4. Is the cost of observing lower than the cost of being wrong?
5. If yes, observe. If no, act or wait.
```

## 8. Core statement

The safe practical statement is:

> If observation has been zero, the first valid observation often has high value. After that, observation cadence must be adaptive: observe again only when the expected marginal information can change the next action enough to justify the cost.
