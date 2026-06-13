# Roadmap

## v0.1: Theory skeleton

Goal: Fix the minimal theory structure.

- [x] README
- [x] license notice
- [x] timer model
- [x] variables
- [x] assumptions
- [x] axioms
- [x] propositions
- [x] proofs
- [x] counterexamples

Status: complete as initial skeleton.

## v0.2: Applications

Goal: Add structured application examples.

- [x] learning recovery
- [x] work interruption recovery
- [x] health tracking
- [x] relationship uncertainty
- [x] life strategy after failure
- [x] missed re-anchor miscalculation examples
- [x] happy miscalculation examples
- [x] false comfort miscalculation examples

Status: initial examples added. Further examples can be added later.

## v0.3: Related work

Goal: Map the model to existing fields without overclaiming novelty.

- [x] Bayesian filtering
- [x] Kalman filtering
- [x] POMDP / belief state
- [x] active inference
- [x] value of information
- [x] behavioral activation
- [x] cognitive anchoring
- [x] conditional switching and Monty Hall information structure

Status: initial related-work map added. Needs expansion and citations if developed into a paper.

## v0.4: Diagrams

Goal: Add conceptual diagrams.

- [x] uncertainty diffusion without anchors
- [x] lost interval and re-anchored interval
- [x] timer relative dilution
- [x] action value flow
- [x] failure case taxonomy
- [x] observability value flow

Status: Mermaid source diagrams added under `assets/diagrams/`. Rendered figures can be added later under `assets/figures/`.

## v0.5: Formal refinement

Goal: sharpen the mathematical status of the model.

- [x] separate cognitive uncertainty from physical state change
- [x] distinguish absolute uncertainty from relative uncertainty dilution in the timer model
- [x] formalize the possibility that absolute uncertainty increases while relative influence decreases
- [x] add fixed-target scope for the timer seed model
- [x] add controllability boundary for actionable versus uncontrollable uncertainty
- [x] add notation for observation update after re-anchoring
- [x] formalize diminishing information value for repeated checking
- [x] define conditions under which `Q > 0`
- [x] decide whether `P_t` is variance, covariance, entropy, or a general uncertainty functional

Status: complete as formal refinement layer. Core uses variance/covariance-like `P_t`; general uncertainty functional `𝓤_t` is reserved for future extension.

## v0.6: Public-facing safety and clarity

Goal: keep examples useful while preventing misreadings.

- [x] add high-stakes example policy
- [x] require neutral wording for high-stakes examples
- [x] distinguish theory failure cases from missed-application miscalculations
- [x] add a concise public-facing FAQ
- [ ] render diagrams for easier reading

Status: public-facing clarification is mostly complete. Remaining work is rendered figures.

## v0.7: Observability value model

Goal: formalize the value of observation as conditional-action value.

- [x] add observability value model
- [x] add observability variables to `theory/variables.md`
- [x] add observability propositions
- [x] add observability proof sketches
- [x] add upside uncertainty / happy miscalculation
- [x] add downside uncertainty / false comfort miscalculation
- [x] add fixed-target disbelief inequality
- [x] sync observability model into README
- [x] sync observability model into `docs/10_formal_refinement.md`
- [x] sync observability model into `drafts/paper_outline.md`
- [x] add observability consistency checks
- [x] add an observability diagram

Status: complete as a formal integrated layer. Remaining future work is rendering diagrams and possibly expanding examples.

## v0.8: Valid re-anchor and conditional switching

Goal: prevent the model from being misread as arbitrary small action.

- [x] add valid re-anchor condition
- [x] add conditional action switch structure
- [x] connect the structure to the Monty Hall problem in related work
- [x] sync to `theory/propositions.md`
- [x] sync to `docs/05_propositions.md`
- [x] sync to `theory/consistency_review.md`
- [x] add proof sketches for Propositions 11 and 12
- [x] update README entry point with state-informative wording

Status: complete as a formal clarification layer.

## v0.9: Concrete application playbooks

Goal: turn the theory into clear, usable examples without overcomplicating the protocol.

- [x] add concrete action sections to learning example
- [x] add concrete action sections to work example
- [x] add concrete action sections to relationship example
- [x] add concrete action sections to budget example
- [x] convert life strategy after model collapse into a playbook
- [x] add application caution document for timing and domain limits
- [x] add application writing template
- [x] sync examples index
- [x] add simple practical protocol version

