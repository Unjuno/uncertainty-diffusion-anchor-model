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
health or crisis-like contexts -> external support and safety judgment may dominate
```

Therefore, UDAM gives a structure, not a universal schedule.

## 3. Observation can become empty checking

Repeated observation is useful only while:

```text
MOV_i > 0
```

In plain language:

```text
another check is useful only if it can change the next action
```

If the next action is already clear, further checking may be wasteful.

## 4. Some domains need external standards

Some domains cannot be handled by self-observation alone.

Examples:

- serious health uncertainty;
- legal uncertainty;
- financial risk beyond simple planning;
- safety-critical situations;
- complex technical systems.

In these cases, the re-anchor may be:

```text
ask a qualified person
check an authoritative source
use a validated measurement
follow an established procedure
```

UDAM does not replace domain expertise.

## 5. Action value still matters

Even a state-informative observation may not be worth doing if cost is too high.

Use:

```text
V(a) = I(a) + B(a) - C(a)
```

and, for observation-specific actions:

```text
OV > 0
```

## 6. Do not confuse local state with global conclusion

A failed local observation does not prove global failure.

A successful local observation does not prove global success.

UDAM supports local re-anchoring.

```text
one local observation -> one mapped next action
```

It does not justify total conclusions from a single signal.

## 7. Practical caution statement

The safe practical version is:

> Use small observations when they are connected to the relevant state and can change the next action. Do not keep observing when the next action is already clear. Do not use UDAM as a substitute for domain expertise or urgent support.
