# 17 Literature Support Map

This document maps UDAM claims to nearby existing research areas.

It does not claim that UDAM is mathematically original in every component.

The safer claim is:

```text
UDAM combines existing decision-theoretic and cognitive ideas into a timer-derived practical model of re-anchoring after anchor loss.
```

For detailed verification notes, see:

- `docs/22_literature_verification_value_blackwell.md`
- `docs/23_literature_verification_bayesian_experimental_design.md`
- `docs/24_literature_verification_sequential_analysis.md`
- `notes/literature_verification.md`

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

Verification status:

```text
verified: direct support
```

Correction:

```text
state-informative observation is not automatically favorable; observation is favorable when expected decision value exceeds cost
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

Verification status:

```text
verified: partial support
```

Correction:

```text
UDAM's P(y | S) != P(y) is a local belief-update condition, not the full Blackwell order
```

Recommended wording:

```text
UDAM is compatible with Blackwell-style informativeness but should not present its local state-informative condition as Blackwell's theorem.
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
- prior-posterior update;
- adaptive Bayesian design.

UDAM expression:

```text
observe y -> update p(S | y) -> choose a(y)
```

Interpretation:

```text
an observation is selected because its expected result can improve belief, prediction, or downstream action enough to justify the observation
```

Verification status:

```text
verified: direct support for utility-guided observation choice
verified: direct support for prior-posterior updating
verified: partial to direct support for conditional action when utility is decision-relevant
```

Correction:

```text
Bayesian experimental design supports the observation-selection component, not the full timer-derived UDAM synthesis.
```

Recommended wording:

```text
Bayesian experimental design directly supports UDAM's utility-guided observation-selection layer, while UDAM's anchor-loss and re-anchor framing remain UDAM-specific.
```

Avoid:

```text
UDAM is Bayesian experimental design.
```

See:

- `docs/23_literature_verification_bayesian_experimental_design.md`

## 4. Sequential analysis

UDAM claim:

```text
first observation and later observations are different decisions
```

Nearby literature:

- sequential analysis;
- sequential probability ratio testing;
- optimal stopping;
- stopping rules;
- observation cost;
- group sequential methods.

UDAM expression:

```text
MOV_i > 0
```

Interpretation:

```text
continue observing only while the next observation has positive marginal value
```

Verification status:

```text
verified: direct support for repeated observation as a continue-or-stop problem
verified: direct support for the need for stopping rules
verified: partial support for MOV_i as UDAM-specific marginal-value notation
```

Correction:

```text
MOV_i is aligned with optimal-stopping reasoning, but it is not a standard sequential-analysis formula.
```

Additional correction:

```text
MOV_i <= 0 should mean stop or change the current observation mode, not that every possible future observation is worthless.
```

Recommended wording:

```text
Sequential analysis supports UDAM's treatment of repeated observation as a stopping-rule problem: later checks must be justified by expected continuation value, not by the fact that the first observation was useful.
```

Avoid:

```text
MOV_i is Wald's stopping rule.
```

Avoid:

```text
More checking is always safer.
```

See:

- `docs/24_literature_verification_sequential_analysis.md`

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

Verification status:

```text
to verify
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

Verification status:

```text
to verify
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

Verification status:

```text
to verify
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

Verification status:

```text
to verify
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

Verification status:

```text
to verify
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

Verification status:

```text
to verify
```

## 11. What the literature supports

The literature currently supports these parts at different levels:

```text
information can have decision value: verified direct support
more informative signals can improve action choice: verified partial/direct alignment
utility-guided observation choice: verified direct support
prior-observation-posterior updating: verified direct support
conditional action after observation: verified partial to direct support when utility is decision-relevant
repeated observation as a continue-or-stop problem: verified direct support
stopping-rule discipline for checking loops: verified direct support
MOV_i as a specific formula: verified partial support only; UDAM-specific notation
exploration and exploitation must be balanced: to verify
actions can be chosen for epistemic value: to verify
if-then mappings improve action execution: to verify
small steps can support gradual expansion: to verify
geometric expansion can reduce search cost when scale is unknown: to verify
online rules can be useful when offline optimum is unavailable: to verify
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

For future refinement, the next step is to continue formal literature verification one topic at a time.

Verified first pass:

```text
value of information
Blackwell informativeness
Bayesian experimental design
sequential analysis / stopping rules
```

Priority remaining sources:

```text
multi-armed bandits
exponential search
online algorithms
implementation intentions
active inference
successive approximations
behavioral activation
ski-rental-type tradeoffs
```