Status: complete as a practical application layer. Further examples can be added using the playbook template.

## v0.10: Adaptive observation cadence

Goal: clarify how to handle the first observation and later observations.

- [x] add adaptive observation cadence document
- [x] distinguish first valid observation from repeated observation
- [x] connect cadence to hidden upside and hidden downside errors
- [x] add domain-dependent cadence patterns
- [x] sync cadence document into application cautions
- [x] sync cadence document into README

Status: complete as a practical caution layer. Future work may formalize cadence selection by domain.

## v0.11: Adaptive expansion factor

Goal: clarify how much to expand action or observation scope after favorable probes.

- [x] add adaptive expansion factor document
- [x] define expansion factor `r_i`
- [x] connect geometric expansion to search energy
- [x] add adverse-boundary-before-next-observation risk
- [x] connect timer seed model to boundary crossing before observation
- [x] add rough decision inequality for expansion

Status: complete as a practical expansion layer. Future work may formalize optimal expansion factors under specific loss functions.

## v0.12: Positioning and novelty

Goal: prevent overclaiming and clarify that UDAM is a practical synthesis, not a replacement for existing decision theory.

- [x] add positioning and novelty document
- [x] add terminology entries for practical synthesis, timer-derived formulation, and overclaim
- [x] update README novelty position
- [x] link positioning note from README

Status: complete as a positioning layer. Future paper drafts should use the safer novelty claim.

## v0.13: Japanese documentation and visual support

Goal: create a minimal Japanese explanation layer inside the same repository.

- [x] add `docs/ja/` Japanese documentation index
- [x] add plain Japanese explanation
- [x] add Japanese timer model note
- [x] add Japanese practical protocol
- [x] add Japanese failure cases
- [x] add Japanese positioning note
- [x] link Japanese docs from README
- [x] add full UDAM flow diagram
- [x] add positioning map diagram
- [x] add literature verification checklist

Status: minimal Japanese layer exists. Further Japanese expansion should wait until the English structure stabilizes.

## v0.14: Logical synthesis review

Goal: check whether the current model layers are logically coherent and whether any contradictions remain.

- [x] review propositions, variables, formal refinement, and consistency notes
- [x] add logical synthesis review
- [x] distinguish valid observation from favorable observation
- [x] clarify `I(a)` versus `OV`
- [x] clarify first observation versus repeated observation
- [x] clarify expansion versus automatic doubling
- [x] clarify local observation versus global conclusion
- [x] link logical synthesis review from theory index

Status: complete as a coherence-check layer. No major internal contradiction found; watch items are documented.

## v0.15: Five-stage refinement roadmap

Goal: move from theory construction to evidence, clarity, and verification.

- [x] add five-stage development roadmap
- [x] define the five stages: failure boundaries, literature verification, visual explanation, project-note consolidation, Japanese explanation sync
- [x] add evidence hierarchy for UDAM claims
- [x] distinguish timer intuition, internal coherence, examples, counterexamples, literature support, and empirical testing
- [x] add failure decision tree for Stage 1
- [x] add failure decision tree diagram
- [x] begin Stage 2 literature verification with value of information and Blackwell informativeness
- [x] continue Stage 2 literature verification with Bayesian experimental design
- [x] continue Stage 2 literature verification with sequential analysis and stopping rules
- [x] continue Stage 2 literature verification with multi-armed bandits and exploration-exploitation
- [x] continue Stage 2 literature verification with exponential search and doubling strategies

Status: active strategic refinement layer. Stage 1 has a compact failure diagnostic tree. Stage 2 now has first-pass verification for value of information, Blackwell informativeness, Bayesian experimental design, sequential analysis / stopping rules, multi-armed bandits / exploration-exploitation, and exponential search / doubling strategies. Japanese expansion is deferred until the English version stabilizes.

## v1.0: Stable theory note

Goal: Publish a coherent theory note with definitions, propositions, proofs, examples, and limitations.

Remaining work:

- refine definitions;
- add rendered figures;
- continue related-work verification with online algorithms and implementation intentions;
- expand Japanese examples only after English stabilization;
- audit notation consistency across timer, action-value, observability, and expansion layers;
- decide whether contraction needs a separate rule from expansion;
- continue the five-stage refinement process.
