# 29 Literature Verification: Active Inference and Epistemic Value

This document continues Stage 2 of the five-stage refinement roadmap.

It checks active inference, expected free energy, epistemic value, and information-seeking action against UDAM claims about actions that are chosen partly to gain information after anchor loss.

The goal is not to prove UDAM from active inference.

The goal is to classify which UDAM components are directly supported, partially supported, analogy-only, unsupported, or in need of wording correction.

## Sources checked

Reference candidates:

- Karl Friston, Thomas FitzGerald, Francesco Rigoli, Philipp Schwartenbeck, and Giovanni Pezzulo, "Active Inference and Learning," Neuroscience & Biobehavioral Reviews, 2016.
- Karl Friston, Thomas FitzGerald, Francesco Rigoli, Philipp Schwartenbeck, John O'Doherty, and Giovanni Pezzulo, "Active Inference and Learning," Neuroscience & Biobehavioral Reviews, 2016.
- Thomas Parr, Giovanni Pezzulo, and Karl J. Friston, *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*, MIT Press, 2022.
- Noor Sajid, Lancelot Da Costa, Thomas Parr, and Karl Friston, "Active Inference, Bayesian Optimal Design, and Expected Utility," arXiv:2110.04074, 2021.
- Beren Millidge, Alexander Tschantz, and Christopher L. Buckley, "Whence the Expected Free Energy?" arXiv:2004.08128, 2020.
- Thijs van de Laar, Magnus Koudahl, Bart van Erp, and Bert de Vries, "Active Inference and Epistemic Value in Graphical Models," arXiv:2109.00541, 2021.
- Ran Wei, "Value of Information and Reward Specification in Active Inference and POMDPs," arXiv:2408.06542, 2024.

Core literature idea:

```text
policies or actions can be selected not only for pragmatic reward but also for epistemic value, information gain, uncertainty reduction, or model disambiguation
```

This is close to the UDAM action-value layer:

```text
V(a) = I(a) + B(a) - C(a)
```

and to the probe pattern:

```text
small action -> informative feedback -> belief update -> conditional next action
```

But the match is limited.

Active inference is a broad theoretical and computational framework based on generative models and expected free energy. UDAM is a timer-derived practical synthesis after anchor loss.

## Minimal notation

| Symbol | Meaning in this note | Unit | Definition | Domain / assumption | Type |
|---|---|---:|---|---|---|
| `pi` | policy | dimensionless | sequence or plan of actions considered by an active-inference agent | policy set | decision variable |
| `a` | UDAM action or probe | dimensionless | concrete action chosen after anchor loss | feasible action set | decision variable |
| `I(a)` | UDAM informational value | utility unit | expected informational contribution of action `a` | must affect future belief or action | scalar |
| `B(a)` | UDAM practical benefit | utility unit | expected non-informational benefit of action `a` | domain-specific | scalar |
| `C(a)` | UDAM action cost | utility unit | cost or risk of action `a` | non-negative | scalar |
| `G(pi)` | expected free energy | free-energy or objective unit | active-inference objective for policy evaluation | model-specific | scalar |
| `IG(pi)` | expected information gain | information unit or objective unit | expected reduction in uncertainty under policy `pi` | model-specific | scalar |
| `S` | UDAM-relevant state | dimensionless | state being inferred after anchor loss | domain-specific | random variable |
| `y` | observation or outcome | dimensionless | feedback produced by observation or action | must be observable | random variable |
| `p(S | y)` | posterior belief | probability | belief after observing `y` | sums or integrates to 1 | distribution |

Dimension check:

```text
V(a) = I(a) + B(a) - C(a)
```

is valid only if `I(a)`, `B(a)`, and `C(a)` are placed on a common utility scale.

Expected free energy terms are not automatically on this same scale. A mapping from active-inference objective units to UDAM utility units must be defined before the equations can be treated as formally identical.

## Literature pattern

A simplified active-inference pattern is:

```text
consider policy pi -> predict outcomes -> evaluate pragmatic and epistemic consequences -> select policy
```

The epistemic part favors actions or policies that reduce uncertainty or reveal hidden states, parameters, or models.

This supports a limited version of UDAM's claim:

```text
action can be selected partly because it produces information
```

But it does not support the stronger claim:

```text
any information-seeking action is useful
```

UDAM still requires:

```text
state-informativeness
action relevance
cost and boundary-risk checks
conditional action change
```

## UDAM claim 1: Action can be chosen partly to gain information

UDAM statement:

```text
V(a) = I(a) + B(a) - C(a)
```

Literature fit:

```text
direct support for the general action-as-information idea
partial support for the specific UDAM value decomposition
```

Reason:

Active inference explicitly includes epistemic or information-seeking components in policy selection. This directly supports the idea that action can be chosen partly because it is expected to reveal useful information.

However, UDAM's `I(a)` is a practical utility-valued information term. It should not be presented as identical to expected free energy, epistemic value, or information gain without a formal mapping.

Recommended wording:

```text
Active inference directly supports the general idea that actions or policies can have epistemic value. UDAM expresses this more narrowly as an informational contribution I(a) inside a practical action-value calculation.
```

Avoid:

```text
I(a) is expected free energy.
```

## UDAM claim 2: Probe actions can reduce uncertainty after anchor loss

UDAM statement:

```text
small action -> informative feedback -> belief update
```

