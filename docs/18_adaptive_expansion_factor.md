# 18 Adaptive Expansion Factor

This document extends adaptive observation cadence into an expansion strategy.

The question is:

```text
After a small valid observation, how much should the agent expand the next action or observation range?
```

This is not a universal constant.

It depends on the object being observed.

## 1. Expansion factor

Let:

```text
s_i = current action or observation scope
r_i = expansion factor
s_{i+1} = r_i s_i
```

Examples:

```text
r = 2 -> doubling
r = 3 -> tripling
r = 4 -> faster geometric expansion
r close to 1 -> cautious expansion
```

Faster expansion can reduce the number of observations, but it can also increase the risk of crossing an important boundary before the next observation.

## 2. Energy efficiency

Large expansion can reduce search energy.

If the useful scale is unknown, geometric expansion can locate a useful scale in relatively few observations.

Practical form:

```text
small probe -> favorable response -> expand scope
```

The energy advantage is:

```text
fewer observations are needed to reach a large scale
```

But this is not automatically optimal.

## 3. Adverse boundary before next observation

Expansion is constrained by the risk that an unfavorable boundary is crossed before the next observation.

Call this:

```text
adverse boundary risk
```

or:

```text
P_boundary(i) = P(boundary is crossed before the next observation | D_i, s_i, r_i)
```

Let:

```text
C_boundary = cost of crossing that boundary
```

Then the expected boundary term is roughly:

```text
P_boundary(i) * C_boundary
```

This term should reduce the expansion factor.

## 4. Timer-seed interpretation

In the timer seed model, the boundary is a fixed upper time bound.

If the next observation is too late, the upper-bound condition may already have been reached before the agent observes again.

This is the abstract structure:

```text
current position uncertain
next observation delayed
a fixed upper-bound event may occur before observation
```

Therefore, the expansion factor cannot be chosen only by energy savings.

It must also account for the probability of boundary crossing before the next observation.

## 5. Expansion tradeoff

Larger expansion:

```text
observation count decreases
energy cost decreases
learning can accelerate
boundary-crossing risk increases
overshoot risk increases
```

Smaller expansion:

```text
observation count increases
energy cost increases
boundary-crossing risk decreases
adjustment is finer
```

So the practical problem is:

```text
How large should the next expansion be, given the risk of crossing a relevant boundary before the next observation?
```

## 6. A rough decision inequality

A larger expansion is favorable when:

```text
expected gain from expansion > observation cost + boundary risk + correction cost
```

Using rough terms:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

where:

- `B_expand(r_i)` is the benefit of larger scope;
- `I_expand(r_i)` is information gained from the larger probe;
- `C_obs(r_i)` is observation or action cost;
- `P_boundary(i) * C_boundary` is expected boundary-crossing cost;
- `C_correct(r_i)` is the cost of correcting after overshooting.

## 7. When to use a larger factor

Use a larger expansion factor when:

```text
observation cost is high
state changes slowly
boundary-crossing risk is low
action is reversible
prior estimate is reliable
small probes keep returning favorable results
```

## 8. When to use a smaller factor

Use a smaller expansion factor when:

```text
boundary-crossing risk is high
state changes quickly
action is hard to reverse
correction cost is high
prior estimate is weak
recent observations are unstable
```

## 9. Relation to hidden upside and hidden downside

If the agent expands too slowly, hidden upside may remain unused.

```text
favorable state -> too little expansion -> upside remains unused
```

If the agent expands too quickly, hidden downside may be crossed before the next observation.

```text
unfavorable boundary -> too much expansion -> late correction
```

So expansion must balance:

```text
use hidden upside
avoid crossing hidden downside
```

## 10. Practical rule

Use this rule:

```text
start small
observe response
expand when response supports expansion
reduce expansion when boundary risk rises
```

The short version:

```text
small probe -> update -> expand only as far as boundary risk allows
```

## 11. Core statement

When exact observation is costly and the useful scale is unknown, geometric expansion can reduce search energy. However, the expansion factor must be constrained by the probability and cost of crossing a relevant boundary before the next observation.
