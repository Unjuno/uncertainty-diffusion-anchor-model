# Changelog

## 0.7.16 - Behavioral activation literature verification

Continued Stage 2 literature verification with behavioral activation.

Added:

- `docs/30_literature_verification_behavioral_activation.md`

Changed:

- `notes/literature_verification.md` now marks behavioral activation as verified first-pass partial support for structured small action after collapse-like avoidance.
- `docs/17_literature_support_map.md` now records behavioral activation as partial support for small action after collapse, direct support in BA context for targeting avoidance and withdrawal loops, and no support for UDAM as therapy or arbitrary small action.
- ROADMAP now records behavioral activation as part of the active Stage 2 verification sequence.

Core result:

```text
behavioral activation -> partial support for structured small action after collapse-like avoidance
behavioral activation -> direct support in clinical BA context for targeting avoidance and withdrawal loops
behavioral activation -> not support for arbitrary small action or UDAM as therapy
```

Required wording corrections:

```text
UDAM is not behavioral activation therapy
small action != arbitrary action
avoidance != all inaction
behavioral activation != decision-theoretic probe
clinical support does not prove the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover shaping / successive approximations.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.15 - Active inference literature verification

Continued Stage 2 literature verification with active inference and epistemic value.

Added:

- `docs/29_literature_verification_active_inference.md`

Changed:

- `notes/literature_verification.md` now marks active inference / epistemic value as verified first-pass support for epistemic action and information-seeking policy selection.
- `docs/17_literature_support_map.md` now records active inference as direct support for epistemic action, partial support for UDAM's practical `I(a)` term, and no support for treating `I(a)` as expected free energy without a formal mapping.
- ROADMAP now records active inference / epistemic value as part of the active Stage 2 verification sequence.

Core result:

```text
active inference -> direct support for epistemic action and information-seeking policy selection
expected free energy literature -> partial alignment with UDAM's I(a) term
active inference -> not support for treating I(a) as expected free energy without formal mapping
```

Required wording corrections:

```text
I(a) != expected free energy unless formally mapped
epistemic value != automatic favorability
action selection != execution mapping
active inference supports one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover behavioral activation or shaping / successive approximations.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.14 - Implementation intentions literature verification

Continued Stage 2 literature verification with implementation intentions and if-then planning.

Added:

- `docs/28_literature_verification_implementation_intentions.md`

Changed:

- `notes/literature_verification.md` now marks implementation intentions / if-then planning as verified first-pass support for if-result-then-action execution mapping.
- `docs/17_literature_support_map.md` now records implementation intentions as direct support for concrete cue-response mapping and feasible action specification, while rejecting any claim that if-then planning validates the observation or action value.
- ROADMAP now records implementation intentions / if-then planning as part of the active Stage 2 verification sequence.

Core result:

```text
implementation intentions -> direct support for if-result-then-action execution mapping
implementation intentions -> direct support for concrete cue and feasible response requirements
implementation intentions -> not support for observation validity or positive action value
```

Required wording corrections:

```text
execution support != value support
cue-response mapping != state-informativeness
if-then planning does not make an observation valid
if-then planning does not make an action correct
implementation intentions support one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover active inference / epistemic value.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.13 - Online algorithms literature verification

Continued Stage 2 literature verification with online algorithms and robust decision rules.

Added:

- `docs/27_literature_verification_online_algorithms.md`

Changed:

- `notes/literature_verification.md` now marks online algorithms / robust decision rules as verified first-pass support for unavailable offline optimum and robust-rule framing.
- `docs/17_literature_support_map.md` now records online algorithms as direct support for robust-rule framing, direct support for repeated small cost versus one larger commitment in ski-rental-type problems, and partial support for UDAM-specific expansion rules unless a formal cost model is defined.
- ROADMAP now records online algorithms / robust decision rules as part of the active Stage 2 verification sequence.

Core result:

```text
online algorithms -> direct support for decisions without future input
competitive analysis -> direct support for comparing online rules with unavailable offline optimum
ski-rental-type tradeoffs -> direct support for repeated small cost versus one larger commitment under unknown horizon
risk-sensitive online algorithms -> partial support for considering adverse-tail behavior
```

Required wording corrections:

```text
robust != optimal
competitive ratio != expected utility
ski rental is an analogy unless formally modeled
boundary-risk terms remain UDAM-specific
online algorithms support one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover implementation intentions / if-then planning.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.12 - Exponential search literature verification