Literature fit:

```text
partial support
```

Reason:

Active inference supports the selection of actions that sample outcomes expected to reduce uncertainty. This is aligned with UDAM's small-probe logic.

The support is partial because UDAM's anchor-loss setting is narrower and more practical. Active inference does not provide UDAM's timer seed model or its fixed distinction between known interval, unknown interval, and re-anchored interval.

Recommended wording:

```text
Active inference supports the idea that an agent may act in order to sample informative outcomes. UDAM applies this idea to small, bounded probes after anchor loss.
```

Avoid:

```text
Active inference proves the timer-derived re-anchor model.
```

## UDAM claim 3: Information-seeking must be action-relevant

UDAM statement:

```text
state-informative != favorable
```

and:

```text
OV > 0
```

Literature fit:

```text
direct support for balancing epistemic and pragmatic value
partial support for UDAM's exact favorability rule
```

Reason:

Active inference distinguishes epistemic and pragmatic components of action selection. This supports UDAM's distinction between information gain and practical value.

However, active inference can value epistemic action in ways that are not identical to UDAM's expected-decision-value condition. Therefore UDAM should not say that any uncertainty-reducing action is automatically favorable.

Recommended wording:

```text
Active inference supports including epistemic value in action selection, but UDAM still requires the resulting information to be decision-relevant and cost-justified.
```

Avoid:

```text
Any action that reduces uncertainty is useful.
```

## UDAM claim 4: Active inference explains UDAM's entire action-value model

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Active inference is broader and more formal than UDAM's practical synthesis. UDAM uses a simple action-value expression:

```text
V(a) = I(a) + B(a) - C(a)
```

Active inference usually evaluates policies using expected free energy or related objectives. These are not the same expression unless formally related.

Recommended wording:

```text
Active inference is a nearby framework for epistemic action, but UDAM's action-value expression is a simplified practical decomposition, not a restatement of expected free energy.
```

Avoid:

```text
UDAM is active inference.
```

## UDAM claim 5: Epistemic action can be separated from execution mapping

UDAM clarification:

```text
action chosen to gain information != if-then execution plan
```

Literature fit:

```text
requires wording correction
```

Reason:

Active inference helps explain why an action may be chosen for information. Implementation intentions help explain how a chosen action can be executed reliably when a cue appears.

These are different layers.

Recommended wording:

```text
Active inference supports epistemic action selection; implementation intentions support cue-action execution. UDAM should keep these layers separate.
```

Avoid:

```text
If an action is epistemic, it is already executable.
```

## UDAM claim 6: Active inference proves UDAM

UDAM statement:

```text
not claimed
```

Literature fit:

```text
not supported
```

Reason:

Active inference supports a broad theory of perception-action cycles and epistemic value. It does not provide UDAM's timer seed model:

```text
tau = K + U + R
```

It also does not directly prove:

```text
anchor loss does not imply future anchor invalidation
```

Correct positioning:

```text
Active inference supports UDAM's epistemic-action layer, while the anchor-loss synthesis remains UDAM-specific.
```

Avoid:

```text
UDAM is proven by active inference.
```

## Verification table

| UDAM claim | Active-inference support level | Reason | Correction |
|---|---:|---|---|
| action can be chosen partly to gain information | direct support | active inference includes epistemic value / information gain in policy selection | keep |
| `I(a)` as informational contribution | partial support | aligned with epistemic value, but not identical to expected free energy | avoid formal identity |
| small probes can sample informative outcomes | partial support | active inference supports sampling informative outcomes; UDAM's anchor-loss setting is specific | keep as applied analogy |
| information-seeking must be balanced with practical value | direct / partial | active inference includes epistemic and pragmatic components; UDAM uses its own value checks | keep but distinguish formulas |
| any uncertainty reduction is useful | not supported | epistemic value alone does not guarantee UDAM favorability | reject |
| active inference equals UDAM | not supported | active inference is broader; UDAM is practical timer-derived synthesis | reject |
| timer-derived anchor-loss structure | analogy only | active inference does not contain `tau = K + U + R` | keep UDAM-specific |
| literature proves UDAM as a whole | not supported | only epistemic-action layer is supported | reject |

## Recommended repository wording

Use:

```text
Active inference supports UDAM's epistemic-action layer: actions can be selected partly because they are expected to reveal information that improves later belief or action.
```

Use:

```text
UDAM's I(a) is aligned with epistemic value but should not be described as expected free energy unless a formal mapping is supplied.
```

Use:

```text
Information-seeking action still needs UDAM's checks for state-informativeness, action relevance, cost, and boundary risk.
```

Avoid:

```text
I(a) is expected free energy.
```

Avoid:

```text
Any uncertainty-reducing action is useful.
```

Avoid:

```text
UDAM is active inference.
```

## Impact on current theory

No major correction is required.

Active inference strengthens the existing UDAM wording around:

```text
epistemic action
information-seeking probes
action as both intervention and observation
balancing information and practical value
```

The main cautions are:

```text
I(a) != expected free energy unless formally mapped
epistemic value != automatic favorability
action selection != execution mapping
active inference support != full synthesis proof
```

## Next literature topic

The next check should be:

```text
behavioral activation
```

Reason:

Active inference verifies the epistemic-action layer. Behavioral activation is the next natural area for checking practical small action after collapse, while avoiding clinical overclaiming.
