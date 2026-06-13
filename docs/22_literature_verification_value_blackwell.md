# 22 Literature Verification: Value of Information and Blackwell Informativeness

This document starts Stage 2 of the five-stage refinement roadmap.

It verifies two nearby literature areas against UDAM claims:

```text
1. value of information
2. Blackwell informativeness
```

The goal is not to collect many references.

The goal is to determine which UDAM claims are directly supported, partially supported, analogy-only, or in need of wording correction.

## Sources checked

### Value of information

Reference candidates:

- Ronald A. Howard, "Information Value Theory," IEEE Transactions on Systems Science and Cybernetics, 1966.
- Expected value of sample information / expected value of perfect information literature.
- Decision analysis literature derived from Howard/Raiffa/Schlaifer traditions.

Core literature idea:

```text
information has value when receiving it before action can improve expected decision value
```

A common formulation is:

```text
value with information - value without information - cost of information
```

### Blackwell informativeness

Reference candidates:

- David Blackwell, "Comparison of Experiments," 1951.
- David Blackwell, "Equivalent Comparisons of Experiments," Annals of Mathematical Statistics, 1953.
- Later Blackwell-order literature.

Core literature idea:

```text
one information structure is more informative than another if every expected-utility-maximizing decision maker can do at least as well with it
```

Another equivalent statement is that the less informative experiment can be obtained by garbling the more informative one.

## UDAM claim 1: Observation can have positive decision value

UDAM statement:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Observation is favorable when:

```text
OV > 0
```

Literature fit:

```text
direct support
```

Reason:

This is essentially a value-of-information structure: observe before acting, update belief, choose the best action conditional on the observation, and subtract observation cost.

The wording should emphasize:

```text
observation is not valuable merely because it reduces uncertainty
observation is valuable when it improves expected decision value enough to exceed cost
```

Recommended status:

```text
strongly supported by value-of-information decision analysis
```

## UDAM claim 2: Observation can be non-negative under ideal no-cost conditions

UDAM statement:

```text
E_y[max_a E[V(a,S) | y]] >= max_a E[V(a,S)]
```

under ideal conditions and no observation cost.

Literature fit:

```text
direct support
```

Reason:

The decision maker can ignore unhelpful information and choose the same action as before. Therefore, information cannot reduce the optimal expected value under ideal assumptions.

Required caveat:

This relies on idealized decision conditions:

```text
correct updating
ability to ignore information
no processing error
no harmful delay
no observation cost
```

If these fail, the practical value of information can be negative.

Recommended wording:

```text
Under ideal no-cost decision-theoretic conditions, observation has non-negative option value.
```

Avoid:

```text
observation is always good
```

## UDAM claim 3: A valid re-anchor must be state-informative

UDAM statement:

```text
P(y | S) != P(y)
```

or equivalently:

```text
P(S | y) != P(S)
```

Literature fit:

```text
partial support
```

Reason:

Blackwell informativeness concerns comparative ranking of entire information structures by expected utility across decision problems. UDAM's condition is weaker and local: it asks whether one observation result can update belief about the relevant state.

The UDAM condition is necessary for a local observation to be belief-relevant, but it is not the full Blackwell ordering.

Recommended status:

```text
consistent with Blackwell-style informativeness, but not identical to Blackwell informativeness
```

Recommended wording:

```text
UDAM's state-informative condition is a local belief-update condition. It is compatible with Blackwell informativeness but should not be presented as the Blackwell theorem itself.
```

Avoid:

```text
P(y | S) != P(y) is Blackwell informativeness
```

## UDAM claim 4: Better information enables a larger feasible set of conditional actions

UDAM statement:

```text
a(y) != a_0
```

and:

```text
observation -> posterior update -> conditional action
```

Literature fit:

```text
partial to direct support
```

Reason:

Blackwell's theorem links more informative experiments to decision makers being able to achieve at least as high expected utility across decision problems. This matches UDAM's idea that useful observation supports conditional action.

However, UDAM usually discusses one local action-switch situation, not a full comparison of experiments across all decision problems.

Recommended wording:

```text
The conditional-action layer is decision-theoretically aligned with Blackwell-style information structures, but UDAM uses a local and practical version rather than the full comparative theorem.
```

## UDAM claim 5: Repeated checking can lose value

UDAM statement:

```text
MOV_i <= 0
```

means repeated observation is no longer favorable.

Literature fit:

```text
partial support
```

Reason:

Value-of-information analysis supports the idea that information-gathering should be compared against cost. It also supports non-additivity and diminishing usefulness in many practical contexts.

But the exact UDAM expression `MOV_i` is an internal model construct, not directly taken from a single cited source.

Recommended status:

```text
internally coherent and broadly consistent with value-of-information reasoning
```

Avoid:

```text
MOV_i is a standard VOI formula
```

## UDAM claim 6: Literature proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

The literature supports components of the framework, not the whole timer-derived synthesis.

Correct positioning:

```text
UDAM combines timer-derived anchor loss, belief uncertainty, observability value, conditional action, and boundary-risk-constrained expansion into a practical synthesis.
```

Avoid:

```text
UDAM is proven by value-of-information theory or Blackwell informativeness
```

## Verification table

| UDAM claim | Literature area | Support level | Correction |
|---|---|---:|---|
| `OV > 0` justifies observation | value of information | direct | keep; emphasize expected decision value minus cost |
| ideal no-cost information has non-negative option value | value of information | direct | keep with ideal-condition caveat |
| `P(y | S) != P(y)` defines valid local re-anchor | Blackwell informativeness | partial | do not call it Blackwell theorem |
| observation can enable conditional action | Blackwell / decision theory | partial to direct | say aligned, not identical |
| repeated observation needs marginal value `MOV_i > 0` | value of information | partial | present as UDAM-specific marginal form |
| literature proves UDAM as a whole | none | not supported | reject |

## Recommended repository wording

Use:

```text
UDAM's observability-value layer is directly aligned with value-of-information reasoning: information is useful when it improves expected decision value enough to exceed its cost.
```

Use:

```text
UDAM's state-informative condition is compatible with Blackwell-style informativeness but is a local belief-update condition, not the full Blackwell ordering.
```

Use:

```text
Existing literature supports components of UDAM, while the timer-derived synthesis and practical framing remain UDAM-specific.
```

Avoid:

```text
UDAM is proven by Blackwell's theorem.
```

Avoid:

```text
Any state-informative observation is worth making.
```

Avoid:

```text
P(y | S) != P(y) is the same as Blackwell informativeness.
```

## Impact on current theory

No major correction is required.

However, current wording should remain careful on three points:

```text
state-informative != favorable
local belief-update condition != Blackwell order
component support != proof of full synthesis
```

## Next literature topics

Recommended next checks:

```text
Bayesian experimental design
sequential analysis / stopping rules
exponential search / online algorithms
implementation intentions
behavioral activation
```
