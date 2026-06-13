# 23 Literature Verification: Bayesian Experimental Design

This document continues Stage 2 of the five-stage refinement roadmap.

It checks Bayesian experimental design against UDAM claims about observation choice, posterior update, and conditional action after anchor loss.

The goal is not to prove UDAM from Bayesian experimental design.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- D. V. Lindley, "On a Measure of the Information Provided by an Experiment," Annals of Mathematical Statistics, 1956.
- Kathryn Chaloner and Isabella Verdinelli, "Bayesian Experimental Design: A Review," Statistical Science, 1995.
- David C. Woods, Antony M. Overstall, Maria Adamou, and Timothy W. Waite, "Bayesian Design of Experiments for Generalised Linear Models and Dimensional Analysis with Industrial and Scientific Application," Quality Engineering, 2017; arXiv:1606.05892.
- Tom Rainforth, Adam Foster, Desi R. Ivanova, and Freddie Bickford Smith, "Modern Bayesian Experimental Design," arXiv:2302.14545.
- Antony M. Overstall and James M. McGree, "Bayesian Design of Experiments for Intractable Likelihood Models Using Coupled Auxiliary Models and Multivariate Emulation," arXiv:1803.07018.

Core literature idea:

```text
choose an experiment or design by maximizing expected utility or expected information gain under prior uncertainty
```

Typical structure:

```text
prior belief -> proposed design -> possible outcome -> posterior belief -> utility evaluation
```

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `S` | UDAM-relevant state | dimensionless | state variable after anchor loss | discrete or continuous state space | random variable |
| `y` | observation result | dimensionless | observed outcome of a probe or experiment | generated under an observation model | random variable |
| `xi` | experimental design / observation choice | dimensionless | controllable design or probe selection | chosen before observing `y` | decision variable |
| `a` | action | dimensionless | action selected before or after observation | belongs to feasible action set | decision variable |
| `p(S)` | prior belief over `S` | probability | belief before observing `y` | sums or integrates to 1 | distribution |
| `p(S | y)` | posterior belief over `S` | probability | belief after observing `y` | defined when `p(y) > 0` | distribution |
| `U(xi, y)` | experiment utility | utility unit | value of outcome `y` under design `xi` | criterion-dependent | scalar |
| `C(obs)` | observation cost | utility unit | cost of acquiring or processing observation | non-negative in ordinary use | scalar |
| `OV` | UDAM observability value | utility unit | expected conditional-action value minus baseline and cost | positive means favorable | scalar |

Dimension check:

```text
expected utility - expected utility - cost = utility unit
```

Therefore UDAM's `OV` is dimensionally valid if `C(obs)` is expressed in the same utility unit as the decision value terms.

## Literature pattern

Bayesian experimental design usually chooses a design `xi` by optimizing an expected utility over unknown outcomes:

```text
EU(xi) = E_y[U(xi, y)]
```

A common information-theoretic utility is expected information gain:

```text
EIG(xi) = E[log p(S | y, xi) - log p(S)]
```

This matches the broad UDAM pattern:

```text
choose observation -> observe y -> update belief -> choose or revise action
```

But the match is not exact.

Bayesian experimental design is a general framework for experiment selection. UDAM is a narrower timer-derived practical synthesis for acting after anchor loss.

## UDAM claim 1: Observation should be chosen by expected usefulness

UDAM statement:

```text
choose observations by expected usefulness, not by curiosity alone
```

Related UDAM expression:

```text
OV = E_y[max_a E[V(a, S) | y]] - max_a E[V(a, S)] - C(obs)
```

Literature fit:

```text
direct support
```

Reason:

Bayesian experimental design explicitly treats experiment or observation choice as an optimization problem under uncertainty. The design is chosen before the result is known, and its value is evaluated by expected utility or expected information gain.

This supports UDAM's rule that an observation is not justified merely because it is possible or interesting. It must be useful under the chosen decision criterion.

Recommended wording:

```text
UDAM's observation-selection layer is directly aligned with Bayesian experimental design: observations should be selected by expected usefulness under uncertainty, not by curiosity alone.
```

Avoid:

```text
Any observation that gives information is worth making.
```

## UDAM claim 2: Observation updates belief before action

UDAM statement:

```text
observe y -> update p(S | y) -> choose a(y)
```

Literature fit:

```text
partial to direct support
```

Reason:

Bayesian experimental design directly supports the prior-to-posterior part:

```text
p(S) -> p(S | y)
```

It also supports choosing designs by downstream utility. However, BED is often written around experiment design, parameter learning, prediction, or model discrimination rather than an explicit UDAM-style post-collapse action map.

The action-selection layer is therefore aligned with decision-theoretic BED, but UDAM's concrete `a(y)` protocol remains UDAM-specific.

Recommended wording:

```text
Bayesian experimental design supports UDAM's prior-observation-posterior structure and partly supports its conditional-action layer when the experiment utility is decision-relevant.
```

Avoid:

```text
Bayesian experimental design is the same as UDAM.
```

## UDAM claim 3: State-informative is not the same as favorable

UDAM distinction:

```text
state-informative != favorable
```

Literature fit:

```text
direct support for the distinction
```