Continued Stage 2 literature verification with exponential search and doubling strategies.

Added:

- `docs/26_literature_verification_exponential_search.md`

Changed:

- `notes/literature_verification.md` now marks exponential search / doubling strategies as verified first-pass support for geometric expansion under unknown scale in structured search settings.
- `docs/17_literature_support_map.md` now records exponential search as direct support for geometric expansion in ordered or spatial search settings, partial support for UDAM's practical expansion-factor layer, and only analogy-level support for boundary-risk-constrained expansion.
- ROADMAP now records exponential search / doubling strategies as part of the active Stage 2 verification sequence.

Core result:

```text
exponential search -> direct support for geometric expansion under unknown scale in structured search domains
doubling -> partial support as a common default example, not a universal optimum
online search / cow-path literature -> partial support for bounded-overhead search under unknown distance
```

Required wording corrections:

```text
unknown scale != unknown state
doubling is not always optimal
local probe success != global expansion permission
boundary-risk-constrained expansion remains UDAM-specific
exponential search supports one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover online algorithms / robust decision rules.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.11 - Multi-armed bandit literature verification

Continued Stage 2 literature verification with multi-armed bandits and exploration-exploitation.

Added:

- `docs/25_literature_verification_multi_armed_bandits.md`

Changed:

- `notes/literature_verification.md` now marks multi-armed bandits / exploration-exploitation as verified first-pass support for action-with-feedback and exploration-exploitation tradeoff.
- `docs/17_literature_support_map.md` now records bandit theory as direct support for the action-with-feedback structure, direct support for exploration as a costly value tradeoff, and partial support for UDAM's practical small-probe framing.
- ROADMAP now records multi-armed bandits / exploration-exploitation as part of the active Stage 2 verification sequence.

Core result:

```text
multi-armed bandits -> direct support for action-with-feedback
exploration-exploitation -> direct support for learning/action tradeoff
regret analysis -> direct support that exploration is costly, not automatically favorable
```

Required wording corrections:

```text
small != useful
feedback-producing != favorable
local probe success != global expansion permission
UDAM is not a bandit algorithm
bandit theory supports one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover exponential search / doubling strategies.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.10 - Sequential analysis literature verification

Continued Stage 2 literature verification with sequential analysis and stopping rules.

Added:

- `docs/24_literature_verification_sequential_analysis.md`

Changed:

- `notes/literature_verification.md` now marks sequential analysis / stopping rules as verified first-pass support for repeated observation as a continue-or-stop problem.
- `docs/17_literature_support_map.md` now records sequential analysis as direct support for stopping-rule discipline and partial support for UDAM's `MOV_i` notation.
- ROADMAP now records sequential analysis / stopping rules as part of the active Stage 2 verification sequence.

Core result:

```text
sequential analysis -> direct support for repeated observation as a continue-or-stop problem
sequential analysis -> direct support for stopping-rule discipline
optimal stopping -> partial support for MOV_i-style continuation-value reasoning
```

Required wording corrections:

```text
MOV_i is UDAM-specific notation, not a standard sequential-analysis formula
MOV_i <= 0 means stop or change the current observation mode, not that all possible future observations are worthless
more checking is not automatically safer
sequential analysis supports one component, not the whole timer-derived UDAM synthesis
```

Status:

- Stage 2 has verified one more literature area.
- The next literature checks should cover multi-armed bandits / exploration-exploitation and exponential search / doubling strategies.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.9 - Bayesian experimental design literature verification

Continued Stage 2 literature verification with Bayesian experimental design.

Added:

- `docs/23_literature_verification_bayesian_experimental_design.md`

Changed:

- `notes/literature_verification.md` now marks Bayesian experimental design as verified first-pass support for utility-guided observation choice and prior-posterior updating.
- `docs/17_literature_support_map.md` now records Bayesian experimental design as verified direct support for observation selection, direct support for prior-posterior updating, and partial-to-direct support for conditional action when utility is decision-relevant.
- ROADMAP now records Bayesian experimental design as part of the active Stage 2 verification sequence.

