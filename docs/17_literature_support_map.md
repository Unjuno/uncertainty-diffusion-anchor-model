# 17 Literature Support Map

This document maps UDAM claims to nearby existing research areas.

It does not claim that UDAM is mathematically original in every component.

The safer claim is:

```text
UDAM combines existing decision-theoretic and cognitive ideas into a timer-derived practical model of re-anchoring after anchor loss.
```

## 1. Value of information

UDAM claim:

```text
an observation is useful when it can improve the next decision enough to justify its cost
```

Nearby literature:

- value of information;
- expected value of sample information;
- expected value of perfect information;
- decision analysis.

UDAM expression:

```text
OV = E_y[max_a E[V(a,S) | y]] - max_a E[V(a,S)] - C(obs)
```

Interpretation:

```text
information is valuable because it enables better conditional action
```

## 2. Blackwell informativeness

UDAM claim:

```text
more informative observations are better when they expand feasible conditional action
```

Nearby literature:

- Blackwell's comparison of experiments;
- information structures;
- decision problems under uncertainty.

UDAM expression:

```text
P(y | S) != P(y)
```

and:

```text
a(y) != a_0
```

Interpretation:

```text
useful observation changes either posterior belief or feasible action choice
```

## 3. Bayesian experimental design

UDAM claim:

```text
choose observations by expected usefulness, not by curiosity alone
```

Nearby literature:

- Bayesian experimental design;
- expected information gain;
- experiment utility;
- prior-posterior update.

UDAM expression:

```text
observe y -> update p(S | y) -> choose a(y)
```

## 4. Sequential analysis

UDAM claim:

```text
first observation and later observations are different decisions
```

Nearby literature:

- sequential analysis;
- sequential probability ratio testing;
- stopping rules;
- observation cost.

UDAM expression:

```text
MOV_i > 0
```

Interpretation:

```text
continue observing only while the next observation has positive marginal value
```

## 5. Multi-armed bandits and exploration-exploitation

UDAM claim:

```text
small actions can be useful because they both test and act
```

Nearby literature:

- multi-armed bandit problems;
- exploration-exploitation tradeoff;
- adaptive sampling;
- explore-then-commit strategies.

UDAM interpretation:

```text
observe locally, update belief, then expand or switch action
```

This supports the practical idea:

```text
probe small -> observe response -> expand when favorable
```

## 6. Active inference and epistemic value

UDAM claim:

```text
action can be selected partly to gain information
```

Nearby literature:

- active inference;
- epistemic value;
- expected free energy;
- information-seeking action.

UDAM is narrower than active inference.

It focuses on:

```text
anchor loss -> small state-informative observation -> conditional action
```

## 7. Implementation intentions

UDAM claim:

```text
mapping situations to specific next actions makes the protocol usable
```

Nearby literature:

- implementation intentions;
- if-then planning;
- action planning;
- goal pursuit.

UDAM expression:

```text
if result y occurs -> do action a(y)
```

This supports the playbook structure:

```text
observation result -> mapped next action
```

## 8. Shaping and successive approximations

UDAM claim:

```text
small successful observations can justify gradual expansion
```

Nearby literature:

- shaping;
- successive approximations;
- graded action;
- stepwise skill building.

UDAM expression:

```text
small valid observation -> favorable result -> expand scope
```

## 9. Exponential search and doubling strategies

UDAM claim:

```text
when useful scale is unknown, the agent can expand scope geometrically after successful probes
```

Nearby literature:

- exponential search;
- doubling search;
- geometric search;
- unbounded search over ordered domains.

UDAM expression:

```text
s_{i+1} = r_i s_i
```

Default example:

```text
1 -> 2 -> 4 -> 8
```

Interpretation:

```text
previous scope was safe or useful -> test a larger scope
```

UDAM differs by adding adverse boundary risk:

```text
P_boundary(i) * C_boundary
```

## 10. Online algorithms and robust decision rules

UDAM claim:

```text
when future duration or boundary location is unknown, the agent needs a robust sequential rule rather than a perfect offline optimum
```

Nearby literature:

- online algorithms;
- competitive analysis;
- ski-rental-type tradeoffs;
- robust sequential decision-making.

UDAM interpretation:

```text
choose expansion under uncertainty, knowing that the offline optimum is unavailable
```

The practical question is not always:

```text
what is the perfect expansion factor?
```

but often:

```text
what expansion factor is not too bad under uncertainty?
```

## 11. What the literature supports

The literature supports these parts:

```text
information can have decision value
more informative signals can improve action choice
sampling can be adaptive
sequential observation needs stopping rules
exploration and exploitation must be balanced
actions can be chosen for epistemic value
if-then mappings improve action execution
small steps can support gradual expansion
geometric expansion can reduce search cost when scale is unknown
online rules can be useful when offline optimum is unavailable
```

## 12. What remains UDAM-specific

UDAM-specific synthesis:

```text
timer seed model -> anchor loss -> unknown interval -> valid future anchor -> practical re-anchoring after model collapse
```

The distinctive contribution is not a new theorem replacing decision theory.

The distinctive contribution is the practical unification:

```text
when you feel unable to conclude because the anchor is lost, do not globally invalidate the future; take one valid local observation, map the result, and expand only when the response supports expansion and boundary risk allows it
```

## 13. Current research task

For a future paper, the next step is to turn this map into a formal related-work section with verified citations.

Priority sources:

```text
value of information
Blackwell informativeness
Bayesian experimental design
sequential analysis
multi-armed bandits
active inference
implementation intentions
successive approximations
exponential search
online algorithms
ski-rental-type tradeoffs
```
