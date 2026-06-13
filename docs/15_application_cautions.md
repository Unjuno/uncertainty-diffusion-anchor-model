# 15 Application Cautions

This document records practical cautions for applying UDAM.

The goal is to prevent overgeneralization.

UDAM says:

```text
unclear state -> state-informative observation -> conditional next action
```

It does not say:

```text
observe everything all the time
```

## 1. State-informative observation is required

A useful re-anchor must be connected to the state.

Formal condition:

```text
P(y | S) != P(y)
```

Practical test:

```text
What result would change the next action?
```

If no possible result changes belief or action, the observation is weak.

## 2. Optimal timing is domain-specific

UDAM does not provide a universal timing rule.

The best timing for re-anchoring depends on the domain.

Examples:

```text
learning -> frequent short tests may be useful
work -> checks should match project rhythm
relationships -> repeated checking can become counterproductive
budget -> checking is useful when it changes a plan
high-impact contexts -> external standards may dominate
```

Therefore, UDAM gives a structure, not a universal schedule.

For a detailed cadence rule, see:

- `docs/16_adaptive_observation_cadence.md`

## 3. First observation and later observations are different

If observation has been zero for a while, the first valid observation often has high value.

```text
observation rate = 0 -> stale belief state
```

After the first observation, the question changes:

```text
Would another observation change the next action?
```

So the first observation may be strongly justified, while later observations require a marginal-value test.

## 4. Observation can become empty checking

Repeated observation is useful only while:

```text
MOV_i > 0
```

In plain language:

```text
another check is useful only if it can change the next action
```

If the next action is already clear, further checking may be wasteful.

## 5. Some domains need external standards

Some domains cannot be handled by self-observation alone.

In these cases, the re-anchor may be:

```text
ask a qualified person
check an authoritative source
use a validated measurement
follow an established procedure
```

UDAM does not replace domain expertise.

## 6. Action value still matters

Even a state-informative observation may not be worth doing if cost is too high.

Use:

```text
V(a) = I(a) + B(a) - C(a)
```

and, for observation-specific actions:

```text
OV > 0
```

## 7. Do not confuse local state with global conclusion

A failed local observation does not prove global failure.

A successful local observation does not prove global success.

UDAM supports local re-anchoring.

```text
one local observation -> one mapped next action
```

It does not justify total conclusions from a single signal.

## 8. Practical caution statement

The safe practical version is:

> Use small observations when they are connected to the relevant state and can change the next action. If observation has been zero, the first valid observation often has high value. After that, observe again only when the next observation can change belief or action enough to justify its cost. UDAM gives a decision structure, not a universal schedule.