Core result:

```text
Bayesian experimental design -> direct support for utility-guided observation choice
Bayesian experimental design -> direct support for prior-observation-posterior updating
Bayesian experimental design -> partial to direct support for conditional action when utility is decision-relevant
```

Required wording corrections:

```text
Bayesian experimental design supports UDAM components, not the whole timer-derived synthesis
state-informative != favorable
valid re-anchor framing remains UDAM-specific
MOV_i still needs sequential-analysis / stopping-rule verification
```

Status:

- Stage 2 has verified one more literature area.
- The next literature check should cover sequential analysis / stopping rules.
- Japanese expansion remains deferred until English structure stabilizes.

## 0.7.8 - Initial literature verification pass

Started Stage 2 literature verification with value of information and Blackwell informativeness.

Added:

- `docs/22_literature_verification_value_blackwell.md`

Changed:

- `notes/literature_verification.md` now marks value of information as verified direct support and Blackwell informativeness as verified partial support.
- `docs/17_literature_support_map.md` now records the verification status and wording corrections.
- ROADMAP now records the start of Stage 2 verification.

Core result:

```text
value of information -> direct support for OV > 0 style observation value
Blackwell informativeness -> partial support for state-informative observation and conditional action, but not identical to UDAM's local condition
```

Required wording corrections:

```text
state-informative != favorable
P(y | S) != P(y) is not the full Blackwell order
component support != proof of the whole UDAM synthesis
```

Status:

- Stage 2 has started.
- Next literature checks should cover Bayesian experimental design and sequential analysis.

## 0.7.7 - English-first refinement order

Corrected the five-stage refinement order so that Japanese documentation is treated as the final synchronization layer, not an immediate next step.

Changed:

- `docs/20_five_stage_development_roadmap.md` now orders the stages as failure boundaries, literature verification, visual explanation, project-note consolidation, and Japanese explanation sync.
- ROADMAP now states that further Japanese expansion should wait until the English structure stabilizes.
- README is now English-first and treats Japanese documentation as a later synchronization layer.

Updated five-stage order:

```text
1. failure boundaries
2. literature verification
3. visual explanation
4. project-note consolidation
5. Japanese explanation sync
```

Status:

- Japanese files remain in the repository.
- New Japanese expansion is deferred until English terminology, structure, and evidence links are more stable.

## 0.7.6 - Failure decision tree

Added a compact diagnostic tree for determining whether UDAM applies, weakens, or fails in a given situation.

Added:

- `docs/21_failure_decision_tree.md`
- `assets/diagrams/failure_decision_tree.mmd`

Changed:

- `docs/06_failure_cases.md` now links to the failure decision tree.
- `assets/diagrams/README.md` now lists the failure decision tree diagram.
- ROADMAP now marks the Stage 1 failure diagnostic tree as complete.

Core diagnostic sequence:

```text
name the state
check target scope
check actionability
check state-informativeness
check conditional action change
check value versus cost
check repeated-observation marginal value
check expansion value and boundary risk
avoid local-to-global overreach
```

Status:

- Stage 1 now has a practical decision tree, not only a list of failure cases.

## 0.7.5 - Five-stage refinement roadmap

Added a strategic roadmap for continuing the project after the core theory stabilized.

Added:

- `docs/20_five_stage_development_roadmap.md`
- `notes/evidence_hierarchy.md`

Changed:

- ROADMAP now includes v0.15: Five-stage refinement roadmap.

The original five-stage outline was:

```text
1. failure boundaries
2. Japanese explanation layer
3. literature verification
4. visual explanation
5. project-note consolidation
```

This order was later corrected in 0.7.7 so that Japanese synchronization comes after English stabilization.

Evidence levels:

```text
Level 1: timer intuition
Level 2: internal logical coherence
Level 3: concrete examples
Level 4: failure cases and counterexamples
Level 5: nearby literature
Level 6: empirical testing or simulation
```

Status:

- The theory is stable enough to refine.
- The next work should focus on support, clarity, verification, and reader confidence.
