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
- `docs/25_literature_verification_multi_armed_bandits.md`
- `docs/26_literature_verification_exponential_search.md`
- `docs/27_literature_verification_online_algorithms.md`
- `docs/28_literature_verification_implementation_intentions.md`
- `docs/29_literature_verification_active_inference.md`
- `docs/30_literature_verification_behavioral_activation.md`
- `docs/31_literature_verification_shaping_successive_approximations.md`
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
- regret minimization;
- action-with-feedback models;
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
verified: direct support for action-with-feedback structure
verified: direct support for exploration-exploitation as a value tradeoff
verified: partial support for UDAM's practical post-anchor-loss small-probe framing
```

Correction:

```text
Bandit theory supports probes as actions that produce feedback, but it does not imply that any small action is useful.
```

Additional correction:

```text
Local probe success does not imply global expansion permission or automatic doubling.
```

Recommended wording:

```text
Multi-armed bandit theory supports UDAM's small-probe layer in a limited sense: an action can both produce payoff and reveal information for later action selection.
```

Avoid:

```text
Any small action is useful.
```

Avoid:

```text
UDAM is a bandit algorithm.
```

See:

- `docs/25_literature_verification_multi_armed_bandits.md`

## 6. Active inference and epistemic value

UDAM claim:

```text
action can be selected partly to gain information
```

Nearby literature:

- active inference;
- epistemic value;
- expected free energy;
- information-seeking action;
- Bayesian optimal design under expected free energy.

UDAM expression:

```text
V(a) = I(a) + B(a) - C(a)
```

Interpretation:

```text
a small action can be selected partly because it produces information that improves later belief or action
```

Verification status:

```text
verified: direct support for epistemic action and information-seeking policy selection
verified: partial support for UDAM's practical I(a) term
verified: not support for treating I(a) as expected free energy without formal mapping
```

Correction:

```text
I(a) != expected free energy unless formally mapped
```

Additional correction:

```text
epistemic value != automatic favorability
```

Recommended wording:

```text
Active inference supports UDAM's epistemic-action layer: actions can be selected partly because they are expected to reveal information that improves later belief or action.
```

Avoid:

```text
I(a) is expected free energy.
```

Avoid:

```text
UDAM is active inference.
```

See:

- `docs/29_literature_verification_active_inference.md`

## 7. Implementation intentions

UDAM claim:

```text
mapping situations to specific next actions makes the protocol usable
```

Nearby literature:

- implementation intentions;
- if-then planning;
- action planning;
- goal pursuit;
- planning prompts.

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
verified: direct support for if-result-then-action execution mapping
verified: direct support for concrete cue and feasible response requirements
verified: not support for observation validity or positive action value
```

Correction:

```text
execution support != value support
```

Additional correction:

```text
if-then planning does not make an observation valid
```

Recommended wording:

```text
Implementation-intention research directly supports UDAM's if-result-then-action mapping as a practical execution device: a recognized cue should be linked to a concrete feasible response.
```

Avoid:

```text
If-then planning makes the action correct.
```

Avoid:

```text
UDAM is implementation intentions.
```

See:

- `docs/28_literature_verification_implementation_intentions.md`

## 8. Behavioral activation

UDAM claim:

```text
small action after collapse can matter
```

Nearby literature:

- behavioral activation;
- activity scheduling;
- avoidance-loop interruption;
- reinforcement-oriented behavioral accounts of depression;
- action before motivation.

UDAM interpretation:

```text
after anchor loss -> choose a bounded concrete action -> observe response -> update and continue, switch, or stop
```

Verification status:

```text
verified: partial support for structured small action after avoidance-like collapse
verified: direct support in behavioral-activation context for targeting avoidance and withdrawal loops
verified: not support for UDAM as therapy or arbitrary small action
```

Correction:

```text
UDAM is not behavioral activation therapy
```

Additional correction:

```text
avoidance != all inaction
```

Recommended wording:

```text
Behavioral activation partially supports UDAM's practical small-action-after-collapse layer: structured concrete activity can interrupt avoidance-like loops and restore contact with feedback or reinforcement.
```

Avoid:

```text
UDAM treats depression.
```

Avoid:

```text
Any small action is therapeutic.
```

See:

- `docs/30_literature_verification_behavioral_activation.md`

## 9. Shaping and successive approximations

UDAM claim:

```text
small successful observations can justify gradual expansion
```

Nearby literature:

- shaping;
- successive approximations;
- operant conditioning;
- differential reinforcement;
- graded action;
- reward shaping in reinforcement learning.

UDAM expression:

```text
small valid observation -> favorable result -> expand scope
```

Verification status:

```text
verified: partial support for gradual progression through successful intermediate approximations
verified: analogy-only support from reinforcement-learning reward shaping
verified: not support for treating reinforcement as state-informativeness or boundary-risk permission
```

Correction:

```text
reinforcement != state-informativeness
```

Additional correction:

```text
successive approximation != boundary-risk permission
```

Recommended wording:

```text
Shaping and successive approximations partially support UDAM's gradual-expansion intuition: progress can sometimes be built through successful intermediate steps rather than a single global leap.
```

Avoid:

```text
A small success always justifies expansion.
```

Avoid:

```text
UDAM is shaping.
```

See:

- `docs/31_literature_verification_shaping_successive_approximations.md`

## 10. Exponential search and doubling strategies

UDAM claim:

```text
when useful scale is unknown, the agent can expand scope geometrically after successful probes
```

Nearby literature:

- exponential search;
- doubling search;
- geometric search;
- unbounded search over ordered domains;
- linear search problem;
- cow-path problem;
- online search with turn cost.

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
verified: direct support for geometric expansion under unknown scale in ordered or spatial search settings
verified: partial support for UDAM's practical expansion-factor layer
verified: analogy only / not direct support for boundary-risk-constrained expansion
```

Correction:

```text
Doubling is a default example of geometric expansion, not a universal optimum.
```

Additional correction:

```text
unknown scale != unknown state
```

Recommended wording:

```text
Exponential search supports UDAM's use of geometric expansion as a scale-discovery heuristic when the useful scale is unknown and the domain has suitable search structure.
```

Avoid:

```text
Doubling is always optimal.
```

Avoid:

```text
A favorable local probe justifies global expansion.
```

See:

- `docs/26_literature_verification_exponential_search.md`

## 11. Online algorithms and robust decision rules

UDAM claim:

```text
when future duration or boundary location is unknown, the agent needs a robust sequential rule rather than a perfect offline optimum
```

Nearby literature:

- online algorithms;
- competitive analysis;
- ski-rental-type tradeoffs;
- robust sequential decision-making;
- risk-sensitive online algorithms.

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
verified: direct support for unavailable offline optimum and robust-rule framing
verified: direct support for repeated small cost versus one larger commitment in ski-rental-type problems
verified: partial support for UDAM-specific expansion rules unless a formal cost model is defined
```

Correction:

```text
competitive ratio != expected utility
```

Additional correction:

```text
robust != optimal
```

Recommended wording:

```text
Online algorithms support UDAM's robust-rule framing: when future inputs or durations are unknown, the relevant practical question is often how to choose a rule that is not too bad without future knowledge, not how to compute an unavailable offline optimum.
```

Avoid:

```text
UDAM gives the optimal expansion factor.
```

Avoid:

```text
UDAM's expansion inequality is a competitive ratio.
```

See:

- `docs/27_literature_verification_online_algorithms.md`

## 12. What the literature supports

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
action-with-feedback small probes: verified direct / partial support
exploration-exploitation as value tradeoff: verified direct support
geometric expansion under unknown scale: verified direct support in structured search settings
boundary-risk-constrained expansion: analogy only / UDAM-specific
robust-rule framing under unavailable future information: verified direct support
repeated small cost versus one larger commitment: verified direct support in ski-rental-type problems, analogy for UDAM
if-result-then-action execution mapping: verified direct support
concrete cue and feasible response requirements: verified direct support
epistemic action and information-seeking policy selection: verified direct support
I(a) as active-inference expected free energy: not supported without formal mapping
small concrete action after collapse-like avoidance: verified partial support
avoidance-loop interruption: verified direct in behavioral-activation context, partial for UDAM
gradual progression by successive approximations: verified partial support
reinforcement as valid re-anchor: not supported
```

## 13. What remains UDAM-specific

UDAM-specific synthesis:

```text
timer seed model -> anchor loss -> unknown interval -> valid future anchor -> practical re-anchoring after model collapse
```

The distinctive contribution is not a new theorem replacing decision theory.

The distinctive contribution is the practical unification:

```text
when you feel unable to conclude because the anchor is lost, do not globally invalidate the future; take one valid local observation, map the result, and expand only when the response supports expansion and boundary risk allows it
```

## 14. Current research task

The planned Stage 2 first-pass literature verification sequence is now complete enough to move to Stage 3.

Verified first pass:

```text
value of information
Blackwell informativeness
Bayesian experimental design
sequential analysis / stopping rules
multi-armed bandits / exploration-exploitation
exponential search / doubling strategies
online algorithms / robust decision rules
implementation intentions / if-then planning
active inference / epistemic value
behavioral activation
shaping / successive approximations
```

Next stage:

```text
Stage 3: visual explanation
```

Future literature checks can still be added if a specific unsupported claim appears.
