# Changelog

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