Reason:

Bayesian experimental design distinguishes the existence of information from the criterion used to choose an experiment. A design can be informative about a state or parameter but still be a poor choice if the expected utility is too low, the cost is too high, or the information is irrelevant to the decision objective.

This supports the UDAM correction:

```text
P(y | S) != P(y)
```

is not enough for favorable observation. The observation must also pass a value condition such as:

```text
OV > 0
```

Recommended wording:

```text
State-informativeness is a belief-update condition. Favorability is a value condition. Bayesian experimental design supports keeping these separate.
```

Avoid:

```text
If an observation changes belief, it should be taken.
```

## UDAM claim 4: Valid re-anchor condition

UDAM statement:

```text
P(y | S) != P(y)
```

or:

```text
P(S | y) != P(S)
```

Literature fit:

```text
partial support
```

Reason:

Bayesian experimental design assumes an observation model and uses possible observations to update beliefs. That is compatible with UDAM's local belief-update condition.

However, BED does not define `valid re-anchor` as a timer-derived condition after anchor loss. UDAM's re-anchor language is practical and model-specific.

Recommended wording:

```text
UDAM's valid re-anchor condition is Bayesian-compatible because it requires the observation to update belief about the relevant state. The re-anchor framing itself is UDAM-specific.
```

Avoid:

```text
Bayesian experimental design proves the valid re-anchor condition.
```

## UDAM claim 5: Repeated observation can be adaptive

UDAM statement:

```text
MOV_i > 0
```

means the next repeated observation remains favorable.

Literature fit:

```text
partial support
```

Reason:

Adaptive Bayesian experimental design supports sequentially choosing later observations using information gained from earlier observations. This aligns with UDAM's idea that the first observation and later observations are different decisions.

But UDAM's `MOV_i` notation is not a standard BED formula. It is a practical marginal-value rule inside UDAM.

Sequential analysis and stopping-rule literature should be checked separately because it is closer to the question:

```text
continue observing or stop?
```

Recommended wording:

```text
Adaptive Bayesian experimental design supports updating observation choices after each result. UDAM's MOV_i rule remains an internal marginal-value criterion and should be verified further against sequential analysis.
```

Avoid:

```text
MOV_i is a standard Bayesian experimental design equation.
```

## UDAM claim 6: Timer-derived anchor loss

UDAM statement:

```text
anchor loss does not imply future anchor invalidation
```

Literature fit:

```text
analogy only
```

Reason:

Bayesian experimental design supports rational observation choice under uncertainty. It does not provide the timer seed model:

```text
tau = K + U + R
```

It also does not directly state UDAM's central practical correction:

```text
partial uncertainty does not imply total invalidation
```

The connection is only analogical:

```text
uncertainty remains local if future observations can still update belief and guide action
```

Recommended wording:

```text
Bayesian experimental design supports the observation-selection component of UDAM, not the timer-derived anchor-loss argument itself.
```

Avoid:

```text
Bayesian experimental design proves the timer model.
```

## Verification table

| UDAM claim | BED support level | Reason | Correction |
|---|---:|---|---|
| choose observations by expected usefulness | direct support | BED optimizes designs by expected utility or expected information gain | keep |
| observe `y` then update `p(S | y)` | direct support | prior-posterior updating is central | keep |
| choose `a(y)` after observation | partial to direct support | supported when utility is action-relevant; not always explicit in BED | say aligned, not identical |
| `state-informative != favorable` | direct support | information and utility criteria are distinct | keep strongly |
| `P(y | S) != P(y)` as valid re-anchor | partial support | compatible with belief update, but re-anchor framing is UDAM-specific | do not call it a BED theorem |
| `MOV_i > 0` for repeated observation | partial support | adaptive BED supports sequential design choice, but not this notation | verify later with stopping rules |
| timer-derived anchor-loss structure | analogy only | BED does not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only components are supported | reject |

## Recommended repository wording

Use:

```text
Bayesian experimental design directly supports UDAM's utility-guided observation-selection layer: observations should be chosen by expected usefulness under uncertainty.
```

Use:

```text
Bayesian experimental design supports the prior-observation-posterior structure that UDAM uses for re-anchoring, while UDAM's timer-derived anchor-loss framing remains specific to UDAM.
```

Use:

```text
State-informativeness is not enough. A favorable observation must also satisfy a value condition such as OV > 0.
```

Avoid:

```text
UDAM is Bayesian experimental design.
```

Avoid:

```text
Bayesian experimental design proves the whole UDAM synthesis.
```

Avoid:

```text
Any information-gaining action is worth taking.
```

## Impact on current theory

No major correction is required.

Bayesian experimental design strengthens the existing UDAM wording around:

```text
expected usefulness
prior -> observation -> posterior
observation cost and utility criterion
adaptive observation choice
```

The main caution remains:

```text
component support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
sequential analysis / stopping rules
```

Reason:

Bayesian experimental design supports choosing and adapting observations. Sequential analysis is closer to the specific UDAM question:

```text
when should repeated checking stop?
```

This should be used to verify the status of:

```text
MOV_i > 0
MOV_i <= 0
first observation versus repeated observation
```
